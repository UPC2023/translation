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


def main() -> int:
    parser = argparse.ArgumentParser(
        description="BLEU 评分：test(原文) + out(Qwen译文) + outgo(标准译文) -> 输出对比表 qwen_bleu"
    )
    parser.add_argument("--src", default="test.txt", help="翻译前原文文件 (Japanese)")
    parser.add_argument("--hyp", default="out.txt", help="Qwen 翻译结果文件 (English hypothesis)")
    parser.add_argument("--ref", default="outgo.txt", help="标准答案文件 (English reference)")
    parser.add_argument("--out", default="qwen_bleu", help="输出文件名（不带后缀时会生成 .md 和 .tsv 两份）")
    parser.add_argument("--tokenize", default="13a", help="sacrebleu tokenize 方式（默认 13a）")
    args = parser.parse_args()

    for p in (args.src, args.hyp, args.ref):
        if not os.path.exists(p):
            raise FileNotFoundError(p)

    src_lines = _read_non_empty_lines(args.src)
    hyp_lines = _read_non_empty_lines(args.hyp)
    ref_lines = _read_non_empty_lines(args.ref)

    n = max(len(src_lines), len(hyp_lines), len(ref_lines))
    if len(src_lines) != len(hyp_lines) or len(hyp_lines) != len(ref_lines):
        print(
            "[WARN] 三个文件的非空行数不一致："
            f"src={len(src_lines)}, hyp={len(hyp_lines)}, ref={len(ref_lines)}。将按顺序对齐到最大长度，缺失项记为空。"
        )

    refs: List[str] = []
    hyps: List[str] = []
    sent_scores: List[float] = []

    out_base = args.out
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
        f.write("idx\tbleu\tsrc_line\thyp_line\tref_line\tsource\tqwen\tref\n")

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
        f.write("# Qwen Translation BLEU Report\n\n")
        f.write(f"- Source: `{args.src}`\n- Hypothesis (Qwen): `{args.hyp}`\n- Reference (Gold): `{args.ref}`\n")
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
            f.write(f"BLEU评分：{bleu_cell}\n\n")
            f.write("原文：\n")
            f.write(_md_fenced(_md_escape(src)) + "\n\n")
            f.write("译文：\n")
            f.write(_md_fenced(_md_escape(hyp)) + "\n\n")
            f.write("标准译文：\n")
            f.write(_md_fenced(_md_escape(ref)) + "\n\n")
            f.write("---\n\n")

        if hyps and refs:
            corpus = sacrebleu.corpus_bleu(hyps, [refs], tokenize=args.tokenize)
            avg_sent = sum(sent_scores) / len(sent_scores)
            f.write(f"**句子平均 BLEU**: {avg_sent:.2f}  \n")
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

