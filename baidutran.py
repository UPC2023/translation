import requests
import random
import json
from pathlib import Path
from hashlib import md5

# ========================================================
# 1. 请将你在控制台复制的内容粘贴到下面两个引号中间
# ========================================================
APP_ID = '20260114002539454'   # 比如 '2023010100001'
APP_KEY = 'I3KVWPJrsSHYWLyzg_cL'     # 比如 'GTx8s9d......'
# ========================================================

def baidu_translate(query, from_lang='jp', to_lang='en'):
    """
    百度通用翻译 API
    :param query: 要翻译的文本
    :param from_lang: 源语言 (jp=日语, zh=中文, en=英语) *注意百度日语是jp*
    :param to_lang: 目标语言 (en=英语, zh=中文)
    """
    endpoint = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    salt = random.randint(32768, 65536)
    
    # 签名生成
    sign = md5((APP_ID + query + str(salt) + APP_KEY).encode('utf-8')).hexdigest()
    
    # 发送请求
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        'appid': APP_ID,
        'q': query,
        'from': from_lang,
        'to': to_lang,
        'salt': salt,
        'sign': sign
    }
    
    try:
        r = requests.post(endpoint, params=payload, headers=headers)
        result = r.json()
        
        # 错误处理
        if 'error_code' in result:
            return f"报错了，错误码: {result['error_code']}, 信息: {result['error_msg']}"
            
        if 'trans_result' in result:
            return result['trans_result'][0]['dst']
        
    except Exception as e:
        return f"网络请求异常: {e}"

def translate_file(in_path: Path, out_path: Path, from_lang: str = "jp", to_lang: str = "en") -> None:
    """Translate each line in in_path and write to out_path."""
    count = 0
    with in_path.open("r", encoding="utf-8") as fin, out_path.open("w", encoding="utf-8") as fout:
        for line in fin:
            text = line.rstrip("\n")
            if text.strip() == "":
                fout.write("\n")
                continue

            translated = baidu_translate(text, from_lang=from_lang, to_lang=to_lang)
            fout.write(str(translated) + "\n")
            count += 1

    print(f"完成: {count} 行已翻译并写入 {out_path}")


def main() -> None:
    default_in = "train_data/test_0429.txt"
    default_out = "ref_en.txt"

    in_prompt = f"请输入待翻译文件路径 (回车默认: {default_in}): "
    out_prompt = f"请输入输出文件路径 (回车默认: {default_out}): "

    in_path = Path(input(in_prompt).strip() or default_in)
    out_path = Path(input(out_prompt).strip() or default_out)

    if not in_path.exists():
        print(f"错误: 输入文件不存在: {in_path}")
        return

    translate_file(in_path, out_path)


if __name__ == "__main__":
    main()