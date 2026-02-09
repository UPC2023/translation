import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from pathlib import Path
import json

# 1. 加载模型（这部分只运行一次）
print("正在加载 Qwen 模型...")
path = "/home/cyw/Qwen2.5-0.5B"
tokenizer = AutoTokenizer.from_pretrained(path)
model = AutoModelForCausalLM.from_pretrained(path, device_map="auto")
print("模型加载完成！")

# 2. 批量读取输入文件
input_dir = Path("/home/cyw/pro/train_data_2")
output_file = Path("/home/cyw/pro/train_data_2/outs/out_qwen3.jsonl")
output_file.parent.mkdir(parents=True, exist_ok=True)

# 用户输入要处理的 test 文件范围（例如: 1,5 表示 test1.jsonl 到 test5.jsonl）
user_input = input("请输入要处理的 test 文件范围（例如 1,5 表示 test1.jsonl 到 test5.jsonl）：").strip()

try:
    start, end = map(int, user_input.split(','))
    if start > end or start < 1:
        raise ValueError
except ValueError:
    print("输入格式错误，请输入两个正整数，用逗号分隔，例如 1,5。")
    exit(1)

# 读取指定范围的 jsonl 文件并合并
all_data = []
for i in range(start, end + 1):
    file_path = input_dir / f"test{i}.jsonl"
    if not file_path.exists():
        print(f"警告: 文件 {file_path.name} 不存在，已跳过。")
        continue
    print(f"正在读取文件: {file_path.name}")
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    data = json.loads(line)
                    all_data.append(data)
                except json.JSONDecodeError:
                    print(f"警告: 文件 {file_path.name} 中有无效的 JSON 行，已跳过。")

print(f"共读取 {len(all_data)} 条数据")
print("开始翻译...")

# 3. 处理每条数据
for idx, data in enumerate(all_data, 1):
    content = data.get("content", "")
    context = data.get("context", "")

    if not content:
        continue

    print(f"正在翻译第 {idx}/{len(all_data)} 行: {content[:30]}...")

    messages = [
        {"role": "system", "content": (
            "You are an expert translator for TV subtitles. "
            "Translate the Japanese 'content' into fluent, natural English. "
            "Use the 'context' for better understanding the situation. "
            "Output only the English translation of the 'content'."
        )},
        {"role": "user", "content": f"Context: \"{context}\"\n\nContent to translate: \"{content}\""}
    ]

    prompt_text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    model_inputs = tokenizer([prompt_text], return_tensors="pt").to(model.device)

    with torch.no_grad():
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=256,
            do_sample=False
        )

    # 只取生成的新内容
    new_token_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs["input_ids"], generated_ids)
    ]
    translation = tokenizer.batch_decode(new_token_ids, skip_special_tokens=True)[0].strip()
    if not translation:
        translation = content

    data["output"] = translation
    print(f"✓ 完成: {content[:20]}... -> {translation[:20]}...")

# 4. 输出到单个 JSONL 文件（支持追加）
mode = "a" if output_file.exists() else "w"
with open(output_file, mode, encoding="utf-8") as f:
    for data in all_data:
        f.write(json.dumps(data, ensure_ascii=False) + '\n')

print(f"\n全部翻译任务已完成！结果已保存到: {output_file}")