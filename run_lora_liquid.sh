#!/usr/bin/env bash
set -euo pipefail

# LoRA fine-tune LiquidAI-350M with LlamaFactory (pip install llamafactory)
# Prereqs: translated train/test JSONL (see fill_with_baidu.py), torch/transformers/peft installed.

TRAIN_JSON=/home/cyw/pro/train_data/captions_0429_train_filled.jsonl
EVAL_JSON=/home/cyw/pro/train_data/captions_0429_test_filled.jsonl
MODEL_DIR=/home/cyw/LiquidAI-350M
OUTPUT_DIR=/home/cyw/pro/outputs/liquidai-350m-lora

# Force CPU only (unset CUDA)
export CUDA_VISIBLE_DEVICES=

llamafactory-cli train \
  --stage sft \
  --model_name_or_path "$MODEL_DIR" \
  --data_path "$TRAIN_JSON" \
  --eval_data_path "$EVAL_JSON" \
  --finetuning_type lora \
  --lora_rank 64 \
  --lora_alpha 128 \
  --lora_dropout 0.05 \
  --per_device_train_batch_size 1 \
  --per_device_eval_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --learning_rate 2e-4 \
  --weight_decay 0.01 \
  --num_train_epochs 3 \
  --lr_scheduler_type cosine \
  --warmup_ratio 0.03 \
  --logging_steps 10 \
  --eval_steps 200 \
  --save_steps 1000 \
  --save_total_limit 3 \
  --gradient_checkpointing True \
  --output_dir "$OUTPUT_DIR" \
  --report_to none \
  --max_seq_length 256 \
  --cutoff_len 256 \
  --dataset_format instruction

# To merge LoRA after training:
# llamafactory-cli export --model_name_or_path $MODEL_DIR --adapter_name_or_path $OUTPUT_DIR --export_dir $OUTPUT_DIR/merged --export_legacy_format False
