"""
Stage-2 用量回归模型：输入 reaction FP + Stage-1 种类的 embedding，
输出 7 个用量字段。Masked MSE 训练（只在 mask=1 的样本上算 loss）。

训练用 ground-truth 种类 index（teacher forcing），推理用 Stage-1 argmax。
"""
import torch
import torch.nn as nn
from typing import Dict


AMOUNT_FIELDS = ['catalyst_equiv', 'reagent_equiv', 'ligand_equiv', 'additive_equiv',
                 'electrolyte_M', 'current_mA', 'current_density',
                 'potential_V', 'temperature_C', 'time_h']
HEAD_KEYS = ['anode', 'cathode', 'cell_type', 'solvent', 'electrolyte',
             'catalyst', 'reagent', 'ligand', 'additive']
CATEGORY_EMB_DIM = 32


class ConditionStage2(nn.Module):
    """用量回归器。"""

    def __init__(self, num_classes: Dict[str, int], fp_dim: int = 6144,
                 emb_dim: int = CATEGORY_EMB_DIM, hidden_dims=(512, 256),
                 dropout: float = 0.2):
        super().__init__()
        # 每个 head 一个 embedding
        self.embeddings = nn.ModuleDict({
            k: nn.Embedding(num_classes[k], emb_dim)
            for k in HEAD_KEYS if k in num_classes
        })
        cat_total = emb_dim * len(self.embeddings)

        layers = []
        prev = fp_dim + cat_total
        for h in hidden_dims:
            layers += [
                nn.Linear(prev, h),
                nn.BatchNorm1d(h),
                nn.GELU(),
                nn.Dropout(dropout),
            ]
            prev = h
        self.encoder = nn.Sequential(*layers)

        # 7 个回归 head
        self.heads = nn.ModuleDict({
            f: nn.Linear(prev, 1) for f in AMOUNT_FIELDS
        })

    def forward(self, fp: torch.Tensor, category_indices: Dict[str, torch.Tensor]) -> Dict[str, torch.Tensor]:
        """
        Args:
            fp: [B, fp_dim]
            category_indices: dict head_name → [B] long tensor of class indices
        Returns:
            dict field_name → [B] regression output (normalized)
        """
        embs = [self.embeddings[k](category_indices[k]) for k in HEAD_KEYS if k in self.embeddings]
        cat_emb = torch.cat(embs, dim=-1)
        x = torch.cat([fp, cat_emb], dim=-1)
        h = self.encoder(x)
        return {f: head(h).squeeze(-1) for f, head in self.heads.items()}
