"""
改进版分段产率预测模型 - 测试多种聚类策略

聚类策略：
1. yield_based: 直接按产率范围分段（最简单直接）
2. pca_kmeans: PCA降维后K-Means
3. combined: 结合结构特征和产率进行聚类
"""
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
import numpy as np

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset, Subset
from tqdm import tqdm
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class SimpleYieldPredictor(nn.Module):
    """简单的产率预测网络"""

    def __init__(self, input_dim: int, hidden_dims: list = [256, 128], dropout: float = 0.3):
        super().__init__()

        layers = []
        prev_dim = input_dim
        for h_dim in hidden_dims:
            layers.extend([
                nn.Linear(prev_dim, h_dim),
                nn.LayerNorm(h_dim),
                nn.GELU(),
                nn.Dropout(dropout),
            ])
            prev_dim = h_dim
        layers.append(nn.Linear(prev_dim, 1))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return torch.sigmoid(self.net(x))


class ClusteredDataset(Dataset):
    """带聚类标签的数据集"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path, weights_only=False)
        self.cluster_labels = None

    def __len__(self):
        return len(self.data)

    def get_reaction_fp(self, idx):
        item = self.data[idx]
        return np.array(item['reactant_fp'] + item['product_fp'] + item['diff_fp'])

    def get_yield(self, idx):
        return self.data[idx]['yield']

    def get_all_reaction_fps(self):
        return np.array([self.get_reaction_fp(i) for i in range(len(self.data))])

    def get_all_yields(self):
        return np.array([self.get_yield(i) for i in range(len(self.data))])

    def set_cluster_labels(self, labels):
        self.cluster_labels = labels

    def __getitem__(self, idx):
        item = self.data[idx]
        full_features = (
            item['reactant_fp'] + item['product_fp'] + item['diff_fp'] +
            item['solvent_fp'] + item['electrolyte_fp'] +
            [item['anode'], item['cathode'], item['cell_type'],
             item['electrolyte_label'], item['solvent_label'], item['reagent_label']] +
            item['reactant_xtb'] + item['product_xtb'] +
            item['solvent_xtb'] + item['electrolyte_xtb'] + item['reaction_diff_xtb']
        )
        return {
            'features': torch.tensor(full_features, dtype=torch.float32),
            'yield': torch.tensor(item['yield'] / 100.0, dtype=torch.float32),
            'reaction_fp': torch.tensor(self.get_reaction_fp(idx), dtype=torch.float32),
        }


def cluster_by_yield(train_yields, val_yields, test_yields, num_clusters):
    """
    策略1: 按产率范围分段

    优点：直接按目标变量分段，每个模型只需预测特定范围
    """
    # 计算分位数作为边界
    percentiles = np.linspace(0, 100, num_clusters + 1)
    boundaries = np.percentile(train_yields, percentiles)
    boundaries[-1] = 101  # 确保最大值被包含

    def assign_cluster(yields):
        labels = np.zeros(len(yields), dtype=int)
        for i, y in enumerate(yields):
            for c in range(num_clusters):
                if boundaries[c] <= y < boundaries[c + 1]:
                    labels[i] = c
                    break
        return labels

    train_labels = assign_cluster(train_yields)
    val_labels = assign_cluster(val_yields)
    test_labels = assign_cluster(test_yields)

    print(f"  产率边界: {[f'{b:.1f}' for b in boundaries]}")

    return train_labels, val_labels, test_labels, {'boundaries': boundaries.tolist()}


def cluster_by_pca_kmeans(train_fps, val_fps, test_fps, num_clusters, n_components=50):
    """
    策略2: PCA降维后K-Means

    优点：降低维度，缓解高维诅咒
    """
    # PCA降维
    pca = PCA(n_components=n_components, random_state=42)
    train_reduced = pca.fit_transform(train_fps)
    val_reduced = pca.transform(val_fps)
    test_reduced = pca.transform(test_fps)

    print(f"  PCA 解释方差: {pca.explained_variance_ratio_.sum():.2%}")

    # K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    train_labels = kmeans.fit_predict(train_reduced)
    val_labels = kmeans.predict(val_reduced)
    test_labels = kmeans.predict(test_reduced)

    return train_labels, val_labels, test_labels, {'pca': pca, 'kmeans': kmeans}


def cluster_by_combined(train_fps, train_yields, val_fps, val_yields, test_fps, test_yields,
                        num_clusters, n_components=50, yield_weight=0.3):
    """
    策略3: 结合结构特征和产率

    优点：同时考虑分子结构相似性和产率相似性
    """
    # PCA降维结构特征
    pca = PCA(n_components=n_components, random_state=42)
    train_struct = pca.fit_transform(train_fps)
    val_struct = pca.transform(val_fps)
    test_struct = pca.transform(test_fps)

    # 标准化
    struct_scaler = StandardScaler()
    train_struct_scaled = struct_scaler.fit_transform(train_struct)
    val_struct_scaled = struct_scaler.transform(val_struct)
    test_struct_scaled = struct_scaler.transform(test_struct)

    # 标准化产率
    yield_scaler = StandardScaler()
    train_yield_scaled = yield_scaler.fit_transform(train_yields.reshape(-1, 1))
    val_yield_scaled = yield_scaler.transform(val_yields.reshape(-1, 1))
    test_yield_scaled = yield_scaler.transform(test_yields.reshape(-1, 1))

    # 组合特征（结构 + 加权产率）
    train_combined = np.hstack([train_struct_scaled, train_yield_scaled * yield_weight * n_components])
    val_combined = np.hstack([val_struct_scaled, val_yield_scaled * yield_weight * n_components])
    test_combined = np.hstack([test_struct_scaled, test_yield_scaled * yield_weight * n_components])

    print(f"  组合特征维度: {train_combined.shape[1]}, 产率权重: {yield_weight}")

    # K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    train_labels = kmeans.fit_predict(train_combined)
    val_labels = kmeans.predict(val_combined)
    test_labels = kmeans.predict(test_combined)

    return train_labels, val_labels, test_labels, {'pca': pca, 'kmeans': kmeans}


def train_single_model(model, train_loader, val_loader, device, epochs, patience, lr, weight_decay):
    """训练单个模型"""
    optimizer = optim.AdamW(model.parameters(), lr=lr, weight_decay=weight_decay)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs, eta_min=1e-6)
    criterion = nn.MSELoss()

    best_val_mae = float('inf')
    best_state = None
    patience_counter = 0

    for epoch in range(epochs):
        model.train()
        for batch in train_loader:
            features = batch['features'].to(device)
            labels = batch['yield'].to(device).unsqueeze(1)
            optimizer.zero_grad()
            pred = model(features)
            loss = criterion(pred, labels)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()

        model.eval()
        val_preds, val_labels_list = [], []
        with torch.no_grad():
            for batch in val_loader:
                features = batch['features'].to(device)
                labels = batch['yield'].to(device)
                pred = model(features).flatten()
                val_preds.extend((pred * 100).cpu().tolist())
                val_labels_list.extend((labels * 100).cpu().tolist())

        val_mae = np.mean(np.abs(np.array(val_preds) - np.array(val_labels_list)))

        if val_mae < best_val_mae:
            best_val_mae = val_mae
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            patience_counter = 0
        else:
            patience_counter += 1

        scheduler.step()
        if patience_counter >= patience:
            break

    if best_state:
        model.load_state_dict(best_state)
    return best_val_mae


def evaluate_clusters(models, test_dataset, test_labels, num_clusters, device, batch_size):
    """评估每个聚类的性能"""
    all_preds, all_labels = [], []
    cluster_metrics = {}

    for c in range(num_clusters):
        test_indices = [i for i in range(len(test_dataset)) if test_labels[i] == c]
        if len(test_indices) == 0 or c not in models:
            continue

        test_subset = Subset(test_dataset, test_indices)
        test_loader = DataLoader(test_subset, batch_size=batch_size, shuffle=False, num_workers=2)

        model = models[c]
        model.eval()
        cluster_preds, cluster_labels = [], []

        with torch.no_grad():
            for batch in test_loader:
                features = batch['features'].to(device)
                labels = batch['yield'].to(device)
                pred = model(features).flatten()
                cluster_preds.extend((pred * 100).cpu().tolist())
                cluster_labels.extend((labels * 100).cpu().tolist())

        all_preds.extend(cluster_preds)
        all_labels.extend(cluster_labels)

        preds_arr = np.array(cluster_preds)
        labels_arr = np.array(cluster_labels)
        mae = np.mean(np.abs(preds_arr - labels_arr))

        if len(labels_arr) > 1 and np.var(labels_arr) > 0:
            r2 = 1 - np.sum((preds_arr - labels_arr)**2) / np.sum((labels_arr - labels_arr.mean())**2)
        else:
            r2 = 0.0

        cluster_metrics[c] = {'count': len(test_indices), 'mae': mae, 'r2': r2}

    # 总体指标
    all_preds = np.array(all_preds)
    all_labels = np.array(all_labels)
    total_mae = np.mean(np.abs(all_preds - all_labels))
    total_rmse = np.sqrt(np.mean((all_preds - all_labels)**2))
    ss_res = np.sum((all_preds - all_labels)**2)
    ss_tot = np.sum((all_labels - all_labels.mean())**2)
    total_r2 = 1 - ss_res / ss_tot

    return total_mae, total_rmse, total_r2, cluster_metrics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default=str(project_root / 'data'))
    parser.add_argument('--output_dir', type=str, default=str(project_root / 'checkpoints' / 'clustered_v2'))
    parser.add_argument('--cluster_method', type=str, default='yield_based',
                        choices=['yield_based', 'pca_kmeans', 'combined'])
    parser.add_argument('--num_clusters', type=int, default=6)
    parser.add_argument('--pca_components', type=int, default=50)
    parser.add_argument('--yield_weight', type=float, default=0.3)
    parser.add_argument('--hidden_dims', type=str, default='256,128')
    parser.add_argument('--dropout', type=float, default=0.3)
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--weight_decay', type=float, default=1e-4)
    parser.add_argument('--epochs', type=int, default=50)
    parser.add_argument('--patience', type=int, default=10)
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    hidden_dims = [int(x) for x in args.hidden_dims.split(',')]
    device = torch.device(args.device)

    output_dir = Path(args.output_dir) / args.cluster_method
    output_dir.mkdir(parents=True, exist_ok=True)

    # 加载数据
    print(f"\nDevice: {device}")
    print("=" * 70)
    print("加载数据...")

    train_dataset = ClusteredDataset(Path(args.data_dir) / 'train_xtb_cat.pt')
    val_dataset = ClusteredDataset(Path(args.data_dir) / 'val_xtb_cat.pt')
    test_dataset = ClusteredDataset(Path(args.data_dir) / 'test_xtb_cat.pt')

    train_fps = train_dataset.get_all_reaction_fps()
    val_fps = val_dataset.get_all_reaction_fps()
    test_fps = test_dataset.get_all_reaction_fps()

    train_yields = train_dataset.get_all_yields()
    val_yields = val_dataset.get_all_yields()
    test_yields = test_dataset.get_all_yields()

    print(f"  Train: {len(train_dataset)}, Val: {len(val_dataset)}, Test: {len(test_dataset)}")

    # 聚类
    print("=" * 70)
    print(f"聚类方法: {args.cluster_method}, K={args.num_clusters}")
    print("=" * 70)

    if args.cluster_method == 'yield_based':
        train_labels, val_labels, test_labels, info = cluster_by_yield(
            train_yields, val_yields, test_yields, args.num_clusters
        )
    elif args.cluster_method == 'pca_kmeans':
        train_labels, val_labels, test_labels, info = cluster_by_pca_kmeans(
            train_fps, val_fps, test_fps, args.num_clusters, args.pca_components
        )
    elif args.cluster_method == 'combined':
        train_labels, val_labels, test_labels, info = cluster_by_combined(
            train_fps, train_yields, val_fps, val_yields, test_fps, test_yields,
            args.num_clusters, args.pca_components, args.yield_weight
        )

    train_dataset.set_cluster_labels(train_labels)
    val_dataset.set_cluster_labels(val_labels)
    test_dataset.set_cluster_labels(test_labels)

    # 聚类分布
    print("\n聚类分布:")
    for c in range(args.num_clusters):
        train_c = (train_labels == c).sum()
        val_c = (val_labels == c).sum()
        test_c = (test_labels == c).sum()

        # 该聚类的产率统计
        cluster_yields = train_yields[train_labels == c]
        if len(cluster_yields) > 0:
            yield_info = f"产率: {cluster_yields.mean():.1f}±{cluster_yields.std():.1f}%"
        else:
            yield_info = ""
        print(f"  Cluster {c}: Train={train_c}, Val={val_c}, Test={test_c}, {yield_info}")

    # 训练
    print("\n" + "=" * 70)
    print("训练各聚类模型...")
    print("=" * 70)

    models = {}
    start_time = datetime.now()

    for c in range(args.num_clusters):
        train_indices = [i for i in range(len(train_dataset)) if train_labels[i] == c]
        val_indices = [i for i in range(len(val_dataset)) if val_labels[i] == c]

        if len(train_indices) < 10 or len(val_indices) < 5:
            print(f"Cluster {c}: 样本不足，跳过")
            continue

        train_subset = Subset(train_dataset, train_indices)
        val_subset = Subset(val_dataset, val_indices)
        train_loader = DataLoader(train_subset, batch_size=args.batch_size, shuffle=True, num_workers=2)
        val_loader = DataLoader(val_subset, batch_size=args.batch_size*2, shuffle=False, num_workers=2)

        model = SimpleYieldPredictor(10301, hidden_dims, args.dropout).to(device)
        best_mae = train_single_model(model, train_loader, val_loader, device,
                                      args.epochs, args.patience, args.lr, args.weight_decay)
        models[c] = model
        print(f"Cluster {c}: N={len(train_indices)}, Val MAE={best_mae:.2f}%")

    elapsed = datetime.now() - start_time
    print(f"\n训练完成: {elapsed}")

    # 评估
    print("\n" + "=" * 70)
    print("测试集评估")
    print("=" * 70)

    total_mae, total_rmse, total_r2, cluster_metrics = evaluate_clusters(
        models, test_dataset, test_labels, args.num_clusters, device, args.batch_size*2
    )

    for c in sorted(cluster_metrics.keys()):
        m = cluster_metrics[c]
        print(f"  Cluster {c}: N={m['count']}, MAE={m['mae']:.2f}%, R²={m['r2']:.4f}")

    print(f"\n总体结果:")
    print(f"  Test MAE:  {total_mae:.2f}%")
    print(f"  Test RMSE: {total_rmse:.2f}%")
    print(f"  Test R²:   {total_r2:.4f}")

    baseline_r2, baseline_mae = 0.363, 12.43
    r2_imp = total_r2 - baseline_r2
    print(f"\n与基线比较: R² {r2_imp:+.4f} ({baseline_r2:.3f} → {total_r2:.3f})")

    if r2_imp > 0:
        print(f"🎉 成功超越基线!")

    # 保存
    results = {
        'cluster_method': args.cluster_method,
        'num_clusters': args.num_clusters,
        'test_mae': total_mae,
        'test_r2': total_r2,
        'r2_improvement': r2_imp,
        'cluster_metrics': {str(k): v for k, v in cluster_metrics.items()},
        'args': vars(args),
    }
    with open(output_dir / 'results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n保存到: {output_dir}")
    return results


if __name__ == "__main__":
    main()
