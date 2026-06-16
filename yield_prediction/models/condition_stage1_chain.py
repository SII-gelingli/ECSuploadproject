"""Stage-1 链式 (chain) 解码版本：

精确按用户要求, 只对 solvent → electrolyte → reagent 这条**化学组合链**做条件依赖,
其他 6 个 head (cell_type, anode, cathode, catalyst, ligand, additive) 仍然并行独立。

这样设计的化学理由:
- 反应器配置 (cell_type/anode/cathode) 主要由 lab 偏好决定, 与具体试剂耦合弱
- catalyst/ligand/additive 多数 ABSENT, cond 信号噪声大
- **solvent → electrolyte → reagent 是最强的化学耦合链** (如 MeCN→LiClO4→TEMPO 是典型电氧化组合)

训练时 teacher forcing: solvent_label → electrolyte 输入, electrolyte_label → reagent 输入
推理时: 用上一个 head 的 argmax 取 embedding
"""
import torch
import torch.nn as nn
from typing import Dict, Optional


HEAD_KEYS = ['anode', 'cathode', 'cell_type', 'solvent', 'electrolyte',
             'catalyst', 'reagent', 'ligand', 'additive']

PARALLEL_HEADS = ['cell_type', 'anode', 'cathode', 'catalyst', 'ligand', 'additive']
CHAIN_HEADS = ['solvent', 'electrolyte', 'reagent']  # 顺序: solvent → electrolyte → reagent


class ConditionStage1Chain(nn.Module):
    """混合并行+链式: 6 head 并行 + (solvent→electrolyte→reagent) 链。

    特性:
    - solvent: 输入 h, 输出 solvent logits, 取 argmax 或 GT label embedding → cat
    - electrolyte: 输入 [h, solvent_embed], 输出 electrolyte logits, embed → cat
    - reagent: 输入 [h, solvent_embed, electrolyte_embed], 输出 reagent logits
    - 其他 6 head: 输入 h, 并行预测
    """

    def __init__(self, num_classes: Dict[str, int], fp_dim: int = 6144,
                 hidden_dims=(1024, 768, 512), dropout: float = 0.3,
                 cond_embed_dim: int = 32):
        super().__init__()
        layers = []
        prev = fp_dim
        for h in hidden_dims:
            layers += [nn.Linear(prev, h), nn.BatchNorm1d(h),
                       nn.GELU(), nn.Dropout(dropout)]
            prev = h
        self.encoder = nn.Sequential(*layers)
        self.hidden = prev
        self.cond_embed_dim = cond_embed_dim

        # 并行 head: 输入 = h
        self.parallel_heads = nn.ModuleDict({
            k: nn.Linear(prev, num_classes[k]) for k in PARALLEL_HEADS
        })

        # 链式 head 的 embedding 表 (solvent + electrolyte, reagent 不需要 embed)
        self.chain_embed = nn.ModuleDict({
            'solvent': nn.Embedding(num_classes['solvent'], cond_embed_dim),
            'electrolyte': nn.Embedding(num_classes['electrolyte'], cond_embed_dim),
        })

        # 链式 head 的分类器
        self.chain_heads = nn.ModuleDict({
            'solvent':     nn.Linear(prev, num_classes['solvent']),
            'electrolyte': nn.Linear(prev + cond_embed_dim, num_classes['electrolyte']),
            'reagent':     nn.Linear(prev + 2 * cond_embed_dim, num_classes['reagent']),
        })

    def forward(self, fp: torch.Tensor,
                teacher_labels: Optional[Dict[str, torch.Tensor]] = None
                ) -> Dict[str, torch.Tensor]:
        h = self.encoder(fp)
        logits: Dict[str, torch.Tensor] = {}

        # 1. 并行 head
        for k in PARALLEL_HEADS:
            logits[k] = self.parallel_heads[k](h)

        # 2. 链式 head: solvent → electrolyte → reagent
        # Solvent
        logits['solvent'] = self.chain_heads['solvent'](h)
        sol_label = teacher_labels['solvent'] if (teacher_labels and 'solvent' in teacher_labels) else logits['solvent'].argmax(dim=-1)
        sol_emb = self.chain_embed['solvent'](sol_label)

        # Electrolyte (given solvent)
        logits['electrolyte'] = self.chain_heads['electrolyte'](torch.cat([h, sol_emb], dim=-1))
        elc_label = teacher_labels['electrolyte'] if (teacher_labels and 'electrolyte' in teacher_labels) else logits['electrolyte'].argmax(dim=-1)
        elc_emb = self.chain_embed['electrolyte'](elc_label)

        # Reagent (given solvent + electrolyte)
        logits['reagent'] = self.chain_heads['reagent'](torch.cat([h, sol_emb, elc_emb], dim=-1))

        return logits

    def encode(self, fp: torch.Tensor) -> torch.Tensor:
        return self.encoder(fp)
