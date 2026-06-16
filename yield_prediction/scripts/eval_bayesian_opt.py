"""
评估 Bayesian Optimization 模块的条件推荐能力

评估内容:
  1. BO Rerank vs M1 Top-1: 在 test set 上对比 rerank 后的 top-1 准确率
  2. BO Offline Search vs M1 Top-1: BO 搜索 N 轮后找到的条件 vs M1 argmax
  3. 迭代收敛性: suggest→observe 循环中 best yield 和 acquisition value 变化
  4. GP 校准度: predicted std vs 实际误差相关性

指标:
  - Per-condition Top-1 Accuracy (7 conditions)
  - Joint Exact Match (7/7)
  - Partial Match (>=5/7, >=6/7)
  - Average conditions correct
  - Yield prediction correlation
  - GP calibration (std vs |error|)

数据: test.pt (1064 reactions)

用法:
    cd condition_agent
    python yield_prediction/scripts/eval_bayesian_opt.py [--n-reactions 100] [--bo-iters 20]
"""
import sys
import os
import argparse
import json
import time
import warnings
from pathlib import Path
from datetime import datetime

warnings.filterwarnings('ignore')

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.append(LOCAL_PACKAGES)

# Ensure condition_agent root is on path
AGENT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(AGENT_ROOT))

import numpy as np
import torch
import torch.nn.functional as F
from tqdm import tqdm

# This triggers yp_* module registration
import config as agent_config
from config import (
    ELECTRODE_NAMES, CELL_TYPE_NAMES, UNKNOWN_INDICES,
    FINGERPRINT_SIZE, VOCAB_PATH,
)
from models.loader import ModelManager
from bayesian_opt.space import ConditionSpace
from bayesian_opt.surrogate import YieldSurrogate
from bayesian_opt.acquisition import AcquisitionOptimizer, ACQUISITION_FUNCTIONS
from bayesian_opt.optimizer import BayesianConditionOptimizer

# ── Constants ─────────────────────────────────────────────────
CONDITION_KEYS = ['anode', 'cathode', 'cell_type', 'electrolyte', 'solvent', 'reagent', 'catalyst']
GT_LABEL_MAP = {
    'anode': 'anode',
    'cathode': 'cathode',
    'cell_type': 'cell_type',
    'electrolyte': 'electrolyte_label',
    'solvent': 'solvent_label',
    'reagent': 'reagent_label',
    'catalyst': 'catalyst_label',
}


# ── Data Loading ──────────────────────────────────────────────

def load_test_data():
    """Load test.pt with 1064 reactions."""
    test_path = AGENT_ROOT / 'yield_prediction' / 'data' / 'test.pt'
    data = torch.load(test_path, map_location='cpu', weights_only=False)
    print(f"  Loaded {len(data)} test reactions")
    return data


def load_vocab():
    """Load vocab.json and build index-to-SMILES maps."""
    with open(VOCAB_PATH) as f:
        vocab = json.load(f)
    idx_to_smiles = {}
    for key in ['electrolyte', 'solvent', 'reagent', 'catalyst']:
        idx_to_smiles[key] = {v: k for k, v in vocab.get(key, {}).items()}
        idx_to_smiles[key][0] = ''
    return vocab, idx_to_smiles


def reaction_to_smiles(rxn: dict) -> str:
    """Reconstruct reaction SMILES from reactant/product SMILES lists."""
    reactants = '.'.join(rxn['reactant_smiles'])
    products = '.'.join(rxn['product_smiles'])
    return f"{reactants}>>{products}"


def get_gt_condition(rxn: dict) -> dict:
    """Extract ground truth condition indices from a test reaction."""
    return {
        'anode_index': rxn['anode'],
        'cathode_index': rxn['cathode'],
        'cell_type_index': rxn['cell_type'],
        'electrolyte_index': rxn['electrolyte_label'],
        'solvent_index': rxn['solvent_label'],
        'reagent_index': rxn['reagent_label'],
        'catalyst_index': rxn['catalyst_label'],
    }


# ── M1 Baseline ──────────────────────────────────────────────

def get_m1_predictions(mm, rxn, device, top_k=5):
    """
    Run M1 condition recommender on a single reaction.
    Returns: dict of {condition: [{'index': ..., 'confidence': ...}, ...]}
    """
    # Build reaction fingerprint from precomputed FPs
    fp = np.concatenate([rxn['reactant_fp'], rxn['product_fp'], rxn['diff_fp']])

    # Check if model needs xTB features
    xtb_lookup = mm.condition_xtb_lookup
    if xtb_lookup is not None:
        # Pad with xTB features (zeros for simplicity — same as main eval scripts)
        xtb_dim = mm.condition_reaction_dim - 6144
        fp = np.concatenate([fp, np.zeros(xtb_dim, dtype=np.float32)])

    features_tensor = torch.tensor([fp], dtype=torch.float32).to(device)
    model = mm.condition_model
    idx_maps = mm.idx_maps

    model.eval()
    with torch.no_grad():
        predictions = model(features_tensor)

    head_configs = [
        ('anode', ELECTRODE_NAMES),
        ('cathode', ELECTRODE_NAMES),
        ('cell_type', CELL_TYPE_NAMES),
        ('electrolyte', idx_maps['electrolyte']),
        ('solvent', idx_maps['solvent']),
        ('reagent', idx_maps['reagent']),
        ('catalyst', idx_maps['catalyst']),
    ]

    results = {}
    for name, name_map in head_configs:
        logit_key = f'{name}_logits' if f'{name}_logits' in predictions else name
        logits = predictions[logit_key]
        if name in UNKNOWN_INDICES:
            logits = logits.clone()
            logits[:, UNKNOWN_INDICES[name]] = float('-inf')
        probs = F.softmax(logits, dim=-1)
        k = min(top_k, probs.size(-1))
        top_probs, top_indices = torch.topk(probs, k, dim=-1)

        items = []
        for idx_val, prob_val in zip(top_indices[0].tolist(), top_probs[0].tolist()):
            smiles = ''
            if name in idx_maps:
                smiles = idx_maps[name].get(idx_val, '')
            items.append({
                'index': idx_val,
                'confidence': prob_val,
                'smiles': smiles,
            })
        results[name] = items

    return results


def m1_top1_condition(m1_preds: dict) -> dict:
    """Extract M1 top-1 as a condition dict."""
    cond = {}
    for key in CONDITION_KEYS:
        idx = m1_preds[key][0]['index']
        cond[f'{key}_index'] = idx
        if key in ['solvent', 'electrolyte', 'reagent', 'catalyst']:
            cond[f'{key}_smiles'] = m1_preds[key][0].get('smiles', '')
    return cond


# ── Yield Predictor Function Factory ──────────────────────────

def make_yield_fn(mm, rxn, device):
    """Create a yield prediction callable for a specific reaction."""
    reaction_fp_base = np.concatenate([
        rxn['reactant_fp'], rxn['product_fp'], rxn['diff_fp']
    ]).astype(np.float32)

    yield_model = mm.yield_model
    yield_input_dim = mm.yield_input_dim
    base_dim = 5 * FINGERPRINT_SIZE + 6
    mol_extractor = mm.mol_extractor

    def predict(conditions: dict) -> float:
        solvent_smiles = conditions.get('solvent_smiles', '')
        electrolyte_smiles = conditions.get('electrolyte_smiles', '')
        anode_idx = conditions.get('anode_index', 0)
        cathode_idx = conditions.get('cathode_index', 0)
        cell_type_idx = conditions.get('cell_type_index', 0)

        solvent_fp = (mol_extractor.get_morgan_fingerprint(solvent_smiles)
                      if solvent_smiles else np.zeros(FINGERPRINT_SIZE))
        electrolyte_fp = (mol_extractor.get_morgan_fingerprint(electrolyte_smiles)
                          if electrolyte_smiles else np.zeros(FINGERPRINT_SIZE))

        echem = np.array([anode_idx, cathode_idx, 0.0, 0.0, 0.0, cell_type_idx],
                         dtype=np.float32)

        full = np.concatenate([reaction_fp_base, solvent_fp, electrolyte_fp, echem])
        if yield_input_dim > base_dim:
            full = np.concatenate([full, np.zeros(yield_input_dim - base_dim, dtype=np.float32)])

        t = torch.tensor(full, dtype=torch.float32).unsqueeze(0).to(device)
        with torch.no_grad():
            return yield_model(t).item() * 100

    return predict


# ── Metrics ───────────────────────────────────────────────────

def compute_condition_match(pred_cond: dict, gt_cond: dict) -> dict:
    """Compare predicted vs ground truth conditions. Returns per-condition match."""
    matches = {}
    for key in CONDITION_KEYS:
        pred_idx = pred_cond.get(f'{key}_index', -1)
        gt_idx = gt_cond.get(f'{key}_index', -1)
        matches[key] = int(pred_idx == gt_idx)
    return matches


def aggregate_metrics(all_matches: list, label: str) -> dict:
    """Aggregate per-reaction match dicts into summary metrics."""
    n = len(all_matches)
    if n == 0:
        return {}

    # Per-condition accuracy
    top1_acc = {}
    for key in CONDITION_KEYS:
        top1_acc[key] = sum(m[key] for m in all_matches) / n

    # Joint metrics
    correct_counts = [sum(m.values()) for m in all_matches]
    exact_match = sum(1 for c in correct_counts if c == 7) / n
    partial_6 = sum(1 for c in correct_counts if c >= 6) / n
    partial_5 = sum(1 for c in correct_counts if c >= 5) / n
    avg_correct = np.mean(correct_counts)

    return {
        'label': label,
        'n_reactions': n,
        'top1_accuracy': top1_acc,
        'avg_top1': np.mean(list(top1_acc.values())),
        'joint_exact_match': exact_match,
        'partial_6_7': partial_6,
        'partial_5_7': partial_5,
        'avg_correct': avg_correct,
    }


# ── Evaluation Functions ──────────────────────────────────────

def eval_m1_baseline(mm, test_data, device):
    """Evaluate M1 top-1 as baseline."""
    print("\n[1/4] Evaluating M1 Top-1 baseline...")
    all_matches = []

    for rxn in tqdm(test_data, desc="M1 Top-1"):
        gt = get_gt_condition(rxn)
        m1_preds = get_m1_predictions(mm, rxn, device)
        pred = m1_top1_condition(m1_preds)
        matches = compute_condition_match(pred, gt)
        all_matches.append(matches)

    return aggregate_metrics(all_matches, "M1_TOP1")


def eval_bo_rerank(mm, test_data, device, idx_to_smiles, m1_top_k=5):
    """
    Evaluate BO rerank mode:
    - Run M1 top-k → build candidates → BO rerank → select top-1
    """
    print(f"\n[2/4] Evaluating BO Rerank (M1 top-{m1_top_k} → GP rerank)...")
    space = ConditionSpace(str(VOCAB_PATH))

    all_matches_rerank = []
    all_yield_errors = []  # (predicted_yield, gt_yield) for correlation
    all_gp_calibration = []  # (predicted_std, actual_error) for calibration

    for rxn in tqdm(test_data, desc="BO Rerank"):
        gt = get_gt_condition(rxn)
        gt_yield = rxn['yield']
        m1_preds = get_m1_predictions(mm, rxn, device, top_k=m1_top_k)

        # Build candidate set from M1 top-k
        candidates = []
        m1_probs = []
        all_keys = ['anode', 'cathode', 'cell_type', 'solvent', 'electrolyte', 'reagent', 'catalyst']

        # Base: all top-1
        base = {}
        base_prob = 1.0
        for key in all_keys:
            item = m1_preds[key][0]
            base[f'{key}_index'] = item['index']
            if key in ['solvent', 'electrolyte', 'reagent', 'catalyst']:
                base[f'{key}_smiles'] = item.get('smiles', '')
            base_prob *= item['confidence']
        candidates.append(base)
        m1_probs.append(base_prob)

        # Single-swap variants
        for key in all_keys:
            for item in m1_preds[key][1:m1_top_k]:
                variant = dict(base)
                variant[f'{key}_index'] = item['index']
                if key in ['solvent', 'electrolyte', 'reagent', 'catalyst']:
                    variant[f'{key}_smiles'] = item.get('smiles', '')
                # Approximate joint probability
                vp = base_prob / m1_preds[key][0]['confidence'] * item['confidence']
                candidates.append(variant)
                m1_probs.append(vp)

        # Create yield function and surrogate
        yield_fn = make_yield_fn(mm, rxn, device)
        surrogate = YieldSurrogate(space, yield_predictor_fn=yield_fn)

        # Give surrogate a few data points from candidates (simulate warm-start)
        warmup_conds = candidates[:min(5, len(candidates))]
        warmup_yields = np.array([yield_fn(c) for c in warmup_conds])
        if len(warmup_conds) > 0:
            surrogate.fit(warmup_conds, warmup_yields)

        # GP predictions for all candidates
        mean, std = surrogate.predict(candidates)

        # Rerank: combined score = alpha * m1_prob + (1-alpha) * UCB_norm
        alpha = 0.5
        beta_ucb = 1.5
        ucb = mean + beta_ucb * std
        ucb_min, ucb_max = ucb.min(), ucb.max()
        if ucb_max > ucb_min:
            ucb_norm = (ucb - ucb_min) / (ucb_max - ucb_min)
        else:
            ucb_norm = np.ones_like(ucb) * 0.5

        m1_probs_arr = np.array(m1_probs)
        if m1_probs_arr.max() > 0:
            m1_probs_arr = m1_probs_arr / m1_probs_arr.max()
        combined = alpha * m1_probs_arr + (1 - alpha) * ucb_norm

        best_idx = int(np.argmax(combined))
        pred_cond = candidates[best_idx]

        matches = compute_condition_match(pred_cond, gt)
        all_matches_rerank.append(matches)

        # GP calibration data
        all_yield_errors.append((mean[best_idx], gt_yield))
        all_gp_calibration.append((std[best_idx], abs(mean[best_idx] - gt_yield)))

    metrics = aggregate_metrics(all_matches_rerank, "BO_RERANK")

    # Yield correlation
    if all_yield_errors:
        preds, gts = zip(*all_yield_errors)
        corr = float(np.corrcoef(preds, gts)[0, 1]) if len(preds) > 1 else 0
        metrics['yield_correlation'] = corr
        metrics['avg_predicted_yield'] = float(np.mean(preds))
        metrics['avg_gt_yield'] = float(np.mean(gts))

    # GP calibration
    if all_gp_calibration:
        stds, errors = zip(*all_gp_calibration)
        cal_corr = float(np.corrcoef(stds, errors)[0, 1]) if len(stds) > 1 else 0
        metrics['gp_calibration_corr'] = cal_corr
        metrics['avg_gp_std'] = float(np.mean(stds))
        metrics['avg_abs_error'] = float(np.mean(errors))

    return metrics


def eval_bo_search(mm, test_data, device, idx_to_smiles, n_iter=20, n_reactions=None):
    """
    Evaluate BO offline search mode:
    - For each reaction, run BO search with YieldPredictor as oracle
    - Compare best-found conditions to GT
    """
    print(f"\n[3/4] Evaluating BO Offline Search ({n_iter} iters)...")
    space = ConditionSpace(str(VOCAB_PATH))

    subset = test_data[:n_reactions] if n_reactions else test_data
    all_matches = []
    convergence_data = []  # Track convergence

    for rxn in tqdm(subset, desc="BO Search"):
        gt = get_gt_condition(rxn)
        yield_fn = make_yield_fn(mm, rxn, device)

        optimizer = BayesianConditionOptimizer(
            condition_space=space,
            yield_predictor_fn=yield_fn,
        )

        # Run search
        rxn_smiles = reaction_to_smiles(rxn)
        optimizer.initialize(rxn_smiles)

        # Phase 1: evaluate initial candidates
        init_cands = list(optimizer._candidates_pool[:5])
        if len(init_cands) < 3:
            init_cands.extend(space.sample_random(3 - len(init_cands)))

        best_yield_history = []
        for cond in init_cands:
            y = yield_fn(cond)
            optimizer.observe(cond, y)

        best = optimizer.get_best()
        best_yield_history.append(best['yield'] if best else 0)

        # Phase 2: BO iterations
        for it in range(n_iter):
            suggestions = optimizer.suggest_next(n=1, acq_func='ei')
            if not suggestions:
                break
            cond = suggestions[0]
            y = yield_fn(cond)
            optimizer.observe(cond, y)
            best = optimizer.get_best()
            best_yield_history.append(best['yield'] if best else 0)

        # Get final best
        best = optimizer.get_best()
        if best:
            pred_cond = best['conditions']
            matches = compute_condition_match(pred_cond, gt)
            all_matches.append(matches)
            convergence_data.append(best_yield_history)

    metrics = aggregate_metrics(all_matches, f"BO_SEARCH_{n_iter}iter")

    # Convergence analysis
    if convergence_data:
        # Average convergence curve
        max_len = max(len(c) for c in convergence_data)
        padded = np.array([
            c + [c[-1]] * (max_len - len(c))
            for c in convergence_data
        ])
        avg_curve = padded.mean(axis=0)
        metrics['convergence_curve'] = {
            'iterations': list(range(len(avg_curve))),
            'avg_best_yield': [round(float(v), 2) for v in avg_curve],
        }
        metrics['convergence_improvement'] = round(float(avg_curve[-1] - avg_curve[0]), 2)

    return metrics


def eval_iterative_convergence(mm, test_data, device, n_rounds=10, n_reactions=50):
    """
    Evaluate iterative suggest→observe convergence.
    Simulate experiments by using GT yield as the observed value.
    """
    print(f"\n[4/4] Evaluating Iterative Convergence ({n_rounds} rounds, {n_reactions} rxns)...")
    space = ConditionSpace(str(VOCAB_PATH))

    subset = test_data[:n_reactions]
    all_acq_histories = []
    all_yield_histories = []

    for rxn in tqdm(subset, desc="Iterative"):
        yield_fn = make_yield_fn(mm, rxn, device)
        gt_yield = rxn['yield']

        optimizer = BayesianConditionOptimizer(
            condition_space=space,
            yield_predictor_fn=yield_fn,
        )

        rxn_smiles = reaction_to_smiles(rxn)
        optimizer.initialize(rxn_smiles)

        acq_history = []
        yield_history = []

        for rd in range(n_rounds):
            details = optimizer.suggest_with_details(n=1, acq_func='ei')
            if not details:
                break
            cond = details[0]['conditions']
            acq_val = details[0]['acq_value']
            pred_yield = details[0]['predicted_mean']

            # Simulate experiment: use yield_fn as oracle
            obs_yield = yield_fn(cond)
            optimizer.observe(cond, obs_yield)

            acq_history.append(acq_val)
            best = optimizer.get_best()
            yield_history.append(best['yield'] if best else 0)

        all_acq_histories.append(acq_history)
        all_yield_histories.append(yield_history)

    # Aggregate convergence
    metrics = {'label': 'ITERATIVE_CONVERGENCE', 'n_reactions': len(subset), 'n_rounds': n_rounds}

    if all_acq_histories:
        max_len = max(len(h) for h in all_acq_histories)
        padded_acq = np.array([
            h + [h[-1]] * (max_len - len(h)) if h else [0] * max_len
            for h in all_acq_histories
        ])
        padded_yield = np.array([
            h + [h[-1]] * (max_len - len(h)) if h else [0] * max_len
            for h in all_yield_histories
        ])

        avg_acq = padded_acq.mean(axis=0)
        avg_yield = padded_yield.mean(axis=0)

        metrics['avg_acquisition_per_round'] = [round(float(v), 4) for v in avg_acq]
        metrics['avg_best_yield_per_round'] = [round(float(v), 2) for v in avg_yield]
        metrics['acq_decreasing'] = bool(avg_acq[-1] < avg_acq[0]) if len(avg_acq) > 1 else False
        metrics['yield_improving'] = bool(avg_yield[-1] > avg_yield[0]) if len(avg_yield) > 1 else False
        metrics['final_avg_best_yield'] = round(float(avg_yield[-1]), 2)
        metrics['initial_avg_best_yield'] = round(float(avg_yield[0]), 2)
        metrics['yield_improvement'] = round(float(avg_yield[-1] - avg_yield[0]), 2)

    return metrics


# ── Main ──────────────────────────────────────────────────────

def print_comparison(m1_metrics, rerank_metrics, search_metrics=None):
    """Print a formatted comparison table."""
    print("\n" + "=" * 80)
    print("COMPARISON: Per-Condition Top-1 Accuracy")
    print("=" * 80)

    header = f"{'Condition':<15} {'M1_TOP1':>10} {'BO_RERANK':>12}"
    if search_metrics:
        header += f" {'BO_SEARCH':>12} {'Delta(Re)':>10} {'Delta(Se)':>10}"
    else:
        header += f" {'Delta':>10}"
    print(header)
    print("-" * len(header))

    for key in CONDITION_KEYS:
        m1_val = m1_metrics['top1_accuracy'][key]
        re_val = rerank_metrics['top1_accuracy'][key]
        line = f"{key:<15} {m1_val:>10.3f} {re_val:>12.3f}"
        if search_metrics and key in search_metrics.get('top1_accuracy', {}):
            se_val = search_metrics['top1_accuracy'][key]
            line += f" {se_val:>12.3f} {re_val - m1_val:>+10.3f} {se_val - m1_val:>+10.3f}"
        else:
            line += f" {re_val - m1_val:>+10.3f}"
        print(line)

    print("-" * len(header))
    m1_avg = m1_metrics['avg_top1']
    re_avg = rerank_metrics['avg_top1']
    line = f"{'AVG':<15} {m1_avg:>10.3f} {re_avg:>12.3f}"
    if search_metrics:
        se_avg = search_metrics['avg_top1']
        line += f" {se_avg:>12.3f} {re_avg - m1_avg:>+10.3f} {se_avg - m1_avg:>+10.3f}"
    else:
        line += f" {re_avg - m1_avg:>+10.3f}"
    print(line)

    print("\n" + "=" * 80)
    print("Joint Match Metrics")
    print("=" * 80)
    joint_keys = ['joint_exact_match', 'partial_6_7', 'partial_5_7', 'avg_correct']
    labels = ['Exact (7/7)', 'Partial (≥6/7)', 'Partial (≥5/7)', 'Avg correct']

    for label, key in zip(labels, joint_keys):
        m1_val = m1_metrics.get(key, 0)
        re_val = rerank_metrics.get(key, 0)
        line = f"  {label:<20} M1={m1_val:.4f}  Rerank={re_val:.4f}  Δ={re_val - m1_val:+.4f}"
        if search_metrics:
            se_val = search_metrics.get(key, 0)
            line += f"  Search={se_val:.4f}  Δ={se_val - m1_val:+.4f}"
        print(line)

    # GP calibration
    if 'gp_calibration_corr' in rerank_metrics:
        print(f"\n  GP Calibration (std vs |error| corr): {rerank_metrics['gp_calibration_corr']:.4f}")
        print(f"  Avg GP std: {rerank_metrics['avg_gp_std']:.2f}, Avg |error|: {rerank_metrics['avg_abs_error']:.2f}")

    if 'yield_correlation' in rerank_metrics:
        print(f"  Yield correlation (predicted vs GT): {rerank_metrics['yield_correlation']:.4f}")


def main():
    parser = argparse.ArgumentParser(description="Evaluate Bayesian Optimization module")
    parser.add_argument('--device', default='cpu', help='cpu or cuda')
    parser.add_argument('--n-reactions', type=int, default=None,
                        help='Limit number of test reactions (default: all 1064)')
    parser.add_argument('--n-search-reactions', type=int, default=100,
                        help='Number of reactions for BO search eval (default: 100)')
    parser.add_argument('--n-convergence-reactions', type=int, default=50,
                        help='Number of reactions for convergence eval (default: 50)')
    parser.add_argument('--bo-iters', type=int, default=20,
                        help='BO search iterations per reaction (default: 20)')
    parser.add_argument('--convergence-rounds', type=int, default=10,
                        help='Iterative convergence rounds (default: 10)')
    parser.add_argument('--m1-top-k', type=int, default=5,
                        help='M1 top-k for rerank candidates (default: 5)')
    parser.add_argument('--output', default=None, help='Output JSON path')
    args = parser.parse_args()

    print("=" * 80)
    print("Bayesian Optimization Module Evaluation")
    print("=" * 80)

    # Load models
    print("\nLoading models...")
    mm = ModelManager(device=args.device)
    _ = mm.condition_model  # Trigger lazy load
    _ = mm.yield_model
    print(f"  Condition model input dim: {mm.condition_reaction_dim}")
    print(f"  Yield model input dim: {mm.yield_input_dim}")

    # Load data
    print("\nLoading data...")
    test_data = load_test_data()
    vocab, idx_to_smiles = load_vocab()

    if args.n_reactions:
        test_data = test_data[:args.n_reactions]
        print(f"  Using {len(test_data)} reactions (limited)")

    t0 = time.time()
    results = {}

    # 1. M1 baseline
    m1_metrics = eval_m1_baseline(mm, test_data, args.device)
    results['M1_TOP1'] = m1_metrics

    # 2. BO rerank
    rerank_metrics = eval_bo_rerank(mm, test_data, args.device, idx_to_smiles,
                                     m1_top_k=args.m1_top_k)
    results['BO_RERANK'] = rerank_metrics

    # 3. BO search (on subset)
    search_subset = test_data[:args.n_search_reactions]
    search_metrics = eval_bo_search(mm, search_subset, args.device, idx_to_smiles,
                                     n_iter=args.bo_iters,
                                     n_reactions=args.n_search_reactions)
    results['BO_SEARCH'] = search_metrics

    # Also compute M1 baseline on same subset for fair comparison
    m1_sub_matches = []
    for rxn in search_subset:
        gt = get_gt_condition(rxn)
        m1_preds = get_m1_predictions(mm, rxn, args.device)
        pred = m1_top1_condition(m1_preds)
        m1_sub_matches.append(compute_condition_match(pred, gt))
    m1_sub_metrics = aggregate_metrics(m1_sub_matches, "M1_TOP1_search_subset")
    results['M1_TOP1_search_subset'] = m1_sub_metrics

    # 4. Iterative convergence
    convergence_metrics = eval_iterative_convergence(
        mm, test_data, args.device,
        n_rounds=args.convergence_rounds,
        n_reactions=args.n_convergence_reactions,
    )
    results['ITERATIVE_CONVERGENCE'] = convergence_metrics

    elapsed = time.time() - t0
    results['meta'] = {
        'n_test': len(test_data),
        'n_search_subset': len(search_subset),
        'n_convergence_subset': min(args.n_convergence_reactions, len(test_data)),
        'bo_iters': args.bo_iters,
        'convergence_rounds': args.convergence_rounds,
        'm1_top_k': args.m1_top_k,
        'device': args.device,
        'elapsed_sec': round(elapsed, 1),
        'timestamp': datetime.now().strftime('%Y%m%d_%H%M%S'),
    }

    # Print comparison
    print_comparison(m1_metrics, rerank_metrics, search_metrics)

    # Print convergence
    print("\n" + "=" * 80)
    print("Iterative Convergence Analysis")
    print("=" * 80)
    conv = convergence_metrics
    if 'avg_best_yield_per_round' in conv:
        yields = conv['avg_best_yield_per_round']
        acqs = conv['avg_acquisition_per_round']
        print(f"  Rounds: {conv['n_rounds']}, Reactions: {conv['n_reactions']}")
        print(f"  Initial best yield: {conv['initial_avg_best_yield']:.2f}%")
        print(f"  Final best yield:   {conv['final_avg_best_yield']:.2f}%")
        print(f"  Yield improvement:  {conv['yield_improvement']:+.2f}%")
        print(f"  Acquisition decreasing: {conv['acq_decreasing']}")
        print(f"  Yield improving: {conv['yield_improving']}")
        print(f"\n  Per-round avg best yield:")
        for i, y in enumerate(yields):
            bar = '█' * int(y / 2)
            print(f"    Round {i:2d}: {y:6.2f}%  {bar}")

    print(f"\n  Total eval time: {elapsed:.1f}s")

    # Save results
    output_dir = AGENT_ROOT / 'yield_prediction' / 'eval_results' / 'bayesian_opt'
    output_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = args.output or str(output_dir / f'bo_eval_{ts}.json')
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n  Results saved to: {output_path}")


if __name__ == '__main__':
    main()
