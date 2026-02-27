from pathlib import Path
import json
import os
import re
import signal
from typing import Optional

from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer,
    TrainerCallback,
    TrainingArguments,
    
    DataCollatorForLanguageModeling,
)
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, TaskType # 添加导入
import numpy as np
import evaluate
from sentence_transformers import SentenceTransformer, util


_INTERRUPT_REQUESTED = False


def _handle_sigint(signum, frame):
    global _INTERRUPT_REQUESTED
    _INTERRUPT_REQUESTED = True


def _find_latest_checkpoint(output_dir: str) -> Optional[str]:
    root = Path(output_dir)
    if not root.exists() or not root.is_dir():
        return None

    checkpoints = []
    for child in root.iterdir():
        if not child.is_dir():
            continue
        m = re.match(r"^checkpoint-(\d+)$", child.name)
        if m:
            checkpoints.append((int(m.group(1)), str(child)))
    if not checkpoints:
        return None
    checkpoints.sort(key=lambda x: x[0])
    return checkpoints[-1][1]


class _GracefulInterruptCallback(TrainerCallback):
    """On SIGINT, save a checkpoint at the next safe step boundary."""

    def __init__(self, trainer: Trainer):
        self.trainer = trainer

    def on_step_end(self, args, state, control, **kwargs):
        if not _INTERRUPT_REQUESTED:
            return control

        # Save a full checkpoint (model + optimizer/scheduler + trainer state)
        # using Trainer internals, then stop training.
        try:
            self.trainer._save_checkpoint(model=kwargs.get("model"), trial=None)
        except Exception:
            # Fallback: at least persist model + state.
            self.trainer.save_model()
            self.trainer.save_state()
        control.should_training_stop = True
        return control


class LoRAFineTuner:
    def __init__(self, config: dict):
        self.config = config
        self.model = None
        self.tokenizer = None
        self.train_dataset = None
        self.eval_dataset = None
        self.labse_model = None
        self.bleu_metric = None
        # Toggle eval/metrics so we can avoid heavy models (e.g., LaBSE) on low-memory machines
        self.enable_eval = bool(config.get('enable_eval', False))          # backward compat
        self.enable_labse = bool(config.get('enable_labse', False))
        self.eval_during_training = bool(config.get('eval_during_training', False))
        self.run_final_eval = bool(config.get('run_final_eval', False))

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
        # 从Hugging Face Hub加载数据集
        print("Loading dataset 'nntsuzu/JParaCrawl'...")
        dataset = load_dataset("nntsuzu/JParaCrawl")

        # 只选小子集用于快速测试/迭代
        print("Selecting small subsets: train 0-199, test 200-219...")
        full_train = dataset['train']
        self.train_dataset = full_train.select(range(200))
        self.eval_dataset = full_train.select(range(200, 220))

        cutoff = int(self.config.get('cutoff_len', 512))
        
        def generate_prompt_and_tokenize(example):
            # JParaCrawl的数据格式是{'en': '...', 'ja': '...'}
            japanese_text = example.get('ja', '')
            output_text = example.get('en', '')
            
            # 构造 Chat 格式
            messages = [
                {"role": "system", "content": "You are a professional translator from Japanese to English."},
                {"role": "user", "content": f"Source: {japanese_text}"},
                {"role": "assistant", "content": output_text}
            ]
            
            full_ids = self.tokenizer.apply_chat_template(
                messages,
                tokenize=True,
                add_generation_prompt=False
            )
            
            prompt_messages = messages[:-1]
            prompt_ids = self.tokenizer.apply_chat_template(
                prompt_messages,
                tokenize=True,
                add_generation_prompt=True
            )
            
            prompt_len = len(prompt_ids)
            
            input_ids = full_ids
            labels = [-100] * prompt_len + input_ids[prompt_len:]
            
            if len(input_ids) > cutoff:
                input_ids = input_ids[:cutoff]
                labels = labels[:cutoff]
            
            pad_len = cutoff - len(input_ids)
            if pad_len > 0:
                input_ids += [self.tokenizer.pad_token_id] * pad_len
                labels += [-100] * pad_len
            
            attention_mask = [1 if id != self.tokenizer.pad_token_id else 0 for id in input_ids]

            return {
                "input_ids": input_ids,
                "labels": labels,
                "attention_mask": attention_mask
            }

        print("Tokenizing and masking data...")
        self.train_dataset = self.train_dataset.map(
            generate_prompt_and_tokenize, 
            batched=False, 
            remove_columns=self.train_dataset.column_names
        )
        self.eval_dataset = self.eval_dataset.map(
            generate_prompt_and_tokenize, 
            batched=False, 
            remove_columns=self.eval_dataset.column_names
        )
        
        self.train_dataset.set_format(type='torch', columns=['input_ids', 'labels', 'attention_mask'])
        self.eval_dataset.set_format(type='torch', columns=['input_ids', 'labels', 'attention_mask'])

        print(f"Sample Input IDs length: {len(self.train_dataset[0]['input_ids'])}")
        print(f"Sample Labels (first 10): {self.train_dataset[0]['labels'][:10]}")

    def compute_metrics(self, eval_preds):
        if self.bleu_metric is None:
            print("Loading BLEU metric...")
            self.bleu_metric = evaluate.load('sacrebleu')
        if self.enable_labse and self.labse_model is None:
            print("Loading LaBSE model for similarity evaluation...")
            self.labse_model = SentenceTransformer('sentence-transformers/LaBSE')

        preds, labels = eval_preds
        if isinstance(preds, tuple):
            preds = preds[0]
        
        # 将-100替换为pad_token_id，以便解码
        labels[labels == -100] = self.tokenizer.pad_token_id
        
        # 解码
        decoded_preds = self.tokenizer.batch_decode(preds, skip_special_tokens=True)
        decoded_labels = self.tokenizer.batch_decode(labels, skip_special_tokens=True)

        # 清理文本，移除空格等
        decoded_preds = [pred.strip() for pred in decoded_preds]
        decoded_labels = [[label.strip()] for label in decoded_labels] # sacrebleu需要list of lists

        # 计算BLEU
        bleu_result = self.bleu_metric.compute(predictions=decoded_preds, references=decoded_labels)

        if not self.enable_labse:
            return {
                "bleu": bleu_result["score"]
            }

        # 计算LaBSE相似度（可选，内存占用较大）
        label_texts = [item[0] for item in decoded_labels]
        embeddings_preds = self.labse_model.encode(decoded_preds, convert_to_tensor=True)
        embeddings_labels = self.labse_model.encode(label_texts, convert_to_tensor=True)
        cosine_scores = util.cos_sim(embeddings_preds, embeddings_labels)
        labse_similarity = np.mean(np.diag(cosine_scores.cpu().numpy()))

        return {
            "bleu": bleu_result["score"],
            "labse_similarity": labse_similarity
        }

    def train(self):
        self.model.train()

        output_dir = self.config.get('output_dir', './results')
        num_epochs = int(self.config.get('num_epochs', 1))
        per_device_batch = int(self.config.get('batch_size', 1))
        learning_rate = float(self.config.get('learning_rate', 5e-5))
        resume_from_checkpoint = self.config.get('resume_from_checkpoint', None)
        logging_steps = int(self.config.get('logging_steps', 10))
        logging_strategy = self.config.get('logging_strategy', 'steps')

        # Checkpointing / resume
        save_steps = int(self.config.get('save_steps', 10))
        save_total_limit = int(self.config.get('save_total_limit', 2))
        save_safetensors = bool(self.config.get('save_safetensors', True))

        # eval_during_training controls periodic eval; run_final_eval triggers one-off eval after training
        eval_active = self.eval_during_training or self.enable_eval  # keep legacy flag behavior

        # For best-model selection, Transformers requires eval/save strategies to match.
        # Use step-based eval+save so we both (a) can resume quickly and (b) can track best BLEU.
        if self.eval_during_training:
            eval_strategy = "steps"
            save_strategy = "steps"
            eval_steps = int(self.config.get('eval_steps', save_steps))
            # Keep them equal to ensure best checkpoint exists.
            save_steps = eval_steps
        else:
            eval_strategy = "no"
            save_strategy = "steps" if save_steps > 0 else "no"
            eval_steps = None

        training_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=num_epochs,
            per_device_train_batch_size=per_device_batch,
            per_device_eval_batch_size=per_device_batch,
            gradient_accumulation_steps=int(self.config.get('gradient_accumulation_steps', 1)),
            learning_rate=learning_rate,
            logging_dir=self.config.get('logging_dir', './logs'),
            logging_strategy=logging_strategy,
            logging_steps=logging_steps,
            logging_first_step=True,
            save_strategy=save_strategy,
            save_steps=save_steps if save_strategy == "steps" else None,
            save_total_limit=save_total_limit,
            save_safetensors=save_safetensors,
            fp16=False,
            remove_unused_columns=False,
            gradient_checkpointing=True,
            eval_strategy=eval_strategy,
            eval_steps=eval_steps if eval_strategy == "steps" else None,
            load_best_model_at_end=self.eval_during_training,
            metric_for_best_model="bleu",
            report_to=self.config.get('report_to', 'none'),
            disable_tqdm=bool(self.config.get('disable_tqdm', False)),
        )

        data_collator = DataCollatorForLanguageModeling(tokenizer=self.tokenizer, mlm=False)

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=self.train_dataset,
            eval_dataset=self.eval_dataset if (eval_active or self.run_final_eval) else None,
            data_collator=data_collator,
            compute_metrics=self.compute_metrics if (eval_active or self.run_final_eval) else None,
        )

        # Allow Ctrl+C to trigger a checkpoint on the next step boundary.
        try:
            signal.signal(signal.SIGINT, _handle_sigint)
        except Exception:
            pass
        trainer.add_callback(_GracefulInterruptCallback(trainer))

        # Auto-resume: if resume_from_checkpoint is 'auto'/True, pick latest checkpoint under output_dir.
        resolved_resume = None
        if isinstance(resume_from_checkpoint, str) and resume_from_checkpoint.lower() == 'auto':
            resolved_resume = _find_latest_checkpoint(output_dir)
        elif resume_from_checkpoint is True:
            resolved_resume = _find_latest_checkpoint(output_dir)
        elif isinstance(resume_from_checkpoint, str) and resume_from_checkpoint:
            resolved_resume = resume_from_checkpoint

        try:
            trainer.train(resume_from_checkpoint=resolved_resume)
        except KeyboardInterrupt:
            # If interrupted before next step_end callback, at least persist current weights + state.
            trainer.save_model()
            trainer.save_state()
            raise

        if self.run_final_eval:
            metrics = trainer.evaluate(eval_dataset=self.eval_dataset, metric_key_prefix="final_eval")
            print("Final evaluation:", metrics)
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
