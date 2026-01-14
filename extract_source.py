
import json
from pathlib import Path

def main():
    """
    从指定的 JSONL 文件中提取 'input' 字段，并将其保存到指定的文本文件中。
    输入和输出路径都将通过交互式提示获取。
    """
    # 获取输入文件路径
    default_in_path = "train_data/captions_0429_test.jsonl"
    in_path_str = input(f"请输入源 JSONL 文件路径 (回车默认: {default_in_path}): ").strip()
    in_path = Path(in_path_str or default_in_path)

    if not in_path.exists():
        print(f"错误: 输入文件不存在: {in_path}")
        return

    # 获取输出文件路径
    default_out_path = "test.txt"
    out_path_str = input(f"请输入目标 TXT 文件名 (回车默认: {default_out_path}): ").strip()
    out_path = Path(out_path_str or default_out_path)

    print(f"正在从 {in_path} 提取原文...")

    try:
        count = 0
        with open(in_path, "r", encoding="utf-8") as f_in, open(out_path, "w", encoding="utf-8") as f_out:
            for line in f_in:
                line = line.strip()
                if not line:
                    continue
                
                try:
                    data = json.loads(line)
                    # 检查 'input' 键是否存在
                    if "input" in data:
                        f_out.write(data["input"] + "\n")
                        count += 1
                    else:
                        print(f"警告: 在行 '{line}' 中未找到 'input' 键，已跳过。")

                except json.JSONDecodeError:
                    print(f"警告: 无法解析行 '{line}' 为 JSON，已跳过。")
        
        print(f"成功！已提取 {count} 行原文并保存到 {out_path}")

    except IOError as e:
        print(f"文件操作失败: {e}")

if __name__ == "__main__":
    main()
