"""Conditional decoding 版本的 Stage-1：head 顺序预测，前面 head 的结果作为后续 head 输入。

顺序: cell_type → anode → cathode → solvent → electrolyte → reagent → catalyst → ligand → additive

训练时 teacher forcing（用 GT label 取 embedding），推理时用上一个 head 的 argmax。
"""
import torch
import torch.nn as nn
from typing import Dict, Optional


HEAD_ORDER = ['cell_type', 'anode', 'cathode', 'solvent', 'electrolyte',
              'reagent', 'catalyst', 'ligand', 'additive']
HEAD_KEYS = HEAD_ORDER  # 保持兼容


class ConditionStage1Cond(nn.Module):
    """Conditional 顺序解码 9 个 head。

    每个 head_i 的输入 = [encoder_h, embed(head_0_label), ..., embed(head_{i-1}_label)]
    """

    def __init__(self, num_classes: Dict[str, int], fp_dim: int = 6144,
                 hidden_dims=(1024, 768, 512), dropout: float = 0.3,
                 cond_embed_dim: int = 32):
        super().__init__()
        # encoder
        layers = []
        prev = fp_dim
        for h in hidden_dims:
            layers += [nn.Linear(prev, h), nn.BatchNorm1d(h),
                       nn.GELU(), nn.Dropout(dropout)]
            prev = h
        self.encoder = nn.Sequential(*layers)
        self.hidden = prev
        self.cond_embed_dim = cond_embed_dim

        # 每个 head 的 embedding 表
        self.head_embed = nn.ModuleDict({
            k: nn.Embedding(num_classes[k], cond_embed_dim) for k in HEAD_ORDER
        })
        # 每个 head 的分类器: encoder_hidden + (前面 head 数量 × cond_embed_dim)
        self.classifiers = nn.ModuleDict()
        for i, k in enumerate(HEAD_ORDER):
            cond_dim = i * cond_embed_dim
            self.classifiers[k] = nn.Linear(prev + cond_dim, num_classes[k])

    def forward(self, fp: torch.Tensor,
                teacher_labels: Optional[Dict[str, torch.Tensor]] = None
                ) -> Dict[str, torch.Tensor]:
        h = self.encoder(fp)
        logits = {}
        prev_embeds = []  # list of (B, cond_embed_dim)
        for k in HEAD_ORDER:
            if prev_embeds:
                cat_inp = torch.cat([h] + prev_embeds, dim=-1)
            else:
                cat_inp = h
            logits[k] = self.classifiers[k](cat_inp)
            # 决定下一步用哪个 label 取 embedding
            if teacher_labels is not None and k in teacher_labels:
                lbl = teacher_labels[k]
            else:
                lbl = logits[k].argmax(dim=-1)
            prev_embeds.append(self.head_embed[k](lbl))
        return logits

    def encode(self, fp: torch.Tensor) -> torch.Tensor:
        return self.encoder(fp)
