from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 1. 路径
model_path = "/home/cyw/Qwen2.5-0.5B"
print("--- 正在加载 Qwen 0.5B ---")

# 2. 加载 (注意这里是 CausalLM，和混元不一样)
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, low_cpu_mem_usage=True)
print("加载成功！！")

# 3. 准备翻译
text = "She set a new personal best, it is unbelievable!"
# 构造提示词
prompt = f"<|im_start|>system\n你是一个专业的体育频道字幕翻译。<|im_end|>\n<|im_start|>user\n请翻译：{text}<|im_end|>\n<|im_start|>assistant\n"

inputs = tokenizer([prompt], return_tensors="pt")

# 4. 推理
print("正在翻译...")
with torch.no_grad():
    generated_ids = model.generate(**inputs, max_new_tokens=128)

# 5. 解码
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, generated_ids)
]
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]


print(f"原文: {text}")
print(f"结果: {response}")