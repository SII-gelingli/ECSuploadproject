"""
Mixture of Experts (MoE) 产率预测模型

策略：先根据反应物和产物的分子指纹进行分类/聚类，然后用多个专家网络分别预测产率，
最终通过门控网络加权得到最终预测。

理论依据：
1. 不同类型的反应有不同的产率影响因素
2. 专门化的模型在同质数据上预测更准确
3. MoE可以端到端训练，避免聚类后分割数据带来的信息损失
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Optional, Tuple


class ExpertNetwork(nn.Module):
    """单个专家网络 - 用于预测特定类型反应的产率"""

    def __init__(
        self,
        input_dim: int,
        hidden_dims: List[int] = [256, 128],
        dropout: float = 0.3
    ):
        super().__init__()

        layers = []
        prev_dim = input_dim

        for hidden_dim in hidden_dims:
            layers.extend([
                nn.Linear(prev_dim, hidden_dim),
                nn.LayerNorm(hidden_dim),
                nn.GELU(),
                nn.Dropout(dropout)
            ])
            prev_dim = hidden_dim

        self.encoder = nn.Sequential(*layers)
        self.output = nn.Linear(hidden_dims[-1], 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """返回产率预测 (0-1)"""
        h = self.encoder(x)
        return torch.sigmoid(self.output(h))


class GatingNetwork(nn.Module):
    """门控网络 - 基于反应指纹决定使用哪些专家"""

    def __init__(
        self,
        reaction_fp_dim: int,
        num_experts: int,
        hidden_dim: int = 256,
        dropout: float = 0.2,
        temperature: float = 1.0
    ):
        super().__init__()
        self.num_experts = num_experts
        self.temperature = temperature

        # 门控网络：从反应指纹预测专家权重
        self.gate = nn.Sequential(
            nn.Linear(reaction_fp_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.LayerNorm(hidden_dim // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim // 2, num_experts)
        )

    def forward(self, reaction_fp: torch.Tensor) -> torch.Tensor:
        """
        返回专家权重 (softmax 归一化)
        Args:
            reaction_fp: 反应指纹 [batch_size, reaction_fp_dim]
        Returns:
            weights: 专家权重 [batch_size, num_experts]
        """
        logits = self.gate(reaction_fp)
        return F.softmax(logits / self.temperature, dim=-1)


class MoEYieldPredictor(nn.Module):
    """
    Mixture of Experts 产率预测模型

    架构：
    1. 反应指纹 (6144D) → 门控网络 → 专家权重
    2. 完整特征 (10301D) → 多个专家网络 → 各自产率预测
    3. 加权组合 → 最终产率预测

    训练策略：
    - 使用负载均衡损失防止专家塌缩
    - 使用辅助聚类损失增强专家分化
    """

    def __init__(
        self,
        full_input_dim: int = 10301,      # 完整特征维度 (10246 + 55)
        reaction_fp_dim: int = 6144,       # 反应指纹维度 (用于门控)
        num_experts: int = 8,              # 专家数量
        expert_hidden_dims: List[int] = [256, 128],
        gate_hidden_dim: int = 256,
        dropout: float = 0.3,
        gate_temperature: float = 1.0,
        top_k: int = 0,                    # 0 表示使用所有专家（软路由），>0 表示只用top_k专家
    ):
        super().__init__()

        self.full_input_dim = full_input_dim
        self.reaction_fp_dim = reaction_fp_dim
        self.num_experts = num_experts
        self.top_k = top_k

        # 门控网络：基于反应指纹选择专家
        self.gating = GatingNetwork(
            reaction_fp_dim=reaction_fp_dim,
            num_experts=num_experts,
            hidden_dim=gate_hidden_dim,
            dropout=dropout,
            temperature=gate_temperature
        )

        # 多个专家网络
        self.experts = nn.ModuleList([
            ExpertNetwork(
                input_dim=full_input_dim,
                hidden_dims=expert_hidden_dims,
                dropout=dropout
            )
            for _ in range(num_experts)
        ])

        # 用于负载均衡的辅助变量
        self.register_buffer('expert_counts', torch.zeros(num_experts))
        self.register_buffer('total_samples', torch.zeros(1))

    def forward(
        self,
        full_features: torch.Tensor,
        reaction_fp: Optional[torch.Tensor] = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        前向传播

        Args:
            full_features: 完整特征 [batch_size, full_input_dim]
            reaction_fp: 反应指纹 [batch_size, reaction_fp_dim]，如果为None则从full_features提取

        Returns:
            yield_pred: 产率预测 [batch_size, 1]
            expert_weights: 专家权重 [batch_size, num_experts]
        """
        batch_size = full_features.size(0)

        # 如果没有提供反应指纹，从完整特征中提取
        if reaction_fp is None:
            reaction_fp = full_features[:, :self.reaction_fp_dim]

        # 1. 计算专家权重
        expert_weights = self.gating(reaction_fp)  # [B, num_experts]

        # 2. 所有专家的预测
        expert_outputs = torch.stack([
            expert(full_features) for expert in self.experts
        ], dim=1)  # [B, num_experts, 1]

        expert_outputs = expert_outputs.squeeze(-1)  # [B, num_experts]

        # 3. Top-k 路由（如果启用）
        if self.top_k > 0 and self.top_k < self.num_experts:
            topk_weights, topk_indices = torch.topk(expert_weights, self.top_k, dim=-1)
            # 重新归一化
            topk_weights = topk_weights / topk_weights.sum(dim=-1, keepdim=True)

            # 只使用 top-k 专家的输出
            mask = torch.zeros_like(expert_weights)
            mask.scatter_(1, topk_indices, 1.0)
            expert_weights = expert_weights * mask
            expert_weights = expert_weights / expert_weights.sum(dim=-1, keepdim=True)

        # 4. 加权组合
        yield_pred = (expert_weights * expert_outputs).sum(dim=-1, keepdim=True)  # [B, 1]

        # 更新专家使用统计（用于负载均衡）
        if self.training:
            with torch.no_grad():
                # 使用 argmax 统计主专家
                primary_experts = expert_weights.argmax(dim=-1)
                for i in range(self.num_experts):
                    self.expert_counts[i] += (primary_experts == i).sum().float()
                self.total_samples += batch_size

        return yield_pred, expert_weights

    def get_load_balance_loss(self, expert_weights: torch.Tensor) -> torch.Tensor:
        """
        计算负载均衡损失，防止专家塌缩

        理想情况：每个专家被等概率选择
        损失 = 方差(各专家平均使用率)
        """
        # 计算每个专家的平均使用概率
        avg_weights = expert_weights.mean(dim=0)  # [num_experts]

        # 理想的均匀分布
        target = torch.ones_like(avg_weights) / self.num_experts

        # 使用 KL 散度作为损失
        loss = F.kl_div(
            torch.log(avg_weights + 1e-8),
            target,
            reduction='sum'
        )

        return loss

    def get_expert_diversity_loss(self, expert_weights: torch.Tensor) -> torch.Tensor:
        """
        计算专家多样性损失，鼓励不同样本使用不同专家

        损失 = -平均熵(专家权重分布)
        """
        # 计算每个样本的专家权重熵
        entropy = -(expert_weights * torch.log(expert_weights + 1e-8)).sum(dim=-1)

        # 最大化熵（返回负值）
        return -entropy.mean()

    def predict_yield(self, full_features: torch.Tensor) -> torch.Tensor:
        """预测产率（百分比）"""
        with torch.no_grad():
            yield_01, _ = self.forward(full_features)
            return yield_01 * 100

    def get_expert_assignment(self, full_features: torch.Tensor) -> torch.Tensor:
        """获取专家分配（用于分析）"""
        with torch.no_grad():
            reaction_fp = full_features[:, :self.reaction_fp_dim]
            weights = self.gating(reaction_fp)
            return weights.argmax(dim=-1)

    def get_expert_stats(self) -> dict:
        """获取专家使用统计"""
        if self.total_samples.item() == 0:
            return {}

        usage_rates = self.expert_counts / self.total_samples
        return {
            'expert_usage_rates': usage_rates.cpu().numpy().tolist(),
            'total_samples': int(self.total_samples.item()),
            'usage_std': usage_rates.std().item(),
        }

    def reset_stats(self):
        """重置统计"""
        self.expert_counts.zero_()
        self.total_samples.zero_()


class ClusterAwareMoEYieldPredictor(nn.Module):
    """
    带预聚类的 MoE 产率预测模型

    改进：先用 K-Means 对反应指纹进行聚类初始化，
    然后用聚类中心指导门控网络的学习。
    """

    def __init__(
        self,
        full_input_dim: int = 10301,
        reaction_fp_dim: int = 6144,
        num_clusters: int = 8,
        expert_hidden_dims: List[int] = [256, 128],
        dropout: float = 0.3,
        cluster_centers: Optional[torch.Tensor] = None,
    ):
        super().__init__()

        self.full_input_dim = full_input_dim
        self.reaction_fp_dim = reaction_fp_dim
        self.num_clusters = num_clusters

        # 聚类中心（可以用 K-Means 初始化）
        if cluster_centers is not None:
            self.register_buffer('cluster_centers', cluster_centers)
        else:
            # 随机初始化，之后用 K-Means 更新
            self.register_buffer(
                'cluster_centers',
                torch.randn(num_clusters, reaction_fp_dim)
            )

        # 反应指纹编码器
        self.fp_encoder = nn.Sequential(
            nn.Linear(reaction_fp_dim, 512),
            nn.LayerNorm(512),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(512, 256),
            nn.LayerNorm(256),
            nn.GELU(),
        )

        # 聚类中心编码器（共享参数以对齐空间）
        self.center_encoder = nn.Sequential(
            nn.Linear(reaction_fp_dim, 512),
            nn.LayerNorm(512),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(512, 256),
            nn.LayerNorm(256),
            nn.GELU(),
        )

        # 专家网络
        self.experts = nn.ModuleList([
            ExpertNetwork(
                input_dim=full_input_dim,
                hidden_dims=expert_hidden_dims,
                dropout=dropout
            )
            for _ in range(num_clusters)
        ])

    def compute_cluster_weights(self, reaction_fp: torch.Tensor) -> torch.Tensor:
        """
        计算反应与各聚类中心的相似度权重

        使用编码后的余弦相似度，然后 softmax 归一化
        """
        # 编码反应指纹
        fp_encoded = self.fp_encoder(reaction_fp)  # [B, 256]
        fp_encoded = F.normalize(fp_encoded, dim=-1)

        # 编码聚类中心
        centers_encoded = self.center_encoder(self.cluster_centers)  # [K, 256]
        centers_encoded = F.normalize(centers_encoded, dim=-1)

        # 计算相似度（余弦相似度）
        similarities = torch.matmul(fp_encoded, centers_encoded.T)  # [B, K]

        # softmax 得到权重
        weights = F.softmax(similarities * 10, dim=-1)  # 温度=0.1

        return weights

    def forward(
        self,
        full_features: torch.Tensor,
        reaction_fp: Optional[torch.Tensor] = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """前向传播"""
        if reaction_fp is None:
            reaction_fp = full_features[:, :self.reaction_fp_dim]

        # 计算聚类权重
        cluster_weights = self.compute_cluster_weights(reaction_fp)  # [B, K]

        # 所有专家预测
        expert_outputs = torch.stack([
            expert(full_features) for expert in self.experts
        ], dim=1).squeeze(-1)  # [B, K]

        # 加权组合
        yield_pred = (cluster_weights * expert_outputs).sum(dim=-1, keepdim=True)

        return yield_pred, cluster_weights

    def init_clusters_with_kmeans(self, reaction_fps: torch.Tensor):
        """使用 K-Means 初始化聚类中心"""
        from sklearn.cluster import KMeans
        import numpy as np

        fps_np = reaction_fps.cpu().numpy()
        kmeans = KMeans(n_clusters=self.num_clusters, random_state=42, n_init=10)
        kmeans.fit(fps_np)

        centers = torch.from_numpy(kmeans.cluster_centers_).float()
        self.cluster_centers.copy_(centers)

        return kmeans.labels_

    def get_load_balance_loss(self, expert_weights: torch.Tensor) -> torch.Tensor:
        """计算负载均衡损失"""
        avg_weights = expert_weights.mean(dim=0)
        target = torch.ones_like(avg_weights) / self.num_clusters
        loss = F.kl_div(
            torch.log(avg_weights + 1e-8),
            target,
            reduction='sum'
        )
        return loss


class HierarchicalMoEYieldPredictor(nn.Module):
    """
    分层 MoE 产率预测模型

    架构：
    Level 1: 粗粒度分类（如反应类型）
    Level 2: 细粒度专家（每个粗类别下的多个专家）

    这种分层结构可以更好地处理反应的层次结构
    """

    def __init__(
        self,
        full_input_dim: int = 10301,
        reaction_fp_dim: int = 6144,
        num_coarse_classes: int = 4,   # 粗粒度类别数
        num_fine_experts: int = 2,      # 每个粗类别下的专家数
        expert_hidden_dims: List[int] = [256, 128],
        dropout: float = 0.3,
    ):
        super().__init__()

        self.num_coarse = num_coarse_classes
        self.num_fine = num_fine_experts
        self.total_experts = num_coarse_classes * num_fine_experts

        # 粗粒度分类器
        self.coarse_classifier = nn.Sequential(
            nn.Linear(reaction_fp_dim, 512),
            nn.LayerNorm(512),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(512, 256),
            nn.LayerNorm(256),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(256, num_coarse_classes)
        )

        # 细粒度门控网络（每个粗类别一个）
        self.fine_gates = nn.ModuleList([
            nn.Sequential(
                nn.Linear(reaction_fp_dim, 128),
                nn.LayerNorm(128),
                nn.GELU(),
                nn.Dropout(dropout),
                nn.Linear(128, num_fine_experts)
            )
            for _ in range(num_coarse_classes)
        ])

        # 专家网络（total = coarse * fine）
        self.experts = nn.ModuleList([
            ExpertNetwork(
                input_dim=full_input_dim,
                hidden_dims=expert_hidden_dims,
                dropout=dropout
            )
            for _ in range(self.total_experts)
        ])

    def forward(
        self,
        full_features: torch.Tensor,
        reaction_fp: Optional[torch.Tensor] = None
    ) -> Tuple[torch.Tensor, dict]:
        """前向传播"""
        batch_size = full_features.size(0)

        if reaction_fp is None:
            reaction_fp = full_features[:, :6144]

        # 粗粒度分类
        coarse_logits = self.coarse_classifier(reaction_fp)
        coarse_weights = F.softmax(coarse_logits, dim=-1)  # [B, C]

        # 细粒度门控
        fine_weights_list = []
        for i in range(self.num_coarse):
            fine_logits = self.fine_gates[i](reaction_fp)
            fine_weights = F.softmax(fine_logits, dim=-1)  # [B, F]
            fine_weights_list.append(fine_weights)

        fine_weights = torch.stack(fine_weights_list, dim=1)  # [B, C, F]

        # 计算所有专家的输出
        expert_outputs = torch.stack([
            expert(full_features) for expert in self.experts
        ], dim=1).squeeze(-1)  # [B, C*F]

        expert_outputs = expert_outputs.view(batch_size, self.num_coarse, self.num_fine)  # [B, C, F]

        # 层次化加权
        # 先在细粒度层面加权
        fine_combined = (fine_weights * expert_outputs).sum(dim=-1)  # [B, C]
        # 再在粗粒度层面加权
        yield_pred = (coarse_weights * fine_combined).sum(dim=-1, keepdim=True)  # [B, 1]

        return yield_pred, {
            'coarse_weights': coarse_weights,
            'fine_weights': fine_weights,
        }

    def get_load_balance_loss(self, expert_weights) -> torch.Tensor:
        """计算负载均衡损失 (对于分层模型，使用粗粒度权重)"""
        if isinstance(expert_weights, dict):
            coarse_weights = expert_weights['coarse_weights']
        else:
            coarse_weights = expert_weights
        avg_weights = coarse_weights.mean(dim=0)
        target = torch.ones_like(avg_weights) / self.num_coarse
        loss = F.kl_div(
            torch.log(avg_weights + 1e-8),
            target,
            reduction='sum'
        )
        return loss


def create_moe_yield_predictor(
    model_type: str = "standard",
    **kwargs
) -> nn.Module:
    """
    创建 MoE 产率预测模型

    Args:
        model_type: 模型类型
            - "standard": 标准 MoE
            - "cluster_aware": 带预聚类的 MoE
            - "hierarchical": 分层 MoE
    """
    if model_type == "standard":
        return MoEYieldPredictor(**kwargs)
    elif model_type == "cluster_aware":
        return ClusterAwareMoEYieldPredictor(**kwargs)
    elif model_type == "hierarchical":
        return HierarchicalMoEYieldPredictor(**kwargs)
    else:
        raise ValueError(f"Unknown model type: {model_type}")


if __name__ == "__main__":
    # 测试模型
    batch_size = 32
    full_dim = 10301
    fp_dim = 6144

    print("=" * 60)
    print("测试 MoE 产率预测模型")
    print("=" * 60)

    # 1. 标准 MoE
    print("\n1. 标准 MoE 模型")
    model = MoEYieldPredictor(
        full_input_dim=full_dim,
        reaction_fp_dim=fp_dim,
        num_experts=8,
    )
    x = torch.randn(batch_size, full_dim)
    y, weights = model(x)
    print(f"   输入: {x.shape}")
    print(f"   输出: {y.shape}, 范围: [{y.min():.3f}, {y.max():.3f}]")
    print(f"   专家权重: {weights.shape}")
    print(f"   参数量: {sum(p.numel() for p in model.parameters()):,}")

    # 2. 带聚类的 MoE
    print("\n2. 带聚类的 MoE 模型")
    model2 = ClusterAwareMoEYieldPredictor(
        full_input_dim=full_dim,
        reaction_fp_dim=fp_dim,
        num_clusters=8,
    )
    y2, weights2 = model2(x)
    print(f"   输出: {y2.shape}")
    print(f"   聚类权重: {weights2.shape}")
    print(f"   参数量: {sum(p.numel() for p in model2.parameters()):,}")

    # 3. 分层 MoE
    print("\n3. 分层 MoE 模型")
    model3 = HierarchicalMoEYieldPredictor(
        full_input_dim=full_dim,
        reaction_fp_dim=fp_dim,
        num_coarse_classes=4,
        num_fine_experts=2,
    )
    y3, info = model3(x)
    print(f"   输出: {y3.shape}")
    print(f"   粗粒度权重: {info['coarse_weights'].shape}")
    print(f"   细粒度权重: {info['fine_weights'].shape}")
    print(f"   参数量: {sum(p.numel() for p in model3.parameters()):,}")

    print("\n测试完成!")
