"""Stage-1 GNN 版本: 用 MolecularGNN 替换 Morgan FP encoder。

输入: reactant_graph + product_graph (从 SMILES 动态构建)
GNN 输出每个分子的 graph-level vec (hidden_dim=128)
反应级特征 = [vec_r, vec_p, vec_p - vec_r] → 384D → 9 heads

复用 models.gnn_condition_recommender.MolecularGNN (纯 PyTorch, 不依赖 PyG)
"""
import torch
import torch.nn as nn
from typing import Dict, Optional

from .gnn_condition_recommender import MolecularGNN
from .condition_stage1 import HEAD_KEYS


class ConditionStage1GNN(nn.Module):
    """GNN-based Stage-1: 反应物 GNN + 产物 GNN → 9 head 分类。"""

    def __init__(self, num_classes: Dict[str, int],
                  atom_feat_dim: int = 42, edge_feat_dim: int = 10,
                  gnn_hidden: int = 128, gnn_layers: int = 3, gnn_heads: int = 4,
                  hidden_dims=(512, 384), dropout: float = 0.3,
                  extra_heads=None):
        super().__init__()
        self.gnn = MolecularGNN(
            atom_feat_dim=atom_feat_dim, edge_feat_dim=edge_feat_dim,
            xtb_feat_dim=11,  # 不用 xTB 但 MolecularGNN 必须有这维度 (后面置零输入)
            hidden_dim=gnn_hidden, num_layers=gnn_layers, num_heads=gnn_heads,
            dropout=dropout,
        )
        # 反应级特征: reactant + product + diff = 3 * gnn_hidden
        reaction_dim = 3 * gnn_hidden

        # 后续 MLP encoder
        layers = []
        prev = reaction_dim
        for h in hidden_dims:
            layers += [nn.Linear(prev, h), nn.BatchNorm1d(h),
                       nn.GELU(), nn.Dropout(dropout)]
            prev = h
        self.encoder = nn.Sequential(*layers)

        all_heads = list(HEAD_KEYS) + list(extra_heads or [])
        self.heads = nn.ModuleDict({
            k: nn.Linear(prev, num_classes[k]) for k in all_heads if k in num_classes
        })

    def _encode_graph(self, graph: Dict) -> torch.Tensor:
        """对一个 graph dict 跑 GNN 得 graph-level vec (B, gnn_hidden)。"""
        num_graphs = graph['num_graphs']
        node_feats = graph['node_feats']
        # GNN 输入 xtb 全零 (我们不用 xTB)
        zeros = torch.zeros(num_graphs, 11, device=node_feats.device)
        return self.gnn(
            node_feats=node_feats,
            edge_index=graph['edge_index'],
            edge_feats=graph['edge_feats'],
            batch=graph['batch'],
            num_graphs=num_graphs,
            xtb_feats=zeros,
        )

    def forward(self, reactant_graph: Dict, product_graph: Dict) -> Dict[str, torch.Tensor]:
        vec_r = self._encode_graph(reactant_graph)
        vec_p = self._encode_graph(product_graph)
        diff = vec_p - vec_r
        x = torch.cat([vec_r, vec_p, diff], dim=-1)
        h = self.encoder(x)
        return {k: head(h) for k, head in self.heads.items()}
