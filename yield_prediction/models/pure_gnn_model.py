"""
纯GNN产率预测模型：只使用分子图学习特征，不依赖预计算指纹或xTB

设计理念：
1. GNN直接从分子图（原子+键）学习表征
2. 不使用Morgan指纹、xTB等预计算特征
3. 只保留必要的电化学条件参数（电极类型、电流等，这些信息不在分子结构中）
4. 轻量级设计，避免小数据集过拟合
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, Optional


class MessagePassingLayer(nn.Module):
    """消息传递层：带边特征的图卷积"""

    def __init__(self, node_dim: int, edge_dim: int, dropout: float = 0.1):
        super().__init__()
        # 消息函数：节点特征 + 边特征 -> 消息
        self.message_mlp = nn.Sequential(
            nn.Linear(node_dim + edge_dim, node_dim),
            nn.ReLU(),
            nn.Linear(node_dim, node_dim),
        )
        # 更新函数：聚合消息 + 自身 -> 新特征
        self.update_mlp = nn.Sequential(
            nn.Linear(node_dim * 2, node_dim),
            nn.BatchNorm1d(node_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

    def forward(self, node_feats, edge_index, edge_feats):
        """
        Args:
            node_feats: [N, node_dim]
            edge_index: [2, E]
            edge_feats: [E, edge_dim]
        Returns:
            updated_node_feats: [N, node_dim]
        """
        num_nodes = node_feats.shape[0]

        if edge_index.shape[1] == 0:
            # 无边情况，返回原特征
            return node_feats

        src, tgt = edge_index[0], edge_index[1]

        # 计算消息
        src_feats = node_feats[src]  # [E, node_dim]
        messages = self.message_mlp(torch.cat([src_feats, edge_feats], dim=-1))  # [E, node_dim]

        # 聚合消息（mean aggregation）
        agg = torch.zeros(num_nodes, node_feats.shape[1], device=node_feats.device)
        agg = agg.scatter_add(0, tgt.unsqueeze(-1).expand_as(messages), messages)
        counts = torch.zeros(num_nodes, device=node_feats.device)
        counts = counts.scatter_add(0, tgt, torch.ones_like(tgt, dtype=torch.float))
        counts = counts.clamp(min=1).unsqueeze(-1)
        agg = agg / counts

        # 更新节点
        updated = self.update_mlp(torch.cat([node_feats, agg], dim=-1))
        return updated + node_feats  # 残差连接


class PureMolecularGNN(nn.Module):
    """
    纯分子GNN编码器

    只从分子图学习表征，不使用任何预计算特征
    """

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

        # 原子特征投影
        self.node_embed = nn.Sequential(
            nn.Linear(atom_feat_dim, hidden_dim),
            nn.ReLU(),
        )

        # 边特征投影
        self.edge_embed = nn.Linear(edge_feat_dim, hidden_dim // 2)

        # 消息传递层
        self.mp_layers = nn.ModuleList([
            MessagePassingLayer(hidden_dim, hidden_dim // 2, dropout)
            for _ in range(num_layers)
        ])

        # 图级读出（Set2Set风格的注意力池化）
        self.attention = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.Tanh(),
            nn.Linear(hidden_dim // 2, 1),
        )

        # 最终投影
        self.readout = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),  # mean + attention-weighted
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

    def forward(self, node_feats, edge_index, edge_feats, batch, num_graphs):
        """
        Args:
            node_feats: [total_nodes, atom_feat_dim]
            edge_index: [2, total_edges]
            edge_feats: [total_edges, edge_feat_dim]
            batch: [total_nodes] 每个节点属于哪个图
            num_graphs: batch中图的数量
        Returns:
            graph_embeddings: [num_graphs, hidden_dim]
        """
        # 嵌入
        h = self.node_embed(node_feats)
        e = self.edge_embed(edge_feats) if edge_feats.shape[0] > 0 else edge_feats

        # 消息传递
        for mp_layer in self.mp_layers:
            h = mp_layer(h, edge_index, e)

        # 图级池化
        # 1. Mean pooling
        mean_pool = self._scatter_mean(h, batch, num_graphs)

        # 2. Attention pooling
        attn_weights = self.attention(h)  # [N, 1]
        attn_weights = self._scatter_softmax(attn_weights, batch, num_graphs)
        attn_pool = self._scatter_sum(h * attn_weights, batch, num_graphs)

        # 合并
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
        # 计算每个图内的softmax
        max_vals = torch.zeros(num_graphs, x.shape[-1], device=x.device)
        idx = batch.unsqueeze(-1).expand_as(x)
        max_vals = torch.scatter_reduce(max_vals, 0, idx, x, reduce='amax')
        x_shifted = x - max_vals[batch]
        exp_x = torch.exp(x_shifted)
        sum_exp = torch.zeros(num_graphs, x.shape[-1], device=x.device)
        sum_exp = sum_exp.scatter_add(0, idx, exp_x)
        return exp_x / sum_exp[batch].clamp(min=1e-8)


class PureGNNYieldPredictor(nn.Module):
    """
    纯GNN产率预测器

    使用：
    1. 反应物分子图 -> GNN编码
    2. 产物分子图 -> GNN编码
    3. 溶剂分子图 -> GNN编码
    4. 电解质分子图 -> GNN编码
    5. 电化学条件（电极、电流等）-> 简单编码

    不使用：
    - Morgan指纹
    - xTB量子化学描述符
    """

    def __init__(
        self,
        atom_feat_dim: int = 42,
        edge_feat_dim: int = 10,
        gnn_hidden_dim: int = 128,
        gnn_num_layers: int = 3,
        echem_feat_dim: int = 6,
        dropout: float = 0.2,
        use_solvent: bool = True,
        use_electrolyte: bool = True,
        separate_encoder: bool = False,  # 是否为溶剂/电解质使用独立编码器
    ):
        super().__init__()
        self.use_solvent = use_solvent
        self.use_electrolyte = use_electrolyte
        self.separate_encoder = separate_encoder
        self.gnn_hidden_dim = gnn_hidden_dim

        # 反应物/产物GNN编码器
        self.reaction_gnn = PureMolecularGNN(
            atom_feat_dim=atom_feat_dim,
            edge_feat_dim=edge_feat_dim,
            hidden_dim=gnn_hidden_dim,
            num_layers=gnn_num_layers,
            dropout=dropout,
        )

        # 溶剂/电解质GNN编码器（独立或共享）
        if separate_encoder and (use_solvent or use_electrolyte):
            # 独立的轻量级编码器（层数更少）
            self.condition_gnn = PureMolecularGNN(
                atom_feat_dim=atom_feat_dim,
                edge_feat_dim=edge_feat_dim,
                hidden_dim=gnn_hidden_dim // 2,  # 更小的隐藏维度
                num_layers=2,  # 更少的层数
                dropout=dropout,
            )
            condition_emb_dim = gnn_hidden_dim // 2
        else:
            self.condition_gnn = self.reaction_gnn  # 共享编码器
            condition_emb_dim = gnn_hidden_dim

        # 电化学条件编码
        self.echem_encoder = nn.Sequential(
            nn.Linear(echem_feat_dim, 32),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(32, 32),
            nn.ReLU(),
        )

        # 反应变化编码
        self.reaction_encoder = nn.Sequential(
            nn.Linear(gnn_hidden_dim * 3, gnn_hidden_dim),
            nn.BatchNorm1d(gnn_hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

        # 融合维度
        fusion_dim = gnn_hidden_dim + 32  # reaction + echem
        if use_solvent:
            fusion_dim += condition_emb_dim
        if use_electrolyte:
            fusion_dim += condition_emb_dim

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
        echem_features: torch.Tensor,
        solvent_graph: Optional[Dict[str, torch.Tensor]] = None,
        electrolyte_graph: Optional[Dict[str, torch.Tensor]] = None,
    ) -> torch.Tensor:
        # 反应物/产物用reaction_gnn编码
        reactant_emb = self._encode_reaction_graph(reactant_graph)
        product_emb = self._encode_reaction_graph(product_graph)

        # 反应变化
        diff_emb = product_emb - reactant_emb
        reaction_repr = torch.cat([reactant_emb, product_emb, diff_emb], dim=-1)
        reaction_emb = self.reaction_encoder(reaction_repr)

        # 电化学条件
        echem_emb = self.echem_encoder(echem_features)

        # 融合特征
        features = [reaction_emb, echem_emb]

        # 溶剂/电解质用condition_gnn编码
        if self.use_solvent and solvent_graph is not None:
            solvent_emb = self._encode_condition_graph(solvent_graph)
            features.append(solvent_emb)

        if self.use_electrolyte and electrolyte_graph is not None:
            electrolyte_emb = self._encode_condition_graph(electrolyte_graph)
            features.append(electrolyte_emb)

        combined = torch.cat(features, dim=-1)
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


class PureGNNWithAttention(nn.Module):
    """
    带反应物-产物注意力的纯GNN

    使用交叉注意力学习反应物和产物之间的关系
    """

    def __init__(
        self,
        atom_feat_dim: int = 42,
        edge_feat_dim: int = 10,
        gnn_hidden_dim: int = 128,
        gnn_num_layers: int = 3,
        echem_feat_dim: int = 6,
        num_attention_heads: int = 4,
        dropout: float = 0.2,
    ):
        super().__init__()
        self.gnn_hidden_dim = gnn_hidden_dim

        # 分子GNN
        self.gnn = PureMolecularGNN(
            atom_feat_dim=atom_feat_dim,
            edge_feat_dim=edge_feat_dim,
            hidden_dim=gnn_hidden_dim,
            num_layers=gnn_num_layers,
            dropout=dropout,
        )

        # 反应物-产物交叉注意力
        self.cross_attention = nn.MultiheadAttention(
            embed_dim=gnn_hidden_dim,
            num_heads=num_attention_heads,
            dropout=dropout,
            batch_first=True,
        )

        # 电化学条件
        self.echem_encoder = nn.Sequential(
            nn.Linear(echem_feat_dim, 32),
            nn.ReLU(),
            nn.Linear(32, 32),
            nn.ReLU(),
        )

        # 预测头
        fusion_dim = gnn_hidden_dim * 2 + 32  # attended_reactant + product + echem
        self.predictor = nn.Sequential(
            nn.Linear(fusion_dim, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
        )

    def forward(self, reactant_graph, product_graph, echem_features):
        # GNN编码
        reactant_emb = self._encode_graph(reactant_graph)  # [B, H]
        product_emb = self._encode_graph(product_graph)    # [B, H]

        # 交叉注意力：反应物关注产物
        reactant_emb = reactant_emb.unsqueeze(1)  # [B, 1, H]
        product_emb_q = product_emb.unsqueeze(1)  # [B, 1, H]

        attended, _ = self.cross_attention(
            query=reactant_emb,
            key=product_emb_q,
            value=product_emb_q,
        )
        attended = attended.squeeze(1)  # [B, H]

        # 电化学条件
        echem_emb = self.echem_encoder(echem_features)

        # 融合预测
        combined = torch.cat([attended, product_emb, echem_emb], dim=-1)
        return torch.sigmoid(self.predictor(combined))

    def _encode_graph(self, graph):
        return self.gnn(
            node_feats=graph['node_feats'],
            edge_index=graph['edge_index'],
            edge_feats=graph['edge_feats'],
            batch=graph['batch'],
            num_graphs=graph['num_graphs'],
        )


if __name__ == "__main__":
    # 测试
    import sys
    sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent.parent))
    from utils.graph_features import smiles_to_graph, batch_graphs, ATOM_FEAT_DIM, BOND_FEAT_DIM

    print(f"原子特征维度: {ATOM_FEAT_DIM}")
    print(f"键特征维度: {BOND_FEAT_DIM}")

    # 创建模型
    model = PureGNNYieldPredictor(
        atom_feat_dim=ATOM_FEAT_DIM,
        edge_feat_dim=BOND_FEAT_DIM,
        gnn_hidden_dim=128,
        gnn_num_layers=3,
        dropout=0.2,
    )

    num_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"模型参数量: {num_params:,}")

    # 测试前向传播
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
    echem_feat = torch.randn(batch_size, 6)

    output = model(reactant_g, product_g, echem_feat)
    print(f"输出形状: {output.shape}")
    print(f"输出值: {output.flatten().tolist()}")
