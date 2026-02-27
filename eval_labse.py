import argparse
from typing import List, Tuple
import torch
from sentence_transformers import SentenceTransformer, util
import os
import json
import math
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

def _read_non_empty_lines(path: str, key: str) -> List[Tuple[int, str]]:
    """Read lines; support both JSON array and JSONL formats.

    key: the field name to read.
    """
    lines: List[Tuple[int, str]] = []

    # 判断文件类型
    is_jsonl = path.lower().endswith(".jsonl")
    is_json_array = path.lower().endswith(".json")

    if is_json_array:
        # JSON数组格式: [{...}, {...}, ...]
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    for idx, obj in enumerate(data, 1):
                        if isinstance(obj, dict):
                            text = obj.get(key, "")
                            if text.strip() != "":
                                lines.append((idx, text))
            except json.JSONDecodeError as e:
                raise ValueError(f"无法解析JSON文件 {path}: {e}")
    elif is_jsonl:
        # JSONL格式: 每行一个JSON对象
        with open(path, "r", encoding="utf-8") as f:
            for line_no, raw in enumerate(f, 1):
                text = raw.rstrip("\n")
                if text.strip() == "":
                    continue
                try:
                    obj = json.loads(text)
                    text = obj.get(key, "")
                except json.JSONDecodeError:
                    continue
                if text.strip() == "":
                    continue
                lines.append((line_no, text))
    else:
        # 普通文本格式
        with open(path, "r", encoding="utf-8") as f:
            for line_no, raw in enumerate(f, 1):
                text = raw.rstrip("\n")
                if text.strip() == "":
                    continue
                lines.append((line_no, text))

    return lines


def _md_escape_cell(text: str) -> str:
    # Markdown table cell-safe.
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("\r", " ").replace("\n", "<br>")


def _ensure_path(name: str, path: str, force_ask: bool = False) -> str:
    """If path does not exist or force_ask=True, prompt user for a path."""
    if force_ask or not os.path.exists(path):
        print(f"[警告] {name}文件不存在: {path}")
        prompt = f"请重新输入{name}文件路径 : "
        entered = input(prompt).strip()
        if entered:
            path = entered
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    return path


def _prompt_name(label: str, default: str) -> str:
    entered = input(f"请为{label}起一个名称 (当前: {default}): ").strip()
    return entered or default


def main() -> int:
    parser = argparse.ArgumentParser(
        description="使用 LaBSE 计算日语原文与英文译文的语义相似度，可选择单个或对比评分。"
    )
    parser.add_argument("--file", default="outqw.txt", help="翻译文件路径 (默认值，用于非交互)")
    parser.add_argument("--out", default="labse_report.md", help="输出 Markdown 报告文件 (默认值，用于非交互)")
    parser.add_argument("--model", default="sentence-transformers/LaBSE", help="Sentence-Transformers 模型")
    parser.add_argument("--device", default="auto", choices=["auto", "cpu", "cuda"], help="推理设备")
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--no-prompt", action="store_true", help="跳过交互，直接使用命令行提供的路径与名称")
    parser.add_argument("--single", action="store_true", help="单个评分模式")
    parser.add_argument("--name1", default="模型1", help="目标1名称")
    parser.add_argument("--name2", default="模型2", help="目标2名称")
    args = parser.parse_args()

    # 默认交互；如需无交互可加 --no-prompt。
    if args.no_prompt:
        path1 = _ensure_path("文件", args.file)
        single = args.single
        name1 = args.name1
        name2 = args.name2 if not single else ""
        field1 = "output" if single else "output"
        field2 = "" if single else "tv_translation"
        out_path = args.out if args.out.lower().endswith(".md") else args.out + ".md"
    else:
        path1_in = input(f"请输入译文文件路径 (回车默认: {args.file}): ").strip()
        path1 = path1_in or args.file
        path1 = _ensure_path("文件", path1)

        mode_in = input("选择模式: 1. 单个评分 2. 对比评分 (默认2): ").strip()
        single = mode_in == "1"

        if single:
            field1_in = input("翻译字段名 (默认 output): ").strip()
            field1 = field1_in or "output"
            name1 = _prompt_name("翻译", args.name1)
            name2 = ""
            field2 = ""
        else:
            field1_in = input("第一个翻译字段名 (默认 output): ").strip()
            field1 = field1_in or "output"
            name1 = _prompt_name("第一个翻译", args.name1)

            field2_in = input("第二个翻译字段名 (默认 output2): ").strip()
            field2 = field2_in or "output2"
            name2 = _prompt_name("第二个翻译", args.name2)

        out_in = input(f"请输入输出报告文件名 (默认: {args.out}, 自动补 .md): ").strip()
        out_path = out_in or args.out
        if not out_path.lower().endswith(".md"):
            out_path += ".md"

    device = args.device
    if device == "auto":
        device = "cuda" if torch.cuda.is_available() else "cpu"

    print(f"--- 正在加载 LaBSE 模型: {args.model} (device={device}) ---")
    st_model = SentenceTransformer(args.model, device=device)
    print("开始评测...\n")

    # 原文直接取自译文 jsonl 的 content 字段
    src_lines = _read_non_empty_lines(path1, "content")
    qwen_lines = _read_non_empty_lines(path1, field1)
    google_lines = _read_non_empty_lines(path1, field2) if field2 else []

    n = max(len(src_lines), len(qwen_lines), len(google_lines) if google_lines else len(qwen_lines))
    if len(src_lines) != len(qwen_lines) or (google_lines and len(qwen_lines) != len(google_lines)):
        print(
            "[WARN] 文件非空行数不一致："
            f"src={len(src_lines)}, {name1}={len(qwen_lines)}" + (f", {name2}={len(google_lines)}" if google_lines else "") + "。将按顺序对齐到最大长度。"
        )

    aligned: List[Tuple[int, str, str, str]] = []
    valid_src: List[str] = []
    valid_qwen: List[str] = []
    valid_google: List[str] = []
    valid_pos: List[int] = []

    for i in range(n):
        _, src = src_lines[i] if i < len(src_lines) else (0, "")
        _, qwen = qwen_lines[i] if i < len(qwen_lines) else (0, "")
        _, google = google_lines[i] if i < len(google_lines) else (0, "")
        aligned.append((i + 1, src, qwen, google))
        if src.strip() != "" and qwen.strip() != "" and (not google_lines or google.strip() != ""):
            valid_pos.append(i)
            valid_src.append(src)
            valid_qwen.append(qwen)
            if google_lines:
                valid_google.append(google)

    # 批量编码，速度更快
    if valid_src:
        emb_src = st_model.encode(
            valid_src,
            convert_to_tensor=True,
            batch_size=args.batch_size,
            show_progress_bar=True,
            normalize_embeddings=True,
        )
        emb_qwen = st_model.encode(
            valid_qwen,
            convert_to_tensor=True,
            batch_size=args.batch_size,
            show_progress_bar=True,
            normalize_embeddings=True,
        )
        if valid_google:
            emb_google = st_model.encode(
                valid_google,
                convert_to_tensor=True,
                batch_size=args.batch_size,
                show_progress_bar=True,
                normalize_embeddings=True,
            )
            scores_g = util.cos_sim(emb_src, emb_google).diagonal().tolist()
        else:
            scores_g = []

        # normalize_embeddings=True 后，cos_sim 就等于点积
        scores_q = util.cos_sim(emb_src, emb_qwen).diagonal().tolist()
    else:
        scores_q = []
        scores_g = []

    # 回填到每行
    qwen_score_by_i = {valid_pos[k]: float(scores_q[k]) for k in range(len(valid_pos))}
    google_score_by_i = {valid_pos[k]: float(scores_g[k]) for k in range(len(valid_pos))} if scores_g else {}

    qwen_wins = 0
    google_wins = 0
    ties = 0
    qwen_sum = 0.0
    google_sum = 0.0
    scored = 0

    rows: List[Tuple[int, str, str, float, str, float, str]] = []
    for pos, (idx, src, qwen, google) in enumerate(aligned):
        if pos in qwen_score_by_i:
            sq = qwen_score_by_i[pos]
            sg = google_score_by_i.get(pos, float("nan"))
            scored += 1
            qwen_sum += sq
            if not math.isnan(sg):
                google_sum += sg
                if sq > sg:
                    winner = name1
                    qwen_wins += 1
                elif sg > sq:
                    winner = name2
                    google_wins += 1
                else:
                    winner = "平手"
                    ties += 1
            else:
                winner = "N/A"
        else:
            sq = float("nan")
            sg = float("nan")
            winner = "N/A"

        rows.append((idx, src, qwen, sq, google, sg, winner))

    qwen_avg = (qwen_sum / scored) if scored else float("nan")
    google_avg = (google_sum / scored) if scored and google_sum > 0 else float("nan")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# 翻译质量评估报告 (LaBSE 语义相似度)\n\n")
        f.write(f"- 原文来源: `{path1}` (content 字段)\n")
        f.write(f"- {name1} 文件: `{path1}`\n")
        if name2:
            f.write(f"- {name2} 文件: `{path1}`\n")
        f.write(f"- LaBSE 模型: `{args.model}`\n")
        f.write(f"- device: `{device}`\n\n")

        f.write("## 统计\n\n")
        f.write(f"- {name1} 平均得分: {qwen_avg:.4f}\n")
        if name2:
            f.write(f"- {name2} 平均得分: {google_avg:.4f}\n")
            f.write(f"- {name1} 优于 {name2}: {qwen_wins}\n")
            f.write(f"- {name2} 优于 {name1}: {google_wins}\n")
            f.write(f"- 平手: {ties}\n")
        f.write(f"- 参与统计句子数: {scored}\n\n")

        f.write("## 明细对比表\n\n")
        header_name1 = _md_escape_cell(name1)
        header_name2 = _md_escape_cell(name2) if name2 else ""
        if name2:
            f.write(
                f"| 序号 | 日语原文 | {header_name1}翻译 | {header_name1}得分 | {header_name2}翻译 | {header_name2}得分 | 优胜方 |\n"
            )
            f.write("|---:|---|---|---:|---|---:|---|\n")
            for idx, src, qwen, sq, google, sg, winner in rows:
                sq_cell = "" if math.isnan(sq) else f"{sq:.4f}"
                sg_cell = "" if math.isnan(sg) else f"{sg:.4f}"
                f.write(
                    "| "
                    + " | ".join(
                        [
                            str(idx),
                            _md_escape_cell(src),
                            _md_escape_cell(qwen),
                            sq_cell,
                            _md_escape_cell(google),
                            sg_cell,
                            winner,
                        ]
                    )
                    + " |\n"
                )
        else:
            f.write(
                f"| 序号 | 日语原文 | {header_name1}翻译 | {header_name1}得分 |\n"
            )
            f.write("|---:|---|---|---:|\n")
            for idx, src, qwen, sq, google, sg, winner in rows:
                sq_cell = "" if math.isnan(sq) else f"{sq:.4f}"
                f.write(
                    "| "
                    + " | ".join(
                        [
                            str(idx),
                            _md_escape_cell(src),
                            _md_escape_cell(qwen),
                            sq_cell,
                        ]
                    )
                    + " |\n"
                )

    print(f"已写出: {out_path}")
    print(f"{name1} 的评分如下：")
    print(f"{name1} 平均得分: {qwen_avg:.4f}")
    if name2:
        print(f"{name2} 平均得分: {google_avg:.4f}")
        print(f"{name1}>{name2}: {qwen_wins}, {name2}>{name1}: {google_wins}, 平手: {ties}, 参与统计: {scored}")
    else:
        print(f"参与统计: {scored}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())