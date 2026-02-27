import json
import torch
from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer, AutoModelForCausalLM

# ================= 配置区 =================
# 建议先用 Base 模型测试，排除 Lora 的干扰
MODEL_PATH = "/home/cyw/Qwen2.5-0.5B" 
INPUT_FILE = "/home/cyw/pro/train_data_2/outs/out_qwen2.jsonl"
OUTPUT_FILE = "/home/cyw/pro/train_data_2/outs/out_smart_rag.jsonl"
GLOSSARY_FILE = "/home/cyw/pro/train_data_2/glossary.txt"

# 门控阈值：如果 Context 和 Input 的相似度低于这个值，就丢弃 Context
# 0.2 是一个比较保守的值，既能过滤掉完全无关的菜谱，又能保留相关的剧情
CONTEXT_THRESHOLD = 0.25 
# =========================================

class SmartTranslator:
    def __init__(self):
        print("1. Loading Models...")
        # 加载向量模型用来做“门控”判断
        self.embedder = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
        
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map="auto", trust_remote_code=True)
        
        # 加载术语表
        self.glossary = {}
        self.load_glossary()

    def load_glossary(self):
        try:
            with open(GLOSSARY_FILE, 'r', encoding='utf-8') as f:
                for line in f:
                    if "->" in line:
                        k, v = line.strip().split("->")
                        self.glossary[k.strip()] = v.strip()
            print(f"   术语表加载完成: {len(self.glossary)} 条")
        except:
            print("   未找到术语表，跳过。")

    def check_context_relevance(self, input_text, context_text):
        """
        核心逻辑：判断 Context 是否是噪声
        """
        if not context_text or len(context_text) < 5:
            return False, 0.0
            
        # 计算两个句子的相似度
        embeddings = self.embedder.encode([input_text, context_text], convert_to_tensor=True)
        score = util.cos_sim(embeddings[0], embeddings[1]).item()
        
        # 如果相似度太低，说明上下文是废话（比如“做意面” vs “走过的路”）
        return score >= CONTEXT_THRESHOLD, score

    def translate(self, text, raw_context):
        # 1. 术语硬匹配 (最高优先级)
        glossary_hits = []
        for k, v in self.glossary.items():
            if k in text:
                glossary_hits.append(f"{k}={v}")
        
        # 2. Context 智能过滤 (RAG 降权逻辑)
        is_relevant, score = self.check_context_relevance(text, raw_context)
        
        final_context = ""
        # 只有当相关性够高，或者 Context 里包含了当前句子的术语时，才保留
        if is_relevant:
            # 极度精简：只取 Context 的前 50 个字符，防止 0.5B 晕头转向
            short_context = raw_context[:50].replace("\n", " ") + "..."
            final_context = short_context
        else:
            # 如果不相关，强制清空！防止“Hirunandesu”幻觉
            final_context = ""

        # 3. 构造 Prompt
        # 使用 XML 标签让模型分清主次，这是 0.5B 模型更容易理解的格式
        
        sys_prompt = "You are a professional subtitle translator. Translate Japanese to English."
        
        # 动态构建 User Prompt
        user_prompt_parts = []
        
        # A. 术语提示 (最强约束)
        if glossary_hits:
            user_prompt_parts.append(f"<glossary>{', '.join(glossary_hits)}</glossary>")
            
        # B. 背景信息 (如果有的话)
        if final_context:
            user_prompt_parts.append(f"<background>{final_context}</background>")
            
        # C. 待翻译文本
        user_prompt_parts.append(f"<text>{text}</text>")
        
        user_msg = "\n".join(user_prompt_parts)
        
        # 构造 ChatML
        prompt = f"<|im_start|>system\n{sys_prompt}<|im_end|>\n<|im_start|>user\n{user_msg}<|im_end|>\n<|im_start|>assistant\n"

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=80,
                temperature=0.1, # 必须低温
                do_sample=False, # 确定性输出
                repetition_penalty=1.1,
                eos_token_id=self.tokenizer.eos_token_id
            )
            
        decoded = self.tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
        
        # 清理 XML 标签（如果模型傻乎乎地输出了标签）
        decoded = decoded.replace("<text>", "").replace("</text>", "").strip()
        return decoded, is_relevant, score

# ================= 主程序 =================
translator = SmartTranslator()

with open(INPUT_FILE, 'r', encoding='utf-8') as fin, \
     open(OUTPUT_FILE, 'w', encoding='utf-8') as fout:
    
    for i, line in enumerate(fin):
        data = json.loads(line)
        content = data.get('content', '')
        context = data.get('context', '') # 这里是你原来 JSON 里的 context
        original_output = data.get('output', '')  # 添加这一行
        # 跳过空行
        if not content: continue

        # 翻译
        translation, used_context, score = translator.translate(content, context)
        
        # 保存
        data['output_qwen'] = original_output  # 保存原output
        data['output'] = translation 
        # 调试信息保存进去，方便你查看 Context 是否被使用了
        data['debug_context_used'] = used_context
        data['debug_context_score'] = round(score, 3)
        
        fout.write(json.dumps(data, ensure_ascii=False) + "\n")
        
        if i % 10 == 0:
            status = "[Context保留]" if used_context else "[Context丢弃]"
            print(f"{status} (Sim:{score:.2f})")
            print(f"原文: {content}")
            if used_context: print(f"背景: {context[:30]}...")
            print(f"译文: {translation}")
            print("-" * 30)

print("Done.")