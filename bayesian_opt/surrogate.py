"""
GP Surrogate model for yield prediction in Bayesian optimization.

Key design: GP learns residuals over a YieldPredictor prior mean function,
which is more data-efficient than learning absolute yields from scratch.
"""
import numpy as np
from typing import Optional, Tuple, List, Callable

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import (
    RBF, Matern, WhiteKernel, ConstantKernel,
)


# Max observations before GP becomes too slow (~O(n^3))
MAX_OBSERVATIONS = 500

# Supported kernel names. 'matern' (nu=2.5) is a better default for chemistry
# response surfaces than 'rbf' which assumes infinite smoothness.
SUPPORTED_KERNELS = ("matern", "matern25", "matern15", "rbf")


def _make_kernel(kernel_name: str, input_dim: int,
                 length_scale_init: float = 1.0,
                 noise_level: float = 0.1,
                 use_ard: bool = True):
    """Build a GP kernel with optional ARD (per-dim length scales).

    ARD lets the kernel learn a separate length scale for each feature
    dimension — critical for high-D mixed inputs (one-hot + PCA FP),
    where many dims are irrelevant to yield and should be effectively
    ignored (long length_scale -> flat contribution).
    """
    if use_ard:
        length_scale = np.ones(input_dim, dtype=np.float64) * length_scale_init
    else:
        length_scale = length_scale_init

    if kernel_name == "rbf":
        base = RBF(length_scale=length_scale,
                   length_scale_bounds=(1e-2, 1e2))
    elif kernel_name in ("matern", "matern25"):
        base = Matern(length_scale=length_scale,
                      length_scale_bounds=(1e-2, 1e2), nu=2.5)
    elif kernel_name == "matern15":
        base = Matern(length_scale=length_scale,
                      length_scale_bounds=(1e-2, 1e2), nu=1.5)
    else:
        raise ValueError(
            f"Unsupported kernel '{kernel_name}'. "
            f"Choose from {SUPPORTED_KERNELS}"
        )

    return (
        ConstantKernel(1.0, constant_value_bounds=(1e-3, 1e3)) * base
        + WhiteKernel(noise_level=noise_level,
                      noise_level_bounds=(1e-5, 1e1))
    )


class YieldSurrogate:
    """
    Gaussian Process surrogate model for yield prediction.

    Defaults to ARD Matern-5/2 kernel (one length scale per input dim).
    For high-dim inputs (e.g., 308D here), ARD is much better than a scalar
    length scale because it learns which dims matter and which are noise.

    If a yield_predictor_fn is provided AND use_prior_mean=True, the GP
    models the residual (observed - predicted) rather than the raw yield.
    If the prior predictor is weak (e.g., R^2 < 0.4), it's often better
    to disable it (use_prior_mean=False) and let GP+normalize_y handle
    the mean via the observation empirical mean.
    """

    def __init__(self, condition_space, yield_predictor_fn: Optional[Callable] = None,
                 length_scale: float = 1.0, noise_level: float = 0.1,
                 alpha: float = 1e-2,
                 kernel: str = "matern",
                 use_ard: bool = True,
                 use_prior_mean: bool = True,
                 n_restarts_optimizer: int = 3):
        """
        Args:
            condition_space: ConditionSpace instance for encoding conditions
            yield_predictor_fn: Optional callable(conditions_dict) -> float
                Returns predicted yield (0-100) for a condition set.
                Only used as prior mean if use_prior_mean=True.
            length_scale: initial length scale (per-dim if use_ard)
            noise_level: WhiteKernel noise level
            alpha: GP regularization (added to diagonal of kernel matrix)
            kernel: 'matern' (default, nu=2.5) | 'matern15' | 'rbf'
            use_ard: if True, one length_scale per input dim (RECOMMENDED)
            use_prior_mean: if True and yield_predictor_fn given, GP fits
                residuals; else GP fits raw yields via normalize_y.
            n_restarts_optimizer: GP hyperparameter restarts
        """
        self.space = condition_space
        self.yield_predictor_fn = yield_predictor_fn
        self.use_prior_mean = use_prior_mean and (yield_predictor_fn is not None)
        self.kernel_name = kernel
        self.use_ard = use_ard

        input_dim = getattr(condition_space, "dim", None)
        if input_dim is None or input_dim <= 0:
            # Fallback: infer on first fit. Disable ARD until known.
            self.use_ard = False
            input_dim = 1

        gp_kernel = _make_kernel(
            kernel_name=kernel,
            input_dim=input_dim,
            length_scale_init=length_scale,
            noise_level=noise_level,
            use_ard=self.use_ard,
        )
        self.gp = GaussianProcessRegressor(
            kernel=gp_kernel,
            alpha=alpha,
            normalize_y=True,
            n_restarts_optimizer=n_restarts_optimizer,
        )

        # Observation storage
        self.X_observed: List[dict] = []
        self.y_observed: List[float] = []
        self.X_encoded: Optional[np.ndarray] = None
        self.y_residuals: Optional[np.ndarray] = None
        self._fitted = False

    @property
    def n_observations(self) -> int:
        return len(self.y_observed)

    @property
    def best_yield(self) -> float:
        """Best observed yield so far."""
        if not self.y_observed:
            return 0.0
        return max(self.y_observed)

    def _compute_prior_mean(self, conditions_list: List[dict]) -> np.ndarray:
        """Compute prior mean (YieldPredictor output) for a batch of conditions.

        Returns zeros if use_prior_mean is False or no predictor is set —
        in that case GP's normalize_y handles the mean via training data.
        """
        if not self.use_prior_mean or self.yield_predictor_fn is None:
            return np.zeros(len(conditions_list), dtype=np.float64)

        means = []
        for cond in conditions_list:
            try:
                pred = self.yield_predictor_fn(cond)
                means.append(float(pred))
            except Exception:
                means.append(50.0)  # fallback to median
        return np.array(means, dtype=np.float64)

    def _encode_batch(self, conditions_list: List[dict]) -> np.ndarray:
        """Encode a batch of condition dicts to a feature matrix."""
        return np.array([self.space.encode(c) for c in conditions_list],
                        dtype=np.float64)

    def fit(self, conditions_list: List[dict], yields: np.ndarray):
        """
        Fit the GP on observed data.

        Args:
            conditions_list: list of condition dicts
            yields: array of observed yields (0-100 scale)
        """
        self.X_observed = list(conditions_list)
        self.y_observed = list(yields.flatten())

        # Limit observations for GP scalability
        if len(self.X_observed) > MAX_OBSERVATIONS:
            # Keep most recent observations
            self.X_observed = self.X_observed[-MAX_OBSERVATIONS:]
            self.y_observed = self.y_observed[-MAX_OBSERVATIONS:]

        self.X_encoded = self._encode_batch(self.X_observed)
        prior_mean = self._compute_prior_mean(self.X_observed)
        self.y_residuals = np.array(self.y_observed, dtype=np.float64) - prior_mean

        self.gp.fit(self.X_encoded, self.y_residuals)
        self._fitted = True

    def predict(self, conditions_list: List[dict]) -> Tuple[np.ndarray, np.ndarray]:
        """
        Predict yield mean and std for a batch of conditions.

        Returns:
            (mean, std) — both on 0-100 scale
        """
        if not self._fitted:
            # No data yet — return prior mean with high uncertainty
            prior_mean = self._compute_prior_mean(conditions_list)
            return prior_mean, np.full(len(conditions_list), 25.0)

        X = self._encode_batch(conditions_list)
        residual_mean, residual_std = self.gp.predict(X, return_std=True)

        prior_mean = self._compute_prior_mean(conditions_list)
        mean = prior_mean + residual_mean
        # Clip to valid range
        mean = np.clip(mean, 0.0, 100.0)

        return mean, residual_std

    def update(self, new_conditions: dict, new_yield: float):
        """
        Add a single new observation and refit the GP.

        Args:
            new_conditions: condition dict
            new_yield: observed yield (0-100)
        """
        self.X_observed.append(new_conditions)
        self.y_observed.append(float(new_yield))

        # Limit observations
        if len(self.X_observed) > MAX_OBSERVATIONS:
            self.X_observed = self.X_observed[-MAX_OBSERVATIONS:]
            self.y_observed = self.y_observed[-MAX_OBSERVATIONS:]

        self.X_encoded = self._encode_batch(self.X_observed)
        prior_mean = self._compute_prior_mean(self.X_observed)
        self.y_residuals = np.array(self.y_observed, dtype=np.float64) - prior_mean

        self.gp.fit(self.X_encoded, self.y_residuals)
        self._fitted = True

    def get_state(self) -> dict:
        """Serialize surrogate state for persistence."""
        return {
            'X_observed': self.X_observed,
            'y_observed': self.y_observed,
            'fitted': self._fitted,
        }

    def load_state(self, state: dict):
        """Restore surrogate state and refit GP."""
        self.X_observed = state.get('X_observed', [])
        self.y_observed = state.get('y_observed', [])
        if self.X_observed and self.y_observed:
            self.fit(
                self.X_observed,
                np.array(self.y_observed, dtype=np.float64),
            )

    def get_kernel_summary(self) -> dict:
        """Inspect learned kernel hyperparameters (for debugging ARD).

        Returns a dict with per-dim length scales (if ARD) plus noise / variance.
        Useful for diagnosing which input dims the GP considers informative —
        very large length scales (near upper bound) mean the dim is effectively
        ignored.
        """
        if not self._fitted:
            return {"fitted": False}

        k = self.gp.kernel_
        summary = {
            "fitted": True,
            "kernel_name": self.kernel_name,
            "use_ard": self.use_ard,
            "kernel_repr": str(k),
        }
        # Extract length scales from inner Matern/RBF kernel
        try:
            # kernel layout: Constant * (Matern/RBF) + WhiteKernel
            product = k.k1  # Constant * base
            base = product.k2  # Matern or RBF
            ls = np.atleast_1d(base.length_scale).astype(float)
            summary["length_scale_min"] = float(ls.min())
            summary["length_scale_max"] = float(ls.max())
            summary["length_scale_median"] = float(np.median(ls))
            # Identify "effectively ignored" dims (length_scale near upper bound of 100)
            n_ignored = int(np.sum(ls > 50.0))
            summary["n_ignored_dims"] = n_ignored
            summary["n_total_dims"] = int(ls.shape[0])
            # Top-10 most informative dims (smallest length scales)
            if ls.shape[0] > 1:
                top_dims = np.argsort(ls)[:10].tolist()
                summary["most_informative_dims"] = top_dims
                summary["their_length_scales"] = [float(ls[i]) for i in top_dims]
        except Exception as e:
            summary["length_scale_error"] = str(e)

        # Noise
        try:
            summary["noise_level"] = float(k.k2.noise_level)
        except Exception:
            pass
        return summary
