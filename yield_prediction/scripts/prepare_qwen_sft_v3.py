"""Convert data_audited_v3_clean .pt files into ChatML JSONL for Qwen SFT.

Improvements over prepare_qwen_sft.py:
- Uses v3 cleaned data (canonical SMILES, electrolyte_name_map applied, cell_type cleaned)
- Includes 8 condition fields: + ligands, + additives (vs 7 before)
- Paper-level split inherited from v3_clean/split_meta.json
- For multi-item fields, uses set_labels (model can learn multi-solvent etc.)
- OTHER (vocab idx=1) entries are dropped from output lists (rare SMILES, no canonical form)
"""
import json
import sys
from pathlib import Path
from collections import Counter

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import torch

PROJECT = Path("/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/yield_prediction")
sys.path.insert(0, str(PROJECT))

from utils.electrode_normalizer import ID_TO_ELECTRODE, NUM_ELECTRODE_TYPES

DATA_DIR = PROJECT / "data_audited_v3_clean"
OUT_DIR = PROJECT / "data_qwen_sft_v3"

CELL_TYPE_STR = {0: "undivided", 1: "divided", 2: "flow", 3: ""}

# vocab indices: 0=ABSENT, 1=OTHER, ≥2=real SMILES
ABSENT_IDX = 0
OTHER_IDX = 1

LIST_FIELDS = ('solvents', 'electrolytes', 'reagents', 'catalysts', 'ligands', 'additives')
LIST_FIELD_TO_VOCAB = {
    'solvents': 'solvent',
    'electrolytes': 'electrolyte',
    'reagents': 'reagent',
    'catalysts': 'catalyst',
    'ligands': 'ligand',
    'additives': 'additive',
}
# Which fields are stored as set_labels (list of indices) vs single label
SET_FIELDS = {'solvent', 'reagent', 'catalyst'}  # from v3 schema

SYSTEM_PROMPT = (
    "You are an expert in electrochemical organic synthesis. "
    "Given an alkene electrochemistry reaction (reactants and product as SMILES), "
    "recommend reaction conditions. Respond with a single JSON object containing the keys: "
    "anode, cathode, cell_type, electrolytes, solvents, reagents, catalysts, ligands, additives. "
    "anode and cathode are short electrode-material strings (e.g. \"graphite\", \"platinum\", "
    "\"carbon_felt\"); cell_type is \"undivided\", \"divided\", \"flow\", or \"\". "
    "Each of electrolytes/solvents/reagents/catalysts/ligands/additives is a list of "
    "SMILES strings (empty list if not used). "
    "Do not include any text outside the JSON object."
)


def build_inverse_vocab(vocab: dict) -> dict:
    """For each vocab category, return idx → SMILES."""
    inv = {}
    for cat in ('solvent', 'electrolyte', 'catalyst', 'reagent', 'ligand', 'additive'):
        inv[cat] = {idx: smi for smi, idx in vocab[cat].items()}
    return inv


def labels_to_smiles_list(rec: dict, vocab_inv: dict, field: str) -> list:
    """Map class indices to SMILES, dropping ABSENT and OTHER. Uses set_labels if available."""
    set_labels = rec.get('set_labels', {})
    labels = rec.get('labels', {})
    indices: list = []
    if field in SET_FIELDS and field in set_labels:
        indices = list(set_labels[field])
    else:
        idx = labels.get(field, 0)
        if idx and idx != ABSENT_IDX:
            indices = [idx]
    smis = []
    seen = set()
    for i in indices:
        if i == ABSENT_IDX or i == OTHER_IDX:
            continue
        smi = vocab_inv[field].get(i)
        if smi and smi not in seen:
            seen.add(smi)
            smis.append(smi)
    return smis


def electrode_str(idx: int) -> str:
    """Map electrode id to lowercase name; unknown (=22) → ''."""
    if idx is None or idx >= NUM_ELECTRODE_TYPES - 1:  # last idx is unknown/ABSENT
        return ""
    return ID_TO_ELECTRODE.get(idx, "")


def record_to_messages(rec: dict, vocab_inv: dict) -> dict | None:
    """Build one ChatML messages entry from a .pt record. Returns None if invalid."""
    reactants = rec.get('reactant_smiles') or []
    products = rec.get('product_smiles') or []
    if not reactants or not products:
        return None
    labels = rec.get('labels') or {}
    target = {
        'anode': electrode_str(labels.get('anode')),
        'cathode': electrode_str(labels.get('cathode')),
        'cell_type': CELL_TYPE_STR.get(labels.get('cell_type', 3), ""),
        'electrolytes': labels_to_smiles_list(rec, vocab_inv, 'electrolyte'),
        'solvents': labels_to_smiles_list(rec, vocab_inv, 'solvent'),
        'reagents': labels_to_smiles_list(rec, vocab_inv, 'reagent'),
        'catalysts': labels_to_smiles_list(rec, vocab_inv, 'catalyst'),
        'ligands': labels_to_smiles_list(rec, vocab_inv, 'ligand'),
        'additives': labels_to_smiles_list(rec, vocab_inv, 'additive'),
    }
    # Drop reactions where every condition field is empty (no signal to learn)
    has_any = (
        target['anode'] or target['cathode'] or target['cell_type']
        or any(target[f] for f in LIST_FIELDS)
    )
    if not has_any:
        return None

    user = f"Reactants: {'.'.join(reactants)}\nProducts: {'.'.join(products)}\n\nRecommend reaction conditions."
    assistant = json.dumps(target, ensure_ascii=False, separators=(',', ':'))
    return {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant},
        ],
    }


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    vocab = json.loads((DATA_DIR / 'vocab.json').read_text())
    vocab_inv = build_inverse_vocab(vocab)
    print(f"Loaded vocab: " + ", ".join(f"{k}={len(vocab[k])}" for k in ('solvent','electrolyte','catalyst','reagent','ligand','additive')))

    stats = {}
    for split in ('train', 'val', 'test'):
        records = torch.load(DATA_DIR / f'{split}.pt', weights_only=False)
        kept, skipped = [], 0
        for rec in records:
            ex = record_to_messages(rec, vocab_inv)
            if ex is None:
                skipped += 1
                continue
            kept.append(ex)
        out_path = OUT_DIR / f'{split}.jsonl'
        with open(out_path, 'w') as f:
            for ex in kept:
                f.write(json.dumps(ex, ensure_ascii=False) + '\n')
        print(f"{split}: kept={len(kept)} skipped={skipped} → {out_path}")
        stats[split] = {'kept': len(kept), 'skipped': skipped}

    (OUT_DIR / 'stats.json').write_text(json.dumps({
        'source': str(DATA_DIR),
        'system_prompt': SYSTEM_PROMPT,
        'splits': stats,
    }, indent=2, ensure_ascii=False))
    print(f"\nwrote {OUT_DIR / 'stats.json'}")


if __name__ == "__main__":
    main()
