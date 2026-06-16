"""
多种产率预测模型架构
"""
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Optional, Dict


# ============================================================
# 1. MLP (当前使用的基础模型)
# ============================================================
class MLPPredictor(nn.Module):
    """多层感知机 - 简单快速"""

    def __init__(
        self,
        input_dim: int,
        hidden_dims: List[int] = [512, 256, 128],
        dropout: float = 0.2
    ):
        super().__init__()
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
        self.output = nn.Linear(hidden_dims[-1], 1)

    def forward(self, x):
        h = self.encoder(x)
        return torch.sigmoid(self.output(h))


# ============================================================
# 2. ResNet风格的深度网络
# ============================================================
class ResidualBlock(nn.Module):
    """残差块"""

    def __init__(self, dim: int, dropout: float = 0.2):
        super().__init__()
        self.block = nn.Sequential(
            nn.Linear(dim, dim),
            nn.BatchNorm1d(dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(dim, dim),
            nn.BatchNorm1d(dim)
        )
        self.relu = nn.ReLU()

    def forward(self, x):
        return self.relu(x + self.block(x))


class ResNetPredictor(nn.Module):
    """残差网络 - 更深的模型，更好的梯度流"""

    def __init__(
        self,
        input_dim: int,
        hidden_dim: int = 512,
        num_blocks: int = 4,
        dropout: float = 0.2
    ):
        super().__init__()

        self.input_proj = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU()
        )

        self.blocks = nn.Sequential(*[
            ResidualBlock(hidden_dim, dropout) for _ in range(num_blocks)
        ])

        self.output = nn.Sequential(
            nn.Linear(hidden_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def forward(self, x):
        h = self.input_proj(x)
        h = self.blocks(h)
        return torch.sigmoid(self.output(h))


# ============================================================
# 3. Transformer编码器
# ============================================================
class TransformerPredictor(nn.Module):
    """Transformer - 捕捉特征间的复杂关系"""

    def __init__(
        self,
        input_dim: int,
        d_model: int = 256,
        nhead: int = 8,
        num_layers: int = 4,
        dropout: float = 0.1
    ):
        super().__init__()

        self.input_proj = nn.Linear(input_dim, d_model)

        # 将输入分成多个token
        self.num_tokens = 16
        self.token_dim = d_model

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=d_model * 4,
            dropout=dropout,
            batch_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)

        self.output = nn.Sequential(
            nn.Linear(d_model, 128),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(128, 1)
        )

        # 可学习的位置编码
        self.pos_embedding = nn.Parameter(torch.randn(1, self.num_tokens, d_model) * 0.02)

    def forward(self, x):
        # x: [B, input_dim]
        h = self.input_proj(x)  # [B, d_model]

        # 重塑为序列
        B = h.size(0)
        h = h.unsqueeze(1).expand(-1, self.num_tokens, -1)  # [B, num_tokens, d_model]
        h = h + self.pos_embedding

        # Transformer编码
        h = self.transformer(h)  # [B, num_tokens, d_model]

        # 池化
        h = h.mean(dim=1)  # [B, d_model]

        return torch.sigmoid(self.output(h))


# ============================================================
# 4. 注意力增强的MLP
# ============================================================
class AttentionMLP(nn.Module):
    """带自注意力的MLP - 学习特征重要性"""

    def __init__(
        self,
        input_dim: int,
        hidden_dim: int = 512,
        num_heads: int = 8,
        dropout: float = 0.2
    ):
        super().__init__()

        self.input_proj = nn.Linear(input_dim, hidden_dim)

        # 多头自注意力
        self.attention = nn.MultiheadAttention(
            embed_dim=hidden_dim,
            num_heads=num_heads,
            dropout=dropout,
            batch_first=True
        )

        self.mlp = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim // 2, 1)
        )

        self.norm = nn.LayerNorm(hidden_dim)

    def forward(self, x):
        h = self.input_proj(x)
        h = h.unsqueeze(1)  # [B, 1, H]

        # 自注意力
        attn_out, _ = self.attention(h, h, h)
        h = self.norm(h + attn_out)

        h = h.squeeze(1)
        return torch.sigmoid(self.mlp(h))


# ============================================================
# 5. 双塔模型（分别编码反应和条件）
# ============================================================
class DualTowerPredictor(nn.Module):
    """双塔模型 - 分别编码反应和条件，然后融合"""

    def __init__(
        self,
        reaction_dim: int = 6144,  # 3 * 2048
        condition_dim: int = 4102,  # 2 * 2048 + 6
        hidden_dim: int = 256,
        dropout: float = 0.2
    ):
        super().__init__()

        # 反应编码塔
        self.reaction_tower = nn.Sequential(
            nn.Linear(reaction_dim, hidden_dim * 2),
            nn.BatchNorm1d(hidden_dim * 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU()
        )

        # 条件编码塔
        self.condition_tower = nn.Sequential(
            nn.Linear(condition_dim, hidden_dim * 2),
            nn.BatchNorm1d(hidden_dim * 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU()
        )

        # 融合层
        self.fusion = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

        # 交互注意力
        self.cross_attention = nn.MultiheadAttention(
            embed_dim=hidden_dim,
            num_heads=4,
            dropout=dropout,
            batch_first=True
        )

    def forward(self, x, reaction_dim=6144):
        # 分割输入
        reaction_feat = x[:, :reaction_dim]
        condition_feat = x[:, reaction_dim:]

        # 编码
        reaction_h = self.reaction_tower(reaction_feat)  # [B, H]
        condition_h = self.condition_tower(condition_feat)  # [B, H]

        # 交叉注意力
        reaction_h = reaction_h.unsqueeze(1)  # [B, 1, H]
        condition_h = condition_h.unsqueeze(1)

        attn_out, _ = self.cross_attention(reaction_h, condition_h, condition_h)
        reaction_h = (reaction_h + attn_out).squeeze(1)
        condition_h = condition_h.squeeze(1)

        # 融合
        combined = torch.cat([reaction_h, condition_h], dim=-1)
        return torch.sigmoid(self.fusion(combined))


# ============================================================
# 6. Highway网络
# ============================================================
class HighwayLayer(nn.Module):
    """Highway层"""

    def __init__(self, dim: int):
        super().__init__()
        self.transform = nn.Linear(dim, dim)
        self.gate = nn.Linear(dim, dim)

    def forward(self, x):
        t = torch.sigmoid(self.gate(x))
        h = F.relu(self.transform(x))
        return t * h + (1 - t) * x


class HighwayPredictor(nn.Module):
    """Highway网络 - 自适应深度"""

    def __init__(
        self,
        input_dim: int,
        hidden_dim: int = 512,
        num_layers: int = 6,
        dropout: float = 0.2
    ):
        super().__init__()

        self.input_proj = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU()
        )

        self.highways = nn.Sequential(*[
            HighwayLayer(hidden_dim) for _ in range(num_layers)
        ])

        self.output = nn.Sequential(
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def forward(self, x):
        h = self.input_proj(x)
        h = self.highways(h)
        return torch.sigmoid(self.output(h))


# ============================================================
# 7. 集成模型
# ============================================================
class EnsemblePredictor(nn.Module):
    """集成多个模型"""

    def __init__(self, input_dim: int, dropout: float = 0.2):
        super().__init__()

        self.models = nn.ModuleList([
            MLPPredictor(input_dim, [512, 256, 128], dropout),
            ResNetPredictor(input_dim, 256, 3, dropout),
            HighwayPredictor(input_dim, 256, 4, dropout)
        ])

        # 学习权重
        self.weights = nn.Parameter(torch.ones(len(self.models)) / len(self.models))

    def forward(self, x):
        outputs = torch.stack([m(x) for m in self.models], dim=-1)  # [B, 1, num_models]
        weights = F.softmax(self.weights, dim=0)
        return (outputs * weights).sum(dim=-1)


# ============================================================
# 8. 双塔XTB融合模型
# ============================================================
class DualTowerXTBPredictor(nn.Module):
    """双塔模型 - 指纹塔 + XTB量子特征塔，门控融合

    将高维稀疏指纹和低维稠密XTB特征分别压缩到低维空间，
    通过门控机制自适应融合两类异质特征。
    """

    def __init__(
        self,
        input_dim: int,  # 总输入维度（仅用于兼容接口）
        fp_dim: int = 10246,  # 指纹特征维度
        xtb_dim: int = 55,  # XTB特征维度
        fp_hidden: int = 256,  # 指纹塔输出维度
        xtb_hidden: int = 64,  # XTB塔输出维度
        dropout: float = 0.2
    ):
        super().__init__()
        self.fp_dim = fp_dim
        self.xtb_dim = xtb_dim

        # Tower 1: 指纹塔（高维稀疏 → 低维稠密）
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

        # Tower 2: XTB塔（低维稠密 → 增强表征）
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

        # 门控融合：学习两个塔的贡献权重
        self.gate = nn.Sequential(
            nn.Linear(fused_dim, fused_dim),
            nn.Sigmoid()
        )

        # 预测头
        self.predictor = nn.Sequential(
            nn.Linear(fused_dim, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(128, 1)
        )

    def forward(self, x):
        # 切分特征
        fp_feat = x[:, :self.fp_dim]
        xtb_feat = x[:, self.fp_dim:]

        # 双塔编码
        fp_h = self.fp_tower(fp_feat)
        xtb_h = self.xtb_tower(xtb_feat)

        # 门控融合
        combined = torch.cat([fp_h, xtb_h], dim=-1)
        gate_weights = self.gate(combined)
        fused = combined * gate_weights

        return torch.sigmoid(self.predictor(fused))


# ============================================================
# 9. Compact模型（PCA降维指纹 + 溶剂/电解质Embedding）
# ============================================================
class CompactYieldPredictor(nn.Module):
    """紧凑产率预测模型

    PCA压缩反应指纹 + 可学习溶剂/电解质Embedding + 电化学参数 + xTB特征
    总输入维度 ~253D（vs 原来10,301D），参数量大幅减少。
    """

    def __init__(
        self,
        continuous_dim: int,  # PCA反应特征 + 电化学参数 + xTB特征
        num_solvents: int = 94,  # 93 + 1(unknown)
        num_electrolytes: int = 101,  # 100 + 1(unknown)
        embed_dim: int = 32,
        hidden_dims: List[int] = [256, 128],
        dropout: float = 0.2
    ):
        super().__init__()

        self.solvent_embed = nn.Embedding(num_solvents, embed_dim)
        self.electrolyte_embed = nn.Embedding(num_electrolytes, embed_dim)

        fused_dim = continuous_dim + embed_dim * 2  # ~253

        layers = []
        prev_dim = fused_dim
        for h_dim in hidden_dims:
            layers.extend([
                nn.Linear(prev_dim, h_dim),
                nn.BatchNorm1d(h_dim),
                nn.ReLU(),
                nn.Dropout(dropout)
            ])
            prev_dim = h_dim

        self.encoder = nn.Sequential(*layers)
        self.output = nn.Linear(prev_dim, 1)

    def forward(self, continuous, solvent_idx, electrolyte_idx):
        """
        Args:
            continuous: [B, continuous_dim] PCA反应FP + echem + xTB
            solvent_idx: [B] 溶剂词汇表索引
            electrolyte_idx: [B] 电解质词汇表索引
        """
        solvent_emb = self.solvent_embed(solvent_idx)  # [B, 32]
        electrolyte_emb = self.electrolyte_embed(electrolyte_idx)  # [B, 32]

        x = torch.cat([continuous, solvent_emb, electrolyte_emb], dim=-1)
        h = self.encoder(x)
        return torch.sigmoid(self.output(h))


# ============================================================
# 模型工厂
# ============================================================
MODEL_REGISTRY = {
    'mlp': MLPPredictor,
    'resnet': ResNetPredictor,
    'transformer': TransformerPredictor,
    'attention_mlp': AttentionMLP,
    'dual_tower': DualTowerPredictor,
    'highway': HighwayPredictor,
    'ensemble': EnsemblePredictor,
    'dual_tower_xtb': DualTowerXTBPredictor,
    # 'gnn': GNNYieldPredictor — GNN模型需要图数据输入，使用专用的 train_gnn.py 训练
}


def create_model(model_name: str, input_dim: int, **kwargs) -> nn.Module:
    """创建模型"""
    if model_name not in MODEL_REGISTRY:
        raise ValueError(f"Unknown model: {model_name}. Available: {list(MODEL_REGISTRY.keys())}")

    model_class = MODEL_REGISTRY[model_name]

    # 设置默认参数
    if model_name == 'mlp':
        kwargs.setdefault('hidden_dims', [512, 256, 128])
    elif model_name == 'resnet':
        kwargs.setdefault('hidden_dim', 512)
        kwargs.setdefault('num_blocks', 4)
    elif model_name == 'transformer':
        kwargs.setdefault('d_model', 256)
        kwargs.setdefault('nhead', 8)
        kwargs.setdefault('num_layers', 4)
    elif model_name == 'attention_mlp':
        kwargs.setdefault('hidden_dim', 512)
        kwargs.setdefault('num_heads', 8)
    elif model_name == 'highway':
        kwargs.setdefault('hidden_dim', 512)
        kwargs.setdefault('num_layers', 6)

    return model_class(input_dim, **kwargs)


def get_model_info():
    """获取所有可用模型信息"""
    return {
        'mlp': {
            'name': 'MLP (Multi-Layer Perceptron)',
            'description': '简单快速的全连接网络',
            'params': '~3M',
            'speed': '快'
        },
        'resnet': {
            'name': 'ResNet',
            'description': '残差连接的深度网络，更好的梯度流',
            'params': '~5M',
            'speed': '中'
        },
        'transformer': {
            'name': 'Transformer',
            'description': '自注意力机制，捕捉复杂特征关系',
            'params': '~8M',
            'speed': '慢'
        },
        'attention_mlp': {
            'name': 'Attention MLP',
            'description': '带注意力的MLP，学习特征重要性',
            'params': '~4M',
            'speed': '中'
        },
        'dual_tower': {
            'name': 'Dual Tower',
            'description': '双塔模型，分别编码反应和条件',
            'params': '~4M',
            'speed': '中'
        },
        'highway': {
            'name': 'Highway Network',
            'description': 'Highway连接，自适应深度',
            'params': '~4M',
            'speed': '中'
        },
        'ensemble': {
            'name': 'Ensemble',
            'description': '集成多个模型，更稳定',
            'params': '~12M',
            'speed': '慢'
        },
        'gnn': {
            'name': 'GNN (Graph Neural Network)',
            'description': 'GIN图神经网络 + xTB量化描述符，学习分子图表征',
            'params': '~3M',
            'speed': '中',
            'note': '需要使用 train_gnn.py 训练'
        }
    }


if __name__ == "__main__":
    # 测试所有模型
    input_dim = 10246
    batch_size = 8
    x = torch.randn(batch_size, input_dim)

    print("Testing all models:\n")
    for name, info in get_model_info().items():
        try:
            model = create_model(name, input_dim)
            y = model(x)
            params = sum(p.numel() for p in model.parameters())
            print(f"{name:15s} | output: {y.shape} | params: {params:,}")
        except Exception as e:
            print(f"{name:15s} | ERROR: {e}")
