"""V3 + Ligand/Additive SMI heads + xTB-aware class embeddings。

每个 class-output head 加一个辅助 logit 项:
  logit[c] = W[c] @ h  +  alpha * (h @ xtb_proj(xtb_table[c])) * mask[c]
其中:
  W[c]      : 标准 trainable head
  xtb_proj  : 11 → hidden 的 MLP, 每 head 独立
  xtb_table : (N_classes, 11) 固定 buffer (z-scored)
  mask[c]   : 该 class 是否有有效 xTB QC 数据 (0/1)
  alpha     : 学习的标量, 初始 0.1
"""
import torch
import torch.nn as nn
from typing import Dict, Optional


SINGLE_HEADS_V3 = [
    'anode_material',
    'cathode_material',
    'cell_class_v3',
    'electrolyte_cation',
    'electrolyte_anion',
    'ligand_class_v3',
    'additive_class_v3',
]
HIER_KEYS = [
    'reagent_class_v3',
    'catalyst_class_v3',
    'solvent_class_v3',
]
SMI_FROM_CLASS = {
    'ligand':   'ligand_class_v3',
    'additive': 'additive_class_v3',
}
SET_HEADS = ['solvent', 'reagent', 'catalyst']
CAT_TAG_KEY = 'catalyst_mech_tags'
CAT_TAG_BITS = 4
K_SLOTS = 4
XTB_DIM = 11


class XTBAwareLinear(nn.Module):
    """Linear head with xTB-aware auxiliary class embedding."""

    def __init__(self, in_dim: int, num_classes: int,
                 xtb_table: torch.Tensor,    # (num_classes, 11)
                 xtb_mask: torch.Tensor,     # (num_classes,)
                 xtb_dim: int = XTB_DIM,
                 hidden: int = 64):
        super().__init__()
        self.in_dim = in_dim
        self.num_classes = num_classes
        # Standard linear head
        self.W = nn.Linear(in_dim, num_classes)
        # xTB projection: 11 → hidden → in_dim
        self.xtb_proj = nn.Sequential(
            nn.Linear(xtb_dim, hidden), nn.GELU(),
            nn.Linear(hidden, in_dim),
        )
        # alpha (per-head learnable, init 0.1)
        self.alpha = nn.Parameter(torch.tensor(0.1))
        # Register buffers (固定, 不训练)
        self.register_buffer('xtb_table', xtb_table)
        self.register_buffer('xtb_mask', xtb_mask)

    def forward(self, h: torch.Tensor) -> torch.Tensor:
        # h: (B, in_dim)
        std_logits = self.W(h)  # (B, num_classes)
        # xTB-projected class features: (N, in_dim)
        xtb_class_emb = self.xtb_proj(self.xtb_table)
        # aux logit: (B, N) = h @ xtb_class_emb.T
        aux_logits = h @ xtb_class_emb.T
        # apply mask: classes without xtb get 0
        aux_logits = aux_logits * self.xtb_mask
        return std_logits + self.alpha * aux_logits


class XTBAwareSetLinear(nn.Module):
    """Set head with K slots × (num_classes + 1) outputs, xTB only on first N classes."""

    def __init__(self, in_dim: int, num_classes: int, k_slots: int,
                 xtb_table: torch.Tensor, xtb_mask: torch.Tensor,
                 xtb_dim: int = XTB_DIM, hidden: int = 64):
        super().__init__()
        self.k_slots = k_slots
        self.num_classes = num_classes  # 不含 no_obj
        out_dim = k_slots * (num_classes + 1)
        self.W = nn.Linear(in_dim, out_dim)
        self.xtb_proj = nn.Sequential(
            nn.Linear(xtb_dim, hidden), nn.GELU(),
            nn.Linear(hidden, in_dim),
        )
        self.alpha = nn.Parameter(torch.tensor(0.1))
        self.register_buffer('xtb_table', xtb_table)
        self.register_buffer('xtb_mask', xtb_mask)

    def forward(self, h: torch.Tensor) -> torch.Tensor:
        # h: (B, in_dim)
        B = h.size(0)
        std_logits = self.W(h).view(B, self.k_slots, self.num_classes + 1)
        # xTB-projected: (N, in_dim)
        xtb_class_emb = self.xtb_proj(self.xtb_table)
        # aux per (B, N), then broadcast over K slots
        aux_logits = h @ xtb_class_emb.T   # (B, N)
        aux_logits = aux_logits * self.xtb_mask
        # broadcast: (B, K, N) — add only to first N classes, not no_obj
        std_logits[:, :, :self.num_classes] = (
            std_logits[:, :, :self.num_classes] + self.alpha * aux_logits.unsqueeze(1)
        )
        return std_logits


class ConditionStage1HierSetV3XTB(nn.Module):
    def __init__(self, num_classes: Dict[str, int],
                 num_classes_v3: Dict[str, int],
                 xtb_class_table: Dict[str, Dict[str, torch.Tensor]],
                 fp_dim: int = 6144,
                 hidden_dims=(1024, 768, 512), dropout: float = 0.3,
                 k_slots: int = K_SLOTS,
                 class_embed_dim: int = 32,
                 cat_tag_embed_dim: int = 8,
                 xtb_mlp_hidden: int = 64):
        super().__init__()
        self.k_slots = k_slots
        self.class_embed_dim = class_embed_dim

        # encoder
        layers = []
        prev = fp_dim
        for h in hidden_dims:
            layers += [nn.Linear(prev, h), nn.BatchNorm1d(h),
                       nn.GELU(), nn.Dropout(dropout)]
            prev = h
        self.encoder = nn.Sequential(*layers)
        self.hidden = prev

        # === v3 single heads — XTBAwareLinear ===
        self.single_heads = nn.ModuleDict()
        for k in SINGLE_HEADS_V3:
            t = xtb_class_table[k]
            self.single_heads[k] = XTBAwareLinear(
                prev, num_classes_v3[k],
                torch.from_numpy(t['feat']).float(),
                torch.from_numpy(t['mask']).float(),
                hidden=xtb_mlp_hidden,
            )

        # === v3 hier class heads — XTBAwareLinear ===
        self.hier_class_heads = nn.ModuleDict()
        self.hier_class_embed = nn.ModuleDict()
        for k in HIER_KEYS:
            t = xtb_class_table[k]
            self.hier_class_heads[k] = XTBAwareLinear(
                prev, num_classes_v3[k],
                torch.from_numpy(t['feat']).float(),
                torch.from_numpy(t['mask']).float(),
                hidden=xtb_mlp_hidden,
            )
            self.hier_class_embed[k] = nn.Embedding(num_classes_v3[k], class_embed_dim)

        self.smi_class_embed = nn.ModuleDict({
            cls_name: nn.Embedding(num_classes_v3[cls_name], class_embed_dim)
            for cls_name in SMI_FROM_CLASS.values()
        })

        # === catalyst tags ===
        self.catalyst_tag_head = nn.Linear(prev, CAT_TAG_BITS)
        self.catalyst_tag_embed = nn.Linear(CAT_TAG_BITS, cat_tag_embed_dim)

        # === set heads — XTBAwareSetLinear (xTB on SMILES vocab) ===
        # solvent set: 输入 [h, sc_emb] (prev + class_embed_dim)
        t = xtb_class_table['solvent']
        self.solvent_set = XTBAwareSetLinear(
            prev + class_embed_dim, num_classes['solvent'], k_slots,
            torch.from_numpy(t['feat']).float(),
            torch.from_numpy(t['mask']).float(),
            hidden=xtb_mlp_hidden,
        )
        # catalyst set: 输入 [h, cc_emb, cat_tag_emb]
        t = xtb_class_table['catalyst']
        self.catalyst_set = XTBAwareSetLinear(
            prev + class_embed_dim + cat_tag_embed_dim,
            num_classes['catalyst'], k_slots,
            torch.from_numpy(t['feat']).float(),
            torch.from_numpy(t['mask']).float(),
            hidden=xtb_mlp_hidden,
        )
        # reagent set: 输入 [h, rc_emb]
        t = xtb_class_table['reagent']
        self.reagent_set = XTBAwareSetLinear(
            prev + class_embed_dim, num_classes['reagent'], k_slots,
            torch.from_numpy(t['feat']).float(),
            torch.from_numpy(t['mask']).float(),
            hidden=xtb_mlp_hidden,
        )

        # === ligand / additive single SMILES heads — XTBAwareLinear ===
        self.smi_single_heads = nn.ModuleDict()
        for smi_name in SMI_FROM_CLASS:
            t = xtb_class_table[smi_name]
            self.smi_single_heads[smi_name] = XTBAwareLinear(
                prev + class_embed_dim, num_classes[smi_name],
                torch.from_numpy(t['feat']).float(),
                torch.from_numpy(t['mask']).float(),
                hidden=xtb_mlp_hidden,
            )

        self.num_classes = num_classes
        self.num_classes_v3 = num_classes_v3
        self.no_obj_idx = {k: num_classes[k] for k in SET_HEADS}

    def forward(self, fp: torch.Tensor,
                teacher: Optional[Dict[str, torch.Tensor]] = None
                ) -> Dict[str, torch.Tensor]:
        h = self.encoder(fp)
        out = {}

        # 1. v3 single heads
        for k, head in self.single_heads.items():
            out[k] = head(h)

        # 2. hier class heads
        for k, head in self.hier_class_heads.items():
            out[k] = head(h)

        # 3. catalyst tags
        out[CAT_TAG_KEY] = self.catalyst_tag_head(h)

        # 4. set heads
        if teacher is not None:
            rc_idx = teacher['reagent_class_v3']
            cc_idx = teacher['catalyst_class_v3']
            sc_idx = teacher['solvent_class_v3']
            lc_idx = teacher['ligand_class_v3']
            ac_idx = teacher['additive_class_v3']
            cat_tag = teacher[CAT_TAG_KEY].float()
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
        lc_emb = self.smi_class_embed['ligand_class_v3'](lc_idx)
        ac_emb = self.smi_class_embed['additive_class_v3'](ac_idx)

        out['solvent'] = self.solvent_set(torch.cat([h, sc_emb], dim=-1))
        out['reagent'] = self.reagent_set(torch.cat([h, rc_emb], dim=-1))
        out['catalyst'] = self.catalyst_set(torch.cat([h, cc_emb, cat_tag_emb], dim=-1))
        out['ligand'] = self.smi_single_heads['ligand'](torch.cat([h, lc_emb], dim=-1))
        out['additive'] = self.smi_single_heads['additive'](torch.cat([h, ac_emb], dim=-1))

        return out
