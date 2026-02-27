import torch
import json
import os
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm  # 进度条库，如果没有请 pip install tqdm

# ================= 生产环境配置 =================
# 1. 模型路径 (使用官方 Instruct 版)
MODEL_PATH = "Qwen/Qwen2.5-0.5B-Instruct"

# 2. 术语表路径 (确保路径正确)
GLOSSARY_FILE = "/home/cyw/pro/train_data_2/glossary.txt"

# 3. 输入文件 (你的原始字幕 JSONL)
INPUT_FILE = "/home/cyw/pro/train_data_2/outs/out_qwen2.jsonl"

# 4. 输出文件 (最终结果)
OUTPUT_FILE = "/home/cyw/pro/train_data_2/outs/out_tv_production.jsonl"
# ===============================================

def load_glossary(filepath):
    """加载并解析术语表"""
    glossary = []
    if not os.path.exists(filepath):
        print(f"⚠️ 警告：找不到术语表 {filepath}，将进行裸翻模式。")
        return []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if "->" in line:
                parts = line.strip().split("->")
                if len(parts) >= 2:
                    # 格式清洗：去除多余空格，去除括号备注
                    src = parts[0].strip()
                    tgt = parts[1].split("(")[0].strip()
                    glossary.append({"src": src, "tgt": tgt})
    return glossary

def main():
    print(f"🚀 初始化模型: {MODEL_PATH} ...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map="auto", torch_dtype="auto")
    
    # 加载术语表
    glossary_list = load_glossary(GLOSSARY_FILE)
    print(f"📚 已加载术语: {len(glossary_list)} 条")

    # 读取所有行
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"🎬 开始翻译 {len(lines)} 行字幕...")
    
    # 打开输出文件
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as fout:
        
        # 使用 tqdm 显示进度条
        for line in tqdm(lines, desc="Translating"):
            data = json.loads(line)
            content = data.get('content', '')
            
            # 如果内容为空，跳过翻译但保留空行
            if not content.strip():
                fout.write(json.dumps(data, ensure_ascii=False) + "\n")
                continue

            # --- 步骤 1: 严格匹配术语 (Strict Matching) ---
            matched_terms = []
            for item in glossary_list:
                if item['src'] in content:
                    matched_terms.append(item)
            
            # --- 步骤 2: 构造 Prompt (System + One-Shot) ---
            
            # A. 构造参考信息 (RAG)
            rag_str = ""
            if matched_terms:
                rag_str = f"Reference Terms: {json.dumps(matched_terms, ensure_ascii=False)}\n"
            
            # B. System Prompt (立规矩)
            sys_msg = (
                "You are a professional subtitle translator. Translate Japanese to English.\n"
                "RULES:\n"
                "1. Use the Reference Terms strictly.\n"
                "2. NO Romaji (Do not output Japanese pronunciation).\n"
                "3. Concise and natural subtitles."
            )

            # C. User Input (实际任务)
            user_msg = f"{rag_str}Source: {content}"

            # D. 组合 Messages (包含教学案例 One-Shot)
            messages = [
                {"role": "system", "content": sys_msg},
                # One-Shot 教学：教它如何处理 Reference 和输出格式
                {"role": "user", "content": 'Reference Terms: [{"src": "天然水", "tgt": "Natural Water"}]\nSource: 天然水を飲みます。'},
                {"role": "assistant", "content": "I drink Natural Water."},
                # 真实任务
                {"role": "user", "content": user_msg}
            ]
            
            # --- 步骤 3: 格式化与生成 ---
            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
            
            inputs = tokenizer([text], return_tensors="pt").to(model.device)
            
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=80,       # 字幕通常很短
                    do_sample=False,         # 贪婪搜索 (最稳)
                    temperature=0.1,         # 兜底
                    repetition_penalty=1.1,  # 防止复读
                    eos_token_id=tokenizer.eos_token_id,
                    pad_token_id=tokenizer.pad_token_id
                )
            
            # 解码
            trans = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
            
            # 后处理：清理可能残留的 Translation: 前缀
            clean_trans = trans.strip().replace("Translation:", "").replace("English:", "")

            # --- 步骤 4: 保存结果 ---
            # 我们把结果存入一个新的字段 'final_en'
            data['final_en'] = clean_trans
            
            # 同时保留命中的术语，方便人工检查
            if matched_terms:
                data['debug_terms'] = str([t['tgt'] for t in matched_terms])
            
            fout.write(json.dumps(data, ensure_ascii=False) + "\n")

    print(f"\n✅ 翻译完成！结果已保存至: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()