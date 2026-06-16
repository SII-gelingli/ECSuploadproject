"""
分段产率预测模型：先聚类，再为每个聚类训练独立模型

策略：
1. 使用 K-Means 对反应指纹进行聚类
2. 为每个聚类训练一个独立的小型 MLP
3. 推理时先判断聚类，再用对应模型预测

优点：
- 每个模型只需要学习一类反应的规律
- 完全避免不同类型反应之间的干扰
- 模型更小，不容易过拟合
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
from sklearn.neighbors import KNeighborsClassifier

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


class ClusteredYieldDataset(Dataset):
    """带聚类标签的数据集"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path, weights_only=False)
        self.cluster_labels = None

    def __len__(self):
        return len(self.data)

    def get_reaction_fp(self, idx):
        """获取反应指纹（用于聚类）"""
        item = self.data[idx]
        return np.array(item['reactant_fp'] + item['product_fp'] + item['diff_fp'])

    def get_all_reaction_fps(self):
        """获取所有反应指纹"""
        fps = []
        for i in range(len(self.data)):
            fps.append(self.get_reaction_fp(i))
        return np.array(fps)

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

        result = {
            'features': torch.tensor(full_features, dtype=torch.float32),
            'yield': torch.tensor(item['yield'] / 100.0, dtype=torch.float32),
            'reaction_fp': torch.tensor(self.get_reaction_fp(idx), dtype=torch.float32),
        }

        if self.cluster_labels is not None:
            result['cluster'] = self.cluster_labels[idx]

        return result


def train_single_model(model, train_loader, val_loader, device, args):
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
        for batch in train_loader:
            features = batch['features'].to(device)
            labels = batch['yield'].to(device).unsqueeze(1)

            optimizer.zero_grad()
            pred = model(features)
            loss = criterion(pred, labels)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()

        # Validate
        model.eval()
        val_preds, val_labels = [], []
        with torch.no_grad():
            for batch in val_loader:
                features = batch['features'].to(device)
                labels = batch['yield'].to(device)
                pred = model(features).squeeze()
                pred_list = (pred * 100).cpu().flatten().tolist()
                label_list = (labels * 100).cpu().flatten().tolist()
                val_preds.extend(pred_list if isinstance(pred_list, list) else [pred_list])
                val_labels.extend(label_list if isinstance(label_list, list) else [label_list])

        val_mae = np.mean(np.abs(np.array(val_preds) - np.array(val_labels)))

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default=str(project_root / 'data'))
    parser.add_argument('--output_dir', type=str, default=str(project_root / 'checkpoints' / 'clustered_yield'))
    parser.add_argument('--num_clusters', type=int, default=4)
    parser.add_argument('--hidden_dims', type=str, default='256,128')
    parser.add_argument('--dropout', type=float, default=0.3)
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--weight_decay', type=float, default=1e-4)
    parser.add_argument('--epochs_per_cluster', type=int, default=50)
    parser.add_argument('--patience_per_cluster', type=int, default=10)
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    hidden_dims = [int(x) for x in args.hidden_dims.split(',')]
    device = torch.device(args.device)
    print(f"Device: {device}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    data_dir = Path(args.data_dir)

    # 加载数据
    print("\n" + "=" * 70)
    print("加载数据...")
    print("=" * 70)

    train_dataset = ClusteredYieldDataset(data_dir / 'train_xtb_cat.pt')
    val_dataset = ClusteredYieldDataset(data_dir / 'val_xtb_cat.pt')
    test_dataset = ClusteredYieldDataset(data_dir / 'test_xtb_cat.pt')

    print(f"  Train: {len(train_dataset)}, Val: {len(val_dataset)}, Test: {len(test_dataset)}")

    # K-Means 聚类
    print("\n" + "=" * 70)
    print(f"K-Means 聚类 (K={args.num_clusters})...")
    print("=" * 70)

    train_fps = train_dataset.get_all_reaction_fps()
    kmeans = KMeans(n_clusters=args.num_clusters, random_state=args.seed, n_init=10)
    train_labels = kmeans.fit_predict(train_fps)
    train_dataset.set_cluster_labels(train_labels)

    # 使用 KNN 对验证集和测试集分配聚类
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(train_fps, train_labels)

    val_fps = val_dataset.get_all_reaction_fps()
    val_labels = knn.predict(val_fps)
    val_dataset.set_cluster_labels(val_labels)

    test_fps = test_dataset.get_all_reaction_fps()
    test_labels = knn.predict(test_fps)
    test_dataset.set_cluster_labels(test_labels)

    # 聚类分布统计
    print("\n聚类分布:")
    for c in range(args.num_clusters):
        train_count = (train_labels == c).sum()
        val_count = (val_labels == c).sum()
        test_count = (test_labels == c).sum()
        print(f"  Cluster {c}: Train={train_count}, Val={val_count}, Test={test_count}")

    # 为每个聚类训练独立模型
    print("\n" + "=" * 70)
    print("为每个聚类训练独立模型...")
    print("=" * 70)

    models = {}
    cluster_metrics = {}

    start_time = datetime.now()

    for c in range(args.num_clusters):
        print(f"\n--- Cluster {c} ---")

        # 获取该聚类的数据子集
        train_indices = [i for i in range(len(train_dataset)) if train_labels[i] == c]
        val_indices = [i for i in range(len(val_dataset)) if val_labels[i] == c]

        if len(train_indices) < 10 or len(val_indices) < 5:
            print(f"  样本太少，跳过")
            continue

        train_subset = Subset(train_dataset, train_indices)
        val_subset = Subset(val_dataset, val_indices)

        train_loader = DataLoader(train_subset, batch_size=args.batch_size, shuffle=True, num_workers=2)
        val_loader = DataLoader(val_subset, batch_size=args.batch_size*2, shuffle=False, num_workers=2)

        # 创建并训练模型
        model = SimpleYieldPredictor(
            input_dim=10301,
            hidden_dims=hidden_dims,
            dropout=args.dropout
        ).to(device)

        num_params = sum(p.numel() for p in model.parameters())
        print(f"  Train: {len(train_indices)}, Val: {len(val_indices)}, Params: {num_params:,}")

        best_mae = train_single_model(model, train_loader, val_loader, device, args)
        print(f"  Best Val MAE: {best_mae:.2f}%")

        models[c] = model
        cluster_metrics[c] = {'train_count': len(train_indices), 'val_mae': best_mae}

    elapsed_train = datetime.now() - start_time
    print(f"\n训练完成，耗时: {elapsed_train}")

    # 测试
    print("\n" + "=" * 70)
    print("在测试集上评估")
    print("=" * 70)

    all_preds = []
    all_labels = []
    cluster_test_metrics = {}

    for c in range(args.num_clusters):
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
                cluster_preds.extend((pred * 100).cpu().tolist())
                cluster_labels.extend((labels * 100).cpu().tolist())

        all_preds.extend(cluster_preds)
        all_labels.extend(cluster_labels)

        preds_arr = np.array(cluster_preds)
        labels_arr = np.array(cluster_labels)
        mae = np.mean(np.abs(preds_arr - labels_arr))
        r2 = 1 - np.sum((preds_arr - labels_arr)**2) / np.sum((labels_arr - labels_arr.mean())**2)

        cluster_test_metrics[c] = {'count': len(test_indices), 'mae': mae, 'r2': r2}
        print(f"  Cluster {c}: N={len(test_indices)}, MAE={mae:.2f}%, R²={r2:.4f}")

    # 总体指标
    all_preds = np.array(all_preds)
    all_labels = np.array(all_labels)

    total_mae = np.mean(np.abs(all_preds - all_labels))
    total_rmse = np.sqrt(np.mean((all_preds - all_labels)**2))
    ss_res = np.sum((all_preds - all_labels)**2)
    ss_tot = np.sum((all_labels - all_labels.mean())**2)
    total_r2 = 1 - ss_res / ss_tot

    print(f"\n总体测试结果:")
    print(f"  Test MAE:  {total_mae:.2f}%")
    print(f"  Test RMSE: {total_rmse:.2f}%")
    print(f"  Test R²:   {total_r2:.4f}")

    baseline_r2 = 0.363
    baseline_mae = 12.43
    r2_imp = total_r2 - baseline_r2
    mae_imp = baseline_mae - total_mae

    print(f"\n与基线比较:")
    print(f"  R² 变化: {r2_imp:+.4f} ({baseline_r2:.3f} → {total_r2:.3f})")
    print(f"  MAE 变化: {mae_imp:+.2f}% ({baseline_mae:.2f}% → {total_mae:.2f}%)")

    if r2_imp > 0:
        print(f"\n🎉 成功超越基线! R² 提升 {r2_imp:.4f}")
    else:
        print(f"\n未超越基线")

    # 保存模型和结果
    for c, model in models.items():
        torch.save({
            'model_state_dict': model.state_dict(),
            'cluster_id': c,
        }, output_dir / f'model_cluster_{c}.pt')

    # 保存聚类器
    import pickle
    with open(output_dir / 'kmeans.pkl', 'wb') as f:
        pickle.dump(kmeans, f)
    with open(output_dir / 'knn.pkl', 'wb') as f:
        pickle.dump(knn, f)

    results = {
        'model': 'ClusteredYieldPredictor',
        'num_clusters': args.num_clusters,
        'test_mae': total_mae,
        'test_rmse': total_rmse,
        'test_r2': total_r2,
        'r2_improvement': r2_imp,
        'mae_improvement': mae_imp,
        'cluster_test_metrics': {str(k): v for k, v in cluster_test_metrics.items()},
        'training_time': str(elapsed_train),
        'args': vars(args),
    }

    with open(output_dir / 'results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n结果已保存到: {output_dir}")
    return results


if __name__ == "__main__":
    main()
