"""
产率预测模型
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Optional


class YieldPredictor(nn.Module):
    """产率预测神经网络"""

    def __init__(
        self,
        input_dim: int,
        hidden_dims: List[int] = [512, 256, 128],
        dropout: float = 0.2
    ):
        super().__init__()

        self.input_dim = input_dim
        self.hidden_dims = hidden_dims

        # 构建MLP层
        layers = []
        prev_dim = input_dim

        for hidden_dim in hidden_dims:
            layers.extend([
                nn.Linear(prev_dim, hidden_dim),
                nn.BatchNorm1d(hidden_dim),
                nn.ReLU(),
                nn.Dropout(dropout)
            ])
            prev_dim = hidden_dim

        self.encoder = nn.Sequential(*layers)

        # 输出层
        self.output_layer = nn.Linear(hidden_dims[-1], 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        前向传播
        Args:
            x: 输入特征 [batch_size, input_dim]
        Returns:
            yield_pred: 产率预测 [batch_size, 1]
        """
        h = self.encoder(x)
        yield_pred = torch.sigmoid(self.output_layer(h))  # 输出0-1
        return yield_pred

    def forward_raw(self, x: torch.Tensor) -> torch.Tensor:
        """返回 sigmoid 之前的原始 logit，用于 pairwise ranking loss"""
        h = self.encoder(x)
        return self.output_layer(h)

    def predict_yield(self, x: torch.Tensor) -> torch.Tensor:
        """预测产率（百分比）"""
        with torch.no_grad():
            yield_01 = self.forward(x)
            return yield_01 * 100  # 转换为百分比


class AttentionYieldPredictor(nn.Module):
    """带注意力机制的产率预测模型"""

    def __init__(
        self,
        reaction_dim: int,  # 反应指纹维度
        condition_dim: int,  # 条件特征维度
        hidden_dim: int = 256,
        num_heads: int = 4,
        dropout: float = 0.2
    ):
        super().__init__()

        self.reaction_dim = reaction_dim
        self.condition_dim = condition_dim

        # 反应编码器
        self.reaction_encoder = nn.Sequential(
            nn.Linear(reaction_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout)
        )

        # 条件编码器
        self.condition_encoder = nn.Sequential(
            nn.Linear(condition_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout)
        )

        # 多头注意力
        self.attention = nn.MultiheadAttention(
            embed_dim=hidden_dim,
            num_heads=num_heads,
            dropout=dropout,
            batch_first=True
        )

        # 输出层
        self.output_mlp = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, 1)
        )

    def forward(
        self,
        reaction_features: torch.Tensor,
        condition_features: torch.Tensor
    ) -> torch.Tensor:
        """
        前向传播
        Args:
            reaction_features: 反应特征 [batch_size, reaction_dim]
            condition_features: 条件特征 [batch_size, condition_dim]
        """
        # 编码
        reaction_h = self.reaction_encoder(reaction_features)  # [B, H]
        condition_h = self.condition_encoder(condition_features)  # [B, H]

        # 注意力：条件对反应的影响
        reaction_h = reaction_h.unsqueeze(1)  # [B, 1, H]
        condition_h = condition_h.unsqueeze(1)  # [B, 1, H]

        attn_out, _ = self.attention(
            query=reaction_h,
            key=condition_h,
            value=condition_h
        )

        # 合并特征
        combined = torch.cat([
            reaction_h.squeeze(1),
            attn_out.squeeze(1)
        ], dim=-1)

        # 预测产率
        yield_pred = torch.sigmoid(self.output_mlp(combined))
        return yield_pred


class MultiTaskYieldPredictor(nn.Module):
    """多任务学习：同时预测产率和分类高/低产率"""

    def __init__(
        self,
        input_dim: int,
        hidden_dims: List[int] = [512, 256, 128],
        dropout: float = 0.2,
        num_yield_classes: int = 10  # 产率分10档
    ):
        super().__init__()

        # 共享编码器
        layers = []
        prev_dim = input_dim

        for hidden_dim in hidden_dims[:-1]:
            layers.extend([
                nn.Linear(prev_dim, hidden_dim),
                nn.BatchNorm1d(hidden_dim),
                nn.ReLU(),
                nn.Dropout(dropout)
            ])
            prev_dim = hidden_dim

        self.shared_encoder = nn.Sequential(*layers)

        # 回归头（产率预测）
        self.regression_head = nn.Sequential(
            nn.Linear(prev_dim, hidden_dims[-1]),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dims[-1], 1)
        )

        # 分类头（产率档位分类）
        self.classification_head = nn.Sequential(
            nn.Linear(prev_dim, hidden_dims[-1]),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dims[-1], num_yield_classes)
        )

    def forward(self, x: torch.Tensor):
        """
        前向传播
        Returns:
            yield_pred: 产率回归预测
            class_logits: 产率分类logits
        """
        shared_features = self.shared_encoder(x)

        yield_pred = torch.sigmoid(self.regression_head(shared_features))
        class_logits = self.classification_head(shared_features)

        return yield_pred, class_logits


def create_yield_predictor(
    input_dim: int,
    model_type: str = "simple",
    **kwargs
) -> nn.Module:
    """
    创建产率预测模型
    Args:
        input_dim: 输入特征维度
        model_type: 模型类型 (simple, attention, multitask)
    """
    if model_type == "simple":
        return YieldPredictor(input_dim, **kwargs)
    elif model_type == "attention":
        # 需要分离反应和条件特征
        raise NotImplementedError("Attention model requires separate features")
    elif model_type == "multitask":
        return MultiTaskYieldPredictor(input_dim, **kwargs)
    else:
        raise ValueError(f"Unknown model type: {model_type}")


if __name__ == "__main__":
    # 测试模型
    batch_size = 32
    input_dim = 10246

    model = YieldPredictor(input_dim)
    x = torch.randn(batch_size, input_dim)
    y = model(x)
    print(f"Output shape: {y.shape}")
    print(f"Output range: [{y.min().item():.4f}, {y.max().item():.4f}]")
