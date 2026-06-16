"""
分子图特征提取模块：将SMILES转换为图数据结构（纯PyTorch实现，不依赖torch_geometric）
"""
import torch
import numpy as np
from typing import List, Dict, Optional, Tuple
from rdkit import Chem
from rdkit.Chem import rdchem


# ============================================================
# 原子特征化
# ============================================================

# 支持的原子类型（覆盖有机化学常见元素）
ATOM_LIST = [6, 7, 8, 9, 15, 16, 17, 35, 53, 5]  # C, N, O, F, P, S, Cl, Br, I, B
DEGREE_LIST = [0, 1, 2, 3, 4, 5, 6]
FORMAL_CHARGE_LIST = [-2, -1, 0, 1, 2]
HYBRIDIZATION_LIST = [
    rdchem.HybridizationType.SP,
    rdchem.HybridizationType.SP2,
    rdchem.HybridizationType.SP3,
    rdchem.HybridizationType.SP3D,
    rdchem.HybridizationType.SP3D2,
]
NUM_HS_LIST = [0, 1, 2, 3, 4]
RING_SIZE_LIST = [3, 4, 5, 6, 7, 8]

# 特征维度常量
ATOM_FEAT_DIM = (
    len(ATOM_LIST) + 1       # 原子类型 one-hot (11)
    + len(DEGREE_LIST)        # 度数 (7)
    + len(FORMAL_CHARGE_LIST) # 形式电荷 (5)
    + len(HYBRIDIZATION_LIST) # 杂化 (5)
    + 1                       # 芳香性 (1)
    + len(NUM_HS_LIST)        # 氢原子数 (5)
    + 1                       # 在环中 (1)
    + len(RING_SIZE_LIST) + 1 # 环大小 (7)
)  # 总计 42

BOND_FEAT_DIM = (
    4    # 键类型 (单/双/三/芳香)
    + 1  # 是否共轭
    + 1  # 在环中
    + 4  # 立体化学
)  # 总计 10


def one_hot(value, choices: list) -> List[int]:
    """生成one-hot编码，如果不在choices中则最后一位为1"""
    encoding = [0] * (len(choices) + 1)
    if value in choices:
        encoding[choices.index(value)] = 1
    else:
        encoding[-1] = 1  # unknown
    return encoding


def one_hot_no_unknown(value, choices: list) -> List[int]:
    """生成one-hot编码（无unknown位）"""
    encoding = [0] * len(choices)
    if value in choices:
        encoding[choices.index(value)] = 1
    return encoding


def atom_features(atom: rdchem.Atom) -> List[float]:
    """提取原子特征向量"""
    features = []

    # 原子类型 one-hot (11维: 10 types + unknown)
    features.extend(one_hot(atom.GetAtomicNum(), ATOM_LIST))

    # 度数 one-hot (7维，无unknown)
    features.extend(one_hot_no_unknown(atom.GetTotalDegree(), DEGREE_LIST))

    # 形式电荷 one-hot (5维，无unknown)
    features.extend(one_hot_no_unknown(atom.GetFormalCharge(), FORMAL_CHARGE_LIST))

    # 杂化 one-hot (5维，无unknown)
    features.extend(one_hot_no_unknown(atom.GetHybridization(), HYBRIDIZATION_LIST))

    # 芳香性 (1维)
    features.append(1.0 if atom.GetIsAromatic() else 0.0)

    # 氢原子数 one-hot (5维，无unknown)
    features.extend(one_hot_no_unknown(atom.GetTotalNumHs(), NUM_HS_LIST))

    # 在环中 (1维)
    features.append(1.0 if atom.IsInRing() else 0.0)

    # 环大小 one-hot (7维: 6 sizes + 不在环)
    ring_info = atom.GetOwningMol().GetRingInfo()
    ring_sizes = []
    if atom.IsInRing():
        for size in RING_SIZE_LIST:
            if ring_info.IsAtomInRingOfSize(atom.GetIdx(), size):
                ring_sizes.append(size)
    if ring_sizes:
        ring_encoding = [0] * (len(RING_SIZE_LIST) + 1)
        for s in ring_sizes:
            if s in RING_SIZE_LIST:
                ring_encoding[RING_SIZE_LIST.index(s)] = 1
        features.extend(ring_encoding)
    else:
        ring_encoding = [0] * len(RING_SIZE_LIST) + [1]  # 不在环
        features.extend(ring_encoding)

    return features


def bond_features(bond: rdchem.Bond) -> List[float]:
    """提取化学键特征向量"""
    features = []

    # 键类型 one-hot (4维)
    bt = bond.GetBondType()
    features.extend([
        1.0 if bt == rdchem.BondType.SINGLE else 0.0,
        1.0 if bt == rdchem.BondType.DOUBLE else 0.0,
        1.0 if bt == rdchem.BondType.TRIPLE else 0.0,
        1.0 if bt == rdchem.BondType.AROMATIC else 0.0,
    ])

    # 是否共轭 (1维)
    features.append(1.0 if bond.GetIsConjugated() else 0.0)

    # 在环中 (1维)
    features.append(1.0 if bond.IsInRing() else 0.0)

    # 立体化学 one-hot (4维)
    stereo = bond.GetStereo()
    features.extend([
        1.0 if stereo == rdchem.BondStereo.STEREONONE else 0.0,
        1.0 if stereo == rdchem.BondStereo.STEREOZ else 0.0,
        1.0 if stereo == rdchem.BondStereo.STEREOE else 0.0,
        1.0 if stereo in (rdchem.BondStereo.STEREOCIS, rdchem.BondStereo.STEREOTRANS,
                          rdchem.BondStereo.STEREOANY) else 0.0,
    ])

    return features


# ============================================================
# SMILES → 分子图
# ============================================================

def smiles_to_graph(smiles: str) -> Optional[Dict[str, torch.Tensor]]:
    """
    将SMILES转换为图数据

    Returns:
        dict with:
            'node_feats': Tensor [num_atoms, ATOM_FEAT_DIM]
            'edge_index': Tensor [2, num_edges*2] (双向边)
            'edge_feats': Tensor [num_edges*2, BOND_FEAT_DIM]
        如果SMILES无效返回None
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None

    # 原子特征
    node_feat_list = []
    for atom in mol.GetAtoms():
        node_feat_list.append(atom_features(atom))

    if len(node_feat_list) == 0:
        return None

    node_feats = torch.tensor(node_feat_list, dtype=torch.float32)

    # 化学键（双向边）
    edge_indices = []
    edge_feat_list = []
    for bond in mol.GetBonds():
        i = bond.GetBeginAtomIdx()
        j = bond.GetEndAtomIdx()
        bf = bond_features(bond)
        # 添加双向边
        edge_indices.append([i, j])
        edge_indices.append([j, i])
        edge_feat_list.append(bf)
        edge_feat_list.append(bf)

    if len(edge_indices) > 0:
        edge_index = torch.tensor(edge_indices, dtype=torch.long).t().contiguous()  # [2, E]
        edge_feats = torch.tensor(edge_feat_list, dtype=torch.float32)
    else:
        # 单原子分子（如金属离子），没有边
        edge_index = torch.zeros(2, 0, dtype=torch.long)
        edge_feats = torch.zeros(0, BOND_FEAT_DIM, dtype=torch.float32)

    return {
        'node_feats': node_feats,
        'edge_index': edge_index,
        'edge_feats': edge_feats,
    }


def get_dummy_graph() -> Dict[str, torch.Tensor]:
    """返回一个虚拟图（用于缺失分子的占位符）"""
    return {
        'node_feats': torch.zeros(1, ATOM_FEAT_DIM, dtype=torch.float32),
        'edge_index': torch.zeros(2, 0, dtype=torch.long),
        'edge_feats': torch.zeros(0, BOND_FEAT_DIM, dtype=torch.float32),
    }


def smiles_list_to_graph(smiles_list: List[str]) -> Dict[str, torch.Tensor]:
    """
    将多个SMILES合并为一个图（多个不连通子图）

    用于处理多个反应物/溶剂的情况
    """
    if not smiles_list:
        return get_dummy_graph()

    graphs = []
    for smi in smiles_list:
        g = smiles_to_graph(smi)
        if g is not None:
            graphs.append(g)

    if not graphs:
        return get_dummy_graph()

    if len(graphs) == 1:
        return graphs[0]

    return merge_graphs(graphs)


def merge_graphs(graphs: List[Dict[str, torch.Tensor]]) -> Dict[str, torch.Tensor]:
    """合并多个分子图为一个不连通图"""
    all_node_feats = []
    all_edge_indices = []
    all_edge_feats = []
    node_offset = 0

    for g in graphs:
        n_nodes = g['node_feats'].shape[0]
        all_node_feats.append(g['node_feats'])

        if g['edge_index'].shape[1] > 0:
            all_edge_indices.append(g['edge_index'] + node_offset)
        all_edge_feats.append(g['edge_feats'])

        node_offset += n_nodes

    node_feats = torch.cat(all_node_feats, dim=0)

    if all_edge_indices:
        edge_index = torch.cat(all_edge_indices, dim=1)
    else:
        edge_index = torch.zeros(2, 0, dtype=torch.long)

    if all_edge_feats and sum(ef.shape[0] for ef in all_edge_feats) > 0:
        edge_feats = torch.cat([ef for ef in all_edge_feats if ef.shape[0] > 0], dim=0)
    else:
        edge_feats = torch.zeros(0, BOND_FEAT_DIM, dtype=torch.float32)

    return {
        'node_feats': node_feats,
        'edge_index': edge_index,
        'edge_feats': edge_feats,
    }


# ============================================================
# 批处理
# ============================================================

def batch_graphs(graph_list: List[Dict[str, torch.Tensor]]) -> Dict[str, torch.Tensor]:
    """
    将一个batch的图拼接成一个大的不连通图

    Returns:
        dict with:
            'node_feats': Tensor [total_nodes, ATOM_FEAT_DIM]
            'edge_index': Tensor [2, total_edges]
            'edge_feats': Tensor [total_edges, BOND_FEAT_DIM]
            'batch': Tensor [total_nodes] — 每个节点所属的图索引
            'num_graphs': int
    """
    all_node_feats = []
    all_edge_indices = []
    all_edge_feats = []
    batch_indices = []
    node_offset = 0

    for i, g in enumerate(graph_list):
        n_nodes = g['node_feats'].shape[0]
        all_node_feats.append(g['node_feats'])

        if g['edge_index'].shape[1] > 0:
            all_edge_indices.append(g['edge_index'] + node_offset)
        all_edge_feats.append(g['edge_feats'])

        batch_indices.extend([i] * n_nodes)
        node_offset += n_nodes

    node_feats = torch.cat(all_node_feats, dim=0)

    if all_edge_indices:
        edge_index = torch.cat(all_edge_indices, dim=1)
    else:
        edge_index = torch.zeros(2, 0, dtype=torch.long)

    valid_edge_feats = [ef for ef in all_edge_feats if ef.shape[0] > 0]
    if valid_edge_feats:
        edge_feats = torch.cat(valid_edge_feats, dim=0)
    else:
        edge_feats = torch.zeros(0, BOND_FEAT_DIM, dtype=torch.float32)

    batch = torch.tensor(batch_indices, dtype=torch.long)

    return {
        'node_feats': node_feats,
        'edge_index': edge_index,
        'edge_feats': edge_feats,
        'batch': batch,
        'num_graphs': len(graph_list),
    }


if __name__ == "__main__":
    # 测试
    test_smiles = "C=C(c1ccccc1)C(C)(O)c1ccccc1"
    g = smiles_to_graph(test_smiles)
    if g:
        print(f"节点数: {g['node_feats'].shape[0]}")
        print(f"原子特征维度: {g['node_feats'].shape[1]} (期望 {ATOM_FEAT_DIM})")
        print(f"边数: {g['edge_index'].shape[1]}")
        print(f"键特征维度: {g['edge_feats'].shape[1]} (期望 {BOND_FEAT_DIM})")

    # 测试批处理
    smiles_list = ["CCO", "c1ccccc1", "CC(=O)O"]
    graphs = [smiles_to_graph(s) for s in smiles_list]
    batched = batch_graphs(graphs)
    print(f"\n批处理 {len(smiles_list)} 个图:")
    print(f"  总节点数: {batched['node_feats'].shape[0]}")
    print(f"  总边数: {batched['edge_index'].shape[1]}")
    print(f"  batch索引: {batched['batch']}")
