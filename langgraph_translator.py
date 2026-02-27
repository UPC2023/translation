import os
import json
from typing import TypedDict, Literal, Tuple, Dict, Optional
from concurrent.futures import ThreadPoolExecutor
import gc
import torch
from langgraph.graph import StateGraph, END
from transformers import AutoModelForCausalLM, AutoTokenizer
from sentence_transformers import SentenceTransformer, util


# ================= 配置区 =================
QWEN_MODEL_PATH = "/home/cyw/Qwen2.5-0.5B"
HY_MODEL_PATH = "/home/cyw/HY1.8B"
LABSE_MODEL = "sentence-transformers/LaBSE"
INPUT_FILE = "/home/cyw/pro/train_data_2/test2.jsonl"
OUTPUT_FILE = "/home/cyw/pro/train_data_2/test2_translated.jsonl"

# ================= 性能开关（环境变量） =================
# 1) PARALLEL_TRANSLATION=1：尝试并行跑 Qwen/HY（仅在 CPU 或多 GPU 时更可能有收益；单 GPU 通常不会更快且可能更慢/更占内存）
# 2) CACHE_MODELS=1：缓存并复用模型/分词器/LaBSE，避免每条样本重复 from_pretrained（通常是最大提速点）
PARALLEL_TRANSLATION = os.getenv("PARALLEL_TRANSLATION", "0") == "1"
CACHE_MODELS = os.getenv("CACHE_MODELS", "0") == "1"

_MODEL_CACHE: Dict[str, Tuple[object, object]] = {}
_LABSE_CACHE: Optional[SentenceTransformer] = None

class AgentState(TypedDict):
    original_text: str
    qwen_translation: str
    hy_translation: str
    qwen_labse_score: float
    hy_labse_score: float
    final_translation: str
    best_model: str
    # 添加模型路径以在节点间传递
    qwen_model_path: str
    hy_model_path: str
    labse_model_path: str


def get_model_and_tokenizer(model_path: str):
    if CACHE_MODELS and model_path in _MODEL_CACHE:
        return _MODEL_CACHE[model_path]

    # 部分 HY 模型缺少 fast tokenizer 元数据，优先禁用 fast；若仍失败则回退重试
    use_fast = False if "HY" in model_path.upper() else True
    try:
        tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=True,
            use_fast=use_fast,
            padding_side="left",
            truncation_side="left"
        )
    except Exception:
        tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=True,
            use_fast=False,
            padding_side="left",
            truncation_side="left",
            legacy=False
        )
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", trust_remote_code=True)
    model.eval()

    # 修复 attention_mask 警告：设置 pad_token
    if tokenizer.pad_token is None:
        if tokenizer.eos_token is not None:
            tokenizer.pad_token = tokenizer.eos_token
        else:
            tokenizer.pad_token_id = 0

    if CACHE_MODELS:
        _MODEL_CACHE[model_path] = (model, tokenizer)
    return model, tokenizer


def unload_model_and_tokenizer(model, tokenizer) -> None:
    if CACHE_MODELS:
        return
    del model, tokenizer
    gc.collect()
    torch.cuda.empty_cache()


def translate(text: str, model, tokenizer, model_type: str) -> str:
    target_language = "中文"

    if model_type == "hy":
        # HY-MT 官方模板（README）
        content = f"将以下文本翻译为{target_language}，注意只需要输出翻译后的结果，不要额外解释：\n\n{text}"
        messages = [{"role": "user", "content": content}]
        inputs = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=False, return_tensors="pt").to(model.device)

        # 创建 attention_mask
        attention_mask = (inputs != tokenizer.pad_token_id).long()

        with torch.inference_mode():
            outputs = model.generate(
                inputs,
                attention_mask=attention_mask,
                max_new_tokens=256,
                pad_token_id=tokenizer.pad_token_id
            )
        generated_ids = outputs[0][inputs.shape[1]:]
        response = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
        # 移除 HY 模型输出中可能包含的指令文本
        if "。\n" in response:
            return response.split("。\n")[-1].strip()
        if "：" in response:
            parts = response.split('：', 1)
            if len(parts) > 1:
                return parts[1].strip()
        return response
    else:
        system_prompt = (
            "你是一名资深的日语→中文字幕翻译，擅长口语化、凝练的表达。"
            "请将提供的日文内容翻译成自然流畅的中文，仅输出译文本身，不要添加注释或解释。"
        )
        user_prompt = (
            "上下文（可能为空）：\n"
            "<无额外上下文>\n\n"
            "待翻译内容（日文）：\n"
            f"{text}\n\n"
            "中文译文："
        )

        if getattr(tokenizer, "chat_template", None):
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
            prompt_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        else:
            prompt_text = f"{system_prompt}\n\n{user_prompt}"

        inputs = tokenizer(prompt_text, return_tensors="pt").to(model.device)
        if 'token_type_ids' in inputs:
            del inputs['token_type_ids']
        with torch.inference_mode():
            outputs = model.generate(**inputs, max_new_tokens=256, pad_token_id=tokenizer.eos_token_id)
        generated_ids = outputs[0][inputs["input_ids"].shape[1]:]
        response = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()

        if "assistant\n" in response:
            return response.split("assistant\n")[-1].strip()
        return response


def compute_labse_similarity(text1: str, text2: str, labse_model) -> float:
    if not text1 or not text2:
        return 0.0
    emb1 = labse_model.encode(text1, convert_to_tensor=True, normalize_embeddings=True)
    emb2 = labse_model.encode(text2, convert_to_tensor=True, normalize_embeddings=True)
    return util.cos_sim(emb1, emb2).item()


def translate_with_qwen(state: AgentState) -> AgentState:
    print("🤖 Qwen翻译中...")
    model, tokenizer = get_model_and_tokenizer(state['qwen_model_path'])
    state['qwen_translation'] = translate(state['original_text'], model, tokenizer, "qwen")
    print(f"  Qwen 输出: {state['qwen_translation']}")
    unload_model_and_tokenizer(model, tokenizer)
    return state


def translate_with_hy(state: AgentState) -> AgentState:
    print("🌀 HY-MT 翻译中...")
    model, tokenizer = get_model_and_tokenizer(state['hy_model_path'])
    state['hy_translation'] = translate(state['original_text'], model, tokenizer, "hy")
    print(f"  HY 输出: {state['hy_translation']}")
    unload_model_and_tokenizer(model, tokenizer)
    return state


def translate_with_both(state: AgentState) -> AgentState:
    """在一个节点里拿到两路译文。

    - 默认顺序执行，最省显存。
    - 打开 PARALLEL_TRANSLATION=1 时，会在 CPU 或多 GPU 环境尝试并行。
    """

    def _run_one(model_path: str, model_type: str) -> str:
        model, tokenizer = get_model_and_tokenizer(model_path)
        out = translate(state['original_text'], model, tokenizer, model_type)
        unload_model_and_tokenizer(model, tokenizer)
        return out

    cuda_available = torch.cuda.is_available()
    cuda_count = torch.cuda.device_count() if cuda_available else 0

    can_parallel = PARALLEL_TRANSLATION and (not cuda_available or cuda_count >= 2)
    if can_parallel:
        print("⚡ 并行翻译中（Qwen + HY）...")
        with ThreadPoolExecutor(max_workers=2) as ex:
            f_q = ex.submit(_run_one, state['qwen_model_path'], "qwen")
            f_h = ex.submit(_run_one, state['hy_model_path'], "hy")
            state['qwen_translation'] = f_q.result()
            state['hy_translation'] = f_h.result()
    else:
        if PARALLEL_TRANSLATION and cuda_available and cuda_count < 2:
            print("ℹ️ 仅检测到单 GPU：跳过并行（通常不会提速且更容易爆显存）")
        print("🤖 顺序翻译中（Qwen -> HY）...")
        state['qwen_translation'] = _run_one(state['qwen_model_path'], "qwen")
        print(f"  Qwen 输出: {state['qwen_translation']}")
        state['hy_translation'] = _run_one(state['hy_model_path'], "hy")
        print(f"  HY 输出: {state['hy_translation']}")

    if can_parallel:
        print(f"  Qwen 输出: {state['qwen_translation']}")
        print(f"  HY 输出: {state['hy_translation']}")
    return state


def evaluate_with_labse(state: AgentState) -> AgentState:
    print("📊 LaBSE评分中...")
    device = "cuda" if torch.cuda.is_available() else "cpu"

    global _LABSE_CACHE
    if CACHE_MODELS and _LABSE_CACHE is not None:
        labse_model = _LABSE_CACHE
    else:
        labse_model = SentenceTransformer(state['labse_model_path'], device=device)
        if CACHE_MODELS:
            _LABSE_CACHE = labse_model
    
    original = state['original_text']
    state['qwen_labse_score'] = compute_labse_similarity(original, state['qwen_translation'], labse_model)
    state['hy_labse_score'] = compute_labse_similarity(original, state['hy_translation'], labse_model)
    print(f"  Qwen: {state['qwen_labse_score']:.3f}, HY: {state['hy_labse_score']:.3f}")

    if not CACHE_MODELS:
        del labse_model
        gc.collect()
        torch.cuda.empty_cache()
    return state


def select_best_translation(state: AgentState) -> AgentState:
    print("🏆 选择最佳翻译...")
    if state['qwen_labse_score'] >= state['hy_labse_score']:
        state['final_translation'] = state['qwen_translation']
        state['best_model'] = "Qwen"
    else:
        state['final_translation'] = state['hy_translation']
        state['best_model'] = "HY"
    print(f"  ✅ {state['best_model']} 选中")
    return state


def quality_check(state: AgentState) -> Literal["acceptable", "needs_review"]:
    score_diff = abs(state['qwen_labse_score'] - state['hy_labse_score'])
    threshold = 0.02
    if score_diff < threshold:
        print(f"⚠️ 分数差距({score_diff:.3f})小，进入人工审核")
        return "needs_review"
    print("✅ 分数差距足够大，自动结束")
    return "acceptable"


def human_review_node(state: AgentState) -> AgentState:
    print("👤 人工审核")
    print("原文:", state['original_text'])
    print("[Q] Qwen译文:", state['qwen_translation'])
    print("[H] HY译文:", state['hy_translation'])
    choice = input("选 Q 还是 H ? (回车默认选更高分): ").strip().lower()

    if choice == 'q':
        state['final_translation'] = state['qwen_translation']
        state['best_model'] = "Qwen (人工确认)"
    elif choice == 'h':
        state['final_translation'] = state['hy_translation']
        state['best_model'] = "HY (人工确认)"
    else:
        if state['qwen_labse_score'] >= state['hy_labse_score']:
            state['final_translation'] = state['qwen_translation']
            state['best_model'] = "Qwen (人工确认)"
        else:
            state['final_translation'] = state['hy_translation']
            state['best_model'] = "HY (人工确认)"
    return state


def build_translation_graph():
    workflow = StateGraph(AgentState)
    workflow.add_node("both_translator", translate_with_both)
    workflow.add_node("labse_evaluator", evaluate_with_labse)
    workflow.add_node("selector", select_best_translation)
    workflow.add_node("human_review", human_review_node)

    workflow.set_entry_point("both_translator")
    workflow.add_edge("both_translator", "labse_evaluator")
    workflow.add_edge("labse_evaluator", "selector")
    workflow.add_conditional_edges(
        "selector",
        quality_check,
        {
            "acceptable": END,
            "needs_review": "human_review",
        },
    )
    workflow.add_edge("human_review", END)
    return workflow.compile()


def run_translation_pipeline(graph, text: str) -> AgentState:
    state = AgentState(
        original_text=text,
        qwen_translation="",
        hy_translation="",
        qwen_labse_score=0.0,
        hy_labse_score=0.0,
        final_translation="",
        best_model="",
        qwen_model_path=QWEN_MODEL_PATH,
        hy_model_path=HY_MODEL_PATH,
        labse_model_path=LABSE_MODEL,
    )
    result = graph.invoke(state)
    print(f"最终: {result['final_translation']} ({result['best_model']})")
    return result


def main():
    graph = build_translation_graph()
    with open(INPUT_FILE, 'r', encoding='utf-8') as fin, open(OUTPUT_FILE, 'w', encoding='utf-8') as fout:
        for line in fin:
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            content = item.get("content")
            if not content:
                fout.write(json.dumps(item, ensure_ascii=False) + "\n")
                continue
            result = run_translation_pipeline(graph, content)
            item.update({
                "output": result['final_translation'],
                "best_model": result['best_model'],
                "qwen_labse_score": result['qwen_labse_score'],
                "hy_labse_score": result['hy_labse_score'],
                "hy_translation": result['hy_translation'],
            })
            fout.write(json.dumps(item, ensure_ascii=False) + "\n")
    print("批量翻译完成，结果写至", OUTPUT_FILE)


if __name__ == "__main__":
    main()
