"""Charts for §5.5.8.4 — three-model radius-0 vs radius-1 comparison."""
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

# Data (from r0 / r1 JSON files)
def load(model_tag):
    base = Path('eval_results/template_analysis')
    r0 = json.load(open(base / f'template_aware_eval__{model_tag}.json'))
    r1 = json.load(open(base / f'r1_template_aware_eval__{model_tag}.json'))
    return r0, r1

def vec(d, group, metric_key):
    return [d['per_field'][f][group][metric_key] /
            max(d['per_field'][f][group]['eligible'], 1) * 100
            for f in FIELDS]

MODELS = [
    ('Sonnet 4.6', 'sonnet46', '#3498DB'),
    ('Opus 4.8', 'opus48', '#9B59B6'),
    ('Gemini Pro Low', 'gemini31prolow', '#F39C12'),
]

R0_HATCH = ''
R1_HATCH = '///'

def autolabel(ax, bars, fmt='{:.1f}'):
    for b in bars:
        h = b.get_height()
        if h <= 0: continue
        ax.annotate(fmt.format(h), xy=(b.get_x() + b.get_width()/2, h),
                    xytext=(0, 2), textcoords='offset points',
                    ha='center', va='bottom', fontsize=7)


def chart_12_hit_winners(group='C'):
    """{group} group: hit ∈ winners. r0 vs r1 across 3 models × 4 fields."""
    data = {}
    for name, tag, _ in MODELS:
        r0, r1 = load(tag)
        data[name] = {'r0': vec(r0, group, 'exact_winner'),
                      'r1': vec(r1, group, 'exact_winner')}

    prompt_desc = {
        'A': 'A prompt: reaction SMILES only (no retrieval, pure LLM)',
        'B': 'B prompt: reaction SMILES + top-5 similar reactions',
        'C': 'C prompt: reaction SMILES + similar reactions + mechanism',
    }[group]

    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(FIELDS))
    w = 0.13
    for i, (name, _, color) in enumerate(MODELS):
        bars0 = ax.bar(x + (i*2 - 2.5)*w, data[name]['r0'], w,
                       label=f'{name} r0', color=color, edgecolor='white', alpha=0.55)
        bars1 = ax.bar(x + (i*2 - 1.5)*w, data[name]['r1'], w,
                       label=f'{name} r1', color=color, edgecolor='black',
                       hatch=R1_HATCH, linewidth=0.8)
        autolabel(ax, bars0); autolabel(ax, bars1)
    ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
    ax.set_ylabel(f'Hit ∈ winners [%] ({group} group)', fontsize=11)
    ax.set_title(f'Three models: hit ∈ winners under radius-0 vs radius-1 ({group} prompt)\n'
                 f'{prompt_desc} | Solid = r0 (~1650 eligible),  Hatched = r1 (~226 eligible)',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=9, ncol=3, framealpha=1.0)
    ax.set_axisbelow(True)
    suffix = {'A': '_A', 'B': '_B', 'C': ''}[group]  # C keeps original name for back-compat
    p = OUT / f'12_three_models_hit_winners_r0_r1{suffix}.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_13_exact_gt(group='C'):
    """{group} group: exact GT. r0 vs r1 across 3 models × 4 fields."""
    data = {}
    for name, tag, _ in MODELS:
        r0, r1 = load(tag)
        data[name] = {'r0': vec(r0, group, 'exact_gt'),
                      'r1': vec(r1, group, 'exact_gt')}
    prompt_desc = {
        'A': 'A prompt: reaction SMILES only (no retrieval, pure LLM)',
        'B': 'B prompt: reaction SMILES + top-5 similar reactions',
        'C': 'C prompt: reaction SMILES + similar reactions + mechanism',
    }[group]

    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(FIELDS))
    w = 0.13
    for i, (name, _, color) in enumerate(MODELS):
        bars0 = ax.bar(x + (i*2 - 2.5)*w, data[name]['r0'], w,
                       label=f'{name} r0', color=color, edgecolor='white', alpha=0.55)
        bars1 = ax.bar(x + (i*2 - 1.5)*w, data[name]['r1'], w,
                       label=f'{name} r1', color=color, edgecolor='black',
                       hatch=R1_HATCH, linewidth=0.8)
        autolabel(ax, bars0); autolabel(ax, bars1)
    ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
    ax.set_ylabel(f'Exact GT match [%] ({group} group, strict)', fontsize=11)
    ax.set_title(f'Three models: exact GT under radius-0 vs radius-1 ({group} prompt)\n'
                 f'{prompt_desc} | Note: r1 numbers are selection-biased toward chemistry-precedented reactions',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper left', fontsize=9, ncol=3, framealpha=1.0)
    ax.set_axisbelow(True)
    # Annotate catalyst column dramatic jump (only meaningful for B/C since A catalyst is 0)
    if group != 'A':
        cat_idx = FIELDS.index('catalysts')
        for i, (name, _, color) in enumerate(MODELS):
            r0v = data[name]['r0'][cat_idx]
            r1v = data[name]['r1'][cat_idx]
            if r1v < 5: continue
            ratio = r1v / max(r0v, 0.01)
            ax.annotate(f'×{ratio:.1f}', xy=(cat_idx + (i*2 - 1.5)*w, r1v),
                        xytext=(0, 16), textcoords='offset points',
                        ha='center', fontsize=10, fontweight='bold', color='red')
    suffix = {'A': '_A', 'B': '_B', 'C': ''}[group]
    p = OUT / f'13_three_models_exact_gt_r0_r1{suffix}.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_14_catalyst_truth():
    """Catalyst dedicated chart: 3 models × ABC × r0/r1, both metrics."""
    cat_idx = FIELDS.index('catalysts')

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    for ax, metric_key, mname in zip(
            axes, ['exact_winner', 'exact_gt'],
            ['Hit ∈ winners (template-aware)', 'Exact GT (strict)']):
        groups = ['A', 'B', 'C']
        x = np.arange(len(groups))
        w = 0.13
        for i, (name, tag, color) in enumerate(MODELS):
            r0, r1 = load(tag)
            r0v = [r0['per_field']['catalysts'][g][metric_key] /
                   max(r0['per_field']['catalysts'][g]['eligible'], 1) * 100 for g in groups]
            r1v = [r1['per_field']['catalysts'][g][metric_key] /
                   max(r1['per_field']['catalysts'][g]['eligible'], 1) * 100 for g in groups]
            b0 = ax.bar(x + (i*2 - 2.5)*w, r0v, w, label=f'{name} r0',
                        color=color, alpha=0.55, edgecolor='white')
            b1 = ax.bar(x + (i*2 - 1.5)*w, r1v, w, label=f'{name} r1',
                        color=color, edgecolor='black', hatch=R1_HATCH, linewidth=0.8)
            autolabel(ax, b0); autolabel(ax, b1)
        ax.set_xticks(x); ax.set_xticklabels(['A pure', 'B +rxn', 'C +rxn+mech'], fontsize=11)
        ax.set_ylabel(f'{mname} [%]', fontsize=11)
        ax.set_title(mname, fontsize=12, fontweight='bold')
        ax.legend(loc='upper left', fontsize=8, ncol=3, framealpha=1.0)
        ax.set_axisbelow(True)
    fig.suptitle('Catalyst: r0 vs r1 reveals models are much closer than r0 suggests',
                 fontsize=13, fontweight='bold', y=1.02)
    p = OUT / '14_catalyst_r0_r1_three_models.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_15_gemini_illusion():
    """Highlight: Gemini A-group electrolyte 54.9 → 24.5 illusion under r1."""
    r0, r1 = load('gemini31prolow')
    fig, ax = plt.subplots(figsize=(10, 5.5))

    # 4 fields × 2 (r0, r1), A group only
    groups_to_show = [('A pure', 'A'), ('B +rxn', 'B'), ('C +rxn+mech', 'C')]
    x = np.arange(len(FIELDS))
    w = 0.27

    for i, (label, g) in enumerate(groups_to_show):
        r0v = vec(r0, g, 'exact_winner')
        r1v = vec(r1, g, 'exact_winner')
        offset = (i - 1) * w
        b0 = ax.bar(x + offset - w/4, r0v, w/2, label=f'{label} r0',
                    color=['#E74C3C','#3498DB','#27AE60'][i], alpha=0.55, edgecolor='white')
        b1 = ax.bar(x + offset + w/4, r1v, w/2, label=f'{label} r1',
                    color=['#E74C3C','#3498DB','#27AE60'][i], edgecolor='black',
                    hatch=R1_HATCH, linewidth=0.8)
        autolabel(ax, b0); autolabel(ax, b1)

    ax.set_xticks(x); ax.set_xticklabels(FIELDS, fontsize=11)
    ax.set_ylabel('Hit ∈ winners [%]', fontsize=11)
    ax.set_title('Gemini 3.1 Pro Low: r0 inflated A-group electrolyte by 30pp\n'
                 '(54.9% → 24.5% under r1 — pure recall not as strong as r0 suggested)',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=9, ncol=3, framealpha=1.0)
    ax.set_axisbelow(True)

    # Annotate the A-group electrolyte drop
    e_idx = FIELDS.index('electrolytes')
    ax.annotate('−30pp drop\nunder r1\n(jewel of r1)',
                xy=(e_idx - w + w/4, 24.5),
                xytext=(e_idx + 0.5, 50),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
                fontsize=10, fontweight='bold', color='red',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFE5E5', edgecolor='red'))
    p = OUT / '15_gemini_a_illusion.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def chart_16_eligible_drop():
    """Show how 7.3x sample drop is consistent across 3 models."""
    fig, ax = plt.subplots(figsize=(8, 4.5))
    names = [m[0] for m in MODELS]
    r0_counts = []; r1_counts = []
    for _, tag, _ in MODELS:
        r0, r1 = load(tag)
        r0_counts.append(r0['n_eligible_records'])
        r1_counts.append(r1['n_eligible_records'])

    x = np.arange(len(names))
    w = 0.35
    b0 = ax.bar(x - w/2, r0_counts, w, label='r0 eligible', color='#16A085', edgecolor='white')
    b1 = ax.bar(x + w/2, r1_counts, w, label='r1 eligible', color='#E67E22', edgecolor='white')
    for b in list(b0) + list(b1):
        ax.annotate(f'{int(b.get_height())}',
                    xy=(b.get_x() + b.get_width()/2, b.get_height()),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', fontsize=10, fontweight='bold')

    for i, (r0c, r1c) in enumerate(zip(r0_counts, r1_counts)):
        ax.annotate(f'÷{r0c/r1c:.1f}', xy=(i, r1c+30),
                    fontsize=11, fontweight='bold', color='red', ha='center')
    ax.set_xticks(x); ax.set_xticklabels(names, fontsize=11)
    ax.set_ylabel('Eligible test reactions', fontsize=11)
    ax.set_title('Sample size cost of radius-1: ~7.3× drop across all models',
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10, framealpha=1.0)
    ax.set_axisbelow(True)
    p = OUT / '16_eligible_drop_r0_r1.png'
    plt.tight_layout(); plt.savefig(p); plt.close()
    print(f'  saved {p}')


def main():
    print(f'Saving to {OUT}/')
    for g in 'ABC':
        chart_12_hit_winners(g)
        chart_13_exact_gt(g)
    chart_14_catalyst_truth()
    chart_15_gemini_illusion()
    chart_16_eligible_drop()
    print('[OK] charts saved')


if __name__ == '__main__':
    main()
