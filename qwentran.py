
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
# 2. 打开输入输出文件
inpath = input("请输入待翻译的 jsonl 文件的路径: ").strip()
if not inpath:
    inpath = Path("captions_0429_test.jsonl")
else:
    inpath = Path(inpath)

model_tag = input("请输入模型名称简称（默认: qwen）: ").strip() or "qwen"
outpath = inpath.with_name(f"out_{model_tag}.jsonl")
f_in = open(inpath, "r", encoding="utf-8")
f_out = open(outpath, "w", encoding="utf-8")

print("开始翻译...")
    
# 3. 逐行读取输入文件并进行翻译
for line_num, line in enumerate(f_in, 1):
    # 跳过空行
    if not line.strip():
        f_out.write("\n")
        continue

    # 解析 JSONL
    try:
        data = json.loads(line)
        text = data.get("input", "")
    except json.JSONDecodeError:
        print(f"警告: 第 {line_num} 行不是有效的 JSON，已跳过。")
        continue
    
    # 跳过没有 input 的行
    if not text:
        f_out.write("\n")
        continue
    
    print(f"正在翻译第 {line_num} 行: {text[:30]}...")
    
    # --- 翻译核心开始 ---
    # 构造 Prompt
    prompt = f"<|im_start|>system\nYou are an expert Japanese-to-English translator. Translate Japanese to English. Output only the English.<|im_end|>\n<|im_start|>user\n{text}<|im_end|>\n<|im_start|>assistant\n"
    
    # 编码输入
    inputs = tokenizer([prompt], return_tensors="pt").to(model.device)
    
    # 生成结果
    with torch.no_grad():
        generated_ids = model.generate(**inputs, max_new_tokens=256, do_sample=False)
    
    # 截取生成的回复部分（跳过 prompt 部分）
    result_ids = generated_ids[0][inputs.input_ids.shape[1]:]
    translation = tokenizer.decode(result_ids, skip_special_tokens=True).strip()
    # --- 翻译核心结束 ---

    # 写入文件（保持 jsonl 结构）
    record = {"input": text, "output": translation}
    f_out.write(json.dumps(record, ensure_ascii=False) + "\n")
    
    # flush 确保数据立即写入文件
    f_out.flush() 
    
    print(f"✓ 完成: {text[:20]}... -> {translation[:20]}...")

# 4. 记得关掉文件
f_in.close()
f_out.close()

print("\n全部翻译任务已完成！")