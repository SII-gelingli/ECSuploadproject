"""
产率感知聚类 (Yield-Aware Clustering) 产率预测模型

策略：
1. 产率分层聚类：先按产率范围分层，再在每层内根据反应特征细分
2. 联合特征聚类：将产率信息融入聚类特征
3. 迭代优化聚类：根据预测误差动态调整聚类分配

优点：
- 聚类直接服务于预测任务
- 每个聚类内产率分布更集中，更容易学习
- 减少不同产率范围反应的相互干扰
"""
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
import numpy as np
from collections import defaultdict

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset, Subset
from tqdm import tqdm
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from scipy.spatial.distance import cdist

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class SimpleYieldPredictor(nn.Module):
    """产率预测网络"""

    def __init__(self, input_dim: int, hidden_dims: list = [512, 256, 128], dropout: float = 0.3):
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


class YieldAwareDataset(Dataset):
    """产率感知数据集"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path, weights_only=False)
        self.cluster_labels = None

    def __len__(self):
        return len(self.data)

    def get_yield(self, idx):
        """获取产率"""
        return self.data[idx]['yield']

    def get_all_yields(self):
        """获取所有产率"""
        return np.array([self.get_yield(i) for i in range(len(self.data))])

    def get_reaction_fp(self, idx):
        """获取反应指纹"""
        item = self.data[idx]
        return np.array(item['reactant_fp'] + item['product_fp'] + item['diff_fp'])

    def get_all_reaction_fps(self):
        """获取所有反应指纹"""
        return np.array([self.get_reaction_fp(i) for i in range(len(self.data))])

    def get_condition_features(self, idx):
        """获取反应条件特征"""
        item = self.data[idx]
        return np.array(
            item['solvent_fp'] + item['electrolyte_fp'] +
            [item['anode'], item['cathode'], item['cell_type'],
             item['electrolyte_label'], item['solvent_label'], item['reagent_label']]
        )

    def get_all_condition_features(self):
        """获取所有条件特征"""
        return np.array([self.get_condition_features(i) for i in range(len(self.data))])

    def get_full_features(self, idx):
        """获取完整特征（用于模型输入）"""
        item = self.data[idx]
        return (
            item['reactant_fp'] + item['product_fp'] + item['diff_fp'] +
            item['solvent_fp'] + item['electrolyte_fp'] +
            [item['anode'], item['cathode'], item['cell_type'],
             item['electrolyte_label'], item['solvent_label'], item['reagent_label']] +
            item['reactant_xtb'] + item['product_xtb'] +
            item['solvent_xtb'] + item['electrolyte_xtb'] + item['reaction_diff_xtb']
        )

    def set_cluster_labels(self, labels):
        self.cluster_labels = labels

    def __getitem__(self, idx):
        item = self.data[idx]
        full_features = self.get_full_features(idx)

        result = {
            'features': torch.tensor(full_features, dtype=torch.float32),
            'yield': torch.tensor(item['yield'] / 100.0, dtype=torch.float32),
            'yield_raw': item['yield'],
        }

        if self.cluster_labels is not None:
            result['cluster'] = self.cluster_labels[idx]

        return result


class YieldAwareClusterer:
    """产率感知聚类器"""

    def __init__(self, method='stratified', n_yield_bins=4, n_subclusters=2,
                 yield_weight=0.3, random_state=42):
        """
        Args:
            method: 聚类方法
                - 'stratified': 产率分层 + 特征子聚类
                - 'joint': 联合特征聚类（产率 + 反应特征）
                - 'hierarchical': 层次聚类（先产率后特征）
            n_yield_bins: 产率分层数量
            n_subclusters: 每个产率层的子聚类数
            yield_weight: 联合聚类时产率的权重
            random_state: 随机种子
        """
        self.method = method
        self.n_yield_bins = n_yield_bins
        self.n_subclusters = n_subclusters
        self.yield_weight = yield_weight
        self.random_state = random_state

        self.yield_bins = None
        self.sub_clusterers = {}
        self.scaler = StandardScaler()
        self.knn_classifier = None

    def _create_yield_bins(self, yields):
        """创建产率分箱（使用分位数确保每箱样本数相近）"""
        # 使用分位数分箱
        percentiles = np.linspace(0, 100, self.n_yield_bins + 1)
        self.yield_bins = np.percentile(yields, percentiles)
        # 确保边界
        self.yield_bins[0] = -0.1
        self.yield_bins[-1] = 100.1
        return self.yield_bins

    def _get_yield_bin(self, y):
        """获取产率所属的分箱"""
        for i in range(len(self.yield_bins) - 1):
            if self.yield_bins[i] <= y < self.yield_bins[i + 1]:
                return i
        return len(self.yield_bins) - 2

    def fit_stratified(self, reaction_fps, yields):
        """产率分层 + 特征子聚类"""
        n_samples = len(yields)
        labels = np.zeros(n_samples, dtype=int)

        # 创建产率分箱
        self._create_yield_bins(yields)
        yield_bin_labels = np.array([self._get_yield_bin(y) for y in yields])

        print(f"\n产率分层 (分位数分箱):")
        for i in range(self.n_yield_bins):
            bin_mask = yield_bin_labels == i
            count = bin_mask.sum()
            yield_range = (self.yield_bins[i], self.yield_bins[i + 1])
            print(f"  Bin {i}: 产率 [{yield_range[0]:.1f}, {yield_range[1]:.1f}), N={count}")

        # 对每个产率层进行子聚类
        cluster_id = 0
        self.sub_clusterers = {}

        print(f"\n在每个产率层内进行子聚类 (K={self.n_subclusters}):")
        for bin_idx in range(self.n_yield_bins):
            bin_mask = yield_bin_labels == bin_idx
            bin_indices = np.where(bin_mask)[0]

            if len(bin_indices) < self.n_subclusters * 10:
                # 样本太少，不分子聚类
                labels[bin_indices] = cluster_id
                print(f"  Bin {bin_idx}: 样本少，单一聚类 -> Cluster {cluster_id} (N={len(bin_indices)})")
                cluster_id += 1
                continue

            # 在这个产率层内进行 K-Means 聚类
            bin_fps = reaction_fps[bin_indices]
            kmeans = KMeans(n_clusters=self.n_subclusters, random_state=self.random_state, n_init=10)
            sub_labels = kmeans.fit_predict(bin_fps)

            self.sub_clusterers[bin_idx] = kmeans

            for sub_idx in range(self.n_subclusters):
                sub_mask = sub_labels == sub_idx
                sub_indices = bin_indices[sub_mask]
                labels[sub_indices] = cluster_id
                print(f"  Bin {bin_idx}, Sub {sub_idx} -> Cluster {cluster_id} (N={len(sub_indices)})")
                cluster_id += 1

        self.n_clusters = cluster_id
        return labels

    def fit_joint(self, reaction_fps, yields, condition_features=None):
        """联合特征聚类"""
        # 标准化反应指纹
        fps_scaled = self.scaler.fit_transform(reaction_fps)

        # 标准化产率并扩展权重
        yields_scaled = (yields - yields.mean()) / (yields.std() + 1e-8)
        yields_weighted = yields_scaled.reshape(-1, 1) * self.yield_weight * fps_scaled.shape[1]

        # 组合特征
        if condition_features is not None:
            cond_scaled = StandardScaler().fit_transform(condition_features)
            joint_features = np.hstack([fps_scaled, yields_weighted, cond_scaled * 0.5])
        else:
            joint_features = np.hstack([fps_scaled, yields_weighted])

        # K-Means 聚类
        n_clusters = self.n_yield_bins * self.n_subclusters
        self.joint_clusterer = KMeans(n_clusters=n_clusters, random_state=self.random_state, n_init=10)
        labels = self.joint_clusterer.fit_predict(joint_features)

        self.n_clusters = n_clusters
        self._joint_features_dim = joint_features.shape[1]

        # 打印聚类统计
        print(f"\n联合特征聚类 (K={n_clusters}, yield_weight={self.yield_weight}):")
        for c in range(n_clusters):
            mask = labels == c
            if mask.sum() > 0:
                c_yields = yields[mask]
                print(f"  Cluster {c}: N={mask.sum()}, 产率范围=[{c_yields.min():.1f}, {c_yields.max():.1f}], "
                      f"均值={c_yields.mean():.1f}, 标准差={c_yields.std():.1f}")

        return labels

    def fit_hierarchical(self, reaction_fps, yields):
        """层次聚类：先按产率分层，再在每层内用层次聚类"""
        n_samples = len(yields)
        labels = np.zeros(n_samples, dtype=int)

        # 创建产率分箱
        self._create_yield_bins(yields)
        yield_bin_labels = np.array([self._get_yield_bin(y) for y in yields])

        print(f"\n层次聚类 (产率分层 + AgglomerativeClustering):")

        cluster_id = 0
        self.sub_clusterers = {}

        for bin_idx in range(self.n_yield_bins):
            bin_mask = yield_bin_labels == bin_idx
            bin_indices = np.where(bin_mask)[0]

            if len(bin_indices) < self.n_subclusters * 5:
                labels[bin_indices] = cluster_id
                print(f"  Bin {bin_idx}: 样本少，单一聚类 -> Cluster {cluster_id} (N={len(bin_indices)})")
                cluster_id += 1
                continue

            # 使用层次聚类
            bin_fps = reaction_fps[bin_indices]
            agg = AgglomerativeClustering(n_clusters=self.n_subclusters, linkage='ward')
            sub_labels = agg.fit_predict(bin_fps)

            # 保存聚类中心（用于预测）
            centers = []
            for sub_idx in range(self.n_subclusters):
                sub_mask = sub_labels == sub_idx
                if sub_mask.sum() > 0:
                    centers.append(bin_fps[sub_mask].mean(axis=0))
                else:
                    centers.append(np.zeros(bin_fps.shape[1]))
            self.sub_clusterers[bin_idx] = np.array(centers)

            for sub_idx in range(self.n_subclusters):
                sub_mask = sub_labels == sub_idx
                sub_indices = bin_indices[sub_mask]
                if len(sub_indices) > 0:
                    labels[sub_indices] = cluster_id
                    c_yields = yields[sub_indices]
                    print(f"  Bin {bin_idx}, Sub {sub_idx} -> Cluster {cluster_id} "
                          f"(N={len(sub_indices)}, yield_std={c_yields.std():.2f})")
                    cluster_id += 1

        self.n_clusters = cluster_id
        return labels

    def fit(self, reaction_fps, yields, condition_features=None):
        """训练聚类器"""
        print(f"\n{'='*70}")
        print(f"产率感知聚类 (方法: {self.method})")
        print(f"{'='*70}")

        if self.method == 'stratified':
            labels = self.fit_stratified(reaction_fps, yields)
        elif self.method == 'joint':
            labels = self.fit_joint(reaction_fps, yields, condition_features)
        elif self.method == 'hierarchical':
            labels = self.fit_hierarchical(reaction_fps, yields)
        else:
            raise ValueError(f"Unknown method: {self.method}")

        # 训练 KNN 分类器用于预测新样本的聚类
        self.knn_classifier = KNeighborsClassifier(n_neighbors=5, weights='distance')
        self.knn_classifier.fit(reaction_fps, labels)

        # 保存训练数据的产率统计
        self.cluster_yield_stats = {}
        for c in range(self.n_clusters):
            mask = labels == c
            if mask.sum() > 0:
                c_yields = yields[mask]
                self.cluster_yield_stats[c] = {
                    'mean': float(c_yields.mean()),
                    'std': float(c_yields.std()),
                    'min': float(c_yields.min()),
                    'max': float(c_yields.max()),
                    'count': int(mask.sum())
                }

        return labels

    def predict(self, reaction_fps):
        """预测新样本的聚类标签"""
        return self.knn_classifier.predict(reaction_fps)


def train_single_model(model, train_loader, val_loader, device, args, cluster_id=None):
    """训练单个模型"""
    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs_per_cluster, eta_min=1e-6)
    criterion = nn.MSELoss()

    best_val_mae = float('inf')
    best_state = None
    patience_counter = 0

    for epoch in range(args.epochs_per_cluster):
        # Train
        model.train()
        train_loss = 0
        for batch in train_loader:
            features = batch['features'].to(device)
            labels = batch['yield'].to(device).unsqueeze(1)

            optimizer.zero_grad()
            pred = model(features)
            loss = criterion(pred, labels)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            train_loss += loss.item()

        # Validate
        model.eval()
        val_preds, val_labels = [], []
        with torch.no_grad():
            for batch in val_loader:
                features = batch['features'].to(device)
                labels = batch['yield'].to(device)
                pred = model(features).squeeze()
                val_preds.extend((pred * 100).cpu().tolist())
                val_labels.extend((labels * 100).cpu().tolist())

        val_preds = np.array(val_preds)
        val_labels = np.array(val_labels)
        val_mae = np.mean(np.abs(val_preds - val_labels))

        if val_mae < best_val_mae:
            best_val_mae = val_mae
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            patience_counter = 0
        else:
            patience_counter += 1

        scheduler.step()

        if patience_counter >= args.patience_per_cluster:
            break

    if best_state is not None:
        model.load_state_dict(best_state)

    return best_val_mae


def evaluate_model(models, test_dataset, test_labels, device, args):
    """评估模型"""
    all_preds = []
    all_labels = []
    cluster_metrics = {}

    n_clusters = max(test_labels) + 1

    for c in range(n_clusters):
        test_indices = [i for i in range(len(test_dataset)) if test_labels[i] == c]

        if len(test_indices) == 0 or c not in models:
            continue

        test_subset = Subset(test_dataset, test_indices)
        test_loader = DataLoader(test_subset, batch_size=args.batch_size*2, shuffle=False, num_workers=2)

        model = models[c]
        model.eval()

        cluster_preds = []
        cluster_labels = []

        with torch.no_grad():
            for batch in test_loader:
                features = batch['features'].to(device)
                labels = batch['yield'].to(device)
                pred = model(features).squeeze()

                if pred.dim() == 0:
                    cluster_preds.append((pred * 100).cpu().item())
                    cluster_labels.append((labels * 100).cpu().item())
                else:
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
            r2 = 0

        cluster_metrics[c] = {
            'count': len(test_indices),
            'mae': mae,
            'r2': r2,
            'yield_mean': labels_arr.mean(),
            'yield_std': labels_arr.std()
        }
        print(f"  Cluster {c}: N={len(test_indices):3d}, MAE={mae:.2f}%, R²={r2:.4f}, "
              f"产率=[{labels_arr.min():.1f}, {labels_arr.max():.1f}]")

    # 总体指标
    all_preds = np.array(all_preds)
    all_labels = np.array(all_labels)

    total_mae = np.mean(np.abs(all_preds - all_labels))
    total_rmse = np.sqrt(np.mean((all_preds - all_labels)**2))
    ss_res = np.sum((all_preds - all_labels)**2)
    ss_tot = np.sum((all_labels - all_labels.mean())**2)
    total_r2 = 1 - ss_res / ss_tot

    return {
        'mae': total_mae,
        'rmse': total_rmse,
        'r2': total_r2,
        'cluster_metrics': cluster_metrics,
        'predictions': all_preds,
        'labels': all_labels
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default=str(project_root / 'data'))
    parser.add_argument('--output_dir', type=str, default=str(project_root / 'checkpoints' / 'yield_aware_cluster'))

    # 聚类参数
    parser.add_argument('--cluster_method', type=str, default='stratified',
                        choices=['stratified', 'joint', 'hierarchical'],
                        help='聚类方法')
    parser.add_argument('--n_yield_bins', type=int, default=4, help='产率分层数量')
    parser.add_argument('--n_subclusters', type=int, default=2, help='每层子聚类数')
    parser.add_argument('--yield_weight', type=float, default=0.3, help='联合聚类时产率权重')

    # 模型参数
    parser.add_argument('--hidden_dims', type=str, default='512,256,128')
    parser.add_argument('--dropout', type=float, default=0.3)
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--weight_decay', type=float, default=1e-4)
    parser.add_argument('--epochs_per_cluster', type=int, default=100)
    parser.add_argument('--patience_per_cluster', type=int, default=15)
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    hidden_dims = [int(x) for x in args.hidden_dims.split(',')]
    device = torch.device(args.device)
    print(f"Device: {device}")

    # 创建输出目录
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    data_dir = Path(args.data_dir)

    # 加载数据
    print("\n" + "=" * 70)
    print("加载数据...")
    print("=" * 70)

    train_dataset = YieldAwareDataset(data_dir / 'train_xtb_cat.pt')
    val_dataset = YieldAwareDataset(data_dir / 'val_xtb_cat.pt')
    test_dataset = YieldAwareDataset(data_dir / 'test_xtb_cat.pt')

    print(f"  Train: {len(train_dataset)}, Val: {len(val_dataset)}, Test: {len(test_dataset)}")

    # 获取特征和产率
    train_fps = train_dataset.get_all_reaction_fps()
    train_yields = train_dataset.get_all_yields()
    train_conditions = train_dataset.get_all_condition_features()

    val_fps = val_dataset.get_all_reaction_fps()
    val_yields = val_dataset.get_all_yields()

    test_fps = test_dataset.get_all_reaction_fps()
    test_yields = test_dataset.get_all_yields()

    # 产率分布统计
    print(f"\n产率分布:")
    print(f"  Train: 均值={train_yields.mean():.2f}, 标准差={train_yields.std():.2f}, "
          f"范围=[{train_yields.min():.1f}, {train_yields.max():.1f}]")

    # 创建聚类器并聚类
    clusterer = YieldAwareClusterer(
        method=args.cluster_method,
        n_yield_bins=args.n_yield_bins,
        n_subclusters=args.n_subclusters,
        yield_weight=args.yield_weight,
        random_state=args.seed
    )

    if args.cluster_method == 'joint':
        train_labels = clusterer.fit(train_fps, train_yields, train_conditions)
    else:
        train_labels = clusterer.fit(train_fps, train_yields)

    train_dataset.set_cluster_labels(train_labels)

    # 预测验证集和测试集的聚类
    val_labels = clusterer.predict(val_fps)
    val_dataset.set_cluster_labels(val_labels)

    test_labels = clusterer.predict(test_fps)
    test_dataset.set_cluster_labels(test_labels)

    # 聚类分布统计
    print(f"\n聚类分布统计:")
    for c in range(clusterer.n_clusters):
        train_count = (train_labels == c).sum()
        val_count = (val_labels == c).sum()
        test_count = (test_labels == c).sum()
        stats = clusterer.cluster_yield_stats.get(c, {})
        print(f"  Cluster {c}: Train={train_count:4d}, Val={val_count:3d}, Test={test_count:3d}, "
              f"产率均值={stats.get('mean', 0):.1f}±{stats.get('std', 0):.1f}")

    # 为每个聚类训练独立模型
    print("\n" + "=" * 70)
    print("为每个聚类训练独立模型...")
    print("=" * 70)

    models = {}
    cluster_train_metrics = {}
    start_time = datetime.now()

    for c in range(clusterer.n_clusters):
        print(f"\n--- Cluster {c} ---")

        train_indices = [i for i in range(len(train_dataset)) if train_labels[i] == c]
        val_indices = [i for i in range(len(val_dataset)) if val_labels[i] == c]

        if len(train_indices) < 10:
            print(f"  训练样本太少 ({len(train_indices)}), 跳过")
            continue

        if len(val_indices) < 3:
            # 如果验证集太小，从训练集中分一部分
            print(f"  验证集太小 ({len(val_indices)}), 从训练集分割")
            np.random.shuffle(train_indices)
            split = max(len(train_indices) - 20, int(len(train_indices) * 0.8))
            val_indices = train_indices[split:]
            train_indices = train_indices[:split]

        train_subset = Subset(train_dataset, train_indices)
        val_subset = Subset(val_dataset, val_indices) if len(val_indices) >= 3 else Subset(train_dataset, val_indices)

        train_loader = DataLoader(train_subset, batch_size=args.batch_size, shuffle=True, num_workers=2)
        val_loader = DataLoader(val_subset, batch_size=args.batch_size*2, shuffle=False, num_workers=2)

        # 创建模型
        model = SimpleYieldPredictor(
            input_dim=10301,
            hidden_dims=hidden_dims,
            dropout=args.dropout
        ).to(device)

        num_params = sum(p.numel() for p in model.parameters())
        stats = clusterer.cluster_yield_stats.get(c, {})
        print(f"  Train: {len(train_indices)}, Val: {len(val_indices)}, Params: {num_params:,}")
        print(f"  产率范围: [{stats.get('min', 0):.1f}, {stats.get('max', 0):.1f}], 均值: {stats.get('mean', 0):.1f}")

        best_mae = train_single_model(model, train_loader, val_loader, device, args, cluster_id=c)
        print(f"  Best Val MAE: {best_mae:.2f}%")

        models[c] = model
        cluster_train_metrics[c] = {
            'train_count': len(train_indices),
            'val_count': len(val_indices),
            'val_mae': best_mae
        }

    elapsed_train = datetime.now() - start_time
    print(f"\n训练完成，耗时: {elapsed_train}")

    # 测试
    print("\n" + "=" * 70)
    print("在测试集上评估")
    print("=" * 70)

    test_results = evaluate_model(models, test_dataset, test_labels, device, args)

    print(f"\n总体测试结果:")
    print(f"  Test MAE:  {test_results['mae']:.2f}%")
    print(f"  Test RMSE: {test_results['rmse']:.2f}%")
    print(f"  Test R²:   {test_results['r2']:.4f}")

    # 与基线比较
    baseline_r2 = 0.363
    baseline_mae = 12.43
    r2_imp = test_results['r2'] - baseline_r2
    mae_imp = baseline_mae - test_results['mae']

    print(f"\n与基线比较 (MLP+xTB: R²=0.363, MAE=12.43%):")
    print(f"  R² 变化: {r2_imp:+.4f} ({baseline_r2:.3f} → {test_results['r2']:.3f})")
    print(f"  MAE 变化: {mae_imp:+.2f}% ({baseline_mae:.2f}% → {test_results['mae']:.2f}%)")

    if r2_imp > 0 and mae_imp > 0:
        print(f"\n🎉 成功超越基线! R² 提升 {r2_imp:.4f}, MAE 降低 {mae_imp:.2f}%")
    elif r2_imp > 0:
        print(f"\n✅ R² 提升 {r2_imp:.4f}，但 MAE 上升 {-mae_imp:.2f}%")
    else:
        print(f"\n未超越基线")

    # 保存模型和结果
    for c, model in models.items():
        torch.save({
            'model_state_dict': model.state_dict(),
            'cluster_id': c,
            'cluster_stats': clusterer.cluster_yield_stats.get(c, {}),
        }, output_dir / f'model_cluster_{c}.pt')

    # 保存聚类器
    import pickle
    with open(output_dir / 'clusterer.pkl', 'wb') as f:
        pickle.dump(clusterer, f)

    # 保存结果
    results = {
        'model': 'YieldAwareClusterPredictor',
        'cluster_method': args.cluster_method,
        'n_yield_bins': args.n_yield_bins,
        'n_subclusters': args.n_subclusters,
        'n_clusters': clusterer.n_clusters,
        'test_mae': float(test_results['mae']),
        'test_rmse': float(test_results['rmse']),
        'test_r2': float(test_results['r2']),
        'r2_improvement': float(r2_imp),
        'mae_improvement': float(mae_imp),
        'cluster_test_metrics': {str(k): v for k, v in test_results['cluster_metrics'].items()},
        'cluster_yield_stats': clusterer.cluster_yield_stats,
        'training_time': str(elapsed_train),
        'args': vars(args),
    }

    with open(output_dir / 'results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n结果已保存到: {output_dir}")

    return results


if __name__ == "__main__":
    main()
