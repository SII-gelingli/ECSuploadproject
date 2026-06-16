"""
添加催化剂信息到现有数据集
"""
import sys
import json
from pathlib import Path
from collections import Counter

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

import torch
from tqdm import tqdm

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.data_processor import ReactionDataProcessor
from utils.feature_extractor import MolecularFeatureExtractor


def main():
    data_dir = project_root / 'data'

    # 加载原始反应数据
    print("加载原始反应数据...")
    processor = ReactionDataProcessor(
        yield_data_dir="/inspire/hdd/global_user/gelingli-253114010248/alkene_reactions_by_yield",
        smiles_data_path="/inspire/hdd/global_user/gelingli-253114010248/extracted_smiles.json"
    )
    reactions = processor.load_combined_data(include_failed=True)
    print(f"总反应数: {len(reactions)}")

    # 建立反应索引 (用reaction_smiles作为key)
    reaction_lookup = {}
    for rxn in reactions:
        key = rxn.get('reaction_smiles', '')
        if key:
            reaction_lookup[key] = rxn

    # 统计催化剂
    print("\n统计催化剂...")
    catalysts = Counter()
    for rxn in reactions:
        for cat in rxn.get('catalysts', []):
            smiles = cat.get('smiles', '')
            if smiles:
                catalysts[smiles] += 1

    print(f"  独特催化剂: {len(catalysts)}")
    print(f"  有催化剂的反应: {sum(1 for r in reactions if r.get('catalysts'))}")

    # 构建催化剂词汇表
    catalyst_vocab = {s: i + 1 for i, (s, _) in enumerate(catalysts.most_common(100))}
    print(f"  词汇表大小: {len(catalyst_vocab)} (取Top 100)")

    # 更新vocab.json
    vocab_path = data_dir / 'vocab.json'
    if vocab_path.exists():
        with open(vocab_path) as f:
            vocab = json.load(f)
    else:
        vocab = {}

    vocab['catalyst'] = catalyst_vocab

    with open(vocab_path, 'w') as f:
        json.dump(vocab, f, indent=2)
    print(f"\n已更新 vocab.json，添加 {len(catalyst_vocab)} 种催化剂")

    # 特征提取器
    mol_extractor = MolecularFeatureExtractor(fingerprint_size=2048)

    # 更新每个数据集
    for split in ['train', 'val', 'test']:
        # 加载带xTB的数据
        xtb_path = data_dir / f'{split}_xtb.pt'
        if not xtb_path.exists():
            print(f"\n跳过 {split}: {xtb_path} 不存在")
            continue

        print(f"\n处理 {split} 数据...")
        data = torch.load(xtb_path, weights_only=False)
        print(f"  样本数: {len(data)}")

        updated = 0
        has_catalyst = 0

        for item in tqdm(data, desc=f"添加催化剂到{split}"):
            # 尝试找到原始反应
            reactant_smiles = item.get('reactant_smiles', [])
            product_smiles = item.get('product_smiles', [])

            # 查找匹配的原始反应
            catalyst_smiles_list = []
            catalyst_label = 0

            # 遍历原始反应寻找匹配
            for rxn in reactions:
                rxn_reactants = [r.get('smiles', '') for r in rxn.get('reactants', [])]
                rxn_products = [p.get('smiles', '') for p in rxn.get('products', [])]

                # 简单匹配（检查是否有重叠）
                if (set(reactant_smiles) & set(rxn_reactants) and
                    set(product_smiles) & set(rxn_products)):
                    # 找到匹配
                    for cat in rxn.get('catalysts', []):
                        smi = cat.get('smiles', '')
                        if smi:
                            catalyst_smiles_list.append(smi)
                            if smi in catalyst_vocab:
                                catalyst_label = catalyst_vocab[smi]
                    break

            # 添加催化剂信息
            item['catalyst_label'] = catalyst_label
            item['catalyst_smiles'] = catalyst_smiles_list

            # 计算催化剂指纹
            if catalyst_smiles_list:
                catalyst_fp = mol_extractor.encode_molecules(catalyst_smiles_list)
                has_catalyst += 1
            else:
                catalyst_fp = [0.0] * 2048

            item['catalyst_fp'] = catalyst_fp

            # 计算催化剂xTB特征 (如果有的话，用占位符)
            item['catalyst_xtb'] = [0.0] * 11  # 占位符，后续可从xTB CSV补充

            updated += 1

        print(f"  更新: {updated}, 有催化剂: {has_catalyst} ({has_catalyst/len(data)*100:.1f}%)")

        # 保存更新后的数据
        output_path = data_dir / f'{split}_xtb_cat.pt'
        torch.save(data, output_path)
        print(f"  保存到: {output_path}")

    print("\n完成!")


if __name__ == "__main__":
    main()
