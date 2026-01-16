"""Translate a jsonl file with the local fugumt-ja-en model.

Input: jsonl lines with an "input" field containing Japanese text.
Output: /home/cyw/pro/train_data/<model_tag>_out.jsonl with English translations.
"""

from pathlib import Path
import json
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Model and output locations
model_dir_raw = input("请输入模型路径（默认: /home/cyw/ fugumt-ja-en ）: ").strip()
if not model_dir_raw:
    model_dir_raw = "/home/cyw/ fugumt-ja-en "  # directory name includes leading/trailing spaces
MODEL_DIR = Path(model_dir_raw)
OUTPUT_DIR = Path("/home/cyw/pro/train_data")

print("正在加载模型...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR, device_map="auto")
print("模型加载完成！")

script_dir = Path(__file__).resolve().parent
inpath_raw = input("请输入待翻译的 jsonl 文件的路径: ").strip()
if not inpath_raw:
    inpath = script_dir / "captions_0429_test.jsonl"
else:
    inpath = Path(inpath_raw)

model_tag = input("请输入模型名称简称（默认: fugu）: ").strip() or "fugu"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
outpath = OUTPUT_DIR / f"{model_tag}_out.jsonl"

print(f"输出文件将保存到: {outpath}")
print("开始翻译...")

with inpath.open("r", encoding="utf-8") as f_in, outpath.open("w", encoding="utf-8") as f_out:
    for line_num, line in enumerate(f_in, start=1):
        if not line.strip():
            f_out.write("\n")
            continue

        try:
            data = json.loads(line)
            text = data.get("input", "")
        except json.JSONDecodeError:
            print(f"警告: 第 {line_num} 行不是有效的 JSON，已跳过。")
            continue

        if not text:
            f_out.write("\n")
            continue

        print(f"正在翻译第 {line_num} 行: {text[:30]}...")

        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=512,
        ).to(model.device)

        with torch.no_grad():
            generated = model.generate(
                **inputs,
                max_new_tokens=256,
                num_beams=4,
                early_stopping=True,
            )

        translation = tokenizer.decode(generated[0], skip_special_tokens=True).strip()

        print(f"✓ 完成: {text[:20]}... -> {translation[:20]}...")

        record = {"input": text, "output": translation}
        f_out.write(json.dumps(record, ensure_ascii=False) + "\n")
        f_out.flush()

print("\n全部翻译任务已完成！")
