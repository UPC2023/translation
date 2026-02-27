"""
2026/1/16 chenyawen
Translate `test.txt` to English using local LiquidAI-350M.
Fixed by Official Docs Recommendation.
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

# IO paths
SCRIPT_DIR = Path(__file__).resolve().parent
IN_PATH = input("请输入待翻译的 jsonl 文件的路径: ").strip()
if not IN_PATH:
    IN_PATH = SCRIPT_DIR / "captions_0429_test.jsonl"
else:
    IN_PATH = Path(IN_PATH)

model_tag = input("请输入模型名称简称（默认: liquid）: ").strip() or "liquid"
OUT_PATH = IN_PATH.with_name(f"out_{model_tag}.jsonl")

# --- 【修改点 1：严格遵守官方 System Prompt】 ---
# 官方文档强调：日英翻译必须严格使用 "Translate to English." (含句号)
# 不要加 "You are a...", 不要加 "no explanation"，否则模型会崩。
system_prompt = "Translate to English."

eos_token_id = tokenizer.eos_token_id
pad_token_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else eos_token_id

print("开始翻译...")

with IN_PATH.open("r", encoding="utf-8") as in_f, OUT_PATH.open("w", encoding="utf-8") as out_f:
    for line_num, line in enumerate(in_f, start=1):
        if not line.strip():
            continue

        try:
            data = json.loads(line)
            # --- 【修改点：提取所有需要的信息】 ---
            part = data.get("part", "unknown") # 如果没有 part，提供一个默认值
            channel = data.get("channel", "unknown") # 如果没有 channel，提供一个默认值
            jp_text = data.get("content", "")
        except json.JSONDecodeError:
            print(f"警告: 第 {line_num} 行 JSON 解析失败，已跳过。")
            continue

        if not jp_text:
            print(f"警告: 第 {line_num} 行 'content' 为空，已跳过。")
            continue

        print(f"正在翻译第 {line_num} 行: {jp_text[:30]}...")

        # --- 【修改点：构造与训练时完全一致的 user_content】 ---
        context_info = f"[Context: This is a '{part}' from the '{channel}' channel.]"
        user_content = f"{context_info}\n{jp_text}"

        # 构造对话模版
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}, # 使用新构造的 user_content
        ]
        
        inputs = tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt",
        )

        if isinstance(inputs, torch.Tensor):
            inputs = {"input_ids": inputs}

        if use_cuda:
            inputs = {k: v.to("cuda") for k, v in inputs.items()}

        # --- 【修改点 2：调整生成参数为官方推荐值】 ---
        # 官方文档推荐: temp=0.5, top_p=1.0, min_p=0.1, rep_penalty=1.05
        gen = model.generate(
            **inputs,
            max_new_tokens=512,  # 稍微调大一点，防截断
            do_sample=True,      # 开启采样
            temperature=0.5,     # 官方推荐值
            top_p=1.0,               # 官方推荐值
            repetition_penalty=1.05, # 官方推荐值
            eos_token_id=eos_token_id,
            pad_token_id=pad_token_id,
        )

        if "input_ids" in inputs:
            output_tokens = gen[0, inputs["input_ids"].shape[1]:]
        else:
            output_tokens = gen[0]
            
        decoded_output = tokenizer.decode(output_tokens, skip_special_tokens=True)

        # 保存结果
        data["output"] = decoded_output.strip()
        out_f.write(json.dumps(data, ensure_ascii=False) + "\n")

print("\n全部翻译任务已完成！")