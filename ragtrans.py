import torch
from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer, AutoModelForCausalLM

class SimpleRAGTranslator:
    def __init__(self, llm_path, embedding_model_name='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'):
        # 1. 加载向量化模型 (负责“找”资料)
        # 这个模型很小，专门用来判断两句话的意思像不像
        print("正在加载向量模型...")
        self.embedder = SentenceTransformer(embedding_model_name)
        
        # 2. 加载你的 Qwen 模型 (负责“写”翻译)
        print(f"正在加载 LLM: {llm_path}...")
        self.tokenizer = AutoTokenizer.from_pretrained(llm_path, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(llm_path, device_map="auto", trust_remote_code=True)
        
        # 内存里的“知识库”
        self.knowledge_texts = []      # 存原始文字
        self.knowledge_embeddings = None # 存转化后的向量

    def load_glossary(self, glossary_list):
        """
        把术语表加载进来，并预先计算好向量
        """
        print("正在构建知识库索引...")
        self.knowledge_texts = glossary_texts
        # 这里把所有的术语一次性变成向量矩阵
        self.knowledge_embeddings = self.embedder.encode(self.knowledge_texts, convert_to_tensor=True)
        print(f"知识库构建完成，共 {len(self.knowledge_texts)} 条术语。")

    def search(self, query, top_k=2):
        """
        核心逻辑：在知识库里找和 query 最相关的 top_k 条
        """
        # 1. 把输入句子变成向量
        query_embedding = self.embedder.encode(query, convert_to_tensor=True)
        
        # 2. 计算余弦相似度 (Cosine Similarity)
        # 这就是 RAG 的本质：算向量之间的距离
        cos_scores = util.cos_sim(query_embedding, self.knowledge_embeddings)[0]
        
        # 3. 找出分数最高的 top_k 个索引
        top_results = torch.topk(cos_scores, k=min(top_k, len(self.knowledge_texts)))
        
        results = []
        for score, idx in zip(top_results[0], top_results[1]):
            # 只有相似度大于 0.3 才算相关，防止把不相干的词也拉进来
            if score > 0.3: 
                results.append(self.knowledge_texts[idx])
        
        return results

    def translate(self, input_text):
        # --- RAG 步骤 1: 检索 ---
        relevant_terms = self.search(input_text)
        
        # --- RAG 步骤 2: 增强 Prompt ---
        # 如果找到了相关术语，就拼接到 Prompt 里
        context_str = ""
        if relevant_terms:
            context_str = "Terminology Context:\n" + "\n".join([f"- {term}" for term in relevant_terms])
        else:
            context_str = "No specific terminology found."

        # 构造适合 Qwen 的 Prompt (ChatML 格式)
        prompt = f"""<|im_start|>system
You are a professional translator. Translate the Japanese text to English.<|im_end|>
<|im_start|>user
{context_str}

Text to Translate:
{input_text}<|im_end|>
<|im_start|>assistant
"""
        
        # --- RAG 步骤 3: 生成 ---
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs, 
                max_new_tokens=100, 
                temperature=0.1, # 翻译任务温度要低，越低越稳定
                repetition_penalty=1.1
            )
        
        # 解码并去除 Prompt 部分
        response = self.tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
        return response.strip(), relevant_terms

# ================= 使用示例 =================

if __name__ == "__main__":
    # 你的术语表 (格式：原文 -> 译文 [备注])
    glossary_texts = [
        "ユーク -> Yuke (Protagonist)",
        "レイン -> Rain (Female Mage)",
        "Ａランク -> A-Rank",
        "ヱビス -> Yebisu (Beer Brand)",
        "離脱 -> Left/Defected",
        "迷宮 -> Dungeon"
    ]

    # 初始化翻译器 (替换为你微调后的模型路径)
    # 如果微调还没修好，先用 "Qwen/Qwen2.5-0.5B-Instruct" 原版试试
    translator = SimpleRAGTranslator(llm_path="/home/cyw/Qwen2.5-0.5B") 

    # 加载术语
    translator.load_glossary(glossary_texts)

    # 测试句子
    test_sentences = [
        "Ａランクパーティを離脱したユークは、迷宮深部を目指す。",
        "今日はヱビスビールでお祝いだ！"
    ]

    print("\n" + "="*30)
    for sent in test_sentences:
        print(f"原文: {sent}")
        translation, used_terms = translator.translate(sent)
        print(f"检索到的知识: {used_terms}")
        print(f"翻译结果: {translation}")
        print("-" * 30)