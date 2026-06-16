"""Stage-1 Hier + Set V3 联合架构 — 用 CLASSIFICATION_DESIGN_V3.md 的化学分类。

V3 vs v2 的差异:
1. **electrolyte 拆双 head**: cation (23) + anion (26) 互独立; 原 electrolyte single head 移除
2. **catalyst tags multi-label**: 4 bit (mediator/photoredox/HAT/chiral), sigmoid + BCE
3. **reagent_class 47→103**: 用 v3 化学分类(无 OTHER, 全有化学意义)
4. **catalyst_class hier signal**: 49 类粗类 → embedding → catalyst set head (新增 hier)
5. **solvent_class hier signal**: 27 类粗类 → embedding → solvent set head (新增 hier)
6. **anode/cathode 23→15**: 用 v3 材料家族
7. **additive 多 head**: additive_class_v3 (105 类) — single

保留 v2 的:
- 3 个 set head (solvent/reagent/catalyst, K=4 slot, Hungarian matching)
- set head 仍输出原 SMILES vocab(具体 SMILES, 不是粗类)
"""
import torch
import torch.nn as nn
from typing import Dict, Optional


# v3 single 类 head
SINGLE_HEADS_V3 = [
    'anode_material',     # 15 (粗类: 碳/Pt/牺牲极...)
    'cathode_material',   # 15
    'cell_class_v3',      # 4
    'electrolyte_cation', # 23
    'electrolyte_anion',  # 26
    'ligand_class_v3',    # 20
    'additive_class_v3',  # 105
]
# 细粒度电极 (材料 × 形状, anode 43 / cathode 49 类)
# 例: carbon_felt, graphite_rod, platinum_plate, RVC, BDD, glassy_carbon ...
# label key in records = anode_fine / cathode_fine, vocab in stats.num_classes
FINE_ELECTRODE_HEADS = ['anode_fine', 'cathode_fine']
# v3 hier (粗类 → embedding → set head)
HIER_KEYS = [
    'reagent_class_v3',    # 103 → reagent set
    'catalyst_class_v3',   # 49 → catalyst set
    'solvent_class_v3',    # 27 → solvent set
]
# v3 hier → single SMILES head (类喂给单 head 在具体 SMILES vocab 内选)
# label 名 (SMILES vocab): class 名
SMI_FROM_CLASS = {
    'ligand':   'ligand_class_v3',    # 20 类 → 176 SMILES
    'additive': 'additive_class_v3',  # 105 类 → 105 SMILES
}
# set head (具体 SMILES vocab, K-slot)
SET_HEADS = ['solvent', 'reagent', 'catalyst']
# catalyst mech tags (multi-label, 4 bits)
CAT_TAG_KEY = 'catalyst_mech_tags'
CAT_TAG_BITS = 4

K_SLOTS = 4


class ConditionStage1HierSetV3(nn.Module):
    def __init__(self, num_classes: Dict[str, int],
                 num_classes_v3: Dict[str, int],
                 fp_dim: int = 6144,
                 hidden_dims=(1024, 768, 512), dropout: float = 0.3,
                 k_slots: int = K_SLOTS,
                 class_embed_dim: int = 32,
                 cat_tag_embed_dim: int = 8):
        super().__init__()
        self.k_slots = k_slots
        self.class_embed_dim = class_embed_dim
        self.cat_tag_embed_dim = cat_tag_embed_dim

        # 共享 encoder
        layers = []
        prev = fp_dim
        for h in hidden_dims:
            layers += [nn.Linear(prev, h), nn.BatchNorm1d(h),
                       nn.GELU(), nn.Dropout(dropout)]
            prev = h
        self.encoder = nn.Sequential(*layers)
        self.hidden = prev

        # === v3 single heads ===
        self.single_heads = nn.ModuleDict({
            k: nn.Linear(prev, num_classes_v3[k]) for k in SINGLE_HEADS_V3
        })
        # === 细粒度电极 head (anode_fine ~43 / cathode_fine ~49 类) ===
        self.fine_electrode_heads = nn.ModuleDict({
            'anode_fine': nn.Linear(prev, num_classes['anode_fine']),
            'cathode_fine': nn.Linear(prev, num_classes['cathode_fine']),
        })

        # === v3 hier class heads (先预测粗类) ===
        self.hier_class_heads = nn.ModuleDict({
            k: nn.Linear(prev, num_classes_v3[k]) for k in HIER_KEYS
        })
        # 每个粗类 head 各自 embedding (用于 set head 输入)
        self.hier_class_embed = nn.ModuleDict({
            k: nn.Embedding(num_classes_v3[k], class_embed_dim) for k in HIER_KEYS
        })
        # ligand_class_v3 / additive_class_v3 (在 single_heads 已经有 logits head)
        # 再加一份 embedding 喂给 SMILES single head
        self.smi_class_embed = nn.ModuleDict({
            cls_name: nn.Embedding(num_classes_v3[cls_name], class_embed_dim)
            for cls_name in SMI_FROM_CLASS.values()
        })

        # === catalyst tags multi-label head (4 bits) ===
        self.catalyst_tag_head = nn.Linear(prev, CAT_TAG_BITS)
        # tag bits → 一个小 embedding(用 Linear from 4-d float to dim)
        self.catalyst_tag_embed = nn.Linear(CAT_TAG_BITS, cat_tag_embed_dim)

        # === set heads (具体 SMILES vocab, K slot) ===
        self.solvent_set = nn.Linear(prev + class_embed_dim,
                                      k_slots * (num_classes['solvent'] + 1))
        self.catalyst_set = nn.Linear(prev + class_embed_dim + cat_tag_embed_dim,
                                       k_slots * (num_classes['catalyst'] + 1))
        self.reagent_set = nn.Linear(prev + class_embed_dim,
                                      k_slots * (num_classes['reagent'] + 1))

        # === ligand / additive single SMILES heads (用 class hier signal) ===
        # 输出: 具体 SMILES vocab (ligand=176, additive=105)
        self.smi_single_heads = nn.ModuleDict({
            smi_name: nn.Linear(prev + class_embed_dim, num_classes[smi_name])
            for smi_name in SMI_FROM_CLASS  # 'ligand', 'additive'
        })

        self.num_classes = num_classes
        self.num_classes_v3 = num_classes_v3
        # no_obj index for set heads = vocab size N (vocab 之后 1 位)
        self.no_obj_idx = {k: num_classes[k] for k in SET_HEADS}

    def forward(self, fp: torch.Tensor,
                teacher: Optional[Dict[str, torch.Tensor]] = None
                ) -> Dict[str, torch.Tensor]:
        """
        teacher: 若不为 None, 包含 reagent_class_v3 / catalyst_class_v3 / solvent_class_v3 /
                 catalyst_mech_tags 的 GT, 用于 teacher forcing。
        """
        h = self.encoder(fp)  # (B, hidden)
        out = {}

        # 1. v3 single heads
        for k, head in self.single_heads.items():
            out[k] = head(h)
        # 1b. V2 细粒度电极 heads
        for k, head in self.fine_electrode_heads.items():
            out[k] = head(h)

        # 2. hier class heads (粗类 logits)
        for k, head in self.hier_class_heads.items():
            out[k] = head(h)

        # 3. catalyst tags (multi-label, 4 bit logits — sigmoid + BCE)
        out[CAT_TAG_KEY] = self.catalyst_tag_head(h)  # (B, 4)

        # 4. set heads: 接收对应 hier embedding
        if teacher is not None:
            rc_idx = teacher['reagent_class_v3']
            cc_idx = teacher['catalyst_class_v3']
            sc_idx = teacher['solvent_class_v3']
            lc_idx = teacher['ligand_class_v3']
            ac_idx = teacher['additive_class_v3']
            cat_tag = teacher[CAT_TAG_KEY].float()  # (B, 4) float
        else:
            rc_idx = out['reagent_class_v3'].argmax(dim=-1)
            cc_idx = out['catalyst_class_v3'].argmax(dim=-1)
            sc_idx = out['solvent_class_v3'].argmax(dim=-1)
            lc_idx = out['ligand_class_v3'].argmax(dim=-1)
            ac_idx = out['additive_class_v3'].argmax(dim=-1)
            cat_tag = (torch.sigmoid(out[CAT_TAG_KEY]) > 0.5).float()

        rc_emb = self.hier_class_embed['reagent_class_v3'](rc_idx)
        cc_emb = self.hier_class_embed['catalyst_class_v3'](cc_idx)
        sc_emb = self.hier_class_embed['solvent_class_v3'](sc_idx)
        cat_tag_emb = self.catalyst_tag_embed(cat_tag)
        # ligand/additive 类的 embedding (用于具体 SMILES head)
        lc_emb = self.smi_class_embed['ligand_class_v3'](lc_idx)
        ac_emb = self.smi_class_embed['additive_class_v3'](ac_idx)

        B = h.size(0)
        out['solvent'] = self.solvent_set(
            torch.cat([h, sc_emb], dim=-1)
        ).view(B, self.k_slots, -1)
        out['reagent'] = self.reagent_set(
            torch.cat([h, rc_emb], dim=-1)
        ).view(B, self.k_slots, -1)
        out['catalyst'] = self.catalyst_set(
            torch.cat([h, cc_emb, cat_tag_emb], dim=-1)
        ).view(B, self.k_slots, -1)
        # ligand / additive single SMILES heads
        out['ligand'] = self.smi_single_heads['ligand'](
            torch.cat([h, lc_emb], dim=-1)
        )
        out['additive'] = self.smi_single_heads['additive'](
            torch.cat([h, ac_emb], dim=-1)
        )

        return out
