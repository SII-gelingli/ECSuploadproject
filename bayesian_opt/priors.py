"""
RAG-mean prior for Bayesian optimization.

Replaces M3 YieldPredictor (R²≈0.39, mean prediction ~98%) with a two-stage
retrieval approach: (1) find similar reactions via FAISS, (2) k-NN over
condition vectors to compute a weighted yield mean as the GP prior.
"""
import logging
import warnings
from collections import OrderedDict
from typing import Optional

import numpy as np

logger = logging.getLogger(__name__)


class RAGMeanPrior:
    """
    Two-stage RAG-based prior mean function for GP surrogate.

    Stage 1 (init): Retrieve similar reactions → build context pool of
                     (condition, yield, rxn_similarity) tuples.
    Stage 2 (call): For each candidate condition, compute cosine similarity
                     against pool vectors, select top-k neighbors, return
                     weighted yield mean.

    Compatible with YieldSurrogate.yield_predictor_fn signature:
        __call__(cond: dict) -> float
    """

    def __init__(
        self,
        retriever,
        space,
        reaction_smiles: str,
        model_manager,
        n_context: int = 50,
        k_neighbors: int = 5,
        rxn_sim_threshold: float = 0.3,
        cond_sim_threshold: float = 0.0,
        fallback_mean: float = 57.8,
        shrinkage_alpha: Optional[float] = None,
        cache_size: int = 4096,
    ):
        """
        Args:
            retriever: ReactionRetriever instance with .search() method
            space: ConditionSpace instance with .encode() method
            reaction_smiles: target reaction SMILES for this BO session
            model_manager: ModelManager providing mol_extractor and idx_maps
            n_context: number of similar reactions to retrieve (Stage 1 pool)
            k_neighbors: number of nearest neighbors for condition k-NN
            rxn_sim_threshold: minimum reaction similarity for Stage 1
            cond_sim_threshold: minimum condition similarity for Stage 2
            fallback_mean: global dataset yield mean, used when pool is empty
            shrinkage_alpha: if set, shrink toward fallback_mean
            cache_size: LRU cache capacity
        """
        self.retriever = retriever
        self.space = space
        self.model_manager = model_manager
        self.n_context = n_context
        self.k_neighbors = k_neighbors
        self.rxn_sim_threshold = rxn_sim_threshold
        self.cond_sim_threshold = cond_sim_threshold
        self.fallback_mean = fallback_mean
        self.shrinkage_alpha = shrinkage_alpha
        self.cache_size = cache_size

        # Diagnostics
        self.stats = {
            "total_calls": 0,
            "cache_hits": 0,
            "n_fallback_empty_pool": 0,
            "n_fallback_low_sim": 0,
            "pool_size": 0,
            "mean_rxn_sim_in_pool": 0.0,
            "yield_distribution_in_pool": (0.0, 0.0, 0.0, 0.0, 0.0),
        }

        # LRU cache
        self._cache: OrderedDict = OrderedDict()

        # Build context pool
        self.R = None          # (N, D) L2-normalized condition vectors
        self.y_pool = None     # (N,) yields
        self.sim_rxn = None    # (N,) reaction similarities
        self.pool_size = 0
        self.solvent_mixtures = []  # RAG-derived mixed solvents

        self._build_context_pool(reaction_smiles)

    # ── Stage 1: Context pool construction ─────────────────────

    def _build_context_pool(self, reaction_smiles: str):
        """Retrieve similar reactions and build the context pool."""
        from utils.smiles_utils import parse_reaction_smiles, compute_reaction_fingerprint

        try:
            reactants, products = parse_reaction_smiles(reaction_smiles)
            xtb_lookup = getattr(self.model_manager, 'condition_xtb_lookup', None)
            fp = compute_reaction_fingerprint(
                reactants, products, self.model_manager.mol_extractor, xtb_lookup
            )
        except Exception as e:
            logger.warning(f"RAGMeanPrior: failed to compute reaction FP: {e}")
            self.pool_size = 0
            self.stats["pool_size"] = 0
            return

        try:
            raw_results = self.retriever.search(
                fp,
                top_k=self.n_context,
                threshold=self.rxn_sim_threshold,
                rerank_by_yield=False,
            )
        except Exception as e:
            import traceback
            logger.warning(f"RAGMeanPrior: retriever.search failed: {e}\n{traceback.format_exc()}")
            self.pool_size = 0
            self.stats["pool_size"] = 0
            return

        pool = []
        for r in raw_results:
            y = r.get('yield')
            if y is None or y <= 0 or y > 100:
                continue
            cond = self._extract_conditions_from_result(r)
            try:
                vec = self.space.encode(cond)
            except Exception as e:
                logger.debug(f"RAGMeanPrior: encode failed for result: {e}")
                continue
            pool.append({
                'cond': cond,
                'yield': float(y),
                'sim_rxn': float(r.get('similarity', 0.0)),
                'vec': vec,
            })

        if pool:
            R_raw = np.stack([p['vec'] for p in pool], axis=0)
            # L2-normalize for cosine similarity via dot product
            norms = np.linalg.norm(R_raw, axis=1, keepdims=True) + 1e-12
            self.R = R_raw / norms
            self.y_pool = np.array([p['yield'] for p in pool])
            self.sim_rxn = np.array([p['sim_rxn'] for p in pool])
            self.pool_size = len(pool)

            # Extract solvent mixtures from similar reactions
            self._collect_solvent_mixtures(pool)

            # Update diagnostics
            self.stats["pool_size"] = self.pool_size
            self.stats["mean_rxn_sim_in_pool"] = float(np.mean(self.sim_rxn))
            self.stats["yield_distribution_in_pool"] = (
                float(np.min(self.y_pool)),
                float(np.percentile(self.y_pool, 25)),
                float(np.median(self.y_pool)),
                float(np.percentile(self.y_pool, 75)),
                float(np.max(self.y_pool)),
            )
            logger.info(
                f"RAGMeanPrior: built context pool with {self.pool_size} entries, "
                f"mean rxn sim={self.stats['mean_rxn_sim_in_pool']:.3f}, "
                f"yield median={self.stats['yield_distribution_in_pool'][2]:.1f}, "
                f"solvent mixtures={len(self.solvent_mixtures)}"
            )
        else:
            self.pool_size = 0
            self.stats["pool_size"] = 0
            self.solvent_mixtures = []
            logger.warning("RAGMeanPrior: context pool is empty, will use fallback_mean")

    def _extract_conditions_from_result(self, result: dict) -> dict:
        """Convert a retriever result dict to a standardized condition dict.

        Mirrors WarmStarter._extract_conditions_from_result logic.
        """
        from config import ELECTRODE_NAMES, CELL_TYPE_NAMES

        anode_name = result.get('anode', 'Unknown')
        cathode_name = result.get('cathode', 'Unknown')
        cell_type_name = result.get('cell_type', 'Unknown')

        anode_idx = self._name_to_idx(anode_name, ELECTRODE_NAMES)
        cathode_idx = self._name_to_idx(cathode_name, ELECTRODE_NAMES)
        cell_type_idx = self._name_to_idx(cell_type_name, CELL_TYPE_NAMES)

        # Molecular conditions
        solvents = result.get('solvents', [])
        if isinstance(solvents, str):
            solvents_list = [solvents] if solvents else []
        else:
            solvents_list = [s for s in (solvents or []) if s]
        solvent_smiles = '.'.join(solvents_list) if solvents_list else ''
        electrolyte_smiles = result.get('electrolyte', '') or ''
        reagent_smiles = result.get('reagent', '') or ''
        catalyst_smiles = result.get('catalyst', '') or ''

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
        for idx, n in name_map.items():
            if n.lower() == name.lower():
                return idx
        return default

    def _collect_solvent_mixtures(self, pool: list):
        """Extract unique solvent mixtures from the context pool.

        Collects all multi-component solvent SMILES (containing '.') seen in
        similar reactions, paired with their first-component vocab index.
        """
        solvent_vocab = self.model_manager.idx_maps.get('solvent', {})
        smiles_to_idx = {smi: idx for idx, smi in solvent_vocab.items()}

        seen = set()
        mixtures = []
        for entry in pool:
            smi = entry['cond'].get('solvent_smiles', '')
            if '.' in smi and smi not in seen:
                seen.add(smi)
                first_comp = smi.split('.')[0]
                mixtures.append({
                    'smiles': smi,
                    'index': smiles_to_idx.get(first_comp, 0),
                })
        self.solvent_mixtures = mixtures

    def _smiles_to_vocab_idx(self, cond_key: str, smiles: str) -> int:
        if not smiles:
            return 0
        idx_maps = self.model_manager.idx_maps
        rev_map = idx_maps.get(cond_key, {})
        for idx, smi in rev_map.items():
            if smi == smiles:
                return idx
        return 0

    # ── Stage 2: Per-query computation ─────────────────────────

    def __call__(self, cond: dict) -> float:
        """
        Compute prior yield for a candidate condition.

        Returns a float in [0, 100], compatible with
        YieldSurrogate.yield_predictor_fn signature.
        """
        self.stats["total_calls"] += 1

        # Cache lookup
        key = self._hash_cond(cond)
        if key in self._cache:
            self.stats["cache_hits"] += 1
            # Move to end (most recently used)
            self._cache.move_to_end(key)
            return self._cache[key]

        # Empty pool → fallback
        if self.pool_size == 0:
            val = self.fallback_mean
            self.stats["n_fallback_empty_pool"] += 1
            self._cache_put(key, val)
            return val

        # Encode query and compute cosine similarity
        try:
            q = self.space.encode(cond)
        except Exception as e:
            logger.warning(f"RAGMeanPrior: encode failed for query: {e}")
            val = self.fallback_mean
            self.stats["n_fallback_empty_pool"] += 1
            self._cache_put(key, val)
            return val

        q_norm = q / (np.linalg.norm(q) + 1e-12)
        sim_cond = self.R @ q_norm  # (N,)

        # Combined weight: reaction similarity × condition similarity
        w = self.sim_rxn * np.clip(sim_cond, 0.0, 1.0)

        # Apply condition similarity threshold
        if self.cond_sim_threshold > 0:
            mask = sim_cond >= self.cond_sim_threshold
            w = w * mask

        # Top-k selection
        if w.sum() <= 0:
            # All neighbors filtered → fall back to pool mean
            val = float(np.mean(self.y_pool))
            self.stats["n_fallback_low_sim"] += 1
        else:
            k = min(self.k_neighbors, len(w))
            if k < len(w):
                top_idx = np.argpartition(-w, k)[:k]
            else:
                top_idx = np.arange(len(w))
            w_top = w[top_idx]
            y_top = self.y_pool[top_idx]
            if w_top.sum() > 0:
                val = float(np.sum(w_top * y_top) / w_top.sum())
            else:
                val = float(np.mean(y_top))

        # Optional shrinkage toward global mean
        if self.shrinkage_alpha is not None:
            val = self.shrinkage_alpha * val + (1 - self.shrinkage_alpha) * self.fallback_mean

        # Clip and cache
        val = float(np.clip(val, 0.0, 100.0))
        self._cache_put(key, val)
        return val

    # ── Cache helpers ──────────────────────────────────────────

    @staticmethod
    def _hash_cond(cond: dict) -> tuple:
        """Create a hashable key for a condition dict."""
        return (
            cond.get('anode_index', 0),
            cond.get('cathode_index', 0),
            cond.get('cell_type_index', 0),
            cond.get('solvent_index', 0),
            cond.get('solvent_smiles', ''),
            cond.get('electrolyte_index', 0),
            cond.get('electrolyte_smiles', ''),
            cond.get('reagent_index', 0),
            cond.get('reagent_smiles', ''),
            cond.get('catalyst_index', 0),
            cond.get('catalyst_smiles', ''),
        )

    def _cache_put(self, key: tuple, val: float):
        """Insert into LRU cache, evicting oldest if full."""
        if key in self._cache:
            self._cache.move_to_end(key)
        else:
            if len(self._cache) >= self.cache_size:
                self._cache.popitem(last=False)
        self._cache[key] = val

    def clear_cache(self):
        """Clear the LRU cache (call when reaction_smiles changes)."""
        self._cache.clear()

    # ── Diagnostics ────────────────────────────────────────────

    def diagnostics(self) -> dict:
        """Return diagnostic statistics snapshot."""
        return dict(self.stats)
