import json
from pathlib import Path
from openai import OpenAI

# 配置 DeepSeek API
API_KEY = "sk-sbexgswzdmgwayfqtteskfkwfzorfkgrkvvfuyoxtfgqqbcp"
BASE_URL = "https://api.siliconflow.cn/v1"
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


def clean_and_translate(japanese_text: str, context: str, channel: str):
    # 优化提示词
    system_prompt = (
        "You are an expert translator specializing in TV subtitles.\n"
        "Tasks:\n"
        "1. Translate the provided 'content' field from Japanese to fluent, natural, and context-rich English.\n"
        "2. Respect the 'context' and 'channel' information for better cultural and contextual translation.\n"
        "3. Output JSON format strictly: {\"instruction\": \"Translate to fluent English\","
        " \"input\": \"JAPANESE_TEXT\", \"output\": \"ENGLISH_TRANSLATION\"}\n"
        "Context provides background information about the sentence, while channel represents the domain.\n"
        "Use this information as guidance for generating accurate translations."
    )

    # 构造请求：
    user_input = {
        "context": context,
        "channel": channel,
        "content": japanese_text,
    }

    try:
        # 调用DeepSeek API
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3.2",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": json.dumps(user_input)},
            ],
            temperature=0.2,
        )
        # 从响应中解析结果
        result = response.choices[0].message.content
        return json.loads(result)
    except Exception as e:
        print(f"Error while processing input: '{japanese_text[:10]}...': {e}")
        return None


def get_last_processed_line(output_path: Path):
    """
    返回 output_path 中 output 字段有内容的行数
    """
    if not output_path.exists():
        return 0
    count = 0
    with output_path.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get("output"):
                    count += 1
            except Exception:
                continue
    return count


def process_file(file_path: Path, output_path: Path, skip_existing: bool):
    # 读取所有输入行
    with file_path.open("r", encoding="utf-8") as f:
        all_lines = f.readlines()

    # 读取已翻译行数
    processed_count = get_last_processed_line(output_path)
    print(f"'{output_path.name}' 已存在，已翻译 {processed_count} 行，从第 {processed_count+1} 行继续...")

    # 以追加模式打开文件
    with output_path.open("a", encoding="utf-8") as f_out:
        for i, line in enumerate(all_lines):
            if i < processed_count:
                continue  # 跳过已翻译行

            try:
                json_data = json.loads(line)
            except json.JSONDecodeError:
                print(f"[Line {i+1}] Skipping: Not valid JSON format.")
                f_out.write(line)
                continue

            if skip_existing and json_data.get("output"):
                f_out.write(json.dumps(json_data, ensure_ascii=False) + "\n")
                continue

            raw_content = json_data.get("content", "")
            channel = json_data.get("channel", "")
            context = json_data.get("context", "")

            translated_data = clean_and_translate(
                japanese_text=raw_content,
                context=context,
                channel=channel,
            )

            if translated_data and translated_data.get("output"):
                json_data["output"] = translated_data["output"]
                print(f"[Line {i+1}] Translated")
            else:
                print(f"[Line {i+1}] Translation failed or incomplete.")
                json_data["output"] = ""

            f_out.write(json.dumps(json_data, ensure_ascii=False) + "\n")
            f_out.flush()

    print(f"完成处理: {output_path.name}")


def main():
    data_dir = Path("/home/cyw/pro/train_data_2")
    output_dir = data_dir / "trans"
    output_dir.mkdir(exist_ok=True)

    jsonl_files = [f for f in data_dir.glob("*.jsonl")
                   if f.name.startswith("20250425") or f.name.startswith("20250426")]
    jsonl_files = sorted(jsonl_files)

    # 找到最后一个已处理的文件
    last_idx = -1
    for idx, file_path in enumerate(jsonl_files):
        output_path = output_dir / f"filled{idx+1}.jsonl"
        if output_path.exists():
            last_idx = idx
        else:
            break

    # 从最后一个未完成的文件继续
    for idx, file_path in enumerate(jsonl_files):
        output_path = output_dir / f"filled{idx+1}.jsonl"
        process_file(file_path, output_path, skip_existing=True)


if __name__ == "__main__":
    main()