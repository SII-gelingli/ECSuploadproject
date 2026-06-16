# Test 预测 part 5 — 反应 #2001-#2500

[← 返回 INDEX](INDEX.md)

### Reaction #2001  yield=42.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #9)

```
C=C(c1cc(OC)c(OC)c(OC)c1)C(F)(F)F>>COc1cc(C(O)(CN=[N+]=[N-])C(F)(F)F)cc(OC)c1OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (90.2%) | `carbon_felt` (3.4%) | `carbon_plate` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.2%) | `carbon` (0.5%) | `sacrificial_iron` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (70.9%) | `platinum_plate` (27.8%) | `platinum_foil` (1.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (56.2%) | `ABSENT` (42.7%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (84.9%) | `NBu4` (8.3%) | `K` (4.6%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (49.4%) | `BF4` (34.3%) | `molecular_no_ion` (4.0%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (16.0%) | `ABSENT` (9.5%) | `ketone` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (83.7%) | `Fe_complex` (6.1%) | `tempo_mediator` (2.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (74.8%) | `polar_protic_alcohol` (23.4%) | `cyclic_ether` (0.8%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `CO` (14%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `C[Si](C)(C)N=[N+]=` (56%) | `[N-]=[N+]=[N-].[Na` (28%) | `CC(=O)O` (9%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `[Pt]` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✓ / any ✓ |

---

### Reaction #2002  yield=59.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #10)

```
C=C(c1cccc(-c2ccccc2)c1)C(F)(F)F>>[N-]=[N+]=NCC(O)(c1cccc(-c2ccccc2)c1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.1%) | `platinum` (1.8%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (36.0%) | `graphite_rod` (32.7%) | `carbon_plate` (12.0%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.8%) | `carbon` (0.1%) | `ABSENT` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (49.5%) | `platinum_plate` (44.2%) | `platinum_foil` (6.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (65.2%) | `K` (23.1%) | `ABSENT` (5.4%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (45.5%) | `molecular_no_ion` (27.6%) | `carboxylate` (10.5%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (30.4%) | `ABSENT` (7.2%) | `alkali_other_salt` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (85.7%) | `Mn_complex` (5.7%) | `Pt_complex` (2.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (96.4%) | `polar_protic_alcohol` (1.3%) | `aqueous` (1.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (99%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `OB(O)B(O)O` (44%) | `CC(=O)O` (34%) | `__OTHER__` (29%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (55%) | `CC(C)(C)c1cc(C=N[C` (13%) | `O=S(=O)(O)C(F)(F)F` (8%) | set ✓ / any ✓ |

---

### Reaction #2003  yield=52.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #11)

```
C=C(c1ccc2oc3ccccc3c2c1)C(F)(F)F>>[N-]=[N+]=NCC(N=[N+]=[N-])(c1ccc2oc3ccccc3c2c1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (75.9%) | `platinum` (23.3%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (45.5%) | `carbon_felt` (20.0%) | `platinum_plate` (17.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (74.7%) | `platinum_plate` (25.2%) | `platinum_foil` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (86.5%) | `Li` (12.4%) | `NEt4` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (67.8%) | `BF4` (14.0%) | `carboxylate` (11.5%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (23.0%) | `ABSENT` (6.2%) | `carboxylic_acid` (1.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (71.3%) | `Fe_complex` (10.4%) | `pyridine_organocat` (4.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.9%) | `polar_protic_alcohol` (0.3%) | `halogenated_aliphatic` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (87%) | `CO` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `O=C(O)C(F)(F)F` (67%) | `CC(=O)O` (16%) | `C[Si](C)(C)N=[N+]=` (8%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)NC1CC2(CCCCC` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2004  yield=60.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #12)

```
C=C(c1cccc(-c2ccccc2)c1)C(F)(F)F>>[N-]=[N+]=NCC(N=[N+]=[N-])(c1cccc(-c2ccccc2)c1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `platinum` (1.9%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (98.0%) | `graphite_generic` (0.8%) | `carbon_generic` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `ABSENT` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (82.5%) | `platinum_plate` (10.2%) | `platinum_foil` (7.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (53.9%) | `NBu4` (18.9%) | `ABSENT` (11.2%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (71.4%) | `carboxylate` (7.6%) | `ABSENT` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (63.8%) | `alkali_other_salt` (2.6%) | `carboxylic_acid` (1.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (44.8%) | `Mn_complex` (20.8%) | `Cu_complex` (16.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `polar_protic_acid` (0.4%) | `polar_protic_alcohol` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `CO` (4%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `OB(O)B(O)O` (73%) | `CC[Si](CC)CC` (44%) | `__OTHER__` (36%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (28%) | `O=S(=O)(O)C(F)(F)F` (23%) | `Oc1ccccc1C=NCCN=Cc` (10%) | set ✓ / any ✓ |

---

### Reaction #2005  yield=56.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #13)

```
C=C(c1ccc(C(=O)OC)cc1)C(F)(F)F>>COC(=O)c1ccc(C(CN=[N+]=[N-])(N=[N+]=[N-])C(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (85.2%) | `platinum` (14.6%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (95.2%) | `graphite_generic` (3.1%) | `platinum_generic` (0.7%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `carbon` (0.3%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (87.3%) | `platinum_foil` (11.4%) | `platinum_plate` (1.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (93.3%) | `ABSENT` (6.4%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (82.4%) | `NBu4` (13.3%) | `NEt4` (1.4%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (75.3%) | `molecular_no_ion` (10.1%) | `BF4` (8.7%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (35.4%) | `carboxylic_acid` (2.6%) | `ABSENT` (2.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (53.4%) | `Mn_complex` (26.6%) | `Fe_complex` (8.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.3%) | `polar_protic_alcohol` (0.8%) | `halogenated_aliphatic` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (95%) | `CO` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `[N-]=[N+]=[N-].[Na` (67%) | `CC(=O)O` (48%) | `C[Si](C)(C)N=[N+]=` (23%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (69%) | `CC(=O)NC1CC2(CCCCC` (10%) | `[Br][Mn][Br]` (6%) | set ✓ / any ✓ |

---

### Reaction #2006  yield=65.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #14)

```
C=C(c1ccc2ccccc2c1)C(F)(F)F>>[N-]=[N+]=NCC(O)(c1ccc2ccccc2c1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (79.2%) | `platinum` (15.3%) | `ABSENT` (5.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (30.5%) | `graphite_rod` (14.3%) | `carbon_felt` (12.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (95.6%) | `carbon` (1.9%) | `lead` (0.9%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (72.3%) | `platinum_plate` (25.0%) | `lead_generic` (1.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (64.7%) | `undivided` (33.8%) | `divided` (1.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (76.7%) | `NBu4` (9.7%) | `K` (5.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (51.3%) | `I` (11.4%) | `molecular_no_ion` (9.1%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (10.5%) | `ABSENT` (10.4%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Fe_complex` (0.8%) | `Pt_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (89.8%) | `cyclic_ether` (2.5%) | `polar_protic_acid` (2.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (99%) | `OC(C(F)(F)F)C(F)(F` (4%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `O=C(O)C(F)(F)F` (45%) | `C[Si](C)(C)N=[N+]=` (28%) | `CC(=O)O` (23%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (94%) | `[Pt]` (3%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2007  yield=68.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #15)

```
N.N#CS.C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F>>OC(CN=C=S)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (57.9%) | `carbon_rod` (31.7%) | `graphite_rod` (7.2%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.9%) | `carbon` (0.9%) | `stainless_steel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (95.8%) | `platinum_generic` (3.0%) | `graphite_rod` (0.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (90.0%) | `NEt4` (4.9%) | `Li` (2.3%) | ✗ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (42.3%) | `molecular_no_ion` (37.0%) | `I` (11.9%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (26.4%) | `alkali_other_salt` (2.6%) | `metal_oxide_oxidant` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (98.8%) | `polar_aprotic_sulfoxide` (0.5%) | `halogenated_aliphatic` (0.3%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (100%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2008  yield=64.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #16)

```
C=C(c1ccc(SC)cc1)C(F)(F)F>>CSc1ccc(C(O)(CN=[N+]=[N-])C(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `platinum` (4.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (72.2%) | `graphite_generic` (9.9%) | `carbon_felt` (6.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.9%) | `carbon` (0.5%) | `sacrificial_iron` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (79.2%) | `platinum_plate` (11.1%) | `platinum_foil` (9.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (95.2%) | `ABSENT` (4.6%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (54.8%) | `NBu4` (43.6%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (72.4%) | `BF4` (23.7%) | `PF6` (1.1%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (29.9%) | `ABSENT` (5.7%) | `metal_oxide_oxidant` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (55.5%) | `Cu_complex` (30.6%) | `Fe_complex` (10.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (78.9%) | `polar_protic_acid` (6.4%) | `halogenated_aliphatic` (4.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (99%) | `ClC(Cl)Cl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `C[Si](C)(C)N=[N+]=` (99%) | `O=P([O-])([O-])[O-` (17%) | `CC(=O)O` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `O=S(=O)([O-])C(F)(` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #2009  yield=63.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #17)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F>>[N-]=[N+]=NCC(N=[N+]=[N-])(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.9%) | `platinum` (4.8%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (92.0%) | `carbon_felt` (3.2%) | `carbon_generic` (1.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.1%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (90.4%) | `platinum_plate` (4.8%) | `platinum_foil` (4.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.5%) | `ABSENT` (1.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (89.6%) | `NBu4` (6.0%) | `K` (1.4%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (71.1%) | `molecular_no_ion` (20.1%) | `carboxylate` (2.9%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (64.6%) | `alkali_other_salt` (3.1%) | `ABSENT` (1.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (61.6%) | `Mn_complex` (13.4%) | `Cu_complex` (10.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.8%) | `polar_protic_acid` (5.2%) | `polar_protic_alcohol` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `O` (100%) | `CC#N` (99%) | `CO` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `[N-]=[N+]=[N-].[Na` (72%) | `CC(=O)O` (49%) | `OB(O)B(O)O` (13%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (39%) | `CC(=O)NC1CC2(CCCCC` (13%) | `[Pt]` (10%) | set ✓ / any ✓ |

---

### Reaction #2010  yield=65.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #18)

```
C=C(c1ccc2oc3ccccc3c2c1)C(F)(F)F>>[N-]=[N+]=NCC(O)(c1ccc2oc3ccccc3c2c1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (86.2%) | `platinum` (13.3%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (65.1%) | `carbon_felt` (13.2%) | `platinum_plate` (8.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.9%) | `carbon` (0.1%) | `ABSENT` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (78.9%) | `platinum_generic` (21.1%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (60.1%) | `Li` (37.7%) | `K` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (42.7%) | `BF4` (33.3%) | `carboxylate` (17.6%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (24.1%) | `azide_source` (3.5%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.0%) | `Fe_complex` (2.0%) | `tempo_mediator` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.9%) | `polar_protic_alcohol` (1.3%) | `aqueous` (0.2%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (99%) | `CO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (99%) | `CC(=O)O` (2%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)NC1CC2(CCCCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2011  yield=62.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #19)

```
C=C(c1ccc(OCc2ccc(S(=O)(=O)N(CCC)CCC)cc2)cc1)C(F)(F)F>>CCCN(CCC)S(=O)(=O)c1ccc(COc2ccc(C(CN=[N+]=[N-])(N=[N+]=[N-])C(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.2%) | `platinum` (11.4%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (77.6%) | `platinum_plate` (15.5%) | `carbon_felt` (2.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (77.1%) | `platinum_generic` (22.7%) | `carbon_felt` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (56.3%) | `undivided` (43.6%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NEt4` (43.3%) | `Li` (27.9%) | `NBu4` (27.4%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (90.4%) | `I` (3.2%) | `BF4` (1.4%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `alkali_other_salt` (16.7%) | `azide_source` (8.2%) | `ABSENT` (5.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.1%) | `Pt_complex` (0.6%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `halogenated_aliphatic` (0.4%) | `cyclic_ether` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (98%) | `ClCCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `O=C(O)O.[Na]` (40%) | `__ABSENT__` (14%) | `C[Si](C)(C)N=[N+]=` (14%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)NC1CC2(CCCCC` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #2012  yield=62.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #20)

```
C=C(c1ccc(OCc2ccc(S(=O)(=O)N(CCC)CCC)cc2)cc1)C(F)(F)F>>CCCN(CCC)S(=O)(=O)c1ccc(COc2ccc(C(O)(CN=[N+]=[N-])C(F)(F)F)cc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `platinum` (1.4%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (40.7%) | `carbon_rod` (18.4%) | `graphite_rod` (15.5%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.6%) | `carbon` (0.2%) | `ABSENT` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (90.1%) | `platinum_generic` (9.8%) | `ABSENT` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (60.8%) | `ABSENT` (39.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (39.7%) | `Li` (36.9%) | `NEt4` (19.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (58.7%) | `carboxylate` (16.2%) | `BF4` (10.1%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (17.4%) | `alkali_other_salt` (5.4%) | `azide_source` (3.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.7%) | `polar_protic_alcohol` (0.1%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (97%) | `OC(C(F)(F)F)C(F)(F` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2013  yield=62.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #21)

```
C=C(c1ccc(OC(=O)Cc2ccc3c(c2)C(=O)c2ccccc2OC3)cc1)C(F)(F)F>>[N-]=[N+]=NCC(O)(c1ccc(OC(=O)Cc2ccc3c(c2)C(=O)c2ccccc2OC3)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (49.3%) | `carbon_plate` (22.1%) | `carbon_felt` (7.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.0%) | `carbon` (0.9%) | `sacrificial_iron` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (76.0%) | `platinum_plate` (23.7%) | `graphite_rod` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.0%) | `Li` (20.0%) | `K` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (30.2%) | `I` (24.8%) | `ClO4` (23.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (24.5%) | `azide_source` (3.7%) | `diboron` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `Fe_complex` (0.4%) | `ferrocene_mediator` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (99.1%) | `polar_protic_alcohol` (0.7%) | `ketone` (0.1%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `O` (59%) | `CO` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2014  yield=70.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #22)

```
C=C(c1ccc(OCc2ccccc2)cc1)C(F)(F)F>>[N-]=[N+]=NCC(O)(c1ccc(OCc2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.1%) | `platinum` (3.8%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (57.5%) | `graphite_rod` (10.4%) | `graphite_generic` (7.8%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.9%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (95.3%) | `platinum_plate` (4.7%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (93.8%) | `ABSENT` (6.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (49.1%) | `K` (31.3%) | `NBu4` (15.9%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (33.0%) | `molecular_no_ion` (24.0%) | `carboxylate` (18.6%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (18.9%) | `alkali_other_salt` (6.2%) | `azide_source` (4.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.0%) | `Fe_complex` (0.6%) | `Pt_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (98.5%) | `polar_protic_alcohol` (0.6%) | `cyclic_ether` (0.3%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `O` (100%) | `CC#N` (100%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (99%) | `CC(=O)O` (5%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Pt]` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2015  yield=80.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #23)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.9%) | `platinum` (2.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (49.6%) | `carbon_plate` (26.1%) | `graphite_generic` (7.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.9%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_plate` | `platinum_generic` (79.4%) | `platinum_plate` (19.8%) | `platinum_foil` (0.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `ABSENT` (0.8%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (78.4%) | `K` (13.9%) | `NBu4` (6.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (38.0%) | `molecular_no_ion` (24.1%) | `carboxylate` (22.7%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (38.7%) | `ABSENT` (6.4%) | `alkali_other_salt` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (78.5%) | `Fe_complex` (5.6%) | `Cu_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (84.2%) | `polar_protic_acid` (11.5%) | `polar_protic_alcohol` (2.8%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `O` (100%) | `CC#N` (99%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `CC(=O)O` (53%) | `[N-]=[N+]=[N-].[Na` (39%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (55%) | `[Pt]` (13%) | `CC(=O)NC1CC2(CCCCC` (4%) | set ✓ / any ✓ |

---

### Reaction #2016  yield=66.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #0)

```
Cn1ccc2ccccc21.C=Cc1c(C)cc(C)cc1C>>Cc1cc(C)c(C(C[N+](=O)[O-])c2cn(C)c3ccccc23)c(C)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (89.8%) | `graphite_generic` (10.1%) | `carbon_cloth` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (42.1%) | `platinum` (41.6%) | `carbon` (13.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (51.2%) | `stainless_steel_generic` (39.1%) | `platinum_generic` (5.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `ABSENT` (63.8%) | `NBu4` (20.7%) | `Na` (7.4%) | ✓ |
| 电解质 anion | 26 | `NO3` | `ABSENT` (48.0%) | `I` (36.8%) | `Br` (3.9%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `alkali_sulfonate` (21.7%) | `alkali_other_salt` (10.5%) | `alkali_sulfinate` (6.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (92.5%) | `ABSENT` (6.2%) | `pyridine_organocat` (0.4%) | ✓ |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (99.3%) | `ABSENT` (0.4%) | `polar_protic_alcohol` (0.1%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (97%) | `ClCCl` (19%) | `CCOCC` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Br-].[Li+]` + `__OTHER__` + `O=S(=O)([O-])C(F)(` | `O=O` (100%) | `O=S(=O)([O-])C(F)(` (89%) | `__OTHER__` (73%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl-].[Cl-].[Co+2]` (93%) | `c1ccncc1` (13%) | `[Cl][Co][Cl]` (5%) | set ✗ / any ✗ |

---

### Reaction #2017  yield=65.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #1)

```
Cn1ccc2ccccc21.C=Cc1cccs1>>Cn1cc(C(C[N+](=O)[O-])c2cccs2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (70.9%) | `graphite_generic` (27.3%) | `carbon_cloth` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `carbon` (55.3%) | `platinum` (27.3%) | `stainless_steel` (16.1%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (63.3%) | `stainless_steel_generic` (18.8%) | `graphite_generic` (5.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (92.3%) | `ABSENT` (7.6%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (66.8%) | `Li` (14.6%) | `Na` (12.1%) | ✗ |
| 电解质 anion | 26 | `I` | `ABSENT` (48.3%) | `Cl` (16.4%) | `I` (15.6%) | ✓ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (8.2%) | `o2_oxidant` (7.5%) | `alkali_other_salt` (6.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (50.0%) | `Co_complex` (45.2%) | `pyridine_organocat` (2.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (99.8%) | `ABSENT` (0.1%) | `cyclic_ether` (0.0%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `ClCCl` (64%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (93%) | `O=S(=O)([O-])C(F)(` (91%) | `__OTHER__` (8%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (85%) | `[Cl-].[Cl-].[Co+2]` (8%) | `c1ccncc1` (3%) | set ✓ / any ✓ |

---

### Reaction #2018  yield=68.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc([N+](=O)[O-])cc1.Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc([N+](=O)[O-])cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (81.2%) | `graphite_generic` (18.0%) | `carbon_cloth` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (65.8%) | `carbon` (26.8%) | `stainless_steel` (4.0%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (87.8%) | `platinum_generic` (5.4%) | `reticulated_vitreous_carbon` (1.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (57.3%) | `ABSENT` (16.9%) | `Na` (12.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (72.8%) | `I` (18.1%) | `ABSENT` (2.9%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (14.3%) | `ABSENT` (10.3%) | `alkali_other_salt` (4.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (75.8%) | `ABSENT` (11.8%) | `Mn_complex` (8.0%) | ✓ |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (99.1%) | `ABSENT` (0.6%) | `halogenated_aliphatic` (0.1%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `ClCCl` (29%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=S(=O)([O-])C(F)(` (93%) | `O=O` (42%) | `Fc1c(F)c(F)c(B(c2c` (2%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl-].[Cl-].[Co+2]` (94%) | `[Cl][Co][Cl]` (1%) | `CC(C)(C)c1ccc2[O-]` (0%) | set ✗ / any ✗ |

---

### Reaction #2019  yield=64.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1ccc(-c2ccccc2)cc1.Cc1ccc(S(=O)(=O)n2ccc3ccccc32)cc1>>Cc1ccc(S(=O)(=O)n2cc(C(C[N+](=O)[O-])c3ccc(-c4ccccc4)cc3)c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (97.7%) | `graphite_rod` (1.4%) | `graphite_plate` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (71.6%) | `carbon` (14.2%) | `stainless_steel` (13.4%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_generic` (58.5%) | `platinum_plate` (20.3%) | `stainless_steel_generic` (12.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (75.1%) | `NBu4` (23.5%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Cl` (36.2%) | `I` (33.3%) | `ClO4` (9.3%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (24.5%) | `transition_metal_salt_reagent` (3.9%) | `ABSENT` (3.0%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (53.6%) | `Mn_complex` (26.3%) | `Co_complex` (8.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.6%) | `polar_protic_acid` (0.1%) | `halogenated_aliphatic` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (85%) | `[H+].[OH-]` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (94%) | `__OTHER__` (84%) | `OB(O)B(O)O` (29%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)(O)C(F)(F)F` | `__ABSENT__` (61%) | `[Cl-].[Cl-].[Mn+2]` (7%) | `O=S(=O)(O)C(F)(F)F` (4%) | set ✗ / any ✗ |

---

### Reaction #2020  yield=70.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #4)

```
Cn1ccc2ccccc21.C=Cc1ccc(C#N)cc1>>Cn1cc(C(C[N+](=O)[O-])c2ccc(C#N)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (98.8%) | `graphite_rod` (1.0%) | `carbon_cloth` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `carbon` (51.8%) | `stainless_steel` (41.9%) | `platinum` (6.1%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `graphite_generic` (51.4%) | `stainless_steel_generic` (42.1%) | `platinum_plate` (2.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.3%) | `ABSENT` (1.6%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `protonated_amine` (46.2%) | `ABSENT` (25.7%) | `NBu4` (9.8%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `fluoride_complex` (30.7%) | `I` (26.5%) | `ABSENT` (18.6%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (14.2%) | `inorganic_simple` (12.6%) | `alkali_other_salt` (8.1%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (66.6%) | `Co_complex` (16.2%) | `pyridine_organocat` (8.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.2%) | `ABSENT` (3.5%) | `halogenated_aliphatic` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (5%) | `CN(C)C=O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=S(=O)([O-])C(F)(` (58%) | `O=O` (52%) | `BrCCBr` (21%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (68%) | `c1ccncc1` (58%) | `__OTHER__` (27%) | set ✗ / any ✗ |

---

### Reaction #2021  yield=80.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #5)

```
C=Cc1ccc(-c2ccccc2)cc1.Cn1ccc2ccc(Br)cc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccc(Br)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (57.0%) | `graphite_rod` (39.9%) | `reticulated_vitreous_carbon` (1.0%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (66.6%) | `carbon` (20.0%) | `stainless_steel` (11.9%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (58.1%) | `platinum_generic` (26.1%) | `stainless_steel_generic` (12.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.8%) | `ABSENT` (1.9%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (91.7%) | `Li` (7.0%) | `ABSENT` (0.5%) | ✓ |
| 电解质 anion | 26 | `OTf` | `Cl` (56.1%) | `I` (19.0%) | `BF4` (11.3%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (39.9%) | `alkali_other_salt` (2.8%) | `ABSENT` (2.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (88.6%) | `Co_complex` (8.3%) | `Mn_complex` (1.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (93.8%) | `ABSENT` (4.7%) | `polar_protic_acid` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (78%) | `O` (49%) | `CCOCC` (21%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (99%) | `__OTHER__` (90%) | `CC[Si](CC)CC` (54%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (67%) | `[Cl][Mn][Cl]` (2%) | `c1ccncc1` (2%) | set ✗ / any ✗ |

---

### Reaction #2022  yield=71.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #6)

```
C=Cc1cccs1.Cc1ccc2cc(-c3ccccc3)[nH]c2c1>>Cc1ccc2c(C(C[N+](=O)[O-])c3cccs3)c(-c3ccccc3)[nH]c2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (52.9%) | `graphite_generic` (43.8%) | `carbon_felt` (0.9%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `carbon` (59.7%) | `stainless_steel` (20.0%) | `platinum` (10.1%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (70.1%) | `platinum_generic` (7.1%) | `platinum_plate` (5.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (80.6%) | `undivided` (19.3%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Li` | `Li` (98.4%) | `ABSENT` (0.7%) | `NBu4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `ClO4` (48.3%) | `I` (17.8%) | `molecular_no_ion` (12.2%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `ABSENT` (11.8%) | `transition_metal_salt_reagent` (8.0%) | `alkali_nitrate` (2.8%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (98.7%) | `ionic_organocat` (0.9%) | `Ni_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.2%) | `ketone` (0.4%) | `cyclic_ether` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (7%) | `CC(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `__ABSENT__` (99%) | `__OTHER__` (2%) | `C[Si](C)(C)N=[N+]=` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (99%) | `c1ccncc1` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #2023  yield=71.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #7)

```
Cn1ccc2ccccc21.C=Cc1ccccc1C>>Cc1ccccc1C(C[N+](=O)[O-])c1cn(C)c2ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (50.3%) | `graphite_rod` (47.2%) | `carbon_cloth` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `carbon` (48.8%) | `platinum` (27.0%) | `stainless_steel` (16.9%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (45.3%) | `stainless_steel_generic` (20.2%) | `platinum_generic` (8.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (94.9%) | `ABSENT` (4.8%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (45.6%) | `Li` (43.5%) | `Na` (4.1%) | ✓ |
| 电解质 anion | 26 | `OTf` | `I` (32.7%) | `ABSENT` (28.2%) | `molecular_no_ion` (20.5%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (11.7%) | `ABSENT` (10.0%) | `chloride_anion` (4.0%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (69.1%) | `ABSENT` (23.5%) | `ammonium_PTC_organocat` (2.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.3%) | `ABSENT` (0.3%) | `polar_protic_alcohol` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (3%) | `CC(C)=O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=S(=O)([O-])C(F)(` (90%) | `O=O` (16%) | `Fc1c(F)c(F)c(B(c2c` (5%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (97%) | `[Cl][Co][Cl]` (1%) | `c1ccncc1` (1%) | set ✗ / any ✗ |

---

### Reaction #2024  yield=79.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #8)

```
C=Cc1ccc(-c2ccccc2)cc1.Cn1ccc2c(Br)cccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2c(Br)cccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (77.4%) | `graphite_rod` (16.1%) | `carbon_generic` (1.4%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (53.2%) | `platinum` (31.2%) | `carbon` (10.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (88.0%) | `platinum_generic` (6.5%) | `platinum_plate` (3.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.2%) | `ABSENT` (2.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (78.3%) | `Li` (11.3%) | `ABSENT` (8.7%) | ✓ |
| 电解质 anion | 26 | `OTf` | `Cl` (49.5%) | `Br` (22.5%) | `I` (11.9%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (8.6%) | `transition_metal_salt_reagent` (6.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (84.5%) | `Co_complex` (3.6%) | `pyridine_organocat` (2.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.6%) | `ABSENT` (5.6%) | `polar_protic_acid` (5.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (79%) | `CC(C)=O` (9%) | `FC(F)(F)c1ccccc1` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Li][Br]` + `__OTHER__` | `O=O` (97%) | `__OTHER__` (93%) | `CC[Si](CC)CC` (90%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)(O)C(F)(F)F` | `__ABSENT__` (20%) | `c1ccncc1` (16%) | `__OTHER__` (6%) | set ✗ / any ✗ |

---

### Reaction #2025  yield=76.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #9)

```
C=Cc1ccc(-c2ccccc2)cc1.c1ccc(Cn2ccc3ccccc32)cc1>>O=[N+]([O-])CC(c1ccc(-c2ccccc2)cc1)c1cn(Cc2ccccc2)c2ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `sacrificial_aluminum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (99.0%) | `graphite_rod` (0.8%) | `carbon_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (66.8%) | `carbon` (28.3%) | `nickel` (2.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (79.2%) | `graphite_generic` (9.9%) | `unknown_electrode` (4.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.6%) | `ABSENT` (2.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (61.8%) | `Li` (34.7%) | `Na` (2.1%) | ✓ |
| 电解质 anion | 26 | `OTf` | `I` (73.0%) | `Cl` (15.6%) | `BF4` (2.9%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (43.4%) | `transition_metal_salt_reagent` (4.5%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (69.9%) | `Co_complex` (21.1%) | `Mn_complex` (5.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `ABSENT` (0.2%) | `polar_aprotic_amide` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (9%) | `CCOCC` (7%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (95%) | `O=S(=O)([O-])C(F)(` (66%) | `__OTHER__` (55%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (65%) | `[Cl-].[Cl-].[Mn+2]` (5%) | `__OTHER__` (4%) | set ✗ / any ✗ |

---

### Reaction #2026  yield=76.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #10)

```
Cn1ccc2ccccc21.C=Cc1cc(C)ccc1C>>Cc1ccc(C)c(C(C[N+](=O)[O-])c2cn(C)c3ccccc23)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (52.2%) | `graphite_generic` (45.8%) | `carbon_cloth` (1.0%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (51.8%) | `carbon` (36.8%) | `stainless_steel` (9.9%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_generic` (56.7%) | `platinum_plate` (25.6%) | `reticulated_vitreous_carbon` (7.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (97.3%) | `ABSENT` (2.6%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (44.5%) | `ABSENT` (32.7%) | `Na` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (44.4%) | `I` (25.6%) | `molecular_no_ion` (17.9%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `ABSENT` (11.3%) | `alkali_sulfonate` (5.9%) | `chloride_anion` (4.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (60.7%) | `Co_complex` (35.9%) | `pyridine_organocat` (1.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `ABSENT` (0.4%) | `ketone` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (2%) | `CC(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `__ABSENT__` (96%) | `O=S(=O)([O-])C(F)(` (3%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (99%) | `[Cl-].[Cl-].[Co+2]` (1%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #2027  yield=75.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #11)

```
Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(Cl)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (97.3%) | `graphite_rod` (2.2%) | `carbon_cloth` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (81.8%) | `carbon` (15.5%) | `platinum` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (91.6%) | `graphite_generic` (6.4%) | `platinum_plate` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (66.4%) | `ABSENT` (33.4%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (36.8%) | `Na` (36.0%) | `Li` (13.4%) | ✓ |
| 电解质 anion | 26 | `OTf` | `Cl` (33.4%) | `molecular_no_ion` (23.8%) | `ABSENT` (19.9%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `transition_metal_salt_reagent` (17.7%) | `inorganic_simple` (10.2%) | `alkali_sulfonate` (6.0%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (83.1%) | `Co_complex` (13.7%) | `Mn_complex` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.4%) | `polar_protic_alcohol` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (53%) | `O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (88%) | `O.O.O.O.O.O.O.O.O.` (29%) | `O=S(=O)([O-])C(F)(` (16%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (84%) | `c1ccncc1` (9%) | `__OTHER__` (3%) | set ✗ / any ✗ |

---

### Reaction #2028  yield=78.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #12)

```
c1ccc2[nH]ccc2c1.C=Cc1ccc(-c2ccccc2)cc1>>O=[N]([O-])CC(c1ccc(-c2ccccc2)cc1)c1c[nH]c2ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.7%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (74.5%) | `graphite_rod` (10.4%) | `carbon_rod` (6.9%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (99.7%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_generic` (99.5%) | `platinum_plate` (0.5%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (48.7%) | `ABSENT` (48.1%) | `Li` (2.1%) | ✓ |
| 电解质 anion | 26 | `OTf` | `PF6` (59.2%) | `ABSENT` (32.2%) | `ClO4` (3.4%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `chloride_anion` (7.6%) | `alkali_sulfonate` (6.6%) | `ABSENT` (4.8%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (48.9%) | `Cu_complex` (47.9%) | `Mn_complex` (2.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (71.9%) | `polar_aprotic_amide` (13.7%) | `polar_protic_acid` (9.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (66%) | `O` (37%) | `CN(C)C=O` (28%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Li][Br]` + `__OTHER__` | `O=O` (72%) | `[Cl-].[Na+]` (51%) | `O=S(=O)([O-])C(F)(` (22%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=S(=O)(O)C(F)(F)F` | `[Cl-].[Cl-].[Co+2]` (21%) | `CC1[CH-][C](=O)[Co` (15%) | `COCCOC.[Br][Ni][Br` (6%) | set ✗ / any ✗ |

---

### Reaction #2029  yield=78.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #13)

```
C=Cc1ccc(-c2ccccc2)cc1.Cn1c(-c2ccccc2)cc2ccccc21>>Cn1c(-c2ccccc2)c(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `sacrificial_aluminum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (99.8%) | `graphite_rod` (0.1%) | `carbon_generic` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (92.2%) | `platinum` (3.2%) | `carbon` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (97.7%) | `graphite_generic` (0.9%) | `platinum_generic` (0.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (54.1%) | `NBu4` (32.7%) | `Na` (10.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Br` (40.0%) | `I` (27.2%) | `Cl` (26.8%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `transition_metal_salt_reagent` (15.1%) | `alkali_sulfonate` (11.9%) | `ABSENT` (3.5%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (71.3%) | `Mn_complex` (13.7%) | `Co_complex` (6.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.1%) | `polar_protic_alcohol` (0.4%) | `polar_protic_acid` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (90%) | `CCOCC` (19%) | `O` (18%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (98%) | `__OTHER__` (93%) | `OB(O)B(O)O` (77%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Mn+2]` (34%) | `[Cl][Mn][Cl]` (17%) | `__ABSENT__` (16%) | set ✗ / any ✗ |

---

### Reaction #2030  yield=78.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #14)

```
Cn1ccc2ccccc21.C=Cc1ccc(C(C)(C)C)cc1>>Cn1cc(C(C[N+](=O)[O-])c2ccc(C(C)(C)C)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (83.9%) | `graphite_generic` (15.2%) | `glassy_carbon` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `carbon` (52.6%) | `platinum` (33.6%) | `ABSENT` (7.9%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (56.9%) | `stainless_steel_generic` (12.0%) | `graphite_generic` (10.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.7%) | `ABSENT` (17.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (30.5%) | `Li` (29.1%) | `ABSENT` (23.8%) | ✓ |
| 电解质 anion | 26 | `OTf` | `I` (30.3%) | `OTf` (28.7%) | `ABSENT` (13.6%) | ✓ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (19.3%) | `alkali_other_salt` (5.4%) | `alkali_nitrate` (3.7%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (85.6%) | `ABSENT` (13.1%) | `brønsted_acid_cat` (0.4%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.7%) | `ester` (0.5%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `C1CCOC1` (19%) | `ClCCl` (6%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (100%) | `__OTHER__` (90%) | `OB(O)B(O)O` (64%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `O=S(=O)([O-])C(F)(` (77%) | `[Cl-].[Cl-].[Co+2]` (75%) | `Oc1ccccc1C=NCCN=Cc` (13%) | set ✗ / any ✗ |

---

### Reaction #2031  yield=78.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #15)

```
Cn1ccc2ccccc21.C=Cc1ccc(Br)cc1>>Cn1cc(C(C[N+](=O)[O-])c2ccc(Br)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (91.0%) | `graphite_rod` (8.3%) | `carbon_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `carbon` (82.8%) | `platinum` (10.8%) | `stainless_steel` (5.6%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `graphite_generic` (52.5%) | `stainless_steel_generic` (12.8%) | `platinum_generic` (11.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (74.2%) | `ABSENT` (25.6%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (39.3%) | `Li` (28.9%) | `ABSENT` (13.7%) | ✓ |
| 电解质 anion | 26 | `OTf` | `I` (39.8%) | `Cl` (39.1%) | `molecular_no_ion` (5.5%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (38.5%) | `alkali_other_salt` (7.4%) | `transition_metal_salt_reagent` (2.8%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (91.0%) | `ABSENT` (7.4%) | `Mn_complex` (0.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.0%) | `ABSENT` (0.6%) | `ester` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (36%) | `CCOCC` (6%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (99%) | `__OTHER__` (81%) | `O=S(=O)([O-])C(F)(` (58%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Co+2]` | `[Cl-].[Cl-].[Co+2]` (92%) | `c1ccncc1` (30%) | `[Cl][Co][Cl]` (4%) | set ✓ / any ✓ |

---

### Reaction #2032  yield=72.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #16)

```
Cn1ccc2ccccc21.C=Cc1ccc(C(=O)OC)cc1>>COC(=O)c1ccc(C(C[N+](=O)[O-])c2cn(C)c3ccccc23)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (88.8%) | `graphite_rod` (11.2%) | `carbon_cloth` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (37.0%) | `carbon` (34.4%) | `stainless_steel` (27.2%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (36.8%) | `stainless_steel_generic` (25.2%) | `graphite_generic` (23.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.2%) | `ABSENT` (1.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (40.8%) | `Na` (20.8%) | `ABSENT` (16.6%) | ✗ |
| 电解质 anion | 26 | `OTf` | `I` (42.8%) | `Br` (24.2%) | `Cl` (13.6%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (10.1%) | `alkali_other_salt` (8.5%) | `transition_metal_salt_reagent` (7.2%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (50.1%) | `ABSENT` (40.1%) | `pyridine_organocat` (4.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.4%) | `ABSENT` (0.4%) | `polar_protic_alcohol` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (93%) | `CCOCC` (32%) | `ClCCl` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (99%) | `O=S(=O)([O-])C(F)(` (53%) | `__OTHER__` (37%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (91%) | `c1ccncc1` (84%) | `__OTHER__` (5%) | set ✗ / any ✗ |

---

### Reaction #2033  yield=75.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #17)

```
Cn1ccc2ccccc21.C=Cc1ccccc1Cl>>Cn1cc(C(C[N+](=O)[O-])c2ccccc2Cl)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (69.9%) | `graphite_rod` (28.2%) | `carbon_cloth` (1.6%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (38.6%) | `platinum` (36.0%) | `carbon` (24.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (41.6%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (23.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (86.4%) | `ABSENT` (13.5%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (25.8%) | `Li` (25.1%) | `Na` (20.6%) | ✓ |
| 电解质 anion | 26 | `OTf` | `Cl` (31.6%) | `I` (28.1%) | `ABSENT` (13.1%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `o2_oxidant` (16.5%) | `ABSENT` (8.0%) | `alkali_other_salt` (4.4%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (45.4%) | `Co_complex` (43.5%) | `pyridine_organocat` (3.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.8%) | `ABSENT` (0.1%) | `polar_protic_alcohol` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (95%) | `ClCCl` (59%) | `CC(C)=O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (100%) | `O=S(=O)([O-])C(F)(` (2%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (83%) | `[Cl-].[Cl-].[Co+2]` (9%) | `__OTHER__` (1%) | set ✗ / any ✗ |

---

### Reaction #2034  yield=72.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #18)

```
Cn1ccc2ccccc21.C=Cc1ccccc1Br>>Cn1cc(C(C[N+](=O)[O-])c2ccccc2Br)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (55.9%) | `graphite_rod` (43.7%) | `carbon_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (63.6%) | `stainless_steel` (25.1%) | `carbon` (10.4%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_generic` (54.7%) | `stainless_steel_generic` (31.9%) | `platinum_plate` (11.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.7%) | `ABSENT` (1.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (82.3%) | `Li` (10.9%) | `ABSENT` (3.3%) | ✓ |
| 电解质 anion | 26 | `OTf` | `I` (40.0%) | `Cl` (36.3%) | `OTf` (5.5%) | ✓ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (32.6%) | `alkali_other_salt` (5.3%) | `ABSENT` (4.0%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (79.8%) | `ABSENT` (18.3%) | `pyridine_organocat` (0.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.3%) | `ABSENT` (0.4%) | `polar_protic_alcohol` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (87%) | `CCOCC` (13%) | `FC(F)(F)c1ccccc1` (10%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `O=[N+]([O-])[O-].[` + `__OTHER__` + `[Br-].[Li+]` | `O=O` (100%) | `O=S(=O)([O-])C(F)(` (87%) | `__OTHER__` (48%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (90%) | `c1ccncc1` (39%) | `__OTHER__` (4%) | set ✗ / any ✗ |

---

### Reaction #2035  yield=77.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #19)

```
Cn1ccc2ccccc21.C=Cc1cccc(C=O)c1>>Cn1cc(C(C[N+](=O)[O-])c2cccc(C=O)c2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (99.9%) | `graphite_generic` (0.1%) | `carbon_rod` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (76.4%) | `stainless_steel` (14.0%) | `nickel` (5.5%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `platinum_plate` (58.3%) | `platinum_generic` (23.5%) | `graphite_rod` (8.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (43.4%) | `NBu4` (38.0%) | `K` (7.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `molecular_no_ion` | `I` (90.2%) | `Cl` (5.5%) | `Br` (1.4%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (42.8%) | `ABSENT` (5.4%) | `alkali_other_salt` (2.7%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (82.3%) | `ABSENT` (12.7%) | `pyridine_organocat` (3.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.0%) | `ABSENT` (0.9%) | `polar_protic_alcohol` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `CCOCC` (1%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=S(=O)([O-])C(F)(` (97%) | `O=O` (76%) | `Fc1c(F)c(F)c(B(c2c` (2%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (95%) | `[Cl][Co][Cl]` (4%) | `c1ccncc1` (1%) | set ✗ / any ✗ |

---

### Reaction #2036  yield=75.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #20)

```
Cc1cc2ccccc2n1C.C=Cc1ccc(-c2ccccc2)cc1>>Cc1c(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc2n1C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (86.2%) | `graphite_rod` (10.4%) | `carbon_generic` (1.2%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (70.7%) | `carbon` (19.5%) | `platinum` (5.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (86.7%) | `platinum_generic` (6.9%) | `platinum_plate` (2.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (92.9%) | `ABSENT` (5.6%) | `divided` (1.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (83.9%) | `Li` (13.2%) | `Na` (1.9%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `Cl` (55.6%) | `I` (30.7%) | `Br` (7.3%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (22.7%) | `transition_metal_salt_reagent` (14.3%) | `ABSENT` (3.1%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (69.0%) | `Co_complex` (16.8%) | `Fe_complex` (5.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.9%) | `polar_protic_alcohol` (2.0%) | `cyclic_ether` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `O` (8%) | `ClCCl` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (98%) | `__OTHER__` (83%) | `O=S(=O)([O-])C(F)(` (56%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (36%) | `[Cl-].[Cl-].[Co+2]` (7%) | `[Fe+2].c1cc[cH-]c1` (4%) | set ✗ / any ✗ |

---

### Reaction #2037  yield=72.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #21)

```
C=Cc1ccc(-c2ccccc2)cc1.c1ccc(-n2ccc3ccccc32)cc1>>O=[N+]([O-])CC(c1ccc(-c2ccccc2)cc1)c1cn(-c2ccccc2)c2ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (94.6%) | `graphite_rod` (4.4%) | `graphite_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (93.9%) | `platinum` (3.6%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (90.9%) | `platinum_plate` (7.6%) | `unknown_electrode` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (94.3%) | `ABSENT` (5.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (68.4%) | `Li` (16.2%) | `Na` (11.2%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `Cl` (55.5%) | `Br` (22.7%) | `I` (18.1%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (12.8%) | `transition_metal_salt_reagent` (6.8%) | `ABSENT` (6.5%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (87.2%) | `Co_complex` (6.2%) | `Mn_complex` (5.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.4%) | `halogenated_aliphatic` (1.0%) | `polar_protic_acid` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (83%) | `ClCCl` (56%) | `FC(F)(F)c1ccccc1` (10%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Li][Br]` + `__OTHER__` | `O=O` (99%) | `__OTHER__` (94%) | `CC[Si](CC)CC` (86%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)(O)C(F)(F)F` | `__ABSENT__` (29%) | `c1ccncc1` (12%) | `[Cl-].[Cl-].[Mn+2]` (12%) | set ✗ / any ✗ |

---

### Reaction #2038  yield=77.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #22)

```
Cn1ccc2ccccc21.C=Cc1cccc(Cl)c1>>Cn1cc(C(C[N+](=O)[O-])c2cccc(Cl)c2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (91.6%) | `graphite_rod` (8.3%) | `carbon_cloth` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (51.6%) | `carbon` (30.1%) | `platinum` (17.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (61.2%) | `graphite_generic` (17.5%) | `platinum_generic` (14.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (58.6%) | `Na` (14.1%) | `Li` (12.4%) | ✓ |
| 电解质 anion | 26 | `OTf` | `I` (79.9%) | `Cl` (11.4%) | `molecular_no_ion` (3.4%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (31.5%) | `alkali_other_salt` (7.7%) | `ABSENT` (4.5%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (69.2%) | `Co_complex` (25.4%) | `ammonium_PTC_organocat` (2.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.6%) | `ABSENT` (0.2%) | `polar_protic_alcohol` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (96%) | `ClCCl` (11%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=S(=O)([O-])C(F)(` (82%) | `O=O` (64%) | `O.O.O.O.O.O.O.O.O.` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (88%) | `c1ccncc1` (18%) | `__OTHER__` (8%) | set ✗ / any ✗ |

---

### Reaction #2039  yield=73.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #23)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc2c(ccn2C)c1>>COc1ccc2c(c1)c(C(C[N+](=O)[O-])c1ccc(-c3ccccc3)cc1)cn2C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (92.2%) | `graphite_rod` (7.4%) | `carbon_cloth` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (92.2%) | `carbon` (4.4%) | `platinum` (3.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (97.4%) | `platinum_generic` (1.4%) | `platinum_plate` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (33.5%) | `Li` (26.4%) | `ABSENT` (22.6%) | ✓ |
| 电解质 anion | 26 | `OTf` | `Cl` (96.7%) | `I` (1.1%) | `Br` (0.7%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (12.2%) | `transition_metal_salt_reagent` (8.0%) | `ABSENT` (4.8%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (86.0%) | `Co_complex` (8.5%) | `Fe_complex` (2.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (89.3%) | `ABSENT` (9.2%) | `polar_protic_acid` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (92%) | `ClCCl` (16%) | `FC(F)(F)c1ccccc1` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Li][Br]` + `__OTHER__` | `O=O` (96%) | `O=S(=O)([O-])C(F)(` (69%) | `__OTHER__` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)(O)C(F)(F)F` | `__ABSENT__` (67%) | `c1ccncc1` (2%) | `[Cl][Mn][Cl]` (2%) | set ✗ / any ✗ |

---

### Reaction #2040  yield=75.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #24)

```
Cn1ccc2ccccc21.C=Cc1cccc(Br)c1>>Cn1cc(C(C[N+](=O)[O-])c2cccc(Br)c2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (50.9%) | `graphite_rod` (48.5%) | `carbon_cloth` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (49.4%) | `carbon` (38.2%) | `stainless_steel` (9.9%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_generic` (53.1%) | `platinum_plate` (17.4%) | `stainless_steel_generic` (12.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (54.0%) | `Li` (17.6%) | `Na` (13.9%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `I` (79.9%) | `Cl` (10.3%) | `molecular_no_ion` (4.3%) | ✓ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (80.3%) | `alkali_sulfinate` (2.1%) | `alkali_other_salt` (1.4%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (93.7%) | `ABSENT` (5.6%) | `pyridine_organocat` (0.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.0%) | `ABSENT` (0.8%) | `polar_protic_alcohol` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (94%) | `CCOCC` (22%) | `ClCCl` (16%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Li][Br]` + `__OTHER__` | `O=O` (100%) | `O=S(=O)([O-])C(F)(` (99%) | `__OTHER__` (56%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)(O)C(F)(F)F` | `[Cl-].[Cl-].[Co+2]` (91%) | `c1ccncc1` (44%) | `[Cl][Co][Cl]` (7%) | set ✗ / any ✗ |

---

### Reaction #2041  yield=76.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #25)

```
c1ccc(-c2cc3ccccc3[nH]2)cc1.C=Cc1ccc(-c2ccccc2)cc1>>O=[N+]([O-])CC(c1ccc(-c2ccccc2)cc1)c1c(-c2ccccc2)[nH]c2ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (83.2%) | `carbon_generic` (16.5%) | `graphite_rod` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (60.0%) | `carbon` (31.1%) | `nickel` (4.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (82.4%) | `graphite_generic` (5.4%) | `platinum_generic` (3.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.6%) | `ABSENT` (2.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (92.3%) | `NBu4` (6.8%) | `Na` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `I` (59.1%) | `Cl` (11.4%) | `ClO4` (9.7%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `transition_metal_salt_reagent` (16.4%) | `alkali_sulfonate` (10.3%) | `chloride_anion` (7.0%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (67.2%) | `Mn_complex` (13.3%) | `ionic_organocat` (6.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.1%) | `polar_aprotic_amide` (1.1%) | `polar_protic_acid` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `O` (71%) | `[H+].[OH-]` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (98%) | `__OTHER__` (96%) | `OB(O)B(O)O` (93%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `c1ccncc1` (17%) | `COCCOC.[Br][Ni][Br` (15%) | `[Cl-].[Cl-].[Mn+2]` (9%) | set ✗ / any ✗ |

---

### Reaction #2042  yield=76.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #26)

```
C=Cc1ccccc1F.Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccccc2F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (95.9%) | `graphite_rod` (3.4%) | `carbon_cloth` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `carbon` (54.2%) | `stainless_steel` (33.1%) | `platinum` (11.9%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `graphite_generic` (34.7%) | `stainless_steel_generic` (33.8%) | `platinum_plate` (19.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (30.5%) | `NBu4` (29.8%) | `Li` (27.3%) | ✓ |
| 电解质 anion | 26 | `OTf` | `Cl` (45.6%) | `I` (26.3%) | `ABSENT` (11.9%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `o2_oxidant` (10.9%) | `alkali_sulfonate` (6.0%) | `ABSENT` (5.5%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (53.5%) | `Co_complex` (42.3%) | `ammonium_PTC_organocat` (1.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.6%) | `ABSENT` (0.2%) | `polar_protic_alcohol` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (97%) | `ClCCl` (20%) | `CC(C)=O` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (100%) | `O=S(=O)([O-])C(F)(` (15%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (95%) | `[Cl-].[Cl-].[Co+2]` (3%) | `c1ccncc1` (1%) | set ✗ / any ✗ |

---

### Reaction #2043  yield=81.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #27)

```
C=Cc1ccc(-c2ccccc2)cc1.Cn1ccc2cc(C#N)ccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2cc(C#N)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (99.9%) | `graphite_rod` (0.1%) | `carbon_cloth` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (64.6%) | `platinum` (29.3%) | `carbon` (6.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (81.8%) | `platinum_generic` (15.1%) | `graphite_generic` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (80.8%) | `ABSENT` (15.7%) | `protonated_amine` (1.8%) | ✗ |
| 电解质 anion | 26 | `OTf` | `BF4` (25.3%) | `ABSENT` (25.2%) | `I` (23.6%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (14.3%) | `o2_oxidant` (6.4%) | `inorganic_simple` (6.1%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (98.8%) | `pyridine_organocat` (0.6%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (57.5%) | `polar_aprotic_nitrile` (41.7%) | `halogenated_aliphatic` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `__ABSENT__` (89%) | `CC#N` (14%) | `FC(F)(F)c1ccccc1` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (48%) | `O.O.O.O.O.O.O.O.O.` (48%) | `OC(C(F)(F)F)C(F)(F` (17%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (92%) | `c1ccncc1` (17%) | `__OTHER__` (5%) | set ✗ / any ✗ |

---

### Reaction #2044  yield=81.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #28)

```
C=Cc1cccc(C(F)(F)F)c1.Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2cccc(C(F)(F)F)c2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (86.2%) | `graphite_rod` (13.7%) | `carbon_cloth` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `carbon` (64.3%) | `platinum` (21.4%) | `stainless_steel` (14.0%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `graphite_generic` (39.0%) | `stainless_steel_generic` (22.5%) | `platinum_plate` (21.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (56.2%) | `NEt4` (16.5%) | `Li` (7.6%) | ✓ |
| 电解质 anion | 26 | `OTf` | `I` (72.8%) | `Cl` (14.0%) | `molecular_no_ion` (4.5%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (31.5%) | `alkali_other_salt` (23.6%) | `ammonium_salt` (2.7%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (84.8%) | `Co_complex` (14.1%) | `pyridine_organocat` (0.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.4%) | `ABSENT` (0.4%) | `cyclic_ether` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (92%) | `ClCCl` (21%) | `CC(C)=O` (5%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (94%) | `O=S(=O)([O-])C(F)(` (91%) | `__OTHER__` (19%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (96%) | `c1ccncc1` (22%) | `__OTHER__` (2%) | set ✗ / any ✗ |

---

### Reaction #2045  yield=84.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #29)

```
Cn1ccc2ccccc21.C=Cc1ccc(C)cc1>>Cc1ccc(C(C[N+](=O)[O-])c2cn(C)c3ccccc23)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (79.1%) | `graphite_rod` (19.4%) | `graphite_plate` (0.9%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `carbon` (72.9%) | `stainless_steel` (18.5%) | `platinum` (7.2%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (38.9%) | `platinum_plate` (28.4%) | `graphite_generic` (26.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.2%) | `ABSENT` (2.4%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (38.9%) | `ABSENT` (33.8%) | `NBu4` (11.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `ABSENT` (24.5%) | `Cl` (22.7%) | `molecular_no_ion` (17.7%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (15.8%) | `inorganic_simple` (6.4%) | `transition_metal_salt_reagent` (6.2%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (85.1%) | `Co_complex` (12.0%) | `ammonium_PTC_organocat` (0.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.7%) | `ABSENT` (3.5%) | `polar_protic_alcohol` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (26%) | `ClCCl` (22%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `__OTHER__` | `O=O` (99%) | `__OTHER__` (90%) | `OB(O)B(O)O` (57%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (58%) | `[Cl-].[Cl-].[Mn+2]` (15%) | `c1ccncc1` (14%) | set ✗ / any ✗ |

---

### Reaction #2046  yield=87.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #30)

```
C=Cc1ccc(-c2ccccc2)cc1.Cn1ccc2cc(Br)ccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2cc(Br)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (98.9%) | `graphite_rod` (1.0%) | `carbon_generic` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (58.9%) | `carbon` (29.9%) | `platinum` (9.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (91.2%) | `platinum_generic` (4.8%) | `graphite_generic` (2.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.7%) | `ABSENT` (2.1%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (56.2%) | `ABSENT` (29.7%) | `Li` (8.5%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `Cl` (96.1%) | `I` (1.6%) | `ABSENT` (1.2%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (18.3%) | `iodide_anion` (6.0%) | `o2_oxidant` (2.7%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (93.8%) | `Co_complex` (3.2%) | `Fe_complex` (1.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (77.9%) | `ABSENT` (20.1%) | `polar_protic_alcohol` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (87%) | `O` (11%) | `CC(C)=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (93%) | `__OTHER__` (33%) | `CC[Si](CC)CC` (31%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (85%) | `[Cl][Mn][Cl]` (3%) | `c1ccncc1` (2%) | set ✗ / any ✗ |

---

### Reaction #2047  yield=83.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #31)

```
Cn1ccc2ccccc21.C=Cc1ccc(-c2ccccc2)cc1>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (87.5%) | `graphite_rod` (11.9%) | `carbon_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (46.7%) | `carbon` (36.4%) | `platinum` (14.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (61.3%) | `platinum_plate` (15.7%) | `graphite_generic` (9.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (77.6%) | `ABSENT` (22.2%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (45.5%) | `NBu4` (28.4%) | `ABSENT` (14.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `molecular_no_ion` | `I` (43.1%) | `Cl` (31.9%) | `ABSENT` (6.9%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (27.4%) | `transition_metal_salt_reagent` (10.5%) | `ABSENT` (2.9%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (64.0%) | `ABSENT` (25.4%) | `Mn_complex` (5.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.4%) | `ABSENT` (0.5%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (45%) | `O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (99%) | `__OTHER__` (91%) | `OB(O)B(O)O` (64%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Co+2]` | `[Cl-].[Cl-].[Co+2]` (78%) | `c1ccncc1` (10%) | `[Cl][Co][Cl]` (2%) | set ✓ / any ✓ |

---

### Reaction #2048  yield=82.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #32)

```
C=Cc1ccc(-c2ccccc2)cc1.Cn1ccc2cccc(Br)c21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2cccc(Br)c21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (74.5%) | `graphite_rod` (25.3%) | `carbon_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (74.4%) | `carbon` (23.5%) | `stainless_steel` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_generic` (94.1%) | `platinum_plate` (3.0%) | `stainless_steel_generic` (1.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `ABSENT` (1.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (51.1%) | `NBu4` (44.9%) | `Na` (3.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `I` (69.0%) | `molecular_no_ion` (11.7%) | `OTf` (11.3%) | ✓ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (64.1%) | `ABSENT` (2.0%) | `alkali_other_salt` (1.0%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (81.2%) | `Co_complex` (16.1%) | `Fe_complex` (0.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (1.2%) | `polar_protic_acid` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (96%) | `CCOCC` (25%) | `O` (14%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (99%) | `__OTHER__` (94%) | `CC[Si](CC)CC` (43%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (61%) | `c1ccncc1` (10%) | `__OTHER__` (9%) | set ✗ / any ✗ |

---

### Reaction #2049  yield=82.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #33)

```
Cn1ccc2ccccc21.C=Cc1ccc(C=O)cc1>>Cn1cc(C(C[N+](=O)[O-])c2ccc(C=O)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (86.4%) | `graphite_rod` (13.5%) | `pencil_graphite` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (50.2%) | `carbon` (41.5%) | `nickel` (3.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (65.3%) | `graphite_generic` (26.5%) | `platinum_plate` (2.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.5%) | `ABSENT` (2.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (56.6%) | `NBu4` (26.0%) | `ABSENT` (9.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `I` (45.2%) | `Cl` (17.0%) | `Br` (10.6%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (16.1%) | `transition_metal_salt_reagent` (10.1%) | `ABSENT` (4.6%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (49.0%) | `Co_complex` (44.7%) | `Mn_complex` (2.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (91.5%) | `ABSENT` (8.2%) | `halogenated_aliphatic` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (91%) | `CCOCC` (28%) | `ClCCl` (16%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (98%) | `O=S(=O)([O-])C(F)(` (79%) | `__OTHER__` (70%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (73%) | `[Cl-].[Cl-].[Co+2]` (7%) | `[Cl-].[Cl-].[Mn+2]` (5%) | set ✗ / any ✗ |

---

### Reaction #2050  yield=86.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #34)

```
C=Cc1ccc(F)cc1.Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(F)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (76.3%) | `graphite_rod` (23.5%) | `pencil_graphite` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `carbon` (47.5%) | `stainless_steel` (32.0%) | `platinum` (19.8%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `graphite_generic` (48.4%) | `stainless_steel_generic` (21.2%) | `platinum_plate` (16.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (49.1%) | `Na` (14.7%) | `ABSENT` (10.9%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `I` (81.8%) | `Cl` (5.7%) | `molecular_no_ion` (2.8%) | ✓ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (20.8%) | `alkali_other_salt` (5.3%) | `inorganic_simple` (3.8%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (53.3%) | `ABSENT` (40.8%) | `ionic_organocat` (2.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `ABSENT` (2.8%) | `halogenated_aliphatic` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (44%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (99%) | `O=S(=O)([O-])C(F)(` (80%) | `__OTHER__` (73%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (85%) | `c1ccncc1` (13%) | `[Cl][Co][Cl]` (7%) | set ✗ / any ✗ |

---

### Reaction #2051  yield=85.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #35)

```
C=Cc1ccccc1.Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccccc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (68.6%) | `graphite_rod` (30.0%) | `carbon_cloth` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (47.9%) | `carbon` (41.5%) | `platinum` (5.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (92.1%) | `graphite_generic` (3.4%) | `platinum_plate` (1.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.9%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (36.0%) | `Li` (25.1%) | `NBu4` (15.2%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `I` (35.2%) | `ABSENT` (19.9%) | `Cl` (18.9%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (14.0%) | `transition_metal_salt_reagent` (8.8%) | `o2_oxidant` (4.6%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (47.7%) | `Co_complex` (43.2%) | `ammonium_PTC_organocat` (5.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.5%) | `polar_protic_alcohol` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (87%) | `C1COCCO1` (12%) | `C[N+](=O)[O-]` (5%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (100%) | `OB(O)B(O)O` (63%) | `O=S(=O)([O-])C(F)(` (40%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Co][Cl]` | `c1ccncc1` (91%) | `__OTHER__` (85%) | `__ABSENT__` (7%) | set ✗ / any ✗ |

---

### Reaction #2052  yield=83.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #36)

```
C=Cc1cccc(F)c1.Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2cccc(F)c2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (88.1%) | `graphite_rod` (11.5%) | `carbon_cloth` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (55.8%) | `stainless_steel` (35.7%) | `carbon` (8.2%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_generic` (46.4%) | `stainless_steel_generic` (40.0%) | `platinum_plate` (10.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (62.3%) | `protonated_amine` (12.4%) | `NEt4` (6.9%) | ✗ |
| 电解质 anion | 26 | `OTf` | `I` (90.7%) | `fluoride_complex` (2.2%) | `Cl` (1.7%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (43.2%) | `alkali_other_salt` (8.0%) | `inorganic_simple` (5.1%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (69.8%) | `Co_complex` (13.9%) | `ammonium_PTC_organocat` (7.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.3%) | `ABSENT` (3.3%) | `tfe` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (49%) | `CC(C)=O` (49%) | `ClCCl` (14%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (82%) | `O=S(=O)([O-])C(F)(` (68%) | `[Cl-].[Li+]` (64%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `c1ccncc1` (68%) | `__OTHER__` (66%) | `__ABSENT__` (32%) | set ✗ / any ✗ |

---

### Reaction #2053  yield=85.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #37)

```
C=Cc1ccc(C(F)(F)F)cc1.Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(C(F)(F)F)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (90.2%) | `graphite_rod` (9.5%) | `carbon_cloth` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `carbon` (68.6%) | `platinum` (16.5%) | `stainless_steel` (13.9%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (53.3%) | `graphite_generic` (32.8%) | `stainless_steel_generic` (8.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.7%) | `ABSENT` (1.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (37.1%) | `ABSENT` (31.8%) | `Li` (14.4%) | ✓ |
| 电解质 anion | 26 | `OTf` | `I` (41.4%) | `ABSENT` (21.2%) | `molecular_no_ion` (11.3%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_other_salt` (25.8%) | `alkali_sulfonate` (9.1%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (58.0%) | `Co_complex` (38.8%) | `pyridine_organocat` (2.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `ABSENT` (0.3%) | `halogenated_aliphatic` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (64%) | `CCOCC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `__OTHER__` + `[Li][Br]` | `O=O` (81%) | `__OTHER__` (79%) | `Fc1c(F)c(F)c(B(c2c` (21%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Cl][Co][Cl]` | `__ABSENT__` (82%) | `c1ccncc1` (35%) | `[Cl-].[Cl-].[Mn+2]` (4%) | set ✗ / any ✗ |

---

### Reaction #2054  yield=81.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #38)

```
C=Cc1cccc(C)c1.Cn1ccc2ccccc21>>Cc1cccc(C(C[N+](=O)[O-])c2cn(C)c3ccccc23)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (75.7%) | `graphite_rod` (23.8%) | `carbon_cloth` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (44.2%) | `carbon` (35.3%) | `platinum` (20.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (63.9%) | `platinum_plate` (20.1%) | `graphite_generic` (7.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (37.4%) | `Li` (30.2%) | `Na` (15.1%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `I` (47.2%) | `Cl` (18.2%) | `OTf` (13.7%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (41.1%) | `inorganic_simple` (6.0%) | `alkali_other_salt` (3.4%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (75.6%) | `Co_complex` (23.5%) | `pyridine_organocat` (0.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.0%) | `ABSENT` (0.9%) | `cyclic_ether` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (87%) | `CCOCC` (29%) | `ClCCl` (28%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (100%) | `O=S(=O)([O-])C(F)(` (93%) | `__OTHER__` (82%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)(O)C(F)(F)F` | `__ABSENT__` (71%) | `c1ccncc1` (28%) | `[Cl-].[Cl-].[Co+2]` (12%) | set ✗ / any ✗ |

---

### Reaction #2055  yield=85.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #39)

```
C=Cc1ccc(-c2ccccc2)cc1.Cn1ccc2ccc(C#N)cc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccc(C#N)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (99.1%) | `graphite_rod` (0.9%) | `carbon_generic` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (55.2%) | `platinum` (31.6%) | `carbon` (13.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (74.0%) | `platinum_generic` (14.0%) | `platinum_plate` (6.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `ABSENT` (0.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (66.6%) | `ABSENT` (18.1%) | `Li` (10.5%) | ✓ |
| 电解质 anion | 26 | `OTf` | `Cl` (36.7%) | `BF4` (21.1%) | `I` (13.0%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (18.6%) | `alkali_other_salt` (6.7%) | `inorganic_simple` (5.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (96.0%) | `pyridine_organocat` (2.0%) | `Co_complex` (0.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `ABSENT` (2.8%) | `halogenated_aliphatic` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (90%) | `CC(C)=O` (8%) | `O` (7%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `__OTHER__` | `O.O.O.O.O.O.O.O.O.` (41%) | `O=S(=O)([O-])C(F)(` (19%) | `O=O` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (91%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✗ / any ✗ |

---

### Reaction #2056  yield=88.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_26_8936-8946.json) (反应 idx 在该 JSON 内 = #40)

```
Cn1ccc2ccccc21.C=Cc1ccc2ccccc2c1>>Cn1cc(C(C[N+](=O)[O-])c2ccc3ccccc3c2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (59.5%) | `graphite_rod` (40.3%) | `carbon_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (63.1%) | `carbon` (21.2%) | `platinum` (14.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (76.3%) | `platinum_plate` (7.0%) | `platinum_generic` (6.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.7%) | `ABSENT` (1.1%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (56.8%) | `NBu4` (19.4%) | `Na` (9.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `molecular_no_ion` | `Cl` (44.2%) | `I` (39.2%) | `Br` (6.6%) | ✗ |
| 试剂大类 | 103 | `tetraaryl_borate` | `alkali_sulfonate` (33.0%) | `inorganic_simple` (5.4%) | `transition_metal_salt_reagent` (5.0%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (50.3%) | `ABSENT` (43.1%) | `brønsted_acid_cat` (4.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.2%) | `ABSENT` (2.3%) | `polar_aprotic_sulfoxide` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (97%) | `[H+].[OH-]` (50%) | `ClCCl` (33%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (100%) | `__OTHER__` (99%) | `OB(O)B(O)O` (87%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Co+2]` | `[Cl-].[Cl-].[Co+2]` (73%) | `CC[C@H]1CN2CC[C@H]` (46%) | `c1ccncc1` (15%) | set ✗ / any ✓ |

---

### Reaction #2057  yield=39.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json) (反应 idx 在该 JSON 内 = #0)

```
N#CCCl.CCCCc1ccc(C#Cc2ccccc2C=C2C=C(C(C)(C)C)C(=O)C(C(C)(C)C)=C2)cc1>>CCCCc1ccc(/C(Cl)=C2/c3ccccc3C(CC#N)C23C=C(C(C)(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (90.0%) | `carbon` (7.4%) | `ABSENT` (2.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_disk` | `platinum_disk` (85.0%) | `platinum_generic` (9.3%) | `ABSENT` (1.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.1%) | `stainless_steel` (1.9%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_disk` | `platinum_generic` (55.1%) | `platinum_disk` (38.7%) | `platinum_plate` (4.7%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (66.9%) | `undivided` (32.6%) | `divided` (0.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (88.4%) | `NBu4` (10.4%) | `Na` (0.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (55.8%) | `carboxylate` (18.9%) | `Br` (10.7%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (41.0%) | `tellurium_reagent` (1.7%) | `metal_oxide_oxidant` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.2%) | `organic_neutral_cat` (4.7%) | `ionic_organocat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (95.7%) | `polar_aprotic_nitrile` (3.6%) | `polar_aprotic_amide` (0.2%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` | `CO` (89%) | `ClCCCl` (45%) | `CC#N` (10%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2058  yield=45.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json) (反应 idx 在该 JSON 内 = #1)

```
N#CCBr.CCCc1ccc(C#Cc2ccccc2C=C2C=C(C(C)(C)C)C(=O)C(C(C)(C)C)=C2)cc1>>CCCc1ccc(/C(Br)=C2/c3ccccc3C(CC#N)C23C=C(C(C)(C)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `carbon` (0.9%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_disk` | `platinum_disk` (58.7%) | `platinum_generic` (31.2%) | `platinum_plate` (9.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `stainless_steel` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_disk` | `platinum_generic` (60.8%) | `platinum_disk` (24.0%) | `platinum_plate` (14.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (93.0%) | `ABSENT` (6.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (71.5%) | `NBu4` (18.0%) | `NEt4` (9.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (71.5%) | `ClO4` (9.8%) | `carboxylate` (4.9%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (44.9%) | `primary_amine` (1.6%) | `hydrosilane` (1.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.3%) | `organic_neutral_cat` (0.7%) | `ammonium_PTC_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (76.1%) | `polar_aprotic_nitrile` (22.2%) | `polar_aprotic_amide` (0.8%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` | `ClCCCl` (89%) | `CO` (75%) | `CC#N` (23%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #2059  yield=44.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json) (反应 idx 在该 JSON 内 = #2)

```
N#CCCl.CCCc1ccc(C#Cc2ccccc2C=C2C=C(C(C)(C)C)C(=O)C(C(C)(C)C)=C2)cc1>>CCCc1ccc(/C(Cl)=C2/c3ccccc3C(CC#N)C23C=C(C(C)(C)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (95.1%) | `carbon` (3.0%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_disk` | `platinum_disk` (84.4%) | `platinum_generic` (9.4%) | `platinum_plate` (3.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.6%) | `stainless_steel` (0.7%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_disk` | `platinum_disk` (46.0%) | `platinum_generic` (41.9%) | `platinum_plate` (10.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (64.9%) | `undivided` (34.7%) | `divided` (0.4%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (65.3%) | `NBu4` (32.6%) | `NEt4` (0.9%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (73.3%) | `carboxylate` (11.2%) | `Br` (3.3%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (41.9%) | `metal_oxide_oxidant` (1.6%) | `tellurium_reagent` (1.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.9%) | `organic_neutral_cat` (1.0%) | `ammonium_PTC_organocat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (95.8%) | `polar_aprotic_nitrile` (3.3%) | `polar_aprotic_amide` (0.3%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` | `ClCCCl` (89%) | `CO` (86%) | `CC#N` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2060  yield=41.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json) (反应 idx 在该 JSON 内 = #3)

```
N#CCBr.CCCCc1ccc(C#Cc2ccccc2C=C2C=C(C(C)(C)C)C(=O)C(C(C)(C)C)=C2)cc1>>CCCCc1ccc(/C(Br)=C2/c3ccccc3C(CC#N)C23C=C(C(C)(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (98.5%) | `carbon` (1.2%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_disk` | `platinum_disk` (52.9%) | `platinum_generic` (41.1%) | `platinum_plate` (5.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `stainless_steel` (0.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_disk` | `platinum_generic` (62.5%) | `platinum_disk` (30.7%) | `platinum_plate` (6.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (93.0%) | `ABSENT` (6.3%) | `divided` (0.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (93.9%) | `NBu4` (4.2%) | `NEt4` (1.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (52.9%) | `Br` (13.8%) | `PF6` (11.6%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (43.7%) | `primary_amine` (1.8%) | `hydrosilane` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ammonium_PTC_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (72.6%) | `polar_aprotic_nitrile` (26.3%) | `polar_aprotic_amide` (0.5%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` | `CO` (75%) | `ClCCCl` (53%) | `CC#N` (24%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #2061  yield=41.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json) (反应 idx 在该 JSON 内 = #4)

```
N#CCCl.COc1ccc(C#Cc2ccccc2C=C2C=C(C(C)(C)C)C(=O)C(C(C)(C)C)=C2)cc1>>COc1ccc(/C(Cl)=C2/c3ccccc3C(CC#N)C23C=C(C(C)(C)C)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (91.6%) | `carbon` (7.2%) | `ABSENT` (1.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_disk` | `platinum_disk` (85.1%) | `platinum_generic` (9.2%) | `platinum_plate` (2.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `stainless_steel` (0.5%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_disk` | `platinum_generic` (54.4%) | `platinum_disk` (44.2%) | `platinum_plate` (1.1%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (60.4%) | `undivided` (39.0%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (92.7%) | `NBu4` (5.4%) | `Na` (1.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (84.9%) | `carboxylate` (4.7%) | `Br` (3.3%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (39.7%) | `tellurium_reagent` (1.7%) | `metal_oxide_oxidant` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.5%) | `organic_neutral_cat` (1.0%) | `ionic_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (79.7%) | `polar_aprotic_nitrile` (18.5%) | `polar_aprotic_amide` (0.6%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` | `ClCCCl` (75%) | `CO` (59%) | `CC#N` (40%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2062  yield=57.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json) (反应 idx 在该 JSON 内 = #5)

```
N#CCCl.CCCOc1ccc(C#Cc2ccccc2C=C2C=C(C(C)(C)C)C(=O)C(C(C)(C)C)=C2)cc1>>CCCOc1ccc(/C(Cl)=C2/c3ccccc3C(CC#N)C23C=C(C(C)(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (92.0%) | `carbon` (6.7%) | `ABSENT` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_disk` | `platinum_disk` (93.8%) | `platinum_generic` (4.1%) | `unknown_electrode` (0.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `stainless_steel` (0.3%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_disk` | `platinum_generic` (67.9%) | `platinum_disk` (31.2%) | `platinum_plate` (0.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (79.7%) | `ABSENT` (19.8%) | `divided` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (62.9%) | `NBu4` (35.4%) | `Na` (0.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (78.6%) | `carboxylate` (9.0%) | `Br` (4.8%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (39.7%) | `hydrosilane` (2.1%) | `tellurium_reagent` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (93.0%) | `polar_aprotic_nitrile` (6.4%) | `polar_aprotic_amide` (0.2%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` | `ClCCCl` (86%) | `CO` (72%) | `CC#N` (28%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #2063  yield=54.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json) (反应 idx 在该 JSON 内 = #6)

```
N#CCCl.Cc1cccc(C#Cc2ccccc2C=C2C=C(C(C)(C)C)C(=O)C(C(C)(C)C)=C2)c1>>Cc1cccc(/C(Cl)=C2/c3ccccc3C(CC#N)C23C=C(C(C)(C)C)C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (88.5%) | `carbon` (11.3%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_disk` | `platinum_disk` (80.6%) | `platinum_generic` (8.2%) | `platinum_plate` (5.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `stainless_steel` (0.3%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_disk` | `platinum_generic` (70.0%) | `platinum_disk` (15.4%) | `platinum_plate` (14.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (95.3%) | `ABSENT` (4.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (71.1%) | `NBu4` (27.4%) | `Li` (0.9%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (74.8%) | `carboxylate` (14.4%) | `Br` (3.7%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (34.8%) | `metal_oxide_oxidant` (1.8%) | `tellurium_reagent` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.8%) | `organic_neutral_cat` (0.9%) | `ionic_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (72.2%) | `polar_aprotic_nitrile` (25.4%) | `polar_aprotic_amide` (0.9%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` | `ClCCCl` (88%) | `CC#N` (81%) | `CO` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #2064  yield=58.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json) (反应 idx 在该 JSON 内 = #7)

```
N#CCCl.Cc1ccc(C#Cc2ccccc2C=C2C=C(C(C)(C)C)C(=O)C(C(C)(C)C)=C2)cc1>>Cc1ccc(/C(Cl)=C2/c3ccccc3C(CC#N)C23C=C(C(C)(C)C)C(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (85.5%) | `carbon` (13.7%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_disk` | `platinum_disk` (86.0%) | `platinum_generic` (6.9%) | `graphite_generic` (4.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `stainless_steel` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_disk` | `platinum_generic` (60.6%) | `platinum_disk` (36.6%) | `platinum_plate` (2.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.4%) | `ABSENT` (15.8%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (85.6%) | `NBu4` (12.6%) | `Na` (0.9%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (75.7%) | `Br` (7.7%) | `carboxylate` (5.5%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (31.1%) | `tellurium_reagent` (1.9%) | `metal_oxide_oxidant` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.3%) | `organic_neutral_cat` (0.7%) | `ionic_organocat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (94.5%) | `polar_aprotic_nitrile` (3.8%) | `polar_aprotic_amide` (1.0%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` | `CO` (89%) | `ClCCCl` (84%) | `O` (23%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #2065  yield=65.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json) (反应 idx 在该 JSON 内 = #8)

```
N#CCI.CCCCc1ccc(C#Cc2ccccc2C=C2C=C(C(C)(C)C)C(=O)C(C(C)(C)C)=C2)cc1>>CCCCc1ccc(/C(I)=C2/c3ccccc3C(CC#N)C23C=C(C(C)(C)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (98.2%) | `carbon` (1.4%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_disk` | `platinum_disk` (99.3%) | `platinum_generic` (0.6%) | `platinum_plate` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.7%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_disk` | `platinum_disk` (95.4%) | `platinum_generic` (4.5%) | `platinum_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.2%) | `ABSENT` (1.6%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `K` (97.4%) | `NBu4` (1.4%) | `Na` (0.8%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `I` (84.8%) | `Br` (6.1%) | `carboxylate` (4.0%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (44.2%) | `primary_amine` (1.7%) | `tellurium_reagent` (1.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `ionic_organocat` (0.3%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (99.3%) | `polar_aprotic_nitrile` (0.5%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` | `CO` (100%) | `ClCCCl` (95%) | `O` (16%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2066  yield=61.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json) (反应 idx 在该 JSON 内 = #9)

```
N#CCBr.CCc1ccc(C#Cc2ccccc2C=C2C=C(C(C)(C)C)C(=O)C(C(C)(C)C)=C2)cc1>>CCc1ccc(/C(Br)=C2/c3ccccc3C(CC#N)C23C=C(C(C)(C)C)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (97.3%) | `ABSENT` (2.1%) | `carbon` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_disk` | `platinum_generic` (49.4%) | `platinum_disk` (45.1%) | `platinum_plate` (4.4%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.3%) | `ABSENT` (1.1%) | `stainless_steel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_disk` | `platinum_disk` (59.0%) | `platinum_generic` (38.4%) | `platinum_plate` (1.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.2%) | `divided` (1.4%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (98.3%) | `NBu4` (1.3%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (60.9%) | `ClO4` (14.8%) | `Br` (6.7%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (42.1%) | `hydrosilane` (2.6%) | `primary_amine` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `organic_neutral_cat` (0.1%) | `Pt_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (49.3%) | `polar_protic_alcohol` (48.8%) | `polar_aprotic_amide` (1.4%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (91%) | `ClCCCl` (58%) | `CO` (9%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #2067  yield=71.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json) (反应 idx 在该 JSON 内 = #10)

```
N#CCCl.CCc1ccc(C#Cc2ccccc2C=C2C=C(C(C)(C)C)C(=O)C(C(C)(C)C)=C2)cc1>>CCc1ccc(/C(Cl)=C2/c3ccccc3C(CC#N)C23C=C(C(C)(C)C)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (87.7%) | `ABSENT` (8.9%) | `carbon` (3.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_disk` | `platinum_disk` (81.8%) | `platinum_generic` (12.1%) | `unknown_electrode` (2.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.3%) | `ABSENT` (2.3%) | `stainless_steel` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_disk` | `platinum_disk` (67.9%) | `platinum_generic` (29.8%) | `ABSENT` (1.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (72.4%) | `ABSENT` (25.9%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `K` (96.5%) | `NBu4` (2.8%) | `Na` (0.4%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `I` (73.7%) | `carboxylate` (8.6%) | `Br` (6.7%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (40.8%) | `tellurium_reagent` (1.7%) | `metal_oxide_oxidant` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `ionic_organocat` (0.3%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (88.9%) | `polar_aprotic_nitrile` (9.9%) | `polar_aprotic_amide` (0.8%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` | `CO` (68%) | `ClCCCl` (41%) | `CC#N` (31%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #2068  yield=72.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_30_10725-10731.json) (反应 idx 在该 JSON 内 = #11)

```
N#CCBr.CCCOc1ccc(C#Cc2ccccc2C=C2C=C(C(C)(C)C)C(=O)C(C(C)(C)C)=C2)cc1>>CCCOc1ccc(/C(Br)=C2/c3ccccc3C(CC#N)C23C=C(C(C)(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (97.9%) | `carbon` (1.8%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_disk` | `platinum_disk` (87.3%) | `platinum_generic` (11.6%) | `platinum_plate` (0.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `ABSENT` (0.1%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_disk` | `platinum_generic` (72.9%) | `platinum_disk` (26.6%) | `platinum_plate` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.4%) | `ABSENT` (1.3%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `K` (72.5%) | `NBu4` (25.4%) | `NEt4` (1.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `I` (73.7%) | `ClO4` (9.1%) | `Br` (5.1%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (42.0%) | `hydrosilane` (3.3%) | `metal_oxide_oxidant` (1.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `organic_neutral_cat` (0.1%) | `ammonium_PTC_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (80.3%) | `polar_aprotic_nitrile` (18.8%) | `polar_aprotic_amide` (0.4%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` | `ClCCCl` (94%) | `CO` (67%) | `CC#N` (33%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #2069  yield=18.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #0)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1>>O=C1C(CC(F)(F)F)CCN1C(=O)C(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (65.1%) | `graphite_rod` (33.9%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (47.9%) | `carbon` (32.6%) | `nickel` (18.4%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (87.0%) | `graphite_generic` (4.4%) | `nickel_generic` (2.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.4%) | `NEt4` (3.3%) | `ABSENT` (1.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (97.2%) | `ClO4` (1.5%) | `PF6` (0.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `alkali_phosphate` (3.9%) | `alkali_carbonate` (2.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (92.1%) | `polar_aprotic_nitrile` (6.5%) | `aqueous` (0.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` + `O` | `O` (100%) | `ClCCl` (99%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (98%) | `CC(=O)[O-].[Na+]` (1%) | `O=P([O-])(O)O.[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `Cc1cc(O[C@@H](C)C(` (0%) | set ✓ / any ✓ |

---

### Reaction #2070  yield=28.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #1)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1cccs1)c1cccs1>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1cccs1)c1cccs1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (99.9%) | `graphite_generic` (0.1%) | `carbon_felt` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.8%) | `NEt4` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (99.3%) | `PF6` (0.2%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.6%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (95.4%) | `polar_aprotic_nitrile` (4.4%) | `ketone` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `ClCCl` (99%) | `O` (99%) | `CC#N` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `O=P([O-])(O)O.[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |

---

### Reaction #2071  yield=25.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #2)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccccc1)C(C)c1ccccc1>>C/C(=C(/C(=O)N1CCC(CC(F)(F)F)C1=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (49.4%) | `graphite_rod` (46.4%) | `carbon_felt` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (85.8%) | `nickel` (12.8%) | `carbon` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (46.3%) | `platinum_generic` (44.8%) | `nickel_generic` (6.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.2%) | `Li` (4.4%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (92.4%) | `ClO4` (6.8%) | `PF6` (0.2%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (9.2%) | `alkali_phosphate` (3.1%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (99.0%) | `polar_aprotic_nitrile` (0.9%) | `aqueous` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (100%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (99%) | `CC(=O)[O-].[Na+]` (1%) | `O=P([O-])(O)O.[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `Cc1cc(O[C@@H](C)C(` (0%) | set ✓ / any ✓ |

---

### Reaction #2072  yield=25.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #3)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccccc1)C(C)c1ccccc1>>CC(=C(C(=O)N1CCC(CC(F)(F)F)C1=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (49.4%) | `graphite_rod` (46.4%) | `carbon_felt` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (85.8%) | `nickel` (12.8%) | `carbon` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (46.3%) | `platinum_generic` (44.8%) | `nickel_generic` (6.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.2%) | `Li` (4.4%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (92.4%) | `ClO4` (6.8%) | `PF6` (0.2%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (9.2%) | `alkali_phosphate` (3.1%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (99.0%) | `polar_aprotic_nitrile` (0.9%) | `aqueous` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (100%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (99%) | `CC(=O)[O-].[Na+]` (1%) | `O=P([O-])(O)O.[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `Cc1cc(O[C@@H](C)C(` (0%) | set ✓ / any ✓ |

---

### Reaction #2073  yield=40.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #4)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1cc(C)ccc1C)c1cc(C)ccc1C>>Cc1ccc(C)c(C2(c3cc(C)ccc3C)N=C3C(CC(F)(F)F)CCN3C2=O)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (99.2%) | `carbon_felt` (0.4%) | `graphite_generic` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (99.2%) | `nickel` (0.7%) | `carbon` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.2%) | `ABSENT` (21.9%) | `Na` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (94.8%) | `ABSENT` (4.7%) | `molecular_no_ion` (0.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.4%) | `nitrite_alkyl` (2.7%) | `metal_oxide_oxidant` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (99.5%) | `polar_aprotic_nitrile` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (99%) | `ClCCl` (87%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=P([O-])(O)O.[K+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `Cc1cc(O[C@@H](C)C(` (0%) | set ✓ / any ✓ |

---

### Reaction #2074  yield=35.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #5)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (97.9%) | `graphite_generic` (2.0%) | `carbon_felt` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (93.4%) | `nickel` (3.6%) | `carbon` (2.3%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.1%) | `graphite_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.8%) | `ABSENT` (1.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (95.7%) | `Br` (1.6%) | `ABSENT` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.3%) | `alkali_bicarbonate` (3.5%) | `metal_oxide_oxidant` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (97.5%) | `polar_aprotic_nitrile` (2.2%) | `ketone` (0.2%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` + `O` | `ClCCl` (100%) | `O` (100%) | `O=C(O)C(F)(F)F` (25%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (98%) | `CC(=O)[O-].[Na+]` (1%) | `O=P([O-])(O)O.[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccc(-c2ccccn2)nc` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2075  yield=32.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #5)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (97.9%) | `graphite_generic` (2.0%) | `carbon_felt` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (93.4%) | `nickel` (3.6%) | `carbon` (2.3%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.1%) | `graphite_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.8%) | `ABSENT` (1.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.7%) | `Br` (1.6%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ammonium_salt` | `ABSENT` (11.3%) | `alkali_bicarbonate` (3.5%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `halogenated_aliphatic` (97.5%) | `polar_aprotic_nitrile` (2.2%) | `ketone` (0.2%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` + `O` | `ClCCl` (100%) | `O` (100%) | `O=C(O)C(F)(F)F` (25%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (98%) | `CC(=O)[O-].[Na+]` (1%) | `O=P([O-])(O)O.[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccc(-c2ccccn2)nc` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2076  yield=35.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #5)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (97.9%) | `graphite_generic` (2.0%) | `carbon_felt` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (93.4%) | `nickel` (3.6%) | `carbon` (2.3%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.1%) | `graphite_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.8%) | `ABSENT` (1.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (95.7%) | `Br` (1.6%) | `ABSENT` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.3%) | `alkali_bicarbonate` (3.5%) | `metal_oxide_oxidant` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (97.5%) | `polar_aprotic_nitrile` (2.2%) | `ketone` (0.2%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` + `O` | `ClCCl` (100%) | `O` (100%) | `O=C(O)C(F)(F)F` (25%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (98%) | `CC(=O)[O-].[Na+]` (1%) | `O=P([O-])(O)O.[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccc(-c2ccccn2)nc` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2077  yield=35.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #8)

```
O=S(=O)(O)C(F)(F)F.[Na+].C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (96.9%) | `graphite_generic` (1.1%) | `glassy_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (97.0%) | `carbon` (2.0%) | `nickel` (0.7%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (99.8%) | `zinc_generic` (0.1%) | `platinum_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.4%) | `ABSENT` (0.9%) | `K` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (98.5%) | `ABSENT` (0.4%) | `Br` (0.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_phosphate` (18.2%) | `ABSENT` (3.9%) | `carboxylic_acid` (3.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.2%) | `Mn_complex` (1.2%) | `ferrocene_mediator` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (89.0%) | `polar_aprotic_nitrile` (9.7%) | `ketone` (0.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` + `O` | `O` (100%) | `ClCCl` (99%) | `CC#N` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=P([O-])(O)O.[K+]` (97%) | `CCCC[N+](CCCC)(CCC` (1%) | `O=C([O-])O.[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)NC1CC2(CCCCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2078  yield=43.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #9)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(Cc1ccccc1)c1ccc(OC)cc1>>COc1ccc(/C(=C\c2ccccc2)C(=O)N2CCC(CC(F)(F)F)C2=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (70.4%) | `carbon_generic` (17.8%) | `carbon_felt` (6.0%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (64.4%) | `nickel` (34.0%) | `carbon` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (84.0%) | `platinum_generic` (13.0%) | `nickel_generic` (1.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.8%) | `ABSENT` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (99.5%) | `PF6` (0.3%) | `ABSENT` (0.1%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (7.0%) | `hcl` (3.5%) | `alkali_phosphate` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (82.4%) | `polar_aprotic_amide` (10.8%) | `polar_aprotic_nitrile` (2.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (99%) | `ClCCl` (88%) | `CC(=O)O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (79%) | `CC(=O)[O-].[Na+]` (20%) | `[Cl-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2079  yield=59.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #10)

```
O=S(O)C(F)(F)F.[Na].C=CCC(C)(C)CN(C#N)C(=O)C(c1ccccc1)c1ccccc1>>CC1(C)CC(CC(F)(F)F)C2=NC(c3ccccc3)(c3ccccc3)C(=O)N2C1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (80.7%) | `graphite_rod` (16.5%) | `graphite_felt` (1.6%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `nickel` (68.0%) | `platinum` (26.4%) | `carbon` (2.9%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (77.6%) | `nickel_plate` (10.7%) | `stainless_steel_generic` (3.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (83.7%) | `ABSENT` (8.3%) | `NEt4` (6.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (75.4%) | `Br` (12.2%) | `ABSENT` (8.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.8%) | `alkali_other_salt` (2.8%) | `electrophilic_N_F` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (96.6%) | `polar_aprotic_nitrile` (2.8%) | `ketone` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (97%) | `ClCCl` (90%) | `CC#N` (7%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccc(-c2ccccn2)nc` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2080  yield=51.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #11)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(Cc1ccccc1)c1ccc(C)cc1>>Cc1ccc(/C(=C\c2ccccc2)C(=O)N2CCC(CC(F)(F)F)C2=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (90.7%) | `carbon_generic` (4.7%) | `graphite_generic` (4.0%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `nickel` (70.2%) | `platinum` (29.4%) | `carbon` (0.3%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (61.8%) | `platinum_generic` (13.6%) | `nickel_generic` (11.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.1%) | `ABSENT` (0.6%) | `Li` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (99.5%) | `ABSENT` (0.2%) | `PF6` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (11.5%) | `amidine_guanidine_base` (3.2%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (75.1%) | `ABSENT` (9.7%) | `polar_aprotic_amide` (7.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (97%) | `ClCCl` (65%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2081  yield=54.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #12)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1c(C)cc(C)cc1C)c1c(C)cc(C)cc1C>>Cc1cc(C)c(C2(c3c(C)cc(C)cc3C)N=C3C(CC(F)(F)F)C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (99.7%) | `graphite_generic` (0.3%) | `carbon_felt` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (99.2%) | `carbon` (0.5%) | `nickel` (0.2%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (99.2%) | `platinum_generic` (0.7%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (59.3%) | `NBu4` (39.1%) | `Na` (1.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (69.3%) | `ABSENT` (30.1%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.7%) | `alkali_other_salt` (2.7%) | `alkali_bicarbonate` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (99.3%) | `polar_aprotic_nitrile` (0.6%) | `aqueous` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `ClCCl` (99%) | `O` (99%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O=P([O-])(O)O.[K+]` (1%) | `CC(=O)[O-].[Na+]` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2082  yield=57.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #13)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccc(C)cc1C)c1ccc(C)cc1C>>Cc1ccc(C2(c3ccc(C)cc3C)N=C3C(CC(F)(F)F)CCN3C2=O)c(C)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (98.9%) | `graphite_generic` (1.0%) | `carbon_rod` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (94.0%) | `nickel` (4.7%) | `carbon` (1.2%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (99.4%) | `nickel_plate` (0.5%) | `platinum_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.5%) | `ABSENT` (7.5%) | `Na` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (97.1%) | `ABSENT` (2.4%) | `Br` (0.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (20.9%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (99.4%) | `polar_aprotic_nitrile` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (99%) | `ClCCl` (93%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=P([O-])(O)O.[K+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Cc1cc(O[C@@H](C)C(` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2083  yield=53.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #14)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(Cc1ccccc1)c1ccc(Cl)cc1>>O=C(/C(=C/c1ccccc1)c1ccc(Cl)cc1)N1CCC(CC(F)(F)F)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (53.3%) | `carbon_generic` (25.9%) | `graphite_generic` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (57.2%) | `nickel` (40.8%) | `carbon` (1.2%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (87.2%) | `platinum_generic` (5.4%) | `nickel_generic` (5.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.1%) | `ABSENT` (0.8%) | `NEt4` (0.0%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (99.7%) | `ABSENT` (0.2%) | `PF6` (0.1%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (6.9%) | `ferrocene_mediator` (3.5%) | `amidine_guanidine_base` (3.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `ferrocene_mediator` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (88.0%) | `polar_aprotic_amide` (5.9%) | `polar_aprotic_nitrile` (2.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (97%) | `ClCCl` (91%) | `[H+].[OH-]` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (99%) | `CC(=O)[O-].[Na+]` (1%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2084  yield=61.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #15)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccccc1)C(C)c1ccccc1>>C/C(=C(\C(=O)N1CCC(CC(F)(F)F)C1=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (49.4%) | `graphite_rod` (46.4%) | `carbon_felt` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (85.8%) | `nickel` (12.8%) | `carbon` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (46.3%) | `platinum_generic` (44.8%) | `nickel_generic` (6.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.2%) | `Li` (4.4%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (92.4%) | `ClO4` (6.8%) | `PF6` (0.2%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (9.2%) | `alkali_phosphate` (3.1%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (99.0%) | `polar_aprotic_nitrile` (0.9%) | `aqueous` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (100%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (99%) | `CC(=O)[O-].[Na+]` (1%) | `O=P([O-])(O)O.[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `Cc1cc(O[C@@H](C)C(` (0%) | set ✓ / any ✓ |

---

### Reaction #2085  yield=69.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #16)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccc(Br)cc1)c1ccc(Br)cc1>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccc(Br)cc1)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (99.8%) | `graphite_generic` (0.1%) | `carbon_felt` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (95.8%) | `nickel` (2.9%) | `carbon` (1.0%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (99.7%) | `platinum_generic` (0.2%) | `graphite_rod` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (89.6%) | `NEt4` (5.7%) | `ABSENT` (4.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (98.4%) | `ABSENT` (0.9%) | `Br` (0.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.9%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (88.9%) | `polar_aprotic_nitrile` (10.4%) | `ketone` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC#N` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=P([O-])(O)O.[K+]` (0%) | `O=C([O-])[O-].[Na+` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2086  yield=68.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #17)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C1c2ccccc2Oc2ccccc21>>O=C1N2CCC(CC(F)(F)F)C2=NC12c1ccccc1Oc1ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (82.8%) | `graphite_generic` (16.9%) | `graphite_felt` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.6%) | `nickel` (2.4%) | `stainless_steel` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (99.1%) | `platinum_generic` (0.8%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.0%) | `ABSENT` (1.2%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (98.7%) | `ABSENT` (0.5%) | `PF6` (0.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.8%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (99.7%) | `polar_aprotic_nitrile` (0.1%) | `hfip` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `ClCCl` (100%) | `O` (99%) | `CC(=O)O` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (96%) | `CC(=O)[O-].[Na+]` (3%) | `O=P([O-])(O)O.[K+]` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2087  yield=68.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #18)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccc(C)cc1)C(c1ccccc1)c1ccccc1>>Cc1ccc(C(C(=O)N2CCC(CC(F)(F)F)C2=O)=C(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (76.0%) | `graphite_generic` (23.5%) | `carbon_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (88.3%) | `nickel` (6.0%) | `carbon` (5.7%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (86.3%) | `platinum_generic` (10.8%) | `graphite_generic` (1.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.1%) | `Li` (4.3%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (92.1%) | `ClO4` (6.7%) | `PF6` (0.4%) | ✓ |
| 试剂大类 | 103 | `ammonium_salt` | `ABSENT` (11.9%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `brønsted_acid_cat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (62.3%) | `polar_aprotic_nitrile` (36.5%) | `aqueous` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (96%) | `CC#N` (25%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` + `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `Cc1cc(O[C@@H](C)C(` (0%) | set ✓ / any ✓ |

---

### Reaction #2088  yield=65.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #19)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccc(C)c(C)c1)c1ccc(C)c(C)c1>>Cc1ccc(C2(c3ccc(C)c(C)c3)N=C3C(CC(F)(F)F)CCN3C2=…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (98.8%) | `graphite_generic` (1.1%) | `carbon_plate` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (82.2%) | `nickel` (14.3%) | `carbon` (3.2%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (96.4%) | `platinum_generic` (2.1%) | `nickel_plate` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.5%) | `NEt4` (5.2%) | `ABSENT` (2.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (92.5%) | `Br` (3.3%) | `ABSENT` (1.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (20.6%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (99.1%) | `polar_aprotic_nitrile` (0.8%) | `ketone` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `ClCCl` (100%) | `O` (100%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |

---

### Reaction #2089  yield=70.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #20)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccc(C(C)C)cc1)c1ccc(C(C)C)cc1>>CC(C)c1ccc(C2(c3ccc(C(C)C)cc3)N=C3C(CC(F)(F)F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (91.1%) | `graphite_generic` (8.9%) | `carbon_felt` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (94.0%) | `nickel` (4.2%) | `carbon` (1.6%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (97.7%) | `platinum_generic` (1.1%) | `graphite_generic` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.4%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (98.9%) | `Br` (0.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.0%) | `alkali_bicarbonate` (2.7%) | `metal_oxide_oxidant` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (98.4%) | `polar_aprotic_nitrile` (1.5%) | `ketone` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (100%) | `CC#N` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=P([O-])(O)O.[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccc(-c2ccccn2)nc` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2090  yield=76.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #21)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccc(Cl)cc1)c1ccc(Cl)cc1>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccc(Cl)cc1)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (98.5%) | `graphite_generic` (1.5%) | `carbon_felt` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (93.5%) | `nickel` (4.1%) | `carbon` (1.6%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (99.7%) | `platinum_generic` (0.2%) | `stainless_steel_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.8%) | `ABSENT` (3.6%) | `NEt4` (2.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (98.3%) | `ABSENT` (0.8%) | `Br` (0.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `alkali_other_salt` (2.7%) | `metal_oxide_oxidant` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (96.0%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (100%) | `CC#N` (16%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)[O-].[Na+]` (1%) | `O=P([O-])(O)O.[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #2091  yield=76.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #5)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (97.9%) | `graphite_generic` (2.0%) | `carbon_felt` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (93.4%) | `nickel` (3.6%) | `carbon` (2.3%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.1%) | `graphite_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.8%) | `ABSENT` (1.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (95.7%) | `Br` (1.6%) | `ABSENT` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.3%) | `alkali_bicarbonate` (3.5%) | `metal_oxide_oxidant` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (97.5%) | `polar_aprotic_nitrile` (2.2%) | `ketone` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `ClCCl` + `O` | `ClCCl` (100%) | `O` (100%) | `O=C(O)C(F)(F)F` (25%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (98%) | `CC(=O)[O-].[Na+]` (1%) | `O=P([O-])(O)O.[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccc(-c2ccccn2)nc` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2092  yield=78.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #23)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccc(OC)cc1)c1ccc(OC)cc1>>COc1ccc(C2(c3ccc(OC)cc3)N=C3C(CC(F)(F)F)CCN3C2=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (99.4%) | `graphite_generic` (0.6%) | `carbon_felt` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (85.5%) | `nickel` (8.6%) | `carbon` (5.1%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (98.5%) | `platinum_generic` (0.9%) | `nickel_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.0%) | `ABSENT` (2.5%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (97.9%) | `ABSENT` (1.3%) | `Br` (0.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.2%) | `alkali_bicarbonate` (2.8%) | `metal_oxide_oxidant` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (4.5%) | `ketone` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (100%) | `CC#N` (10%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (92%) | `CC(=O)[O-].[Na+]` (7%) | `O=P([O-])(O)O.[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✓ / any ✓ |

---

### Reaction #2093  yield=72.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13116-13130.json) (反应 idx 在该 JSON 内 = #24)

```
O=S(O)C(F)(F)F.[Na].C=CCCN(C#N)C(=O)C(c1ccc(C)cc1)c1ccc(C)cc1>>Cc1ccc(C2(c3ccc(C)cc3)N=C3C(CC(F)(F)F)CCN3C2=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (99.5%) | `graphite_generic` (0.5%) | `reticulated_vitreous_carbon` (0.0%) | ✓ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (91.8%) | `nickel` (6.4%) | `carbon` (1.6%) | ✗ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_plate` (97.4%) | `platinum_generic` (1.6%) | `nickel_plate` (0.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.1%) | `ABSENT` (12.7%) | `NEt4` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (94.5%) | `ABSENT` (3.5%) | `Br` (1.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.8%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.0%) | `ferrocene_mediator` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (92.2%) | `polar_aprotic_nitrile` (7.0%) | `aqueous` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (97%) | `CC#N` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=P([O-])(O)O.[K+]` (0%) | `O=C(O)O.[Na]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2094  yield=38.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCc1ccc(OC(C)=O)c(OC)c1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1>>COc1ccc(SC(Cc2ccc(OC(C)=O)c(OC)c2)CC(F)(F)C(F…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (68.1%) | `sacrificial_zinc` (18.5%) | `carbon` (10.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `zinc_generic` (51.0%) | `platinum_generic` (38.4%) | `unknown_electrode` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (86.4%) | `carbon` (9.2%) | `nickel` (2.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (97.5%) | `carbon_felt` (0.6%) | `reticulated_vitreous_carbon` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (81.4%) | `undivided` (16.7%) | `ABSENT` (1.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.3%) | `NBu4` (27.7%) | `NEt4` (4.0%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (55.4%) | `ABSENT` (38.3%) | `Cl` (5.3%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (16.1%) | `boron_lewis_acid` (7.8%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (73.0%) | `Ni_complex` (23.8%) | `Co_complex` (2.3%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (28.6%) | `halogenated_aliphatic` (27.9%) | `polar_aprotic_amide` (21.1%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `O` | `O` (69%) | `CC#N` (53%) | `ClCCl` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (99%) | `CCN(CC)CC.F.F.F` (1%) | `Cc1ccc(S(=O)(=O)O)` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (100%) | `CC1[CH-]C(C)=[O]->` (0%) | `Br[Ni](Br)(n1ccccc` (0%) | set ✗ / any ✗ |

---

### Reaction #2095  yield=45.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #1)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=CCc1cccc2ccccc12>>COc1ccc(SC(Cc2cccc3ccccc23)CC(F)(F)C(F)(F)C(F)(F)C(F…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (50.7%) | `sacrificial_zinc` (39.2%) | `carbon` (6.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (47.8%) | `zinc_generic` (46.6%) | `platinum_wire` (3.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (69.9%) | `carbon` (29.5%) | `ABSENT` (0.2%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.3%) | `carbon_felt` (0.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (77.9%) | `undivided` (18.4%) | `ABSENT` (3.7%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (74.1%) | `NBu4` (17.2%) | `Na` (6.0%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (68.6%) | `BF4` (16.1%) | `Cl` (10.1%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (27.4%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (49.6%) | `Ni_complex` (49.3%) | `Fe_complex` (0.6%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (74.4%) | `aqueous` (13.8%) | `polar_aprotic_nitrile` (6.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (96%) | `O` (45%) | `ClCCl` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (99%) | `CCN(CC)CC.F.F.F` (0%) | `[Na+].[OH-]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | `Br[Ni](Br)(n1ccccc` (0%) | set ✗ / any ✗ |

---

### Reaction #2096  yield=42.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #2)

```
C=CCc1ccccc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1>>COc1ccc(SC(Cc2ccccc2)CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (67.7%) | `sacrificial_zinc` (19.7%) | `carbon` (6.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (78.9%) | `zinc_generic` (9.6%) | `carbon_cloth` (7.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (76.5%) | `carbon` (19.6%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `carbon_cloth` (0.1%) | `carbon_felt` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (93.7%) | `undivided` (5.2%) | `ABSENT` (1.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (83.7%) | `NBu4` (7.9%) | `NEt4` (3.5%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (75.4%) | `Cl` (11.0%) | `BF4` (10.2%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (14.0%) | `hf_amine_complex` (5.4%) | `hf` (2.0%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (57.4%) | `Ni_complex` (40.8%) | `Fe_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (34.5%) | `aqueous` (27.9%) | `polar_aprotic_nitrile` (10.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (72%) | `O` (49%) | `ClCCl` (26%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (85%) | `O=O` (3%) | `CC(=O)[O-].[Na+]` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (75%) | `CC#N.CC(c1ccccn1)(` (1%) | `[Cl-].[Cl-].[Ni+2]` (0%) | set ✗ / any ✗ |

---

### Reaction #2097  yield=42.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #3)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1.CC(C)c1cc(C(C)C)c(S)c(C(C)C)c1>>CC(C)c1cc(C(C)C)c(SC(CC(F)(F)C(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.4%) | `platinum` (12.8%) | `sacrificial_iron` (2.3%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (54.1%) | `carbon_felt` (12.8%) | `platinum_generic` (7.2%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.3%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (94.2%) | `platinum_plate` (2.3%) | `nickel_foam` (1.5%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (68.7%) | `undivided` (31.2%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.8%) | `NEt4` (3.9%) | `ABSENT` (1.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (98.5%) | `Cl` (0.5%) | `ABSENT` (0.5%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `boron_lewis_acid` (54.6%) | `ABSENT` (6.9%) | `diboron` (1.1%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (64.9%) | `Ni_complex` (21.2%) | `Cu_complex` (8.6%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (57.7%) | `polar_aprotic_nitrile` (15.0%) | `ketone` (13.6%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (82%) | `O` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `CCCC[N+](CCCC)(CCC` (58%) | `__ABSENT__` (15%) | `F[B-](F)(F)F.[H+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `Br[Ni](Br)(n1ccccc` (0%) | set ✗ / any ✗ |

---

### Reaction #2098  yield=42.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #4)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1ccc(C(=O)Oc2ccc3c(c2)CC[C@@H]2[C@@H]3CC[C@]3(C)C(=O)CC[C@@H]23)cc1>…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (96.9%) | `carbon` (1.6%) | `sacrificial_zinc` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (93.2%) | `zinc_generic` (1.5%) | `platinum_plate` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.5%) | `carbon` (1.8%) | `ABSENT` (0.2%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (98.4%) | `platinum_plate` (0.8%) | `platinum_wire` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (94.7%) | `undivided` (5.3%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (68.5%) | `ABSENT` (27.8%) | `NEt4` (3.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (63.5%) | `ABSENT` (28.5%) | `Cl` (3.3%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (29.0%) | `boron_lewis_acid` (6.2%) | `hf_amine_complex` (2.0%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (69.4%) | `ABSENT` (29.2%) | `Fe_complex` (0.6%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (77.2%) | `polar_aprotic_nitrile` (8.3%) | `aqueous` (4.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (59%) | `CC#N` (8%) | `ClCCl` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (18%) | `[Br][Ni][Br].c1cc(` (9%) | `[Br-][Ni+2]1([Br-]` (4%) | set ✗ / any ✗ |

---

### Reaction #2099  yield=60.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #5)

```
C=C(C)c1ccccc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1>>COc1ccc(SC(C)(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (98.3%) | `sacrificial_zinc` (0.8%) | `sacrificial_magnesium` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (99.6%) | `platinum_rod` (0.1%) | `zinc_generic` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (100.0%) | `platinum_plate` (0.0%) | `reticulated_vitreous_carbon` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (85.4%) | `undivided` (14.4%) | `ABSENT` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (64.6%) | `ABSENT` (15.5%) | `NEt4` (14.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (69.5%) | `ABSENT` (11.9%) | `Cl` (9.5%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `boron_lewis_acid` (23.9%) | `ABSENT` (16.3%) | `metal_oxide_oxidant` (1.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Ni_complex` (85.9%) | `ABSENT` (13.4%) | `Cu_complex` (0.2%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (93.9%) | `aqueous` (3.9%) | `polar_aprotic_nitrile` (1.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (99%) | `O` (91%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `F[B-](F)(F)F.[H+]` (66%) | `CCCC[N+](CCCC)(CCC` (24%) | `CC(=O)O` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `Br[Ni](Br)(n1ccccc` (37%) | `[Br][Ni][Br].c1cc(` (10%) | `__ABSENT__` (4%) | set ✗ / any ✓ |

---

### Reaction #2100  yield=56.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #6)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1ccc(C(=O)N2CCN(C3NSc4ccccc43)CC2)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (97.8%) | `platinum` (1.3%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (99.0%) | `ABSENT` (0.2%) | `carbon_cloth` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (96.9%) | `nickel` (1.9%) | `carbon` (0.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (69.7%) | `platinum_generic` (21.0%) | `platinum_wire` (7.3%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (100.0%) | `undivided` (0.0%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (83.3%) | `ABSENT` (13.7%) | `Li` (2.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (82.0%) | `ABSENT` (13.4%) | `ClO4` (2.2%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (5.2%) | `phosphine_neutral` (2.7%) | `carboxylic_acid` (2.4%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (91.0%) | `Ni_complex` (6.9%) | `brønsted_acid_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (83.2%) | `polar_aprotic_nitrile` (7.3%) | `halogenated_aliphatic` (4.7%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CC#N` (33%) | `CN(C)C=O` (24%) | `O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (87%) | `O=C(O)C(F)(F)F` (7%) | `CC(=O)O` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (99%) | `CC#N.CC(c1ccccn1)(` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #2101  yield=58.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #7)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1.COC(=O)[C@@H](CS)NC(=O)OC(C)(C)C>>COC(=O)[C@@H](CSC(CC(F)(F)C(F…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `sacrificial_zinc` (81.6%) | `carbon` (5.3%) | `platinum` (4.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `zinc_generic` (48.7%) | `zinc_plate` (22.9%) | `unknown_electrode` (8.0%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (94.6%) | `carbon` (2.2%) | `ABSENT` (1.0%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (42.8%) | `unknown_electrode` (29.2%) | `platinum_plate` (9.9%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (81.2%) | `undivided` (18.5%) | `ABSENT` (0.3%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.5%) | `NEt4` (11.0%) | `NBu4` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (86.1%) | `BF4` (12.3%) | `Cl` (1.3%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (19.5%) | `boron_lewis_acid` (13.7%) | `iodide_anion` (2.7%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (54.1%) | `Ni_complex` (44.1%) | `Fe_complex` (1.2%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (73.5%) | `ketone` (14.2%) | `ABSENT` (8.8%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (100%) | `ClCCl` (0%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (100%) | `BrCCBr` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (100%) | `Br[Ni](Br)(n1ccccc` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✗ |

---

### Reaction #2102  yield=57.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #8)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1ccc(OC(C)=O)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccc(OC…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (87.3%) | `sacrificial_zinc` (7.2%) | `carbon` (4.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (73.4%) | `zinc_generic` (11.6%) | `platinum_wire` (6.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.6%) | `carbon` (1.8%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (97.0%) | `platinum_wire` (1.1%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (85.5%) | `undivided` (14.5%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (59.2%) | `NBu4` (39.3%) | `NEt4` (1.0%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (43.9%) | `BF4` (42.6%) | `Cl` (11.5%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (19.9%) | `boron_lewis_acid` (7.0%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (50.2%) | `ABSENT` (48.5%) | `Fe_complex` (0.9%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (82.5%) | `polar_aprotic_nitrile` (6.4%) | `aqueous` (4.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (79%) | `O` (52%) | `CC#N` (10%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (99%) | `CCN(CC)CC.F.F.F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (17%) | `[Br][Ni][Br].c1cc(` (7%) | `Br[Ni](Br)(n1ccccc` (3%) | set ✗ / any ✗ |

---

### Reaction #2103  yield=56.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #9)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1cc(C)c(C)cc1C>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2cc(C)c(C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (82.6%) | `sacrificial_zinc` (12.2%) | `carbon` (2.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `zinc_generic` (41.3%) | `platinum_generic` (39.9%) | `platinum_wire` (11.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (64.5%) | `carbon` (31.0%) | `nickel` (2.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (65.9%) | `carbon_felt` (11.2%) | `reticulated_vitreous_carbon` (11.1%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (95.7%) | `undivided` (4.2%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (87.8%) | `NBu4` (11.0%) | `NEt4` (0.7%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (79.1%) | `BF4` (10.6%) | `Cl` (9.1%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (19.1%) | `boron_lewis_acid` (5.6%) | `phosphine_neutral` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (89.9%) | `ABSENT` (9.6%) | `Fe_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (59.8%) | `aqueous` (24.6%) | `polar_aprotic_nitrile` (10.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (80%) | `O` (12%) | `CC#N` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `BrCCBr` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (16%) | `[Br-][Ni+2]1([Br-]` (16%) | `Br[Ni](Br)(n1ccccc` (7%) | set ✗ / any ✗ |

---

### Reaction #2104  yield=56.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #10)

```
C=Cc1ccccn1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccccn2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `sacrificial_zinc` (81.7%) | `platinum` (13.1%) | `carbon` (1.6%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `zinc_generic` (94.9%) | `platinum_generic` (2.9%) | `platinum_rod` (1.4%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (96.7%) | `carbon` (1.4%) | `nickel` (0.9%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (98.6%) | `reticulated_vitreous_carbon` (0.4%) | `tin_generic` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (99.5%) | `undivided` (0.4%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (92.7%) | `NBu4` (5.9%) | `NEt4` (0.6%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (80.8%) | `Cl` (11.5%) | `BF4` (6.2%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (28.4%) | `phosphine_neutral` (2.3%) | `thiol` (1.9%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (97.5%) | `ABSENT` (2.3%) | `Co_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (78.2%) | `polar_aprotic_sulfoxide` (6.5%) | `polar_aprotic_nitrile` (6.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (64%) | `CS(C)=O` (30%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (2%) | `CC(=O)O` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (87%) | `Br[Ni](Br)(n1ccccc` (2%) | `__ABSENT__` (2%) | set ✗ / any ✗ |

---

### Reaction #2105  yield=52.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #11)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1ccc(C(=O)OC2CC(C)CCC2C(C)C)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (98.5%) | `carbon` (1.0%) | `sacrificial_zinc` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (98.9%) | `platinum_wire` (0.3%) | `platinum_plate` (0.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (86.9%) | `carbon` (8.4%) | `nickel` (3.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (97.3%) | `graphite_generic` (0.6%) | `nickel_foam` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (71.6%) | `undivided` (28.0%) | `ABSENT` (0.4%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.0%) | `ABSENT` (2.9%) | `NEt4` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (63.6%) | `Cl` (21.3%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (28.0%) | `boron_lewis_acid` (4.8%) | `phosphine_neutral` (1.9%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (95.6%) | `Ni_complex` (4.3%) | `Co_complex` (0.0%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (80.8%) | `polar_aprotic_nitrile` (10.4%) | `aqueous` (4.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (64%) | `O` (43%) | `CC#N` (25%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (100%) | `Br[Ni](Br)(n1ccccc` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✗ / any ✗ |

---

### Reaction #2106  yield=51.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #12)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1.Cc1occc1S>>Cc1occc1SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c1ccc(-c2c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (59.0%) | `sacrificial_zinc` (23.7%) | `platinum` (14.2%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (58.6%) | `zinc_generic` (11.3%) | `platinum_wire` (10.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (50.4%) | `platinum_wire` (40.5%) | `nickel_foam` (4.3%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (69.8%) | `undivided` (30.2%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (64.6%) | `NBu4` (32.5%) | `Li` (2.2%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (63.2%) | `BF4` (31.1%) | `Cl` (3.6%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (25.1%) | `boron_lewis_acid` (5.6%) | `phosphine_neutral` (2.0%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (57.9%) | `ABSENT` (36.9%) | `Fe_complex` (3.9%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ketone` (33.6%) | `polar_aprotic_nitrile` (31.7%) | `polar_aprotic_amide` (24.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CC(C)=O` (22%) | `O` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[I-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (8%) | `[Ni]` (2%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✗ / any ✗ |

---

### Reaction #2107  yield=64.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #13)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccccc1C.COc1ccc(S)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccccc2C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (95.3%) | `sacrificial_zinc` (2.3%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (91.6%) | `zinc_generic` (4.1%) | `platinum_rod` (1.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.1%) | `carbon` (2.2%) | `nickel` (0.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (98.8%) | `reticulated_vitreous_carbon` (0.5%) | `platinum_wire` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (99.5%) | `undivided` (0.4%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (81.4%) | `NBu4` (18.0%) | `NEt4` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (83.0%) | `BF4` (13.0%) | `Cl` (2.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (17.0%) | `hf_amine_complex` (5.3%) | `boron_lewis_acid` (4.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Ni_complex` (91.5%) | `ABSENT` (8.0%) | `Fe_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (81.0%) | `aqueous` (8.8%) | `polar_aprotic_nitrile` (3.7%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (83%) | `CS(C)=O` (11%) | `O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (96%) | `O=C(O)C(F)(F)F` (3%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Ni]` (13%) | `__ABSENT__` (11%) | `Br[Ni](Br)(n1ccccc` (9%) | set ✗ / any ✓ |

---

### Reaction #2108  yield=63.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #14)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1ccc(Cl)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccc(Cl)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (98.3%) | `carbon` (0.7%) | `sacrificial_zinc` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (97.1%) | `zinc_generic` (1.2%) | `platinum_wire` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.9%) | `carbon` (0.9%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.4%) | `platinum_plate` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (99.4%) | `undivided` (0.5%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (85.3%) | `NBu4` (14.1%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (75.7%) | `BF4` (15.4%) | `Cl` (8.2%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (21.7%) | `boron_lewis_acid` (4.9%) | `hf_amine_complex` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Ni_complex` (60.3%) | `ABSENT` (39.1%) | `Fe_complex` (0.2%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (49.7%) | `polar_aprotic_nitrile` (38.1%) | `aqueous` (6.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (50%) | `CC#N` (44%) | `O` (28%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `[Na+].[OH-]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (14%) | `[Br][Ni][Br].c1cc(` (3%) | `Br[Ni](Br)(n1ccccc` (3%) | set ✗ / any ✓ |

---

### Reaction #2109  yield=68.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #15)

```
Cc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(OC)cc1>>COc1ccc(C(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)Sc2ccc(C)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (86.2%) | `sacrificial_zinc` (7.4%) | `carbon` (3.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (72.1%) | `zinc_generic` (14.2%) | `platinum_rod` (3.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.5%) | `carbon` (1.7%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (97.9%) | `carbon_felt` (0.6%) | `platinum_wire` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (99.5%) | `undivided` (0.4%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (83.9%) | `NBu4` (14.2%) | `Na` (1.0%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (74.9%) | `BF4` (17.0%) | `Cl` (4.6%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (17.9%) | `boron_lewis_acid` (6.5%) | `as_solvent_polar_aprotic_sulfo` (2.3%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (71.1%) | `ABSENT` (27.7%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `aqueous` (41.1%) | `polar_aprotic_amide` (40.2%) | `polar_aprotic_nitrile` (6.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `O` (87%) | `CC#N` (7%) | `CS(C)=O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (95%) | `CC(=O)O` (2%) | `CCN(CC)CC` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `Br[Ni](Br)(n1ccccc` (12%) | `[Ni]` (11%) | `__ABSENT__` (8%) | set ✗ / any ✗ |

---

### Reaction #2110  yield=68.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #16)

```
Fc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1>>Fc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccc(-c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (48.5%) | `sacrificial_zinc` (34.8%) | `carbon` (6.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (28.0%) | `platinum_rod` (2.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.3%) | `carbon` (0.5%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.5%) | `platinum_plate` (0.3%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (91.0%) | `undivided` (8.7%) | `ABSENT` (0.3%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.3%) | `ABSENT` (15.7%) | `NEt4` (2.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (80.0%) | `ABSENT` (14.7%) | `Cl` (2.2%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (19.0%) | `boron_lewis_acid` (13.6%) | `iodide_anion` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (56.3%) | `ABSENT` (40.6%) | `Cu_complex` (1.5%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (91.9%) | `polar_aprotic_nitrile` (4.0%) | `polar_protic_acid` (1.2%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (27%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (99%) | `O=C(O)C(F)(F)F` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (12%) | `Br[Ni](Br)(n1ccccc` (8%) | `COCCOC.[Br][Ni][Br` (1%) | set ✗ / any ✗ |

---

### Reaction #2111  yield=62.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #17)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1ccc(Br)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccc(Br)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (92.1%) | `sacrificial_zinc` (5.1%) | `carbon` (1.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (74.4%) | `zinc_generic` (16.1%) | `platinum_wire` (6.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (96.7%) | `carbon` (2.5%) | `nickel` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (92.7%) | `platinum_wire` (6.0%) | `nickel_foam` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (97.0%) | `undivided` (2.9%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (54.1%) | `NBu4` (45.3%) | `NEt4` (0.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (60.2%) | `BF4` (25.8%) | `Cl` (10.8%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (27.6%) | `phosphine_neutral` (2.1%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Ni_complex` (86.2%) | `ABSENT` (12.7%) | `Fe_complex` (0.8%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (78.9%) | `polar_aprotic_nitrile` (12.5%) | `polar_aprotic_sulfoxide` (3.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (79%) | `CC#N` (15%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` + `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (99%) | `O=C(O)C(F)(F)F` (1%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Ni]` (7%) | `__ABSENT__` (3%) | `Br[Ni](Br)(n1ccccc` (2%) | set ✗ / any ✓ |

---

### Reaction #2112  yield=67.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #18)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1ccc(-c2ccccc2)cc1>>COc1cc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (72.5%) | `sacrificial_zinc` (21.0%) | `sacrificial_magnesium` (2.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (69.2%) | `zinc_generic` (17.3%) | `platinum_rod` (7.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.8%) | `carbon` (1.3%) | `nickel` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.3%) | `nickel_foam` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (99.0%) | `undivided` (0.9%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (54.5%) | `ABSENT` (37.6%) | `NEt4` (4.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (49.0%) | `ABSENT` (24.9%) | `Cl` (18.2%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (21.1%) | `boron_lewis_acid` (8.5%) | `hf_amine_complex` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Ni_complex` (95.9%) | `ABSENT` (3.3%) | `Fe_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (92.3%) | `polar_aprotic_nitrile` (2.6%) | `polar_aprotic_sulfoxide` (1.6%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (99%) | `O` (25%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `F[B-](F)(F)F.[H+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Ni]` (40%) | `Br[Ni](Br)(n1ccccc` (25%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #2113  yield=67.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #19)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1ccc(C(=O)OCc2ccc3c(c2)OCO3)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (90.7%) | `carbon` (8.7%) | `sacrificial_zinc` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (92.7%) | `carbon_felt` (3.4%) | `platinum_rod` (0.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.3%) | `carbon` (1.7%) | `nickel` (0.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (91.3%) | `platinum_plate` (3.2%) | `platinum_wire` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (97.3%) | `undivided` (2.6%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (91.9%) | `NBu4` (8.0%) | `Na` (0.1%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (94.8%) | `BF4` (4.7%) | `Cl` (0.3%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (16.5%) | `boron_lewis_acid` (6.1%) | `phosphine_neutral` (2.4%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (50.2%) | `ABSENT` (49.4%) | `Fe_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (52.2%) | `polar_aprotic_nitrile` (22.5%) | `halogenated_aliphatic` (8.1%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CC#N` (20%) | `O` (16%) | `CN(C)C=O` (14%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (99%) | `O=C(O)C(F)(F)F` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (83%) | `[Br-][Ni+2]1([Br-]` (1%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #2114  yield=62.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #20)

```
C=Cc1ccc(C(F)(F)F)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccc(C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (82.1%) | `carbon` (6.1%) | `sacrificial_magnesium` (5.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (80.6%) | `zinc_generic` (4.9%) | `unknown_electrode` (3.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (95.8%) | `carbon` (3.4%) | `nickel` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (97.5%) | `platinum_wire` (1.0%) | `platinum_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (96.8%) | `undivided` (3.1%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (55.3%) | `ABSENT` (42.6%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.0%) | `ABSENT` (35.4%) | `Cl` (17.9%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (25.9%) | `boron_lewis_acid` (4.2%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (89.2%) | `ABSENT` (8.7%) | `Fe_complex` (1.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (60.7%) | `aqueous` (18.0%) | `polar_aprotic_nitrile` (8.7%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (90%) | `ClCCl` (13%) | `O` (10%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (98%) | `CCN(CC)CC.F.F.F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (9%) | `Br[Ni](Br)(n1ccccc` (7%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #2115  yield=65.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #21)

```
C=Cc1cccc(C)c1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2cccc(C)c2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (82.2%) | `sacrificial_zinc` (8.3%) | `carbon` (6.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (55.9%) | `zinc_generic` (20.6%) | `platinum_rod` (6.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (94.0%) | `carbon` (5.2%) | `nickel` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (92.2%) | `platinum_plate` (3.6%) | `reticulated_vitreous_carbon` (1.2%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (98.5%) | `undivided` (1.4%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (81.4%) | `NBu4` (16.4%) | `Na` (1.6%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.4%) | `BF4` (12.0%) | `Cl` (3.6%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (22.3%) | `boron_lewis_acid` (3.7%) | `hf_amine_complex` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Ni_complex` (78.9%) | `ABSENT` (20.6%) | `Fe_complex` (0.2%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (87.2%) | `aqueous` (7.6%) | `polar_aprotic_nitrile` (1.6%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (95%) | `O` (18%) | `ClCCl` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (99%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Ni]` (17%) | `Br[Ni](Br)(n1ccccc` (12%) | `[Br][Ni][Br].c1cc(` (2%) | set ✗ / any ✗ |

---

### Reaction #2116  yield=67.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #22)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(C)cc1.COc1ccc(S)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccc(C)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (86.2%) | `sacrificial_zinc` (7.4%) | `carbon` (3.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (72.1%) | `zinc_generic` (14.2%) | `platinum_rod` (3.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.5%) | `carbon` (1.7%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (97.9%) | `carbon_felt` (0.6%) | `platinum_wire` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (99.5%) | `undivided` (0.4%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (83.9%) | `NBu4` (14.2%) | `Na` (1.0%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (74.9%) | `BF4` (17.0%) | `Cl` (4.6%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (17.9%) | `boron_lewis_acid` (6.5%) | `as_solvent_polar_aprotic_sulfo` (2.3%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (71.1%) | `ABSENT` (27.7%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `aqueous` (41.1%) | `polar_aprotic_amide` (40.2%) | `polar_aprotic_nitrile` (6.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `O` (87%) | `CC#N` (7%) | `CS(C)=O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (95%) | `CC(=O)O` (2%) | `CCN(CC)CC` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `Br[Ni](Br)(n1ccccc` (12%) | `[Ni]` (11%) | `__ABSENT__` (8%) | set ✗ / any ✗ |

---

### Reaction #2117  yield=65.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #23)

```
C=Cc1ccc(F)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccc(F)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (89.9%) | `carbon` (4.3%) | `sacrificial_zinc` (3.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_plate` | `platinum_generic` (91.8%) | `zinc_generic` (3.8%) | `platinum_wire` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.8%) | `carbon` (1.5%) | `ABSENT` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `nickel_plate` | `platinum_generic` (98.9%) | `platinum_wire` (0.6%) | `platinum_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (94.9%) | `undivided` (4.8%) | `ABSENT` (0.3%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (76.3%) | `ABSENT` (20.2%) | `Na` (2.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (61.9%) | `ABSENT` (17.5%) | `Br` (10.1%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (26.4%) | `boron_lewis_acid` (5.0%) | `metal_oxide_oxidant` (1.9%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (65.7%) | `Ni_complex` (33.7%) | `brønsted_acid_cat` (0.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (60.7%) | `polar_aprotic_nitrile` (22.6%) | `aqueous` (6.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `O` (68%) | `CC#N` (50%) | `CN(C)C=O` (39%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (97%) | `O=C(O)C(F)(F)F` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #2118  yield=70.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #24)

```
Sc1ccc2ccccc2c1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc2ccccc2c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (42.6%) | `sacrificial_zinc` (38.5%) | `sacrificial_magnesium` (8.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (61.5%) | `zinc_generic` (24.6%) | `platinum_rod` (4.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.1%) | `carbon` (0.8%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_wire` (0.1%) | `platinum_plate` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (73.2%) | `undivided` (26.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.8%) | `ABSENT` (14.6%) | `NEt4` (2.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (87.4%) | `ABSENT` (8.4%) | `Cl` (2.6%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `boron_lewis_acid` (22.1%) | `ABSENT` (20.1%) | `metal_oxide_oxidant` (1.6%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (83.3%) | `ABSENT` (14.8%) | `Cu_complex` (0.7%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (81.1%) | `polar_aprotic_nitrile` (13.4%) | `polar_aprotic_sulfoxide` (1.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (97%) | `O` (11%) | `CC#N` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `CCCC[N+](CCCC)(CCC` (32%) | `F[B-](F)(F)F.[H+]` (20%) | `O=C(O)C(F)(F)F` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `Br[Ni](Br)(n1ccccc` (15%) | `[Ni]` (9%) | `COCCOC.[Br][Ni][Br` (1%) | set ✗ / any ✗ |

---

### Reaction #2119  yield=70.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #25)

```
Sc1ccc(Cl)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(Cl)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (79.8%) | `sacrificial_zinc` (11.4%) | `carbon` (5.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (81.8%) | `zinc_generic` (12.5%) | `platinum_rod` (1.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.0%) | `carbon` (0.9%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.3%) | `reticulated_vitreous_carbon` (0.2%) | `platinum_wire` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (99.4%) | `undivided` (0.6%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (70.9%) | `NBu4` (27.8%) | `NEt4` (1.0%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (57.6%) | `BF4` (39.4%) | `Cl` (2.4%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (17.9%) | `boron_lewis_acid` (8.8%) | `hf_amine_complex` (3.9%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (72.1%) | `ABSENT` (22.9%) | `Cu_complex` (3.5%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (90.1%) | `polar_aprotic_nitrile` (7.1%) | `polar_protic_acid` (1.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (12%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (99%) | `O=C(O)C(F)(F)F` (1%) | `BrCCBr` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `Br[Ni](Br)(n1ccccc` (12%) | `[Ni]` (11%) | `__ABSENT__` (1%) | set ✗ / any ✗ |

---

### Reaction #2120  yield=80.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #26)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1.Cc1cc(C)cc(S)c1>>Cc1cc(C)cc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `sacrificial_zinc` (81.8%) | `platinum` (14.4%) | `sacrificial_iron` (1.6%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `zinc_generic` (68.1%) | `platinum_generic` (12.6%) | `zinc_plate` (10.4%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (90.7%) | `carbon` (8.4%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (88.8%) | `reticulated_vitreous_carbon` (4.2%) | `platinum_wire` (3.5%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (99.6%) | `undivided` (0.4%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (67.5%) | `NBu4` (25.9%) | `BnNMe3` (2.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (52.8%) | `BF4` (38.4%) | `Cl` (5.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (22.3%) | `boron_lewis_acid` (6.3%) | `metal_oxide_oxidant` (1.9%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (68.9%) | `ABSENT` (28.5%) | `Co_complex` (0.9%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (81.7%) | `ABSENT` (7.8%) | `polar_aprotic_nitrile` (3.7%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (97%) | `CC#N` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (100%) | `O=O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (22%) | `Br[Ni](Br)(n1ccccc` (14%) | `__ABSENT__` (3%) | set ✗ / any ✗ |

---

### Reaction #2121  yield=71.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #27)

```
FC(F)(F)C(F)(I)C(F)(F)F.COc1ccc(S)cc1.C=Cc1ccc(-c2ccccc2)cc1>>COc1ccc(SC(CC(F)(C(F)(F)F)C(F)(F)F)c2ccc(-c3ccccc3)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (70.5%) | `platinum` (29.1%) | `sacrificial_iron` (0.2%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_rod` (31.0%) | `graphite_generic` (24.7%) | `reticulated_vitreous_carbon` (18.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.0%) | `carbon` (0.6%) | `nickel` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (96.7%) | `platinum_plate` (3.0%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.5%) | `Na` (4.6%) | `NEt4` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (35.7%) | `Br` (25.9%) | `Cl` (17.2%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (16.7%) | `alkali_carbonate` (2.3%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (98.8%) | `Fe_complex` (0.5%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (51.9%) | `ketone` (17.4%) | `aqueous` (15.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CC#N` (90%) | `O` (82%) | `CC(=O)O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` | `__ABSENT__` (99%) | `CCN(CC)CC.F.F.F` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (0%) | `COCCOC.[Br][Ni][Br` (0%) | set ✗ / any ✗ |

---

### Reaction #2122  yield=76.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #28)

```
Cc1cccc(C)c1S.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1>>Cc1cccc(C)c1SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `sacrificial_zinc` (51.7%) | `platinum` (36.4%) | `sacrificial_iron` (4.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `zinc_generic` (22.5%) | `platinum_generic` (20.8%) | `platinum_rod` (19.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.5%) | `carbon` (0.9%) | `nickel` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (87.9%) | `platinum_plate` (4.7%) | `platinum_wire` (2.8%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (98.9%) | `undivided` (1.0%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (52.4%) | `NBu4` (41.9%) | `NEt4` (5.4%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (69.9%) | `ABSENT` (28.9%) | `Cl` (0.5%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `boron_lewis_acid` (39.2%) | `ABSENT` (12.0%) | `hf_amine_complex` (1.8%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (77.8%) | `ABSENT` (15.9%) | `Cu_complex` (4.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.3%) | `ABSENT` (3.3%) | `halogenated_aliphatic` (2.3%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (97%) | `O` (1%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `F[B-](F)(F)F.[H+]` (28%) | `CCCC[N+](CCCC)(CCC` (10%) | `__ABSENT__` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `Br[Ni](Br)(n1ccccc` (26%) | `[Ni]` (9%) | `__ABSENT__` (1%) | set ✗ / any ✗ |

---

### Reaction #2123  yield=76.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #29)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1ccc2ccccc2c1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccc3ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (73.1%) | `sacrificial_zinc` (9.4%) | `sacrificial_magnesium` (9.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (72.0%) | `platinum_wire` (8.0%) | `zinc_generic` (6.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (95.0%) | `carbon` (4.5%) | `nickel` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (97.2%) | `platinum_wire` (1.5%) | `platinum_plate` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (98.0%) | `undivided` (1.9%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (67.6%) | `ABSENT` (29.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (52.4%) | `ABSENT` (26.6%) | `Cl` (16.8%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (29.6%) | `boron_lewis_acid` (6.8%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (96.1%) | `ABSENT` (3.1%) | `brønsted_acid_cat` (0.4%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (78.9%) | `polar_aprotic_nitrile` (10.2%) | `polar_aprotic_sulfoxide` (5.7%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (77%) | `O` (26%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (99%) | `[Na+].[OH-]` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `Br[Ni](Br)(n1ccccc` (13%) | `[Ni]` (11%) | `COCCOCCOC.[Br][Ni]` (1%) | set ✗ / any ✗ |

---

### Reaction #2124  yield=73.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #30)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1cccc2ccccc12>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2cccc3cccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (90.0%) | `sacrificial_zinc` (7.7%) | `sacrificial_iron` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (79.8%) | `zinc_generic` (13.5%) | `platinum_wire` (3.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (93.0%) | `carbon` (4.9%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (93.8%) | `reticulated_vitreous_carbon` (3.2%) | `nickel_foam` (1.0%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (98.5%) | `undivided` (1.5%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.3%) | `ABSENT` (47.1%) | `Na` (3.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `ABSENT` (44.3%) | `BF4` (21.9%) | `Cl` (17.8%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (30.9%) | `boron_lewis_acid` (4.6%) | `phosphine_neutral` (1.9%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (88.9%) | `ABSENT` (10.9%) | `Fe_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (74.8%) | `aqueous` (12.2%) | `polar_aprotic_nitrile` (7.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (92%) | `O` (33%) | `CC#N` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (99%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (11%) | `Br[Ni](Br)(n1ccccc` (10%) | `__ABSENT__` (8%) | set ✗ / any ✗ |

---

### Reaction #2125  yield=78.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #31)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1ccc(-c2ccccc2)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccc(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #2126  yield=72.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #32)

```
Sc1ccc(Br)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(Br)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `sacrificial_zinc` (47.1%) | `platinum` (42.7%) | `sacrificial_iron` (4.3%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `zinc_generic` (66.5%) | `platinum_generic` (27.1%) | `platinum_wire` (2.5%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.5%) | `carbon` (0.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (98.4%) | `platinum_wire` (1.0%) | `platinum_plate` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (91.3%) | `undivided` (8.6%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (55.0%) | `ABSENT` (42.4%) | `NEt4` (2.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (51.4%) | `ABSENT` (44.5%) | `Cl` (2.1%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (22.8%) | `boron_lewis_acid` (5.0%) | `thiol` (2.0%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (88.8%) | `ABSENT` (7.8%) | `Cu_complex` (2.4%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (86.9%) | `polar_aprotic_nitrile` (7.7%) | `polar_protic_acid` (2.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (97%) | `CC#N` (2%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (36%) | `Br[Ni](Br)(n1ccccc` (8%) | `COCCOC.[Br][Ni][Br` (1%) | set ✗ / any ✗ |

---

### Reaction #2127  yield=74.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #33)

```
Cc1cccc(S)c1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1>>Cc1cccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccc(-…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (34.2%) | `sacrificial_zinc` (33.7%) | `carbon` (20.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `zinc_generic` (36.0%) | `platinum_generic` (21.5%) | `zinc_plate` (13.4%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (93.0%) | `carbon` (6.9%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (94.0%) | `reticulated_vitreous_carbon` (2.3%) | `platinum_wire` (1.4%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (92.8%) | `undivided` (7.2%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (64.6%) | `NBu4` (33.6%) | `Li` (0.8%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (60.1%) | `ABSENT` (38.4%) | `Cl` (0.8%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (22.0%) | `boron_lewis_acid` (5.5%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (76.3%) | `ABSENT` (20.9%) | `Fe_complex` (1.2%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (75.1%) | `polar_aprotic_nitrile` (12.1%) | `ABSENT` (8.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (96%) | `CC#N` (2%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` | `__ABSENT__` (100%) | `O=O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (4%) | `Br[Ni](Br)(n1ccccc` (3%) | `__ABSENT__` (2%) | set ✗ / any ✗ |

---

### Reaction #2128  yield=73.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #34)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1ccc(-c2ccccc2)cc1>>COc1ccc(SC(CC(F)(F)C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (72.5%) | `sacrificial_zinc` (21.0%) | `sacrificial_magnesium` (2.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (69.2%) | `zinc_generic` (17.3%) | `platinum_rod` (7.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.8%) | `carbon` (1.3%) | `nickel` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.3%) | `nickel_foam` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (99.0%) | `undivided` (0.9%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (54.5%) | `ABSENT` (37.6%) | `NEt4` (4.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (49.0%) | `ABSENT` (24.9%) | `Cl` (18.2%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (21.1%) | `boron_lewis_acid` (8.5%) | `hf_amine_complex` (2.4%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (95.9%) | `ABSENT` (3.3%) | `Fe_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (92.3%) | `polar_aprotic_nitrile` (2.6%) | `polar_aprotic_sulfoxide` (1.6%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (99%) | `O` (25%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `F[B-](F)(F)F.[H+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (40%) | `Br[Ni](Br)(n1ccccc` (25%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #2129  yield=75.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #35)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1ccc(C(C)(C)C)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccc(C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (92.0%) | `sacrificial_zinc` (5.4%) | `carbon` (1.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (90.6%) | `zinc_generic` (7.3%) | `platinum_wire` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.3%) | `carbon` (1.3%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.6%) | `platinum_wire` (0.2%) | `platinum_plate` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (81.0%) | `undivided` (18.8%) | `ABSENT` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (71.5%) | `NBu4` (26.0%) | `NEt4` (0.9%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (60.3%) | `BF4` (32.0%) | `Cl` (5.3%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (19.9%) | `boron_lewis_acid` (2.5%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (79.6%) | `ABSENT` (19.5%) | `Fe_complex` (0.4%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (81.8%) | `polar_aprotic_nitrile` (14.0%) | `aqueous` (1.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CC#N` (57%) | `CN(C)C=O` (41%) | `O` (39%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (93%) | `O=C(O)C(F)(F)F` (6%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (7%) | `Br[Ni](Br)(n1ccccc` (4%) | `[Br][Ni][Br].c1cc(` (2%) | set ✗ / any ✗ |

---

### Reaction #2130  yield=75.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #36)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)I.COc1ccc(S)cc1.C=Cc1ccc(-c2ccccc2)cc1>>COc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (72.5%) | `sacrificial_zinc` (21.0%) | `sacrificial_magnesium` (2.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (69.2%) | `zinc_generic` (17.3%) | `platinum_rod` (7.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.8%) | `carbon` (1.3%) | `nickel` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.3%) | `nickel_foam` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (99.0%) | `undivided` (0.9%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (54.5%) | `ABSENT` (37.6%) | `NEt4` (4.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (49.0%) | `ABSENT` (24.9%) | `Cl` (18.2%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (21.1%) | `boron_lewis_acid` (8.5%) | `hf_amine_complex` (2.4%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (95.9%) | `ABSENT` (3.3%) | `Fe_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (92.3%) | `polar_aprotic_nitrile` (2.6%) | `polar_aprotic_sulfoxide` (1.6%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (99%) | `O` (25%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `F[B-](F)(F)F.[H+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (40%) | `Br[Ni](Br)(n1ccccc` (25%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #2131  yield=84.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #37)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1.CC(C)c1ccc(S)cc1>>CC(C)c1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (72.2%) | `sacrificial_zinc` (14.2%) | `carbon` (6.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (81.0%) | `zinc_generic` (5.8%) | `platinum_rod` (5.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.6%) | `platinum_plate` (0.1%) | `nickel_foam` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (88.8%) | `undivided` (11.1%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.9%) | `ABSENT` (17.4%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (90.2%) | `ABSENT` (7.5%) | `Cl` (0.9%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `boron_lewis_acid` (50.7%) | `ABSENT` (10.5%) | `iodide_anion` (1.3%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (70.8%) | `ABSENT` (26.8%) | `Cu_complex` (1.7%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (88.9%) | `polar_aprotic_nitrile` (6.7%) | `ketone` (1.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (12%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `CCCC[N+](CCCC)(CCC` (49%) | `F[B-](F)(F)F.[H+]` (24%) | `__ABSENT__` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `__ABSENT__` (14%) | `Br[Ni](Br)(n1ccccc` (9%) | `[Br][Ni][Br].c1cc(` (2%) | set ✗ / any ✗ |

---

### Reaction #2132  yield=83.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #38)

```
Cc1ccccc1S.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1>>Cc1ccccc1SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c1ccc(-c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `sacrificial_zinc` (61.3%) | `platinum` (21.2%) | `carbon` (10.3%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `zinc_generic` (62.3%) | `platinum_generic` (11.9%) | `platinum_rod` (7.5%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.3%) | `nickel` (1.0%) | `carbon` (0.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (89.3%) | `nickel_foam` (4.9%) | `platinum_plate` (2.7%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (86.0%) | `undivided` (13.9%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (71.5%) | `NBu4` (27.2%) | `NEt4` (1.1%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (64.0%) | `BF4` (35.2%) | `Cl` (0.3%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `boron_lewis_acid` (15.5%) | `ABSENT` (13.9%) | `hf_amine_complex` (2.0%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (76.2%) | `ABSENT` (13.6%) | `Cu_complex` (7.8%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (96.1%) | `polar_aprotic_nitrile` (1.1%) | `ABSENT` (0.7%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (100%) | `O` (0%) | `O=CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `F[B-](F)(F)F.[H+]` (12%) | `__ABSENT__` (8%) | `CCCC[N+](CCCC)(CCC` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (11%) | `Br[Ni](Br)(n1ccccc` (8%) | `__ABSENT__` (6%) | set ✗ / any ✗ |

---

### Reaction #2133  yield=86.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #39)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1.CC(C)(C)c1ccc(S)cc1>>CC(C)(C)c1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (57.0%) | `sacrificial_zinc` (38.2%) | `carbon` (2.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_foil` | `platinum_generic` (64.7%) | `zinc_generic` (33.2%) | `platinum_rod` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.9%) | `carbon` (0.9%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.1%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (63.7%) | `undivided` (36.2%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (71.6%) | `NBu4` (25.2%) | `NEt4` (1.5%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (59.7%) | `BF4` (37.7%) | `Cl` (1.2%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (17.6%) | `boron_lewis_acid` (5.5%) | `thiol` (2.1%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (69.0%) | `ABSENT` (29.2%) | `Cu_complex` (0.7%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (90.7%) | `polar_aprotic_nitrile` (6.6%) | `ABSENT` (0.8%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (91%) | `O` (11%) | `CC#N` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `O=O` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (14%) | `Br[Ni](Br)(n1ccccc` (11%) | `COCCOC.[Br][Ni][Br` (1%) | set ✗ / any ✗ |

---

### Reaction #2134  yield=82.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #40)

```
Cc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1>>Cc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccc(-c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (49.7%) | `sacrificial_zinc` (38.0%) | `carbon` (5.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (47.9%) | `zinc_generic` (33.8%) | `platinum_rod` (6.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.8%) | `carbon` (0.9%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.0%) | `platinum_plate` (0.5%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (98.8%) | `undivided` (1.2%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.8%) | `ABSENT` (34.5%) | `NEt4` (2.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (67.9%) | `ABSENT` (27.7%) | `Br` (1.8%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (19.0%) | `boron_lewis_acid` (15.3%) | `metal_oxide_oxidant` (1.7%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (59.4%) | `ABSENT` (37.5%) | `Cu_complex` (2.0%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (82.8%) | `polar_aprotic_nitrile` (6.3%) | `ABSENT` (2.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (99%) | `O` (43%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (99%) | `O=O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (21%) | `Br[Ni](Br)(n1ccccc` (17%) | `__ABSENT__` (1%) | set ✗ / any ✗ |

---

### Reaction #2135  yield=83.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_37_13262-13269.json) (反应 idx 在该 JSON 内 = #41)

```
FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I.C=Cc1ccc(-c2ccccc2)cc1.Cc1ccc(S)c(C)c1>>Cc1ccc(SC(CC(F)(F)C(F)(F)C(F)(F)C(F)(F)F)c2ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `sacrificial_zinc` (76.2%) | `carbon` (13.2%) | `sacrificial_iron` (3.8%) | ✗ |
| 阳极 (细类) | 43 | `platinum_generic` | `zinc_generic` (60.1%) | `zinc_plate` (18.6%) | `platinum_rod` (6.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.2%) | `carbon` (1.6%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (85.1%) | `platinum_plate` (7.0%) | `platinum_wire` (4.6%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (93.2%) | `undivided` (6.8%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.7%) | `ABSENT` (21.4%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (77.9%) | `ABSENT` (20.9%) | `Br` (0.5%) | ✗ |
| 试剂大类 | 103 | `primary_amine` | `ABSENT` (17.4%) | `boron_lewis_acid` (7.3%) | `thiol` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (61.7%) | `ABSENT` (30.7%) | `Cu_complex` (5.5%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (88.5%) | `ABSENT` (9.7%) | `tfe` (0.6%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (99%) | `CC#N` (0%) | `__ABSENT__` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `NCCCN` | `__ABSENT__` (100%) | `O=O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (23%) | `__ABSENT__` (6%) | `Br[Ni](Br)(n1ccccc` (5%) | set ✗ / any ✗ |

---

### Reaction #2136  yield=20.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #0)

```
CCOC(=O)CC(=O)OCC.Cn1ccc2ccccc21.CC=Cc1c(OC)cc(OC)cc1OC>>CCOC(=O)C(C(=O)OCC)[C@H](C)[C@@H](c1c(OC)cc(OC)cc1OC)c1cn(C)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (92.2%) | `carbon_cloth` (3.9%) | `reticulated_vitreous_carbon` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.2%) | `nickel` (1.4%) | `carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (74.6%) | `platinum_generic` (25.1%) | `nickel_rod` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (94.1%) | `Li` (2.0%) | `ABSENT` (1.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `I` (80.7%) | `BF4` (9.3%) | `Cl` (4.8%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `alkali_sulfonate` (13.6%) | `o2_oxidant` (4.8%) | `alkali_carbonate` (4.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (99.0%) | `ABSENT` (0.8%) | `ionic_organocat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.7%) | `polar_protic_alcohol` (0.2%) | `halogenated_aliphatic` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (100%) | `ClCCl` (14%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O.[Na]` | `O=S(=O)([O-])C(F)(` (100%) | `O=O` (69%) | `O=[N+]([O-])[O-].[` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (99%) | `[Cl][Co][Cl]` (1%) | `CC(C)(C)c1ccc2[O-]` (0%) | set ✗ / any ✗ |

---

### Reaction #2137  yield=35.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #1)

```
Cn1ccc2ccccc21.C=Cc1ccc(OC)cc1.CCOC(=O)CC(=O)OC(C)(C)C>>CCOC(=O)[C@H](C[C@H](c1ccc(OC)cc1)c1cn(C)c2ccccc12)C(=O)OC(C)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (87.7%) | `carbon_cloth` (6.2%) | `carbon_felt` (2.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.3%) | `carbon` (2.3%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.8%) | `platinum_generic` (1.1%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (52.7%) | `ABSENT` (35.7%) | `Na` (6.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (57.9%) | `I` (11.2%) | `PF6` (7.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (10.3%) | `alkali_other_salt` (9.5%) | `alkali_carbonate` (4.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (93.1%) | `ABSENT` (2.2%) | `pyridine_organocat` (1.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (78.9%) | `halogenated_aliphatic` (6.9%) | `ketone` (5.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (98%) | `ClCCl` (15%) | `OCC(F)(F)F` (11%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (78%) | `O=S(=O)([O-])C(F)(` (16%) | `O=O` (11%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (78%) | `[Cl][Co][Cl]` (1%) | `CC(=O)[CH-]C(C)=O.` (1%) | set ✗ / any ✗ |

---

### Reaction #2138  yield=35.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #2)

```
Cn1ccc2ccccc21.C=Cc1ccc(OC)cc1.CCOC(=O)CC(=O)OC(C)(C)C>>CCOC(=O)[C@@H](C[C@H](c1ccc(OC)cc1)c1cn(C)c2ccccc12)C(=O)OC(C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (87.7%) | `carbon_cloth` (6.2%) | `carbon_felt` (2.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.3%) | `carbon` (2.3%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.8%) | `platinum_generic` (1.1%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (52.7%) | `ABSENT` (35.7%) | `Na` (6.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (57.9%) | `I` (11.2%) | `PF6` (7.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (10.3%) | `alkali_other_salt` (9.5%) | `alkali_carbonate` (4.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (93.1%) | `ABSENT` (2.2%) | `pyridine_organocat` (1.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (78.9%) | `halogenated_aliphatic` (6.9%) | `ketone` (5.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (98%) | `ClCCl` (15%) | `OCC(F)(F)F` (11%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (78%) | `O=S(=O)([O-])C(F)(` (16%) | `O=O` (11%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (78%) | `[Cl][Co][Cl]` (1%) | `CC(=O)[CH-]C(C)=O.` (1%) | set ✗ / any ✗ |

---

### Reaction #2139  yield=40.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #3)

```
CCOC(=O)CC(=O)OCC.Cn1ccc2ccccc21.CC=Cc1c(OC)cc(OC)cc1OC>>CCOC(=O)C(C(=O)OCC)[C@@H](C)[C@@H](c1c(OC)cc(OC)cc1OC)c1cn(C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (92.2%) | `carbon_cloth` (3.9%) | `reticulated_vitreous_carbon` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.2%) | `nickel` (1.4%) | `carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (74.6%) | `platinum_generic` (25.1%) | `nickel_rod` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.1%) | `Li` (2.0%) | `ABSENT` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (80.7%) | `BF4` (9.3%) | `Cl` (4.8%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `alkali_sulfonate` (13.6%) | `o2_oxidant` (4.8%) | `alkali_carbonate` (4.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (99.0%) | `ABSENT` (0.8%) | `ionic_organocat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.7%) | `polar_protic_alcohol` (0.2%) | `halogenated_aliphatic` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (100%) | `ClCCl` (14%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O.[Na]` | `O=S(=O)([O-])C(F)(` (100%) | `O=O` (69%) | `O=[N+]([O-])[O-].[` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (99%) | `[Cl][Co][Cl]` (1%) | `CC(C)(C)c1ccc2[O-]` (0%) | set ✗ / any ✗ |

---

### Reaction #2140  yield=50.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #4)

```
CCOC(=O)CC(=O)OCC.C=Cc1ccc(OC)cc1.Cc1cn(C)c2ccccc12>>CCOC(=O)C(CC(c1ccc(OC)cc1)c1c(C)c2ccccc2n1C)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `platinum` (2.0%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (59.7%) | `carbon_cloth` (14.9%) | `carbon_felt` (8.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `nickel` (0.2%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (96.5%) | `platinum_generic` (3.4%) | `nickel_foam` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.0%) | `Na` (0.4%) | `Li` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (47.9%) | `BF4` (15.7%) | `PF6` (15.0%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `alkali_other_salt` (17.7%) | `ABSENT` (6.7%) | `alkali_carbonate` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (76.5%) | `pyridine_organocat` (10.1%) | `ABSENT` (6.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (53.4%) | `tfe` (19.9%) | `ketone` (7.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (24%) | `[H+].[OH-]` (0%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=C(O)O.[K]` (32%) | `__ABSENT__` (12%) | `O=O` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Cl-].[Cl-].[Co+2]` (39%) | `__ABSENT__` (6%) | `CC(=O)[CH-]C(C)=O.` (6%) | set ✗ / any ✗ |

---

### Reaction #2141  yield=56.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #5)

```
CCOC(=O)CC(=O)OCC.Cn1ccc2ccccc21.C=Cc1ccccc1OC>>CCOC(=O)C(CC(c1ccccc1OC)c1cn(C)c2ccccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.5%) | `platinum` (2.1%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (65.2%) | `carbon_felt` (13.3%) | `reticulated_vitreous_carbon` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.5%) | `nickel` (0.4%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (68.7%) | `platinum_plate` (30.3%) | `carbon_felt` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.2%) | `ABSENT` (1.0%) | `Li` (0.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (35.5%) | `ClO4` (24.0%) | `Cl` (11.2%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `o2_oxidant` (58.0%) | `alkali_other_salt` (11.5%) | `ABSENT` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (98.6%) | `pyridine_organocat` (0.5%) | `ABSENT` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.5%) | `ABSENT` (1.5%) | `polar_protic_alcohol` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (96%) | `__ABSENT__` (0%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=O` (98%) | `__ABSENT__` (4%) | `O=S(=O)([O-])C(F)(` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Cl-].[Cl-].[Co+2]` (77%) | `CC(C)(C)c1ccc2[O-]` (9%) | `__ABSENT__` (4%) | set ✗ / any ✗ |

---

### Reaction #2142  yield=52.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #6)

```
CCOC(=O)CC(=O)OCC.Cn1ccc2ccccc21.C=Cc1cc2ccccc2o1>>CCOC(=O)C(CC(c1cc2ccccc2o1)c1cn(C)c2ccccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `platinum` (1.7%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (54.5%) | `carbon_cloth` (28.5%) | `unknown_electrode` (5.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (75.9%) | `platinum_generic` (24.0%) | `carbon_felt` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.4%) | `ABSENT` (7.1%) | `Li` (2.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (31.3%) | `ABSENT` (20.8%) | `PF6` (17.9%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `alkali_other_salt` (34.6%) | `alkali_carbonate` (15.5%) | `o2_oxidant` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (93.1%) | `pyridine_organocat` (2.4%) | `ABSENT` (2.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.7%) | `ketone` (11.2%) | `tfe` (2.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (97%) | `CC(C)=O` (0%) | `OCC(F)(F)F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=C(O)O.[K]` (51%) | `O=C(O)O.[Na]` (7%) | `__ABSENT__` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `CC(C)(C)c1ccc2[O-]` (23%) | `__ABSENT__` (15%) | `[Cl-].[Cl-].[Co+2]` (8%) | set ✗ / any ✗ |

---

### Reaction #2143  yield=51.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #7)

```
CCOC(=O)CC(=O)OCC.Cn1ccc2ccccc21.C=Cc1cc2c(cc1Br)OCO2>>CCOC(=O)C(CC(c1cc2c(cc1Br)OCO2)c1cn(C)c2ccccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (96.4%) | `carbon_generic` (1.8%) | `reticulated_vitreous_carbon` (1.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `nickel` (0.2%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (85.3%) | `platinum_plate` (14.6%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.4%) | `Li` (0.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (59.3%) | `PF6` (22.2%) | `BF4` (11.1%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `alkali_sulfonate` (32.8%) | `alkali_other_salt` (23.3%) | `alkali_sulfinate` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (99.7%) | `pyridine_organocat` (0.2%) | `ABSENT` (0.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.7%) | `tfe` (0.4%) | `polar_protic_alcohol` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (99%) | `CC(C)=O` (0%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=S(=O)([O-])C(F)(` (98%) | `O=O` (6%) | `O=S([O-])[O-].[Na+` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Cl-].[Cl-].[Co+2]` (88%) | `[Cl][Co][Cl]` (7%) | `CC(=O)[CH-]C(C)=O.` (3%) | set ✗ / any ✗ |

---

### Reaction #2144  yield=57.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #8)

```
CCOC(=O)CC(=O)OCC.Cn1ccc2ccccc21.C=Cc1sccc1C>>CCOC(=O)C(CC(c1sccc1C)c1cn(C)c2ccccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (58.2%) | `reticulated_vitreous_carbon` (29.0%) | `carbon_generic` (5.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (92.9%) | `platinum_generic` (7.1%) | `unknown_electrode` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.2%) | `ABSENT` (2.2%) | `NEt4` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `PF6` (88.6%) | `ABSENT` (3.7%) | `I` (3.3%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `alkali_other_salt` (14.3%) | `ABSENT` (8.7%) | `o2_oxidant` (4.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (96.0%) | `Cu_complex` (1.5%) | `ABSENT` (0.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.0%) | `tfe` (4.8%) | `halogenated_aliphatic` (2.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (100%) | `ClCCl` (6%) | `COC(C)(C)C` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O.[Na]` | `O=C(O)O.[Na]` (23%) | `__ABSENT__` (13%) | `O=S(=O)([O-])C(F)(` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (68%) | `CC(C)(C)c1ccc2[O-]` (5%) | `[Cl][Co][Cl]` (4%) | set ✗ / any ✗ |

---

### Reaction #2145  yield=53.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #9)

```
CCOC(=O)CC(=O)OCC.Cn1ccc2ccccc21.C=Cc1ccc(OC)c(Cl)c1>>CCOC(=O)C(CC(c1ccc(OC)c(Cl)c1)c1cn(C)c2ccccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (98.8%) | `reticulated_vitreous_carbon` (0.7%) | `carbon_cloth` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (86.6%) | `platinum_generic` (13.4%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.1%) | `NEt4` (4.6%) | `Li` (1.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (75.9%) | `Cl` (8.2%) | `ClO4` (7.0%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `alkali_sulfonate` (11.8%) | `ABSENT` (10.7%) | `alkali_other_salt` (7.6%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (91.8%) | `ABSENT` (6.3%) | `pyridine_organocat` (1.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.6%) | `halogenated_aliphatic` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (100%) | `ClCCl` (48%) | `[H+].[OH-]` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=S(=O)([O-])C(F)(` (97%) | `O=O` (55%) | `[Cl-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Cl-].[Cl-].[Co+2]` (92%) | `[Cl][Co][Cl]` (3%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✗ / any ✗ |

---

### Reaction #2146  yield=69.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #10)

```
Cn1ccc2ccccc21.C=Cc1ccc(OC)cc1.O=C(CC(=O)OCc1ccccc1)OCc1ccccc1>>COc1ccc(C(CC(C(=O)OCc2ccccc2)C(=O)OCc2ccccc2)c2cn(C)c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (79.1%) | `carbon_felt` (6.1%) | `boron_doped_diamond` (5.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.1%) | `carbon` (10.1%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.0%) | `platinum_generic` (0.6%) | `graphite_rod` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (0.9%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (66.1%) | `Na` (20.5%) | `Li` (7.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (31.0%) | `I` (18.5%) | `OTf` (11.8%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (17.5%) | `alkali_other_salt` (4.1%) | `alkali_carboxylate` (2.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (92.2%) | `ABSENT` (2.2%) | `Fe_complex` (2.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (58.0%) | `halogenated_aliphatic` (12.7%) | `nitroalkane` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (99%) | `ClCCl` (54%) | `COC(C)(C)C` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (85%) | `O=O` (17%) | `O=S(=O)([O-])C(F)(` (12%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl-].[Cl-].[Co+2]` (89%) | `CC(=O)[CH-]C(C)=O.` (1%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✗ / any ✗ |

---

### Reaction #2147  yield=68.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #11)

```
Cn1cccc1.CCOC(=O)CC(=O)OCC.C=Cc1ccc(OC)cc1>>CCOC(=O)C(CC(c1ccc(OC)cc1)c1ccn(C)c1)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `ABSENT` (0.2%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (58.5%) | `reticulated_vitreous_carbon` (19.2%) | `carbon_felt` (15.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.5%) | `carbon` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (91.9%) | `platinum_plate` (6.9%) | `carbon_felt` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (68.7%) | `ABSENT` (31.1%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (56.9%) | `Li` (36.3%) | `ABSENT` (4.8%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `I` (36.8%) | `ClO4` (33.9%) | `PF6` (24.7%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `alkali_sulfonate` (11.6%) | `ABSENT` (6.3%) | `alkali_other_salt` (3.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (95.1%) | `Ir_complex` (1.0%) | `ABSENT` (1.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.6%) | `nitroalkane` (7.8%) | `ABSENT` (2.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (88%) | `C1CCOC1` (0%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=S(=O)([O-])C(F)(` (94%) | `O=O` (25%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (82%) | `[Cl][Co][Cl]` (5%) | `__OTHER__` (4%) | set ✗ / any ✗ |

---

### Reaction #2148  yield=68.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #12)

```
CCOC(=O)CC(=O)OCC.Cn1ccc2ccccc21.C=Cc1ccc2cc(OC)ccc2c1>>CCOC(=O)C(CC(c1ccc2cc(OC)ccc2c1)c1cn(C)c2ccccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (91.1%) | `reticulated_vitreous_carbon` (6.6%) | `carbon_felt` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.0%) | `carbon` (0.9%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (87.9%) | `platinum_generic` (11.8%) | `graphite_rod` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (89.5%) | `Na` (4.5%) | `ABSENT` (3.4%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `I` (54.7%) | `PF6` (8.1%) | `molecular_no_ion` (7.0%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `alkali_other_salt` (17.7%) | `ABSENT` (11.0%) | `alkali_sulfonate` (8.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (99.4%) | `ABSENT` (0.3%) | `pyridine_organocat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.7%) | `tfe` (2.5%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (100%) | `ClCCl` (6%) | `[H+].[OH-]` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=S(=O)([O-])C(F)(` (33%) | `O=O` (30%) | `__ABSENT__` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (71%) | `CC(=O)[O-].CC(=O)[` (3%) | `[Cl][Co][Cl]` (2%) | set ✗ / any ✗ |

---

### Reaction #2149  yield=68.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #13)

```
CCOC(=O)CC(=O)OCC.Cn1ccc2ccccc21.C=Cc1ccc(C)cc1>>CCOC(=O)C(CC(c1ccc(C)cc1)c1cn(C)c2ccccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (89.8%) | `reticulated_vitreous_carbon` (4.9%) | `carbon_generic` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.0%) | `carbon` (1.7%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (91.8%) | `platinum_generic` (7.9%) | `graphite_rod` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.6%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (55.0%) | `ABSENT` (41.6%) | `Li` (2.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ABSENT` (65.4%) | `I` (13.1%) | `BF4` (7.3%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `alkali_other_salt` (46.2%) | `alkali_sulfonate` (10.0%) | `alkali_sulfinate` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (97.1%) | `ABSENT` (1.6%) | `pyridine_organocat` (0.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.7%) | `ABSENT` (20.1%) | `tfe` (6.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (99%) | `ClCCl` (1%) | `OCC(F)(F)F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=O` (45%) | `Fc1c(F)c(F)c(B(c2c` (26%) | `O=S(O)O.[Na]` (12%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (48%) | `[Cl][Co][Cl]` (17%) | `__OTHER__` (5%) | set ✗ / any ✗ |

---

### Reaction #2150  yield=61.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #14)

```
CCOC(=O)CC(=O)OCC.C=Cc1ccc(OC)cc1.Cn1ccc2cc(C#N)ccc21>>CCOC(=O)C(CC(c1ccc(OC)cc1)c1cn(C)c2ccc(C#N)cc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (71.9%) | `graphite_rod` (9.8%) | `carbon_felt` (8.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.3%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (79.2%) | `platinum_plate` (20.2%) | `carbon_felt` (0.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.9%) | `ABSENT` (3.0%) | `Na` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (24.6%) | `I` (20.2%) | `ABSENT` (18.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carboxylate` | `o2_oxidant` (71.5%) | `alkali_sulfonate` (2.1%) | `alkali_other_salt` (1.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (55.1%) | `Co_complex` (41.9%) | `pyridine_organocat` (1.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (94.4%) | `nitroalkane` (3.8%) | `halogenated_aliphatic` (0.7%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `__ABSENT__` (100%) | `ClCCl` (0%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=O` (100%) | `O=S(=O)([O-])C(F)(` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (3%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2151  yield=70.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #15)

```
CCOC(=O)CC(=O)OCC.Cn1ccc2ccccc21.C=Cc1c(OC)cc(OC)cc1OC>>CCOC(=O)C(CC(c1c(OC)cc(OC)cc1OC)c1cn(C)c2ccccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (92.8%) | `reticulated_vitreous_carbon` (6.5%) | `carbon_cloth` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (60.8%) | `platinum_plate` (39.2%) | `nickel_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (93.3%) | `Li` (2.5%) | `ABSENT` (2.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `I` (75.1%) | `PF6` (8.2%) | `ClO4` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `alkali_sulfonate` (28.1%) | `alkali_other_salt` (16.3%) | `o2_oxidant` (4.1%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (100.0%) | `pyridine_organocat` (0.0%) | `ABSENT` (0.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.2%) | `tfe` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (100%) | `ClCCl` (2%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O.[Na]` | `O=S(=O)([O-])C(F)(` (98%) | `O=O` (91%) | `O=S([O-])[O-].[Na+` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (95%) | `[Cl][Co][Cl]` (4%) | `c1ccncc1` (1%) | set ✗ / any ✗ |

---

### Reaction #2152  yield=73.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #16)

```
CCOC(=O)CC(=O)OCC.C=Cc1ccc(OC)cc1.Cn1c(-c2ccccc2)cc2ccccc21>>CCOC(=O)C(CC(c1ccc(OC)cc1)c1c(-c2ccccc2)n(C)c2ccccc12)C(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (52.1%) | `graphite_rod` (25.8%) | `reticulated_vitreous_carbon` (14.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.1%) | `carbon` (0.7%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (56.2%) | `platinum_generic` (43.1%) | `carbon_felt` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.3%) | `Li` (2.9%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (50.7%) | `ClO4` (19.3%) | `PF6` (8.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `alkali_other_salt` (16.5%) | `ABSENT` (5.9%) | `o2_oxidant` (4.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (76.1%) | `pyridine_organocat` (13.8%) | `ABSENT` (4.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.3%) | `ABSENT` (2.9%) | `ketone` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (99%) | `COC(C)(C)C` (0%) | `FC(F)(F)c1ccccc1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (56%) | `C[Si](C)(C)N=[N+]=` (19%) | `O=O` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Cl-].[Cl-].[Co+2]` (38%) | `__OTHER__` (8%) | `[Cl][Co][Cl]` (3%) | set ✗ / any ✗ |

---

### Reaction #2153  yield=76.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #17)

```
CCOC(=O)CC(=O)OCC.Cn1ccc2ccccc21.C=Cc1ccc(OCc2ccccc2)cc1>>CCOC(=O)C(CC(c1ccc(OCc2ccccc2)cc1)c1cn(C)c2ccccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (96.4%) | `reticulated_vitreous_carbon` (1.7%) | `carbon_generic` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `carbon` (0.4%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (64.2%) | `platinum_generic` (35.6%) | `carbon_felt` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.5%) | `ABSENT` (5.1%) | `Na` (0.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (57.5%) | `PF6` (15.5%) | `ABSENT` (12.9%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `alkali_other_salt` (41.3%) | `alkali_sulfonate` (11.6%) | `o2_oxidant` (4.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (98.9%) | `ABSENT` (0.7%) | `pyridine_organocat` (0.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (91.3%) | `ABSENT` (3.9%) | `halogenated_aliphatic` (2.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (99%) | `ClCCl` (1%) | `OCC(F)(F)F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=O` (56%) | `O=S(=O)([O-])C(F)(` (22%) | `Fc1c(F)c(F)c(B(c2c` (14%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (79%) | `[Cl][Co][Cl]` (14%) | `c1ccncc1` (2%) | set ✗ / any ✗ |

---

### Reaction #2154  yield=73.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #18)

```
CCOC(=O)CC(=O)OCC.C=Cc1ccc(OC)cc1.c1cc2c3c(c1)ccn3CCC2>>CCOC(=O)C(CC(c1ccc(OC)cc1)c1cn2c3c(cccc13)CCC2)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `sacrificial_zinc` (0.2%) | `sacrificial_aluminum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (89.2%) | `reticulated_vitreous_carbon` (3.7%) | `carbon_felt` (2.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.8%) | `carbon` (1.0%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (98.2%) | `platinum_plate` (1.5%) | `carbon_felt` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.5%) | `Na` (0.3%) | `Li` (0.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `I` (71.1%) | `PF6` (13.4%) | `BF4` (10.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `alkali_sulfonate` (11.1%) | `ABSENT` (8.8%) | `hydrosilane` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (99.4%) | `ABSENT` (0.4%) | `Ni_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.8%) | `tfe` (1.1%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (96%) | `ClCCl` (1%) | `FC(F)(F)c1ccccc1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=S(=O)([O-])C(F)(` (97%) | `O=O` (35%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (48%) | `[Cl][Co][Cl]` (39%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #2155  yield=76.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #19)

```
CCOC(=O)CC(=O)OCC.C=Cc1ccc(OC)cc1.CCCCCCn1ccc2ccccc21>>CCCCCCn1cc(C(CC(C(=O)OCC)C(=O)OCC)c2ccc(OC)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (47.3%) | `carbon_cloth` (19.5%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.2%) | `carbon` (0.7%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (55.3%) | `platinum_plate` (44.3%) | `unknown_electrode` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (60.3%) | `Li` (38.1%) | `Na` (1.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (65.7%) | `I` (9.6%) | `molecular_no_ion` (8.5%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (18.3%) | `alkali_sulfonate` (5.6%) | `o2_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (98.0%) | `ABSENT` (1.0%) | `pyridine_organocat` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `ketone` (0.5%) | `tfe` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (99%) | `ClCCl` (2%) | `OCC(F)(F)F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O.[Na]` | `__ABSENT__` (99%) | `O=S(=O)([O-])C(F)(` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (93%) | `[Cl][Co][Cl]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |

---

### Reaction #2156  yield=73.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #20)

```
CCOC(=O)CC(=O)OCC.Cn1ccc2ccccc21.C=Cc1ccc(SC)cc1>>CCOC(=O)C(CC(c1ccc(SC)cc1)c1cn(C)c2ccccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (58.8%) | `carbon_generic` (14.2%) | `graphite_rod` (12.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.1%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (82.2%) | `platinum_plate` (17.7%) | `carbon_felt` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.0%) | `ABSENT` (3.1%) | `Li` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (25.0%) | `PF6` (21.9%) | `I` (19.2%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `o2_oxidant` (11.9%) | `alkali_other_salt` (8.8%) | `alkali_sulfonate` (5.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (82.7%) | `ABSENT` (5.1%) | `Cu_complex` (4.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (55.4%) | `halogenated_aliphatic` (26.2%) | `ABSENT` (11.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (93%) | `ClCCl` (2%) | `O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=O` (98%) | `C[Si](C)(C)N=[N+]=` (2%) | `__ABSENT__` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (42%) | `__ABSENT__` (5%) | `[Cl][Co][Cl]` (4%) | set ✗ / any ✗ |

---

### Reaction #2157  yield=78.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #21)

```
COC(=O)CC(=O)OC.Cn1ccc2ccccc21.C=Cc1ccc(OC)cc1>>COC(=O)C(CC(c1ccc(OC)cc1)c1cn(C)c2ccccc12)C(=O)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (56.4%) | `reticulated_vitreous_carbon` (16.4%) | `unknown_electrode` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.6%) | `carbon` (2.6%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (96.1%) | `platinum_generic` (3.8%) | `graphite_plate` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (54.9%) | `NBu4` (37.3%) | `ABSENT` (5.7%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `carboxylate` (30.8%) | `I` (23.8%) | `Cl` (14.4%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.5%) | `alkali_other_salt` (5.6%) | `metal_oxide_oxidant` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (97.1%) | `ABSENT` (2.0%) | `Mn_complex` (0.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (87.8%) | `halogenated_aliphatic` (7.1%) | `tfe` (2.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (100%) | `ClCCl` (86%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (69%) | `O=S(=O)([O-])C(F)(` (19%) | `O=O` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (93%) | `CC(=O)[O-].CC(=O)[` (1%) | `CC(C)(C)c1ccc2[O-]` (1%) | set ✗ / any ✗ |

---

### Reaction #2158  yield=75.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #22)

```
Cn1ccc2ccccc21.CCOC(=O)C(C)C(=O)OCC.C=Cc1ccc(OC)cc1>>CCOC(=O)C(C)(CC(c1ccc(OC)cc1)c1cn(C)c2ccccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (100.0%) | `carbon_generic` (0.0%) | `carbon_rod` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `carbon` (0.9%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (88.8%) | `platinum_generic` (11.2%) | `graphite_rod` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (79.9%) | `ABSENT` (14.4%) | `Na` (4.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `I` (49.7%) | `ABSENT` (18.5%) | `OTf` (10.3%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `alkali_sulfonate` (14.9%) | `alkali_other_salt` (10.2%) | `ABSENT` (6.0%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (99.6%) | `ABSENT` (0.2%) | `pyridine_organocat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.1%) | `halogenated_aliphatic` (2.0%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (99%) | `ClCCl` (63%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O.[Na]` | `O=S(=O)([O-])C(F)(` (98%) | `O=O` (80%) | `Fc1c(F)c(F)c(B(c2c` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Cl-].[Cl-].[Co+2]` (99%) | `[Cl][Co][Cl]` (1%) | `CC(=O)[CH-]C(C)=O.` (1%) | set ✗ / any ✗ |

---

### Reaction #2159  yield=78.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #23)

```
CCOC(=O)CC(=O)OCC.Cn1ccc2ccccc21.C=Cc1ccc(OC)cc1>>CCOC(=O)C(CC(c1ccc(OC)cc1)c1cn(C)c2ccccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (88.4%) | `reticulated_vitreous_carbon` (3.6%) | `carbon_cloth` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.3%) | `carbon` (1.5%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.3%) | `platinum_generic` (0.7%) | `carbon_felt` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.2%) | `Na` (22.5%) | `ABSENT` (19.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ABSENT` (29.4%) | `I` (15.0%) | `OTf` (13.4%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (12.8%) | `alkali_other_salt` (7.6%) | `o2_oxidant` (4.0%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (98.9%) | `ABSENT` (0.5%) | `pyridine_organocat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `halogenated_aliphatic` (9.2%) | `tfe` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (99%) | `ClCCl` (75%) | `OCC(F)(F)F` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (49%) | `O=S(=O)([O-])C(F)(` (45%) | `O=O` (35%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Cl-].[Cl-].[Co+2]` (95%) | `CC(=O)[CH-]C(C)=O.` (1%) | `CC(=O)[O-].CC(=O)[` (1%) | set ✗ / any ✗ |

---

### Reaction #2160  yield=72.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #24)

```
CCOC(=O)CC(=O)OCC.C=Cc1ccc(OC)cc1.Cn1ccc2cc(Cl)ccc21>>CCOC(=O)C(CC(c1ccc(OC)cc1)c1cn(C)c2ccc(Cl)cc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.4%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_felt` (40.4%) | `reticulated_vitreous_carbon` (24.4%) | `graphite_rod` (16.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `carbon` (0.4%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (68.4%) | `platinum_plate` (30.7%) | `carbon_felt` (0.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (96.3%) | `NBu4` (2.0%) | `Na` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (93.4%) | `Cl` (5.5%) | `molecular_no_ion` (0.4%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (8.6%) | `alkali_other_salt` (4.5%) | `o2_oxidant` (3.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (74.9%) | `ABSENT` (21.9%) | `Fe_complex` (1.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (44.0%) | `polar_aprotic_nitrile` (33.1%) | `halogenated_aliphatic` (5.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `__ABSENT__` (99%) | `ClCCl` (0%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (100%) | `O=O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (14%) | `__OTHER__` (10%) | `CC(C)(C)c1ccc2[O-]` (8%) | set ✗ / any ✗ |

---

### Reaction #2161  yield=77.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #25)

```
CCOC(=O)CC(=O)OCC.C=Cc1ccc(OC)cc1.COc1ccc2ccn(C)c2c1>>CCOC(=O)C(CC(c1ccc(OC)cc1)c1cn(C)c2cc(OC)ccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (88.5%) | `carbon_felt` (6.3%) | `reticulated_vitreous_carbon` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (97.3%) | `platinum_generic` (2.6%) | `carbon_felt` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (90.9%) | `ABSENT` (4.2%) | `Li` (3.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (26.9%) | `ClO4` (17.1%) | `ABSENT` (16.8%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `alkali_other_salt` (11.1%) | `ABSENT` (6.7%) | `alkali_sulfonate` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (97.6%) | `ABSENT` (1.9%) | `pyridine_organocat` (0.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (77.5%) | `ABSENT` (6.9%) | `tfe` (5.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (90%) | `ClCCl` (28%) | `FC(F)(F)c1ccccc1` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=O` (80%) | `O=S(=O)([O-])C(F)(` (41%) | `__ABSENT__` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (84%) | `CC(=O)[CH-]C(C)=O.` (7%) | `c1ccncc1` (2%) | set ✗ / any ✗ |

---

### Reaction #2162  yield=74.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #26)

```
CCOC(=O)CC(=O)OCC.C=Cc1ccc(OC)cc1.Cn1ccc2ccc(F)cc21>>CCOC(=O)C(CC(c1ccc(OC)cc1)c1cn(C)c2cc(F)ccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (81.3%) | `reticulated_vitreous_carbon` (8.7%) | `carbon_felt` (8.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (88.9%) | `platinum_generic` (11.1%) | `carbon_felt` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (86.0%) | `ABSENT` (10.2%) | `Na` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (34.9%) | `ABSENT` (34.2%) | `carboxylate` (8.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (9.3%) | `alkali_other_salt` (7.8%) | `alkali_sulfonate` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (84.6%) | `ABSENT` (13.9%) | `Fe_complex` (0.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (70.2%) | `halogenated_aliphatic` (13.6%) | `ABSENT` (6.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (93%) | `ClCCl` (49%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (99%) | `O=O` (2%) | `O=S(=O)([O-])C(F)(` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (43%) | `CC(=O)[CH-]C(C)=O.` (6%) | `__ABSENT__` (5%) | set ✗ / any ✗ |

---

### Reaction #2163  yield=72.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #27)

```
CCOC(=O)CC(=O)OCC.C=Cc1ccc(OC)cc1.Cn1ccc2c(Br)cccc21>>CCOC(=O)C(CC(c1ccc(OC)cc1)c1cn(C)c2cccc(Br)c12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (1.2%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (53.4%) | `carbon_felt` (27.9%) | `carbon_cloth` (10.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.3%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (86.4%) | `platinum_generic` (13.0%) | `carbon_felt` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (87.1%) | `ABSENT` (10.8%) | `Li` (1.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (42.0%) | `ClO4` (17.2%) | `BF4` (11.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (17.1%) | `o2_oxidant` (4.9%) | `alkali_other_salt` (2.8%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (66.3%) | `ABSENT` (21.3%) | `Ir_complex` (3.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (29.6%) | `nitroalkane` (27.4%) | `ketone` (17.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (39%) | `OCC(F)(F)F` (4%) | `FC(F)(F)c1ccccc1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O.[Na]` | `__ABSENT__` (100%) | `O=O` (1%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (14%) | `__ABSENT__` (8%) | `CC(C)(C)c1ccc2[O-]` (7%) | set ✗ / any ✗ |

---

### Reaction #2164  yield=72.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #28)

```
CCOC(=O)CC(=O)OCC.Cn1ccc2ccccc21.C=C(C)c1ccc(OC)cc1>>CCOC(=O)C(CC(C)(c1ccc(OC)cc1)c1cn(C)c2ccccc12)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (84.8%) | `carbon_generic` (13.5%) | `unknown_electrode` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.5%) | `carbon` (0.4%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (53.9%) | `platinum_generic` (46.0%) | `reticulated_vitreous_carbon` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (92.0%) | `NBu4` (6.3%) | `Na` (1.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (96.1%) | `PF6` (1.7%) | `Cl` (0.8%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `o2_oxidant` (23.0%) | `alkali_other_salt` (10.2%) | `ABSENT` (7.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (99.0%) | `pyridine_organocat` (0.3%) | `ABSENT` (0.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.4%) | `ketone` (0.4%) | `aqueous` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (99%) | `ClCCl` (1%) | `OCC(F)(F)F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=O` (100%) | `O=S(=O)([O-])C(F)(` (1%) | `O=S([O-])[O-].[Na+` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (97%) | `CC(=O)[CH-]C(C)=O.` (1%) | `c1ccncc1` (1%) | set ✗ / any ✗ |

---

### Reaction #2165  yield=88.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #29)

```
COC(=O)C(F)C(=O)OC.Cn1ccc2ccccc21.C=Cc1ccc(OC)cc1>>COC(=O)C(F)(CC(c1ccc(OC)cc1)c1cn(C)c2ccccc12)C(=O)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (93.9%) | `reticulated_vitreous_carbon` (4.6%) | `graphite_felt` (0.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.1%) | `carbon` (0.7%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (97.0%) | `platinum_generic` (3.0%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (73.8%) | `Na` (19.3%) | `ABSENT` (5.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (50.8%) | `I` (15.9%) | `Cl` (10.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (15.7%) | `alkali_sulfonate` (4.3%) | `alkali_carbonate` (3.0%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (98.8%) | `Fe_complex` (0.7%) | `ferrocene_mediator` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.4%) | `polar_protic_alcohol` (16.2%) | `tfe` (8.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (97%) | `ClCCl` (10%) | `CO` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (70%) | `O=S(=O)([O-])C(F)(` (27%) | `O=C([O-])[O-].[Na+` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Cl-].[Cl-].[Co+2]` (90%) | `CC(=O)[CH-]C(C)=O.` (1%) | `[Cl][Co][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #2166  yield=81.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #30)

```
CCOC(=O)CC(=O)OCC.C=Cc1ccc(OC)cc1.c1ccc(-c2ccc(Cn3ccc4ccccc43)cc2)cc1>>CCOC(=O)C(CC(c1ccc(OC)cc1)c1cn(Cc2ccc(-c3ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `sacrificial_iron` (0.6%) | `sacrificial_zinc` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (30.0%) | `graphite_rod` (27.3%) | `carbon_felt` (16.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (91.1%) | `nickel` (7.4%) | `carbon` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (83.9%) | `nickel_foam` (12.4%) | `platinum_plate` (2.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.6%) | `Li` (7.9%) | `Na` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (52.5%) | `ClO4` (32.9%) | `molecular_no_ion` (7.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `alkali_sulfonate` (12.0%) | `ABSENT` (9.0%) | `hydrosilane` (5.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (97.4%) | `ABSENT` (1.3%) | `Ni_complex` (0.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (93.8%) | `ketone` (2.9%) | `tfe` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (98%) | `CC(C)=O` (0%) | `CN(C)C=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=S(=O)([O-])C(F)(` (62%) | `__ABSENT__` (18%) | `C[SiH](C)O[SiH](C)` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Cl-].[Cl-].[Co+2]` (39%) | `__ABSENT__` (20%) | `[Cl][Co][Cl]` (4%) | set ✗ / any ✗ |

---

### Reaction #2167  yield=81.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_9_3232-3242.json) (反应 idx 在该 JSON 内 = #31)

```
Cn1ccc2ccccc21.C=Cc1ccc(OC)cc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(c1ccc(OC)cc1)c1cn(C)c2ccccc12)(C(=O)OCC)C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (99.8%) | `unknown_electrode` (0.1%) | `graphite_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `carbon` (0.5%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (72.1%) | `platinum_generic` (27.8%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (48.7%) | `Na` (41.3%) | `ABSENT` (4.6%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `I` (60.8%) | `Cl` (9.4%) | `OTf` (8.9%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `o2_oxidant` (7.5%) | `ABSENT` (6.5%) | `alkali_sulfonate` (5.8%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (99.8%) | `ABSENT` (0.1%) | `Mn_complex` (0.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (91.8%) | `halogenated_aliphatic` (5.3%) | `cyclic_ether` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (99%) | `ClCCl` (92%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `O=O` (100%) | `O=S(=O)([O-])C(F)(` (49%) | `Fc1c(F)c(F)c(B(c2c` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Cl-].[Cl-].[Co+2]` (100%) | `[Cl][Co][Cl]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #2168  yield=50.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccc1NC(=O)C1CCCC1>>CC1(CCl)OC(C2CCCC2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `carbon` (0.6%) | `sacrificial_magnesium` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (99.7%) | `platinum_generic` (0.3%) | `carbon_rod` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.6%) | `platinum_generic` (0.4%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.4%) | `NEt4` (9.2%) | `Na` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `Cl` (99.0%) | `I` (0.3%) | `Br` (0.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `phosphine_neutral` | `ABSENT` (39.2%) | `electrophilic_N_F` (1.8%) | `unparseable_text` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.2%) | `ABSENT` (0.5%) | `pyridine_organocat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (99.5%) | `halogenated_aliphatic` (0.2%) | `polar_protic_acid` (0.2%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (100%) | `ClCCl` (0%) | `O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([PH](=O)c2c` | `__ABSENT__` (100%) | `Cc1ccc([P+](=O)c2c` (0%) | `COC(=O)c1ccc2cc(C(` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (99%) | `N#Cc1cc(C#N)c(-n2c` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |

---

### Reaction #2169  yield=56.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #1)

```
C=C(C)c1ccc(C)cc1NC(=O)c1ccc(C)cc1>>Cc1ccc(C2=Nc3cc(C)ccc3C(C)(CBr)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (96.9%) | `carbon` (3.1%) | `sacrificial_zinc` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (80.1%) | `platinum_generic` (17.3%) | `graphite_rod` (1.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (92.0%) | `platinum_generic` (7.9%) | `nickel_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (87.4%) | `divided` (12.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (51.3%) | `NBu4` (35.4%) | `ABSENT` (7.1%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (99.6%) | `Cl` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (9.3%) | `alkali_other_salt` (6.0%) | `alkali_bicarbonate` (4.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (50.8%) | `organic_neutral_cat` (44.7%) | `Pt_complex` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (62.9%) | `polar_aprotic_sulfoxide` (14.1%) | `aromatic_hydrocarbon` (8.3%) | ✗ |
| 溶剂 set | 79 | `CO` | `CC#N` (93%) | `O` (36%) | `O=C(O)C(F)(F)F` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (89%) | `O=C(O)C(F)(F)F` (8%) | `CC(=O)O` (4%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (82%) | `N#Cc1c(C#N)c(-n2c3` (14%) | `CC(C)c1cc(C(C)C)c(` (2%) | set ✓ / any ✓ |

---

### Reaction #2170  yield=55.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #2)

```
C=C(C)c1ccccc1NC(=O)CCCCC>>CCCCCC1=Nc2ccccc2C(C)(CCl)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (72.0%) | `carbon` (27.7%) | `sacrificial_iron` (0.2%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (97.3%) | `graphite_rod` (0.9%) | `platinum_generic` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.2%) | `nickel` (0.7%) | `stainless_steel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.6%) | `NEt4` (7.5%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `Cl` (91.8%) | `BF4` (5.1%) | `Br` (1.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `phosphine_neutral` | `ABSENT` (23.1%) | `metal_oxide_oxidant` (2.2%) | `disulfide` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (89.6%) | `ABSENT` (8.8%) | `Mn_complex` (0.4%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (99.3%) | `halogenated_aliphatic` (0.4%) | `polar_protic_acid` (0.1%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (100%) | `ClCCl` (1%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (99%) | `O=C(O)C(F)(F)F` (1%) | `O=S(=O)(O)O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (86%) | `N#Cc1cc(C#N)c(-n2c` (5%) | `CC(C)c1cc(C(C)C)c(` (1%) | set ✗ / any ✗ |

---

### Reaction #2171  yield=52.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #3)

```
C=C(C)c1ccccc1NC(=O)Cc1ccccc1>>CC1(CCl)OC(Cc2ccccc2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_felt` | `platinum_plate` (90.5%) | `platinum_generic` (9.5%) | `carbon_cloth` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.5%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (78.7%) | `platinum_generic` (21.3%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.7%) | `NEt4` (13.6%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `Cl` (96.8%) | `BF4` (1.8%) | `Br` (0.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `phosphine_neutral` | `ABSENT` (33.1%) | `electrophilic_N_F` (2.0%) | `unparseable_text` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (89.8%) | `ABSENT` (9.5%) | `pyridine_organocat` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (99.6%) | `polar_protic_acid` (0.2%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (100%) | `[H+].[OH-]` (0%) | `O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `Cc1ccc([P+](=O)c2c` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (97%) | `N#Cc1cc(C#N)c(-n2c` (2%) | `__ABSENT__` (0%) | set ✗ / any ✓ |

---

### Reaction #2172  yield=52.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #4)

```
C=C(C)c1ccccc1NC(=O)CCc1ccccc1>>CC1(CBr)OC(CCc2ccccc2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (97.1%) | `carbon` (2.8%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (86.1%) | `platinum_generic` (13.6%) | `graphite_rod` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.1%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.9%) | `platinum_generic` (8.1%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.3%) | `ABSENT` (3.4%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.1%) | `Na` (13.2%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (96.7%) | `BF4` (1.3%) | `Cl` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (28.3%) | `alkali_bicarbonate` (6.8%) | `carboxylic_acid` (2.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (98.0%) | `ABSENT` (1.7%) | `ionic_organocat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (58.1%) | `aromatic_hydrocarbon` (39.1%) | `polar_aprotic_sulfoxide` (0.9%) | ✗ |
| 溶剂 set | 79 | `CO` | `CC#N` (94%) | `O=C(O)C(F)(F)F` (70%) | `O` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (90%) | `O=C(O)C(F)(F)F` (7%) | `Cc1ccc([PH](=O)c2c` (2%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (82%) | `CC(C)c1cc(C(C)C)c(` (16%) | `__OTHER__` (1%) | set ✗ / any ✗ |

---

### Reaction #2173  yield=60.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #5)

```
C=C(C)c1ccccc1NC(=O)c1ccncc1>>CC1(CCl)OC(c2ccncc2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (98.8%) | `carbon` (1.2%) | `sacrificial_iron` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `platinum_plate` (95.6%) | `platinum_generic` (4.2%) | `carbon_rod` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (89.7%) | `platinum_generic` (10.3%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.8%) | `NEt4` (1.8%) | `Na` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `Cl` (97.4%) | `Br` (1.6%) | `I` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `phosphine_neutral` | `ABSENT` (27.3%) | `electrophilic_N_F` (2.0%) | `unparseable_text` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.9%) | `ABSENT` (0.0%) | `pyridine_organocat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `aromatic_hydrocarbon` (0.7%) | `polar_protic_acid` (0.2%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (99%) | `O=C(O)C(F)(F)F` (8%) | `CO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (98%) | `Cc1ccc([P+](=O)c2c` (6%) | `Cc1ccc([PH](=O)c2c` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `N#Cc1c(C#N)c(-n2c3` | `N#Cc1c(C#N)c(-n2c3` (99%) | `N#Cc1cc(C#N)c(-n2c` (1%) | `CC(C)c1cc(C(C)C)c(` (0%) | set ✓ / any ✓ |

---

### Reaction #2174  yield=60.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #6)

```
C=C(C)c1ccccc1NC(=O)c1ccc(F)cc1>>CC1(CBr)OC(c2ccc(F)cc2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.1%) | `carbon` (0.9%) | `sacrificial_iron` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_felt` | `platinum_plate` (90.2%) | `platinum_generic` (9.7%) | `graphite_rod` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `nickel` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.3%) | `platinum_generic` (8.7%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (49.8%) | `Na` (44.2%) | `K` (3.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (99.2%) | `Cl` (0.6%) | `I` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (19.7%) | `alkali_bicarbonate` (16.2%) | `primary_amine` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (98.0%) | `ABSENT` (1.7%) | `pyridine_organocat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (63.3%) | `aromatic_hydrocarbon` (34.2%) | `polar_aprotic_sulfoxide` (0.6%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (99%) | `O=C(O)C(F)(F)F` (21%) | `O` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (96%) | `Cc1ccc([P+](=O)c2c` (4%) | `Cc1ccc([PH](=O)c2c` (2%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `N#Cc1c(C#N)c(-n2c3` | `N#Cc1c(C#N)c(-n2c3` (91%) | `CC(C)c1cc(C(C)C)c(` (8%) | `N#Cc1cc(C#N)c(-n2c` (0%) | set ✓ / any ✓ |

---

### Reaction #2175  yield=60.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #7)

```
C=C(C)c1ccccc1NC(=O)c1ccc(F)cc1>>CC1(CCl)OC(c2ccc(F)cc2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.2%) | `carbon` (0.8%) | `sacrificial_iron` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_plate` (98.7%) | `platinum_generic` (1.2%) | `carbon_rod` (0.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.1%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.9%) | `platinum_generic` (1.1%) | `reticulated_vitreous_carbon` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.4%) | `NEt4` (11.4%) | `Na` (3.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `Cl` (98.6%) | `I` (0.6%) | `Br` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `phosphine_neutral` | `ABSENT` (34.6%) | `metal_oxide_oxidant` (1.8%) | `tellurium_reagent` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (98.5%) | `ABSENT` (1.2%) | `ionic_organocat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (99.3%) | `halogenated_aliphatic` (0.3%) | `polar_protic_acid` (0.3%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (100%) | `Cc1ccc([P+](=O)c2c` (1%) | `O=S(=O)(O)O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `N#Cc1c(C#N)c(-n2c3` | `N#Cc1c(C#N)c(-n2c3` (99%) | `N#Cc1cc(C#N)c(-n2c` (1%) | `CC(=O)O` (0%) | set ✓ / any ✓ |

---

### Reaction #2176  yield=60.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #8)

```
C=C(C)c1ccccc1NC(=O)c1ccccc1>>CC1(CCl)OC(c2ccccc2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (98.8%) | `carbon` (1.1%) | `sacrificial_zinc` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `platinum_generic` (95.3%) | `platinum_plate` (4.3%) | `graphite_rod` (0.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.7%) | `sacrificial_aluminum` (4.2%) | `stainless_steel` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (93.4%) | `platinum_plate` (6.5%) | `ABSENT` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.4%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (39.0%) | `Na` (37.4%) | `NBu4` (15.2%) | ✓ |
| 电解质 anion | 26 | `Cl` | `Cl` (97.3%) | `Br` (1.1%) | `I` (0.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `phosphine_neutral` | `ABSENT` (14.4%) | `alkali_bicarbonate` (6.2%) | `chloride_anion` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (97.9%) | `polycyclic_arene_cat` (1.2%) | `ABSENT` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (81.5%) | `aromatic_hydrocarbon` (11.7%) | `polar_protic_alcohol` (1.9%) | ✓ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `O=C(O)C(F)(F)F` (82%) | `CC#N` (66%) | `CO` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N#C[S-].[NH4+]` + `O=S(=O)(O)O` | `O=S(=O)(O)O` (68%) | `N#C[S-].[NH4+]` (47%) | `__ABSENT__` (47%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)c1cc(C(C)C)c(` | `CC(C)c1cc(C(C)C)c(` (53%) | `N#Cc1cc(C#N)c(-n2c` (36%) | `N#Cc1c(C#N)c(-n2c3` (10%) | set ✓ / any ✓ |

---

### Reaction #2177  yield=60.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #9)

```
C=C(C)c1ccccc1NC(=O)C1CCC1>>CC1(CBr)OC(C2CCC2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.3%) | `carbon` (0.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_felt` | `platinum_plate` (99.8%) | `platinum_generic` (0.2%) | `carbon_rod` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `carbon` (0.2%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.1%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.5%) | `NEt4` (2.7%) | `K` (2.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (86.2%) | `Cl` (12.4%) | `PF6` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (35.8%) | `alkali_bicarbonate` (4.8%) | `electrophilic_N_F` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.5%) | `ABSENT` (0.4%) | `ionic_organocat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (94.6%) | `aromatic_hydrocarbon` (4.5%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CO` | `CC#N` (100%) | `O` (1%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (100%) | `Cc1ccc([P+](=O)c2c` (0%) | `Cc1ccc([PH](=O)c2c` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (100%) | `CC(C)c1cc(C(C)C)c(` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #2178  yield=65.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #10)

```
C=C(C)c1ccccc1NC(=O)c1ccncc1>>CC1(CBr)OC(c2ccncc2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (98.9%) | `carbon` (1.1%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (80.4%) | `platinum_generic` (19.3%) | `graphite_rod` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (60.1%) | `platinum_generic` (39.9%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (53.1%) | `NBu4` (43.9%) | `K` (1.6%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (99.2%) | `Cl` (0.4%) | `PF6` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `alkali_bicarbonate` (38.2%) | `ABSENT` (11.6%) | `bromide_anion` (3.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.7%) | `ABSENT` (0.2%) | `pyridine_organocat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `aromatic_hydrocarbon` (92.0%) | `polar_aprotic_nitrile` (7.6%) | `polar_protic_alcohol` (0.1%) | ✓ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `O=C(O)C(F)(F)F` (85%) | `CO` (75%) | `Cc1ccccc1` (21%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `Cc1ccc([P+](=O)c2c` (51%) | `Cc1ccc([PH](=O)c2c` (36%) | `N#C[S-].[NH4+]` (30%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `N#Cc1c(C#N)c(-n2c3` | `N#Cc1c(C#N)c(-n2c3` (53%) | `CC(C)c1cc(C(C)C)c(` (46%) | `N#Cc1cc(C#N)c(-n2c` (0%) | set ✓ / any ✓ |

---

### Reaction #2179  yield=62.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #11)

```
C=C(C)c1ccccc1NC(=O)c1ccc(I)cc1>>CC1(CBr)OC(c2ccc(I)cc2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.4%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (91.4%) | `platinum_generic` (8.6%) | `graphite_felt` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (79.6%) | `platinum_generic` (20.4%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (62.7%) | `NBu4` (35.9%) | `K` (0.5%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (99.1%) | `Cl` (0.7%) | `carboxylate` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `alkali_bicarbonate` (33.8%) | `ABSENT` (17.8%) | `bromide_anion` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.1%) | `ABSENT` (0.8%) | `pyridine_organocat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `aromatic_hydrocarbon` (77.6%) | `polar_aprotic_nitrile` (21.3%) | `polar_protic_acid` (0.3%) | ✗ |
| 溶剂 set | 79 | `CO` | `O=C(O)C(F)(F)F` (63%) | `Cc1ccccc1` (45%) | `CC#N` (41%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `Cc1ccc([PH](=O)c2c` (45%) | `O=C([O-])O.[Na+]` (17%) | `__ABSENT__` (16%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (95%) | `CC(C)c1cc(C(C)C)c(` (5%) | `N#Cc1cc(C#N)c(-n2c` (0%) | set ✗ / any ✗ |

---

### Reaction #2180  yield=61.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #12)

```
C=C(C)c1ccccc1NC(=O)c1cccs1>>CC1(CCl)OC(c2cccs2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.5%) | `carbon` (0.5%) | `sacrificial_iron` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (53.8%) | `platinum_generic` (46.1%) | `carbon_rod` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.0%) | `nickel` (0.9%) | `sacrificial_aluminum` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (59.0%) | `platinum_plate` (41.0%) | `nickel_plate` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (45.7%) | `NBu4` (37.2%) | `NEt4` (15.6%) | ✓ |
| 电解质 anion | 26 | `Cl` | `Cl` (82.9%) | `Br` (15.6%) | `PF6` (0.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `phosphine_neutral` | `alkali_bicarbonate` (27.6%) | `ABSENT` (17.3%) | `metal_oxide_oxidant` (1.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.8%) | `ABSENT` (0.1%) | `ionic_organocat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `aromatic_hydrocarbon` (78.2%) | `polar_aprotic_nitrile` (15.5%) | `halogenated_aliphatic` (2.5%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (35%) | `Cc1ccccc1` (34%) | `CO` (24%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc([P+](=O)c2c` | `Cc1ccc([P+](=O)c2c` (50%) | `__ABSENT__` (33%) | `O=C([O-])O.[Na+]` (15%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `CC(C)c1cc(C(C)C)c(` | `N#Cc1c(C#N)c(-n2c3` (57%) | `CC(C)c1cc(C(C)C)c(` (35%) | `N#Cc1cc(C#N)c(-n2c` (7%) | set ✗ / any ✓ |

---

### Reaction #2181  yield=65.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #13)

```
C=C(C)c1ccccc1NC(=O)c1ccccc1OC>>COc1ccccc1C1=Nc2ccccc2C(C)(CBr)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (97.5%) | `carbon` (2.5%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_felt` | `platinum_plate` (98.1%) | `platinum_generic` (1.7%) | `graphite_rod` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.3%) | `platinum_generic` (1.7%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (80.5%) | `Na` (16.1%) | `K` (2.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (98.1%) | `Cl` (1.6%) | `BF4` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (17.7%) | `alkali_bicarbonate` (12.4%) | `electrophilic_N_F` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.2%) | `ABSENT` (0.8%) | `pyridine_organocat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `aromatic_hydrocarbon` (64.4%) | `polar_aprotic_nitrile` (34.7%) | `polar_aprotic_sulfoxide` (0.4%) | ✗ |
| 溶剂 set | 79 | `CO` | `O=C(O)C(F)(F)F` (82%) | `CC#N` (62%) | `CO` (19%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (76%) | `Cc1ccc([PH](=O)c2c` (18%) | `O=C(O)C(F)(F)F` (5%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (92%) | `CC(C)c1cc(C(C)C)c(` (8%) | `N#Cc1cc(C#N)c(-n2c` (0%) | set ✗ / any ✗ |

---

### Reaction #2182  yield=66.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #14)

```
C=C(C)c1ccccc1NC(=O)C(C)C>>CC(C)C1=Nc2ccccc2C(C)(CBr)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.9%) | `carbon` (0.1%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_felt` | `platinum_plate` (92.7%) | `platinum_generic` (7.3%) | `platinum_foil` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `stainless_steel` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (95.7%) | `platinum_generic` (4.3%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.6%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (80.5%) | `NBu4` (12.1%) | `H` (3.6%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (99.6%) | `Cl` (0.2%) | `PF6` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `alkali_bicarbonate` (48.2%) | `ABSENT` (6.7%) | `bromide_anion` (4.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.3%) | `ABSENT` (0.5%) | `Pt_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `aromatic_hydrocarbon` (83.3%) | `polar_aprotic_nitrile` (16.0%) | `polar_aprotic_sulfoxide` (0.3%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `Cc1ccccc1` (82%) | `O` (49%) | `O=C(O)C(F)(F)F` (20%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `O=C([O-])O.[Na+]` (44%) | `Cc1ccc([PH](=O)c2c` (33%) | `Cc1ccc([P+](=O)c2c` (25%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (71%) | `CC(C)c1cc(C(C)C)c(` (27%) | `__OTHER__` (1%) | set ✗ / any ✗ |

---

### Reaction #2183  yield=61.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #15)

```
C=C(C)c1ccccc1NC(=O)C(C)C>>CC(C)C1=Nc2ccccc2C(C)(CCl)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_felt` | `platinum_plate` (92.5%) | `platinum_generic` (7.5%) | `graphite_cloth` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.5%) | `stainless_steel` (0.3%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (82.9%) | `platinum_generic` (17.1%) | `reticulated_vitreous_carbon` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (71.6%) | `NBu4` (22.3%) | `Na` (3.4%) | ✓ |
| 电解质 anion | 26 | `Br` | `Cl` (99.6%) | `Br` (0.3%) | `I` (0.1%) | ✓ |
| 试剂大类 | 103 | `phosphine_neutral` | `ABSENT` (14.4%) | `alkali_bicarbonate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.4%) | `ABSENT` (0.3%) | `polycyclic_arene_cat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (97.9%) | `halogenated_aliphatic` (1.2%) | `polar_protic_acid` (0.4%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (100%) | `ClCCl` (3%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (99%) | `Cc1ccc([P+](=O)c2c` (1%) | `Cc1ccc([PH](=O)c2c` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (93%) | `N#Cc1cc(C#N)c(-n2c` (6%) | `CC(C)c1cc(C(C)C)c(` (1%) | set ✗ / any ✗ |

---

### Reaction #2184  yield=62.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #16)

```
C=C(C)c1ccccc1NC(=O)CCCCC>>CCCCCC1=Nc2ccccc2C(C)(CBr)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (85.0%) | `carbon` (14.9%) | `ABSENT` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (93.7%) | `graphite_rod` (4.6%) | `platinum_generic` (1.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.5%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.1%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (69.1%) | `Na` (24.3%) | `ABSENT` (2.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (99.4%) | `BF4` (0.2%) | `PF6` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (17.3%) | `alkali_bicarbonate` (7.3%) | `bromide_anion` (5.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (80.4%) | `ABSENT` (18.3%) | `pyridine_organocat` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (86.5%) | `aromatic_hydrocarbon` (9.5%) | `polar_aprotic_sulfoxide` (2.9%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (100%) | `O=C(O)C(F)(F)F` (20%) | `O` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (88%) | `O=C(O)C(F)(F)F` (7%) | `Cc1ccc([PH](=O)c2c` (4%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (59%) | `CC(C)c1cc(C(C)C)c(` (35%) | `__OTHER__` (4%) | set ✗ / any ✗ |

---

### Reaction #2185  yield=66.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #17)

```
C=C(C)c1ccccc1NC(=O)Cc1ccccc1>>CC1(CBr)OC(Cc2ccccc2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.9%) | `carbon` (0.1%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (95.1%) | `platinum_generic` (4.9%) | `graphite_rod` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (94.6%) | `platinum_generic` (5.4%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.7%) | `Na` (12.0%) | `NEt4` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (98.9%) | `Cl` (0.5%) | `BF4` (0.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (33.3%) | `alkali_bicarbonate` (8.4%) | `electrophilic_N_F` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (88.0%) | `ABSENT` (11.4%) | `pyridine_organocat` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (90.1%) | `aromatic_hydrocarbon` (9.0%) | `polar_protic_acid` (0.3%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (100%) | `O=C(O)C(F)(F)F` (3%) | `O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (99%) | `O=C(O)C(F)(F)F` (1%) | `Cc1ccc([PH](=O)c2c` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (98%) | `CC(C)c1cc(C(C)C)c(` (2%) | `N#Cc1cc(C#N)c(-n2c` (0%) | set ✗ / any ✗ |

---

### Reaction #2186  yield=63.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #18)

```
C=C(C)c1ccccc1NC(=O)C1CCCC1>>CC1(CBr)OC(C2CCCC2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.2%) | `carbon` (0.8%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.2%) | `graphite_rod` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `nickel` (0.1%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.4%) | `NEt4` (1.7%) | `K` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (96.4%) | `Cl` (2.7%) | `PF6` (0.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (33.0%) | `alkali_bicarbonate` (3.0%) | `electrophilic_N_F` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.5%) | `ABSENT` (0.3%) | `pyridine_organocat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (95.3%) | `aromatic_hydrocarbon` (3.7%) | `cyclic_ether` (0.3%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (100%) | `O` (1%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([PH](=O)c2c` | `__ABSENT__` (100%) | `Cc1ccc([P+](=O)c2c` (0%) | `Cc1ccc([PH](=O)c2c` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (99%) | `CC(C)c1cc(C(C)C)c(` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #2187  yield=63.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #19)

```
C=C(C)c1ccccc1NC(=O)c1ccccc1C>>Cc1ccccc1C1=Nc2ccccc2C(C)(CCl)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (98.6%) | `carbon` (1.4%) | `sacrificial_magnesium` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `platinum_plate` (99.1%) | `platinum_generic` (0.7%) | `carbon_rod` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (99.8%) | `nickel` (0.1%) | `carbon` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.8%) | `platinum_generic` (1.2%) | `carbon_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (89.4%) | `NEt4` (9.3%) | `Na` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `Cl` (99.4%) | `Br` (0.4%) | `BF4` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `as_solvent_aromatic_hydrocarbo` | `ABSENT` (21.3%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.7%) | `ABSENT` (0.2%) | `polycyclic_arene_cat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (99.7%) | `polar_protic_acid` (0.1%) | `aromatic_hydrocarbon` (0.1%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (100%) | `O=C(O)C(F)(F)F` (7%) | `ClCCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc([PH](=O)c2c` | `__ABSENT__` (95%) | `Cc1ccc([PH](=O)c2c` (5%) | `Cc1ccc([P+](=O)c2c` (4%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `N#Cc1c(C#N)c(-n2c3` | `N#Cc1c(C#N)c(-n2c3` (100%) | `N#Cc1cc(C#N)c(-n2c` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |

---

### Reaction #2188  yield=67.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #20)

```
C=C(C)c1ccccc1NC(=O)c1cccc(C)c1>>Cc1cccc(C2=Nc3ccccc3C(C)(CCl)O2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (98.9%) | `carbon` (1.1%) | `sacrificial_magnesium` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `carbon_rod` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.1%) | `platinum_generic` (0.9%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (55.6%) | `NBu4` (40.5%) | `Na` (1.5%) | ✓ |
| 电解质 anion | 26 | `Cl` | `Cl` (99.6%) | `I` (0.2%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `phosphine_neutral` | `ABSENT` (38.6%) | `metal_oxide_oxidant` (1.7%) | `tellurium_reagent` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.7%) | `ABSENT` (0.2%) | `pyridine_organocat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (99.8%) | `aromatic_hydrocarbon` (0.0%) | `polar_protic_acid` (0.0%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (100%) | `ClCCl` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([PH](=O)c2c` | `__ABSENT__` (100%) | `Cc1ccc([P+](=O)c2c` (2%) | `O=S(=O)(O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `N#Cc1c(C#N)c(-n2c3` | `N#Cc1c(C#N)c(-n2c3` (99%) | `N#Cc1cc(C#N)c(-n2c` (1%) | `CC(=O)O` (0%) | set ✓ / any ✓ |

---

### Reaction #2189  yield=66.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #21)

```
C=C(C)c1ccccc1NC(=O)c1cccc(C)c1>>Cc1cccc(C2=Nc3ccccc3C(C)(CBr)O2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.0%) | `carbon` (1.0%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `platinum_plate` (97.3%) | `platinum_generic` (2.6%) | `graphite_rod` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.9%) | `platinum_generic` (3.1%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (60.4%) | `NBu4` (26.7%) | `K` (5.3%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (97.2%) | `Cl` (1.7%) | `PF6` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `alkali_bicarbonate` (27.5%) | `ABSENT` (18.5%) | `bromide_anion` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.6%) | `ABSENT` (0.2%) | `pyridine_organocat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `aromatic_hydrocarbon` (57.5%) | `polar_aprotic_nitrile` (41.8%) | `polar_aprotic_sulfoxide` (0.3%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (44%) | `Cc1ccccc1` (40%) | `O=C(O)C(F)(F)F` (36%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([PH](=O)c2c` | `Cc1ccc([PH](=O)c2c` (46%) | `Cc1ccc([P+](=O)c2c` (46%) | `O=C(O)C(F)(F)F` (17%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `N#Cc1c(C#N)c(-n2c3` | `N#Cc1c(C#N)c(-n2c3` (82%) | `CC(C)c1cc(C(C)C)c(` (18%) | `N#Cc1cc(C#N)c(-n2c` (0%) | set ✓ / any ✓ |

---

### Reaction #2190  yield=63.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #22)

```
C=C(C)c1ccccc1NC(=O)c1cc(C)cc(C)c1>>Cc1cc(C)cc(C2=Nc3ccccc3C(C)(CCl)O2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.1%) | `carbon` (0.9%) | `sacrificial_iron` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (98.8%) | `platinum_generic` (1.1%) | `graphite_cloth` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.1%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (97.8%) | `platinum_generic` (2.2%) | `carbon_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (89.1%) | `NEt4` (8.7%) | `Na` (1.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `Cl` (98.7%) | `Br` (0.5%) | `carboxylate` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `as_solvent_aromatic_hydrocarbo` | `ABSENT` (39.9%) | `electrophilic_N_F` (1.8%) | `unparseable_text` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.7%) | `ABSENT` (0.2%) | `pyridine_organocat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (99.1%) | `halogenated_aliphatic` (0.3%) | `polar_protic_acid` (0.2%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (100%) | `ClCCCl` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([PH](=O)c2c` | `__ABSENT__` (100%) | `Cc1ccc([P+](=O)c2c` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (98%) | `N#Cc1cc(C#N)c(-n2c` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |

---

### Reaction #2191  yield=70.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #23)

```
C=C(C)c1ccccc1NC(=O)c1cc(C)cc(C)c1>>Cc1cc(C)cc(C2=Nc3ccccc3C(C)(CBr)O2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.3%) | `carbon` (0.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (96.6%) | `platinum_generic` (3.4%) | `platinum_foil` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.1%) | `platinum_generic` (3.8%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.9%) | `Na` (41.4%) | `H` (3.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (98.3%) | `Cl` (0.9%) | `carboxylate` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.0%) | `alkali_bicarbonate` (20.3%) | `bromide_anion` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.6%) | `ABSENT` (0.3%) | `pyridine_organocat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `aromatic_hydrocarbon` (66.4%) | `polar_aprotic_nitrile` (32.1%) | `polar_aprotic_sulfoxide` (0.5%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (56%) | `Cc1ccccc1` (35%) | `O=C(O)C(F)(F)F` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([PH](=O)c2c` | `__ABSENT__` (98%) | `Cc1ccc([PH](=O)c2c` (1%) | `Cc1ccc([P+](=O)c2c` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (82%) | `CC(C)c1cc(C(C)C)c(` (17%) | `N#Cc1cc(C#N)c(-n2c` (0%) | set ✗ / any ✗ |

---

### Reaction #2192  yield=70.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #24)

```
C=C(C)c1ccccc1NC(=O)c1ccc(Cl)cc1>>CC1(CBr)OC(c2ccc(Cl)cc2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (98.8%) | `carbon` (1.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `platinum_plate` (97.6%) | `platinum_generic` (2.3%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.5%) | `platinum_generic` (1.5%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (64.7%) | `Na` (30.7%) | `K` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (97.6%) | `Cl` (2.1%) | `carboxylate` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (24.1%) | `alkali_bicarbonate` (9.3%) | `alkali_other_salt` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (98.9%) | `ABSENT` (0.9%) | `pyridine_organocat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (77.9%) | `aromatic_hydrocarbon` (19.5%) | `polar_protic_acid` (0.8%) | ✗ |
| 溶剂 set | 79 | `CO` | `CC#N` (100%) | `O` (13%) | `O=C(O)C(F)(F)F` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (98%) | `Cc1ccc([PH](=O)c2c` (2%) | `Cc1ccc([P+](=O)c2c` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `N#Cc1c(C#N)c(-n2c3` | `N#Cc1c(C#N)c(-n2c3` (93%) | `CC(C)c1cc(C(C)C)c(` (6%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2193  yield=75.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #25)

```
C=C(C)c1ccccc1NC(=O)c1ccc(C)cc1>>Cc1ccc(C2=Nc3ccccc3C(C)(CCl)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.3%) | `carbon` (0.6%) | `sacrificial_zinc` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `platinum_plate` (91.8%) | `platinum_generic` (8.0%) | `carbon_rod` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.1%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (93.5%) | `platinum_generic` (6.5%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (87.7%) | `NEt4` (6.5%) | `Na` (1.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `Cl` (98.0%) | `Br` (1.5%) | `BF4` (0.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `as_solvent_aromatic_hydrocarbo` | `ABSENT` (26.5%) | `chloride_anion` (2.4%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (98.4%) | `ABSENT` (1.2%) | `ionic_organocat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.5%) | `polar_protic_acid` (0.5%) | `halogenated_aliphatic` (0.4%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (100%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (100%) | `Cc1ccc([P+](=O)c2c` (1%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `N#Cc1c(C#N)c(-n2c3` | `N#Cc1c(C#N)c(-n2c3` (99%) | `N#Cc1cc(C#N)c(-n2c` (0%) | `CC(C)c1cc(C(C)C)c(` (0%) | set ✓ / any ✓ |

---

### Reaction #2194  yield=71.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #26)

```
C=C(C)c1ccccc1NC(=O)c1cccs1.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>CC1(CBr)OC(c2cccs2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_felt` | `platinum_plate` (99.0%) | `platinum_generic` (1.0%) | `graphite_felt` (0.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.1%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (97.3%) | `platinum_generic` (2.7%) | `carbon_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (92.6%) | `Na` (5.8%) | `NEt4` (1.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Cl` (79.8%) | `Br` (19.7%) | `PF6` (0.4%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (30.3%) | `alkali_bicarbonate` (19.9%) | `electrophilic_N_F` (1.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (100.0%) | `ABSENT` (0.0%) | `pyridine_organocat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `aromatic_hydrocarbon` (78.1%) | `polar_aprotic_nitrile` (21.2%) | `polar_protic_acid` (0.2%) | ✗ |
| 溶剂 set | 79 | `CO` | `CC#N` (90%) | `Cc1ccccc1` (8%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (100%) | `Cc1ccc([P+](=O)c2c` (1%) | `Cc1ccc([PH](=O)c2c` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (100%) | `__OTHER__` (0%) | `CC(C)c1cc(C(C)C)c(` (0%) | set ✗ / any ✗ |

---

### Reaction #2195  yield=76.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #27)

```
C=C(C)c1ccccc1NC(=O)c1ccc2ccccc2c1.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>CC1(CBr)OC(c2ccc3ccccc3c2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.8%) | `carbon` (0.2%) | `sacrificial_magnesium` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_felt` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `carbon_rod` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.3%) | `sacrificial_aluminum` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.1%) | `NEt4` (0.7%) | `Na` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Cl` (98.8%) | `Br` (1.1%) | `PF6` (0.0%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (43.1%) | `electrophilic_N_F` (1.7%) | `unparseable_text` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.9%) | `ABSENT` (0.1%) | `polycyclic_arene_cat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (99.0%) | `aromatic_hydrocarbon` (0.8%) | `polar_protic_acid` (0.1%) | ✗ |
| 溶剂 set | 79 | `CO` | `CC#N` (100%) | `[H+].[OH-]` (0%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (100%) | `Cc1ccc([P+](=O)c2c` (0%) | `Cc1ccc([PH](=O)c2c` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (100%) | `CC(=O)O` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #2196  yield=71.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #28)

```
C=C(C)c1ccccc1NC(=O)c1ccc(C(F)(F)F)cc1>>CC1(CBr)OC(c2ccc(C(F)(F)F)cc2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.0%) | `carbon` (1.0%) | `sacrificial_iron` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (84.8%) | `platinum_generic` (14.9%) | `graphite_rod` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.5%) | `nickel` (0.4%) | `copper` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `graphite_plate` | `platinum_plate` (72.6%) | `platinum_generic` (27.3%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.2%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.2%) | `Na` (16.8%) | `NEt4` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (99.1%) | `Cl` (0.7%) | `PF6` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `alkali_bicarbonate` (26.0%) | `ABSENT` (13.9%) | `bromide_anion` (5.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (97.8%) | `ABSENT` (1.8%) | `pyridine_organocat` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (48.6%) | `aromatic_hydrocarbon` (48.3%) | `polar_aprotic_sulfoxide` (1.0%) | ✗ |
| 溶剂 set | 79 | `CO` | `CC#N` (97%) | `O=C(O)C(F)(F)F` (33%) | `O` (11%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([PH](=O)c2c` | `Cc1ccc([PH](=O)c2c` (35%) | `Cc1ccc([P+](=O)c2c` (29%) | `O=C(O)C(F)(F)F` (25%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (84%) | `CC(C)c1cc(C(C)C)c(` (15%) | `N#Cc1cc(C#N)c(-n2c` (0%) | set ✗ / any ✗ |

---

### Reaction #2197  yield=81.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #29)

```
C=C(C)c1ccccc1NC(C)=O>>CC1=Nc2ccccc2C(C)(CBr)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (90.7%) | `carbon` (9.3%) | `sacrificial_iron` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (69.0%) | `platinum_generic` (21.0%) | `graphite_rod` (8.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.0%) | `platinum_generic` (27.0%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.3%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (69.1%) | `NBu4` (25.7%) | `ABSENT` (2.2%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (99.7%) | `Cl` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (13.8%) | `bromide_anion` (5.1%) | `carboxylic_acid` (4.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (67.9%) | `ABSENT` (31.3%) | `Pt_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (79.8%) | `aromatic_hydrocarbon` (14.4%) | `polar_protic_acid` (4.5%) | ✗ |
| 溶剂 set | 79 | `CO` | `CC#N` (96%) | `O=C(O)C(F)(F)F` (94%) | `CO` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (82%) | `O=C(O)C(F)(F)F` (14%) | `Cc1ccc([PH](=O)c2c` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (63%) | `CC(C)c1cc(C(C)C)c(` (34%) | `N#Cc1cc(C#N)c(-n2c` (1%) | set ✗ / any ✗ |

---

### Reaction #2198  yield=83.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #30)

```
C=C(C)c1ccccc1NC(=O)c1ccc(C)cc1>>Cc1ccc(C2=Nc3ccccc3C(C)(CBr)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.2%) | `carbon` (0.8%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `platinum_plate` (75.7%) | `platinum_generic` (23.9%) | `graphite_rod` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.1%) | `copper` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (75.1%) | `platinum_generic` (24.9%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.2%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (68.5%) | `NBu4` (24.6%) | `K` (2.9%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (99.5%) | `Cl` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `alkali_bicarbonate` (25.3%) | `ABSENT` (11.8%) | `bromide_anion` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (97.2%) | `ABSENT` (2.2%) | `Pt_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `aromatic_hydrocarbon` (77.1%) | `polar_aprotic_nitrile` (19.8%) | `polar_aprotic_sulfoxide` (1.2%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `Cc1ccccc1` (45%) | `CO` (42%) | `O=C(O)C(F)(F)F` (42%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `Cc1ccc([P+](=O)c2c` (46%) | `Cc1ccc([PH](=O)c2c` (37%) | `O=C(O)C(F)(F)F` (32%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `N#Cc1c(C#N)c(-n2c3` | `N#Cc1c(C#N)c(-n2c3` (82%) | `CC(C)c1cc(C(C)C)c(` (17%) | `N#Cc1cc(C#N)c(-n2c` (0%) | set ✓ / any ✓ |

---

### Reaction #2199  yield=81.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #31)

```
C=C(C)c1ccccc1NC(=O)c1ccc(C#N)cc1>>CC1(CBr)OC(c2ccc(C#N)cc2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.3%) | `carbon` (0.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (97.3%) | `platinum_generic` (2.6%) | `graphite_rod` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (95.6%) | `platinum_generic` (4.3%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.1%) | `Na` (39.3%) | `ABSENT` (3.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (98.0%) | `Cl` (1.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `alkali_bicarbonate` (19.1%) | `ABSENT` (17.0%) | `bromide_anion` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (99.4%) | `ABSENT` (0.4%) | `pyridine_organocat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (69.5%) | `aromatic_hydrocarbon` (29.3%) | `polar_aprotic_sulfoxide` (0.4%) | ✗ |
| 溶剂 set | 79 | `CO` | `CC#N` (98%) | `O=C(O)C(F)(F)F` (11%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `Cc1ccc([P+](=O)c2c` | `Cc1ccc([PH](=O)c2c` (49%) | `Cc1ccc([P+](=O)c2c` (34%) | `O=C(O)C(F)(F)F` (23%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `N#Cc1c(C#N)c(-n2c3` | `N#Cc1c(C#N)c(-n2c3` (96%) | `CC(C)c1cc(C(C)C)c(` (4%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2200  yield=81.0%

**Source paper**: [`Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json`](reactions_by_journal_alkene_ec_audited/Journal/2025_Journal_of_Heterocyclic_Chemistry_2025_62_9_899-905.json) (反应 idx 在该 JSON 内 = #32)

```
C=C(C)c1ccccc1NC(=O)c1ccc2ccccc2c1>>CC1(CCl)OC(c2ccc3ccccc3c2)=Nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (98.8%) | `carbon` (1.2%) | `sacrificial_magnesium` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.6%) | `carbon_rod` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.8%) | `platinum_generic` (1.1%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (64.9%) | `NEt4` (33.8%) | `Na` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Cl` (99.0%) | `Br` (0.4%) | `I` (0.4%) | ✓ |
| 试剂大类 | 103 | `phosphine_neutral` | `ABSENT` (31.5%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (98.7%) | `ABSENT` (1.2%) | `ionic_organocat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `polar_protic_acid` (0.6%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CO` + `O=C(O)C(F)(F)F` | `CC#N` (100%) | `O` (0%) | `[H+].[OH-]` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `Cc1ccc([P+](=O)c2c` | `__ABSENT__` (100%) | `Cc1ccc([P+](=O)c2c` (1%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `N#Cc1c(C#N)c(-n2c3` (96%) | `N#Cc1cc(C#N)c(-n2c` (2%) | `CC(C)c1cc(C(C)C)c(` (0%) | set ✗ / any ✗ |

---

### Reaction #2201  yield=33.0%

**Source paper**: [`GreenChem/2022_Green_Chemistry_2022_24_17_6556-6561.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2022_Green_Chemistry_2022_24_17_6556-6561.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1.N#C[S-].[NH4+]>>N#CSCC(SC#N)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (80.4%) | `platinum` (19.0%) | `nickel` (0.3%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `carbon_generic` (45.8%) | `carbon_rod` (23.8%) | `platinum_generic` (12.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (67.5%) | `carbon` (31.5%) | `ABSENT` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `graphite_plate` | `carbon_generic` (72.4%) | `platinum_plate` (15.9%) | `platinum_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.3%) | `ABSENT` (1.7%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NH4` | `ABSENT` (74.4%) | `Li` (12.3%) | `NBu4` (9.6%) | ✗ |
| 电解质 anion | 26 | `SCN` | `ABSENT` (74.3%) | `PF6` (8.1%) | `BF4` (7.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (24.8%) | `ABSENT` (5.9%) | `sulfonic_acid` (3.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `organic_neutral_cat` (0.4%) | `polycyclic_arene_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.6%) | `polar_protic_alcohol` (1.4%) | `polar_aprotic_sulfoxide` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `CC#N` | `CC#N` (100%) | `O` (0%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (43%) | `O=CO` (15%) | `O=C(O)C(F)(F)F` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `N#Cc1c(C#N)c(-n2c3` (0%) | set ✓ / any ✓ |

---

### Reaction #2202  yield=34.0%

**Source paper**: [`NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json`](reactions_by_journal_alkene_ec_audited/NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CC2C=CC1C2.O=C(Nc1cccc2cccnc12)c1ccccc1>>O=C1c2ccccc2[C@H]2[C@H]([C@@H]3C=C[C@H]2C3)N1c1cccc2cccnc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `unknown_electrode` (45.7%) | `reticulated_vitreous_carbon` (28.6%) | `graphite_rod` (10.0%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.2%) | `nickel` (1.1%) | `carbon` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_generic` (54.7%) | `platinum_plate` (43.0%) | `nickel_plate` (1.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `imidazolium` | `Na` (76.5%) | `NEt4` (17.8%) | `NBu4` (2.1%) | ✗ |
| 电解质 anion | 26 | `PF6` | `carboxylate` (56.9%) | `molecular_no_ion` (23.8%) | `BF4` (10.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (18.5%) | `alkali_carboxylate` (8.7%) | `metal_oxide_oxidant` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (99.9%) | `ABSENT` (0.0%) | `Cu_complex` (0.0%) | ✗ |
| 溶剂大类 | 27 | `cyclic_ether` | `tfe` (97.3%) | `polar_protic_alcohol` (2.1%) | `polar_aprotic_nitrile` (0.5%) | ✗ |
| 溶剂 set | 79 | `C1COCCO1` + `CC(=O)N(C)C` | `OCC(F)(F)F` (100%) | `ClCCCl` (95%) | `CC#N` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (96%) | `CC(C)(C)C(=O)[O-].` (4%) | `CC(C)(C)C(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `CC(=O)[O-].CC(=O)[` | `CC(C)(C)c1cccc(C2=` (76%) | `CC(=O)[O-].CC(=O)[` (23%) | `CC1[CH-]C(C)=[O]->` (7%) | set ✗ / any ✗ |

---

### Reaction #2203  yield=50.0%

**Source paper**: [`NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json`](reactions_by_journal_alkene_ec_audited/NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json) (反应 idx 在该 JSON 内 = #1)

```
O=C(Nc1cccc2cccnc12)c1ccccc1.O=C(OCc1ccccc1)N1C2C=CC1c1ccccc12>>O=C1c2ccccc2[C@H]2[C@H]([C@@H]3c4ccccc4[C@H]2N3C(=O)O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `reticulated_vitreous_carbon` (58.8%) | `unknown_electrode` (17.0%) | `graphite_felt` (10.1%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.0%) | `nickel` (1.6%) | `carbon` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.4%) | `platinum_generic` (1.2%) | `nickel_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `divided` (0.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `imidazolium` | `NBu4` (74.4%) | `Na` (21.6%) | `molecular_no_ion` (1.7%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (55.6%) | `carboxylate` (19.5%) | `molecular_no_ion` (11.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.7%) | `carboxylic_acid` (6.1%) | `alkali_carboxylate` (4.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (97.2%) | `ABSENT` (2.4%) | `ionic_organocat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `cyclic_ether` | `tfe` (79.8%) | `polar_protic_alcohol` (19.6%) | `polar_aprotic_nitrile` (0.2%) | ✗ |
| 溶剂 set | 79 | `C1COCCO1` + `CC(=O)N(C)C` | `OCC(F)(F)F` (100%) | `CO` (52%) | `ClCCCl` (12%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `CC(C)(C)C(=O)[O-].` (6%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `CC(=O)[O-].CC(=O)[` + `__OTHER__` | `CC(C)(C)c1cccc(C2=` (42%) | `CC(=O)[CH-]C(C)=O.` (30%) | `CC(=O)[O-].CC(=O)[` (12%) | set ✗ / any ✗ |

---

### Reaction #2204  yield=50.0%

**Source paper**: [`NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json`](reactions_by_journal_alkene_ec_audited/NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json) (反应 idx 在该 JSON 内 = #2)

```
Brc1cc2c(cc1Br)C1C=CC2O1.O=C(Nc1cccc2cccnc12)c1cccs1>>O=C1c2sccc2[C@H]2[C@H]([C@H]3O[C@@H]2c2cc(Br)c(Br)cc23)N1c1cccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (97.5%) | `graphite_felt` (1.1%) | `unknown_electrode` (0.8%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.2%) | `nickel` (0.7%) | `stainless_steel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (54.0%) | `platinum_generic` (26.3%) | `platinum_wire` (19.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `imidazolium` | `NBu4` (56.8%) | `NEt4` (37.8%) | `Li` (4.2%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (47.3%) | `PF6` (22.9%) | `ClO4` (22.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (18.3%) | `carboxylic_acid` (2.6%) | `water` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (54.1%) | `Co_complex` (18.5%) | `ABSENT` (15.4%) | ✗ |
| 溶剂大类 | 27 | `cyclic_ether` | `tfe` (95.7%) | `ketone` (1.2%) | `ABSENT` (1.1%) | ✗ |
| 溶剂 set | 79 | `C1COCCO1` + `CC(=O)N(C)C` | `OCC(F)(F)F` (99%) | `CC(C)=O` (0%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `CC(C)(C)c1cccc(C2=` (18%) | `__ABSENT__` (18%) | `__OTHER__` (8%) | set ✗ / any ✓ |

---

### Reaction #2205  yield=45.0%

**Source paper**: [`NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json`](reactions_by_journal_alkene_ec_audited/NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json) (反应 idx 在该 JSON 内 = #3)

```
CC(C)(C)OC(=O)N1C2C=CC1c1ccccc12.O=C(Nc1cccc2cccnc12)c1ccccc1>>CC(C)(C)OC(=O)N1[C@@H]2c3ccccc3[C@H]1[C@H]1[C@@H]2c2cc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `reticulated_vitreous_carbon` (46.1%) | `unknown_electrode` (15.0%) | `graphite_felt` (11.4%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (84.2%) | `nickel` (15.0%) | `carbon` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (85.2%) | `platinum_generic` (7.7%) | `nickel_plate` (4.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `divided` (0.7%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (55.9%) | `NBu4` (35.1%) | `molecular_no_ion` (4.7%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (37.2%) | `molecular_no_ion` (36.3%) | `carboxylate` (13.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (9.2%) | `ABSENT` (5.7%) | `sulfonic_acid` (3.7%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (99.0%) | `ABSENT` (0.6%) | `Cu_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `cyclic_ether` | `tfe` (79.1%) | `polar_protic_alcohol` (19.2%) | `polar_aprotic_nitrile` (0.6%) | ✗ |
| 溶剂 set | 79 | `C1COCCO1` + `CC(=O)N(C)C` | `OCC(F)(F)F` (100%) | `CO` (43%) | `ClCCCl` (18%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `CC(C)(C)C(=O)[O-].` (85%) | `CC(C)(C)C(=O)O` (3%) | `CC(C)(C)C(=O)O.[Na` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `CC(=O)[O-].CC(=O)[` + `__OTHER__` | `CC(C)(C)c1cccc(C2=` (32%) | `CC(=O)[CH-]C(C)=O.` (26%) | `CC(=O)[O-].CC(=O)[` (9%) | set ✗ / any ✗ |

---

### Reaction #2206  yield=56.0%

**Source paper**: [`NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json`](reactions_by_journal_alkene_ec_audited/NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json) (反应 idx 在该 JSON 内 = #4)

```
O=C(Nc1cccc2cccnc12)c1ccccc1.O=C(OCc1ccccc1)N1C2C=CC1c1ccccc12>>O=C1c2ccccc2[C@H]2[C@@H]1[C@@H]1c3ccccc3[C@H]2N1C(=O)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.2%) | `platinum` (3.8%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_felt` (17.8%) | `graphite_plate` (17.7%) | `zinc_plate` (17.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (62.4%) | `platinum_generic` (35.6%) | `nickel_plate` (0.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (94.1%) | `divided` (5.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NBu4` (54.7%) | `Na` (36.3%) | `Li` (3.2%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (25.8%) | `Cl` (20.8%) | `PF6` (16.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.2%) | `carboxylic_acid` (9.6%) | `as_solvent_cyclic_ether` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `Co_complex` (75.7%) | `ABSENT` (24.0%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `tfe` (62.1%) | `polar_protic_alcohol` (28.5%) | `polar_aprotic_nitrile` (6.2%) | ✗ |
| 溶剂 set | 79 | `C1COCCO1` + `CC(=O)N(C)C` | `OCC(F)(F)F` (98%) | `CO` (27%) | `ClCCCl` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(C)(C)C(=O)[O-].` (0%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `CC(=O)[O-].CC(=O)[` + `__OTHER__` | `__ABSENT__` (40%) | `CC(C)(C)c1cccc(C2=` (26%) | `CC(=O)[CH-]C(C)=O.` (15%) | set ✗ / any ✗ |

---

### Reaction #2207  yield=52.0%

**Source paper**: [`NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json`](reactions_by_journal_alkene_ec_audited/NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json) (反应 idx 在该 JSON 内 = #5)

```
O=C(Nc1cccc2cccnc12)c1ccccc1.Fc1cc2c(cc1F)C1C=CC2O1>>O=C1c2ccccc2[C@H]2[C@H]([C@H]3O[C@@H]2c2cc(F)c(F)cc23)N1c1cccc2c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_rod` (62.7%) | `reticulated_vitreous_carbon` (15.3%) | `graphite_rod` (15.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (96.3%) | `nickel` (3.6%) | `stainless_steel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (76.2%) | `nickel_plate` (16.7%) | `platinum_wire` (3.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `imidazolium` | `NBu4` (82.2%) | `Na` (7.9%) | `NEt4` (5.1%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (92.1%) | `carboxylate` (5.3%) | `Br` (0.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `water` (8.4%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (95.9%) | `ABSENT` (3.1%) | `ionic_organocat` (0.7%) | ✗ |
| 溶剂大类 | 27 | `cyclic_ether` | `tfe` (61.6%) | `polar_protic_alcohol` (22.7%) | `polar_aprotic_nitrile` (13.0%) | ✗ |
| 溶剂 set | 79 | `C1COCCO1` + `CC(=O)N(C)C` | `OCC(F)(F)F` (100%) | `CC#N` (30%) | `CO` (24%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(C)(C)C(=O)[O-].` (1%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `CC(=O)[O-].CC(=O)[` + `__OTHER__` | `__ABSENT__` (33%) | `CC1[CH-]C(C)=[O]->` (12%) | `[Fe+2].c1cc[cH-]c1` (12%) | set ✗ / any ✓ |

---

### Reaction #2208  yield=52.0%

**Source paper**: [`NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json`](reactions_by_journal_alkene_ec_audited/NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json) (反应 idx 在该 JSON 内 = #6)

```
O=C(Nc1cccc2cccnc12)c1ccccc1.Brc1cc2c(cc1Br)C1C=CC2O1>>O=C1c2ccccc2[C@H]2[C@H]([C@H]3O[C@@H]2c2cc(Br)c(Br)cc23)N1c1cc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (28.8%) | `graphite_felt` (23.5%) | `graphite_rod` (15.9%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (93.4%) | `nickel` (6.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (30.1%) | `platinum_wire` (29.9%) | `nickel_plate` (25.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `divided` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `imidazolium` | `NBu4` (95.9%) | `Na` (1.6%) | `Li` (1.2%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (96.1%) | `carboxylate` (1.5%) | `Br` (1.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.6%) | `water` (2.6%) | `metal_oxide_oxidant` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (94.6%) | `ABSENT` (4.3%) | `ionic_organocat` (0.5%) | ✗ |
| 溶剂大类 | 27 | `cyclic_ether` | `tfe` (58.2%) | `polar_protic_alcohol` (33.2%) | `polar_aprotic_nitrile` (5.0%) | ✗ |
| 溶剂 set | 79 | `C1COCCO1` + `CC(=O)N(C)C` | `OCC(F)(F)F` (99%) | `CO` (18%) | `CC#N` (14%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(C)(C)C(=O)[O-].` (1%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `CC(=O)[O-].CC(=O)[` + `__OTHER__` | `__ABSENT__` (40%) | `CC(=O)[CH-]C(C)=O.` (21%) | `CC1[CH-]C(C)=[O]->` (19%) | set ✗ / any ✗ |

---

### Reaction #2209  yield=60.0%

**Source paper**: [`NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json`](reactions_by_journal_alkene_ec_audited/NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json) (反应 idx 在该 JSON 内 = #7)

```
O=C(Nc1cccc2cccnc12)c1ccccc1.Fc1cc2c(cc1F)C1C=CC2O1>>O=C1c2ccccc2[C@H]2[C@@H]1[C@H]1O[C@@H]2c2cc(F)c(F)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.3%) | `platinum` (2.6%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (25.1%) | `carbon_rod` (20.6%) | `unknown_electrode` (19.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (71.5%) | `platinum_plate` (20.8%) | `platinum_wire` (6.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `divided` (10.0%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (36.0%) | `Na` (26.1%) | `NBu4` (24.1%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `BF4` (38.3%) | `Cl` (33.0%) | `Br` (9.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.1%) | `water` (2.8%) | `thiol` (2.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `Co_complex` (96.7%) | `ABSENT` (2.1%) | `organic_neutral_cat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `tfe` (50.0%) | `polar_aprotic_nitrile` (39.7%) | `polar_protic_alcohol` (6.5%) | ✗ |
| 溶剂 set | 79 | `C1COCCO1` + `CC(=O)N(C)C` | `OCC(F)(F)F` (95%) | `CC#N` (9%) | `CO` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(C)(C)C(=O)[O-].` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `CC(=O)[O-].CC(=O)[` + `__OTHER__` | `__ABSENT__` (58%) | `CC1[CH-]C(C)=[O]->` (12%) | `CC(=O)[CH-]C(C)=O.` (8%) | set ✗ / any ✗ |

---

### Reaction #2210  yield=61.0%

**Source paper**: [`NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json`](reactions_by_journal_alkene_ec_audited/NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json) (反应 idx 在该 JSON 内 = #8)

```
C1=CC2C=CC1C2.O=C(Nc1cccc2cccnc12)c1ccccc1>>O=C1c2ccccc2[C@H]2[C@@H]1[C@@H]1C=C[C@H]2C1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.6%) | `platinum` (5.6%) | `sacrificial_zinc` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `unknown_electrode` (58.0%) | `graphite_generic` (17.6%) | `platinum_generic` (6.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.6%) | `carbon` (7.2%) | `nickel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.8%) | `nickel_plate` (1.6%) | `reticulated_vitreous_carbon` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (97.6%) | `ABSENT` (2.1%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `ABSENT` (54.3%) | `Na` (22.8%) | `NEt4` (8.8%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `ABSENT` (59.1%) | `Cl` (26.5%) | `molecular_no_ion` (5.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.4%) | `thiol` (3.4%) | `as_solvent_polar_protic_alcoho` (2.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `Co_complex` (99.8%) | `ABSENT` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `tfe` (56.0%) | `polar_aprotic_nitrile` (29.5%) | `polar_protic_alcohol` (11.6%) | ✗ |
| 溶剂 set | 79 | `C1COCCO1` + `CC(=O)N(C)C` | `OCC(F)(F)F` (96%) | `ClCCCl` (37%) | `CO` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(C)(C)C(=O)[O-].` (0%) | `CC(C)(C)C(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `CC(=O)[O-].CC(=O)[` | `CC1[CH-]C(C)=[O]->` (38%) | `__ABSENT__` (24%) | `CC(C)(C)c1cccc(C2=` (16%) | set ✗ / any ✗ |

---

### Reaction #2211  yield=76.0%

**Source paper**: [`NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json`](reactions_by_journal_alkene_ec_audited/NatCatal/2025_Nature_Catalysis_2025_8_3_257-269.json) (反应 idx 在该 JSON 内 = #9)

```
Cc1cc2c(cc1C)C1C=CC2O1.O=C(Nc1cccc2cccnc12)c1ccccc1>>Cc1cc2c(cc1C)[C@@H]1O[C@H]2[C@H]2c3ccccc3C(=O)N(c3cccc4cccnc34)[…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `reticulated_vitreous_carbon` (51.2%) | `graphite_rod` (16.3%) | `carbon_rod` (14.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (91.9%) | `nickel` (8.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_plate` (38.2%) | `platinum_plate` (35.1%) | `platinum_wire` (13.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.8%) | `divided` (3.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (53.1%) | `Na` (39.1%) | `NEt4` (3.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (72.3%) | `carboxylate` (16.9%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.0%) | `water` (5.3%) | `carboxylic_acid` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (98.1%) | `ABSENT` (1.3%) | `ionic_organocat` (0.3%) | ✗ |
| 溶剂大类 | 27 | `cyclic_ether` | `tfe` (71.7%) | `polar_protic_alcohol` (21.2%) | `polar_aprotic_nitrile` (5.2%) | ✗ |
| 溶剂 set | 79 | `C1COCCO1` + `CC(=O)N(C)C` | `OCC(F)(F)F` (100%) | `CO` (36%) | `CC#N` (11%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(C)(C)C(=O)[O-].` (1%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (32%) | `CC1[CH-]C(C)=[O]->` (20%) | `CC(C)(C)c1cccc(C2=` (20%) | set ✗ / any ✗ |

---

### Reaction #2212  yield=0.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `borate_other` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `phosphine_organocat` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2213  yield=76.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `borate_other` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `phosphine_organocat` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2214  yield=56.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `borate_other` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `phosphine_organocat` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2215  yield=73.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `borate_other` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `phosphine_organocat` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2216  yield=0.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2217  yield=73.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `nickel` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_zinc` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `borate_other` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2218  yield=0.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `borate_other` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2219  yield=76.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `nickel` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_zinc` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `borate_other` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2220  yield=0.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `borate_other` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2221  yield=0.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `borate_other` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2222  yield=0.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2223  yield=0.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `borate_other` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2224  yield=0.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `borate_other` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2225  yield=56.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `borate_other` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2226  yield=0.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `borate_other` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2227  yield=0.0%

**Source paper**: [`NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/NatCommun/10.1038_s41467-026-68437-w_si1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)c1ccccc1-c1c(C=O)cccc1C=O.C=CCN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(C(=O)c3cccc(C=O)c3-c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `nickel` | `carbon` (63.5%) | `platinum` (34.1%) | `sacrificial_magnesium` (1.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `graphite_generic` (82.5%) | `reticulated_vitreous_carbon` (5.1%) | `graphite_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_zinc` | `carbon` (64.0%) | `platinum` (30.0%) | `nickel` (5.8%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (60.2%) | `graphite_felt` (12.4%) | `nickel_foam` (12.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `Li` (99.3%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `borate_other` | `ClO4` (99.6%) | `molecular_no_ion` (0.3%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `primary_amine` (2.3%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.9%) | `triarylamine_radical_cat` (0.3%) | `aryl_iodide_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.0%) | `ABSENT` (23.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `O` (7%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cl` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `C[C@H](C[C@H](C)P(` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #2228  yield=41.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CC(=NO)c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>FC(F)(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (97.1%) | `graphite_generic` (1.3%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (92.8%) | `nickel` (5.1%) | `platinum` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (80.8%) | `graphite_plate` (6.5%) | `graphite_generic` (4.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (93.1%) | `NBu4` (2.5%) | `ABSENT` (2.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (96.7%) | `PF6` (1.1%) | `molecular_no_ion` (1.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.2%) | `alkali_carbonate` (7.0%) | `alkali_sulfonate` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `aqueous` (0.9%) | `polar_protic_alcohol` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (100%) | `CC#N` (92%) | `CS(C)=O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `CC(=O)[O-].[Na+]` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2229  yield=31.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CC(=NO)c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>FC(F)(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (97.1%) | `graphite_generic` (1.3%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (92.8%) | `nickel` (5.1%) | `platinum` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (80.8%) | `graphite_plate` (6.5%) | `graphite_generic` (4.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (93.1%) | `NBu4` (2.5%) | `ABSENT` (2.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (96.7%) | `PF6` (1.1%) | `molecular_no_ion` (1.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.2%) | `alkali_carbonate` (7.0%) | `alkali_sulfonate` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `aqueous` (0.9%) | `polar_protic_alcohol` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (100%) | `CC#N` (92%) | `CS(C)=O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `CC(=O)[O-].[Na+]` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2230  yield=47.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CC(=NO)c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>FC(F)(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (97.1%) | `graphite_generic` (1.3%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (92.8%) | `nickel` (5.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (80.8%) | `graphite_plate` (6.5%) | `graphite_generic` (4.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `Li` (93.1%) | `NBu4` (2.5%) | `ABSENT` (2.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (96.7%) | `PF6` (1.1%) | `molecular_no_ion` (1.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.2%) | `alkali_carbonate` (7.0%) | `alkali_sulfonate` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `aqueous` (0.9%) | `polar_protic_alcohol` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (100%) | `CC#N` (92%) | `CS(C)=O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `CC(=O)[O-].[Na+]` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2231  yield=32.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CC(=NO)c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>FC(F)(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (97.1%) | `graphite_generic` (1.3%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (92.8%) | `nickel` (5.1%) | `platinum` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (80.8%) | `graphite_plate` (6.5%) | `graphite_generic` (4.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `Li` (93.1%) | `NBu4` (2.5%) | `ABSENT` (2.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (96.7%) | `PF6` (1.1%) | `molecular_no_ion` (1.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.2%) | `alkali_carbonate` (7.0%) | `alkali_sulfonate` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `aqueous` (0.9%) | `polar_protic_alcohol` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (100%) | `CC#N` (92%) | `CS(C)=O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `CC(=O)[O-].[Na+]` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2232  yield=63.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CC(=NO)c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>FC(F)(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (97.1%) | `graphite_generic` (1.3%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (92.8%) | `nickel` (5.1%) | `platinum` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (80.8%) | `graphite_plate` (6.5%) | `graphite_generic` (4.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (93.1%) | `NBu4` (2.5%) | `ABSENT` (2.4%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ClO4` (96.7%) | `PF6` (1.1%) | `molecular_no_ion` (1.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.2%) | `alkali_carbonate` (7.0%) | `alkali_sulfonate` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `aqueous` (0.9%) | `polar_protic_alcohol` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (100%) | `CC#N` (92%) | `CS(C)=O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `CC(=O)[O-].[Na+]` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2233  yield=50.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CC(=NO)c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>FC(F)(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (97.1%) | `graphite_generic` (1.3%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (92.8%) | `nickel` (5.1%) | `platinum` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (80.8%) | `graphite_plate` (6.5%) | `graphite_generic` (4.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `Li` (93.1%) | `NBu4` (2.5%) | `ABSENT` (2.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (96.7%) | `PF6` (1.1%) | `molecular_no_ion` (1.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.2%) | `alkali_carbonate` (7.0%) | `alkali_sulfonate` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `aqueous` (0.9%) | `polar_protic_alcohol` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (100%) | `CC#N` (92%) | `CS(C)=O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `CC(=O)[O-].[Na+]` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2234  yield=72.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CC(=NO)c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>FC(F)(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (97.1%) | `graphite_generic` (1.3%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (92.8%) | `nickel` (5.1%) | `platinum` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (80.8%) | `graphite_plate` (6.5%) | `graphite_generic` (4.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (93.1%) | `NBu4` (2.5%) | `ABSENT` (2.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (96.7%) | `PF6` (1.1%) | `molecular_no_ion` (1.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.2%) | `alkali_carbonate` (7.0%) | `alkali_sulfonate` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `aqueous` (0.9%) | `polar_protic_alcohol` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (100%) | `CC#N` (92%) | `CS(C)=O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `CC(=O)[O-].[Na+]` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2235  yield=18.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CC(=NO)c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>FC(F)(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (97.1%) | `graphite_generic` (1.3%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (92.8%) | `nickel` (5.1%) | `platinum` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (80.8%) | `graphite_plate` (6.5%) | `graphite_generic` (4.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (93.1%) | `NBu4` (2.5%) | `ABSENT` (2.4%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.7%) | `PF6` (1.1%) | `molecular_no_ion` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.2%) | `alkali_carbonate` (7.0%) | `alkali_sulfonate` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `aqueous` (0.9%) | `polar_protic_alcohol` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (100%) | `CC#N` (92%) | `CS(C)=O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `CC(=O)[O-].[Na+]` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2236  yield=22.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CC(=NO)c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>FC(F)(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (97.1%) | `graphite_generic` (1.3%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (92.8%) | `nickel` (5.1%) | `platinum` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (80.8%) | `graphite_plate` (6.5%) | `graphite_generic` (4.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (93.1%) | `NBu4` (2.5%) | `ABSENT` (2.4%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (96.7%) | `PF6` (1.1%) | `molecular_no_ion` (1.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.2%) | `alkali_carbonate` (7.0%) | `alkali_sulfonate` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `aqueous` (0.9%) | `polar_protic_alcohol` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (100%) | `CC#N` (92%) | `CS(C)=O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `CC(=O)[O-].[Na+]` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2237  yield=64.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CC(=NO)c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>FC(F)(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (97.1%) | `graphite_generic` (1.3%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (92.8%) | `nickel` (5.1%) | `platinum` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (80.8%) | `graphite_plate` (6.5%) | `graphite_generic` (4.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (93.1%) | `NBu4` (2.5%) | `ABSENT` (2.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (96.7%) | `PF6` (1.1%) | `molecular_no_ion` (1.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.2%) | `alkali_carbonate` (7.0%) | `alkali_sulfonate` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `aqueous` (0.9%) | `polar_protic_alcohol` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (100%) | `CC#N` (92%) | `CS(C)=O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `CC(=O)[O-].[Na+]` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2238  yield=35.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CC(=NO)c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>FC(F)(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (97.1%) | `graphite_generic` (1.3%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (92.8%) | `nickel` (5.1%) | `platinum` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (80.8%) | `graphite_plate` (6.5%) | `graphite_generic` (4.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (93.1%) | `NBu4` (2.5%) | `ABSENT` (2.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (96.7%) | `PF6` (1.1%) | `molecular_no_ion` (1.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.2%) | `alkali_carbonate` (7.0%) | `alkali_sulfonate` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `aqueous` (0.9%) | `polar_protic_alcohol` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (100%) | `CC#N` (92%) | `CS(C)=O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `CC(=O)[O-].[Na+]` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2239  yield=29.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CC(=NO)c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>FC(F)(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (97.1%) | `graphite_generic` (1.3%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (92.8%) | `nickel` (5.1%) | `platinum` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (80.8%) | `graphite_plate` (6.5%) | `graphite_generic` (4.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (93.1%) | `NBu4` (2.5%) | `ABSENT` (2.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (96.7%) | `PF6` (1.1%) | `molecular_no_ion` (1.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.2%) | `alkali_carbonate` (7.0%) | `alkali_sulfonate` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `aqueous` (0.9%) | `polar_protic_alcohol` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (100%) | `CC#N` (92%) | `CS(C)=O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `CC(=O)[O-].[Na+]` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2240  yield=52.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00694E_p2_t0.json) (反应 idx 在该 JSON 内 = #12)

```
C=C(CC(=NO)c1ccccc1)c1ccccc1>>FC(F)(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.3%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (99.8%) | `graphite_generic` (0.1%) | `platinum_generic` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (98.7%) | `nickel` (0.9%) | `platinum` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (99.9%) | `graphite_generic` (0.1%) | `nickel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (97.7%) | `NBu4` (1.3%) | `K` (0.8%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (98.6%) | `PF6` (0.7%) | `molecular_no_ion` (0.5%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfinate` | `alkali_sulfonate` (95.7%) | `alkali_sulfinate` (0.8%) | `alkali_carboxylate` (0.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.0%) | `Co_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.1%) | `polar_aprotic_sulfoxide` (4.0%) | `polar_protic_alcohol` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `O` (100%) | `CS(C)=O` (91%) | `CC#N` (9%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` + `[Br-].[K+]` | `O=S(=O)([O-])C(F)(` (70%) | `[Br-].[K+]` (65%) | `CC(=O)[O-].[Na+]` (30%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)NC1CC2(CCCCC` (0%) | `CC(C)(C)c1cc(C=N[C` (0%) | set ✓ / any ✓ |

---

### Reaction #2241  yield=74.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.NC(=O)c1ccccc1>>O=C(NCCCl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (4.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (40.2%) | `carbon_generic` (19.7%) | `platinum_plate` (14.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (65.6%) | `platinum` (31.2%) | `carbon` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (48.2%) | `nickel_generic` (42.8%) | `nickel_plate` (4.6%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.4%) | `K` (6.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (84.0%) | `molecular_no_ion` (7.7%) | `ClO4` (6.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.2%) | `alkali_other_salt` (6.0%) | `alkali_carboxylate` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `Co_complex` (0.3%) | `ammonium_PTC_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (71.4%) | `polar_aprotic_nitrile` (14.3%) | `aqueous` (5.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCCl` + `CCOC(C)=O` | `ClCCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (58%) | `CCOC(C)=O` (18%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O` (1%) | `CCOC(C)=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `c1ccncc1` (4%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #2242  yield=58.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.NC(=O)c1ccccc1>>O=C(NCCCl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (4.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (40.2%) | `carbon_generic` (19.7%) | `platinum_plate` (14.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (65.6%) | `platinum` (31.2%) | `carbon` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (48.2%) | `nickel_generic` (42.8%) | `nickel_plate` (4.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.4%) | `K` (6.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (84.0%) | `molecular_no_ion` (7.7%) | `ClO4` (6.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.2%) | `alkali_other_salt` (6.0%) | `alkali_carboxylate` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `Co_complex` (0.3%) | `ammonium_PTC_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (71.4%) | `polar_aprotic_nitrile` (14.3%) | `aqueous` (5.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCCl` + `CCOC(C)=O` | `ClCCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (58%) | `CCOC(C)=O` (18%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O` (1%) | `CCOC(C)=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `c1ccncc1` (4%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #2243  yield=0.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.NC(=O)c1ccccc1>>O=C(NCCCl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (4.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (40.2%) | `carbon_generic` (19.7%) | `platinum_plate` (14.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (65.6%) | `platinum` (31.2%) | `carbon` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (48.2%) | `nickel_generic` (42.8%) | `nickel_plate` (4.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.4%) | `K` (6.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (84.0%) | `molecular_no_ion` (7.7%) | `ClO4` (6.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.2%) | `alkali_other_salt` (6.0%) | `alkali_carboxylate` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `Co_complex` (0.3%) | `ammonium_PTC_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `halogenated_aliphatic` (71.4%) | `polar_aprotic_nitrile` (14.3%) | `aqueous` (5.1%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` + `CCOC(C)=O` | `ClCCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (58%) | `CCOC(C)=O` (18%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O` (1%) | `CCOC(C)=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `c1ccncc1` (4%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #2244  yield=0.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.NC(=O)c1ccccc1>>O=C(NCCCl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (4.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (40.2%) | `carbon_generic` (19.7%) | `platinum_plate` (14.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (65.6%) | `platinum` (31.2%) | `carbon` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (48.2%) | `nickel_generic` (42.8%) | `nickel_plate` (4.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.4%) | `K` (6.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (84.0%) | `molecular_no_ion` (7.7%) | `ClO4` (6.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.2%) | `alkali_other_salt` (6.0%) | `alkali_carboxylate` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `Co_complex` (0.3%) | `ammonium_PTC_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (71.4%) | `polar_aprotic_nitrile` (14.3%) | `aqueous` (5.1%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` + `CCOC(C)=O` | `ClCCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (58%) | `CCOC(C)=O` (18%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O` (1%) | `CCOC(C)=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `c1ccncc1` (4%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #2245  yield=85.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.NC(=O)c1ccccc1>>O=C(NCCCl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (4.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (40.2%) | `carbon_generic` (19.7%) | `platinum_plate` (14.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (65.6%) | `platinum` (31.2%) | `carbon` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (48.2%) | `nickel_generic` (42.8%) | `nickel_plate` (4.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.4%) | `K` (6.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (84.0%) | `molecular_no_ion` (7.7%) | `ClO4` (6.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.2%) | `alkali_other_salt` (6.0%) | `alkali_carboxylate` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `Co_complex` (0.3%) | `ammonium_PTC_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (71.4%) | `polar_aprotic_nitrile` (14.3%) | `aqueous` (5.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCCl` + `CCOC(C)=O` | `ClCCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (58%) | `CCOC(C)=O` (18%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O` (1%) | `CCOC(C)=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `c1ccncc1` (4%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #2246  yield=57.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.NC(=O)c1ccccc1>>O=C(NCCCl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (4.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (40.2%) | `carbon_generic` (19.7%) | `platinum_plate` (14.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (65.6%) | `platinum` (31.2%) | `carbon` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (48.2%) | `nickel_generic` (42.8%) | `nickel_plate` (4.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.4%) | `K` (6.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (84.0%) | `molecular_no_ion` (7.7%) | `ClO4` (6.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.2%) | `alkali_other_salt` (6.0%) | `alkali_carboxylate` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `Co_complex` (0.3%) | `ammonium_PTC_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (71.4%) | `polar_aprotic_nitrile` (14.3%) | `aqueous` (5.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCCl` + `CCOC(C)=O` | `ClCCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (58%) | `CCOC(C)=O` (18%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O` (1%) | `CCOC(C)=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `c1ccncc1` (4%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #2247  yield=0.5%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.NC(=O)c1ccccc1>>O=C(NCCCl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (4.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (40.2%) | `carbon_generic` (19.7%) | `platinum_plate` (14.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (65.6%) | `platinum` (31.2%) | `carbon` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (48.2%) | `nickel_generic` (42.8%) | `nickel_plate` (4.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.4%) | `K` (6.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (84.0%) | `molecular_no_ion` (7.7%) | `ClO4` (6.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.2%) | `alkali_other_salt` (6.0%) | `alkali_carboxylate` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `Co_complex` (0.3%) | `ammonium_PTC_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (71.4%) | `polar_aprotic_nitrile` (14.3%) | `aqueous` (5.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCCl` + `CCOC(C)=O` | `ClCCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (58%) | `CCOC(C)=O` (18%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O` (1%) | `CCOC(C)=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `c1ccncc1` (4%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #2248  yield=0.0%

**Source paper**: [`OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/10.1039_D5OB00874C_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.NC(=O)c1ccccc1>>O=C(NCCCl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (4.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (40.2%) | `carbon_generic` (19.7%) | `platinum_plate` (14.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (65.6%) | `platinum` (31.2%) | `carbon` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (48.2%) | `nickel_generic` (42.8%) | `nickel_plate` (4.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.4%) | `K` (6.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (84.0%) | `molecular_no_ion` (7.7%) | `ClO4` (6.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.2%) | `alkali_other_salt` (6.0%) | `alkali_carboxylate` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `Co_complex` (0.3%) | `ammonium_PTC_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (71.4%) | `polar_aprotic_nitrile` (14.3%) | `aqueous` (5.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCCl` + `CCOC(C)=O` | `ClCCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (58%) | `CCOC(C)=O` (18%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O` (1%) | `CCOC(C)=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `c1ccncc1` (4%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #2249  yield=11.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.NC(=O)c1ccccc1Cl>>O=C(NC(CCl)c1ccccc1)c1ccccc1Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `sacrificial_magnesium` (1.4%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (83.0%) | `graphite_rod` (8.6%) | `reticulated_vitreous_carbon` (3.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (76.9%) | `platinum` (17.7%) | `nickel` (5.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `graphite_generic` (64.5%) | `platinum_plate` (27.5%) | `nickel_plate` (1.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (91.0%) | `NBu4` (7.6%) | `ABSENT` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ClO4` (31.8%) | `BF4` (29.4%) | `PF6` (16.7%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (27.7%) | `polyhalo_radical_transfer` (4.5%) | `metal_oxide_oxidant` (1.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.3%) | `Mn_complex` (2.5%) | `brønsted_acid_cat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (84.5%) | `halogenated_aliphatic` (11.4%) | `ABSENT` (2.7%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (82%) | `ClCCCl` (10%) | `OC(C(F)(F)F)C(F)(F` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (1%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2250  yield=11.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccccc1.NC(=O)c1ccccc1Cl>>O=C(NCC(Cl)c1ccccc1)c1ccccc1Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (54.9%) | `reticulated_vitreous_carbon` (18.4%) | `carbon_generic` (17.7%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (71.8%) | `nickel` (14.1%) | `platinum` (14.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (33.6%) | `platinum_foil` (23.1%) | `graphite_generic` (17.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (69.9%) | `NBu4` (21.1%) | `ABSENT` (6.1%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ClO4` (43.7%) | `molecular_no_ion` (38.9%) | `PF6` (9.2%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `alkali_other_salt` (9.2%) | `ABSENT` (6.8%) | `carboxylic_acid` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.1%) | `Mn_complex` (7.2%) | `pyridine_organocat` (2.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (70.3%) | `ABSENT` (19.1%) | `halogenated_aliphatic` (9.4%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (72%) | `FC(F)(F)c1ccccc1` (18%) | `C1COCCO1` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `CC[Si](CC)CC` (27%) | `C[Si](C)(C)N=[N+]=` (25%) | `O.O.O.O.O.O.O.O.O.` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (76%) | `__ABSENT__` (57%) | `__OTHER__` (42%) | set ✗ / any ✓ |

---

### Reaction #2251  yield=28.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccccc1.NC(=O)c1ccccc1F>>O=C(NC(CCl)c1ccccc1)c1ccccc1F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (72.7%) | `sacrificial_magnesium` (21.3%) | `platinum` (4.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (64.3%) | `graphite_rod` (8.8%) | `magnesium_generic` (8.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (64.3%) | `carbon` (31.6%) | `nickel` (4.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (45.1%) | `graphite_generic` (25.2%) | `platinum_plate` (23.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (66.6%) | `NBu4` (31.5%) | `Li` (1.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Cl` (73.7%) | `ClO4` (18.6%) | `PF6` (3.0%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (31.9%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.6%) | `brønsted_acid_cat` (1.6%) | `organic_neutral_cat` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (95.4%) | `halogenated_aliphatic` (2.4%) | `cyclic_ether` (1.6%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (98%) | `ClCCCl` (2%) | `C1CCOC1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2252  yield=28.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1ccccc1.NC(=O)c1cccc(F)c1>>O=C(NCC(Cl)c1ccccc1)c1ccccc1F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (89.8%) | `graphite_generic` (6.3%) | `reticulated_vitreous_carbon` (1.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (66.4%) | `platinum` (28.8%) | `carbon` (4.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (68.6%) | `platinum_generic` (26.6%) | `platinum_plate` (1.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (88.2%) | `Li` (11.5%) | `ABSENT` (0.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (56.0%) | `ClO4` (42.8%) | `molecular_no_ion` (0.6%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (7.2%) | `alkali_other_salt` (3.1%) | `carboxylic_acid` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (86.3%) | `pyridine_organocat` (6.3%) | `Mn_complex` (5.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (52.6%) | `halogenated_aliphatic` (46.2%) | `ABSENT` (0.4%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (95%) | `O` (15%) | `CO` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (99%) | `CCOC(C)=O` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2253  yield=28.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #4)

```
NC(=O)c1ccccc1.C=Cc1ccc(OC(F)(F)F)cc1>>O=C(NCC(Cl)c1ccc(OC(F)(F)F)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (53.2%) | `graphite_generic` (20.3%) | `carbon_rod` (10.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (72.8%) | `nickel` (24.8%) | `carbon` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (89.9%) | `nickel_foam` (2.8%) | `platinum_generic` (2.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (68.0%) | `ABSENT` (18.9%) | `NBu4` (12.4%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (74.2%) | `ClO4` (14.9%) | `ABSENT` (7.5%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `alkali_other_salt` (15.0%) | `ammonia` (3.1%) | `carboxylic_acid` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (82.4%) | `Mn_complex` (15.3%) | `pyridine_organocat` (2.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (50.7%) | `halogenated_aliphatic` (44.0%) | `ABSENT` (2.5%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `FC(F)(F)c1ccccc1` (50%) | `CC#N` (36%) | `ClCCCl` (10%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `[Cl-].[Na+]` (17%) | `O.O.O.O.O.O.O.O.O.` (12%) | `CC(=O)O.[Na]` (12%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (4%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2254  yield=28.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #5)

```
NC(=O)c1ccccc1.C=Cc1ccc(OC(F)(F)F)cc1>>O=C(NC(CCl)c1ccc(OC(F)(F)F)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (49.5%) | `reticulated_vitreous_carbon` (49.4%) | `carbon_rod` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (96.4%) | `nickel` (1.7%) | `carbon` (1.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (94.3%) | `platinum_generic` (4.7%) | `graphite_generic` (0.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (40.1%) | `NEt4` (33.0%) | `ABSENT` (21.5%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (26.5%) | `Cl` (25.6%) | `ClO4` (19.3%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (12.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.2%) | `Mn_complex` (25.7%) | `organic_neutral_cat` (3.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (55.0%) | `polar_aprotic_nitrile` (43.7%) | `polar_protic_alcohol` (0.5%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `ClCCCl` (84%) | `CC#N` (21%) | `ClCCl` (20%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2255  yield=26.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #6)

```
C=Cc1ccccc1.NC(=O)c1ccc2ccccc2c1>>O=C(NCC(Cl)c1ccccc1)c1ccc2ccccc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (91.8%) | `platinum` (7.7%) | `sacrificial_iron` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (43.8%) | `reticulated_vitreous_carbon` (22.8%) | `carbon_rod` (15.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (77.5%) | `carbon` (12.9%) | `platinum` (9.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (62.8%) | `platinum_generic` (16.6%) | `nickel_plate` (8.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.2%) | `Li` (10.5%) | `NEt4` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (84.2%) | `ClO4` (14.1%) | `molecular_no_ion` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `alkali_other_salt` (5.5%) | `ABSENT` (4.8%) | `sulfonyl_chloride` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `pyridine_organocat` (0.7%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (71.0%) | `halogenated_aliphatic` (15.6%) | `ABSENT` (9.7%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (59%) | `FC(F)(F)c1ccccc1` (26%) | `ClCCCl` (20%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `CC[Si](CC)CC` (37%) | `O=O` (28%) | `ClCCCl` (19%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (73%) | `c1ccncc1` (72%) | `__OTHER__` (26%) | set ✗ / any ✓ |

---

### Reaction #2256  yield=26.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #7)

```
C=Cc1ccccc1.NC(=O)c1ccc2ccccc2c1>>O=C(NC(CCl)c1ccccc1)c1ccc2ccccc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (62.5%) | `platinum` (36.8%) | `sacrificial_magnesium` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `platinum_plate` (31.5%) | `platinum_generic` (26.1%) | `reticulated_vitreous_carbon` (22.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (59.7%) | `nickel` (21.4%) | `carbon` (18.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (78.2%) | `nickel_generic` (6.9%) | `platinum_plate` (6.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (74.2%) | `NEt4` (24.2%) | `Li` (0.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (83.9%) | `ClO4` (7.7%) | `Cl` (5.7%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (22.4%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.6%) | `Co_complex` (0.4%) | `ammonium_PTC_organocat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (77.6%) | `halogenated_aliphatic` (19.4%) | `cyclic_ether` (0.7%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `ClCCCl` (63%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2257  yield=24.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #8)

```
C=Cc1ccccc1.COc1cccc(C(N)=O)c1>>COc1cccc(C(=O)NCC(Cl)c2ccccc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (55.9%) | `carbon_generic` (33.2%) | `graphite_generic` (6.0%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (42.1%) | `carbon` (35.5%) | `platinum` (22.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (72.6%) | `platinum_plate` (9.1%) | `platinum_generic` (3.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (45.0%) | `Li` (44.1%) | `ABSENT` (4.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (45.3%) | `PF6` (28.4%) | `ClO4` (20.2%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `alkali_other_salt` (6.5%) | `carboxylic_acid` (5.2%) | `alkali_carboxylate` (3.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.2%) | `Mn_complex` (2.7%) | `pyridine_organocat` (2.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (54.7%) | `halogenated_aliphatic` (22.1%) | `ABSENT` (20.7%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `FC(F)(F)c1ccccc1` (51%) | `CC#N` (37%) | `ClCCCl` (6%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `CC(=O)O.[Na]` (21%) | `ClCCCl` (14%) | `O.O.O.O.O.O.O.O.O.` (8%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (95%) | `c1ccncc1` (29%) | `__OTHER__` (5%) | set ✓ / any ✓ |

---

### Reaction #2258  yield=24.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #9)

```
C=Cc1ccccc1.COc1cccc(C(N)=O)c1>>COc1cccc(C(=O)NC(CCl)c2ccccc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.2%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (74.7%) | `graphite_generic` (22.0%) | `carbon_generic` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (70.3%) | `carbon` (21.2%) | `nickel` (8.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (49.2%) | `platinum_plate` (22.4%) | `nickel_generic` (9.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `divided` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (62.5%) | `NBu4` (26.8%) | `BnNMe3` (3.3%) | ✓ |
| 电解质 anion | 26 | `PF6` | `PF6` (37.6%) | `molecular_no_ion` (19.5%) | `Cl` (17.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (17.2%) | `polyhalo_radical_transfer` (4.3%) | `metal_oxide_oxidant` (2.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (87.6%) | `brønsted_acid_cat` (5.6%) | `Mn_complex` (2.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (81.8%) | `halogenated_aliphatic` (15.2%) | `ABSENT` (2.0%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (97%) | `ClCCCl` (23%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O=O` (0%) | `BrCCBr` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2259  yield=22.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #10)

```
ClCCCl.NC(=O)c1ccccc1Br>>O=C(NC(CCl)c1ccccc1)c1ccccc1Br
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (99.1%) | `carbon_generic` (0.6%) | `graphite_rod` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (91.8%) | `platinum` (6.5%) | `nickel` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `graphite_generic` (96.5%) | `platinum_generic` (2.0%) | `graphite_rod` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (94.3%) | `ABSENT` (5.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.2%) | `NEt4` (21.6%) | `Li` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (97.3%) | `ClO4` (1.5%) | `PF6` (0.5%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (40.9%) | `electrophilic_N_F` (1.9%) | `unparseable_text` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.8%) | `Mn_complex` (2.4%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (99.7%) | `polar_protic_alcohol` (0.1%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `CO` (0%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O.O.O.O.[Cl][Mn][C` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #2260  yield=22.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #11)

```
C=Cc1ccccc1.NC(=O)c1ccccc1Br>>O=C(NCC(Cl)c1ccccc1)c1ccccc1Br
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (73.8%) | `graphite_generic` (9.9%) | `carbon_felt` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (61.3%) | `nickel` (24.2%) | `carbon` (14.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (48.1%) | `platinum_plate` (33.8%) | `platinum_foil` (6.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (54.1%) | `NBu4` (45.3%) | `Na` (0.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (61.3%) | `molecular_no_ion` (17.9%) | `BF4` (11.5%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (8.7%) | `carboxylic_acid` (2.3%) | `diboron` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `pyridine_organocat` (0.6%) | `Mn_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (97.1%) | `halogenated_aliphatic` (1.3%) | `ABSENT` (0.9%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `O` (12%) | `FC(F)(F)c1ccccc1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (99%) | `O` (1%) | `CC[Si](CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `c1ccncc1` (8%) | `__OTHER__` (3%) | set ✓ / any ✓ |

---

### Reaction #2261  yield=22.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #12)

```
NC(=O)c1ccccc1.C=Cc1ccc(I)cc1>>O=C(NCC(Cl)c1ccc(I)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (61.2%) | `graphite_generic` (17.5%) | `carbon_rod` (10.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (67.8%) | `platinum` (25.8%) | `carbon` (5.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (47.0%) | `nickel_generic` (44.9%) | `nickel_plate` (4.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (49.2%) | `NBu4` (47.2%) | `Na` (1.9%) | ✓ |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (39.8%) | `PF6` (38.8%) | `ClO4` (19.1%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (4.5%) | `fluoride_anion` (2.5%) | `sulfonyl_chloride` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.2%) | `Mn_complex` (3.9%) | `pyridine_organocat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (63.5%) | `halogenated_aliphatic` (30.2%) | `ketone` (2.0%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (80%) | `ClCCCl` (69%) | `FC(F)(F)c1ccccc1` (14%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `CCOC(C)=O` (1%) | `O=S([O-])O.[Na+]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (1%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2262  yield=22.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #13)

```
NC(=O)c1ccccc1.C=Cc1ccc(I)cc1>>O=C(NC(CCl)c1ccc(I)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (81.4%) | `reticulated_vitreous_carbon` (16.2%) | `carbon_generic` (0.9%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (70.7%) | `nickel` (24.3%) | `carbon` (4.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (78.3%) | `platinum_generic` (9.7%) | `nickel_generic` (6.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (71.0%) | `NEt4` (23.3%) | `Na` (3.3%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (64.4%) | `Cl` (13.1%) | `ClO4` (10.7%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (16.6%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (86.4%) | `Mn_complex` (8.2%) | `brønsted_acid_cat` (2.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (57.6%) | `polar_aprotic_nitrile` (40.9%) | `polar_protic_alcohol` (1.0%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `ClCCCl` (99%) | `CC#N` (70%) | `ClCCl` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `CCOC(C)=O` (0%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2263  yield=40.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #14)

```
C=Cc1ccccc1.NC(=O)c1cccc(Br)c1>>O=C(NCC(Cl)c1ccccc1)c1cccc(Br)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (39.3%) | `carbon_generic` (37.7%) | `graphite_generic` (10.0%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (95.8%) | `platinum` (2.2%) | `carbon` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (59.0%) | `nickel_plate` (20.2%) | `nickel_foam` (14.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (88.5%) | `Li` (9.7%) | `ABSENT` (1.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (58.7%) | `ClO4` (26.6%) | `molecular_no_ion` (9.9%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `alkali_other_salt` (7.3%) | `alkali_carboxylate` (4.9%) | `carboxylic_acid` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `pyridine_organocat` (3.2%) | `Mn_complex` (2.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (45.3%) | `halogenated_aliphatic` (40.9%) | `ABSENT` (11.4%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `FC(F)(F)c1ccccc1` (51%) | `CC#N` (30%) | `ClCCCl` (19%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `CC(=O)O.[Na]` (22%) | `O=S(O)O.[Na]` (14%) | `ClCCCl` (12%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `c1ccncc1` (32%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #2264  yield=40.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #15)

```
C=Cc1ccccc1.NC(=O)c1cccc(Br)c1>>O=C(NC(CCl)c1ccccc1)c1cccc(Br)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (85.4%) | `graphite_generic` (12.7%) | `carbon_generic` (0.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (64.3%) | `platinum` (30.2%) | `carbon` (5.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (38.6%) | `nickel_plate` (28.5%) | `nickel_generic` (19.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.5%) | `NEt4` (4.6%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (62.4%) | `ClO4` (15.9%) | `BF4` (15.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (13.8%) | `alkali_carboxylate` (2.3%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.2%) | `Mn_complex` (3.4%) | `ammonium_PTC_organocat` (2.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (59.9%) | `polar_aprotic_nitrile` (38.3%) | `ABSENT` (0.7%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `ClCCCl` (96%) | `CC#N` (4%) | `CCOC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `CCOC(C)=O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2265  yield=40.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #16)

```
C=Cc1ccccc1.NC(=O)c1cccs1>>O=C(NC(CCl)c1ccccc1)c1cccs1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (1.2%) | `sacrificial_magnesium` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (41.7%) | `carbon_generic` (25.7%) | `graphite_generic` (11.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (85.9%) | `carbon` (12.2%) | `nickel` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (97.0%) | `platinum_generic` (2.2%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (52.0%) | `NEt4` (42.8%) | `Li` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (70.4%) | `ClO4` (12.3%) | `Cl` (9.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (22.0%) | `carboxylic_acid` (2.9%) | `polyhalo_radical_transfer` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (87.1%) | `brønsted_acid_cat` (6.5%) | `Mn_complex` (4.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (97.8%) | `halogenated_aliphatic` (1.7%) | `polar_protic_acid` (0.2%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (4%) | `O` (4%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O=O` (0%) | `[Cl-].[Cl-].[Mg+2]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `O=S(=O)([O-])C(F)(` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2266  yield=40.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #17)

```
C=Cc1ccccc1.NC(=O)c1cccs1>>O=C(NCC(Cl)c1ccccc1)c1cccs1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (74.0%) | `carbon_felt` (12.1%) | `carbon_rod` (5.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (66.2%) | `nickel` (22.3%) | `carbon` (11.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (90.6%) | `platinum_foil` (3.5%) | `platinum_generic` (2.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.2%) | `Li` (21.2%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (46.5%) | `ClO4` (36.5%) | `molecular_no_ion` (11.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `carboxylic_acid` (15.6%) | `ABSENT` (4.0%) | `diboron` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.8%) | `pyridine_organocat` (2.9%) | `Mn_complex` (1.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (79.3%) | `halogenated_aliphatic` (19.1%) | `ABSENT` (0.6%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `O` (6%) | `CCOCC` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `CC(=O)O` (39%) | `[Cl-].[Cl-].[Mg+2]` (16%) | `O=C(O)C(F)(F)F` (14%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `c1ccncc1` (8%) | `__OTHER__` (3%) | set ✓ / any ✓ |

---

### Reaction #2267  yield=40.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccccc1.Cc1cccc(C(N)=O)c1>>Cc1cccc(C(=O)NCC(Cl)c2ccccc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.4%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (47.8%) | `carbon_generic` (25.2%) | `graphite_generic` (13.4%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (72.2%) | `platinum` (15.8%) | `carbon` (11.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (57.7%) | `platinum_plate` (24.4%) | `nickel_plate` (9.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (83.1%) | `Li` (14.6%) | `ABSENT` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (45.4%) | `ClO4` (25.4%) | `molecular_no_ion` (22.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `alkali_other_salt` (12.3%) | `ABSENT` (3.6%) | `carboxylic_acid` (3.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.6%) | `pyridine_organocat` (4.1%) | `Mn_complex` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (82.8%) | `halogenated_aliphatic` (9.6%) | `ABSENT` (6.1%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (66%) | `FC(F)(F)c1ccccc1` (30%) | `ClCCCl` (4%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `O.O.O.O.O.O.O.O.O.` (25%) | `CC(=O)O.[Na]` (17%) | `__ABSENT__` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `c1ccncc1` (54%) | `__OTHER__` (9%) | set ✗ / any ✓ |

---

### Reaction #2268  yield=40.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #19)

```
C=Cc1ccccc1.Cc1cccc(C(N)=O)c1>>Cc1cccc(C(=O)NC(CCl)c2ccccc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.4%) | `platinum` (3.6%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (49.4%) | `graphite_generic` (37.4%) | `platinum_plate` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (69.8%) | `carbon` (17.8%) | `nickel` (12.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (62.9%) | `platinum_generic` (16.4%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.1%) | `NEt4` (10.1%) | `ABSENT` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (62.9%) | `BF4` (17.5%) | `ClO4` (7.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (21.7%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.4%) | `Mn_complex` (2.4%) | `ammonium_PTC_organocat` (1.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (88.8%) | `halogenated_aliphatic` (10.4%) | `polar_protic_alcohol` (0.3%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `ClCCCl` (23%) | `OC(C(F)(F)F)C(F)(F` (9%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2269  yield=40.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #20)

```
NC(=O)c1ccccc1.C=Cc1ccc(Br)cc1>>O=C(NCC(Cl)c1ccc(Br)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (66.4%) | `graphite_felt` (11.6%) | `carbon_cloth` (8.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (67.2%) | `platinum` (27.4%) | `carbon` (5.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.4%) | `nickel_generic` (14.4%) | `nickel_foam` (9.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.0%) | `Li` (20.7%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (61.9%) | `ClO4` (25.4%) | `molecular_no_ion` (10.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `alkali_other_salt` (6.6%) | `carboxylic_acid` (5.9%) | `sulfonyl_chloride` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.8%) | `pyridine_organocat` (5.3%) | `Mn_complex` (1.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (62.9%) | `halogenated_aliphatic` (27.0%) | `ABSENT` (5.0%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (89%) | `O` (9%) | `FC(F)(F)c1ccccc1` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `CC(=O)O.[Na]` (27%) | `[Cl-].[Na+]` (10%) | `O=S(O)O.[Na]` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (7%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2270  yield=40.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #21)

```
NC(=O)c1ccccc1.C=Cc1ccc(Br)cc1>>O=C(NC(CCl)c1ccc(Br)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (89.8%) | `graphite_generic` (7.4%) | `carbon_generic` (1.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (72.5%) | `nickel` (24.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (82.4%) | `platinum_generic` (11.5%) | `nickel_plate` (2.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.6%) | `NEt4` (10.4%) | `Li` (0.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (82.4%) | `ClO4` (9.8%) | `BF4` (5.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (11.8%) | `carboxylic_acid` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (82.8%) | `Mn_complex` (10.0%) | `brønsted_acid_cat` (3.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (50.2%) | `halogenated_aliphatic` (46.3%) | `polar_protic_alcohol` (1.1%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `ClCCCl` (11%) | `O` (6%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O=O` (0%) | `CCOC(C)=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `O=S(=O)([O-])C(F)(` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2271  yield=40.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #22)

```
C=Cc1ccccc1.NC(=O)c1cccc(Cl)c1>>O=C(NCC(Cl)c1ccccc1)c1cccc(Cl)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (53.5%) | `reticulated_vitreous_carbon` (27.8%) | `carbon_rod` (14.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (90.8%) | `platinum` (8.4%) | `carbon` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (63.4%) | `platinum_plate` (16.4%) | `nickel_plate` (12.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.4%) | `Li` (10.7%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (55.4%) | `ClO4` (30.5%) | `BF4` (6.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `alkali_carboxylate` (10.0%) | `ABSENT` (3.2%) | `alkali_other_salt` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.8%) | `pyridine_organocat` (1.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (44.2%) | `polar_aprotic_nitrile` (41.0%) | `ABSENT` (8.2%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `ClCCCl` (96%) | `OC(C(F)(F)F)C(F)(F` (27%) | `CCOC(C)=O` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `CC(=O)[O-].[Na+]` (68%) | `O` (16%) | `CCOC(C)=O` (15%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `c1ccncc1` (33%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #2272  yield=40.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #23)

```
C=Cc1ccccc1.NC(=O)c1cccc(Cl)c1>>O=C(NC(CCl)c1ccccc1)c1cccc(Cl)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (71.0%) | `graphite_generic` (16.3%) | `carbon_generic` (8.0%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (59.5%) | `nickel` (37.3%) | `carbon` (3.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (62.3%) | `platinum_generic` (12.8%) | `nickel_plate` (12.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (97.8%) | `NEt4` (1.1%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (71.8%) | `BF4` (17.8%) | `ClO4` (7.5%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (19.6%) | `alkali_carboxylate` (3.5%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.2%) | `organic_neutral_cat` (0.6%) | `Mn_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (50.9%) | `polar_aprotic_nitrile` (44.4%) | `polar_protic_alcohol` (3.1%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `ClCCCl` (97%) | `OC(C(F)(F)F)C(F)(F` (14%) | `CC#N` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `CCOC(C)=O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2273  yield=38.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #24)

```
NC(=O)c1ccccc1.C=Cc1cccc(Br)c1>>O=C(NCC(Cl)c1cccc(Br)c1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (79.2%) | `graphite_generic` (8.1%) | `reticulated_vitreous_carbon` (6.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (89.6%) | `platinum` (9.5%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (58.4%) | `platinum_plate` (31.2%) | `nickel_plate` (5.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.2%) | `Li` (0.6%) | `ABSENT` (0.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (96.5%) | `ClO4` (2.7%) | `BF4` (0.3%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `alkali_sulfinate` (3.9%) | `ABSENT` (3.9%) | `alkali_carboxylate` (3.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.3%) | `pyridine_organocat` (2.0%) | `Mn_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (79.4%) | `polar_aprotic_nitrile` (18.5%) | `ABSENT` (0.9%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `ClCCCl` (96%) | `FC(F)(F)c1ccccc1` (72%) | `CCOCC` (20%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `O=S([O-])O.[Na+]` (65%) | `__ABSENT__` (18%) | `O=S(=O)([O-])C(F)(` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (22%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2274  yield=38.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #25)

```
NC(=O)c1ccccc1.C=Cc1ccc(Br)cc1.ClCCCl>>O=C(NC(CCl)c1cccc(Br)c1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (95.1%) | `carbon_generic` (3.1%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (71.8%) | `platinum` (26.2%) | `nickel` (1.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `graphite_generic` (84.7%) | `platinum_generic` (6.8%) | `graphite_rod` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (92.4%) | `ABSENT` (7.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (63.8%) | `NBu4` (35.5%) | `ABSENT` (0.4%) | ✓ |
| 电解质 anion | 26 | `PF6` | `BF4` (79.7%) | `PF6` (16.8%) | `Cl` (1.7%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (15.2%) | `alkali_sulfonate` (2.6%) | `primary_amine` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Mn_complex` (57.6%) | `Co_complex` (23.5%) | `ABSENT` (11.6%) | ✓ |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (97.7%) | `polar_protic_alcohol` (1.2%) | `halogenated_aliphatic` (0.8%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `ClCCCl` (2%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O.O.O.O.[Cl][Mn][C` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (39%) | `[Cl][Mn][Cl]` (16%) | `__OTHER__` (3%) | set ✓ / any ✓ |

---

### Reaction #2275  yield=38.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #26)

```
NC(=O)c1ccccc1.C=Cc1ccc(F)cc1>>O=C(NCC(Cl)c1ccc(F)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (57.8%) | `graphite_felt` (15.2%) | `reticulated_vitreous_carbon` (10.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (66.4%) | `platinum` (28.7%) | `carbon` (4.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (51.4%) | `platinum_plate` (26.5%) | `platinum_generic` (9.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (77.7%) | `NBu4` (18.6%) | `K` (1.3%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (71.7%) | `ClO4` (16.6%) | `PF6` (10.3%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `carboxylic_acid` (5.1%) | `alkali_other_salt` (4.2%) | `sulfonyl_chloride` (3.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.6%) | `Mn_complex` (5.5%) | `pyridine_organocat` (4.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (52.6%) | `halogenated_aliphatic` (25.3%) | `ABSENT` (19.2%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` | `CC#N` (57%) | `FC(F)(F)c1ccccc1` (32%) | `O` (10%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `CC(=O)O` (13%) | `ClCCCl` (11%) | `CC[Si](CC)CC` (10%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `c1ccncc1` (4%) | `[Cl-].[Cl-].[Mn+2]` (1%) | set ✓ / any ✓ |

---

### Reaction #2276  yield=38.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #27)

```
NC(=O)c1ccccc1.C=Cc1ccc(F)cc1>>O=C(NC(CCl)c1ccc(F)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (65.2%) | `graphite_generic` (31.6%) | `carbon_generic` (1.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (88.7%) | `nickel` (8.2%) | `carbon` (2.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (64.5%) | `platinum_generic` (27.5%) | `nickel_generic` (2.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.2%) | `NEt4` (12.8%) | `ABSENT` (4.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (64.5%) | `ClO4` (18.0%) | `molecular_no_ion` (7.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.3%) | `sulfonyl_chloride` (2.3%) | `diboron` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (62.9%) | `Mn_complex` (22.4%) | `brønsted_acid_cat` (12.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (81.8%) | `polar_aprotic_nitrile` (17.0%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCCl` | `ClCCCl` (68%) | `ClCCl` (34%) | `CC#N` (33%) | set ✓ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O=O` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `O=S(=O)([O-])C(F)(` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2277  yield=38.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #28)

```
NC(=O)c1ccccc1.C=Cc1cccc(C)c1>>Cc1cccc(C(Cl)CNC(=O)c2ccccc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (44.4%) | `carbon_generic` (41.5%) | `reticulated_vitreous_carbon` (5.5%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (65.4%) | `platinum` (29.6%) | `carbon` (4.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (43.4%) | `nickel_generic` (36.5%) | `platinum_generic` (12.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.3%) | `Li` (1.4%) | `K` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (86.8%) | `ClO4` (8.9%) | `molecular_no_ion` (1.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `carboxylic_acid` (7.2%) | `ABSENT` (5.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `Mn_complex` (0.4%) | `pyridine_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (75.8%) | `polar_aprotic_nitrile` (18.5%) | `ABSENT` (3.2%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` | `FC(F)(F)c1ccccc1` (85%) | `ClCCCl` (60%) | `CCOCC` (43%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `CC[Si](CC)CC` (32%) | `O=C(O)C(F)(F)F` (10%) | `__ABSENT__` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (5%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2278  yield=38.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #28)

```
NC(=O)c1ccccc1.C=Cc1cccc(C)c1>>Cc1cccc(C(Cl)CNC(=O)c2ccccc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (44.4%) | `carbon_generic` (41.5%) | `reticulated_vitreous_carbon` (5.5%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (65.4%) | `platinum` (29.6%) | `carbon` (4.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (43.4%) | `nickel_generic` (36.5%) | `platinum_generic` (12.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.3%) | `Li` (1.4%) | `K` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (86.8%) | `ClO4` (8.9%) | `molecular_no_ion` (1.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (7.2%) | `ABSENT` (5.0%) | `metal_oxide_oxidant` (2.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `Mn_complex` (0.4%) | `pyridine_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (75.8%) | `polar_aprotic_nitrile` (18.5%) | `ABSENT` (3.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCCl` | `FC(F)(F)c1ccccc1` (85%) | `ClCCCl` (60%) | `CCOCC` (43%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `CC[Si](CC)CC` (32%) | `O=C(O)C(F)(F)F` (10%) | `__ABSENT__` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (5%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2279  yield=37.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #30)

```
C=Cc1ccccc1.NC(=O)c1ccc(F)cc1>>O=C(NCC(Cl)c1ccccc1)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (77.3%) | `reticulated_vitreous_carbon` (10.9%) | `graphite_generic` (3.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (63.3%) | `platinum` (33.4%) | `carbon` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (56.7%) | `platinum_plate` (26.1%) | `platinum_generic` (10.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (54.7%) | `Li` (29.9%) | `K` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (46.8%) | `molecular_no_ion` (31.9%) | `ClO4` (17.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `alkali_other_salt` (11.0%) | `ABSENT` (5.2%) | `carboxylic_acid` (3.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.7%) | `pyridine_organocat` (7.4%) | `Mn_complex` (1.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (53.9%) | `halogenated_aliphatic` (30.4%) | `ABSENT` (14.0%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (45%) | `FC(F)(F)c1ccccc1` (32%) | `ClCCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `O.O.O.O.O.O.O.O.O.` (25%) | `C[Si](C)(C)N=[N+]=` (18%) | `CC[Si](CC)CC` (14%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (59%) | `__ABSENT__` (41%) | set ✗ / any ✓ |

---

### Reaction #2280  yield=37.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #31)

```
C=Cc1ccccc1.NC(=O)c1ccc(F)cc1>>O=C(NC(CCl)c1ccccc1)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (3.3%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (48.2%) | `graphite_generic` (27.8%) | `graphite_cloth` (6.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (86.9%) | `nickel` (8.8%) | `carbon` (4.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (61.3%) | `platinum_generic` (29.4%) | `nickel_generic` (5.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (70.9%) | `NEt4` (21.9%) | `ABSENT` (4.0%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (76.0%) | `ClO4` (10.2%) | `BF4` (3.6%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (24.7%) | `acid_anhydride` (2.3%) | `metal_oxide_oxidant` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.1%) | `ammonium_PTC_organocat` (3.3%) | `Mn_complex` (2.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (74.0%) | `polar_aprotic_nitrile` (24.9%) | `ABSENT` (0.3%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `ClCCCl` (95%) | `CC#N` (14%) | `OC(C(F)(F)F)C(F)(F` (4%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (1%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2281  yield=37.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #32)

```
C=Cc1ccccc1.NC(=O)c1ccc(Cl)cc1>>O=C(NCC(Cl)c1ccccc1)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (89.3%) | `reticulated_vitreous_carbon` (4.9%) | `graphite_generic` (2.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (70.5%) | `platinum` (24.8%) | `carbon` (4.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (58.2%) | `platinum_plate` (35.8%) | `platinum_generic` (1.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (33.2%) | `Li` (31.3%) | `ABSENT` (21.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (78.0%) | `PF6` (13.0%) | `ClO4` (5.0%) | ✓ |
| 试剂大类 | 103 | `ester` | `alkali_other_salt` (22.5%) | `ABSENT` (3.6%) | `alkali_carboxylate` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.9%) | `pyridine_organocat` (6.9%) | `Mn_complex` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (66.0%) | `halogenated_aliphatic` (19.1%) | `aqueous` (4.7%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` | `C[N+](=O)[O-]` (68%) | `FC(F)(F)c1ccccc1` (44%) | `C1COCCO1` (38%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCOC(C)=O` | `O` (73%) | `O.O.O.O.O.O.O.O.O.` (53%) | `CC[Si](CC)CC` (24%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `__ABSENT__` (1%) | set ✗ / any ✓ |

---

### Reaction #2282  yield=37.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #33)

```
C=Cc1ccccc1.NC(=O)c1ccc(Cl)cc1.ClCCCl>>O=C(NCC(Cl)c1ccccc1)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (96.4%) | `graphite_generic` (2.6%) | `reticulated_vitreous_carbon` (0.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `carbon` (65.9%) | `nickel` (25.8%) | `platinum` (8.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (88.3%) | `graphite_rod` (3.2%) | `platinum_plate` (1.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.2%) | `ABSENT` (9.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.0%) | `Li` (22.7%) | `ABSENT` (4.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.0%) | `molecular_no_ion` (25.9%) | `ClO4` (11.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ester` | `ABSENT` (8.4%) | `alkali_other_salt` (4.0%) | `alkali_carboxylate` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (84.1%) | `Mn_complex` (10.6%) | `Co_complex` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (95.5%) | `ABSENT` (1.0%) | `halogenated_aliphatic` (1.0%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (84%) | `FC(F)(F)c1ccccc1` (7%) | `C1COCCO1` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCOC(C)=O` | `__ABSENT__` (100%) | `O` (2%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (73%) | `__OTHER__` (56%) | `__ABSENT__` (44%) | set ✗ / any ✓ |

---

### Reaction #2283  yield=36.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #34)

```
NC(=O)c1ccccc1.C=Cc1ccc(Cl)cc1.ClCCCl>>O=C(NCC(Cl)c1ccc(Cl)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (73.0%) | `graphite_generic` (22.3%) | `graphite_felt` (1.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `carbon` (78.6%) | `nickel` (16.2%) | `platinum` (4.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (62.9%) | `graphite_felt` (18.3%) | `graphite_generic` (11.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (54.8%) | `Li` (35.2%) | `ABSENT` (7.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (29.4%) | `PF6` (26.4%) | `molecular_no_ion` (21.1%) | ✓ |
| 试剂大类 | 103 | `ester` | `ABSENT` (4.2%) | `alkali_other_salt` (3.1%) | `alkali_carboxylate` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (54.7%) | `Mn_complex` (40.4%) | `Fe_complex` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (90.8%) | `ketone` (6.3%) | `halogenated_aliphatic` (1.0%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (95%) | `CC(C)=O` (3%) | `FC(F)(F)c1ccccc1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCOC(C)=O` | `__ABSENT__` (98%) | `CC(=O)[O-].[Na+]` (0%) | `O=P([O-])([O-])[O-` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2284  yield=36.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #35)

```
NC(=O)c1ccccc1.C=Cc1ccc(Cl)cc1>>O=C(NC(CCl)c1ccc(Cl)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (67.3%) | `reticulated_vitreous_carbon` (17.7%) | `carbon_generic` (13.0%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (66.8%) | `nickel` (27.7%) | `carbon` (4.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (71.1%) | `nickel_generic` (19.2%) | `platinum_generic` (3.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (57.0%) | `ABSENT` (30.0%) | `NEt4` (8.5%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (43.2%) | `molecular_no_ion` (21.2%) | `ABSENT` (15.2%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (11.1%) | `ammonium_salt` (3.2%) | `boron_lewis_acid` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (81.2%) | `Mn_complex` (16.1%) | `brønsted_acid_cat` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (50.9%) | `polar_aprotic_nitrile` (42.9%) | `polar_protic_alcohol` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` + `CCOC(C)=O` | `ClCCCl` (61%) | `CC#N` (35%) | `CCOC(C)=O` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `CCOC(C)=O` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Cl][Mn][Cl]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2285  yield=36.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #36)

```
NC(=O)c1ccccc1.C=Cc1cccc(F)c1>>O=C(NCC(Cl)c1cccc(F)c1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (93.3%) | `graphite_generic` (3.5%) | `reticulated_vitreous_carbon` (1.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (88.7%) | `platinum` (10.1%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (97.1%) | `nickel_foam` (1.6%) | `platinum_generic` (0.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.3%) | `Li` (3.9%) | `K` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (93.1%) | `ClO4` (6.2%) | `molecular_no_ion` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carboxylate` (6.5%) | `ABSENT` (4.3%) | `alkali_other_salt` (3.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (67.4%) | `pyridine_organocat` (26.7%) | `Mn_complex` (2.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (78.3%) | `polar_aprotic_nitrile` (18.0%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCCl` | `ClCCCl` (85%) | `CCOC(C)=O` (13%) | `O` (5%) | set ✓ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `CC(=O)[O-].[Na+]` (37%) | `ClCCCl` (32%) | `O=S(=O)([O-])C(F)(` (13%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (87%) | `c1ccncc1` (28%) | `__OTHER__` (12%) | set ✓ / any ✓ |

---

### Reaction #2286  yield=36.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #37)

```
NC(=O)c1ccccc1.C=Cc1cccc(F)c1>>O=C(NC(CCl)c1cccc(F)c1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (0.7%) | `sacrificial_zinc` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (43.2%) | `graphite_generic` (32.3%) | `carbon_generic` (13.2%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (56.8%) | `nickel` (39.2%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (83.9%) | `platinum_generic` (14.2%) | `nickel_foam` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `divided` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.8%) | `NEt4` (3.3%) | `Li` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (79.1%) | `ClO4` (17.1%) | `BF4` (1.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (14.4%) | `acid_anhydride` (4.8%) | `primary_amine` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (86.1%) | `organic_neutral_cat` (2.7%) | `brønsted_acid_cat` (2.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (85.4%) | `polar_aprotic_nitrile` (12.1%) | `polar_aprotic_amide` (1.1%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` | `ClCCCl` (84%) | `CCOC(C)=O` (3%) | `CN(C)C=O` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2287  yield=36.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #38)

```
NC(=O)c1ccccc1.C=Cc1ccc(C(F)(F)F)cc1>>O=C(NCC(Cl)c1ccc(C(F)(F)F)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (42.8%) | `carbon_rod` (22.8%) | `graphite_generic` (22.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (51.2%) | `platinum` (45.2%) | `carbon` (2.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (71.3%) | `nickel_generic` (13.7%) | `platinum_generic` (7.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (75.6%) | `Li` (22.6%) | `ABSENT` (1.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (34.8%) | `PF6` (31.3%) | `molecular_no_ion` (28.0%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (3.8%) | `carboxylic_acid` (3.2%) | `alkali_other_salt` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.3%) | `pyridine_organocat` (5.0%) | `Mn_complex` (3.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (48.5%) | `polar_aprotic_nitrile` (44.6%) | `ABSENT` (3.6%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` | `ClCCl` (69%) | `FC(F)(F)c1ccccc1` (36%) | `ClCCCl` (24%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (99%) | `CCOC(C)=O` (7%) | `__OTHER__` (2%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (16%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2288  yield=36.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #38)

```
NC(=O)c1ccccc1.C=Cc1ccc(C(F)(F)F)cc1>>O=C(NCC(Cl)c1ccc(C(F)(F)F)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (42.8%) | `carbon_rod` (22.8%) | `graphite_generic` (22.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (51.2%) | `platinum` (45.2%) | `carbon` (2.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (71.3%) | `nickel_generic` (13.7%) | `platinum_generic` (7.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (75.6%) | `Li` (22.6%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (34.8%) | `PF6` (31.3%) | `molecular_no_ion` (28.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (3.8%) | `carboxylic_acid` (3.2%) | `alkali_other_salt` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.3%) | `pyridine_organocat` (5.0%) | `Mn_complex` (3.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (48.5%) | `polar_aprotic_nitrile` (44.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCCl` | `ClCCl` (69%) | `FC(F)(F)c1ccccc1` (36%) | `ClCCCl` (24%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (99%) | `CCOC(C)=O` (7%) | `__OTHER__` (2%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (16%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2289  yield=35.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #40)

```
C=Cc1ccccc1.NC(=O)c1ccc(Br)cc1>>O=C(NC(CCl)c1ccccc1)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.4%) | `platinum` (5.5%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (71.9%) | `graphite_generic` (11.2%) | `platinum_plate` (8.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (76.0%) | `nickel` (18.7%) | `carbon` (5.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (75.0%) | `platinum_generic` (18.4%) | `nickel_generic` (2.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (76.0%) | `NEt4` (22.9%) | `Li` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (91.3%) | `ClO4` (4.0%) | `BF4` (1.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (19.0%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.7%) | `ammonium_PTC_organocat` (0.6%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (60.5%) | `halogenated_aliphatic` (38.0%) | `ABSENT` (0.3%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` | `CC#N` (96%) | `ClCCCl` (34%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O=O` (0%) | `CCOC(C)=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2290  yield=35.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #41)

```
C=Cc1ccccc1.NC(=O)c1ccc(Br)cc1>>O=C(NCC(Cl)c1ccccc1)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (67.4%) | `reticulated_vitreous_carbon` (18.4%) | `graphite_generic` (5.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (61.2%) | `platinum` (35.2%) | `carbon` (3.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (74.7%) | `nickel_generic` (14.8%) | `platinum_generic` (5.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (89.9%) | `Li` (6.6%) | `ABSENT` (1.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (84.0%) | `ClO4` (7.9%) | `molecular_no_ion` (5.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ester` | `alkali_other_salt` (18.1%) | `ABSENT` (3.5%) | `carboxylic_acid` (3.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.2%) | `pyridine_organocat` (4.3%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (60.6%) | `halogenated_aliphatic` (31.5%) | `ABSENT` (5.7%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` | `CC#N` (73%) | `FC(F)(F)c1ccccc1` (18%) | `ClCCCl` (14%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `CC[Si](CC)CC` (15%) | `ClCCCl` (11%) | `O.O.O.O.O.O.O.O.O.` (10%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (69%) | `__ABSENT__` (60%) | `__OTHER__` (39%) | set ✗ / any ✓ |

---

### Reaction #2291  yield=34.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #42)

```
NC(=O)c1ccccc1.C=Cc1ccccc1Br>>O=C(NCC(Cl)c1ccccc1Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (58.9%) | `reticulated_vitreous_carbon` (24.5%) | `graphite_generic` (13.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (55.5%) | `nickel` (43.6%) | `carbon` (0.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (41.7%) | `nickel_generic` (37.8%) | `platinum_generic` (18.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.0%) | `Li` (2.6%) | `NEt4` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (54.5%) | `ClO4` (42.1%) | `BF4` (2.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (6.7%) | `alkali_sulfonate` (3.4%) | `carboxylic_acid` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (3.7%) | `ammonium_PTC_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (77.2%) | `polar_aprotic_nitrile` (19.5%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCCl` | `ClCCCl` (90%) | `FC(F)(F)c1ccccc1` (76%) | `CCOCC` (51%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (1%) | `CCOC(C)=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `c1ccncc1` (4%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2292  yield=34.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #43)

```
NC(=O)c1ccccc1.C=Cc1ccccc1Br.ClCCCl>>O=C(NCC(Cl)c1ccccc1Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (67.7%) | `carbon_generic` (26.0%) | `reticulated_vitreous_carbon` (5.7%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (47.7%) | `carbon` (35.2%) | `nickel` (16.9%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (56.8%) | `platinum_generic` (19.3%) | `platinum_plate` (10.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.9%) | `Li` (3.5%) | `NEt4` (2.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (28.9%) | `BF4` (27.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ester` | `ABSENT` (14.2%) | `alkali_sulfonate` (3.2%) | `diboron` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (71.4%) | `Mn_complex` (19.7%) | `ammonium_PTC_organocat` (5.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (95.4%) | `ketone` (2.2%) | `halogenated_aliphatic` (1.3%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (94%) | `FC(F)(F)c1ccccc1` (3%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCOC(C)=O` | `__ABSENT__` (100%) | `O=O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2293  yield=33.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #44)

```
C=Cc1ccccc1.Cc1ccc(C(N)=O)cc1.ClCCCl>>Cc1ccc(C(=O)NCC(Cl)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (74.9%) | `graphite_generic` (16.7%) | `reticulated_vitreous_carbon` (5.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (60.1%) | `platinum` (20.2%) | `carbon` (19.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (72.2%) | `nickel_plate` (9.2%) | `platinum_generic` (7.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.7%) | `ABSENT` (2.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.1%) | `Li` (2.7%) | `NEt4` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (45.7%) | `BF4` (41.9%) | `ClO4` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ester` | `ABSENT` (7.7%) | `alkali_other_salt` (4.0%) | `diboron` (3.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (75.1%) | `Mn_complex` (16.4%) | `ammonium_PTC_organocat` (3.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (96.3%) | `halogenated_aliphatic` (1.0%) | `cyclic_ether` (0.8%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `ClCCCl` (3%) | `O=CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCOC(C)=O` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=P([O-])([O-])[O-` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2294  yield=33.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #45)

```
C=Cc1ccccc1.Cc1ccc(C(N)=O)cc1>>Cc1ccc(C(=O)NC(CCl)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.7%) | `platinum` (3.2%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (54.1%) | `reticulated_vitreous_carbon` (16.8%) | `graphite_rod` (14.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (79.0%) | `nickel` (18.4%) | `carbon` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (66.3%) | `platinum_generic` (18.8%) | `nickel_plate` (7.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (80.9%) | `NEt4` (15.1%) | `BnNMe3` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (59.1%) | `BF4` (16.3%) | `ClO4` (7.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (22.2%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.3%) | `ammonium_PTC_organocat` (1.8%) | `Mn_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (62.1%) | `halogenated_aliphatic` (34.6%) | `cyclic_ether` (0.9%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `ClCCCl` (58%) | `OC(C(F)(F)F)C(F)(F` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O=O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2295  yield=33.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #46)

```
C=Cc1ccccc1.COc1ccc(C(N)=O)cc1>>COc1ccc(C(=O)NC(CCl)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `platinum` (1.7%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (45.1%) | `graphite_rod` (22.6%) | `graphite_generic` (19.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (84.6%) | `nickel` (11.5%) | `carbon` (3.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (75.4%) | `platinum_generic` (21.1%) | `nickel_plate` (1.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (58.3%) | `NEt4` (29.7%) | `Na` (5.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (63.6%) | `Cl` (12.5%) | `molecular_no_ion` (7.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (22.2%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.3%) | `Co_complex` (1.3%) | `organic_neutral_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (94.2%) | `halogenated_aliphatic` (4.1%) | `ABSENT` (0.5%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `ClCCCl` (41%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2296  yield=33.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #47)

```
C=Cc1ccccc1.COc1ccc(C(N)=O)cc1>>COc1ccc(C(=O)NCC(Cl)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_rod` (34.9%) | `reticulated_vitreous_carbon` (29.8%) | `carbon_generic` (26.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (52.0%) | `nickel` (44.0%) | `carbon` (3.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (79.5%) | `nickel_generic` (12.7%) | `platinum_generic` (5.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.5%) | `Li` (7.9%) | `K` (2.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (54.4%) | `molecular_no_ion` (25.4%) | `ClO4` (14.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (4.8%) | `alkali_other_salt` (4.1%) | `alkali_carboxylate` (3.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.3%) | `pyridine_organocat` (1.0%) | `Mn_complex` (1.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (89.3%) | `halogenated_aliphatic` (6.1%) | `ABSENT` (2.4%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (91%) | `ClCCCl` (28%) | `FC(F)(F)c1ccccc1` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (97%) | `CC(=O)[O-].[Na+]` (1%) | `O=S([O-])O.[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `c1ccncc1` (10%) | `__OTHER__` (3%) | set ✓ / any ✓ |

---

### Reaction #2297  yield=43.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #48)

```
NC(=O)c1ccccc1.C=Cc1cccc(Cl)c1>>O=C(NCC(Cl)c1cccc(Cl)c1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (77.8%) | `graphite_generic` (10.3%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (93.0%) | `platinum` (6.2%) | `carbon` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (94.9%) | `nickel_plate` (2.2%) | `platinum_plate` (1.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.7%) | `Li` (6.7%) | `ABSENT` (2.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (70.6%) | `molecular_no_ion` (13.4%) | `ClO4` (12.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `alkali_carboxylate` (12.4%) | `ABSENT` (6.5%) | `alkali_other_salt` (3.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.0%) | `pyridine_organocat` (2.2%) | `Mn_complex` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (92.0%) | `polar_aprotic_nitrile` (5.5%) | `polar_aprotic_sulfoxide` (0.7%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `ClCCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (63%) | `CCOC(C)=O` (25%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `CC(=O)[O-].[Na+]` (72%) | `ClCCCl` (8%) | `CCOC(C)=O` (8%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `c1ccncc1` (10%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #2298  yield=43.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #49)

```
NC(=O)c1ccccc1.C=Cc1cccc(Cl)c1>>O=C(NC(CCl)c1cccc(Cl)c1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (78.1%) | `reticulated_vitreous_carbon` (8.1%) | `carbon_generic` (5.4%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (60.6%) | `platinum` (31.5%) | `carbon` (7.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (85.4%) | `platinum_generic` (6.0%) | `nickel_plate` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (76.1%) | `ABSENT` (16.3%) | `Li` (4.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (37.1%) | `PF6` (28.8%) | `ClO4` (13.2%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (21.5%) | `alkali_carboxylate` (2.9%) | `acid_anhydride` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.2%) | `organic_neutral_cat` (2.5%) | `Mn_complex` (2.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (89.1%) | `polar_aprotic_nitrile` (6.1%) | `polar_protic_alcohol` (3.4%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `ClCCCl` (92%) | `OC(C(F)(F)F)C(F)(F` (33%) | `CCOC(C)=O` (24%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `CCOC(C)=O` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2299  yield=43.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #50)

```
NC(=O)c1ccccc1.C=Cc1ccccc1>>O=C(NCC(Cl)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (51.8%) | `carbon_generic` (29.2%) | `carbon_rod` (9.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (92.3%) | `platinum` (6.5%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (73.7%) | `platinum_plate` (16.1%) | `nickel_plate` (6.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (68.9%) | `Li` (24.0%) | `NEt4` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (50.1%) | `ClO4` (36.2%) | `molecular_no_ion` (10.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `alkali_other_salt` (6.6%) | `alkali_carboxylate` (4.3%) | `ABSENT` (3.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.6%) | `Mn_complex` (4.6%) | `pyridine_organocat` (1.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (44.5%) | `polar_aprotic_nitrile` (42.1%) | `ABSENT` (4.3%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` + `CCOC(C)=O` | `ClCCCl` (88%) | `FC(F)(F)c1ccccc1` (20%) | `O` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `O` (32%) | `CC[Si](CC)CC` (16%) | `O=S(O)O.[Na]` (11%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (90%) | `__OTHER__` (53%) | `__ABSENT__` (46%) | set ✗ / any ✓ |

---

### Reaction #2300  yield=43.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #51)

```
NC(=O)c1ccccc1.C=Cc1ccccc1>>O=C(NC(CCl)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.4%) | `platinum` (2.5%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (59.1%) | `graphite_generic` (27.4%) | `carbon_generic` (7.0%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (54.9%) | `platinum` (40.3%) | `carbon` (4.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (48.2%) | `nickel_generic` (24.7%) | `platinum_generic` (14.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (54.8%) | `NEt4` (39.9%) | `ABSENT` (1.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (73.2%) | `ClO4` (12.1%) | `BF4` (7.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (18.1%) | `polyhalo_radical_transfer` (2.7%) | `as_solvent_ionic_liquid` (1.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.1%) | `Mn_complex` (3.9%) | `ammonium_PTC_organocat` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (53.6%) | `polar_aprotic_nitrile` (41.8%) | `polar_aprotic_sulfoxide` (0.9%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` + `CCOC(C)=O` | `ClCCCl` (94%) | `CC#N` (24%) | `OC(C(F)(F)F)C(F)(F` (11%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `CCOC(C)=O` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `__OTHER__` (1%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #2301  yield=42.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #52)

```
NC(=O)c1ccccc1.C=Cc1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc(C(Cl)CNC(=O)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (31.5%) | `carbon_generic` (23.1%) | `carbon_felt` (20.4%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (80.9%) | `platinum` (17.2%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (27.1%) | `nickel_generic` (24.2%) | `nickel_foam` (21.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (63.3%) | `NBu4` (34.3%) | `K` (1.0%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ClO4` (54.0%) | `molecular_no_ion` (24.1%) | `PF6` (20.4%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `alkali_other_salt` (5.2%) | `carboxylic_acid` (3.9%) | `ABSENT` (3.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (83.2%) | `Mn_complex` (8.0%) | `pyridine_organocat` (6.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (75.6%) | `halogenated_aliphatic` (15.0%) | `ABSENT` (5.1%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (98%) | `O` (4%) | `ClCCCl` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `C[Si](C)(C)N=[N+]=` (20%) | `CC(=O)O.[Na]` (10%) | `O=C(O)O.[Cs]` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `c1ccncc1` (1%) | `COCCOC.[Br][Ni][Br` (1%) | set ✓ / any ✓ |

---

### Reaction #2302  yield=42.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #53)

```
NC(=O)c1ccccc1.C=Cc1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc(C(CCl)NC(=O)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.7%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (64.3%) | `graphite_generic` (31.4%) | `carbon_felt` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (48.8%) | `nickel` (47.5%) | `carbon` (3.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (52.8%) | `platinum_generic` (31.9%) | `nickel_plate` (5.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (46.6%) | `NEt4` (44.9%) | `Li` (5.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (49.0%) | `PF6` (37.5%) | `molecular_no_ion` (6.8%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (15.5%) | `ester` (3.1%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (69.6%) | `brønsted_acid_cat` (11.6%) | `Mn_complex` (11.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (66.4%) | `halogenated_aliphatic` (28.6%) | `ABSENT` (2.7%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `ClCCCl` (15%) | `O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `O.O.O.[Li+].[O-][C` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `O=S(=O)([O-])C(F)(` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2303  yield=41.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #54)

```
NC(=O)c1ccccc1.C=Cc1ccccc1Cl>>O=C(NCC(Cl)c1ccccc1Cl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (36.1%) | `graphite_generic` (34.2%) | `carbon_rod` (13.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (82.2%) | `platinum` (16.6%) | `carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (65.9%) | `nickel_plate` (13.5%) | `platinum_plate` (10.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (92.2%) | `Li` (6.3%) | `ABSENT` (1.0%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (78.5%) | `ClO4` (11.8%) | `molecular_no_ion` (6.6%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (8.4%) | `acid_anhydride` (2.3%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (81.9%) | `Mn_complex` (12.5%) | `pyridine_organocat` (2.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (95.6%) | `polar_aprotic_nitrile` (1.7%) | `polar_protic_alcohol` (1.1%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `ClCCCl` (99%) | `OC(C(F)(F)F)C(F)(F` (91%) | `ClCCl` (16%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `CCOC(C)=O` (1%) | `CC(=O)OC(C)=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COc1c(I)cc2c(c1I)-` (1%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2304  yield=41.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_27_6610-6615.json) (反应 idx 在该 JSON 内 = #55)

```
NC(=O)c1ccccc1.C=Cc1ccccc1Cl>>O=C(NC(CCl)c1ccccc1Cl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (74.5%) | `reticulated_vitreous_carbon` (12.5%) | `graphite_felt` (7.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (51.2%) | `nickel` (35.0%) | `carbon` (13.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (26.5%) | `platinum_generic` (25.3%) | `nickel_generic` (19.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (86.9%) | `ABSENT` (10.2%) | `Li` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `PF6` (47.7%) | `BF4` (19.6%) | `ClO4` (14.4%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (19.9%) | `acid_anhydride` (4.0%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (78.0%) | `organic_neutral_cat` (14.9%) | `Mn_complex` (3.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (97.8%) | `polar_aprotic_nitrile` (1.1%) | `ABSENT` (0.4%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `ClCCCl` (98%) | `OC(C(F)(F)F)C(F)(F` (88%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `__ABSENT__` (100%) | `CC(=O)OC(C)=O` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COc1c(I)cc2c(c1I)-` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2305  yield=35.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #0)

```
O=S(O)C(F)(F)F.[Na].CC(C)(CC=Cc1ccccc1)C(=NO)c1ccccc1>>CC1(C)CC(C(F)(F)F)C(c2ccccc2)[N+]([O-])=C1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (99.3%) | `unknown_electrode` (0.2%) | `graphite_plate` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (49.9%) | `platinum` (27.0%) | `carbon` (14.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (74.6%) | `graphite_generic` (10.3%) | `stainless_steel_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (97.2%) | `ABSENT` (2.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `ABSENT` (82.2%) | `Li` (15.6%) | `NBu4` (1.8%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (89.8%) | `ClO4` (6.3%) | `molecular_no_ion` (1.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (24.2%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (93.2%) | `ketone` (2.5%) | `ABSENT` (1.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (95%) | `CN(C)C=O` (0%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2306  yield=50.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #1)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(Cc1ccccc1)=NO)c1ccccc1>>FC(F)(F)CC1(c2ccccc2)CC(Cc2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (99.4%) | `carbon_plate` (0.3%) | `carbon_generic` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (95.1%) | `nickel` (3.4%) | `platinum` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (99.0%) | `graphite_plate` (0.4%) | `stainless_steel_generic` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (92.9%) | `ABSENT` (5.4%) | `NBu4` (0.7%) | ✗ |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (65.1%) | `ClO4` (26.5%) | `ABSENT` (6.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (32.4%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `Mn_complex` (0.1%) | `ionic_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `aqueous` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (83%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O=C([O-])[O-].[Ca+` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2307  yield=49.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #2)

```
Cc1ccc(S(=O)O)cc1.[Na].C=C(CC(=NO)c1ccccc1)c1ccccc1>>Cc1ccc(S(=O)(=O)CC2(c3ccccc3)CC(c3ccccc3)=NO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_generic` (44.4%) | `graphite_generic` (41.9%) | `carbon_plate` (7.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (73.1%) | `platinum` (15.7%) | `nickel` (11.0%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (44.5%) | `nickel_plate` (28.4%) | `platinum_generic` (18.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (64.1%) | `ABSENT` (24.4%) | `Li` (11.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (65.5%) | `ClO4` (20.5%) | `ABSENT` (13.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.1%) | `electrophilic_N_F` (2.2%) | `unparseable_text` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.4%) | `polar_aprotic_sulfoxide` (0.4%) | `cyclic_ether` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (88%) | `OC(C(F)(F)F)C(F)(F` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2308  yield=42.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #3)

```
O=S(O)c1ccc(Cl)cc1.[Na].C=C(CC(=NO)c1ccccc1)c1ccccc1>>O=S(=O)(CC1(c2ccccc2)CC(c2ccccc2)=NO1)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (77.0%) | `carbon_generic` (16.8%) | `graphite_rod` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (57.7%) | `platinum` (33.1%) | `nickel` (8.7%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (35.0%) | `nickel_plate` (28.0%) | `platinum_generic` (14.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `ABSENT` (89.7%) | `NBu4` (8.3%) | `Li` (1.9%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (80.5%) | `BF4` (17.8%) | `ClO4` (1.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (32.3%) | `electrophilic_N_F` (2.1%) | `unparseable_text` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.7%) | `polar_aprotic_sulfoxide` (0.2%) | `aqueous` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (81%) | `OC(C(F)(F)F)C(F)(F` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2309  yield=46.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #4)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(C#Cc1ccccc1)=NO)c1ccccc1>>FC(F)(F)CC1(c2ccccc2)CC(C#Cc2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (99.7%) | `graphite_plate` (0.1%) | `carbon_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (99.3%) | `platinum` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (98.4%) | `graphite_plate` (0.7%) | `graphite_felt` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (99.2%) | `NEt4` (0.4%) | `NBu4` (0.3%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ClO4` (64.6%) | `molecular_no_ion` (34.5%) | `Cl` (0.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (34.9%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `ketone` (0.2%) | `aqueous` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `O` (100%) | `CC#N` (100%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `Cl` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `Cc1cc(O[C@@H](C)C(` (0%) | set ✓ / any ✓ |

---

### Reaction #2310  yield=46.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #5)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccc(C#N)cc1)c1ccccc1>>N#Cc1ccc(C2=NOC(CC(F)(F)F)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (99.8%) | `carbon_generic` (0.1%) | `carbon_plate` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (99.1%) | `nickel` (0.4%) | `stainless_steel` (0.2%) | ✗ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (98.0%) | `stainless_steel_generic` (0.8%) | `graphite_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (99.1%) | `ABSENT` (0.7%) | `NBu4` (0.1%) | ✗ |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (57.5%) | `ClO4` (40.4%) | `ABSENT` (1.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.3%) | `electrophilic_N_F` (2.2%) | `unparseable_text` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `aqueous` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (79%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2311  yield=48.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #6)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccsc1)c1ccccc1>>FC(F)(F)CC1(c2ccccc2)CC(c2ccsc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (99.8%) | `carbon_generic` (0.1%) | `carbon_plate` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (99.1%) | `nickel` (0.8%) | `platinum` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (99.7%) | `nickel_plate` (0.2%) | `carbon_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (99.3%) | `NBu4` (0.6%) | `NEt4` (0.0%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ClO4` (99.1%) | `molecular_no_ion` (0.7%) | `BF4` (0.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (32.0%) | `alkali_sulfonate` (2.5%) | `electrophilic_N_F` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.8%) | `polar_protic_alcohol` (0.1%) | `aqueous` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (81%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2312  yield=49.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #7)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccoc1)c1ccccc1>>FC(F)(F)CC1(c2ccccc2)CC(c2ccoc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (99.4%) | `carbon_plate` (0.3%) | `carbon_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (99.6%) | `nickel` (0.3%) | `platinum` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (99.4%) | `nickel_plate` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (98.3%) | `NBu4` (1.0%) | `ABSENT` (0.6%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (86.2%) | `molecular_no_ion` (12.7%) | `PF6` (0.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (43.6%) | `electrophilic_N_F` (1.7%) | `unparseable_text` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ionic_organocat` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (0.6%) | `aqueous` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (29%) | `CO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.[Li+].[O-][C` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #2313  yield=42.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #8)

```
O=S(O)C(F)(F)F.[Na].C=CCC(=NO)c1ccccc1>>FC(F)(F)CC1CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (86.5%) | `graphite_plate` (12.2%) | `carbon_rod` (0.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (98.9%) | `nickel` (0.7%) | `platinum` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `graphite_generic` (88.4%) | `graphite_plate` (11.0%) | `graphite_rod` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (98.1%) | `ABSENT` (0.6%) | `NBu4` (0.5%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (51.8%) | `molecular_no_ion` (45.4%) | `BF4` (1.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.1%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (81.6%) | `aqueous` (15.2%) | `ester` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `O` (100%) | `CC#N` (99%) | `CS(C)=O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2314  yield=58.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #9)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccc(C)cc1)c1ccccc1>>Cc1ccc(C2=NOC(CC(F)(F)F)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (49.9%) | `carbon_generic` (45.2%) | `carbon_plate` (4.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (98.2%) | `nickel` (1.5%) | `platinum` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `graphite_generic` (81.3%) | `graphite_plate` (9.1%) | `carbon_generic` (6.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (99.9%) | `NBu4` (0.1%) | `ABSENT` (0.0%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (82.8%) | `molecular_no_ion` (16.9%) | `BF4` (0.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (34.8%) | `alkali_sulfonate` (2.4%) | `electrophilic_N_F` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.7%) | `aqueous` (0.3%) | `polar_protic_alcohol` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (99%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2315  yield=54.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #10)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)C1CCCCC1)c1ccccc1>>FC(F)(F)CC1(c2ccccc2)CC(C2CCCCC2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (72.8%) | `carbon_plate` (24.8%) | `carbon_generic` (1.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (78.4%) | `carbon` (19.2%) | `stainless_steel` (1.7%) | ✗ |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_plate` (92.1%) | `graphite_generic` (6.0%) | `nickel_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (77.7%) | `Li` (21.6%) | `NBu4` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (58.8%) | `molecular_no_ion` (36.0%) | `ClO4` (4.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (24.0%) | `electrophilic_N_F` (2.2%) | `unparseable_text` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.4%) | `aqueous` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (2%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S([O-])O.[Na+]` (0%) | `O=C([O-])[O-].[Cs+` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2316  yield=54.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #11)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccc(C(C)(C)C)cc1)c1ccccc1>>CC(C)(C)c1ccc(C2=NOC(CC(F)(F)F)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `nickel` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (97.6%) | `carbon_generic` (1.0%) | `carbon_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (98.0%) | `nickel` (1.5%) | `platinum` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (97.7%) | `graphite_plate` (1.0%) | `nickel_plate` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (96.5%) | `Na` (1.6%) | `K` (0.7%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (56.0%) | `ClO4` (42.8%) | `ABSENT` (0.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (40.5%) | `electrophilic_N_F` (1.8%) | `unparseable_text` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.4%) | `aqueous` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (98%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `[Br-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2317  yield=55.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #12)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccc2ccccc2c1)c1ccccc1>>FC(F)(F)CC1(c2ccccc2)CC(c2ccc3ccccc3c2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (96.4%) | `carbon_generic` (2.9%) | `carbon_plate` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (98.8%) | `nickel` (0.8%) | `platinum` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (96.4%) | `carbon_generic` (1.0%) | `graphite_plate` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (99.9%) | `NBu4` (0.1%) | `Na` (0.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (91.3%) | `molecular_no_ion` (8.5%) | `BF4` (0.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (32.3%) | `electrophilic_N_F` (2.0%) | `unparseable_text` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.9%) | `aqueous` (0.1%) | `ketone` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (98%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2318  yield=53.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #13)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1cccc(F)c1)c1ccccc1>>Fc1cccc(C2=NOC(CC(F)(F)F)(c3ccccc3)C2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (99.3%) | `carbon_generic` (0.7%) | `carbon_plate` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (98.8%) | `nickel` (1.0%) | `platinum` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (99.4%) | `nickel_plate` (0.2%) | `carbon_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (99.7%) | `NBu4` (0.2%) | `K` (0.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (96.8%) | `molecular_no_ion` (2.8%) | `PF6` (0.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (30.4%) | `alkali_sulfonate` (3.4%) | `electrophilic_N_F` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.8%) | `aqueous` (0.1%) | `ketone` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (96%) | `CO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2319  yield=67.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #14)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccccc1)c1ccc(C)cc1>>Cc1ccc(C2(CC(F)(F)F)CC(c3ccccc3)=NO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (77.1%) | `carbon_generic` (20.3%) | `carbon_plate` (1.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (98.8%) | `nickel` (0.9%) | `platinum` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `graphite_generic` (90.1%) | `graphite_plate` (4.6%) | `carbon_generic` (3.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (99.8%) | `NBu4` (0.1%) | `ABSENT` (0.0%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (93.2%) | `molecular_no_ion` (6.4%) | `BF4` (0.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (32.3%) | `alkali_sulfonate` (3.4%) | `electrophilic_N_F` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.8%) | `aqueous` (0.1%) | `polar_protic_alcohol` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (99%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Br-].[Mn+2]` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2320  yield=63.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #15)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1cccc(C)c1)c1ccccc1>>Cc1cccc(C2=NOC(CC(F)(F)F)(c3ccccc3)C2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (96.9%) | `carbon_generic` (2.5%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (99.1%) | `nickel` (0.7%) | `platinum` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (99.5%) | `carbon_generic` (0.2%) | `nickel_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (99.6%) | `ABSENT` (0.2%) | `NBu4` (0.1%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (82.2%) | `molecular_no_ion` (17.3%) | `ABSENT` (0.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (35.7%) | `electrophilic_N_F` (1.9%) | `unparseable_text` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.9%) | `aqueous` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (74%) | `CO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.[Li+].[O-][C` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2321  yield=68.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #16)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1cc(C)cc(C)c1)c1ccccc1>>Cc1cc(C)cc(C2=NOC(CC(F)(F)F)(c3ccccc3)C2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (99.3%) | `carbon_generic` (0.5%) | `carbon_plate` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (97.5%) | `nickel` (2.3%) | `platinum` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (99.1%) | `nickel_plate` (0.4%) | `carbon_generic` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (99.7%) | `NBu4` (0.2%) | `ABSENT` (0.1%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (81.9%) | `molecular_no_ion` (17.7%) | `BF4` (0.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (30.3%) | `electrophilic_N_F` (2.1%) | `unparseable_text` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.7%) | `aqueous` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (82%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.[Li+].[O-][C` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2322  yield=68.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #17)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccc(I)cc1)c1ccccc1>>FC(F)(F)CC1(c2ccccc2)CC(c2ccc(I)cc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (96.5%) | `carbon_generic` (2.8%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (98.8%) | `nickel` (1.1%) | `platinum` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (94.7%) | `graphite_plate` (2.7%) | `nickel_plate` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (99.9%) | `Na` (0.0%) | `NBu4` (0.0%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (68.8%) | `molecular_no_ion` (31.1%) | `BF4` (0.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (36.0%) | `electrophilic_N_F` (1.9%) | `unparseable_text` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.8%) | `aqueous` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (98%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #2323  yield=63.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #18)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccccc1)c1ccc(I)cc1>>FC(F)(F)CC1(c2ccc(I)cc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (98.9%) | `carbon_generic` (0.8%) | `carbon_plate` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (99.4%) | `nickel` (0.5%) | `platinum` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (97.9%) | `graphite_plate` (1.2%) | `carbon_generic` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (99.9%) | `NBu4` (0.0%) | `Na` (0.0%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (73.7%) | `molecular_no_ion` (26.1%) | `BF4` (0.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (34.7%) | `electrophilic_N_F` (1.9%) | `unparseable_text` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.8%) | `aqueous` (0.1%) | `ketone` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (99%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `[Br-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #2324  yield=64.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #19)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccc(Br)cc1)c1ccccc1>>FC(F)(F)CC1(c2ccccc2)CC(c2ccc(Br)cc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (64.2%) | `carbon_generic` (32.3%) | `carbon_plate` (2.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (99.0%) | `nickel` (0.8%) | `platinum` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (74.9%) | `graphite_plate` (18.0%) | `carbon_generic` (4.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (99.6%) | `NBu4` (0.1%) | `ABSENT` (0.1%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (92.0%) | `molecular_no_ion` (7.5%) | `BF4` (0.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (33.2%) | `electrophilic_N_F` (2.0%) | `alkali_formate` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.6%) | `aqueous` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (99%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2325  yield=61.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #20)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccc2c(c1)OC(F)(F)O2)c1ccccc1>>FC(F)(F)CC1(c2ccccc2)CC(c2ccc3c(c2)OC(F)(F)O3)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (97.3%) | `carbon_plate` (1.5%) | `carbon_generic` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (98.8%) | `nickel` (0.7%) | `platinum` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (99.2%) | `carbon_generic` (0.3%) | `nickel_plate` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (98.1%) | `K` (1.3%) | `NBu4` (0.3%) | ✗ |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (52.5%) | `ClO4` (46.5%) | `PF6` (0.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (38.2%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.9%) | `aqueous` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (98%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[K+]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2326  yield=70.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #22)

```
O=S(O)C(F)F.[Na].C=C(CC(=NO)c1ccccc1)c1ccccc1>>FC(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (90.0%) | `carbon_plate` (4.1%) | `graphite_plate` (2.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (68.5%) | `carbon` (23.4%) | `platinum` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_plate` (85.9%) | `graphite_generic` (8.8%) | `platinum_generic` (2.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (81.4%) | `Li` (10.8%) | `ABSENT` (6.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (79.2%) | `ClO4` (15.8%) | `ABSENT` (3.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (30.0%) | `electrophilic_N_F` (2.0%) | `unparseable_text` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.5%) | `polar_aprotic_sulfoxide` (1.6%) | `polar_protic_alcohol` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (68%) | `OC(C(F)(F)F)C(F)(F` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2327  yield=80.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #23)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccc(Cl)cc1)c1ccccc1>>FC(F)(F)CC1(c2ccccc2)CC(c2ccc(Cl)cc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (83.9%) | `carbon_generic` (13.8%) | `carbon_plate` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (97.8%) | `platinum` (1.1%) | `nickel` (1.0%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (94.0%) | `graphite_plate` (1.8%) | `nickel_plate` (1.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (98.9%) | `ABSENT` (0.6%) | `NBu4` (0.1%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (74.8%) | `molecular_no_ion` (23.3%) | `ABSENT` (1.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (39.9%) | `electrophilic_N_F` (1.8%) | `unparseable_text` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ionic_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.7%) | `aqueous` (0.2%) | `polar_protic_alcohol` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (97%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2328  yield=72.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #24)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccccc1)c1ccccc1>>FC(F)(F)CC1(c2ccccc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (98.2%) | `carbon_plate` (0.9%) | `carbon_generic` (0.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (99.3%) | `nickel` (0.5%) | `platinum` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `graphite_generic` (98.7%) | `carbon_generic` (0.4%) | `nickel_plate` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (98.6%) | `ABSENT` (0.9%) | `NBu4` (0.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (88.0%) | `molecular_no_ion` (10.3%) | `ABSENT` (1.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (25.1%) | `electrophilic_N_F` (2.1%) | `unparseable_text` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.4%) | `aqueous` (0.4%) | `polar_protic_alcohol` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (93%) | `CS(C)=O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2329  yield=71.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #25)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccccc1)c1ccc(Cl)cc1>>FC(F)(F)CC1(c2ccc(Cl)cc2)CC(c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (94.3%) | `carbon_generic` (5.0%) | `carbon_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (98.8%) | `platinum` (0.7%) | `nickel` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (97.1%) | `carbon_generic` (1.0%) | `graphite_plate` (0.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (98.9%) | `ABSENT` (0.6%) | `NBu4` (0.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (85.4%) | `molecular_no_ion` (12.0%) | `ABSENT` (1.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (33.6%) | `alkali_sulfonate` (2.8%) | `electrophilic_N_F` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ionic_organocat` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.8%) | `aqueous` (0.1%) | `polar_protic_alcohol` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (98%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `[Br-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2330  yield=72.0%

**Source paper**: [`OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2025_Organic_Biomolecular_Chemistry_2025_23_28_6808-6813.json) (反应 idx 在该 JSON 内 = #26)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(=NO)c1ccc(C(F)(F)F)cc1)c1ccccc1>>FC(F)(F)CC1(c2ccccc2)CC(c2ccc(C(F)(F)F)cc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (97.9%) | `carbon_generic` (1.6%) | `carbon_plate` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (99.6%) | `nickel` (0.3%) | `platinum` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (99.0%) | `carbon_generic` (0.4%) | `nickel_plate` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (99.4%) | `ABSENT` (0.2%) | `NBu4` (0.2%) | ✗ |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (68.3%) | `ClO4` (30.9%) | `ABSENT` (0.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (32.9%) | `alkali_sulfonate` (2.8%) | `metal_oxide_oxidant` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.8%) | `aqueous` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (95%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2331  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ammonium_PTC_organocat` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2332  yield=50.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ammonium_PTC_organocat` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2333  yield=58.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ammonium_PTC_organocat` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2334  yield=51.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ammonium_PTC_organocat` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2335  yield=22.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Br` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ammonium_PTC_organocat` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2336  yield=49.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `water` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ammonium_PTC_organocat` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2337  yield=44.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_phosphate` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ammonium_PTC_organocat` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2338  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ammonium_PTC_organocat` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2339  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ammonium_PTC_organocat` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2340  yield=65.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_phosphate` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ammonium_PTC_organocat` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2341  yield=28.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `chloride_anion` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ammonium_PTC_organocat` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2342  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2343  yield=36.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2344  yield=49.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2345  yield=51.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2346  yield=54.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2347  yield=22.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2348  yield=52.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2349  yield=45.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2350  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2351  yield=64.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2352  yield=63.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_hydroxide` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2353  yield=39.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2354  yield=56.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_phosphate` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2355  yield=39.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2356  yield=42.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_hydroxide` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2357  yield=14.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `hcl` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2358  yield=16.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `inorganic_simple` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2359  yield=63.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_phosphate` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2360  yield=49.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_phosphate` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2361  yield=30.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_alkoxide` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2362  yield=26.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `aromatic_neutral` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2363  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2364  yield=45.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_phosphate` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2365  yield=65.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_phosphate` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2366  yield=41.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_alkoxide` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2367  yield=44.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00289c_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00289c_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OCCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (74.5%) | `carbon_generic` (12.5%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (33.4%) | `stainless_steel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_foil` (32.9%) | `platinum_plate` (27.9%) | `carbon_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.7%) | `NBu4` (20.3%) | `NEt4` (13.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (67.6%) | `Br` (13.9%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_phosphate` | `iodide_anion` (14.9%) | `carboxylic_acid` (4.8%) | `azide_source` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `Mn_complex` (5.0%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_acid` (52.0%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_amide` (5.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC(=O)O` (92%) | `O=CO` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `CC(C)(C)c1cc(C=N[C` (15%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #2368  yield=18.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2369  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2370  yield=75.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2371  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2372  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2373  yield=7.5%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2374  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2375  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2376  yield=0.5%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `thianthrene_phenothiazine_cat` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2377  yield=65.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2378  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2379  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2380  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `tempo_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2381  yield=40.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2382  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2383  yield=53.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `alkali_hydroxide` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2384  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2385  yield=13.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2386  yield=30.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2387  yield=37.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2388  yield=23.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `alkali_phosphate` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2389  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `alkali_alkoxide` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2390  yield=75.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2391  yield=31.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2392  yield=30.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `alkali_phosphate` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2393  yield=0.5%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2394  yield=18.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `alkali_phosphate` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2395  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2396  yield=73.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4ccccc4n3C(C)(C2)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (45.0%) | `reticulated_vitreous_carbon` (26.3%) | `graphite_generic` (14.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `ABSENT` (0.1%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (85.2%) | `platinum_generic` (14.6%) | `unknown_electrode` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (53.4%) | `ABSENT` (45.8%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.7%) | `NEt4` (1.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (98.7%) | `ClO4` (0.8%) | `PF6` (0.4%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (12.1%) | `ABSENT` (4.7%) | `electrophilic_N_F` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (85.7%) | `organic_neutral_cat` (7.5%) | `Mn_complex` (2.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (96.4%) | `polar_protic_alcohol` (1.5%) | `halogenated_aliphatic` (0.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (77%) | `C1CCOC1` (2%) | `COCCOC` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (38%) | `O=O` (2%) | `CO` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #2397  yield=73.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #1)

```
C=C(C)C(=O)n1ccc2cc(C)ccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4cc(C)ccc4n3C(C)(C2)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (66.2%) | `reticulated_vitreous_carbon` (21.4%) | `graphite_rod` (4.9%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `stainless_steel` (0.1%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (90.8%) | `platinum_generic` (8.3%) | `stainless_steel_generic` (0.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (65.8%) | `ABSENT` (33.1%) | `divided` (1.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.0%) | `NEt4` (3.1%) | `ABSENT` (1.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (99.1%) | `ABSENT` (0.6%) | `PF6` (0.2%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (42.3%) | `ABSENT` (3.3%) | `electrophilic_N_F` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.9%) | `ferrocene_mediator` (0.4%) | `organic_neutral_cat` (0.4%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (55.4%) | `acyclic_ether` (23.5%) | `ABSENT` (13.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (6%) | `COCCOC` (3%) | `C1CCOC1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `[I-].[Na+]` (66%) | `O=O` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #2398  yield=70.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #2)

```
C=C(C)C(=O)n1ccc2cc(F)ccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4cc(F)ccc4n3C(C)(C2)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (51.5%) | `reticulated_vitreous_carbon` (29.1%) | `graphite_generic` (14.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (80.2%) | `platinum_generic` (19.4%) | `stainless_steel_generic` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.2%) | `ABSENT` (9.9%) | `divided` (0.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.1%) | `NEt4` (2.2%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (99.4%) | `ABSENT` (0.5%) | `ClO4` (0.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (49.7%) | `ABSENT` (4.0%) | `electrophilic_N_F` (1.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.7%) | `ferrocene_mediator` (0.8%) | `organic_neutral_cat` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (47.1%) | `acyclic_ether` (35.2%) | `halogenated_aliphatic` (8.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `COCCOC` (8%) | `ClCCl` (3%) | `CC#N` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `[I-].[Na+]` (70%) | `__ABSENT__` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `__OTHER__` (0%) | set ✗ / any ✓ |

---

### Reaction #2399  yield=73.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #3)

```
C=C(C)C(=O)n1ccc2cc(Cl)ccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4cc(Cl)ccc4n3C(C)(C2)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (68.0%) | `reticulated_vitreous_carbon` (16.7%) | `graphite_generic` (10.4%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (93.8%) | `platinum_generic` (5.8%) | `stainless_steel_generic` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (81.6%) | `ABSENT` (17.7%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.4%) | `ABSENT` (8.8%) | `NEt4` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (94.3%) | `ABSENT` (5.2%) | `PF6` (0.2%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (32.7%) | `ABSENT` (4.7%) | `electrophilic_N_F` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.5%) | `ferrocene_mediator` (0.2%) | `organic_neutral_cat` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (82.6%) | `acyclic_ether` (11.9%) | `halogenated_aliphatic` (1.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (21%) | `COCCOC` (3%) | `ClCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `[I-].[Na+]` (44%) | `__ABSENT__` (1%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #2400  yield=71.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #4)

```
C=C(C)C(=O)n1ccc2cc(Br)ccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4cc(Br)ccc4n3C(C)(C2)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (74.9%) | `reticulated_vitreous_carbon` (14.2%) | `graphite_generic` (8.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.5%) | `platinum_generic` (1.4%) | `platinum_wire` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (92.3%) | `ABSENT` (6.9%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.5%) | `NEt4` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (98.2%) | `ClO4` (1.5%) | `PF6` (0.1%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (11.3%) | `ABSENT` (7.0%) | `electrophilic_N_F` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.5%) | `organic_neutral_cat` (0.3%) | `ferrocene_mediator` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.2%) | `ABSENT` (15.9%) | `halogenated_aliphatic` (6.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (5%) | `COCCOC` (3%) | `C1CCOC1` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `[I-].[Na+]` (31%) | `__ABSENT__` (3%) | `C[Si](C)(C)N=[N+]=` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✓ |

---

### Reaction #2401  yield=69.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #5)

```
C=C(C)C(=O)n1ccc2cc(I)ccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4cc(I)ccc4n3C(C)(C2)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (42.3%) | `graphite_generic` (23.4%) | `graphite_rod` (18.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.3%) | `platinum_generic` (1.6%) | `stainless_steel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (94.5%) | `ABSENT` (5.3%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.4%) | `NEt4` (4.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (98.5%) | `ClO4` (0.6%) | `PF6` (0.5%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (27.0%) | `ABSENT` (6.5%) | `electrophilic_N_F` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.6%) | `organic_neutral_cat` (0.2%) | `ferrocene_mediator` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (79.5%) | `acyclic_ether` (7.7%) | `halogenated_aliphatic` (3.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (6%) | `COCCOC` (3%) | `C1CCOC1` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `[I-].[Na+]` (35%) | `__ABSENT__` (6%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #2402  yield=74.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #6)

```
C=C(C)C(=O)n1ccc2cc(OC)ccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4cc(OC)ccc4n3C(C)(C2)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (76.2%) | `graphite_rod` (13.9%) | `graphite_generic` (8.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (93.1%) | `platinum_generic` (6.6%) | `stainless_steel_generic` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.0%) | `ABSENT` (3.6%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.6%) | `ABSENT` (0.3%) | `NEt4` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (99.4%) | `ClO4` (0.2%) | `ABSENT` (0.2%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (23.1%) | `ABSENT` (5.7%) | `electrophilic_N_F` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.1%) | `ferrocene_mediator` (0.6%) | `Fe_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (77.2%) | `acyclic_ether` (5.7%) | `ABSENT` (5.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `COCCOC` (15%) | `CC#N` (5%) | `C1CCOC1` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `[I-].[Na+]` (53%) | `__ABSENT__` (1%) | `O=O` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✓ |

---

### Reaction #2403  yield=72.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #7)

```
C=C(C)C(=O)n1ccc2cc(OCc3ccccc3)ccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4cc(OCc5ccccc5)ccc4n3C(C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (46.7%) | `graphite_rod` (40.3%) | `graphite_generic` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `ABSENT` (0.0%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (76.0%) | `platinum_generic` (23.8%) | `stainless_steel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (67.5%) | `ABSENT` (32.3%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.6%) | `ABSENT` (1.2%) | `NEt4` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.2%) | `ABSENT` (2.1%) | `PF6` (1.3%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (18.5%) | `ABSENT` (5.2%) | `electrophilic_N_F` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (97.8%) | `ferrocene_mediator` (1.9%) | `organic_neutral_cat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (89.3%) | `ABSENT` (5.6%) | `acyclic_ether` (1.5%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `C1CCOC1` (8%) | `COCCOC` (8%) | `CC#N` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `[I-].[Na+]` (27%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✓ |

---

### Reaction #2404  yield=67.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #8)

```
C=C(C)C(=O)n1ccc2cc(C(=O)OC)ccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4cc(C(=O)OC)ccc4n3C(C)(C2)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `graphite_generic` (42.4%) | `graphite_rod` (39.8%) | `carbon_felt` (14.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.5%) | `carbon` (0.4%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.3%) | `platinum_generic` (3.6%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (82.9%) | `ABSENT` (16.8%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.9%) | `NEt4` (1.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (97.5%) | `PF6` (2.1%) | `ClO4` (0.2%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (14.0%) | `ABSENT` (7.2%) | `as_solvent_cyclic_ether` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.6%) | `ferrocene_mediator` (0.3%) | `organic_neutral_cat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (82.6%) | `acyclic_ether` (5.9%) | `ABSENT` (5.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (16%) | `COCCOC` (3%) | `C1CCOC1` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `[I-].[Na+]` (32%) | `O=O` (2%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `c1ccncc1` (0%) | set ✗ / any ✓ |

---

### Reaction #2405  yield=66.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #9)

```
C=C(C)C(=O)n1ccc2cc(NC(=O)OC(C)(C)C)ccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4cc(NC(=O)OC(C)(C)C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (43.4%) | `graphite_rod` (35.3%) | `carbon_felt` (9.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `ABSENT` (0.1%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (93.0%) | `platinum_generic` (6.9%) | `unknown_electrode` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (81.2%) | `ABSENT` (18.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.0%) | `NEt4` (7.4%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (97.8%) | `PF6` (1.3%) | `ClO4` (0.4%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (10.9%) | `iodide_anion` (7.6%) | `electrophilic_N_F` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.1%) | `ferrocene_mediator` (0.4%) | `organic_neutral_cat` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (89.1%) | `acyclic_ether` (2.8%) | `polar_protic_alcohol` (2.5%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (44%) | `C1CCOC1` (2%) | `COCCOC` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (100%) | `CO` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #2406  yield=74.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #10)

```
C=C(C)C(=O)n1ccc2c(C)cccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4c(C)cccc4n3C(C)(C2)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_generic` (30.9%) | `carbon_felt` (22.7%) | `graphite_rod` (18.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (93.7%) | `platinum_generic` (6.3%) | `platinum_wire` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (63.2%) | `ABSENT` (36.6%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.8%) | `ABSENT` (0.1%) | `NEt4` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (99.7%) | `PF6` (0.2%) | `ABSENT` (0.1%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (3.7%) | `iodide_anion` (3.7%) | `alkali_carboxylate` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (73.8%) | `ferrocene_mediator` (19.4%) | `organic_neutral_cat` (2.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (57.9%) | `polar_protic_alcohol` (26.0%) | `halogenated_aliphatic` (6.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (19%) | `CO` (1%) | `C1CCOC1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (97%) | `CC(=O)[O-].[Na+]` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✓ |

---

### Reaction #2407  yield=72.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #11)

```
C=C(C)C(=O)n1ccc2c(Cl)cccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4c(Cl)cccc4n3C(C)(C2)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (74.9%) | `graphite_rod` (7.8%) | `carbon_cloth` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (97.7%) | `platinum_generic` (2.2%) | `platinum_wire` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (79.0%) | `ABSENT` (20.3%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.9%) | `NEt4` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (99.8%) | `PF6` (0.1%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (12.2%) | `ABSENT` (6.0%) | `electrophilic_N_F` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (95.9%) | `ferrocene_mediator` (2.8%) | `organic_neutral_cat` (0.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (49.5%) | `polar_protic_alcohol` (20.6%) | `halogenated_aliphatic` (14.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `COCCOC` (7%) | `C1CCOC1` (4%) | `ClCCl` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `[I-].[Na+]` (73%) | `O` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✓ |

---

### Reaction #2408  yield=67.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #12)

```
C=C(C)C(=O)n1ccc2ccc(F)cc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4ccc(F)cc4n3C(C)(C2)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (64.0%) | `carbon_felt` (22.9%) | `graphite_generic` (7.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.9%) | `platinum_generic` (3.1%) | `stainless_steel_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (50.7%) | `undivided` (48.9%) | `divided` (0.4%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.7%) | `NEt4` (8.1%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (98.7%) | `PF6` (0.7%) | `ClO4` (0.4%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (32.6%) | `ABSENT` (6.2%) | `electrophilic_N_F` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.3%) | `organic_neutral_cat` (0.3%) | `ferrocene_mediator` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (71.2%) | `acyclic_ether` (15.4%) | `halogenated_aliphatic` (9.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (7%) | `ClCCl` (5%) | `COCCOC` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `[I-].[Na+]` (90%) | `__ABSENT__` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Br-].[Br-].[Mn+2]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #2409  yield=71.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #13)

```
C=C(C)C(=O)n1ccc2ccc(C)cc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4ccc(C)cc4n3C(C)(C2)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (40.0%) | `carbon_felt` (39.2%) | `graphite_generic` (14.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.4%) | `platinum_generic` (3.6%) | `stainless_steel_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (75.7%) | `undivided` (23.1%) | `divided` (1.3%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.7%) | `NEt4` (3.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (99.5%) | `PF6` (0.3%) | `ClO4` (0.2%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (15.2%) | `ABSENT` (7.4%) | `electrophilic_N_F` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.2%) | `ferrocene_mediator` (0.3%) | `organic_neutral_cat` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (74.0%) | `acyclic_ether` (12.7%) | `ABSENT` (5.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (7%) | `C1CCOC1` (2%) | `COCCOC` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `[I-].[Na+]` (82%) | `O=O` (2%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #2410  yield=63.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #14)

```
C=C(C)C(=O)n1ccc2cccc(C)c21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4cccc(C)c4n3C(C)(C2)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `graphite_rod` (81.1%) | `graphite_generic` (7.3%) | `carbon_felt` (5.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (65.1%) | `platinum_generic` (34.8%) | `platinum_wire` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.9%) | `NEt4` (0.1%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (99.9%) | `PF6` (0.1%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `iodide_anion` (5.2%) | `ABSENT` (4.3%) | `electrophilic_N_F` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (97.7%) | `ferrocene_mediator` (0.8%) | `Fe_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (98.3%) | `polar_protic_alcohol` (0.9%) | `acyclic_ether` (0.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (96%) | `O` (4%) | `ClCCl` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `[I-].[Na+]` (43%) | `__ABSENT__` (1%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✗ / any ✓ |

---

### Reaction #2411  yield=65.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #15)

```
C=C(C)C(=O)n1ccc2cccc(Br)c21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C12CC(C)(C1)N1Cc3cc4cccc(Br)c4n3C(C)(C2)C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `graphite_rod` (47.2%) | `reticulated_vitreous_carbon` (23.3%) | `carbon_felt` (19.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (60.9%) | `platinum_plate` (39.0%) | `platinum_wire` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (99.7%) | `ClO4` (0.3%) | `PF6` (0.0%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (10.3%) | `iodide_anion` (4.0%) | `electrophilic_N_F` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.1%) | `organic_neutral_cat` (0.5%) | `ferrocene_mediator` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (98.0%) | `polar_protic_alcohol` (0.9%) | `acyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (93%) | `COCCOC` (1%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✓ |

---

### Reaction #2412  yield=70.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t1.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t1.json) (反应 idx 在该 JSON 内 = #16)

```
C=C(C)C(=O)n1c2c(c3ccccc31)CCCC2.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>O=C1N2Cc3c4c(n3C1(C)CC1(C(=O)OCC)CC2(C)C1)CCCC4
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (99.8%) | `graphite_rod` (0.1%) | `carbon_generic` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `ABSENT` (0.0%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (90.2%) | `platinum_generic` (9.5%) | `platinum_wire` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (78.5%) | `ABSENT` (21.3%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.7%) | `ABSENT` (1.2%) | `Li` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (97.0%) | `ABSENT` (1.8%) | `OH` (0.5%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (9.8%) | `iodide_anion` (3.9%) | `tetraaryl_borate` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (71.3%) | `ferrocene_mediator` (26.2%) | `Fe_complex` (1.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (78.5%) | `polar_aprotic_nitrile` (6.0%) | `polar_aprotic_sulfoxide` (5.1%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `COCCOC` (95%) | `CO` (3%) | `O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✓ |

---

### Reaction #2413  yield=68.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t2.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t2.json) (反应 idx 在该 JSON 内 = #7)

```
C=C(C)C(=O)n1cccc1.CCOC(=O)C(CCC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2(C)Cn3cccc3C21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (79.0%) | `reticulated_vitreous_carbon` (11.1%) | `graphite_rod` (5.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.5%) | `carbon` (1.0%) | `nickel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (92.6%) | `platinum_generic` (5.3%) | `nickel_foam` (1.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (10.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (99.2%) | `NBu4` (0.8%) | `Li` (0.0%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (97.3%) | `BF4` (2.7%) | `PF6` (0.0%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (5.2%) | `sulfonic_acid` (4.5%) | `alkali_other_salt` (4.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (54.8%) | `organic_neutral_cat` (11.7%) | `Co_complex` (8.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (67.6%) | `halogenated_aliphatic` (11.2%) | `polar_aprotic_nitrile` (8.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CO` (6%) | `ClCCCl` (4%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (99%) | `O=C(O)O.[Na]` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC1[CH-]C(C)=[O]->` (0%) | set ✗ / any ✗ |

---

### Reaction #2414  yield=70.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t2.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t2.json) (反应 idx 在该 JSON 内 = #9)

```
C=C(C)C(=O)n1ccc2cc(OC)ccc21.CC(=O)C(CCC=C(C)C)C(=O)OCc1ccccc1>>CC(=O)C(CCC1(C)CC2(C)C(=O)n3cccc3C2(C)C1)C(=O)OCc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_magnesium` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (83.2%) | `carbon_generic` (13.8%) | `glassy_carbon` (1.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (67.7%) | `platinum_plate` (32.0%) | `platinum_foil` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (65.7%) | `undivided` (34.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (99.4%) | `NBu4` (0.6%) | `NEt4` (0.0%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (99.1%) | `BF4` (0.8%) | `PF6` (0.1%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (8.2%) | `carboxylic_acid` (2.9%) | `alkali_other_salt` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (83.5%) | `triarylamine_radical_cat` (4.4%) | `ferrocene_mediator` (3.6%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (92.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (0.5%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (94%) | `CN(C)C=O` (1%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (100%) | `O=C(O)O.[Na]` (0%) | `CC(C)C(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✗ |

---

### Reaction #2415  yield=73.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p3_t2.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p3_t2.json) (反应 idx 在该 JSON 内 = #10)

```
C=C(C)C(=O)n1ccc2cc(OC)ccc21.CCOC(=O)C(CCC=C(C)C)C(C)=O>>CCOC(=O)C(CCC1(C)CC2(C)C(=O)n3cccc3C2(C)C1)C(C)=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_generic` (64.5%) | `reticulated_vitreous_carbon` (32.2%) | `carbon_felt` (1.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (94.9%) | `platinum_plate` (5.0%) | `platinum_foil` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (73.6%) | `undivided` (26.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (99.7%) | `NBu4` (0.3%) | `NEt4` (0.0%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (99.2%) | `BF4` (0.7%) | `PF6` (0.0%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `carboxylic_acid` (6.3%) | `alkali_carboxylate` (5.3%) | `alkali_other_salt` (5.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (24.4%) | `triarylamine_radical_cat` (22.7%) | `ferrocene_mediator` (19.4%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (73.4%) | `polar_protic_alcohol` (21.8%) | `polar_aprotic_sulfoxide` (2.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (67%) | `CN(C)C=O` (15%) | `OCC(F)(F)F` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (6%) | `__ABSENT__` (3%) | `CC(=O)O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (33%) | `CC1[CH-]C(C)=[O]->` (12%) | `__OTHER__` (5%) | set ✗ / any ✗ |

---

### Reaction #2416  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2417  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2418  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2419  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2420  yield=22.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2421  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2422  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2423  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2424  yield=21.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2425  yield=0.5%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2426  yield=22.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2427  yield=33.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `solvent_mixture` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2428  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2429  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2430  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2431  yield=26.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2432  yield=37.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2433  yield=75.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2434  yield=75.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2435  yield=15.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2436  yield=0.5%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2437  yield=47.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2438  yield=32.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2439  yield=48.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2440  yield=53.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2441  yield=34.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2442  yield=47.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2443  yield=31.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2444  yield=48.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2445  yield=29.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2446  yield=50.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2447  yield=36.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2448  yield=75.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2449  yield=52.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2450  yield=44.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2451  yield=35.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2452  yield=71.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2453  yield=48.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2454  yield=60.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2455  yield=15.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2456  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2457  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2458  yield=0.0%

**Source paper**: [`OrgChemFront/10.1039_d5qo00353a_p6_t0.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/10.1039_d5qo00353a_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1ccc2ccccc21.CCOC(=O)C(CC=C(C)C)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC2C(C)(C1)C(=O)n1c(cc3ccccc31)C2(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (62.3%) | `graphite_generic` (34.1%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.6%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.4%) | `ClO4` (2.0%) | `ABSENT` (1.3%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `iodide_anion` (26.8%) | `alkali_sulfonate` (5.0%) | `ABSENT` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `ferrocene_mediator` (18.4%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (70.4%) | `ABSENT` (9.0%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC(=O)O` | `CC#N` (11%) | `ClCCCl` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` + `CN(C)c1ccncc1` + `CC(C)(C)C(=O)O` | `[I-].[Na+]` (43%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC1(C)CCCC(C)(C)N1` + `N#CC1=C(C#N)C(=O)C` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2459  yield=3.0%

**Source paper**: [`OrgChemFront/2025_Organic_Chemistry_Frontiers_2025_12_12_3620-3625.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/2025_Organic_Chemistry_Frontiers_2025_12_12_3620-3625.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OC(CCl)c1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.3%) | `sacrificial_magnesium` (2.4%) | `platinum` (1.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (51.4%) | `reticulated_vitreous_carbon` (28.1%) | `carbon_generic` (7.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (86.8%) | `carbon` (10.7%) | `stainless_steel` (1.3%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_foil` (86.1%) | `platinum_generic` (7.8%) | `platinum_plate` (3.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (44.2%) | `NBu4` (31.6%) | `Li` (17.2%) | ✓ |
| 电解质 anion | 26 | `Cl` | `BF4` (41.4%) | `Cl` (29.4%) | `ClO4` (8.2%) | ✓ |
| 试剂大类 | 103 | `water` | `carboxylic_acid` (5.9%) | `polyhalo_radical_transfer` (5.6%) | `ABSENT` (3.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Mn_complex` (57.6%) | `ABSENT` (20.0%) | `brønsted_acid_cat` (16.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (41.7%) | `polar_protic_acid` (41.2%) | `polar_aprotic_amide` (6.0%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (99%) | `O=CO` (95%) | `CC#N` (84%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (99%) | `O=O` (98%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (97%) | `O=S(=O)(O)C(F)(F)F` (3%) | `[Cl-].[Cl-].[Mn+2]` (3%) | set ✓ / any ✓ |

---

### Reaction #2460  yield=12.0%

**Source paper**: [`OrgChemFront/2025_Organic_Chemistry_Frontiers_2025_12_12_3620-3625.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/2025_Organic_Chemistry_Frontiers_2025_12_12_3620-3625.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(-c2ccccc2)cc1>>c1ccc(-c2ccc(C3CO3)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (87.9%) | `platinum` (10.2%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (84.5%) | `glassy_carbon` (6.8%) | `reticulated_vitreous_carbon` (1.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.1%) | `carbon` (0.3%) | `ABSENT` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (67.1%) | `platinum_generic` (27.7%) | `platinum_wire` (3.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (33.4%) | `ABSENT` (22.7%) | `K` (16.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `ABSENT` (27.4%) | `PF6` (22.9%) | `Br` (22.5%) | ✗ |
| 试剂大类 | 103 | `water` | `alkali_other_salt` (12.2%) | `alkali_sulfinate` (6.6%) | `bromide_anion` (4.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (70.1%) | `ABSENT` (14.3%) | `Mn_complex` (6.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (38.0%) | `polar_protic_acid` (37.7%) | `ABSENT` (6.7%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC#N` (83%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `__OTHER__` (99%) | `CC[Si](CC)CC` (98%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `c1ccncc1` (97%) | `__OTHER__` (17%) | `O=S(=O)(O)C(F)(F)F` (3%) | set ✗ / any ✗ |

---

### Reaction #2461  yield=46.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_37_10502-10506.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_37_10502-10506.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCc1ccccc1>>c1ccc(CCC2CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (83.0%) | `ABSENT` (7.2%) | `platinum` (3.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `glassy_carbon` (83.5%) | `graphite_rod` (7.1%) | `pencil_graphite` (6.1%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (66.8%) | `stainless_steel` (23.1%) | `ABSENT` (5.9%) | ✗ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (74.1%) | `stainless_steel_generic` (8.2%) | `unknown_electrode` (7.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (65.4%) | `ABSENT` (29.0%) | `divided` (5.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (64.7%) | `ABSENT` (14.9%) | `Na` (11.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `Br` (58.5%) | `BF4` (26.9%) | `ABSENT` (9.9%) | ✗ |
| 试剂大类 | 103 | `water` | `as_solvent_halogenated_aliphat` (17.6%) | `as_solvent_polar_aprotic_sulfo` (10.5%) | `carboxylic_acid` (6.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `Mn_complex` (0.2%) | `ionic_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (78.6%) | `polar_aprotic_sulfoxide` (7.9%) | `polar_aprotic_amide` (3.7%) | ✓ |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `FC(F)(F)c1ccccc1` (61%) | `CCOCC` (45%) | `O` (45%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[SiH](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (98%) | `OB(O)B(O)O` (96%) | `O` (69%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Br-].[Br-].[Mn+2]` | `__ABSENT__` (55%) | `c1ccncc1` (22%) | `__OTHER__` (14%) | set ✗ / any ✗ |

---

### Reaction #2462  yield=17.0%

**Source paper**: [`OrgChemFront/2025_Organic_Chemistry_Frontiers_2025_12_15_4209-4215.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/2025_Organic_Chemistry_Frontiers_2025_12_15_4209-4215.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1.CCOC(=O)C(CC=C(C)C)C(=O)OCC.C=C(C)C(=O)n1ccc2ccccc21>>CCOC(=O)C1(C(=O)OCC)C[C@H]2C(C)(C)c3cc4cc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `carbon_felt` (51.7%) | `graphite_generic` (41.0%) | `graphite_rod` (5.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.2%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `ABSENT` (6.1%) | `NEt4` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (95.8%) | `ABSENT` (3.1%) | `ClO4` (0.9%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (18.6%) | `alkali_sulfonate` (4.1%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (43.0%) | `ferrocene_mediator` (36.0%) | `organic_neutral_cat` (9.0%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.8%) | `halogenated_aliphatic` (14.6%) | `ABSENT` (10.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (11%) | `ClCCCl` (6%) | `CO` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CN(C)c1cc[nH+]cc1` | `[I-].[Na+]` (32%) | `O=C(O)O.[Na]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #2463  yield=53.0%

**Source paper**: [`OrgChemFront/2025_Organic_Chemistry_Frontiers_2025_12_15_4209-4215.json`](reactions_by_journal_alkene_ec_audited/OrgChemFront/2025_Organic_Chemistry_Frontiers_2025_12_15_4209-4215.json) (反应 idx 在该 JSON 内 = #1)

```
C=C(c1ccccc1)c1ccccc1.CCOC(=O)C(CC=C(C)C)C(=O)OCC.C=C(C)C(=O)n1ccc2ccccc21>>CCOC(=O)C1(CC=C(C)C)CC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `ABSENT` (0.8%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `graphite_rod` (46.3%) | `carbon_felt` (46.2%) | `carbon_generic` (7.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.8%) | `ABSENT` (4.5%) | `nickel` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (97.1%) | `platinum_generic` (2.0%) | `unknown_electrode` (0.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (85.2%) | `ABSENT` (14.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.3%) | `NBu4` (41.6%) | `Li` (0.0%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (57.0%) | `BF4` (42.2%) | `PF6` (0.5%) | ✓ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (15.8%) | `ABSENT` (2.9%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (90.5%) | `ferrocene_mediator` (1.8%) | `Ni_complex` (1.7%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (22.9%) | `polar_protic_alcohol` (18.1%) | `polar_aprotic_amide` (17.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (25%) | `COCCOC` (6%) | `CO` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CN(C)c1cc[nH+]cc1` | `[I-].[Na+]` (45%) | `__OTHER__` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (99%) | `__OTHER__` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✗ / any ✗ |

---

### Reaction #2464  yield=5.0%

**Source paper**: [`JACS/2017_Journal_of_the_American_Chemical_Society_2017_139_43_15548-15553.json`](reactions_by_journal_alkene_ec_audited/JACS/2017_Journal_of_the_American_Chemical_Society_2017_139_43_15548-15553.json) (反应 idx 在该 JSON 内 = #14)

```
C=Cc1ccccc1>>ClCC(Cl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.4%) | `platinum` (1.1%) | `sacrificial_magnesium` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (89.3%) | `graphite_generic` (6.9%) | `carbon_generic` (2.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (60.2%) | `carbon` (37.0%) | `ABSENT` (1.2%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_foil` (99.1%) | `platinum_generic` (0.5%) | `graphite_generic` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (56.6%) | `undivided` (43.0%) | `divided` (0.4%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (41.2%) | `NEt4` (34.1%) | `ABSENT` (18.3%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (57.5%) | `ABSENT` (17.7%) | `BF4` (11.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `polyhalo_radical_transfer` (52.1%) | `carboxylic_acid` (15.0%) | `inorganic_simple` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `brønsted_acid_cat` (85.6%) | `Mn_complex` (9.1%) | `ABSENT` (4.5%) | ✗ |
| 溶剂大类 | 27 | `ketone` | `polar_aprotic_nitrile` (89.0%) | `polar_protic_acid` (5.9%) | `ABSENT` (2.6%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (60%) | `CC#N` (37%) | `C[N+](=O)[O-]` (28%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (100%) | `O=O` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (99%) | `__OTHER__` (98%) | `O=S(=O)(O)C(F)(F)F` (1%) | set ✓ / any ✓ |

---

### Reaction #2465  yield=33.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2466  yield=95.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2467  yield=85.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2468  yield=90.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2469  yield=92.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2470  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2471  yield=90.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2472  yield=41.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2473  yield=38.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2474  yield=51.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2475  yield=69.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2476  yield=83.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2477  yield=49.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2478  yield=79.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2479  yield=85.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00005_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CNC(=O)c1ccccc1.c1cn[nH]c1>>c1ccc(C2=NC(n3cccn3)CO2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (4.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.3%) | `graphite_generic` (25.9%) | `carbon_rod` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (89.1%) | `platinum` (8.2%) | `nickel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (88.5%) | `platinum_plate` (6.2%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `ABSENT` (9.0%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `PF6` (0.3%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `chloride_anion` (3.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ionic_organocat` | `ionic_organocat` (98.2%) | `ABSENT` (1.1%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (43.2%) | `polar_aprotic_nitrile` (41.0%) | `cyclic_ether` (12.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (94%) | `OC(C(F)(F)F)C(F)(F` (42%) | `CC#N` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (65%) | `[Cl-].[Na+]` (32%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (90%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2480  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1>>CCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (98.8%) | `glassy_carbon` (0.4%) | `graphite_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (3.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (73.3%) | `platinum_plate` (17.8%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2481  yield=74.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1>>CCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (98.8%) | `glassy_carbon` (0.4%) | `graphite_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (3.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (73.3%) | `platinum_plate` (17.8%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `molecular_no_ion` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2482  yield=75.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1>>CCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (98.8%) | `glassy_carbon` (0.4%) | `graphite_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (3.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (73.3%) | `platinum_plate` (17.8%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2483  yield=87.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1>>CCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (98.8%) | `glassy_carbon` (0.4%) | `graphite_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (3.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (73.3%) | `platinum_plate` (17.8%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `K` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2484  yield=73.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1>>CCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (98.8%) | `glassy_carbon` (0.4%) | `graphite_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (3.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (73.3%) | `platinum_plate` (17.8%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2485  yield=86.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1>>CCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (98.8%) | `glassy_carbon` (0.4%) | `graphite_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (3.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (73.3%) | `platinum_plate` (17.8%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✓ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2486  yield=62.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1>>CCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (98.8%) | `glassy_carbon` (0.4%) | `graphite_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (3.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (73.3%) | `platinum_plate` (17.8%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2487  yield=69.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1>>CCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (98.8%) | `glassy_carbon` (0.4%) | `graphite_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (3.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (73.3%) | `platinum_plate` (17.8%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2488  yield=64.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1>>CCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (98.8%) | `glassy_carbon` (0.4%) | `graphite_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (3.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (73.3%) | `platinum_plate` (17.8%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2489  yield=83.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1>>CCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (98.8%) | `glassy_carbon` (0.4%) | `graphite_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (3.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (73.3%) | `platinum_plate` (17.8%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2490  yield=85.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1>>CCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (98.8%) | `glassy_carbon` (0.4%) | `graphite_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (3.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (73.3%) | `platinum_plate` (17.8%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2491  yield=71.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1>>CCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (98.8%) | `glassy_carbon` (0.4%) | `graphite_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (3.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (73.3%) | `platinum_plate` (17.8%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2492  yield=86.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1>>CCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (98.8%) | `glassy_carbon` (0.4%) | `graphite_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (3.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (73.3%) | `platinum_plate` (17.8%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `K` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2493  yield=76.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1>>CCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (98.8%) | `glassy_carbon` (0.4%) | `graphite_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (3.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (73.3%) | `platinum_plate` (17.8%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2494  yield=84.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
CCCCCCCC=C=CC1(O)CCCCC1.[Br-].[K+]>>CCCCCCCC1=C(Br)CC2(CCCCC2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (1.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (90.5%) | `graphite_generic` (6.9%) | `glassy_carbon` (1.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (68.5%) | `carbon` (31.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (49.6%) | `graphite_rod` (18.6%) | `platinum_generic` (10.5%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `Na` (90.0%) | `molecular_no_ion` (6.2%) | `ABSENT` (1.7%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (56.5%) | `Br` (24.4%) | `carboxylate` (11.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (42.4%) | `bromide_anion` (2.2%) | `metal_oxide_oxidant` (1.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `main_group_lewis_acid` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.7%) | `polar_protic_alcohol` (7.8%) | `halogenated_aliphatic` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (23%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2495  yield=35.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #1)

```
CCCCCCCC=C=CC1(O)CCCCC1.[Cl-].[K+]>>CCCCCCCC1=C(Cl)CC2(CCCCC2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (0.9%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (92.6%) | `graphite_generic` (2.8%) | `glassy_carbon` (1.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.3%) | `carbon` (15.7%) | `copper` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (66.2%) | `platinum_generic` (12.2%) | `platinum_foil` (5.6%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.3%) | `ABSENT` (0.7%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `ABSENT` (47.8%) | `Na` (28.5%) | `molecular_no_ion` (7.0%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (35.1%) | `ABSENT` (30.9%) | `molecular_no_ion` (20.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (50.5%) | `bromide_anion` (1.5%) | `metal_oxide_oxidant` (1.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `polar_protic_alcohol` (0.3%) | `polar_aprotic_sulfoxide` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (2%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=C(O)O.[Na]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2496  yield=9.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #2)

```
CCCCCCCC=C=CC1(O)CCCCC1.[I-].[K+]>>CCCCCCCC1=C(I)CC2(CCCCC2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `platinum` (3.6%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (57.7%) | `graphite_generic` (18.2%) | `platinum_plate` (6.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (57.5%) | `carbon` (42.3%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.3%) | `reticulated_vitreous_carbon` (13.8%) | `platinum_generic` (4.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `Na` (44.6%) | `ABSENT` (28.3%) | `molecular_no_ion` (21.0%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (65.3%) | `Cl` (14.0%) | `ABSENT` (13.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (48.1%) | `metal_oxide_oxidant` (1.6%) | `tellurium_reagent` (1.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.4%) | `polar_protic_alcohol` (1.3%) | `aqueous` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (21%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C(O)O.[Na]` (0%) | `[Br-].[H+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2497  yield=60.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #3)

```
CCCCCCCC=C=CC1(O)CCC1>>CCCCCCCC1=C(Br)CC2(CCC2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.8%) | `platinum` (6.0%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (38.6%) | `graphite_generic` (29.9%) | `glassy_carbon` (26.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.7%) | `carbon` (8.6%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (87.8%) | `platinum_foil` (3.9%) | `graphite_generic` (2.6%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `Na` (84.5%) | `H` (9.6%) | `molecular_no_ion` (3.0%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (48.8%) | `molecular_no_ion` (37.0%) | `carboxylate` (9.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (22.3%) | `bromide_anion` (12.1%) | `carboxylic_acid` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `main_group_lewis_acid` (0.1%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (54.2%) | `polar_protic_alcohol` (31.1%) | `halogenated_aliphatic` (7.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (33%) | `ClCCl` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `[Br-].[H+]` (1%) | `O=S([O-])([O-])=S.` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2498  yield=74.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #4)

```
CCCCCCCC=C=CC1(O)CCCC1>>CCCCCCCC1=C(Br)CC2(CCCC2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `platinum` (2.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (43.0%) | `graphite_rod` (34.2%) | `glassy_carbon` (20.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (81.7%) | `carbon` (17.8%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (70.5%) | `graphite_generic` (12.2%) | `platinum_generic` (4.9%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `Na` (72.1%) | `H` (17.2%) | `molecular_no_ion` (7.2%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (63.7%) | `molecular_no_ion` (22.3%) | `carboxylate` (10.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (32.7%) | `bromide_anion` (6.8%) | `polyhalo_radical_transfer` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `main_group_lewis_acid` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.6%) | `polar_protic_alcohol` (26.9%) | `halogenated_aliphatic` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (27%) | `ClCCl` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2499  yield=67.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #5)

```
CCCCCCCC=C=CC1(O)CCCCCC1>>CCCCCCCC1=C(Br)CC2(CCCCCC2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.0%) | `platinum` (2.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (75.5%) | `graphite_generic` (14.1%) | `glassy_carbon` (8.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.8%) | `carbon` (14.9%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (76.1%) | `graphite_rod` (6.5%) | `platinum_generic` (5.7%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `Na` (81.2%) | `molecular_no_ion` (8.7%) | `H` (7.2%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (51.9%) | `molecular_no_ion` (37.8%) | `carboxylate` (7.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (35.9%) | `bromide_anion` (5.0%) | `polyhalo_radical_transfer` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `main_group_lewis_acid` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (74.4%) | `polar_protic_alcohol` (22.5%) | `halogenated_aliphatic` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (29%) | `ClCCl` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2500  yield=75.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #6)

```
CCCCCCCC=C=CC1(O)CCCCCCCCCCC1>>CCCCCCCC1=C(Br)CC2(CCCCCCCCCCC2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.0%) | `platinum` (2.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (75.5%) | `graphite_generic` (14.1%) | `glassy_carbon` (8.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.8%) | `carbon` (14.9%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (76.1%) | `graphite_rod` (6.5%) | `platinum_generic` (5.7%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `Na` (81.2%) | `molecular_no_ion` (8.7%) | `H` (7.2%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (51.9%) | `molecular_no_ion` (37.8%) | `carboxylate` (7.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (35.9%) | `bromide_anion` (5.0%) | `polyhalo_radical_transfer` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `main_group_lewis_acid` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (74.4%) | `polar_protic_alcohol` (22.5%) | `halogenated_aliphatic` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (29%) | `ClCCl` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

