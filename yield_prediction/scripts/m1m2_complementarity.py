"""分析 Model 1 和 Model 2 的互补性"""
import sys, yaml, torch, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0, '.')
sys.path.append('/inspire/hdd/global_user/gelingli-253114010248/pip_packages')

from scripts.eval_condition_models import (
    load_test_data, load_condition_model, load_cvae_model,
    get_logits_key, CONDITION_KEYS
)

with open('configs/config.yaml') as f:
    config = yaml.safe_load(f)

device = 'cuda'
test_loader, vocab, info = load_test_data(config, device)

model1, model_type1, _ = load_condition_model('checkpoints/condition_model/best_condition_model.pt', device)
model2, _, _ = load_cvae_model('checkpoints/condition_model/best_cvae_condition_model.pt', device)

m1_logits = {k: [] for k in CONDITION_KEYS}
m2_logits = {k: [] for k in CONDITION_KEYS}
labels = {k: [] for k in CONDITION_KEYS}

model1.eval(); model2.eval()
with torch.no_grad():
    for batch in test_loader:
        fp = batch['reaction_fp'].to(device)
        p1 = model1(fp)
        p2 = model2.recommend(fp)
        for key in CONDITION_KEYS:
            lk1 = get_logits_key(model_type1, key)
            m1_logits[key].append(p1[lk1].cpu())
            m2_logits[key].append(p2[f'{key}_logits'].cpu())
            labels[key].append(batch[key])

for key in CONDITION_KEYS:
    m1_logits[key] = torch.cat(m1_logits[key], dim=0)
    m2_logits[key] = torch.cat(m2_logits[key], dim=0)
    labels[key] = torch.cat(labels[key], dim=0)

total = labels['anode'].size(0)
W = 85

# ═══ 1. Per-condition complementarity ═══
print('=' * W)
print('  1. Per-Condition Complementarity: When M1 wrong, does M2 get it right?')
print('=' * W)
print()

header = f'{"Condition":<15} {"M1✓":>6} {"M2✓":>6} {"Both✓":>6} {"M1✓M2✗":>7} {"M1✗M2✓":>7} {"Both✗":>7} {"M2 rescue":>10}'
print(header)
print('-' * len(header))

m1_correct_all = np.ones(total, dtype=bool)
m2_correct_all = np.ones(total, dtype=bool)
m2_rescue_any = np.zeros(total, dtype=bool)

for key in CONDITION_KEYS:
    m1_pred = m1_logits[key].argmax(dim=-1).numpy()
    m2_pred = m2_logits[key].argmax(dim=-1).numpy()
    gt = labels[key].numpy()

    m1_ok = (m1_pred == gt)
    m2_ok = (m2_pred == gt)
    both_ok = m1_ok & m2_ok
    m1_only = m1_ok & ~m2_ok
    m2_only = ~m1_ok & m2_ok
    both_wrong = ~m1_ok & ~m2_ok

    m1_wrong_count = (~m1_ok).sum()
    rescue_rate = m2_only.sum() / m1_wrong_count if m1_wrong_count > 0 else 0

    m1_correct_all &= m1_ok
    m2_correct_all &= m2_ok
    m2_rescue_any |= m2_only

    print(f'{key:<15} {m1_ok.sum():>6} {m2_ok.sum():>6} {both_ok.sum():>6} '
          f'{m1_only.sum():>7} {m2_only.sum():>7} {both_wrong.sum():>7} '
          f'{rescue_rate:>9.1%}')

# ═══ 2. Joint complementarity ═══
print()
print('=' * W)
print('  2. Joint Complementarity')
print('=' * W)

oracle_correct = np.ones(total, dtype=bool)
for key in CONDITION_KEYS:
    m1_pred = m1_logits[key].argmax(dim=-1).numpy()
    m2_pred = m2_logits[key].argmax(dim=-1).numpy()
    gt = labels[key].numpy()
    oracle_correct &= ((m1_pred == gt) | (m2_pred == gt))

m1_j = m1_correct_all.sum()
m2_j = m2_correct_all.sum()
oracle_j = oracle_correct.sum()

print(f'  M1 joint exact match (7/7): {m1_j}/{total} = {m1_j/total:.2%}')
print(f'  M2 joint exact match (7/7): {m2_j}/{total} = {m2_j/total:.2%}')
print(f'  Oracle (best of M1,M2):     {oracle_j}/{total} = {oracle_j/total:.2%}')
print(f'  Oracle lift over M1 alone:  +{oracle_j - m1_j} reactions (+{(oracle_j-m1_j)/total:.2%})')
print()

m1_wrong = ~m1_correct_all
m1_wrong_m2_rescues = m1_wrong & m2_rescue_any
print(f'  M1 joint wrong:                     {m1_wrong.sum()}/{total}')
print(f'  Of those, M2 corrects >=1 cond:     {m1_wrong_m2_rescues.sum()}/{m1_wrong.sum()} = {m1_wrong_m2_rescues.sum()/m1_wrong.sum():.2%}')

# ═══ 3. Top-3 rescue ═══
print()
print('=' * W)
print('  3. Top-k Complementarity: Can M2 top-3 rescue M1 top-1 misses?')
print('=' * W)
print()

header2 = f'{"Condition":<15} {"M1 top1":>8} {"M2 top3":>8} {"M1✗&M2t3✓":>12} {"rescue%":>10}'
print(header2)
print('-' * len(header2))

for key in CONDITION_KEYS:
    gt = labels[key]
    m1_ok = (m1_logits[key].argmax(dim=-1) == gt).numpy()
    rk = min(3, m2_logits[key].size(-1))
    m2_top3 = m2_logits[key].topk(rk, dim=-1).indices
    m2_top3_hit = (m2_top3 == gt.unsqueeze(1)).any(dim=1).numpy()
    m1_miss_m2_rescue = (~m1_ok) & m2_top3_hit
    m1_miss_count = (~m1_ok).sum()
    rescue = m1_miss_m2_rescue.sum() / m1_miss_count if m1_miss_count > 0 else 0
    print(f'{key:<15} {m1_ok.mean():>8.3f} {m2_top3_hit.mean():>8.3f} '
          f'{m1_miss_m2_rescue.sum():>12} {rescue:>9.1%}')

# ═══ 4. CVAE 采样 ═══
print()
print('=' * W)
print('  4. CVAE Sampling: Can 10 samples find what M1 misses?')
print('=' * W)

all_fps = []
with torch.no_grad():
    for batch in test_loader:
        all_fps.append(batch['reaction_fp'])
all_fps = torch.cat(all_fps, dim=0)

m1_wrong_indices = np.where(~m1_correct_all)[0]
sample_size = min(300, len(m1_wrong_indices))
sample_idx = np.random.RandomState(42).choice(m1_wrong_indices, sample_size, replace=False)

cvae_rescues_any = 0
cvae_rescues_joint = 0
per_cond_rescue = {k: 0 for k in CONDITION_KEYS}

with torch.no_grad():
    for idx in sample_idx:
        fp = all_fps[idx:idx+1].to(device)
        samples = model2.generate(fp, num_samples=10, temperature=1.0)
        gt_labels = {k: labels[k][idx].item() for k in CONDITION_KEYS}
        m1_preds = {k: m1_logits[k][idx].argmax().item() for k in CONDITION_KEYS}

        any_rescue = False
        any_joint = False
        for s in samples:
            sl = {k: s['labels'][k].item() for k in CONDITION_KEYS}
            if all(sl[k] == gt_labels[k] for k in CONDITION_KEYS):
                any_joint = True
            for k in CONDITION_KEYS:
                if m1_preds[k] != gt_labels[k] and sl[k] == gt_labels[k]:
                    any_rescue = True
                    per_cond_rescue[k] += 1
        if any_rescue:
            cvae_rescues_any += 1
        if any_joint:
            cvae_rescues_joint += 1

print(f'  Evaluated {sample_size} reactions where M1 joint is wrong')
print(f'  CVAE 10-sample rescues >=1 cond:  {cvae_rescues_any}/{sample_size} = {cvae_rescues_any/sample_size:.2%}')
print(f'  CVAE 10-sample finds joint correct: {cvae_rescues_joint}/{sample_size} = {cvae_rescues_joint/sample_size:.2%}')
print()
print(f'  Per-condition rescue count (of {sample_size} M1-wrong samples):')
for k in CONDITION_KEYS:
    print(f'    {k:<15} {per_cond_rescue[k]:>4} ({per_cond_rescue[k]/sample_size:.1%})')

# ═══ 5. Verdict ═══
print()
print('=' * W)
print('  5. VERDICT')
print('=' * W)
oracle_lift_pct = (oracle_j - m1_j) / total * 100
print(f'  Oracle joint lift from M2:       +{oracle_lift_pct:.2f}% absolute')
print(f'  CVAE sampling joint rescue rate: {cvae_rescues_joint/sample_size:.2%}')
marginal = cvae_rescues_any / sample_size * 100
print(f'  CVAE sampling any-cond rescue:   {marginal:.1f}%')
