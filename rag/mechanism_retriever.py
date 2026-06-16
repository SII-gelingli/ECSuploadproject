"""
MechanismRetriever: 给定反应 SMILES, 找机理相似的文献.

KB 结构 (build_mechanism_kb.py 输出):
- index.json: doi → mechanism record (rxn_class_summary / mechanism_family / electron_flow / ...)
- rxn2doi.json: reaction_smiles → [doi, ...]
- base_map.json: base_doi → [doi variants]  (允许 _sup/_si 后缀 fallback)
- doi_order.json: 顺序列表 (与 text_vectors 行号对应)
- tfidf_vectorizer.pkl: sklearn TF-IDF 模型
- text_vectors.npz: TF-IDF 矩阵 (sparse csr)

相似度 = α · Jaccard(family) + (1-α) · cosine(TF-IDF text)
默认 α=0.4 (家族标签信号干净但低维; 文本信号丰富但噪)
"""
import re, json, pickle
from pathlib import Path
from typing import List, Dict, Optional

import numpy as np


SUFFIX_STRIP = re.compile(r'(_sup_?\d*|_supl_?\d*|_si_?\d*|_esi_?\d*|_sm_?\d*)$', re.I)


def base_doi(doi: str) -> str:
    """剥 SI 后缀 + 全部小写化, 用于跟 split_meta 的 paper_id (canonical lowercase) 对齐."""
    if not doi: return ''
    return SUFFIX_STRIP.sub('', doi).lower()


class MechanismRetriever:
    """加载 mechanism KB, 提供 reaction_smiles → 相似 paper 检索."""

    def __init__(self, kb_dir):
        self._kb_dir = Path(kb_dir)
        self._records = None      # doi → record
        self._rxn2doi = None      # reaction_smiles → [doi]
        self._base_map = None     # base_doi → [doi variants]
        self._doi_order = None    # 列表, 行号 → doi
        self._doi_index = None    # doi → 行号
        self._vectorizer = None
        self._X = None            # sparse csr (N × F)
        self._family_sets = None  # doi → frozenset(family list)

    def _ensure_loaded(self):
        if self._records is not None: return
        with open(self._kb_dir / 'index.json') as f: self._records = json.load(f)
        with open(self._kb_dir / 'rxn2doi.json') as f: self._rxn2doi = json.load(f)
        with open(self._kb_dir / 'base_map.json') as f: self._base_map = json.load(f)
        with open(self._kb_dir / 'doi_order.json') as f: self._doi_order = json.load(f)
        with open(self._kb_dir / 'tfidf_vectorizer.pkl', 'rb') as f:
            self._vectorizer = pickle.load(f)
        from scipy.sparse import load_npz
        self._X = load_npz(self._kb_dir / 'text_vectors.npz')
        self._doi_index = {d: i for i, d in enumerate(self._doi_order)}
        self._family_sets = {
            d: frozenset(r.get('mechanism_family') or [])
            for d, r in self._records.items()
        }

    # ── public API ─────────────────────────────────────────────

    def lookup_by_reaction(self, reaction_smiles: str) -> Optional[Dict]:
        """直接取该反应所在文献的机理记录 (可能多篇 paper, 取第一个有 mechanism 记录的)."""
        self._ensure_loaded()
        dois = self._rxn2doi.get(reaction_smiles) or []
        # 先尝试直接 DOI
        for d in dois:
            if d in self._records:
                return self._records[d]
        # 退到 base DOI (剥掉 _sup_1 等后缀)
        for d in dois:
            bd = base_doi(d)
            for cand in self._base_map.get(bd, []):
                if cand in self._records:
                    return self._records[cand]
        return None

    def search_by_reaction(self, reaction_smiles: str,
                           top_k: int = 5, family_weight: float = 0.4,
                           include_query_paper: bool = False,
                           exclude_paper_ids: Optional[set] = None,
                           exclude_reaction_smiles: Optional[set] = None) -> List[Dict]:
        """该反应的机理 → 找机理相似的 paper.

        exclude_paper_ids: 排除论文 ID 集合 (base_doi lowercase 形式).
        exclude_reaction_smiles: 排除反应 SMILES 集合 — 若查询反应自己在内,
            seed 也算泄漏 (因为 KB 已记录了某论文有这反应的机理).
        """
        self._ensure_loaded()
        # 跨 paper 同反应泄漏: 若 query 反应 SMILES 本身就是 test 集成员,
        # 任何 KB 返回的 seed 都是"已知该反应的机理摘要" -> 视为泄漏
        is_query_in_exclude_rxn = bool(
            exclude_reaction_smiles and reaction_smiles in exclude_reaction_smiles)
        seed = self.lookup_by_reaction(reaction_smiles)
        if seed is None:
            return {'seed_paper': None, 'seed_excluded': False, 'matches': []}
        seed_bdoi = base_doi(seed.get('doi', ''))
        seed_in_exclude = (
            (exclude_paper_ids and seed_bdoi in exclude_paper_ids) or
            is_query_in_exclude_rxn
        )
        results = self._search_by_record(
            seed, top_k=top_k, family_weight=family_weight,
            exclude_doi=None if include_query_paper else seed['doi'],
            exclude_paper_ids=exclude_paper_ids,
        )
        return {
            'seed_paper': None if seed_in_exclude else self._record_summary(seed),
            'seed_excluded': bool(seed_in_exclude),
            'matches': results,
        }

    def search_by_mechanism_family(self, families: List[str],
                                    free_text: str = '',
                                    top_k: int = 5, family_weight: float = 0.4,
                                    exclude_paper_ids: Optional[set] = None) -> List[Dict]:
        """用户直接给机理家族 (+ 可选文本) 来检索."""
        self._ensure_loaded()
        pseudo = {
            'doi': '__query__', 'mechanism_family': families or [],
            'rxn_class_summary': free_text, 'electron_flow': '',
            'rate_determining_step': '', 'electrochemical_role': '',
            'key_intermediates': [], 'notes': '',
            'evidence_types_used': [], 'evidence_strength': '',
        }
        return self._search_by_record(pseudo, top_k=top_k,
                                      family_weight=family_weight,
                                      exclude_doi=None,
                                      exclude_paper_ids=exclude_paper_ids)

    # ── internals ──────────────────────────────────────────────

    def _make_text_blob(self, record: dict) -> str:
        parts = [
            record.get('rxn_class_summary', ''),
            record.get('electrochemical_role', ''),
            record.get('electron_flow', ''),
            record.get('rate_determining_step', ''),
            record.get('notes', ''),
        ]
        for ki in record.get('key_intermediates') or []:
            if isinstance(ki, dict): parts.append(ki.get('name', '') or '')
        parts.extend(record.get('mechanism_family') or [])
        parts.extend(record.get('evidence_types_used') or [])
        return ' '.join(p for p in parts if p).strip()

    def _search_by_record(self, query_record: dict, top_k: int,
                          family_weight: float, exclude_doi: Optional[str],
                          exclude_paper_ids: Optional[set] = None) -> List[Dict]:
        q_family = frozenset(query_record.get('mechanism_family') or [])
        q_text = self._make_text_blob(query_record)
        q_vec = self._vectorizer.transform([q_text]) if q_text else None

        # cosine on TF-IDF (sparse safe). 已 L2 normalize by sklearn -> dot product works
        if q_vec is not None and q_vec.nnz > 0:
            text_sim = (self._X @ q_vec.T).toarray().ravel()
        else:
            text_sim = np.zeros(self._X.shape[0])

        out = []
        for i, doi in enumerate(self._doi_order):
            if exclude_doi and doi == exclude_doi: continue
            # 论文级排除 (按 base_doi 匹配, 同时排除 _sup/_si 变体)
            if exclude_paper_ids and base_doi(doi) in exclude_paper_ids:
                continue
            cand_fam = self._family_sets.get(doi, frozenset())
            # Jaccard 相似
            if q_family and cand_fam:
                inter = len(q_family & cand_fam)
                union = len(q_family | cand_fam)
                fam_sim = inter / max(union, 1)
            else:
                fam_sim = 0.0
            score = family_weight * fam_sim + (1 - family_weight) * float(text_sim[i])
            out.append((doi, fam_sim, float(text_sim[i]), score))

        out.sort(key=lambda x: x[3], reverse=True)
        results = []
        for doi, fs, ts, sc in out[:top_k]:
            rec = self._records[doi]
            r = self._record_summary(rec)
            r['family_jaccard'] = round(fs, 4)
            r['text_cosine'] = round(ts, 4)
            r['combined_score'] = round(sc, 4)
            r['shared_families'] = sorted(q_family & frozenset(rec.get('mechanism_family') or []))
            results.append(r)
        return results

    def _record_summary(self, rec: dict) -> Dict:
        """节选 paper 字段给 LLM (不返回全部 key_intermediates 完整 list, 太长)."""
        kis = rec.get('key_intermediates') or []
        ki_short = [
            {'name': k.get('name', '')[:120], 'role': k.get('role', '')}
            for k in kis[:5] if isinstance(k, dict)
        ]
        return {
            'doi': rec.get('doi', ''),
            'journal': rec.get('journal', ''),
            'rxn_class_summary': rec.get('rxn_class_summary', ''),
            'mechanism_family': rec.get('mechanism_family') or [],
            'electrochemical_role': rec.get('electrochemical_role', ''),
            'electron_flow': rec.get('electron_flow', '')[:600],  # 截断防止 token 爆炸
            'rate_determining_step': rec.get('rate_determining_step', ''),
            'evidence_types_used': rec.get('evidence_types_used') or [],
            'evidence_strength': rec.get('evidence_strength', ''),
            'key_intermediates_top5': ki_short,
        }

    @property
    def num_papers(self) -> int:
        self._ensure_loaded()
        return len(self._records)

    @property
    def num_reactions_linked(self) -> int:
        self._ensure_loaded()
        return len(self._rxn2doi)
