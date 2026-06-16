"""Plot template-aware ablation results (4 charts)."""
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

COLOR_A = '#E74C3C'; COLOR_B = '#3498DB'; COLOR_C = '#27AE60'

FIELDS = ['electrolytes', 'solvents', 'reagents', 'catalysts']

# Template-aware "hit ∈ winners" metric (main)
DATA_TA = {
    'A': [3.9, 29.4, 1.6, 0.0],
    'B': [44.3, 45.8, 18.2, 28.7],
    'C': [50.5, 49.7, 17.8, 32.5],
}
# Exact GT match metric (old strict, on same 1658 subset)
DATA_GT = {
    'A': [0.6, 7.8, 0.4, 0.0],
    'B': [16.7, 21.7, 3.2, 8.6],
    'C': [17.9, 26.0, 2.8, 8.8],
}
# Overlap (≥1 SMILES in common)
DATA_OV = {
    'A': [4.4, 68.2, 4.7, 0.0],
    'B': [45.4, 80.8, 22.6, 28.9],
    'C': [51.5, 80.5, 23.4, 32.6],
}

GT_IS_WINNER_PCT = [51.8, 19.5, 17.2, 38.4]
ELIGIBLE = [1393, 1603, 1138, 536]

OUT = Path('eval_results/template_analysis/charts')
OUT.mkdir(parents=True, exist_ok=True)


def autolabel(ax, bars, fmt='{:.1f}%'):
    for b in bars:
        h = b.get_height()
        if h <= 0: continue
        ax.annotate(fmt.format(h), xy=(b.get_x() + b.get_width()/2, h),
                    xytext=(0, 2), textcoords='offset points',
                    ha='center', va='bottom', fontsize=8)


# Chart 1: Template-aware main results
def chart_template_aware_main():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    x = np.arange(len(FIELDS))
    w = 0.27
    bA = ax.bar(x - w, DATA_TA['A'], w, label='A: Pure LLM', color=COLOR_A, edgecolor='white')
    bB = ax.bar(x,     DATA_TA['B'], w, label='B: + Reaction DB', color=COLOR_B, edgecolor='white')
    bC = ax.bar(x + w, DATA_TA['C'], w, label='C: + Mechanism', color=COLOR_C, edgecolor='white')
    autolabel(ax, bA); autolabel(ax, bB); autolabel(ax, bC)
    # Eligible counts under x-labels
    xlabels = [f'{f}\nn={n}' for f, n in zip(FIELDS, ELIGIBLE)]
    ax.set_xticks(x); ax.set_xticklabels(xlabels, fontsize=10)
    ax.set_ylabel('Hit rate (pred ∈ winning conditions pool) [%]', fontsize=11)
    ax.set_title('Template-aware Fair Evaluation: pred ∈ same-cluster winning conditions (n=1,658 / 2,947)',
                  fontsize=12, fontweight='bold')
    ax.set_ylim(0, max(DATA_TA['B'] + DATA_TA['C']) * 1.15)
    ax.legend(loc='upper right', fontsize=10, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '01_template_aware_main.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


# Chart 2: Three metrics side-by-side for B group only (to show how lenient template-aware is)
def chart_three_metrics_b():
    fig, axes = plt.subplots(1, 4, figsize=(15, 4.5), sharey=False)
    for i, field in enumerate(FIELDS):
        ax = axes[i]
        metrics = ['exact GT\n(old, strict)', 'hit ∈ winners\n(template-aware)', 'overlap\n(loose)']
        # Use C group for showing the shift (or all three; let's show B as the "main library effect")
        vals_b = [DATA_GT['B'][i], DATA_TA['B'][i], DATA_OV['B'][i]]
        vals_a = [DATA_GT['A'][i], DATA_TA['A'][i], DATA_OV['A'][i]]
        x = np.arange(len(metrics))
        w = 0.4
        bA = ax.bar(x - w/2, vals_a, w, label='A pure', color=COLOR_A)
        bB = ax.bar(x + w/2, vals_b, w, label='B +rxn', color=COLOR_B)
        autolabel(ax, bA); autolabel(ax, bB)
        ax.set_xticks(x); ax.set_xticklabels(metrics, fontsize=9)
        ax.set_title(field, fontsize=11, fontweight='bold')
        if i == 0:
            ax.set_ylabel('Hit rate [%]', fontsize=10)
            ax.legend(fontsize=9, loc='upper left')
        ax.set_axisbelow(True)
    fig.suptitle('How metric strictness affects measured LLM accuracy (B group, n=1,658)',
                  fontsize=13, fontweight='bold', y=1.03)
    p = OUT / '02_three_metrics.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


# Chart 3: Reaction-center clustering pie + cluster-size histogram
def chart_clustering_overview():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    # Left: pie of cluster sizes
    ax1 = axes[0]
    labels = ['singletons\n(1153 clusters)', '2-5\n(459)', '6-10\n(137)', '11-50\n(310)', '51-100\n(56)', '>100\n(47)']
    counts = [1153, 1263, 1062, 7189, 4163, 9571]   # reaction counts in each bucket
    colors = ['#E74C3C', '#E67E22', '#F39C12', '#3498DB', '#27AE60', '#16A085']
    wedges, texts, autotexts = ax1.pie(counts, labels=labels, colors=colors,
                                          autopct='%1.1f%%', startangle=90,
                                          wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
                                          textprops={'fontsize': 9})
    for at in autotexts: at.set_fontsize(10); at.set_fontweight('bold'); at.set_color('white')
    ax1.set_title('Reaction-center cluster size distribution\n(24,401 reactions, 2,162 unique signatures)',
                   fontsize=11, fontweight='bold')

    # Right: coverage waterfall
    ax2 = axes[1]
    cats = ['LLM ablation\nraw rxns', 'sig successfully\nextracted', 'sig has train\nprecedent', 'eligible\n(sig + winners)']
    vals = [2947, 2942, 2942 - 1284, 1658]
    bars = ax2.bar(cats, vals, color=['#BDC3C7', '#3498DB', '#1ABC9C', '#27AE60'], edgecolor='white')
    for b, v in zip(bars, vals):
        ax2.annotate(f'{v}\n({v/2947*100:.1f}%)', xy=(b.get_x() + b.get_width()/2, v),
                     xytext=(0, 3), textcoords='offset points', ha='center', fontweight='bold')
    ax2.set_ylabel('Reaction count', fontsize=10)
    ax2.set_title('Test-set funnel to template-aware-eligible reactions',
                   fontsize=11, fontweight='bold')
    ax2.set_axisbelow(True)

    p = OUT / '03_clustering_overview.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


# Chart 4: GT-is-winner rate per field (showing why exact-GT is too strict)
def chart_gt_is_winner():
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(FIELDS))
    bars = ax.bar(x, GT_IS_WINNER_PCT, 0.55,
                   color=['#E67E22', '#F39C12', '#E74C3C', '#9B59B6'], edgecolor='white')
    for b, v, n in zip(bars, GT_IS_WINNER_PCT, ELIGIBLE):
        ax.annotate(f'{v:.1f}%\n({int(v/100*n)}/{n})',
                    xy=(b.get_x() + b.get_width()/2, v),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
    ax.set_ylabel("% of test reactions where GT is itself a winning condition (yield>50% in train)",
                   fontsize=10)
    ax.set_title("Why exact-GT-match metric undercounts LLM ability\n(only ~17-52% of GT entries are themselves 'winning' conditions for that reaction type)",
                  fontsize=11, fontweight='bold')
    ax.axhline(50, color='gray', linewidth=0.8, linestyle='--', alpha=0.5)
    ax.set_ylim(0, 70)
    ax.set_axisbelow(True)
    p = OUT / '04_gt_is_winner.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def main():
    print(f'Saving template-aware charts to {OUT}/')
    chart_template_aware_main()
    chart_three_metrics_b()
    chart_clustering_overview()
    chart_gt_is_winner()
    print('\n[OK] 4 charts saved')


if __name__ == '__main__':
    main()
