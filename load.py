import os
import psutil
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


proc = psutil.Process(os.getpid())

f= open("log.txt", "w")
def rss_gb() -> float:
    return proc.memory_info().rss / 1e9


def report_model(path: str, name: str, prompt: str = "こんにちは。テストです。") -> None:
    base = rss_gb()
    f.write(f"\n=== {name} ===")
    f.write(f"Baseline RSS GB: {base:.3f}\n")

    tok = AutoTokenizer.from_pretrained(path)
    mdl = AutoModelForCausalLM.from_pretrained(path, device_map=None, dtype=torch.float32)
    after_load = rss_gb()
    f.write(f"After load RSS GB: {after_load:.3f} (delta: {after_load - base:.3f})\n")

    inp = tok(prompt, return_tensors="pt")
    _ = mdl.generate(**inp, max_new_tokens=128, do_sample=False)
    after_gen = rss_gb()
    f.write(f"After gen RSS GB: {after_gen:.3f} (delta: {after_gen - after_load:.3f})\n")


f.write(f"Start RSS GB: {rss_gb():.3f}\n")

MODELS = [
    ("/home/cyw/LiquidAI-350M", "LiquidAI-350M"),
    ("/home/cyw/Qwen2.5-0.5B", "Qwen2.5-0.5B"),
]

for path, name in MODELS:
    report_model(path, name)

f.write(f"\nEnd RSS GB: {rss_gb():.3f}\n")
f.close()
print("Done")
