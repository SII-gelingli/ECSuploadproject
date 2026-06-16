"""
评估脚本：全面评估 ConditionRecommender (Model 1) 和 CategoricalCVAE (Model 2)

指标体系:
  1. Top-k Accuracy (k=1,3,5,10) — 每个条件 head 分别评估
  2. Per-class Precision / Recall / F1 — 每个条件类别
  3. Confusion Matrix — 每个 head 保存为 numpy
  4. Baselines — Random / Most-frequent 对比
  5. CVAE 专有: Joint Exact Match, Partial Match, Diversity, Novelty
  6. 汇总: macro/weighted 平均

数据划分: 与训练完全一致 (random_state=42, 80/10/10)

用法:
    cd yield_prediction
    python scripts/eval_condition_models.py
    python scripts/eval_condition_models.py --device cuda
    python scripts/eval_condition_models.py --config configs/config.yaml --save_dir eval_results
"""
import os
import sys
import argparse
import json
import yaml
import time
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime

import torch
import numpy

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.append(LOCAL_PACKAGES)

import torch.nn.functional as F
from torch.utils.data import DataLoader
from tqdm import tqdm
import numpy as np

# 项目路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.data_processor import ReactionDataProcessor
from utils.feature_extractor import MolecularFeatureExtractor
from models.condition_recommender import (
    ConditionRecommender, ConditionRecommenderXTB,
    DualTowerConditionRecommender, CompactConditionRecommender,
)
from models.condition_cvae import CategoricalCVAE
from utils.electrode_normalizer import electrode_to_id, id_to_electrode, NUM_ELECTRODE_TYPES
from scripts.train_condition import ConditionDataset

# ── 常量 ──────────────────────────────────────────────────────
CONDITION_KEYS = ['anode', 'cathode', 'cell_type', 'electrolyte',
                  'solvent', 'reagent', 'catalyst']
TOP_KS = [1, 3, 5, 10]

CELL_TYPE_NAMES = {
    0: 'undivided', 1: 'divided', 2: 'flow', 3: 'sealed', 4: 'other', 5: 'unknown'
}


# ── 工具函数 ──────────────────────────────────────────────────

def build_label_names(vocab: dict) -> dict:
    """构建 index → 名称 映射（用于可读性输出）"""
    label_names = {}

    # 电极: id_to_electrode
    label_names['anode'] = {i: id_to_electrode(i) for i in range(NUM_ELECTRODE_TYPES)}
    label_names['cathode'] = {i: id_to_electrode(i) for i in range(NUM_ELECTRODE_TYPES)}

    # 电解池
    label_names['cell_type'] = CELL_TYPE_NAMES

    # SMILES 类条件: vocab index → SMILES
    for key in ['electrolyte', 'solvent', 'reagent', 'catalyst']:
        inv = {v: k for k, v in vocab.get(key, {}).items()}
        inv[0] = '<UNK>'
        label_names[key] = inv

    return label_names


def compute_class_metrics(y_true: np.ndarray, y_pred: np.ndarray, num_classes: int):
    """计算 per-class precision / recall / F1 + macro / weighted 平均"""
    # 构建 confusion matrix
    cm = np.zeros((num_classes, num_classes), dtype=np.int64)
    for t, p in zip(y_true, y_pred):
        cm[t, p] += 1

    precision = np.zeros(num_classes)
    recall = np.zeros(num_classes)
    f1 = np.zeros(num_classes)
    support = np.zeros(num_classes)

    for c in range(num_classes):
        tp = cm[c, c]
        fp = cm[:, c].sum() - tp
        fn = cm[c, :].sum() - tp
        support[c] = cm[c, :].sum()

        precision[c] = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall[c] = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1[c] = 2 * precision[c] * recall[c] / (precision[c] + recall[c]) \
            if (precision[c] + recall[c]) > 0 else 0.0

    total = support.sum()
    macro_p = precision[support > 0].mean() if (support > 0).any() else 0.0
    macro_r = recall[support > 0].mean() if (support > 0).any() else 0.0
    macro_f1 = f1[support > 0].mean() if (support > 0).any() else 0.0

    weighted_p = (precision * support).sum() / total if total > 0 else 0.0
    weighted_r = (recall * support).sum() / total if total > 0 else 0.0
    weighted_f1 = (f1 * support).sum() / total if total > 0 else 0.0

    return {
        'confusion_matrix': cm,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'support': support,
        'macro_precision': float(macro_p),
        'macro_recall': float(macro_r),
        'macro_f1': float(macro_f1),
        'weighted_precision': float(weighted_p),
        'weighted_recall': float(weighted_r),
        'weighted_f1': float(weighted_f1),
    }


# ── 数据加载 ──────────────────────────────────────────────────

def load_test_data(config: dict, device: str = 'cpu'):
    """加载数据并返回 test DataLoader（与训练完全一致的 split）"""
    processor = ReactionDataProcessor(
        yield_data_dir=config['data']['yield_data_dir'],
        smiles_data_path=config['data']['smiles_data_path'],
    )
    reactions = processor.load_yield_data()

    # 构建词汇表（仅基于有产率的反应，与训练一致）
    vocab_reactions = [r for r in reactions if r.get('yield_value', 0) > 0]
    electrolytes, solvents, reagents, catalysts = Counter(), Counter(), Counter(), Counter()
    for rxn in vocab_reactions:
        echem = rxn.get('electrochemistry_params', {})
        elec = echem.get('electrolyte', '')
        if elec:
            electrolytes[elec] += 1
        for s in rxn.get('solvents', []):
            sm = s.get('smiles', '')
            if sm:
                solvents[sm] += 1
        for r in rxn.get('reagents', []):
            sm = r.get('smiles', '')
            if sm:
                reagents[sm] += 1
        for c in rxn.get('catalysts', []):
            sm = c.get('smiles', '')
            if sm:
                catalysts[sm] += 1

    electrolyte_vocab = {e: i + 1 for i, (e, _) in enumerate(electrolytes.most_common())}
    solvent_vocab = {s: i + 1 for i, (s, _) in enumerate(solvents.most_common())}
    reagent_vocab = {r: i + 1 for i, (r, _) in enumerate(reagents.most_common())}
    catalyst_vocab = {c: i + 1 for i, (c, _) in enumerate(catalysts.most_common())}

    vocab = {
        'electrolyte': electrolyte_vocab,
        'solvent': solvent_vocab,
        'reagent': reagent_vocab,
        'catalyst': catalyst_vocab,
    }

    # 与训练一致的 split
    from sklearn.model_selection import train_test_split
    train_rxn, temp_rxn = train_test_split(reactions, test_size=0.2, random_state=42)
    val_rxn, test_rxn = train_test_split(temp_rxn, test_size=0.5, random_state=42)

    fp_size = config['model']['mol_encoder']['fingerprint_size']
    mol_extractor = MolecularFeatureExtractor(fp_size)

    # xTB 特征
    xtb_lookup = None
    xtb_config = config.get('xtb', {})
    if xtb_config.get('use_xtb', False):
        from utils.xtb_features import XTBFeatureLookup
        xtb_lookup = XTBFeatureLookup(xtb_config.get('csv_path'))

    # 训练集统计量（用于归一化）
    train_dataset = ConditionDataset(
        train_rxn, mol_extractor,
        electrolyte_vocab, solvent_vocab, reagent_vocab,
        catalyst_vocab=catalyst_vocab,
        xtb_lookup=xtb_lookup,
    )
    xtb_stats = train_dataset.compute_xtb_stats()

    # 测试集
    test_dataset = ConditionDataset(
        test_rxn, mol_extractor,
        electrolyte_vocab, solvent_vocab, reagent_vocab,
        catalyst_vocab=catalyst_vocab,
        xtb_lookup=xtb_lookup, xtb_stats=xtb_stats,
    )

    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

    # 训练集标签分布（用于 most-frequent baseline）
    train_label_dist = {}
    for key in CONDITION_KEYS:
        labels = [d[key] for d in train_dataset.data]
        counter = Counter(labels)
        most_common_label = counter.most_common(1)[0][0]
        train_label_dist[key] = {
            'most_common': most_common_label,
            'distribution': dict(counter),
        }

    info = {
        'train_size': len(train_dataset),
        'test_size': len(test_dataset),
        'vocab_sizes': {
            'anode': NUM_ELECTRODE_TYPES,
            'cathode': NUM_ELECTRODE_TYPES,
            'cell_type': 6,
            'electrolyte': len(electrolyte_vocab) + 1,
            'solvent': len(solvent_vocab) + 1,
            'reagent': len(reagent_vocab) + 1,
            'catalyst': len(catalyst_vocab) + 1,
        },
        'train_label_dist': train_label_dist,
    }

    return test_loader, vocab, info


# ── 模型加载 ──────────────────────────────────────────────────

def load_condition_model(checkpoint_path: str, device: str = 'cpu'):
    """从 checkpoint 加载 Model 1"""
    checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=False)
    state_dict = checkpoint['model_state_dict']

    if 'fp_encoder.0.weight' in state_dict:
        fp_dim = state_dict['fp_encoder.0.weight'].shape[1]
        xtb_dim = state_dict['xtb_encoder.0.weight'].shape[1]
        hidden_dim = state_dict['fusion.0.weight'].shape[0]
        model = ConditionRecommenderXTB(
            fp_dim=fp_dim, xtb_dim=xtb_dim, hidden_dim=hidden_dim,
            num_anode=state_dict['anode_head.weight'].shape[0],
            num_cathode=state_dict['cathode_head.weight'].shape[0],
            num_cell_type=state_dict['cell_type_head.weight'].shape[0],
            num_electrolyte=state_dict['electrolyte_head.weight'].shape[0],
            num_solvent=state_dict['solvent_head.weight'].shape[0],
            num_reagent=state_dict['reagent_head.weight'].shape[0],
            num_catalyst=state_dict['catalyst_head.weight'].shape[0],
        ).to(device)
        model_type = 'ConditionRecommenderXTB'
    elif 'reaction_encoder.0.weight' in state_dict:
        reaction_dim = state_dict['reaction_encoder.0.weight'].shape[1]
        hidden_dim = state_dict['reaction_encoder.0.weight'].shape[0]
        model = ConditionRecommender(
            reaction_dim=reaction_dim, hidden_dim=hidden_dim,
            num_anode_materials=state_dict['anode_head.weight'].shape[0],
            num_cathode_materials=state_dict['cathode_head.weight'].shape[0],
            num_cell_types=state_dict['cell_type_head.weight'].shape[0],
            num_electrolytes=state_dict['electrolyte_head.weight'].shape[0],
            num_solvents=state_dict['solvent_head.weight'].shape[0],
            num_reagents=state_dict['reagent_head.weight'].shape[0],
            num_catalysts=state_dict['catalyst_head.weight'].shape[0],
        ).to(device)
        model_type = 'ConditionRecommender'
    else:
        raise ValueError("Unknown condition model architecture in checkpoint")

    model.load_state_dict(state_dict)
    model.eval()
    return model, model_type, checkpoint.get('accuracy', {})


def load_cvae_model(checkpoint_path: str, device: str = 'cpu'):
    """从 checkpoint 加载 Model 2"""
    checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=False)
    state_dict = checkpoint['model_state_dict']

    reaction_dim = state_dict['reaction_encoder.0.weight'].shape[1]
    model = CategoricalCVAE(
        reaction_dim=reaction_dim, repr_dim=256, latent_dim=64,
        num_anode_materials=state_dict['anode_head.weight'].shape[0],
        num_cathode_materials=state_dict['cathode_head.weight'].shape[0],
        num_cell_types=state_dict['cell_type_head.weight'].shape[0],
        num_electrolytes=state_dict['electrolyte_head.weight'].shape[0],
        num_solvents=state_dict['solvent_head.weight'].shape[0],
        num_reagents=state_dict['reagent_head.weight'].shape[0],
        num_catalysts=state_dict['catalyst_head.weight'].shape[0],
    ).to(device)
    model.load_state_dict(state_dict)
    model.eval()
    return model, checkpoint.get('accuracy', {}), checkpoint.get('avg_accuracy', 0)


# ── 评估函数 ──────────────────────────────────────────────────

def get_logits_key(model_type: str, key: str) -> str:
    """不同模型输出 key 的映射"""
    if model_type == 'ConditionRecommenderXTB':
        return key  # 'anode', 'cathode', ...
    else:
        return f'{key}_logits'  # 'anode_logits', ...


def evaluate_classifier(model, model_type: str, test_loader, device: str,
                        info: dict, label_names: dict):
    """
    全面评估分类模型 (Model 1)

    Returns:
        results dict
    """
    model.eval()

    # 收集所有预测和标签
    all_labels = {key: [] for key in CONDITION_KEYS}
    all_logits = {key: [] for key in CONDITION_KEYS}

    with torch.no_grad():
        for batch in tqdm(test_loader, desc="Evaluating Model 1"):
            reaction_fp = batch['reaction_fp'].to(device)
            predictions = model(reaction_fp)

            for key in CONDITION_KEYS:
                logits_key = get_logits_key(model_type, key)
                all_logits[key].append(predictions[logits_key].cpu())
                all_labels[key].append(batch[key])

    # 拼接
    for key in CONDITION_KEYS:
        all_logits[key] = torch.cat(all_logits[key], dim=0)
        all_labels[key] = torch.cat(all_labels[key], dim=0)

    total = all_labels['anode'].size(0)
    results = {'total_samples': total, 'per_condition': {}}

    # ── 1. Top-k Accuracy ──
    topk_results = {}
    for key in CONDITION_KEYS:
        logits = all_logits[key]
        labels = all_labels[key]
        num_cls = logits.size(-1)

        topk_acc = {}
        for k in TOP_KS:
            real_k = min(k, num_cls)
            top_k_preds = logits.topk(real_k, dim=-1).indices
            hit = (top_k_preds == labels.unsqueeze(1)).any(dim=1)
            topk_acc[k] = float(hit.float().mean().item())

        topk_results[key] = topk_acc

    results['topk_accuracy'] = topk_results

    # 平均 top-k
    results['avg_topk'] = {}
    for k in TOP_KS:
        results['avg_topk'][k] = float(
            np.mean([topk_results[key][k] for key in CONDITION_KEYS])
        )

    # ── 2. Per-class Precision / Recall / F1 + Confusion Matrix ──
    for key in CONDITION_KEYS:
        logits = all_logits[key]
        labels = all_labels[key].numpy()
        preds = logits.argmax(dim=-1).numpy()
        num_cls = info['vocab_sizes'][key]

        metrics = compute_class_metrics(labels, preds, num_cls)

        # 转为可序列化格式
        names = label_names.get(key, {})
        per_class = []
        for c in range(num_cls):
            if metrics['support'][c] > 0:
                per_class.append({
                    'class_id': c,
                    'name': names.get(c, f'class_{c}'),
                    'precision': float(metrics['precision'][c]),
                    'recall': float(metrics['recall'][c]),
                    'f1': float(metrics['f1'][c]),
                    'support': int(metrics['support'][c]),
                })

        results['per_condition'][key] = {
            'per_class': per_class,
            'macro_precision': metrics['macro_precision'],
            'macro_recall': metrics['macro_recall'],
            'macro_f1': metrics['macro_f1'],
            'weighted_precision': metrics['weighted_precision'],
            'weighted_recall': metrics['weighted_recall'],
            'weighted_f1': metrics['weighted_f1'],
            'num_classes_with_support': int((metrics['support'] > 0).sum()),
            'confusion_matrix': metrics['confusion_matrix'],  # numpy, 保存时单独处理
        }

    # ── 3. Baselines ──
    train_dist = info['train_label_dist']
    baselines = {}
    for key in CONDITION_KEYS:
        labels = all_labels[key].numpy()
        num_cls = info['vocab_sizes'][key]

        # Most-frequent baseline
        mf_label = train_dist[key]['most_common']
        mf_acc = float((labels == mf_label).mean())

        # Random baseline (均匀)
        random_acc = 1.0 / num_cls

        # Random weighted baseline (按训练集分布)
        dist = train_dist[key]['distribution']
        total_train = sum(dist.values())
        weighted_random = sum(
            (count / total_train) * (count / total_train)
            for count in dist.values()
        )

        baselines[key] = {
            'random_uniform': float(random_acc),
            'random_weighted': float(weighted_random),
            'most_frequent': float(mf_acc),
            'model_top1': topk_results[key][1],
            'lift_over_mf': float(topk_results[key][1] - mf_acc),
        }

    results['baselines'] = baselines

    return results


def evaluate_cvae(model, test_loader, device: str, info: dict, label_names: dict,
                  num_generate_samples: int = 10, temperature: float = 1.0):
    """
    全面评估 CVAE 模型 (Model 2)

    额外指标:
      - z=0 确定性 top-k accuracy (与 Model 1 对比)
      - Joint Exact Match: 7 个条件全部正确的比例
      - Partial Match: >=5/7, >=6/7 的比例
      - 采样 diversity: 不同方案数 / 采样数
      - Novelty: 生成方案中不在训练集的比例 (近似)
    """
    model.eval()

    # ── Part A: z=0 确定性评估（与 Model 1 同口径）──
    all_labels = {key: [] for key in CONDITION_KEYS}
    all_logits = {key: [] for key in CONDITION_KEYS}

    with torch.no_grad():
        for batch in tqdm(test_loader, desc="Evaluating CVAE (z=0)"):
            reaction_fp = batch['reaction_fp'].to(device)
            predictions = model.recommend(reaction_fp)

            for key in CONDITION_KEYS:
                all_logits[key].append(predictions[f'{key}_logits'].cpu())
                all_labels[key].append(batch[key])

    for key in CONDITION_KEYS:
        all_logits[key] = torch.cat(all_logits[key], dim=0)
        all_labels[key] = torch.cat(all_labels[key], dim=0)

    total = all_labels['anode'].size(0)

    # Top-k accuracy (z=0)
    topk_results = {}
    for key in CONDITION_KEYS:
        logits = all_logits[key]
        labels = all_labels[key]
        num_cls = logits.size(-1)
        topk_acc = {}
        for k in TOP_KS:
            real_k = min(k, num_cls)
            top_k_preds = logits.topk(real_k, dim=-1).indices
            hit = (top_k_preds == labels.unsqueeze(1)).any(dim=1)
            topk_acc[k] = float(hit.float().mean().item())
        topk_results[key] = topk_acc

    avg_topk = {}
    for k in TOP_KS:
        avg_topk[k] = float(np.mean([topk_results[key][k] for key in CONDITION_KEYS]))

    # Per-class metrics (z=0)
    per_condition = {}
    for key in CONDITION_KEYS:
        logits = all_logits[key]
        labels = all_labels[key].numpy()
        preds = logits.argmax(dim=-1).numpy()
        num_cls = info['vocab_sizes'][key]
        metrics = compute_class_metrics(labels, preds, num_cls)
        names = label_names.get(key, {})
        per_class = []
        for c in range(num_cls):
            if metrics['support'][c] > 0:
                per_class.append({
                    'class_id': c,
                    'name': names.get(c, f'class_{c}'),
                    'precision': float(metrics['precision'][c]),
                    'recall': float(metrics['recall'][c]),
                    'f1': float(metrics['f1'][c]),
                    'support': int(metrics['support'][c]),
                })
        per_condition[key] = {
            'per_class': per_class,
            'macro_f1': metrics['macro_f1'],
            'weighted_f1': metrics['weighted_f1'],
            'confusion_matrix': metrics['confusion_matrix'],
        }

    # ── Part B: Joint Match (z=0 确定性) ──
    all_preds = {}
    all_gt = {}
    for key in CONDITION_KEYS:
        all_preds[key] = all_logits[key].argmax(dim=-1).numpy()
        all_gt[key] = all_labels[key].numpy()

    # exact match: 7个全对
    exact_match = np.ones(total, dtype=bool)
    for key in CONDITION_KEYS:
        exact_match &= (all_preds[key] == all_gt[key])
    joint_exact_match = float(exact_match.mean())

    # partial match
    match_count = np.zeros(total)
    for key in CONDITION_KEYS:
        match_count += (all_preds[key] == all_gt[key]).astype(float)

    partial_5 = float((match_count >= 5).mean())
    partial_6 = float((match_count >= 6).mean())
    avg_match_count = float(match_count.mean())

    # ── Part C: 生成多样性 (采样评估) ──
    diversity_scores = []
    novelty_scores = []

    # 取一个子集做采样评估（避免太慢）
    eval_samples = min(200, total)
    sample_indices = np.random.RandomState(42).choice(total, eval_samples, replace=False)

    with torch.no_grad():
        for idx in tqdm(sample_indices, desc="Evaluating CVAE diversity"):
            # 取单条反应
            for batch in test_loader:
                # 找到这条数据的 batch 和 offset
                break
            # 直接从所有数据中重构
            # 用 all_logits 中的 reaction_fp 会丢失，改用重新遍历
            pass

    # 更高效的做法：直接遍历 test_loader 做采样
    all_reaction_fps = []
    with torch.no_grad():
        for batch in test_loader:
            all_reaction_fps.append(batch['reaction_fp'])
    all_reaction_fps = torch.cat(all_reaction_fps, dim=0)

    with torch.no_grad():
        for idx in tqdm(sample_indices, desc="Evaluating CVAE diversity"):
            fp = all_reaction_fps[idx:idx+1].to(device)
            samples = model.generate(fp, num_samples=num_generate_samples, temperature=temperature)

            # 收集生成的条件组合
            schemes = set()
            for s in samples:
                scheme = tuple(s['labels'][key].item() for key in CONDITION_KEYS)
                schemes.add(scheme)

            diversity_scores.append(len(schemes) / num_generate_samples)

    avg_diversity = float(np.mean(diversity_scores))

    results = {
        'total_samples': total,
        'z0_deterministic': {
            'topk_accuracy': topk_results,
            'avg_topk': avg_topk,
            'per_condition': per_condition,
        },
        'joint_match': {
            'exact_match_7_7': joint_exact_match,
            'partial_match_6_7': partial_6,
            'partial_match_5_7': partial_5,
            'avg_conditions_correct': avg_match_count,
        },
        'generation': {
            'num_samples': num_generate_samples,
            'temperature': temperature,
            'eval_reactions': eval_samples,
            'avg_diversity': avg_diversity,
        },
    }

    return results


# ── 打印函数 ──────────────────────────────────────────────────

def print_topk_table(results: dict, model_name: str):
    """打印 top-k accuracy 表格"""
    print(f"\n{'='*80}")
    print(f"  {model_name} — Top-k Accuracy")
    print(f"{'='*80}")

    header = f"{'Condition':<15}" + "".join(f"{'Top-'+str(k):>10}" for k in TOP_KS)
    print(header)
    print("-" * len(header))

    topk = results['topk_accuracy'] if 'topk_accuracy' in results else results['z0_deterministic']['topk_accuracy']

    for key in CONDITION_KEYS:
        row = f"{key:<15}"
        for k in TOP_KS:
            row += f"{topk[key][k]:>10.3f}"
        print(row)

    avg = results.get('avg_topk') or results.get('z0_deterministic', {}).get('avg_topk', {})
    row = f"{'AVERAGE':<15}"
    for k in TOP_KS:
        row += f"{avg[k]:>10.3f}"
    print("-" * len(header))
    print(row)


def print_baseline_comparison(results: dict):
    """打印 baseline 对比"""
    baselines = results.get('baselines', {})
    if not baselines:
        return

    print(f"\n{'='*80}")
    print(f"  Baseline Comparison")
    print(f"{'='*80}")

    header = f"{'Condition':<15}{'Random':>10}{'MostFreq':>10}{'Model':>10}{'Lift':>10}"
    print(header)
    print("-" * len(header))

    for key in CONDITION_KEYS:
        b = baselines[key]
        print(f"{key:<15}{b['random_uniform']:>10.3f}{b['most_frequent']:>10.3f}"
              f"{b['model_top1']:>10.3f}{b['lift_over_mf']:>+10.3f}")


def print_class_metrics_summary(results: dict, model_name: str):
    """打印 per-condition macro/weighted F1"""
    per_cond = results.get('per_condition') or results.get('z0_deterministic', {}).get('per_condition', {})
    if not per_cond:
        return

    print(f"\n{'='*80}")
    print(f"  {model_name} — Per-Condition F1 Summary")
    print(f"{'='*80}")

    header = f"{'Condition':<15}{'Macro-F1':>12}{'Weighted-F1':>14}{'#Classes':>10}"
    print(header)
    print("-" * len(header))

    for key in CONDITION_KEYS:
        m = per_cond[key]
        n_cls = m.get('num_classes_with_support', len(m.get('per_class', [])))
        mf1 = m.get('macro_f1', 0)
        wf1 = m.get('weighted_f1', 0)
        print(f"{key:<15}{mf1:>12.3f}{wf1:>14.3f}{n_cls:>10}")


def print_cvae_joint(results: dict):
    """打印 CVAE joint match 结果"""
    jm = results.get('joint_match', {})
    gen = results.get('generation', {})

    print(f"\n{'='*80}")
    print(f"  CVAE — Joint Match & Generation Metrics")
    print(f"{'='*80}")

    print(f"  Joint Exact Match (7/7):  {jm.get('exact_match_7_7', 0):.4f}")
    print(f"  Partial Match (>=6/7):    {jm.get('partial_match_6_7', 0):.4f}")
    print(f"  Partial Match (>=5/7):    {jm.get('partial_match_5_7', 0):.4f}")
    print(f"  Avg Conditions Correct:   {jm.get('avg_conditions_correct', 0):.2f} / 7")
    print()
    print(f"  Generation Diversity:     {gen.get('avg_diversity', 0):.4f}")
    print(f"    (samples={gen.get('num_samples', 0)}, "
          f"temp={gen.get('temperature', 0)}, "
          f"eval_reactions={gen.get('eval_reactions', 0)})")


def print_model_comparison(m1_results: dict, m2_results: dict):
    """并排对比 Model 1 和 Model 2"""
    print(f"\n{'='*80}")
    print(f"  Model 1 vs Model 2 (CVAE z=0) — Top-k Accuracy Comparison")
    print(f"{'='*80}")

    m1_topk = m1_results['topk_accuracy']
    m2_topk = m2_results['z0_deterministic']['topk_accuracy']

    header = f"{'Condition':<15}" + "".join(
        f"{'M1-T'+str(k):>8}{'M2-T'+str(k):>8}{'Δ':>6}" for k in [1, 3]
    )
    print(header)
    print("-" * len(header))

    for key in CONDITION_KEYS:
        row = f"{key:<15}"
        for k in [1, 3]:
            v1 = m1_topk[key][k]
            v2 = m2_topk[key][k]
            diff = v2 - v1
            row += f"{v1:>8.3f}{v2:>8.3f}{diff:>+6.3f}"
        print(row)

    m1_avg = m1_results['avg_topk']
    m2_avg = m2_results['z0_deterministic']['avg_topk']
    row = f"{'AVERAGE':<15}"
    for k in [1, 3]:
        v1 = m1_avg[k]
        v2 = m2_avg[k]
        diff = v2 - v1
        row += f"{v1:>8.3f}{v2:>8.3f}{diff:>+6.3f}"
    print("-" * len(header))
    print(row)


# ── 结果保存 ──────────────────────────────────────────────────

def make_serializable(obj):
    """递归转换 numpy 对象为 Python 原生类型"""
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, dict):
        return {str(k): make_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [make_serializable(v) for v in obj]
    return obj


def save_results(results: dict, save_path: str):
    """保存结果为 JSON"""
    serializable = make_serializable(results)
    with open(save_path, 'w') as f:
        json.dump(serializable, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to: {save_path}")


# ── Main ──────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='评估 ConditionRecommender 和 CVAE 模型')
    parser.add_argument('--config', type=str, default='configs/config.yaml')
    parser.add_argument('--condition_ckpt', type=str,
                        default='checkpoints/condition_model/best_condition_model.pt')
    parser.add_argument('--cvae_ckpt', type=str,
                        default='checkpoints/condition_model/best_cvae_condition_model.pt')
    parser.add_argument('--device', type=str, default=None)
    parser.add_argument('--save_dir', type=str, default='eval_results')
    parser.add_argument('--cvae_samples', type=int, default=10,
                        help='CVAE 采样数量 (default: 10)')
    parser.add_argument('--cvae_temperature', type=float, default=1.0)
    parser.add_argument('--skip_model1', action='store_true')
    parser.add_argument('--skip_model2', action='store_true')
    args = parser.parse_args()

    device = args.device or ('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Device: {device}")

    # 加载配置
    config_path = project_root / args.config
    with open(config_path) as f:
        config = yaml.safe_load(f)

    # 创建输出目录
    save_dir = project_root / args.save_dir
    save_dir.mkdir(parents=True, exist_ok=True)

    # ── 加载数据 ──
    print("\n" + "="*80)
    print("  Loading test data (same split as training: seed=42, 80/10/10)")
    print("="*80)
    test_loader, vocab, info = load_test_data(config, device)
    label_names = build_label_names(vocab)

    print(f"  Train size: {info['train_size']}")
    print(f"  Test size:  {info['test_size']}")
    print(f"  Vocab sizes: {info['vocab_sizes']}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    all_results = {
        'timestamp': timestamp,
        'device': device,
        'data_info': {k: v for k, v in info.items() if k != 'train_label_dist'},
    }

    # ── Model 1: ConditionRecommender ──
    m1_results = None
    if not args.skip_model1:
        ckpt_path = project_root / args.condition_ckpt
        if ckpt_path.exists():
            print(f"\nLoading Model 1 from: {ckpt_path}")
            model1, model_type, train_acc = load_condition_model(str(ckpt_path), device)
            print(f"  Architecture: {model_type}")
            if train_acc:
                print(f"  Training best accuracy (from checkpoint): {train_acc}")

            t0 = time.time()
            m1_results = evaluate_classifier(model1, model_type, test_loader, device, info, label_names)
            elapsed = time.time() - t0
            m1_results['eval_time_sec'] = elapsed

            print_topk_table(m1_results, f"Model 1 ({model_type})")
            print_baseline_comparison(m1_results)
            print_class_metrics_summary(m1_results, f"Model 1 ({model_type})")

            all_results['model1'] = m1_results
            save_results(
                {'model_type': model_type, **m1_results},
                str(save_dir / 'model1_condition_recommender.json')
            )

            # 保存 confusion matrices (numpy)
            for key in CONDITION_KEYS:
                cm = m1_results['per_condition'][key].pop('confusion_matrix', None)
                if cm is not None:
                    np.save(str(save_dir / f'model1_cm_{key}.npy'), cm)
        else:
            print(f"\n[SKIP] Model 1 checkpoint not found: {ckpt_path}")

    # ── Model 2: CategoricalCVAE ──
    m2_results = None
    if not args.skip_model2:
        ckpt_path = project_root / args.cvae_ckpt
        if ckpt_path.exists():
            print(f"\nLoading Model 2 from: {ckpt_path}")
            model2, train_acc, train_avg = load_cvae_model(str(ckpt_path), device)
            print(f"  Architecture: CategoricalCVAE")
            if train_avg:
                print(f"  Training best avg accuracy: {train_avg:.4f}")

            t0 = time.time()
            m2_results = evaluate_cvae(
                model2, test_loader, device, info, label_names,
                num_generate_samples=args.cvae_samples,
                temperature=args.cvae_temperature,
            )
            elapsed = time.time() - t0
            m2_results['eval_time_sec'] = elapsed

            print_topk_table(m2_results, "Model 2 (CategoricalCVAE)")
            print_class_metrics_summary(m2_results, "Model 2 (CategoricalCVAE)")
            print_cvae_joint(m2_results)

            all_results['model2'] = m2_results
            save_results(
                m2_results,
                str(save_dir / 'model2_cvae.json')
            )

            # 保存 confusion matrices
            per_cond = m2_results.get('z0_deterministic', {}).get('per_condition', {})
            for key in CONDITION_KEYS:
                cm = per_cond.get(key, {}).pop('confusion_matrix', None)
                if cm is not None:
                    np.save(str(save_dir / f'model2_cm_{key}.npy'), cm)
        else:
            print(f"\n[SKIP] Model 2 checkpoint not found: {ckpt_path}")

    # ── 对比 ──
    if m1_results and m2_results:
        print_model_comparison(m1_results, m2_results)

    # ── 保存汇总 ──
    save_results(all_results, str(save_dir / f'eval_summary_{timestamp}.json'))

    print(f"\n{'='*80}")
    print(f"  Evaluation complete. Results saved in: {save_dir}")
    print(f"{'='*80}")


if __name__ == "__main__":
    main()
