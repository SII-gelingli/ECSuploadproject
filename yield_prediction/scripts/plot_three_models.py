"""3 模型对比图: Sonnet 4.6 vs Opus 4.8 vs Gemini 3.1 Pro Low."""
import sys
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

# Template-aware "hit ∈ winners" — main fair metric
DATA = {
    'sonnet46':  {'A':[3.9, 29.4, 1.6, 0.0],   'B':[44.3, 45.8, 18.2, 28.7], 'C':[50.5, 49.7, 17.8, 32.5]},
    'opus48':    {'A':[16.5, 26.8, 6.7, 0.6],  'B':[57.1, 53.0, 19.0, 31.7], 'C':[58.9, 52.9, 21.2, 32.5]},
    'gemini3.1': {'A':[54.9, 54.2, 3.2, 1.5],  'B':[65.4, 57.7, 17.6, 23.9], 'C':[67.0, 62.2, 17.8, 23.1]},
}
MODEL_COLORS = {
    'sonnet46': '#5DADE2',
    'opus48': '#9B59B6',
    'gemini3.1': '#27AE60',
}
MODEL_LABELS = {
    'sonnet46': 'Sonnet 4.6',
    'opus48': 'Opus 4.8',
    'gemini3.1': 'Gemini 3.1 Pro Low',
}
OUT = Path('eval_results/template_analysis/charts')
OUT.mkdir(parents=True, exist_ok=True)


def autolabel(ax, bars, fmt='{:.1f}%'):
    for b in bars:
        h = b.get_height()
        if h <= 0: continue
        ax.annotate(fmt.format(h), xy=(b.get_x() + b.get_width()/2, h),
                    xytext=(0, 2), textcoords='offset points',
                    ha='center', va='bottom', fontsize=8)


def chart_c_compare():
    """三模型 C 组(retrieval+mechanism)对比"""
    fig, ax = plt.subplots(figsize=(11, 5.5))
    x = np.arange(len(FIELDS))
    w = 0.27
    for i, m in enumerate(['sonnet46', 'opus48', 'gemini3.1']):
        offset = (i - 1) * w
        bars = ax.bar(x + offset, DATA[m]['C'], w, label=MODEL_LABELS[m], color=MODEL_COLORS[m], edgecolor='white')
        autolabel(ax, bars)
    ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
    ax.set_ylabel("Hit rate (pred ∈ winning conditions pool) [%]", fontsize=11)
    ax.set_title("Three-model C group (+ReactionDB +Mechanism) — template-aware hit rate (n=1,658)",
                  fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '05_three_models_C.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_a_compare():
    """三模型 A pure (LLM 内置知识) 对比"""
    fig, ax = plt.subplots(figsize=(11, 5.5))
    x = np.arange(len(FIELDS))
    w = 0.27
    for i, m in enumerate(['sonnet46', 'opus48', 'gemini3.1']):
        offset = (i - 1) * w
        bars = ax.bar(x + offset, DATA[m]['A'], w, label=MODEL_LABELS[m], color=MODEL_COLORS[m], edgecolor='white')
        autolabel(ax, bars)
    ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
    ax.set_ylabel("Hit rate (pred ∈ winning conditions pool) [%]", fontsize=11)
    ax.set_title("Three-model A pure baseline (LLM internal knowledge only) — Gemini's electrochem prior is striking",
                  fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '06_three_models_A.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_gains_compare():
    """三模型 reaction-db / mechanism gain 对比"""
    fig, axes = plt.subplots(1, 2, figsize=(15, 5.5))
    for ax_idx, (gain_type, title) in enumerate([
        ('BA', 'Reaction DB gain (B - A)'),
        ('CB', 'Mechanism gain (C - B)'),
    ]):
        ax = axes[ax_idx]
        x = np.arange(len(FIELDS))
        w = 0.27
        for i, m in enumerate(['sonnet46', 'opus48', 'gemini3.1']):
            offset = (i - 1) * w
            if gain_type == 'BA':
                vals = [DATA[m]['B'][j] - DATA[m]['A'][j] for j in range(4)]
            else:
                vals = [DATA[m]['C'][j] - DATA[m]['B'][j] for j in range(4)]
            bars = ax.bar(x + offset, vals, w, label=MODEL_LABELS[m], color=MODEL_COLORS[m], edgecolor='white')
            autolabel(ax, bars, fmt='{:+.1f}')
        ax.axhline(0, color='black', linewidth=0.7)
        ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
        ax.set_ylabel("Gain [pp]", fontsize=11)
        ax.set_title(title, fontsize=12, fontweight='bold')
        if ax_idx == 0:
            ax.legend(loc='upper right', fontsize=9, framealpha=1.0)
        ax.set_axisbelow(True)
    fig.suptitle("Reaction-DB vs Mechanism gains across three Claude/Gemini models",
                  fontsize=13, fontweight='bold', y=1.02)
    p = OUT / '07_three_models_gains.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_cost_perf():
    """性价比图: 横轴 cost,纵轴 C accuracy 平均"""
    fig, ax = plt.subplots(figsize=(10, 5.5))
    # estimated $cost for full 2947 × 3 = 8841 calls
    costs = {'sonnet46': 53, 'opus48': 265, 'gemini3.1': 3}  # Gemini 估算非代理价
    c_avg = {m: np.mean(DATA[m]['C']) for m in DATA}
    for m in DATA:
        ax.scatter(costs[m], c_avg[m], s=300, color=MODEL_COLORS[m], edgecolor='black', linewidth=1.5, zorder=3, label=MODEL_LABELS[m])
        ax.annotate(f'{MODEL_LABELS[m]}\n${costs[m]}, {c_avg[m]:.1f}%',
                    xy=(costs[m], c_avg[m]), xytext=(12, 0),
                    textcoords='offset points', va='center', fontsize=10, fontweight='bold')
    ax.set_xscale('log')
    ax.set_xlabel("Estimated cost for full 2947 × 3 groups (USD, log scale)", fontsize=11)
    ax.set_ylabel("Mean C group hit rate (template-aware, 4 fields avg) [%]", fontsize=11)
    ax.set_title("Cost vs Accuracy — Sonnet/Gemini cost-effective; Opus 5× cost for ~3pp gain",
                  fontsize=12, fontweight='bold')
    ax.set_xlim(1, 500)
    ax.set_ylim(min(c_avg.values()) - 3, max(c_avg.values()) + 3)
    ax.set_axisbelow(True)
    p = OUT / '08_cost_performance.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def main():
    print(f'Saving to {OUT}/')
    chart_a_compare()
    chart_c_compare()
    chart_gains_compare()
    chart_cost_perf()
    print('[OK] 4 charts saved')


if __name__ == '__main__':
    main()
