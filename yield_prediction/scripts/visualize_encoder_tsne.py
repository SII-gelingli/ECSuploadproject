"""跑 t-SNE 把 encoder 输出 (512D) 压到 2D, 按化学属性染色看聚类."""
import sys, json
from pathlib import Path

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
):
    if _p not in sys.path: sys.path.insert(0, _p)

import numpy as np
import torch
from torch.utils.data import DataLoader
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.condition_stage1_hier_set_v3 import ConditionStage1HierSetV3
from scripts.train_stage1_hier_set_v3 import HierSetV3Dataset, collate_fn

DATA_DIR = project_root / 'data_audited_v3_clean'
CKPT = project_root / 'checkpoints/two_stage/stage1_hier_set_v3_smi_fineE.pt'
OUT_DIR = project_root / 'checkpoints/two_stage/experiments/encoder_tsne'
OUT_DIR.mkdir(parents=True, exist_ok=True)


def encoder_forward(model, fp):
    """Run only the encoder MLP, get 512D output."""
    with torch.no_grad():
        return model.encoder(fp)


def main():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'Loading test data + model')
    test = torch.load(DATA_DIR / 'test.pt', weights_only=False)
    stats = json.load(open(DATA_DIR / 'stats.json'))
    vocab = json.load(open(DATA_DIR / 'vocab.json'))
    nc = stats['num_classes']; nc_v3 = stats['num_classes_v3']

    name_maps = {}
    for h in ['solvent', 'electrolyte', 'catalyst', 'reagent', 'ligand', 'additive']:
        if h in vocab: name_maps[h] = {v: k for k, v in vocab[h].items()}
    for h, names in vocab.get('__v3__', {}).items():
        name_maps[h] = {i: n for i, n in enumerate(names)}

    model = ConditionStage1HierSetV3(
        num_classes=nc, num_classes_v3=nc_v3, fp_dim=6144,
        hidden_dims=(1024, 768, 512), dropout=0.3, class_embed_dim=32,
    ).to(device)
    ckpt = torch.load(CKPT, map_location=device, weights_only=False)
    model.load_state_dict(ckpt['model_state_dict']); model.eval()

    # 跑 encoder
    print(f'Encoding {len(test)} test reactions ...')
    coll = lambda b: collate_fn(b, nc)
    loader = DataLoader(HierSetV3Dataset(test), batch_size=128, shuffle=False,
                        num_workers=2, collate_fn=coll)
    all_embeddings = []
    all_labels = {h: [] for h in ['anode_material', 'cathode_material', 'cell_class_v3',
                                    'electrolyte_cation', 'electrolyte_anion',
                                    'catalyst_class_v3', 'solvent_class_v3', 'reagent_class_v3',
                                    'anode_fine']}
    all_yields = []
    with torch.no_grad():
        for batch in loader:
            fp = batch['fp'].to(device)
            emb = encoder_forward(model, fp).cpu().numpy()
            all_embeddings.append(emb)
            for h in all_labels:
                all_labels[h].extend(batch[h].numpy().tolist())
    for r in test:
        all_yields.append(r.get('yield'))
    X = np.vstack(all_embeddings)  # (N, 512)
    print(f'  Embedding shape: {X.shape}')

    # PCA 先降到 50D, t-SNE 再降到 2D (t-SNE 在高维直接跑慢)
    print('PCA 50 → t-SNE 2D ...')
    Xp = PCA(n_components=50, random_state=42).fit_transform(X)
    Xt = TSNE(n_components=2, perplexity=30, max_iter=1000, random_state=42, init='pca').fit_transform(Xp)
    print(f'  t-SNE shape: {Xt.shape}')

    # 按多种属性染色
    panels = [
        ('anode_material', 'Anode material (15 classes)'),
        ('cathode_material', 'Cathode material (15 classes)'),
        ('cell_class_v3', 'Cell type (4 classes)'),
        ('catalyst_class_v3', 'Catalyst class (49 classes)'),
        ('solvent_class_v3', 'Solvent class (27 classes)'),
        ('reagent_class_v3', 'Reagent class (103 classes)'),
        ('electrolyte_cation', 'Electrolyte cation (23 classes)'),
        ('anode_fine', 'Anode fine (43 classes)'),
    ]
    fig, axes = plt.subplots(2, 4, figsize=(28, 12))
    for ax, (head, title) in zip(axes.flat, panels):
        labels = np.array(all_labels[head])
        name_map = name_maps.get(head, {})
        # 只画 Top-N 类, 其他归 '其他' 一类
        from collections import Counter
        cnt = Counter(labels.tolist())
        TOP_N = 10
        top_classes = [c for c, _ in cnt.most_common(TOP_N)]
        # 重新映射 label → top class id 或 -1 (其他)
        plot_labels = np.array([l if l in top_classes else -1 for l in labels])

        # 颜色
        colors = plt.cm.tab10(np.linspace(0, 1, TOP_N))
        for i, cls in enumerate(top_classes):
            mask = plot_labels == cls
            name = name_map.get(cls, f'?({cls})')[:20]
            ax.scatter(Xt[mask, 0], Xt[mask, 1], c=[colors[i]], s=8, alpha=0.6, label=f'{name} ({mask.sum()})')
        mask_other = plot_labels == -1
        if mask_other.sum() > 0:
            ax.scatter(Xt[mask_other, 0], Xt[mask_other, 1], c='lightgray', s=6, alpha=0.3, label=f'other ({mask_other.sum()})')
        ax.set_title(title, fontsize=12)
        ax.legend(fontsize=6, loc='best', markerscale=1.5)
        ax.set_xticks([]); ax.set_yticks([])
    plt.suptitle(f't-SNE of encoder output (512D -> 2D), {len(X)} test reactions', fontsize=14)
    plt.tight_layout()
    out_panel = OUT_DIR / 'tsne_by_class.png'
    plt.savefig(out_panel, dpi=120, bbox_inches='tight')
    plt.close()
    print(f'✓ Wrote {out_panel}')

    # 单独一张 by yield 染色 (连续值)
    yld = np.array([y if y is not None else -1 for y in all_yields])
    mask_y = yld >= 0
    plt.figure(figsize=(10, 8))
    plt.scatter(Xt[~mask_y, 0], Xt[~mask_y, 1], c='lightgray', s=4, alpha=0.2, label=f'no yield ({(~mask_y).sum()})')
    sc = plt.scatter(Xt[mask_y, 0], Xt[mask_y, 1], c=yld[mask_y], cmap='RdYlGn', s=8, alpha=0.7, vmin=0, vmax=100)
    plt.colorbar(sc, label='yield %')
    plt.title(f't-SNE colored by yield ({len(X)} test reactions)', fontsize=12)
    plt.xticks([]); plt.yticks([])
    plt.tight_layout()
    out_y = OUT_DIR / 'tsne_by_yield.png'
    plt.savefig(out_y, dpi=120, bbox_inches='tight')
    plt.close()
    print(f'✓ Wrote {out_y}')

    # 保存 raw embedding 数据
    np.savez(OUT_DIR / 'tsne_data.npz', tsne_2d=Xt, embedding=X,
              labels={h: np.array(v) for h, v in all_labels.items()})
    print(f'✓ Saved raw data to {OUT_DIR}/tsne_data.npz')


if __name__ == '__main__':
    main()
