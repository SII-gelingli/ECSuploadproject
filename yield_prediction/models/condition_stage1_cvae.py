"""Stage-1 CVAE (Conditional VAE) — 9 head 联合条件生成模型。

与判别式 Stage-1 模型不同, CVAE 学的是 **P(conditions | reaction) 的联合分布**:
- 编码: (reaction, conditions) → 潜空间 z (mu, logvar)
- 解码: (reaction, z) → 9 head 联合 logits
- 训练: 重构损失 + KL(q(z|x) || N(0,I))
- 推理: 采样多个 z ~ N(0,I), 解码得到 N 套不同的条件组合

可生成"训练集没见过的条件组合", 因为 z 是连续的。
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, Tuple, List


HEAD_KEYS = ['anode', 'cathode', 'cell_type', 'solvent', 'electrolyte',
             'catalyst', 'reagent', 'ligand', 'additive']

# 每个 head 的 embedding 维度
EMBED_DIM = {
    'anode': 16, 'cathode': 16, 'cell_type': 8,
    'solvent': 32, 'electrolyte': 32,
    'catalyst': 32, 'reagent': 32, 'ligand': 16, 'additive': 16,
}


class ConditionStage1CVAE(nn.Module):
    def __init__(self, num_classes: Dict[str, int], fp_dim: int = 6144,
                 repr_dim: int = 256, latent_dim: int = 64,
                 dropout: float = 0.2):
        super().__init__()
        self.latent_dim = latent_dim
        self.repr_dim = repr_dim
        self.num_classes = num_classes
        self.head_keys = [k for k in HEAD_KEYS if k in num_classes]

        # 条件 embedding (每个 head 一个 nn.Embedding)
        self.cond_embeds = nn.ModuleDict({
            k: nn.Embedding(num_classes[k], EMBED_DIM[k]) for k in self.head_keys
        })
        self.cond_emb_dim = sum(EMBED_DIM[k] for k in self.head_keys)

        # 共享反应编码器
        self.reaction_encoder = nn.Sequential(
            nn.Linear(fp_dim, 512), nn.BatchNorm1d(512), nn.GELU(), nn.Dropout(dropout),
            nn.Linear(512, repr_dim), nn.BatchNorm1d(repr_dim), nn.GELU(), nn.Dropout(dropout),
        )

        # VAE encoder: (repr ⊕ cond_emb) → μ, logσ²
        self.enc_trunk = nn.Sequential(
            nn.Linear(repr_dim + self.cond_emb_dim, 512), nn.BatchNorm1d(512), nn.GELU(), nn.Dropout(dropout),
            nn.Linear(512, 256), nn.BatchNorm1d(256), nn.GELU(), nn.Dropout(dropout),
        )
        self.fc_mu = nn.Linear(256, latent_dim)
        self.fc_logvar = nn.Linear(256, latent_dim)

        # VAE decoder: (repr ⊕ z) → trunk → 9 head logits
        self.dec_trunk = nn.Sequential(
            nn.Linear(repr_dim + latent_dim, 512), nn.BatchNorm1d(512), nn.GELU(), nn.Dropout(dropout),
            nn.Linear(512, 512), nn.BatchNorm1d(512), nn.GELU(), nn.Dropout(dropout),
        )
        self.heads = nn.ModuleDict({
            k: nn.Linear(512, num_classes[k]) for k in self.head_keys
        })

    def embed_conditions(self, labels: Dict[str, torch.Tensor]) -> torch.Tensor:
        return torch.cat([self.cond_embeds[k](labels[k]) for k in self.head_keys], dim=-1)

    def reparameterize(self, mu, logvar):
        if self.training:
            std = torch.exp(0.5 * logvar)
            eps = torch.randn_like(std)
            return mu + eps * std
        return mu

    def encode(self, repr, cond_emb):
        x = torch.cat([repr, cond_emb], dim=-1)
        h = self.enc_trunk(x)
        return self.fc_mu(h), self.fc_logvar(h)

    def decode(self, repr, z) -> Dict[str, torch.Tensor]:
        x = torch.cat([repr, z], dim=-1)
        h = self.dec_trunk(x)
        return {k: head(h) for k, head in self.heads.items()}

    def forward(self, fp: torch.Tensor, labels: Dict[str, torch.Tensor]
                ) -> Tuple[Dict[str, torch.Tensor], torch.Tensor, torch.Tensor]:
        repr = self.reaction_encoder(fp)
        cond_emb = self.embed_conditions(labels)
        mu, logvar = self.encode(repr, cond_emb)
        z = self.reparameterize(mu, logvar)
        logits = self.decode(repr, z)
        return logits, mu, logvar

    @torch.no_grad()
    def generate(self, fp: torch.Tensor, num_samples: int = 10, temperature: float = 1.0
                 ) -> List[Dict[str, torch.Tensor]]:
        """从先验 N(0,I) 采样 N 套条件组合"""
        self.eval()
        repr = self.reaction_encoder(fp)
        B = repr.size(0)
        outputs = []
        for _ in range(num_samples):
            z = torch.randn(B, self.latent_dim, device=fp.device) * temperature
            logits = self.decode(repr, z)
            # 同时返回 argmax 标签
            sample = {f'{k}_logits': v for k, v in logits.items()}
            for k in self.head_keys:
                sample[f'{k}_label'] = logits[k].argmax(dim=-1)
            outputs.append(sample)
        return outputs

    @torch.no_grad()
    def reconstruct(self, fp: torch.Tensor, labels: Dict[str, torch.Tensor]
                    ) -> Dict[str, torch.Tensor]:
        """teacher forcing 重构 (用 GT cond_emb 编码 → 取 mu 解码), 用于 val 评估"""
        self.eval()
        repr = self.reaction_encoder(fp)
        cond_emb = self.embed_conditions(labels)
        mu, _ = self.encode(repr, cond_emb)
        return self.decode(repr, mu)
