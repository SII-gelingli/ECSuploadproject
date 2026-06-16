"""画 LLM ablation 实验结果的统计对比图. 输出到 eval_results/llm_ablation_sonnet46_full/charts/"""
import sys, json
from pathlib import Path
for _p in ('/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages',):
    if _p not in sys.path: sys.path.insert(0, _p)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 通用样式
mpl.rcParams['font.family'] = 'DejaVu Sans'
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.grid'] = True
mpl.rcParams['grid.alpha'] = 0.3
mpl.rcParams['grid.linewidth'] = 0.5
mpl.rcParams['savefig.dpi'] = 150
mpl.rcParams['savefig.bbox'] = 'tight'

# 颜色方案 (3 组)
COLOR_A = '#E74C3C'  # red — pure LLM
COLOR_B = '#3498DB'  # blue — +reaction
COLOR_C = '#27AE60'  # green — +reaction+mechanism

# 数据 (硬编码,因为已经稳定 — 全量 2947 / 实测数字)
FIELDS = ['electrolytes', 'solvents', 'reagents', 'catalysts']

# (a) 全量 2947 — GT 非空 + set✓
DATA_FULL = {
    'GT_nonempty': [2587, 2851, 2193, 1180],
    'A': [1.5, 7.6, 2.4, 0.0],   # % hit on GT-nonempty
    'B': [16.5, 17.9, 5.8, 6.9],
    'C': [19.2, 20.9, 6.4, 11.4],
}

# (b) 只有反应库子集 (1567 反应)
DATA_RXN_ONLY = {
    'GT_nonempty': [1280, 1471, 1119, 524],
    'A': [1.8, 7.1, 1.6, 0.0],
    'B': [22.7, 18.2, 7.6, 5.7],
    'C': [23.1, 18.6, 7.9, 5.0],
}

# (c) 反应+机理都有子集 (1380 反应)
DATA_BOTH = {
    'GT_nonempty': [1307, 1380, 1074, 656],
    'A': [1.2, 8.2, 3.2, 0.0],
    'B': [10.4, 17.5, 3.9, 7.8],
    'C': [15.4, 23.3, 4.8, 16.5],
}

OUT = Path('eval_results/llm_ablation_sonnet46_full/charts')
OUT.mkdir(parents=True, exist_ok=True)


def autolabel(ax, bars, fmt='{:.1f}%'):
    for b in bars:
        h = b.get_height()
        if h <= 0: continue
        ax.annotate(fmt.format(h), xy=(b.get_x() + b.get_width()/2, h),
                    xytext=(0, 2), textcoords='offset points',
                    ha='center', va='bottom', fontsize=8)


# ============ Chart 1: 全量 三组并列柱状图 (主结果) ============
def chart_main():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    x = np.arange(len(FIELDS))
    w = 0.27
    bA = ax.bar(x - w, DATA_FULL['A'], w, label='A: Pure LLM', color=COLOR_A, edgecolor='white')
    bB = ax.bar(x,     DATA_FULL['B'], w, label='B: + Reaction DB', color=COLOR_B, edgecolor='white')
    bC = ax.bar(x + w, DATA_FULL['C'], w, label='C: + Mechanism', color=COLOR_C, edgecolor='white')
    autolabel(ax, bA); autolabel(ax, bB); autolabel(ax, bC)
    ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
    ax.set_ylabel('Hit rate (GT-nonempty, set exact match) [%]', fontsize=11)
    ax.set_title('LLM Ablation: Pure vs +ReactionDB vs +Mechanism (test=2947, Claude Sonnet 4.6)', fontsize=12, fontweight='bold')
    ax.set_ylim(0, max(DATA_FULL['C']) * 1.20)
    ax.legend(loc='upper right', fontsize=10, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '01_main_results.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


# ============ Chart 2: gain decomposition (反应库 vs 机理 净增益) ============
def chart_gain_decomposition():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    x = np.arange(len(FIELDS))
    w = 0.55
    A = np.array(DATA_FULL['A'])
    B = np.array(DATA_FULL['B'])
    C = np.array(DATA_FULL['C'])
    bA = ax.bar(x, A,         w, label='A baseline (LLM internal knowledge)', color=COLOR_A, edgecolor='white')
    bB = ax.bar(x, B - A,     w, bottom=A,     label='Reaction DB gain (B - A)', color=COLOR_B, edgecolor='white')
    bC = ax.bar(x, C - B,     w, bottom=B,     label='Mechanism gain (C - B)', color=COLOR_C, edgecolor='white')

    # 总命中标在顶上
    for i, c in enumerate(C):
        ax.annotate(f'{c:.1f}%', xy=(x[i], c), xytext=(0, 3),
                    textcoords='offset points', ha='center', fontsize=10, fontweight='bold')
    # 反应库 gain 标中段
    for i, (a, b) in enumerate(zip(A, B)):
        gain = b - a
        if gain > 1.5:
            ax.annotate(f'+{gain:.1f}', xy=(x[i], a + gain/2),
                        ha='center', va='center', fontsize=9, color='white', fontweight='bold')
    # 机理 gain 标在 C 段中段
    for i, (b, c) in enumerate(zip(B, C)):
        gain = c - b
        if gain > 1.5:
            ax.annotate(f'+{gain:.1f}', xy=(x[i], b + gain/2),
                        ha='center', va='center', fontsize=9, color='white', fontweight='bold')

    ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
    ax.set_ylabel('Cumulative hit rate [%]', fontsize=11)
    ax.set_title('Gain Decomposition: LLM Internal vs Reaction DB vs Mechanism (full 2947)', fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '02_gain_decomposition.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


# ============ Chart 3: 机理覆盖率 + 稀释效应 (3 子集对比) ============
def chart_subset_dilution():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5),
                              gridspec_kw={'width_ratios': [1, 2.3]})

    # 左:覆盖率 donut
    ax1 = axes[0]
    sizes = [1380, 1567]
    labels = ['with mechanism\n(1380 / 46.8%)', 'no mechanism\n(1567 / 53.2%)']
    colors = [COLOR_C, '#BDC3C7']
    wedges, texts = ax1.pie(sizes, labels=labels, colors=colors, startangle=90,
                              wedgeprops={'width': 0.4, 'edgecolor': 'white', 'linewidth': 2},
                              textprops={'fontsize': 11})
    ax1.text(0, 0, f'{2947}\nreactions', ha='center', va='center', fontsize=14, fontweight='bold')
    ax1.set_title('Mechanism KB Coverage on Test Set', fontsize=12, fontweight='bold')

    # 右:三子集 C-B 增益对比
    ax2 = axes[1]
    x = np.arange(len(FIELDS))
    w = 0.27
    gain_full     = np.array(DATA_FULL['C']) - np.array(DATA_FULL['B'])
    gain_rxn_only = np.array(DATA_RXN_ONLY['C']) - np.array(DATA_RXN_ONLY['B'])
    gain_both     = np.array(DATA_BOTH['C']) - np.array(DATA_BOTH['B'])

    bF = ax2.bar(x - w, gain_full,     w, label='Full 2947 (diluted)', color='#95A5A6')
    bR = ax2.bar(x,     gain_rxn_only, w, label='rxn-only subset (1567, no mech)', color='#BDC3C7')
    bB = ax2.bar(x + w, gain_both,     w, label='both subset (1380, with mech) ← true value', color=COLOR_C)
    autolabel(ax2, bF, fmt='{:+.1f}')
    autolabel(ax2, bR, fmt='{:+.1f}')
    autolabel(ax2, bB, fmt='{:+.1f}')

    ax2.axhline(0, color='black', linewidth=0.8, alpha=0.6)
    ax2.set_xticks(x); ax2.set_xticklabels(FIELDS, fontsize=11)
    ax2.set_ylabel('Mechanism gain C-B [pp]', fontsize=11)
    ax2.set_title('Mechanism Gain by Subset (Dilution Effect)', fontsize=12, fontweight='bold')
    ax2.set_ylim(min(min(gain_full), min(gain_rxn_only), min(gain_both)) - 1,
                  max(gain_both) + 2)
    ax2.legend(loc='upper left', fontsize=9, framealpha=1.0)
    ax2.set_axisbelow(True)

    p = OUT / '03_mechanism_dilution.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


# ============ Chart 4: both 子集主结果 (机理真实价值) ============
def chart_both_subset():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    x = np.arange(len(FIELDS))
    w = 0.27
    bA = ax.bar(x - w, DATA_BOTH['A'], w, label='A: Pure LLM', color=COLOR_A, edgecolor='white')
    bB = ax.bar(x,     DATA_BOTH['B'], w, label='B: + Reaction DB', color=COLOR_B, edgecolor='white')
    bC = ax.bar(x + w, DATA_BOTH['C'], w, label='C: + Mechanism', color=COLOR_C, edgecolor='white')
    autolabel(ax, bA); autolabel(ax, bB); autolabel(ax, bC)
    ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
    ax.set_ylabel('Hit rate (GT-nonempty, set exact) [%]', fontsize=11)
    ax.set_title('"both" subset (1380 reactions with mechanism) — true mechanism value',
                  fontsize=12, fontweight='bold')
    ax.set_ylim(0, max(DATA_BOTH['C']) * 1.20)
    ax.legend(loc='upper right', fontsize=10, framealpha=1.0)
    ax.set_axisbelow(True)

    # Annotate catalyst's +111% relative gain
    cat_i = FIELDS.index('catalysts')
    ax.annotate('+111% relative gain\n(7.8% -> 16.5%)',
                xy=(cat_i + w, DATA_BOTH['C'][cat_i]),
                xytext=(cat_i + 0.5, DATA_BOTH['C'][cat_i] + 5),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.2),
                fontsize=10, fontweight='bold', color='#27AE60',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#D5F5E3', edgecolor='#27AE60'))

    p = OUT / '04_both_subset_main.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


# ============ Chart 5: 全字段对比 (5 子图,每字段一个,显示 ABC 三组) ============
def chart_per_field_detail():
    fig, axes = plt.subplots(1, 4, figsize=(16, 4.5), sharey=False)
    subsets = ['Full\n(2947)', 'rxn-only\n(1567)', 'both\n(1380)']
    data_sets = [DATA_FULL, DATA_RXN_ONLY, DATA_BOTH]

    for i, field in enumerate(FIELDS):
        ax = axes[i]
        x = np.arange(len(subsets))
        w = 0.27
        A_vals = [d['A'][i] for d in data_sets]
        B_vals = [d['B'][i] for d in data_sets]
        C_vals = [d['C'][i] for d in data_sets]
        bA = ax.bar(x - w, A_vals, w, label='A pure', color=COLOR_A)
        bB = ax.bar(x,     B_vals, w, label='B +rxn', color=COLOR_B)
        bC = ax.bar(x + w, C_vals, w, label='C +rxn+mech', color=COLOR_C)
        for bars in [bA, bB, bC]:
            for b in bars:
                h = b.get_height()
                if h > 0.1:
                    ax.annotate(f'{h:.1f}', xy=(b.get_x() + b.get_width()/2, h),
                                xytext=(0, 2), textcoords='offset points',
                                ha='center', fontsize=8)
        ax.set_xticks(x); ax.set_xticklabels(subsets, fontsize=10)
        ax.set_title(field, fontsize=11, fontweight='bold')
        if i == 0:
            ax.set_ylabel('Hit rate [%]', fontsize=10)
            ax.legend(fontsize=8, loc='upper left')
        ax.set_axisbelow(True)

    fig.suptitle('Per-field hit rate across subsets', fontsize=13, fontweight='bold', y=1.02)
    p = OUT / '05_per_field_subsets.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


# ============ Chart 6: 横向条形 — 反应库 vs 机理 增益排序 ============
def chart_horizontal_gain_ranking():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    fields_y = FIELDS
    y = np.arange(len(fields_y))
    h = 0.35

    rxn_gain  = [DATA_FULL['B'][i] - DATA_FULL['A'][i] for i in range(4)]
    mech_gain_full = [DATA_FULL['C'][i] - DATA_FULL['B'][i] for i in range(4)]
    mech_gain_both = [DATA_BOTH['C'][i] - DATA_BOTH['B'][i] for i in range(4)]

    bR = ax.barh(y + h/2, rxn_gain, h, label='Reaction DB gain (B - A)', color=COLOR_B)
    bM = ax.barh(y - h/2, mech_gain_full, h, label='Mechanism gain on full 2947', color=COLOR_C, alpha=0.55)
    # both subset mechanism gain (hatch overlay)
    bM2 = ax.barh(y - h/2, mech_gain_both, h, color='none', edgecolor=COLOR_C, linewidth=2.5,
                   hatch='///', label='Mechanism gain on "both" subset (true value)')

    for bars in [bR, bM]:
        for b in bars:
            w = b.get_width()
            ax.annotate(f'{w:+.1f}', xy=(w, b.get_y() + b.get_height()/2),
                        xytext=(3 if w > 0 else -3, 0), textcoords='offset points',
                        ha='left' if w > 0 else 'right', va='center', fontsize=9, fontweight='bold')
    for b, v in zip(bM2, mech_gain_both):
        ax.annotate(f'({v:+.1f})', xy=(v, b.get_y() + b.get_height()/2),
                    xytext=(20, 0), textcoords='offset points',
                    ha='left', va='center', fontsize=8.5, color='#27AE60', fontweight='bold')

    ax.set_yticks(y); ax.set_yticklabels(fields_y, fontsize=11)
    ax.set_xlabel('Gain [pp]', fontsize=11)
    ax.set_title('Reaction DB vs Mechanism Gain (mech shows true value only on "both" subset)',
                  fontsize=12, fontweight='bold')
    ax.axvline(0, color='black', linewidth=0.8)
    ax.legend(loc='lower right', fontsize=9, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '06_gain_ranking.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def main():
    print(f'Saving charts to {OUT}/')
    chart_main()
    chart_gain_decomposition()
    chart_subset_dilution()
    chart_both_subset()
    chart_per_field_detail()
    chart_horizontal_gain_ranking()
    print(f'\n[OK] 6 charts saved')


if __name__ == '__main__':
    main()
