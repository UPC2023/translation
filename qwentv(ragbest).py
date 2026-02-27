import torch
import json
import os
from transformers import AutoModelForCausalLM, AutoTokenizer

# ================= 配置区 =================
# 必须用官方 Instruct 版，不要用你那个训练坏的 LoRA
#MODEL_PATH = "Qwen/Qwen2.5-0.5B-Instruct" 
MODEL_PATH = "/home/cyw/Qwen2.5-0.5B"
#缓存or本地文件，二选一
# 你的术语表
GLOSSARY_FILE = "/home/cyw/pro/train_data_2/glossary.txt"
# 输入文件 (你的原始字幕)
INPUT_FILE = "/home/cyw/pro/train_data_2/outs/out_qwen2.jsonl"
# 输出文件
OUTPUT_FILE = "/home/cyw/pro/train_data_2/outs/out_tv_final_bak.jsonl"
# =========================================

def load_glossary(filepath):
    glossary = {}
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if "->" in line:
                    parts = line.strip().split("->")
                    if len(parts) >= 2:
                        # 清洗一下，只取核心词
                        k = parts[0].strip()
                        v = parts[1].split("(")[0].strip()
                        glossary[k] = v
    return glossary

def main():
    print("1. Loading Model...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map="auto", torch_dtype="auto")
    
    # 加载术语表
    glossary = load_glossary(GLOSSARY_FILE)
    print(f"2. Loaded Glossary: {len(glossary)} terms.")

    print(f"3. Processing {INPUT_FILE} ...")
    
    with open(INPUT_FILE, 'r', encoding='utf-8') as fin, \
         open(OUTPUT_FILE, 'w', encoding='utf-8') as fout:
        
        lines = fin.readlines()
        total = len(lines)
        
        for i, line in enumerate(lines):
            data = json.loads(line)
            content = data.get('content', '')
            
            if not content: continue

            # --- A. 动态匹配术语 ---
            matched_terms = []
            for k, v in glossary.items():
                if k in content:
                    matched_terms.append({"src": k, "tgt": v})
            
            # --- B. 构造 Prompt (带 One-Shot 教学) ---
            
            # 1. System Prompt: 立规矩
            sys_msg = (
                "You are a subtitle translator. Translate Japanese to English.\n"
                "RULES:\n"
                "1. Use the Reference Terms strictly.\n"
                "2. Do not use 'I' unless the source explicitly says '私/俺'. Use the character name.\n"
                "3. Output ONLY the English translation."
            )
            
            # 2. 伪造一个“教学案例” (One-Shot)
            # 这一步非常重要！教模型如何使用字典
            example_rag = '[{"src": "田中", "tgt": "Tanaka"}]'
            example_user = f"Reference Terms: {example_rag}\n\nText:\n田中は走った。"
            example_assist = "Tanaka ran." 

            # 3. 真实的用户输入
            rag_str = ""
            if matched_terms:
                rag_str = f"Reference Terms: {json.dumps(matched_terms, ensure_ascii=False)}\n\n"
            
            user_msg = f"{rag_str}Text:\n{content}"

            # 4. 组合 Messages
            messages = [
                {"role": "system", "content": sys_msg},
                # 插入教学案例
                {"role": "user", "content": example_user},
                {"role": "assistant", "content": example_assist},
                # 真实任务
                {"role": "user", "content": user_msg}
            ]
            
            # --- C. 生成 ---
            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
            
            inputs = tokenizer([text], return_tensors="pt").to(model.device)
            
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=80,  # 字幕通常不长
                    temperature=0.1,    # 低温
                    repetition_penalty=1.1,
                    do_sample=False     # 贪婪搜索最稳定
                )
            
            trans = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
            
            # 保存结果
            data['tv_translation'] = trans.strip()
            fout.write(json.dumps(data, ensure_ascii=False) + "\n")
            
            # 打印预览
            if i % 5 == 0:
                print(f"原文: {content}")
                if matched_terms: print(f"术语: {matched_terms}")
                print(f"译文: {trans}")
                print("-" * 20)

    print(f"Done! Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()