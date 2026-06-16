"""Charts for dedup exact_GT (true cluster-invariant metric, per unique rxn × hit ANY variant)."""
import sys, json
from pathlib import Path
for _p in ('/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages',):
    if _p not in sys.path: sys.path.insert(0, _p)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'DejaVu Sans'
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.grid'] = True
mpl.rcParams['grid.alpha'] = 0.3
mpl.rcParams['savefig.dpi'] = 150
mpl.rcParams['savefig.bbox'] = 'tight'

FIELDS = ['electrolytes', 'solvents', 'reagents', 'catalysts']
OUT = Path('eval_results/template_analysis/charts')
OUT.mkdir(parents=True, exist_ok=True)

dedup = json.load(open('eval_results/template_analysis/dedup_exact_gt.json'))

MODELS = [
    ('Sonnet 4.6', 'sonnet46', '#3498DB'),
    ('Opus 4.8', 'opus48', '#9B59B6'),
    ('Gemini Pro Low', 'gemini31prolow', '#F39C12'),
]

GROUP_COLORS = {'A': '#E74C3C', 'B': '#3498DB', 'C': '#27AE60'}


def autolabel(ax, bars, fmt='{:.1f}'):
    for b in bars:
        h = b.get_height()
        if h <= 0: continue
        ax.annotate(fmt.format(h), xy=(b.get_x() + b.get_width()/2, h),
                    xytext=(0, 2), textcoords='offset points',
                    ha='center', va='bottom', fontsize=8)


def chart_17_dedup_main():
    """Main chart: dedup exact_GT × 3 models × 3 groups × 4 fields."""
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5), sharey=True)
    for ax, (name, tag, _) in zip(axes, MODELS):
        per_field = dedup[tag]['per_field']
        n_rxn = dedup[tag]['n_unique_rxn']
        x = np.arange(len(FIELDS))
        w = 0.27
        for i, g in enumerate('ABC'):
            vals = [per_field[f]['hits'][g] / max(per_field[f]['eligible'], 1) * 100
                    for f in FIELDS]
            bars = ax.bar(x + (i-1)*w, vals, w,
                          label=f'{g} group',
                          color=GROUP_COLORS[g], edgecolor='white')
            autolabel(ax, bars)
        ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=10, rotation=15)
        ax.set_title(f'{name}\n({n_rxn} unique rxns)', fontsize=12, fontweight='bold')
        ax.set_axisbelow(True)
        if ax == axes[0]:
            ax.set_ylabel('Dedup exact_GT [%] (per rxn, hit ANY variant)', fontsize=11)
        ax.legend(loc='upper right', fontsize=9, framealpha=1.0)
    fig.suptitle('True cluster-invariant exact_GT — dedup by unique reaction (hit ANY paper variant)',
                 fontsize=13, fontweight='bold', y=1.02)
    p = OUT / '17_dedup_exact_gt_three_models.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_18_three_metrics(group='C'):
    """{group} group: row-level vs dedup vs r0 vs r1 — 4 bars per model per field."""
    base = Path('eval_results/template_analysis')

    def load(tag):
        r0 = json.load(open(base / f'template_aware_eval__{tag}.json'))
        r1 = json.load(open(base / f'r1_template_aware_eval__{tag}.json'))
        return r0, r1

    # row-level (full set) for ALL groups
    row_level = {
        'sonnet46': {
            'A': {'electrolytes': 1.5, 'solvents': 7.6, 'reagents': 2.4, 'catalysts': 0.0},
            'B': {'electrolytes': 16.5, 'solvents': 17.9, 'reagents': 5.8, 'catalysts': 6.9},
            'C': {'electrolytes': 19.2, 'solvents': 20.9, 'reagents': 6.4, 'catalysts': 11.4},
        },
        'opus48': {
            'A': {'electrolytes': 3.6, 'solvents': 11.8, 'reagents': 0.9, 'catalysts': 0.1},
            'B': {'electrolytes': 20.1, 'solvents': 18.5, 'reagents': 4.5, 'catalysts': 8.1},
            'C': {'electrolytes': 20.2, 'solvents': 19.7, 'reagents': 4.6, 'catalysts': 11.0},
        },
        'gemini31prolow': {
            'A': {'electrolytes': 23.7, 'solvents': 11.0, 'reagents': 1.1, 'catalysts': 0.0},
            'B': {'electrolytes': 25.8, 'solvents': 18.5, 'reagents': 4.6, 'catalysts': 5.8},
            'C': {'electrolytes': 20.7, 'solvents': 19.0, 'reagents': 4.3, 'catalysts': 8.7},
        },
    }
    prompt_desc = {
        'A': 'A prompt: reaction SMILES only (no retrieval, pure LLM)',
        'B': 'B prompt: reaction SMILES + top-5 similar reactions',
        'C': 'C prompt: reaction SMILES + similar reactions + mechanism',
    }[group]

    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5), sharey=True)
    for ax, (name, tag, color) in zip(axes, MODELS):
        r0, r1 = load(tag)
        per_field = dedup[tag]['per_field']

        x = np.arange(len(FIELDS))
        w = 0.20
        rl = [row_level[tag][group][f] for f in FIELDS]
        de = [per_field[f]['hits'][group] / max(per_field[f]['eligible'], 1) * 100 for f in FIELDS]
        r0c = [r0['per_field'][f][group]['exact_gt'] / max(r0['per_field'][f][group]['eligible'], 1) * 100 for f in FIELDS]
        r1c = [r1['per_field'][f][group]['exact_gt'] / max(r1['per_field'][f][group]['eligible'], 1) * 100 for f in FIELDS]

        b1 = ax.bar(x - 1.5*w, rl, w, label='row-level (2947)', color='#95A5A6', edgecolor='white')
        b2 = ax.bar(x - 0.5*w, de, w, label='dedup truth (1723 unique)', color='#16A085', edgecolor='white')
        b3 = ax.bar(x + 0.5*w, r0c, w, label='r0 eligible (1658)', color='#3498DB', edgecolor='white', alpha=0.7)
        b4 = ax.bar(x + 1.5*w, r1c, w, label='r1 eligible (227)', color='#E74C3C', edgecolor='black', hatch='///')
        for bars in [b1, b2, b3, b4]:
            autolabel(ax, bars)

        ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=10, rotation=15)
        ax.set_title(f'{name}', fontsize=12, fontweight='bold')
        ax.set_axisbelow(True)
        if ax == axes[0]:
            ax.set_ylabel(f'Exact GT match [%] ({group} group)', fontsize=11)
        ax.legend(loc='upper right', fontsize=8, framealpha=1.0)

    fig.suptitle(f'Four exact_GT estimators side by side ({group} group) — {prompt_desc}\n'
                 f'dedup (green) = cluster-invariant truth | row-level (gray) = paper-row may inflate | r1 (red hatched) = selection bias',
                 fontsize=12, fontweight='bold', y=1.02)
    suffix = {'A': '_A', 'B': '_B', 'C': '_C'}[group]
    p = OUT / f'18_exact_gt_four_estimators{suffix}.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_19_gains():
    """B-A and C-B gains under dedup metric, three models × four fields."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    for ax, gain_label, src, tgt in [(axes[0], 'B−A (reaction DB gain)', 'A', 'B'),
                                       (axes[1], 'C−B (mechanism gain)', 'B', 'C')]:
        x = np.arange(len(FIELDS))
        w = 0.27
        for i, (name, tag, color) in enumerate(MODELS):
            per_field = dedup[tag]['per_field']
            elig = [per_field[f]['eligible'] for f in FIELDS]
            src_rate = [per_field[f]['hits'][src] / max(elig[j], 1) * 100 for j, f in enumerate(FIELDS)]
            tgt_rate = [per_field[f]['hits'][tgt] / max(elig[j], 1) * 100 for j, f in enumerate(FIELDS)]
            diff = [t - s for t, s in zip(tgt_rate, src_rate)]
            bars = ax.bar(x + (i-1)*w, diff, w, label=name, color=color, edgecolor='white')
            for b, d in zip(bars, diff):
                ax.annotate(f'{d:+.1f}', xy=(b.get_x()+b.get_width()/2, d),
                            xytext=(0, 3 if d>=0 else -12), textcoords='offset points',
                            ha='center', fontsize=9, fontweight='bold')
        ax.axhline(0, color='black', linewidth=0.7)
        ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=10, rotation=15)
        ax.set_ylabel(f'{gain_label} [pp]', fontsize=11)
        ax.set_title(gain_label, fontsize=12, fontweight='bold')
        ax.legend(loc='upper right', fontsize=9, framealpha=1.0)
        ax.set_axisbelow(True)
    fig.suptitle('Dedup metric: contribution of reaction-DB (B−A) and mechanism (C−B) across 3 models',
                 fontsize=13, fontweight='bold', y=1.02)
    p = OUT / '19_dedup_gains_BminusA_CminusB.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def main():
    print(f'Saving to {OUT}/')
    chart_17_dedup_main()
    for g in 'ABC':
        chart_18_three_metrics(g)
    chart_19_gains()
    print('[OK] dedup charts saved')


if __name__ == '__main__':
    main()
