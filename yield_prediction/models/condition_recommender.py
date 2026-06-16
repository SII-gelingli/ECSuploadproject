"""
反应条件推荐模型：给定反应物和产物，推荐最优条件
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Dict, Tuple, Optional
import numpy as np


class ConditionRecommender(nn.Module):
    """
    条件推荐模型：预测最优的反应条件组合

    给定反应物和产物的分子指纹，推荐：
    - 阳极材料
    - 阴极材料
    - 电解质
    - 溶剂
    - 电流/电流密度
    - 电解池类型
    """

    def __init__(
        self,
        reaction_dim: int,  # 反应指纹维度
        hidden_dim: int = 512,
        num_anode_materials: int = 19,
        num_cathode_materials: int = 19,
        num_cell_types: int = 6,
        num_electrolytes: int = 100,
        num_solvents: int = 100,
        num_reagents: int = 100,
        num_catalysts: int = 100,
        dropout: float = 0.2
    ):
        super().__init__()

        self.reaction_dim = reaction_dim
        self.hidden_dim = hidden_dim

        # 反应编码器
        self.reaction_encoder = nn.Sequential(
            nn.Linear(reaction_dim, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout)
        )

        # 离散条件预测头
        self.anode_head = nn.Linear(hidden_dim, num_anode_materials)
        self.cathode_head = nn.Linear(hidden_dim, num_cathode_materials)
        self.cell_type_head = nn.Linear(hidden_dim, num_cell_types)
        self.electrolyte_head = nn.Linear(hidden_dim, num_electrolytes)
        self.solvent_head = nn.Linear(hidden_dim, num_solvents)
        self.reagent_head = nn.Linear(hidden_dim, num_reagents)
        self.catalyst_head = nn.Linear(hidden_dim, num_catalysts)

    def forward(self, reaction_features: torch.Tensor) -> Dict[str, torch.Tensor]:
        """
        前向传播
        Args:
            reaction_features: 反应特征 [batch_size, reaction_dim]
        Returns:
            Dict包含各个条件的预测
        """
        # 编码反应
        h = self.reaction_encoder(reaction_features)

        # 预测各个条件
        predictions = {
            'anode_logits': self.anode_head(h),
            'cathode_logits': self.cathode_head(h),
            'cell_type_logits': self.cell_type_head(h),
            'electrolyte_logits': self.electrolyte_head(h),
            'solvent_logits': self.solvent_head(h),
            'reagent_logits': self.reagent_head(h),
            'catalyst_logits': self.catalyst_head(h)
        }

        return predictions

    def recommend(
        self,
        reaction_features: torch.Tensor,
        top_k: int = 3
    ) -> Dict[str, List]:
        """
        推荐反应条件
        Args:
            reaction_features: 反应特征
            top_k: 返回top_k个推荐
        Returns:
            推荐的条件及其置信度
        """
        self.eval()
        with torch.no_grad():
            predictions = self.forward(reaction_features)

            recommendations = {}

            # 处理离散条件
            for key in ['anode_logits', 'cathode_logits', 'cell_type_logits',
                        'electrolyte_logits', 'solvent_logits', 'reagent_logits', 'catalyst_logits']:
                logits = predictions[key]
                probs = F.softmax(logits, dim=-1)
                top_probs, top_indices = torch.topk(probs, min(top_k, probs.size(-1)))

                name = key.replace('_logits', '')
                recommendations[name] = {
                    'indices': top_indices.cpu().tolist(),
                    'probabilities': top_probs.cpu().tolist()
                }

        return recommendations


class ConditionRecommenderXTB(nn.Module):
    """条件推荐模型：指纹 + xTB特征 (用于condition_recommender_cat)

    Updated 2024-03: 新架构，支持催化剂预测
    """

    def __init__(
        self,
        fp_dim: int = 6144,      # 3 * 2048 (reactant + product + diff)
        xtb_dim: int = 33,       # 3 * 11 (reactant + product + diff)
        hidden_dim: int = 256,
        num_anode: int = 19,     # 与原始模型一致
        num_cathode: int = 19,   # 与原始模型一致
        num_cell_type: int = 6,  # 与原始模型一致
        num_electrolyte: int = 101,
        num_solvent: int = 101,
        num_reagent: int = 201,
        num_catalyst: int = 101,
        dropout: float = 0.3
    ):
        super().__init__()

        # 指纹编码器
        self.fp_encoder = nn.Sequential(
            nn.Linear(fp_dim, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(512, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
        )

        # xTB编码器
        self.xtb_encoder = nn.Sequential(
            nn.Linear(xtb_dim, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(64, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
        )

        # 融合层
        fused_dim = hidden_dim + 64
        self.fusion = nn.Sequential(
            nn.Linear(fused_dim, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

        # 预测头
        self.anode_head = nn.Linear(hidden_dim, num_anode)
        self.cathode_head = nn.Linear(hidden_dim, num_cathode)
        self.cell_type_head = nn.Linear(hidden_dim, num_cell_type)
        self.electrolyte_head = nn.Linear(hidden_dim, num_electrolyte)
        self.solvent_head = nn.Linear(hidden_dim, num_solvent)
        self.reagent_head = nn.Linear(hidden_dim, num_reagent)
        self.catalyst_head = nn.Linear(hidden_dim, num_catalyst)

    def forward(self, fp_features, xtb_features=None):
        """
        Args:
            fp_features: 反应指纹 [batch, 6144] 或 完整特征 [batch, 6177]
            xtb_features: xTB特征 [batch, 33]，如果为None则从fp_features中切分
        """
        if xtb_features is None and fp_features.shape[1] > 6144:
            # 自动切分
            xtb_features = fp_features[:, 6144:]
            fp_features = fp_features[:, :6144]
        elif xtb_features is None:
            # 如果没有xTB特征，使用零填充
            xtb_features = torch.zeros(fp_features.shape[0], 33, device=fp_features.device)

        fp_h = self.fp_encoder(fp_features)
        xtb_h = self.xtb_encoder(xtb_features)

        combined = torch.cat([fp_h, xtb_h], dim=-1)
        h = self.fusion(combined)

        return {
            'anode': self.anode_head(h),
            'cathode': self.cathode_head(h),
            'cell_type': self.cell_type_head(h),
            'electrolyte': self.electrolyte_head(h),
            'solvent': self.solvent_head(h),
            'reagent': self.reagent_head(h),
            'catalyst': self.catalyst_head(h),
        }

    def recommend(self, fp_features, xtb_features=None, top_k: int = 3):
        """推荐反应条件"""
        self.eval()
        with torch.no_grad():
            predictions = self.forward(fp_features, xtb_features)

            recommendations = {}
            for key, logits in predictions.items():
                probs = F.softmax(logits, dim=-1)
                top_probs, top_indices = torch.topk(probs, min(top_k, probs.size(-1)))

                recommendations[key] = {
                    'indices': top_indices.cpu().tolist(),
                    'probabilities': top_probs.cpu().tolist()
                }

            return recommendations


class DualTowerConditionRecommender(nn.Module):
    """双塔条件推荐模型：指纹塔 + XTB量子特征塔，门控融合

    将高维稀疏指纹和低维稠密XTB特征分别压缩到低维空间，
    通过门控机制自适应融合，然后接分类头预测条件。
    """

    def __init__(
        self,
        fp_dim: int = 6144,  # 反应指纹维度 (3 * 2048)
        xtb_dim: int = 33,   # XTB特征维度 (反应物11 + 产物11 + 差异11)
        fp_hidden: int = 256,
        xtb_hidden: int = 64,
        num_anode_materials: int = 19,
        num_cathode_materials: int = 19,
        num_cell_types: int = 6,
        num_electrolytes: int = 100,
        num_solvents: int = 100,
        num_reagents: int = 100,
        num_catalysts: int = 100,
        dropout: float = 0.2
    ):
        super().__init__()
        self.fp_dim = fp_dim
        self.xtb_dim = xtb_dim

        # Tower 1: 指纹塔
        self.fp_tower = nn.Sequential(
            nn.Linear(fp_dim, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(512, fp_hidden),
            nn.BatchNorm1d(fp_hidden),
            nn.ReLU(),
            nn.Dropout(dropout)
        )

        # Tower 2: XTB塔
        self.xtb_tower = nn.Sequential(
            nn.Linear(xtb_dim, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(128, xtb_hidden),
            nn.BatchNorm1d(xtb_hidden),
            nn.ReLU(),
            nn.Dropout(dropout)
        )

        fused_dim = fp_hidden + xtb_hidden  # 320

        # 门控融合
        self.gate = nn.Sequential(
            nn.Linear(fused_dim, fused_dim),
            nn.Sigmoid()
        )

        # 分类预测头
        self.anode_head = nn.Linear(fused_dim, num_anode_materials)
        self.cathode_head = nn.Linear(fused_dim, num_cathode_materials)
        self.cell_type_head = nn.Linear(fused_dim, num_cell_types)
        self.electrolyte_head = nn.Linear(fused_dim, num_electrolytes)
        self.solvent_head = nn.Linear(fused_dim, num_solvents)
        self.reagent_head = nn.Linear(fused_dim, num_reagents)
        self.catalyst_head = nn.Linear(fused_dim, num_catalysts)

    def forward(self, reaction_features: torch.Tensor) -> Dict[str, torch.Tensor]:
        # 切分特征
        fp_feat = reaction_features[:, :self.fp_dim]
        xtb_feat = reaction_features[:, self.fp_dim:]

        # 双塔编码
        fp_h = self.fp_tower(fp_feat)
        xtb_h = self.xtb_tower(xtb_feat)

        # 门控融合
        combined = torch.cat([fp_h, xtb_h], dim=-1)
        gate_weights = self.gate(combined)
        h = combined * gate_weights

        return {
            'anode_logits': self.anode_head(h),
            'cathode_logits': self.cathode_head(h),
            'cell_type_logits': self.cell_type_head(h),
            'electrolyte_logits': self.electrolyte_head(h),
            'solvent_logits': self.solvent_head(h),
            'reagent_logits': self.reagent_head(h),
            'catalyst_logits': self.catalyst_head(h)
        }


class CompactConditionRecommender(nn.Module):
    """紧凑条件推荐模型：PCA压缩反应指纹 + xTB特征

    输入维度从 6,177D 降至 ~161D（PCA 128D + xTB 33D）。
    """

    def __init__(
        self,
        input_dim: int = 161,
        hidden_dim: int = 256,
        num_anode_materials: int = 19,
        num_cathode_materials: int = 19,
        num_cell_types: int = 6,
        num_electrolytes: int = 100,
        num_solvents: int = 100,
        num_reagents: int = 100,
        num_catalysts: int = 100,
        dropout: float = 0.2
    ):
        super().__init__()

        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout)
        )

        self.anode_head = nn.Linear(hidden_dim, num_anode_materials)
        self.cathode_head = nn.Linear(hidden_dim, num_cathode_materials)
        self.cell_type_head = nn.Linear(hidden_dim, num_cell_types)
        self.electrolyte_head = nn.Linear(hidden_dim, num_electrolytes)
        self.solvent_head = nn.Linear(hidden_dim, num_solvents)
        self.reagent_head = nn.Linear(hidden_dim, num_reagents)
        self.catalyst_head = nn.Linear(hidden_dim, num_catalysts)

    def forward(self, reaction_features: torch.Tensor) -> Dict[str, torch.Tensor]:
        h = self.encoder(reaction_features)
        return {
            'anode_logits': self.anode_head(h),
            'cathode_logits': self.cathode_head(h),
            'cell_type_logits': self.cell_type_head(h),
            'electrolyte_logits': self.electrolyte_head(h),
            'solvent_logits': self.solvent_head(h),
            'reagent_logits': self.reagent_head(h),
            'catalyst_logits': self.catalyst_head(h)
        }


class ConditionVAE(nn.Module):
    """
    变分自编码器用于条件生成
    可以生成多样化的条件组合
    """

    def __init__(
        self,
        reaction_dim: int,
        condition_dim: int,
        latent_dim: int = 64,
        hidden_dim: int = 256,
        dropout: float = 0.2
    ):
        super().__init__()

        self.latent_dim = latent_dim

        # 编码器
        self.encoder = nn.Sequential(
            nn.Linear(reaction_dim + condition_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout)
        )

        self.fc_mu = nn.Linear(hidden_dim, latent_dim)
        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)

        # 解码器
        self.decoder = nn.Sequential(
            nn.Linear(reaction_dim + latent_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, condition_dim)
        )

    def encode(self, reaction: torch.Tensor, condition: torch.Tensor):
        """编码"""
        x = torch.cat([reaction, condition], dim=-1)
        h = self.encoder(x)
        mu = self.fc_mu(h)
        logvar = self.fc_logvar(h)
        return mu, logvar

    def reparameterize(self, mu: torch.Tensor, logvar: torch.Tensor):
        """重参数化技巧"""
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def decode(self, reaction: torch.Tensor, z: torch.Tensor):
        """解码"""
        x = torch.cat([reaction, z], dim=-1)
        return self.decoder(x)

    def forward(self, reaction: torch.Tensor, condition: torch.Tensor):
        """前向传播"""
        mu, logvar = self.encode(reaction, condition)
        z = self.reparameterize(mu, logvar)
        condition_recon = self.decode(reaction, z)
        return condition_recon, mu, logvar

    def generate(self, reaction: torch.Tensor, num_samples: int = 5):
        """生成条件样本"""
        self.eval()
        with torch.no_grad():
            batch_size = reaction.size(0)
            samples = []

            for _ in range(num_samples):
                z = torch.randn(batch_size, self.latent_dim, device=reaction.device)
                condition = self.decode(reaction, z)
                samples.append(condition)

            return torch.stack(samples, dim=1)  # [B, num_samples, condition_dim]


class JointYieldConditionModel(nn.Module):
    """
    联合模型：同时进行产率预测和条件推荐
    利用产率预测来指导条件推荐
    """

    def __init__(
        self,
        reaction_dim: int,
        condition_dim: int,
        hidden_dim: int = 256,
        num_conditions: Dict = None,
        dropout: float = 0.2
    ):
        super().__init__()

        num_conditions = num_conditions or {
            'anode': 15, 'cathode': 15, 'cell_type': 5,
            'electrolyte': 100, 'solvent': 100
        }

        # 反应编码器
        self.reaction_encoder = nn.Sequential(
            nn.Linear(reaction_dim, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU()
        )

        # 条件编码器
        self.condition_encoder = nn.Sequential(
            nn.Linear(condition_dim, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU()
        )

        # 产率预测头
        self.yield_predictor = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, 1),
            nn.Sigmoid()
        )

        # 条件推荐头
        self.condition_recommender = ConditionRecommender(
            reaction_dim=hidden_dim,
            hidden_dim=hidden_dim,
            **num_conditions,
            dropout=dropout
        )

    def forward(
        self,
        reaction_features: torch.Tensor,
        condition_features: Optional[torch.Tensor] = None
    ):
        """
        前向传播
        Args:
            reaction_features: 反应特征
            condition_features: 条件特征（用于产率预测时提供）
        """
        reaction_h = self.reaction_encoder(reaction_features)

        outputs = {}

        # 条件推荐（仅基于反应）
        outputs['condition_predictions'] = self.condition_recommender(reaction_h)

        # 产率预测（需要条件）
        if condition_features is not None:
            condition_h = self.condition_encoder(condition_features)
            combined = torch.cat([reaction_h, condition_h], dim=-1)
            outputs['yield_prediction'] = self.yield_predictor(combined)

        return outputs


if __name__ == "__main__":
    # 测试条件推荐模型
    batch_size = 8
    reaction_dim = 6144  # 3 * 2048

    model = ConditionRecommender(reaction_dim)
    x = torch.randn(batch_size, reaction_dim)

    predictions = model(x)
    for key, value in predictions.items():
        print(f"{key}: {value.shape}")

    recommendations = model.recommend(x, top_k=3)
    print("\nRecommendations:")
    for key, value in recommendations.items():
        print(f"{key}: {value}")
