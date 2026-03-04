import os
import torch

# LangChain & Vector DB imports (Updated for new versions)
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFacePipeline


# Transformers imports
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from sentence_transformers import SentenceTransformer, util

# ================= 配置区 =================
# 1. 模型相关
MODEL_PATH = "Qwen/Qwen2.5-0.5B-Instruct"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
LABSE_MODEL = "sentence-transformers/LaBSE"

# 2. 文件路径
GLOSSARY_FILE = "/home/cyw/pro/train_data_2/glossary.txt" # 包含角色词汇表、地名、翻译记忆库等
INPUT_FILE = "/home/cyw/pro/train_data_2/outs/out_qwen2.jsonl"
OUTPUT_FILE = "/home/cyw/pro/train_data_2/outs/out_advanced_rag_cot.jsonl"

# 3. RAG 相关
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
                    # 使用源文本作为检索内容，完整翻译作为元数据
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
    主函数，设置并运行一个交互式的RAG翻译流程。
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
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map="auto", trust_remote_code=True)
    
    # 使用HuggingFacePipeline封装模型以便与LangChain集成
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=100,
        # 从模型的回应中移除prompt
        return_full_text=False, 
    )
    llm = HuggingFacePipeline(pipeline=pipe)

    # 4. 加载 LaBSE 评分模型
    print(f"2. 加载 LaBSE 评分模型: {LABSE_MODEL}")
    labse_model = SentenceTransformer(LABSE_MODEL)

    # 5. 创建 Prompt 模板
    system_prompt = (
        "You are an expert Japanese-to-English translator for TV subtitles. "
        "Use the provided 'Translation Memory' (retrieved context) to ensure consistency. "
        "Translate the user's 'Original Japanese Text' into natural-sounding English. "
        "Provide ONLY the final English translation."
    )
    template = (
        f"{system_prompt}\n\n"
        "### Translation Memory (Context):\n"
        "{context}\n\n"
        "### Original Japanese Text (Question):\n"
        "{question}\n\n"
        "### English Translation:"
    )
    prompt = PromptTemplate(template=template, input_variables=["context", "question"])

    # 6. (已移除 RetrievalQA 链，改为手动执行RAG流程以修复依赖问题)
    # qa_chain = RetrievalQA.from_chain_type(...) 
    
    print("\n✅ RAG 翻译系统已准备就绪！")
    print("========================================")
    print("🤖 请输入要翻译的日文，或输入 'exit' 退出。")
    print("========================================")

    # --- 交互式翻译循环 ---
    while True:
        query = input("\n> 日文原文: ")
        if query.lower() == 'exit':
            break
        if not query.strip():
            continue

        print("翻译中...")
        try:
            # 1. 手动检索相关文档
            docs = glossary_retriever.invoke(query)
            
            # 2. 构建上下文 (使用 translate metadata 如果可用，否则使用 page_content)
            context_str = "\n".join([doc.metadata.get("translation", doc.page_content) for doc in docs])
            
            # 3. 填充Prompt
            final_prompt_str = prompt.format(context=context_str, question=query)

            # 4. 调用 LLM
            # 注意: llm 是 HuggingFacePipeline, 也是Runnable
            final_translation = llm.invoke(final_prompt_str)
            
            print("\n--- 最终翻译 ---")
            # 清理结果 (有些模型可能会输出额外内容，虽然 pipeline 设置了 return_full_text=False)
            final_translation = final_translation.strip()
            print(final_translation)
            
            # LaBSE Score
            src_emb = labse_model.encode(query, convert_to_tensor=True)
            tgt_emb = labse_model.encode(final_translation, convert_to_tensor=True)
            score = util.pytorch_cos_sim(src_emb, tgt_emb).item()
            print(f"\n--- LaBSE 评分: {score:.4f} ---")
            
            print("\n--- 检索到的相关记忆库条目 ---")
            if docs:
                for i, doc in enumerate(docs):
                    print(f"  [{i+1}] {doc.metadata.get('translation', 'N/A')}")
            else:
                print("  (未找到相关条目)")

        except Exception as e:
            print(f"翻译过程中发生错误: {e}")

    print("\n👋 系统已退出。")

if __name__ == "__main__":
    main()