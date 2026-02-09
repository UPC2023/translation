#!/usr/bin/env python
import sys
import os
import json
from typing import Any, Dict, List


def clean_output(text: Any) -> str:
    """按照新规则清洗 output 字段：
    如果 output 内容中包含 \n，则按 \n 分割句子：
    - 先提取第一个包含双引号 (") 的句子；
    - 如果没有，则提取第一个有英文且不含 "translation"/"japanese" 的句子；
    - 如果都没有，返回空字符串；
    如果不包含 \n，直接返回 strip 后的内容。
    """
    if text is None:
        return ""
    if not isinstance(text, str):
        text = str(text)

    raw = text.strip("\n")
    if not raw.strip():
        return ""

    # 如果不包含 \n，直接返回 raw
    if "\n" not in raw:
        return raw

    # 包含 \n，按 \n 分割句子
    sentences = [s.strip() for s in raw.split("\n") if s.strip()]

    # 先找包含双引号的句子
    for sent in sentences:
        if '"' in sent:
            return sent

    # 如果没有双引号的句子，则找第一句有英文且不含 "translation"/"japanese" 的句子
    for sent in sentences:
        has_english = any(("a" <= c <= "z") or ("A" <= c <= "Z") for c in sent)
        if not has_english:
            continue

        lower = sent.lower()
        if "japanese" in lower or "translation" in lower:
            continue

        return sent

    return ""  # 如果都没有，返回空


def process_jsonl(path: str) -> None:
    lines_out: List[str] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                lines_out.append(line)
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                # 保留原始行，避免破坏文件
                lines_out.append(line)
                continue
            obj["output"] = clean_output(obj.get("output", ""))
            lines_out.append(json.dumps(obj, ensure_ascii=False) + "\n")

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines_out)


def process_json_array(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"[WARN] 无法解析 JSON 文件: {path}")
            return
    if not isinstance(data, list):
        print(f"[WARN] JSON 根不是数组: {path}")
        return

    for obj in data:
        if isinstance(obj, dict):
            obj["output"] = clean_output(obj.get("output", ""))

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        print("用法: python clean_outputs.py <file1> [file2 ...]")
        return 1

    for path in argv[1:]:
        if not os.path.exists(path):
            print(f"[WARN] 文件不存在: {path}")
            continue
        if path.lower().endswith(".jsonl"):
            print(f"[INFO] 处理 JSONL: {path}")
            process_jsonl(path)
        elif path.lower().endswith(".json"):
            print(f"[INFO] 处理 JSON 数组: {path}")
            process_json_array(path)
        else:
            print(f"[WARN] 不支持的扩展名, 跳过: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
