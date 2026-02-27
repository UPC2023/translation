import argparse
import logging
from pathlib import Path
from typing import List

import numpy as np
import torch
from datasets import load_dataset
from sentence_transformers import SentenceTransformer, util
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import evaluate


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def load_test_subset(start: int, end: int):
    dataset = load_dataset("nntsuzu/JParaCrawl")
    train_split = dataset["train"]
    if end <= start:
        raise ValueError("end must be greater than start")
    return train_split.select(range(start, end))


def translate_japanese_to_english(
    prompt: str,
    model: AutoModelForCausalLM,
    tokenizer: AutoTokenizer,
    device: torch.device,
    max_new_tokens: int,
):
    system_message = {"role": "system", "content": "You are a professional translator from Japanese to English."}
    user_message = {"role": "user", "content": f"Source: {prompt}"}
    messages = [system_message, user_message]

    prompt_ids = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
    )

    input_tensor = torch.tensor([prompt_ids], device=device)
    with torch.inference_mode():
        generated = model.generate(
            input_tensor,
            max_new_tokens=max_new_tokens,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.pad_token_id,
            do_sample=False,
            use_cache=True,
        )

    generated_text = tokenizer.decode(generated[0, len(prompt_ids):], skip_special_tokens=True)
    return generated_text.strip()


def evaluate_translations(predictions: List[str], references: List[str]):
    logger.info("Computing BLEU score...")
    bleu_metric = evaluate.load("sacrebleu")
    bleu_result = bleu_metric.compute(
        predictions=predictions,
        references=[[ref] for ref in references],
    )

    logger.info("Computing LaBSE similarity...")
    labse_model = SentenceTransformer("sentence-transformers/LaBSE")
    embedding_preds = labse_model.encode(predictions, convert_to_tensor=True)
    embedding_refs = labse_model.encode(references, convert_to_tensor=True)
    cos_scores = util.cos_sim(embedding_preds, embedding_refs)
    labse_similarity = float(np.mean(np.diag(cos_scores.cpu().numpy())))

    return bleu_result["score"], labse_similarity


def main():
    parser = argparse.ArgumentParser(description="Evaluate Qwen translations with BLEU and LaBSE")
    parser.add_argument("--model", default="/home/cyw/Qwen2.5-0.5B", help="base Qwen model path")
    parser.add_argument("--adapter", default=None, help="optional LoRA adapter path (Trainer.save_model output)")
    parser.add_argument("--start", type=int, default=200, help="start index of subset")
    parser.add_argument("--end", type=int, default=220, help="end index (exclusive)")
    parser.add_argument("--max-new-tokens", type=int, default=256, help="generation length")
    parser.add_argument("--device", default=None, help="torch device (cpu/cuda). auto if not set")
    args = parser.parse_args()

    device = torch.device(args.device if args.device else ("cuda" if torch.cuda.is_available() else "cpu"))
    logger.info("Loading model %s on %s", args.model, device)
    tokenizer = AutoTokenizer.from_pretrained(args.model, use_fast=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(args.model)
    if args.adapter:
        adapter_path = Path(args.adapter)
        adapter_config = adapter_path / "adapter_config.json"
        if adapter_config.exists():
            logger.info("Loading LoRA adapter from %s", adapter_path)
            model = PeftModel.from_pretrained(model, adapter_path)
        else:
            logger.warning("Adapter path '%s' not found or missing adapter_config.json; using base model only", adapter_path)
    model.to(device)
    model.eval()

    test_subset = load_test_subset(args.start, args.end)
    predictions = []
    references = []

    logger.info("Translating %d examples", len(test_subset))
    for entry in test_subset:
        # JParaCrawl样例字段: {"translation": {"ja": ..., "en": ...}}
        translation = entry.get("translation", {})
        source = translation.get("ja", "")
        ref = translation.get("en", "").strip()
        if not source or not ref:
            logger.warning("Skip empty example: source or reference missing")
            continue
        prediction = translate_japanese_to_english(
            source, model, tokenizer, device, args.max_new_tokens
        )
        predictions.append(prediction)
        references.append(ref)
        logger.info("Source: %s", source[:60])
        logger.info("Prediction: %s", prediction)
        logger.info("Reference: %s", ref)

    bleu_score, labse_score = evaluate_translations(predictions, references)
    logger.info("BLEU: %.2f", bleu_score)
    logger.info("LaBSE similarity: %.4f", labse_score)
    print("BLEU", bleu_score)
    print("LaBSE", labse_score)


if __name__ == "__main__":
    main()
