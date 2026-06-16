"""
Categorical CVAE 条件生成模型：联合建模7个反应条件的关联

替代独立分类头方式，使用条件变分自编码器联合生成7个条件，
能建模条件之间的关联（如阳极材料与电解质的匹配关系），
并通过隐变量采样实现多样化推荐。

架构:
  训练: reaction_fp → reaction_encoder → repr
         repr + condition_emb → encoder → mu, logvar → z
         repr + z → decoder → 7个分类头 → logits
  推理: reaction_fp → reaction_encoder → repr
         z ~ N(0, I)
         repr + z → decoder → 7个分类头 → argmax
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, List, Optional, Tuple
import numpy as np


class CategoricalCVAE(nn.Module):
    """
    Categorical Conditional VAE for joint condition generation.

    7个条件: anode(16D), cathode(16D), cell_type(8D),
             electrolyte(32D), solvent(32D), reagent(32D), catalyst(32D)
    总 embedding 维度: 168D
    """

    def __init__(
        self,
        reaction_dim: int = 6144,
        repr_dim: int = 256,
        latent_dim: int = 64,
        num_anode_materials: int = 19,
        num_cathode_materials: int = 19,
        num_cell_types: int = 6,
        num_electrolytes: int = 100,
        num_solvents: int = 100,
        num_reagents: int = 100,
        num_catalysts: int = 100,
        dropout: float = 0.2,
    ):
        super().__init__()

        self.latent_dim = latent_dim
        self.repr_dim = repr_dim

        # 保存类别数量（推理时重建需要）
        self.num_classes = {
            'anode': num_anode_materials,
            'cathode': num_cathode_materials,
            'cell_type': num_cell_types,
            'electrolyte': num_electrolytes,
            'solvent': num_solvents,
            'reagent': num_reagents,
            'catalyst': num_catalysts,
        }

        # ── 条件 Embedding 层 ──────────────────────────────
        self.anode_emb = nn.Embedding(num_anode_materials, 16)
        self.cathode_emb = nn.Embedding(num_cathode_materials, 16)
        self.cell_type_emb = nn.Embedding(num_cell_types, 8)
        self.electrolyte_emb = nn.Embedding(num_electrolytes, 32)
        self.solvent_emb = nn.Embedding(num_solvents, 32)
        self.reagent_emb = nn.Embedding(num_reagents, 32)
        self.catalyst_emb = nn.Embedding(num_catalysts, 32)
        # 总 embedding 维度: 16+16+8+32+32+32+32 = 168

        self.condition_emb_dim = 168

        # ── 共享反应编码器: reaction_dim → repr_dim ────────
        self.reaction_encoder = nn.Sequential(
            nn.Linear(reaction_dim, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(512, repr_dim),
            nn.BatchNorm1d(repr_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

        # ── VAE 编码器: (repr + condition_emb) → mu, logvar ──
        encoder_input_dim = repr_dim + self.condition_emb_dim  # 256 + 168 = 424
        self.encoder = nn.Sequential(
            nn.Linear(encoder_input_dim, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(dropout),
        )
        self.fc_mu = nn.Linear(256, latent_dim)
        self.fc_logvar = nn.Linear(256, latent_dim)

        # ── VAE 解码器: (repr + z) → hidden → 7 个分类头 ──
        decoder_input_dim = repr_dim + latent_dim  # 256 + 64 = 320
        self.decoder_trunk = nn.Sequential(
            nn.Linear(decoder_input_dim, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(512, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

        # 7 个分类头
        self.anode_head = nn.Linear(512, num_anode_materials)
        self.cathode_head = nn.Linear(512, num_cathode_materials)
        self.cell_type_head = nn.Linear(512, num_cell_types)
        self.electrolyte_head = nn.Linear(512, num_electrolytes)
        self.solvent_head = nn.Linear(512, num_solvents)
        self.reagent_head = nn.Linear(512, num_reagents)
        self.catalyst_head = nn.Linear(512, num_catalysts)

    def embed_conditions(
        self,
        anode: torch.Tensor,
        cathode: torch.Tensor,
        cell_type: torch.Tensor,
        electrolyte: torch.Tensor,
        solvent: torch.Tensor,
        reagent: torch.Tensor,
        catalyst: torch.Tensor,
    ) -> torch.Tensor:
        """将 7 个条件标签拼接为 168D embedding 向量"""
        return torch.cat([
            self.anode_emb(anode),        # [B, 16]
            self.cathode_emb(cathode),    # [B, 16]
            self.cell_type_emb(cell_type),  # [B, 8]
            self.electrolyte_emb(electrolyte),  # [B, 32]
            self.solvent_emb(solvent),    # [B, 32]
            self.reagent_emb(reagent),    # [B, 32]
            self.catalyst_emb(catalyst),  # [B, 32]
        ], dim=-1)  # [B, 168]

    def reparameterize(self, mu: torch.Tensor, logvar: torch.Tensor) -> torch.Tensor:
        """重参数化采样"""
        if self.training:
            std = torch.exp(0.5 * logvar)
            eps = torch.randn_like(std)
            return mu + eps * std
        else:
            return mu  # 推理时使用均值

    def encode(self, repr: torch.Tensor, condition_emb: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """编码器: reaction_repr + condition_emb → mu, logvar"""
        x = torch.cat([repr, condition_emb], dim=-1)  # [B, 424]
        h = self.encoder(x)  # [B, 256]
        mu = self.fc_mu(h)  # [B, 64]
        logvar = self.fc_logvar(h)  # [B, 64]
        return mu, logvar

    def decode(self, repr: torch.Tensor, z: torch.Tensor) -> Dict[str, torch.Tensor]:
        """解码器: reaction_repr + z → 7 个 logits"""
        x = torch.cat([repr, z], dim=-1)  # [B, 320]
        h = self.decoder_trunk(x)  # [B, 512]
        return {
            'anode_logits': self.anode_head(h),
            'cathode_logits': self.cathode_head(h),
            'cell_type_logits': self.cell_type_head(h),
            'electrolyte_logits': self.electrolyte_head(h),
            'solvent_logits': self.solvent_head(h),
            'reagent_logits': self.reagent_head(h),
            'catalyst_logits': self.catalyst_head(h),
        }

    def forward(
        self,
        reaction_fp: torch.Tensor,
        anode: torch.Tensor,
        cathode: torch.Tensor,
        cell_type: torch.Tensor,
        electrolyte: torch.Tensor,
        solvent: torch.Tensor,
        reagent: torch.Tensor,
        catalyst: torch.Tensor,
    ) -> Tuple[Dict[str, torch.Tensor], torch.Tensor, torch.Tensor]:
        """
        训练时前向传播

        Args:
            reaction_fp: 反应指纹 [B, reaction_dim]
            anode..catalyst: 7个条件标签 [B]

        Returns:
            predictions: dict of logits
            mu: [B, latent_dim]
            logvar: [B, latent_dim]
        """
        # 共享反应编码
        repr = self.reaction_encoder(reaction_fp)  # [B, 256]

        # 条件 embedding
        cond_emb = self.embed_conditions(
            anode, cathode, cell_type, electrolyte, solvent, reagent, catalyst
        )  # [B, 168]

        # 编码 → mu, logvar
        mu, logvar = self.encode(repr, cond_emb)  # [B, 64], [B, 64]

        # 重参数化采样
        z = self.reparameterize(mu, logvar)  # [B, 64]

        # 解码 → 7 个 logits
        predictions = self.decode(repr, z)

        return predictions, mu, logvar

    @torch.no_grad()
    def generate(
        self,
        reaction_fp: torch.Tensor,
        num_samples: int = 10,
        temperature: float = 1.0,
    ) -> List[Dict[str, torch.Tensor]]:
        """
        推理时采样多组条件（多样化推荐）

        Args:
            reaction_fp: 反应指纹 [B, reaction_dim]（通常 B=1）
            num_samples: 采样次数
            temperature: 采样温度，越大越多样

        Returns:
            list of dicts, 每个dict包含:
              - predictions: 7个logits
              - labels: 7个argmax标签
              - log_prob: 联合对数概率（用于排序）
        """
        self.eval()
        repr = self.reaction_encoder(reaction_fp)  # [B, 256]

        results = []
        for _ in range(num_samples):
            # 从 N(0, I) 采样
            z = torch.randn(repr.size(0), self.latent_dim, device=repr.device) * temperature

            # 解码
            predictions = self.decode(repr, z)

            # 计算各条件的 argmax 和联合概率
            labels = {}
            log_prob = torch.zeros(repr.size(0), device=repr.device)
            for key in ['anode', 'cathode', 'cell_type', 'electrolyte',
                        'solvent', 'reagent', 'catalyst']:
                logits = predictions[f'{key}_logits']
                probs = F.softmax(logits, dim=-1)
                chosen = logits.argmax(dim=-1)
                labels[key] = chosen
                # 累加联合对数概率
                log_prob += torch.log(probs.gather(1, chosen.unsqueeze(1)).squeeze(1) + 1e-10)

            results.append({
                'predictions': predictions,
                'labels': labels,
                'log_prob': log_prob,
            })

        return results

    @torch.no_grad()
    def recommend(
        self,
        reaction_fp: torch.Tensor,
        top_k: int = 3,
    ) -> Dict[str, torch.Tensor]:
        """
        兼容现有 API：z=0 确定性预测

        与 ConditionRecommender.forward() 返回格式相同
        """
        self.eval()
        repr = self.reaction_encoder(reaction_fp)
        z = torch.zeros(repr.size(0), self.latent_dim, device=repr.device)
        return self.decode(repr, z)


if __name__ == "__main__":
    # 快速测试
    batch_size = 8
    reaction_dim = 6144

    model = CategoricalCVAE(
        reaction_dim=reaction_dim,
        num_electrolytes=50,
        num_solvents=50,
        num_reagents=50,
        num_catalysts=50,
    )

    num_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Model parameters: {num_params:,}")

    # 训练模式测试
    x = torch.randn(batch_size, reaction_dim)
    anode = torch.randint(0, 15, (batch_size,))
    cathode = torch.randint(0, 15, (batch_size,))
    cell_type = torch.randint(0, 5, (batch_size,))
    electrolyte = torch.randint(0, 50, (batch_size,))
    solvent = torch.randint(0, 50, (batch_size,))
    reagent = torch.randint(0, 50, (batch_size,))
    catalyst = torch.randint(0, 50, (batch_size,))

    predictions, mu, logvar = model(
        x, anode, cathode, cell_type, electrolyte, solvent, reagent, catalyst
    )
    print("\nTraining mode:")
    for key, val in predictions.items():
        print(f"  {key}: {val.shape}")
    print(f"  mu: {mu.shape}, logvar: {logvar.shape}")

    # 推理模式测试
    model.eval()
    results = model.generate(x[:1], num_samples=5)
    print(f"\nGenerate mode: {len(results)} samples")
    for i, r in enumerate(results):
        labels = {k: v.item() for k, v in r['labels'].items()}
        print(f"  Sample {i}: log_prob={r['log_prob'].item():.3f}, labels={labels}")

    # 兼容API测试
    preds = model.recommend(x[:1])
    print("\nRecommend mode (z=0):")
    for key, val in preds.items():
        print(f"  {key}: {val.shape}")
