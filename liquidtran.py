"""
Translate `test.txt` to English using local LiquidAI-350M.

Notes:
- Optionally set: export HF_ENDPOINT=https://hf-mirror.com
"""

from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Model path
MODEL_DIR = Path("/home/cyw/LiquidAI-350M")

# Device and dtype setup
use_cuda = torch.cuda.is_available()
device_map = "auto" if use_cuda else None
dtype = torch.float16 if use_cuda else torch.float32

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_DIR,
    dtype=dtype,
    device_map=device_map,
)

# IO paths (relative to this script directory)
SCRIPT_DIR = Path(__file__).resolve().parent
IN_PATH = input("请输入输入文件路径（默认: test.txt）: ").strip()
if not IN_PATH:
    IN_PATH = SCRIPT_DIR / "test.txt"
else:
    IN_PATH = Path(IN_PATH)
    
OUT_PATH = input("请输入输出文件路径（默认: outlq.txt）: ").strip()
if not OUT_PATH:
    OUT_PATH = SCRIPT_DIR / "outlq.txt"
else:
    OUT_PATH = Path(OUT_PATH)

system_prompt = (
    "You are a professional translator. Translate the user's text to English. "
    "Only output the translation without any explanations or extra commentary."
)

eos_token_id = tokenizer.eos_token_id
pad_token_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else eos_token_id

# Read input
lines = IN_PATH.read_text(encoding="utf-8").splitlines()

# Translate line by line and write output
with OUT_PATH.open("w", encoding="utf-8") as out_f:
    for line_num, line in enumerate(lines, start=1):
        text = line.strip()

        if not text:
            out_f.write("\n")
            continue

        print(f"正在翻译第 {line_num} 行: {text[:30]}...")

        # Build inputs using chat template if available; fallback to plain prompt
        if hasattr(tokenizer, "apply_chat_template"):
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ]
            inputs = tokenizer.apply_chat_template(
                messages,
                tokenize=True,
                add_generation_prompt=True,
                return_tensors="pt",
            )
        else:
            prompt = (
                "Translate the following text to English. Only output the translation.\n\n"
                + text
            )
            inputs = tokenizer(prompt, return_tensors="pt")

        # Normalize inputs to a mapping (BatchEncoding)
        if isinstance(inputs, torch.Tensor):
            inputs = {"input_ids": inputs}

        if use_cuda:
            inputs = {k: v.to("cuda") for k, v in inputs.items()}

        gen = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=False,
            eos_token_id=eos_token_id,
            pad_token_id=pad_token_id,
        )

        # Decode only the generated tokens (exclude prompt)
        if "input_ids" in inputs:
            gen_tokens = gen[0][inputs["input_ids"].shape[-1] :]
        else:
            gen_tokens = gen[0]

        translated = tokenizer.decode(gen_tokens, skip_special_tokens=True).strip()
        print(f"翻译完成: {translated[:20]}...")
        out_f.write(translated + "\n")
