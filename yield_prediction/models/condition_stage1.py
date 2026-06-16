"""
Stage-1 种类分类模型：8 个 head，每个含 ABSENT 类。
更宽的 encoder：6144 → 1024 → 768 → 512，GELU + BatchNorm + Dropout 0.3。
"""
import torch
import torch.nn as nn
from typing import Dict


HEAD_KEYS = ['anode', 'cathode', 'cell_type', 'solvent', 'electrolyte',
             'catalyst', 'reagent', 'ligand', 'additive']


class ConditionStage1(nn.Module):
    """8 个分类头的多任务分类器。

    输入: reaction fingerprint (6144D)
    输出: 各 head 的 logits dict
    """

    def __init__(self, num_classes: Dict[str, int], fp_dim: int = 6144,
                 hidden_dims=(1024, 768, 512), dropout: float = 0.3,
                 extra_heads=None):
        """
        extra_heads: 可选的额外 head 名列表（如 ['reagent_class']）, 需在 num_classes 中提供。
        """
        super().__init__()
        layers = []
        prev = fp_dim
        for h in hidden_dims:
            layers += [
                nn.Linear(prev, h),
                nn.BatchNorm1d(h),
                nn.GELU(),
                nn.Dropout(dropout),
            ]
            prev = h
        self.encoder = nn.Sequential(*layers)
        self.hidden = prev

        all_heads = list(HEAD_KEYS) + list(extra_heads or [])
        self.heads = nn.ModuleDict({
            k: nn.Linear(prev, num_classes[k])
            for k in all_heads if k in num_classes
        })

    def forward(self, fp: torch.Tensor) -> Dict[str, torch.Tensor]:
        h = self.encoder(fp)
        return {k: head(h) for k, head in self.heads.items()}

    def encode(self, fp: torch.Tensor) -> torch.Tensor:
        """只返回 encoder 输出，供 Stage-2 复用特征。"""
        return self.encoder(fp)
