```
# 日英翻译模型评估

本项目用于使用不同的模型（如 LiquidAI, Qwen 等）进行日英翻译，并使用 BLEU 和 LaBSE 等指标对翻译质量进行评估。

## 1. 环境配置

**注意：** 本项目在 Windows Subsystem for Linux 2 (WSL2) 环境下开发和测试。推荐使用 WSL2 以获得最佳兼容性。
### 1.0 安装 WSL2
使用 wsl --install 命令一键安装 WSL2 和 Ubuntu。
在 VS Code 中安装 WSL 扩展。
通过在 WSL 终端中运行 code . 来打开项目。
确认 VS Code 左下角已成功连接到 WSL: Ubuntu。

本项目依赖 `conda` 来管理复杂的 Python 环境和依赖库。

### 1.1 安装 Conda

如果您的系统中没有 `conda`，请先从官方网站下载并安装 Miniconda。对于 Linux 系统，可以执行以下命令：

```bash
# 下载 Miniconda 安装脚本
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# 运行安装脚本
bash Miniconda3-latest-Linux-x86_64.sh

# 按照提示完成安装，并重启你的终端
```

### 1.2 创建 Conda 环境

为了隔离项目依赖，我们创建一个新的 `conda` 环境。

```bash
# 创建一个名为 'translator' 的 Python 3.11 环境
conda create -n translator python=3.11 -y

# 激活新创建的环境
conda activate translator
```

**注意**：后续所有命令都应在 `translator` 环境中执行。

### 1.3 安装项目依赖

本项目所需的主要依赖库已经整理在 `requirements.txt` 文件中。

```bash
# (请确保你已经创建并激活了 conda 环境)
# 使用 pip 安装 'requirements.txt' 文件中列出的所有依赖
# 使用 -i 参数指定清华大学的 PyPI 镜像以加快下载速度
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```
* **-r requirements.txt**: 告诉 pip 从这个文件读取并安装所有列出的依赖。
* **torch**: 深度学习框架。默认安装的是纯 CPU 版本。如果你的机器有支持 CUDA 的 NVIDIA GPU，可以安装 GPU 版本的 PyTorch 以获得巨大的训练加速。
* **transformers**: Hugging Face 官方库，用于加载和使用预训练模型。我们使用源码安装以支持 lfm2 架构。
* **llamafactory**: LoRA 微调框架。
* **sentence-transformers**: 用于 LaBSE 评估，计算句子相似度。
* **sacrebleu**: 用于 BLEU 评估。
* **pandas, openpyxl**: 可能在数据处理和报告生成中使用。

## 2. 模型准备

本项目使用了多个预训练的翻译模型。您需要将它们下载到指定位置。运行`download_model.py`下载模型，并保存到指定路径。


**提示**: 大部分模型可以通过 Hugging Face Hub 下载。如果遇到网络问题，可以设置环境变量 `HF_ENDPOINT=https://hf-mirror.com` 来使用镜像。

## 3. 数据准备

翻译任务需要一个输入文件。

*   **输入文件格式**: 项目中的脚本（如 `liquidtran.py`）普遍支持 `.jsonl` 格式。文件中的每一行都是一个 JSON 对象，其中包含一个 `input` 字段，其值为待翻译的日文文本，一个 `output` 字段，其值为翻译后的英文文本，一个`instruction`字段翻译任务的描述，例如 "translate to English" 。
    ```json
    {"instruction":"translate to English"}{"input": "こんにちは、世界！"}{"output": ""}
    ```
*   将您的待翻译文件放置在 `pro` 目录下。

## 4. 执行翻译

`pro` 目录下的多个 `*.py` 脚本用于执行翻译。以 `liquidtran.py` 为例：

```bash
# 确保 conda 环境已激活
conda activate translate-env

# 运行翻译脚本
python liquidtran.py
```

脚本会提示您输入：
1.  **待翻译的 jsonl 文件路径**: 可以直接按回车，使用默认路径。
2.  **模型名称简称**: 用于生成输出文件名，例如输入 `liquid`，则输出文件为 `out_liquid.jsonl`。

翻译完成后，会生成一个同样为 `.jsonl` 格式的输出文件，其中每行包含 `input` (原文) 和 `output` (译文)。

## 5. 评估翻译质量

项目提供了两个主要的评估脚本：`eval_bleu.py` 和 `eval_labse.py`。

### 5.1 BLEU 评估

BLEU 分数通过比较机器翻译和专业人工翻译的相似度来衡量翻译质量。

```bash
# 运行 BLEU 评估脚本
python eval_bleu.py
```

脚本会提示您输入：
1.  **待评估的译文文件路径**: 即第 4 步生成的 `out_liquid.jsonl` 等文件。
2.  **标准答案文件路径**: 一个包含正确英文翻译的 `.txt` 或 `.jsonl` 文件。
3.  **输出报告名前缀**: 例如 `liquid_bleu`，脚本会自动生成 `.md` 和 `.tsv` 两种格式的报告。

### 5.2 LaBSE 语义相似度评估

LaBSE (Language-agnostic BERT Sentence Embedding) 模型可以跨语言计算句子向量的相似度。我们用它来评估日文原文和英文译文在语义上的一致性。

```bash
# 运行 LaBSE 评估脚本
python eval_labse.py
```

脚本会提示您输入：
1.  **第一个译文文件路径**: 例如 `out_qwen.jsonl`。
2.  **为第一个译文起一个名称**: 例如 `Qwen`。
3.  **第二个译文文件路径**: 例如 `out_liquid.jsonl`。
4.  **为第二个译文起一个名称**: 例如 `LiquidAI`。
5.  **输出报告文件名**: 默认为 `labse_report.md`。

脚本会生成一个 Markdown 表格，清晰地对比两个模型在每一句上的语义相似度得分，并给出总体统计。

## 6. 使用 LoRA 微调模型

除了直接使用预训练模型，本项目还支持使用 LoRA (Low-Rank Adaptation) 技术对模型进行微调，使其更适应特定的翻译风格或术语。

### 6.1 微调数据准备

LoRA 微调需要符合特定格式的训练和验证数据集。

*   **数据格式**: 训练数据（例如 `train_cleaned_filled.jsonl`）和评估数据（`test_cleaned_filled.jsonl`）都需要是 `.jsonl` 格式，且每一行包含 `instruction`, `input`, 和 `output` 三个字段。
*   **数据路径**: 确保你的数据文件存放在 `pro/train_data/` 目录下。

### 6.2 执行微调

`run_lora_liquid.sh` 脚本封装了所有微调所需的命令和配置。

```bash
# 直接运行微调脚本
./run_lora_liquid.sh
```

该脚本会自动处理以下关键步骤：
1.  **激活正确的 Conda 环境**: 脚本内部会自动激活 `translator` 环境，确保所有依赖和 Python 版本都正确无误。
2.  **设置环境变量**:
    *   `CUDA_VISIBLE_DEVICES=`: 禁用 GPU，强制使用 CPU 进行训练。
    *   `DISABLE_VERSION_CHECK=1`: 绕过 `llamafactory` 的版本检查，以兼容最新的 `transformers` 库。
3.  **调用 `llamafactory-cli`**: 使用预设的参数（如学习率、批大小、LoRA 配置等）启动训练。

训练过程中，模型的检查点 (checkpoint) 会保存在 `pro/outputs/liquidai-350m-lora` 目录下。

### 6.3 合并 LoRA 适配器

训练完成后，`pro/outputs/liquidai-350m-lora` 目录中保存的是 LoRA 适配器（adapter），而不是完整的模型。你需要将这个适配器与原始的基础模型合并，才能得到一个可以直接使用的、经过微调的新模型。

`run_lora_liquid.sh` 脚本的末尾包含了一段被注释掉的合并命令。取消注释并运行它，或者手动执行以下命令：

```bash
# 定义模型和输出路径
MODEL_DIR=/home/cyw/LiquidAI-350M
OUTPUT_DIR=/home/cyw/pro/outputs/liquidai-350m-lora

# 运行合并命令
llamafactory-cli export \
  --model_name_or_path $MODEL_DIR \
  --adapter_name_or_path $OUTPUT_DIR \
  --export_dir $OUTPUT_DIR/merged \
  --export_legacy_format False
```

合并后的完整模型将保存在 `$OUTPUT_DIR/merged` 目录中。

---

按照以上步骤，您就可以完整地复现本项目的翻译和评估流程。
```

