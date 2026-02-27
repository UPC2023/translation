import os
import torch
import json
from tqdm import tqdm

# LangChain & Vector DB imports
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFacePipeline
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Transformers imports
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# ================= 配置区 =================
# 1. 模型相关
MODEL_PATH = "tencent/HY-MT1.5-1.8B"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

# 2. 文件路径
GLOSSARY_FILE = "/home/cyw/pro/train_data_2/glossary.txt"
INPUT_FILE = "/home/cyw/pro/train_data_2/test1.jsonl"
OUTPUT_FILE = "/home/cyw/pro/train_data_2/outs/out_hy_rag.jsonl"

# 3. RAG 相关
PERSIST_DIRECTORY_GLOSSARY = "/home/cyw/pro/db_chroma_glossary_hy" 
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
    读取术语/翻译记忆库，创建并持久化向量数据库。
    """
    print("\n--- 设置术语/翻译记忆库向量数据库 ---")
    if os.path.exists(PERSIST_DIRECTORY_GLOSSARY):
        print(f"1. 从磁盘加载现有库: {PERSIST_DIRECTORY_GLOSSARY}")
        vectorstore = Chroma(persist_directory=PERSIST_DIRECTORY_GLOSSARY, embedding_function=embeddings)
        return vectorstore.as_retriever(search_kwargs={"k": RETRIEVAL_TOP_K})

    print(f"1. 未找到现有库，正在创建新库...")
    print(f"2. 读取文件: {GLOSSARY_FILE}")
    
    if not os.path.exists(GLOSSARY_FILE):
        raise FileNotFoundError(f"错误：文件未找到 {GLOSSARY_FILE}")

    docs = []
    with open(GLOSSARY_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if "->" in line:
                parts = line.split('->')
                if len(parts) == 2:
                    source_term, target_term = parts[0].strip(), parts[1].strip()
                    doc = Document(
                        page_content=source_term, 
                        metadata={"translation": f"{source_term} -> {target_term}"}
                    )
                    docs.append(doc)
    
    if not docs:
        raise ValueError("文件为空或格式不正确，无法创建数据库。")

    print(f"3. 向量化 {len(docs)} 条记录并存入 ChromaDB...")
    vectorstore = Chroma.from_documents(
        documents=docs, 
        embedding=embeddings,
        persist_directory=PERSIST_DIRECTORY_GLOSSARY
    )
    print(f"4. 数据库已成功创建并保存至: {PERSIST_DIRECTORY_GLOSSARY}")
    
    return vectorstore.as_retriever(search_kwargs={"k": RETRIEVAL_TOP_K})

def main():
    """
    主函数，设置并运行一个批处理的RAG翻译流程。
    """
    # --- 初始化 ---
    # 1. 加载嵌入模型
    embeddings = get_embeddings_model()
    
    # 2. 设置向量数据库
    glossary_retriever = setup_glossary_db(embeddings)

    # 3. 加载大语言模型
    print("\n--- 翻译流程初始化 ---")
    print(f"1. 加载 LLM: {MODEL_PATH} (将在 CPU 上运行)")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map="auto", trust_remote_code=True, torch_dtype=torch.float16)
    
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=256,
        return_full_text=False,
    )
    llm = HuggingFacePipeline(pipeline=pipe)

    # 4. 创建 Prompt 模板
    # 这个模板是为翻译任务设计的通用模板，引导模型使用RAG上下文
    system_prompt = (
        "You are a professional Japanese-to-English translator. "
        "Use the provided 'Glossary Terms' to ensure consistency for specific names and phrases. "
        "Translate the 'Original Japanese Text' into fluent, natural-sounding English. "
        "Your response must be ONLY the English translation."
    )
    template = (
        f"{system_prompt}\n\n"
        "### Glossary Terms (Context):\n"
        "{context}\n\n"
        "### Original Japanese Text (Question):\n"
        "{question}\n\n"
        "### English Translation:"
    )
    prompt = PromptTemplate(template=template, input_variables=["context", "question"])

    # 5. 创建 RAG 链 (LCEL 写法)
    def format_docs(docs):
        # 从检索到的文档中提取内容，用于填充prompt
        return "\n".join(doc.metadata.get("translation", doc.page_content) for doc in docs)

    rag_chain = (
        {
            "context": glossary_retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    
    print("\n✅ RAG 批处理翻译系统已准备就绪！")

    # --- 文件批处理 ---
    print(f"\n--- 开始处理文件: {INPUT_FILE} ---")
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as infile, \
             open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
            
            lines = infile.readlines()
            for line in tqdm(lines, desc="Translating"):
                try:
                    data = json.loads(line)
                    japanese_text = data.get("content", "")
                    
                    if not japanese_text:
                        continue

                    # 使用RAG链进行翻译
                    english_translation = rag_chain.invoke(japanese_text).strip()

                    # 准备输出数据，保留原始结构
                    data["output"] = english_translation
                    outfile.write(json.dumps(data, ensure_ascii=False) + '\n')

                except json.JSONDecodeError:
                    print(f"警告: 跳过无法解析的行: {line.strip()}")
                except Exception as e:
                    print(f"处理行时发生错误 '{line.strip()}': {e}")

        print(f"\n✅ 翻译完成！结果已保存到: {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"错误: 输入文件未找到 {INPUT_FILE}")
    except Exception as e:
        print(f"处理文件时发生严重错误: {e}")


if __name__ == "__main__":
    main()
