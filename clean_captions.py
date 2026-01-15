import argparse
import json
import re
from typing import Dict, Iterable, Tuple

# Patterns and constants
TIMESTAMP_RE = re.compile(r"^\s*\d{2}/\d{2}T\d{2}:\d{2}:\d{2}\s*(?:[≥≫»>]+)?\s*")
HTML_TAG_RE = re.compile(r"<[^>]+>")
META_LINE_RE = re.compile(r"^===|=== language|Caption:", re.IGNORECASE)
WHITESPACE_RE = re.compile(r"\s+")

# Characters that routinely appear as noise in the provided dumps
NOISE_CHARS = ["", "", "▽", "≫", "【", "】", "「", "」", "…"]


def remove_control_chars(text: str) -> str:
    # Keep printable characters; drop control/private-use codepoints
    return "".join(ch for ch in text if ch.isprintable())


def strip_timestamp(text: str) -> str:
    return TIMESTAMP_RE.sub("", text)


def strip_noise(text: str) -> str:
    cleaned = text
    for ch in NOISE_CHARS:
        cleaned = cleaned.replace(ch, " ")
    cleaned = HTML_TAG_RE.sub(" ", cleaned)
    cleaned = strip_timestamp(cleaned)
    cleaned = remove_control_chars(cleaned)
    cleaned = WHITESPACE_RE.sub(" ", cleaned).strip()
    return cleaned


def is_meta(text: str) -> bool:
    return META_LINE_RE.search(text) is not None


def quality_bad(src: str, tgt: str) -> bool:
    # Drop very short or punctuation-only outputs
    letters_digits = re.sub(r"[^\w]+", "", tgt)
    if len(letters_digits) < 3:
        return True
    # If source and target identical (case/punct insensitive), drop
    if normalize_for_compare(src) == normalize_for_compare(tgt):
        return True
    return False


def normalize_for_compare(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "", text).lower()


def load_jsonl(path: str) -> Iterable[dict]:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def build_filled_map(path: str) -> Dict[str, dict]:
    return {row.get("id", ""): row for row in load_jsonl(path) if row.get("id")}


def clean_pair(src_row: dict, filled_row: dict) -> Tuple[str, str]:
    raw_input = src_row.get("input", "")
    raw_output = filled_row.get("output", "")
    if not raw_output:
        return "", ""
    if is_meta(raw_input) or is_meta(raw_output):
        return "", ""
    input_clean = strip_noise(raw_input)
    output_clean = strip_noise(raw_output)
    return input_clean, output_clean


def process(src_path: str, filled_path: str, out_path: str) -> None:
    filled_map = build_filled_map(filled_path)
    seen_inputs = set()

    with open(out_path, "w", encoding="utf-8") as out_f:
        for src_row in load_jsonl(src_path):
            rid = src_row.get("id")
            if not rid:
                continue
            filled_row = filled_map.get(rid)
            if not filled_row:
                continue
            src_text, tgt_text = clean_pair(src_row, filled_row)
            if not src_text or not tgt_text:
                continue
            if quality_bad(src_text, tgt_text):
                continue
            # Deduplicate on cleaned source text
            key = src_text
            if key in seen_inputs:
                continue
            seen_inputs.add(key)
            out_obj = {
                "id": rid,
                "source": src_text,
                "target": tgt_text,
            }
            out_f.write(json.dumps(out_obj, ensure_ascii=False) + "\n")


def main() -> None:
    # Defaults so running `python clean_captions.py` just works in this repo
    default_src = "train_data/captions_0429_test.jsonl"
    default_filled = "train_data/captions_0429_test_filled.jsonl"
    default_out = "train_data/captions_0429_test_cleaned.jsonl"

    parser = argparse.ArgumentParser(description="Clean caption JSONL pairs.")
    parser.add_argument("--src", default=default_src, help="Path to source jsonl (outputs empty).")
    parser.add_argument("--filled", default=default_filled, help="Path to filled jsonl with translations.")
    parser.add_argument("--out", default=default_out, help="Path to cleaned output jsonl.")
    args = parser.parse_args()
    process(args.src, args.filled, args.out)


if __name__ == "__main__":
    main()
