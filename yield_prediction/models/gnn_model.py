"""
GNN产率预测模型：使用图神经网络学习分子表征 + xTB量化描述符

纯PyTorch实现，不依赖torch_geometric
"""
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, Optional


# ============================================================
# GIN Layer（Graph Isomorphism Network）
# ============================================================
class GINLayer(nn.Module):
    """
    GIN层：消息传递 + 节点更新

    h_v^{k+1} = MLP((1 + eps) * h_v^k + sum_{u in N(v)} h_u^k)
    带边特征调制版本
    """

    def __init__(self, hidden_dim: int, edge_dim: int, dropout: float = 0.1):
        super().__init__()
        self.eps = nn.Parameter(torch.zeros(1))

        # 边特征投影（用于调制消息）
        self.edge_proj = nn.Linear(edge_dim, hidden_dim)

        # 节点更新MLP
        self.mlp = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim * 2),
            nn.BatchNorm1d(hidden_dim * 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
        )

    def forward(
        self,
        node_feats: torch.Tensor,
        edge_index: torch.Tensor,
        edge_feats: torch.Tensor,
    ) -> torch.Tensor:
        """
        Args:
            node_feats: [N, hidden_dim]
            edge_index: [2, E]
            edge_feats: [E, edge_dim]

        Returns:
            更新后的 node_feats: [N, hidden_dim]
        """
        num_nodes = node_feats.shape[0]
        num_edges = edge_index.shape[1]

        if num_edges == 0:
            # 没有边时，只用自身特征更新
            return self.mlp((1 + self.eps) * node_feats)

        src, tgt = edge_index[0], edge_index[1]

        # 边特征调制的消息
        src_feats = node_feats[src]  # [E, hidden_dim]
        edge_weights = torch.sigmoid(self.edge_proj(edge_feats))  # [E, hidden_dim]
        messages = src_feats * edge_weights  # [E, hidden_dim]

        # 聚合消息 (scatter_add，非in-place)
        agg = torch.zeros(num_nodes, node_feats.shape[1],
                          device=node_feats.device, dtype=node_feats.dtype)
        agg = agg.scatter_add(0, tgt.unsqueeze(-1).expand_as(messages), messages)

        # 更新节点特征
        h = (1 + self.eps) * node_feats + agg
        return self.mlp(h)


# ============================================================
# 分子GNN编码器
# ============================================================
class MolecularGNN(nn.Module):
    """
    分子级GNN编码器

    SMILES → Graph → GIN layers → Global Pooling → 分子嵌入
    """

    def __init__(
        self,
        atom_feat_dim: int = 42,
        edge_feat_dim: int = 10,
        hidden_dim: int = 256,
        num_layers: int = 4,
        dropout: float = 0.2,
    ):
        super().__init__()
        self.hidden_dim = hidden_dim

        # 输入投影
        self.node_embed = nn.Linear(atom_feat_dim, hidden_dim)
        self.edge_embed = nn.Linear(edge_feat_dim, hidden_dim)

        # GIN层
        self.gin_layers = nn.ModuleList([
            GINLayer(hidden_dim, hidden_dim, dropout)
            for _ in range(num_layers)
        ])

        # 跳跃连接：每层输出都参与最终表征
        self.jump_proj = nn.Linear(hidden_dim * num_layers, hidden_dim)

        # 读出层：mean + max pooling → 投影
        self.readout = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
        )

    def forward(
        self,
        node_feats: torch.Tensor,
        edge_index: torch.Tensor,
        edge_feats: torch.Tensor,
        batch: torch.Tensor,
        num_graphs: int,
    ) -> torch.Tensor:
        """
        Args:
            node_feats: [total_nodes, atom_feat_dim]
            edge_index: [2, total_edges]
            edge_feats: [total_edges, edge_feat_dim]
            batch: [total_nodes] — 每个节点所属图的索引
            num_graphs: batch中图的数量

        Returns:
            graph_embeddings: [num_graphs, hidden_dim]
        """
        # 投影到隐藏维度
        h = self.node_embed(node_feats)  # [N, hidden_dim]
        e = self.edge_embed(edge_feats) if edge_feats.shape[0] > 0 else edge_feats

        # 多层GIN + 跳跃连接
        layer_outputs = []
        for gin in self.gin_layers:
            h = gin(h, edge_index, e)
            layer_outputs.append(h)

        # 跳跃连接：拼接所有层输出
        h_jump = torch.cat(layer_outputs, dim=-1)  # [N, hidden_dim * num_layers]
        h = self.jump_proj(h_jump)  # [N, hidden_dim]

        # 全局池化：mean + max
        mean_pool = self._global_pool(h, batch, num_graphs, mode='mean')
        max_pool = self._global_pool(h, batch, num_graphs, mode='max')
        graph_repr = torch.cat([mean_pool, max_pool], dim=-1)  # [B, hidden_dim * 2]

        return self.readout(graph_repr)  # [B, hidden_dim]

    def _global_pool(
        self,
        x: torch.Tensor,
        batch: torch.Tensor,
        num_graphs: int,
        mode: str = 'mean',
    ) -> torch.Tensor:
        """全局图池化"""
        idx = batch.unsqueeze(-1).expand_as(x)

        if mode == 'mean':
            out = torch.zeros(num_graphs, x.shape[-1], device=x.device, dtype=x.dtype)
            out = out.scatter_add(0, idx, x)
            counts = torch.bincount(batch, minlength=num_graphs).float().unsqueeze(-1).to(x.device)
            counts = counts.clamp(min=1)
            return out / counts
        elif mode == 'max':
            # 使用scatter_reduce（非in-place）+ where替换-inf
            out = torch.full((num_graphs, x.shape[-1]), float('-inf'),
                             device=x.device, dtype=x.dtype)
            out = torch.scatter_reduce(out, 0, idx, x, reduce='amax')
            out = torch.where(out == float('-inf'), torch.zeros_like(out), out)
            return out
        else:
            raise ValueError(f"Unknown pool mode: {mode}")


# ============================================================
# 完整的GNN产率预测模型
# ============================================================
class GNNYieldPredictor(nn.Module):
    """
    GNN产率预测器

    架构：
    - 共享的MolecularGNN编码器处理所有分子（反应物、产物、溶剂、电解质）
    - xTB量化描述符编码器
    - 电化学条件编码器
    - 融合MLP输出产率
    """

    def __init__(
        self,
        atom_feat_dim: int = 42,
        edge_feat_dim: int = 10,
        gnn_hidden_dim: int = 256,
        gnn_num_layers: int = 4,
        xtb_feat_dim: int = 55,
        echem_feat_dim: int = 6,
        dropout: float = 0.2,
    ):
        super().__init__()

        self.gnn_hidden_dim = gnn_hidden_dim

        # 共享的分子GNN编码器
        self.gnn = MolecularGNN(
            atom_feat_dim=atom_feat_dim,
            edge_feat_dim=edge_feat_dim,
            hidden_dim=gnn_hidden_dim,
            num_layers=gnn_num_layers,
            dropout=dropout,
        )

        # xTB描述符编码器
        self.xtb_encoder = nn.Sequential(
            nn.Linear(xtb_feat_dim, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(128, 64),
            nn.ReLU(),
        )

        # 电化学条件编码器
        self.echem_encoder = nn.Sequential(
            nn.Linear(echem_feat_dim, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(64, 32),
            nn.ReLU(),
        )

        # 融合层
        # 输入: reactant(256) + product(256) + diff(256) + solvent(256) + electrolyte(256) + xtb(64) + echem(32)
        fusion_input_dim = gnn_hidden_dim * 5 + 64 + 32  # 1376
        self.fusion = nn.Sequential(
            nn.Linear(fusion_input_dim, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(128, 1),
        )

    def forward(
        self,
        reactant_graph: Dict[str, torch.Tensor],
        product_graph: Dict[str, torch.Tensor],
        solvent_graph: Dict[str, torch.Tensor],
        electrolyte_graph: Dict[str, torch.Tensor],
        xtb_features: torch.Tensor,
        echem_features: torch.Tensor,
    ) -> torch.Tensor:
        """
        Args:
            reactant_graph: batched graph dict with node_feats, edge_index, edge_feats, batch, num_graphs
            product_graph: same format
            solvent_graph: same format
            electrolyte_graph: same format
            xtb_features: [B, 55]
            echem_features: [B, 6]

        Returns:
            yield_pred: [B, 1] in range (0, 1)
        """
        # GNN编码各组分子
        reactant_emb = self._encode_graph(reactant_graph)    # [B, hidden_dim]
        product_emb = self._encode_graph(product_graph)      # [B, hidden_dim]
        diff_emb = product_emb - reactant_emb                # [B, hidden_dim]
        solvent_emb = self._encode_graph(solvent_graph)      # [B, hidden_dim]
        electrolyte_emb = self._encode_graph(electrolyte_graph)  # [B, hidden_dim]

        # 编码xTB和电化学条件
        xtb_emb = self.xtb_encoder(xtb_features)     # [B, 64]
        echem_emb = self.echem_encoder(echem_features)  # [B, 32]

        # 融合
        combined = torch.cat([
            reactant_emb,
            product_emb,
            diff_emb,
            solvent_emb,
            electrolyte_emb,
            xtb_emb,
            echem_emb,
        ], dim=-1)  # [B, 1376]

        return torch.sigmoid(self.fusion(combined))  # [B, 1]

    def _encode_graph(self, graph: Dict[str, torch.Tensor]) -> torch.Tensor:
        """用GNN编码一个batched graph"""
        return self.gnn(
            node_feats=graph['node_feats'],
            edge_index=graph['edge_index'],
            edge_feats=graph['edge_feats'],
            batch=graph['batch'],
            num_graphs=graph['num_graphs'],
        )


# ============================================================
# GNNv2：轻量版产率预测器（减少过拟合）
# ============================================================
class GNNv2YieldPredictor(nn.Module):
    """
    轻量GNN产率预测器

    相比GNNYieldPredictor的改进：
    - hidden_dim 256→128, layers 4→2（减少参数 5.7 倍）
    - dropout 0.2→0.3（增强正则化）
    - 简化 fusion MLP（2层而非3层）
    总参数: ~456K
    """

    def __init__(
        self,
        atom_feat_dim: int = 42,
        edge_feat_dim: int = 10,
        gnn_hidden_dim: int = 128,
        gnn_num_layers: int = 2,
        xtb_feat_dim: int = 55,
        echem_feat_dim: int = 6,
        dropout: float = 0.3,
    ):
        super().__init__()
        self.gnn_hidden_dim = gnn_hidden_dim

        self.gnn = MolecularGNN(
            atom_feat_dim=atom_feat_dim,
            edge_feat_dim=edge_feat_dim,
            hidden_dim=gnn_hidden_dim,
            num_layers=gnn_num_layers,
            dropout=dropout,
        )

        self.xtb_encoder = nn.Sequential(
            nn.Linear(xtb_feat_dim, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(64, 32),
            nn.ReLU(),
        )

        self.echem_encoder = nn.Sequential(
            nn.Linear(echem_feat_dim, 32),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(32, 16),
            nn.ReLU(),
        )

        # react(128)+prod(128)+diff(128)+solv(128)+elec(128)+xtb(32)+echem(16) = 688
        fusion_dim = gnn_hidden_dim * 5 + 32 + 16
        self.fusion = nn.Sequential(
            nn.Linear(fusion_dim, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(128, 1),
        )

    def forward(self, reactant_graph, product_graph, solvent_graph, electrolyte_graph,
                xtb_features, echem_features):
        reactant_emb = self._encode_graph(reactant_graph)
        product_emb = self._encode_graph(product_graph)
        diff_emb = product_emb - reactant_emb
        solvent_emb = self._encode_graph(solvent_graph)
        electrolyte_emb = self._encode_graph(electrolyte_graph)

        xtb_emb = self.xtb_encoder(xtb_features)
        echem_emb = self.echem_encoder(echem_features)

        combined = torch.cat([
            reactant_emb, product_emb, diff_emb,
            solvent_emb, electrolyte_emb,
            xtb_emb, echem_emb,
        ], dim=-1)

        return torch.sigmoid(self.fusion(combined))

    def _encode_graph(self, graph):
        return self.gnn(
            node_feats=graph['node_feats'],
            edge_index=graph['edge_index'],
            edge_feats=graph['edge_feats'],
            batch=graph['batch'],
            num_graphs=graph['num_graphs'],
        )


# ============================================================
# GNNv2 Hybrid：GNN + Morgan指纹混合模型
# ============================================================
class GNNv2HybridYieldPredictor(nn.Module):
    """
    GNN + 指纹混合产率预测器

    GNN分支学习图级特征，指纹分支提供已验证的子结构信息。
    总参数: ~2.1M（指纹编码层 ~1.6M 占大头）
    """

    def __init__(
        self,
        atom_feat_dim: int = 42,
        edge_feat_dim: int = 10,
        gnn_hidden_dim: int = 128,
        gnn_num_layers: int = 2,
        fp_dim: int = 6144,
        xtb_feat_dim: int = 55,
        echem_feat_dim: int = 6,
        dropout: float = 0.3,
    ):
        super().__init__()
        self.gnn_hidden_dim = gnn_hidden_dim

        self.gnn = MolecularGNN(
            atom_feat_dim=atom_feat_dim,
            edge_feat_dim=edge_feat_dim,
            hidden_dim=gnn_hidden_dim,
            num_layers=gnn_num_layers,
            dropout=dropout,
        )

        # 指纹编码器
        self.fp_encoder = nn.Sequential(
            nn.Linear(fp_dim, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
        )

        self.xtb_encoder = nn.Sequential(
            nn.Linear(xtb_feat_dim, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(64, 32),
            nn.ReLU(),
        )

        self.echem_encoder = nn.Sequential(
            nn.Linear(echem_feat_dim, 32),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(32, 16),
            nn.ReLU(),
        )

        # gnn(128*5) + fp(128) + xtb(32) + echem(16) = 816
        fusion_dim = gnn_hidden_dim * 5 + 128 + 32 + 16
        self.fusion = nn.Sequential(
            nn.Linear(fusion_dim, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(128, 1),
        )

    def forward(self, reactant_graph, product_graph, solvent_graph, electrolyte_graph,
                xtb_features, echem_features, reaction_fp):
        reactant_emb = self._encode_graph(reactant_graph)
        product_emb = self._encode_graph(product_graph)
        diff_emb = product_emb - reactant_emb
        solvent_emb = self._encode_graph(solvent_graph)
        electrolyte_emb = self._encode_graph(electrolyte_graph)

        fp_emb = self.fp_encoder(reaction_fp)
        xtb_emb = self.xtb_encoder(xtb_features)
        echem_emb = self.echem_encoder(echem_features)

        combined = torch.cat([
            reactant_emb, product_emb, diff_emb,
            solvent_emb, electrolyte_emb,
            fp_emb, xtb_emb, echem_emb,
        ], dim=-1)

        return torch.sigmoid(self.fusion(combined))

    def _encode_graph(self, graph):
        return self.gnn(
            node_feats=graph['node_feats'],
            edge_index=graph['edge_index'],
            edge_feats=graph['edge_feats'],
            batch=graph['batch'],
            num_graphs=graph['num_graphs'],
        )


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent.parent))
    from utils.graph_features import smiles_to_graph, batch_graphs, ATOM_FEAT_DIM, BOND_FEAT_DIM

    # 测试模型
    print(f"原子特征维度: {ATOM_FEAT_DIM}")
    print(f"键特征维度: {BOND_FEAT_DIM}")

    model = GNNYieldPredictor(
        atom_feat_dim=ATOM_FEAT_DIM,
        edge_feat_dim=BOND_FEAT_DIM,
    )
    num_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"模型参数量: {num_params:,}")

    # 构造测试数据
    batch_size = 4
    test_smiles = ["CCO", "c1ccccc1", "CC(=O)O", "CC#N"]

    def make_batched_graph(smiles_list):
        graphs = []
        for smi in smiles_list:
            g = smiles_to_graph(smi)
            if g is None:
                from utils.graph_features import get_dummy_graph
                g = get_dummy_graph()
            graphs.append(g)
        return batch_graphs(graphs)

    reactant_g = make_batched_graph(test_smiles)
    product_g = make_batched_graph(test_smiles)
    solvent_g = make_batched_graph(test_smiles)
    electrolyte_g = make_batched_graph(test_smiles)
    xtb_feat = torch.randn(batch_size, 55)
    echem_feat = torch.randn(batch_size, 6)

    # 前向传播
    output = model(reactant_g, product_g, solvent_g, electrolyte_g, xtb_feat, echem_feat)
    print(f"输出形状: {output.shape}")
    print(f"输出值: {output.flatten().tolist()}")
