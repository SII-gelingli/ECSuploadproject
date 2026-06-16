"""Charts for Gemini ABCD: r1 vs r0 + dedup truth comparison."""
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

# Load r1 ABCD data
r1 = json.load(open('eval_results/template_analysis/r1_template_aware_eval__gemini31_abcd.json'))
# Load r0 ABCD data
r0 = json.load(open('eval_results/template_analysis/template_aware_eval__gemini31_abcd.json'))
# Load dedup ABCD data
dedup = json.load(open('eval_results/template_analysis/dedup_exact_gt_gemini_abcd.json'))

GROUPS = list('ABCD')
COLOR = {'A': '#E74C3C', 'B': '#3498DB', 'C': '#27AE60', 'D': '#F39C12'}
GROUP_LABEL = {'A': 'A pure', 'B': 'B +rxn', 'C': 'C +rxn+mech', 'D': 'D +rxn+mech+small'}


def autolabel(ax, bars, fmt='{:.1f}'):
    for b in bars:
        h = b.get_height()
        if abs(h) < 0.05: continue
        ax.annotate(fmt.format(h), xy=(b.get_x() + b.get_width()/2, h),
                    xytext=(0, 2 if h >= 0 else -12), textcoords='offset points',
                    ha='center', va='bottom', fontsize=8)


def chart_20_gemini_abcd_r1_main():
    """Gemini ABCD r1: hit ∈ winners (template-aware), 4 fields × 4 groups."""
    fig, ax = plt.subplots(figsize=(11, 5.5))
    x = np.arange(len(FIELDS))
    w = 0.20
    for i, g in enumerate(GROUPS):
        vals = [r1['per_field'][f][g]['exact_winner']/max(r1['per_field'][f][g]['eligible'],1)*100 for f in FIELDS]
        bars = ax.bar(x + (i - 1.5)*w, vals, w, label=GROUP_LABEL[g],
                      color=COLOR[g], edgecolor='black', hatch='///', linewidth=0.8)
        autolabel(ax, bars)
    ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
    ax.set_ylabel('Hit ∈ winners [%] (template-aware)', fontsize=11)
    ax.set_title('Gemini 3.1 Pro Low ABCD under Radius-1 (template-aware, 222 eligible)\n'
                 'D wins on electrolyte +21pp; B wins on catalyst +21pp (D over-corrects)',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=9, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '20_gemini_abcd_r1_main.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_21_gemini_abcd_r1_exact_gt():
    """Gemini ABCD r1: exact GT, 4 fields × 4 groups."""
    fig, ax = plt.subplots(figsize=(11, 5.5))
    x = np.arange(len(FIELDS))
    w = 0.20
    for i, g in enumerate(GROUPS):
        vals = [r1['per_field'][f][g]['exact_gt']/max(r1['per_field'][f][g]['eligible'],1)*100 for f in FIELDS]
        bars = ax.bar(x + (i - 1.5)*w, vals, w, label=GROUP_LABEL[g],
                      color=COLOR[g], edgecolor='black', hatch='///', linewidth=0.8)
        autolabel(ax, bars)
    ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
    ax.set_ylabel('Exact GT match [%] (C group, strict)', fontsize=11)
    ax.set_title('Gemini 3.1 Pro Low ABCD under Radius-1 (exact GT, strict, 222 eligible)\n'
                 'B catalyst exact GT 25.6% beats D 23.2% — r1 reverses r0 conclusion',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=9, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '21_gemini_abcd_r1_exact_gt.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_22_gemini_abcd_three_radii():
    """Gemini ABCD: dedup truth vs r0 eligible vs r1 eligible — exact GT."""
    fig, axes = plt.subplots(2, 2, figsize=(15, 8.5))
    axes = axes.flatten()
    for ax_idx, f in enumerate(FIELDS):
        ax = axes[ax_idx]
        x = np.arange(len(GROUPS))
        w = 0.27
        # dedup
        dv = [dedup['per_field'][f]['hits'][g]/max(dedup['per_field'][f]['eligible'],1)*100 for g in GROUPS]
        # r0 (exact GT)
        r0v = [r0['per_field'][f][g]['exact_gt']/max(r0['per_field'][f][g]['eligible'],1)*100 for g in GROUPS]
        # r1 (exact GT)
        r1v = [r1['per_field'][f][g]['exact_gt']/max(r1['per_field'][f][g]['eligible'],1)*100 for g in GROUPS]

        b1 = ax.bar(x - w, dv, w, label=f'dedup truth (n={dedup["per_field"][f]["eligible"]})',
                    color='#16A085', edgecolor='white')
        b2 = ax.bar(x, r0v, w, label=f'r0 eligible (n={r0["per_field"][f]["A"]["eligible"]})',
                    color='#3498DB', alpha=0.7, edgecolor='white')
        b3 = ax.bar(x + w, r1v, w, label=f'r1 eligible (n={r1["per_field"][f]["A"]["eligible"]})',
                    color='#E74C3C', edgecolor='black', hatch='///', linewidth=0.8)
        for bars in [b1, b2, b3]:
            autolabel(ax, bars)
        ax.set_xticks(x); ax.set_xticklabels([GROUP_LABEL[g] for g in GROUPS], fontsize=9, rotation=15)
        ax.set_ylabel('Exact GT [%]', fontsize=10)
        ax.set_title(f'{f}', fontsize=12, fontweight='bold')
        ax.set_axisbelow(True)
        ax.legend(loc='upper left', fontsize=8, framealpha=1.0)

    fig.suptitle('Gemini ABCD: exact GT under three estimators (dedup truth / r0 / r1) — catalyst panel shows r1 bias',
                 fontsize=13, fontweight='bold', y=1.0)
    p = OUT / '22_gemini_abcd_three_radii.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_18d_gemini_abcd_four_estimators():
    """Gemini-only ABCD 4-panel: each panel = 1 group, showing 4 estimators × 4 fields.
    Mirror of Chart 18-A/B/C but Gemini-only since D group only exists for Gemini."""

    base = Path('eval_results/template_analysis')
    # Need row-level numbers for ABCD - compute from raw
    import sys as _sys
    _sys.path.insert(0, '/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages')
    _sys.path.insert(0, '/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent')
    import importlib.util as _ilu
    spec = _ilu.spec_from_file_location('utils.electrode_normalizer',
        '/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/yield_prediction/utils/electrode_normalizer.py')
    m = _ilu.module_from_spec(spec); _sys.modules['utils.electrode_normalizer'] = m; spec.loader.exec_module(m)
    spec = _ilu.spec_from_file_location('_eqs',
        '/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/yield_prediction/scripts/eval_qwen_sft.py')
    m = _ilu.module_from_spec(spec); _sys.modules['_eqs'] = m; spec.loader.exec_module(m)
    canon_set = m.canon_set

    abl = json.load(open('eval_results/llm_ablation_gemini31pro_abcd/raw_results.json'))
    valid = [r for r in abl if r and 'rxn' in r and r.get('gold')]
    row_level_rates = {}
    for g in 'ABCD':
        row_level_rates[g] = {}
        for f in FIELDS:
            n = 0; hits = 0
            for r in valid:
                gold = canon_set(r['gold'].get(f, []) or [])
                if not gold: continue
                n += 1
                pred = canon_set((r.get(f'{g}_pred') or {}).get(f, []) or [])
                if frozenset(pred) == frozenset(gold): hits += 1
            row_level_rates[g][f] = hits / max(n, 1) * 100

    fig, axes = plt.subplots(1, 4, figsize=(22, 5.5), sharey=True)
    for ax, g in zip(axes, GROUPS):
        x = np.arange(len(FIELDS))
        w = 0.20

        rl = [row_level_rates[g][f] for f in FIELDS]
        de = [dedup['per_field'][f]['hits'][g] / max(dedup['per_field'][f]['eligible'], 1) * 100 for f in FIELDS]
        r0c = [r0['per_field'][f][g]['exact_gt'] / max(r0['per_field'][f][g]['eligible'], 1) * 100 for f in FIELDS]
        r1c = [r1['per_field'][f][g]['exact_gt'] / max(r1['per_field'][f][g]['eligible'], 1) * 100 for f in FIELDS]

        b1 = ax.bar(x - 1.5*w, rl, w, label='row-level (2898)', color='#95A5A6', edgecolor='white')
        b2 = ax.bar(x - 0.5*w, de, w, label='dedup truth (1707 unique)', color='#16A085', edgecolor='white')
        b3 = ax.bar(x + 0.5*w, r0c, w, label='r0 eligible (1647)', color='#3498DB', edgecolor='white', alpha=0.7)
        b4 = ax.bar(x + 1.5*w, r1c, w, label='r1 eligible (222)', color='#E74C3C', edgecolor='black', hatch='///')
        for bars in [b1, b2, b3, b4]:
            autolabel(ax, bars)

        ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=10, rotation=15)
        ax.set_title(f'{GROUP_LABEL[g]}', fontsize=12, fontweight='bold')
        ax.set_axisbelow(True)
        if ax == axes[0]:
            ax.set_ylabel('Exact GT match [%] — Gemini Pro Low', fontsize=11)
        ax.legend(loc='upper right', fontsize=7, framealpha=1.0)

    fig.suptitle('Gemini 3.1 Pro Low ABCD: four exact_GT estimators × all 4 prompt groups\n'
                 'D-C catalyst gain: row-level +6.8pp | dedup TRUTH +2.3pp | r0 +12.1pp | r1 +14.7pp — dedup is the unbiased estimate',
                 fontsize=12, fontweight='bold', y=1.02)
    p = OUT / '18_exact_gt_four_estimators_D_gemini.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_23_dedup_truth_abcd():
    """Gemini ABCD: dedup truth main, 4 fields × 4 groups."""
    fig, ax = plt.subplots(figsize=(11, 5.5))
    x = np.arange(len(FIELDS))
    w = 0.20
    for i, g in enumerate(GROUPS):
        vals = [dedup['per_field'][f]['hits'][g]/max(dedup['per_field'][f]['eligible'],1)*100 for f in FIELDS]
        bars = ax.bar(x + (i - 1.5)*w, vals, w, label=GROUP_LABEL[g],
                      color=COLOR[g], edgecolor='white')
        autolabel(ax, bars)
    ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
    ax.set_ylabel('Dedup exact_GT [%]', fontsize=11)
    ax.set_title('Gemini 3.1 Pro Low ABCD: dedup truth (per unique rxn × hit ANY paper variant)\n'
                 f'1,707 unique rxns | D catalyst +2.3pp,solvent +2.0pp,electrolyte +0.8pp,reagent -0.8pp',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=9, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '23_gemini_abcd_dedup_truth.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def main():
    print(f'Saving to {OUT}/')
    chart_20_gemini_abcd_r1_main()
    chart_21_gemini_abcd_r1_exact_gt()
    chart_22_gemini_abcd_three_radii()
    chart_23_dedup_truth_abcd()
    chart_18d_gemini_abcd_four_estimators()
    print('[OK] 5 Gemini ABCD charts saved')


if __name__ == '__main__':
    main()
