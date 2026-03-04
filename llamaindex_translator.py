import os
import torch
import chromadb
from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from sentence_transformers import SentenceTransformer, util

# ================= 配置区 =================
# 1. 模型相关
LLM_PATH = "/home/cyw/HY1.8B"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
LABSE_MODEL = "sentence-transformers/LaBSE" # 新增：LaBSE评分模型

# 2. ChromaDB 相关
PERSIST_DIRECTORY_GLOSSARY = "/home/cyw/pro/db_chroma_glossary"

# 3. RAG 相关
RETRIEVAL_TOP_K = 3
# =========================================

print("--- RAG 翻译系统初始化 ---")

# 确定运行设备
device = "cuda" if torch.cuda.is_available() else "cpu"

# 1. 设置 LlamaIndex 全局配置
print(f"1. 加载 LLM: {LLM_PATH} (device={device})")
# 修复 HY 模型 Tokenizer 问题
tokenizer = AutoTokenizer.from_pretrained(LLM_PATH, trust_remote_code=True, use_fast=False)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    LLM_PATH,
    trust_remote_code=True,
    device_map="auto",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
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

print(f"3. 加载 LaBSE 评分模型: {LABSE_MODEL} (device={device})")
labse_model = SentenceTransformer(LABSE_MODEL, device=device)

# 4. 连接到现有的 ChromaDB
print(f"5. 连接到 ChromaDB 数据库: {PERSIST_DIRECTORY_GLOSSARY}")
if not os.path.exists(PERSIST_DIRECTORY_GLOSSARY):
    raise FileNotFoundError(f"错误：数据库目录未找到 {PERSIST_DIRECTORY_GLOSSARY}。请先运行 qwen_cot_rag.py 创建数据库。")

db = chromadb.PersistentClient(path=PERSIST_DIRECTORY_GLOSSARY)
chroma_collection = db.get_or_create_collection("chroma_collection")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(vector_store=vector_store, embed_model=embed_model)

# 5. 创建查询引擎
print("6. 创建查询引擎...")
retriever = VectorIndexRetriever(index=index, similarity_top_k=RETRIEVAL_TOP_K)

# 6. 定义翻译函数
def translate_with_rag(text_to_translate):
    """
    使用RAG和LlamaIndex进行翻译。
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
    response = text_gen(final_prompt)[0]["generated_text"].strip()
    return response

# 7. 定义评分函数
def score_translation(original_text, translated_text):
    """使用LaBSE模型为翻译评分"""
    print("\n评分中...")
    try:
        # 批量编码（这里只有两个句子，但保持API一致性）
        embeddings = labse_model.encode(
            [original_text, translated_text],
            convert_to_tensor=True,
            normalize_embeddings=True
        )
        # 计算余弦相似度
        similarity = util.cos_sim(embeddings[0], embeddings[1])
        return similarity.item()
    except Exception as e:
        print(f"LaBSE评分时出错: {e}")
        return None

# 8. 交互式翻译循环
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
        # 翻译
        final_translation = translate_with_rag(query)
        print("\n--- 最终翻译 ---")
        print(final_translation)

        # 评分
        labse_score = score_translation(query, final_translation)
        if labse_score is not None:
            print("\n--- LaBSE 语义相似度得分 ---")
            print(f"{labse_score:.4f}")

    except Exception as e:
        print(f"翻译或评分过程中发生错误: {e}")

print("\n👋 系统已退出。")


