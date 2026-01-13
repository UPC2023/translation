import argparse
import os
from typing import List, Tuple
import torch
from sentence_transformers import SentenceTransformer, util


def _read_non_empty_lines(path: str) -> List[Tuple[int, str]]:
    lines: List[Tuple[int, str]] = []
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


def main() -> int:
    parser = argparse.ArgumentParser(
        description="使用 LaBSE 计算日语原文与英文译文的语义相似度，并比较 Qwen vs Google。"
    )
    parser.add_argument("--src", default="test.txt", help="日语原文文件")
    parser.add_argument("--qwen", default="outqw.txt", help="Qwen 翻译结果文件")
    parser.add_argument("--google", default="outgo.txt", help="Google/标准答案文件")
    parser.add_argument("--out", default="labse_report.md", help="输出 Markdown 报告文件")
    parser.add_argument("--model", default="sentence-transformers/LaBSE", help="Sentence-Transformers 模型")
    parser.add_argument("--device", default="auto", choices=["auto", "cpu", "cuda"], help="推理设备")
    parser.add_argument("--batch_size", type=int, default=32)
    args = parser.parse_args()

    for p in (args.src, args.qwen, args.google):
        if not os.path.exists(p):
            raise FileNotFoundError(p)

    device = args.device
    if device == "auto":
        device = "cuda" if torch.cuda.is_available() else "cpu"

    print(f"--- 正在加载 LaBSE 模型: {args.model} (device={device}) ---")
    st_model = SentenceTransformer(args.model, device=device)
    print("开始评测...\n")

    src_lines = _read_non_empty_lines(args.src)
    qwen_lines = _read_non_empty_lines(args.qwen)
    google_lines = _read_non_empty_lines(args.google)

    n = max(len(src_lines), len(qwen_lines), len(google_lines))
    if len(src_lines) != len(qwen_lines) or len(qwen_lines) != len(google_lines):
        print(
            "[WARN] 三个文件非空行数不一致："
            f"src={len(src_lines)}, qwen={len(qwen_lines)}, google={len(google_lines)}。将按顺序对齐到最大长度。"
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
        if src.strip() != "" and qwen.strip() != "" and google.strip() != "":
            valid_pos.append(i)
            valid_src.append(src)
            valid_qwen.append(qwen)
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
        emb_google = st_model.encode(
            valid_google,
            convert_to_tensor=True,
            batch_size=args.batch_size,
            show_progress_bar=True,
            normalize_embeddings=True,
        )

        # normalize_embeddings=True 后，cos_sim 就等于点积
        scores_q = util.cos_sim(emb_src, emb_qwen).diagonal().tolist()
        scores_g = util.cos_sim(emb_src, emb_google).diagonal().tolist()
    else:
        scores_q = []
        scores_g = []

    # 回填到每行
    qwen_score_by_i = {valid_pos[k]: float(scores_q[k]) for k in range(len(valid_pos))}
    google_score_by_i = {valid_pos[k]: float(scores_g[k]) for k in range(len(valid_pos))}

    qwen_wins = 0
    google_wins = 0
    ties = 0
    qwen_sum = 0.0
    google_sum = 0.0
    scored = 0

    rows: List[Tuple[int, str, str, float, str, float, str]] = []
    for pos, (idx, src, qwen, google) in enumerate(aligned):
        if pos in qwen_score_by_i and pos in google_score_by_i:
            sq = qwen_score_by_i[pos]
            sg = google_score_by_i[pos]
            scored += 1
            qwen_sum += sq
            google_sum += sg
            if sq > sg:
                winner = "Qwen"
                qwen_wins += 1
            elif sg > sq:
                winner = "Google"
                google_wins += 1
            else:
                winner = "平手"
                ties += 1
        else:
            sq = float("nan")
            sg = float("nan")
            winner = "N/A"

        rows.append((idx, src, qwen, sq, google, sg, winner))

    qwen_avg = (qwen_sum / scored) if scored else float("nan")
    google_avg = (google_sum / scored) if scored else float("nan")

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("# 翻译质量评估报告 (LaBSE 语义相似度)\n\n")
        f.write(f"- 原文文件: `{args.src}`\n")
        f.write(f"- Qwen 文件: `{args.qwen}`\n")
        f.write(f"- Google 文件: `{args.google}`\n")
        f.write(f"- LaBSE 模型: `{args.model}`\n")
        f.write(f"- device: `{device}`\n\n")

        f.write("## 统计\n\n")
        f.write(f"- Qwen 平均得分: {qwen_avg:.4f}\n")
        f.write(f"- Google 平均得分: {google_avg:.4f}\n")
        f.write(f"- Qwen 优于 Google: {qwen_wins}\n")
        f.write(f"- Google 优于 Qwen: {google_wins}\n")
        f.write(f"- 平手: {ties}\n")
        f.write(f"- 参与统计句子数: {scored}\n\n")

        f.write("## 明细对比表\n\n")
        f.write("| 序号 | 日语原文 | Qwen翻译 | Qwen得分 | Google翻译 | Google得分 | 优胜方 |\n")
        f.write("|---:|---|---|---:|---|---:|---|\n")
        for idx, src, qwen, sq, google, sg, winner in rows:
            sq_cell = "" if sq != sq else f"{sq:.4f}"  # NaN check
            sg_cell = "" if sg != sg else f"{sg:.4f}"
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

    print(f"已写出: {args.out}")
    print(f"Qwen 平均得分: {qwen_avg:.4f}")
    print(f"Google 平均得分: {google_avg:.4f}")
    print(f"Qwen>Google: {qwen_wins}, Google>Qwen: {google_wins}, 平手: {ties}, 参与统计: {scored}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())