from pathlib import Path
import json

from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
    
    DataCollatorForLanguageModeling,
)
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, TaskType # 添加导入


class LoRAFineTuner:
    def __init__(self, config: dict):
        self.config = config
        self.model = None
        self.tokenizer = None
        self.train_dataset = None

    def load_model(self):
        model_name = self.config.get('base_model') or self.config.get('model_name')
        if not model_name:
            raise ValueError('base_model or model_name must be set in config')

        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        base_model = AutoModelForCausalLM.from_pretrained(model_name)

        # Resize token embeddings to match tokenizer vocabulary size
        base_model.resize_token_embeddings(len(self.tokenizer))

        # 确保 base model 启用梯度计算（LoRA 训练必需）
        base_model.enable_input_require_grads()

        # 应用 LoRA 配置 - 从 config.json 读取
        peft_config = LoraConfig(
            task_type=TaskType.CAUSAL_LM,
            inference_mode=False,
            r=int(self.config.get('lora_r', 8)),
            lora_alpha=int(self.config.get('lora_alpha', 32)),
            lora_dropout=float(self.config.get('lora_dropout', 0.1)),
            target_modules=self.config.get('lora_target_modules', ["q_proj", "v_proj"])
        )
        self.model = get_peft_model(base_model, peft_config)
        self.model.print_trainable_parameters() # 确认可训练参数量

    def prepare_data(self):
        data_path = self.config.get('data_path')
        if not data_path:
            raise ValueError('data_path must be set in config')

        cutoff = int(self.config.get('cutoff_len', 512))
        
        # 加载数据
        ds = load_dataset('json', data_files=str(data_path), split='train')

        # 1. 定义 Prompt 生成函数 (不做 tokenization，只做字符串拼接)
        def generate_prompt_and_tokenize(example):
            # --- A. 构建文本 ---
            instruction = 'Translate the following Japanese text to English, considering the given context.'
            japanese_text = example.get('content', '')
            context = example.get('context', '')
            output_text = example.get('output', '') # 必须要有 output
            
            # 构造 Prompt 部分 (模型看到的部分)
            if context:
                prompt = (
                    f"Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n"
                    f"### Instruction:\n{instruction}\n\n"
                    f"### Context:\n{context}\n\n"
                    f"### Input:\n{japanese_text}\n\n"
                    f"### Response:\n"
                )
            else:
                prompt = (
                    f"Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n"
                    f"### Instruction:\n{instruction}\n\n"
                    f"### Input:\n{japanese_text}\n\n"
                    f"### Response:\n"
                )

            # --- B. Tokenize 处理 (核心逻辑) ---
            
            # 1. 编码 Prompt (用来计算长度，方便 Mask)
            # add_special_tokens=False 是为了避免开头重复加 BOS token，后面手动处理
            prompt_ids = self.tokenizer.encode(prompt, add_special_tokens=False)
            
            # 2. 编码 Output (加上结束符 EOS)
            target_ids = self.tokenizer.encode(output_text + self.tokenizer.eos_token, add_special_tokens=False)

            # 3. 拼接 Input IDs
            input_ids = prompt_ids + target_ids
            
            # 4. 构造 Labels (关键步骤！)
            # Prompt 部分设为 -100 (不计算 Loss)
            # Output 部分保留原 ID (计算 Loss)
            labels = [-100] * len(prompt_ids) + target_ids

            # --- C. 截断与填充 (Padding) ---
            
            # 截断
            if len(input_ids) > cutoff:
                input_ids = input_ids[:cutoff]
                labels = labels[:cutoff]
            
            # 填充 (手动填充以确保 labels 对齐)
            pad_len = cutoff - len(input_ids)
            if pad_len > 0:
                input_ids += [self.tokenizer.pad_token_id] * pad_len
                # Padding 部分也不计算 Loss，设为 -100
                labels += [-100] * pad_len
            
            # 构造 Attention Mask (非 padding 部分为 1)
            attention_mask = [1 if id != self.tokenizer.pad_token_id else 0 for id in input_ids]

            return {
                "input_ids": input_ids,
                "labels": labels,
                "attention_mask": attention_mask
            }

        # 应用处理函数 (batched=False 逐条处理逻辑更清晰，且不容易出错)
        print("Tokenizing and masking data...")
        tokenized = ds.map(
            generate_prompt_and_tokenize, 
            batched=False, 
            remove_columns=ds.column_names # 处理完后移除原始文本列
        )
        
        # 转换为 PyTorch 格式
        tokenized.set_format(type='torch', columns=['input_ids', 'labels', 'attention_mask'])

        # 简单的完整性检查
        vocab_size = len(self.tokenizer)
        print(f"Sample Input IDs length: {len(tokenized[0]['input_ids'])}")
        print(f"Sample Labels (first 10): {tokenized[0]['labels'][:10]}") # 应该看到全是 -100

        self.train_dataset = tokenized

    def train(self):
        # 确保模型处于训练模式
        self.model.train()
        # 移除冗长的 Trainable 参数打印，直接用 print_trainable_parameters() 确认
        # for name, param in self.model.named_parameters():
        #     if param.requires_grad:
        #         print(f"Trainable: {name}")

        output_dir = self.config.get('output_dir', './results')
        num_epochs = int(self.config.get('num_epochs', 1))
        per_device_batch = int(self.config.get('batch_size', 1))
        learning_rate = float(self.config.get('learning_rate', 5e-5))

        training_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=num_epochs,
            per_device_train_batch_size=per_device_batch,
            gradient_accumulation_steps=int(self.config.get('gradient_accumulation_steps', 1)),
            learning_rate=learning_rate,
            logging_dir=self.config.get('logging_dir', './logs'),
            save_total_limit=int(self.config.get('save_total_limit', 2)),
            fp16=False,
            remove_unused_columns=False,
            gradient_checkpointing=True, # 开启梯度检查点以节省内存
        )

        data_collator = DataCollatorForLanguageModeling(tokenizer=self.tokenizer, mlm=False)

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=self.train_dataset,
            data_collator=data_collator,
        )

        trainer.train()
        trainer.save_model(output_dir)


def main():
    # Look for config.json in parent directory if not found in current directory
    config_path = Path('config.json')
    if not config_path.exists():
        config_path = Path(__file__).parent.parent / 'config.json'
    if not config_path.exists():
        raise SystemExit('config.json not found')
    config = json.loads(config_path.read_text(encoding='utf-8'))

    tuner = LoRAFineTuner(config=config)
    print('Loading model...')
    tuner.load_model()
    print('Preparing data...')
    tuner.prepare_data()
    print('Starting training...')
    tuner.train()


if __name__ == '__main__':
    main()
