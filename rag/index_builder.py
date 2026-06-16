"""
Build FAISS index from training data and alkene reaction JSON files.

Supports two data sources:
  1. train.pt — pre-processed training data with pre-computed fingerprints
  2. alkene_reactions_by_yield/*.json — CAS reaction data with raw SMILES

Builds a FAISS IndexFlatIP on L2-normalized 6144D vectors (cosine similarity).
"""
import sys
import json
import numpy as np
import pickle
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# Add project paths
_this_dir = Path(__file__).parent.parent
sys.path.insert(0, str(_this_dir))

from config import (
    TRAIN_DATA_PATH, FINGERPRINT_SIZE, FINGERPRINT_RADIUS,
    ELECTRODE_NAMES, CELL_TYPE_NAMES, VOCAB_PATH,
)


def _load_train_pt(train_data_path: str):
    """Load reactions from train.pt using pre-computed fingerprints."""
    import torch

    print(f"Loading training data from {train_data_path}...")
    train_data = torch.load(train_data_path, map_location='cpu', weights_only=False)
    print(f"  Loaded {len(train_data)} reactions")

    # Load vocab for label-to-SMILES mapping
    with open(str(VOCAB_PATH)) as f:
        vocab = json.load(f)
    idx2electrolyte = {v: k for k, v in vocab.get('electrolyte', {}).items()}
    idx2solvent = {v: k for k, v in vocab.get('solvent', {}).items()}
    idx2reagent = {v: k for k, v in vocab.get('reagent', {}).items()}
    idx2catalyst = {v: k for k, v in vocab.get('catalyst', {}).items()}

    fingerprints = []
    reaction_db = []

    for i, rxn in enumerate(train_data):
        if i % 1000 == 0:
            print(f"  Processing train.pt reaction {i}/{len(train_data)}...")

        try:
            reactants = rxn.get('reactant_smiles', [])
            products = rxn.get('product_smiles', [])

            if not reactants or not products:
                continue

            reactant_fp = rxn.get('reactant_fp')
            product_fp = rxn.get('product_fp')
            diff_fp = rxn.get('diff_fp')

            if reactant_fp is None or product_fp is None or diff_fp is None:
                continue

            fp = np.concatenate([
                np.array(reactant_fp, dtype=np.float32),
                np.array(product_fp, dtype=np.float32),
                np.array(diff_fp, dtype=np.float32),
            ])

            reaction_smiles = '.'.join(reactants) + '>>' + '.'.join(products)

            anode_idx = rxn.get('anode', 22)
            cathode_idx = rxn.get('cathode', 22)
            cell_type_idx = rxn.get('cell_type', 5)

            metadata = {
                'reaction_smiles': reaction_smiles,
                'reactants': reactants,
                'products': products,
                'yield': rxn.get('yield', None),
                'anode': ELECTRODE_NAMES.get(anode_idx, 'Unknown'),
                'cathode': ELECTRODE_NAMES.get(cathode_idx, 'Unknown'),
                'cell_type': CELL_TYPE_NAMES.get(cell_type_idx, 'Unknown'),
                'electrolyte': idx2electrolyte.get(rxn.get('electrolyte_label', 0), ''),
                'solvents': [idx2solvent.get(rxn.get('solvent_label', 0), '')] if idx2solvent.get(rxn.get('solvent_label', 0)) else [],
                'reagent': idx2reagent.get(rxn.get('reagent_label', 0), ''),
                'catalyst': idx2catalyst.get(rxn.get('catalyst_label', 0), ''),
                'source': 'train',
            }

            fingerprints.append(fp)
            reaction_db.append(metadata)
        except Exception:
            continue

    print(f"  Successfully processed {len(fingerprints)} reactions from train.pt")
    return fingerprints, reaction_db


def _load_alkene_json(json_dir: str, mol_extractor):
    """Load reactions from alkene_reactions_by_yield JSON files."""
    json_dir = Path(json_dir)
    if not json_dir.exists():
        print(f"  Alkene data directory not found: {json_dir}")
        return [], []

    json_files = sorted(json_dir.glob("yield_*.json"))
    if not json_files:
        print(f"  No yield_*.json files found in {json_dir}")
        return [], []

    fingerprints = []
    reaction_db = []
    seen_keys = set()  # 基于反应+条件组合去重
    total = 0
    failed = 0

    for jf in json_files:
        with open(jf) as f:
            reactions = json.load(f)
        total += len(reactions)

        for rxn in reactions:
            try:
                # Extract reactant and product SMILES
                reactants = [r['smiles'] for r in rxn.get('reactants', []) if r.get('smiles')]
                products = [p['smiles'] for p in rxn.get('products', []) if p.get('smiles')]

                if not reactants or not products:
                    failed += 1
                    continue

                reaction_smiles = '.'.join(reactants) + '>>' + '.'.join(products)

                # Extract conditions first (needed for dedup key)
                echem = rxn.get('electrochemistry_params', {})
                solvents = [s['smiles'] for s in rxn.get('solvents', []) if s.get('smiles')]
                catalysts = [c['smiles'] for c in rxn.get('catalysts', []) if c.get('smiles')]
                reagents = [r['smiles'] for r in rxn.get('reagents', []) if r.get('smiles')]

                anode = echem.get('anode', 'Unknown') or 'Unknown'
                cathode = echem.get('cathode', 'Unknown') or 'Unknown'
                cell_type = echem.get('cell_type', 'Unknown') or 'Unknown'
                electrolyte = echem.get('electrolyte', '') or ''
                catalyst_str = ', '.join(catalysts) if catalysts else ''

                # Deduplicate by reaction + conditions combination
                dedup_key = '|||'.join([
                    reaction_smiles,
                    anode, cathode, cell_type, electrolyte,
                    ','.join(sorted(solvents)),
                    catalyst_str,
                ])
                if dedup_key in seen_keys:
                    continue
                seen_keys.add(dedup_key)

                # Compute 6144D fingerprint
                reactant_fp = mol_extractor.encode_molecules(reactants)
                product_fp = mol_extractor.encode_molecules(products)
                diff_fp = np.abs(product_fp - reactant_fp)
                fp = np.concatenate([reactant_fp, product_fp, diff_fp]).astype(np.float32)

                # Parse yield
                raw_yield = rxn.get('product_yield', None)
                parsed_yield = None
                if raw_yield is not None:
                    try:
                        parsed_yield = float(str(raw_yield).strip().rstrip('%'))
                    except (ValueError, TypeError):
                        pass

                metadata = {
                    'reaction_smiles': reaction_smiles,
                    'reactants': reactants,
                    'products': products,
                    'yield': parsed_yield,
                    'anode': anode,
                    'cathode': cathode,
                    'cell_type': cell_type,
                    'electrolyte': electrolyte,
                    'solvents': solvents,
                    'reagent': ', '.join(reagents) if reagents else '',
                    'catalyst': catalyst_str,
                    'source': 'alkene',
                }

                fingerprints.append(fp)
                reaction_db.append(metadata)
            except Exception:
                failed += 1
                continue

    print(f"  Loaded {total} alkene reactions from {len(json_files)} files")
    print(f"  Successfully processed {len(fingerprints)} unique reaction-condition pairs ({failed} failed)")
    return fingerprints, reaction_db


def _make_dedup_key(meta: Dict) -> str:
    """
    生成去重键：反应SMILES + 条件组合

    相同反应但不同条件视为不同的实验数据点，都应保留。
    """
    parts = [
        meta.get('reaction_smiles', ''),
        meta.get('anode', ''),
        meta.get('cathode', ''),
        meta.get('cell_type', ''),
        meta.get('electrolyte', ''),
        ','.join(sorted(meta.get('solvents', []))) if meta.get('solvents') else '',
        meta.get('catalyst', ''),
    ]
    return '|||'.join(parts)


def build_faiss_index(
    train_data_path: str,
    output_index_path: str,
    output_db_path: str,
    alkene_data_dir: Optional[str] = None,
):
    """
    Build FAISS index and reaction database.

    Combines train.pt data (pre-computed FPs) with optional alkene JSON data
    (computed on the fly). Each reaction is represented by its 6144D fingerprint
    (L2-normalized). The database stores metadata: SMILES, conditions, yield.

    Note: Deduplication is based on reaction SMILES + conditions combination.
    Same reaction with different conditions are kept as different entries.
    Train.pt entries are preferred as they have pre-computed features.
    """
    fingerprints = []
    reaction_db = []
    seen_keys = set()  # 基于反应+条件去重

    # Source 1: train.pt (优先，有预计算特征)
    if train_data_path and Path(train_data_path).exists():
        fps1, db1 = _load_train_pt(train_data_path)
        for fp, meta in zip(fps1, db1):
            dedup_key = _make_dedup_key(meta)
            if dedup_key not in seen_keys:
                seen_keys.add(dedup_key)
                fingerprints.append(fp)
                reaction_db.append(meta)
        print(f"  After dedup: {len(fingerprints)} unique reaction-condition pairs from train.pt")
    elif train_data_path:
        print(f"  Warning: train.pt not found at {train_data_path}, skipping")
    else:
        print(f"  Skipping train.pt (--no_train specified)")

    # Source 2: alkene reactions JSON (跨数据源去重)
    if alkene_data_dir and Path(alkene_data_dir).exists():
        from yp_utils.feature_extractor import MolecularFeatureExtractor
        mol_extractor = MolecularFeatureExtractor(
            fingerprint_size=FINGERPRINT_SIZE,
            fingerprint_radius=FINGERPRINT_RADIUS,
        )
        fps2, db2 = _load_alkene_json(alkene_data_dir, mol_extractor)
        added = 0
        for fp, meta in zip(fps2, db2):
            dedup_key = _make_dedup_key(meta)
            if dedup_key not in seen_keys:
                seen_keys.add(dedup_key)
                fingerprints.append(fp)
                reaction_db.append(meta)
                added += 1
        print(f"  Added {added} new unique reaction-condition pairs from alkene data")

    print(f"\n  Total: {len(fingerprints)} reactions for indexing")

    if not fingerprints:
        print("  ERROR: No reactions were processed. Check data format.")
        return 0

    # Stack and L2-normalize for cosine similarity via inner product
    fp_matrix = np.stack(fingerprints)
    norms = np.linalg.norm(fp_matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    fp_matrix_normalized = fp_matrix / norms

    # Build FAISS index
    dim = fp_matrix_normalized.shape[1]
    try:
        import faiss
        index = faiss.IndexFlatIP(dim)
        index.add(fp_matrix_normalized)
        print(f"  Built FAISS IndexFlatIP with {index.ntotal} vectors, dim={dim}")

        Path(output_index_path).parent.mkdir(parents=True, exist_ok=True)
        faiss.write_index(index, output_index_path)
        print(f"  Saved FAISS index to {output_index_path}")
    except ImportError:
        Path(output_index_path).parent.mkdir(parents=True, exist_ok=True)
        np.save(output_index_path.replace('.bin', '.npy'), fp_matrix_normalized)
        print(f"  FAISS not available. Saved numpy matrix to {output_index_path.replace('.bin', '.npy')}")

    # Save reaction database
    with open(output_db_path, 'wb') as f:
        pickle.dump(reaction_db, f)
    print(f"  Saved reaction database ({len(reaction_db)} entries) to {output_db_path}")

    return len(reaction_db)
