"""LoRA SFT for Qwen3-14B on alkene-EC condition recommendation.

Differences from train_qwen_lora.py (Qwen2.5-3B baseline):
- MODEL_DIR: Qwen3-14B
- num_train_epochs=1 (3B run showed eval_loss bottoms at epoch 1, overfits after)
- learning_rate=1e-4 (more conservative for larger model)
- OUTPUT_DIR: qwen3_14b_lora_v1
"""
import json
import os
import sys
from pathlib import Path
from dataclasses import dataclass

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import torch
from torch.utils.data import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
)
from peft import LoraConfig, get_peft_model, TaskType


PROJECT = Path("/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/yield_prediction")
MODEL_DIR = "/inspire/hdd/global_public/public_models/Qwen/Qwen3-14B"
DATA_DIR = PROJECT / "data_qwen_sft_v3"
OUTPUT_DIR = PROJECT / "checkpoints" / "qwen3_14b_clean_v1"
MAX_LEN = 1024


class JsonlChatDataset(Dataset):
    def __init__(self, jsonl_path: Path, tokenizer, max_len: int = MAX_LEN):
        self.tok = tokenizer
        self.max_len = max_len
        self.rows = []
        with open(jsonl_path) as f:
            for line in f:
                self.rows.append(json.loads(line)["messages"])

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, idx):
        messages = self.rows[idx]
        prompt_text = self.tok.apply_chat_template(
            messages[:-1], tokenize=False, add_generation_prompt=True
        )
        full_text = self.tok.apply_chat_template(messages, tokenize=False)
        prompt_ids = self.tok(prompt_text, add_special_tokens=False).input_ids
        full_ids = self.tok(full_text, add_special_tokens=False).input_ids
        full_ids = full_ids[: self.max_len]
        prompt_len = min(len(prompt_ids), len(full_ids))
        labels = [-100] * prompt_len + full_ids[prompt_len:]
        return {
            "input_ids": full_ids,
            "labels": labels,
            "attention_mask": [1] * len(full_ids),
        }


@dataclass
class PadCollator:
    pad_id: int

    def __call__(self, batch):
        max_len = max(len(b["input_ids"]) for b in batch)
        out = {"input_ids": [], "labels": [], "attention_mask": []}
        for b in batch:
            pad = max_len - len(b["input_ids"])
            out["input_ids"].append(b["input_ids"] + [self.pad_id] * pad)
            out["labels"].append(b["labels"] + [-100] * pad)
            out["attention_mask"].append(b["attention_mask"] + [0] * pad)
        return {k: torch.tensor(v, dtype=torch.long) for k, v in out.items()}


def main():
    tok = AutoTokenizer.from_pretrained(MODEL_DIR, trust_remote_code=True)
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token

    train_ds = JsonlChatDataset(DATA_DIR / "train.jsonl", tok)
    val_ds = JsonlChatDataset(DATA_DIR / "val.jsonl", tok)
    print(f"train={len(train_ds)}  val={len(val_ds)}", flush=True)

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_DIR,
        torch_dtype=torch.bfloat16,
        attn_implementation="eager",
    )
    model.config.use_cache = False

    lora = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj",
        ],
    )
    model = get_peft_model(model, lora)
    model.print_trainable_parameters()

    args = TrainingArguments(
        output_dir=str(OUTPUT_DIR),
        num_train_epochs=1,
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        gradient_accumulation_steps=4,
        learning_rate=1e-4,
        lr_scheduler_type="cosine",
        warmup_ratio=0.03,
        weight_decay=0.0,
        bf16=True,
        logging_steps=20,
        eval_strategy="steps",
        eval_steps=200,
        save_strategy="steps",
        save_steps=200,
        save_total_limit=2,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        gradient_checkpointing=False,
        max_grad_norm=1.0,
        dataloader_num_workers=4,
        report_to=[],
        ddp_find_unused_parameters=False,
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        data_collator=PadCollator(pad_id=tok.pad_token_id),
        processing_class=tok,
    )
    trainer.train()
    trainer.save_model(str(OUTPUT_DIR / "best"))
    tok.save_pretrained(str(OUTPUT_DIR / "best"))


if __name__ == "__main__":
    main()
