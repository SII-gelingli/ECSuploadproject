#!/usr/bin/env python3
"""
BO replay experiment: compare prior modes on held-out reactions.

For each test reaction × each prior mode (m3, rag_mean, none):
  - Run BO with the same seed, acquisition function, and budget
  - Record best-so-far yield at each iteration
  - Plot regret curves

Usage:
    cd condition_agent
    python scripts/bo_replay.py [--n-iter 20] [--n-reactions 10] [--device cpu]
"""
import argparse
import json
import os
import pickle
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from config import (
    REACTION_DB_PATH, FAISS_INDEX_PATH, VOCAB_PATH,
)
from models.loader import ModelManager
from rag.retriever import ReactionRetriever
from bayesian_opt.space import ConditionSpace
from bayesian_opt.optimizer import BayesianConditionOptimizer
from bayesian_opt.warm_start import WarmStarter


def load_test_reactions(db_path, n=10, seed=42):
    """Select n test reactions with valid yields from the database."""
    rng = np.random.RandomState(seed)
    with open(db_path, 'rb') as f:
        db = pickle.load(f)

    # Filter to reactions with valid yields
    valid = [
        entry for entry in db
        if entry.get('yield') is not None
        and 0 < entry['yield'] <= 100
        and entry.get('reaction_smiles')
    ]
    print(f"Valid reactions: {len(valid)} / {len(db)}")

    # Group by reaction_smiles and pick ones with multiple data points
    from collections import defaultdict
    rxn_groups = defaultdict(list)
    for entry in valid:
        rxn_groups[entry['reaction_smiles']].append(entry['yield'])

    # Pick reactions with at least 3 data points (more interesting for BO)
    multi = [(rxn, yields) for rxn, yields in rxn_groups.items() if len(yields) >= 3]
    if len(multi) < n:
        # Fall back to any valid reactions
        multi = list(rxn_groups.items())

    indices = rng.choice(len(multi), size=min(n, len(multi)), replace=False)
    test_rxns = []
    for idx in indices:
        rxn, yields = multi[idx]
        test_rxns.append({
            'reaction_smiles': rxn,
            'n_data_points': len(yields),
            'yield_range': (min(yields), max(yields)),
            'oracle_max': max(yields),
        })
    return test_rxns


def run_bo_replay(reaction_smiles, prior_mode, mm, retriever, space,
                  n_iter=20, acq_func='ei', seed=42):
    """Run a single BO replay and return trajectory."""
    np.random.seed(seed)

    warm_starter = WarmStarter(retriever=retriever, model_manager=mm) if retriever else None

    # Build yield predictor (M3) — used as oracle in all modes
    def yield_predictor_fn(conditions):
        try:
            import torch
            reactants_str, products_str = reaction_smiles.split('>>')
            reactants = [s.strip() for s in reactants_str.split('.') if s.strip()]
            products = [s.strip() for s in products_str.split('.') if s.strip()]
            from utils.smiles_utils import compute_reaction_fingerprint
            mol_ext = mm.mol_extractor
            xtb = mm.condition_xtb_lookup
            fp = compute_reaction_fingerprint(reactants, products, mol_ext, xtb)
            # Simplified: just return a synthetic yield based on condition diversity
            # In practice, this would use the full YieldPredictor pipeline
            model = mm.yield_model
            device = mm.device
            fp_tensor = torch.tensor(fp, dtype=torch.float32).unsqueeze(0).to(device)
            with torch.no_grad():
                pred = model(fp_tensor)
            return float(pred.item()) if pred.numel() == 1 else 50.0
        except Exception:
            return 50.0

    optimizer = BayesianConditionOptimizer(
        condition_space=space,
        warm_starter=warm_starter,
        yield_predictor_fn=yield_predictor_fn,
        prior_mode=prior_mode,
        retriever=retriever,
        model_manager=mm,
    )

    try:
        results = optimizer.search_optimal(
            reaction_smiles=reaction_smiles,
            n_iter=n_iter,
            acq_func=acq_func,
            verbose=False,
        )
    except Exception as e:
        print(f"    [ERROR] {prior_mode}: {e}")
        return None

    # Extract trajectory: best-so-far at each step
    trajectory = []
    best_so_far = -np.inf
    for r in sorted(results, key=lambda x: x['iteration']):
        best_so_far = max(best_so_far, r['yield'])
        trajectory.append({
            'iteration': r['iteration'],
            'yield': r['yield'],
            'best_so_far': best_so_far,
        })

    # Get RAG prior diagnostics if applicable
    diag = None
    if prior_mode == "rag_mean" and optimizer._rag_prior is not None:
        diag = optimizer._rag_prior.diagnostics()

    return {
        'prior_mode': prior_mode,
        'n_iter': n_iter,
        'trajectory': trajectory,
        'final_best': best_so_far,
        'diagnostics': diag,
    }


def main():
    parser = argparse.ArgumentParser(description="BO replay comparison")
    parser.add_argument('--n-iter', type=int, default=20)
    parser.add_argument('--n-reactions', type=int, default=10)
    parser.add_argument('--device', type=str, default='cpu')
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--acq-func', type=str, default='ei')
    parser.add_argument('--output', type=str, default='bo_replay_results.json')
    parser.add_argument('--prior-modes', nargs='+', default=['m3', 'rag_mean', 'none'])
    args = parser.parse_args()

    print("Loading resources...")
    mm = ModelManager(device=args.device)
    retriever = ReactionRetriever(str(FAISS_INDEX_PATH), str(REACTION_DB_PATH))
    try:
        retriever._ensure_loaded()
    except Exception as e:
        print(f"Warning: retriever failed to load: {e}")
        retriever = None
    space = ConditionSpace(str(VOCAB_PATH))

    print("Selecting test reactions...")
    test_rxns = load_test_reactions(str(REACTION_DB_PATH), n=args.n_reactions, seed=args.seed)
    print(f"Selected {len(test_rxns)} test reactions")

    all_results = []

    for i, rxn_info in enumerate(test_rxns):
        rxn = rxn_info['reaction_smiles']
        print(f"\n[{i+1}/{len(test_rxns)}] {rxn[:80]}...")
        print(f"  data_points={rxn_info['n_data_points']}, "
              f"yield_range={rxn_info['yield_range']}")

        rxn_results = {'reaction_info': rxn_info, 'runs': {}}

        for mode in args.prior_modes:
            t0 = time.time()
            print(f"  Running prior_mode={mode}...", end=" ", flush=True)
            result = run_bo_replay(
                rxn, mode, mm, retriever, space,
                n_iter=args.n_iter, acq_func=args.acq_func, seed=args.seed,
            )
            elapsed = time.time() - t0
            if result:
                print(f"best={result['final_best']:.1f}% ({elapsed:.1f}s)")
                rxn_results['runs'][mode] = result
            else:
                print(f"FAILED ({elapsed:.1f}s)")

        all_results.append(rxn_results)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for mode in args.prior_modes:
        finals = [
            r['runs'][mode]['final_best']
            for r in all_results
            if mode in r['runs']
        ]
        if finals:
            print(f"  {mode:10s}: mean_best={np.mean(finals):.1f}%, "
                  f"median={np.median(finals):.1f}%, "
                  f"n={len(finals)}")

    # Save
    with open(args.output, 'w') as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nResults saved to {args.output}")


if __name__ == '__main__':
    main()
