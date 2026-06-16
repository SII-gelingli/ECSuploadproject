"""
Tool handler implementations for the agent tools.

Each handler takes a tool input dict and returns a JSON-serializable result dict.
"""
import json
import base64
import io
import numpy as np
import torch
import torch.nn.functional as F
from pathlib import Path
from collections import Counter
from typing import Dict, List, Any, Optional

from rdkit.Chem import AllChem, Draw

from config import (
    ELECTRODE_NAMES, CELL_TYPE_NAMES, UNKNOWN_INDICES,
    FINGERPRINT_SIZE, AGENT_ROOT, VOCAB_PATH,
)
from utils.smiles_utils import (
    parse_reaction_smiles, validate_smiles,
    compute_reaction_fingerprint, get_molecular_info,
)


class ToolExecutor:
    """
    Executes the agent tools using the ModelManager and ReactionRetriever.

    Maintains a fingerprint cache to avoid recomputation for the same reaction
    across multiple tool calls.
    """

    def __init__(self, model_manager, retriever=None, mechanism_retriever=None):
        """
        Args:
            model_manager: ModelManager instance (lazy-loads models)
            retriever: ReactionRetriever instance (may be None if index not built)
            mechanism_retriever: MechanismRetriever instance (may be None if KB not built)
        """
        self.mm = model_manager
        self.retriever = retriever
        self.mechanism_retriever = mechanism_retriever
        self._fp_cache = {}  # reaction_smiles -> fingerprint
        self._bo_states = {}  # reaction_smiles -> BayesianConditionOptimizer state

    def _get_reaction_fp(self, reaction_smiles: str, xtb_lookup=None) -> np.ndarray:
        """Get or compute reaction fingerprint, with caching."""
        cache_key = (reaction_smiles, id(xtb_lookup))
        if cache_key in self._fp_cache:
            return self._fp_cache[cache_key]

        reactants, products = parse_reaction_smiles(reaction_smiles)
        fp = compute_reaction_fingerprint(
            reactants, products, self.mm.mol_extractor, xtb_lookup
        )
        self._fp_cache[cache_key] = fp
        return fp

    def execute(self, tool_name: str, tool_input: Dict) -> str:
        """
        Dispatch to the appropriate tool handler.

        Returns: JSON string of the tool result.
        """
        handlers = {
            'validate_smiles': self._handle_validate_smiles,
            'parse_reaction': self._handle_parse_reaction,
            'recommend_conditions_default': self._handle_recommend_default,
            'generate_conditions_cvae': self._handle_generate_cvae,
            'predict_yield': self._handle_predict_yield,
            'search_similar_reactions': self._handle_search_similar,
            'search_mechanism': self._handle_search_mechanism,
            'analyze_reaction_chemistry': self._handle_analyze_reaction_chemistry,
            'estimate_experimental_parameters': self._handle_estimate_experimental_parameters,
            'generate_experimental_protocol': self._handle_generate_protocol,
            'draw_reaction': self._handle_draw_reaction,
            'optimize_conditions_bo': self._handle_optimize_conditions_bo,
        }

        handler = handlers.get(tool_name)
        if handler is None:
            return json.dumps({"error": f"Unknown tool: {tool_name}"})

        try:
            result = handler(tool_input)
            return json.dumps(result, ensure_ascii=False, default=str)
        except Exception as e:
            return json.dumps({"error": f"{type(e).__name__}: {str(e)}"})

    # ── Tool 1: validate_smiles ────────────────────────────────

    def _handle_validate_smiles(self, inputs: Dict) -> Dict:
        smiles_list = inputs.get('smiles_list', [])
        results = get_molecular_info(smiles_list)
        return {"results": results}

    # ── Tool 2: parse_reaction ─────────────────────────────────

    def _handle_parse_reaction(self, inputs: Dict) -> Dict:
        reaction_smiles = inputs['reaction_smiles']
        reactants, products = parse_reaction_smiles(reaction_smiles)

        reactant_info = get_molecular_info(reactants)
        product_info = get_molecular_info(products)

        return {
            "reaction_smiles": reaction_smiles,
            "reactants": reactant_info,
            "products": product_info,
            "num_reactants": len(reactants),
            "num_products": len(products),
        }

    # ── Tool 3: recommend_conditions_default ───────────────────

    def _handle_recommend_default(self, inputs: Dict) -> Dict:
        """Recommend conditions using V3 Hier+Set+SMI model (2026-05-20).

        V3 model 输出比老 ConditionRecommender 丰富很多:
        - electrolyte 拆 cation+anion 双 head
        - solvent/reagent/catalyst 用 set head (K=4 slot, 多组分)
        - 新增 ligand/additive 具体 SMILES head
        - 新增 catalyst 机制 tags (mediator/photoredox/HAT/chiral)
        - 新增 v3 hier 粗类 (reagent_class/catalyst_class/solvent_class)

        输出保留 anode/cathode/cell_type/electrolyte/solvent/reagent/catalyst 7 个字段向后兼容,
        + 新字段 ligand/additive/mechanism_tags/v3_hier_classes。
        """
        from yp_models.condition_stage1_set import decode_set_topk

        reaction_smiles = inputs['reaction_smiles']
        top_k = inputs.get('top_k', 3)
        top_k_set = inputs.get('top_k_set', max(top_k, 5))  # set head 默认更多候选

        # V3 用纯 Morgan FP (无 xTB)
        fp = self._get_reaction_fp(reaction_smiles, xtb_lookup=None)
        features = torch.from_numpy(np.asarray(fp, dtype=np.float32)).unsqueeze(0)

        model = self.mm.v3_model
        stats = self.mm.v3_stats
        nc = stats['num_classes']
        idx_maps = self.mm.v3_idx_maps
        device = self.mm.device

        with torch.no_grad():
            out = model(features.to(device), teacher=None)

        def topk_class(head, name_map, k=top_k):
            """Single class head Top-K"""
            logits = out[head]
            probs = F.softmax(logits, dim=-1)
            kk = min(k, probs.size(-1))
            tp, ti = torch.topk(probs, kk, dim=-1)
            items = []
            for idx, prob in zip(ti[0].tolist(), tp[0].tolist()):
                label = name_map.get(idx, f'Unknown (idx={idx})')
                # 跳过 wildcard SMILES
                if label.startswith('__') or label == '*':
                    continue
                items.append({'label': label, 'confidence': round(prob, 4), 'index': idx})
            return items

        from yp_models.condition_stage1_set import decode_set
        from yp_models.condition_stage1_hier_set_v3 import K_SLOTS

        def topk_set(head, name_map, k=top_k_set):
            """Set head (K=4 slot) → Top-K candidates across slots"""
            slots = out[head]
            no_obj = nc[head]
            cand_ids = decode_set_topk(slots, no_obj, K_total=k)[0]
            with torch.no_grad():
                probs_per_slot = F.softmax(slots, dim=-1)
                max_probs = probs_per_slot[0, :, :no_obj].max(dim=0).values
            items = []
            for idx in cand_ids:
                if idx >= no_obj or idx < 0: continue
                smi = name_map.get(idx, f'?(idx={idx})')
                if smi.startswith('__') or smi == '*': continue
                items.append({
                    'label': smi,
                    'smiles': smi,
                    'confidence': round(float(max_probs[idx]), 4),
                    'index': idx,
                })
            return items

        def predicted_set(head, name_map):
            """模型实际预测的多组分集合 — 用 decode_set 每个 slot argmax 后去重."""
            slots = out[head]
            no_obj = nc[head]
            # decode_set 返回 list[list[int]]
            pred_ids = decode_set(slots, no_obj)[0]
            with torch.no_grad():
                probs_per_slot = F.softmax(slots, dim=-1)
            # 找每个 slot argmax (含 no_obj) 拿对应概率
            slot_preds = []  # [(slot_idx, smi, prob), ...]
            for slot_idx in range(K_SLOTS):
                slot_probs = probs_per_slot[0, slot_idx]
                top_id = int(slot_probs.argmax().item())
                top_prob = float(slot_probs[top_id].item())
                if top_id < no_obj:
                    smi = name_map.get(top_id, '')
                    if smi and not smi.startswith('__') and smi != '*':
                        slot_preds.append({'slot': slot_idx, 'smiles': smi,
                                           'confidence': round(top_prob, 4)})
            # 去重 (set 含义)
            seen = set()
            unique = []
            for p in slot_preds:
                if p['smiles'] not in seen:
                    seen.add(p['smiles']); unique.append(p)
            return unique  # 0-4 个不同 SMILES, 模型实际预测的混合

        # === 主要字段 (向后兼容老 condition_model 输出格式) ===
        results = {}
        # 电极/池型/电解质 — V3 用 class 体系不同, 名字保留旧 key 但内容是 V3 类
        results['anode'] = topk_class('anode_material', idx_maps['anode_material'])
        results['cathode'] = topk_class('cathode_material', idx_maps['cathode_material'])
        results['cell_type'] = topk_class('cell_class_v3', idx_maps['cell_class_v3'])
        # 细粒度电极 (材料 × 形状, 43/49 类)
        if 'anode_fine' in out:
            results['anode_fine'] = topk_class('anode_fine', idx_maps.get('anode_fine', {}))
        if 'cathode_fine' in out:
            results['cathode_fine'] = topk_class('cathode_fine', idx_maps.get('cathode_fine', {}))
        # 电解质拆 cation + anion (拼接成可读字符串)
        cat_items = topk_class('electrolyte_cation', idx_maps['electrolyte_cation'])
        an_items = topk_class('electrolyte_anion', idx_maps['electrolyte_anion'])
        # 组合: cation × anion top-K 对
        elec_combos = []
        for c in cat_items[:top_k]:
            for a in an_items[:top_k]:
                elec_combos.append({
                    'label': f"{c['label']}-{a['label']}",
                    'cation': c['label'], 'anion': a['label'],
                    'confidence': round(c['confidence'] * a['confidence'], 4),
                })
        elec_combos.sort(key=lambda x: -x['confidence'])
        results['electrolyte'] = elec_combos[:top_k_set]

        # solvent/reagent/catalyst — V3 用 set head 输出多组分 SMILES 候选
        results['solvent'] = topk_set('solvent', idx_maps['solvent'])
        results['reagent'] = topk_set('reagent', idx_maps['reagent'])
        results['catalyst'] = topk_set('catalyst', idx_maps['catalyst'])

        # 模型实际预测的多组分集合 (key: 每个 set head 实际预测了几个组分)
        # 例如 solvent_predicted_set = [{slot:0, smiles:"ClCCl", confidence:0.66},
        #                                {slot:1, smiles:"O", confidence:0.45}]
        # 表示模型认为本反应应该用 DCM + 水 两个溶剂
        predicted_sets = {
            'solvent': predicted_set('solvent', idx_maps['solvent']),
            'reagent': predicted_set('reagent', idx_maps['reagent']),
            'catalyst': predicted_set('catalyst', idx_maps['catalyst']),
        }

        # === V3 新增字段 ===
        # ligand/additive 具体 SMILES (single head)
        results['ligand'] = topk_class('ligand', idx_maps['ligand'], k=top_k)
        results['additive'] = topk_class('additive', idx_maps['additive'], k=top_k)

        # catalyst 机制 tags (multi-label sigmoid)
        TAG_NAMES = ['mediator', 'photoredox', 'HAT', 'chiral']
        tag_logits = out['catalyst_mech_tags'][0]
        tag_probs = torch.sigmoid(tag_logits).tolist()
        mech_tags = [
            {'tag': TAG_NAMES[i], 'probability': round(tag_probs[i], 4),
             'predicted_positive': bool(tag_probs[i] > 0.5)}
            for i in range(4)
        ]

        # v3 hier 粗类 (chemical class signal)
        v3_hier = {
            'reagent_class': topk_class('reagent_class_v3', idx_maps['reagent_class_v3'], k=top_k),
            'catalyst_class': topk_class('catalyst_class_v3', idx_maps['catalyst_class_v3'], k=top_k),
            'solvent_class': topk_class('solvent_class_v3', idx_maps['solvent_class_v3'], k=top_k),
            'ligand_class': topk_class('ligand_class_v3', idx_maps['ligand_class_v3'], k=top_k),
            'additive_class': topk_class('additive_class_v3', idx_maps['additive_class_v3'], k=top_k),
        }

        # === Stage-2 用量回归 (V3 stage1 推理结果作 condition GT, 然后 stage2 出用量) ===
        stage2_amounts = None
        try:
            from yp_models.condition_stage2 import AMOUNT_FIELDS, HEAD_KEYS
            stage2 = self.mm.stage2_model
            amount_stats = self.mm.stage2_amount_stats
            # Stage-2 用 V2 head 的 class index (anode/cathode/cell_type/solvent/electrolyte/catalyst/reagent/ligand/additive)
            # V3 Stage-1 输出是 V3 类索引, 但 train.pt 里 V2 字段也存在 (labels['anode'] 等)
            # 推理时, 我们没有 train.pt — 必须从 V3 head 推断 V2 idx
            # 简化: 用 Stage-1 V3 输出的 argmax → V2 vocab 反查 SMILES → V2 vocab 正查 idx
            # 但 anode/cathode 是字符串名 (V3 材料家族), 对 V2 是 electrode_name → idx
            from config import ELECTRODE_NAMES, CELL_TYPE_NAMES
            v3_vocab = self.mm.v3_vocab
            # 旧 head idx 推断
            v2_idx = {}
            # anode/cathode: 反查 ELECTRODE_NAMES (V2 23 类, V3 15 类不完全匹配)
            # 简化做法: 用 V3 head argmax → 类名字符串 → V2 ELECTRODE_NAMES 找最接近的
            anode_name = idx_maps['anode_material'].get(out['anode_material'].argmax().item(), 'ABSENT')
            cath_name = idx_maps['cathode_material'].get(out['cathode_material'].argmax().item(), 'ABSENT')
            name_to_v2 = {v: k for k, v in ELECTRODE_NAMES.items()}
            v2_idx['anode'] = name_to_v2.get(anode_name, 22)   # 22 = ABSENT
            v2_idx['cathode'] = name_to_v2.get(cath_name, 22)
            # cell_type: V3 cell_class_v3 直接对应 V2 cell_type
            v2_idx['cell_type'] = out['cell_class_v3'].argmax().item()
            # solvent/electrolyte/catalyst/reagent/ligand/additive: 取 V3 set head/SMI head Top-1 SMILES → V2 vocab idx
            for h in ['solvent', 'reagent', 'catalyst']:
                # V3 set head Top-1 SMILES
                if results[h]:
                    top_smi = results[h][0].get('smiles', '') or results[h][0].get('label', '')
                    v2_idx[h] = v3_vocab.get(h, {}).get(top_smi, 0)
                else:
                    v2_idx[h] = 0
            # electrolyte/ligand/additive — 这些 v3 输出是 SMILES (electrolyte 是 cation×anion 拼接, 略复杂)
            v2_idx['electrolyte'] = 0  # 不容易反推 cation+anion → SMILES, 直接置 0 (ABSENT)
            for h in ['ligand', 'additive']:
                if results[h]:
                    top_smi = results[h][0].get('label', '')
                    v2_idx[h] = v3_vocab.get(h, {}).get(top_smi, 0)
                else:
                    v2_idx[h] = 0
            # Run Stage-2
            cat_idx_tensor = {k: torch.tensor([v2_idx.get(k, 0)], dtype=torch.long, device=device)
                              for k in HEAD_KEYS}
            with torch.no_grad():
                amounts_out = stage2(features.to(device), cat_idx_tensor)

            # Inline inverse_transform (avoid script-path dependency)
            def inverse_transform(norm_values, stats_):
                t = norm_values * stats_['norm_std'] + stats_['norm_mean']
                if stats_['transform'] == 'log':
                    return np.exp(t) - stats_['offset']
                if stats_['transform'] == 'temperature':
                    return t * 30.0 + 25.0
                return t
            stage2_amounts = {}
            for f in AMOUNT_FIELDS:
                norm = float(amounts_out[f][0].item())
                raw = float(inverse_transform(np.array([norm]), amount_stats[f])[0])
                # Round to sensible precision
                if f in ('current_mA', 'temperature_C', 'time_h', 'reagent_equiv', 'additive_equiv'):
                    raw = round(raw, 1)
                elif f in ('current_density', 'potential_V', 'catalyst_equiv', 'ligand_equiv'):
                    raw = round(raw, 2)
                elif f == 'electrolyte_M':
                    raw = round(raw, 3)
                stage2_amounts[f] = raw
        except Exception as _e:
            stage2_amounts = {'error': f'{type(_e).__name__}: {_e}'}

        return {
            "reaction_smiles": reaction_smiles,
            "model_type": "ConditionStage1HierSetV3+SMI + Stage2 (新数据, 2026-05-20)",
            "model_avg_6head": 0.5256,
            "top_k": top_k,
            "recommendations": results,
            "predicted_sets": predicted_sets,
            "v3_hier_classes": v3_hier,
            "catalyst_mech_tags": mech_tags,
            "amounts": stage2_amounts,
        }

    # ── Tool 4: generate_conditions_cvae ───────────────────────

    def _handle_generate_cvae(self, inputs: Dict) -> Dict:
        reaction_smiles = inputs['reaction_smiles']
        num_samples = inputs.get('num_samples', 10)
        temperature = inputs.get('temperature', 1.0)
        top_k = inputs.get('top_k', 3)

        xtb_lookup = self.mm.cvae_xtb_lookup
        fp = self._get_reaction_fp(reaction_smiles, xtb_lookup)
        features_tensor = torch.tensor([fp], dtype=torch.float32)

        model = self.mm.cvae_model
        idx_maps = self.mm.idx_maps
        device = self.mm.device

        name_maps = {
            'anode': ELECTRODE_NAMES,
            'cathode': ELECTRODE_NAMES,
            'cell_type': CELL_TYPE_NAMES,
            'electrolyte': idx_maps['electrolyte'],
            'solvent': idx_maps['solvent'],
            'reagent': idx_maps['reagent'],
            'catalyst': idx_maps['catalyst'],
        }

        # 1) z=0 deterministic prediction -> per-condition top-k
        model.eval()
        with torch.no_grad():
            z0_preds = model.recommend(features_tensor.to(device))

        topk_results = {}
        for cond_key, name_map in name_maps.items():
            # Support both old format (xxx_logits) and new format (xxx)
            logit_key = f'{cond_key}_logits' if f'{cond_key}_logits' in z0_preds else cond_key
            logits = z0_preds[logit_key]
            if cond_key in UNKNOWN_INDICES:
                logits = logits.clone()
                logits[:, UNKNOWN_INDICES[cond_key]] = float('-inf')
            probs = F.softmax(logits, dim=-1)
            k = min(top_k, probs.size(-1))
            top_probs, top_indices = torch.topk(probs, k, dim=-1)
            items = []
            for idx, prob in zip(top_indices[0].tolist(), top_probs[0].tolist()):
                label = name_map.get(idx, f'Unknown (idx={idx})')
                items.append({'label': label, 'confidence': round(prob, 4), 'index': idx})
            topk_results[cond_key] = items

        # 2) Multi-z sampling -> diverse joint condition schemes
        gen_results = model.generate(
            features_tensor.to(device),
            num_samples=num_samples,
            temperature=temperature,
        )

        schemes = []
        seen = set()
        for r in gen_results:
            labels = r['labels']
            preds = r['predictions']
            log_prob = r['log_prob'][0].item()

            scheme = {}
            key_tuple = []
            for cond_key in ['anode', 'cathode', 'cell_type', 'electrolyte',
                             'solvent', 'reagent', 'catalyst']:
                unk_idx = UNKNOWN_INDICES.get(cond_key)
                sampled_idx = labels[cond_key][0].item()
                if unk_idx is not None and sampled_idx == unk_idx:
                    cond_logits = preds[f'{cond_key}_logits'].clone()
                    cond_logits[:, unk_idx] = float('-inf')
                    idx = cond_logits.argmax(dim=-1)[0].item()
                else:
                    idx = sampled_idx
                name = name_maps[cond_key].get(idx, f'Unknown (idx={idx})')
                scheme[cond_key] = {'label': name, 'index': idx}
                key_tuple.append(idx)

            key_tuple = tuple(key_tuple)
            if key_tuple in seen:
                continue
            seen.add(key_tuple)

            scheme['joint_log_prob'] = round(log_prob, 4)
            scheme['joint_probability'] = round(float(np.exp(log_prob)), 6)
            schemes.append(scheme)

        schemes.sort(key=lambda s: s['joint_log_prob'], reverse=True)

        return {
            "reaction_smiles": reaction_smiles,
            "model_type": "CategoricalCVAE",
            "top_k": top_k,
            "num_samples": num_samples,
            "temperature": temperature,
            "topk_recommendations": topk_results,
            "joint_schemes": schemes,
            "num_unique_schemes": len(schemes),
        }

    # ── Tool 5: predict_yield ──────────────────────────────────

    def _handle_predict_yield(self, inputs: Dict) -> Dict:
        reaction_smiles = inputs['reaction_smiles']
        conditions_list = inputs['conditions']
        compute_uncertainty = inputs.get('compute_uncertainty', False)

        reactants, products = parse_reaction_smiles(reaction_smiles)
        mol_extractor = self.mm.mol_extractor

        # Base 6144D fingerprint
        reactant_fp = mol_extractor.encode_molecules(reactants)
        product_fp = mol_extractor.encode_molecules(products)
        diff_fp = np.abs(product_fp - reactant_fp)
        reaction_fp_base = np.concatenate([reactant_fp, product_fp, diff_fp])

        yield_model = self.mm.yield_model
        yield_input_dim = self.mm.yield_input_dim
        device = self.mm.device

        # Check if yield model needs xTB features (input_dim > 10246)
        base_dim = 5 * FINGERPRINT_SIZE + 6  # 10246
        needs_xtb = yield_input_dim > base_dim
        xtb_lookup = None
        if needs_xtb:
            xtb_lookup = self.mm._get_xtb_lookup(yield_input_dim)

        results = []
        for cond in conditions_list:
            solvent_smiles = cond.get('solvent_smiles', '')
            electrolyte_smiles = cond.get('electrolyte_smiles', '')
            anode_idx = cond.get('anode_index', 0)
            cathode_idx = cond.get('cathode_index', 0)
            cell_type_idx = cond.get('cell_type_index', 0)

            solvent_fp = mol_extractor.get_morgan_fingerprint(solvent_smiles) if solvent_smiles else np.zeros(FINGERPRINT_SIZE)
            electrolyte_fp = mol_extractor.get_morgan_fingerprint(electrolyte_smiles) if electrolyte_smiles else np.zeros(FINGERPRINT_SIZE)

            echem_features = np.array([
                anode_idx, cathode_idx,
                cond.get('current_mA', 0.0),
                cond.get('current_density_mA_cm2', 0.0),
                cond.get('potential_V', 0.0),
                cell_type_idx,
            ], dtype=np.float32)

            full_features = np.concatenate([
                reaction_fp_base,
                solvent_fp,
                electrolyte_fp,
                echem_features,
            ])

            # Append xTB features if the model requires them
            if needs_xtb and xtb_lookup is not None:
                solvent_list = [solvent_smiles] if solvent_smiles else []
                xtb_feat = xtb_lookup.get_reaction_features(
                    reactants, products, solvent_list, electrolyte_smiles
                )
                full_features = np.concatenate([full_features, np.array(xtb_feat, dtype=np.float32)])
            elif needs_xtb:
                # xTB lookup not available, pad with zeros
                xtb_dim = yield_input_dim - base_dim
                full_features = np.concatenate([full_features, np.zeros(xtb_dim, dtype=np.float32)])

            features_tensor = torch.tensor(full_features, dtype=torch.float32).unsqueeze(0).to(device)

            # Predict with optional uncertainty estimation
            if compute_uncertainty and hasattr(yield_model, 'predict_with_uncertainty'):
                mean_yield, std_yield = yield_model.predict_with_uncertainty(
                    features_tensor, n_samples=50
                )
                result_entry = {
                    'conditions': {
                        'solvent': solvent_smiles,
                        'electrolyte': electrolyte_smiles,
                        'anode': ELECTRODE_NAMES.get(anode_idx, f'idx={anode_idx}'),
                        'cathode': ELECTRODE_NAMES.get(cathode_idx, f'idx={cathode_idx}'),
                        'cell_type': CELL_TYPE_NAMES.get(cell_type_idx, f'idx={cell_type_idx}'),
                        'current_mA': cond.get('current_mA', None),
                        'current_density_mA_cm2': cond.get('current_density_mA_cm2', None),
                        'potential_V': cond.get('potential_V', None),
                    },
                    'predicted_yield': round(mean_yield, 2),
                    'yield_std': round(std_yield, 2),
                    'confidence': (
                        'high' if std_yield < 5 else
                        'medium' if std_yield < 15 else
                        'low'
                    ),
                }
            else:
                with torch.no_grad():
                    predicted_yield = yield_model(features_tensor).item() * 100
                result_entry = {
                    'conditions': {
                        'solvent': solvent_smiles,
                        'electrolyte': electrolyte_smiles,
                        'anode': ELECTRODE_NAMES.get(anode_idx, f'idx={anode_idx}'),
                        'cathode': ELECTRODE_NAMES.get(cathode_idx, f'idx={cathode_idx}'),
                        'cell_type': CELL_TYPE_NAMES.get(cell_type_idx, f'idx={cell_type_idx}'),
                        'current_mA': cond.get('current_mA', None),
                        'current_density_mA_cm2': cond.get('current_density_mA_cm2', None),
                        'potential_V': cond.get('potential_V', None),
                    },
                    'predicted_yield': round(predicted_yield, 2),
                }
            results.append(result_entry)

        return {
            "reaction_smiles": reaction_smiles,
            "yield_predictions": results,
        }

    # ── Tool 6: search_similar_reactions ───────────────────────

    def _handle_search_similar(self, inputs: Dict) -> Dict:
        reaction_smiles = inputs['reaction_smiles']
        top_k = inputs.get('top_k', 5)
        threshold = inputs.get('threshold', 0.3)
        min_yield = inputs.get('min_yield', None)
        rerank_by_yield = inputs.get('rerank_by_yield', True)

        if self.retriever is None:
            return {
                "error": "Similar reaction search is not available. Run build_index.py first.",
                "reaction_smiles": reaction_smiles,
            }

        # Use base 6144D FP for search (index was built with base FPs)
        reactants, products = parse_reaction_smiles(reaction_smiles)
        fp = compute_reaction_fingerprint(reactants, products, self.mm.mol_extractor)

        results = self.retriever.search(
            fp, top_k=top_k, threshold=threshold,
            min_yield=min_yield, rerank_by_yield=rerank_by_yield,
        )

        # Get condition statistics from results
        condition_stats = self.retriever.get_condition_statistics(results)

        # Format results
        formatted = []
        for r in results:
            entry = {
                'reaction_smiles': r['reaction_smiles'],
                'similarity': r['similarity'],
                'yield': r.get('yield'),
                'conditions': {
                    'anode': r.get('anode', 'Unknown'),
                    'cathode': r.get('cathode', 'Unknown'),
                    'cell_type': r.get('cell_type', 'Unknown'),
                    'solvents': r.get('solvents', []),
                    'electrolyte': r.get('electrolyte', ''),
                    'reagent': r.get('reagent', ''),
                    'catalyst': r.get('catalyst', ''),
                    'current_mA': r.get('current_mA'),
                    'current_density_mA_cm2': r.get('current_density_mA_cm2'),
                    'potential_V': r.get('potential_V'),
                },
            }
            if 'combined_score' in r:
                entry['combined_score'] = r['combined_score']
            formatted.append(entry)

        return {
            "reaction_smiles": reaction_smiles,
            "num_results": len(formatted),
            "database_size": self.retriever.num_reactions,
            "condition_statistics": condition_stats,
            "similar_reactions": formatted,
        }

    # ── Tool 6b: search_mechanism ──────────────────────────────

    def _handle_search_mechanism(self, inputs: Dict) -> Dict:
        """Retrieve mechanism context for a reaction.

        Two modes:
        - 'reaction': lookup this reaction's own paper mechanism + find
          mechanistically similar papers (Jaccard on family + TF-IDF text).
        - 'families': directly query by user-supplied mechanism family tags
          (+ optional free text). Useful when reaction is novel or not in KB.
        """
        if self.mechanism_retriever is None:
            return {
                "error": "Mechanism KB not loaded. "
                         "Run yield_prediction/scripts/build_mechanism_kb.py first."
            }

        mode = inputs.get('mode', 'reaction')
        top_k = int(inputs.get('top_k', 5))
        family_weight = float(inputs.get('family_weight', 0.4))

        if mode == 'families':
            families = inputs.get('mechanism_family', []) or []
            free_text = inputs.get('free_text', '') or ''
            matches = self.mechanism_retriever.search_by_mechanism_family(
                families=families, free_text=free_text,
                top_k=top_k, family_weight=family_weight,
            )
            return {
                "mode": "families",
                "query_families": families,
                "free_text": free_text,
                "num_matches": len(matches),
                "matches": matches,
            }

        # default: search by reaction
        reaction_smiles = inputs.get('reaction_smiles')
        if not reaction_smiles:
            return {"error": "reaction_smiles is required for mode='reaction'"}
        include_query = bool(inputs.get('include_query_paper', False))
        out = self.mechanism_retriever.search_by_reaction(
            reaction_smiles, top_k=top_k, family_weight=family_weight,
            include_query_paper=include_query,
        )
        if not out:
            return {
                "mode": "reaction",
                "reaction_smiles": reaction_smiles,
                "seed_paper": None,
                "message": (
                    "No mechanism record found for this reaction's source paper. "
                    "Try mode='families' with manually-identified mechanism tags "
                    "(e.g., 'radical_anodic', 'mediator_cathodic')."
                ),
                "matches": [],
            }
        return {
            "mode": "reaction",
            "reaction_smiles": reaction_smiles,
            "seed_paper": out["seed_paper"],
            "num_matches": len(out["matches"]),
            "matches": out["matches"],
        }

    # ── Tool 7: analyze_reaction_chemistry ───────────────────

    def _handle_analyze_reaction_chemistry(self, inputs: Dict) -> Dict:
        """Analyze substrate functional groups, olefin type, and reaction class."""
        from rdkit import Chem
        from rdkit.Chem import Descriptors, Fragments, AllChem, rdMolDescriptors

        reaction_smiles = inputs['reaction_smiles']
        reactants, products = parse_reaction_smiles(reaction_smiles)

        # Analyze each reactant
        reactant_analysis = []
        has_olefin = False
        olefin_details = []
        all_functional_groups = []
        all_warnings = []

        for smi in reactants:
            mol = Chem.MolFromSmiles(smi)
            if mol is None:
                reactant_analysis.append({'smiles': smi, 'valid': False})
                continue

            info = {
                'smiles': smi,
                'valid': True,
                'mw': round(Descriptors.MolWt(mol), 1),
                'formula': rdMolDescriptors.CalcMolFormula(mol),
                'functional_groups': [],
                'sensitivity_warnings': [],
            }

            # Detect olefin (C=C double bond) with detailed analysis
            olefin_count = 0
            for bond in mol.GetBonds():
                if (bond.GetBondTypeAsDouble() == 2.0 and
                        bond.GetBeginAtom().GetAtomicNum() == 6 and
                        bond.GetEndAtom().GetAtomicNum() == 6):
                    has_olefin = True
                    olefin_count += 1
                    a1, a2 = bond.GetBeginAtom(), bond.GetEndAtom()

                    # Detailed substitution analysis
                    h1 = a1.GetTotalNumHs()
                    h2 = a2.GetTotalNumHs()
                    total_h = h1 + h2

                    # Substitution pattern
                    if total_h >= 2:
                        if h1 == 2 or h2 == 2:
                            olefin_type = '末端烯烃 (terminal)'
                            substitution = 'monosubstituted' if (h1 == 2 or h2 == 2) else 'disubstituted (1,1-)'
                        else:
                            olefin_type = '1,2-二取代烯烃 (1,2-disubstituted)'
                            substitution = '1,2-disubstituted'
                    elif total_h == 1:
                        olefin_type = '三取代烯烃 (trisubstituted)'
                        substitution = 'trisubstituted'
                    else:
                        olefin_type = '四取代烯烃 (tetrasubstituted)'
                        substitution = 'tetrasubstituted'

                    # Check conjugation with aromatic ring
                    is_conjugated_aromatic = False
                    is_conjugated_carbonyl = False
                    is_conjugated_other = False

                    for neighbor in list(a1.GetNeighbors()) + list(a2.GetNeighbors()):
                        if neighbor.GetIsAromatic():
                            is_conjugated_aromatic = True
                        # Check for C=O conjugation
                        for nb in neighbor.GetBonds():
                            if nb.GetBondTypeAsDouble() == 2.0 and nb.GetIdx() != bond.GetIdx():
                                other_atom = nb.GetOtherAtom(neighbor)
                                if other_atom.GetAtomicNum() == 8:
                                    is_conjugated_carbonyl = True
                                elif other_atom.GetAtomicNum() == 6:
                                    is_conjugated_other = True

                    # Electronic character
                    electron_character = '中性 (neutral)'
                    if is_conjugated_carbonyl:
                        electron_character = '缺电子 (electron-deficient, α,β-unsaturated)'
                    elif is_conjugated_aromatic:
                        electron_character = '共轭稳定 (conjugated with aromatic ring)'

                    # Check for electron-donating groups
                    for neighbor in list(a1.GetNeighbors()) + list(a2.GetNeighbors()):
                        if neighbor.GetAtomicNum() == 8 and neighbor.GetTotalNumHs() == 0:
                            # Ether or ester oxygen
                            electron_character = '富电子 (electron-rich, vinyl ether type)'
                        elif neighbor.GetAtomicNum() == 7:
                            electron_character = '富电子 (electron-rich, enamine type)'

                    # Check if in ring
                    is_in_ring = bond.IsInRing()
                    ring_info = '环内烯烃' if is_in_ring else '非环烯烃'

                    olefin_details.append({
                        'type': olefin_type,
                        'substitution': substitution,
                        'electronic_character': electron_character,
                        'conjugated_with_aromatic': is_conjugated_aromatic,
                        'conjugated_with_carbonyl': is_conjugated_carbonyl,
                        'in_ring': is_in_ring,
                        'ring_info': ring_info,
                    })

            if olefin_count > 0:
                info['olefin_count'] = olefin_count

            # Extended functional group detection
            fg_checks = [
                (Fragments.fr_Al_OH, '醇羟基 (alcohol -OH)'),
                (Fragments.fr_Ar_OH, '酚羟基 (phenol ArOH)'),
                (Fragments.fr_NH2, '伯胺 (primary amine -NH₂)'),
                (Fragments.fr_NH1, '仲胺 (secondary amine -NH-)'),
                (Fragments.fr_aldehyde, '醛基 (aldehyde -CHO)'),
                (Fragments.fr_ketone, '酮基 (ketone C=O)'),
                (Fragments.fr_ester, '酯基 (ester -COOR)'),
                (Fragments.fr_amide, '酰胺 (amide -CONR₂)'),
                (Fragments.fr_nitro, '硝基 (nitro -NO₂)'),
                (Fragments.fr_nitrile, '氰基 (nitrile -CN)'),
                (Fragments.fr_sulfide, '硫醚 (sulfide -S-)'),
                (Fragments.fr_SH, '巯基 (thiol -SH)'),
                (Fragments.fr_sulfone, '砜 (sulfone -SO₂-)'),
                (Fragments.fr_sulfonamd, '磺酰胺 (sulfonamide)'),
                (Fragments.fr_COO, '羧酸 (carboxylic acid -COOH)'),
                (Fragments.fr_COO2, '羧酸酯 (carboxylate ester)'),
                (Fragments.fr_ether, '醚键 (ether -O-)'),
                (Fragments.fr_epoxide, '环氧 (epoxide)'),
                (Fragments.fr_azide, '叠氮 (azide -N₃)'),
                (Fragments.fr_azo, '偶氮 (azo -N=N-)'),
                (Fragments.fr_furan, '呋喃 (furan)'),
                (Fragments.fr_thiophene, '噻吩 (thiophene)'),
                (Fragments.fr_pyridine, '吡啶 (pyridine)'),
                (Fragments.fr_imidazole, '咪唑 (imidazole)'),
            ]
            for func, name in fg_checks:
                if func(mol) > 0:
                    info['functional_groups'].append(name)

            # Halide detection with count
            halide_counts = {'F': 0, 'Cl': 0, 'Br': 0, 'I': 0}
            for atom in mol.GetAtoms():
                if atom.GetAtomicNum() == 9:
                    halide_counts['F'] += 1
                elif atom.GetAtomicNum() == 17:
                    halide_counts['Cl'] += 1
                elif atom.GetAtomicNum() == 35:
                    halide_counts['Br'] += 1
                elif atom.GetAtomicNum() == 53:
                    halide_counts['I'] += 1

            halides_present = [f"{k}×{v}" for k, v in halide_counts.items() if v > 0]
            if halides_present:
                info['functional_groups'].append(f"卤素 (halide: {', '.join(halides_present)})")

            # Check for aromatic rings
            aromatic_rings = rdMolDescriptors.CalcNumAromaticRings(mol)
            if aromatic_rings > 0:
                info['functional_groups'].append(f"芳环 ({aromatic_rings} aromatic ring{'s' if aromatic_rings > 1 else ''})")

            # Detailed sensitivity warnings with recommendations
            if Fragments.fr_Al_OH(mol) > 0 or Fragments.fr_Ar_OH(mol) > 0:
                info['sensitivity_warnings'].append({
                    'group': '羟基 (-OH)',
                    'risk': '可能在阳极被氧化',
                    'recommendation': '使用较低电流密度 (<10 mA/cm²)，或考虑保护基团',
                })
            if Fragments.fr_NH2(mol) > 0 or Fragments.fr_NH1(mol) > 0:
                info['sensitivity_warnings'].append({
                    'group': '胺基 (-NH₂/-NH-)',
                    'risk': '容易在阳极氧化形成亚胺或N-自由基',
                    'recommendation': '可能需要分隔池，或利用胺的氧化作为反应的一部分',
                })
            if Fragments.fr_aldehyde(mol) > 0:
                info['sensitivity_warnings'].append({
                    'group': '醛基 (-CHO)',
                    'risk': '容易过度氧化为羧酸',
                    'recommendation': '控制电荷量，使用低电流密度',
                })
            if Fragments.fr_SH(mol) > 0:
                info['sensitivity_warnings'].append({
                    'group': '巯基 (-SH)',
                    'risk': '极易氧化形成二硫键',
                    'recommendation': '需要惰性气氛保护，低电位操作',
                })
            if Fragments.fr_sulfide(mol) > 0:
                info['sensitivity_warnings'].append({
                    'group': '硫醚 (-S-)',
                    'risk': '可被氧化为亚砜或砜',
                    'recommendation': '控制阳极电位',
                })
            if Fragments.fr_epoxide(mol) > 0:
                info['sensitivity_warnings'].append({
                    'group': '环氧 (epoxide)',
                    'risk': '对酸/碱敏感，可能开环',
                    'recommendation': '避免酸性电解质，中性条件操作',
                })

            all_functional_groups.extend(info['functional_groups'])
            all_warnings.extend(info['sensitivity_warnings'])
            reactant_analysis.append(info)

        # Infer reaction type from atom changes
        reaction_type = self._infer_reaction_type(reactants, products)

        # Get reaction type specific recommendations
        reaction_recommendations = self._get_reaction_type_recommendations(reaction_type)

        # Summarize olefin characteristics
        olefin_summary = None
        if olefin_details:
            olefin_summary = {
                'count': len(olefin_details),
                'types': list(set([o['type'] for o in olefin_details])),
                'electronic_characters': list(set([o['electronic_character'] for o in olefin_details])),
                'any_conjugated': any(o['conjugated_with_aromatic'] or o['conjugated_with_carbonyl'] for o in olefin_details),
                'any_in_ring': any(o['in_ring'] for o in olefin_details),
            }

        return {
            'reaction_smiles': reaction_smiles,
            'summary': {
                'has_olefin': has_olefin,
                'olefin_summary': olefin_summary,
                'reaction_type': reaction_type,
                'total_functional_groups': len(set(all_functional_groups)),
                'has_sensitive_groups': len(all_warnings) > 0,
            },
            'olefin_analysis': olefin_details if olefin_details else '未检测到 C=C 双键',
            'reaction_type_detail': {
                'type': reaction_type,
                'recommendations': reaction_recommendations,
            },
            'reactant_analysis': reactant_analysis,
            'compatibility_notes': self._generate_compatibility_notes(all_functional_groups, all_warnings, reaction_type),
            'num_reactants': len(reactants),
            'num_products': len(products),
        }

    def _get_reaction_type_recommendations(self, reaction_type: str) -> Dict:
        """Get specific recommendations for each reaction type."""
        recommendations = {
            'difluorination': {
                'typical_conditions': 'Et₃N·3HF 作为氟源，Pt 或 BDD 阳极',
                'cell_type': 'undivided (PTFE 容器！)',
                'safety': '⚠️ 含 HF 体系，必须全程做好防护',
                'current_density': '5-15 mA/cm²',
            },
            'bromoamination': {
                'typical_conditions': 'nBu₄NBr 作为溴源，碳或石墨阳极',
                'cell_type': 'undivided',
                'current_density': '5-10 mA/cm²',
            },
            'bromination': {
                'typical_conditions': '溴化物电解质 (Et₄NBr, NaBr)，碳阳极',
                'cell_type': 'undivided',
                'current_density': '5-20 mA/cm²',
            },
            'aminohydroxylation': {
                'typical_conditions': '需要胺源和水/醇，Pt 电极',
                'cell_type': 'undivided 或 divided',
                'current_density': '5-10 mA/cm²',
            },
            'carboamination': {
                'typical_conditions': 'RVC 或石墨阳极，Ni 阴极',
                'cell_type': 'undivided',
                'current_density': '3-10 mA/cm²',
            },
            'dihydroxylation': {
                'typical_conditions': '水作为氧源，Pt 阳极',
                'cell_type': 'undivided',
                'current_density': '5-10 mA/cm²',
            },
        }

        # Find matching recommendation
        for key, rec in recommendations.items():
            if key in reaction_type.lower():
                return rec

        # Default recommendation
        return {
            'typical_conditions': '根据具体反应类型选择',
            'cell_type': 'undivided (一般首选)',
            'current_density': '5-15 mA/cm² (建议从低电流密度开始)',
        }

    def _generate_compatibility_notes(self, functional_groups: List[str], warnings: List, reaction_type: str) -> List[str]:
        """Generate compatibility notes based on functional groups and reaction type."""
        notes = []

        # General notes based on functional groups
        fg_set = set(functional_groups)

        if any('胺' in fg or 'amine' in fg.lower() for fg in fg_set):
            notes.append('含胺基底物：注意胺可能在阳极优先氧化，可考虑利用这一特性或使用分隔池保护')

        if any('醇' in fg or 'alcohol' in fg.lower() for fg in fg_set):
            notes.append('含醇羟基：可能参与反应或被氧化，确认是否需要保护')

        if any('卤素' in fg or 'halide' in fg.lower() for fg in fg_set):
            notes.append('底物含卤素：注意可能的脱卤副反应')

        if any('硫' in fg or 'sulfide' in fg.lower() or 'thio' in fg.lower() for fg in fg_set):
            notes.append('含硫基团：硫易被氧化，可能需要控制电位')

        # Reaction type specific notes
        if 'fluor' in reaction_type.lower():
            notes.append('⚠️ 氟化反应：必须使用 PTFE/HDPE 容器，全程做好 HF 防护')

        if 'bromo' in reaction_type.lower() or 'iodo' in reaction_type.lower():
            notes.append('卤化反应：推荐使用碳/石墨阳极，避免 Pt（可能催化副反应）')

        if not notes:
            notes.append('未发现明显的兼容性问题，可按标准条件进行实验')

        return notes

    @staticmethod
    def _infer_reaction_type(reactants: List[str], products: List[str]) -> str:
        """Infer reaction type from atom count changes between reactants and products."""
        from rdkit import Chem

        def count_atoms(smiles_list):
            counts = Counter()
            for smi in smiles_list:
                mol = Chem.MolFromSmiles(smi)
                if mol:
                    for atom in mol.GetAtoms():
                        counts[atom.GetSymbol()] += 1
            return counts

        r_atoms = count_atoms(reactants)
        p_atoms = count_atoms(products)

        # Compute atom changes (product - reactant)
        added = {}
        for elem, count in p_atoms.items():
            diff = count - r_atoms.get(elem, 0)
            if diff > 0:
                added[elem] = diff

        # Classify based on added atoms
        if 'F' in added and added.get('F', 0) >= 2:
            return 'difluorination'
        elif 'F' in added:
            return 'fluorination (monofluorination or fluoroalkylation)'
        elif 'Br' in added and 'N' in added:
            return 'bromoamination'
        elif 'Br' in added and 'O' in added:
            return 'bromohydroxylation or bromolactonization'
        elif 'Br' in added:
            return 'bromination or bromo-functionalization'
        elif 'I' in added:
            return 'iodofunctionalization'
        elif 'Cl' in added and 'N' in added:
            return 'chloroamination'
        elif 'Cl' in added:
            return 'chlorofunctionalization'
        elif 'N' in added and 'O' in added:
            return 'aminohydroxylation or oxyamination'
        elif 'N' in added and added.get('N', 0) >= 2:
            return 'diamination'
        elif 'N' in added:
            return 'carboamination or amination'
        elif 'O' in added and added.get('O', 0) >= 2:
            return 'dioxygenation or dihydroxylation'
        elif 'O' in added:
            return 'oxygenation or hydroxylation'
        elif 'S' in added:
            return 'thio-functionalization'
        elif not added:
            return 'cyclization or rearrangement (no net atom addition)'
        else:
            elements = ', '.join(f'{elem}(+{n})' for elem, n in added.items())
            return f'difunctionalization (added: {elements})'

    # ── Tool 8: estimate_experimental_parameters ─────────────

    def _handle_estimate_experimental_parameters(self, inputs: Dict) -> Dict:
        """Calculate charge, time, and electrode area for an experiment."""
        FARADAY = 96485.0  # C/mol

        substrate_mmol = inputs.get('substrate_mmol', 0.2)
        num_electrons = inputs.get('num_electrons', 2)
        current_mA = inputs.get('current_mA', 10.0)
        faradaic_efficiency_pct = inputs.get('faradaic_efficiency_pct', 80.0)
        target_current_density = inputs.get('target_current_density_mA_cm2', 10.0)

        # Calculate required charge
        substrate_mol = substrate_mmol / 1000.0
        charge_theoretical_C = substrate_mol * num_electrons * FARADAY
        charge_to_pass_C = charge_theoretical_C / (faradaic_efficiency_pct / 100.0)

        # Calculate time
        current_A = current_mA / 1000.0
        time_seconds = charge_to_pass_C / current_A if current_A > 0 else float('inf')
        time_hours = time_seconds / 3600.0

        # Calculate electrode area
        electrode_area_cm2 = current_mA / target_current_density if target_current_density > 0 else 0

        # Equivalents of electrons (F = Faraday equivalents)
        faraday_equivalents = charge_to_pass_C / FARADAY / substrate_mol if substrate_mol > 0 else 0

        return {
            'input_parameters': {
                'substrate_mmol': substrate_mmol,
                'num_electrons_transferred': num_electrons,
                'current_mA': current_mA,
                'faradaic_efficiency_assumed_pct': faradaic_efficiency_pct,
                'target_current_density_mA_cm2': target_current_density,
            },
            'calculated_results': {
                'charge_theoretical_C': round(charge_theoretical_C, 2),
                'charge_to_pass_C': round(charge_to_pass_C, 2),
                'faraday_equivalents_F': round(faraday_equivalents, 2),
                'estimated_time_hours': round(time_hours, 2),
                'estimated_time_minutes': round(time_hours * 60, 1),
                'recommended_electrode_area_cm2': round(electrode_area_cm2, 2),
            },
            'summary': (
                f"For {substrate_mmol} mmol substrate with {num_electrons}e⁻ transfer: "
                f"pass {charge_to_pass_C:.1f} C ({faraday_equivalents:.1f} F equiv) at {current_mA} mA. "
                f"Estimated time: {time_hours:.1f} h ({time_hours*60:.0f} min). "
                f"Electrode area: ~{electrode_area_cm2:.1f} cm² for {target_current_density} mA/cm²."
            ),
        }

    # ── Tool 9: generate_experimental_protocol ───────────────

    def _handle_generate_protocol(self, inputs: Dict) -> Dict:
        """Generate a complete experimental protocol from recommended conditions."""
        # Load chemistry knowledge base
        kb_path = Path(AGENT_ROOT) / 'data' / 'chemistry_kb.json'
        kb = {}
        if kb_path.exists():
            with open(kb_path, encoding='utf-8') as f:
                kb = json.load(f)

        anode = inputs.get('anode', 'Carbon')
        cathode = inputs.get('cathode', 'Platinum')
        cell_type = inputs.get('cell_type', 'undivided')
        solvent = inputs.get('solvent', '')
        solvent_smiles = inputs.get('solvent_smiles', '')
        electrolyte = inputs.get('electrolyte', '')
        electrolyte_smiles = inputs.get('electrolyte_smiles', '')
        reagent = inputs.get('reagent', '')
        catalyst = inputs.get('catalyst', '')
        substrate_mmol = inputs.get('substrate_mmol', 0.2)
        current_mA = inputs.get('current_mA', 10.0)
        time_hours = inputs.get('time_hours', None)
        charge_C = inputs.get('charge_C', None)
        predicted_yield = inputs.get('predicted_yield', None)

        # Electrode preparation
        anode_prep = kb.get('electrode_prep', {}).get(anode, f'用溶剂淋洗 {anode} 电极表面，晾干。')
        cathode_prep = kb.get('electrode_prep', {}).get(cathode, f'用溶剂淋洗 {cathode} 电极表面，晾干。')

        # Cell assembly
        cell_assembly = kb.get('cell_assembly', {}).get(
            cell_type.lower().split()[0] if cell_type else 'undivided',
            '参照标准电化学池组装步骤。'
        )

        # Solvent safety
        solvent_safety = ''
        if solvent_smiles:
            safety_info = kb.get('solvent_safety', {}).get(solvent_smiles)
            if safety_info:
                solvent_safety = f"⚠️ {safety_info.get('name', solvent)}: {safety_info.get('hazards', '')}"

        # General safety
        general_safety = kb.get('general_safety', [])

        # Workup
        workup = kb.get('workup_general', '旋蒸浓缩，柱层析纯化，NMR 和质谱表征。')

        # Build protocol
        protocol_sections = {
            'title': f'电催化烯烃双官能化反应实验方案',
            'scale': f'{substrate_mmol} mmol',
            'conditions': {
                'anode': anode,
                'cathode': cathode,
                'cell_type': cell_type,
                'solvent': solvent or solvent_smiles,
                'electrolyte': electrolyte or electrolyte_smiles,
                'reagent': reagent if reagent else 'N/A',
                'catalyst': catalyst if catalyst else 'N/A',
                'current_mA': current_mA,
                'time_hours': time_hours,
                'charge_C': charge_C,
            },
            'steps': [
                f'1. 电极准备：\n   - 阳极 ({anode}): {anode_prep}\n   - 阴极 ({cathode}): {cathode_prep}',
                f'2. 电解池组装：{cell_assembly}',
                f'3. 配制电解液：在反应容器中加入溶剂，加入电解质搅拌至完全溶解。',
                f'4. 加入底物 ({substrate_mmol} mmol) 和试剂/催化剂（如有），搅拌均匀。',
                f'5. 插入电极（间距 ~0.5-1.0 cm），连接电源。',
                f'6. 设定恒电流 {current_mA} mA，开始电解。'
                + (f' 反应时间约 {time_hours:.1f} 小时 ({charge_C:.0f} C)。' if time_hours and charge_C else ''),
                f'7. 反应结束后断开电源，取出电极。',
                f'8. 后处理：{workup}',
            ],
            'safety_notes': [],
            'predicted_yield': predicted_yield,
        }

        if solvent_safety:
            protocol_sections['safety_notes'].append(solvent_safety)
        protocol_sections['safety_notes'].extend(general_safety)

        return protocol_sections

    # ── Tool 10: draw_reaction ─────────────────────────────────

    def _handle_draw_reaction(self, inputs: Dict) -> Dict:
        """Draw reaction structure diagrams as images using RDKit."""
        smiles_list = inputs.get("reaction_smiles_list") or [inputs.get("reaction_smiles")]
        legends = inputs.get("legends", [])

        images = []
        for i, rs in enumerate(smiles_list):
            if not rs:
                continue
            rxn = AllChem.ReactionFromSmarts(rs, useSmiles=True)
            img = Draw.ReactionToImage(rxn, subImgSize=(300, 200))
            buf = io.BytesIO()
            img.save(buf, format='PNG')
            b64 = base64.b64encode(buf.getvalue()).decode()
            images.append({
                "reaction_smiles": rs,
                "image_base64": f"data:image/png;base64,{b64}",
                "legend": legends[i] if i < len(legends) else f"Reaction {i+1}",
            })

        return {
            "images": images,
            "num_images": len(images),
            "message": f"Successfully drew {len(images)} reaction(s)",
        }

    # ── Tool 11: optimize_conditions_bo ────────────────────────

    def _get_bo_optimizer(self, reaction_smiles: str, prior_mode: str = "rag_mean"):
        """Get or create a BayesianConditionOptimizer for a reaction."""
        from bayesian_opt import (
            ConditionSpace, WarmStarter, BayesianConditionOptimizer,
        )

        if reaction_smiles in self._bo_states:
            # Restore from cached state
            space = ConditionSpace(str(VOCAB_PATH))
            warm_starter = WarmStarter(self.retriever, self.mm) if self.retriever else None
            yield_fn = self._make_yield_predictor_fn(reaction_smiles)
            optimizer = BayesianConditionOptimizer(
                condition_space=space,
                warm_starter=warm_starter,
                yield_predictor_fn=yield_fn,
                prior_mode=prior_mode,
                retriever=self.retriever,
                model_manager=self.mm,
            )
            optimizer.load_state(self._bo_states[reaction_smiles])
            return optimizer

        # Create new optimizer
        space = ConditionSpace(str(VOCAB_PATH))
        warm_starter = WarmStarter(self.retriever, self.mm) if self.retriever else None
        yield_fn = self._make_yield_predictor_fn(reaction_smiles)
        optimizer = BayesianConditionOptimizer(
            condition_space=space,
            warm_starter=warm_starter,
            yield_predictor_fn=yield_fn,
            prior_mode=prior_mode,
            retriever=self.retriever,
            model_manager=self.mm,
        )
        return optimizer

    def _make_yield_predictor_fn(self, reaction_smiles: str):
        """Create a yield prediction callable for a specific reaction."""
        reactants, products = parse_reaction_smiles(reaction_smiles)
        mol_extractor = self.mm.mol_extractor

        reactant_fp = mol_extractor.encode_molecules(reactants)
        product_fp = mol_extractor.encode_molecules(products)
        diff_fp = np.abs(product_fp - reactant_fp)
        reaction_fp_base = np.concatenate([reactant_fp, product_fp, diff_fp])

        yield_model = self.mm.yield_model
        yield_input_dim = self.mm.yield_input_dim
        device = self.mm.device
        base_dim = 5 * FINGERPRINT_SIZE + 6  # 10246

        def predict_yield(conditions: dict) -> float:
            solvent_smiles = conditions.get('solvent_smiles', '')
            electrolyte_smiles = conditions.get('electrolyte_smiles', '')
            anode_idx = conditions.get('anode_index', 0)
            cathode_idx = conditions.get('cathode_index', 0)
            cell_type_idx = conditions.get('cell_type_index', 0)

            solvent_fp = (mol_extractor.get_morgan_fingerprint(solvent_smiles)
                          if solvent_smiles else np.zeros(FINGERPRINT_SIZE))
            electrolyte_fp = (mol_extractor.get_morgan_fingerprint(electrolyte_smiles)
                              if electrolyte_smiles else np.zeros(FINGERPRINT_SIZE))

            echem_features = np.array([
                anode_idx, cathode_idx, 0.0, 0.0, 0.0, cell_type_idx,
            ], dtype=np.float32)

            full_features = np.concatenate([
                reaction_fp_base, solvent_fp, electrolyte_fp, echem_features,
            ])

            # Pad if model expects more features (xTB)
            if yield_input_dim > base_dim:
                pad = np.zeros(yield_input_dim - base_dim, dtype=np.float32)
                full_features = np.concatenate([full_features, pad])

            import torch as _torch
            features_tensor = _torch.tensor(
                full_features, dtype=_torch.float32
            ).unsqueeze(0).to(device)

            with _torch.no_grad():
                predicted = yield_model(features_tensor).item() * 100
            return predicted

        return predict_yield

    def _handle_optimize_conditions_bo(self, inputs: Dict) -> Dict:
        """
        Bayesian optimization for condition selection.

        Supports four modes:
        - "suggest": suggest next conditions to try (iterative mode)
        - "observe": record an experimental result
        - "search": offline search for optimal conditions
        - "rerank": rerank M1 candidate conditions
        """
        reaction_smiles = inputs['reaction_smiles']
        mode = inputs.get('mode', 'suggest')
        acq_func = inputs.get('acq_func', 'ei')
        n_suggestions = inputs.get('n_suggestions', 3)

        optimizer = self._get_bo_optimizer(reaction_smiles)

        if mode == 'suggest':
            # Initialize if first call
            if not optimizer._initialized:
                optimizer.initialize(reaction_smiles)

            results = optimizer.suggest_with_details(
                n=n_suggestions, acq_func=acq_func
            )

            # Format suggestions
            formatted = []
            for r in results:
                formatted.append({
                    'conditions': optimizer.format_conditions(r['conditions']),
                    'predicted_yield': r['predicted_mean'],
                    'uncertainty': r['predicted_std'],
                    'acquisition_value': r['acq_value'],
                })

            best = optimizer.get_best()

            # Save state
            self._bo_states[reaction_smiles] = optimizer.get_state()

            return {
                'reaction_smiles': reaction_smiles,
                'mode': 'suggest',
                'acq_func': acq_func,
                'suggestions': formatted,
                'n_observations': optimizer.surrogate.n_observations,
                'best_so_far': {
                    'conditions': optimizer.format_conditions(best['conditions']),
                    'yield': best['yield'],
                } if best else None,
            }

        elif mode == 'observe':
            observed = inputs.get('observed_conditions', {})
            observed_yield = inputs.get('observed_yield', 0.0)

            if not optimizer._initialized:
                optimizer.initialize(reaction_smiles)

            optimizer.observe(observed, observed_yield)

            # Save state
            self._bo_states[reaction_smiles] = optimizer.get_state()

            best = optimizer.get_best()
            return {
                'reaction_smiles': reaction_smiles,
                'mode': 'observe',
                'recorded': {
                    'conditions': optimizer.format_conditions(observed),
                    'yield': observed_yield,
                },
                'n_observations': optimizer.surrogate.n_observations,
                'best_so_far': {
                    'conditions': optimizer.format_conditions(best['conditions']),
                    'yield': best['yield'],
                } if best else None,
            }

        elif mode == 'search':
            n_iter = inputs.get('n_iter', 50)
            results = optimizer.search_optimal(
                reaction_smiles, n_iter=n_iter, acq_func=acq_func
            )

            formatted = []
            for r in results[:5]:
                formatted.append({
                    'conditions': optimizer.format_conditions(r['conditions']),
                    'yield': r['yield'],
                    'iteration': r['iteration'],
                    'phase': r['phase'],
                })

            # Save state
            self._bo_states[reaction_smiles] = optimizer.get_state()

            return {
                'reaction_smiles': reaction_smiles,
                'mode': 'search',
                'n_iterations': n_iter,
                'top_results': formatted,
                'best_yield': formatted[0]['yield'] if formatted else 0,
            }

        elif mode == 'rerank':
            candidates = inputs.get('candidates', [])
            m1_probs = inputs.get('m1_probs', None)
            alpha = inputs.get('alpha', 0.5)

            if not candidates:
                return {'error': 'No candidates provided for reranking'}

            results = optimizer.rerank_candidates(
                candidates, reaction_smiles,
                alpha=alpha, m1_probs=m1_probs,
            )

            formatted = []
            for r in results[:n_suggestions]:
                formatted.append({
                    'conditions': optimizer.format_conditions(r['conditions']),
                    'combined_score': r['combined_score'],
                    'gp_mean': r['gp_mean'],
                    'gp_std': r['gp_std'],
                    'ucb': r['ucb'],
                    'm1_prob': r['m1_prob'],
                })

            self._bo_states[reaction_smiles] = optimizer.get_state()

            return {
                'reaction_smiles': reaction_smiles,
                'mode': 'rerank',
                'reranked_candidates': formatted,
            }

        else:
            return {'error': f'Unknown mode: {mode}. Use suggest/observe/search/rerank.'}
