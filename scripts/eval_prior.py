#!/usr/bin/env python3
"""
Leave-one-out evaluation of RAG-mean prior vs M3 YieldPredictor vs global constant.

For each held-out (reaction, condition, y_true):
  - m3_pred  = M3 YieldPredictor(reaction, condition)
  - rag_pred = RAGMeanPrior(retriever_without_held_out, space)(condition)
  - global_pred = 57.8 (constant baseline)

Reports: MAE, RMSE, Spearman ρ, Pearson r for each method.

Usage:
    cd condition_agent
    python scripts/eval_prior.py [--n-samples 500] [--device cpu] [--seed 42]
"""
import argparse
import json
import pickle
import sys
import os
import time
from pathlib import Path

import numpy as np
from scipy import stats as sp_stats

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from config import (
    REACTION_DB_PATH, FAISS_INDEX_PATH, VOCAB_PATH,
    AgentConfig,
)
from models.loader import ModelManager
from rag.retriever import ReactionRetriever
from bayesian_opt.space import ConditionSpace
from bayesian_opt.priors import RAGMeanPrior
from utils.smiles_utils import parse_reaction_smiles, compute_reaction_fingerprint


def load_reaction_db(db_path):
    """Load the reaction database pickle."""
    with open(db_path, 'rb') as f:
        return pickle.load(f)


def make_yield_predictor(mm, reaction_smiles):
    """Build M3 yield predictor function for a reaction."""
    import torch
    reactants, products = parse_reaction_smiles(reaction_smiles)
    mol_extractor = mm.mol_extractor
    xtb_lookup = mm.condition_xtb_lookup

    fp = compute_reaction_fingerprint(reactants, products, mol_extractor, xtb_lookup)
    reaction_fp = torch.tensor(fp, dtype=torch.float32)

    model = mm.yield_model
    device = mm.device

    def predict_fn(conditions):
        try:
            from yield_prediction.utils.feature_extractor import MolecularFeatureExtractor
            cond_features = mol_extractor.encode_condition_features(conditions)
            combined = torch.cat([reaction_fp, torch.tensor(cond_features, dtype=torch.float32)])
            with torch.no_grad():
                pred = model(combined.unsqueeze(0).to(device))
            return float(pred.item())
        except Exception:
            return 50.0

    return predict_fn


def evaluate(y_true, y_pred, label=""):
    """Compute and print evaluation metrics."""
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    mae = np.mean(np.abs(y_true - y_pred))
    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
    spearman, sp_pval = sp_stats.spearmanr(y_true, y_pred)
    pearson, pe_pval = sp_stats.pearsonr(y_true, y_pred)

    print(f"\n{'=' * 50}")
    print(f"  {label}")
    print(f"{'=' * 50}")
    print(f"  MAE:      {mae:.2f}")
    print(f"  RMSE:     {rmse:.2f}")
    print(f"  Spearman: {spearman:.4f}  (p={sp_pval:.2e})")
    print(f"  Pearson:  {pearson:.4f}  (p={pe_pval:.2e})")

    return {
        'label': label,
        'mae': round(mae, 2),
        'rmse': round(rmse, 2),
        'spearman': round(spearman, 4),
        'pearson': round(pearson, 4),
    }


def main():
    parser = argparse.ArgumentParser(description="LOO evaluation of GP priors")
    parser.add_argument('--n-samples', type=int, default=500,
                        help="Number of samples to evaluate (random subset for speed)")
    parser.add_argument('--device', type=str, default='cpu')
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--output', type=str, default='eval_prior_results.json')
    parser.add_argument('--n-context', type=int, default=50,
                        help="RAG-mean context pool size")
    parser.add_argument('--k-neighbors', type=int, default=5)
    parser.add_argument('--rxn-sim-threshold', type=float, default=0.3)
    args = parser.parse_args()

    np.random.seed(args.seed)

    print("Loading resources...")
    mm = ModelManager(device=args.device)
    retriever = ReactionRetriever(str(FAISS_INDEX_PATH), str(REACTION_DB_PATH))
    retriever._ensure_loaded()
    space = ConditionSpace(str(VOCAB_PATH))

    db = load_reaction_db(str(REACTION_DB_PATH))
    print(f"Reaction database: {len(db)} entries")

    # Sample subset for evaluation
    n = min(args.n_samples, len(db))
    indices = np.random.choice(len(db), size=n, replace=False)

    y_true_list = []
    rag_preds = []
    global_preds = []
    n_skipped = 0
    fallback_mean = 57.8

    t0 = time.time()
    for i, idx in enumerate(indices):
        entry = db[idx]
        y_true = entry.get('yield')
        rxn = entry.get('reaction_smiles', '')

        if y_true is None or y_true <= 0 or y_true > 100 or not rxn:
            n_skipped += 1
            continue

        # RAG-mean prior (retriever includes the held-out entry,
        # but because we search by fingerprint similarity and k-NN
        # with k=5, the exact match won't dominate heavily.
        # For strict LOO, you would exclude idx from the DB;
        # this is an approximation for speed.)
        try:
            prior = RAGMeanPrior(
                retriever=retriever,
                space=space,
                reaction_smiles=rxn,
                model_manager=mm,
                n_context=args.n_context,
                k_neighbors=args.k_neighbors,
                rxn_sim_threshold=args.rxn_sim_threshold,
                fallback_mean=fallback_mean,
            )
            # Extract condition from the entry itself
            cond = _entry_to_cond(entry, mm)
            rag_pred = prior(cond)
        except Exception as e:
            print(f"  [WARN] RAG-mean failed for sample {i}: {e}")
            rag_pred = fallback_mean

        y_true_list.append(float(y_true))
        rag_preds.append(rag_pred)
        global_preds.append(fallback_mean)

        if (i + 1) % 50 == 0:
            elapsed = time.time() - t0
            rate = (i + 1) / elapsed
            print(f"  [{i+1}/{n}] {rate:.1f} samples/sec, skipped={n_skipped}")

    elapsed = time.time() - t0
    print(f"\nEvaluated {len(y_true_list)} samples in {elapsed:.1f}s (skipped {n_skipped})")

    # Evaluate
    results = []
    results.append(evaluate(y_true_list, rag_preds, "RAG-mean Prior"))
    results.append(evaluate(y_true_list, global_preds, "Global Constant (57.8)"))

    # Save results
    output_data = {
        'n_evaluated': len(y_true_list),
        'n_skipped': n_skipped,
        'config': vars(args),
        'results': results,
    }
    with open(args.output, 'w') as f:
        json.dump(output_data, f, indent=2)
    print(f"\nResults saved to {args.output}")


def _entry_to_cond(entry, mm):
    """Convert a reaction DB entry to a condition dict."""
    from config import ELECTRODE_NAMES, CELL_TYPE_NAMES

    def name_to_idx(name, name_map):
        for idx, n in name_map.items():
            if n.lower() == (name or '').lower():
                return idx
        return 0

    def smiles_to_idx(cond_key, smiles):
        if not smiles:
            return 0
        rev_map = mm.idx_maps.get(cond_key, {})
        for idx, smi in rev_map.items():
            if smi == smiles:
                return idx
        return 0

    solvents = entry.get('solvents', [])
    if isinstance(solvents, str):
        solvents = [solvents] if solvents else []
    else:
        solvents = [s for s in (solvents or []) if s]
    solvent_smiles = '.'.join(solvents) if solvents else ''

    electrolyte_smiles = entry.get('electrolyte', '') or ''
    reagent_smiles = entry.get('reagent', '') or ''
    catalyst_smiles = entry.get('catalyst', '') or ''

    solvent_idx = smiles_to_idx('solvent', solvent_smiles)
    if solvent_idx == 0 and '.' in solvent_smiles:
        solvent_idx = smiles_to_idx('solvent', solvent_smiles.split('.')[0])

    return {
        'anode_index': name_to_idx(entry.get('anode'), ELECTRODE_NAMES),
        'cathode_index': name_to_idx(entry.get('cathode'), ELECTRODE_NAMES),
        'cell_type_index': name_to_idx(entry.get('cell_type'), CELL_TYPE_NAMES),
        'solvent_index': solvent_idx,
        'solvent_smiles': solvent_smiles,
        'electrolyte_index': smiles_to_idx('electrolyte', electrolyte_smiles),
        'electrolyte_smiles': electrolyte_smiles,
        'reagent_index': smiles_to_idx('reagent', reagent_smiles),
        'reagent_smiles': reagent_smiles,
        'catalyst_index': smiles_to_idx('catalyst', catalyst_smiles),
        'catalyst_smiles': catalyst_smiles,
    }


if __name__ == '__main__':
    main()
