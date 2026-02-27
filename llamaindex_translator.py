import os
import torch
import chromadb
from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# ================= 配置区 =================
# 1. 模型相关
LLM_PATH = "/home/cyw/HY1.8B"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

# 2. ChromaDB 相关
PERSIST_DIRECTORY_GLOSSARY = "/home/cyw/pro/db_chroma_glossary"

# 3. RAG 相关
RETRIEVAL_TOP_K = 3
# =========================================

print("--- RAG 翻译系统初始化 ---")

# 1. 设置 LlamaIndex 全局配置
print(f"1. 加载 LLM: {LLM_PATH}")
# 修复 HY 模型 Tokenizer 问题
tokenizer = AutoTokenizer.from_pretrained(LLM_PATH, trust_remote_code=True, use_fast=False)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# HY-MT 官方模板
prompt_template = "将以下文本翻译为中文，注意只需要输出翻译后的结果，不要额外解释：\n\n{query_str}"

model = AutoModelForCausalLM.from_pretrained(
    LLM_PATH,
    trust_remote_code=True,
    device_map="auto",
    torch_dtype=torch.float16,
)

text_gen = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=256,
    pad_token_id=tokenizer.eos_token_id,
    return_full_text=False,
)

print(f"2. 加载嵌入模型: {EMBEDDING_MODEL}")
embed_model = HuggingFaceEmbedding(model_name=EMBEDDING_MODEL)

# 2. 连接到现有的 ChromaDB
print(f"3. 连接到 ChromaDB 数据库: {PERSIST_DIRECTORY_GLOSSARY}")
if not os.path.exists(PERSIST_DIRECTORY_GLOSSARY):
    raise FileNotFoundError(f"错误：数据库目录未找到 {PERSIST_DIRECTORY_GLOSSARY}。请先运行 qwenadvanced_rag_translator.py 创建数据库。")

db = chromadb.PersistentClient(path=PERSIST_DIRECTORY_GLOSSARY)
chroma_collection = db.get_or_create_collection("chroma_collection") # 注意：这里的名字需要和创建时一致，qwenadvanced_rag_translator.py中是默认名
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(vector_store=vector_store, embed_model=embed_model)

# 3. 创建查询引擎
print("4. 创建查询引擎...")
retriever = VectorIndexRetriever(index=index, similarity_top_k=RETRIEVAL_TOP_K)

# 4. 定义翻译函数
def translate_with_rag(text_to_translate):
    """
    使用RAG和LlamaIndex进行翻译。
    如果找不到相关上下文，则回退到直接翻译。
    """
    print("\n翻译中...")
    
    # 1. 手动进行检索
    retrieved_nodes = retriever.retrieve(text_to_translate)
    
    # 2. 根据检索结果构建不同的Prompt
    print("\n--- 检索到的相关记忆库条目 ---")
    if retrieved_nodes:
        context_str = "\n".join(
            [node.metadata.get('translation', node.get_content()) for node in retrieved_nodes]
        )
        print(context_str)
        
        # RAG模式：带有上下文的Prompt
        final_prompt = f"""
        You are an expert Japanese-to-Chinese translator. 
        Use the provided 'Translation Memory' to ensure consistency.
        Translate the 'Original Japanese Text'.

        ### Translation Memory (Context):
        {context_str}

        ### Original Japanese Text:
        {text_to_translate}

        ### Chinese Translation:
        """
    else:
        # Fallback模式：没有上下文的直接翻译Prompt
        print("  (未找到相关条目，回退到直接翻译模式)")
        final_prompt = f"""
        You are an expert Japanese-to-Chinese translator.
        Translate the 'Original Japanese Text'.

        ### Original Japanese Text:
        {text_to_translate}

        ### Chinese Translation:
        """

    # 3. 调用LLM
    # 注意：我们不再使用 query_engine.query()，而是直接调用 llm.complete()
    response = text_gen(final_prompt)[0]["generated_text"].strip()
    return response


# 5. 交互式翻译循环
print("\n✅ RAG 翻译系统已准备就绪！")
print("========================================")
print("🤖 请输入要翻译的日文，或输入 'exit' 退出。")
print("========================================")

while True:
    query = input("\n> 日文原文: ")
    if query.lower() == 'exit':
        break
    if not query.strip():
        continue

    try:
        final_translation = translate_with_rag(query)
        print("\n--- 最终翻译 ---")
        print(final_translation)

    except Exception as e:
        print(f"翻译过程中发生错误: {e}")

print("\n👋 系统已退出。")


