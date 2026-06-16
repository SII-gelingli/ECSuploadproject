"""
预测脚本：使用训练好的模型进行产率预测和条件推荐
"""
import os
import sys
import argparse
import json
from pathlib import Path

# 添加本地包路径
LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

import torch
import numpy as np
from tqdm import tqdm

# 添加项目路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.feature_extractor import MolecularFeatureExtractor, ReactionFeaturizer
from models.yield_predictor import YieldPredictor
from models.condition_recommender import ConditionRecommender


class YieldConditionPredictor:
    """产率预测和条件推荐"""

    # 电极材料映射
    ELECTRODE_NAMES = {
        0: 'carbon', 1: 'graphite', 2: 'platinum', 3: 'glassy carbon',
        4: 'rvc', 5: 'nickel', 6: 'stainless steel', 7: 'copper',
        8: 'zinc', 9: 'lead', 10: 'gold', 11: 'silver', 12: 'iron',
        13: 'magnesium', 14: 'aluminum', 15: 'boron-doped diamond',
        16: 'niobium', 17: 'titanium', 18: 'unknown'
    }

    CELL_TYPE_NAMES = {
        0: 'undivided', 1: 'divided', 2: 'flow', 3: 'sealed',
        4: 'other', 5: 'unknown'
    }

    def __init__(
        self,
        yield_model_path: str = None,
        condition_model_path: str = None,
        vocab_path: str = None,
        fp_size: int = 2048,
        device: str = None
    ):
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')
        self.fp_size = fp_size
        self.mol_extractor = MolecularFeatureExtractor(fp_size)
        self.featurizer = ReactionFeaturizer(fp_size)

        # 加载产率预测模型
        self.yield_model = None
        if yield_model_path and Path(yield_model_path).exists():
            self._load_yield_model(yield_model_path)

        # 加载条件推荐模型
        self.condition_model = None
        self.electrolyte_vocab = {}
        self.solvent_vocab = {}
        if condition_model_path and Path(condition_model_path).exists():
            self._load_condition_model(condition_model_path, vocab_path)

    def _load_yield_model(self, model_path: str):
        """加载产率预测模型"""
        print(f"Loading yield model from {model_path}")
        checkpoint = torch.load(model_path, map_location=self.device)

        input_dim = self.featurizer.get_feature_dim()
        config = checkpoint.get('config', {})
        hidden_dims = config.get('model', {}).get('predictor', {}).get('hidden_dims', [512, 256, 128])

        self.yield_model = YieldPredictor(
            input_dim=input_dim,
            hidden_dims=hidden_dims
        ).to(self.device)

        self.yield_model.load_state_dict(checkpoint['model_state_dict'])
        self.yield_model.eval()
        print("Yield model loaded successfully")

    def _load_condition_model(self, model_path: str, vocab_path: str = None):
        """加载条件推荐模型"""
        print(f"Loading condition model from {model_path}")
        checkpoint = torch.load(model_path, map_location=self.device)

        # 加载词汇表
        if vocab_path and Path(vocab_path).exists():
            with open(vocab_path) as f:
                vocab = json.load(f)
                self.electrolyte_vocab = vocab.get('electrolyte', {})
                self.solvent_vocab = vocab.get('solvent', {})

        # 创建反向映射
        self.idx_to_electrolyte = {v: k for k, v in self.electrolyte_vocab.items()}
        self.idx_to_solvent = {v: k for k, v in self.solvent_vocab.items()}
        self.reagent_vocab = vocab.get('reagent', {})
        self.idx_to_reagent = {v: k for k, v in self.reagent_vocab.items()}

        reaction_dim = self.fp_size * 3

        self.condition_model = ConditionRecommender(
            reaction_dim=reaction_dim,
            hidden_dim=256,
            num_anode_materials=19,
            num_cathode_materials=19,
            num_cell_types=6,
            num_electrolytes=len(self.electrolyte_vocab) + 1,
            num_solvents=len(self.solvent_vocab) + 1,
            num_reagents=len(self.reagent_vocab) + 1
        ).to(self.device)

        self.condition_model.load_state_dict(checkpoint['model_state_dict'])
        self.condition_model.eval()
        print("Condition model loaded successfully")

    def predict_yield(self, reaction: dict) -> float:
        """
        预测反应产率
        Args:
            reaction: 包含 reactants, products, solvents, electrochemistry 的字典
        Returns:
            预测产率 (0-100%)
        """
        if self.yield_model is None:
            raise RuntimeError("Yield model not loaded")

        features, _ = self.featurizer.featurize(reaction)
        features = torch.tensor(features, dtype=torch.float32).unsqueeze(0).to(self.device)

        with torch.no_grad():
            yield_pred = self.yield_model.predict_yield(features)

        return yield_pred.item()

    # SMILES类条件（索引0为unknown保留值，推理时需屏蔽）
    SMILES_CONDITION_KEYS = {'electrolyte', 'solvent', 'reagent'}

    # 各条件类型中需要屏蔽的 Unknown 索引
    UNKNOWN_INDICES = {
        'anode': 18,
        'cathode': 18,
        'cell_type': 5,
        'electrolyte': 0,
        'solvent': 0,
        'reagent': 0,
    }

    def recommend_conditions(self, reactants: list, products: list, top_k: int = 3) -> dict:
        """
        推荐反应条件
        Args:
            reactants: 反应物SMILES列表
            products: 产物SMILES列表
            top_k: 返回top_k个推荐
        Returns:
            推荐的条件字典
        """
        if self.condition_model is None:
            raise RuntimeError("Condition model not loaded")

        import torch.nn.functional as F_pred

        # 计算反应指纹
        reactant_fp = self.mol_extractor.encode_molecules(reactants)
        product_fp = self.mol_extractor.encode_molecules(products)
        diff_fp = np.abs(product_fp - reactant_fp)
        reaction_fp = np.concatenate([reactant_fp, product_fp, diff_fp])

        reaction_fp = torch.tensor(reaction_fp, dtype=torch.float32).unsqueeze(0).to(self.device)

        # 获取模型前向推理 logits
        self.condition_model.eval()
        with torch.no_grad():
            predictions = self.condition_model(reaction_fp)

        # 转换为可读格式
        result = {
            'anode': [],
            'cathode': [],
            'cell_type': [],
            'electrolyte': [],
            'solvent': [],
            'reagent': []
        }

        head_configs = [
            ('anode', 'anode_logits', 'material', self.ELECTRODE_NAMES),
            ('cathode', 'cathode_logits', 'material', self.ELECTRODE_NAMES),
            ('cell_type', 'cell_type_logits', 'type', self.CELL_TYPE_NAMES),
            ('electrolyte', 'electrolyte_logits', 'smiles', self.idx_to_electrolyte),
            ('solvent', 'solvent_logits', 'smiles', self.idx_to_solvent),
            ('reagent', 'reagent_logits', 'smiles', self.idx_to_reagent),
        ]

        for key, logit_key, label_field, name_map in head_configs:
            logits = predictions[logit_key]
            # 屏蔽 Unknown/缺失 索引
            unk_idx = self.UNKNOWN_INDICES.get(key)
            if unk_idx is not None:
                logits = logits.clone()
                logits[:, unk_idx] = float('-inf')
            probs = F_pred.softmax(logits, dim=-1)
            k = min(top_k, probs.size(-1))
            top_probs, top_indices = torch.topk(probs, k, dim=-1)

            for idx, prob in zip(top_indices[0].tolist(), top_probs[0].tolist()):
                result[key].append({
                    label_field: name_map.get(idx, 'unknown'),
                    'confidence': float(prob)
                })

        return result

    def predict_with_conditions(
        self,
        reactants: list,
        products: list,
        solvents: list = None,
        electrolyte: str = None,
        anode: int = 14,
        cathode: int = 14,
        cell_type: int = 4,
        current: float = 0.0,
        current_density: float = 0.0
    ) -> float:
        """
        给定完整条件预测产率
        """
        if self.yield_model is None:
            raise RuntimeError("Yield model not loaded")

        reaction = {
            'reactants': reactants,
            'products': products,
            'solvents': solvents or [],
            'electrochemistry': {
                'anode': anode,
                'cathode': cathode,
                'electrolyte': electrolyte or '',
                'current': current,
                'current_density': current_density,
                'potential': 0.0,
                'cell_type': cell_type
            }
        }

        return self.predict_yield(reaction)


def demo():
    """演示预测功能"""
    print("=" * 60)
    print("Yield Prediction & Condition Recommendation Demo")
    print("=" * 60)

    # 示例反应
    reactants = ["C=C(c1ccccc1)C(C)(O)c1ccccc1"]  # 双苯乙烯醇
    products = ["CC(=O)C(CCl)(c1ccccc1)c1ccccc1"]  # 氯代产物

    print(f"\nReactants: {reactants}")
    print(f"Products: {products}")

    # 检查模型文件
    model_dir = project_root / 'checkpoints'
    condition_model_dir = model_dir / 'condition_model'

    yield_model_path = model_dir / 'best_model.pt'
    condition_model_path = condition_model_dir / 'best_condition_model.pt'
    vocab_path = condition_model_dir / 'vocab.json'

    # 创建预测器
    predictor = YieldConditionPredictor(
        yield_model_path=str(yield_model_path) if yield_model_path.exists() else None,
        condition_model_path=str(condition_model_path) if condition_model_path.exists() else None,
        vocab_path=str(vocab_path) if vocab_path.exists() else None
    )

    # 推荐条件
    if predictor.condition_model is not None:
        print("\n--- Recommended Conditions ---")
        recommendations = predictor.recommend_conditions(reactants, products)
        print(json.dumps(recommendations, indent=2))
    else:
        print("\nCondition model not found. Train it first using train_condition.py")

    # 预测产率（如果有模型）
    if predictor.yield_model is not None:
        reaction = {
            'reactants': reactants,
            'products': products,
            'solvents': ['CC#N'],  # 乙腈
            'electrochemistry': {
                'anode': 0,  # carbon
                'cathode': 2,  # platinum
                'electrolyte': '[Mg+2].[Cl-].[Cl-]',
                'current': 25.0,
                'current_density': 0.0,
                'potential': 0.0,
                'cell_type': 0  # undivided
            }
        }
        yield_pred = predictor.predict_yield(reaction)
        print(f"\n--- Predicted Yield: {yield_pred:.1f}% ---")
    else:
        print("\nYield model not found. Train it first using train.py")


def main():
    parser = argparse.ArgumentParser(description='Predict yield and recommend conditions')
    parser.add_argument('--yield-model', type=str, default='checkpoints/best_model.pt',
                        help='Path to yield prediction model')
    parser.add_argument('--condition-model', type=str, default='checkpoints/condition_model/best_condition_model.pt',
                        help='Path to condition recommendation model')
    parser.add_argument('--vocab', type=str, default='checkpoints/condition_model/vocab.json',
                        help='Path to vocabulary file')
    parser.add_argument('--input', type=str, help='Input JSON file with reactions')
    parser.add_argument('--output', type=str, help='Output JSON file for predictions')
    parser.add_argument('--demo', action='store_true', help='Run demo')

    args = parser.parse_args()

    if args.demo:
        demo()
        return

    if not args.input:
        print("Please provide --input file or use --demo")
        return

    # 加载输入
    with open(args.input) as f:
        reactions = json.load(f)

    # 创建预测器
    predictor = YieldConditionPredictor(
        yield_model_path=args.yield_model,
        condition_model_path=args.condition_model,
        vocab_path=args.vocab
    )

    # 预测
    results = []
    for rxn in tqdm(reactions, desc="Predicting"):
        result = {'input': rxn}

        try:
            # 条件推荐
            reactants = [r.get('smiles', r.get('SMILES', '')) for r in rxn.get('reactants', [])]
            products = [p.get('smiles', p.get('SMILES', '')) for p in rxn.get('products', [])]

            if predictor.condition_model:
                result['recommended_conditions'] = predictor.recommend_conditions(reactants, products)

            # 产率预测（如果有条件信息）
            if predictor.yield_model and rxn.get('electrochemistry'):
                result['predicted_yield'] = predictor.predict_yield(rxn)

        except Exception as e:
            result['error'] = str(e)

        results.append(result)

    # 保存结果
    output_path = args.output or 'predictions.json'
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Results saved to {output_path}")


if __name__ == "__main__":
    main()
