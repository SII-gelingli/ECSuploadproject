"""Stage-1 GNN 训练: 用 MolecularGNN 替代 Morgan FP。

数据: data_audited_v3/{train,val,test}.pt 里已有 reactant_smiles / product_smiles
图特征 on-the-fly 计算 (并缓存到内存) — 不需要预生成 .pt
"""
import sys
import json
import argparse
from pathlib import Path
from collections import Counter
from datetime import datetime

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm
from rdkit import RDLogger
RDLogger.logger().setLevel(RDLogger.ERROR)

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.condition_stage1_gnn import ConditionStage1GNN
from models.condition_stage1 import HEAD_KEYS
from utils.graph_features import smiles_list_to_graph, get_dummy_graph

DATA_DIR = project_root / 'data_audited_v3'
CKPT_DIR = project_root / 'checkpoints' / 'two_stage'
CKPT_DIR.mkdir(parents=True, exist_ok=True)


class GNNStage1Dataset(Dataset):
    def __init__(self, records, extra_keys=None):
        self.records = records
        self.extra_keys = list(extra_keys or [])
        # 预计算图: 慢但只跑一次
        print(f"  预计算分子图 ({len(records)} 反应) ...")
        self.r_graphs, self.p_graphs = [], []
        for r in tqdm(records, desc="building graphs"):
            r_smi = r.get('reactant_smiles', [])
            p_smi = r.get('product_smiles', [])
            self.r_graphs.append(smiles_list_to_graph([s for s in r_smi if s]) if r_smi else get_dummy_graph())
            self.p_graphs.append(smiles_list_to_graph([s for s in p_smi if s]) if p_smi else get_dummy_graph())

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        r = self.records[idx]
        all_keys = list(HEAD_KEYS) + self.extra_keys
        return {
            'r_graph': self.r_graphs[idx] or get_dummy_graph(),
            'p_graph': self.p_graphs[idx] or get_dummy_graph(),
            'labels': {k: r['labels'].get(k, 0) for k in all_keys},
            'yield': float(r.get('yield', 0.0) or 0.0) / 100.0,
        }


def merge_graphs(graphs):
    all_nodes, all_edges, all_edge_feats, batch_idx = [], [], [], []
    node_offset = 0
    for i, g in enumerate(graphs):
        if g is None:
            g = get_dummy_graph()
        nodes = g['node_feats']
        edges = g['edge_index']
        edge_feats = g['edge_feats']
        all_nodes.append(nodes)
        if edges.shape[1] > 0:
            all_edges.append(edges + node_offset)
            all_edge_feats.append(edge_feats)
        batch_idx.extend([i] * nodes.shape[0])
        node_offset += nodes.shape[0]
    return {
        'node_feats': torch.cat(all_nodes, dim=0),
        'edge_index': torch.cat(all_edges, dim=1) if all_edges else torch.zeros(2, 0, dtype=torch.long),
        'edge_feats': torch.cat(all_edge_feats, dim=0) if all_edge_feats else torch.zeros(0, 10),
        'batch': torch.tensor(batch_idx, dtype=torch.long),
        'num_graphs': len(graphs),
    }


def collate_fn(batch):
    rg = merge_graphs([d['r_graph'] for d in batch])
    pg = merge_graphs([d['p_graph'] for d in batch])
    item = {'r_graph': rg, 'p_graph': pg,
            'yield': torch.tensor([d['yield'] for d in batch], dtype=torch.float32)}
    # 自动收集 batch 里所有 labels keys (含 extra)
    all_keys = list(batch[0]['labels'].keys())
    for k in all_keys:
        item[k] = torch.tensor([d['labels'][k] for d in batch], dtype=torch.long)
    return item


def graph_to_device(g, device):
    return {
        'node_feats': g['node_feats'].to(device),
        'edge_index': g['edge_index'].to(device),
        'edge_feats': g['edge_feats'].to(device),
        'batch': g['batch'].to(device),
        'num_graphs': g['num_graphs'],
    }


def compute_class_weights(records, num_classes):
    weights = {}
    for k in HEAD_KEYS:
        cnt = Counter([r['labels'][k] for r in records])
        n = num_classes[k]
        w = np.zeros(n, dtype=np.float32)
        for i in range(n):
            w[i] = 1.0 / np.sqrt(cnt.get(i, 0) + 1)
        # 均值归一化到 1
        w *= n / w.sum()
        weights[k] = torch.from_numpy(w)
    return weights


def topk_accuracy(logits, targets, ks=(1, 3, 5)):
    maxk = min(max(ks), logits.size(-1))
    _, pred = logits.topk(maxk, dim=-1)
    pred = pred.t()
    correct = pred.eq(targets.view(1, -1).expand_as(pred))
    out = {}
    for k in ks:
        if k <= maxk:
            out[f'top{k}'] = int(correct[:k].any(dim=0).float().sum().item())
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=40)
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--lr', type=float, default=3e-4)
    parser.add_argument('--dropout', type=float, default=0.2)
    parser.add_argument('--gnn_hidden', type=int, default=128)
    parser.add_argument('--gnn_layers', type=int, default=3)
    parser.add_argument('--gnn_heads', type=int, default=4)
    parser.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--label_smoothing', type=float, default=0.05)
    parser.add_argument('--num_workers', type=int, default=4)
    parser.add_argument('--use_reagent_class', action='store_true',
                        help='加 reagent_class (47 类) 辅助 head')
    args = parser.parse_args()

    print(f"device={args.device}, epochs={args.epochs}, batch={args.batch_size}, lr={args.lr}")
    print(f"GNN: hidden={args.gnn_hidden}, layers={args.gnn_layers}, heads={args.gnn_heads}")
    print(f"timestamp={datetime.now().isoformat()}")

    print("Loading data ...")
    train_records = torch.load(DATA_DIR / 'train.pt', weights_only=False)
    val_records = torch.load(DATA_DIR / 'val.pt', weights_only=False)
    stats = json.loads((DATA_DIR / 'stats.json').read_text())
    nc = stats['num_classes']
    print(f"train={len(train_records)}, val={len(val_records)}, num_classes={nc}")

    extra_keys = ['reagent_class'] if args.use_reagent_class else []
    train_ds = GNNStage1Dataset(train_records, extra_keys=extra_keys)
    val_ds = GNNStage1Dataset(val_records, extra_keys=extra_keys)
    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True,
                               num_workers=args.num_workers, collate_fn=collate_fn, drop_last=True)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False,
                             num_workers=args.num_workers, collate_fn=collate_fn)

    all_train_heads = list(HEAD_KEYS) + extra_keys

    print("Computing class weights ...")
    class_weights = {k: w.to(args.device) for k, w in compute_class_weights(train_records, nc).items()}
    if args.use_reagent_class:
        cnt = Counter([r['labels'].get('reagent_class', 0) for r in train_records])
        n_rc = nc['reagent_class']
        w = np.zeros(n_rc, dtype=np.float32)
        for i in range(n_rc):
            w[i] = 1.0 / np.sqrt(cnt.get(i, 0) + 1)
        w *= n_rc / w.sum()
        class_weights['reagent_class'] = torch.from_numpy(w).to(args.device)

    model = ConditionStage1GNN(num_classes=nc, gnn_hidden=args.gnn_hidden,
                                gnn_layers=args.gnn_layers, gnn_heads=args.gnn_heads,
                                dropout=args.dropout,
                                extra_heads=extra_keys).to(args.device)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"Model params: {n_params/1e6:.1f}M, extra_heads={extra_keys}")

    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    head_criterion = {}
    for k in all_train_heads:
        ls = args.label_smoothing if nc[k] > 50 else 0.0
        head_criterion[k] = nn.CrossEntropyLoss(weight=class_weights[k],
                                                  label_smoothing=ls, reduction='none')

    def eval_split(loader, name):
        model.eval()
        sums = {k: {f'top{kv}': 0.0 for kv in (1, 3, 5)} for k in HEAD_KEYS}
        n = 0
        joint_top1 = 0
        with torch.no_grad():
            for batch in tqdm(loader, desc=f"eval {name}", leave=False):
                rg = graph_to_device(batch['r_graph'], args.device)
                pg = graph_to_device(batch['p_graph'], args.device)
                logits = model(rg, pg)
                bsz = batch['yield'].size(0); n += bsz
                per_head_correct = []
                for k in HEAD_KEYS:
                    tgt = batch[k].to(args.device)
                    res = topk_accuracy(logits[k], tgt, ks=(1, 3, 5))
                    for kk in res:
                        sums[k][kk] += res[kk]
                    pred1 = logits[k].argmax(dim=-1)
                    per_head_correct.append(pred1 == tgt)
                joint = torch.stack(per_head_correct, dim=0).all(dim=0)
                joint_top1 += int(joint.sum())
        report = {k: {kk: round(sums[k][kk] / n, 4) for kk in sums[k]} for k in HEAD_KEYS}
        avg = {kk: round(np.mean([report[k][kk] for k in HEAD_KEYS]), 4) for kk in ('top1', 'top3', 'top5')}
        joint = round(joint_top1 / n, 4)
        print(f"\n[{name}] Top-1/3/5  (joint Top-1 = {joint:.4f})")
        print(f"  {'head':<13} {'Top1':>7} {'Top3':>7} {'Top5':>7}")
        for k in HEAD_KEYS:
            r = report[k]
            print(f"  {k:<13} {r['top1']:7.4f} {r['top3']:7.4f} {r['top5']:7.4f}")
        print(f"  {'AVG':<13} {avg['top1']:7.4f} {avg['top3']:7.4f} {avg['top5']:7.4f}")
        return report, avg, joint

    best_avg_top1 = 0.0
    best_epoch = -1
    history = []
    for epoch in range(1, args.epochs + 1):
        model.train()
        running = 0.0
        n_batches = 0
        pbar = tqdm(train_loader, desc=f"Epoch {epoch}/{args.epochs}")
        for batch in pbar:
            rg = graph_to_device(batch['r_graph'], args.device)
            pg = graph_to_device(batch['p_graph'], args.device)
            logits = model(rg, pg)
            total_loss = 0.0
            for k in all_train_heads:
                if k not in logits:
                    continue
                tgt = batch[k].to(args.device)
                ce = head_criterion[k](logits[k], tgt)
                total_loss = total_loss + ce.mean()
            optimizer.zero_grad()
            total_loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            running += float(total_loss.detach())
            n_batches += 1
            pbar.set_postfix(loss=f"{total_loss.item():.4f}")
        scheduler.step()
        train_loss = running / max(1, n_batches)
        print(f"Epoch {epoch}: train_loss={train_loss:.4f}  lr={optimizer.param_groups[0]['lr']:.2e}")
        report, avg, joint = eval_split(val_loader, name='VAL')
        history.append({'epoch': epoch, 'train_loss': train_loss,
                         'val_avg_top1': avg['top1'], 'val_joint_top1': joint})
        if avg['top1'] > best_avg_top1:
            best_avg_top1 = avg['top1']
            best_epoch = epoch
            torch.save({
                'model_state_dict': model.state_dict(),
                'num_classes': nc,
                'gnn_hidden': args.gnn_hidden,
                'gnn_layers': args.gnn_layers,
                'gnn_heads': args.gnn_heads,
                'dropout': args.dropout,
                'use_gnn': True,
                'use_reagent_class': args.use_reagent_class,
                'epoch': epoch,
                'val_avg_top1': avg['top1'],
                'val_joint_top1': joint,
            }, CKPT_DIR / 'stage1_best.pt')
            print(f"  -> Saved best (val avg Top-1 = {avg['top1']:.4f})")

    history_out = {'best_epoch': best_epoch, 'best_val_top1': best_avg_top1, 'history': history}
    json.dump(history_out, open(CKPT_DIR / 'stage1_history.json', 'w'), indent=2)
    print(f"\nFinished. Best epoch = {best_epoch}, val avg Top-1 = {best_avg_top1:.4f}")


if __name__ == "__main__":
    main()
