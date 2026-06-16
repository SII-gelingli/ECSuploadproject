"""
Bayesian optimization module for electrochemical condition search.

Provides GP-based surrogate modeling and acquisition function optimization
over the discrete condition space (electrodes, solvents, electrolytes, etc.).
"""
from .space import ConditionSpace
from .surrogate import YieldSurrogate
from .acquisition import AcquisitionOptimizer, ACQUISITION_FUNCTIONS
from .warm_start import WarmStarter
from .priors import RAGMeanPrior
from .optimizer import BayesianConditionOptimizer

__all__ = [
    'ConditionSpace',
    'YieldSurrogate',
    'AcquisitionOptimizer',
    'ACQUISITION_FUNCTIONS',
    'WarmStarter',
    'RAGMeanPrior',
    'BayesianConditionOptimizer',
]
