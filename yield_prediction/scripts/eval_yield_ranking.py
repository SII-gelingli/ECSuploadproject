"""
评估 YieldPredictor 作为 top-k 条件排序器的贡献

场景: Model 1 对每个条件提出 top-k 候选 → 枚举组合 → YieldPredictor 打分 → 选最高产率

排序策略:
  M1_TOP1          : M1 argmax（基线，不用 Yield 模型）
  M1_TOP3_PROB     : M1 top-3 per condition → 联合概率排序 → 选最高（不用 Yield）
  M1_TOP3_YIELD    : M1 top-3 per condition → Yield 打分 → 选最高产率
  M1_TOP5_YIELD    : M1 top-5 (yield-visible) + top-1 (invisible) → Yield 打分
  M1_TOP3_COMBINED : 0.5*normalized_prob + 0.5*normalized_yield → 混合排序

注意: YieldPredictor 输入为 reaction_fp(6144) + solvent_fp(2048) + electrolyte_fp(2048) + echem(6) [+ xtb(55)]
  → 只能 "看见" 5/7 条件: anode, cathode, cell_type, solvent, electrolyte
  → 对 reagent, catalyst 无感知 → 这两个始终用 M1 top-1

评估指标:
  - Per-condition top-1 accuracy
  - Joint exact match (7/7)
  - Avg conditions correct
  - 预测产率 vs 真实产率相关性
  - 不同策略间的 delta

数据: train.pt 测试集 (851 reactions, seed=42 80/10/10)
  → 与 yield model 训练数据同源，确保无泄漏

用法:
    cd yield_prediction
    python scripts/eval_yield_ranking.py --device cuda
"""
import sys
import argparse
import json
import time
import warnings
from pathlib import Path
from datetime import datetime
from itertools import product as iter_product

warnings.filterwarnings('ignore')

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.append(LOCAL_PACKAGES)

import numpy as np
import torch
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
from tqdm import tqdm

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.yield_predictor import YieldPredictor
from models.condition_recommender import (
    ConditionRecommender, ConditionRecommenderXTB,
    DualTowerConditionRecommender, CompactConditionRecommender,
)
from utils.feature_extractor import MolecularFeatureExtractor

# ── 常量 ──────────────────────────────────────────────────────
CONDITION_KEYS = ['anode', 'cathode', 'cell_type', 'electrolyte', 'solvent', 'reagent', 'catalyst']
YIELD_VISIBLE_KEYS = ['anode', 'cathode', 'cell_type', 'solvent', 'electrolyte']
YIELD_INVISIBLE_KEYS = ['reagent', 'catalyst']
FINGERPRINT_SIZE = 2048


# ── 数据加载 ──────────────────────────────────────────────────

def load_data_and_split(device):
    """加载 train.pt 并按 seed=42 分割，返回 test set (851 reactions)"""
    data = torch.load(project_root / 'data' / 'train.pt', map_location='cpu', weights_only=False)
    train_data, temp = train_test_split(data, test_size=0.2, random_state=42)
    val_data, test_data = train_test_split(temp, test_size=0.5, random_state=42)
    print(f"  Data: {len(data)} total, {len(train_data)} train, {len(val_data)} val, {len(test_data)} test")
    return train_data, test_data


def load_vocab():
    """加载 vocab.json 并构建 idx→SMILES 映射"""
    vocab_path = project_root / 'data' / 'vocab.json'
    with open(vocab_path) as f:
        vocab = json.load(f)
    idx_to_smiles = {}
    for key in ['electrolyte', 'solvent', 'reagent', 'catalyst']:
        idx_to_smiles[key] = {v: k for k, v in vocab.get(key, {}).items()}
        idx_to_smiles[key][0] = ''  # index 0 = none/unknown
    return vocab, idx_to_smiles


# ── 模型加载 ──────────────────────────────────────────────────

def load_condition_model(device):
    """加载条件推荐模型 (Model 1)"""
    ckpt_path = project_root / 'checkpoints' / 'condition_model' / 'best_condition_model.pt'
    checkpoint = torch.load(ckpt_path, map_location=device, weights_only=False)
    sd = checkpoint['model_state_dict']

    # 提取 vocab sizes
    vocab_sizes = {}
    for key_name in ['anode', 'cathode', 'cell_type', 'electrolyte', 'solvent', 'reagent', 'catalyst']:
        head_key = f'{key_name}_head.weight'
        if head_key in sd:
            vocab_sizes[key_name] = sd[head_key].shape[0]

    # 检测架构并构建模型
    if 'fp_encoder.0.weight' in sd:
        # ConditionRecommenderXTB: separate fp_encoder + xtb_encoder
        fp_dim = sd['fp_encoder.0.weight'].shape[1]
        xtb_dim = sd['xtb_encoder.0.weight'].shape[1]
        model = ConditionRecommenderXTB(
            fp_dim=fp_dim, xtb_dim=xtb_dim, hidden_dim=256,
            num_anode_materials=vocab_sizes['anode'],
            num_cathode_materials=vocab_sizes['cathode'],
            num_cell_types=vocab_sizes['cell_type'],
            num_electrolytes=vocab_sizes['electrolyte'],
            num_solvents=vocab_sizes['solvent'],
            num_reagents=vocab_sizes['reagent'],
            num_catalysts=vocab_sizes['catalyst'],
        )
        model_type = 'ConditionRecommenderXTB'
        cond_input_dim = fp_dim + xtb_dim
    elif 'reaction_encoder.0.weight' in sd:
        # ConditionRecommender: single reaction_encoder
        reaction_dim = sd['reaction_encoder.0.weight'].shape[1]
        hidden_dim = sd['reaction_encoder.0.weight'].shape[0]
        model = ConditionRecommender(
            reaction_dim=reaction_dim, hidden_dim=hidden_dim,
            num_anode_materials=vocab_sizes['anode'],
            num_cathode_materials=vocab_sizes['cathode'],
            num_cell_types=vocab_sizes['cell_type'],
            num_electrolytes=vocab_sizes['electrolyte'],
            num_solvents=vocab_sizes['solvent'],
            num_reagents=vocab_sizes['reagent'],
            num_catalysts=vocab_sizes['catalyst'],
        )
        model_type = 'ConditionRecommender'
        cond_input_dim = reaction_dim
    else:
        raise ValueError("Unknown condition model architecture in checkpoint")

    model.load_state_dict(sd)
    model.to(device).eval()
    print(f"  Condition model: {model_type}, input_dim={cond_input_dim}, vocab_sizes={vocab_sizes}")
    return model, model_type, cond_input_dim, vocab_sizes


def load_yield_model(device, ckpt_override=None):
    """加载产率预测模型"""
    ckpt_path = Path(ckpt_override) if ckpt_override else project_root / 'checkpoints' / 'best_model.pt'
    checkpoint = torch.load(ckpt_path, map_location=device, weights_only=False)
    sd = checkpoint['model_state_dict']
    input_dim = sd['encoder.0.weight'].shape[1]

    config = checkpoint.get('config', {})
    hidden_dims = config.get('model', {}).get('predictor', {}).get('hidden_dims', [512, 256, 128])
    dropout = config.get('model', {}).get('predictor', {}).get('dropout', 0.2)

    # Fix legacy key naming
    fixed_sd = {}
    for k, v in sd.items():
        if k.startswith('output.'):
            fixed_sd['output_layer.' + k[len('output.'):]] = v
        else:
            fixed_sd[k] = v

    model = YieldPredictor(input_dim=input_dim, hidden_dims=hidden_dims, dropout=dropout)
    model.load_state_dict(fixed_sd)
    model.to(device).eval()
    print(f"  Yield model: input_dim={input_dim}, hidden={hidden_dims}")
    return model, input_dim


# ── xTB 特征 ──────────────────────────────────────────────────

def load_xtb_lookup(yield_input_dim):
    """加载 xTB 特征查找表（如果 yield 模型需要）"""
    base_dim = 5 * FINGERPRINT_SIZE + 6  # 10246
    if yield_input_dim <= base_dim:
        return None, 0

    xtb_dim = yield_input_dim - base_dim
    csv_path = project_root / 'data' / 'xtb_reaction_molecules.csv'
    if not csv_path.exists():
        print(f"  Warning: xTB CSV not found at {csv_path}, will pad zeros")
        return None, xtb_dim

    from utils.xtb_features import XTBFeatureLookup
    lookup = XTBFeatureLookup(str(csv_path))
    print(f"  xTB lookup loaded: {len(lookup.xtb_lookup)} entries, dim={xtb_dim}")
    return lookup, xtb_dim


# ── 指纹缓存 ──────────────────────────────────────────────────

class FingerprintCache:
    """缓存 SMILES → Morgan FP 映射，避免重复计算"""

    def __init__(self, fp_size=2048, radius=2):
        self.extractor = MolecularFeatureExtractor(fp_size)
        self.fp_size = fp_size
        self._cache = {'': np.zeros(fp_size, dtype=np.float32)}

    def get(self, smiles: str) -> np.ndarray:
        if smiles not in self._cache:
            try:
                fp = self.extractor.get_morgan_fingerprint(smiles)
                self._cache[smiles] = np.array(fp, dtype=np.float32)
            except Exception:
                self._cache[smiles] = np.zeros(self.fp_size, dtype=np.float32)
        return self._cache[smiles]

    def preload_vocab(self, idx_to_smiles):
        """预加载 vocab 中所有 SMILES 的指纹"""
        count = 0
        for key in ['solvent', 'electrolyte']:
            for idx, smiles in idx_to_smiles[key].items():
                if smiles and smiles not in self._cache:
                    self.get(smiles)
                    count += 1
        print(f"  FP cache preloaded: {count} new entries, {len(self._cache)} total")


# ── 构建 Yield 模型特征向量 ───────────────────────────────────

def build_yield_features(
    reaction_fp_base,   # 6144D
    solvent_fp,         # 2048D
    electrolyte_fp,     # 2048D
    anode_idx,
    cathode_idx,
    cell_type_idx,
    xtb_features=None,  # 55D or None
    xtb_dim=0,
):
    """构建 yield 模型的完整输入特征"""
    echem = np.array([
        float(anode_idx), float(cathode_idx),
        0.0,  # current_mA (unknown)
        0.0,  # current_density (unknown)
        0.0,  # potential_V (unknown)
        float(cell_type_idx),
    ], dtype=np.float32)

    features = np.concatenate([reaction_fp_base, solvent_fp, electrolyte_fp, echem])

    if xtb_dim > 0:
        if xtb_features is not None:
            features = np.concatenate([features, np.array(xtb_features, dtype=np.float32)])
        else:
            features = np.concatenate([features, np.zeros(xtb_dim, dtype=np.float32)])

    return features


# ── 条件标签提取 ──────────────────────────────────────────────

def extract_labels(test_data):
    """从 test_data 提取所有条件标签和反应信息"""
    labels = {k: [] for k in CONDITION_KEYS}
    reaction_fps = []
    solvent_fps = []
    electrolyte_fps = []
    reactant_smiles_list = []
    product_smiles_list = []
    yields = []

    label_key_map = {
        'anode': 'anode', 'cathode': 'cathode', 'cell_type': 'cell_type',
        'electrolyte': 'electrolyte_label', 'solvent': 'solvent_label',
        'reagent': 'reagent_label', 'catalyst': 'catalyst_label',
    }

    for r in test_data:
        for cond_key in CONDITION_KEYS:
            data_key = label_key_map[cond_key]
            labels[cond_key].append(r[data_key])

        rxn_fp = np.concatenate([r['reactant_fp'], r['product_fp'], r['diff_fp']])
        reaction_fps.append(rxn_fp)
        solvent_fps.append(np.array(r['solvent_fp'], dtype=np.float32))
        electrolyte_fps.append(np.array(r['electrolyte_fp'], dtype=np.float32))
        reactant_smiles_list.append(r['reactant_smiles'])
        product_smiles_list.append(r['product_smiles'])
        yields.append(r['yield'])

    labels = {k: np.array(v) for k, v in labels.items()}
    return {
        'labels': labels,
        'reaction_fps': np.array(reaction_fps, dtype=np.float32),
        'solvent_fps': np.array(solvent_fps, dtype=np.float32),
        'electrolyte_fps': np.array(electrolyte_fps, dtype=np.float32),
        'reactant_smiles': reactant_smiles_list,
        'product_smiles': product_smiles_list,
        'yields': np.array(yields, dtype=np.float32),
    }


# ── M1 推理 ──────────────────────────────────────────────────

def get_m1_logits(model, reaction_fps, cond_input_dim, device, test_data=None, batch_size=256):
    """获取 Model 1 对所有测试反应的 logits

    如果条件模型需要的 input_dim > 6144 (如 6177 = 6144+33 xTB),
    则计算 xTB 特征并拼接。
    """
    logits = {k: [] for k in CONDITION_KEYS}
    n = len(reaction_fps)
    fp_dim = reaction_fps.shape[1]  # 6144
    pad_dim = cond_input_dim - fp_dim if cond_input_dim > fp_dim else 0

    # 如果条件模型需要 xTB 特征，zero-pad（xTB 归一化统计量未保存在 checkpoint）
    # 注意: 这会略微降低 M1 绝对性能，但所有策略共享相同的 M1 logits，
    # 因此策略间的相对比较仍然有效。
    if pad_dim > 0:
        print(f"  Zero-padding {pad_dim}D xTB features for condition model "
              f"(normalization stats not in checkpoint)")
        full_fps = np.concatenate([reaction_fps, np.zeros((n, pad_dim), dtype=np.float32)], axis=1)
    else:
        full_fps = reaction_fps

    with torch.no_grad():
        for start in range(0, n, batch_size):
            end = min(start + batch_size, n)
            fp_batch = torch.tensor(full_fps[start:end], dtype=torch.float32).to(device)
            preds = model(fp_batch)
            for key in CONDITION_KEYS:
                logits[key].append(preds[f'{key}_logits'].cpu())

    return {k: torch.cat(v, dim=0) for k, v in logits.items()}


# ── 排序策略 ──────────────────────────────────────────────────

def strategy_m1_top1(m1_logits, **kwargs):
    """M1 argmax（基线）"""
    preds = {}
    for key in CONDITION_KEYS:
        preds[key] = m1_logits[key].argmax(dim=-1).numpy()
    return preds


def strategy_m1_topk_prob(m1_logits, k=3, **kwargs):
    """M1 top-k per condition → 联合概率排序 → 选最高"""
    n = m1_logits['anode'].size(0)
    preds = {key: np.zeros(n, dtype=int) for key in CONDITION_KEYS}

    # 预计算 softmax
    probs = {}
    for key in CONDITION_KEYS:
        probs[key] = F.softmax(m1_logits[key], dim=-1)

    for i in range(n):
        # 获取每个条件的 top-k
        topk_indices = {}
        topk_probs = {}
        for key in CONDITION_KEYS:
            rk = min(k, probs[key].size(-1))
            top_p, top_idx = torch.topk(probs[key][i], rk)
            topk_indices[key] = top_idx.numpy()
            topk_probs[key] = top_p.numpy()

        # 枚举所有组合，计算联合概率
        combo_ranges = [range(min(k, len(topk_indices[key]))) for key in CONDITION_KEYS]
        best_prob = -1
        best_combo = None

        for combo in iter_product(*combo_ranges):
            joint_prob = 1.0
            for j, key in enumerate(CONDITION_KEYS):
                joint_prob *= topk_probs[key][combo[j]]
            if joint_prob > best_prob:
                best_prob = joint_prob
                best_combo = combo

        # 写入预测
        for j, key in enumerate(CONDITION_KEYS):
            preds[key][i] = topk_indices[key][best_combo[j]]

    return preds


def strategy_m1_topk_yield(
    m1_logits, k, yield_model, yield_input_dim, device,
    test_info, idx_to_smiles, fp_cache, xtb_lookup, xtb_dim,
    **kwargs,
):
    """M1 top-k → 枚举组合 → YieldPredictor 打分 → 选最高产率"""
    n = m1_logits['anode'].size(0)
    preds = {key: np.zeros(n, dtype=int) for key in CONDITION_KEYS}
    predicted_yields = np.zeros(n)

    probs = {}
    for key in CONDITION_KEYS:
        probs[key] = F.softmax(m1_logits[key], dim=-1)

    reaction_fps = test_info['reaction_fps']

    for i in tqdm(range(n), desc=f"  Yield ranking (k={k})", leave=False):
        rxn_fp = reaction_fps[i]  # 6144D

        # 获取每个条件的 top-k 候选
        topk_indices = {}
        topk_probs_arr = {}
        for key in CONDITION_KEYS:
            rk = min(k, probs[key].size(-1))
            if key in YIELD_INVISIBLE_KEYS:
                rk = 1  # reagent/catalyst 只取 top-1
            top_p, top_idx = torch.topk(probs[key][i], rk)
            topk_indices[key] = top_idx.numpy()
            topk_probs_arr[key] = top_p.numpy()

        # 枚举 yield-visible 条件的组合
        visible_ranges = [range(len(topk_indices[key])) for key in YIELD_VISIBLE_KEYS]
        invisible_indices = {key: topk_indices[key][0] for key in YIELD_INVISIBLE_KEYS}

        # 预获取 xTB 特征（整个反应共享）
        xtb_feats = None
        if xtb_lookup is not None and xtb_dim > 0:
            try:
                xtb_feats = xtb_lookup.get_reaction_features(
                    test_info['reactant_smiles'][i],
                    test_info['product_smiles'][i],
                    [], '',  # solvent/electrolyte varies per combo
                )
            except Exception:
                xtb_feats = None

        # 批量构建特征
        combo_features = []
        combo_list = []
        for combo in iter_product(*visible_ranges):
            vis_map = {}
            for j, key in enumerate(YIELD_VISIBLE_KEYS):
                vis_map[key] = topk_indices[key][combo[j]]

            solvent_idx = vis_map['solvent']
            electrolyte_idx = vis_map['electrolyte']
            solvent_smiles = idx_to_smiles['solvent'].get(int(solvent_idx), '')
            electrolyte_smiles = idx_to_smiles['electrolyte'].get(int(electrolyte_idx), '')
            solvent_fp = fp_cache.get(solvent_smiles)
            electrolyte_fp = fp_cache.get(electrolyte_smiles)

            feat = build_yield_features(
                rxn_fp, solvent_fp, electrolyte_fp,
                vis_map['anode'], vis_map['cathode'], vis_map['cell_type'],
                xtb_feats, xtb_dim,
            )
            combo_features.append(feat)
            combo_list.append(combo)

        # 批量 yield 推理
        feat_tensor = torch.tensor(np.array(combo_features), dtype=torch.float32).to(device)
        with torch.no_grad():
            yields_pred = yield_model(feat_tensor).cpu().numpy().flatten() * 100

        # 选最高产率
        best_idx = np.argmax(yields_pred)
        best_combo = combo_list[best_idx]
        predicted_yields[i] = yields_pred[best_idx]

        for j, key in enumerate(YIELD_VISIBLE_KEYS):
            preds[key][i] = topk_indices[key][best_combo[j]]
        for key in YIELD_INVISIBLE_KEYS:
            preds[key][i] = invisible_indices[key]

    return preds, predicted_yields


def strategy_m1_topk_combined(
    m1_logits, k, yield_model, yield_input_dim, device,
    test_info, idx_to_smiles, fp_cache, xtb_lookup, xtb_dim,
    alpha=0.5,
    **kwargs,
):
    """混合排序: alpha * normalized_yield + (1-alpha) * normalized_prob"""
    n = m1_logits['anode'].size(0)
    preds = {key: np.zeros(n, dtype=int) for key in CONDITION_KEYS}
    predicted_yields = np.zeros(n)

    probs = {}
    for key in CONDITION_KEYS:
        probs[key] = F.softmax(m1_logits[key], dim=-1)

    reaction_fps = test_info['reaction_fps']

    for i in tqdm(range(n), desc=f"  Combined ranking (k={k}, α={alpha})", leave=False):
        rxn_fp = reaction_fps[i]

        topk_indices = {}
        topk_probs_arr = {}
        for key in CONDITION_KEYS:
            rk = min(k, probs[key].size(-1))
            if key in YIELD_INVISIBLE_KEYS:
                rk = 1
            top_p, top_idx = torch.topk(probs[key][i], rk)
            topk_indices[key] = top_idx.numpy()
            topk_probs_arr[key] = top_p.numpy()

        visible_ranges = [range(len(topk_indices[key])) for key in YIELD_VISIBLE_KEYS]
        invisible_indices = {key: topk_indices[key][0] for key in YIELD_INVISIBLE_KEYS}

        xtb_feats = None
        if xtb_lookup is not None and xtb_dim > 0:
            try:
                xtb_feats = xtb_lookup.get_reaction_features(
                    test_info['reactant_smiles'][i],
                    test_info['product_smiles'][i],
                    [], '',
                )
            except Exception:
                xtb_feats = None

        combo_features = []
        combo_probs = []
        combo_list = []
        for combo in iter_product(*visible_ranges):
            vis_map = {}
            joint_prob = 1.0
            for j, key in enumerate(YIELD_VISIBLE_KEYS):
                vis_map[key] = topk_indices[key][combo[j]]
                joint_prob *= topk_probs_arr[key][combo[j]]
            for key in YIELD_INVISIBLE_KEYS:
                joint_prob *= topk_probs_arr[key][0]

            solvent_smiles = idx_to_smiles['solvent'].get(int(vis_map['solvent']), '')
            electrolyte_smiles = idx_to_smiles['electrolyte'].get(int(vis_map['electrolyte']), '')
            solvent_fp = fp_cache.get(solvent_smiles)
            electrolyte_fp = fp_cache.get(electrolyte_smiles)

            feat = build_yield_features(
                rxn_fp, solvent_fp, electrolyte_fp,
                vis_map['anode'], vis_map['cathode'], vis_map['cell_type'],
                xtb_feats, xtb_dim,
            )
            combo_features.append(feat)
            combo_probs.append(joint_prob)
            combo_list.append(combo)

        feat_tensor = torch.tensor(np.array(combo_features), dtype=torch.float32).to(device)
        with torch.no_grad():
            yields_pred = yield_model(feat_tensor).cpu().numpy().flatten() * 100

        # 归一化后混合
        prob_arr = np.array(combo_probs)
        prob_norm = prob_arr / (prob_arr.max() + 1e-10)
        yield_norm = yields_pred / (yields_pred.max() + 1e-10)
        scores = alpha * yield_norm + (1 - alpha) * prob_norm

        best_idx = np.argmax(scores)
        best_combo = combo_list[best_idx]
        predicted_yields[i] = yields_pred[best_idx]

        for j, key in enumerate(YIELD_VISIBLE_KEYS):
            preds[key][i] = topk_indices[key][best_combo[j]]
        for key in YIELD_INVISIBLE_KEYS:
            preds[key][i] = invisible_indices[key]

    return preds, predicted_yields


# ── 评估函数 ──────────────────────────────────────────────────

def evaluate(preds, labels, true_yields=None, predicted_yields=None):
    """评估预测结果"""
    n = len(labels['anode'])
    results = {}

    # Per-condition accuracy
    acc = {}
    for key in CONDITION_KEYS:
        acc[key] = float((preds[key] == labels[key]).mean())
    results['top1_accuracy'] = acc
    results['avg_top1'] = float(np.mean(list(acc.values())))

    # Yield-visible vs invisible accuracy
    vis_acc = np.mean([acc[k] for k in YIELD_VISIBLE_KEYS])
    invis_acc = np.mean([acc[k] for k in YIELD_INVISIBLE_KEYS])
    results['visible_avg_top1'] = float(vis_acc)
    results['invisible_avg_top1'] = float(invis_acc)

    # Joint match
    joint = np.ones(n, dtype=bool)
    match_count = np.zeros(n)
    for key in CONDITION_KEYS:
        correct = (preds[key] == labels[key])
        joint &= correct
        match_count += correct.astype(float)

    results['joint_exact_match'] = float(joint.mean())
    results['partial_6_7'] = float((match_count >= 6).mean())
    results['partial_5_7'] = float((match_count >= 5).mean())
    results['avg_correct'] = float(match_count.mean())

    # Yield-visible joint (5/5)
    vis_joint = np.ones(n, dtype=bool)
    for key in YIELD_VISIBLE_KEYS:
        vis_joint &= (preds[key] == labels[key])
    results['visible_joint_5_5'] = float(vis_joint.mean())

    # Yield correlation
    if true_yields is not None and predicted_yields is not None:
        corr = np.corrcoef(true_yields, predicted_yields)[0, 1]
        results['yield_correlation'] = float(corr) if not np.isnan(corr) else 0.0
        results['avg_predicted_yield'] = float(predicted_yields.mean())
        results['avg_true_yield'] = float(true_yields.mean())

        # 当条件全对时，预测产率 vs 真实产率
        if joint.sum() > 0:
            correct_mask = joint
            results['yield_corr_when_correct'] = float(
                np.corrcoef(true_yields[correct_mask], predicted_yields[correct_mask])[0, 1]
            ) if correct_mask.sum() > 2 else None

    return results


# ── 输出 ──────────────────────────────────────────────────────

def print_comparison(all_results, labels):
    """打印对比表格"""
    W = 110

    # 1. Overall summary
    print(f"\n{'=' * W}")
    print(f"  YIELD RANKING EVALUATION — OVERALL RESULTS")
    print(f"{'=' * W}")

    header = (f"{'Strategy':<25} {'AvgTop1':>8} {'VisTop1':>8} {'InvTop1':>8} "
              f"{'Joint7/7':>9} {'Vis5/5':>8} {'AvgCorr':>8} {'PredYld':>8}")
    print(header)
    print("-" * len(header))

    baseline_avg = None
    for name, res in all_results.items():
        if baseline_avg is None:
            baseline_avg = res['avg_top1']
        pred_yld = f"{res.get('avg_predicted_yield', 0):.1f}" if 'avg_predicted_yield' in res else "  N/A"
        print(f"{name:<25} {res['avg_top1']:>8.4f} {res['visible_avg_top1']:>8.4f} "
              f"{res['invisible_avg_top1']:>8.4f} {res['joint_exact_match']:>9.4f} "
              f"{res['visible_joint_5_5']:>8.4f} {res['avg_correct']:>8.2f} {pred_yld:>8}")

    # 2. Per-condition breakdown
    print(f"\n{'=' * W}")
    print(f"  PER-CONDITION TOP-1 ACCURACY")
    print(f"{'=' * W}")

    header2 = f"{'Strategy':<25}" + "".join(f"{k:>12}" for k in CONDITION_KEYS) + f"{'AVG':>8}"
    print(header2)
    print("-" * len(header2))

    for name, res in all_results.items():
        row = f"{name:<25}"
        for key in CONDITION_KEYS:
            row += f"{res['top1_accuracy'][key]:>12.4f}"
        row += f"{res['avg_top1']:>8.4f}"
        print(row)

    # 3. Delta vs M1_TOP1
    print(f"\n{'=' * W}")
    print(f"  DELTA vs M1_TOP1 BASELINE")
    print(f"{'=' * W}")

    base = all_results.get('M1_TOP1')
    if base:
        header3 = f"{'Strategy':<25}" + "".join(f"{k:>12}" for k in CONDITION_KEYS) + f"{'ΔAvg':>8} {'ΔJoint':>8}"
        print(header3)
        print("-" * len(header3))

        for name, res in all_results.items():
            if name == 'M1_TOP1':
                continue
            row = f"{name:<25}"
            for key in CONDITION_KEYS:
                delta = res['top1_accuracy'][key] - base['top1_accuracy'][key]
                row += f"{delta:>+12.4f}"
            d_avg = res['avg_top1'] - base['avg_top1']
            d_joint = res['joint_exact_match'] - base['joint_exact_match']
            row += f"{d_avg:>+8.4f} {d_joint:>+8.4f}"
            print(row)

    # 4. Yield correlation analysis
    print(f"\n{'=' * W}")
    print(f"  YIELD PREDICTION ANALYSIS")
    print(f"{'=' * W}")

    for name, res in all_results.items():
        if 'yield_correlation' in res:
            print(f"  {name}:")
            print(f"    Predicted yield (avg):    {res['avg_predicted_yield']:.1f}%")
            print(f"    True yield (avg):         {res['avg_true_yield']:.1f}%")
            print(f"    Correlation (all):        {res['yield_correlation']:.4f}")
            if res.get('yield_corr_when_correct') is not None:
                print(f"    Correlation (7/7 correct):{res['yield_corr_when_correct']:.4f}")
            print()


# ── Main ──────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Yield Ranking Evaluation')
    parser.add_argument('--device', type=str, default=None)
    parser.add_argument('--yield_ckpt', type=str, default=None,
                        help='Override yield model checkpoint path')
    parser.add_argument('--save_dir', type=str, default='eval_results/yield_ranking')
    args = parser.parse_args()

    device = args.device or ('cuda' if torch.cuda.is_available() else 'cpu')
    save_dir = project_root / args.save_dir
    save_dir.mkdir(parents=True, exist_ok=True)

    print(f"Device: {device}")
    print(f"\n{'=' * 80}")
    print(f"  LOADING DATA & MODELS")
    print(f"{'=' * 80}")

    # 加载数据
    train_data, test_data = load_data_and_split(device)
    vocab, idx_to_smiles = load_vocab()
    test_info = extract_labels(test_data)
    n = len(test_data)
    print(f"  Test reactions: {n}")
    print(f"  Yield range: {test_info['yields'].min():.1f} - {test_info['yields'].max():.1f}, "
          f"mean={test_info['yields'].mean():.1f}")

    # 加载模型
    cond_model, cond_type, cond_input_dim, vocab_sizes = load_condition_model(device)
    yield_model, yield_input_dim = load_yield_model(device, ckpt_override=args.yield_ckpt)
    xtb_lookup, xtb_dim = load_xtb_lookup(yield_input_dim)

    # 预缓存指纹
    fp_cache = FingerprintCache()
    fp_cache.preload_vocab(idx_to_smiles)

    # M1 推理
    print("\nRunning Model 1 inference...")
    m1_logits = get_m1_logits(cond_model, test_info['reaction_fps'], cond_input_dim, device, test_data=test_data)

    labels = test_info['labels']
    true_yields = test_info['yields']

    # ── 运行各策略 ──
    all_results = {}

    # Strategy 1: M1 TOP-1 (baseline)
    print(f"\n{'=' * 80}")
    print(f"  STRATEGY 1: M1_TOP1 (baseline)")
    print(f"{'=' * 80}")
    t0 = time.time()
    preds_top1 = strategy_m1_top1(m1_logits)
    # 也计算 baseline 预测产率（用 M1 top-1 的条件）
    print("  Computing M1_TOP1 predicted yields...")
    m1_yields = np.zeros(n)
    batch_feats = []
    for i in range(n):
        sol_idx = int(preds_top1['solvent'][i])
        elec_idx = int(preds_top1['electrolyte'][i])
        sol_smiles = idx_to_smiles['solvent'].get(sol_idx, '')
        elec_smiles = idx_to_smiles['electrolyte'].get(elec_idx, '')
        feat = build_yield_features(
            test_info['reaction_fps'][i],
            fp_cache.get(sol_smiles),
            fp_cache.get(elec_smiles),
            preds_top1['anode'][i],
            preds_top1['cathode'][i],
            preds_top1['cell_type'][i],
            None, xtb_dim,
        )
        batch_feats.append(feat)

    feat_tensor = torch.tensor(np.array(batch_feats), dtype=torch.float32).to(device)
    with torch.no_grad():
        m1_yields = yield_model(feat_tensor).cpu().numpy().flatten() * 100

    res = evaluate(preds_top1, labels, true_yields, m1_yields)
    res['time_sec'] = time.time() - t0
    all_results['M1_TOP1'] = res
    print(f"  AvgTop1={res['avg_top1']:.4f}  Joint={res['joint_exact_match']:.4f}  "
          f"PredYield={res.get('avg_predicted_yield', 0):.1f}%  Time={res['time_sec']:.1f}s")

    # Strategy 2: M1 TOP-3 by joint probability
    print(f"\n{'=' * 80}")
    print(f"  STRATEGY 2: M1_TOP3_PROB (joint probability ranking)")
    print(f"{'=' * 80}")
    t0 = time.time()
    preds_prob = strategy_m1_topk_prob(m1_logits, k=3)
    res = evaluate(preds_prob, labels, true_yields)
    res['time_sec'] = time.time() - t0
    all_results['M1_TOP3_PROB'] = res
    print(f"  AvgTop1={res['avg_top1']:.4f}  Joint={res['joint_exact_match']:.4f}  "
          f"Time={res['time_sec']:.1f}s")

    # Strategy 3: M1 TOP-3 by yield
    print(f"\n{'=' * 80}")
    print(f"  STRATEGY 3: M1_TOP3_YIELD (yield ranking, k=3)")
    print(f"{'=' * 80}")
    t0 = time.time()
    preds_y3, yields_y3 = strategy_m1_topk_yield(
        m1_logits, k=3, yield_model=yield_model, yield_input_dim=yield_input_dim,
        device=device, test_info=test_info, idx_to_smiles=idx_to_smiles,
        fp_cache=fp_cache, xtb_lookup=xtb_lookup, xtb_dim=xtb_dim,
    )
    res = evaluate(preds_y3, labels, true_yields, yields_y3)
    res['time_sec'] = time.time() - t0
    all_results['M1_TOP3_YIELD'] = res
    print(f"  AvgTop1={res['avg_top1']:.4f}  Joint={res['joint_exact_match']:.4f}  "
          f"PredYield={res.get('avg_predicted_yield', 0):.1f}%  Time={res['time_sec']:.1f}s")

    # Strategy 4: M1 TOP-5 by yield (only visible conditions)
    print(f"\n{'=' * 80}")
    print(f"  STRATEGY 4: M1_TOP5_YIELD (yield ranking, k=5)")
    print(f"{'=' * 80}")
    t0 = time.time()
    preds_y5, yields_y5 = strategy_m1_topk_yield(
        m1_logits, k=5, yield_model=yield_model, yield_input_dim=yield_input_dim,
        device=device, test_info=test_info, idx_to_smiles=idx_to_smiles,
        fp_cache=fp_cache, xtb_lookup=xtb_lookup, xtb_dim=xtb_dim,
    )
    res = evaluate(preds_y5, labels, true_yields, yields_y5)
    res['time_sec'] = time.time() - t0
    all_results['M1_TOP5_YIELD'] = res
    print(f"  AvgTop1={res['avg_top1']:.4f}  Joint={res['joint_exact_match']:.4f}  "
          f"PredYield={res.get('avg_predicted_yield', 0):.1f}%  Time={res['time_sec']:.1f}s")

    # Strategy 5: M1 TOP-3 combined (α=0.5)
    print(f"\n{'=' * 80}")
    print(f"  STRATEGY 5: M1_TOP3_COMBINED (0.5*yield + 0.5*prob)")
    print(f"{'=' * 80}")
    t0 = time.time()
    preds_c3, yields_c3 = strategy_m1_topk_combined(
        m1_logits, k=3, yield_model=yield_model, yield_input_dim=yield_input_dim,
        device=device, test_info=test_info, idx_to_smiles=idx_to_smiles,
        fp_cache=fp_cache, xtb_lookup=xtb_lookup, xtb_dim=xtb_dim,
        alpha=0.5,
    )
    res = evaluate(preds_c3, labels, true_yields, yields_c3)
    res['time_sec'] = time.time() - t0
    all_results['M1_TOP3_COMBINED'] = res
    print(f"  AvgTop1={res['avg_top1']:.4f}  Joint={res['joint_exact_match']:.4f}  "
          f"PredYield={res.get('avg_predicted_yield', 0):.1f}%  Time={res['time_sec']:.1f}s")

    # Strategy 6: M1 TOP-3 combined (α=0.3, yield偏低权重)
    print(f"\n{'=' * 80}")
    print(f"  STRATEGY 6: M1_TOP3_COMB_A03 (0.3*yield + 0.7*prob)")
    print(f"{'=' * 80}")
    t0 = time.time()
    preds_c3b, yields_c3b = strategy_m1_topk_combined(
        m1_logits, k=3, yield_model=yield_model, yield_input_dim=yield_input_dim,
        device=device, test_info=test_info, idx_to_smiles=idx_to_smiles,
        fp_cache=fp_cache, xtb_lookup=xtb_lookup, xtb_dim=xtb_dim,
        alpha=0.3,
    )
    res = evaluate(preds_c3b, labels, true_yields, yields_c3b)
    res['time_sec'] = time.time() - t0
    all_results['M1_TOP3_COMB_A03'] = res
    print(f"  AvgTop1={res['avg_top1']:.4f}  Joint={res['joint_exact_match']:.4f}  "
          f"PredYield={res.get('avg_predicted_yield', 0):.1f}%  Time={res['time_sec']:.1f}s")

    # ── 打印对比 ──
    print_comparison(all_results, labels)

    # ── 额外分析: 产率模型是否选了"更好"的条件? ──
    print(f"\n{'=' * 110}")
    print(f"  ANALYSIS: Does yield ranking select 'better' conditions?")
    print(f"{'=' * 110}")

    # 比较: 选 M1_TOP1 正确 vs 选 YIELD 正确的反应
    top1_joint = np.ones(n, dtype=bool)
    y3_joint = np.ones(n, dtype=bool)
    for key in CONDITION_KEYS:
        top1_joint &= (preds_top1[key] == labels[key])
        y3_joint &= (preds_y3[key] == labels[key])

    top1_right_y3_wrong = top1_joint & ~y3_joint
    y3_right_top1_wrong = y3_joint & ~top1_joint
    both_right = top1_joint & y3_joint
    both_wrong = ~top1_joint & ~y3_joint

    print(f"\n  M1_TOP1 vs M1_TOP3_YIELD (joint 7/7):")
    print(f"    Both correct:           {both_right.sum():>4}")
    print(f"    TOP1 correct, YIELD wrong: {top1_right_y3_wrong.sum():>4}")
    print(f"    YIELD correct, TOP1 wrong: {y3_right_top1_wrong.sum():>4}")
    print(f"    Both wrong:             {both_wrong.sum():>4}")

    # Per-condition: how often does yield flip from correct→wrong or wrong→correct?
    print(f"\n  Per-condition flips (M1_TOP3_YIELD vs M1_TOP1):")
    print(f"  {'Condition':<15} {'TOP1→YIELD':>12} {'YIELD→TOP1':>12} {'Net':>8}")
    print(f"  {'-'*47}")
    for key in CONDITION_KEYS:
        top1_ok = (preds_top1[key] == labels[key])
        y3_ok = (preds_y3[key] == labels[key])
        gained = (~top1_ok & y3_ok).sum()
        lost = (top1_ok & ~y3_ok).sum()
        print(f"  {key:<15} {f'+{gained}':>12} {f'-{lost}':>12} {f'{gained-lost:+d}':>8}")

    # ── 保存结果 ──
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = save_dir / f"yield_ranking_{timestamp}.json"

    # Make serializable
    def to_serializable(obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, dict):
            return {k: to_serializable(v) for k, v in obj.items()}
        return obj

    with open(save_path, 'w') as f:
        json.dump(to_serializable(all_results), f, indent=2, ensure_ascii=False)
    print(f"\n  Results saved to: {save_path}")

    print(f"\n{'=' * 80}")
    print(f"  Evaluation complete.")
    print(f"{'=' * 80}")


if __name__ == "__main__":
    main()
