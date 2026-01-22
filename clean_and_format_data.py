import json
import re
import os

def clean_data(input_file, output_file):
    """
    Cleans the training data by:
    1. Keeping only 'instruction', 'input', 'output' fields.
    2. Removing timestamps from 'input' and 'output'.
    3. Dropping records whose input/output starts with '===', 'Event ...', or schedule lines like '04/28（月）09:50:00～11:30:00'.
    4. Setting instruction to a fixed prompt: 'Translate to natural English.'.
    """
    # 确保输出目录存在
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 正则表达式用于匹配并移除 "MM/DDTHH:MM:SS " 格式的时间戳
    timestamp_regex = re.compile(r'^\d{2}/\d{2}T\d{2}:\d{2}:\d{2}\s*≫?\s*')
    meaningless_regex = re.compile(r'^\s*===')
    event_regex = re.compile(r'^\s*Event\b')
    schedule_regex = re.compile(r'^\s*\d{2}/\d{2}（.*?）\d{2}:\d{2}:\d{2}～\d{2}:\d{2}:\d{2}')

    cleaned_records = 0
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            try:
                data = json.loads(line)

                # 检查必要的字段是否存在
                if 'input' not in data or 'output' not in data:
                    continue

                raw_input = data.get('input', '')
                raw_output = data.get('output', '')

                # 丢弃无意义行：=== 开头、Event 日志、整行时间段
                if (
                    meaningless_regex.match(raw_input)
                    or meaningless_regex.match(raw_output)
                    or event_regex.match(raw_input)
                    or event_regex.match(raw_output)
                    or schedule_regex.match(raw_input)
                    or schedule_regex.match(raw_output)
                ):
                    continue

                # 移除 input 和 output 中的时间戳
                cleaned_input = timestamp_regex.sub('', raw_input).strip()
                cleaned_output = timestamp_regex.sub('', raw_output).strip()

                # 再次检查清理结果是否为空或仍为无意义行
                if (
                    not cleaned_input
                    or meaningless_regex.match(cleaned_input)
                    or event_regex.match(cleaned_input)
                    or schedule_regex.match(cleaned_input)
                ):
                    continue
                if (
                    meaningless_regex.match(cleaned_output)
                    or event_regex.match(cleaned_output)
                    or schedule_regex.match(cleaned_output)
                ):
                    cleaned_output = ''

                # 创建新的、干净的记录
                cleaned_record = {
                    'instruction': 'Translate to natural English.',
                    'input': cleaned_input,
                    'output': cleaned_output
                }

                # 写入新文件，确保每行是一个独立的 JSON 对象
                outfile.write(json.dumps(cleaned_record, ensure_ascii=False) + '\n')
                cleaned_records += 1
            except json.JSONDecodeError:
                print(f"Skipping line due to JSON decoding error: {line.strip()}")
                continue

    print(f"Successfully cleaned {cleaned_records} records.")
    print(f"Cleaned data saved to: {output_file}")

if __name__ == '__main__':
    # 定义输入和输出文件路径
    # 注意：我们从 'pro' 目录运行，所以使用相对路径
    input_jsonl = input('请输入待清理的 jsonl 文件路径: ').strip()
    output_jsonl = input('请输入保存清理数据的 jsonl 文件路径: ').strip()
    
    # 检查输入文件是否存在
    if not os.path.exists(input_jsonl):
        print(f"Error: Input file not found at '{input_jsonl}'")
    else:
        clean_data(input_jsonl, output_jsonl)
