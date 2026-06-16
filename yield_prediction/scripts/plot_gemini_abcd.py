"""Plots for §5.7 — Gemini ABCD with small-model D group."""
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

# Template-aware hit ∈ winners (Gemini ABCD)
GEM = {
    'A': [50.3, 50.8, 2.1, 1.5],
    'B': [65.5, 57.5, 24.1, 22.0],
    'C': [64.8, 62.8, 25.2, 22.8],
    'D': [55.7, 57.3, 23.8, 27.8],
}
# Exact GT (strict) — to show catalyst breakthrough
GEM_GT = {
    'A': [20.4, 17.7, 0.1, 0.0],
    'B': [23.8, 20.7, 3.4, 1.9],
    'C': [22.5, 23.4, 3.8, 2.6],
    'D': [21.2, 24.2, 3.9, 14.7],
}

# Cross-model catalyst comparison
CATA_TA = {  # template-aware
    'Sonnet 4.6 C': 32.5,
    'Opus 4.8 C': 32.5,
    'Gemini C': 22.8,
    'Gemini D (+small)': 27.8,
}
CATA_GT = {  # exact GT
    'Sonnet 4.6 C': 8.8,
    'Opus 4.8 C': 8.6,
    'Gemini C': 2.6,
    'Gemini D (+small)': 14.7,
}

COLOR_A = '#E74C3C'; COLOR_B = '#3498DB'; COLOR_C = '#27AE60'; COLOR_D = '#F39C12'
OUT = Path('eval_results/template_analysis/charts')
OUT.mkdir(parents=True, exist_ok=True)


def autolabel(ax, bars, fmt='{:.1f}%'):
    for b in bars:
        h = b.get_height()
        if h <= 0: continue
        ax.annotate(fmt.format(h), xy=(b.get_x() + b.get_width()/2, h),
                    xytext=(0, 2), textcoords='offset points',
                    ha='center', va='bottom', fontsize=8)


def chart_abcd_main():
    """ABCD 主图 — template-aware"""
    fig, ax = plt.subplots(figsize=(11, 5.5))
    x = np.arange(len(FIELDS))
    w = 0.20
    for i, (grp, color, label) in enumerate([
            ('A', COLOR_A, 'A pure'),
            ('B', COLOR_B, 'B +rxn'),
            ('C', COLOR_C, 'C +rxn+mech'),
            ('D', COLOR_D, 'D +rxn+mech+small'),
        ]):
        bars = ax.bar(x + (i - 1.5) * w, GEM[grp], w, label=label, color=color, edgecolor='white')
        autolabel(ax, bars)
    ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
    ax.set_ylabel('Hit rate (pred ∈ winning conditions pool) [%]', fontsize=11)
    ax.set_title('Gemini 3.1 Pro Low: ABCD groups (template-aware) — D wins on catalyst (+5pp)',
                  fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=9, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '09_gemini_abcd_main.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_catalyst_breakthrough():
    """Catalyst exact-GT 单字段:Gemini D 击败所有"""
    fig, ax = plt.subplots(figsize=(10, 5.5))
    models = list(CATA_GT.keys())
    vals_ta = [CATA_TA[m] for m in models]
    vals_gt = [CATA_GT[m] for m in models]
    x = np.arange(len(models))
    w = 0.35
    bars1 = ax.bar(x - w/2, vals_ta, w, label='template-aware (hit ∈ winners)', color='#16A085', edgecolor='white')
    bars2 = ax.bar(x + w/2, vals_gt, w, label='exact GT (strict)', color='#E67E22', edgecolor='white')
    autolabel(ax, bars1); autolabel(ax, bars2)
    ax.set_xticks(x); ax.set_xticklabels(models, fontsize=10)
    ax.set_ylabel('Catalyst hit rate [%]', fontsize=11)
    ax.set_title('Catalyst hit rate across models — Gemini D (small-model hint) beats Opus on exact GT',
                  fontsize=12, fontweight='bold')
    ax.legend(loc='upper left', fontsize=10, framealpha=1.0)
    ax.set_axisbelow(True)
    # Annotation arrow for Gemini D exact GT
    ax.annotate(f'+12.1pp vs Gemini C\n(5.5× boost)',
                xy=(3 + w/2, 14.7), xytext=(3.4, 30),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                fontsize=10, fontweight='bold', color='#E67E22',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#FDEBD0', edgecolor='#E67E22'))
    p = OUT / '10_catalyst_breakthrough.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_d_vs_c_diff():
    """D-C 差异:catalyst 唯一正,其他都负"""
    fig, ax = plt.subplots(figsize=(10, 5))
    diffs_ta = [GEM['D'][i] - GEM['C'][i] for i in range(4)]
    diffs_gt = [GEM_GT['D'][i] - GEM_GT['C'][i] for i in range(4)]
    x = np.arange(len(FIELDS))
    w = 0.35
    bars1 = ax.bar(x - w/2, diffs_ta, w, label='template-aware', color=['#27AE60' if v>0 else '#E74C3C' for v in diffs_ta], edgecolor='white')
    bars2 = ax.bar(x + w/2, diffs_gt, w, label='exact GT', color=['#16A085' if v>0 else '#C0392B' for v in diffs_gt], edgecolor='white')
    for bars in [bars1, bars2]:
        for b in bars:
            h = b.get_height()
            ax.annotate(f'{h:+.1f}', xy=(b.get_x() + b.get_width()/2, h),
                        xytext=(0, 3 if h>=0 else -10), textcoords='offset points',
                        ha='center', fontsize=10, fontweight='bold')
    ax.axhline(0, color='black', linewidth=0.7)
    ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
    ax.set_ylabel('D − C diff [pp]', fontsize=11)
    ax.set_title("Effect of adding small-model hint on Gemini (D − C diff per field)",
                  fontsize=12, fontweight='bold')
    ax.legend(loc='upper left', fontsize=9, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '11_d_vs_c_diff.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def main():
    print(f'Saving to {OUT}/')
    chart_abcd_main()
    chart_catalyst_breakthrough()
    chart_d_vs_c_diff()
    print('[OK] 3 charts saved')


if __name__ == '__main__':
    main()
