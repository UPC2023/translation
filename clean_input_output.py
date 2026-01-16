import argparse
import json
import re
from pathlib import Path
from typing import Iterable, TextIO

# Matches leading timestamps like 04/28T09:50:02
TIMESTAMP_RE = re.compile(r"^\d{2}/\d{2}T\d{2}:\d{2}:\d{2}\s*")
# Detects presence of Japanese characters (Hiragana, Katakana, Kanji blocks)
JAPANESE_CHAR_RE = re.compile(r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff]")


def strip_timestamp(text: str) -> str:
    """Remove a leading timestamp like 04/28T09:50:02 from the text."""
    return TIMESTAMP_RE.sub("", text.strip())


def has_japanese(text: str) -> bool:
    """Return True if the text contains at least one Japanese character."""
    return bool(JAPANESE_CHAR_RE.search(text))


def process_stream(fin: TextIO) -> Iterable[dict]:
    """Yield cleaned records with only input/output fields."""
    for line in fin:
        line = line.strip()
        if not line:
            continue
        record = json.loads(line)
        raw_input = record.get("input", "")
        cleaned_input = strip_timestamp(raw_input)

        # Drop entries that have no Japanese content after cleaning.
        if not has_japanese(cleaned_input):
            continue

        yield {
            "input": cleaned_input,
            "output": record.get("output", ""),
        }


def prompt_path(prompt: str, fallback: str | None = None, allow_empty: bool = False) -> str:
    """Ask user for a path if it was not provided via CLI."""
    if fallback:
        return fallback
    value = ""
    while not value:
        value = input(prompt).strip()
        if value or allow_empty:
            break
    return value


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Clean JSONL: strip timestamps and drop non-Japanese inputs.",
        add_help=True,
    )
    parser.add_argument("src", nargs="?", help="Source JSONL file")
    parser.add_argument("dst", nargs="?", help="Output JSONL file")
    args = parser.parse_args()

    src_path = Path(prompt_path("Source JSONL path: ", args.src))
    dst_raw = prompt_path("Output JSONL path (leave blank to default): ", args.dst, allow_empty=True)
    dst_path = Path(dst_raw) if dst_raw else src_path.with_name(f"{src_path.stem}.cleaned.jsonl")

    with open(src_path, "r", encoding="utf-8") as fin, open(dst_path, "w", encoding="utf-8") as fout:
        for rec in process_stream(fin):
            fout.write(json.dumps(rec, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
