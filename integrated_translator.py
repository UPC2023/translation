import os
import torch
import chromadb
import gc
from llama_index.core import VectorStoreIndex, Document
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from sentence_transformers import SentenceTransformer, util

# ================= 配置区 =================
# 1. 模型相关
QWEN_MODEL_PATH = "Qwen/Qwen2.5-0.5B-Instruct"
HY_MODEL_PATH = "/home/cyw/HY1.8B"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
LABSE_MODEL = "sentence-transformers/LaBSE"

# 2. ChromaDB 相关
PERSIST_DIRECTORY_GLOSSARY = "/home/cyw/pro/db_chroma_glossary"

# 3. RAG & 学习机制相关
RETRIEVAL_TOP_K = 3
LEARNING_THRESHOLD = 0.8  # LaBSE分数大于此阈值时，自动存入知识库
# =========================================

# --- 全局变量 ---
labse_model = None
text_gen_pipelines = {}
_model_tokenizer_cache = {}
retriever = None
index = None


def _get_model_and_tokenizer(model_path: str):
    """Load (and cache) model+tokenizer.

    HY 模型推荐走 chat_template（README），而 Qwen 仍可走 pipeline。
    """
    if model_path in _model_tokenizer_cache:
        return _model_tokenizer_cache[model_path]

    use_fast = False if "HY" in model_path.upper() else True
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True, use_fast=use_fast)
    except Exception:
        tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True, use_fast=False)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        trust_remote_code=True,
        device_map="auto",
        torch_dtype=torch.float16,
    )
    model.eval()

    _model_tokenizer_cache[model_path] = (model, tokenizer)
    return model, tokenizer


def _build_hy_prompt(
    source_text: str,
    target_language: str = "中文",
    context: str | None = None,
) -> str:
    """Build HY prompt following HY1.8B README templates.

    - 有 context：走“contextual translation”模板，并明确不翻译上文。
    - 无 context：走基础 ZH<=>XX 模板。
    """
    if context and context.strip():
        return (
            f"{context}\n"
            f"参考上面的信息，把下面的文本翻译成{target_language}，注意不需要翻译上文，也不要额外解释：\n"
            f"{source_text}\n"
        )
    return (
        f"将以下文本翻译为{target_language}，注意只需要输出翻译后的结果，不要额外解释：\n\n"
        f"{source_text}\n"
    )

def setup_models_and_retriever():
    """一次性加载所有模型和数据库连接"""
    global labse_model, text_gen_pipelines, retriever, index
    
    print("--- 系统初始化 ---")

    # 1. 加载 LaBSE 模型
    print(f"1. 加载 LaBSE 评估模型: {LABSE_MODEL}")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    labse_model = SentenceTransformer(LABSE_MODEL, device=device)

    # 2. 加载嵌入模型
    print(f"2. 加载嵌入模型: {EMBEDDING_MODEL}")
    embed_model = HuggingFaceEmbedding(model_name=EMBEDDING_MODEL)

    # 3. 连接到 ChromaDB
    print(f"3. 连接到 ChromaDB: {PERSIST_DIRECTORY_GLOSSARY}")
    db = chromadb.PersistentClient(path=PERSIST_DIRECTORY_GLOSSARY)
    chroma_collection = db.get_or_create_collection("chroma_collection")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store, embed_model=embed_model)
    retriever = VectorIndexRetriever(index=index, similarity_top_k=RETRIEVAL_TOP_K)
    
    # 4. 预加载翻译模型 (可选，如果内存充足)
    # 为了节省内存，我们也可以在需要时动态加载
    print("4. 翻译模型将在首次使用时动态加载。")
    print("\n✅ 系统初始化完成！")


def get_translation_pipeline(model_path: str):
    """动态加载或从缓存获取翻译模型pipeline"""
    if model_path in text_gen_pipelines:
        return text_gen_pipelines[model_path]

    print(f"\n首次加载翻译模型: {model_path}...")
    # Qwen 等模型走 pipeline；HY 走 chat_template + generate（见 translate_with_model）
    use_fast = False if "HY" in model_path.upper() else True
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True, use_fast=use_fast)
    except Exception:
        tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True, use_fast=False)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        trust_remote_code=True,
        device_map="auto",
        torch_dtype=torch.float16,
    )
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=256,
        return_full_text=False,
    )
    text_gen_pipelines[model_path] = pipe
    return pipe


def translate_with_model(
    model_path: str,
    prompt: str,
    *,
    hy_source_text: str | None = None,
    hy_context: str | None = None,
    hy_target_language: str = "中文",
) -> str:
    """使用指定模型进行翻译。

    注意：HY 不建议把“英文 RAG 指令块”当作 source_text 直接翻译；
    因此 HY 路径支持传入 hy_source_text / hy_context 来构造官方模板。
    """

    if "HY" in model_path.upper():
        model, tokenizer = _get_model_and_tokenizer(model_path)
        source_text = hy_source_text if hy_source_text is not None else prompt
        hy_prompt = _build_hy_prompt(source_text, target_language=hy_target_language, context=hy_context)
        messages = [{"role": "user", "content": hy_prompt}]

        if getattr(tokenizer, "chat_template", None):
            inputs = tokenizer.apply_chat_template(
                messages,
                tokenize=True,
                add_generation_prompt=False,
                return_tensors="pt",
            ).to(model.device)
            attention_mask = (inputs != tokenizer.pad_token_id).long()
            input_len = inputs.shape[1]
            with torch.inference_mode():
                outputs = model.generate(
                    inputs,
                    attention_mask=attention_mask,
                    max_new_tokens=256,
                    top_k=20,
                    top_p=0.6,
                    repetition_penalty=1.05,
                    temperature=0.7,
                    do_sample=True,
                    pad_token_id=tokenizer.pad_token_id,
                )
            generated_ids = outputs[0][input_len:]
            return tokenizer.decode(generated_ids, skip_special_tokens=True).strip()

        # 兜底：无 chat_template 时直接喂纯文本
        inputs = tokenizer(hy_prompt, return_tensors="pt").to(model.device)
        with torch.inference_mode():
            outputs = model.generate(
                **inputs,
                max_new_tokens=256,
                top_k=20,
                top_p=0.6,
                repetition_penalty=1.05,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.pad_token_id,
            )
        generated_ids = outputs[0][inputs["input_ids"].shape[1]:]
        return tokenizer.decode(generated_ids, skip_special_tokens=True).strip()

    # Qwen 等模型：RAG prompt 已经构造好，直接 pipeline
    pipe = get_translation_pipeline(model_path)
    response = pipe(prompt)
    return response[0]["generated_text"].strip()


def compute_labse_similarity(text1: str, text2: str) -> float:
    """计算两个文本的LaBSE相似度"""
    if not text1 or not text2 or labse_model is None:
        return 0.0
    emb1 = labse_model.encode(text1, convert_to_tensor=True, normalize_embeddings=True)
    emb2 = labse_model.encode(text2, convert_to_tensor=True, normalize_embeddings=True)
    return util.cos_sim(emb1, emb2).item()


def integrated_translation_flow(text_to_translate: str):
    """完整的集成翻译流程"""
    
    # 1. RAG检索
    print("\n--- 1. RAG 检索 ---")
    retrieved_nodes = retriever.retrieve(text_to_translate)
    context_str = ""
    if retrieved_nodes:
        context_str = "\n".join([node.metadata.get('translation', node.get_content()) for node in retrieved_nodes])
        print("  检索到上下文:")
        print(context_str)
    else:
        print("  未找到相关上下文。")

    # 2. 构建Prompt
    rag_prompt = f"""
You are an expert Japanese-to-Chinese translator. 
Use the provided 'Translation Memory' to ensure consistency if available.
Translate the 'Original Japanese Text'.

### Translation Memory (Context):
{context_str if context_str else "N/A"}

### Original Japanese Text:
{text_to_translate}

### Chinese Translation:
"""
    
    # 3. 双模型翻译 (Agents)
    print("\n--- 2. 双模型翻译 (Agents) ---")
    print("  🤖 Agent 1 (Qwen) 翻译中...")
    qwen_translation = translate_with_model(QWEN_MODEL_PATH, rag_prompt)
    print(f"  Qwen 输出: {qwen_translation}")

    print("\n  🌀 Agent 2 (HY) 翻译中...")
    # HY 按 README 的 contextual translation 模板来构造 prompt；避免把英文 RAG 指令块当作 source_text。
    hy_translation = translate_with_model(
        HY_MODEL_PATH,
        rag_prompt,
        hy_source_text=text_to_translate,
        hy_context=context_str if context_str else None,
        hy_target_language="中文",
    )
    print(f"  HY 输出: {hy_translation}")

    # 4. LaBSE 评估
    print("\n--- 3. LaBSE 评估 ---")
    qwen_score = compute_labse_similarity(text_to_translate, qwen_translation)
    hy_score = compute_labse_similarity(text_to_translate, hy_translation)
    print(f"  Qwen 分数: {qwen_score:.4f}")
    print(f"  HY 分数: {hy_score:.4f}")

    # 5. 选择最佳翻译
    print("\n--- 4. 选择最佳翻译 ---")
    if qwen_score >= hy_score:
        final_translation = qwen_translation
        best_model_name = "Qwen"
        best_score = qwen_score
        print(f"  ✅ 选择 Qwen 作为最佳翻译。")
    else:
        final_translation = hy_translation
        best_model_name = "HY"
        best_score = hy_score
        print(f"  ✅ 选择 HY 作为最佳翻译。")

    # 6. 自动学习机制
    print("\n--- 5. 自动学习 ---")
    if best_score > LEARNING_THRESHOLD:
        print(f"  📈 分数 ({best_score:.4f}) > 阈值 ({LEARNING_THRESHOLD})，存入知识库...")
        new_doc_text = f"{text_to_translate} -> {final_translation}"
        new_doc = Document(
            text=text_to_translate, 
            metadata={"translation": new_doc_text}
        )
        index.insert(new_doc)
        print("  💾 保存成功！")
    else:
        print(f"  📉 分数 ({best_score:.4f}) <= 阈值 ({LEARNING_THRESHOLD})，不保存。")
        
    return final_translation, best_model_name


def main():
    """主交互循环"""
    setup_models_and_retriever()
    
    print("\n========================================")
    print("🤖 集成翻译系统已准备就绪！")
    print("   - RAG + 双模型 Agents (Qwen & HY)")
    print(f"   - LaBSE评估 & 自动学习 (阈值: {LEARNING_THRESHOLD})")
    print("========================================")

    while True:
        query = input("\n> 日文原文 (或输入 'exit' 退出): ")
        if query.lower() == 'exit':
            break
        if not query.strip():
            continue

        try:
            final_translation, best_model = integrated_translation_flow(query)
            print("\n--- 最终翻译结果 ---")
            print(f"  模型: {best_model}")
            print(f"  译文: {final_translation}")

        except Exception as e:
            print(f"\n❌ 翻译过程中发生严重错误: {e}")
            # 在发生错误时，尝试释放GPU内存
            gc.collect()
            torch.cuda.empty_cache()

    print("\n👋 系统已退出。")


if __name__ == "__main__":
    main()
