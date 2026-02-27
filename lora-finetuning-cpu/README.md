# LoRA Fine-Tuning on CPU

This project implements a fine-tuning process for language models using Low-Rank Adaptation (LoRA) techniques. The code is designed to run on CPU and is structured to facilitate easy modifications and extensions.

## Project Structure

```
lora-finetuning-cpu
├── src
│   ├── finetune.py       # Main logic for fine-tuning the model
│   └── utils.py          # Utility functions for preprocessing and evaluation
├── data
│   └── dataset.jsonl     # Dataset in JSON Lines format
├── requirements.txt       # Python dependencies
├── config.json            # Configuration settings for fine-tuning
└── README.md              # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd lora-finetuning-cpu
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

## Running the Fine-Tuning

To start the fine-tuning process, run the following command:

```
python src/finetune.py
```

Make sure to adjust the configuration in `config.json` as needed for your specific use case.

## Dataset

The dataset used for training is located in the `data` directory in JSON Lines format. Each line should represent a separate training example.

## License

This project is licensed under the Apache 2.0 License. See the LICENSE file for more details.

## Acknowledgments

This project utilizes the Qwen2.5 model and the Hugging Face Transformers library for model handling and training.