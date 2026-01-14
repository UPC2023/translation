import argparse
import os
from typing import List, Tuple

import sacrebleu


def _read_non_empty_lines(path: str) -> List[Tuple[int, str]]:
    lines: List[Tuple[int, str]] = []
    with open(path, "r", encoding="utf-8") as f:
        for line_no, raw in enumerate(f, 1):
            text = raw.rstrip("\n")
            if text.strip() == "":
                continue
            lines.append((line_no, text))
    return lines


def _tsv_escape(text: str) -> str:
    return text.replace("\t", " ").replace("\r", " ").replace("\n", " ")


def _md_escape(text: str) -> str:
    return text.replace("\r", "")


def _truncate(text: str, limit: int = 120) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def _md_fenced(text: str) -> str:
    # Use fenced blocks to avoid Markdown formatting issues.
    # Also avoid accidentally closing the fence if input contains ```.
    safe = text.replace("```", "``\u200b`")
    return f"```text\n{safe}\n```"


def _ensure_path(name: str, path: str, force_ask: bool = False) -> str:
    """If path does not exist or force_ask=True, prompt user for a path."""
    if force_ask or not os.path.exists(path):
        print(f"[警告] {name}文件不存在: {path}")
        prompt = f"请重新输入{name}文件路径: "
        entered = input(prompt).strip()
        if entered:
            path = entered
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    return path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="BLEU 评分：可交互输入或通过命令行参数指定原文、译文、标准答案，并输出对比报告。"
    )
    parser.add_argument("--src", default="test.txt", help="翻译前原文文件 (Japanese)")
    parser.add_argument("--hyp", default="out.txt", help="待评估的翻译结果文件 (English hypothesis)")
    parser.add_argument("--ref", default="outgo.txt", help="标准答案文件 (English reference)")
    parser.add_argument("--out", default="bleu_report", help="输出文件名（不带后缀时会生成 .md 和 .tsv）")
    parser.add_argument("--tokenize", default="13a", help="sacrebleu tokenize 方式（默认 13a）")
    parser.add_argument("--no-prompt", action="store_true", help="跳过交互，直接使用命令行提供的路径")
    args = parser.parse_args()

    if args.no_prompt:
        src_path = _ensure_path("原文", args.src)
        hyp_path = _ensure_path("译文", args.hyp)
        ref_path = _ensure_path("标准答案", args.ref)
        out_base = args.out
    else:
        src_path_in = input(f"请输入原文文件路径 (回车默认: {args.src}): ").strip()
        src_path = _ensure_path("原文", src_path_in or args.src)

        hyp_path_in = input(f"请输入待评估的译文文件路径 (回车默认: {args.hyp}): ").strip()
        hyp_path = _ensure_path("译文", hyp_path_in or args.hyp)

        ref_path_in = input(f"请输入标准答案文件路径 (回车默认: {args.ref}): ").strip()
        ref_path = _ensure_path("标准答案", ref_path_in or args.ref)

        out_in = input(f"请输入输出报告名前缀 (回车默认: {args.out}): ").strip()
        out_base = out_in or args.out

    src_lines = _read_non_empty_lines(src_path)
    hyp_lines = _read_non_empty_lines(hyp_path)
    ref_lines = _read_non_empty_lines(ref_path)

    n = max(len(src_lines), len(hyp_lines), len(ref_lines))
    if len(src_lines) != len(hyp_lines) or len(hyp_lines) != len(ref_lines):
        print(
            "[WARN] 三个文件的非空行数不一致："
            f"src={len(src_lines)}, hyp={len(hyp_lines)}, ref={len(ref_lines)}。将按顺序对齐到最大长度，缺失项记为空。"
        )

    refs: List[str] = []
    hyps: List[str] = []
    sent_scores: List[float] = []

    if out_base.endswith(".md"):
        out_md = out_base
        out_tsv = out_base[: -3] + ".tsv"
    elif out_base.endswith(".tsv"):
        out_tsv = out_base
        out_md = out_base[: -4] + ".md"
    else:
        out_md = out_base + ".md"
        out_tsv = out_base + ".tsv"

    # TSV：便于 Excel/表格软件
    with open(out_tsv, "w", encoding="utf-8") as f:
        f.write("idx\tbleu\tsrc_line\thyp_line\tref_line\tsource\thyp\tref\n")

        for i in range(n):
            src_no, src = src_lines[i] if i < len(src_lines) else (0, "")
            hyp_no, hyp = hyp_lines[i] if i < len(hyp_lines) else (0, "")
            ref_no, ref = ref_lines[i] if i < len(ref_lines) else (0, "")

            if hyp.strip() != "" and ref.strip() != "":
                score = sacrebleu.sentence_bleu(hyp, [ref], tokenize=args.tokenize).score
                refs.append(ref)
                hyps.append(hyp)
                sent_scores.append(score)
                score_str = f"{score:.2f}"
            else:
                score_str = ""

            f.write(
                "\t".join(
                    [
                        str(i + 1),
                        score_str,
                        str(src_no),
                        str(hyp_no),
                        str(ref_no),
                        _tsv_escape(src),
                        _tsv_escape(hyp),
                        _tsv_escape(ref),
                    ]
                )
                + "\n"
            )

        f.write("\n")
        if hyps and refs:
            corpus = sacrebleu.corpus_bleu(hyps, [refs], tokenize=args.tokenize)
            avg_sent = sum(sent_scores) / len(sent_scores)
            f.write(f"# sentence_avg_bleu\t{avg_sent:.2f}\n")
            f.write(f"# corpus_bleu\t{corpus.score:.2f}\n")
            f.write(f"# scored_pairs\t{len(hyps)}\n")
        else:
            f.write("# scored_pairs\t0\n")

    # Markdown：竖向对比（不使用表格）
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("# Translation BLEU Report\n\n")
        f.write(f"- Source: `{src_path}`\n- Hypothesis: `{hyp_path}`\n- Reference: `{ref_path}`\n")
        f.write(f"- sacrebleu tokenize: `{args.tokenize}`\n\n")

        for i in range(n):
            _, src = src_lines[i] if i < len(src_lines) else (0, "")
            _, hyp = hyp_lines[i] if i < len(hyp_lines) else (0, "")
            _, ref = ref_lines[i] if i < len(ref_lines) else (0, "")

            if hyp.strip() != "" and ref.strip() != "":
                score = sacrebleu.sentence_bleu(hyp, [ref], tokenize=args.tokenize).score
                bleu_cell = f"{score:.2f}"
            else:
                bleu_cell = ""

            f.write(f"## {i + 1}\n\n")
            f.write(f"BLEU Score: {bleu_cell}\n\n")
            f.write("Source:\n")
            f.write(_md_fenced(_md_escape(src)) + "\n\n")
            f.write("Hypothesis:\n")
            f.write(_md_fenced(_md_escape(hyp)) + "\n\n")
            f.write("Reference:\n")
            f.write(_md_fenced(_md_escape(ref)) + "\n\n")
            f.write("---\n\n")

        if hyps and refs:
            corpus = sacrebleu.corpus_bleu(hyps, [refs], tokenize=args.tokenize)
            avg_sent = sum(sent_scores) / len(sent_scores)
            f.write(f"**Average Sentence BLEU**: {avg_sent:.2f}  \n")
            f.write(f"**Corpus BLEU**: {corpus.score:.2f}  \n")
            f.write(f"**Scored pairs**: {len(hyps)}\n")
        else:
            f.write("**Scored pairs**: 0\n")

    if hyps and refs:
        corpus = sacrebleu.corpus_bleu(hyps, [refs], tokenize=args.tokenize)
        print(f"已写出: {out_md}")
        print(f"已写出: {out_tsv}")
        print(f"句子平均 BLEU: {sum(sent_scores) / len(sent_scores):.2f}")
        print(f"Corpus BLEU:  {corpus.score:.2f}")
    else:
        print(f"已写出: {out_md} / {out_tsv}（无可评分的 hyp/ref 对）")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

