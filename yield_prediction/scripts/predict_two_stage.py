"""
端到端推理: 输入 reaction SMILES (reactant>>product)，输出完整反应条件 JSON。

用法:
    python predict_two_stage.py "C=Cc1ccccc1>>OC(c1ccccc1)C(O)"

或交互模式:
    python predict_two_stage.py --interactive
"""
import sys
import json
import argparse
from pathlib import Path

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import numpy as np
import torch

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.feature_extractor import MolecularFeatureExtractor
from utils.electrode_normalizer import id_to_electrode
from models.condition_stage1 import ConditionStage1, HEAD_KEYS
from models.condition_stage2 import ConditionStage2, AMOUNT_FIELDS
from scripts.train_stage2 import inverse_transform

DATA_DIR = project_root / 'data_audited_v3'
CKPT_DIR = project_root / 'checkpoints' / 'two_stage'

ABSENT_INDEX = {'anode': 22, 'cathode': 22, 'cell_type': 3,
                'solvent': 0, 'electrolyte': 0, 'catalyst': 0,
                'reagent': 0, 'ligand': 0, 'additive': 0}

CELL_TYPES = {0: 'undivided', 1: 'divided', 2: 'flow', 3: 'ABSENT'}


def load_models(device='cuda'):
    ckpt1 = torch.load(CKPT_DIR / 'stage1_best.pt', weights_only=False)
    ckpt2 = torch.load(CKPT_DIR / 'stage2_best.pt', weights_only=False)
    nc = ckpt1['num_classes']
    vocab = json.loads((DATA_DIR / 'vocab.json').read_text())
    amount_stats = json.loads((DATA_DIR / 'amount_stats.json').read_text())

    m1 = ConditionStage1(num_classes=nc, fp_dim=ckpt1['fp_dim'],
                          hidden_dims=tuple(ckpt1['hidden_dims']),
                          dropout=ckpt1.get('dropout', 0.3)).to(device)
    m1.load_state_dict(ckpt1['model_state_dict'])
    m1.eval()

    m2 = ConditionStage2(num_classes=nc, fp_dim=ckpt2['fp_dim'],
                          hidden_dims=tuple(ckpt2['hidden_dims']),
                          dropout=ckpt2.get('dropout', 0.2)).to(device)
    m2.load_state_dict(ckpt2['model_state_dict'])
    m2.eval()

    # idx → smiles 反向表
    idx_to_smiles = {h: {v: k for k, v in vocab[h].items()} for h in vocab}

    return m1, m2, vocab, idx_to_smiles, amount_stats


def parse_reaction_smiles(smiles: str):
    if '>>' in smiles:
        left, right = smiles.split('>>', 1)
    else:
        raise ValueError("Expected format 'reactant>>product' or 'reactants.reactants>>products'")
    reactants = left.split('.')
    products = right.split('.')
    return reactants, products


def featurize(reactants, products, mol_extractor):
    r_fp = mol_extractor.encode_molecules(reactants)
    p_fp = mol_extractor.encode_molecules(products)
    diff_fp = np.abs(p_fp - r_fp)
    return np.concatenate([r_fp, p_fp, diff_fp]).astype(np.float32)


def decode_class(head, idx, idx_to_smiles_dict):
    if head in ('anode', 'cathode'):
        return id_to_electrode(idx)
    if head == 'cell_type':
        return CELL_TYPES.get(idx, f'cell_{idx}')
    # SMILES head
    table = idx_to_smiles_dict[head]
    label = table.get(idx, f'index_{idx}')
    if label == '__ABSENT__':
        return 'ABSENT'
    if label == '__OTHER__':
        return 'OTHER'
    return label


def predict_one(reaction_smiles: str, m1, m2, vocab, idx_to_smiles, amount_stats,
                 mol_extractor, device='cuda', top_k=3):
    reactants, products = parse_reaction_smiles(reaction_smiles)
    fp = featurize(reactants, products, mol_extractor)
    fp_t = torch.from_numpy(fp).unsqueeze(0).to(device)

    with torch.no_grad():
        logits = m1(fp_t)
        # 各 head argmax
        cat_pred = {k: logits[k].argmax(dim=-1) for k in HEAD_KEYS}
        # Top-K
        topk = {}
        for k in HEAD_KEYS:
            vals, idxs = logits[k].topk(min(top_k, logits[k].size(-1)), dim=-1)
            probs = torch.softmax(logits[k][0], dim=-1)
            topk[k] = [
                {'class': decode_class(k, int(idxs[0, j]), idx_to_smiles),
                 'prob': float(probs[idxs[0, j]])}
                for j in range(idxs.size(-1))
            ]

        # Stage-2
        amt = m2(fp_t, cat_pred)
        amounts = {}
        for i, f in enumerate(AMOUNT_FIELDS):
            v_norm = float(amt[f].item())
            v_real = float(inverse_transform(np.array([v_norm]), amount_stats[f])[0])
            amounts[f] = round(v_real, 3)

    # 输出
    categories = {k: decode_class(k, int(cat_pred[k].item()), idx_to_smiles) for k in HEAD_KEYS}
    result = {
        'reaction_smiles': reaction_smiles,
        'reactants': reactants,
        'products': products,
        'category_top1': categories,
        'category_topk': topk,
        'amounts': amounts,
    }
    return result


def pretty_print(result):
    print(f"\n=== Reaction: {result['reaction_smiles']} ===")
    print(f"\n[Top-1 Categories]")
    for k, v in result['category_top1'].items():
        print(f"  {k:<13} = {v}")
    print(f"\n[Top-3 Candidates per head]")
    for k, choices in result['category_topk'].items():
        s = '  ' + k.ljust(13) + ' : '
        s += '  |  '.join(f"{c['class']} ({c['prob']*100:.1f}%)" for c in choices)
        print(s)
    print(f"\n[Amounts]")
    for k, v in result['amounts'].items():
        print(f"  {k:<20} = {v}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('reaction', nargs='?', default=None,
                        help='reaction SMILES, e.g. "C=Cc1ccccc1>>OC(c1ccccc1)C(O)"')
    parser.add_argument('--interactive', action='store_true')
    parser.add_argument('--json', action='store_true', help='输出 JSON 而非美化文本')
    parser.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--top_k', type=int, default=3)
    args = parser.parse_args()

    print(f"Loading models from {CKPT_DIR}...", file=sys.stderr)
    m1, m2, vocab, idx_to_smiles, amount_stats = load_models(args.device)
    mol_extractor = MolecularFeatureExtractor(fingerprint_size=2048)

    def run(smiles):
        result = predict_one(smiles, m1, m2, vocab, idx_to_smiles, amount_stats,
                              mol_extractor, args.device, top_k=args.top_k)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            pretty_print(result)

    if args.interactive:
        print("Interactive mode. Enter reaction SMILES (or 'quit'):")
        while True:
            try:
                line = input("> ").strip()
            except EOFError:
                break
            if not line or line.lower() in ('quit', 'exit'):
                break
            try:
                run(line)
            except Exception as e:
                print(f"Error: {e}")
    elif args.reaction:
        run(args.reaction)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
