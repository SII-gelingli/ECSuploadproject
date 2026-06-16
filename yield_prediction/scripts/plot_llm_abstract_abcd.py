"""Charts for LLM ABCD on abstract class taxonomy (SMILES → class mapping)."""
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

OUT = Path('eval_results/template_analysis/charts')

llm = json.load(open('eval_results/template_analysis/llm_abstract_eval__gemini_abcd.json'))
test_res = json.load(open('yield_prediction/checkpoints/two_stage/experiments/hier_set_v3_smi_fineE_strict_noleak_test.json'))
sm_joint = json.load(open('eval_results/small_model_joint_accuracy.json'))

HEADS_PRETTY = {
    'anode_material': 'anode (15)',
    'cathode_material': 'cathode (15)',
    'cell_class_v3': 'cell type (4)',
    'electrolyte_cation': 'cation (23)',
    'electrolyte_anion': 'anion (26)',
    'catalyst_class_v3': 'catalyst (49)',
    'solvent_class_v3': 'solvent (27)',
    'reagent_class_v3': 'reagent (103)',
}
HEADS = list(HEADS_PRETTY.keys())
GROUPS = llm['groups']
GROUP_COLOR = {'A': '#E74C3C', 'B': '#3498DB', 'C': '#27AE60', 'D': '#F39C12'}
GROUP_LABEL = {'A': 'A pure', 'B': 'B +rxn', 'C': 'C +rxn+mech', 'D': 'D +small'}


def autolabel(ax, bars, fmt='{:.1f}'):
    for b in bars:
        h = b.get_height()
        if h <= 0.1: continue
        ax.annotate(fmt.format(h), xy=(b.get_x() + b.get_width()/2, h),
                    xytext=(0, 2), textcoords='offset points',
                    ha='center', va='bottom', fontsize=7)


def chart_28_llm_abcd_per_head():
    """LLM ABCD per-head abstract accuracy."""
    fig, ax = plt.subplots(figsize=(14, 6))
    x = np.arange(len(HEADS))
    w = 0.20
    for i, g in enumerate(GROUPS):
        vals = [llm['per_head'][g][h]['pct'] for h in HEADS]
        bars = ax.bar(x + (i - 1.5)*w, vals, w, label=GROUP_LABEL[g],
                      color=GROUP_COLOR[g], edgecolor='white')
        autolabel(ax, bars)
    ax.set_xticks(x); ax.set_xticklabels([HEADS_PRETTY[h] for h in HEADS], fontsize=10)
    ax.set_ylabel('Abstract class accuracy [%] (top-1, SMILES → class mapping)', fontsize=11)
    ax.set_title('Gemini ABCD on small-model abstract taxonomy — LLM SMILES output mapped to abstract classes\n'
                 'n = 2,898 matched test reactions',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '28_llm_abcd_abstract_per_head.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_29_llm_vs_small_per_head():
    """LLM A/C/D vs small model on per-head abstract."""
    sm_top1 = {h: test_res[h]['top1']*100 for h in HEADS}
    sm_top3 = {h: test_res[h]['top3']*100 for h in HEADS}

    fig, ax = plt.subplots(figsize=(15, 6))
    x = np.arange(len(HEADS))
    w = 0.135
    # Bars: SmallTop1, SmallTop3, LLM-A, LLM-B, LLM-C, LLM-D
    items = [
        ('Small top-1', '#7F8C8D', sm_top1, None),
        ('Small top-3', '#BDC3C7', sm_top3, None),
        ('Gemini A', GROUP_COLOR['A'], None, 'A'),
        ('Gemini B', GROUP_COLOR['B'], None, 'B'),
        ('Gemini C', GROUP_COLOR['C'], None, 'C'),
        ('Gemini D', GROUP_COLOR['D'], None, 'D'),
    ]
    for i, (label, color, data, group) in enumerate(items):
        if data is not None:
            vals = [data[h] for h in HEADS]
        else:
            vals = [llm['per_head'][group][h]['pct'] for h in HEADS]
        offset = (i - 2.5) * w
        bars = ax.bar(x + offset, vals, w, label=label, color=color, edgecolor='white')
        autolabel(ax, bars)

    ax.set_xticks(x); ax.set_xticklabels([HEADS_PRETTY[h] for h in HEADS], fontsize=10)
    ax.set_ylabel('Abstract class accuracy [%]', fontsize=11)
    ax.set_title('Small model vs Gemini ABCD on abstract class taxonomy\n'
                 'Surprising: LLM A often matches or beats small model top-1 (cation/anion/reagent), losing only on solvent and catalyst class top-1',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=8, ncol=3, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '29_llm_vs_small_abstract_per_head.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_30_joint_abstract_abcd():
    """Joint accuracy on abstract subsets for LLM ABCD + small model."""
    SUBSETS = [
        ('core_2', '2 heads\n(anode+cathode)'),
        ('core_3', '3 heads\n(+ cell type)'),
        ('chem_2', '2 heads\n(catalyst+solvent)'),
        ('electrolyte_2', '2 heads\n(cation+anion)'),
        ('no_anion_6', '6 heads\n(- anion)'),
        ('full_7', '7 heads\n(full core)'),
    ]
    SM_SUBSETS = ['electrodes_2','electrochem_setup_3','chem_2','electrolyte_2','no_anion_6','full_core_7']
    labels = [l[1] for l in SUBSETS]

    fig, ax = plt.subplots(figsize=(15, 6.5))
    x = np.arange(len(labels))
    w = 0.135
    items = [
        ('Small top-1', '#7F8C8D', [sm_joint['subsets_top1'][s] for s in SM_SUBSETS]),
        ('Small top-3', '#BDC3C7', [sm_joint['subsets_top3'][s] for s in SM_SUBSETS]),
        ('Gemini A', GROUP_COLOR['A'], [llm['joint']['A'][s] for s,_ in SUBSETS]),
        ('Gemini B', GROUP_COLOR['B'], [llm['joint']['B'][s] for s,_ in SUBSETS]),
        ('Gemini C', GROUP_COLOR['C'], [llm['joint']['C'][s] for s,_ in SUBSETS]),
        ('Gemini D', GROUP_COLOR['D'], [llm['joint']['D'][s] for s,_ in SUBSETS]),
    ]
    for i, (label, color, vals) in enumerate(items):
        offset = (i - 2.5)*w
        bars = ax.bar(x + offset, vals, w, label=label, color=color, edgecolor='white')
        autolabel(ax, bars)

    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylabel('Joint accuracy [%] (all heads correct on same rxn)', fontsize=11)
    ax.set_title('Joint accuracy — abstract subsets — Small model vs Gemini ABCD\n'
                 'LLM matches or beats small-model top-1 across all subsets; small-model top-3 still dominant',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=8, ncol=3, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '30_joint_abstract_small_vs_llm.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def main():
    print(f'Saving to {OUT}/')
    chart_28_llm_abcd_per_head()
    chart_29_llm_vs_small_per_head()
    chart_30_joint_abstract_abcd()
    print('[OK] 3 LLM-abstract charts saved')


if __name__ == '__main__':
    main()
