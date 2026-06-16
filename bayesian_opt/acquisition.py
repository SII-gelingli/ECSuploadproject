"""
Acquisition functions for Bayesian optimization.

Implements EI / Log-EI / Noisy-EI / UCB / Thompson sampling (single + batch).

Single-point acquisitions return per-candidate scores.
Batch selection utilities (select_batch_*) return a list of chosen indices
to support parallel experiments (q-EI via Kriging Believer and Thompson batch).
"""
import numpy as np
from scipy.stats import norm
from typing import List, Dict, Tuple, Optional


def expected_improvement(mean: np.ndarray, std: np.ndarray,
                         best_y: float, xi: float = 0.01,
                         **kwargs) -> np.ndarray:
    """
    Expected Improvement acquisition function.

    EI(x) = (mean(x) - best_y - xi) * Phi(Z) + std(x) * phi(Z)
    where Z = (mean(x) - best_y - xi) / std(x)
    """
    std = np.maximum(std, 1e-8)
    z = (mean - best_y - xi) / std
    ei = (mean - best_y - xi) * norm.cdf(z) + std * norm.pdf(z)
    return np.maximum(ei, 0.0)


def log_expected_improvement(mean: np.ndarray, std: np.ndarray,
                             best_y: float, xi: float = 0.01,
                             **kwargs) -> np.ndarray:
    """Log-EI: numerically stable for large candidate pools.

    Returns log(EI + eps) so that tiny EI values don't underflow during
    sorting — important when batch size is small relative to pool size.
    """
    ei = expected_improvement(mean, std, best_y, xi)
    return np.log(ei + 1e-12)


def noisy_expected_improvement(mean: np.ndarray, std: np.ndarray,
                               best_y: float, xi: float = 0.01,
                               obs_std: float = 5.0,
                               **kwargs) -> np.ndarray:
    """Noisy-EI: a simple robust-to-noise variant.

    Treats best_y as itself uncertain (observation noise), so the improvement
    target is 'best_y + k*obs_std' rather than exact best_y. Prevents chasing
    an optimistic best when experiments are noisy (common in wet-lab yields).

    obs_std is the estimated observation noise in % yield (5.0 is a
    reasonable default for electrochemistry).
    """
    effective_best = best_y + 0.5 * obs_std  # mild penalty on believed-best
    return expected_improvement(mean, std, effective_best, xi)


def upper_confidence_bound(mean: np.ndarray, std: np.ndarray,
                           beta: float = 2.0, **kwargs) -> np.ndarray:
    """UCB(x) = mean(x) + beta * std(x). Higher beta = more exploration."""
    return mean + beta * std


def thompson_sampling(mean: np.ndarray, std: np.ndarray,
                      n_samples: int = 1, rng: Optional[np.random.Generator] = None,
                      **kwargs) -> np.ndarray:
    """Thompson Sampling: draw a single realization from the GP posterior
    (per-point Gaussian). If n_samples>1, return the mean of the draws
    (this is NOT a batch selection — use select_batch_thompson for that).
    """
    std = np.maximum(std, 1e-8)
    rng = rng if rng is not None else np.random.default_rng()
    samples = rng.normal(mean, std, size=(n_samples, len(mean)))
    return samples.mean(axis=0)


# ──────────────────────────────────────────────────────────────────────
# Batch selection utilities
# ──────────────────────────────────────────────────────────────────────

def select_batch_thompson(mean: np.ndarray, std: np.ndarray,
                          n_select: int = 4,
                          rng: Optional[np.random.Generator] = None,
                          **kwargs) -> List[int]:
    """Batch Thompson Sampling — natural diversification via independent draws.

    For each of n_select rounds, draw one posterior sample over all candidates,
    then pick argmax. Repeats-suppressed.

    This is a strong, cheap default for parallel batch BO.
    """
    rng = rng if rng is not None else np.random.default_rng()
    std = np.maximum(std, 1e-8)
    picked: List[int] = []
    picked_set = set()
    # Try up to 3x rounds to avoid repeats; fall back to sorted uniqueness.
    max_rounds = n_select * 3
    for _ in range(max_rounds):
        if len(picked) >= n_select:
            break
        sample = rng.normal(mean, std)
        # Mask already-picked
        sample_masked = sample.copy()
        for i in picked_set:
            sample_masked[i] = -np.inf
        idx = int(np.argmax(sample_masked))
        if idx not in picked_set:
            picked.append(idx)
            picked_set.add(idx)

    # Fallback: top-k by mean if still short
    if len(picked) < n_select:
        ranked = np.argsort(mean)[::-1]
        for i in ranked:
            if int(i) not in picked_set:
                picked.append(int(i))
                picked_set.add(int(i))
            if len(picked) >= n_select:
                break
    return picked


def select_batch_qei_kb(candidates_mean: np.ndarray, candidates_std: np.ndarray,
                       best_y: float, n_select: int = 4,
                       xi: float = 0.01,
                       **kwargs) -> List[int]:
    """Batch EI via Kriging Believer heuristic.

    Pick argmax EI → imagine it was observed at its predicted mean (→ update
    best_y) → pick next argmax → repeat. Cheap approximation to q-EI that
    captures 'don't suggest the same peak twice'.

    No GP refit is done (true qEI would refit after each fantasy observation,
    which is too expensive). This is why we call it heuristic.
    """
    picked: List[int] = []
    picked_set = set()
    current_best = best_y

    for _ in range(n_select):
        ei = expected_improvement(
            candidates_mean, candidates_std, current_best, xi
        )
        # Mask already-picked
        for i in picked_set:
            ei[i] = -1.0
        idx = int(np.argmax(ei))
        if ei[idx] <= 0 and picked:
            # No more improvement available; fall back to argmax mean
            ranked = np.argsort(candidates_mean)[::-1]
            for r in ranked:
                if int(r) not in picked_set:
                    idx = int(r)
                    break
        picked.append(idx)
        picked_set.add(idx)
        # Fantasy: assume we observed y = predicted mean; update best_y
        current_best = max(current_best, float(candidates_mean[idx]))

    return picked


# Registry of single-point acquisition functions
ACQUISITION_FUNCTIONS = {
    'ei': expected_improvement,
    'log_ei': log_expected_improvement,
    'noisy_ei': noisy_expected_improvement,
    'ucb': upper_confidence_bound,
    'thompson': thompson_sampling,
}

# Registry of batch selection strategies
BATCH_SELECTORS = {
    'thompson_batch': select_batch_thompson,
    'qei_kb': select_batch_qei_kb,
}


class AcquisitionOptimizer:
    """
    Optimizes acquisition function over a discrete candidate set.

    Given a GP surrogate and candidate conditions, computes acquisition values
    and returns candidates ranked by acquisition score.
    """

    def __init__(self, surrogate):
        """
        Args:
            surrogate: YieldSurrogate instance
        """
        self.surrogate = surrogate

    def optimize(self, candidates: List[dict],
                 acq_func: str = 'ei',
                 best_y: Optional[float] = None,
                 n_select: int = 1,
                 **acq_kwargs) -> List[Tuple[dict, float]]:
        """
        Rank candidates by acquisition value and return the top-n.

        Args:
            candidates: list of condition dicts to evaluate
            acq_func: acquisition function name ('ei', 'ucb', 'thompson')
            best_y: best observed yield (required for EI, ignored for UCB/Thompson)
            n_select: number of top candidates to return
            **acq_kwargs: extra kwargs passed to the acquisition function
                (e.g., xi=0.01 for EI, beta=2.0 for UCB)

        Returns:
            List of (condition_dict, acq_value) tuples, sorted descending.
        """
        if not candidates:
            return []

        # Get GP predictions
        mean, std = self.surrogate.predict(candidates)

        # Select acquisition function
        acq_fn = ACQUISITION_FUNCTIONS.get(acq_func)
        if acq_fn is None:
            raise ValueError(f"Unknown acquisition function: {acq_func}. "
                             f"Choose from {list(ACQUISITION_FUNCTIONS.keys())}")

        # Compute acquisition values
        if best_y is None:
            best_y = self.surrogate.best_yield

        acq_values = acq_fn(mean, std, best_y=best_y, **acq_kwargs)

        # Rank by acquisition value
        ranked_indices = np.argsort(acq_values)[::-1]

        results = []
        for i in ranked_indices[:n_select]:
            results.append((candidates[i], float(acq_values[i])))

        return results

    def optimize_with_details(self, candidates: List[dict],
                              acq_func: str = 'ei',
                              best_y: Optional[float] = None,
                              n_select: int = 5,
                              **acq_kwargs) -> List[dict]:
        """
        Like optimize(), but returns detailed info for each candidate.

        Returns:
            List of dicts with 'conditions', 'acq_value', 'predicted_mean',
            'predicted_std' keys.
        """
        if not candidates:
            return []

        mean, std = self.surrogate.predict(candidates)

        acq_fn = ACQUISITION_FUNCTIONS.get(acq_func)
        if acq_fn is None:
            raise ValueError(f"Unknown acquisition function: {acq_func}")

        if best_y is None:
            best_y = self.surrogate.best_yield

        acq_values = acq_fn(mean, std, best_y=best_y, **acq_kwargs)
        ranked_indices = np.argsort(acq_values)[::-1]

        results = []
        for i in ranked_indices[:n_select]:
            results.append({
                'conditions': candidates[i],
                'acq_value': round(float(acq_values[i]), 4),
                'predicted_mean': round(float(mean[i]), 2),
                'predicted_std': round(float(std[i]), 2),
            })

        return results
