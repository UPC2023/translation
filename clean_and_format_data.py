import json
import re
import os

def clean_data(input_file, output_file):
    """
    Cleans the training data by:
    1. Keeping only 'instruction', 'input', 'output' fields.
    2. Removing timestamps from 'input' and 'output'.
    """
    # 确保输出目录存在
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 正则表达式用于匹配并移除 "MM/DDTHH:MM:SS " 格式的时间戳
    timestamp_regex = re.compile(r'^\d{2}/\d{2}T\d{2}:\d{2}:\d{2}\s*≫?\s*')

    cleaned_records = 0
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            try:
                data = json.loads(line)

                # 检查必要的字段是否存在
                if 'instruction' not in data or 'input' not in data or 'output' not in data:
                    continue

                # 移除 input 和 output 中的时间戳
                cleaned_input = timestamp_regex.sub('', data['input']).strip()
                cleaned_output = timestamp_regex.sub('', data['output']).strip()

                # 创建新的、干净的记录
                cleaned_record = {
                    'instruction': data['instruction'],
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
    input_jsonl = 'train_data/captions_0429_train_filled.jsonl'
    output_jsonl = 'train_data/captions_train_cleaned.jsonl'
    
    # 检查输入文件是否存在
    if not os.path.exists(input_jsonl):
        print(f"Error: Input file not found at '{input_jsonl}'")
    else:
        clean_data(input_jsonl, output_jsonl)
