
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 1. 加载模型（这部分只运行一次）
print("正在加载 Qwen 模型...")
path = "./Qwen2.5-0.5B"
tokenizer = AutoTokenizer.from_pretrained(path)
model = AutoModelForCausalLM.from_pretrained(path, device_map="auto")
print("模型加载完成！")
# 2. 打开输入输出文件
f_in = open("test.txt", "r", encoding="utf-8")
f_out = open("outqw.txt", "w", encoding="utf-8")

print("开始翻译...")
    
# 3. 逐行读取输入文件并进行翻译
for line_num, text in enumerate(f_in, 1):
    # 去除换行符和空白字符
    text = text.strip()
    
    # 跳过空行
    if not text:
        f_out.write("\n")
        continue
    
    print(f"正在翻译第 {line_num} 行: {text[:30]}...")
    
    # --- 翻译核心开始 ---
    # 构造 Prompt
    prompt = f"<|im_start|>system\nYou are a professional translator. Translate Japanese to English. Output only the English.<|im_end|>\n<|im_start|>user\n{text}<|im_end|>\n<|im_start|>assistant\n"
    
    # 编码输入
    inputs = tokenizer([prompt], return_tensors="pt").to(model.device)
    
    # 生成结果
    with torch.no_grad():
        generated_ids = model.generate(**inputs, max_new_tokens=256, do_sample=False)
    
    # 截取生成的回复部分（跳过 prompt 部分）
    result_ids = generated_ids[0][inputs.input_ids.shape[1]:]
    translation = tokenizer.decode(result_ids, skip_special_tokens=True).strip()
    # --- 翻译核心结束 ---

    # 写入文件
    f_out.write(translation + "\n")
    
    # flush 确保数据立即写入文件
    f_out.flush() 
    
    print(f"✓ 完成: {text[:20]}... -> {translation[:20]}...")

# 4. 记得关掉文件
f_in.close()
f_out.close()

print("\n全部翻译任务已完成！结果已存入 out.txt")