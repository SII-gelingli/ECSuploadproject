"""
BayesianConditionOptimizer: main optimizer class supporting three modes.

1. Iterative experiment optimization — suggest → observe → suggest cycles
2. Offline condition search — automated search using YieldPredictor as oracle
3. M1 candidate reranking — use GP + acquisition function to rerank M1 top-k
"""
import numpy as np
from typing import List, Dict, Optional, Tuple

from typing import Literal

from .space import ConditionSpace
from .surrogate import YieldSurrogate
from .acquisition import AcquisitionOptimizer, ACQUISITION_FUNCTIONS
from .warm_start import WarmStarter
from .priors import RAGMeanPrior

from config import ELECTRODE_NAMES, CELL_TYPE_NAMES


class BayesianConditionOptimizer:
    """
    Bayesian optimization over the electrochemical condition space.

    Wraps ConditionSpace, YieldSurrogate, and AcquisitionOptimizer into
    a unified interface supporting three usage modes:

    Mode 1 - Iterative: suggest_next() / observe() for real experiments
    Mode 2 - Offline:   search_optimal() using YieldPredictor as oracle
    Mode 3 - Reranking: rerank_candidates() to reorder M1 predictions
    """

    def __init__(self, condition_space: ConditionSpace,
                 warm_starter: Optional[WarmStarter] = None,
                 yield_predictor_fn=None,
                 prior_mode: Literal["m3", "rag_mean", "none"] = "rag_mean",
                 retriever=None,
                 model_manager=None,
                 rag_prior_kwargs: Optional[Dict] = None):
        """
        Args:
            condition_space: ConditionSpace instance
            warm_starter: WarmStarter instance (for RAG + M1 warm start)
            yield_predictor_fn: callable(conditions_dict) -> float
                Predicted yield (0-100) for a condition set.
                Used as GP prior mean (m3 mode) and as oracle in offline mode.
            prior_mode: GP prior mean strategy
                "m3"       — use yield_predictor_fn (M3 YieldPredictor), existing behavior
                "rag_mean" — use RAGMeanPrior (two-stage retrieval k-NN yield mean)
                "none"     — no prior mean, GP uses normalize_y with empirical mean
            retriever: ReactionRetriever instance (required for rag_mean mode)
            model_manager: ModelManager instance (required for rag_mean mode)
            rag_prior_kwargs: extra kwargs passed to RAGMeanPrior constructor
        """
        self.space = condition_space
        self.warm_starter = warm_starter
        self.yield_predictor_fn = yield_predictor_fn
        self.prior_mode = prior_mode
        self._retriever = retriever
        self._model_manager = model_manager
        self._rag_prior_kwargs = rag_prior_kwargs or {}
        self._rag_prior: Optional[RAGMeanPrior] = None

        # Surrogate is constructed lazily in initialize() for rag_mean mode;
        # for m3/none mode, build it immediately (backward compatible).
        if prior_mode == "none":
            self.surrogate = YieldSurrogate(
                condition_space=condition_space,
                yield_predictor_fn=None,
                use_prior_mean=False,
            )
        else:
            # m3 (default) or rag_mean (surrogate rebuilt in initialize)
            self.surrogate = YieldSurrogate(
                condition_space=condition_space,
                yield_predictor_fn=yield_predictor_fn,
            )
        self.acq_optimizer = AcquisitionOptimizer(self.surrogate)

        # State
        self._candidates_pool: List[dict] = []
        self._reaction_smiles: Optional[str] = None
        self._initialized = False

    # ── Mode 1: Iterative experiment optimization ──────────────

    def initialize(self, reaction_smiles: str,
                   n_similar: int = 10, m1_top_k: int = 5):
        """
        Initialize the optimizer for a specific reaction.

        Performs warm-start by retrieving similar reactions and M1 predictions.
        For rag_mean mode, constructs a RAGMeanPrior and rebuilds the surrogate.

        Args:
            reaction_smiles: target reaction SMILES
            n_similar: number of similar reactions to retrieve for warm-start
            m1_top_k: number of M1 top-k to use as initial candidates
        """
        self._reaction_smiles = reaction_smiles

        # Build RAG-mean prior if requested
        if self.prior_mode == "rag_mean":
            if self._retriever is None or self._model_manager is None:
                raise ValueError(
                    "prior_mode='rag_mean' requires retriever and model_manager"
                )
            self._rag_prior = RAGMeanPrior(
                retriever=self._retriever,
                space=self.space,
                reaction_smiles=reaction_smiles,
                model_manager=self._model_manager,
                **self._rag_prior_kwargs,
            )
            self.surrogate = YieldSurrogate(
                condition_space=self.space,
                yield_predictor_fn=self._rag_prior,
                use_prior_mean=True,
            )
            self.acq_optimizer = AcquisitionOptimizer(self.surrogate)

            # Pass RAG-derived solvent mixtures to condition space
            if self._rag_prior.solvent_mixtures:
                self.space.set_solvent_mixtures(self._rag_prior.solvent_mixtures)

        if self.warm_starter is not None:
            init_obs, init_yields, candidates = self.warm_starter.get_initial_data(
                reaction_smiles, n_similar=n_similar, m1_top_k=m1_top_k,
            )

            # Fit GP on warm-start data
            if init_obs and init_yields:
                self.surrogate.fit(init_obs, np.array(init_yields))

            self._candidates_pool = candidates
        else:
            # No warm start — start with random candidates
            self._candidates_pool = self.space.sample_random(50)

        self._initialized = True

    def suggest_next(self, n: int = 1, acq_func: str = 'ei',
                     pool_size: int = 200,
                     **acq_kwargs) -> List[dict]:
        """
        Suggest the next condition(s) to try.

        Builds a candidate pool from:
        1. M1 predictions (from warm start)
        2. Random samples
        3. Perturbations of the current best

        Then selects top-n by acquisition value.

        Args:
            n: number of suggestions
            acq_func: acquisition function ('ei', 'ucb', 'thompson')
            pool_size: total candidate pool size
            **acq_kwargs: extra kwargs for acquisition function

        Returns:
            List of suggested condition dicts
        """
        # Build candidate pool
        candidates = list(self._candidates_pool)

        # Add random samples
        n_random = max(0, pool_size - len(candidates))
        if n_random > 0:
            candidates.extend(self.space.sample_random(n_random))

        # Add perturbations of current best
        if self.surrogate.n_observations > 0:
            best_idx = int(np.argmax(self.surrogate.y_observed))
            best_cond = self.surrogate.X_observed[best_idx]
            candidates.extend(self.space.perturb(best_cond, n=20))

        # Deduplicate by encoding
        candidates = self._deduplicate(candidates)

        # Select by acquisition function
        results = self.acq_optimizer.optimize(
            candidates, acq_func=acq_func, n_select=n, **acq_kwargs
        )

        return [cond for cond, _ in results]

    def observe(self, conditions: dict, yield_value: float):
        """
        Record an experimental observation.

        Args:
            conditions: condition dict that was used
            yield_value: observed yield (0-100)
        """
        self.surrogate.update(conditions, yield_value)

    def get_best(self) -> Optional[dict]:
        """Return the best observed conditions so far."""
        if not self.surrogate.y_observed:
            return None
        best_idx = int(np.argmax(self.surrogate.y_observed))
        return {
            'conditions': self.surrogate.X_observed[best_idx],
            'yield': self.surrogate.y_observed[best_idx],
            'n_observations': self.surrogate.n_observations,
        }

    def suggest_with_details(self, n: int = 5, acq_func: str = 'ei',
                             pool_size: int = 200,
                             **acq_kwargs) -> List[dict]:
        """
        Like suggest_next but returns detailed prediction info.

        Returns list of dicts with 'conditions', 'acq_value',
        'predicted_mean', 'predicted_std'.
        """
        candidates = list(self._candidates_pool)
        n_random = max(0, pool_size - len(candidates))
        if n_random > 0:
            candidates.extend(self.space.sample_random(n_random))
        if self.surrogate.n_observations > 0:
            best_idx = int(np.argmax(self.surrogate.y_observed))
            best_cond = self.surrogate.X_observed[best_idx]
            candidates.extend(self.space.perturb(best_cond, n=20))

        candidates = self._deduplicate(candidates)

        return self.acq_optimizer.optimize_with_details(
            candidates, acq_func=acq_func, n_select=n, **acq_kwargs
        )

    # ── Mode 2: Offline condition search ───────────────────────

    def search_optimal(self, reaction_smiles: str,
                       n_iter: int = 50,
                       pool_size: int = 500,
                       acq_func: str = 'ei',
                       n_initial_random: int = 10,
                       verbose: bool = False,
                       ) -> List[dict]:
        """
        Offline search for optimal conditions using YieldPredictor as oracle.

        Iteratively:
        1. Suggest next conditions via acquisition function
        2. Evaluate with YieldPredictor
        3. Observe result and update GP
        4. Repeat

        Args:
            reaction_smiles: target reaction SMILES
            n_iter: number of BO iterations
            pool_size: candidate pool size per iteration
            acq_func: acquisition function
            n_initial_random: number of random initial evaluations
            verbose: print progress

        Returns:
            Top-k results sorted by yield, each with 'conditions', 'yield',
            'iteration' keys.
        """
        if self.yield_predictor_fn is None:
            raise ValueError("search_optimal requires yield_predictor_fn")

        # Initialize
        self.initialize(reaction_smiles)

        # Phase 1: evaluate initial candidates (warm-start + random)
        initial_candidates = list(self._candidates_pool)
        if len(initial_candidates) < n_initial_random:
            initial_candidates.extend(
                self.space.sample_random(n_initial_random - len(initial_candidates))
            )

        history = []
        for i, cond in enumerate(initial_candidates[:n_initial_random]):
            y = self.yield_predictor_fn(cond)
            self.observe(cond, y)
            history.append({
                'conditions': cond,
                'yield': round(y, 2),
                'iteration': 0,
                'phase': 'init',
            })

        # Phase 2: BO iterations
        for it in range(1, n_iter + 1):
            suggestions = self.suggest_next(
                n=1, acq_func=acq_func, pool_size=pool_size
            )
            if not suggestions:
                break

            cond = suggestions[0]
            y = self.yield_predictor_fn(cond)
            self.observe(cond, y)

            history.append({
                'conditions': cond,
                'yield': round(y, 2),
                'iteration': it,
                'phase': 'bo',
            })

            if verbose and it % 10 == 0:
                best = self.get_best()
                print(f"  BO iter {it}/{n_iter}: best yield = {best['yield']:.1f}%")

        # Sort by yield and return top results
        history.sort(key=lambda x: x['yield'], reverse=True)
        return history[:10]

    # ── Mode 3: M1 Candidate Reranking ─────────────────────────

    def rerank_candidates(self, candidates: List[dict],
                          reaction_smiles: str,
                          alpha: float = 0.5,
                          beta_ucb: float = 1.5,
                          m1_probs: Optional[List[float]] = None,
                          ) -> List[dict]:
        """
        Rerank M1 candidate conditions using GP-UCB scores.

        Score = alpha * m1_prob + (1-alpha) * normalized_UCB

        Args:
            candidates: list of condition dicts from M1
            reaction_smiles: target reaction SMILES
            alpha: weight for M1 probability (0-1)
            beta_ucb: UCB exploration parameter
            m1_probs: optional list of M1 probabilities per candidate.
                If not provided, all candidates get equal M1 weight.

        Returns:
            List of dicts with 'conditions', 'combined_score',
            'gp_mean', 'gp_std', 'ucb', 'm1_prob' keys.
        """
        if not candidates:
            return []

        # Initialize GP if needed
        if not self._initialized:
            self.initialize(reaction_smiles)

        # GP predictions
        mean, std = self.surrogate.predict(candidates)
        ucb = mean + beta_ucb * std

        # Normalize UCB to [0, 1]
        ucb_min, ucb_max = ucb.min(), ucb.max()
        if ucb_max > ucb_min:
            ucb_norm = (ucb - ucb_min) / (ucb_max - ucb_min)
        else:
            ucb_norm = np.ones_like(ucb) * 0.5

        # M1 probabilities
        if m1_probs is None:
            m1_probs_arr = np.ones(len(candidates)) / len(candidates)
        else:
            m1_probs_arr = np.array(m1_probs, dtype=np.float64)
            # Normalize to [0, 1]
            if m1_probs_arr.max() > 0:
                m1_probs_arr = m1_probs_arr / m1_probs_arr.max()

        # Combined score
        combined = alpha * m1_probs_arr + (1 - alpha) * ucb_norm

        # Build results
        ranked_indices = np.argsort(combined)[::-1]
        results = []
        for i in ranked_indices:
            results.append({
                'conditions': candidates[i],
                'combined_score': round(float(combined[i]), 4),
                'gp_mean': round(float(mean[i]), 2),
                'gp_std': round(float(std[i]), 2),
                'ucb': round(float(ucb[i]), 2),
                'm1_prob': round(float(m1_probs_arr[i]), 4),
            })

        return results

    # ── State management ───────────────────────────────────────

    def get_state(self) -> dict:
        """Serialize optimizer state for persistence across tool calls."""
        return {
            'reaction_smiles': self._reaction_smiles,
            'initialized': self._initialized,
            'surrogate_state': self.surrogate.get_state(),
            'candidates_pool': self._candidates_pool[:100],  # limit size
        }

    def load_state(self, state: dict):
        """Restore optimizer state from a previous session."""
        self._reaction_smiles = state.get('reaction_smiles')
        self._initialized = state.get('initialized', False)
        self._candidates_pool = state.get('candidates_pool', [])

        surrogate_state = state.get('surrogate_state', {})
        if surrogate_state:
            self.surrogate.load_state(surrogate_state)

    # ── Helpers ────────────────────────────────────────────────

    def _deduplicate(self, candidates: List[dict]) -> List[dict]:
        """Remove duplicate candidates by their encoded representation."""
        seen = set()
        unique = []
        for cond in candidates:
            # Use a hashable key based on indices
            key = (
                cond.get('anode_index', 0),
                cond.get('cathode_index', 0),
                cond.get('cell_type_index', 0),
                cond.get('solvent_index', 0),
                cond.get('electrolyte_index', 0),
                cond.get('reagent_index', 0),
                cond.get('catalyst_index', 0),
            )
            if key not in seen:
                seen.add(key)
                unique.append(cond)
        return unique

    def format_conditions(self, conditions: dict) -> dict:
        """Format a condition dict with human-readable names."""
        formatted = {}

        anode_idx = conditions.get('anode_index', 0)
        cathode_idx = conditions.get('cathode_index', 0)
        cell_type_idx = conditions.get('cell_type_index', 0)

        formatted['anode'] = {
            'index': anode_idx,
            'name': ELECTRODE_NAMES.get(anode_idx, f'idx={anode_idx}'),
        }
        formatted['cathode'] = {
            'index': cathode_idx,
            'name': ELECTRODE_NAMES.get(cathode_idx, f'idx={cathode_idx}'),
        }
        formatted['cell_type'] = {
            'index': cell_type_idx,
            'name': CELL_TYPE_NAMES.get(cell_type_idx, f'idx={cell_type_idx}'),
        }

        for cond_key in ['solvent', 'electrolyte', 'reagent', 'catalyst']:
            idx = conditions.get(f'{cond_key}_index', 0)
            smiles = conditions.get(f'{cond_key}_smiles', '')
            formatted[cond_key] = {
                'index': idx,
                'smiles': smiles,
            }

        return formatted
