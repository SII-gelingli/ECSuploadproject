#!/usr/bin/env python
"""
Demo script: test the electrochemical condition agent tools without Claude API.

This script directly invokes the 6 tools to verify that models load correctly
and produce reasonable outputs. Useful for testing before running the full agent.

Usage:
    python demo.py
    python demo.py --device cuda
    python demo.py --reaction "C=Cc1ccccc1.O>>OCC(O)c1ccccc1"
"""
import sys
import json
import argparse
from pathlib import Path

_this_dir = Path(__file__).parent
sys.path.insert(0, str(_this_dir))

from config import AgentConfig


def main():
    parser = argparse.ArgumentParser(description='Demo: test agent tools locally')
    parser.add_argument('--device', type=str, default='cpu', choices=['cpu', 'cuda'])
    parser.add_argument('--reaction', type=str,
                        default='C=Cc1ccccc1.O=C(Nc1cccc2cccnc12)c1ccccc1>>O=C1c2ccccc2CC(c2ccccc2)N1c1cccc2cccnc12',
                        help='Reaction SMILES to test')
    args = parser.parse_args()

    print("=" * 60)
    print("  Electrochemical Condition Agent — Tool Demo")
    print("=" * 60)

    # Initialize
    print("\n[1/6] Initializing models...")
    config = AgentConfig(device=args.device)

    from models.loader import ModelManager
    model_manager = ModelManager(device=config.device)

    retriever = None
    try:
        from rag.retriever import ReactionRetriever
        if Path(config.reaction_db_path).exists():
            retriever = ReactionRetriever(config.faiss_index_path, config.reaction_db_path)
            print(f"  Reaction database loaded ({retriever.num_reactions} reactions)")
    except Exception as e:
        print(f"  Retriever not available: {e}")

    from agent.tools import ToolExecutor
    executor = ToolExecutor(model_manager, retriever)

    reaction = args.reaction

    # Tool 1: validate_smiles
    print("\n[2/6] Tool: validate_smiles")
    reactant_part = reaction.split('>>')[0]
    reactant_smiles = reactant_part.split('.')
    result = json.loads(executor.execute('validate_smiles', {
        'smiles_list': reactant_smiles[:2]
    }))
    for r in result.get('results', []):
        status = 'Valid' if r.get('valid') else 'Invalid'
        print(f"  {r.get('smiles', '?')}: {status}, MW={r.get('molecular_weight', '?')}")

    # Tool 2: parse_reaction
    print("\n[3/6] Tool: parse_reaction")
    result = json.loads(executor.execute('parse_reaction', {
        'reaction_smiles': reaction
    }))
    print(f"  Reactants: {result.get('num_reactants', '?')}, Products: {result.get('num_products', '?')}")

    # Tool 3: recommend_conditions_default
    print("\n[4/6] Tool: recommend_conditions_default")
    result = json.loads(executor.execute('recommend_conditions_default', {
        'reaction_smiles': reaction, 'top_k': 3
    }))
    if 'error' not in result:
        recs = result.get('recommendations', {})
        for cond_type in ['anode', 'cathode', 'cell_type', 'electrolyte', 'solvent']:
            items = recs.get(cond_type, [])
            top = items[0] if items else {}
            print(f"  {cond_type}: {top.get('label', '?')} (conf={top.get('confidence', '?')})")
    else:
        print(f"  Error: {result['error']}")

    # Tool 4: generate_conditions_cvae
    print("\n[5/6] Tool: generate_conditions_cvae")
    result = json.loads(executor.execute('generate_conditions_cvae', {
        'reaction_smiles': reaction, 'num_samples': 5, 'top_k': 2
    }))
    if 'error' not in result:
        schemes = result.get('joint_schemes', [])
        print(f"  Generated {result.get('num_unique_schemes', 0)} unique condition schemes")
        if schemes:
            best = schemes[0]
            print(f"  Best scheme (prob={best.get('joint_probability', '?')}):")
            for k in ['anode', 'cathode', 'cell_type', 'electrolyte', 'solvent']:
                print(f"    {k}: {best.get(k, {}).get('label', '?')}")
    else:
        print(f"  Error: {result['error']}")

    # Tool 5: predict_yield
    print("\n[6/6] Tool: predict_yield")
    # Use the top recommended conditions for yield prediction
    cond_result = json.loads(executor.execute('recommend_conditions_default', {
        'reaction_smiles': reaction, 'top_k': 1
    }))
    if 'error' not in cond_result:
        recs = cond_result.get('recommendations', {})
        solvent_smiles = recs.get('solvent', [{}])[0].get('label', '')
        electrolyte_smiles = recs.get('electrolyte', [{}])[0].get('label', '')
        anode_idx = recs.get('anode', [{}])[0].get('index', 0)
        cathode_idx = recs.get('cathode', [{}])[0].get('index', 0)
        cell_type_idx = recs.get('cell_type', [{}])[0].get('index', 0)

        result = json.loads(executor.execute('predict_yield', {
            'reaction_smiles': reaction,
            'conditions': [{
                'solvent_smiles': solvent_smiles,
                'electrolyte_smiles': electrolyte_smiles,
                'anode_index': anode_idx,
                'cathode_index': cathode_idx,
                'cell_type_index': cell_type_idx,
            }]
        }))
        if 'error' not in result:
            preds = result.get('yield_predictions', [])
            if preds:
                print(f"  Predicted yield: {preds[0].get('predicted_yield', '?')}%")
        else:
            print(f"  Error: {result['error']}")

    # Tool 6: search_similar_reactions
    if retriever:
        print("\n[Bonus] Tool: search_similar_reactions")
        result = json.loads(executor.execute('search_similar_reactions', {
            'reaction_smiles': reaction, 'top_k': 3
        }))
        if 'error' not in result:
            print(f"  Found {result.get('num_results', 0)} similar reactions (from {result.get('database_size', '?')} total)")
            for r in result.get('similar_reactions', [])[:3]:
                print(f"    similarity={r.get('similarity', '?'):.3f}, yield={r.get('yield', '?')}%, rxn={r.get('reaction_smiles', '?')[:60]}...")
        else:
            print(f"  {result['error']}")
    else:
        print("\n[Bonus] Tool: search_similar_reactions — SKIPPED (index not built)")

    print("\n" + "=" * 60)
    print("  Demo complete! All tools working.")
    print("=" * 60)


if __name__ == '__main__':
    main()
