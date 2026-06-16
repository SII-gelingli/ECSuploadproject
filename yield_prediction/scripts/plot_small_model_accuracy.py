"""Charts for ConditionStage1HierSetV3 abstract condition classifier results."""
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

# Load test results
test_res = json.load(open('yield_prediction/checkpoints/two_stage/experiments/hier_set_v3_smi_fineE_strict_noleak_test.json'))
joint = json.load(open('eval_results/small_model_joint_accuracy.json'))


def autolabel(ax, bars, fmt='{:.1f}'):
    for b in bars:
        h = b.get_height()
        if h <= 0.1: continue
        ax.annotate(fmt.format(h), xy=(b.get_x() + b.get_width()/2, h),
                    xytext=(0, 2), textcoords='offset points',
                    ha='center', va='bottom', fontsize=8)


def chart_24_per_head_accuracy():
    """Per-head top-1/3/5 for 13 abstract single-label heads."""
    HEADS_ORDER = [
        ('anode_material', 'anode\n(15 classes)'),
        ('cathode_material', 'cathode\n(15 classes)'),
        ('cell_class_v3', 'cell type\n(4 classes)'),
        ('electrolyte_cation', 'electrolyte\ncation (23)'),
        ('electrolyte_anion', 'electrolyte\nanion (26)'),
        ('catalyst_class_v3', 'catalyst class\n(49)'),
        ('solvent_class_v3', 'solvent class\n(27)'),
        ('reagent_class_v3', 'reagent class\n(103)'),
        ('anode_fine', 'anode fine\n(43)'),
        ('cathode_fine', 'cathode fine\n(49)'),
    ]
    labels = [l[1] for l in HEADS_ORDER]
    top1 = [test_res[k]['top1']*100 for k,_ in HEADS_ORDER]
    top3 = [test_res[k]['top3']*100 for k,_ in HEADS_ORDER]
    top5 = [test_res[k]['top5']*100 for k,_ in HEADS_ORDER]

    fig, ax = plt.subplots(figsize=(14, 6))
    x = np.arange(len(labels))
    w = 0.27
    b1 = ax.bar(x - w, top1, w, label='top-1', color='#E74C3C', edgecolor='white')
    b2 = ax.bar(x, top3, w, label='top-3', color='#3498DB', edgecolor='white')
    b3 = ax.bar(x + w, top5, w, label='top-5', color='#27AE60', edgecolor='white')
    for bars in [b1, b2, b3]:
        autolabel(ax, bars)
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel('Accuracy [%]', fontsize=11)
    ax.set_title('Small model (ConditionStage1HierSetV3, 10M params) — per-head abstract accuracy on 2,947 test reactions\n'
                 'Strict no-leak test set; class count in parentheses',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10, framealpha=1.0)
    ax.set_axisbelow(True)
    ax.set_ylim(0, 105)
    p = OUT / '24_small_model_per_head_accuracy.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_25_set_head_metrics():
    """3 SMILES set heads: P/R/F1 + coverage."""
    SETS = [('solvent_set', 'solvent set\n(79 SMILES)'),
            ('reagent_set', 'reagent set\n(545 SMILES)'),
            ('catalyst_set', 'catalyst set\n(526 SMILES)')]
    labels = [l[1] for l in SETS]
    p_vals = [test_res[k]['precision']*100 for k,_ in SETS]
    r_vals = [test_res[k]['recall']*100 for k,_ in SETS]
    f1_vals = [test_res[k]['f1']*100 for k,_ in SETS]
    cov5 = [test_res[k]['top5']*100 for k,_ in SETS]
    cov10 = [test_res[k]['top10']*100 for k,_ in SETS]
    cov20 = [test_res[k]['top20']*100 for k,_ in SETS]

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    # Left: P/R/F1
    ax = axes[0]
    x = np.arange(len(labels))
    w = 0.27
    b1 = ax.bar(x - w, p_vals, w, label='precision', color='#3498DB', edgecolor='white')
    b2 = ax.bar(x, r_vals, w, label='recall', color='#9B59B6', edgecolor='white')
    b3 = ax.bar(x + w, f1_vals, w, label='F1', color='#E74C3C', edgecolor='white')
    for bars in [b1, b2, b3]: autolabel(ax, bars)
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylabel('Score [%]', fontsize=11)
    ax.set_title('SMILES set head: P / R / F1', fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10)
    ax.set_axisbelow(True)
    # Right: Top-k coverage
    ax = axes[1]
    b1 = ax.bar(x - w, cov5, w, label='top-5 cov', color='#27AE60', edgecolor='white')
    b2 = ax.bar(x, cov10, w, label='top-10 cov', color='#16A085', edgecolor='white')
    b3 = ax.bar(x + w, cov20, w, label='top-20 cov', color='#1ABC9C', edgecolor='white')
    for bars in [b1, b2, b3]: autolabel(ax, bars)
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylabel('Coverage [%]', fontsize=11)
    ax.set_title('SMILES set head: top-k coverage', fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10)
    ax.set_axisbelow(True)

    fig.suptitle('Small model SMILES set heads — direct multi-element SMILES output',
                 fontsize=13, fontweight='bold', y=1.0)
    p = OUT / '25_small_model_set_heads.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_26_joint_accuracy():
    """Joint accuracy: how strict is requiring ALL fields correct?"""
    SUBSETS = [
        ('electrodes_2', '2 heads\n(anode+cathode)'),
        ('electrochem_setup_3', '3 heads\n(+ cell type)'),
        ('chem_2', '2 heads\n(catalyst+solvent)'),
        ('electrolyte_2', '2 heads\n(cation+anion)'),
        ('no_anion_6', '6 heads\n(- anion)'),
        ('full_core_7', '7 heads\n(full core)'),
    ]
    labels = [l[1] for l in SUBSETS]
    top1 = [joint['subsets_top1'][k] for k,_ in SUBSETS]
    top3 = [joint['subsets_top3'][k] for k,_ in SUBSETS]

    fig, ax = plt.subplots(figsize=(13, 6))
    x = np.arange(len(labels))
    w = 0.35
    b1 = ax.bar(x - w/2, top1, w, label='all heads top-1 correct', color='#E74C3C', edgecolor='white')
    b2 = ax.bar(x + w/2, top3, w, label='all heads top-3 correct', color='#3498DB', edgecolor='white')
    for bars in [b1, b2]: autolabel(ax, bars)

    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylabel('Joint accuracy [%] (all heads in subset correct on same reaction)', fontsize=11)
    ax.set_title('Small model: joint accuracy — how often are ALL heads correct on the same reaction?\n'
                 f'n = {joint["n_total"]} test reactions | Difficulty grows fast as more heads are required',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=11, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '26_small_model_joint_accuracy.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_27_small_vs_llm_field():
    """Direct comparison: small model abstract vs LLM dedup truth on 4 fields."""
    fields = ['electrolytes', 'solvents', 'reagents', 'catalysts']
    # Small model: use the most relevant head per field
    small_class_top1 = [
        test_res['electrolyte_cation']['top1']*100,  # use cation as proxy
        test_res['solvent_class_v3']['top1']*100,
        test_res['reagent_class_v3']['top1']*100,
        test_res['catalyst_class_v3']['top1']*100,
    ]
    small_class_top3 = [
        test_res['electrolyte_cation']['top3']*100,
        test_res['solvent_class_v3']['top3']*100,
        test_res['reagent_class_v3']['top3']*100,
        test_res['catalyst_class_v3']['top3']*100,
    ]
    # Small model set head F1
    small_set_f1 = [
        np.nan,  # no electrolyte set head
        test_res['solvent_set']['f1']*100,
        test_res['reagent_set']['f1']*100,
        test_res['catalyst_set']['f1']*100,
    ]
    # LLM dedup truth (Sonnet C)
    dedup = json.load(open('eval_results/template_analysis/dedup_exact_gt.json'))
    s = dedup['sonnet46']['per_field']
    llm_dedup = [
        s['electrolytes']['hits']['C']/max(s['electrolytes']['eligible'],1)*100,
        s['solvents']['hits']['C']/max(s['solvents']['eligible'],1)*100,
        s['reagents']['hits']['C']/max(s['reagents']['eligible'],1)*100,
        s['catalysts']['hits']['C']/max(s['catalysts']['eligible'],1)*100,
    ]

    fig, ax = plt.subplots(figsize=(13, 6))
    x = np.arange(len(fields))
    w = 0.20
    b1 = ax.bar(x - 1.5*w, small_class_top1, w, label='Small model abstract class top-1', color='#27AE60', edgecolor='white')
    b2 = ax.bar(x - 0.5*w, small_class_top3, w, label='Small model abstract class top-3', color='#16A085', edgecolor='white')
    # Small set F1 (skip electrolyte where NaN)
    valid_idx = [i for i, v in enumerate(small_set_f1) if not np.isnan(v)]
    b3 = ax.bar([x[i]+0.5*w for i in valid_idx], [small_set_f1[i] for i in valid_idx], w,
                label='Small model SMILES set F1', color='#F39C12', edgecolor='white')
    b4 = ax.bar(x + 1.5*w, llm_dedup, w, label='LLM (Sonnet C) dedup truth exact GT', color='#E74C3C', edgecolor='white')
    for bars in [b1, b2, b3, b4]:
        autolabel(ax, bars)

    ax.set_xticks(x); ax.set_xticklabels(fields, fontsize=11)
    ax.set_ylabel('Accuracy / F1 [%]', fontsize=11)
    ax.set_title('Small model (abstract task) vs LLM (SMILES task) — different tasks, different rules\n'
                 'Small model classifies into closed vocab; LLM generates SMILES strings — not apples-to-apples',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=9, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '27_small_vs_llm_per_field.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def main():
    print(f'Saving to {OUT}/')
    chart_24_per_head_accuracy()
    chart_25_set_head_metrics()
    chart_26_joint_accuracy()
    chart_27_small_vs_llm_field()
    print('[OK] 4 small-model charts saved')


if __name__ == '__main__':
    main()
