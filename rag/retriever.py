"""
ReactionRetriever: cosine similarity search for similar reactions.

Uses FAISS IndexFlatIP on L2-normalized fingerprints, with a numpy
brute-force fallback when FAISS is unavailable.

Supports yield-aware reranking and condition statistics aggregation.
"""
import pickle
import numpy as np
from collections import Counter
from pathlib import Path
from typing import List, Dict, Optional


class ReactionRetriever:
    """
    Retrieve similar reactions from the training set using cosine similarity
    on 6144D reaction fingerprints.

    Features:
    - Yield-aware reranking: combines fingerprint similarity with reaction yield
    - Condition statistics: aggregates condition distributions from retrieved results
    - Min-yield filtering: exclude low-yield reactions from results
    """

    def __init__(self, index_path: str, db_path: str):
        self._index = None
        self._np_matrix = None
        self._reaction_db = None
        self._index_path = index_path
        self._db_path = db_path
        self._use_faiss = False

    _load_lock = __import__('threading').Lock()

    def _ensure_loaded(self):
        with self._load_lock:
            return self._ensure_loaded_unsafe()

    def _ensure_loaded_unsafe(self):
        """Lazy-load index and database."""
        if self._reaction_db is not None:
            return

        # Load reaction database
        with open(self._db_path, 'rb') as f:
            self._reaction_db = pickle.load(f)

        # Try FAISS first, fall back to numpy
        try:
            import faiss
            if Path(self._index_path).exists():
                self._index = faiss.read_index(self._index_path)
                self._use_faiss = True
                return
        except ImportError:
            pass

        # Numpy fallback
        npy_path = self._index_path.replace('.bin', '.npy')
        if Path(npy_path).exists():
            self._np_matrix = np.load(npy_path)
        else:
            raise FileNotFoundError(
                f"Neither FAISS index ({self._index_path}) nor numpy matrix ({npy_path}) found. "
                "Run build_index.py first."
            )

    def search(
        self,
        query_fp: np.ndarray,
        top_k: int = 5,
        threshold: float = 0.3,
        min_yield: Optional[float] = None,
        rerank_by_yield: bool = False,
        sim_weight: float = 0.6,
        yield_weight: float = 0.4,
        exclude_paper_ids: Optional[set] = None,
        exclude_reaction_smiles: Optional[set] = None,
    ) -> List[Dict]:
        """
        Search for similar reactions.

        Args:
            query_fp: 6144D reaction fingerprint (will be L2-normalized)
            top_k: number of results to return
            threshold: minimum cosine similarity threshold
            min_yield: if set, exclude reactions with yield below this value
            rerank_by_yield: if True, rerank results using combined score
                             (sim_weight * similarity + yield_weight * yield/100)
            sim_weight: weight for similarity in combined score (default: 0.6)
            yield_weight: weight for yield in combined score (default: 0.4)

        Returns:
            List of dicts with 'similarity' and reaction metadata.
        """
        self._ensure_loaded()

        # L2-normalize query
        query = query_fp.astype(np.float32).reshape(1, -1)
        norm = np.linalg.norm(query)
        if norm > 0:
            query = query / norm

        # Retrieve more candidates for filtering/reranking/exclusion
        need_extra = bool(min_yield or rerank_by_yield or exclude_paper_ids or exclude_reaction_smiles)
        # 之前 100 不够: 同一篇 paper 的多个 sub-reaction 聚簇时会全被排掉
        fetch_k = max(top_k * 50, 500) if need_extra else top_k * 2

        if self._use_faiss:
            scores, indices = self._index.search(query, min(fetch_k, self._index.ntotal))
            scores = scores[0]
            indices = indices[0]
        else:
            # Brute-force cosine similarity
            scores = (self._np_matrix @ query.T).flatten()
            top_indices = np.argsort(scores)[::-1][:fetch_k]
            scores = scores[top_indices]
            indices = top_indices

        candidates = []
        for score, idx in zip(scores, indices):
            if idx < 0 or idx >= len(self._reaction_db):
                continue
            sim = float(score)
            if sim < threshold:
                break

            entry = dict(self._reaction_db[idx])
            entry['similarity'] = round(sim, 4)

            # Apply paper-id exclusion (论文级零泄漏)
            if exclude_paper_ids and entry.get('paper_id') in exclude_paper_ids:
                continue
            # 跨 paper 同反应排除: 相同 SMILES 在多 paper 出现时
            # 仍要排除等价于 GT 的副本 (即使该副本 paper_id 不在 test_pids)
            if exclude_reaction_smiles and entry.get('reaction_smiles') in exclude_reaction_smiles:
                continue

            # Apply min_yield filter
            if min_yield is not None:
                entry_yield = entry.get('yield')
                if entry_yield is None or entry_yield < min_yield:
                    continue

            candidates.append(entry)

        # Rerank by combined score if requested
        if rerank_by_yield and candidates:
            for c in candidates:
                c_yield = c.get('yield')
                yield_score = (c_yield / 100.0) if c_yield is not None else 0.0
                c['combined_score'] = round(
                    sim_weight * c['similarity'] + yield_weight * yield_score, 4
                )
            candidates.sort(key=lambda x: x['combined_score'], reverse=True)

        return candidates[:top_k]

    def get_condition_statistics(self, results: List[Dict]) -> Dict:
        """
        Aggregate condition statistics from retrieved reactions.

        Returns a summary of most common conditions and yield statistics,
        useful for evidence-based recommendations.
        """
        if not results:
            return {'num_results': 0}

        yields = [r['yield'] for r in results if r.get('yield') is not None]
        currents = [r.get('current_mA') for r in results if r.get('current_mA') is not None]
        densities = [r.get('current_density_mA_cm2') for r in results if r.get('current_density_mA_cm2') is not None]

        anodes = Counter(r.get('anode', 'Unknown') for r in results if r.get('anode') != 'Unknown')
        cathodes = Counter(r.get('cathode', 'Unknown') for r in results if r.get('cathode') != 'Unknown')
        cell_types = Counter(r.get('cell_type', 'Unknown') for r in results if r.get('cell_type') != 'Unknown')
        electrolytes = Counter(r.get('electrolyte', '') for r in results if r.get('electrolyte'))
        solvents = Counter()
        for r in results:
            for s in r.get('solvents', []):
                if s:
                    solvents[s] += 1

        stats = {
            'num_results': len(results),
            'yield_stats': {
                'mean': round(np.mean(yields), 1) if yields else None,
                'max': round(float(max(yields)), 1) if yields else None,
                'min': round(float(min(yields)), 1) if yields else None,
                'median': round(float(np.median(yields)), 1) if yields else None,
            },
            'current_stats': {
                'mean_mA': round(np.mean(currents), 1) if currents else None,
                'range_mA': [round(float(min(currents)), 1), round(float(max(currents)), 1)] if currents else None,
                'num_with_data': len(currents),
            },
            'current_density_stats': {
                'mean_mA_cm2': round(np.mean(densities), 1) if densities else None,
                'range_mA_cm2': [round(float(min(densities)), 1), round(float(max(densities)), 1)] if densities else None,
                'num_with_data': len(densities),
            },
            'most_common_anode': anodes.most_common(3) if anodes else [],
            'most_common_cathode': cathodes.most_common(3) if cathodes else [],
            'most_common_cell_type': cell_types.most_common(3) if cell_types else [],
            'most_common_electrolyte': electrolytes.most_common(3) if electrolytes else [],
            'most_common_solvent': solvents.most_common(3) if solvents else [],
        }

        return stats

    @property
    def num_reactions(self) -> int:
        self._ensure_loaded()
        return len(self._reaction_db)
