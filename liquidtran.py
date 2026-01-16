"""
Translate `test.txt` to English using local LiquidAI-350M.

Notes:
- Optionally set: export HF_ENDPOINT=https://hf-mirror.com
"""

from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import json

# Model path
MODEL_DIR = Path("/home/cyw/LiquidAI-350M")

# Device and dtype setup
use_cuda = torch.cuda.is_available()
device_map = "auto" if use_cuda else None
dtype = torch.float16 if use_cuda else torch.float32

# Load tokenizer and model
print("正在加载 LiquidAI 模型...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_DIR,
    dtype=dtype,
    device_map=device_map,
)
print("模型加载完成！")

# IO paths (relative to this script directory)
SCRIPT_DIR = Path(__file__).resolve().parent
IN_PATH = input("请输入待翻译的 jsonl 文件的路径: ").strip()
if not IN_PATH:
    IN_PATH = SCRIPT_DIR / "captions_0429_test.jsonl"
else:
    IN_PATH = Path(IN_PATH)

model_tag = input("请输入模型名称简称（默认: liquid）: ").strip() or "liquid"
OUT_PATH = IN_PATH.with_name(f"out_{model_tag}.jsonl")

system_prompt = (
    "You are a professional translator. Translate the user's text to English. "
    "Only output the translation without any explanations or extra commentary."
)

eos_token_id = tokenizer.eos_token_id
pad_token_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else eos_token_id

print("开始翻译...")
# Translate line by line and write output
with IN_PATH.open("r", encoding="utf-8") as in_f, OUT_PATH.open("w", encoding="utf-8") as out_f:
    for line_num, line in enumerate(in_f, start=1):
        if not line.strip():
            out_f.write("\n")
            continue

        try:
            data = json.loads(line)
            text = data.get("input", "")
        except json.JSONDecodeError:
            print(f"警告: 第 {line_num} 行不是有效的 JSON，已跳过。")
            continue

        if not text:
            out_f.write("\n")
            continue

        print(f"正在翻译第 {line_num} 行: {text[:30]}...")

        if hasattr(tokenizer, "apply_chat_template"):
            messages = [
                {
                    "role": "system", 
                    "content": "You are a specialized subtitle translator. Translate the following Japanese TV transcript into natural English. \nConstraint: Do not repeat text. Do not add information not present in the source."
                },
                # Few-Shot 要给一个带有噪音（符号、不完整句子）的例子，教它怎么处理。
                {
                    "role": "user", 
                    "content": "≫結成１６年以上のベテラン漫才師たちが"
                },
                {
                    "role": "assistant", 
                    "content": ">> Veteran manzai comedians formed over 16 years ago"
                },
                # 实际输入
                {
                    "role": "user", 
                    "content": text
                }
            ] 
            inputs = tokenizer.apply_chat_template(
                messages,
                tokenize=True,
                add_generation_prompt=True,
                return_tensors="pt",
            )
        else:
            prompt = (
                "Japanese: おはようございます。\nEnglish: Good morning.\n"
                "Japanese: 思い出のＧＷです。\nEnglish: Memorable Golden Week.\n"
                f"Japanese: {text}\nEnglish:"
            )
            inputs = tokenizer(prompt, return_tensors="pt")

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

        if "input_ids" in inputs:
            gen_tokens = gen[0][inputs["input_ids"].shape[-1] :]
        else:
            gen_tokens = gen[0]

        translated = tokenizer.decode(gen_tokens, skip_special_tokens=True).strip()
        print(f"✓ 完成: {text[:20]}... -> {translated[:20]}...")

        record = {"input": text, "output": translated}
        out_f.write(json.dumps(record, ensure_ascii=False) + "\n")
        out_f.flush()

print("\n全部翻译任务已完成！")
