"""
Hybrid GNN 产率预测模型：结合GNN局部结构学习 + xTB全局量子化学特征

核心思路：
1. GNN编码器学习分子局部结构（原子连接、官能团等）
2. xTB特征提供全局量子化学信息（HOMO/LUMO/能隙/偶极矩/溶剂化能等）
3. 电极/电解池使用可学习Embedding
4. 多尺度特征融合

目标：超越MLP基线（MAE 12.36）
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, Optional, Tuple


class EdgeGatedMessagePassing(nn.Module):
    """
    边门控消息传递层 (Edge-Gated MPNN)

    相比简单的消息传递：
    1. 边特征作为门控信号，控制信息流动
    2. 多头注意力聚合消息
    3. 残差连接 + LayerNorm
    """

    def __init__(self, node_dim: int, edge_dim: int, num_heads: int = 4, dropout: float = 0.1):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = node_dim // num_heads
        assert node_dim % num_heads == 0, f"node_dim must be divisible by num_heads"

        # 边门控
        self.edge_gate = nn.Sequential(
            nn.Linear(edge_dim, node_dim),
            nn.Sigmoid(),
        )

        # 消息变换 (多头)
        self.query = nn.Linear(node_dim, node_dim)
        self.key = nn.Linear(node_dim, node_dim)
        self.value = nn.Linear(node_dim, node_dim)

        # 输出投影
        self.out_proj = nn.Linear(node_dim, node_dim)

        # 正则化
        self.layer_norm = nn.LayerNorm(node_dim)
        self.dropout = nn.Dropout(dropout)

        # FFN
        self.ffn = nn.Sequential(
            nn.Linear(node_dim, node_dim * 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(node_dim * 2, node_dim),
            nn.Dropout(dropout),
        )
        self.ffn_norm = nn.LayerNorm(node_dim)

    def forward(self, node_feats, edge_index, edge_feats):
        """
        Args:
            node_feats: [N, node_dim]
            edge_index: [2, E]
            edge_feats: [E, edge_dim]
        """
        num_nodes = node_feats.shape[0]

        if edge_index.shape[1] == 0:
            return node_feats

        src, tgt = edge_index[0], edge_index[1]

        # 计算 Q, K, V
        Q = self.query(node_feats)  # [N, D]
        K = self.key(node_feats)    # [N, D]
        V = self.value(node_feats)  # [N, D]

        # 边门控
        edge_gate = self.edge_gate(edge_feats)  # [E, D]

        # 消息计算
        Q_src = Q[src]  # [E, D]
        K_tgt = K[tgt]  # [E, D]
        V_src = V[src]  # [E, D]

        # 多头注意力分数
        Q_src = Q_src.view(-1, self.num_heads, self.head_dim)  # [E, H, D/H]
        K_tgt = K_tgt.view(-1, self.num_heads, self.head_dim)  # [E, H, D/H]
        V_src = V_src.view(-1, self.num_heads, self.head_dim)  # [E, H, D/H]

        attn_scores = (Q_src * K_tgt).sum(dim=-1) / (self.head_dim ** 0.5)  # [E, H]

        # 边门控调制
        edge_gate = edge_gate.view(-1, self.num_heads, self.head_dim)
        V_gated = V_src * edge_gate  # [E, H, D/H]

        # Softmax 在每个目标节点的入边上
        attn_scores = attn_scores.unsqueeze(-1)  # [E, H, 1]

        # 计算注意力权重（scatter softmax）
        attn_max = torch.zeros(num_nodes, self.num_heads, 1, device=node_feats.device)
        attn_max.scatter_reduce_(0, tgt.view(-1, 1, 1).expand(-1, self.num_heads, 1),
                                  attn_scores, reduce='amax')
        attn_scores = attn_scores - attn_max[tgt]
        attn_weights = torch.exp(attn_scores)

        attn_sum = torch.zeros(num_nodes, self.num_heads, 1, device=node_feats.device)
        attn_sum.scatter_add_(0, tgt.view(-1, 1, 1).expand(-1, self.num_heads, 1), attn_weights)
        attn_weights = attn_weights / attn_sum[tgt].clamp(min=1e-8)

        # 加权消息聚合
        messages = V_gated * attn_weights  # [E, H, D/H]
        messages = messages.view(-1, node_feats.shape[-1])  # [E, D]

        agg = torch.zeros_like(node_feats)
        agg.scatter_add_(0, tgt.unsqueeze(-1).expand_as(messages), messages)

        # 输出投影 + 残差
        out = self.out_proj(agg)
        out = self.dropout(out)
        out = self.layer_norm(node_feats + out)

        # FFN
        out = out + self.ffn(out)
        out = self.ffn_norm(out)

        return out


class XTBFeatureEncoder(nn.Module):
    """
    xTB量子化学特征编码器

    输入: 11维特征 (6 xTB + 5 RDKit)
    - total_energy, homo_lumo_gap, homo, lumo, dipole, gsolv
    - num_heavy_atoms, MW, rotatable_bonds, TPSA, LogP
    """

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


class HybridMolecularGNN(nn.Module):
    """
    混合分子GNN编码器

    结合：
    1. 局部：GNN消息传递学习原子级结构
    2. 全局：xTB量子化学描述符
    """

    def __init__(
        self,
        atom_feat_dim: int = 42,
        edge_feat_dim: int = 10,
        xtb_feat_dim: int = 11,
        hidden_dim: int = 128,
        num_layers: int = 4,
        num_heads: int = 4,
        dropout: float = 0.2,
    ):
        super().__init__()
        self.hidden_dim = hidden_dim

        # 原子特征投影
        self.node_embed = nn.Sequential(
            nn.Linear(atom_feat_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.GELU(),
        )

        # 边特征投影
        self.edge_embed = nn.Sequential(
            nn.Linear(edge_feat_dim, hidden_dim // 2),
            nn.GELU(),
        )

        # 消息传递层
        self.mp_layers = nn.ModuleList([
            EdgeGatedMessagePassing(hidden_dim, hidden_dim // 2, num_heads, dropout)
            for _ in range(num_layers)
        ])

        # xTB特征编码器
        self.xtb_encoder = XTBFeatureEncoder(xtb_feat_dim, hidden_dim, hidden_dim // 2, dropout)

        # 多尺度池化
        self.attention_pool = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.Tanh(),
            nn.Linear(hidden_dim // 2, 1),
        )

        # 最终融合: GNN (mean + attn) + xTB
        self.fusion = nn.Sequential(
            nn.Linear(hidden_dim * 2 + hidden_dim // 2, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
        )

    def forward(self, node_feats, edge_index, edge_feats, batch, num_graphs, xtb_feats=None):
        """
        Args:
            node_feats: [total_nodes, atom_feat_dim]
            edge_index: [2, total_edges]
            edge_feats: [total_edges, edge_feat_dim]
            batch: [total_nodes] 每个节点属于哪个图
            num_graphs: batch中图的数量
            xtb_feats: [num_graphs, 11] xTB特征 (可选)
        """
        # 节点嵌入
        h = self.node_embed(node_feats)

        # 边嵌入
        if edge_feats.shape[0] > 0:
            e = self.edge_embed(edge_feats)
        else:
            e = torch.zeros(0, self.hidden_dim // 2, device=node_feats.device)

        # 消息传递
        for mp_layer in self.mp_layers:
            h = mp_layer(h, edge_index, e)

        # 图级池化
        # 1. Mean pooling
        mean_pool = self._scatter_mean(h, batch, num_graphs)

        # 2. Attention pooling
        attn_weights = self.attention_pool(h)
        attn_weights = self._scatter_softmax(attn_weights, batch, num_graphs)
        attn_pool = self._scatter_sum(h * attn_weights, batch, num_graphs)

        # 3. xTB特征
        if xtb_feats is not None:
            xtb_emb = self.xtb_encoder(xtb_feats)
            graph_repr = torch.cat([mean_pool, attn_pool, xtb_emb], dim=-1)
        else:
            # 无xTB时使用零填充
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
    """
    反应变化Transformer

    对反应物和产物的GNN表示进行交叉注意力，
    学习化学转化的模式。
    """

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
        """
        Args:
            reactant_emb: [B, D]
            product_emb: [B, D]
        Returns:
            reaction_emb: [B, D]
        """
        # 扩展为序列格式 [B, 1, D]
        r = reactant_emb.unsqueeze(1)
        p = product_emb.unsqueeze(1)

        # 反应物关注产物
        r_attended, _ = self.cross_attn_r2p(r, p, p)
        r_attended = self.norm1(r + r_attended)

        # 产物关注反应物
        p_attended, _ = self.cross_attn_p2r(p, r, r)
        p_attended = self.norm2(p + p_attended)

        # 融合
        combined = torch.cat([r_attended.squeeze(1), p_attended.squeeze(1)], dim=-1)
        return self.ffn(combined)


class HybridGNNYieldPredictor(nn.Module):
    """
    混合GNN产率预测器 - 目标：超越MLP基线

    特征融合：
    1. 反应物/产物: HybridMolecularGNN (GNN + xTB)
    2. 溶剂/电解质: 轻量GNN + xTB
    3. 电极: 可学习Embedding
    4. 电解池类型: 可学习Embedding
    5. 反应变化: ReactionTransformer
    """

    def __init__(
        self,
        atom_feat_dim: int = 42,
        edge_feat_dim: int = 10,
        xtb_feat_dim: int = 11,
        gnn_hidden_dim: int = 128,
        gnn_num_layers: int = 4,
        gnn_num_heads: int = 4,
        num_electrode_types: int = 20,
        num_cell_types: int = 6,
        electrode_embed_dim: int = 32,
        cell_embed_dim: int = 16,
        dropout: float = 0.2,
    ):
        super().__init__()
        self.gnn_hidden_dim = gnn_hidden_dim

        # 反应物/产物 GNN (完整版)
        self.reaction_gnn = HybridMolecularGNN(
            atom_feat_dim=atom_feat_dim,
            edge_feat_dim=edge_feat_dim,
            xtb_feat_dim=xtb_feat_dim,
            hidden_dim=gnn_hidden_dim,
            num_layers=gnn_num_layers,
            num_heads=gnn_num_heads,
            dropout=dropout,
        )

        # 溶剂/电解质 GNN (轻量版)
        self.condition_gnn = HybridMolecularGNN(
            atom_feat_dim=atom_feat_dim,
            edge_feat_dim=edge_feat_dim,
            xtb_feat_dim=xtb_feat_dim,
            hidden_dim=gnn_hidden_dim // 2,
            num_layers=2,
            num_heads=2,
            dropout=dropout,
        )

        # 反应变化Transformer
        self.reaction_transformer = ReactionTransformer(
            hidden_dim=gnn_hidden_dim,
            num_heads=gnn_num_heads,
            dropout=dropout,
        )

        # 电极 Embedding
        self.anode_embed = nn.Embedding(num_electrode_types, electrode_embed_dim)
        self.cathode_embed = nn.Embedding(num_electrode_types, electrode_embed_dim)

        # 电解池类型 Embedding
        self.cell_embed = nn.Embedding(num_cell_types, cell_embed_dim)

        # 电流编码
        self.current_encoder = nn.Sequential(
            nn.Linear(1, 32),
            nn.GELU(),
            nn.Linear(32, 32),
        )

        # 条件融合
        condition_dim = gnn_hidden_dim // 2 * 2  # solvent + electrolyte
        self.condition_fusion = nn.Sequential(
            nn.Linear(condition_dim, gnn_hidden_dim // 2),
            nn.LayerNorm(gnn_hidden_dim // 2),
            nn.GELU(),
            nn.Dropout(dropout),
        )

        # 电化学参数融合
        echem_dim = electrode_embed_dim * 2 + cell_embed_dim + 32
        self.echem_fusion = nn.Sequential(
            nn.Linear(echem_dim, 64),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(64, 64),
        )

        # 最终预测头
        # reaction (gnn_hidden) + condition (gnn_hidden/2) + echem (64)
        fusion_dim = gnn_hidden_dim + gnn_hidden_dim // 2 + 64

        self.predictor = nn.Sequential(
            nn.Linear(fusion_dim, 256),
            nn.LayerNorm(256),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(256, 128),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(128, 1),
        )

    def forward(
        self,
        reactant_graph: Dict[str, torch.Tensor],
        product_graph: Dict[str, torch.Tensor],
        solvent_graph: Dict[str, torch.Tensor],
        electrolyte_graph: Dict[str, torch.Tensor],
        anode_id: torch.Tensor,
        cathode_id: torch.Tensor,
        cell_type_id: torch.Tensor,
        current: torch.Tensor,
        reactant_xtb: Optional[torch.Tensor] = None,
        product_xtb: Optional[torch.Tensor] = None,
        solvent_xtb: Optional[torch.Tensor] = None,
        electrolyte_xtb: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """
        前向传播

        Args:
            *_graph: 图数据字典 {node_feats, edge_index, edge_feats, batch, num_graphs}
            *_id: 分类特征ID
            current: [B, 1] 标准化电流
            *_xtb: [B, 11] xTB特征
        """
        # 1. 反应物/产物编码
        reactant_emb = self._encode_reaction_graph(reactant_graph, reactant_xtb)
        product_emb = self._encode_reaction_graph(product_graph, product_xtb)

        # 2. 反应变化建模
        reaction_emb = self.reaction_transformer(reactant_emb, product_emb)

        # 3. 条件编码
        solvent_emb = self._encode_condition_graph(solvent_graph, solvent_xtb)
        electrolyte_emb = self._encode_condition_graph(electrolyte_graph, electrolyte_xtb)
        condition_repr = torch.cat([solvent_emb, electrolyte_emb], dim=-1)
        condition_emb = self.condition_fusion(condition_repr)

        # 4. 电化学参数编码
        anode_emb = self.anode_embed(anode_id)
        cathode_emb = self.cathode_embed(cathode_id)
        cell_emb = self.cell_embed(cell_type_id)
        current_emb = self.current_encoder(current)

        echem_repr = torch.cat([anode_emb, cathode_emb, cell_emb, current_emb], dim=-1)
        echem_emb = self.echem_fusion(echem_repr)

        # 5. 最终融合和预测
        combined = torch.cat([reaction_emb, condition_emb, echem_emb], dim=-1)
        return torch.sigmoid(self.predictor(combined))

    def _encode_reaction_graph(self, graph, xtb_feats=None):
        return self.reaction_gnn(
            node_feats=graph['node_feats'],
            edge_index=graph['edge_index'],
            edge_feats=graph['edge_feats'],
            batch=graph['batch'],
            num_graphs=graph['num_graphs'],
            xtb_feats=xtb_feats,
        )

    def _encode_condition_graph(self, graph, xtb_feats=None):
        return self.condition_gnn(
            node_feats=graph['node_feats'],
            edge_index=graph['edge_index'],
            edge_feats=graph['edge_feats'],
            batch=graph['batch'],
            num_graphs=graph['num_graphs'],
            xtb_feats=xtb_feats,
        )


if __name__ == "__main__":
    # 测试
    model = HybridGNNYieldPredictor()
    num_params = sum(p.numel() for p in model.parameters())
    print(f"模型参数量: {num_params:,}")

    # 预期参数量比 PureGNN v2 多，但性能应该更好
