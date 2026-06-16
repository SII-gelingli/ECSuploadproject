"""Stage-1 Hier + Set 联合架构。

设计:
- encoder (共享)
- 6 个普通 single head (anode/cathode/cell_type/electrolyte/ligand/additive)
- reagent_class head (47 类): 先预测反应类型 (粗类)
- 3 个 set head (DETR-style, K=4 slot 每个):
    solvent_set_head    : 输入 encoder_h
    catalyst_set_head   : 输入 encoder_h
    reagent_set_head    : 输入 [encoder_h, reagent_class_emb] ★ 化学层次
- 训练 teacher forcing reagent_class label

推理时可选:
- soft: 用 reagent_class argmax 取 embed
- hard constraint: 屏蔽不属于预测 class 的 reagent SMILES
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, Optional


from .condition_stage1 import HEAD_KEYS
PARALLEL_HEADS = ['anode', 'cathode', 'cell_type', 'electrolyte', 'ligand', 'additive']
SET_HEADS = ['solvent', 'reagent', 'catalyst']
K_SLOTS = 4


class ConditionStage1HierSet(nn.Module):
    def __init__(self, num_classes: Dict[str, int], fp_dim: int = 6144,
                 hidden_dims=(1024, 768, 512), dropout: float = 0.3,
                 k_slots: int = K_SLOTS,
                 class_embed_dim: int = 32):
        super().__init__()
        self.k_slots = k_slots
        self.class_embed_dim = class_embed_dim

        # 共享 encoder
        layers = []
        prev = fp_dim
        for h in hidden_dims:
            layers += [nn.Linear(prev, h), nn.BatchNorm1d(h),
                       nn.GELU(), nn.Dropout(dropout)]
            prev = h
        self.encoder = nn.Sequential(*layers)
        self.hidden = prev

        # 6 个普通 single head + ligand/additive
        single_heads = list(PARALLEL_HEADS)
        self.single_heads = nn.ModuleDict({
            k: nn.Linear(prev, num_classes[k]) for k in single_heads if k in num_classes
        })

        # reagent_class head (先预测)
        self.reagent_class_head = nn.Linear(prev, num_classes['reagent_class'])
        self.reagent_class_embed = nn.Embedding(num_classes['reagent_class'], class_embed_dim)

        # 3 个 set head
        # solvent/catalyst: 输入 encoder_h
        # reagent: 输入 [encoder_h, class_emb] ← 化学层次
        self.solvent_set = nn.Linear(prev, k_slots * (num_classes['solvent'] + 1))
        self.catalyst_set = nn.Linear(prev, k_slots * (num_classes['catalyst'] + 1))
        self.reagent_set = nn.Linear(prev + class_embed_dim,
                                     k_slots * (num_classes['reagent'] + 1))

        self.num_classes = num_classes
        self.no_obj_idx = {k: num_classes[k] for k in SET_HEADS}  # = N (vocab 之后 1 位)

    def forward(self, fp: torch.Tensor,
                teacher_class: Optional[torch.Tensor] = None
                ) -> Dict[str, torch.Tensor]:
        h = self.encoder(fp)  # (B, hidden)
        out = {}

        # 1. 普通 single head
        for k, head in self.single_heads.items():
            out[k] = head(h)

        # 2. reagent_class (粗类预测)
        rc_logits = self.reagent_class_head(h)
        out['reagent_class'] = rc_logits

        # 3. set head: solvent / catalyst — 直接用 encoder_h
        B = h.size(0)
        out['solvent'] = self.solvent_set(h).view(B, self.k_slots, -1)
        out['catalyst'] = self.catalyst_set(h).view(B, self.k_slots, -1)

        # 4. reagent set head: 接收 reagent_class embedding (teacher forcing 或 argmax)
        if teacher_class is not None:
            rc_idx = teacher_class
        else:
            rc_idx = rc_logits.argmax(dim=-1)
        rc_emb = self.reagent_class_embed(rc_idx)  # (B, class_embed_dim)
        reagent_input = torch.cat([h, rc_emb], dim=-1)
        out['reagent'] = self.reagent_set(reagent_input).view(B, self.k_slots, -1)

        return out
