"""Stage-1 Set Prediction 模型 (DETR-style)。

对 solvent/reagent/catalyst 做 set 预测 (K=4 slots, 每 slot 输出 N+1 类含 no_object)。
其他 head (anode/cathode/cell_type/electrolyte/ligand/additive + reagent_class) 仍是 softmax 单标签。

训练用 Hungarian matching 在 K 个 slot 与真实 set 间找最优匹配。
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, List, Tuple


from .condition_stage1 import HEAD_KEYS  # 9 head 总名单
PARALLEL_HEADS = ['anode', 'cathode', 'cell_type', 'electrolyte', 'ligand', 'additive']
SET_HEADS = ['solvent', 'reagent', 'catalyst']
K_SLOTS = 4   # 每个 set head 输出 K 个 slot


class ConditionStage1Set(nn.Module):
    def __init__(self, num_classes: Dict[str, int], fp_dim: int = 6144,
                 hidden_dims=(1024, 768, 512), dropout: float = 0.3,
                 extra_heads=None, k_slots: int = K_SLOTS):
        super().__init__()
        self.k_slots = k_slots
        layers = []
        prev = fp_dim
        for h in hidden_dims:
            layers += [nn.Linear(prev, h), nn.BatchNorm1d(h),
                       nn.GELU(), nn.Dropout(dropout)]
            prev = h
        self.encoder = nn.Sequential(*layers)
        self.hidden = prev

        # 单标签 (softmax) head
        single_heads = list(PARALLEL_HEADS) + list(extra_heads or [])
        self.single_heads = nn.ModuleDict({
            k: nn.Linear(prev, num_classes[k])
            for k in single_heads if k in num_classes
        })
        # set head: 输出 K * (N + 1), 多 1 维是 no_object
        # 等价于 K 个独立 (N+1)-class softmax slot
        self.set_heads = nn.ModuleDict({
            k: nn.Linear(prev, k_slots * (num_classes[k] + 1))
            for k in SET_HEADS if k in num_classes
        })
        self.num_classes = num_classes
        self.no_obj_idx = {k: num_classes[k] for k in SET_HEADS}  # 用 N (vocab 之后 1 位) 当 no_obj

    def encode(self, fp: torch.Tensor) -> torch.Tensor:
        return self.encoder(fp)

    def forward(self, fp: torch.Tensor) -> Dict[str, torch.Tensor]:
        h = self.encoder(fp)
        out = {}
        for k, head in self.single_heads.items():
            out[k] = head(h)  # (B, num_classes[k])
        for k, head in self.set_heads.items():
            # (B, K * (N+1)) → (B, K, N+1)
            raw = head(h)
            out[k] = raw.view(h.size(0), self.k_slots, -1)
        return out


def hungarian_set_loss(slot_logits: torch.Tensor, target_set_padded: torch.Tensor,
                       target_lens: torch.Tensor, no_obj_idx: int,
                       class_weights: torch.Tensor = None) -> torch.Tensor:
    """
    Hungarian matching loss for one set head.

    Args:
        slot_logits: (B, K, N+1)
        target_set_padded: (B, K) int — 真实 set 的 idx, padding 用 no_obj_idx
        target_lens: (B,) int — 每 reaction 的真实 set 大小
        no_obj_idx: int — "no object" 的索引 (== N)
        class_weights: (N+1,) 可选, 含 no_obj 的权重

    Returns:
        scalar loss
    """
    from scipy.optimize import linear_sum_assignment

    B, K, NC = slot_logits.shape
    log_probs = F.log_softmax(slot_logits, dim=-1)
    losses = []
    for b in range(B):
        T = int(target_lens[b].item())
        # 构建 cost matrix (K, K): K slot × K "目标位"
        # 前 T 个目标位是真实 idx, 剩下 K-T 个目标位是 no_obj
        # cost[i, t] = -log P_i(target[t])
        # 这样 Hungarian 找出 K slot 与 K 目标位的最优一对一匹配
        target_extended = target_set_padded[b].clone()
        # 真实 set 在前 T 位, target_lens 之后 padding 已经是 no_obj_idx
        # cost[i, t] = -log P_i(target_extended[t])
        cost = -log_probs[b, :, target_extended]  # (K, K)
        cost_np = cost.detach().cpu().numpy()
        rows, cols = linear_sum_assignment(cost_np)
        # 匹配后 loss
        if class_weights is not None:
            w = class_weights[target_extended[cols]]  # (K,)
            loss_b = (cost[rows, cols] * w).sum() / max(1, w.sum())
        else:
            loss_b = cost[rows, cols].mean()
        losses.append(loss_b)
    return torch.stack(losses).mean()


def decode_set(slot_logits: torch.Tensor, no_obj_idx: int) -> List[List[int]]:
    """每个 slot 取 argmax, 去除 no_object 和重复, 返回 set list。

    Args:
        slot_logits: (B, K, N+1)
        no_obj_idx: N

    Returns:
        list of B element, 每个是 list of int (去重 + 排除 no_obj)
    """
    preds = slot_logits.argmax(dim=-1).cpu().numpy()  # (B, K)
    sets = []
    for b in range(preds.shape[0]):
        seen = set()
        s = []
        for p in preds[b]:
            if p != no_obj_idx and p not in seen:
                seen.add(int(p)); s.append(int(p))
        sets.append(s)
    return sets


def decode_set_topk(slot_logits: torch.Tensor, no_obj_idx: int, K_total: int = 20) -> List[List[int]]:
    """从所有 slot 的 logits 取 Top-K 候选 (跨 slot, 去 no_obj, 去重)。

    Args:
        slot_logits: (B, K, N+1)
        no_obj_idx: N
        K_total: 总候选数

    Returns:
        list of B element, 每个是按概率排序的 list of int (去 no_obj 去重, 长度 <= K_total)
    """
    B, K, NC = slot_logits.shape
    probs = F.softmax(slot_logits, dim=-1)  # (B, K, N+1)
    # 对每个 slot 取 max 概率类 → 实际上更好的是把所有 (slot, class) pair 当候选, 按概率排序
    # 把所有 slot 的概率"取 max"得到 (B, N+1) 然后取 Top-K_total
    max_over_slots = probs.max(dim=1).values  # (B, N+1)
    max_over_slots[..., no_obj_idx] = -1.0  # 屏蔽 no_obj
    topk = max_over_slots.topk(min(K_total, NC), dim=-1).indices  # (B, K_total)
    return topk.cpu().numpy().tolist()
