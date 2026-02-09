import json
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

BASE_MODEL_PATH = Path("/home/cyw/Qwen2.5-0.5B")
ADAPTER_PATH = Path("/home/cyw/pro/lora-finetuning-cpu/lora-tuned-model/checkpoint-15")
INPUT_FILE = Path("/home/cyw/pro/train_data_2/test1.jsonl")
OUTPUT_FILE = Path("/home/cyw/pro/train_data_2/outs/out_qwen_lora_2.jsonl")


def load_translator():
    tokenizer = AutoTokenizer.from_pretrained(ADAPTER_PATH)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL_PATH,
        device_map="auto",
        torch_dtype=torch_dtype,
    )
    # 确保基础模型的词表大小与训练 LoRA 时一致
    base_model.resize_token_embeddings(len(tokenizer))
    model = PeftModel.from_pretrained(base_model, ADAPTER_PATH)
    model.eval()
    return tokenizer, model


def read_jsonl(file_path: Path):
    samples = []
    with file_path.open("r", encoding="utf-8") as src:
        for line in src:
            line = line.strip()
            if not line:
                continue
            try:
                samples.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return samples


def build_prompt(tokenizer, content: str, context: str) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert translator for TV subtitles. "
                "Translate the Japanese 'content' into fluent, natural English. "
                "Use the 'context' for better understanding the situation. "
                "Output only the English translation of the 'content'."
            ),
        },
        {
            "role": "user",
            "content": f"Context: \"{context}\"\n\nContent to translate: \"{content}\"",
        },
    ]

    return tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )


def translate_samples(tokenizer, model, samples):
    translated = []
    for idx, sample in enumerate(samples, 1):
        content = sample.get("content", "").strip()
        context = sample.get("context", "").strip()
        if not content:
            continue

        prompt = build_prompt(tokenizer, content, context)
        model_inputs = tokenizer([prompt], return_tensors="pt").to(model.device)

        with torch.no_grad():
            generated_ids = model.generate(
                **model_inputs,
                max_new_tokens=256,
                do_sample=False,
            )

        new_token_ids = [
            output_ids[len(input_ids) :]
            for input_ids, output_ids in zip(model_inputs["input_ids"], generated_ids)
        ]
        translation = tokenizer.batch_decode(new_token_ids, skip_special_tokens=True)[0].strip()
        if not translation:
            translation = content

        sample["output"] = translation
        translated.append(sample)
        print(f"[{idx}/{len(samples)}] {content[:20]} -> {translation[:20]}")

    return translated


def save_jsonl(samples, file_path: Path):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as dst:
        for sample in samples:
            dst.write(json.dumps(sample, ensure_ascii=False) + "\n")


def main():
    print("Loading base model and LoRA adapter...")
    tokenizer, model = load_translator()
    print("Loading input samples...")
    samples = read_jsonl(INPUT_FILE)
    print(f"Loaded {len(samples)} samples. Starting translation...")
    translated = translate_samples(tokenizer, model, samples)
    save_jsonl(translated, OUTPUT_FILE)
    print(f"Translation finished. Results saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
