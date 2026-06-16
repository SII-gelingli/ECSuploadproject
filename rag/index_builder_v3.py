"""V3 数据 → FAISS index builder.

读 data_audited_v3_clean/train.pt (含 v3 labels), 转成 retriever 兼容的
metadata schema, 输出 faiss_index.bin + reaction_db.pkl。
"""
import sys, json, pickle
from pathlib import Path
from typing import Optional

import numpy as np
import torch


def build_v3_index(
    data_dir: str,
    vocab_path: str,
    output_index_path: str,
    output_db_path: str,
    splits=('train', 'val', 'test'),
    dedup=False,
):
    """构建 v3 检索索引: 默认含 train+val+test, 不去重."""
    all_recs = []
    for split in splits:
        sp = Path(data_dir) / f'{split}.pt'
        if not sp.exists():
            print(f'  Skipping missing split: {sp}')
            continue
        sp_data = torch.load(sp, map_location='cpu', weights_only=False)
        for r in sp_data:
            r['_split'] = split
        all_recs += sp_data
        print(f'  {split}.pt: {len(sp_data)} reactions')
    train = all_recs
    vocab = json.load(open(vocab_path))
    print(f'  TOTAL: {len(train)} reactions (dedup={dedup})')

    # Inverse maps idx → SMILES / class name
    inv = {}
    for head in ['solvent', 'electrolyte', 'catalyst', 'reagent', 'ligand', 'additive', 'anode', 'cathode']:
        if head in vocab:
            inv[head] = {v: k for k, v in vocab[head].items()}

    # v3 class names (材料家族, cation, anion, cell type)
    v3 = vocab.get('__v3__', {})
    inv['anode_material'] = {i: n for i, n in enumerate(v3.get('anode_material', []))}
    inv['cathode_material'] = {i: n for i, n in enumerate(v3.get('cathode_material', []))}
    inv['cell_class_v3'] = {i: n for i, n in enumerate(v3.get('cell_class_v3', []))}
    inv['electrolyte_cation'] = {i: n for i, n in enumerate(v3.get('electrolyte_cation', []))}
    inv['electrolyte_anion'] = {i: n for i, n in enumerate(v3.get('electrolyte_anion', []))}

    fingerprints = []
    db = []
    seen = set()

    def smis_from_set_labels(set_labels, head):
        out = []
        for idx in (set_labels or []):
            smi = inv.get(head, {}).get(idx, '')
            if smi and not smi.startswith('__'):
                out.append(smi)
        return out

    n_skip = 0
    for i, r in enumerate(train):
        if i % 2000 == 0:
            print(f'  {i}/{len(train)}', flush=True)
        try:
            reactants = r.get('reactant_smiles', [])
            products = r.get('product_smiles', [])
            if not reactants or not products:
                n_skip += 1; continue

            fp = np.concatenate([
                np.asarray(r['reactant_fp'], dtype=np.float32),
                np.asarray(r['product_fp'], dtype=np.float32),
                np.asarray(r['diff_fp'], dtype=np.float32),
            ])

            rxn_smi = '.'.join(reactants) + '>>' + '.'.join(products)
            lab = r.get('labels', {})
            sl = r.get('set_labels', {})

            # 材料家族名
            anode_mat = inv['anode_material'].get(lab.get('anode_material', 0), 'ABSENT')
            cathode_mat = inv['cathode_material'].get(lab.get('cathode_material', 0), 'ABSENT')
            cell_name = inv['cell_class_v3'].get(lab.get('cell_class_v3', 0), 'undivided')

            # Electrolyte cation+anion → SMILES (via single SMILES vocab)
            elec_smi = inv['electrolyte'].get(lab.get('electrolyte', 0), '')
            cation = inv['electrolyte_cation'].get(lab.get('electrolyte_cation', 0), '')
            anion = inv['electrolyte_anion'].get(lab.get('electrolyte_anion', 0), '')

            # 多组分: set_labels 给完整列表; fallback single SMILES if set 为空
            solvents = smis_from_set_labels(sl.get('solvent', []), 'solvent')
            if not solvents:
                s = inv['solvent'].get(lab.get('solvent', 0), '')
                if s and not s.startswith('__'): solvents = [s]
            reagents = smis_from_set_labels(sl.get('reagent', []), 'reagent')
            if not reagents:
                s = inv['reagent'].get(lab.get('reagent', 0), '')
                if s and not s.startswith('__'): reagents = [s]
            catalysts = smis_from_set_labels(sl.get('catalyst', []), 'catalyst')
            if not catalysts:
                s = inv['catalyst'].get(lab.get('catalyst', 0), '')
                if s and not s.startswith('__'): catalysts = [s]

            ligand = inv['ligand'].get(lab.get('ligand', 0), '')
            additive = inv['additive'].get(lab.get('additive', 0), '')

            metadata = {
                'reaction_smiles': rxn_smi,
                'reactants': reactants,
                'products': products,
                'yield': r.get('yield', None),
                'anode': anode_mat,
                'cathode': cathode_mat,
                'cell_type': cell_name,
                'electrolyte': elec_smi,
                'electrolyte_cation': cation,
                'electrolyte_anion': anion,
                'solvents': solvents,
                'reagent': reagents[0] if reagents else '',
                'reagents': reagents,
                'catalyst': catalysts[0] if catalysts else '',
                'catalysts': catalysts,
                'ligand': ligand if not ligand.startswith('__') else '',
                'additive': additive if not additive.startswith('__') else '',
                'source': f'v3_clean_{r.get("_split", "?")}',
            }

            if dedup:
                key = (rxn_smi, anode_mat, cathode_mat, elec_smi,
                       tuple(sorted(solvents)), tuple(sorted(reagents)),
                       tuple(sorted(catalysts)), r.get('yield'))
                if key in seen:
                    continue
                seen.add(key)

            fingerprints.append(fp)
            db.append(metadata)
        except Exception as e:
            n_skip += 1
            continue

    print(f'\n  Total: {len(fingerprints)} unique reactions (skipped {n_skip})')

    # L2 normalize + FAISS
    fp_mat = np.stack(fingerprints).astype(np.float32)
    norms = np.linalg.norm(fp_mat, axis=1, keepdims=True); norms[norms==0] = 1.0
    fp_mat /= norms

    try:
        import faiss
        index = faiss.IndexFlatIP(fp_mat.shape[1])
        index.add(fp_mat)
        Path(output_index_path).parent.mkdir(parents=True, exist_ok=True)
        faiss.write_index(index, output_index_path)
        print(f'  Wrote FAISS index ({index.ntotal} vectors) → {output_index_path}')
    except ImportError:
        np.save(output_index_path.replace('.bin', '.npy'), fp_mat)
        print(f'  faiss missing → saved numpy at {output_index_path.replace(".bin",".npy")}')

    with open(output_db_path, 'wb') as f:
        pickle.dump(db, f)
    print(f'  Wrote reaction_db ({len(db)} entries) → {output_db_path}')
    return len(db)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default='yield_prediction/data_audited_v3_clean')
    parser.add_argument('--vocab', default='yield_prediction/data_audited_v3_clean/vocab.json')
    parser.add_argument('--out_index', default='data/faiss_index.bin')
    parser.add_argument('--out_db', default='data/reaction_db.pkl')
    parser.add_argument('--no_val_test', action='store_true', help='只用 train')
    parser.add_argument('--dedup', action='store_true', help='开启去重')
    args = parser.parse_args()
    splits = ('train',) if args.no_val_test else ('train', 'val', 'test')
    build_v3_index(args.data_dir, args.vocab, args.out_index, args.out_db,
                    splits=splits, dedup=args.dedup)
