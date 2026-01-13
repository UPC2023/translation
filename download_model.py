import os
from huggingface_hub import snapshot_download

# 可以用镜像站或官方 Hugging Face
# os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

print("--- 正在下载---")

# 只改这一段
try:
    snapshot_download(
        repo_id=input('网址：'), 
        local_dir=input('保存路径：'),            
        resume_download=True,
        max_workers=8
    )
    print("--- 恭喜！下载成功！ ---")
    
except Exception as e:
    print("\n!!! 下载失败 !!!")
    print("错误信息:", e)
