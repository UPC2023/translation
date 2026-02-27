import torch
from transformers import pipeline, WhisperProcessor, WhisperForConditionalGeneration
from transformers.utils import is_flash_attn_2_available
import librosa
import os # 导入 os 模块

# 1. 语音到文本 (Speech-to-Text)
def transcribe_audio(audio_path):
    """
    使用Hugging Face的Whisper模型将音频文件转录为文本。
    此版本直接使用 model.generate() 以获得更准确的长音频转录。
    :param audio_path: 音频文件的路径。
    :return: 转录的文本。
    """
    # 定义模型和设备
    model_id = "openai/whisper-base"
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    # 加载模型和处理器
    processor = WhisperProcessor.from_pretrained(model_id)
    model = WhisperForConditionalGeneration.from_pretrained(
        model_id, 
        torch_dtype=torch_dtype,
        low_cpu_mem_usage=True, # 优化CPU内存使用
        use_safetensors=True
    )
    model.to(device)

    # 加载并处理音频文件
    # 使用 librosa 加载音频
    audio_array, sampling_rate = librosa.load(audio_path, sr=16000)
    
    # **音频预处理步骤**
    # 1. 去除音频文件开头和结尾的静音部分
    audio_array, _ = librosa.effects.trim(audio_array, top_db=20)
    
    # 2. 音量归一化 (可选，但推荐)
    # 如果需要，可以取消下面的注释来启用音量归一化
    # audio_array = librosa.util.normalize(audio_array)

    # 使用处理器将音频转换为输入特征
    input_features = processor(audio_array, sampling_rate=16000, return_tensors="pt").input_features
    input_features = input_features.to(device, dtype=torch_dtype)

    # 生成 token ids
    # 强制模型将输出语言设置为日语
    predicted_ids = model.generate(input_features, forced_decoder_ids=processor.get_decoder_prompt_ids(language="japanese", task="transcribe"))
    
    # 将 token ids 解码为文本
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
    
    return transcription[0]

# 2. 文本到文本翻译 (Text-to-Text Translation)
#    这部分将使用您现有的翻译模型或一个新的翻译模型。
#    我们可以在下一步中集成您在 qwen_pro.py 或其他文件中使用的翻译逻辑。
def translate_text(text, model_path="~/Qwen2.5-0.5B"):
    """
    使用Hugging Face的模型将文本从日语翻译成中文。
    :param text: 日语文本。
    :param model_path: 要使用的翻译模型的路径。
    :return: 翻译后的中文文本。
    """
    # 展开用户目录 '~'
    model_path = os.path.expanduser(model_path)

    # 检查是否有可用的GPU
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    # 使用 pipeline 加载本地模型进行翻译
    # 对于生成式模型，我们通常使用 "text-generation" pipeline
    translator = pipeline(
        "text-generation", 
        model=model_path, 
        device=device,
        torch_dtype=torch_dtype
    )
    
    # 构建适用于Qwen翻译的prompt (参考 langgraph_translator.py)
    system_prompt = (
        "你是一名资深的日语→中文字幕翻译，擅长口语化、凝练的表达。"
        "请将提供的日文内容翻译成自然流畅的中文，仅输出译文本身，不要添加注释或解释。"
    )
    user_prompt = (
        "上下文（可能为空）：\n"
        "<无额外上下文>\n\n"
        "待翻译内容（日文）：\n"
        f"{text}\n\n"
        "中文译文："
    )

    # 使用 apply_chat_template 构建完整的 prompt
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    full_prompt = translator.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    # 生成翻译结果
    outputs = translator(full_prompt, max_new_tokens=256, num_return_sequences=1, eos_token_id=translator.tokenizer.eos_token_id)
    
    # 从输出中提取翻译文本
    generated_text = outputs[0]['generated_text']
    # 解析 apply_chat_template 添加的 'assistant' 角色后的输出
    if "assistant\n" in generated_text:
        translated_text = generated_text.split("assistant\n")[-1].strip()
    else:
        # 作为备用方案，移除原始的prompt部分
        translated_text = generated_text.replace(full_prompt, "").strip()

    return translated_text


# 主函数
if __name__ == "__main__":
    # 这是一个示例音频文件的路径。
    # 您需要准备一个日语语音文件并替换此路径。
    # 例如: "path/to/your/japanese_audio.wav"
    # 如果您没有音频文件，我可以帮您找一个。
    japanese_audio_path = "/home/cyw/janpan/duan.mp3" 

    print("步骤 1: 开始将日语语音转录为文本...")
    try:
        japanese_text = transcribe_audio(japanese_audio_path)
        print(f"转录的日语文本: {japanese_text}")

        print("\n步骤 2: 开始将日语文本翻译为中文...")
        chinese_text = translate_text(japanese_text)
        print(f"翻译的中文文本: {chinese_text}")

    except FileNotFoundError:
        print(f"错误: 音频文件未找到 '{japanese_audio_path}'。")
        print("请将一个日语WAV格式的音频文件放在项目根目录并命名为 'example_japanese_audio.wav'，或者在代码中更新文件路径。")
    except Exception as e:
        print(f"处理过程中发生错误: {e}")
        print("请确保您已安装所有必需的库 (pip install transformers torch torchaudio soundfile librosa)。")
        if "flash_attention_2" in str(e):
            print("Flash Attention 2 不可用，将使用 'sdpa'。如果遇到问题，请检查您的PyTorch和CUDA版本。")

