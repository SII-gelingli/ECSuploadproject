"""
Condition space encoding/decoding for Bayesian optimization.

Encodes electrochemical conditions as fixed-length vectors:
- Device conditions (anode 23, cathode 23, cell_type 6) → one-hot (52D)
- Molecular conditions (solvent, electrolyte, reagent, catalyst) → PCA(MorganFP) (4×64=256D)
- Total GP input: ~308D
"""
import json
import numpy as np
from typing import Dict, List, Optional, Tuple

from sklearn.decomposition import PCA
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs


# Dimensions
NUM_ANODE = 23
NUM_CATHODE = 23
NUM_CELL_TYPE = 6
DEVICE_DIM = NUM_ANODE + NUM_CATHODE + NUM_CELL_TYPE  # 52

MOL_CONDITION_KEYS = ['solvent', 'electrolyte', 'reagent', 'catalyst']
DEFAULT_PCA_DIM = 64
DEFAULT_FP_SIZE = 2048
DEFAULT_FP_RADIUS = 2

# Common solvent mixtures (46.3% of training data). Dot-joined SMILES.
COMMON_SOLVENT_MIXTURES = [
    'CC#N.O',               # MeCN + H2O
    'CC#N.CO',              # MeCN + MeOH
    'ClCCl.O',              # DCM + H2O
    'OCC(F)(F)F.CC#N',      # HFIP + MeCN
    'OCC(F)(F)F.CC(C)=O',   # TFE + acetone
    'CS(C)=O.O',            # DMSO + H2O
    'ClCCl.CC#N',           # DCM + MeCN
    'CC#N.CC(C)=O',         # MeCN + acetone
    'CN(C)C=O.O',           # DMF + H2O
]


def _smiles_to_morgan(smiles: str, fp_size: int = DEFAULT_FP_SIZE,
                       radius: int = DEFAULT_FP_RADIUS) -> np.ndarray:
    """Convert a SMILES string to a Morgan fingerprint array."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return np.zeros(fp_size, dtype=np.float32)
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=fp_size)
    arr = np.zeros(fp_size, dtype=np.float32)
    DataStructs.ConvertToNumpyArray(fp, arr)
    return arr


class ConditionSpace:
    """
    Encode/decode electrochemical conditions as fixed-length vectors.

    The encoding separates device conditions (one-hot) from molecular conditions
    (PCA-compressed Morgan fingerprints), producing a compact ~308D vector
    suitable for GP modeling.
    """

    def __init__(self, vocab_path: str, pca_dim: int = DEFAULT_PCA_DIM,
                 fp_size: int = DEFAULT_FP_SIZE, fp_radius: int = DEFAULT_FP_RADIUS):
        self.pca_dim = pca_dim
        self.fp_size = fp_size
        self.fp_radius = fp_radius

        # Load vocab: {condition_type: {smiles: index}}
        with open(vocab_path) as f:
            self.vocab = json.load(f)

        # Build inverse maps: {index: smiles}
        self.idx_to_smiles = {}
        for cond_key in MOL_CONDITION_KEYS:
            self.idx_to_smiles[cond_key] = {
                v: k for k, v in self.vocab.get(cond_key, {}).items()
            }

        # Fit PCA for each molecular condition type
        self.pca_models: Dict[str, PCA] = {}
        self.mol_embeddings: Dict[str, Dict[int, np.ndarray]] = {}
        self._fit_pca_models()

        # Dynamic solvent mixtures from RAG (set by optimizer after retrieval)
        self._solvent_mixtures: List[dict] = []

        # Total encoding dimension
        self.dim = DEVICE_DIM + len(MOL_CONDITION_KEYS) * self.pca_dim

    def _fit_pca_models(self):
        """Compute Morgan FP for all vocab entries and fit PCA per condition type."""
        for cond_key in MOL_CONDITION_KEYS:
            smiles_to_idx = self.vocab.get(cond_key, {})
            if not smiles_to_idx:
                # No vocab entries — use zero embedding
                self.pca_models[cond_key] = None
                self.mol_embeddings[cond_key] = {}
                continue

            indices = []
            fps = []
            for smiles, idx in smiles_to_idx.items():
                fp = _smiles_to_morgan(smiles, self.fp_size, self.fp_radius)
                indices.append(idx)
                fps.append(fp)

            fp_matrix = np.array(fps, dtype=np.float32)

            # Fit PCA (handle case where vocab is smaller than pca_dim)
            n_components = min(self.pca_dim, len(fps), fp_matrix.shape[1])
            pca = PCA(n_components=n_components)
            embeddings = pca.fit_transform(fp_matrix)

            # Pad to pca_dim if n_components < pca_dim
            if n_components < self.pca_dim:
                pad = np.zeros((embeddings.shape[0], self.pca_dim - n_components),
                               dtype=np.float32)
                embeddings = np.hstack([embeddings, pad])

            self.pca_models[cond_key] = pca
            self.mol_embeddings[cond_key] = {
                idx: embeddings[i] for i, idx in enumerate(indices)
            }

    def encode(self, conditions: dict) -> np.ndarray:
        """
        Encode a condition dict to a fixed-length vector.

        Args:
            conditions: dict with keys like 'anode_index', 'cathode_index',
                        'cell_type_index', 'solvent_index', 'electrolyte_index',
                        'reagent_index', 'catalyst_index'.
                        Alternatively accepts 'solvent_smiles', etc.

        Returns:
            np.ndarray of shape (self.dim,)
        """
        parts = []

        # Device conditions → one-hot
        anode_idx = conditions.get('anode_index', 0)
        cathode_idx = conditions.get('cathode_index', 0)
        cell_type_idx = conditions.get('cell_type_index', 0)

        anode_oh = np.zeros(NUM_ANODE, dtype=np.float32)
        cathode_oh = np.zeros(NUM_CATHODE, dtype=np.float32)
        cell_oh = np.zeros(NUM_CELL_TYPE, dtype=np.float32)

        if 0 <= anode_idx < NUM_ANODE:
            anode_oh[anode_idx] = 1.0
        if 0 <= cathode_idx < NUM_CATHODE:
            cathode_oh[cathode_idx] = 1.0
        if 0 <= cell_type_idx < NUM_CELL_TYPE:
            cell_oh[cell_type_idx] = 1.0

        parts.extend([anode_oh, cathode_oh, cell_oh])

        # Molecular conditions → PCA embedding
        for cond_key in MOL_CONDITION_KEYS:
            idx = conditions.get(f'{cond_key}_index', 0)
            smiles = conditions.get(f'{cond_key}_smiles', '')

            embedding = self._get_mol_embedding(cond_key, idx, smiles)
            parts.append(embedding)

        return np.concatenate(parts)

    def _get_mol_embedding(self, cond_key: str, idx: int = 0,
                           smiles: str = '') -> np.ndarray:
        """Get PCA embedding for a molecular condition."""
        # Try by index first
        if idx and idx in self.mol_embeddings.get(cond_key, {}):
            return self.mol_embeddings[cond_key][idx].copy()

        # Try by SMILES
        if smiles and cond_key in self.vocab:
            vocab_idx = self.vocab[cond_key].get(smiles, 0)
            if vocab_idx and vocab_idx in self.mol_embeddings.get(cond_key, {}):
                return self.mol_embeddings[cond_key][vocab_idx].copy()

            # Not in vocab — compute on-the-fly via PCA transform
            if smiles and self.pca_models.get(cond_key) is not None:
                fp = _smiles_to_morgan(smiles, self.fp_size, self.fp_radius)
                pca = self.pca_models[cond_key]
                emb = pca.transform(fp.reshape(1, -1))[0]
                if len(emb) < self.pca_dim:
                    emb = np.concatenate([emb, np.zeros(self.pca_dim - len(emb))])
                return emb.astype(np.float32)

        # Fallback: zero embedding
        return np.zeros(self.pca_dim, dtype=np.float32)

    def decode(self, vector: np.ndarray) -> dict:
        """
        Decode a vector back to a condition dict.

        Uses argmax for one-hot device conditions and nearest-neighbor
        matching in PCA space for molecular conditions.

        Returns:
            dict with '*_index' and '*_smiles' keys
        """
        result = {}
        offset = 0

        # Device conditions: argmax on one-hot
        anode_oh = vector[offset:offset + NUM_ANODE]
        result['anode_index'] = int(np.argmax(anode_oh))
        offset += NUM_ANODE

        cathode_oh = vector[offset:offset + NUM_CATHODE]
        result['cathode_index'] = int(np.argmax(cathode_oh))
        offset += NUM_CATHODE

        cell_oh = vector[offset:offset + NUM_CELL_TYPE]
        result['cell_type_index'] = int(np.argmax(cell_oh))
        offset += NUM_CELL_TYPE

        # Molecular conditions: nearest neighbor in PCA space
        for cond_key in MOL_CONDITION_KEYS:
            emb = vector[offset:offset + self.pca_dim]
            offset += self.pca_dim

            best_idx, best_smiles = self._nearest_neighbor(cond_key, emb)
            result[f'{cond_key}_index'] = best_idx
            result[f'{cond_key}_smiles'] = best_smiles

        return result

    def _nearest_neighbor(self, cond_key: str, query_emb: np.ndarray) -> Tuple[int, str]:
        """Find the vocab entry closest to query_emb in PCA space."""
        embeddings = self.mol_embeddings.get(cond_key, {})
        if not embeddings:
            return 0, ''

        best_idx = 0
        best_sim = -np.inf
        for idx, emb in embeddings.items():
            # Cosine similarity
            norm_q = np.linalg.norm(query_emb)
            norm_e = np.linalg.norm(emb)
            if norm_q > 0 and norm_e > 0:
                sim = np.dot(query_emb, emb) / (norm_q * norm_e)
            else:
                sim = 0.0
            if sim > best_sim:
                best_sim = sim
                best_idx = idx

        smiles = self.idx_to_smiles.get(cond_key, {}).get(best_idx, '')
        return best_idx, smiles

    def set_solvent_mixtures(self, mixtures: List[dict]):
        """Set dynamic solvent mixtures extracted from RAG retrieval.

        Args:
            mixtures: list of {'smiles': 'A.B', 'index': int} dicts
                      from RAGMeanPrior.solvent_mixtures
        """
        self._solvent_mixtures = mixtures

    def _pick_solvent_mixture(self, rng) -> Optional[tuple]:
        """Pick a random solvent mixture. Returns (index, smiles) or None.

        Prefers RAG-derived mixtures (reaction-specific); falls back to
        common mixtures if RAG pool is empty.
        """
        if self._solvent_mixtures:
            m = self._solvent_mixtures[int(rng.integers(len(self._solvent_mixtures)))]
            return m['index'], m['smiles']
        if COMMON_SOLVENT_MIXTURES:
            mix = COMMON_SOLVENT_MIXTURES[int(rng.integers(len(COMMON_SOLVENT_MIXTURES)))]
            solvent_vocab = self.idx_to_smiles.get('solvent', {})
            smiles_to_idx = {smi: idx for idx, smi in solvent_vocab.items()}
            first_comp = mix.split('.')[0]
            return smiles_to_idx.get(first_comp, 0), mix
        return None

    def sample_random(self, n: int, mixture_ratio: float = 0.46) -> List[dict]:
        """Sample n random condition combinations from the vocab.

        Args:
            n: number of samples
            mixture_ratio: probability of using a mixed solvent (~46% in training data)
        """
        rng = np.random.default_rng()
        # Exclude Unknown indices (last index for device conditions)
        valid_anode = list(range(0, NUM_ANODE - 1))    # exclude 22
        valid_cathode = list(range(0, NUM_CATHODE - 1))  # exclude 22
        valid_cell = list(range(0, NUM_CELL_TYPE - 1))   # exclude 5

        samples = []
        for _ in range(n):
            cond = {
                'anode_index': int(rng.choice(valid_anode)),
                'cathode_index': int(rng.choice(valid_cathode)),
                'cell_type_index': int(rng.choice(valid_cell)),
            }
            for cond_key in MOL_CONDITION_KEYS:
                if cond_key == 'solvent' and rng.random() < mixture_ratio:
                    mix = self._pick_solvent_mixture(rng)
                    if mix is not None:
                        cond['solvent_index'] = mix[0]
                        cond['solvent_smiles'] = mix[1]
                        continue
                idx_map = self.idx_to_smiles.get(cond_key, {})
                if idx_map:
                    valid_indices = [i for i in idx_map.keys() if i != 0]
                    if valid_indices:
                        chosen_idx = int(rng.choice(valid_indices))
                        cond[f'{cond_key}_index'] = chosen_idx
                        cond[f'{cond_key}_smiles'] = idx_map[chosen_idx]
                    else:
                        cond[f'{cond_key}_index'] = 0
                        cond[f'{cond_key}_smiles'] = ''
                else:
                    cond[f'{cond_key}_index'] = 0
                    cond[f'{cond_key}_smiles'] = ''
            samples.append(cond)
        return samples

    def get_m1_candidates(self, m1_predictions: dict, top_k: int = 5) -> List[dict]:
        """
        Build candidate condition dicts from M1 model top-k predictions.

        Args:
            m1_predictions: dict with keys like 'anode', 'cathode', etc.
                Each value is a list of {'label': ..., 'index': ..., 'confidence': ...}
            top_k: number of top candidates per condition type

        Returns:
            List of condition dicts formed by combining top-1 of each type,
            plus variants swapping each condition's top-2..top_k.
        """
        # Extract top-k indices per condition
        top_indices = {}
        for cond_key in ['anode', 'cathode', 'cell_type'] + MOL_CONDITION_KEYS:
            items = m1_predictions.get(cond_key, [])[:top_k]
            top_indices[cond_key] = [it['index'] for it in items] if items else [0]

        # Base candidate: all top-1
        base = {
            'anode_index': top_indices['anode'][0],
            'cathode_index': top_indices['cathode'][0],
            'cell_type_index': top_indices['cell_type'][0],
        }
        for cond_key in MOL_CONDITION_KEYS:
            idx = top_indices[cond_key][0]
            base[f'{cond_key}_index'] = idx
            base[f'{cond_key}_smiles'] = self.idx_to_smiles.get(cond_key, {}).get(idx, '')

        candidates = [base]

        # Variants: swap one condition at a time
        all_keys = ['anode', 'cathode', 'cell_type'] + MOL_CONDITION_KEYS
        for key in all_keys:
            for alt_idx in top_indices[key][1:]:
                variant = dict(base)
                if key in ('anode', 'cathode', 'cell_type'):
                    variant[f'{key}_index'] = alt_idx
                else:
                    variant[f'{key}_index'] = alt_idx
                    variant[f'{key}_smiles'] = self.idx_to_smiles.get(key, {}).get(alt_idx, '')
                candidates.append(variant)

        return candidates

    def perturb(self, conditions: dict, n: int = 5) -> List[dict]:
        """
        Generate local perturbations of a condition set.

        For device conditions: randomly swap one device category.
        For molecular conditions: pick a random neighbor from vocab or mixture.
        """
        rng = np.random.default_rng()
        perturbations = []

        for _ in range(n):
            variant = dict(conditions)
            # Pick a random condition to perturb
            all_keys = ['anode', 'cathode', 'cell_type'] + MOL_CONDITION_KEYS
            key = rng.choice(all_keys)

            if key == 'anode':
                variant['anode_index'] = int(rng.integers(0, NUM_ANODE))
            elif key == 'cathode':
                variant['cathode_index'] = int(rng.integers(0, NUM_CATHODE))
            elif key == 'cell_type':
                variant['cell_type_index'] = int(rng.integers(0, NUM_CELL_TYPE))
            elif key == 'solvent' and rng.random() < 0.46:
                mix = self._pick_solvent_mixture(rng)
                if mix is not None:
                    variant['solvent_index'] = mix[0]
                    variant['solvent_smiles'] = mix[1]
                else:
                    idx_map = self.idx_to_smiles.get('solvent', {})
                    valid_indices = [i for i in idx_map.keys() if i != 0]
                    if valid_indices:
                        chosen_idx = int(rng.choice(valid_indices))
                        variant['solvent_index'] = chosen_idx
                        variant['solvent_smiles'] = idx_map[chosen_idx]
            else:
                idx_map = self.idx_to_smiles.get(key, {})
                valid_indices = [i for i in idx_map.keys() if i != 0]
                if valid_indices:
                    chosen_idx = int(rng.choice(valid_indices))
                    variant[f'{key}_index'] = chosen_idx
                    variant[f'{key}_smiles'] = idx_map[chosen_idx]

            perturbations.append(variant)

        return perturbations
