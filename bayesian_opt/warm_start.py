"""
Warm-start module for Bayesian optimization.

Uses RAG retrieval of similar reactions + M1 model predictions
to provide initial observations and candidates for the GP surrogate,
avoiding cold-start issues.
"""
import numpy as np
import torch
import torch.nn.functional as F
from typing import List, Dict, Tuple, Optional

from config import (
    ELECTRODE_NAMES, CELL_TYPE_NAMES, UNKNOWN_INDICES,
    FINGERPRINT_SIZE, SMILES_CONDITION_KEYS,
)
from utils.smiles_utils import parse_reaction_smiles, compute_reaction_fingerprint


# Top solvent mixtures observed in the training set (10,635 reactions, 46.3% multi-solvent).
# Each entry is a list of component SMILES; combined into a dot-SMILES for tool use.
# Ordered by frequency: MeCN+H2O, MeCN+MeOH, DCM+H2O, HFIP+MeCN, TFE+acetone, DMSO+H2O,
# DCM+MeCN, MeCN+acetone, DMF+H2O.
COMMON_SOLVENT_MIXTURES = [
    ['CC#N', 'O'],               # MeCN + H2O (1393)
    ['CC#N', 'CO'],              # MeCN + MeOH (217)
    ['ClCCl', 'O'],              # DCM + H2O (176)
    ['OCC(F)(F)F', 'CC#N'],      # HFIP + MeCN (162)
    ['OCC(F)(F)F', 'CC(C)=O'],   # TFE + acetone (112)
    ['CS(C)=O', 'O'],            # DMSO + H2O (107)
    ['ClCCl', 'CC#N'],           # DCM + MeCN (103)
    ['CC#N', 'CC(C)=O'],         # MeCN + acetone (101)
    ['CN(C)C=O', 'O'],           # DMF + H2O (99)
]


def _join_solvents(solvents) -> str:
    """Join a list of solvent SMILES into a dot-notation multi-solvent SMILES."""
    if not solvents:
        return ''
    if isinstance(solvents, str):
        return solvents
    parts = [s for s in solvents if s]
    return '.'.join(parts)


class WarmStarter:
    """
    Provides warm-start data for Bayesian optimization using:
    1. RAG retrieval — find similar reactions with known yields
    2. M1 predictions — generate candidate conditions from the classification model
    """

    def __init__(self, retriever, model_manager):
        """
        Args:
            retriever: ReactionRetriever instance (FAISS-based)
            model_manager: ModelManager instance (lazy-loads M1, yield model)
        """
        self.retriever = retriever
        self.mm = model_manager

    def get_initial_data(self, reaction_smiles: str,
                         n_similar: int = 10,
                         m1_top_k: int = 5,
                         ) -> Tuple[List[dict], List[float], List[dict]]:
        """
        Get warm-start data for a reaction.

        Returns:
            (initial_observations, initial_yields, candidates)
            - initial_observations: conditions from similar reactions (with known yields)
            - initial_yields: corresponding observed yields
            - candidates: M1-derived candidate conditions (for acquisition optimization)
        """
        initial_obs = []
        initial_yields = []
        candidates = []

        # 1. RAG retrieval — similar reactions with yields
        if self.retriever is not None:
            rag_obs, rag_yields = self._get_rag_observations(
                reaction_smiles, n_similar
            )
            initial_obs.extend(rag_obs)
            initial_yields.extend(rag_yields)

        # 2. M1 predictions → candidates
        m1_candidates = self._get_m1_candidates(reaction_smiles, m1_top_k)
        candidates.extend(m1_candidates)

        return initial_obs, initial_yields, candidates

    def _get_rag_observations(self, reaction_smiles: str,
                              n_similar: int) -> Tuple[List[dict], List[float]]:
        """
        Retrieve similar reactions and extract their conditions + yields.

        Returns:
            (conditions_list, yields_list)
        """
        reactants, products = parse_reaction_smiles(reaction_smiles)
        fp = compute_reaction_fingerprint(
            reactants, products, self.mm.mol_extractor
        )

        results = self.retriever.search(
            fp, top_k=n_similar, threshold=0.3,
            rerank_by_yield=True,
        )

        conditions_list = []
        yields_list = []

        for r in results:
            y = r.get('yield')
            if y is None or y <= 0:
                continue

            cond = self._extract_conditions_from_result(r)
            conditions_list.append(cond)
            yields_list.append(float(y))

        return conditions_list, yields_list

    def _extract_conditions_from_result(self, result: dict) -> dict:
        """Convert a retriever result dict to a standardized condition dict."""
        # Reverse-map electrode/cell_type names to indices
        anode_name = result.get('anode', 'Unknown')
        cathode_name = result.get('cathode', 'Unknown')
        cell_type_name = result.get('cell_type', 'Unknown')

        anode_idx = self._name_to_idx(anode_name, ELECTRODE_NAMES, default=0)
        cathode_idx = self._name_to_idx(cathode_name, ELECTRODE_NAMES, default=0)
        cell_type_idx = self._name_to_idx(cell_type_name, CELL_TYPE_NAMES, default=0)

        # Molecular conditions — preserve multi-solvent lists as dot-SMILES
        solvents = result.get('solvents', [])
        if isinstance(solvents, str):
            solvents_list = [solvents] if solvents else []
        else:
            solvents_list = [s for s in (solvents or []) if s]
        solvent_smiles = _join_solvents(solvents_list)
        electrolyte_smiles = result.get('electrolyte', '')
        reagent_smiles = result.get('reagent', '')
        catalyst_smiles = result.get('catalyst', '')

        # Map SMILES to vocab indices. For multi-solvent mixtures, the vocab only
        # contains pure components, so fall back to the first component's index.
        solvent_idx = self._smiles_to_vocab_idx('solvent', solvent_smiles)
        if solvent_idx == 0 and '.' in solvent_smiles:
            solvent_idx = self._smiles_to_vocab_idx('solvent', solvent_smiles.split('.')[0])
        electrolyte_idx = self._smiles_to_vocab_idx('electrolyte', electrolyte_smiles)
        reagent_idx = self._smiles_to_vocab_idx('reagent', reagent_smiles)
        catalyst_idx = self._smiles_to_vocab_idx('catalyst', catalyst_smiles)

        return {
            'anode_index': anode_idx,
            'cathode_index': cathode_idx,
            'cell_type_index': cell_type_idx,
            'solvent_index': solvent_idx,
            'solvent_smiles': solvent_smiles,
            'electrolyte_index': electrolyte_idx,
            'electrolyte_smiles': electrolyte_smiles,
            'reagent_index': reagent_idx,
            'reagent_smiles': reagent_smiles,
            'catalyst_index': catalyst_idx,
            'catalyst_smiles': catalyst_smiles,
        }

    @staticmethod
    def _name_to_idx(name: str, name_map: dict, default: int = 0) -> int:
        """Reverse-lookup: name -> index in a {idx: name} map."""
        for idx, n in name_map.items():
            if n.lower() == name.lower():
                return idx
        return default

    def _smiles_to_vocab_idx(self, cond_key: str, smiles: str) -> int:
        """Look up vocab index for a SMILES string."""
        if not smiles:
            return 0
        idx_maps = self.mm.idx_maps
        rev_map = idx_maps.get(cond_key, {})
        # rev_map is {idx: smiles}, we need {smiles: idx}
        for idx, smi in rev_map.items():
            if smi == smiles:
                return idx
        return 0

    def _get_m1_candidates(self, reaction_smiles: str,
                           top_k: int = 5) -> List[dict]:
        """
        Run M1 condition recommender and build candidate condition dicts.

        Returns list of condition dicts with top-1 base + single-swap variants.
        """
        xtb_lookup = self.mm.condition_xtb_lookup
        reactants, products = parse_reaction_smiles(reaction_smiles)
        fp = compute_reaction_fingerprint(
            reactants, products, self.mm.mol_extractor, xtb_lookup
        )
        features_tensor = torch.tensor([fp], dtype=torch.float32)

        model = self.mm.condition_model
        idx_maps = self.mm.idx_maps
        device = self.mm.device

        model.eval()
        with torch.no_grad():
            predictions = model(features_tensor.to(device))

        # Extract top-k per condition head
        head_configs = [
            ('anode', ELECTRODE_NAMES),
            ('cathode', ELECTRODE_NAMES),
            ('cell_type', CELL_TYPE_NAMES),
            ('electrolyte', idx_maps['electrolyte']),
            ('solvent', idx_maps['solvent']),
            ('reagent', idx_maps['reagent']),
            ('catalyst', idx_maps['catalyst']),
        ]

        m1_preds = {}
        for name, name_map in head_configs:
            logit_key = f'{name}_logits' if f'{name}_logits' in predictions else name
            logits = predictions[logit_key]
            if name in UNKNOWN_INDICES:
                logits = logits.clone()
                logits[:, UNKNOWN_INDICES[name]] = float('-inf')
            probs = F.softmax(logits, dim=-1)
            k = min(top_k, probs.size(-1))
            top_probs, top_indices = torch.topk(probs, k, dim=-1)

            items = []
            for idx, prob in zip(top_indices[0].tolist(), top_probs[0].tolist()):
                items.append({
                    'index': idx,
                    'confidence': round(prob, 4),
                    'label': name_map.get(idx, f'idx={idx}'),
                })
            m1_preds[name] = items

        # Build candidate set from M1 predictions
        return self._build_candidates_from_m1(m1_preds, idx_maps, top_k)

    def _build_candidates_from_m1(self, m1_preds: dict, idx_maps: dict,
                                   top_k: int) -> List[dict]:
        """Build candidate condition dicts from M1 top-k predictions."""
        # Base: all top-1
        base = {
            'anode_index': m1_preds['anode'][0]['index'],
            'cathode_index': m1_preds['cathode'][0]['index'],
            'cell_type_index': m1_preds['cell_type'][0]['index'],
        }
        for cond_key in ['solvent', 'electrolyte', 'reagent', 'catalyst']:
            idx = m1_preds[cond_key][0]['index']
            base[f'{cond_key}_index'] = idx
            base[f'{cond_key}_smiles'] = idx_maps[cond_key].get(idx, '')

        # Store M1 confidences in base
        base['_m1_confidence'] = {
            k: m1_preds[k][0]['confidence']
            for k in m1_preds
        }

        candidates = [base]

        # Single-swap variants
        all_keys = ['anode', 'cathode', 'cell_type', 'solvent', 'electrolyte',
                     'reagent', 'catalyst']
        for key in all_keys:
            for item in m1_preds[key][1:top_k]:
                variant = dict(base)
                variant.pop('_m1_confidence', None)
                alt_idx = item['index']
                if key in ('anode', 'cathode', 'cell_type'):
                    variant[f'{key}_index'] = alt_idx
                else:
                    variant[f'{key}_index'] = alt_idx
                    variant[f'{key}_smiles'] = idx_maps[key].get(alt_idx, '')
                candidates.append(variant)

        # Multi-solvent mixture variants. 46.3% of training reactions use mixtures,
        # so we enumerate the most common mixtures as candidates (dot-joined SMILES).
        # The PCA/MorganFP encoder and YieldPredictor both handle multi-component
        # SMILES natively; M1 vocab only stores pure components so we keep the
        # solvent_index pointing at the first component for bookkeeping.
        base_no_conf = dict(base)
        base_no_conf.pop('_m1_confidence', None)
        solvent_vocab = idx_maps.get('solvent', {})
        # Build {smiles: idx} reverse lookup once
        solvent_smiles_to_idx = {smi: idx for idx, smi in solvent_vocab.items()}
        seen_mixtures = set()
        for components in COMMON_SOLVENT_MIXTURES:
            mix_smiles = '.'.join(components)
            if mix_smiles in seen_mixtures:
                continue
            seen_mixtures.add(mix_smiles)
            variant = dict(base_no_conf)
            variant['solvent_smiles'] = mix_smiles
            # Use first-component vocab index (falls back to 0 if not in vocab)
            variant['solvent_index'] = solvent_smiles_to_idx.get(components[0], 0)
            candidates.append(variant)

        return candidates
