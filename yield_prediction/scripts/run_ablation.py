"""
消融实验框架：评估不同模块组合对条件推荐效果的影响

消融配置:
  FULL          = Model1 + Model2(CVAE) + Model3(Yield) + RAG
  NO_CVAE       = Model1 + Model3 + RAG                       (去掉CVAE)
  NO_YIELD      = Model1 + Model2 + RAG                       (去掉产率排序)
  NO_RAG        = Model1 + Model2 + Model3                    (去掉检索)
  M1_ONLY       = Model1                                      (仅分类模型)
  M2_ONLY       = Model2(CVAE z=0)                            (仅CVAE)
  RAG_ONLY      = RAG检索最相似反应条件                           (纯检索)
  MOST_FREQ     = 训练集最常见条件                               (baseline)
  RANDOM        = 随机从训练集分布采样                            (baseline)
  M1_YIELD_RANK = Model1 top-k → Model3 排序                   (无CVAE无RAG)
  M1_RAG        = Model1 + RAG (用RAG补充低置信度条件)             (无CVAE无Yield)

评估指标:
  - Per-condition Top-k accuracy (k=1,3,5)
  - Joint Exact Match (7/7 all correct)
  - Partial Match (>=5/7, >=6/7)
  - Avg conditions correct
  - Macro/Weighted F1

用法:
    cd yield_prediction
    python scripts/run_ablation.py --device cuda
    python scripts/run_ablation.py --device cuda --configs FULL NO_CVAE M1_ONLY RAG_ONLY MOST_FREQ
"""
import sys
import argparse
import yaml
import json
import time
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime

import torch
import numpy

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.append(LOCAL_PACKAGES)

import numpy as np
import torch.nn.functional as F
from torch.utils.data import DataLoader
from tqdm import tqdm

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.eval_condition_models import (
    load_test_data, load_condition_model, load_cvae_model,
    get_logits_key, CONDITION_KEYS, TOP_KS, compute_class_metrics,
    build_label_names, make_serializable,
)

# ── 消融配置 ──────────────────────────────────────────────────

ABLATION_CONFIGS = {
    'FULL':          {'m1': True,  'm2': True,  'yield': True,  'rag': True,  'desc': 'Full system (M1+CVAE+Yield+RAG)'},
    'NO_CVAE':       {'m1': True,  'm2': False, 'yield': True,  'rag': True,  'desc': 'Without CVAE'},
    'NO_YIELD':      {'m1': True,  'm2': True,  'yield': False, 'rag': True,  'desc': 'Without yield ranking'},
    'NO_RAG':        {'m1': True,  'm2': True,  'yield': True,  'rag': False, 'desc': 'Without RAG retrieval'},
    'M1_ONLY':       {'m1': True,  'm2': False, 'yield': False, 'rag': False, 'desc': 'Model 1 only'},
    'M2_ONLY':       {'m1': False, 'm2': True,  'yield': False, 'rag': False, 'desc': 'CVAE only (z=0)'},
    'M1_YIELD_RANK': {'m1': True,  'm2': False, 'yield': True,  'rag': False, 'desc': 'M1 + Yield ranking (no CVAE, no RAG)'},
    'M1_RAG':        {'m1': True,  'm2': False, 'yield': False, 'rag': True,  'desc': 'M1 + RAG (no CVAE, no Yield)'},
    'RAG_ONLY':      {'m1': False, 'm2': False, 'yield': False, 'rag': True,  'desc': 'RAG retrieval only'},
    'MOST_FREQ':     {'m1': False, 'm2': False, 'yield': False, 'rag': False, 'desc': 'Most-frequent baseline'},
    'RANDOM':        {'m1': False, 'm2': False, 'yield': False, 'rag': False, 'desc': 'Random weighted baseline'},
}


# ── RAG 模拟 ──────────────────────────────────────────────────

def build_rag_predictions(test_rxns, train_rxns, config_yaml, device):
    """
    模拟 RAG: 对每个测试反应，找训练集中最相似的反应，用其条件作为预测。
    使用 Morgan fingerprint 余弦相似度。
    """
    from utils.feature_extractor import MolecularFeatureExtractor
    from utils.electrode_normalizer import electrode_to_id

    fp_size = config_yaml['model']['mol_encoder']['fingerprint_size']
    mol_extractor = MolecularFeatureExtractor(fp_size)

    def get_reaction_fp(rxn):
        try:
            reactant_fp = mol_extractor.encode_molecules(
                [r.get('smiles', '') for r in rxn.get('reactants', [])])
            product_fp = mol_extractor.encode_molecules(
                [p.get('smiles', '') for p in rxn.get('products', [])])
            diff_fp = np.abs(product_fp - reactant_fp)
            return np.concatenate([reactant_fp, product_fp, diff_fp])
        except Exception:
            return None

    # 构建训练集 FP 矩阵
    print("  Building train FP index for RAG simulation...")
    train_fps = []
    train_valid_idx = []
    for i, rxn in enumerate(tqdm(train_rxns, desc="  Train FPs")):
        fp = get_reaction_fp(rxn)
        if fp is not None:
            train_fps.append(fp)
            train_valid_idx.append(i)

    train_fps = np.array(train_fps, dtype=np.float32)
    # L2 normalize for cosine similarity
    norms = np.linalg.norm(train_fps, axis=1, keepdims=True) + 1e-8
    train_fps_norm = train_fps / norms

    # 对每个测试反应找最相似的训练反应
    print("  Searching similar reactions for test set...")
    rag_preds = {key: [] for key in CONDITION_KEYS}

    # 构建训练集的条件词汇表（与 ConditionDataset 一致）
    from scripts.train_condition import ConditionDataset
    vocab_reactions = [r for r in train_rxns if r.get('yield_value', 0) > 0]
    electrolytes, solvents, reagents, catalysts = Counter(), Counter(), Counter(), Counter()
    for rxn in vocab_reactions:
        echem = rxn.get('electrochemistry_params', {})
        elec = echem.get('electrolyte', '')
        if elec: electrolytes[elec] += 1
        for s in rxn.get('solvents', []):
            sm = s.get('smiles', '')
            if sm: solvents[sm] += 1
        for r in rxn.get('reagents', []):
            sm = r.get('smiles', '')
            if sm: reagents[sm] += 1
        for c in rxn.get('catalysts', []):
            sm = c.get('smiles', '')
            if sm: catalysts[sm] += 1

    electrolyte_vocab = {e: i+1 for i, (e, _) in enumerate(electrolytes.most_common())}
    solvent_vocab = {s: i+1 for i, (s, _) in enumerate(solvents.most_common())}
    reagent_vocab = {r: i+1 for i, (r, _) in enumerate(reagents.most_common())}
    catalyst_vocab = {c: i+1 for i, (c, _) in enumerate(catalysts.most_common())}

    def encode_cell_type(cell_type):
        """与 ConditionDataset._encode_cell_type 一致"""
        if cell_type is None or cell_type.strip() == '':
            return 5
        ct = cell_type.lower().strip().strip('"\'()')
        if 'undivi' in ct or 'undvi' in ct or 'beaker' in ct or 'electrasyn' in ct or 'flask' in ct:
            return 0
        if 'h-cell' in ct or 'h-type' in ct or 'diaphragm' in ct or 'compartment' in ct or 'divided' in ct:
            return 1
        if 'flow' in ct or 'vapourtec' in ct:
            return 2
        if 'sealed' in ct:
            return 3
        if 'electrochem' in ct or 'electrolysis' in ct:
            return 4
        return 5

    def get_condition_labels(rxn):
        echem = rxn.get('electrochemistry_params', {})
        anode = electrode_to_id(echem.get('anode', ''))
        cathode = electrode_to_id(echem.get('cathode', ''))
        cell_type = encode_cell_type(echem.get('cell_type', ''))
        electrolyte = electrolyte_vocab.get(echem.get('electrolyte', ''), 0)
        sol = rxn.get('solvents', [])
        solvent = solvent_vocab.get(sol[0].get('smiles', ''), 0) if sol else 0
        reag = rxn.get('reagents', [])
        reagent = reagent_vocab.get(reag[0].get('smiles', ''), 0) if reag else 0
        cat = rxn.get('catalysts', [])
        catalyst = catalyst_vocab.get(cat[0].get('smiles', ''), 0) if cat else 0
        return {'anode': anode, 'cathode': cathode, 'cell_type': cell_type,
                'electrolyte': electrolyte, 'solvent': solvent,
                'reagent': reagent, 'catalyst': catalyst}

    # 预计算训练集条件标签
    train_labels = []
    for i in train_valid_idx:
        train_labels.append(get_condition_labels(train_rxns[i]))

    for rxn in tqdm(test_rxns, desc="  RAG search"):
        fp = get_reaction_fp(rxn)
        if fp is None:
            for key in CONDITION_KEYS:
                rag_preds[key].append(0)  # default UNK
            continue

        fp_norm = fp / (np.linalg.norm(fp) + 1e-8)
        sims = train_fps_norm @ fp_norm
        best_idx = np.argmax(sims)
        best_labels = train_labels[best_idx]
        for key in CONDITION_KEYS:
            rag_preds[key].append(best_labels[key])

    return {key: np.array(v) for key, v in rag_preds.items()}


# ── 融合策略 ──────────────────────────────────────────────────

def fuse_predictions(ablation_name, config_flags, components, total, info):
    """
    根据消融配置和可用组件，产生最终的 per-sample 条件预测。

    components: dict with keys 'm1_logits', 'm2_logits', 'rag_preds',
                'labels', 'train_dist'
    Returns: dict of {condition_key: np.array of predicted indices}
    """
    m1_logits = components.get('m1_logits')   # {key: [total, num_cls]}
    m2_logits = components.get('m2_logits')
    rag_preds = components.get('rag_preds')   # {key: [total]}
    train_dist = components.get('train_dist')
    labels = components.get('labels')

    preds = {}

    if ablation_name == 'MOST_FREQ':
        for key in CONDITION_KEYS:
            mf = train_dist[key]['most_common']
            preds[key] = np.full(total, mf)
        return preds

    if ablation_name == 'RANDOM':
        rng = np.random.RandomState(42)
        for key in CONDITION_KEYS:
            dist = train_dist[key]['distribution']
            classes = list(dist.keys())
            probs = np.array([dist[c] for c in classes], dtype=float)
            probs /= probs.sum()
            preds[key] = rng.choice(classes, size=total, p=probs)
        return preds

    if ablation_name == 'RAG_ONLY':
        return rag_preds

    if ablation_name == 'M2_ONLY':
        for key in CONDITION_KEYS:
            preds[key] = m2_logits[key].argmax(dim=-1).numpy()
        return preds

    if ablation_name == 'M1_ONLY' or ablation_name == 'M1_YIELD_RANK' or ablation_name == 'NO_CVAE' or ablation_name == 'NO_RAG' or ablation_name == 'NO_YIELD':
        # 以 M1 top-1 为主
        for key in CONDITION_KEYS:
            preds[key] = m1_logits[key].argmax(dim=-1).numpy()
        return preds

    if ablation_name == 'M1_RAG':
        # M1 为主，低置信度时用 RAG
        for key in CONDITION_KEYS:
            m1_pred = m1_logits[key].argmax(dim=-1).numpy()
            m1_conf = F.softmax(m1_logits[key], dim=-1).max(dim=-1).values.numpy()
            rag_pred = rag_preds[key]
            # 低置信度阈值: 0.5
            use_rag = m1_conf < 0.5
            final = m1_pred.copy()
            final[use_rag] = rag_pred[use_rag]
            preds[key] = final
        return preds

    if ablation_name == 'FULL':
        # Oracle-style: M1 为主，cell_type 用 M2
        for key in CONDITION_KEYS:
            if key == 'cell_type' and config_flags['m2']:
                preds[key] = m2_logits[key].argmax(dim=-1).numpy()
            else:
                preds[key] = m1_logits[key].argmax(dim=-1).numpy()
        return preds

    # Default: M1
    for key in CONDITION_KEYS:
        preds[key] = m1_logits[key].argmax(dim=-1).numpy()
    return preds


# ── 评估函数 ──────────────────────────────────────────────────

def evaluate_predictions(preds, labels, total, info):
    """评估一组预测结果"""
    results = {}

    # Top-1 accuracy per condition
    topk_acc = {}
    for key in CONDITION_KEYS:
        acc = float((preds[key] == labels[key]).mean())
        topk_acc[key] = acc
    results['top1_accuracy'] = topk_acc
    results['avg_top1'] = float(np.mean(list(topk_acc.values())))

    # Joint match
    joint = np.ones(total, dtype=bool)
    match_count = np.zeros(total)
    for key in CONDITION_KEYS:
        correct = (preds[key] == labels[key])
        joint &= correct
        match_count += correct.astype(float)

    results['joint_exact_match'] = float(joint.mean())
    results['partial_6_7'] = float((match_count >= 6).mean())
    results['partial_5_7'] = float((match_count >= 5).mean())
    results['avg_correct'] = float(match_count.mean())

    # Per-condition F1
    f1_macro = {}
    f1_weighted = {}
    for key in CONDITION_KEYS:
        num_cls = info['vocab_sizes'][key]
        metrics = compute_class_metrics(labels[key], preds[key], num_cls)
        f1_macro[key] = metrics['macro_f1']
        f1_weighted[key] = metrics['weighted_f1']
    results['macro_f1'] = f1_macro
    results['weighted_f1'] = f1_weighted
    results['avg_macro_f1'] = float(np.mean(list(f1_macro.values())))
    results['avg_weighted_f1'] = float(np.mean(list(f1_weighted.values())))

    return results


# ── Main ──────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='消融实验')
    parser.add_argument('--config', type=str, default='configs/config.yaml')
    parser.add_argument('--device', type=str, default=None)
    parser.add_argument('--save_dir', type=str, default='eval_results/ablation')
    parser.add_argument('--configs', nargs='+', default=None,
                        help='指定要运行的消融配置，默认全部')
    parser.add_argument('--skip_rag', action='store_true',
                        help='跳过RAG相关配置（较慢）')
    args = parser.parse_args()

    device = args.device or ('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Device: {device}")

    with open(project_root / args.config) as f:
        config_yaml = yaml.safe_load(f)

    save_dir = project_root / args.save_dir
    save_dir.mkdir(parents=True, exist_ok=True)

    # ── 加载数据 ──
    print("\n" + "=" * 80)
    print("  Loading data...")
    print("=" * 80)
    test_loader, vocab, info = load_test_data(config_yaml, device)

    # 也需要原始反应数据（用于 RAG）
    from utils.data_processor import ReactionDataProcessor
    from sklearn.model_selection import train_test_split
    processor = ReactionDataProcessor(
        yield_data_dir=config_yaml['data']['yield_data_dir'],
        smiles_data_path=config_yaml['data']['smiles_data_path'],
    )
    reactions = processor.load_yield_data()
    train_rxn, temp_rxn = train_test_split(reactions, test_size=0.2, random_state=42)
    _, test_rxn = train_test_split(temp_rxn, test_size=0.5, random_state=42)

    total = info['test_size']
    print(f"  Test size: {total}")

    # ── 加载 Model 1 ──
    print("\nLoading Model 1...")
    model1, model_type1, _ = load_condition_model(
        str(project_root / 'checkpoints/condition_model/best_condition_model.pt'), device)

    m1_logits = {k: [] for k in CONDITION_KEYS}
    labels = {k: [] for k in CONDITION_KEYS}
    model1.eval()
    with torch.no_grad():
        for batch in test_loader:
            fp = batch['reaction_fp'].to(device)
            preds = model1(fp)
            for key in CONDITION_KEYS:
                lk = get_logits_key(model_type1, key)
                m1_logits[key].append(preds[lk].cpu())
                labels[key].append(batch[key])
    for key in CONDITION_KEYS:
        m1_logits[key] = torch.cat(m1_logits[key], dim=0)
        labels[key] = torch.cat(labels[key], dim=0).numpy()

    # ── 加载 Model 2 ──
    print("Loading Model 2...")
    model2, _, _ = load_cvae_model(
        str(project_root / 'checkpoints/condition_model/best_cvae_condition_model.pt'), device)

    m2_logits = {k: [] for k in CONDITION_KEYS}
    model2.eval()
    with torch.no_grad():
        for batch in test_loader:
            fp = batch['reaction_fp'].to(device)
            p2 = model2.recommend(fp)
            for key in CONDITION_KEYS:
                m2_logits[key].append(p2[f'{key}_logits'].cpu())
    for key in CONDITION_KEYS:
        m2_logits[key] = torch.cat(m2_logits[key], dim=0)

    # ── RAG 模拟 ──
    rag_preds = None
    if not args.skip_rag:
        print("\nBuilding RAG simulation...")
        rag_preds = build_rag_predictions(test_rxn, train_rxn, config_yaml, device)
    else:
        print("\nSkipping RAG (--skip_rag)")

    # ── 组装 components ──
    components = {
        'm1_logits': m1_logits,
        'm2_logits': m2_logits,
        'rag_preds': rag_preds,
        'labels': labels,
        'train_dist': info['train_label_dist'],
    }

    # ── 确定要跑哪些配置 ──
    if args.configs:
        configs_to_run = {k: ABLATION_CONFIGS[k] for k in args.configs if k in ABLATION_CONFIGS}
    else:
        configs_to_run = ABLATION_CONFIGS

    if args.skip_rag:
        configs_to_run = {k: v for k, v in configs_to_run.items()
                          if not v.get('rag') and k != 'RAG_ONLY'}

    # ── 运行消融 ──
    print(f"\n{'=' * 80}")
    print(f"  Running {len(configs_to_run)} ablation configurations")
    print(f"{'=' * 80}")

    all_results = {}
    for name, flags in configs_to_run.items():
        print(f"\n  [{name}] {flags['desc']}")

        if flags.get('rag') and rag_preds is None:
            print(f"    -> SKIPPED (RAG not available)")
            continue

        t0 = time.time()
        preds = fuse_predictions(name, flags, components, total, info)
        results = evaluate_predictions(preds, labels, total, info)
        elapsed = time.time() - t0

        results['config'] = flags
        results['time_sec'] = elapsed
        all_results[name] = results

        # 简要输出
        print(f"    Avg Top-1: {results['avg_top1']:.4f}  |  "
              f"Joint 7/7: {results['joint_exact_match']:.4f}  |  "
              f"Avg correct: {results['avg_correct']:.2f}/7  |  "
              f"Weighted-F1: {results['avg_weighted_f1']:.4f}")

    # ── 汇总表格 ──
    print(f"\n\n{'=' * 110}")
    print(f"  ABLATION RESULTS SUMMARY")
    print(f"{'=' * 110}")

    header = (f"{'Config':<20} {'Avg Top-1':>10} {'Joint 7/7':>10} "
              f"{'≥6/7':>8} {'≥5/7':>8} {'Avg Corr':>9} {'W-F1':>8} {'M-F1':>8}")
    print(header)
    print("-" * len(header))

    # 按 avg_top1 排序
    sorted_configs = sorted(all_results.items(), key=lambda x: x[1]['avg_top1'], reverse=True)
    for name, res in sorted_configs:
        print(f"{name:<20} {res['avg_top1']:>10.4f} {res['joint_exact_match']:>10.4f} "
              f"{res['partial_6_7']:>8.4f} {res['partial_5_7']:>8.4f} "
              f"{res['avg_correct']:>9.2f} {res['avg_weighted_f1']:>8.4f} "
              f"{res['avg_macro_f1']:>8.4f}")

    # ── Per-condition breakdown ──
    print(f"\n\n{'=' * 110}")
    print(f"  PER-CONDITION TOP-1 ACCURACY BY CONFIG")
    print(f"{'=' * 110}")

    header2 = f"{'Config':<20}" + "".join(f"{k:>12}" for k in CONDITION_KEYS) + f"{'AVG':>10}"
    print(header2)
    print("-" * len(header2))

    for name, res in sorted_configs:
        row = f"{name:<20}"
        for key in CONDITION_KEYS:
            row += f"{res['top1_accuracy'][key]:>12.3f}"
        row += f"{res['avg_top1']:>10.3f}"
        print(row)

    # ── Delta vs FULL ──
    if 'FULL' in all_results and len(all_results) > 1:
        print(f"\n\n{'=' * 110}")
        print(f"  DELTA vs FULL SYSTEM")
        print(f"{'=' * 110}")

        full = all_results['FULL']
        header3 = f"{'Config':<20} {'ΔAvgTop1':>10} {'ΔJoint':>10} {'ΔAvgCorr':>10} {'ΔW-F1':>10}"
        print(header3)
        print("-" * len(header3))

        for name, res in sorted_configs:
            if name == 'FULL':
                continue
            d_top1 = res['avg_top1'] - full['avg_top1']
            d_joint = res['joint_exact_match'] - full['joint_exact_match']
            d_corr = res['avg_correct'] - full['avg_correct']
            d_wf1 = res['avg_weighted_f1'] - full['avg_weighted_f1']
            print(f"{name:<20} {d_top1:>+10.4f} {d_joint:>+10.4f} "
                  f"{d_corr:>+10.2f} {d_wf1:>+10.4f}")

    # ── 保存结果 ──
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = save_dir / f"ablation_results_{timestamp}.json"
    serializable = make_serializable(all_results)
    with open(save_path, 'w') as f:
        json.dump(serializable, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to: {save_path}")

    print(f"\n{'=' * 80}")
    print(f"  Ablation complete.")
    print(f"{'=' * 80}")


if __name__ == "__main__":
    main()
