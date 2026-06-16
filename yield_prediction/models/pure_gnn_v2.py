"""
纯GNN产率预测模型 V2：改进的电化学特征处理

改进点：
1. 电极材料使用可学习的 Embedding（20类）
2. 电解池类型使用 Embedding（5类）
3. 去掉无用的 current_density 和 potential
4. 溶剂/电解质使用独立的GNN编码器
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, Optional


class MessagePassingLayer(nn.Module):
    """消息传递层"""

    def __init__(self, node_dim: int, edge_dim: int, dropout: float = 0.1):
        super().__init__()
        self.message_mlp = nn.Sequential(
            nn.Linear(node_dim + edge_dim, node_dim),
            nn.ReLU(),
            nn.Linear(node_dim, node_dim),
        )
        self.update_mlp = nn.Sequential(
            nn.Linear(node_dim * 2, node_dim),
            nn.BatchNorm1d(node_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

    def forward(self, node_feats, edge_index, edge_feats):
        num_nodes = node_feats.shape[0]
        if edge_index.shape[1] == 0:
            return node_feats

        src, tgt = edge_index[0], edge_index[1]
        src_feats = node_feats[src]
        messages = self.message_mlp(torch.cat([src_feats, edge_feats], dim=-1))

        agg = torch.zeros(num_nodes, node_feats.shape[1], device=node_feats.device)
        agg = agg.scatter_add(0, tgt.unsqueeze(-1).expand_as(messages), messages)
        counts = torch.zeros(num_nodes, device=node_feats.device)
        counts = counts.scatter_add(0, tgt, torch.ones_like(tgt, dtype=torch.float))
        counts = counts.clamp(min=1).unsqueeze(-1)
        agg = agg / counts

        updated = self.update_mlp(torch.cat([node_feats, agg], dim=-1))
        return updated + node_feats


class MolecularGNN(nn.Module):
    """分子GNN编码器"""

    def __init__(
        self,
        atom_feat_dim: int = 42,
        edge_feat_dim: int = 10,
        hidden_dim: int = 128,
        num_layers: int = 3,
        dropout: float = 0.2,
    ):
        super().__init__()
        self.hidden_dim = hidden_dim

        self.node_embed = nn.Sequential(
            nn.Linear(atom_feat_dim, hidden_dim),
            nn.ReLU(),
        )
        self.edge_embed = nn.Linear(edge_feat_dim, hidden_dim // 2)

        self.mp_layers = nn.ModuleList([
            MessagePassingLayer(hidden_dim, hidden_dim // 2, dropout)
            for _ in range(num_layers)
        ])

        self.attention = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.Tanh(),
            nn.Linear(hidden_dim // 2, 1),
        )

        self.readout = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

    def forward(self, node_feats, edge_index, edge_feats, batch, num_graphs):
        h = self.node_embed(node_feats)
        e = self.edge_embed(edge_feats) if edge_feats.shape[0] > 0 else edge_feats

        for mp_layer in self.mp_layers:
            h = mp_layer(h, edge_index, e)

        mean_pool = self._scatter_mean(h, batch, num_graphs)
        attn_weights = self.attention(h)
        attn_weights = self._scatter_softmax(attn_weights, batch, num_graphs)
        attn_pool = self._scatter_sum(h * attn_weights, batch, num_graphs)

        graph_repr = torch.cat([mean_pool, attn_pool], dim=-1)
        return self.readout(graph_repr)

    def _scatter_mean(self, x, batch, num_graphs):
        out = torch.zeros(num_graphs, x.shape[-1], device=x.device)
        idx = batch.unsqueeze(-1).expand_as(x)
        out = out.scatter_add(0, idx, x)
        counts = torch.bincount(batch, minlength=num_graphs).float().unsqueeze(-1).to(x.device)
        return out / counts.clamp(min=1)

    def _scatter_sum(self, x, batch, num_graphs):
        out = torch.zeros(num_graphs, x.shape[-1], device=x.device)
        idx = batch.unsqueeze(-1).expand_as(x)
        return out.scatter_add(0, idx, x)

    def _scatter_softmax(self, x, batch, num_graphs):
        max_vals = torch.zeros(num_graphs, x.shape[-1], device=x.device)
        idx = batch.unsqueeze(-1).expand_as(x)
        max_vals = torch.scatter_reduce(max_vals, 0, idx, x, reduce='amax')
        x_shifted = x - max_vals[batch]
        exp_x = torch.exp(x_shifted)
        sum_exp = torch.zeros(num_graphs, x.shape[-1], device=x.device)
        sum_exp = sum_exp.scatter_add(0, idx, exp_x)
        return exp_x / sum_exp[batch].clamp(min=1e-8)


class PureGNNv2(nn.Module):
    """
    纯GNN产率预测器 V2

    特征：
    - 反应物/产物: GNN编码
    - 溶剂/电解质: 独立GNN编码
    - 电极材料: Embedding (20类 x 32维)
    - 电解池类型: Embedding (5类 x 16维)
    - 电流: 标准化数值
    """

    def __init__(
        self,
        atom_feat_dim: int = 42,
        edge_feat_dim: int = 10,
        gnn_hidden_dim: int = 128,
        gnn_num_layers: int = 3,
        num_electrode_types: int = 20,
        num_cell_types: int = 5,
        electrode_embed_dim: int = 32,
        cell_embed_dim: int = 16,
        dropout: float = 0.2,
    ):
        super().__init__()
        self.gnn_hidden_dim = gnn_hidden_dim

        # 反应物/产物 GNN
        self.reaction_gnn = MolecularGNN(
            atom_feat_dim=atom_feat_dim,
            edge_feat_dim=edge_feat_dim,
            hidden_dim=gnn_hidden_dim,
            num_layers=gnn_num_layers,
            dropout=dropout,
        )

        # 溶剂/电解质 GNN（独立，更轻量）
        self.condition_gnn = MolecularGNN(
            atom_feat_dim=atom_feat_dim,
            edge_feat_dim=edge_feat_dim,
            hidden_dim=gnn_hidden_dim // 2,
            num_layers=2,
            dropout=dropout,
        )

        # 电极 Embedding
        self.anode_embed = nn.Embedding(num_electrode_types, electrode_embed_dim)
        self.cathode_embed = nn.Embedding(num_electrode_types, electrode_embed_dim)

        # 电解池类型 Embedding
        self.cell_embed = nn.Embedding(num_cell_types, cell_embed_dim)

        # 电流编码
        self.current_encoder = nn.Sequential(
            nn.Linear(1, 16),
            nn.ReLU(),
            nn.Linear(16, 16),
        )

        # 反应编码器
        self.reaction_encoder = nn.Sequential(
            nn.Linear(gnn_hidden_dim * 3, gnn_hidden_dim),
            nn.BatchNorm1d(gnn_hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

        # 条件编码器（溶剂+电解质）
        condition_dim = gnn_hidden_dim // 2 * 2  # solvent + electrolyte
        self.condition_encoder = nn.Sequential(
            nn.Linear(condition_dim, gnn_hidden_dim // 2),
            nn.BatchNorm1d(gnn_hidden_dim // 2),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

        # 电化学参数编码器
        echem_dim = electrode_embed_dim * 2 + cell_embed_dim + 16  # anode + cathode + cell + current
        self.echem_encoder = nn.Sequential(
            nn.Linear(echem_dim, 64),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(64, 64),
            nn.ReLU(),
        )

        # 融合维度: reaction + condition + echem
        fusion_dim = gnn_hidden_dim + gnn_hidden_dim // 2 + 64

        # 预测头
        self.predictor = nn.Sequential(
            nn.Linear(fusion_dim, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(64, 1),
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
    ) -> torch.Tensor:
        """
        Args:
            reactant_graph, product_graph: 反应物/产物图
            solvent_graph, electrolyte_graph: 溶剂/电解质图
            anode_id: [B] 阳极类型ID
            cathode_id: [B] 阴极类型ID
            cell_type_id: [B] 电解池类型ID
            current: [B, 1] 标准化电流
        """
        # 反应编码
        reactant_emb = self._encode_reaction_graph(reactant_graph)
        product_emb = self._encode_reaction_graph(product_graph)
        diff_emb = product_emb - reactant_emb
        reaction_repr = torch.cat([reactant_emb, product_emb, diff_emb], dim=-1)
        reaction_emb = self.reaction_encoder(reaction_repr)

        # 条件编码（溶剂+电解质）
        solvent_emb = self._encode_condition_graph(solvent_graph)
        electrolyte_emb = self._encode_condition_graph(electrolyte_graph)
        condition_repr = torch.cat([solvent_emb, electrolyte_emb], dim=-1)
        condition_emb = self.condition_encoder(condition_repr)

        # 电化学参数编码
        anode_emb = self.anode_embed(anode_id)
        cathode_emb = self.cathode_embed(cathode_id)
        cell_emb = self.cell_embed(cell_type_id)
        current_emb = self.current_encoder(current)

        echem_repr = torch.cat([anode_emb, cathode_emb, cell_emb, current_emb], dim=-1)
        echem_emb = self.echem_encoder(echem_repr)

        # 融合预测
        combined = torch.cat([reaction_emb, condition_emb, echem_emb], dim=-1)
        return torch.sigmoid(self.predictor(combined))

    def _encode_reaction_graph(self, graph):
        return self.reaction_gnn(
            node_feats=graph['node_feats'],
            edge_index=graph['edge_index'],
            edge_feats=graph['edge_feats'],
            batch=graph['batch'],
            num_graphs=graph['num_graphs'],
        )

    def _encode_condition_graph(self, graph):
        return self.condition_gnn(
            node_feats=graph['node_feats'],
            edge_index=graph['edge_index'],
            edge_feats=graph['edge_feats'],
            batch=graph['batch'],
            num_graphs=graph['num_graphs'],
        )


if __name__ == "__main__":
    # 测试
    model = PureGNNv2()
    num_params = sum(p.numel() for p in model.parameters())
    print(f"模型参数量: {num_params:,}")
