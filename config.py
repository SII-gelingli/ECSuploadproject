"""
Configuration for the Electrochemical Condition Agent.

Paths, constants, AgentConfig dataclass, and yield_prediction module imports.

Because yield_prediction/ has 'models/' and 'utils/' packages that collide
with our own, we load them via importlib under prefixed names (yp_models,
yp_utils) instead of adding yield_prediction to sys.path.
"""
import os
import sys
import importlib
import importlib.util
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

from agent.debate_config import DebateConfig

# ── Project paths ──────────────────────────────────────────────
AGENT_ROOT = Path(__file__).parent
YIELD_PREDICTION_ROOT = AGENT_ROOT / "yield_prediction"

# pip packages path (optional, for custom package installations)
LOCAL_PACKAGES = os.environ.get("LOCAL_PACKAGES", "/inspire/hdd/global_user/gelingli-253114010248/pip_packages")
if os.path.isdir(LOCAL_PACKAGES) and LOCAL_PACKAGES not in sys.path:
    sys.path.append(LOCAL_PACKAGES)

# Ensure AGENT_ROOT is on sys.path for our own modules
_agent_root_str = str(AGENT_ROOT)
if _agent_root_str not in sys.path:
    sys.path.insert(0, _agent_root_str)


# ── Import yield_prediction modules without polluting sys.path ─

def _import_yp_module(subpath: str, module_name: str):
    """
    Import a module from yield_prediction by file path.

    Example: _import_yp_module('models/condition_recommender.py', 'yp_condition_recommender')
    """
    full_path = YIELD_PREDICTION_ROOT / subpath
    spec = importlib.util.spec_from_file_location(module_name, str(full_path))
    if spec is None:
        raise ImportError(f"Cannot find module at {full_path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)
    return mod


def _import_yp_package(pkg_dir: str, pkg_name: str):
    """
    Import a yield_prediction package (directory with __init__.py) under a
    given name, so its submodules can be imported via 'pkg_name.submodule'.
    """
    init_path = YIELD_PREDICTION_ROOT / pkg_dir / "__init__.py"
    spec = importlib.util.spec_from_file_location(
        pkg_name,
        str(init_path),
        submodule_search_locations=[str(YIELD_PREDICTION_ROOT / pkg_dir)],
    )
    if spec is None:
        raise ImportError(f"Cannot find package at {init_path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[pkg_name] = mod
    spec.loader.exec_module(mod)
    return mod


def load_yp_modules():
    """
    Load all needed yield_prediction modules under 'yp_*' names.

    After calling this:
        import yp_models.condition_recommender
        import yp_models.condition_cvae
        import yp_models.yield_predictor
        import yp_utils.feature_extractor
        import yp_utils.xtb_features
    """
    # Register packages first
    _import_yp_package("models", "yp_models")
    _import_yp_package("utils", "yp_utils")

    # Import specific submodules
    _import_yp_module("utils/xtb_features.py", "yp_utils.xtb_features")
    _import_yp_module("utils/feature_extractor.py", "yp_utils.feature_extractor")
    _import_yp_module("models/condition_recommender.py", "yp_models.condition_recommender")
    _import_yp_module("models/condition_cvae.py", "yp_models.condition_cvae")
    _import_yp_module("models/yield_predictor.py", "yp_models.yield_predictor")
    # V3 (Hier+Set + Ligand/Additive SMI heads, 2026-05-20 当前最佳)
    _import_yp_module("models/condition_stage1_set.py", "yp_models.condition_stage1_set")
    _import_yp_module("models/condition_stage1_hier_set_v3.py", "yp_models.condition_stage1_hier_set_v3")
    _import_yp_module("models/condition_stage1.py", "yp_models.condition_stage1")
    _import_yp_module("models/condition_stage2.py", "yp_models.condition_stage2")


# Load on import so all other modules can use yp_* imports
load_yp_modules()


# ── Model checkpoint paths ─────────────────────────────────────
# Updated 2026-03: Retrained with full alkene_reactions_by_yield data (10635 reactions)
CONDITION_MODEL_PATH = YIELD_PREDICTION_ROOT / "checkpoints" / "condition_model" / "best_condition_model.pt"
CVAE_MODEL_PATH = YIELD_PREDICTION_ROOT / "checkpoints" / "condition_model" / "best_cvae_condition_model.pt"
YIELD_MODEL_PATH = YIELD_PREDICTION_ROOT / "checkpoints" / "best_model.pt"
VOCAB_PATH = YIELD_PREDICTION_ROOT / "data" / "vocab.json"  # Updated vocab with new data

# V3 Hier+Set + Ligand/Additive SMI heads + Fine Electrode (2026-05-21 严格零泄漏版)
# 数据: data_audited_v3_clean/ (paper+rxn 双零泄漏切分, 118 test paper / 2947 rxn)
# Stage-1 综合 score 0.5350, AVG single 68.65%, catalyst set F1 58.54%
CONDITION_V3_MODEL_PATH = YIELD_PREDICTION_ROOT / "checkpoints" / "two_stage" / "stage1_hier_set_v3_smi_fineE.pt"
CONDITION_V3_DATA_DIR = YIELD_PREDICTION_ROOT / "data_audited_v3_clean"
# Multi-task model for failure prediction (optional)
MULTITASK_MODEL_PATH = YIELD_PREDICTION_ROOT / "checkpoints" / "multitask" / "best_model.pt"

# ── Data paths ─────────────────────────────────────────────────
TRAIN_DATA_PATH = YIELD_PREDICTION_ROOT / "data" / "train.pt"
XTB_CSV_PATH = YIELD_PREDICTION_ROOT / "data" / "xtb_reaction_molecules.csv"

# ── xTB binary paths (for on-the-fly computation) ─────────────
_XTB_INSTALL = Path(os.environ.get(
    "XTB_INSTALL_DIR",
    "/inspire/hdd/global_user/gelingli-253114010248/xtb_install/xtb-dist",
))
XTB_BIN_PATH = Path(os.environ.get("XTB_BIN", str(_XTB_INSTALL / "bin" / "xtb")))
XTB_DATA_PATH = str(os.environ.get("XTBPATH", str(_XTB_INSTALL / "share" / "xtb")))
XTB_LIB_PATH = str(os.environ.get("XTB_LIB", str(_XTB_INSTALL / "lib")))
XTB_TIMEOUT = int(os.environ.get("XTB_TIMEOUT", "60"))

# FAISS index paths (generated by build_index.py)
FAISS_INDEX_PATH = AGENT_ROOT / "data" / "faiss_index.bin"
REACTION_DB_PATH = AGENT_ROOT / "data" / "reaction_db.pkl"

# Mechanism KB (generated by yield_prediction/scripts/build_mechanism_kb.py)
MECHANISM_KB_DIR = AGENT_ROOT / "data" / "mechanism_kb"

# ── Label mappings ─────────────────────────────────────────────
# Updated 2026-03: 23 electrode classes (0-22), 6 cell types (0-5)
ELECTRODE_NAMES = {
    0: 'Carbon', 1: 'Graphite', 2: 'Platinum', 3: 'Glassy Carbon',
    4: 'RVC', 5: 'Nickel', 6: 'Stainless Steel', 7: 'Copper',
    8: 'Zinc', 9: 'Lead', 10: 'Gold', 11: 'Silver', 12: 'Iron',
    13: 'Magnesium', 14: 'Aluminum', 15: 'Titanium', 16: 'Cobalt',
    17: 'Palladium', 18: 'Tin', 19: 'Niobium', 20: 'Mercury',
    21: 'Pencil Graphite', 22: 'Unknown',
}

CELL_TYPE_NAMES = {
    0: 'Undivided', 1: 'Divided', 2: 'Flow', 3: 'Sealed',
    4: 'H-cell', 5: 'Unknown',
}

# Indices to mask out during inference (avoid recommending "Unknown")
UNKNOWN_INDICES = {
    'anode': 22,
    'cathode': 22,
    'cell_type': 5,
    'electrolyte': 0,
    'solvent': 0,
    'reagent': 0,
    'catalyst': 0,
}

# SMILES-based condition keys (as opposed to electrode/cell_type which use fixed labels)
SMILES_CONDITION_KEYS = {'electrolyte', 'solvent', 'reagent', 'catalyst'}

# ── Feature dimensions ─────────────────────────────────────────
FINGERPRINT_SIZE = 2048
FINGERPRINT_RADIUS = 2
REACTION_FP_DIM = 6144  # 3 x 2048

# ── Agent configuration ────────────────────────────────────────
@dataclass
class AgentConfig:
    """Configuration for the ElectrochemAgent."""
    # LLM backend: "anthropic" or "openai" (for vLLM / OpenAI-compatible endpoints)
    backend: str = field(default_factory=lambda: os.environ.get("LLM_BACKEND", "openai"))

    # LLM API (fields are reused by both backends)
    model: str = field(default_factory=lambda: os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-6"))
    temperature: float = field(default_factory=lambda: float(os.environ.get("ANTHROPIC_TEMPERATURE", "1.0")))
    max_tokens: int = 60000
    max_tool_rounds: int = 15
    api_key: Optional[str] = field(default_factory=lambda: os.environ.get("ANTHROPIC_API_KEY"))
    base_url: Optional[str] = field(default_factory=lambda: os.environ.get("ANTHROPIC_BASE_URL"))

    # Inference device
    device: str = "cpu"

    # Model paths (use defaults from above)
    condition_model_path: str = field(default_factory=lambda: str(CONDITION_MODEL_PATH))
    cvae_model_path: str = field(default_factory=lambda: str(CVAE_MODEL_PATH))
    yield_model_path: str = field(default_factory=lambda: str(YIELD_MODEL_PATH))
    vocab_path: str = field(default_factory=lambda: str(VOCAB_PATH))
    xtb_csv_path: str = field(default_factory=lambda: str(XTB_CSV_PATH))

    # FAISS index
    faiss_index_path: str = field(default_factory=lambda: str(FAISS_INDEX_PATH))
    reaction_db_path: str = field(default_factory=lambda: str(REACTION_DB_PATH))

    # Defaults for tool parameters
    default_top_k: int = 3
    default_num_samples: int = 10
    default_temperature: float = 1.0
    default_similarity_threshold: float = 0.3

    # Bayesian optimization parameters
    bo_pca_dim: int = 64
    bo_default_acq_func: str = 'ei'
    bo_default_n_similar: int = 10
    bo_default_m1_top_k: int = 5
    bo_default_pool_size: int = 200
    bo_search_n_iter: int = 50
    bo_rerank_alpha: float = 0.5
    bo_rerank_beta_ucb: float = 1.5

    # Debate mode configuration
    debate: DebateConfig = field(default_factory=DebateConfig)
