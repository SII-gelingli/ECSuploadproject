"""
条件推荐脚本：输入反应SMILES，推荐电化学反应条件

用法:
    python recommend_conditions.py "reactant1.reactant2>>product1.product2"
    python recommend_conditions.py "reactant1.reactant2>>product1.product2" --top_k 5
    python recommend_conditions.py --interactive
"""
import os
import sys
import json
import argparse
from pathlib import Path

# 添加本地包路径
LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

import torch
import torch.nn.functional as F
import numpy as np

# 添加项目路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.condition_recommender import ConditionRecommender
from models.condition_cvae import CategoricalCVAE
from utils.feature_extractor import MolecularFeatureExtractor


# ─── Yield 重排支持 ─────────────────────────────────────────

def load_yield_model(model_path: str, device: str):
    """加载产率预测模型用于条件重排"""
    from models.yield_predictor import YieldPredictor
    checkpoint = torch.load(model_path, map_location=device, weights_only=False)
    state_dict = checkpoint['model_state_dict']
    input_dim = state_dict['encoder.0.weight'].shape[1]

    config = checkpoint.get('config', {})
    hidden_dims = config.get('model', {}).get('predictor', {}).get(
        'hidden_dims', [512, 256, 128])
    dropout = config.get('model', {}).get('predictor', {}).get('dropout', 0.2)

    # 兼容旧 checkpoint 键名：output.* → output_layer.*
    fixed_state_dict = {}
    for k, v in state_dict.items():
        if k.startswith('output.'):
            fixed_state_dict['output_layer.' + k[len('output.'):]] = v
        else:
            fixed_state_dict[k] = v

    model = YieldPredictor(input_dim=input_dim, hidden_dims=hidden_dims,
                           dropout=dropout).to(device)
    model.load_state_dict(fixed_state_dict)
    model.eval()
    print(f"  产率模型已加载 (input_dim={input_dim})")
    return model, input_dim


def rerank_by_yield(schemes, reaction_fp_base, yield_model, mol_extractor,
                    idx_maps, device='cpu'):
    """用产率模型对推荐方案打分并重排。

    对每组条件方案：构建完整特征向量 → 产率模型预测 → 按预测产率降序排列。

    Args:
        schemes: CVAE 生成的条件方案列表
        reaction_fp_base: 反应指纹 (6144D = reactant + product + diff)
        yield_model: 产率预测模型
        mol_extractor: 分子指纹提取器
        idx_maps: {electrolyte: {idx: smiles}, solvent: {idx: smiles}, ...}
        device: 设备

    Returns:
        带 predicted_yield 字段的方案列表（按预测产率降序）
    """
    for scheme in schemes:
        # 从推荐条件中提取 SMILES
        solvent_smiles = idx_maps['solvent'].get(scheme['solvent']['index'], '')
        electrolyte_smiles = idx_maps['electrolyte'].get(scheme['electrolyte']['index'], '')

        # 编码溶剂和电解质指纹
        solvent_fp = mol_extractor.get_morgan_fingerprint(solvent_smiles) if solvent_smiles else np.zeros(mol_extractor.fp_size)
        electrolyte_fp = mol_extractor.get_morgan_fingerprint(electrolyte_smiles) if electrolyte_smiles else np.zeros(mol_extractor.fp_size)

        # 电化学参数向量 (6D)
        echem_features = np.array([
            scheme['anode']['index'],
            scheme['cathode']['index'],
            0.0,  # current
            0.0,  # current_density
            0.0,  # potential
            scheme['cell_type']['index'],
        ], dtype=np.float32)

        # 拼接完整特征: [reaction_fp, solvent_fp, electrolyte_fp, echem]
        full_features = np.concatenate([
            reaction_fp_base,  # 6144
            solvent_fp,        # 2048
            electrolyte_fp,    # 2048
            echem_features     # 6
        ])

        features_tensor = torch.tensor(full_features, dtype=torch.float32).unsqueeze(0).to(device)

        with torch.no_grad():
            predicted_yield = yield_model(features_tensor).item() * 100  # 0-100%

        scheme['predicted_yield'] = predicted_yield

    schemes.sort(key=lambda s: s['predicted_yield'], reverse=True)
    return schemes


# ─── 标签映射 ───────────────────────────────────────────────

ELECTRODE_NAMES = {
    0: 'Carbon', 1: 'Graphite', 2: 'Platinum', 3: 'Glassy Carbon',
    4: 'RVC', 5: 'Nickel', 6: 'Stainless Steel', 7: 'Copper',
    8: 'Zinc', 9: 'Lead', 10: 'Gold', 11: 'Silver', 12: 'Iron',
    13: 'Magnesium', 14: 'Aluminum', 15: 'Boron-doped Diamond',
    16: 'Niobium', 17: 'Titanium', 18: 'Unknown'
}

CELL_TYPE_NAMES = {
    0: 'Undivided', 1: 'Divided', 2: 'Flow', 3: 'Sealed',
    4: 'Other', 5: 'Unknown'
}


def parse_reaction_smiles(reaction_smiles: str):
    """
    解析反应SMILES字符串

    支持格式:
        "reactants>>products"
        "reactant1.reactant2>>product1.product2"

    Returns:
        (reactant_smiles_list, product_smiles_list)
    """
    reaction_smiles = reaction_smiles.strip()
    if '>>' not in reaction_smiles:
        raise ValueError("反应SMILES格式错误，需要包含 '>>'，例如: 'CC=CC>>CC(O)CC'")

    parts = reaction_smiles.split('>>')
    if len(parts) != 2:
        raise ValueError("反应SMILES格式错误，'>>' 应该只出现一次")

    reactants_str, products_str = parts[0].strip(), parts[1].strip()

    if not reactants_str or not products_str:
        raise ValueError("反应物和产物均不能为空")

    # 按'.'分割各个分子
    reactants = [s.strip() for s in reactants_str.split('.') if s.strip()]
    products = [s.strip() for s in products_str.split('.') if s.strip()]

    return reactants, products


def compute_reaction_fingerprint(reactant_smiles: list, product_smiles: list,
                                 mol_extractor: MolecularFeatureExtractor,
                                 xtb_lookup=None) -> np.ndarray:
    """
    计算反应特征向量

    基础: 6144维反应指纹 = reactant_fp(2048) + product_fp(2048) + diff_fp(2048)
    可选: +33维 xTB/RDKit 特征 = reactant_desc(11) + product_desc(11) + diff_desc(11)
    """
    reactant_fp = mol_extractor.encode_molecules(reactant_smiles)
    product_fp = mol_extractor.encode_molecules(product_smiles)
    diff_fp = np.abs(product_fp - reactant_fp)
    fp = np.concatenate([reactant_fp, product_fp, diff_fp])

    if xtb_lookup is not None:
        r_feat = xtb_lookup.get_aggregated_features(reactant_smiles)
        p_feat = xtb_lookup.get_aggregated_features(product_smiles)
        diff_feat = [p_feat[i] - r_feat[i] for i in range(len(r_feat))]
        xtb_feat = np.array(r_feat + p_feat + diff_feat, dtype=np.float32)
        fp = np.concatenate([fp, xtb_feat])

    return fp


def load_model(model_path: str, vocab_path: str, device: str):
    """加载模型和词表"""
    # 加载词表
    with open(vocab_path) as f:
        vocab = json.load(f)

    # 构建反向映射 (index -> SMILES)
    idx_to_electrolyte = {v: k for k, v in vocab.get('electrolyte', {}).items()}
    idx_to_solvent = {v: k for k, v in vocab.get('solvent', {}).items()}
    idx_to_reagent = {v: k for k, v in vocab.get('reagent', {}).items()}
    idx_to_catalyst = {v: k for k, v in vocab.get('catalyst', {}).items()}

    # 加载checkpoint
    checkpoint = torch.load(model_path, map_location=device, weights_only=False)

    # 从checkpoint推断模型参数
    state_dict = checkpoint['model_state_dict']
    reaction_dim = state_dict['reaction_encoder.0.weight'].shape[1]
    hidden_dim = state_dict['reaction_encoder.0.weight'].shape[0]
    num_electrolytes = state_dict['electrolyte_head.weight'].shape[0]
    num_solvents = state_dict['solvent_head.weight'].shape[0]
    num_reagents = state_dict['reagent_head.weight'].shape[0]
    num_catalysts = state_dict['catalyst_head.weight'].shape[0]

    # 创建模型
    model = ConditionRecommender(
        reaction_dim=reaction_dim,
        hidden_dim=hidden_dim,
        num_anode_materials=19,
        num_cathode_materials=19,
        num_cell_types=6,
        num_electrolytes=num_electrolytes,
        num_solvents=num_solvents,
        num_reagents=num_reagents,
        num_catalysts=num_catalysts,
    ).to(device)

    model.load_state_dict(state_dict)
    model.eval()

    print(f"  模型架构: ConditionRecommender (input={reaction_dim}, hidden={hidden_dim})")
    print(f"  最佳 epoch: {checkpoint.get('epoch', '?')}")
    acc = checkpoint.get('accuracy', {})
    if acc:
        first_val = next(iter(acc.values()))
        if isinstance(first_val, dict):
            avg = sum(v[1] for v in acc.values()) / len(acc)
            print(f"  验证集平均 Top-1 准确率: {avg:.1%}")
        else:
            avg = sum(acc.values()) / len(acc)
            print(f"  验证集平均准确率: {avg:.1%}")

    return model, {
        'electrolyte': idx_to_electrolyte,
        'solvent': idx_to_solvent,
        'reagent': idx_to_reagent,
        'catalyst': idx_to_catalyst,
    }, reaction_dim


def load_cvae_model(model_path: str, vocab_path: str, device: str):
    """加载 CategoricalCVAE 模型和词表"""
    # 加载词表
    with open(vocab_path) as f:
        vocab = json.load(f)

    idx_to_electrolyte = {v: k for k, v in vocab.get('electrolyte', {}).items()}
    idx_to_solvent = {v: k for k, v in vocab.get('solvent', {}).items()}
    idx_to_reagent = {v: k for k, v in vocab.get('reagent', {}).items()}
    idx_to_catalyst = {v: k for k, v in vocab.get('catalyst', {}).items()}

    # 加载 checkpoint
    checkpoint = torch.load(model_path, map_location=device, weights_only=False)
    state_dict = checkpoint['model_state_dict']

    # 从 checkpoint 推断模型参数
    reaction_dim = state_dict['reaction_encoder.0.weight'].shape[1]
    num_electrolytes = state_dict['electrolyte_head.weight'].shape[0]
    num_solvents = state_dict['solvent_head.weight'].shape[0]
    num_reagents = state_dict['reagent_head.weight'].shape[0]
    num_catalysts = state_dict['catalyst_head.weight'].shape[0]

    model = CategoricalCVAE(
        reaction_dim=reaction_dim,
        repr_dim=256,
        latent_dim=64,
        num_anode_materials=19,
        num_cathode_materials=19,
        num_cell_types=6,
        num_electrolytes=num_electrolytes,
        num_solvents=num_solvents,
        num_reagents=num_reagents,
        num_catalysts=num_catalysts,
    ).to(device)

    model.load_state_dict(state_dict)
    model.eval()

    print(f"  模型架构: CategoricalCVAE (input={reaction_dim}, latent=64)")
    print(f"  最佳 epoch: {checkpoint.get('epoch', '?')}")
    acc = checkpoint.get('accuracy', {})
    if acc:
        first_val = next(iter(acc.values()))
        if isinstance(first_val, dict):
            avg = sum(v[1] for v in acc.values()) / len(acc)
            print(f"  验证集平均 Top-1 准确率: {avg:.1%}")
        else:
            avg = sum(acc.values()) / len(acc)
            print(f"  验证集平均准确率: {avg:.1%}")

    return model, {
        'electrolyte': idx_to_electrolyte,
        'solvent': idx_to_solvent,
        'reagent': idx_to_reagent,
        'catalyst': idx_to_catalyst,
    }, reaction_dim


SMILES_CONDITION_KEYS = {'electrolyte', 'solvent', 'reagent', 'catalyst'}

# 各条件类型中需要屏蔽的 "Unknown/缺失" 索引
# SMILES 类: index 0 保留给未知; 电极类: index 18 = Unknown; 电解槽: index 5 = Unknown
UNKNOWN_INDICES = {
    'anode': 18,
    'cathode': 18,
    'cell_type': 5,
    'electrolyte': 0,
    'solvent': 0,
    'reagent': 0,
    'catalyst': 0,
}


def recommend(model, features_tensor, idx_maps, top_k=3, device='cpu'):
    """运行模型推理，返回每个条件的 top-k 候选"""
    model.eval()
    with torch.no_grad():
        predictions = model(features_tensor.to(device))

    results = {}

    head_configs = [
        ('anode', 'anode_logits', ELECTRODE_NAMES),
        ('cathode', 'cathode_logits', ELECTRODE_NAMES),
        ('cell_type', 'cell_type_logits', CELL_TYPE_NAMES),
        ('electrolyte', 'electrolyte_logits', idx_maps['electrolyte']),
        ('solvent', 'solvent_logits', idx_maps['solvent']),
        ('reagent', 'reagent_logits', idx_maps['reagent']),
        ('catalyst', 'catalyst_logits', idx_maps['catalyst']),
    ]

    for name, logit_key, name_map in head_configs:
        logits = predictions[logit_key]
        # 屏蔽 Unknown/缺失 索引，推理时不应推荐
        if name in UNKNOWN_INDICES:
            logits = logits.clone()
            logits[:, UNKNOWN_INDICES[name]] = float('-inf')
        probs = F.softmax(logits, dim=-1)
        k = min(top_k, probs.size(-1))
        top_probs, top_indices = torch.topk(probs, k, dim=-1)

        items = []
        for idx, prob in zip(top_indices[0].tolist(), top_probs[0].tolist()):
            label = name_map.get(idx, f'Unknown (idx={idx})')
            items.append({'label': label, 'confidence': prob, 'index': idx})
        results[name] = items

    return results


def format_results(results: dict, reaction_smiles: str, top_k: int = 3):
    """格式化输出推荐结果，按 top-1/3/5/10 分层展示"""
    lines = []
    lines.append("=" * 70)
    lines.append("  电化学反应条件推荐结果")
    lines.append("=" * 70)
    lines.append(f"  反应: {reaction_smiles}")
    lines.append("-" * 70)

    section_names = {
        'anode': '阳极材料 (Anode)',
        'cathode': '阴极材料 (Cathode)',
        'cell_type': '电解槽类型 (Cell Type)',
        'electrolyte': '电解质 (Electrolyte)',
        'solvent': '溶剂 (Solvent)',
        'reagent': '试剂 (Reagent)',
        'catalyst': '催化剂 (Catalyst)',
    }

    # 展示层级: top_k 以内的所有候选
    display_tiers = [k for k in [1, 3, 5, 10] if k <= top_k]
    if top_k not in display_tiers:
        display_tiers.append(top_k)
    display_tiers.sort()

    for key, title in section_names.items():
        items = results[key]
        lines.append(f"\n  [{title}]")

        prev_tier_end = 0
        for tier in display_tiers:
            tier_end = min(tier, len(items))
            if tier_end <= prev_tier_end:
                continue
            if tier == 1:
                lines.append(f"    ★ Top-1 推荐:")
            else:
                lines.append(f"    ── Top-{tier} 候选:")
            for i in range(prev_tier_end, tier_end):
                item = items[i]
                conf = item['confidence'] * 100
                bar = '#' * int(conf / 5)
                lines.append(f"      {i+1}. {item['label']:<45s} {conf:5.1f}%  {bar}")
            prev_tier_end = tier_end

    lines.append("\n" + "=" * 70)
    return '\n'.join(lines)


def recommend_cvae(model, features_tensor, idx_maps, num_samples=10,
                   temperature=1.0, top_k=3, device='cpu'):
    """CVAE 多样化推荐：采样多组条件方案 + 每条件 top-k 候选"""
    # 1) z=0 确定性预测 → 每条件 top-k 候选
    model.eval()
    with torch.no_grad():
        z0_preds = model.recommend(features_tensor.to(device))

    name_maps = {
        'anode': ELECTRODE_NAMES,
        'cathode': ELECTRODE_NAMES,
        'cell_type': CELL_TYPE_NAMES,
        'electrolyte': idx_maps['electrolyte'],
        'solvent': idx_maps['solvent'],
        'reagent': idx_maps['reagent'],
        'catalyst': idx_maps['catalyst'],
    }

    topk_results = {}
    for cond_key, name_map in name_maps.items():
        logits = z0_preds[f'{cond_key}_logits']
        # 屏蔽 Unknown/缺失 索引
        if cond_key in UNKNOWN_INDICES:
            logits = logits.clone()
            logits[:, UNKNOWN_INDICES[cond_key]] = float('-inf')
        probs = F.softmax(logits, dim=-1)
        k = min(top_k, probs.size(-1))
        top_probs, top_indices = torch.topk(probs, k, dim=-1)
        items = []
        for idx, prob in zip(top_indices[0].tolist(), top_probs[0].tolist()):
            label = name_map.get(idx, f'Unknown (idx={idx})')
            items.append({'label': label, 'confidence': prob, 'index': idx})
        topk_results[cond_key] = items

    # 2) 多 z 采样 → 多组联合条件方案
    results = model.generate(
        features_tensor.to(device),
        num_samples=num_samples,
        temperature=temperature,
    )

    schemes = []
    seen = set()
    for r in results:
        labels = r['labels']
        preds = r['predictions']
        log_prob = r['log_prob'][0].item()

        scheme = {}
        key_tuple = []
        for cond_key in ['anode', 'cathode', 'cell_type', 'electrolyte',
                         'solvent', 'reagent', 'catalyst']:
            # 若采样到 Unknown 索引，用屏蔽后的 argmax 替代
            unk_idx = UNKNOWN_INDICES.get(cond_key)
            sampled_idx = labels[cond_key][0].item()
            if unk_idx is not None and sampled_idx == unk_idx:
                logits = preds[f'{cond_key}_logits'].clone()
                logits[:, unk_idx] = float('-inf')
                idx = logits.argmax(dim=-1)[0].item()
            else:
                idx = sampled_idx
            name = name_maps[cond_key].get(idx, f'Unknown (idx={idx})')
            scheme[cond_key] = {'label': name, 'index': idx}
            key_tuple.append(idx)

        key_tuple = tuple(key_tuple)
        if key_tuple in seen:
            continue
        seen.add(key_tuple)

        scheme['log_prob'] = log_prob
        schemes.append(scheme)

    schemes.sort(key=lambda s: s['log_prob'], reverse=True)
    return topk_results, schemes


def format_cvae_results(topk_results: dict, schemes: list, reaction_smiles: str, top_k: int = 3):
    """格式化 CVAE 推荐结果：每条件 top-k + 多样化联合方案"""
    lines = []
    lines.append("=" * 70)
    lines.append("  电化学反应条件推荐结果 (CVAE)")
    lines.append("=" * 70)
    lines.append(f"  反应: {reaction_smiles}")
    lines.append("-" * 70)

    # Part 1: 每条件 top-k 候选（z=0 确定性预测）
    lines.append("\n  [Part 1] 各条件 Top-K 候选 (z=0 确定性预测)")
    lines.append("  " + "-" * 50)

    section_names = {
        'anode': '阳极材料 (Anode)',
        'cathode': '阴极材料 (Cathode)',
        'cell_type': '电解槽类型 (Cell Type)',
        'electrolyte': '电解质 (Electrolyte)',
        'solvent': '溶剂 (Solvent)',
        'reagent': '试剂 (Reagent)',
        'catalyst': '催化剂 (Catalyst)',
    }

    display_tiers = [k for k in [1, 3, 5, 10] if k <= top_k]
    if top_k not in display_tiers:
        display_tiers.append(top_k)
    display_tiers.sort()

    for key, title in section_names.items():
        items = topk_results[key]
        lines.append(f"\n  [{title}]")

        prev_tier_end = 0
        for tier in display_tiers:
            tier_end = min(tier, len(items))
            if tier_end <= prev_tier_end:
                continue
            if tier == 1:
                lines.append(f"    ★ Top-1 推荐:")
            else:
                lines.append(f"    ── Top-{tier} 候选:")
            for i in range(prev_tier_end, tier_end):
                item = items[i]
                conf = item['confidence'] * 100
                bar = '#' * int(conf / 5)
                lines.append(f"      {i+1}. {item['label']:<45s} {conf:5.1f}%  {bar}")
            prev_tier_end = tier_end

    # Part 2: 多样化联合方案
    lines.append("\n" + "-" * 70)
    lines.append(f"\n  [Part 2] 多样化联合条件方案 (共 {len(schemes)} 组)")
    lines.append("  " + "-" * 50)

    short_names = {
        'anode': '阳极',
        'cathode': '阴极',
        'cell_type': '电解槽',
        'electrolyte': '电解质',
        'solvent': '溶剂',
        'reagent': '试剂',
        'catalyst': '催化剂',
    }

    for i, scheme in enumerate(schemes, 1):
        prob = np.exp(scheme['log_prob']) * 100
        header = f"  方案 {i} (联合概率: {prob:.2f}%"
        if 'predicted_yield' in scheme:
            header += f", 预测产率: {scheme['predicted_yield']:.1f}%"
        header += ")"
        lines.append(f"\n{header}")
        lines.append("  " + "-" * 40)
        for cond_key, title in short_names.items():
            label = scheme[cond_key]['label']
            lines.append(f"    {title:<12s}: {label}")

    lines.append("\n" + "=" * 70)
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='电化学反应条件推荐：输入反应SMILES，推荐最优条件',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s "CC=CC>>CC(O)CC"
  %(prog)s "C=Cc1ccccc1>>ClCC(Cl)c1ccccc1" --top_k 5
  %(prog)s --model_type cvae --num_samples 20 "CC=CC>>CC(O)CC"
  %(prog)s --interactive
        """
    )
    parser.add_argument('reaction', nargs='?', type=str,
                        help='反应SMILES (格式: "reactants>>products")')
    parser.add_argument('--top_k', type=int, default=3,
                        help='每个条件返回top-k个推荐 (默认: 3)')
    parser.add_argument('--model_type', type=str, default='default',
                        choices=['default', 'cvae'],
                        help='模型类型: default (独立分类头) 或 cvae (联合生成)')
    parser.add_argument('--num_samples', type=int, default=10,
                        help='CVAE 多样化采样数 (默认: 10)')
    parser.add_argument('--temperature', type=float, default=1.0,
                        help='CVAE 采样温度，越大越多样 (默认: 1.0)')
    parser.add_argument('--model', type=str, default=None,
                        help='模型权重路径 (默认自动选择)')
    parser.add_argument('--vocab', type=str,
                        default=str(project_root / 'checkpoints' / 'condition_model' / 'vocab.json'),
                        help='词表文件路径')
    parser.add_argument('--interactive', action='store_true',
                        help='交互模式，连续输入反应SMILES')
    parser.add_argument('--json', action='store_true',
                        help='以JSON格式输出')
    parser.add_argument('--rerank', action='store_true',
                        help='用产率预测模型对条件方案重排')
    parser.add_argument('--yield_model', type=str,
                        default=str(project_root / 'checkpoints' / 'mlp' / 'best_model.pt'),
                        help='产率模型路径 (用于 --rerank)')

    args = parser.parse_args()

    if not args.reaction and not args.interactive:
        parser.print_help()
        print("\n请提供反应SMILES或使用 --interactive 模式")
        sys.exit(1)

    # 默认模型路径
    if args.model is None:
        if args.model_type == 'cvae':
            args.model = str(project_root / 'checkpoints' / 'condition_model' / 'best_cvae_condition_model.pt')
        else:
            args.model = str(project_root / 'checkpoints' / 'condition_model' / 'best_condition_model.pt')

    # 设备
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # 加载模型
    print(f"加载模型: {args.model} (类型: {args.model_type})")
    if args.model_type == 'cvae':
        model, idx_maps, reaction_dim = load_cvae_model(args.model, args.vocab, device)
    else:
        model, idx_maps, reaction_dim = load_model(args.model, args.vocab, device)
    print(f"  设备: {device}")

    # 分子指纹提取器
    mol_extractor = MolecularFeatureExtractor(fingerprint_size=2048, fingerprint_radius=2)

    # 如果模型输入维度 > 6144，说明训练时使用了 xTB 特征，推理时也需要
    xtb_lookup = None
    if reaction_dim > 6144:
        from utils.xtb_features import XTBFeatureLookup
        xtb_csv = str(project_root / 'data' / 'xtb_reaction_molecules.csv')
        print(f"  模型需要 xTB 特征 (dim={reaction_dim}), 加载 xTB 描述符...")
        xtb_lookup = XTBFeatureLookup(xtb_csv)

    # 加载产率模型（用于重排）
    yield_model = None
    if args.rerank:
        print(f"加载产率模型用于重排: {args.yield_model}")
        yield_model, _ = load_yield_model(args.yield_model, device)

    print("模型加载完成!\n")

    def process_reaction(reaction_smiles: str):
        """处理单个反应"""
        reactants, products = parse_reaction_smiles(reaction_smiles)

        # 计算反应特征（指纹 + 可选 xTB）
        reaction_fp = compute_reaction_fingerprint(reactants, products, mol_extractor, xtb_lookup)
        features_tensor = torch.tensor([reaction_fp], dtype=torch.float32)

        if args.model_type == 'cvae':
            # CVAE 多样化推荐
            topk_results, schemes = recommend_cvae(
                model, features_tensor, idx_maps,
                num_samples=args.num_samples,
                temperature=args.temperature,
                top_k=args.top_k,
                device=device,
            )

            # 产率重排
            if yield_model is not None and schemes:
                reaction_fp_base = compute_reaction_fingerprint(
                    reactants, products, mol_extractor)
                schemes = rerank_by_yield(
                    schemes, reaction_fp_base, yield_model,
                    mol_extractor, idx_maps, device=device)

            if args.json:
                output = {
                    'reaction': reaction_smiles,
                    'reactants': reactants,
                    'products': products,
                    'model_type': 'cvae',
                    'top_k': args.top_k,
                    'topk_recommendations': {
                        k: [{'label': it['label'], 'confidence': it['confidence']} for it in v]
                        for k, v in topk_results.items()
                    },
                    'num_schemes': len(schemes),
                    'schemes': [
                        {k: v for k, v in s.items() if k not in ('log_prob', 'predicted_yield')}
                        | {'joint_probability': float(np.exp(s['log_prob']))}
                        | ({'predicted_yield': s['predicted_yield']} if 'predicted_yield' in s else {})
                        for s in schemes
                    ],
                }
                print(json.dumps(output, indent=2, ensure_ascii=False))
            else:
                print(format_cvae_results(topk_results, schemes, reaction_smiles, top_k=args.top_k))
        else:
            # 默认推荐
            results = recommend(model, features_tensor, idx_maps, top_k=args.top_k, device=device)
            if args.json:
                output = {
                    'reaction': reaction_smiles,
                    'reactants': reactants,
                    'products': products,
                    'top_k': args.top_k,
                    'recommendations': {
                        k: [{'label': it['label'], 'confidence': it['confidence']} for it in v]
                        for k, v in results.items()
                    },
                }
                print(json.dumps(output, indent=2, ensure_ascii=False))
            else:
                print(format_results(results, reaction_smiles, top_k=args.top_k))

    if args.interactive:
        print("交互模式 - 输入反应SMILES (输入 'q' 退出)")
        print("格式: reactants>>products (多个分子用'.'分隔)")
        print("-" * 50)

        while True:
            try:
                reaction_smiles = input("\n反应SMILES> ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n再见!")
                break

            if reaction_smiles.lower() in ('q', 'quit', 'exit', ''):
                print("再见!")
                break

            try:
                process_reaction(reaction_smiles)
            except Exception as e:
                print(f"错误: {e}")
    else:
        process_reaction(args.reaction)


if __name__ == "__main__":
    main()
