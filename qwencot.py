import argparse
import json
import re
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

try:
    import fugashi  # type: ignore
except Exception:  # pragma: no cover
    fugashi = None


DEFAULT_MODEL_PATH = "/home/cyw/Qwen2.5-0.5B"
DEFAULT_INPUT_DIR = "/home/cyw/pro/train_data_2"  # 这个目录下应该有 test1.jsonl, test2.jsonl 等文件
DEFAULT_OUTPUT_FILE = "/home/cyw/pro/train_data_2/outs/out_qwencot.jsonl"


def parse_range(range_str: str) -> tuple[int, int]:
    try:
        start, end = map(int, range_str.split(","))
        if start < 1 or end < 1 or start > end:
            raise ValueError
        return start, end
    except Exception as exc:
        raise argparse.ArgumentTypeError(
            "Range must be like '1,5' meaning test1.jsonl..test5.jsonl"
        ) from exc


def _extract_json_object(text: str) -> dict | None:
    """Best-effort: extract the first top-level JSON object from text."""
    if not text:
        return None
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return None
    candidate = text[start : end + 1].strip()
    try:
        return json.loads(candidate)
    except Exception:
        return None


_ZH_RE = re.compile(r"(?:中文译文|中文翻译)\s*[:：]\s*(.+)", re.DOTALL)


def _extract_zh_fallback(text: str) -> str | None:
    if not text:
        return None
    m = _ZH_RE.search(text)
    if m:
        # take first non-empty line(s)
        val = m.group(1).strip()
        # stop at next section header if present
        for stop in ["切分", "词汇", "单词", "语法", "JSON", "{"]:
            idx = val.find(stop)
            if idx > 0:
                val = val[:idx].strip()
        return val.strip().strip('"')
    return None


def build_messages(*, content: str, context: str) -> list[dict]:
    """Few-shot + strict JSON output for reliable parsing."""

    system = (
        "你是专业的日文→中文字幕翻译助手，同时具备日语语言学分析能力。\n"
        "要求：只输出一个 JSON 对象，不要输出任何额外文字/Markdown/代码块。\n"
        "JSON 必须包含且仅包含这些字段：\n"
        "- segmentation: 字符串数组，对日文原句进行合理切分（短语/词块），至少 1 项。\n"
        "- vocab_ja_zh: 字符串数组，列出你有把握的日中词汇对照（格式：日文->中文）。\n"
        "- grammar_ja_zh: 字符串数组，列出相关的日中语法/表达对照（简短）。\n"
        "- zh_translation: 字符串，最终中文译文（口语化、符合字幕风格，尽量简洁自然），禁止为空。\n"
        "硬性规则：\n"
        "1) zh_translation 必须是中文，不要输出日文假名（ひらがな/カタカナ）。\n"
        "2) 不要把内容原样复制回 zh_translation。\n"
        "3) 遇到说话人标签如（レイン）（ユーク）请保留标签原样，不要翻译人名。\n"
        "4) context 仅作参考，不相关时忽略。\n"
        "注意：如果没有把握，vocab_ja_zh/grammar_ja_zh 可以给空数组，但 zh_translation 必须给出你的最佳翻译。"
    )

    example_user = (
        "【示例】\n"
        "Context: 朋友在餐厅点餐。\n"
        "Content: ちょっと待って、今行く。"
    )

    example_assistant = {
        "segmentation": ["ちょっと待って", "今行く"],
        "vocab_ja_zh": ["ちょっと->有点/稍微", "待って->等一下", "今->现在", "行く->去/过去"],
        "grammar_ja_zh": ["命令/请求形『Vて』：待って→等一下", "省略主语的口语：今行く→我现在就过去"],
        "zh_translation": "等一下，我现在就过去。",
    }

    user = (
        "Context: " + (context.strip()[:120] if context else "") + "\n"
        "Content: " + content.strip() + "\n"
    )

    return [
        {"role": "system", "content": system},
        {"role": "user", "content": example_user},
        {"role": "assistant", "content": json.dumps(example_assistant, ensure_ascii=False)},
        {"role": "user", "content": user},
    ]


def build_retry_messages(*, content: str, context: str) -> list[dict]:
    """Retry prompt: translation-only for robustness."""
    system = (
        "你是专业的日文→中文字幕翻译助手。\n"
        "只输出最终【中文译文】一行，不要输出日文，不要解释。\n"
        "遇到（レイン）（ユーク）等说话人标签请保留标签原样，不要翻译人名。\n"
        "字幕风格：口语化、简洁、自然。"
    )
    user = (
        "Context: " + (context.strip()[:120] if context else "") + "\n"
        "Content: " + content.strip() + "\n"
        "中文译文："
    )
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


_JP_KANA_RE = re.compile(r"[\u3040-\u309F\u30A0-\u30FF]")


def _contains_kana(text: str) -> bool:
    return bool(text and _JP_KANA_RE.search(text))


def _looks_like_json(text: str) -> bool:
    t = (text or "").lstrip()
    return t.startswith("{") and t.rstrip().endswith("}")


def _is_bad_translation(zh: str | None, *, content: str) -> bool:
    if zh is None:
        return True
    z = zh.strip()
    if not z:
        return True
    if _looks_like_json(z):
        return True
    if z == content.strip():
        return True
    # Still outputs Japanese kana => likely not translated.
    if _contains_kana(z):
        return True
    return False


_SFX_MAP = {
    "笑い声": "（笑声）",
    "笑": "（笑）",
    "拍手": "（掌声）",
    "ため息": "（叹气）",
    "泣き声": "（哭声）",
    "歓声": "（欢呼）",
}


def _translate_stage_direction(content: str) -> str | None:
    s = (content or "").strip()
    if not s:
        return None
    # Match full-parentheses stage directions like （笑い声） / (笑)
    if (s.startswith("（") and s.endswith("）")) or (s.startswith("(") and s.endswith(")")):
        inner = s[1:-1].strip()
        if inner in _SFX_MAP:
            return _SFX_MAP[inner]
        # generic: keep parentheses but try to Chinese-ify common suffixes
        if inner.endswith("声") and _contains_kana(inner):
            return "（声音）"
    return None


def _segment_japanese(text: str, *, tagger=None) -> list[str]:
    t = (text or "").strip()
    if not t:
        return []
    if tagger is not None:
        try:
            words = [w.surface for w in tagger(t)]
            words = [w for w in words if w.strip()]
            if words:
                return words
        except Exception:
            pass
    # fallback: split by punctuation/space
    parts = [p for p in re.split(r"[\s、。！？…]+", t) if p]
    return parts if parts else [t]


def main():
    parser = argparse.ArgumentParser(description="Qwen CoT translation (JA->ZH) for jsonl batches")
    parser.add_argument("--model", default=DEFAULT_MODEL_PATH, help="Local model path or HF id")
    parser.add_argument("--input-dir", default=DEFAULT_INPUT_DIR, help="Directory containing test{i}.jsonl")
    parser.add_argument("--output", default=DEFAULT_OUTPUT_FILE, help="Output jsonl path")
    parser.add_argument("--range", dest="range_", type=parse_range, default=None, help="e.g. 1,5")
    parser.add_argument("--max-new-tokens", type=int, default=384)
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--top-p", type=float, default=0.9)
    parser.add_argument("--repetition-penalty", type=float, default=1.05)
    parser.add_argument("--no-sample", action="store_true", help="Disable sampling (greedy decode)")
    parser.add_argument("--retry", type=int, default=1, help="Retry count when translation looks bad")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_file = Path(args.output)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    if args.range_ is None:
        user_input = input("请输入要处理的 test 文件范围（例如 1,5 表示 test1.jsonl 到 test5.jsonl）：").strip()
        start, end = parse_range(user_input)
    else:
        start, end = args.range_

    print("正在加载 Qwen 模型...")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    )
    model.eval()
    print("模型加载完成！")

    tagger = None
    if fugashi is not None:
        try:
            tagger = fugashi.Tagger()
        except Exception:
            tagger = None

    all_data: list[dict] = []
    for i in range(start, end + 1):
        file_path = input_dir / f"test{i}.jsonl"
        if not file_path.exists():
            print(f"警告: 文件 {file_path.name} 不存在，已跳过。")
            continue
        print(f"正在读取文件: {file_path.name}")
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    all_data.append(json.loads(line))
                except json.JSONDecodeError:
                    print(f"警告: 文件 {file_path.name} 中有无效的 JSON 行，已跳过。")

    print(f"共读取 {len(all_data)} 条数据")
    print("开始翻译...")

    for idx, data in enumerate(all_data, 1):
        content = (data.get("content") or "").strip()
        context = (data.get("context") or "").strip()

        if not content:
            continue

        print(f"正在翻译第 {idx}/{len(all_data)} 行: {content[:30]}...")

        # Fast-path: common stage directions
        sfx = _translate_stage_direction(content)
        if sfx is not None:
            seg = _segment_japanese(content, tagger=tagger)
            data["cot_full"] = ""
            data["cot_json"] = {
                "segmentation": seg,
                "vocab_ja_zh": [],
                "grammar_ja_zh": [],
                "zh_translation": sfx,
            }
            data["output"] = sfx
            print(f"✓ 完成(音效): {content} -> {data['output']}")
            continue

        seg = _segment_japanese(content, tagger=tagger)

        def _gen_from_messages(msgs: list[dict]) -> str:
            prompt_text_local = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
            model_inputs_local = tokenizer([prompt_text_local], return_tensors="pt").to(model.device)
            with torch.inference_mode():
                generated_ids_local = model.generate(
                    **model_inputs_local,
                    max_new_tokens=args.max_new_tokens,
                    do_sample=not args.no_sample,
                    temperature=args.temperature,
                    top_p=args.top_p,
                    repetition_penalty=args.repetition_penalty,
                    eos_token_id=tokenizer.eos_token_id,
                    pad_token_id=tokenizer.eos_token_id,
                )
            new_token_ids_local = [
                output_ids[len(input_ids) :]
                for input_ids, output_ids in zip(model_inputs_local["input_ids"], generated_ids_local)
            ]
            return tokenizer.batch_decode(new_token_ids_local, skip_special_tokens=True)[0].strip()

        raw = _gen_from_messages(build_messages(content=content, context=context))

        cot_json = _extract_json_object(raw) if raw else None
        zh_translation = None
        if isinstance(cot_json, dict):
            zh_translation = cot_json.get("zh_translation")

        if zh_translation is None:
            zh_translation = _extract_zh_fallback(raw)

        # Normalize/patch cot_json fields for stability
        if not isinstance(cot_json, dict):
            cot_json = {
                "segmentation": seg,
                "vocab_ja_zh": [],
                "grammar_ja_zh": [],
                "zh_translation": "",
            }
        else:
            if not cot_json.get("segmentation"):
                cot_json["segmentation"] = seg
            if cot_json.get("vocab_ja_zh") is None:
                cot_json["vocab_ja_zh"] = []
            if cot_json.get("grammar_ja_zh") is None:
                cot_json["grammar_ja_zh"] = []

        # Retry when translation is empty / JSON dumped / still Japanese
        retry_used = False
        if _is_bad_translation(zh_translation, content=content):
            for _ in range(max(0, args.retry)):
                retry_used = True
                raw_retry = _gen_from_messages(build_retry_messages(content=content, context=context))
                cand = raw_retry.strip().strip('"').strip()
                if not _is_bad_translation(cand, content=content):
                    zh_translation = cand
                    data["cot_full_retry"] = raw_retry
                    break

        if _is_bad_translation(zh_translation, content=content):
            # final fallback: don't write raw JSON into output
            zh_translation = content

        cot_json["zh_translation"] = str(zh_translation).strip()

        data["cot_full"] = raw
        data["cot_json"] = cot_json
        if retry_used and "cot_full_retry" not in data:
            data["cot_full_retry"] = ""
        data["output"] = cot_json["zh_translation"].strip()

        print(f"✓ 完成: {content[:16]}... -> {data['output'][:16]}...")

    mode = "a" if output_file.exists() else "w"
    with open(output_file, mode, encoding="utf-8") as f:
        for data in all_data:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")

    print(f"\n全部翻译任务已完成！结果已保存到: {output_file}")


if __name__ == "__main__":
    main()
