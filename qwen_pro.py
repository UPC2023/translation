import torch
import json
import os
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm

# ================= 最终生产配置 =================
MODEL_PATH = "Qwen/Qwen2.5-0.5B-Instruct"
GLOSSARY_FILE = "/home/cyw/pro/train_data_2/glossary.txt"
INPUT_FILE = "/home/cyw/pro/train_data_2/outs/out_qwen2.jsonl"
OUTPUT_FILE = "/home/cyw/pro/train_data_2/outs/out_tv_pro_final.jsonl"
# ===============================================

def load_glossary(filepath):
    glossary = []
    if not os.path.exists(filepath):
        print(f"⚠️ 警告：找不到术语表 {filepath}")
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if "->" in line:
                parts = line.strip().split("->")
                if len(parts) >= 2:
                    src = parts[0].strip()
                    tgt = parts[1].split("(")[0].strip()
                    glossary.append({"src": src, "tgt": tgt})
    return glossary

def main():
    print(f"🚀 初始化模型: {MODEL_PATH} ...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map="auto", torch_dtype="auto")
    
    glossary_list = load_glossary(GLOSSARY_FILE)
    print(f"📚 已加载术语: {len(glossary_list)} 条")

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"🎬 开始翻译 {len(lines)} 行字幕...")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as fout:
        for line in tqdm(lines, desc="Translating"):
            data = json.loads(line)
            content = data.get('content', '')
            
            if not content.strip():
                fout.write(json.dumps(data, ensure_ascii=False) + "\n")
                continue

            # --- 1. RAG 严格匹配 ---
            matched_terms = []
            for item in glossary_list:
                if item['src'] in content:
                    matched_terms.append(item)
            
            rag_str = ""
            if matched_terms:
                rag_str = f"Reference Terms: {json.dumps(matched_terms, ensure_ascii=False)}\n"
            
            # --- 2. System Prompt (v1 的逻辑 + v3 的规则) ---
            sys_msg = (
                "You are a professional subtitle translator. Translate Japanese to English.\n"
                "RULES:\n"
                "1. Use the Reference Terms strictly.\n"
                "2. Do not use 'I' unless the source explicitly says '私/俺'. Use the character name.\n"
                "3. OUTPUT ONLY ENGLISH. No Romaji, no Japanese, no Chinese.\n"
                "4. Keep it concise and natural."
            )

            # --- 3. One-Shot (回归 v1 的'田中'案例，但加强了防罗马音) ---
            # 这个示例非常关键，它告诉模型：即使原文是人名，也要翻译，不要写拼音
            example_user = 'Reference Terms: [{"src": "田中", "tgt": "Tanaka"}]\nSource: 田中は走った。'
            example_assist = "Tanaka ran."

            # --- 4. 组合 Messages ---
            user_msg = f"{rag_str}Source: {content}"
            
            messages = [
                {"role": "system", "content": sys_msg},
                {"role": "user", "content": example_user},
                {"role": "assistant", "content": example_assist},
                {"role": "user", "content": user_msg}
            ]
            
            # --- 5. 生成 ---
            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
            
            inputs = tokenizer([text], return_tensors="pt").to(model.device)
            
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=80,       # v1 的长度
                    do_sample=False,         # 贪婪搜索最稳
                    temperature=0.1,         # 低温
                    repetition_penalty=1.1,
                    eos_token_id=tokenizer.eos_token_id
                )
            
            trans = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
            clean_trans = trans.strip().replace("Translation:", "")

            # 写入结果
            data['tv_final_translation'] = clean_trans
            fout.write(json.dumps(data, ensure_ascii=False) + "\n")

    print(f"\n✅ 翻译完成！")

if __name__ == "__main__":
    main()  