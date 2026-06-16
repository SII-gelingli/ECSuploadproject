"""
数据处理模块：加载和预处理反应数据
"""
import json
import os
from typing import Dict, List, Tuple, Optional
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tqdm import tqdm


class ReactionDataProcessor:
    """处理电化学反应数据"""

    # 电极材料编码
    ELECTRODE_MATERIALS = {
        'carbon': 0, 'graphite': 1, 'platinum': 2, 'platinum plate': 2,
        'carbon rod': 0, 'glassy carbon': 3, 'rvc': 4, 'nickel': 5,
        'stainless steel': 6, 'copper': 7, 'zinc': 8, 'lead': 9,
        'gold': 10, 'silver': 11, 'iron': 12, 'magnesium': 13,
        None: 14, '': 14, 'unknown': 14
    }

    # 电解池类型编码
    CELL_TYPES = {
        'undivided': 0, 'divided': 1, 'h-cell': 2, 'flow': 3,
        None: 4, '': 4, 'unknown': 4
    }

    def __init__(self, yield_data_dir: str, smiles_data_path: str):
        self.yield_data_dir = Path(yield_data_dir)
        self.smiles_data_path = Path(smiles_data_path)
        self.reactions = []

    def load_yield_data(self) -> List[Dict]:
        """加载按产率分类的反应数据"""
        reactions = []

        # 遍历所有yield文件
        yield_files = sorted(self.yield_data_dir.glob("yield_*.json"))

        for yield_file in tqdm(yield_files, desc="Loading yield data"):
            with open(yield_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for reaction in data:
                    # 跳过无效数据
                    if reaction.get('is_valid') != 'true':
                        continue
                    # 确保有产率信息
                    yield_val = reaction.get('product_yield', '')
                    if yield_val and yield_val != '':
                        try:
                            yield_float = float(yield_val)
                            if 0 <= yield_float <= 100:
                                reaction['yield_value'] = yield_float
                                reactions.append(reaction)
                        except (ValueError, TypeError):
                            continue

        print(f"Loaded {len(reactions)} valid reactions with yield data")
        self.reactions = reactions
        return reactions

    def load_smiles_data(self) -> List[Dict]:
        """加载SMILES数据用于推理"""
        with open(self.smiles_data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    @staticmethod
    def _parse_yield_string(yield_str: str) -> Optional[float]:
        """Parse yield string to float. Returns None if unparseable.

        Handles: '73%', '73', '<5%', 'trace' (→0.5), 'n.d.'/'n.r.' (→None), '0%' (→0).
        """
        if not yield_str:
            return None
        val = yield_str.strip().lower().replace('％', '%').replace(' ', '')
        if val in ('-', ''):
            return None
        if val in ('trace', 'traces'):
            return 0.5
        if val in ('n.d.', 'nd', 'n.d', 'n.r.', 'nr', 'n.r'):
            return None
        # "<5%" → 2.5 (midpoint of 0-5)
        if val.startswith('<') or val.startswith('＜'):
            try:
                num = float(val.lstrip('<＜').rstrip('%'))
                return num / 2.0
            except (ValueError, TypeError):
                return None
        # Range "28-33%" → midpoint
        if '-' in val and '%' in val:
            try:
                parts = val.rstrip('%').split('-')
                return (float(parts[0]) + float(parts[1])) / 2.0
            except (ValueError, TypeError, IndexError):
                return None
        # Normal "73%" or "73"
        try:
            return float(val.rstrip('%'))
        except (ValueError, TypeError):
            return None

    def load_smiles_reactions(self) -> List[Dict]:
        """从 extracted_smiles.json 加载反应，正确解析 yield_ratio 和 isolated_yield，
        转换为与 alkene_reactions_by_yield 相同的格式。

        优先使用 isolated_yield，其次 yield_ratio。无法解析产率的反应也保留
        （yield_value=None，后续过滤由调用方决定）。

        Returns:
            转换后的反应列表
        """
        raw_data = self.load_smiles_data()
        reactions = []
        stats = {'numeric': 0, 'trace': 0, 'zero': 0, 'unparseable': 0, 'no_yield': 0}

        for entry in raw_data:
            products = entry.get('products', [])
            if not products:
                continue

            # Parse yield: prefer isolated_yield, fallback to yield_ratio
            p0 = products[0]
            yield_val = None
            for field in ('isolated_yield', 'yield_ratio'):
                yield_str = p0.get(field, '').strip()
                if yield_str:
                    yield_val = self._parse_yield_string(yield_str)
                    if yield_val is not None:
                        break

            # Stats
            if yield_val is None:
                raw_yr = p0.get('yield_ratio', '').strip()
                raw_iy = p0.get('isolated_yield', '').strip()
                if raw_yr or raw_iy:
                    stats['unparseable'] += 1
                else:
                    stats['no_yield'] += 1
            elif yield_val == 0:
                stats['zero'] += 1
            elif yield_val <= 1:
                stats['trace'] += 1
            else:
                stats['numeric'] += 1

            converted = {
                'is_valid': 'true',
                '_source': 'extracted_smiles',
                'reactants': [
                    {'smiles': r.get('SMILES') or r.get('smiles', '')}
                    for r in entry.get('reactants', [])
                ],
                'products': [
                    {'smiles': p.get('SMILES') or p.get('smiles', '')}
                    for p in products
                ],
                'solvents': [
                    {'smiles': s.get('SMILES') or s.get('smiles', '')}
                    for s in entry.get('solvents', [])
                ],
                'reagents': [
                    {'smiles': r.get('SMILES') or r.get('smiles', '')}
                    for r in entry.get('reagents', [])
                ],
                'catalysts': [
                    {'smiles': c.get('SMILES') or c.get('smiles', '')}
                    for c in entry.get('catalysts', [])
                ],
            }

            if yield_val is not None:
                yield_val = max(0.0, min(100.0, yield_val))
                converted['yield_value'] = yield_val
                converted['product_yield'] = str(yield_val)

            # 转换 current_conditions → electrochemistry_params
            conds = entry.get('current_conditions', [])
            cond = conds[0] if conds else {}
            converted['electrochemistry_params'] = {
                'anode': cond.get('Anode(+)', '') or '',
                'cathode': cond.get('Cathode(-)', '') or '',
                'electrolyte': cond.get('Electrolyte_SMILES', '') or '',
                'cell_type': cond.get('Reaction_Type', '') or '',
                'current': cond.get('Constant_Current', '') or '',
                'current_density': cond.get('Current_Density', '') or '',
                'potential': cond.get('Constant_Potential', '') or '',
            }

            # 过滤掉无反应物或无产物的条目
            if (converted['reactants'] and converted['reactants'][0]['smiles']
                    and converted['products'] and converted['products'][0]['smiles']):
                reactions.append(converted)

        print(f"Loaded {len(reactions)} reactions from extracted_smiles.json")
        print(f"  Yield stats: {stats['numeric']} numeric, {stats['trace']} trace, "
              f"{stats['zero']} zero, {stats['unparseable']} unparseable, {stats['no_yield']} no_yield")
        return reactions

    def load_failed_reactions(self) -> List[Dict]:
        """Backward-compatible wrapper: load reactions with yield=0 for failed ones."""
        all_rxns = self.load_smiles_reactions()
        # Only return those without a valid yield (truly failed/unmeasured)
        failed = []
        for rxn in all_rxns:
            if 'yield_value' not in rxn:
                rxn['yield_value'] = 0.0
                rxn['product_yield'] = '0'
                rxn['_source'] = 'extracted_smiles_failed'
                failed.append(rxn)
        print(f"  Of which {len(failed)} have no parseable yield (marked as failed)")
        return failed

    @staticmethod
    def _reaction_signature(rxn: Dict) -> tuple:
        """生成反应签名用于去重（基于反应物+产物 SMILES 集合）"""
        reactants = tuple(sorted(
            r.get('smiles') or r.get('SMILES', '')
            for r in rxn.get('reactants', [])
        ))
        products = tuple(sorted(
            p.get('smiles') or p.get('SMILES', '')
            for p in rxn.get('products', [])
        ))
        return (reactants, products)

    @staticmethod
    def _full_signature(rxn: Dict) -> tuple:
        """生成包含条件信息的完整签名（反应物+产物+电极+电解质+溶剂）"""
        reactants = tuple(sorted(
            r.get('smiles') or r.get('SMILES', '')
            for r in rxn.get('reactants', [])
        ))
        products = tuple(sorted(
            p.get('smiles') or p.get('SMILES', '')
            for p in rxn.get('products', [])
        ))
        echem = rxn.get('electrochemistry_params', {})
        anode = echem.get('anode', '') or ''
        cathode = echem.get('cathode', '') or ''
        electrolyte = echem.get('electrolyte', '') or ''
        solvents = tuple(sorted(
            s.get('smiles') or s.get('SMILES', '')
            for s in rxn.get('solvents', [])
        ))
        return (reactants, products, anode, cathode, electrolyte, solvents)

    def load_combined_data(self, include_failed: bool = True) -> List[Dict]:
        """合并 alkene_reactions_by_yield 数据和 extracted_smiles.json 数据，去重。

        去重策略：
        - 与产率数据去重：按反应物+产物签名（同一反应在产率数据中已有记录则跳过）
        - extracted_smiles 内部去重：按完整签名（反应物+产物+条件）

        Args:
            include_failed: 是否包含 extracted_smiles.json 中的数据

        Returns:
            合并后的反应列表
        """
        yield_reactions = self.load_yield_data()

        if not include_failed:
            return yield_reactions

        # 产率数据的反应签名（用于跨数据源去重）
        yield_reaction_sigs = set()
        for rxn in yield_reactions:
            yield_reaction_sigs.add(self._reaction_signature(rxn))

        smiles_reactions = self.load_smiles_reactions()

        # 去重并过滤
        seen_full_sigs = set()
        new_reactions = []
        skipped_overlap = 0
        skipped_dup = 0
        skipped_no_yield = 0
        for rxn in smiles_reactions:
            # 只保留有产率数据的
            if 'yield_value' not in rxn:
                skipped_no_yield += 1
                continue
            rxn_sig = self._reaction_signature(rxn)
            if rxn_sig in yield_reaction_sigs:
                skipped_overlap += 1
                continue
            full_sig = self._full_signature(rxn)
            if full_sig in seen_full_sigs:
                skipped_dup += 1
                continue
            seen_full_sigs.add(full_sig)
            new_reactions.append(rxn)

        combined = yield_reactions + new_reactions
        print(f"Combined dataset: {len(yield_reactions)} from alkene + {len(new_reactions)} from extracted_smiles "
              f"= {len(combined)} total "
              f"(skipped: {skipped_overlap} overlap, {skipped_dup} dup, {skipped_no_yield} no yield)")
        self.reactions = combined
        return combined

    def extract_reaction_features(self, reaction: Dict) -> Dict:
        """提取单个反应的特征"""
        features = {
            'reaction_smiles': reaction.get('reaction_smiles', ''),
            'mapped_smiles': reaction.get('mapped_smiles', ''),
            'reactants': [],
            'products': [],
            'solvents': [],
            'catalysts': [],
            'reagents': [],
            'yield': reaction.get('yield_value', None)
        }

        # 提取反应物SMILES
        for r in reaction.get('reactants', []):
            smiles = r.get('smiles') or r.get('SMILES', '')
            if smiles:
                features['reactants'].append(smiles)

        # 提取产物SMILES
        for p in reaction.get('products', []):
            smiles = p.get('smiles') or p.get('SMILES', '')
            if smiles:
                features['products'].append(smiles)

        # 提取溶剂SMILES
        for s in reaction.get('solvents', []):
            smiles = s.get('smiles') or s.get('SMILES', '')
            if smiles:
                features['solvents'].append(smiles)

        # 提取催化剂SMILES
        for c in reaction.get('catalysts', []):
            smiles = c.get('smiles') or c.get('SMILES', '')
            if smiles:
                features['catalysts'].append(smiles)

        # 提取电化学参数
        echem = reaction.get('electrochemistry_params', {})
        features['electrochemistry'] = {
            'anode': self._encode_electrode(echem.get('anode')),
            'cathode': self._encode_electrode(echem.get('cathode')),
            'electrolyte': echem.get('electrolyte', ''),
            'current': self._parse_current(echem.get('current')),
            'current_density': self._parse_current_density(echem.get('current_density')),
            'potential': self._parse_potential(echem.get('potential')),
            'cell_type': self._encode_cell_type(echem.get('cell_type'))
        }

        return features

    def _encode_electrode(self, electrode: Optional[str]) -> int:
        """编码电极材料"""
        if electrode is None:
            return self.ELECTRODE_MATERIALS[None]
        electrode_lower = electrode.lower().strip()
        return self.ELECTRODE_MATERIALS.get(electrode_lower, 14)

    def _encode_cell_type(self, cell_type: Optional[str]) -> int:
        """编码电解池类型"""
        if cell_type is None:
            return self.CELL_TYPES[None]
        cell_lower = cell_type.lower().strip()
        return self.CELL_TYPES.get(cell_lower, 4)

    def _parse_current(self, current_str: Optional[str]) -> float:
        """解析电流值 (转换为mA)"""
        if not current_str:
            return 0.0
        try:
            # 移除单位，提取数值
            current_str = current_str.lower().replace(' ', '')
            if 'ma' in current_str:
                return float(current_str.replace('ma', ''))
            elif 'a' in current_str:
                return float(current_str.replace('a', '')) * 1000
            return float(current_str)
        except (ValueError, AttributeError):
            return 0.0

    def _parse_current_density(self, cd_str: Optional[str]) -> float:
        """解析电流密度 (转换为mA/cm²)"""
        if not cd_str:
            return 0.0
        try:
            cd_str = cd_str.lower().replace(' ', '')
            # 简化处理，提取数值部分
            import re
            nums = re.findall(r'[\d.]+', cd_str)
            if nums:
                return float(nums[0])
            return 0.0
        except (ValueError, AttributeError):
            return 0.0

    def _parse_potential(self, potential_str: Optional[str]) -> float:
        """解析电势值 (V)"""
        if not potential_str:
            return 0.0
        try:
            potential_str = potential_str.lower().replace(' ', '')
            import re
            nums = re.findall(r'[-\d.]+', potential_str)
            if nums:
                return float(nums[0])
            return 0.0
        except (ValueError, AttributeError):
            return 0.0

    def prepare_dataset(self, random_seed: int = 42,
                         include_failed: bool = False) -> Tuple[List[Dict], List[Dict], List[Dict]]:
        """准备训练、验证、测试数据集

        Args:
            random_seed: 随机种子
            include_failed: 是否包含 extracted_smiles.json 中的失败反应 (yield=0)
        """
        if not self.reactions:
            if include_failed:
                self.load_combined_data(include_failed=True)
            else:
                self.load_yield_data()

        # 提取所有反应特征
        processed_reactions = []
        for rxn in tqdm(self.reactions, desc="Processing reactions"):
            features = self.extract_reaction_features(rxn)
            if features['reactants'] and features['products'] and features['yield'] is not None:
                processed_reactions.append(features)

        print(f"Processed {len(processed_reactions)} valid reactions")

        # 划分数据集
        train_data, temp_data = train_test_split(
            processed_reactions, test_size=0.2, random_state=random_seed
        )
        val_data, test_data = train_test_split(
            temp_data, test_size=0.5, random_state=random_seed
        )

        print(f"Train: {len(train_data)}, Val: {len(val_data)}, Test: {len(test_data)}")

        return train_data, val_data, test_data

    def get_condition_vocabulary(self) -> Dict:
        """获取反应条件的词汇表（用于条件推荐）"""
        solvents = set()
        electrolytes = set()

        for rxn in self.reactions:
            # 收集溶剂
            for s in rxn.get('solvents', []):
                smiles = s.get('smiles', '')
                if smiles:
                    solvents.add(smiles)

            # 收集电解质
            echem = rxn.get('electrochemistry_params', {})
            elec = echem.get('electrolyte', '')
            if elec:
                electrolytes.add(elec)

        return {
            'solvents': list(solvents),
            'electrolytes': list(electrolytes),
            'electrode_materials': list(self.ELECTRODE_MATERIALS.keys()),
            'cell_types': list(self.CELL_TYPES.keys())
        }


if __name__ == "__main__":
    # 测试数据加载
    processor = ReactionDataProcessor(
        yield_data_dir="/inspire/hdd/global_user/gelingli-253114010248/alkene_reactions_by_yield",
        smiles_data_path="/inspire/hdd/global_user/gelingli-253114010248/extracted_smiles.json"
    )

    # 测试失败反应加载
    failed = processor.load_failed_reactions()
    print(f"Failed reactions: {len(failed)}")
    if failed:
        print(f"Sample failed reaction keys: {list(failed[0].keys())}")

    # 测试合并数据集
    combined = processor.load_combined_data(include_failed=True)
    num_failed = sum(1 for r in combined if r.get('yield_value', -1) == 0.0)
    print(f"Total combined: {len(combined)}, failed: {num_failed}")

    # 测试完整 pipeline
    train, val, test = processor.prepare_dataset(include_failed=True)
    print(f"\nTrain: {len(train)}, Val: {len(val)}, Test: {len(test)}")
    print(f"Sample reaction: {train[0]}")
