import argparse
import json
from pathlib import Path
from openai import OpenAI

# 1. 配置 DeepSeek API（保持你的 Key）
API_KEY = "sk-sbexgswzdmgwayfqtteskfkwfzorfkgrkvvfuyoxtfgqqbcp"
BASE_URL = "https://api.siliconflow.cn/v1"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


def clean_and_translate(japanese_text: str):
    system_prompt = (
        "You are an expert translator for TV subtitles.\n"
        "Task:\n"
        "1. Translate the Japanese text to natural, context-aware English.\n"
        "2. Infer omitted subjects (I/You/He/She/They) based on common speech patterns.\n"
        "3. Output JSON format strictly: {\"instruction\": \"Translate to natural English.\","
        " \"input\": \"JAPANESE_TEXT\", \"output\": \"ENGLISH_TEXT\"}"
    )

    try:
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Japanese Input: {japanese_text}"},
            ],
            response_format={"type": "json_object"},
            temperature=0.1,
        )
        result = response.choices[0].message.content
        return json.loads(result)
    except Exception as e:
        print(f"Error processing {japanese_text[:10]}...: {e}")
        return None


def count_processed_lines(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def process_file(input_path: Path, output_path: Path, resume: bool):
    processed_existing = count_processed_lines(output_path) if resume else 0
    mode = "a" if processed_existing else "w"

    print(
        f"开始清洗数据（调用 DeepSeek）: {input_path} -> {output_path}"
        + (f"，从第 {processed_existing + 1} 行继续" if processed_existing else "")
    )

    with input_path.open("r", encoding="utf-8") as inf, output_path.open(mode, encoding="utf-8") as outf:
        for i, line in enumerate(inf, start=1):
            if i <= processed_existing:
                continue

            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                print(f"[{i}] 跳过：非 JSON 行")
                continue

            raw_japanese = str(data.get("input", ""))

            clean_data = clean_and_translate(raw_japanese)

            if clean_data and clean_data.get("output"):
                data_to_write = clean_data
                print(f"[{i}] 已处理: {clean_data.get('output', '')}")
            else:
                data_to_write = {
                    "instruction": "Translate to natural English.",
                    "input": raw_japanese,
                    "output": raw_japanese,
                }
                print(f"[{i}] 翻译失败，写入原文")

            json.dump(data_to_write, outf, ensure_ascii=False)
            outf.write("\n")
            outf.flush()

    print(f"完成！数据已保存至 {output_path}")


def main():
    parser = argparse.ArgumentParser(description="调用 DeepSeek 清洗翻译 JSONL 数据")
    parser.add_argument("--input", help="输入 JSONL 文件路径，需含 input 字段")
    parser.add_argument("--no-resume", action="store_true", help="不从已有输出续跑，直接覆盖")
    args = parser.parse_args()

    input_path_str = args.input or input("请输入输入文件路径: ").strip()
    input_path = Path(input_path_str)
    if not input_path.is_file():
        raise FileNotFoundError(f"找不到输入文件: {input_path}")

    output_path = input_path.with_name(f"{input_path.stem}_filled{input_path.suffix}")
    resume = not args.no_resume
    if resume and output_path.exists():
        answer = input(f"发现已有输出 {output_path}，是否续跑? (y/n): ").lower()
        if answer not in ["y", "yes", "是", "好", "1"]:
            resume = False

    if not resume and output_path.exists():
        print(f"覆盖已存在的文件: {output_path}")
        output_path.unlink()

    process_file(input_path, output_path, resume)


if __name__ == "__main__":
    main()