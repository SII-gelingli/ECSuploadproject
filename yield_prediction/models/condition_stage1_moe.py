"""Stage-1 MoE 版本: shared encoder + N 个 expert head 套件 + soft router。

设计 (省 GPU 内存的轻量 MoE):
- encoder (共享): fp → hidden
- router: hidden → N 个 expert 权重 (softmax)
- N 个 expert head 套件: 每个是一组 9 个 nn.Linear(hidden, num_classes[k])
- output[head] = Σ_i w_i * expert_i.head(hidden)

参数量 ≈ baseline + (N-1) × (9 个 head 的 Linear) ≈ baseline + 0.5M-1M
比 N 个完整模型 (N × 7M) 省很多。

训练时加 load balancing loss 防止 router 退化为单 expert。
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, Optional

from .condition_stage1 import HEAD_KEYS


class ConditionStage1MoE(nn.Module):
    """共享 encoder + N expert head sets + soft router."""

    def __init__(self, num_classes: Dict[str, int], fp_dim: int = 6144,
                 hidden_dims=(1024, 768, 512), dropout: float = 0.3,
                 num_experts: int = 4, router_hidden: int = 256,
                 router_temperature: float = 1.0,
                 extra_heads=None):
        super().__init__()
        self.num_experts = num_experts
        self.router_temperature = router_temperature

        # 共享 encoder
        layers = []
        prev = fp_dim
        for h in hidden_dims:
            layers += [nn.Linear(prev, h), nn.BatchNorm1d(h),
                       nn.GELU(), nn.Dropout(dropout)]
            prev = h
        self.encoder = nn.Sequential(*layers)
        self.hidden = prev

        # Router (gating network)
        self.router = nn.Sequential(
            nn.Linear(prev, router_hidden),
            nn.LayerNorm(router_hidden),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(router_hidden, num_experts),
        )

        # N 个 expert head 套件 (每个 expert 含 9 + extra 个 head)
        all_heads = list(HEAD_KEYS) + list(extra_heads or [])
        self.head_keys = [k for k in all_heads if k in num_classes]
        # ModuleList of ModuleDict: experts[i][head] = Linear
        self.experts = nn.ModuleList([
            nn.ModuleDict({k: nn.Linear(prev, num_classes[k]) for k in self.head_keys})
            for _ in range(num_experts)
        ])

    def forward(self, fp: torch.Tensor, return_route: bool = False) -> Dict[str, torch.Tensor]:
        h = self.encoder(fp)  # (B, hidden)
        router_logits = self.router(h)  # (B, N)
        weights = F.softmax(router_logits / self.router_temperature, dim=-1)  # (B, N)

        # 对每个 head: 把 N 个 expert 输出加权求和
        merged = {}
        for k in self.head_keys:
            # 收集所有 expert 的 logits, (N, B, num_classes_k)
            expert_logits = torch.stack([expert[k](h) for expert in self.experts], dim=0)
            # weight (B, N) → (N, B, 1) for broadcasting
            w = weights.t().unsqueeze(-1)  # (N, B, 1)
            merged[k] = (w * expert_logits).sum(dim=0)  # (B, num_classes_k)

        if return_route:
            return merged, weights
        return merged

    def load_balancing_loss(self, weights: torch.Tensor) -> torch.Tensor:
        """鼓励 router 使用所有 expert (avg 用量接近 1/N)。

        Importance loss: var(平均 weight 跨样本) — 越小越均衡
        """
        avg_w = weights.mean(dim=0)  # (N,)
        ideal = 1.0 / self.num_experts
        # Coefficient of variation squared
        return ((avg_w - ideal) ** 2).sum() * self.num_experts

    def encode(self, fp: torch.Tensor) -> torch.Tensor:
        return self.encoder(fp)
