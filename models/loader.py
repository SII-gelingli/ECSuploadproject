"""
ModelManager: lazy-loads the 3 trained models and feature extractors.

Adapted from yield_prediction/scripts/recommend_conditions.py load functions.
Uses yp_* module names registered by config.py to avoid namespace collision.
"""
import json
import torch
import torch.nn.functional as F
import numpy as np
from typing import Dict, List, Optional, Tuple

from config import (
    CONDITION_MODEL_PATH, CVAE_MODEL_PATH, YIELD_MODEL_PATH,
    CONDITION_V3_MODEL_PATH, CONDITION_V3_DATA_DIR,
    VOCAB_PATH, XTB_CSV_PATH,
    ELECTRODE_NAMES, CELL_TYPE_NAMES, UNKNOWN_INDICES,
    FINGERPRINT_SIZE, FINGERPRINT_RADIUS,
    XTB_BIN_PATH, XTB_DATA_PATH, XTB_LIB_PATH, XTB_TIMEOUT,
)

# Import yield_prediction modules via aliased names (registered by config.py)
from yp_models.condition_recommender import ConditionRecommender, ConditionRecommenderXTB
from yp_models.condition_cvae import CategoricalCVAE
from yp_models.yield_predictor import YieldPredictor
from yp_models.condition_stage1_hier_set_v3 import (
    ConditionStage1HierSetV3,
    SINGLE_HEADS_V3 as V3_SINGLE_HEADS,
    HIER_KEYS as V3_HIER_KEYS,
    SET_HEADS as V3_SET_HEADS,
    SMI_FROM_CLASS as V3_SMI_FROM_CLASS,
    K_SLOTS as V3_K_SLOTS,
)
from yp_utils.feature_extractor import MolecularFeatureExtractor


class ModelManager:
    """
    Lazy-loads and manages the three trained models and feature extractors.

    Models are loaded on first access to avoid startup delay when not all
    models are needed.
    """

    def __init__(self, device: str = 'cpu',
                 condition_model_path: str = None,
                 cvae_model_path: str = None,
                 yield_model_path: str = None,
                 vocab_path: str = None,
                 xtb_csv_path: str = None):
        self.device = device
        self._condition_model_path = condition_model_path or str(CONDITION_MODEL_PATH)
        self._cvae_model_path = cvae_model_path or str(CVAE_MODEL_PATH)
        self._yield_model_path = yield_model_path or str(YIELD_MODEL_PATH)
        self._vocab_path = vocab_path or str(VOCAB_PATH)
        self._xtb_csv_path = xtb_csv_path or str(XTB_CSV_PATH)

        # Lazy-loaded state
        self._condition_model = None
        self._cvae_model = None
        self._yield_model = None
        self._idx_maps = None
        self._condition_reaction_dim = None
        self._cvae_reaction_dim = None
        self._yield_input_dim = None

        # V3 model state
        self._v3_model = None
        self._v3_stats = None
        self._v3_vocab = None
        self._v3_idx_maps = None

        self._mol_extractor = None
        self._xtb_lookup = None

    @property
    def mol_extractor(self) -> MolecularFeatureExtractor:
        if self._mol_extractor is None:
            self._mol_extractor = MolecularFeatureExtractor(
                fingerprint_size=FINGERPRINT_SIZE,
                fingerprint_radius=FINGERPRINT_RADIUS,
            )
        return self._mol_extractor

    def _load_vocab(self) -> Dict:
        """Load vocabulary and build index-to-SMILES maps."""
        if self._idx_maps is not None:
            return self._idx_maps

        with open(self._vocab_path) as f:
            vocab = json.load(f)

        self._idx_maps = {
            'electrolyte': {v: k for k, v in vocab.get('electrolyte', {}).items()},
            'solvent': {v: k for k, v in vocab.get('solvent', {}).items()},
            'reagent': {v: k for k, v in vocab.get('reagent', {}).items()},
            'catalyst': {v: k for k, v in vocab.get('catalyst', {}).items()},
        }
        return self._idx_maps

    @property
    def idx_maps(self) -> Dict:
        return self._load_vocab()

    def _get_xtb_lookup(self, reaction_dim: int):
        """Load XTB lookup if the model requires xTB features (dim > 6144)."""
        if reaction_dim > 6144 and self._xtb_lookup is None:
            from yp_utils.xtb_features import XTBFeatureLookup
            self._xtb_lookup = XTBFeatureLookup(
                csv_path=self._xtb_csv_path,
                xtb_bin=str(XTB_BIN_PATH),
                xtb_data=XTB_DATA_PATH,
                xtb_lib=XTB_LIB_PATH,
                timeout=XTB_TIMEOUT,
            )
        return self._xtb_lookup if reaction_dim > 6144 else None

    # ── ConditionRecommender ────────────────────────────────────

    def _load_condition_model(self):
        if self._condition_model is not None:
            return

        self._load_vocab()
        checkpoint = torch.load(self._condition_model_path, map_location=self.device, weights_only=False)
        state_dict = checkpoint['model_state_dict']

        # Detect model architecture based on state_dict keys
        if 'fp_encoder.0.weight' in state_dict:
            # New ConditionRecommenderXTB architecture
            fp_dim = state_dict['fp_encoder.0.weight'].shape[1]
            xtb_dim = state_dict['xtb_encoder.0.weight'].shape[1]
            hidden_dim = state_dict['fusion.0.weight'].shape[0]
            num_anode = state_dict['anode_head.weight'].shape[0]
            num_cathode = state_dict['cathode_head.weight'].shape[0]
            num_cell_type = state_dict['cell_type_head.weight'].shape[0]
            num_electrolyte = state_dict['electrolyte_head.weight'].shape[0]
            num_solvent = state_dict['solvent_head.weight'].shape[0]
            num_reagent = state_dict['reagent_head.weight'].shape[0]
            num_catalyst = state_dict['catalyst_head.weight'].shape[0]

            model = ConditionRecommenderXTB(
                fp_dim=fp_dim,
                xtb_dim=xtb_dim,
                hidden_dim=hidden_dim,
                num_anode=num_anode,
                num_cathode=num_cathode,
                num_cell_type=num_cell_type,
                num_electrolyte=num_electrolyte,
                num_solvent=num_solvent,
                num_reagent=num_reagent,
                num_catalyst=num_catalyst,
            ).to(self.device)
            self._condition_reaction_dim = fp_dim + xtb_dim  # 6144 + 33 = 6177
        else:
            # Legacy ConditionRecommender architecture
            reaction_dim = state_dict['reaction_encoder.0.weight'].shape[1]
            hidden_dim = state_dict['reaction_encoder.0.weight'].shape[0]
            num_electrolytes = state_dict['electrolyte_head.weight'].shape[0]
            num_solvents = state_dict['solvent_head.weight'].shape[0]
            num_reagents = state_dict['reagent_head.weight'].shape[0]
            num_catalysts = state_dict['catalyst_head.weight'].shape[0]

            num_anode_materials = state_dict['anode_head.weight'].shape[0]
            num_cathode_materials = state_dict['cathode_head.weight'].shape[0]
            num_cell_types = state_dict['cell_type_head.weight'].shape[0]

            model = ConditionRecommender(
                reaction_dim=reaction_dim,
                hidden_dim=hidden_dim,
                num_anode_materials=num_anode_materials,
                num_cathode_materials=num_cathode_materials,
                num_cell_types=num_cell_types,
                num_electrolytes=num_electrolytes,
                num_solvents=num_solvents,
                num_reagents=num_reagents,
                num_catalysts=num_catalysts,
            ).to(self.device)
            self._condition_reaction_dim = reaction_dim

        model.load_state_dict(state_dict)
        model.eval()
        self._condition_model = model

    @property
    def condition_model(self):
        self._load_condition_model()
        return self._condition_model

    @property
    def condition_reaction_dim(self):
        self._load_condition_model()
        return self._condition_reaction_dim

    @property
    def condition_xtb_lookup(self):
        self._load_condition_model()
        return self._get_xtb_lookup(self._condition_reaction_dim)

    # ── CategoricalCVAE ────────────────────────────────────────

    def _load_cvae_model(self):
        if self._cvae_model is not None:
            return

        self._load_vocab()
        checkpoint = torch.load(self._cvae_model_path, map_location=self.device, weights_only=False)
        state_dict = checkpoint['model_state_dict']

        reaction_dim = state_dict['reaction_encoder.0.weight'].shape[1]
        num_electrolytes = state_dict['electrolyte_head.weight'].shape[0]
        num_solvents = state_dict['solvent_head.weight'].shape[0]
        num_reagents = state_dict['reagent_head.weight'].shape[0]
        num_catalysts = state_dict['catalyst_head.weight'].shape[0]

        num_anode_materials = state_dict['anode_head.weight'].shape[0]
        num_cathode_materials = state_dict['cathode_head.weight'].shape[0]
        num_cell_types = state_dict['cell_type_head.weight'].shape[0]

        model = CategoricalCVAE(
            reaction_dim=reaction_dim,
            repr_dim=256,
            latent_dim=64,
            num_anode_materials=num_anode_materials,
            num_cathode_materials=num_cathode_materials,
            num_cell_types=num_cell_types,
            num_electrolytes=num_electrolytes,
            num_solvents=num_solvents,
            num_reagents=num_reagents,
            num_catalysts=num_catalysts,
        ).to(self.device)
        model.load_state_dict(state_dict)
        model.eval()

        self._cvae_model = model
        self._cvae_reaction_dim = reaction_dim

    @property
    def cvae_model(self):
        self._load_cvae_model()
        return self._cvae_model

    @property
    def cvae_reaction_dim(self):
        self._load_cvae_model()
        return self._cvae_reaction_dim

    @property
    def cvae_xtb_lookup(self):
        self._load_cvae_model()
        return self._get_xtb_lookup(self._cvae_reaction_dim)

    # ── YieldPredictor ──────────────────────────────────────────

    def _load_yield_model(self):
        if self._yield_model is not None:
            return

        checkpoint = torch.load(self._yield_model_path, map_location=self.device, weights_only=False)
        state_dict = checkpoint['model_state_dict']
        input_dim = state_dict['encoder.0.weight'].shape[1]

        config = checkpoint.get('config', {})
        hidden_dims = config.get('model', {}).get('predictor', {}).get('hidden_dims', [512, 256, 128])
        dropout = config.get('model', {}).get('predictor', {}).get('dropout', 0.2)

        # Fix legacy key naming: output.* -> output_layer.*
        fixed_state_dict = {}
        for k, v in state_dict.items():
            if k.startswith('output.'):
                fixed_state_dict['output_layer.' + k[len('output.'):]] = v
            else:
                fixed_state_dict[k] = v

        model = YieldPredictor(
            input_dim=input_dim,
            hidden_dims=hidden_dims,
            dropout=dropout,
        ).to(self.device)
        model.load_state_dict(fixed_state_dict)
        model.eval()

        self._yield_model = model
        self._yield_input_dim = input_dim

    @property
    def yield_model(self):
        self._load_yield_model()
        return self._yield_model

    @property
    def yield_input_dim(self):
        self._load_yield_model()
        return self._yield_input_dim

    # ── V3 Hier+Set + SMI heads (2026-05-20, 6-head AVG 52.76%) ────

    def _load_v3_model(self):
        if self._v3_model is not None:
            return
        from pathlib import Path
        data_dir = Path(CONDITION_V3_DATA_DIR)
        # Load metadata
        with open(data_dir / 'stats.json') as f:
            self._v3_stats = json.load(f)
        with open(data_dir / 'vocab.json') as f:
            self._v3_vocab = json.load(f)
        # Build idx -> SMILES / name maps for downstream display
        self._v3_idx_maps = {}
        for head in ['solvent', 'electrolyte', 'catalyst', 'reagent', 'ligand', 'additive']:
            self._v3_idx_maps[head] = {v: k for k, v in self._v3_vocab[head].items()}
        # v3 class lists
        for head, names in self._v3_vocab.get('__v3__', {}).items():
            self._v3_idx_maps[head] = {i: n for i, n in enumerate(names)}

        # Load ckpt
        ckpt = torch.load(CONDITION_V3_MODEL_PATH, map_location=self.device, weights_only=False)
        nc = self._v3_stats['num_classes']
        nc_v3 = self._v3_stats['num_classes_v3']
        model = ConditionStage1HierSetV3(
            num_classes=nc, num_classes_v3=nc_v3, fp_dim=6144,
            hidden_dims=tuple(ckpt.get('hidden_dims', (1024, 768, 512))),
            dropout=ckpt.get('dropout', 0.3),
            class_embed_dim=ckpt.get('class_embed_dim', 32),
        ).to(self.device)
        model.load_state_dict(ckpt['model_state_dict'])
        model.eval()
        self._v3_model = model

    @property
    def v3_model(self):
        self._load_v3_model()
        return self._v3_model

    @property
    def v3_stats(self):
        self._load_v3_model()
        return self._v3_stats

    @property
    def v3_vocab(self):
        self._load_v3_model()
        return self._v3_vocab

    @property
    def v3_idx_maps(self):
        self._load_v3_model()
        return self._v3_idx_maps

    # ── Stage-2 用量回归 (新数据训练) ──────────────────────────

    def _load_stage2_model(self):
        if getattr(self, '_stage2_model', None) is not None:
            return
        from pathlib import Path
        from yp_models.condition_stage2 import ConditionStage2
        self._load_v3_model()  # 共用 v3_stats num_classes
        data_dir = Path(CONDITION_V3_DATA_DIR)
        with open(data_dir / 'amount_stats.json') as f:
            self._stage2_amount_stats = json.load(f)
        ckpt_path = CONDITION_V3_MODEL_PATH.parent / 'stage2_clean_v1.pt'
        ckpt = torch.load(ckpt_path, map_location=self.device, weights_only=False)
        nc = self._v3_stats['num_classes']
        model = ConditionStage2(
            num_classes=nc,
            fp_dim=ckpt.get('fp_dim', 6144),
            hidden_dims=tuple(ckpt.get('hidden_dims', (512, 256))),
            dropout=ckpt.get('dropout', 0.2),
        ).to(self.device)
        model.load_state_dict(ckpt['model_state_dict'])
        model.eval()
        self._stage2_model = model

    @property
    def stage2_model(self):
        self._load_stage2_model()
        return self._stage2_model

    @property
    def stage2_amount_stats(self):
        self._load_stage2_model()
        return self._stage2_amount_stats
