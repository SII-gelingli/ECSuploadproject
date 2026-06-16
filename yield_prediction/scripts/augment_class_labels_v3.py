"""给 data_audited_v3/{train,val,test}.pt 加 v3 分类 label。

新增 label keys:
  reagent_class_v3        — int, 见 REAGENT_CLASSES
  catalyst_class_v3       — int, 见 CATALYST_CLASSES
  catalyst_mech_tags      — int (bitmask 4 bits: mediator/photoredox/HAT/chiral)
  ligand_class_v3         — int
  solvent_class_v3        — int
  electrolyte_cation      — int
  electrolyte_anion       — int
  additive_class_v3       — int
  anode_material          — int (基于老 electrode_to_id 映射 → 14 类)
  cathode_material        — int
  cell_class_v3           — int (复用现有 cell_type encoding,4 类不变 → 直接 copy)

不改动现有 labels(向后兼容)。把新 vocab 写到 vocab.json 的新键 + 更新 stats.json。
"""
import sys
import json
from pathlib import Path
from collections import Counter

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import torch
from tqdm import tqdm
from rdkit import RDLogger
RDLogger.logger().setLevel(RDLogger.ERROR)

PROJECT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT))

from utils.classifier_v3 import (
    classify_reagent, classify_catalyst, classify_ligand, classify_solvent,
    classify_electrolyte, classify_additive, classify_anode_from_id,
    REAGENT_NAME2ID, CATALYST_NAME2ID, LIGAND_NAME2ID, SOLVENT_NAME2ID,
    CATION_NAME2ID, ANION_NAME2ID, ADDITIVE_NAME2ID, ELECTRODE_NAME2ID,
    TAG_NAME2BIT,
    REAGENT_CLASSES, CATALYST_CLASSES, LIGAND_CLASSES, SOLVENT_CLASSES,
    ELECTROLYTE_CATIONS, ELECTROLYTE_ANIONS, ADDITIVE_CLASSES,
    ANODE_CATHODE_CLASSES, CELL_CLASSES, CATALYST_TAGS,
)

DATA_DIR = PROJECT / 'data_audited_v3'
SPLITS = ['train', 'val', 'test']


def build_smi_classifiers(vocab: dict):
    """对 vocab 里每个 SMILES 预先分类,避免每条 record 都跑 SMARTS。
    返回 dict: head -> {old_idx: new_label}。
    """
    idx_lookup = {}

    # reagent: int -> reagent_class_v3 id, catalyst_class_v3 id (跨 head 同名), additive_class_v3 id
    reagent_idx_to_smi = {v: k for k, v in vocab['reagent'].items()}
    idx_lookup['reagent->reagent_class_v3'] = {}
    for idx, smi in tqdm(reagent_idx_to_smi.items(), desc='reagent'):
        s = '' if smi.startswith('__') else smi
        idx_lookup['reagent->reagent_class_v3'][idx] = REAGENT_NAME2ID[classify_reagent(s)]

    catalyst_idx_to_smi = {v: k for k, v in vocab['catalyst'].items()}
    idx_lookup['catalyst->catalyst_class_v3'] = {}
    idx_lookup['catalyst->catalyst_mech_tags'] = {}
    for idx, smi in tqdm(catalyst_idx_to_smi.items(), desc='catalyst'):
        s = '' if smi.startswith('__') else smi
        cls, tags = classify_catalyst(s)
        idx_lookup['catalyst->catalyst_class_v3'][idx] = CATALYST_NAME2ID[cls]
        bits = 0
        for t in tags:
            bits |= TAG_NAME2BIT.get(t, 0)
        idx_lookup['catalyst->catalyst_mech_tags'][idx] = bits

    ligand_idx_to_smi = {v: k for k, v in vocab['ligand'].items()}
    idx_lookup['ligand->ligand_class_v3'] = {}
    for idx, smi in tqdm(ligand_idx_to_smi.items(), desc='ligand'):
        s = '' if smi.startswith('__') else smi
        idx_lookup['ligand->ligand_class_v3'][idx] = LIGAND_NAME2ID[classify_ligand(s)]

    solvent_idx_to_smi = {v: k for k, v in vocab['solvent'].items()}
    idx_lookup['solvent->solvent_class_v3'] = {}
    for idx, smi in tqdm(solvent_idx_to_smi.items(), desc='solvent'):
        s = '' if smi.startswith('__') else smi
        idx_lookup['solvent->solvent_class_v3'][idx] = SOLVENT_NAME2ID[classify_solvent(s)]

    elec_idx_to_smi = {v: k for k, v in vocab['electrolyte'].items()}
    idx_lookup['electrolyte->cation'] = {}
    idx_lookup['electrolyte->anion'] = {}
    for idx, smi in tqdm(elec_idx_to_smi.items(), desc='electrolyte'):
        s = '' if smi.startswith('__') else smi
        c, a = classify_electrolyte(s)
        idx_lookup['electrolyte->cation'][idx] = CATION_NAME2ID.get(
            c, CATION_NAME2ID['molecular_no_ion'])
        idx_lookup['electrolyte->anion'][idx] = ANION_NAME2ID.get(
            a, ANION_NAME2ID['molecular_no_ion'])

    addi_idx_to_smi = {v: k for k, v in vocab['additive'].items()}
    idx_lookup['additive->additive_class_v3'] = {}
    for idx, smi in tqdm(addi_idx_to_smi.items(), desc='additive'):
        s = '' if smi.startswith('__') else smi
        idx_lookup['additive->additive_class_v3'][idx] = ADDITIVE_NAME2ID[classify_additive(s)]

    # 老 electrode_to_id 0..22 → 新 anode_material/cathode_material 0..14
    idx_lookup['electrode->v3'] = {}
    for old_idx in range(23):
        idx_lookup['electrode->v3'][old_idx] = ELECTRODE_NAME2ID[classify_anode_from_id(old_idx)]

    return idx_lookup


def main():
    vocab = json.load(open(DATA_DIR / 'vocab.json'))
    print('SMILES head vocab sizes:')
    for h in ['solvent', 'electrolyte', 'catalyst', 'reagent', 'ligand', 'additive']:
        print(f"  {h}: {len(vocab[h])}")

    lookup = build_smi_classifiers(vocab)

    distributions = {}
    for split in SPLITS:
        recs = torch.load(DATA_DIR / f'{split}.pt', weights_only=False)
        dist = {k: Counter() for k in (
            'reagent_class_v3', 'catalyst_class_v3', 'catalyst_mech_tags',
            'ligand_class_v3', 'solvent_class_v3',
            'electrolyte_cation', 'electrolyte_anion',
            'additive_class_v3', 'anode_material', 'cathode_material',
            'cell_class_v3',
        )}
        for r in tqdm(recs, desc=f'augment {split}'):
            lab = r['labels']
            lab['reagent_class_v3'] = lookup['reagent->reagent_class_v3'][lab['reagent']]
            lab['catalyst_class_v3'] = lookup['catalyst->catalyst_class_v3'][lab['catalyst']]
            lab['catalyst_mech_tags'] = lookup['catalyst->catalyst_mech_tags'][lab['catalyst']]
            lab['ligand_class_v3'] = lookup['ligand->ligand_class_v3'][lab['ligand']]
            lab['solvent_class_v3'] = lookup['solvent->solvent_class_v3'][lab['solvent']]
            lab['electrolyte_cation'] = lookup['electrolyte->cation'][lab['electrolyte']]
            lab['electrolyte_anion'] = lookup['electrolyte->anion'][lab['electrolyte']]
            lab['additive_class_v3'] = lookup['additive->additive_class_v3'][lab['additive']]
            lab['anode_material'] = lookup['electrode->v3'][lab['anode']]
            lab['cathode_material'] = lookup['electrode->v3'][lab['cathode']]
            lab['cell_class_v3'] = int(lab['cell_type'])  # 4 类不变,直接复用
            for k in dist:
                dist[k][lab[k]] += 1
        torch.save(recs, DATA_DIR / f'{split}.pt')
        print(f"  saved {split}.pt ({len(recs)} records)")
        distributions[split] = dist

    # 更新 vocab.json — 加入 v3 类列表
    vocab['__v3__'] = {
        'reagent_class_v3': REAGENT_CLASSES,
        'catalyst_class_v3': CATALYST_CLASSES,
        'catalyst_mech_tags': CATALYST_TAGS,
        'ligand_class_v3': LIGAND_CLASSES,
        'solvent_class_v3': SOLVENT_CLASSES,
        'electrolyte_cation': ELECTROLYTE_CATIONS,
        'electrolyte_anion': ELECTROLYTE_ANIONS,
        'additive_class_v3': ADDITIVE_CLASSES,
        'anode_material': ANODE_CATHODE_CLASSES,
        'cathode_material': ANODE_CATHODE_CLASSES,
        'cell_class_v3': CELL_CLASSES,
    }
    with open(DATA_DIR / 'vocab.json', 'w') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=1)
    print("vocab.json 已更新")

    # 更新 stats.json
    stats = json.load(open(DATA_DIR / 'stats.json'))
    stats['num_classes_v3'] = {
        'reagent_class_v3': len(REAGENT_CLASSES),
        'catalyst_class_v3': len(CATALYST_CLASSES),
        'catalyst_mech_tags': len(CATALYST_TAGS),
        'ligand_class_v3': len(LIGAND_CLASSES),
        'solvent_class_v3': len(SOLVENT_CLASSES),
        'electrolyte_cation': len(ELECTROLYTE_CATIONS),
        'electrolyte_anion': len(ELECTROLYTE_ANIONS),
        'additive_class_v3': len(ADDITIVE_CLASSES),
        'anode_material': len(ANODE_CATHODE_CLASSES),
        'cathode_material': len(ANODE_CATHODE_CLASSES),
        'cell_class_v3': len(CELL_CLASSES),
    }
    json.dump(stats, open(DATA_DIR / 'stats.json', 'w'), indent=2)
    print("stats.json 已更新,num_classes_v3:")
    for k, v in stats['num_classes_v3'].items():
        print(f"  {k:<28} {v}")

    # 打印每个 split 的类分布(top 10)
    print()
    for split in SPLITS:
        n = sum(distributions[split]['reagent_class_v3'].values())
        print(f"\n[{split}] reagent_class_v3 top 10 (n={n}):")
        for cls_id, cnt in distributions[split]['reagent_class_v3'].most_common(10):
            print(f"  {cls_id:3d}  {REAGENT_CLASSES[cls_id]:<32}  {cnt:5d}  ({100*cnt/n:.1f}%)")

        print(f"\n[{split}] catalyst_class_v3 top 10:")
        n = sum(distributions[split]['catalyst_class_v3'].values())
        for cls_id, cnt in distributions[split]['catalyst_class_v3'].most_common(10):
            print(f"  {cls_id:3d}  {CATALYST_CLASSES[cls_id]:<32}  {cnt:5d}  ({100*cnt/n:.1f}%)")

        print(f"\n[{split}] catalyst_mech_tags distribution (bitmask):")
        n = sum(distributions[split]['catalyst_mech_tags'].values())
        for bits, cnt in distributions[split]['catalyst_mech_tags'].most_common(10):
            tag_list = [t for t in CATALYST_TAGS if bits & TAG_NAME2BIT[t]]
            label = ','.join(tag_list) if tag_list else '(none)'
            print(f"  bits={bits:04b}  {label:<32}  {cnt:5d}  ({100*cnt/n:.1f}%)")

        print(f"\n[{split}] electrolyte_cation top 10:")
        n = sum(distributions[split]['electrolyte_cation'].values())
        for cls_id, cnt in distributions[split]['electrolyte_cation'].most_common(10):
            print(f"  {cls_id:3d}  {ELECTROLYTE_CATIONS[cls_id]:<24}  {cnt:5d}  ({100*cnt/n:.1f}%)")

        print(f"\n[{split}] electrolyte_anion top 10:")
        n = sum(distributions[split]['electrolyte_anion'].values())
        for cls_id, cnt in distributions[split]['electrolyte_anion'].most_common(10):
            print(f"  {cls_id:3d}  {ELECTROLYTE_ANIONS[cls_id]:<24}  {cnt:5d}  ({100*cnt/n:.1f}%)")

        print(f"\n[{split}] anode_material distribution:")
        n = sum(distributions[split]['anode_material'].values())
        for cls_id, cnt in distributions[split]['anode_material'].most_common():
            print(f"  {cls_id:3d}  {ANODE_CATHODE_CLASSES[cls_id]:<24}  {cnt:5d}  ({100*cnt/n:.1f}%)")

        print(f"\n[{split}] cathode_material distribution:")
        n = sum(distributions[split]['cathode_material'].values())
        for cls_id, cnt in distributions[split]['cathode_material'].most_common():
            print(f"  {cls_id:3d}  {ANODE_CATHODE_CLASSES[cls_id]:<24}  {cnt:5d}  ({100*cnt/n:.1f}%)")


if __name__ == '__main__':
    main()
