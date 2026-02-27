import os
import json
from tqdm import tqdm
import torch
import fugashi

# LangChain & Vector DB importshome\cyw
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Transformers imports
from transformers import AutoModelForCausalLM, AutoTokenizer

# ================= 配置区 =================
# 1. 模型相关
MODEL_PATH = os.path.expanduser("~/HY1.8B")
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

# 2. 文件路径
GLOSSARY_FILE = "/home/cyw/pro/train_data_2/glossary.txt"
INPUT_FILE = "/home/cyw/pro/train_data_2/outs/out_qwen2.jsonl"
OUTPUT_FILE = "/home/cyw/pro/train_data_2/outs/out_glossary_rag_cot.jsonl" # <-- 修改输出文件名

# 3. RAG & CoT 相关
PERSIST_DIRECTORY_GLOSSARY = "/home/cyw/pro/db_chroma_glossary" 
RETRIEVAL_TOP_K = 3 
# =========================================

def get_embeddings_model(device='cpu'):
    """封装嵌入模型的加载，方便复用"""
    print(f"加载嵌入模型: {EMBEDDING_MODEL} (将在 {device} 上运行)")
    model_kwargs = {'device': device}
    encode_kwargs = {'normalize_embeddings': False}
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

def setup_glossary_db(embeddings):
    """
    读取术语表，创建并持久化【术语】向量数据库。
    """
    print("\n--- 设置术语向量数据库 (Glossary DB) ---")
    if os.path.exists(PERSIST_DIRECTORY_GLOSSARY):
        print(f"1. 从磁盘加载现有术语库: {PERSIST_DIRECTORY_GLOSSARY}")
        vectorstore = Chroma(persist_directory=PERSIST_DIRECTORY_GLOSSARY, embedding_function=embeddings)
        return vectorstore.as_retriever(search_kwargs={"k": RETRIEVAL_TOP_K})

    print(f"1. 未找到现有术语库，正在创建新库...")
    print(f"2. 读取术语表: {GLOSSARY_FILE}")
    
    if not os.path.exists(GLOSSARY_FILE):
        raise FileNotFoundError(f"错误：术语表文件未找到 {GLOSSARY_FILE}")

    docs = []
    with open(GLOSSARY_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if "->" in line:
                parts = line.split('->')
                if len(parts) == 2:
                    source_term, target_term = parts[0].strip(), parts[1].strip()
                    doc = Document(
                        page_content=source_term, # 使用日文术语作为检索内容
                        metadata={"translation": f"{source_term} -> {target_term}"}
                    )
                    docs.append(doc)
    
    if not docs:
        raise ValueError("术语表为空或格式不正确，无法创建数据库。")

    print(f"3. 向量化 {len(docs)} 条术语并存入 ChromaDB...")
    vectorstore = Chroma.from_documents(
        documents=docs, 
        embedding=embeddings,
        persist_directory=PERSIST_DIRECTORY_GLOSSARY
    )
    print(f"4. 术语库已成功创建并保存至: {PERSIST_DIRECTORY_GLOSSARY}")
    
    return vectorstore.as_retriever(search_kwargs={"k": RETRIEVAL_TOP_K})

def main():
    # --- 初始化 ---
    # 统一加载嵌入模型
    embeddings = get_embeddings_model()
    
    # 设置术语向量数据库
    glossary_retriever = setup_glossary_db(embeddings)

    # 初始化分词器
    print("\n--- 初始化日文分词器 (MeCab) ---")
    try:
        tagger = fugashi.Tagger()
        print("分词器加载成功。")
    except RuntimeError:
        print("错误：无法加载MeCab。请确保已正确安装 MeCab 及其字典。")
        print("在Debian/Ubuntu上，请尝试: sudo apt-get install mecab libmecab-dev mecab-ipadic-utf8")
        print("在macOS上，请尝试: brew install mecab mecab-ipadic")
        return

    print("\n--- 翻译流程初始化 ---")
    print(f"1. 加载 LLM: {MODEL_PATH} (将在 CPU 上运行)")
    # HY 系列模型常见：fast tokenizer 元数据不完整，优先禁用 fast
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True, use_fast=False)
    except TypeError:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)

    if tokenizer.pad_token is None:
        if tokenizer.eos_token is not None:
            tokenizer.pad_token = tokenizer.eos_token
        else:
            tokenizer.pad_token_id = 0

    dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=dtype,
        low_cpu_mem_usage=True,
    )

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"2. 准备翻译 {len(lines)} 行字幕...")

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as fout:
        for line in tqdm(lines, desc="CoT翻译"):
            data = json.loads(line)
            content = data.get('content', '')

            if not content.strip():
                fout.write(line)
                continue

            # --- CoT + RAG 核心流程 ---
            # 1. 分词
            words = [word.surface for word in tagger(content)]
            
            # 2. 术语库查询 (向量检索)
            glossary_docs = glossary_retriever.invoke(content)
            glossary_terms = [doc.metadata['translation'] for doc in glossary_docs]

            # 3. 构建 CoT Prompt
            # 针对 HY 模型：使用更接近 HY-MT README 的“单轮 user 指令”模板，避免要求模型输出推理过程。
            glossary_context = "; ".join(glossary_terms) if glossary_terms else "(无)"
            tokenization_context = ", ".join(words) if words else "(无)"

            user_prompt_content = (
                "将以下日文翻译为英文（TV 字幕风格，口语化、自然、简洁）。"
                "注意：只需要输出最终英文译文，不要额外解释，不要输出分析过程。\n\n"
                f"术语表（如有命中请优先使用）：{glossary_context}\n"
                f"分词参考（可选）：{tokenization_context}\n\n"
                f"日文原文：\n{content}\n\n"
                "英文译文："
            )

            messages = [{"role": "user", "content": user_prompt_content}]

            # HY 模型 chat_template 常用于直接生成，不添加 generation prompt
            if getattr(tokenizer, "chat_template", None):
                inputs = tokenizer.apply_chat_template(
                    messages,
                    tokenize=True,
                    add_generation_prompt=False,
                    return_tensors="pt",
                ).to(model.device)
                attention_mask = (inputs != tokenizer.pad_token_id).long()
                outputs = model.generate(
                    inputs,
                    attention_mask=attention_mask,
                    max_new_tokens=256,
                    pad_token_id=tokenizer.pad_token_id,
                )
                generated_ids = outputs[0][inputs.shape[1]:]
                final_translation = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
            else:
                inputs = tokenizer(user_prompt_content, return_tensors="pt").to(model.device)
                outputs = model.generate(**inputs, max_new_tokens=256, pad_token_id=tokenizer.pad_token_id)
                generated_ids = outputs[0][inputs["input_ids"].shape[1]:]
                final_translation = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()

            # 移除模型输出中可能带出的提示前缀
            if "：" in final_translation:
                parts = final_translation.split("：", 1)
                if len(parts) > 1 and len(parts[1].strip()) > 0:
                    final_translation = parts[1].strip()

            data['output'] = final_translation
            data['cot_prompt'] = user_prompt_content # 保存prompt用于调试
            fout.write(json.dumps(data, ensure_ascii=False) + '\n')

    print(f"\n✅ 翻译完成！结果已保存至: {OUTPUT_FILE}")
    print(f"ℹ️ 提示：下次运行时，向量数据库将直接从 '{PERSIST_DIRECTORY_GLOSSARY}' 加载。")

if __name__ == "__main__":
    main()