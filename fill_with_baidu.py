import json
import time
import random
import argparse
from pathlib import Path
from hashlib import md5
import requests

# Use the same credentials as in baidutran.py or override via CLI
DEFAULT_APP_ID = "20260114002539454"
DEFAULT_APP_KEY = "I3KVWPJrsSHYWLyzg_cL"


def baidu_translate(query: str, app_id: str, app_key: str, from_lang: str = "jp", to_lang: str = "en") -> str:
    endpoint = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    salt = random.randint(32768, 65536)
    sign = md5((app_id + query + str(salt) + app_key).encode("utf-8")).hexdigest()

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {
        "appid": app_id,
        "q": query,
        "from": from_lang,
        "to": to_lang,
        "salt": salt,
        "sign": sign,
    }
    r = requests.post(endpoint, params=payload, headers=headers, timeout=15)
    result = r.json()
    if "error_code" in result:
        # 20003 = sensitive word: fallback to original text instead of aborting
        if str(result.get("error_code")) == "20003":
            return query
        raise RuntimeError(f"Baidu API error {result['error_code']}: {result['error_msg']}")
    return result["trans_result"][0]["dst"]


def process_file(src: Path, dst: Path, app_id: str, app_key: str, delay: float = 0.4, resume: bool = True):
    """Stream through src and write translated lines to dst.

    If resume=True and dst exists, skip already-written lines and append from there.
    This allows long runs to continue after中断 without重跑。"""

    already_written = 0
    if resume and dst.exists():
        with dst.open("r", encoding="utf-8") as f_out:
            for _ in f_out:
                already_written += 1

    total = 0
    filled = 0
    skipped = 0

    with src.open("r", encoding="utf-8") as f_in, dst.open("a", encoding="utf-8") as f_out:
        # 快进已写部分
        for _ in range(already_written):
            line = f_in.readline()
            if not line:
                break
            total += 1

        for line in f_in:
            if not line.strip():
                continue
            obj = json.loads(line)
            total += 1

            if obj.get("output"):
                skipped += 1
            else:
                text = obj.get("input", "")
                if not text:
                    print(f"Skipping line {total} because 'input' is empty.")
                    skipped += 1
                    continue
                obj["output"] = baidu_translate(text, app_id, app_key)
                filled += 1
                time.sleep(delay)  # be nice to the API

            f_out.write(json.dumps(obj, ensure_ascii=False) + "\n")
            f_out.flush()

    print(
        f"{src.name}: total_seen={total}, newly_filled={filled}, reused_with_output={skipped}, resume_start={already_written}, written_to={dst}"
    )


def main():
    ap = argparse.ArgumentParser(description="Fill JSONL output field via Baidu Translate (jp->en).")
    ap.add_argument("--src", help="source jsonl path (will be prompted if not provided)")
    ap.add_argument("--dst", help="destination jsonl path (will be derived from --src if not provided)")
    ap.add_argument("--app_id", default=DEFAULT_APP_ID)
    ap.add_argument("--app_key", default=DEFAULT_APP_KEY)
    ap.add_argument("--delay", type=float, default=0.4, help="seconds between requests")
    ap.add_argument("--no-resume", action="store_true", help="force overwrite, disable resume")
    args = ap.parse_args()

    src_path_str = args.src
    if not src_path_str:
        src_path_str = input("请输入源文件路径 (e.g., /home/cyw/pro/train_data/captions_0429_train.jsonl): ")

    src_path = Path(src_path_str)
    if not src_path.is_file():
        print(f"错误：文件不存在: {src_path}")
        return

    dst_path_str = args.dst
    if not dst_path_str:
        dst_path = src_path.with_name(f"{src_path.stem}_filled{src_path.suffix}")
    else:
        dst_path = Path(dst_path_str)

    resume = not args.no_resume
    if resume and dst_path.exists():
        answer = input(f"发现已存在的目标文件: {dst_path}\n要从上次中断的地方继续吗? (y/n): ").lower()
        if answer not in ['y', 'yes', '是']:
            resume = False

    if not resume and dst_path.exists():
        print(f"将覆盖已存在的目标文件: {dst_path}")
        dst_path.unlink()

    process_file(src_path, dst_path, args.app_id, args.app_key, delay=args.delay, resume=resume)


if __name__ == "__main__":
    main()
