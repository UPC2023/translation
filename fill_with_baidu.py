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


def process_file(src: Path, dst: Path, app_id: str, app_key: str, delay: float = 0.4):
    total = 0
    filled = 0
    skipped = 0
    outputs = []

    with src.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            total += 1
            if obj.get("output"):
                skipped += 1
                outputs.append(obj)
                continue
            text = obj.get("input", "")
            translated = baidu_translate(text, app_id, app_key)
            obj["output"] = translated
            filled += 1
            outputs.append(obj)
            time.sleep(delay)  # be nice to the API

    with dst.open("w", encoding="utf-8") as f:
        for obj in outputs:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")

    print(f"{src.name}: total={total}, filled={filled}, kept={skipped}, written={dst}")


def main():
    ap = argparse.ArgumentParser(description="Fill JSONL output field via Baidu Translate (jp->en).")
    ap.add_argument("--src", required=True, help="source jsonl path")
    ap.add_argument("--dst", required=True, help="destination jsonl path")
    ap.add_argument("--app_id", default=DEFAULT_APP_ID)
    ap.add_argument("--app_key", default=DEFAULT_APP_KEY)
    ap.add_argument("--delay", type=float, default=0.4, help="seconds between requests")
    args = ap.parse_args()

    process_file(Path(args.src), Path(args.dst), args.app_id, args.app_key, delay=args.delay)


if __name__ == "__main__":
    main()
