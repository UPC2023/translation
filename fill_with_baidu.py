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
    ap.add_argument("--src", required=True, help="source jsonl path")
    ap.add_argument("--dst", required=True, help="destination jsonl path")
    ap.add_argument("--app_id", default=DEFAULT_APP_ID)
    ap.add_argument("--app_key", default=DEFAULT_APP_KEY)
    ap.add_argument("--delay", type=float, default=0.4, help="seconds between requests")
    ap.add_argument("--no-resume", action="store_true", help="do not resume, overwrite dst")
    args = ap.parse_args()

    dst_path = Path(args.dst)
    if args.no_resume and dst_path.exists():
        dst_path.unlink()

    process_file(Path(args.src), dst_path, args.app_id, args.app_key, delay=args.delay, resume=not args.no_resume)


if __name__ == "__main__":
    main()
