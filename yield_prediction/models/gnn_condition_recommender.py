"""
GNN 条件推荐模型：基于分子图结构学习，推荐电化学反应条件

核心架构：
1. HybridMolecularGNN 编码反应物和产物的分子图 (原子级结构 + xTB量子特征)
2. ReactionTransformer 学习反应物到产物的化学转变
3. 多分类头预测各个反应条件

预测目标：
- 阳极 (anode)
- 阴极 (cathode)
- 电解池类型 (cell_type)
- 电解质 (electrolyte)
- 溶剂 (solvent)
- 试剂 (reagent)
- 催化剂 (catalyst)
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, Optional, List


class EdgeGatedMessagePassing(nn.Module):
    """边门控消息传递层"""

    def __init__(self, node_dim: int, edge_dim: int, num_heads: int = 4, dropout: float = 0.1):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = node_dim // num_heads

        # 边门控
        self.edge_gate = nn.Sequential(
            nn.Linear(edge_dim, node_dim),
            nn.Sigmoid(),
        )

        # 消息变换
        self.query = nn.Linear(node_dim, node_dim)
        self.key = nn.Linear(node_dim, node_dim)
        self.value = nn.Linear(node_dim, node_dim)

        self.out_proj = nn.Linear(node_dim, node_dim)
        self.layer_norm = nn.LayerNorm(node_dim)
        self.dropout = nn.Dropout(dropout)

        self.ffn = nn.Sequential(
            nn.Linear(node_dim, node_dim * 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(node_dim * 2, node_dim),
            nn.Dropout(dropout),
        )
        self.ffn_norm = nn.LayerNorm(node_dim)

    def forward(self, node_feats, edge_index, edge_feats):
        num_nodes = node_feats.shape[0]
        if edge_index.shape[1] == 0:
            return node_feats

        src, tgt = edge_index[0], edge_index[1]

        Q = self.query(node_feats)
        K = self.key(node_feats)
        V = self.value(node_feats)

        edge_gate = self.edge_gate(edge_feats)

        Q_src = Q[src].view(-1, self.num_heads, self.head_dim)
        K_tgt = K[tgt].view(-1, self.num_heads, self.head_dim)
        V_src = V[src].view(-1, self.num_heads, self.head_dim)

        attn_scores = (Q_src * K_tgt).sum(dim=-1) / (self.head_dim ** 0.5)
        edge_gate = edge_gate.view(-1, self.num_heads, self.head_dim)
        V_gated = V_src * edge_gate

        attn_scores = attn_scores.unsqueeze(-1)
        attn_max = torch.zeros(num_nodes, self.num_heads, 1, device=node_feats.device)
        attn_max.scatter_reduce_(0, tgt.view(-1, 1, 1).expand(-1, self.num_heads, 1),
                                  attn_scores, reduce='amax')
        attn_scores = attn_scores - attn_max[tgt]
        attn_weights = torch.exp(attn_scores)

        attn_sum = torch.zeros(num_nodes, self.num_heads, 1, device=node_feats.device)
        attn_sum.scatter_add_(0, tgt.view(-1, 1, 1).expand(-1, self.num_heads, 1), attn_weights)
        attn_weights = attn_weights / attn_sum[tgt].clamp(min=1e-8)

        messages = V_gated * attn_weights
        messages = messages.view(-1, node_feats.shape[-1])

        agg = torch.zeros_like(node_feats)
        agg.scatter_add_(0, tgt.unsqueeze(-1).expand_as(messages), messages)

        out = self.out_proj(agg)
        out = self.dropout(out)
        out = self.layer_norm(node_feats + out)
        out = out + self.ffn(out)
        out = self.ffn_norm(out)

        return out


class XTBFeatureEncoder(nn.Module):
    """xTB量子化学特征编码器"""

    def __init__(self, input_dim: int = 11, hidden_dim: int = 64, output_dim: int = 64, dropout: float = 0.1):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, output_dim),
            nn.LayerNorm(output_dim),
            nn.GELU(),
        )

    def forward(self, x):
        return self.encoder(x)


class MolecularGNN(nn.Module):
    """分子GNN编码器"""

    def __init__(
        self,
        atom_feat_dim: int = 42,
        edge_feat_dim: int = 10,
        xtb_feat_dim: int = 11,
        hidden_dim: int = 128,
        num_layers: int = 3,
        num_heads: int = 4,
        dropout: float = 0.2,
    ):
        super().__init__()
        self.hidden_dim = hidden_dim

        self.node_embed = nn.Sequential(
            nn.Linear(atom_feat_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.GELU(),
        )

        self.edge_embed = nn.Sequential(
            nn.Linear(edge_feat_dim, hidden_dim // 2),
            nn.GELU(),
        )

        self.mp_layers = nn.ModuleList([
            EdgeGatedMessagePassing(hidden_dim, hidden_dim // 2, num_heads, dropout)
            for _ in range(num_layers)
        ])

        self.xtb_encoder = XTBFeatureEncoder(xtb_feat_dim, hidden_dim, hidden_dim // 2, dropout)

        self.attention_pool = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.Tanh(),
            nn.Linear(hidden_dim // 2, 1),
        )

        # GNN (mean + attn) + xTB
        self.fusion = nn.Sequential(
            nn.Linear(hidden_dim * 2 + hidden_dim // 2, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
        )

    def forward(self, node_feats, edge_index, edge_feats, batch, num_graphs, xtb_feats=None):
        h = self.node_embed(node_feats)

        if edge_feats.shape[0] > 0:
            e = self.edge_embed(edge_feats)
        else:
            e = torch.zeros(0, self.hidden_dim // 2, device=node_feats.device)

        for mp_layer in self.mp_layers:
            h = mp_layer(h, edge_index, e)

        # Mean pooling
        mean_pool = self._scatter_mean(h, batch, num_graphs)

        # Attention pooling
        attn_weights = self.attention_pool(h)
        attn_weights = self._scatter_softmax(attn_weights, batch, num_graphs)
        attn_pool = self._scatter_sum(h * attn_weights, batch, num_graphs)

        # xTB特征
        if xtb_feats is not None:
            xtb_emb = self.xtb_encoder(xtb_feats)
        else:
            xtb_emb = torch.zeros(num_graphs, self.hidden_dim // 2, device=h.device)

        graph_repr = torch.cat([mean_pool, attn_pool, xtb_emb], dim=-1)
        return self.fusion(graph_repr)

    def _scatter_mean(self, x, batch, num_graphs):
        out = torch.zeros(num_graphs, x.shape[-1], device=x.device)
        idx = batch.unsqueeze(-1).expand_as(x)
        out.scatter_add_(0, idx, x)
        counts = torch.bincount(batch, minlength=num_graphs).float().unsqueeze(-1).clamp(min=1)
        return out / counts.to(x.device)

    def _scatter_sum(self, x, batch, num_graphs):
        out = torch.zeros(num_graphs, x.shape[-1], device=x.device)
        idx = batch.unsqueeze(-1).expand_as(x)
        return out.scatter_add_(0, idx, x)

    def _scatter_softmax(self, x, batch, num_graphs):
        max_vals = torch.zeros(num_graphs, x.shape[-1], device=x.device)
        idx = batch.unsqueeze(-1).expand_as(x)
        max_vals.scatter_reduce_(0, idx, x, reduce='amax')
        x_shifted = x - max_vals[batch]
        exp_x = torch.exp(x_shifted)
        sum_exp = torch.zeros(num_graphs, x.shape[-1], device=x.device)
        sum_exp.scatter_add_(0, idx, exp_x)
        return exp_x / sum_exp[batch].clamp(min=1e-8)


class ReactionTransformer(nn.Module):
    """反应变化建模器：交叉注意力学习反应物→产物转变"""

    def __init__(self, hidden_dim: int = 128, num_heads: int = 4, dropout: float = 0.2):
        super().__init__()
        self.cross_attn_r2p = nn.MultiheadAttention(
            hidden_dim, num_heads, dropout=dropout, batch_first=True
        )
        self.cross_attn_p2r = nn.MultiheadAttention(
            hidden_dim, num_heads, dropout=dropout, batch_first=True
        )
        self.norm1 = nn.LayerNorm(hidden_dim)
        self.norm2 = nn.LayerNorm(hidden_dim)

        self.ffn = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
        )

    def forward(self, reactant_emb, product_emb):
        r = reactant_emb.unsqueeze(1)
        p = product_emb.unsqueeze(1)

        r_attended, _ = self.cross_attn_r2p(r, p, p)
        r_attended = self.norm1(r + r_attended)

        p_attended, _ = self.cross_attn_p2r(p, r, r)
        p_attended = self.norm2(p + p_attended)

        combined = torch.cat([r_attended.squeeze(1), p_attended.squeeze(1)], dim=-1)
        return self.ffn(combined)


class GNNConditionRecommender(nn.Module):
    """
    GNN 条件推荐模型

    架构：
    1. 反应物/产物分子图 → MolecularGNN → 分子表示
    2. 反应物+产物表示 → ReactionTransformer → 反应表示
    3. 反应表示 → 多分类头 → 条件预测

    性能目标：超越 MLP+xTB (81.2% Top-1, 95.6% Top-3)
    """

    def __init__(
        self,
        atom_feat_dim: int = 42,
        edge_feat_dim: int = 10,
        xtb_feat_dim: int = 11,
        gnn_hidden_dim: int = 128,
        gnn_num_layers: int = 3,
        gnn_num_heads: int = 4,
        num_anode: int = 15,
        num_cathode: int = 15,
        num_cell_type: int = 5,
        num_electrolyte: int = 101,
        num_solvent: int = 98,
        num_reagent: int = 201,
        num_catalyst: int = 101,
        dropout: float = 0.3,
    ):
        super().__init__()
        self.gnn_hidden_dim = gnn_hidden_dim

        # 分子GNN编码器
        self.mol_gnn = MolecularGNN(
            atom_feat_dim=atom_feat_dim,
            edge_feat_dim=edge_feat_dim,
            xtb_feat_dim=xtb_feat_dim,
            hidden_dim=gnn_hidden_dim,
            num_layers=gnn_num_layers,
            num_heads=gnn_num_heads,
            dropout=dropout,
        )

        # 反应变化建模
        self.reaction_transformer = ReactionTransformer(
            hidden_dim=gnn_hidden_dim,
            num_heads=gnn_num_heads,
            dropout=dropout,
        )

        # 融合层
        self.fusion = nn.Sequential(
            nn.Linear(gnn_hidden_dim, gnn_hidden_dim),
            nn.LayerNorm(gnn_hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
        )

        # 条件分类头
        self.anode_head = nn.Linear(gnn_hidden_dim, num_anode)
        self.cathode_head = nn.Linear(gnn_hidden_dim, num_cathode)
        self.cell_type_head = nn.Linear(gnn_hidden_dim, num_cell_type)
        self.electrolyte_head = nn.Linear(gnn_hidden_dim, num_electrolyte)
        self.solvent_head = nn.Linear(gnn_hidden_dim, num_solvent)
        self.reagent_head = nn.Linear(gnn_hidden_dim, num_reagent)
        self.catalyst_head = nn.Linear(gnn_hidden_dim, num_catalyst)

    def forward(
        self,
        reactant_graph: Dict[str, torch.Tensor],
        product_graph: Dict[str, torch.Tensor],
        reactant_xtb: Optional[torch.Tensor] = None,
        product_xtb: Optional[torch.Tensor] = None,
    ) -> Dict[str, torch.Tensor]:
        """
        前向传播

        Args:
            reactant_graph: 反应物图 {node_feats, edge_index, edge_feats, batch, num_graphs}
            product_graph: 产物图
            reactant_xtb: 反应物xTB特征 [B, 11]
            product_xtb: 产物xTB特征 [B, 11]

        Returns:
            Dict of logits for each condition
        """
        # 编码反应物和产物
        reactant_emb = self.mol_gnn(
            node_feats=reactant_graph['node_feats'],
            edge_index=reactant_graph['edge_index'],
            edge_feats=reactant_graph['edge_feats'],
            batch=reactant_graph['batch'],
            num_graphs=reactant_graph['num_graphs'],
            xtb_feats=reactant_xtb,
        )

        product_emb = self.mol_gnn(
            node_feats=product_graph['node_feats'],
            edge_index=product_graph['edge_index'],
            edge_feats=product_graph['edge_feats'],
            batch=product_graph['batch'],
            num_graphs=product_graph['num_graphs'],
            xtb_feats=product_xtb,
        )

        # 反应变化建模
        reaction_emb = self.reaction_transformer(reactant_emb, product_emb)

        # 融合
        h = self.fusion(reaction_emb)

        # 条件预测
        return {
            'anode': self.anode_head(h),
            'cathode': self.cathode_head(h),
            'cell_type': self.cell_type_head(h),
            'electrolyte': self.electrolyte_head(h),
            'solvent': self.solvent_head(h),
            'reagent': self.reagent_head(h),
            'catalyst': self.catalyst_head(h),
        }

    def recommend(
        self,
        reactant_graph: Dict[str, torch.Tensor],
        product_graph: Dict[str, torch.Tensor],
        reactant_xtb: Optional[torch.Tensor] = None,
        product_xtb: Optional[torch.Tensor] = None,
        top_k: int = 3
    ) -> Dict[str, Dict]:
        """推荐条件"""
        self.eval()
        with torch.no_grad():
            predictions = self.forward(reactant_graph, product_graph, reactant_xtb, product_xtb)

            recommendations = {}
            for key in predictions:
                logits = predictions[key]
                probs = F.softmax(logits, dim=-1)
                top_probs, top_indices = torch.topk(probs, min(top_k, probs.size(-1)))

                recommendations[key] = {
                    'indices': top_indices.cpu().tolist(),
                    'probabilities': top_probs.cpu().tolist()
                }

        return recommendations


if __name__ == "__main__":
    # 测试
    model = GNNConditionRecommender()
    num_params = sum(p.numel() for p in model.parameters())
    print(f"模型参数量: {num_params:,}")

    # 模拟输入
    batch_size = 4
    num_atoms = 20
    num_edges = 40

    reactant_graph = {
        'node_feats': torch.randn(num_atoms, 42),
        'edge_index': torch.randint(0, num_atoms, (2, num_edges)),
        'edge_feats': torch.randn(num_edges, 10),
        'batch': torch.repeat_interleave(torch.arange(batch_size), num_atoms // batch_size),
        'num_graphs': batch_size,
    }

    product_graph = {
        'node_feats': torch.randn(num_atoms, 42),
        'edge_index': torch.randint(0, num_atoms, (2, num_edges)),
        'edge_feats': torch.randn(num_edges, 10),
        'batch': torch.repeat_interleave(torch.arange(batch_size), num_atoms // batch_size),
        'num_graphs': batch_size,
    }

    reactant_xtb = torch.randn(batch_size, 11)
    product_xtb = torch.randn(batch_size, 11)

    outputs = model(reactant_graph, product_graph, reactant_xtb, product_xtb)
    for key, value in outputs.items():
        print(f"{key}: {value.shape}")
