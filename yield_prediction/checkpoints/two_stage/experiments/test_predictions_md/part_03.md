# Test 预测 part 3 — 反应 #1001-#1500

[← 返回 INDEX](INDEX.md)

### Reaction #1001  yield=5.0%

**Source paper**: [`ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json) (反应 idx 在该 JSON 内 = #1)

```
CS(=O)(=O)n1cc(-c2ccccc2)nn1.C=C(c1ccccc1)c1ccccc1>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `platinum` (1.7%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (98.9%) | `graphite_rod` (0.4%) | `graphite_plate` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.2%) | `ABSENT` (0.8%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (65.7%) | `K` (15.2%) | `Li` (13.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (44.3%) | `carboxylate` (12.6%) | `molecular_no_ion` (10.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.7%) | `boron_lewis_acid` (6.2%) | `water` (4.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.7%) | `halogenated_aliphatic` (0.4%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (98%) | `ClCCl` (41%) | `O` (30%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[NH4+].[OH-]` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1002  yield=19.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1.O=S(=O)(c1ccc(OC(F)(F)F)cc1)n1cc(-c2ccccc2)nn1>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (78.5%) | `platinum` (19.4%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (61.2%) | `graphite_generic` (20.4%) | `graphite_rod` (11.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `ABSENT` (0.1%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (85.7%) | `platinum_generic` (14.3%) | `unknown_electrode` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (87.5%) | `ABSENT` (12.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (96.1%) | `NBu4` (2.8%) | `Li` (0.8%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (97.4%) | `PF6` (1.3%) | `ClO4` (0.7%) | ✗ |
| 试剂大类 | 103 | `water` | `water` (12.1%) | `ABSENT` (7.2%) | `o2_oxidant` (5.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `organic_neutral_cat` (0.1%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.0%) | `halogenated_aliphatic` (1.0%) | `polar_aprotic_amide` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (88%) | `ClCCl` (30%) | `O` (7%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (89%) | `O=O` (1%) | `CCN(CC)CC.F.F.F` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1003  yield=26.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #1)

```
C/C=C/c1ccccc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>C[C@@H]([C@H](O)c1ccccc1)n1ncc(-c2ccccc2)n1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_generic` (89.9%) | `carbon_felt` (7.5%) | `carbon_cloth` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.7%) | `stainless_steel` (7.0%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.0%) | `stainless_steel_generic` (2.9%) | `platinum_generic` (0.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (93.1%) | `divided` (6.8%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (71.9%) | `Li` (25.9%) | `NEt4` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (75.1%) | `BF4` (20.6%) | `molecular_no_ion` (2.3%) | ✗ |
| 试剂大类 | 103 | `imine` | `iodide_anion` (14.0%) | `as_solvent_polar_aprotic_sulfo` (11.4%) | `cf3_source` (4.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `ionic_organocat` (0.3%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (65.5%) | `halogenated_aliphatic` (29.8%) | `ketone` (1.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (51%) | `O` (21%) | `CC#N` (13%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC=1N=C(C)C=CC1=C` + `O` | `O` (24%) | `[Na+].[OH-]` (14%) | `[Li+].[O-][Cl+3]([` (11%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COC(=O)CC[C@@H]1C2` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1004  yield=26.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #2)

```
C/C=C/c1ccccc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>C[C@H]([C@H](O)c1ccccc1)n1ncc(-c2ccccc2)n1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_generic` (89.9%) | `carbon_felt` (7.5%) | `carbon_cloth` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.7%) | `stainless_steel` (7.0%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.0%) | `stainless_steel_generic` (2.9%) | `platinum_generic` (0.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (93.1%) | `divided` (6.8%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (71.9%) | `Li` (25.9%) | `NEt4` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (75.1%) | `BF4` (20.6%) | `molecular_no_ion` (2.3%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (14.0%) | `as_solvent_polar_aprotic_sulfo` (11.4%) | `cf3_source` (4.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `ionic_organocat` (0.3%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (65.5%) | `halogenated_aliphatic` (29.8%) | `ketone` (1.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (51%) | `O` (21%) | `CC#N` (13%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC=1N=C(C)C=CC1=C` + `O` | `O` (24%) | `[Na+].[OH-]` (14%) | `[Li+].[O-][Cl+3]([` (11%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COC(=O)CC[C@@H]1C2` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1005  yield=24.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #3)

```
C/C=C\c1ccccc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>C[C@@H]([C@H](O)c1ccccc1)n1ncc(-c2ccccc2)n1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_generic` (89.9%) | `carbon_felt` (7.5%) | `carbon_cloth` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.7%) | `stainless_steel` (7.0%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.0%) | `stainless_steel_generic` (2.9%) | `platinum_generic` (0.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (93.1%) | `divided` (6.8%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (71.9%) | `Li` (25.9%) | `NEt4` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (75.1%) | `BF4` (20.6%) | `molecular_no_ion` (2.3%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (14.0%) | `as_solvent_polar_aprotic_sulfo` (11.4%) | `cf3_source` (4.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `ionic_organocat` (0.3%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (65.5%) | `halogenated_aliphatic` (29.8%) | `ketone` (1.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (51%) | `O` (21%) | `CC#N` (13%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `O` | `O` (24%) | `[Na+].[OH-]` (14%) | `[Li+].[O-][Cl+3]([` (11%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COC(=O)CC[C@@H]1C2` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1006  yield=24.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #4)

```
C/C=C\c1ccccc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>C[C@H]([C@H](O)c1ccccc1)n1ncc(-c2ccccc2)n1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_generic` (89.9%) | `carbon_felt` (7.5%) | `carbon_cloth` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.7%) | `stainless_steel` (7.0%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.0%) | `stainless_steel_generic` (2.9%) | `platinum_generic` (0.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (93.1%) | `divided` (6.8%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (71.9%) | `Li` (25.9%) | `NEt4` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (75.1%) | `BF4` (20.6%) | `molecular_no_ion` (2.3%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `iodide_anion` (14.0%) | `as_solvent_polar_aprotic_sulfo` (11.4%) | `cf3_source` (4.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `ionic_organocat` (0.3%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (65.5%) | `halogenated_aliphatic` (29.8%) | `ketone` (1.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (51%) | `O` (21%) | `CC#N` (13%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `O` | `O` (24%) | `[Na+].[OH-]` (14%) | `[Li+].[O-][Cl+3]([` (11%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COC(=O)CC[C@@H]1C2` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1007  yield=27.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #5)

```
C=C(c1ccccc1)c1ccccc1.COc1ccc(S(=O)(=O)n2cc(-c3ccccc3)nn2)cc1>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (62.0%) | `platinum` (29.8%) | `ABSENT` (7.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (77.2%) | `platinum_plate` (15.7%) | `unknown_electrode` (1.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.1%) | `ABSENT` (0.3%) | `carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (95.4%) | `platinum_generic` (4.4%) | `unknown_electrode` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (81.4%) | `undivided` (18.6%) | `flow` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (54.4%) | `K` (38.1%) | `Li` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `PF6` (45.4%) | `I` (18.0%) | `ClO4` (15.0%) | ✗ |
| 试剂大类 | 103 | `water` | `water` (21.0%) | `ABSENT` (14.8%) | `alkali_bicarbonate` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.5%) | `ketone` (8.3%) | `polar_aprotic_amide` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (75%) | `O` (62%) | `ClCCl` (31%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `O` (99%) | `C` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1008  yield=21.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #6)

```
C=C(c1ccccc1)c1ccccc1.Cc1ccc(S(=O)(=O)n2cc(-c3ccccc3)nn2)cc1>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (57.2%) | `platinum` (37.2%) | `ABSENT` (4.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (89.1%) | `graphite_rod` (6.5%) | `platinum_plate` (2.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `ABSENT` (0.1%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (97.1%) | `platinum_generic` (2.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.2%) | `ABSENT` (2.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (75.6%) | `ABSENT` (18.4%) | `Li` (2.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (38.2%) | `BF4` (23.4%) | `I` (13.4%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (14.8%) | `water` (9.6%) | `boron_lewis_acid` (3.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.7%) | `polar_aprotic_amide` (1.2%) | `halogenated_aliphatic` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (97%) | `ClCCl` (21%) | `O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #1009  yield=49.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #7)

```
CC(=O)O.C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>CC(=O)OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (97.4%) | `graphite_rod` (1.9%) | `graphite_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (69.6%) | `Li` (22.2%) | `K` (5.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (63.1%) | `molecular_no_ion` (25.2%) | `BF4` (4.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.9%) | `acid_anhydride` (2.4%) | `metal_oxide_oxidant` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `pyridine_organocat` (0.2%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.9%) | `halogenated_aliphatic` (0.9%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (94%) | `ClCCl` (5%) | `CC(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |

---

### Reaction #1010  yield=43.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #8)

```
C=C(c1ccccc1)c1ccccc1.CC(C)S(=O)(=O)n1cc(-c2ccccc2)nn1>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `ABSENT` (0.3%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (78.4%) | `graphite_rod` (11.9%) | `graphite_generic` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `platinum_generic` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (67.0%) | `ABSENT` (18.4%) | `NBu4` (9.0%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (53.5%) | `ABSENT` (29.5%) | `molecular_no_ion` (8.4%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (10.7%) | `water` (5.0%) | `alkali_bicarbonate` (2.6%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.1%) | `cyclic_ether` (0.3%) | `ketone` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (96%) | `O` (30%) | `ClCCl` (6%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1011  yield=54.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #9)

```
CS(=O)(=O)n1cc(-c2ccccc2)nn1.C=C(c1ccc(Cl)cc1)c1ccc(OC(C)(C)C(=O)C(C)C)cc1>>CC(C)C(=O)C(C)(C)Oc1ccc(C(O)(Cn2ncc(-c3cc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (1.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (97.3%) | `platinum_plate` (0.7%) | `graphite_generic` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.2%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.6%) | `Li` (10.8%) | `ABSENT` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (49.2%) | `BF4` (23.2%) | `I` (9.5%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (15.1%) | `boron_lewis_acid` (2.6%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (100.0%) | `halogenated_aliphatic` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (9%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1012  yield=60.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #10)

```
C=Cc1ccc(Cl)cc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>OC(Cn1ncc(-c2ccccc2)n1)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (91.4%) | `carbon_felt` (4.0%) | `graphite_generic` (2.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.5%) | `stainless_steel` (4.2%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `stainless_steel_generic` (0.0%) | `platinum_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.2%) | `Li` (6.5%) | `Na` (3.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (47.3%) | `I` (15.8%) | `carboxylate` (14.9%) | ✓ |
| 试剂大类 | 103 | `pyridine` | `boron_lewis_acid` (7.5%) | `ABSENT` (6.1%) | `water` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (91.1%) | `ketone` (5.0%) | `ABSENT` (1.7%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (97%) | `O` (15%) | `CCOCC` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `O` | `CCCC[N+](CCCC)(CCC` (36%) | `C[Si](C)(C)N=[N+]=` (12%) | `CC[Si](CC)CC` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1013  yield=58.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #11)

```
C=Cc1ccc(C)c(Cl)c1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>Cc1ccc(C(O)Cn2ncc(-c3ccccc3)n2)cc1Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_aluminum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (76.0%) | `carbon_felt` (9.2%) | `graphite_generic` (8.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `stainless_steel` (0.4%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `stainless_steel_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (69.0%) | `NBu4` (24.3%) | `K` (4.1%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (47.8%) | `ClO4` (38.9%) | `I` (6.7%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `ABSENT` (11.5%) | `boron_lewis_acid` (4.9%) | `water` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `ionic_organocat` (0.5%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.5%) | `ketone` (2.2%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (94%) | `O` (17%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `O` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `O.O.[K+].[K+].[O]=` (0%) | set ✓ / any ✓ |

---

### Reaction #1014  yield=57.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #12)

```
C=Cc1ccc(Cl)cc1Cl.c1ccc(-c2cc[nH]n2)cc1>>OC(Cn1ccc(-c2ccccc2)n1)c1ccc(Cl)cc1Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_generic` (99.5%) | `graphite_felt` (0.1%) | `carbon_felt` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.1%) | `stainless_steel` (4.2%) | `nickel` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (55.6%) | `platinum_generic` (19.6%) | `stainless_steel_generic` (16.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (39.1%) | `Li` (33.2%) | `NBu4` (11.4%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (82.1%) | `BF4` (5.6%) | `Br` (4.0%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (10.6%) | `boron_lewis_acid` (2.9%) | `bromide_anion` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (54.2%) | `organic_neutral_cat` (27.9%) | `Mn_complex` (10.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (72.4%) | `polar_aprotic_sulfoxide` (10.7%) | `cyclic_ether` (5.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (97%) | `O` (88%) | `CC(=O)O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (68%) | `__OTHER__` (1%) | `[Fe+2].c1cc[cH-]c1` (1%) | set ✓ / any ✓ |

---

### Reaction #1015  yield=57.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #13)

```
C=C(c1ccccc1)c1ccccc1.CCc1ccc(-c2cn(S(C)(=O)=O)nn2)cc1>>CCc1ccc(-c2cnn(CC(N)(c3ccccc3)c3ccccc3)n2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (85.2%) | `carbon_felt` (7.0%) | `graphite_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_wire` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.0%) | `Li` (12.4%) | `K` (6.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (51.3%) | `molecular_no_ion` (35.3%) | `BF4` (5.8%) | ✗ |
| 试剂大类 | 103 | `ammonium_salt` | `ABSENT` (17.6%) | `boron_lewis_acid` (5.3%) | `carboxylic_acid` (3.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `polar_aprotic_sulfoxide` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (1%) | `O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[NH4+].[OH-]` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)NC1CC2(CCCCC` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1016  yield=51.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #14)

```
C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>NC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (89.4%) | `graphite_rod` (8.4%) | `graphite_plate` (1.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.9%) | `ABSENT` (2.0%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.1%) | `NEt4` (3.1%) | `Li` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (30.5%) | `ClO4` (24.4%) | `Br` (12.3%) | ✗ |
| 试剂大类 | 103 | `ammonium_salt` | `ABSENT` (9.1%) | `boron_lewis_acid` (3.5%) | `azide_source` (3.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.4%) | `polar_aprotic_sulfoxide` (1.6%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `ClCCl` (24%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[NH4+].[OH-]` | `__ABSENT__` (99%) | `CCN(CC)CC.F.F.F` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1017  yield=57.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #15)

```
CC(=O)O.C=C(c1ccccc1)c1ccc(OC)cc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>COc1ccc(C(Cn2ncc(-c3ccccc3)n2)(OC(C)=O)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (97.1%) | `graphite_rod` (1.9%) | `graphite_plate` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (73.3%) | `K` (14.3%) | `ABSENT` (5.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (48.0%) | `ClO4` (22.0%) | `I` (8.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (33.4%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `pyridine_organocat` (0.2%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.3%) | `ABSENT` (0.3%) | `halogenated_aliphatic` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (2%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |

---

### Reaction #1018  yield=68.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #16)

```
C=Cc1ccc(Br)cc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>OC(Cn1ncc(-c2ccccc2)n1)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (91.4%) | `graphite_generic` (4.5%) | `graphite_plate` (1.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.5%) | `carbon` (0.4%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.6%) | `Li` (6.8%) | `K` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (50.3%) | `molecular_no_ion` (22.7%) | `I` (13.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `ABSENT` (9.5%) | `azide_source` (3.8%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ionic_organocat` (0.1%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.2%) | `ABSENT` (4.3%) | `ketone` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (6%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `O` | `__ABSENT__` (100%) | `O=O` (4%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1019  yield=68.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #17)

```
C=Cc1ccc(Cl)cc1Cl.c1ccc(-c2cn[nH]n2)cc1>>OC(Cn1ncc(-c2ccccc2)n1)c1ccc(Cl)cc1Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (92.2%) | `platinum_plate` (2.8%) | `graphite_generic` (1.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `nickel` (0.6%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.2%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (38.3%) | `Li` (28.6%) | `ABSENT` (15.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (87.8%) | `carboxylate` (6.3%) | `ABSENT` (3.5%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (34.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.3%) | `Mn_complex` (0.9%) | `pyridine_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (92.3%) | `ketone` (4.8%) | `polar_protic_acid` (0.5%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `O` (14%) | `ClCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O` + `CC(=O)[O-].CCCC[N+` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1020  yield=69.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #18)

```
C=C(c1ccccc1)c1ccccc1.c1ccc(-c2nnn[nH]2)cc1>>OC(Cn1nnnc1-c1ccccc1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.1%) | `platinum` (9.9%) | `sacrificial_magnesium` (1.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (93.0%) | `graphite_rod` (5.2%) | `platinum_plate` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.2%) | `carbon` (1.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.7%) | `platinum_generic` (0.2%) | `carbon_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.3%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (76.6%) | `ABSENT` (22.2%) | `NEt4` (0.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `PF6` (75.0%) | `ABSENT` (18.1%) | `ClO4` (4.2%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (5.4%) | `azide_source` (3.4%) | `ketone` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.2%) | `Cu_complex` (1.6%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (74.2%) | `polar_aprotic_sulfoxide` (13.3%) | `polar_aprotic_amide` (6.9%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (96%) | `O` (22%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O` | `CC[Si](CC)CC` (47%) | `__ABSENT__` (45%) | `O=O` (30%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (88%) | `__OTHER__` (6%) | `c1ccncc1` (5%) | set ✓ / any ✓ |

---

### Reaction #1021  yield=69.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #19)

```
C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2ccccc2Br)nn1>>OC(Cn1ncc(-c2ccccc2Br)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (82.6%) | `graphite_plate` (16.4%) | `graphite_generic` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.0%) | `Li` (6.7%) | `K` (5.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (72.6%) | `carboxylate` (8.0%) | `BF4` (5.9%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (13.6%) | `boron_lewis_acid` (2.6%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.3%) | `halogenated_aliphatic` (0.4%) | `polar_aprotic_sulfoxide` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (72%) | `ClCCl` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=C([O-])O.[Na+]` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1022  yield=65.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #20)

```
C=C(c1ccccc1)c1ccccc1.Cc1ccc(-c2cn(S(C)(=O)=O)nn2)c(C)c1>>Cc1ccc(-c2cnn(CC(O)(c3ccccc3)c3ccccc3)n2)c(C)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (77.8%) | `graphite_plate` (19.2%) | `carbon_felt` (1.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.2%) | `carbon` (0.8%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (71.8%) | `Li` (23.9%) | `K` (3.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (81.7%) | `molecular_no_ion` (6.1%) | `BF4` (5.5%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (19.5%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `polar_aprotic_sulfoxide` (0.1%) | `halogenated_aliphatic` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (74%) | `ClCCl` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.[K+].[K+].[O]=` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #1023  yield=61.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #21)

```
C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2ccc3ccccc3c2)nn1>>OC(Cn1ncc(-c2ccc3ccccc3c2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (97.7%) | `graphite_plate` (2.0%) | `graphite_rod` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.0%) | `Li` (12.3%) | `K` (3.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (68.6%) | `BF4` (10.1%) | `carboxylate` (8.8%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (12.9%) | `boron_lewis_acid` (8.4%) | `azide_source` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `Pt_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.4%) | `halogenated_aliphatic` (0.2%) | `polar_aprotic_sulfoxide` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (33%) | `O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.[K+].[K+].[O]=` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1024  yield=68.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #22)

```
C=C1CCCc2ccccc21.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>OC1(Cn2ncc(-c3ccccc3)n2)CCCc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_plate` (48.9%) | `carbon_rod` (45.0%) | `platinum_plate` (1.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.2%) | `carbon` (0.5%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `nickel_plate` (0.0%) | `platinum_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (47.0%) | `NBu4` (41.5%) | `Li` (7.6%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (40.7%) | `ClO4` (40.1%) | `molecular_no_ion` (10.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (15.7%) | `boron_lewis_acid` (10.4%) | `cyanide` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (83.5%) | `ABSENT` (11.0%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (91%) | `O` (35%) | `ClCCl` (16%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.[K+].[K+].[O]=` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1025  yield=78.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #23)

```
C=Cc1ccccc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>OC(Cn1ncc(-c2ccccc2)n1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (97.0%) | `graphite_rod` (1.7%) | `carbon_felt` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `stainless_steel` (0.4%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `stainless_steel_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (71.0%) | `K` (17.9%) | `Li` (4.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `I` (31.3%) | `ClO4` (17.9%) | `carboxylate` (17.2%) | ✓ |
| 试剂大类 | 103 | `pyridine` | `ABSENT` (10.5%) | `water` (8.4%) | `cyanide` (4.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `ionic_organocat` (1.1%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (65.2%) | `ABSENT` (25.3%) | `ketone` (3.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (67%) | `C[N+](=O)[O-]` (29%) | `C1COCCO1` (22%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `O` | `__ABSENT__` (91%) | `O=O` (49%) | `O` (18%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (57%) | `__ABSENT__` (50%) | `__OTHER__` (49%) | set ✗ / any ✓ |

---

### Reaction #1026  yield=77.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #24)

```
C=C(C)c1ccccc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>CC(O)(Cn1ncc(-c2ccccc2)n1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (88.4%) | `carbon_cloth` (4.9%) | `carbon_plate` (3.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `stainless_steel` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `stainless_steel_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (64.0%) | `NBu4` (32.6%) | `Li` (2.5%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (26.7%) | `Br` (19.4%) | `BF4` (14.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (12.4%) | `carboxylic_acid` (9.8%) | `boron_lewis_acid` (4.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.1%) | `polar_aprotic_sulfoxide` (3.0%) | `cyclic_ether` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `O` (92%) | `ClCCl` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (98%) | `CC(=O)O` (2%) | `O=C(O)C(F)(F)F` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1027  yield=79.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #25)

```
C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2cc(F)c(F)c(F)c2)nn1>>OC(Cn1ncc(-c2cc(F)c(F)c(F)c2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (99.3%) | `carbon_cloth` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (56.9%) | `NEt4` (15.2%) | `Li` (9.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (30.6%) | `BF4` (14.4%) | `carboxylate` (13.8%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (7.5%) | `carboxylic_acid` (3.9%) | `o2_oxidant` (3.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.8%) | `ABSENT` (0.1%) | `halogenated_aliphatic` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (43%) | `O` (7%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O=C([O-])O.[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1028  yield=79.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #26)

```
C=C(c1ccccc1)c1ccccc1.CC(C)(C)c1ccc(-c2cn(S(C)(=O)=O)nn2)cc1>>CC(C)(C)c1ccc(-c2cnn(CC(O)(c3ccccc3)c3ccccc3)n2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `platinum` (2.0%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (96.1%) | `graphite_plate` (2.1%) | `platinum_plate` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (43.6%) | `K` (42.7%) | `NBu4` (11.4%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (46.3%) | `molecular_no_ion` (43.4%) | `carboxylate` (7.2%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (11.7%) | `water` (4.8%) | `carboxylic_acid` (4.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.8%) | `ABSENT` (0.1%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (6%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1029  yield=78.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #27)

```
C=C(c1ccccc1)c1ccccc1.c1ccc(-c2cn[nH]n2)cc1>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (86.7%) | `platinum` (13.0%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (83.3%) | `graphite_rod` (11.7%) | `platinum_plate` (2.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `ABSENT` (0.0%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (97.5%) | `platinum_generic` (2.5%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.2%) | `Li` (5.5%) | `NBu4` (3.7%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (95.2%) | `ClO4` (1.4%) | `PF6` (1.4%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (28.3%) | `alkali_bicarbonate` (2.3%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `polar_aprotic_sulfoxide` (0.3%) | `polar_aprotic_amide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (95%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=C([O-])O.[Na+]` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1030  yield=77.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #28)

```
C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2ccc(C(F)(F)F)cc2)nn1>>OC(Cn1ncc(-c2ccc(C(F)(F)F)cc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (99.5%) | `graphite_plate` (0.4%) | `carbon_cloth` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `carbon_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.0%) | `Li` (11.0%) | `K` (2.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (56.6%) | `carboxylate` (24.4%) | `molecular_no_ion` (10.5%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (12.5%) | `boron_lewis_acid` (3.9%) | `carboxylic_acid` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.4%) | `halogenated_aliphatic` (2.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (96%) | `ClCCl` (61%) | `O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1031  yield=76.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #29)

```
C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2cccc(F)c2)nn1>>OC(Cn1ncc(-c2cccc(F)c2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (95.2%) | `graphite_plate` (3.8%) | `graphite_generic` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.5%) | `Li` (14.0%) | `K` (2.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (77.2%) | `carboxylate` (8.0%) | `BF4` (6.2%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (13.4%) | `boron_lewis_acid` (2.8%) | `azide_source` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.6%) | `halogenated_aliphatic` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (97%) | `O` (42%) | `ClCCl` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1032  yield=76.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #30)

```
C=C(c1ccccc1)c1ccccc1.Brc1c[nH]nc1-c1ccccc1>>OC(Cn1cc(Br)c(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.4%) | `platinum` (4.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (90.3%) | `graphite_rod` (8.2%) | `carbon_felt` (1.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.1%) | `carbon` (0.6%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (92.1%) | `platinum_generic` (7.2%) | `carbon_felt` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (60.6%) | `NBu4` (32.2%) | `NEt4` (5.9%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (89.2%) | `PF6` (5.4%) | `BF4` (4.3%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (12.1%) | `o2_oxidant` (3.1%) | `boron_lewis_acid` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `ketone` (0.1%) | `cyclic_ether` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (8%) | `CC(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1033  yield=76.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #31)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)c1ccc(-c2cn(S(C)(=O)=O)nn2)cc1>>COC(=O)c1ccc(-c2cnn(CC(O)(c3ccccc3)c3ccccc3)n2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (87.9%) | `platinum_plate` (3.0%) | `graphite_plate` (2.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.6%) | `Li` (33.7%) | `K` (10.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (54.1%) | `molecular_no_ion` (36.4%) | `PF6` (2.3%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (11.9%) | `carboxylic_acid` (4.4%) | `inorganic_simple` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.0%) | `ABSENT` (0.4%) | `ketone` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (94%) | `CCOCC` (18%) | `O` (10%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1034  yield=72.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #32)

```
C=C(c1ccccc1)c1ccccc1.Brc1ccc2[nH]ncc2c1>>OC(Cn1ncc2cc(Br)ccc21)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (47.9%) | `carbon_rod` (44.0%) | `carbon_felt` (4.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.5%) | `carbon` (1.5%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.7%) | `platinum_generic` (0.2%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (71.3%) | `ABSENT` (13.3%) | `NBu4` (10.8%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (38.5%) | `ABSENT` (22.7%) | `Cl` (18.6%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (11.9%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_sulfoxide` (0.0%) | `cyclic_ether` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (92%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=O` (1%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #1035  yield=71.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #33)

```
C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2cc(F)cc(F)c2)nn1>>OC(Cn1ncc(-c2cc(F)cc(F)c2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `platinum` (3.6%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (85.5%) | `graphite_plate` (11.1%) | `platinum_plate` (1.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (54.8%) | `K` (23.2%) | `Li` (15.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (36.1%) | `ClO4` (18.2%) | `molecular_no_ion` (18.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (16.7%) | `boron_lewis_acid` (3.3%) | `carboxylic_acid` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Pt_complex` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.6%) | `halogenated_aliphatic` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (47%) | `ClCCl` (31%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1036  yield=88.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #34)

```
C=C(c1ccccc1)C1CC1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)C1CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (78.6%) | `graphite_generic` (19.5%) | `carbon_felt` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `stainless_steel` (0.0%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `stainless_steel_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (41.8%) | `NEt4` (38.1%) | `Li` (19.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (92.3%) | `BF4` (5.3%) | `I` (0.8%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (17.4%) | `boron_lewis_acid` (6.4%) | `carboxylic_acid` (5.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.2%) | `Mn_complex` (1.5%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.1%) | `halogenated_aliphatic` (3.9%) | `ketone` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (94%) | `ClCCl` (30%) | `O` (20%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1037  yield=89.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #35)

```
CCO.C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>CCOC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (75.7%) | `graphite_rod` (22.0%) | `graphite_plate` (1.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.4%) | `K` (2.0%) | `Li` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (49.1%) | `ClO4` (14.5%) | `BF4` (14.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.8%) | `azide_source` (7.1%) | `boron_lewis_acid` (3.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.0%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (61.5%) | `polar_aprotic_nitrile` (37.8%) | `halogenated_aliphatic` (0.5%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `__ABSENT__` (91%) | `CC#N` (1%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1038  yield=89.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #36)

```
C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `platinum` (1.7%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (98.9%) | `graphite_rod` (0.4%) | `graphite_plate` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `ABSENT` (0.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (65.7%) | `K` (15.2%) | `Li` (13.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (44.3%) | `carboxylate` (12.6%) | `molecular_no_ion` (10.6%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (9.7%) | `boron_lewis_acid` (6.2%) | `water` (4.6%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.7%) | `halogenated_aliphatic` (0.4%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (98%) | `ClCCl` (41%) | `O` (30%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[NH4+].[OH-]` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1039  yield=88.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #37)

```
C=C(c1ccccc1)c1ccccc1.Cc1ccc(-c2cn(S(C)(=O)=O)nn2)cc1>>Cc1ccc(-c2cnn(CC(O)(c3ccccc3)c3ccccc3)n2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `platinum` (1.7%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (91.0%) | `graphite_plate` (7.1%) | `platinum_plate` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (67.6%) | `Li` (26.1%) | `K` (5.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (65.7%) | `molecular_no_ion` (18.3%) | `BF4` (7.2%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (13.8%) | `boron_lewis_acid` (3.3%) | `carboxylic_acid` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.6%) | `polar_aprotic_sulfoxide` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (53%) | `ClCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #1040  yield=88.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #38)

```
C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>FC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (98.6%) | `graphite_plate` (1.1%) | `graphite_rod` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.3%) | `NEt4` (6.6%) | `Li` (1.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (54.4%) | `F` (28.9%) | `ClO4` (9.8%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `boron_lewis_acid` (8.3%) | `inorganic_simple` (5.9%) | `ABSENT` (5.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.8%) | `halogenated_aliphatic` (5.2%) | `polar_aprotic_sulfoxide` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (98%) | `O` (61%) | `ClCCl` (28%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[NH4+].[OH-]` | `CCCC[N+](CCCC)(CCC` (20%) | `CCN(CC)CC.F.F.F` (2%) | `[Pt]` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.[K+].[K+].[O]=` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1041  yield=87.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #39)

```
C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2ccc(Br)cc2)nn1>>OC(Cn1ncc(-c2ccc(Br)cc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (88.6%) | `graphite_plate` (7.2%) | `carbon_cloth` (2.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.6%) | `K` (11.4%) | `Li` (9.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (67.5%) | `carboxylate` (10.0%) | `BF4` (5.9%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (12.5%) | `carboxylic_acid` (2.6%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `ABSENT` (0.2%) | `halogenated_aliphatic` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (39%) | `ClCCl` (20%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1042  yield=87.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #40)

```
C=C(c1ccccc1)c1ccccc1.c1ccc(-c2cc[nH]n2)cc1>>OC(Cn1ccc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (48.1%) | `carbon` (46.3%) | `sacrificial_magnesium` (5.1%) | ✓ |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_generic` (44.9%) | `carbon_rod` (32.0%) | `platinum_generic` (17.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.8%) | `carbon` (0.6%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (65.1%) | `platinum_plate` (24.8%) | `unknown_electrode` (4.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (44.6%) | `Li` (44.1%) | `NEt4` (10.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (83.1%) | `BF4` (10.1%) | `PF6` (5.2%) | ✗ |
| 试剂大类 | 103 | `water` | `boron_lewis_acid` (24.7%) | `iodide_anion` (5.1%) | `ABSENT` (4.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `Mn_complex` (0.5%) | `organic_neutral_cat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (83.2%) | `polar_aprotic_amide` (10.9%) | `cyclic_ether` (2.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (96%) | `O` (93%) | `CN(C)C=O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `[Pt]` (35%) | `CCCC[N+](CCCC)(CCC` (32%) | `CC[Si](CC)CC` (14%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `Brc1ccc(N(c2ccc(Br` (2%) | `[Pt]` (2%) | set ✓ / any ✓ |

---

### Reaction #1043  yield=86.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #41)

```
C=C(c1ccccc1)c1ccccc1.Brc1ccc(-c2cc[nH]n2)cc1>>OC(Cn1ccc(-c2ccc(Br)cc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (85.7%) | `platinum` (13.0%) | `sacrificial_magnesium` (1.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_generic` (38.7%) | `carbon_rod` (33.6%) | `platinum_generic` (6.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (75.9%) | `platinum_generic` (23.5%) | `platinum_wire` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.0%) | `Li` (14.9%) | `NEt4` (2.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (82.8%) | `BF4` (13.0%) | `PF6` (2.0%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (9.3%) | `boron_lewis_acid` (5.4%) | `water` (4.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `organic_neutral_cat` (0.1%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.2%) | `polar_aprotic_amide` (0.3%) | `cyclic_ether` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (54%) | `CCOCC` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br][Mn][Br]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1044  yield=86.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #42)

```
C=C(c1ccccc1)c1ccccc1.CCOC(=O)c1ccc(-c2cn(S(C)(=O)=O)nn2)cc1>>CCOC(=O)c1ccc(-c2cnn(CC(O)(c3ccccc3)c3ccccc3)n2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_plate` (57.8%) | `carbon_rod` (28.9%) | `carbon_felt` (6.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (54.7%) | `Li` (25.9%) | `K` (16.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (63.3%) | `molecular_no_ion` (27.8%) | `carboxylate` (3.2%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (8.0%) | `carboxylic_acid` (7.4%) | `azide_source` (4.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.1%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `ABSENT` (0.4%) | `polar_aprotic_sulfoxide` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (37%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O.O.O.O.O.O.O.O.O.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1045  yield=83.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #43)

```
CO.C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2ccccc2)nn1>>COC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (91.7%) | `graphite_rod` (7.9%) | `graphite_plate` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.9%) | `ABSENT` (0.5%) | `NH4` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (46.8%) | `I` (25.5%) | `ClO4` (11.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (9.2%) | `ABSENT` (6.3%) | `o2_oxidant` (4.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.0%) | `triarylamine_radical_cat` (1.2%) | `organic_neutral_cat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (81.5%) | `polar_aprotic_nitrile` (18.2%) | `cyclic_ether` (0.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `__ABSENT__` (92%) | `CC#N` (6%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (76%) | `__ABSENT__` (9%) | `O=S([O-])O.[Na+]` (5%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC[N+](CC)(CC)CC.F` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1046  yield=82.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #44)

```
C=C(c1ccccc1)c1ccccc1.COc1ccc(-c2cn(S(C)(=O)=O)nn2)cc1>>COc1ccc(-c2cnn(CC(O)(c3ccccc3)c3ccccc3)n2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (99.0%) | `graphite_plate` (0.5%) | `platinum_plate` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `carbon_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (58.6%) | `Li` (20.3%) | `K` (16.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (43.1%) | `molecular_no_ion` (34.5%) | `carboxylate` (6.3%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (15.0%) | `boron_lewis_acid` (6.6%) | `water` (2.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ionic_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.9%) | `halogenated_aliphatic` (0.3%) | `ketone` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (84%) | `ClCCl` (7%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #1047  yield=82.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #45)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)c1ccc(-c2cn(S(C)(=O)=O)nn2)cc1>>COC(=O)c1ccc(-c2cnn(CC(F)(c3ccccc3)c3ccccc3)n2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `sacrificial_aluminum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (92.1%) | `carbon_cloth` (2.4%) | `graphite_plate` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.7%) | `Li` (3.8%) | `NEt4` (1.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (48.2%) | `BF4` (23.8%) | `F` (13.8%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `ABSENT` (7.5%) | `inorganic_simple` (7.1%) | `boron_lewis_acid` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.3%) | `halogenated_aliphatic` (4.5%) | `ABSENT` (2.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (87%) | `CCOCC` (16%) | `O` (15%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `O.O.[K+].[K+].[O]=` (0%) | set ✓ / any ✓ |

---

### Reaction #1048  yield=81.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #46)

```
C=C(c1ccccc1)c1ccccc1.CCc1ccc(-c2cn(S(C)(=O)=O)nn2)cc1>>CCc1ccc(-c2cnn(CC(O)(c3ccccc3)c3ccccc3)n2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.0%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (97.0%) | `carbon_felt` (1.2%) | `graphite_plate` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_wire` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (33.8%) | `NBu4` (32.9%) | `Li` (32.0%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (67.0%) | `molecular_no_ion` (20.7%) | `carboxylate` (7.8%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (14.4%) | `boron_lewis_acid` (10.3%) | `water` (5.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `polar_aprotic_sulfoxide` (0.2%) | `ketone` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `O` (8%) | `ClCCl` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[NH4+].[OH-]` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1049  yield=81.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #47)

```
C=C(c1ccccc1)c1ccccc1.c1ccc(-c2cnn[nH]2)cc1>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.9%) | `platinum` (4.6%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (75.5%) | `graphite_rod` (20.4%) | `glassy_carbon` (1.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `ABSENT` (0.3%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (95.3%) | `platinum_generic` (4.0%) | `platinum_foil` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (92.1%) | `ABSENT` (7.6%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (94.3%) | `NBu4` (4.1%) | `K` (1.0%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (96.6%) | `Br` (1.5%) | `PF6` (0.8%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (8.6%) | `carboxylic_acid` (4.8%) | `iodide_anion` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `Mn_complex` (0.2%) | `Cu_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.5%) | `polar_aprotic_sulfoxide` (3.5%) | `polar_aprotic_amide` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `O` (98%) | `CC#N` (92%) | `CS(C)=O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (96%) | `CC(=O)O` (2%) | `O=C(O)C(F)(F)F` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1050  yield=90.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #48)

```
C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2cccc(Cl)c2)nn1>>OC(Cn1ncc(-c2cccc(Cl)c2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (98.4%) | `graphite_plate` (1.5%) | `platinum_plate` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `carbon_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.4%) | `Li` (4.0%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (48.1%) | `BF4` (26.3%) | `carboxylate` (7.0%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (13.6%) | `boron_lewis_acid` (3.3%) | `water` (2.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `halogenated_aliphatic` (0.2%) | `ketone` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (7%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1051  yield=91.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #49)

```
C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2ccccc2OC(F)(F)F)nn1>>OC(Cn1ncc(-c2ccccc2OC(F)(F)F)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `platinum` (2.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (82.3%) | `graphite_plate` (9.4%) | `platinum_plate` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `carbon_felt` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.5%) | `ABSENT` (10.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (74.4%) | `Li` (20.9%) | `NEt4` (2.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (84.8%) | `carboxylate` (5.3%) | `BF4` (4.9%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (13.6%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.0%) | `halogenated_aliphatic` (0.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (24%) | `ClCCl` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1052  yield=91.0%

**Source paper**: [`ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/2025_Chinese_Chemical_Letters_2025_36_9_110822.json) (反应 idx 在该 JSON 内 = #50)

```
C=C(c1ccccc1)c1ccccc1.CS(=O)(=O)n1cc(-c2ccc(-c3ccccc3)cc2)nn1>>OC(Cn1ncc(-c2ccc(-c3ccccc3)cc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `platinum` (1.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_rod` (98.2%) | `graphite_plate` (1.1%) | `platinum_plate` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (62.3%) | `Li` (22.9%) | `K` (13.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (49.2%) | `molecular_no_ion` (18.7%) | `carboxylate` (10.0%) | ✓ |
| 试剂大类 | 103 | `water` | `boron_lewis_acid` (12.0%) | `ABSENT` (8.2%) | `azide_source` (5.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.8%) | `ABSENT` (0.8%) | `halogenated_aliphatic` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `O` (44%) | `ClCCl` (18%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `CCCC[N+](CCCC)(CCC` (20%) | `__ABSENT__` (6%) | `[Pt]` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #1053  yield=13.0%

**Source paper**: [`ChinJChem/2025_Chinese_Journal_of_Chemistry_2025_43_5_491-500.json`](reactions_by_journal_alkene_ec_audited/ChinJChem/2025_Chinese_Journal_of_Chemistry_2025_43_5_491-500.json) (反应 idx 在该 JSON 内 = #0)

```
[F-][B+3]([F-])([F-])[CH-]1CCCC1.[K+].C=C(C)C(=O)n1c(-c2ccc(Cl)cc2)c(C)c2ccccc21>>Cc1c2n(c3ccccc13)C(=O)C(C)(CS(=O)(=…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (0.8%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (56.7%) | `graphite_generic` (24.1%) | `carbon_cloth` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (82.8%) | `platinum_generic` (16.7%) | `platinum_foil` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (46.7%) | `NBu4` (25.0%) | `Na` (11.9%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (53.0%) | `molecular_no_ion` (32.5%) | `carboxylate` (4.1%) | ✓ |
| 试剂大类 | 103 | `ammonium_salt` | `ABSENT` (29.5%) | `electrophilic_N_F` (2.1%) | `unparseable_text` (2.1%) | ✗ |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (89.4%) | `pyridine_organocat` (7.1%) | `organic_neutral_cat` (2.3%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.7%) | `polar_aprotic_amide` (0.6%) | `halogenated_aliphatic` (0.2%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (100%) | `O` (99%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S([O-])[N+]12CC[` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cn1cncc1-c1c(F)cnc` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✗ / any ✗ |

---

### Reaction #1054  yield=61.0%

**Source paper**: [`ChinJChem/2025_Chinese_Journal_of_Chemistry_2025_43_5_491-500.json`](reactions_by_journal_alkene_ec_audited/ChinJChem/2025_Chinese_Journal_of_Chemistry_2025_43_5_491-500.json) (反应 idx 在该 JSON 内 = #1)

```
[F-][B+3]([F-])([F-])[CH-]1CCCC1.[K+].C=CC(=O)N(Cc1ccccc1)C(=CC)c1ccc(Cl)cc1>>CC1=C(c2ccc(Cl)cc2)N(Cc2ccccc2)C(=O)C1C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_felt` (35.0%) | `carbon_felt` (25.6%) | `carbon_generic` (20.0%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (80.3%) | `stainless_steel` (19.4%) | `nickel` (0.2%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (99.1%) | `stainless_steel_generic` (0.9%) | `platinum_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.2%) | `ABSENT` (15.4%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.7%) | `ABSENT` (10.5%) | `Na` (1.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (55.5%) | `ABSENT` (16.3%) | `carboxylate` (13.2%) | ✓ |
| 试剂大类 | 103 | `ammonium_salt` | `alkali_carbonate` (9.3%) | `ABSENT` (6.6%) | `alkali_other_salt` (4.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (41.2%) | `ABSENT` (36.4%) | `pyridine_organocat` (15.6%) | ✓ |
| 溶剂大类 | 27 | `ABSENT` | `ketone` (45.8%) | `halogenated_aliphatic` (23.2%) | `polar_aprotic_nitrile` (11.3%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `OC(C(F)(F)F)C(F)(F` (2%) | `O` (1%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])[N+]12CC[` | `__ABSENT__` (31%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (88%) | `__ABSENT__` (2%) | `N#Cc1c(-n2c3ccccc3` (2%) | set ✗ / any ✓ |

---

### Reaction #1055  yield=61.0%

**Source paper**: [`China/China_CN119571341_A_2025-03-07.json`](reactions_by_journal_alkene_ec_audited/China/China_CN119571341_A_2025-03-07.json) (反应 idx 在该 JSON 内 = #0)

```
NC(=O)c1ccccc1.C=Cc1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc(C2CN=C(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.7%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (94.4%) | `carbon_generic` (3.4%) | `graphite_generic` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (73.3%) | `platinum` (25.6%) | `stainless_steel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (60.1%) | `nickel_generic` (34.2%) | `platinum_plate` (3.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (50.9%) | `NBu4` (49.0%) | `NEt4` (0.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `PF6` (73.8%) | `ABSENT` (24.3%) | `BF4` (0.9%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carboxylate` (39.2%) | `alkali_other_salt` (7.1%) | `ABSENT` (3.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.1%) | `Mn_complex` (0.4%) | `Cu_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (95.6%) | `polar_aprotic_nitrile` (3.2%) | `ABSENT` (0.4%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `ClCCCl` (99%) | `CCOC(C)=O` (98%) | `ClCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClCCCl` + `CCOC(C)=O` | `CC(=O)[O-].[Na+]` (71%) | `ClCCCl` (27%) | `CCOC(C)=O` (22%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1056  yield=65.0%

**Source paper**: [`China/China_CN120231068_A_2025-07-01.json`](reactions_by_journal_alkene_ec_audited/China/China_CN120231068_A_2025-07-01.json) (反应 idx 在该 JSON 内 = #0)

```
CCO.CCOC(=O)CC(=O)OCC.C=Cc1ccc(OC)cc1>>CCOC(=O)C(CC(OCC)c1ccc(OC)cc1)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (27.9%) | `carbon_rod` (27.4%) | `carbon_felt` (19.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.9%) | `carbon` (6.9%) | `stainless_steel` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.0%) | `platinum_wire` (0.2%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.4%) | `ABSENT` (0.8%) | `divided` (0.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (65.1%) | `NBu4` (20.6%) | `Li` (12.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (61.3%) | `PF6` (20.5%) | `molecular_no_ion` (9.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (7.7%) | `water` (5.9%) | `alkali_carbonate` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (84.7%) | `Ir_complex` (6.6%) | `thianthrene_phenothiazine_cat` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (52.5%) | `ketone` (29.7%) | `polar_protic_alcohol` (4.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `CC#N` (85%) | `OCC(F)(F)F` (1%) | `CC(C)=O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `O=P([O-])([O-])O.[` | `__ABSENT__` (99%) | `O=C([O-])[O-].[K+]` (1%) | `O` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1057  yield=62.0%

**Source paper**: [`China/China_CN120231068_A_2025-07-01.json`](reactions_by_journal_alkene_ec_audited/China/China_CN120231068_A_2025-07-01.json) (反应 idx 在该 JSON 内 = #1)

```
CO.CCOC(=O)CC(=O)OCC.C=Cc1cc2c(cc1Br)OCO2>>CCOC(=O)C(CC(OC)c1cc2c(cc1Br)OCO2)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `sacrificial_magnesium` (0.3%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (32.1%) | `carbon_cloth` (27.3%) | `reticulated_vitreous_carbon` (21.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.9%) | `carbon` (9.4%) | `nickel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.0%) | `platinum_generic` (1.0%) | `platinum_wire` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (96.4%) | `ABSENT` (2.6%) | `Li` (0.8%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (77.6%) | `BF4` (7.3%) | `ClO4` (6.4%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ammonium_salt` (9.6%) | `ABSENT` (9.4%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (95.6%) | `pyridine_organocat` (1.9%) | `Ir_complex` (1.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (65.5%) | `polar_aprotic_nitrile` (15.3%) | `ketone` (15.2%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `C1CCOC1` | `__ABSENT__` (100%) | `CC(C)=O` (0%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `O=P([O-])([O-])O.[` | `O=C([O-])[O-].[K+]` (13%) | `CCCC[N+](CCCC)(CCC` (13%) | `CCCC[N+](CCCC)(CCC` (4%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #1058  yield=82.0%

**Source paper**: [`China/China_CN120575190_A_2025-09-02.json`](reactions_by_journal_alkene_ec_audited/China/China_CN120575190_A_2025-09-02.json) (反应 idx 在该 JSON 内 = #0)

```
O=C=O.C=CCC(CN)(c1ccccc1)c1ccccc1>>O=C1OCC2CC(c3ccccc3)(c3ccccc3)CN12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `ABSENT` (53.0%) | `platinum` (30.4%) | `carbon` (8.7%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (27.1%) | `unknown_electrode` (24.9%) | `ABSENT` (8.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `ABSENT` (57.9%) | `platinum` (21.7%) | `nickel` (15.0%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `unknown_electrode` (25.5%) | `platinum_generic` (23.3%) | `ABSENT` (16.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NH4` | `NBu4` (92.9%) | `Li` (2.7%) | `ABSENT` (2.0%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (51.1%) | `I` (20.1%) | `ClO4` (11.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `silane_other` (7.5%) | `hydrosilane` (3.5%) | `alkali_carbonate` (3.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (51.4%) | `ABSENT` (38.0%) | `Ni_complex` (1.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (55.1%) | `polar_protic_alcohol` (16.7%) | `polar_aprotic_nitrile` (15.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `O` (73%) | `CO` (62%) | `CN(C)C=O` (19%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `c1ccc([SiH2]c2cccc` (27%) | `Cl` (25%) | `CC(=O)[O-].[Na+]` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `CC(C)(C)c1cc2c(c(C` (86%) | `CC1[CH-]C(C)=[O]->` (2%) | `__ABSENT__` (2%) | set ✗ / any ✓ |

---

### Reaction #1059  yield=55.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `BnNMe3` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✗ |
| 电解质 anion | 26 | `Cl` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1060  yield=73.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1061  yield=45.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1062  yield=45.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1063  yield=57.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1064  yield=61.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1065  yield=45.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1066  yield=39.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1067  yield=50.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1068  yield=40.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1069  yield=31.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1070  yield=38.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1071  yield=42.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1072  yield=46.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1073  yield=30.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1074  yield=63.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1075  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1076  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1077  yield=54.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1078  yield=30.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1079  yield=52.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1080  yield=50.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1081  yield=45.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1082  yield=62.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1083  yield=73.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1084  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1085  yield=38.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1086  yield=55.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1087  yield=42.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1088  yield=35.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_aluminum` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1089  yield=31.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1090  yield=25.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1091  yield=64.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1092  yield=64.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1093  yield=53.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1094  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1095  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1096  yield=40.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1097  yield=55.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ammonium_salt` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1098  yield=57.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1099  yield=45.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1100  yield=45.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1101  yield=46.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1102  yield=55.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1103  yield=39.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1104  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)=CCCOc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC(C)(c1ccc(C#N)cc1)C1CCOc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.7%) | `sacrificial_zinc` (0.9%) | `sacrificial_magnesium` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `graphite_generic` (56.6%) | `carbon_felt` (10.0%) | `unknown_electrode` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (71.8%) | `carbon` (22.1%) | `ABSENT` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `unknown_electrode` (29.6%) | `platinum_generic` (23.5%) | `platinum_plate` (17.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.8%) | `ABSENT` (21.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.7%) | `NEt4` (20.1%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (50.6%) | `BF4` (30.5%) | `ABSENT` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `Fe_complex` (4.4%) | `Ni_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (64.7%) | `polar_aprotic_amide` (10.0%) | `polar_protic_alcohol` (8.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `C1CCOC1` + `ClCCCl` | `CC#N` (89%) | `CN(C)C=O` (6%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #1105  yield=31.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1106  yield=20.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1107  yield=21.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_aluminum` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1108  yield=38.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✗ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1109  yield=15.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1110  yield=5.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1111  yield=35.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1112  yield=21.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1113  yield=34.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1114  yield=36.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1115  yield=39.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1116  yield=37.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1117  yield=35.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1118  yield=31.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1119  yield=46.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1120  yield=36.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1121  yield=23.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1122  yield=29.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `OTs` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1123  yield=36.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1124  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NMe4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✗ |
| 电解质 anion | 26 | `F` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1125  yield=44.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `BnNMe3` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✗ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1126  yield=30.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NMe4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1127  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1128  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1129  yield=19.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1130  yield=34.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1131  yield=35.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1132  yield=25.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1133  yield=5.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1134  yield=31.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1135  yield=30.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `Br` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1136  yield=35.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1137  yield=25.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1138  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500222_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)COc1ccccc1I.N#Cc1ccc(C#N)cc1>>CC1(Cc2ccc(C#N)cc2)COc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (79.8%) | `sacrificial_zinc` (9.2%) | `platinum` (8.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `platinum_generic` (23.7%) | `carbon_generic` (15.8%) | `carbon_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (61.4%) | `carbon` (34.2%) | `ABSENT` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (46.4%) | `carbon_generic` (25.7%) | `platinum_plate` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.1%) | `NBu4` (32.5%) | `Li` (4.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.7%) | `Cl` (9.4%) | `BF4` (9.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.5%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (82.9%) | `polar_aprotic_sulfoxide` (12.1%) | `halogenated_aliphatic` (1.7%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CS(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1139  yield=47.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_23_e202500222.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_23_e202500222.json) (反应 idx 在该 JSON 内 = #0)

```
N#Cc1ccc(C#N)cc1.C=CCOc1ccccc1I>>N#Cc1ccc(CC2COc3ccccc32)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (97.2%) | `platinum` (0.9%) | `sacrificial_zinc` (0.6%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_plate` | `carbon_generic` (28.0%) | `graphite_generic` (14.2%) | `glassy_carbon` (14.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `stainless_steel` (50.9%) | `nickel` (19.8%) | `carbon` (16.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `nickel_generic` (57.0%) | `stainless_steel_generic` (27.2%) | `nickel_foam` (8.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (70.9%) | `ABSENT` (23.0%) | `K` (4.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ABSENT` (39.9%) | `PF6` (24.3%) | `BF4` (15.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (5.3%) | `amide` (4.5%) | `primary_amine` (3.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (36.2%) | `pyridine_organocat` (25.7%) | `ferrocene_mediator` (13.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (66.8%) | `polar_aprotic_nitrile` (10.2%) | `polar_aprotic_sulfoxide` (8.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (62%) | `CO` (18%) | `CN(C)C=O` (10%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `O=C(O)O.[K]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1140  yield=55.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_23_e202500222.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_23_e202500222.json) (反应 idx 在该 JSON 内 = #1)

```
N#Cc1ccc(C#N)cc1.C=CCCOc1ccccc1I>>N#Cc1ccc(CC2CCOc3ccccc32)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (86.4%) | `sacrificial_zinc` (7.1%) | `sacrificial_magnesium` (4.5%) | ✓ |
| 阳极 (细类) | 43 | `magnesium_plate` | `graphite_generic` (28.3%) | `glassy_carbon` (19.6%) | `zinc_plate` (13.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (92.4%) | `platinum` (5.0%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `graphite_rod` (39.0%) | `carbon_generic` (13.2%) | `graphite_generic` (12.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.0%) | `K` (0.3%) | `BnNMe3` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `PF6` (67.6%) | `BF4` (19.0%) | `Br` (4.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (6.5%) | `primary_amine` (3.9%) | `o2_oxidant` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.2%) | `pyridine_organocat` (4.3%) | `Fe_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (36.5%) | `polar_aprotic_amide` (21.7%) | `polar_protic_alcohol` (16.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (90%) | `CN(C)C=O` (5%) | `CO` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1141  yield=52.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_23_e202500222.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_23_e202500222.json) (反应 idx 在该 JSON 内 = #2)

```
N#Cc1ccc(C#N)cc1.C=CCCOc1ccc(F)cc1I>>N#Cc1ccc(CC2CCOc3ccc(F)cc32)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (49.0%) | `sacrificial_zinc` (31.5%) | `platinum` (13.5%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_plate` | `graphite_generic` (47.0%) | `zinc_plate` (20.7%) | `platinum_generic` (16.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (83.7%) | `platinum` (11.1%) | `stainless_steel` (2.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `graphite_generic` (36.3%) | `reticulated_vitreous_carbon` (15.1%) | `carbon_felt` (14.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.7%) | `divided` (3.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `protonated_amine` (4.1%) | `NEt4` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `PF6` (34.3%) | `BF4` (15.6%) | `fluoride_complex` (13.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.3%) | `o2_oxidant` (2.8%) | `primary_amine` (2.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.2%) | `pyridine_organocat` (2.5%) | `ammonium_PTC_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (57.1%) | `ABSENT` (22.6%) | `polar_aprotic_nitrile` (7.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `__ABSENT__` (40%) | `ClCCl` (2%) | `O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `BrCCBr` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1142  yield=0.5%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1143  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1144  yield=21.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1145  yield=77.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1146  yield=34.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1147  yield=24.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1148  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1149  yield=68.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1150  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #8)

```
C=CCCNc1ccc(Cl)cc1>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (73.4%) | `graphite_generic` (19.1%) | `graphite_rod` (3.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.1%) | `nickel` (0.8%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (86.4%) | `platinum_foil` (10.8%) | `platinum_plate` (2.5%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (96.8%) | `ABSENT` (3.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (71.9%) | `K` (14.0%) | `Na` (12.4%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (93.3%) | `I` (3.0%) | `ClO4` (2.3%) | ✗ |
| 试剂大类 | 103 | `alkali_sulfinate` | `ABSENT` (12.7%) | `alkali_sulfonate` (10.7%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (58.5%) | `Mn_complex` (25.0%) | `brønsted_acid_cat` (10.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.9%) | `aqueous` (1.1%) | `polar_aprotic_sulfoxide` (0.5%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (98%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])C(F)(F)F.` + `__OTHER__` + `O=C(O)C(F)(F)F` | `__ABSENT__` (99%) | `CC(=O)O` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `[I-].[Li+]` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #1151  yield=66.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1152  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1153  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1154  yield=0.5%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1155  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=CCCNc1ccc(Cl)cc1.C[Si](C)(C)C(F)(F)F>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (43.6%) | `carbon_generic` (21.4%) | `reticulated_vitreous_carbon` (11.6%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.5%) | `nickel` (0.4%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (79.9%) | `platinum_foil` (12.6%) | `platinum_plate` (7.3%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (84.9%) | `ABSENT` (15.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (49.2%) | `Na` (34.7%) | `K` (13.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (90.6%) | `I` (5.6%) | `ClO4` (1.9%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (16.9%) | `alkali_sulfonate` (2.3%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (53.1%) | `Mn_complex` (28.9%) | `brønsted_acid_cat` (7.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (98.6%) | `aqueous` (0.7%) | `polar_aprotic_sulfoxide` (0.2%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (97%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `O=S(=O)([O-])C(F)(` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[I-].[Li+]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1156  yield=0.5%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=CCCNc1ccc(Cl)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.1%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (46.3%) | `carbon_felt` (22.2%) | `graphite_generic` (16.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.2%) | `ABSENT` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (50.2%) | `platinum_plate` (44.3%) | `platinum_foil` (5.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (93.6%) | `ABSENT` (6.4%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (49.0%) | `Li` (28.4%) | `Na` (12.6%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (54.3%) | `molecular_no_ion` (36.9%) | `carboxylate` (3.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (19.7%) | `cyanide` (2.3%) | `thiol` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (44.2%) | `Mn_complex` (33.7%) | `Co_complex` (6.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.3%) | `acyclic_ether` (0.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (94%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[I-].[Li+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1157  yield=64.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1158  yield=0.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #4)

```
C=CCCNc1ccc(Cl)cc1.O=S(=O)([O-])C(F)(F)F.[Na+]>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `ABSENT` (1.0%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (88.7%) | `graphite_generic` (5.5%) | `unknown_electrode` (3.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `nickel` (3.3%) | `carbon` (2.4%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (32.9%) | `nickel_generic` (27.5%) | `platinum_generic` (19.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (92.9%) | `ABSENT` (7.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (57.0%) | `Na` (12.8%) | `K` (10.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (70.8%) | `ABSENT` (10.5%) | `I` (9.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (25.1%) | `alkali_phosphate` (3.1%) | `metal_oxide_oxidant` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.4%) | `Mn_complex` (2.5%) | `pyridine_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.2%) | `aqueous` (0.9%) | `acyclic_ether` (0.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (87%) | `COC(C)(C)C` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `CCN(CC)CC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1159  yield=24.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1160  yield=62.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1161  yield=21.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1162  yield=63.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1163  yield=60.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1164  yield=68.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #8)

```
C=CCCNc1ccc(Cl)cc1>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (73.4%) | `graphite_generic` (19.1%) | `graphite_rod` (3.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.1%) | `nickel` (0.8%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (86.4%) | `platinum_foil` (10.8%) | `platinum_plate` (2.5%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (96.8%) | `ABSENT` (3.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NMe4` | `Li` (71.9%) | `K` (14.0%) | `Na` (12.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (93.3%) | `I` (3.0%) | `ClO4` (2.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (12.7%) | `alkali_sulfonate` (10.7%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (58.5%) | `Mn_complex` (25.0%) | `brønsted_acid_cat` (10.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.9%) | `aqueous` (1.1%) | `polar_aprotic_sulfoxide` (0.5%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (98%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])C(F)(F)F.` + `__OTHER__` + `O=C(O)C(F)(F)F` | `__ABSENT__` (99%) | `CC(=O)O` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `[I-].[Li+]` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #1165  yield=34.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1166  yield=41.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1167  yield=24.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1168  yield=0.5%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1169  yield=61.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1170  yield=21.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1171  yield=39.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1172  yield=40.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1173  yield=16.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `ketone` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1174  yield=70.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1175  yield=66.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1176  yield=50.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1177  yield=77.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1178  yield=69.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1179  yield=74.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OC(C(F)(F)F)(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (36.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (21.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_foil` (57.7%) | `platinum_generic` (41.5%) | `platinum_plate` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (72.3%) | `ABSENT` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (98.8%) | `Na` (0.8%) | `K` (0.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (98.3%) | `ClO4` (1.3%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `carboxylic_acid` (3.7%) | `thiol` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (60.3%) | `ABSENT` (16.4%) | `Mn_complex` (14.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_amide` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (57%) | `__ABSENT__` (10%) | `[I-].[Li+]` (3%) | set ✗ / any ✓ |

---

### Reaction #1180  yield=62.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `hcl` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1181  yield=40.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1182  yield=21.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1183  yield=68.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1184  yield=60.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1185  yield=70.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1186  yield=66.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1187  yield=72.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1188  yield=71.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1189  yield=72.0%

**Source paper**: [`EurJOC/10.1002_ejoc.202500634_p3_t0.json`](reactions_by_journal_alkene_ec_audited/EurJOC/10.1002_ejoc.202500634_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCNc1ccc(Cl)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1190  yield=28.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #0)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(C(=O)OC)cc1>>COC(=O)c1ccc2c(c1)C(CC(F)(F)F)CCN2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.8%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (45.5%) | `reticulated_vitreous_carbon` (21.6%) | `carbon_generic` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (88.2%) | `nickel` (10.9%) | `carbon` (0.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (96.5%) | `platinum_plate` (1.3%) | `nickel_plate` (1.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (75.5%) | `Li` (22.4%) | `K` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (73.9%) | `ClO4` (16.9%) | `BF4` (3.8%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (23.0%) | `thiol` (2.3%) | `alkali_sulfonate` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `Co_complex` (0.2%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.6%) | `cyclic_ether` (1.4%) | `ABSENT` (0.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (97%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br][Mn][Br]` (0%) | set ✓ / any ✓ |

---

### Reaction #1191  yield=24.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #1)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(C(F)(F)F)cc1OC>>COc1cc(C(F)(F)F)cc2c1NCCC2CC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_felt` (31.9%) | `graphite_generic` (22.9%) | `graphite_rod` (21.6%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.6%) | `nickel` (3.6%) | `carbon` (0.7%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (85.8%) | `platinum_plate` (12.8%) | `nickel_plate` (1.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.4%) | `Li` (0.5%) | `Na` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (66.4%) | `I` (15.5%) | `PF6` (9.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (30.7%) | `thiol` (2.3%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `Co_complex` (0.2%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.3%) | `polar_protic_alcohol` (0.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (99%) | `O` (79%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1192  yield=21.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #2)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccccc1C(F)(F)F>>FC(F)(F)CC1CCNc2c1cccc2C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (52.2%) | `carbon_generic` (19.3%) | `graphite_felt` (14.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.6%) | `nickel` (3.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (93.4%) | `platinum_plate` (5.5%) | `nickel_plate` (0.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (88.7%) | `Li` (10.1%) | `K` (0.4%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (59.6%) | `I` (14.0%) | `ClO4` (10.5%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (26.7%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `Fe_complex` (0.4%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (92.1%) | `polar_protic_alcohol` (2.8%) | `polar_aprotic_amide` (2.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (99%) | `O` (61%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1193  yield=40.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #3)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(C)c(C(=O)OC)c1>>COC(=O)c1c(C)ccc2c1C(CC(F)(F)F)CCN2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.4%) | `platinum` (5.2%) | `sacrificial_magnesium` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (59.1%) | `graphite_rod` (20.3%) | `platinum_generic` (7.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.8%) | `nickel` (0.1%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (94.2%) | `platinum_plate` (5.8%) | `nickel_foam` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.5%) | `Li` (7.8%) | `NEt4` (2.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (36.2%) | `I` (33.9%) | `ClO4` (21.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (19.1%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.0%) | `organic_neutral_cat` (18.0%) | `ionic_organocat` (3.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.9%) | `cyclic_ether` (0.7%) | `halogenated_aliphatic` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (96%) | `CC#N` (95%) | `ClCCCl` (4%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1194  yield=35.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #4)

```
C=CCCNc1ccccc1Cl.O=C1OI(C(F)(F)F)c2ccccc21>>FC(F)(F)CC1CCNC2C(Cl)=CC=CC12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (29.3%) | `carbon_generic` (25.3%) | `carbon_felt` (19.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `nickel` (46.0%) | `platinum` (45.2%) | `carbon` (8.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (64.5%) | `nickel_plate` (33.1%) | `platinum_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (90.2%) | `Li` (8.3%) | `Na` (1.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (47.7%) | `PF6` (18.2%) | `I` (15.6%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (19.0%) | `thiol` (2.6%) | `phosphine_neutral` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.2%) | `Co_complex` (1.3%) | `ionic_organocat` (1.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.8%) | `aqueous` (14.9%) | `polar_aprotic_amide` (6.5%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (49%) | `CC#N` (32%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1195  yield=45.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #5)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Cl)c(C)c1>>Cc1c(Cl)ccc2c1C(CC(F)(F)F)CCN2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (99.2%) | `platinum` (0.7%) | `ABSENT` (0.0%) | ✗ |
| 阳极 (细类) | 43 | `magnesium_generic` | `reticulated_vitreous_carbon` (81.4%) | `graphite_rod` (7.6%) | `carbon_generic` (3.2%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (97.6%) | `nickel` (2.3%) | `carbon` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_generic` (99.9%) | `platinum_plate` (0.0%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (59.1%) | `NBu4` (39.4%) | `NEt4` (0.6%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (62.7%) | `BF4` (20.8%) | `I` (10.7%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (19.4%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (78.3%) | `Co_complex` (7.0%) | `organic_neutral_cat` (6.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.8%) | `cyclic_ether` (0.9%) | `aqueous` (0.5%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (99%) | `O` (98%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl][Au].c1ccc(P(c` (0%) | set ✓ / any ✓ |

---

### Reaction #1196  yield=43.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #6)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(F)cc1C>>Cc1cc(F)cc2c1NCCC2CC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_felt` (43.3%) | `graphite_rod` (41.5%) | `reticulated_vitreous_carbon` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `nickel` (1.5%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (80.2%) | `platinum_plate` (15.5%) | `nickel_plate` (4.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.6%) | `Na` (12.4%) | `Li` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (45.3%) | `I` (43.6%) | `molecular_no_ion` (5.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.0%) | `thiol` (2.0%) | `tetraaryl_borate` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Co_complex` (0.5%) | `ionic_organocat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (87.5%) | `halogenated_aliphatic` (4.7%) | `cyclic_ether` (1.8%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (90%) | `ClCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCN(CC)CC` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1197  yield=42.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #7)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Br)cc1C>>Cc1cc(Br)cc2c1NCCC2CC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_felt` (53.1%) | `carbon_felt` (21.5%) | `graphite_rod` (14.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.7%) | `nickel` (2.2%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (71.0%) | `platinum_plate` (27.3%) | `nickel_plate` (1.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (64.9%) | `Li` (18.7%) | `Na` (11.6%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (41.2%) | `molecular_no_ion` (27.0%) | `I` (23.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (35.3%) | `thiol` (2.0%) | `metal_oxide_oxidant` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Fe_complex` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.4%) | `ketone` (0.1%) | `polar_protic_alcohol` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (100%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCN(CC)CC` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1198  yield=42.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #8)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(C(C)(C)C)cc1C(F)(F)F>>CC(C)(C)c1cc2c(c(C(F)(F)F)c1)NCCC2CC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (79.5%) | `carbon_felt` (5.0%) | `graphite_generic` (4.1%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.1%) | `nickel` (0.8%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (72.8%) | `platinum_generic` (26.7%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (69.0%) | `Li` (11.6%) | `Na` (11.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (70.5%) | `molecular_no_ion` (13.0%) | `BF4` (7.6%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (37.4%) | `thiol` (1.9%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `Mn_complex` (0.6%) | `Co_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.8%) | `ABSENT` (0.1%) | `polar_protic_alcohol` (0.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (99%) | `O` (98%) | `ClCCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1199  yield=41.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #9)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc2c(c1)C(CC(F)(F)F)CCN2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_felt` (29.8%) | `graphite_generic` (17.7%) | `carbon_generic` (16.7%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.1%) | `nickel` (4.1%) | `carbon` (0.8%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (99.3%) | `platinum_plate` (0.4%) | `nickel_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (58.5%) | `NBu4` (18.4%) | `K` (12.9%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `I` (76.2%) | `molecular_no_ion` (12.8%) | `ClO4` (5.5%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (19.2%) | `thiol` (2.6%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `Mn_complex` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (98.6%) | `cyclic_ether` (0.6%) | `polar_aprotic_amide` (0.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `Cl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1200  yield=60.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #10)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Br)c(C(=O)OC)c1>>COC(=O)c1c(Br)ccc2c1C(CC(F)(F)F)CCN2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (98.1%) | `platinum` (1.8%) | `sacrificial_magnesium` (0.1%) | ✗ |
| 阳极 (细类) | 43 | `zinc_generic` | `reticulated_vitreous_carbon` (81.0%) | `graphite_rod` (5.9%) | `platinum_generic` (5.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.9%) | `nickel` (0.1%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `reticulated_vitreous_carbon` | `platinum_generic` (99.4%) | `platinum_plate` (0.6%) | `nickel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.9%) | `Li` (1.9%) | `NEt4` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (42.6%) | `ClO4` (26.2%) | `I` (22.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (20.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (86.7%) | `organic_neutral_cat` (10.0%) | `thianthrene_phenothiazine_cat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (99.0%) | `halogenated_aliphatic` (0.5%) | `cyclic_ether` (0.3%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `O` (99%) | `CC#N` (99%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1201  yield=55.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #11)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1cc(Br)ccc1Cl>>FC(F)(F)CC1CCNc2c(Cl)ccc(Br)c21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (96.4%) | `graphite_felt` (1.9%) | `carbon_generic` (0.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (99.8%) | `platinum_foil` (0.2%) | `platinum_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.4%) | `ABSENT` (3.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.0%) | `Na` (11.0%) | `molecular_no_ion` (4.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (40.4%) | `Cl` (23.8%) | `I` (16.4%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (45.9%) | `thiol` (1.7%) | `metal_oxide_oxidant` (1.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.6%) | `aryl_iodide_mediator` (0.6%) | `organic_neutral_cat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.7%) | `halogenated_aliphatic` (0.2%) | `polar_protic_alcohol` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (100%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `Cc1ccc(S(=O)(=O)O)` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1202  yield=51.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #12)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Cl)c(Cl)c1F>>Fc1c(Cl)c(Cl)cc2c1NCCC2CC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (91.9%) | `graphite_felt` (4.8%) | `carbon_generic` (1.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (92.9%) | `nickel` (5.8%) | `carbon` (1.2%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (50.6%) | `platinum_plate` (33.4%) | `nickel_plate` (15.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.4%) | `Li` (0.9%) | `K` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (88.1%) | `I` (4.7%) | `carboxylate` (3.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (36.1%) | `unparseable_text` (2.0%) | `electrophilic_N_F` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `Co_complex` (0.1%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.0%) | `polar_protic_alcohol` (0.5%) | `aqueous` (0.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (100%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl][Au].c1ccc(P(c` (0%) | set ✓ / any ✓ |

---

### Reaction #1203  yield=51.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #13)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(C(F)(F)F)cc1C>>Cc1cc(C(F)(F)F)cc2c1NCCC2CC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_felt` (74.0%) | `reticulated_vitreous_carbon` (14.4%) | `graphite_generic` (4.7%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.5%) | `nickel` (4.3%) | `carbon` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (93.6%) | `platinum_plate` (4.9%) | `nickel_plate` (1.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.9%) | `Li` (0.6%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (68.5%) | `carboxylate` (11.3%) | `I` (10.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (30.8%) | `thiol` (2.2%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Co_complex` (0.8%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (96.3%) | `polar_protic_alcohol` (1.4%) | `tfe` (0.5%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (99%) | `O` (96%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1204  yield=57.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #14)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Cl)c(Cl)c1C(F)(F)F>>FC(F)(F)CC1CCNc2c1cc(Cl)c(Cl)c2C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (45.4%) | `graphite_generic` (28.1%) | `reticulated_vitreous_carbon` (7.7%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.0%) | `nickel` (1.6%) | `carbon` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `nickel_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.5%) | `Li` (0.4%) | `Na` (0.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (94.5%) | `I` (2.4%) | `ClO4` (1.1%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (34.3%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Co_complex` (0.6%) | `Fe_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (94.1%) | `polar_protic_alcohol` (5.2%) | `halogenated_aliphatic` (0.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (100%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1205  yield=57.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #15)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Cl)c(Br)c1>>FC(F)(F)CC1CCNc2ccc(Cl)c(Br)c21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `platinum` (1.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (38.1%) | `graphite_rod` (34.5%) | `graphite_felt` (8.3%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (96.8%) | `platinum_plate` (3.2%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.5%) | `Li` (2.0%) | `NEt4` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (74.0%) | `I` (13.6%) | `PF6` (5.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (22.1%) | `tellurium_reagent` (2.2%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (98.8%) | `cyclic_ether` (0.5%) | `halogenated_aliphatic` (0.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (99%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCN(CC)CC` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1206  yield=57.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #16)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Br)cc1C(F)(F)F>>FC(F)(F)CC1CCNc2c1cc(Br)cc2C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (54.3%) | `graphite_rod` (36.5%) | `graphite_felt` (3.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (95.4%) | `platinum_generic` (4.5%) | `nickel_plate` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (41.4%) | `Li` (27.2%) | `Na` (24.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (53.5%) | `BF4` (20.3%) | `I` (16.3%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (33.6%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `Mn_complex` (0.3%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.8%) | `polar_protic_alcohol` (0.1%) | `polar_aprotic_sulfoxide` (0.0%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (99%) | `COC(C)(C)C` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1207  yield=53.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #17)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Cl)cc1C>>Cc1cc(Cl)cc2c1NCCC2CC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_felt` (57.8%) | `graphite_generic` (17.6%) | `graphite_rod` (12.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `nickel` (0.4%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (95.7%) | `platinum_plate` (4.1%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.3%) | `Li` (10.9%) | `Na` (8.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (65.8%) | `I` (19.3%) | `carboxylate` (5.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (43.7%) | `metal_oxide_oxidant` (1.7%) | `tellurium_reagent` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.0%) | `Fe_complex` (0.5%) | `Co_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (98.4%) | `polar_protic_alcohol` (0.6%) | `aqueous` (0.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (100%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCN(CC)CC` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1208  yield=53.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #18)

```
C=CCCNc1ccc(C)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>Cc1ccc2c(c1)C(CC(F)(F)F)CCN2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (29.4%) | `carbon_generic` (21.5%) | `graphite_felt` (20.7%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (94.4%) | `nickel` (5.5%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (85.0%) | `platinum_plate` (10.3%) | `nickel_plate` (4.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (95.9%) | `ABSENT` (3.9%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (87.4%) | `Li` (5.5%) | `ABSENT` (3.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (52.0%) | `I` (13.1%) | `PF6` (11.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (22.3%) | `thiol` (2.4%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.8%) | `Co_complex` (1.6%) | `ionic_organocat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (88.2%) | `cyclic_ether` (5.8%) | `aqueous` (1.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (99%) | `CC#N` (97%) | `CS(C)=O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCN(CC)CC` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[I-].[Li+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1209  yield=69.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #19)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Cl)cc1Cl>>FC(F)(F)CC1CCNc2c(Cl)cc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (49.8%) | `graphite_felt` (43.8%) | `graphite_generic` (3.5%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.3%) | `nickel` (0.6%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (80.9%) | `platinum_plate` (18.6%) | `nickel_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (46.6%) | `Na` (39.9%) | `Li` (7.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (45.6%) | `BF4` (43.6%) | `carboxylate` (3.8%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (42.2%) | `metal_oxide_oxidant` (1.7%) | `tellurium_reagent` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ionic_organocat` (0.1%) | `Co_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (94.6%) | `polar_protic_alcohol` (2.3%) | `aqueous` (1.5%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `O` (100%) | `CC#N` (99%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCN(CC)CC` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1210  yield=63.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #20)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Cl)c(Cl)c1>>FC(F)(F)CC1CCNc2ccc(Cl)c(Cl)c21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (54.9%) | `platinum` (45.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `platinum_plate` (51.5%) | `platinum_generic` (38.4%) | `graphite_rod` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.3%) | `nickel` (0.6%) | `carbon` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (96.0%) | `platinum_plate` (4.0%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (93.7%) | `Li` (1.8%) | `H` (1.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `I` (34.3%) | `PF6` (31.3%) | `Cl` (17.8%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (18.3%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (93.7%) | `halogenated_aliphatic` (4.2%) | `polar_aprotic_sulfoxide` (0.5%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (98%) | `O` (97%) | `CS(C)=O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC[N+](CC)(CC)CC.F` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1211  yield=68.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #21)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(I)cc1>>FC(F)(F)CC1CCNc2ccc(I)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_felt` (31.7%) | `graphite_rod` (30.4%) | `graphite_generic` (9.9%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (92.9%) | `nickel` (6.3%) | `carbon` (0.8%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (93.8%) | `nickel_plate` (3.0%) | `platinum_plate` (2.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (66.4%) | `Na` (18.8%) | `NBu4` (11.7%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `I` (50.5%) | `molecular_no_ion` (15.5%) | `ClO4` (14.9%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (28.8%) | `thiol` (2.1%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `Co_complex` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.3%) | `aqueous` (1.2%) | `cyclic_ether` (0.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (99%) | `ClCCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[I-].[Li+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1212  yield=62.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #22)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(C(F)(F)F)cc1C(F)(F)F>>FC(F)(F)CC1CCNc2c1cc(C(F)(F)F)cc2C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (70.9%) | `graphite_felt` (9.6%) | `graphite_generic` (6.1%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.1%) | `nickel` (0.8%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (83.6%) | `platinum_generic` (15.8%) | `nickel_plate` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.9%) | `Li` (0.7%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (66.9%) | `I` (16.9%) | `carboxylate` (12.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.8%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Co_complex` (0.5%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (97.9%) | `polar_protic_alcohol` (1.5%) | `ABSENT` (0.1%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `O` (87%) | `ClCCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1213  yield=65.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #23)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Cl)cc1Br>>FC(F)(F)CC1CCNc2c(Br)cc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_felt` (88.8%) | `graphite_rod` (5.0%) | `boron_doped_diamond` (1.3%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `nickel` (0.2%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (96.9%) | `platinum_plate` (3.1%) | `nickel_foam` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.5%) | `Li` (2.9%) | `Na` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (64.7%) | `I` (28.5%) | `Cl` (2.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (34.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `Fe_complex` (0.2%) | `Co_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (97.3%) | `aqueous` (0.9%) | `polar_protic_alcohol` (0.5%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `O` (100%) | `CC#N` (98%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1214  yield=65.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #24)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Cl)c(C(=O)OC)c1>>COC(=O)c1c(Cl)ccc2c1C(CC(F)(F)F)CCN2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.8%) | `platinum` (3.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (40.9%) | `graphite_rod` (32.4%) | `platinum_generic` (15.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.9%) | `nickel` (0.1%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (99.8%) | `platinum_plate` (0.2%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.1%) | `Li` (4.6%) | `NEt4` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (41.8%) | `I` (34.1%) | `ClO4` (16.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (28.1%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.1%) | `organic_neutral_cat` (1.7%) | `Co_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.4%) | `halogenated_aliphatic` (0.3%) | `cyclic_ether` (0.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (99%) | `O` (94%) | `ClCCCl` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1215  yield=65.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #25)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(F)c(C(=O)OC)c1>>COC(=O)c1c(F)ccc2c1C(CC(F)(F)F)CCN2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (1.3%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (78.5%) | `reticulated_vitreous_carbon` (11.3%) | `platinum_generic` (3.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (87.0%) | `platinum_plate` (13.0%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.7%) | `NEt4` (0.5%) | `Li` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (71.8%) | `I` (16.5%) | `Cl` (5.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (13.5%) | `cyanide` (2.7%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (83.7%) | `Co_complex` (7.5%) | `organic_neutral_cat` (4.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (99.6%) | `cyclic_ether` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `O` (55%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #1216  yield=62.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #26)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Br)c(C(F)(F)F)c1>>FC(F)(F)CC1CCNc2ccc(Br)c(C(F)(F)F)c21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (29.2%) | `graphite_rod` (23.2%) | `carbon_generic` (20.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (94.4%) | `nickel` (5.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (99.8%) | `platinum_plate` (0.1%) | `nickel_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `Li` (1.7%) | `K` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (34.0%) | `BF4` (30.5%) | `PF6` (17.7%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (15.1%) | `phosphine_neutral` (2.4%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `organic_neutral_cat` (0.2%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.3%) | `cyclic_ether` (0.2%) | `polar_aprotic_amide` (0.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (100%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCN(CC)CC` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1217  yield=65.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #27)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(OC(F)(F)F)cc1>>FC(F)(F)CC1CCNc2ccc(OC(F)(F)F)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.8%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (33.6%) | `reticulated_vitreous_carbon` (29.2%) | `unknown_electrode` (8.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.2%) | `nickel` (1.7%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (99.3%) | `platinum_plate` (0.5%) | `nickel_foam` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (64.4%) | `NBu4` (27.1%) | `Na` (6.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (45.7%) | `molecular_no_ion` (18.9%) | `Cl` (10.9%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (24.6%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.5%) | `Co_complex` (7.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.6%) | `aqueous` (1.0%) | `polar_aprotic_amide` (0.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (99%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1218  yield=70.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #28)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Cl)c(C(F)(F)F)c1>>FC(F)(F)CC1CCNc2ccc(Cl)c(C(F)(F)F)c21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (46.9%) | `graphite_rod` (44.1%) | `reticulated_vitreous_carbon` (5.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `nickel` (2.8%) | `carbon` (0.8%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (96.2%) | `platinum_plate` (2.6%) | `nickel_plate` (1.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (93.6%) | `Li` (3.8%) | `NEt4` (2.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (63.1%) | `I` (15.5%) | `ClO4` (11.7%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (22.8%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (98.6%) | `cyclic_ether` (0.4%) | `aqueous` (0.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (99%) | `O` (99%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1219  yield=71.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #29)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Cl)cc1C(F)(F)F>>FC(F)(F)CC1CCNc2c1cc(Cl)cc2C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (69.6%) | `carbon_felt` (18.2%) | `graphite_generic` (4.5%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.9%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (50.4%) | `platinum_plate` (49.5%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (49.6%) | `Na` (38.9%) | `Li` (9.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (45.5%) | `I` (29.3%) | `molecular_no_ion` (14.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (41.6%) | `metal_oxide_oxidant` (1.7%) | `tellurium_reagent` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.6%) | `Co_complex` (1.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (98.9%) | `polar_protic_alcohol` (0.6%) | `aqueous` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (98%) | `COC(C)(C)C` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O=C(O)O.[Na]` (0%) | `[Br-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #1220  yield=76.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #30)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Br)cc1>>FC(F)(F)CC1CCNc2ccc(Br)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (37.8%) | `graphite_felt` (33.0%) | `carbon_generic` (16.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.4%) | `nickel` (2.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (88.9%) | `platinum_plate` (10.3%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (89.1%) | `ABSENT` (10.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (38.9%) | `Li` (28.6%) | `K` (18.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (41.0%) | `molecular_no_ion` (27.8%) | `Br` (13.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (20.7%) | `tellurium_reagent` (2.3%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `Ni_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.2%) | `polar_aprotic_sulfoxide` (0.2%) | `cyclic_ether` (0.2%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (99%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[Li+]` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1221  yield=78.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #31)

```
C=CCCNc1ccc(F)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>Fc1ccc2c(c1)C(CC(F)(F)F)CCN2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (68.8%) | `carbon_generic` (5.8%) | `boron_doped_diamond` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `nickel` (0.3%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (98.9%) | `platinum_plate` (0.9%) | `platinum_foil` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (44.7%) | `Li` (41.5%) | `NBu4` (9.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (62.6%) | `molecular_no_ion` (31.2%) | `ClO4` (2.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (25.1%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (86.1%) | `Co_complex` (4.7%) | `ionic_organocat` (2.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (94.9%) | `aqueous` (3.0%) | `cyclic_ether` (0.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (100%) | `CC#N` (93%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[Li+]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1222  yield=77.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #32)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(Cl)cc1>>FC(F)(F)CC1CCNc2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (25.8%) | `graphite_rod` (22.5%) | `carbon_generic` (19.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (97.2%) | `platinum_plate` (2.4%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (60.0%) | `Li` (19.5%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (60.8%) | `I` (21.9%) | `carboxylate` (7.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `Mn_complex` (1.2%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (97.5%) | `aqueous` (1.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CC(C)=O` + `CO` | `O` (100%) | `CC#N` (100%) | `COC(C)(C)C` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1223  yield=74.0%

**Source paper**: [`EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json`](reactions_by_journal_alkene_ec_audited/EurJOC/2025_European_Journal_of_Organic_Chemistry_2025_28_40_e202500634.json) (反应 idx 在该 JSON 内 = #33)

```
O=C1OI(C(F)(F)F)c2ccccc21.C=CCCNc1ccc(C(F)(F)F)cc1>>FC(F)(F)CC1CCNc2ccc(C(F)(F)F)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (33.3%) | `reticulated_vitreous_carbon` (21.0%) | `graphite_felt` (13.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.2%) | `nickel` (1.8%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (96.6%) | `platinum_plate` (3.1%) | `nickel_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.6%) | `Li` (11.4%) | `Na` (7.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `carboxylate` (34.4%) | `I` (33.0%) | `molecular_no_ion` (14.6%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (22.0%) | `cyanide` (2.4%) | `thiol` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.3%) | `Co_complex` (5.5%) | `organic_neutral_cat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (98.0%) | `cyclic_ether` (0.4%) | `hfip` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `[H+].[OH-]` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1224  yield=82.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1225  yield=17.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1226  yield=0.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `imidazolium` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✗ |
| 电解质 anion | 26 | `Br` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1227  yield=39.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1228  yield=28.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1229  yield=80.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1230  yield=68.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1231  yield=46.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `imidazolium` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1232  yield=38.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1233  yield=92.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1234  yield=63.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `copper` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✗ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1235  yield=84.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1236  yield=5.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `imidazolium` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✗ |
| 电解质 anion | 26 | `Br` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1237  yield=92.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1238  yield=90.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1239  yield=68.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1240  yield=0.5%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1241  yield=0.5%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `imidazolium` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✗ |
| 电解质 anion | 26 | `Br` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1242  yield=0.5%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `imidazolium` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✗ |
| 电解质 anion | 26 | `Br` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1243  yield=5.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `imidazolium` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✗ |
| 电解质 anion | 26 | `Br` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1244  yield=7.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `imidazolium` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✗ |
| 电解质 anion | 26 | `Br` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1245  yield=80.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1246  yield=82.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1247  yield=63.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `copper` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✗ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1248  yield=92.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1249  yield=77.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1250  yield=17.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1251  yield=56.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1252  yield=51.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1253  yield=82.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1254  yield=92.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1255  yield=52.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1256  yield=66.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1257  yield=38.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1258  yield=30.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1259  yield=81.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1260  yield=76.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1261  yield=84.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1262  yield=92.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1263  yield=75.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1264  yield=0.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1265  yield=0.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1266  yield=28.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1267  yield=0.5%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OH` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1268  yield=11.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NMe4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✗ |
| 电解质 anion | 26 | `F` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1269  yield=0.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `molecular_no_ion` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1270  yield=0.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1271  yield=39.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `K` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1272  yield=82.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1273  yield=0.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1274  yield=46.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `imidazolium` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1275  yield=21.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `SO4` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1276  yield=39.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1277  yield=0.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1278  yield=0.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1279  yield=82.0%

**Source paper**: [`GreenChem/10.1039_D5GC01259G_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC01259G_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C1=CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC1CCCCC1[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (66.6%) | `carbon_generic` (29.8%) | `glassy_carbon` (1.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.1%) | `carbon` (12.1%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_generic` (75.6%) | `platinum_plate` (16.1%) | `nickel_generic` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.7%) | `Li` (12.7%) | `NH4` (10.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (21.2%) | `Br` (21.1%) | `I` (17.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (8.0%) | `carboxylic_acid` (4.0%) | `selenium_reagent` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.2%) | `polar_protic_alcohol` (4.0%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `OCC(F)(F)F` | `CC#N` (99%) | `OCC(F)(F)F` (18%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC.F.F.F` | `__ABSENT__` (47%) | `CC(=O)O` (41%) | `O=S([O-])O.[Na+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1280  yield=55.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1.N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (79.2%) | `carbon_rod` (3.7%) | `graphite_felt` (3.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.2%) | `nickel` (1.3%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.0%) | `platinum_generic` (8.3%) | `platinum_foil` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (40.8%) | `Li` (39.0%) | `K` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (45.1%) | `PF6` (15.4%) | `BF4` (13.9%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `alkali_sulfinate` (13.4%) | `alkali_sulfonate` (4.4%) | `ABSENT` (3.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `Mn_complex` (4.6%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (75.2%) | `polar_protic_acid` (6.2%) | `halogenated_aliphatic` (4.3%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (99%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])C(F)(F)F.` + `O=C([O-])[O-].[K+]` + `OC(C(F)(F)F)C(F)(F` | `O=S([O-])C(F)(F)F.` (59%) | `__OTHER__` (23%) | `OB(O)B(O)O` (18%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `[Fe+2].c1cc[cH-]c1` (2%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #1281  yield=38.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(OC)cc1.O=S([O-])C(F)(F)F.[Na+].N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.5%) | `platinum` (5.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (66.7%) | `graphite_generic` (8.0%) | `carbon_felt` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.8%) | `nickel` (8.2%) | `carbon` (3.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (49.1%) | `platinum_generic` (47.8%) | `iron_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.5%) | `Na` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (29.9%) | `BF4` (25.0%) | `PF6` (20.6%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (27.3%) | `alkali_carbonate` (2.1%) | `metal_oxide_oxidant` (1.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.2%) | `ketone` (10.8%) | `halogenated_aliphatic` (10.3%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (98%) | `CC(C)=O` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Rb+` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (0%) | `O=C1CCC(=O)N1Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1282  yield=29.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1.N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (79.2%) | `carbon_rod` (3.7%) | `graphite_felt` (3.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.2%) | `nickel` (1.3%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.0%) | `platinum_generic` (8.3%) | `platinum_foil` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (40.8%) | `Li` (39.0%) | `K` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (45.1%) | `PF6` (15.4%) | `BF4` (13.9%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfinate` | `alkali_sulfinate` (13.4%) | `alkali_sulfonate` (4.4%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `Mn_complex` (4.6%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (75.2%) | `polar_protic_acid` (6.2%) | `halogenated_aliphatic` (4.3%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (99%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])C(F)(F)F.` + `O=C([O-])[O-].[K+]` + `OC(C(F)(F)F)C(F)(F` | `O=S([O-])C(F)(F)F.` (59%) | `__OTHER__` (23%) | `OB(O)B(O)O` (18%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `[Fe+2].c1cc[cH-]c1` (2%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #1283  yield=19.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1.N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (79.2%) | `carbon_rod` (3.7%) | `graphite_felt` (3.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.2%) | `nickel` (1.3%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.0%) | `platinum_generic` (8.3%) | `platinum_foil` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (40.8%) | `Li` (39.0%) | `K` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (45.1%) | `PF6` (15.4%) | `BF4` (13.9%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfinate` | `alkali_sulfinate` (13.4%) | `alkali_sulfonate` (4.4%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `Mn_complex` (4.6%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (75.2%) | `polar_protic_acid` (6.2%) | `halogenated_aliphatic` (4.3%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (99%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])C(F)(F)F.` + `O=C([O-])[O-].[K+]` + `OC(C(F)(F)F)C(F)(F` | `O=S([O-])C(F)(F)F.` (59%) | `__OTHER__` (23%) | `OB(O)B(O)O` (18%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `[Fe+2].c1cc[cH-]c1` (2%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #1284  yield=38.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(OC)cc1.O=S([O-])C(F)(F)F.[Na+].N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.5%) | `platinum` (5.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (66.7%) | `graphite_generic` (8.0%) | `carbon_felt` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.8%) | `nickel` (8.2%) | `carbon` (3.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (49.1%) | `platinum_generic` (47.8%) | `iron_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.5%) | `Na` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (29.9%) | `BF4` (25.0%) | `PF6` (20.6%) | ✓ |
| 试剂大类 | 103 | `alkali_hydroxide` | `ABSENT` (27.3%) | `alkali_carbonate` (2.1%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.2%) | `ketone` (10.8%) | `halogenated_aliphatic` (10.3%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (98%) | `CC(C)=O` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Rb+` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (0%) | `O=C1CCC(=O)N1Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1285  yield=47.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1.N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (79.2%) | `carbon_rod` (3.7%) | `graphite_felt` (3.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.2%) | `nickel` (1.3%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.0%) | `platinum_generic` (8.3%) | `platinum_foil` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (40.8%) | `Li` (39.0%) | `K` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (45.1%) | `PF6` (15.4%) | `BF4` (13.9%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfinate` | `alkali_sulfinate` (13.4%) | `alkali_sulfonate` (4.4%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `Mn_complex` (4.6%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (75.2%) | `polar_protic_acid` (6.2%) | `halogenated_aliphatic` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (99%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])C(F)(F)F.` + `O=C([O-])[O-].[K+]` + `OC(C(F)(F)F)C(F)(F` | `O=S([O-])C(F)(F)F.` (59%) | `__OTHER__` (23%) | `OB(O)B(O)O` (18%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `[Fe+2].c1cc[cH-]c1` (2%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #1286  yield=45.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1.N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (79.2%) | `carbon_rod` (3.7%) | `graphite_felt` (3.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.2%) | `nickel` (1.3%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.0%) | `platinum_generic` (8.3%) | `platinum_foil` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (40.8%) | `Li` (39.0%) | `K` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (45.1%) | `PF6` (15.4%) | `BF4` (13.9%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfinate` | `alkali_sulfinate` (13.4%) | `alkali_sulfonate` (4.4%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `Mn_complex` (4.6%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (75.2%) | `polar_protic_acid` (6.2%) | `halogenated_aliphatic` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (99%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])C(F)(F)F.` + `O=C([O-])[O-].[K+]` + `OC(C(F)(F)F)C(F)(F` | `O=S([O-])C(F)(F)F.` (59%) | `__OTHER__` (23%) | `OB(O)B(O)O` (18%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `[Fe+2].c1cc[cH-]c1` (2%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #1287  yield=72.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1.N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (79.2%) | `carbon_rod` (3.7%) | `graphite_felt` (3.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.2%) | `nickel` (1.3%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.0%) | `platinum_generic` (8.3%) | `platinum_foil` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (40.8%) | `Li` (39.0%) | `K` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (45.1%) | `PF6` (15.4%) | `BF4` (13.9%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfinate` | `alkali_sulfinate` (13.4%) | `alkali_sulfonate` (4.4%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `Mn_complex` (4.6%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (75.2%) | `polar_protic_acid` (6.2%) | `halogenated_aliphatic` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (99%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])C(F)(F)F.` + `O=C([O-])[O-].[K+]` + `OC(C(F)(F)F)C(F)(F` | `O=S([O-])C(F)(F)F.` (59%) | `__OTHER__` (23%) | `OB(O)B(O)O` (18%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `[Fe+2].c1cc[cH-]c1` (2%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #1288  yield=53.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1.N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (79.2%) | `carbon_rod` (3.7%) | `graphite_felt` (3.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.2%) | `nickel` (1.3%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.0%) | `platinum_generic` (8.3%) | `platinum_foil` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (40.8%) | `Li` (39.0%) | `K` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (45.1%) | `PF6` (15.4%) | `BF4` (13.9%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfinate` | `alkali_sulfinate` (13.4%) | `alkali_sulfonate` (4.4%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `Mn_complex` (4.6%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (75.2%) | `polar_protic_acid` (6.2%) | `halogenated_aliphatic` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (99%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])C(F)(F)F.` + `O=C([O-])[O-].[K+]` + `OC(C(F)(F)F)C(F)(F` | `O=S([O-])C(F)(F)F.` (59%) | `__OTHER__` (23%) | `OB(O)B(O)O` (18%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `[Fe+2].c1cc[cH-]c1` (2%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #1289  yield=55.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1.N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (79.2%) | `carbon_rod` (3.7%) | `graphite_felt` (3.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.2%) | `nickel` (1.3%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.0%) | `platinum_generic` (8.3%) | `platinum_foil` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (40.8%) | `Li` (39.0%) | `K` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (45.1%) | `PF6` (15.4%) | `BF4` (13.9%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfinate` | `alkali_sulfinate` (13.4%) | `alkali_sulfonate` (4.4%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `Mn_complex` (4.6%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (75.2%) | `polar_protic_acid` (6.2%) | `halogenated_aliphatic` (4.3%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (99%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])C(F)(F)F.` + `O=C([O-])[O-].[K+]` + `OC(C(F)(F)F)C(F)(F` | `O=S([O-])C(F)(F)F.` (59%) | `__OTHER__` (23%) | `OB(O)B(O)O` (18%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `[Fe+2].c1cc[cH-]c1` (2%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #1290  yield=55.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1.N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (79.2%) | `carbon_rod` (3.7%) | `graphite_felt` (3.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.2%) | `nickel` (1.3%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.0%) | `platinum_generic` (8.3%) | `platinum_foil` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (40.8%) | `Li` (39.0%) | `K` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (45.1%) | `PF6` (15.4%) | `BF4` (13.9%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfinate` | `alkali_sulfinate` (13.4%) | `alkali_sulfonate` (4.4%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `Mn_complex` (4.6%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (75.2%) | `polar_protic_acid` (6.2%) | `halogenated_aliphatic` (4.3%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (99%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])C(F)(F)F.` + `O=C([O-])[O-].[K+]` + `OC(C(F)(F)F)C(F)(F` | `O=S([O-])C(F)(F)F.` (59%) | `__OTHER__` (23%) | `OB(O)B(O)O` (18%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `[Fe+2].c1cc[cH-]c1` (2%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #1291  yield=0.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1.N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (79.2%) | `carbon_rod` (3.7%) | `graphite_felt` (3.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.2%) | `nickel` (1.3%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.0%) | `platinum_generic` (8.3%) | `platinum_foil` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (40.8%) | `Li` (39.0%) | `K` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (45.1%) | `PF6` (15.4%) | `BF4` (13.9%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfinate` | `alkali_sulfinate` (13.4%) | `alkali_sulfonate` (4.4%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `Mn_complex` (4.6%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (75.2%) | `polar_protic_acid` (6.2%) | `halogenated_aliphatic` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (99%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])C(F)(F)F.` + `O=C([O-])[O-].[K+]` + `OC(C(F)(F)F)C(F)(F` | `O=S([O-])C(F)(F)F.` (59%) | `__OTHER__` (23%) | `OB(O)B(O)O` (18%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `[Fe+2].c1cc[cH-]c1` (2%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #1292  yield=44.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(OC)cc1.O=S([O-])C(F)(F)F.[Na+].N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.5%) | `platinum` (5.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (66.7%) | `graphite_generic` (8.0%) | `carbon_felt` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.8%) | `nickel` (8.2%) | `carbon` (3.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (49.1%) | `platinum_generic` (47.8%) | `iron_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.5%) | `Na` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (29.9%) | `BF4` (25.0%) | `PF6` (20.6%) | ✓ |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (27.3%) | `alkali_carbonate` (2.1%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.2%) | `ketone` (10.8%) | `halogenated_aliphatic` (10.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (98%) | `CC(C)=O` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Rb+` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (0%) | `O=C1CCC(=O)N1Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1293  yield=51.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(OC)cc1.O=S([O-])C(F)(F)F.[Na+].N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (94.5%) | `platinum` (5.3%) | `ABSENT` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (66.7%) | `graphite_generic` (8.0%) | `carbon_felt` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.8%) | `nickel` (8.2%) | `carbon` (3.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (49.1%) | `platinum_generic` (47.8%) | `iron_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.5%) | `Na` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (29.9%) | `BF4` (25.0%) | `PF6` (20.6%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (27.3%) | `alkali_carbonate` (2.1%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.2%) | `ketone` (10.8%) | `halogenated_aliphatic` (10.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (98%) | `CC(C)=O` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Rb+` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (0%) | `O=C1CCC(=O)N1Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1294  yield=72.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(OC)cc1.O=S([O-])C(F)(F)F.[Na+].N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.5%) | `platinum` (5.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (66.7%) | `graphite_generic` (8.0%) | `carbon_felt` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.8%) | `nickel` (8.2%) | `carbon` (3.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (49.1%) | `platinum_generic` (47.8%) | `iron_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.5%) | `Na` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (29.9%) | `BF4` (25.0%) | `PF6` (20.6%) | ✓ |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (27.3%) | `alkali_carbonate` (2.1%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.2%) | `ketone` (10.8%) | `halogenated_aliphatic` (10.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (98%) | `CC(C)=O` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Rb+` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (0%) | `O=C1CCC(=O)N1Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1295  yield=57.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1.N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (79.2%) | `carbon_rod` (3.7%) | `graphite_felt` (3.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.2%) | `nickel` (1.3%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.0%) | `platinum_generic` (8.3%) | `platinum_foil` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (40.8%) | `Li` (39.0%) | `K` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (45.1%) | `PF6` (15.4%) | `BF4` (13.9%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfinate` | `alkali_sulfinate` (13.4%) | `alkali_sulfonate` (4.4%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `Mn_complex` (4.6%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (75.2%) | `polar_protic_acid` (6.2%) | `halogenated_aliphatic` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (99%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])C(F)(F)F.` + `O=C([O-])[O-].[K+]` + `OC(C(F)(F)F)C(F)(F` | `O=S([O-])C(F)(F)F.` (59%) | `__OTHER__` (23%) | `OB(O)B(O)O` (18%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `[Fe+2].c1cc[cH-]c1` (2%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #1296  yield=68.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(OC)cc1.O=S([O-])C(F)(F)F.[Na+].N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.5%) | `platinum` (5.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (66.7%) | `graphite_generic` (8.0%) | `carbon_felt` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.8%) | `nickel` (8.2%) | `carbon` (3.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (49.1%) | `platinum_generic` (47.8%) | `iron_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.5%) | `Na` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (29.9%) | `BF4` (25.0%) | `PF6` (20.6%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (27.3%) | `alkali_carbonate` (2.1%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.2%) | `ketone` (10.8%) | `halogenated_aliphatic` (10.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (98%) | `CC(C)=O` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Rb+` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (0%) | `O=C1CCC(=O)N1Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1297  yield=65.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(OC)cc1.O=S([O-])C(F)(F)F.[Na+].N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.5%) | `platinum` (5.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (66.7%) | `graphite_generic` (8.0%) | `carbon_felt` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.8%) | `nickel` (8.2%) | `carbon` (3.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (49.1%) | `platinum_generic` (47.8%) | `iron_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.5%) | `Na` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (29.9%) | `BF4` (25.0%) | `PF6` (20.6%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (27.3%) | `alkali_carbonate` (2.1%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.2%) | `ketone` (10.8%) | `halogenated_aliphatic` (10.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (98%) | `CC(C)=O` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Rb+` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (0%) | `O=C1CCC(=O)N1Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1298  yield=52.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1.N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (79.2%) | `carbon_rod` (3.7%) | `graphite_felt` (3.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.2%) | `nickel` (1.3%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.0%) | `platinum_generic` (8.3%) | `platinum_foil` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (40.8%) | `Li` (39.0%) | `K` (5.4%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (45.1%) | `PF6` (15.4%) | `BF4` (13.9%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfinate` | `alkali_sulfinate` (13.4%) | `alkali_sulfonate` (4.4%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `Mn_complex` (4.6%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (75.2%) | `polar_protic_acid` (6.2%) | `halogenated_aliphatic` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (99%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])C(F)(F)F.` + `O=C([O-])[O-].[K+]` + `OC(C(F)(F)F)C(F)(F` | `O=S([O-])C(F)(F)F.` (59%) | `__OTHER__` (23%) | `OB(O)B(O)O` (18%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `[Fe+2].c1cc[cH-]c1` (2%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #1299  yield=59.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(OC)cc1.O=S([O-])C(F)(F)F.[Na+].N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.5%) | `platinum` (5.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (66.7%) | `graphite_generic` (8.0%) | `carbon_felt` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.8%) | `nickel` (8.2%) | `carbon` (3.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (49.1%) | `platinum_generic` (47.8%) | `iron_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.5%) | `Na` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (29.9%) | `BF4` (25.0%) | `PF6` (20.6%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfinate` | `ABSENT` (27.3%) | `alkali_carbonate` (2.1%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.2%) | `ketone` (10.8%) | `halogenated_aliphatic` (10.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (98%) | `CC(C)=O` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Rb+` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (0%) | `O=C1CCC(=O)N1Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1300  yield=62.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(OC)cc1.O=S([O-])C(F)(F)F.[Na+].N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.5%) | `platinum` (5.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (66.7%) | `graphite_generic` (8.0%) | `carbon_felt` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.8%) | `nickel` (8.2%) | `carbon` (3.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (49.1%) | `platinum_generic` (47.8%) | `iron_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.5%) | `Na` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (29.9%) | `BF4` (25.0%) | `PF6` (20.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (27.3%) | `alkali_carbonate` (2.1%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.2%) | `ketone` (10.8%) | `halogenated_aliphatic` (10.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (98%) | `CC(C)=O` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Rb+` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (0%) | `O=C1CCC(=O)N1Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1301  yield=66.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(OC)cc1.O=S([O-])C(F)(F)F.[Na+].N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.5%) | `platinum` (5.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (66.7%) | `graphite_generic` (8.0%) | `carbon_felt` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.8%) | `nickel` (8.2%) | `carbon` (3.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (49.1%) | `platinum_generic` (47.8%) | `iron_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.5%) | `Na` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (29.9%) | `BF4` (25.0%) | `PF6` (20.6%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (27.3%) | `alkali_carbonate` (2.1%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.2%) | `ketone` (10.8%) | `halogenated_aliphatic` (10.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (98%) | `CC(C)=O` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Rb+` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (0%) | `O=C1CCC(=O)N1Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1302  yield=53.0%

**Source paper**: [`GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC02920A_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(OC)cc1.O=S([O-])C(F)(F)F.[Na+].N=C(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.5%) | `platinum` (5.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (66.7%) | `graphite_generic` (8.0%) | `carbon_felt` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (82.8%) | `nickel` (8.2%) | `carbon` (3.7%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (49.1%) | `platinum_generic` (47.8%) | `iron_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.8%) | `Li` (9.5%) | `Na` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (29.9%) | `BF4` (25.0%) | `PF6` (20.6%) | ✓ |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (27.3%) | `alkali_carbonate` (2.1%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.2%) | `ketone` (10.8%) | `halogenated_aliphatic` (10.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (98%) | `CC(C)=O` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Rb+` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (0%) | `O=C1CCC(=O)N1Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1303  yield=44.0%

**Source paper**: [`GreenChem/10.1039_d5gc02920a_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02920a_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `ABSENT` (1.3%) | `platinum` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (58.0%) | `carbon_felt` (18.2%) | `boron_doped_diamond` (13.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `ABSENT` (1.5%) | `carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.8%) | `platinum_generic` (22.5%) | `platinum_foil` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.9%) | `ABSENT` (8.4%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.8%) | `Li` (20.7%) | `NEt4` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (51.4%) | `PF6` (21.2%) | `BF4` (21.1%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_sulfinate` (22.7%) | `alkali_sulfonate` (9.2%) | `carboxylic_acid` (5.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (38.9%) | `brønsted_acid_cat` (19.0%) | `Mn_complex` (16.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.4%) | `polar_aprotic_amide` (10.2%) | `polar_aprotic_sulfoxide` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (99%) | `CC(=O)O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `N=C(c1ccccc1)c1ccc` + `C1CN=C2NCCCN2C1` + `OC(C(F)(F)F)C(F)(F` | `OB(O)B(O)O` (69%) | `__OTHER__` (64%) | `O=O` (63%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (31%) | `Oc1ccccc1C=NCCN=Cc` (14%) | `__ABSENT__` (8%) | set ✓ / any ✓ |

---

### Reaction #1304  yield=59.0%

**Source paper**: [`GreenChem/10.1039_d5gc02920a_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02920a_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `ABSENT` (1.3%) | `platinum` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (58.0%) | `carbon_felt` (18.2%) | `boron_doped_diamond` (13.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `ABSENT` (1.5%) | `carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.8%) | `platinum_generic` (22.5%) | `platinum_foil` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.9%) | `ABSENT` (8.4%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.8%) | `Li` (20.7%) | `NEt4` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (51.4%) | `PF6` (21.2%) | `BF4` (21.1%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_sulfinate` (22.7%) | `alkali_sulfonate` (9.2%) | `carboxylic_acid` (5.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (38.9%) | `brønsted_acid_cat` (19.0%) | `Mn_complex` (16.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.4%) | `polar_aprotic_amide` (10.2%) | `polar_aprotic_sulfoxide` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (99%) | `CC(=O)O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `N=C(c1ccccc1)c1ccc` + `C1CN=C2NCCCN2C1` + `OC(C(F)(F)F)C(F)(F` | `OB(O)B(O)O` (69%) | `__OTHER__` (64%) | `O=O` (63%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (31%) | `Oc1ccccc1C=NCCN=Cc` (14%) | `__ABSENT__` (8%) | set ✓ / any ✓ |

---

### Reaction #1305  yield=52.0%

**Source paper**: [`GreenChem/10.1039_d5gc02920a_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02920a_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `ABSENT` (1.3%) | `platinum` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (58.0%) | `carbon_felt` (18.2%) | `boron_doped_diamond` (13.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `ABSENT` (1.5%) | `carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.8%) | `platinum_generic` (22.5%) | `platinum_foil` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.9%) | `ABSENT` (8.4%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (66.8%) | `Li` (20.7%) | `NEt4` (5.4%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (51.4%) | `PF6` (21.2%) | `BF4` (21.1%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_sulfinate` (22.7%) | `alkali_sulfonate` (9.2%) | `carboxylic_acid` (5.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (38.9%) | `brønsted_acid_cat` (19.0%) | `Mn_complex` (16.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.4%) | `polar_aprotic_amide` (10.2%) | `polar_aprotic_sulfoxide` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (99%) | `CC(=O)O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `N=C(c1ccccc1)c1ccc` + `C1CN=C2NCCCN2C1` + `OC(C(F)(F)F)C(F)(F` | `OB(O)B(O)O` (69%) | `__OTHER__` (64%) | `O=O` (63%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (31%) | `Oc1ccccc1C=NCCN=Cc` (14%) | `__ABSENT__` (8%) | set ✓ / any ✓ |

---

### Reaction #1306  yield=62.0%

**Source paper**: [`GreenChem/10.1039_d5gc02920a_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02920a_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `ABSENT` (1.3%) | `platinum` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (58.0%) | `carbon_felt` (18.2%) | `boron_doped_diamond` (13.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `ABSENT` (1.5%) | `carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.8%) | `platinum_generic` (22.5%) | `platinum_foil` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.9%) | `ABSENT` (8.4%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.8%) | `Li` (20.7%) | `NEt4` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (51.4%) | `PF6` (21.2%) | `BF4` (21.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_sulfinate` (22.7%) | `alkali_sulfonate` (9.2%) | `carboxylic_acid` (5.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (38.9%) | `brønsted_acid_cat` (19.0%) | `Mn_complex` (16.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.4%) | `polar_aprotic_amide` (10.2%) | `polar_aprotic_sulfoxide` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (99%) | `CC(=O)O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `N=C(c1ccccc1)c1ccc` + `C1CN=C2NCCCN2C1` + `OC(C(F)(F)F)C(F)(F` | `OB(O)B(O)O` (69%) | `__OTHER__` (64%) | `O=O` (63%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (31%) | `Oc1ccccc1C=NCCN=Cc` (14%) | `__ABSENT__` (8%) | set ✓ / any ✓ |

---

### Reaction #1307  yield=53.0%

**Source paper**: [`GreenChem/10.1039_d5gc02920a_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02920a_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `ABSENT` (1.3%) | `platinum` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (58.0%) | `carbon_felt` (18.2%) | `boron_doped_diamond` (13.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.5%) | `ABSENT` (1.5%) | `carbon` (1.0%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.8%) | `platinum_generic` (22.5%) | `platinum_foil` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.9%) | `ABSENT` (8.4%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.8%) | `Li` (20.7%) | `NEt4` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (51.4%) | `PF6` (21.2%) | `BF4` (21.1%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_sulfinate` (22.7%) | `alkali_sulfonate` (9.2%) | `carboxylic_acid` (5.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (38.9%) | `brønsted_acid_cat` (19.0%) | `Mn_complex` (16.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.4%) | `polar_aprotic_amide` (10.2%) | `polar_aprotic_sulfoxide` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (99%) | `CC(=O)O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `N=C(c1ccccc1)c1ccc` + `C1CN=C2NCCCN2C1` + `OC(C(F)(F)F)C(F)(F` | `OB(O)B(O)O` (69%) | `__OTHER__` (64%) | `O=O` (63%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (31%) | `Oc1ccccc1C=NCCN=Cc` (14%) | `__ABSENT__` (8%) | set ✓ / any ✓ |

---

### Reaction #1308  yield=57.0%

**Source paper**: [`GreenChem/10.1039_d5gc02920a_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02920a_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `ABSENT` (1.3%) | `platinum` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (58.0%) | `carbon_felt` (18.2%) | `boron_doped_diamond` (13.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `ABSENT` (1.5%) | `carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.8%) | `platinum_generic` (22.5%) | `platinum_foil` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.9%) | `ABSENT` (8.4%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.8%) | `Li` (20.7%) | `NEt4` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (51.4%) | `PF6` (21.2%) | `BF4` (21.1%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_sulfinate` (22.7%) | `alkali_sulfonate` (9.2%) | `carboxylic_acid` (5.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (38.9%) | `brønsted_acid_cat` (19.0%) | `Mn_complex` (16.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.4%) | `polar_aprotic_amide` (10.2%) | `polar_aprotic_sulfoxide` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (99%) | `CC(=O)O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `N=C(c1ccccc1)c1ccc` + `C1CN=C2NCCCN2C1` + `OC(C(F)(F)F)C(F)(F` | `OB(O)B(O)O` (69%) | `__OTHER__` (64%) | `O=O` (63%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (31%) | `Oc1ccccc1C=NCCN=Cc` (14%) | `__ABSENT__` (8%) | set ✓ / any ✓ |

---

### Reaction #1309  yield=0.0%

**Source paper**: [`GreenChem/10.1039_d5gc02920a_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02920a_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `ABSENT` (1.3%) | `platinum` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (58.0%) | `carbon_felt` (18.2%) | `boron_doped_diamond` (13.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `ABSENT` (1.5%) | `carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.8%) | `platinum_generic` (22.5%) | `platinum_foil` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.9%) | `ABSENT` (8.4%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.8%) | `Li` (20.7%) | `NEt4` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (51.4%) | `PF6` (21.2%) | `BF4` (21.1%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_sulfinate` (22.7%) | `alkali_sulfonate` (9.2%) | `carboxylic_acid` (5.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (38.9%) | `brønsted_acid_cat` (19.0%) | `Mn_complex` (16.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.4%) | `polar_aprotic_amide` (10.2%) | `polar_aprotic_sulfoxide` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (99%) | `CC(=O)O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `N=C(c1ccccc1)c1ccc` + `C1CN=C2NCCCN2C1` + `OC(C(F)(F)F)C(F)(F` | `OB(O)B(O)O` (69%) | `__OTHER__` (64%) | `O=O` (63%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (31%) | `Oc1ccccc1C=NCCN=Cc` (14%) | `__ABSENT__` (8%) | set ✓ / any ✓ |

---

### Reaction #1310  yield=68.0%

**Source paper**: [`GreenChem/10.1039_d5gc02920a_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02920a_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `ABSENT` (1.3%) | `platinum` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (58.0%) | `carbon_felt` (18.2%) | `boron_doped_diamond` (13.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `ABSENT` (1.5%) | `carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.8%) | `platinum_generic` (22.5%) | `platinum_foil` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.9%) | `ABSENT` (8.4%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.8%) | `Li` (20.7%) | `NEt4` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (51.4%) | `PF6` (21.2%) | `BF4` (21.1%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_sulfinate` (22.7%) | `alkali_sulfonate` (9.2%) | `carboxylic_acid` (5.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (38.9%) | `brønsted_acid_cat` (19.0%) | `Mn_complex` (16.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.4%) | `polar_aprotic_amide` (10.2%) | `polar_aprotic_sulfoxide` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (99%) | `CC(=O)O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `N=C(c1ccccc1)c1ccc` + `C1CN=C2NCCCN2C1` + `OC(C(F)(F)F)C(F)(F` | `OB(O)B(O)O` (69%) | `__OTHER__` (64%) | `O=O` (63%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (31%) | `Oc1ccccc1C=NCCN=Cc` (14%) | `__ABSENT__` (8%) | set ✓ / any ✓ |

---

### Reaction #1311  yield=65.0%

**Source paper**: [`GreenChem/10.1039_d5gc02920a_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02920a_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `ABSENT` (1.3%) | `platinum` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (58.0%) | `carbon_felt` (18.2%) | `boron_doped_diamond` (13.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `ABSENT` (1.5%) | `carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.8%) | `platinum_generic` (22.5%) | `platinum_foil` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.9%) | `ABSENT` (8.4%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.8%) | `Li` (20.7%) | `NEt4` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (51.4%) | `PF6` (21.2%) | `BF4` (21.1%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_sulfinate` (22.7%) | `alkali_sulfonate` (9.2%) | `carboxylic_acid` (5.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (38.9%) | `brønsted_acid_cat` (19.0%) | `Mn_complex` (16.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.4%) | `polar_aprotic_amide` (10.2%) | `polar_aprotic_sulfoxide` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (99%) | `CC(=O)O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `N=C(c1ccccc1)c1ccc` + `C1CN=C2NCCCN2C1` + `OC(C(F)(F)F)C(F)(F` | `OB(O)B(O)O` (69%) | `__OTHER__` (64%) | `O=O` (63%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (31%) | `Oc1ccccc1C=NCCN=Cc` (14%) | `__ABSENT__` (8%) | set ✓ / any ✓ |

---

### Reaction #1312  yield=66.0%

**Source paper**: [`GreenChem/10.1039_d5gc02920a_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02920a_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `ABSENT` (1.3%) | `platinum` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (58.0%) | `carbon_felt` (18.2%) | `boron_doped_diamond` (13.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `ABSENT` (1.5%) | `carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.8%) | `platinum_generic` (22.5%) | `platinum_foil` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.9%) | `ABSENT` (8.4%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.8%) | `Li` (20.7%) | `NEt4` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (51.4%) | `PF6` (21.2%) | `BF4` (21.1%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_sulfinate` (22.7%) | `alkali_sulfonate` (9.2%) | `carboxylic_acid` (5.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (38.9%) | `brønsted_acid_cat` (19.0%) | `Mn_complex` (16.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.4%) | `polar_aprotic_amide` (10.2%) | `polar_aprotic_sulfoxide` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (99%) | `CC(=O)O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `N=C(c1ccccc1)c1ccc` + `C1CN=C2NCCCN2C1` + `OC(C(F)(F)F)C(F)(F` | `OB(O)B(O)O` (69%) | `__OTHER__` (64%) | `O=O` (63%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (31%) | `Oc1ccccc1C=NCCN=Cc` (14%) | `__ABSENT__` (8%) | set ✓ / any ✓ |

---

### Reaction #1313  yield=51.0%

**Source paper**: [`GreenChem/10.1039_d5gc02920a_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02920a_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (97.6%) | `ABSENT` (1.3%) | `platinum` (1.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (58.0%) | `carbon_felt` (18.2%) | `boron_doped_diamond` (13.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `ABSENT` (1.5%) | `carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.8%) | `platinum_generic` (22.5%) | `platinum_foil` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.9%) | `ABSENT` (8.4%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.8%) | `Li` (20.7%) | `NEt4` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (51.4%) | `PF6` (21.2%) | `BF4` (21.1%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_sulfinate` (22.7%) | `alkali_sulfonate` (9.2%) | `carboxylic_acid` (5.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (38.9%) | `brønsted_acid_cat` (19.0%) | `Mn_complex` (16.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.4%) | `polar_aprotic_amide` (10.2%) | `polar_aprotic_sulfoxide` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (99%) | `CC(=O)O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `N=C(c1ccccc1)c1ccc` + `C1CN=C2NCCCN2C1` + `OC(C(F)(F)F)C(F)(F` | `OB(O)B(O)O` (69%) | `__OTHER__` (64%) | `O=O` (63%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (31%) | `Oc1ccccc1C=NCCN=Cc` (14%) | `__ABSENT__` (8%) | set ✓ / any ✓ |

---

### Reaction #1314  yield=72.0%

**Source paper**: [`GreenChem/10.1039_d5gc02920a_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02920a_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(OC)cc1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `ABSENT` (1.3%) | `platinum` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (58.0%) | `carbon_felt` (18.2%) | `boron_doped_diamond` (13.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `ABSENT` (1.5%) | `carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.8%) | `platinum_generic` (22.5%) | `platinum_foil` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.9%) | `ABSENT` (8.4%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.8%) | `Li` (20.7%) | `NEt4` (5.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (51.4%) | `PF6` (21.2%) | `BF4` (21.1%) | ✓ |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_sulfinate` (22.7%) | `alkali_sulfonate` (9.2%) | `carboxylic_acid` (5.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (38.9%) | `brønsted_acid_cat` (19.0%) | `Mn_complex` (16.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.4%) | `polar_aprotic_amide` (10.2%) | `polar_aprotic_sulfoxide` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (99%) | `CC(=O)O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `N=C(c1ccccc1)c1ccc` + `C1CN=C2NCCCN2C1` + `OC(C(F)(F)F)C(F)(F` | `OB(O)B(O)O` (69%) | `__OTHER__` (64%) | `O=O` (63%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (31%) | `Oc1ccccc1C=NCCN=Cc` (14%) | `__ABSENT__` (8%) | set ✓ / any ✓ |

---

### Reaction #1315  yield=80.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1316  yield=77.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1317  yield=57.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1318  yield=0.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✗ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1319  yield=80.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1320  yield=62.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aromatic_hydrocarbon` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✗ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1321  yield=63.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1322  yield=59.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1323  yield=24.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1324  yield=46.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1325  yield=43.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1326  yield=0.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1327  yield=55.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1328  yield=44.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1329  yield=57.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1330  yield=74.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1331  yield=77.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1332  yield=0.0%

**Source paper**: [`GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_D5GC03120F_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC=Cc1ccccc1>>COCC=CC(OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.7%) | `platinum` (14.1%) | `ABSENT` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `reticulated_vitreous_carbon` (58.3%) | `graphite_generic` (21.0%) | `carbon_felt` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (73.3%) | `platinum_plate` (21.3%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.4%) | `undivided` (6.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.0%) | `Li` (18.3%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (42.6%) | `ClO4` (25.1%) | `ABSENT` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `inorganic_simple` (6.5%) | `as_solvent_polar_protic_alcoho` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.9%) | `Mn_complex` (13.1%) | `Ni_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (31.4%) | `cyclic_ether` (23.9%) | `halogenated_aliphatic` (17.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `CO` | `CC#N` (83%) | `O` (39%) | `C[N+](=O)[O-]` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (84%) | `O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (74%) | `__OTHER__` (74%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #1333  yield=68.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1334  yield=42.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1335  yield=0.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1336  yield=68.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1337  yield=41.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NMe4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✗ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1338  yield=49.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1339  yield=29.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1340  yield=18.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✓ |
| 电解质 anion | 26 | `Br` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1341  yield=13.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1342  yield=30.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✗ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1343  yield=20.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `silver` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1344  yield=17.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `sacrificial_iron` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1345  yield=23.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_aluminum` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✗ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1346  yield=11.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `nickel` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✗ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1347  yield=24.0%

**Source paper**: [`GreenChem/10.1039_d5gc00295h_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc00295h_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>c1ccc(CCCCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (65.9%) | `sacrificial_zinc` (18.5%) | `platinum` (5.6%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `zinc_generic` (41.6%) | `graphite_rod` (16.5%) | `graphite_generic` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.0%) | `ABSENT` (13.1%) | `platinum` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `carbon_generic` (34.4%) | `graphite_rod` (13.3%) | `graphite_generic` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (84.7%) | `ABSENT` (14.1%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (8.1%) | `NEt4` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (81.7%) | `Br` (12.4%) | `BF4` (1.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.7%) | `bromide_anion` (5.1%) | `polyhalo_radical_transfer` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.1%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.4%) | `polar_aprotic_nitrile` (21.0%) | `aqueous` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (97%) | `C1COCCO1` (95%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `O=O` (100%) | `CC[Si](CC)CC` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1348  yield=12.0%

**Source paper**: [`GreenChem/10.1039_d5gc02319j_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02319j_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.COC(=O)NN>>CCCC(CC(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.1%) | `ABSENT` (7.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (96.1%) | `carbon_generic` (2.8%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.8%) | `ABSENT` (11.7%) | `sacrificial_iron` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `ABSENT` (0.4%) | `iron_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.6%) | `undivided` (5.8%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (48.7%) | `ABSENT` (43.7%) | `Na` (7.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (52.6%) | `BF4` (42.3%) | `Cl` (2.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `as_solvent_polar_protic_alcoho` (17.5%) | `ABSENT` (10.5%) | `tetraaryl_borate` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (93.8%) | `Co_complex` (1.9%) | `ferrocene_mediator` (1.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (95.9%) | `polar_aprotic_nitrile` (3.0%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (42%) | `CO` (33%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (91%) | `CO` (5%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Cl-].` + `__OTHER__` + `[Br-].[Br-].[Ni+2]` | `[Fe+2].c1ccc2c(c1)` (10%) | `__OTHER__` (7%) | `c1ccc2c(c1)-c1nc3c` (2%) | set ✗ / any ✓ |

---

### Reaction #1349  yield=0.0%

**Source paper**: [`GreenChem/10.1039_d5gc02319j_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02319j_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.COC(=O)NN>>CCCC(CC(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.1%) | `ABSENT` (7.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (96.1%) | `carbon_generic` (2.8%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.8%) | `ABSENT` (11.7%) | `sacrificial_iron` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `ABSENT` (0.4%) | `iron_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.6%) | `undivided` (5.8%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.7%) | `ABSENT` (43.7%) | `Na` (7.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (52.6%) | `BF4` (42.3%) | `Cl` (2.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `as_solvent_polar_protic_alcoho` (17.5%) | `ABSENT` (10.5%) | `tetraaryl_borate` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (93.8%) | `Co_complex` (1.9%) | `ferrocene_mediator` (1.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (95.9%) | `polar_aprotic_nitrile` (3.0%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (42%) | `CO` (33%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (91%) | `CO` (5%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Cl-].` + `__OTHER__` + `[Br-].[Br-].[Ni+2]` | `[Fe+2].c1ccc2c(c1)` (10%) | `__OTHER__` (7%) | `c1ccc2c(c1)-c1nc3c` (2%) | set ✗ / any ✓ |

---

### Reaction #1350  yield=0.0%

**Source paper**: [`GreenChem/10.1039_d5gc02319j_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02319j_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.COC(=O)NN>>CCCC(CC(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.1%) | `ABSENT` (7.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (96.1%) | `carbon_generic` (2.8%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.8%) | `ABSENT` (11.7%) | `sacrificial_iron` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `ABSENT` (0.4%) | `iron_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.6%) | `undivided` (5.8%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.7%) | `ABSENT` (43.7%) | `Na` (7.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (52.6%) | `BF4` (42.3%) | `Cl` (2.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `as_solvent_polar_protic_alcoho` (17.5%) | `ABSENT` (10.5%) | `tetraaryl_borate` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (93.8%) | `Co_complex` (1.9%) | `ferrocene_mediator` (1.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (95.9%) | `polar_aprotic_nitrile` (3.0%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (42%) | `CO` (33%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (91%) | `CO` (5%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Cl-].` + `__OTHER__` + `[Br-].[Br-].[Ni+2]` | `[Fe+2].c1ccc2c(c1)` (10%) | `__OTHER__` (7%) | `c1ccc2c(c1)-c1nc3c` (2%) | set ✗ / any ✓ |

---

### Reaction #1351  yield=32.0%

**Source paper**: [`GreenChem/10.1039_d5gc02319j_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02319j_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.COC(=O)NN>>CCCC(CC(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.1%) | `ABSENT` (7.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (96.1%) | `carbon_generic` (2.8%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.8%) | `ABSENT` (11.7%) | `sacrificial_iron` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `ABSENT` (0.4%) | `iron_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.6%) | `undivided` (5.8%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.7%) | `ABSENT` (43.7%) | `Na` (7.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (52.6%) | `BF4` (42.3%) | `Cl` (2.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `as_solvent_polar_protic_alcoho` (17.5%) | `ABSENT` (10.5%) | `tetraaryl_borate` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (93.8%) | `Co_complex` (1.9%) | `ferrocene_mediator` (1.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (95.9%) | `polar_aprotic_nitrile` (3.0%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (42%) | `CO` (33%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (91%) | `CO` (5%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Cl-].` + `__OTHER__` + `[Br-].[Br-].[Ni+2]` | `[Fe+2].c1ccc2c(c1)` (10%) | `__OTHER__` (7%) | `c1ccc2c(c1)-c1nc3c` (2%) | set ✗ / any ✓ |

---

### Reaction #1352  yield=46.0%

**Source paper**: [`GreenChem/10.1039_d5gc02319j_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02319j_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.COC(=O)NN>>CCCC(CC(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.1%) | `ABSENT` (7.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (96.1%) | `carbon_generic` (2.8%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.8%) | `ABSENT` (11.7%) | `sacrificial_iron` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `ABSENT` (0.4%) | `iron_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.6%) | `undivided` (5.8%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.7%) | `ABSENT` (43.7%) | `Na` (7.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (52.6%) | `BF4` (42.3%) | `Cl` (2.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `as_solvent_polar_protic_alcoho` (17.5%) | `ABSENT` (10.5%) | `tetraaryl_borate` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (93.8%) | `Co_complex` (1.9%) | `ferrocene_mediator` (1.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (95.9%) | `polar_aprotic_nitrile` (3.0%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (42%) | `CO` (33%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (91%) | `CO` (5%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Cl-].` + `__OTHER__` + `[Br-].[Br-].[Ni+2]` | `[Fe+2].c1ccc2c(c1)` (10%) | `__OTHER__` (7%) | `c1ccc2c(c1)-c1nc3c` (2%) | set ✗ / any ✓ |

---

### Reaction #1353  yield=0.0%

**Source paper**: [`GreenChem/10.1039_d5gc02319j_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02319j_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.COC(=O)NN>>CCCC(CC(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.1%) | `ABSENT` (7.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (96.1%) | `carbon_generic` (2.8%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.8%) | `ABSENT` (11.7%) | `sacrificial_iron` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `ABSENT` (0.4%) | `iron_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.6%) | `undivided` (5.8%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.7%) | `ABSENT` (43.7%) | `Na` (7.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (52.6%) | `BF4` (42.3%) | `Cl` (2.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `as_solvent_polar_protic_alcoho` (17.5%) | `ABSENT` (10.5%) | `tetraaryl_borate` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (93.8%) | `Co_complex` (1.9%) | `ferrocene_mediator` (1.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (95.9%) | `polar_aprotic_nitrile` (3.0%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (42%) | `CO` (33%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (91%) | `CO` (5%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Cl-].` + `__OTHER__` + `[Br-].[Br-].[Ni+2]` | `[Fe+2].c1ccc2c(c1)` (10%) | `__OTHER__` (7%) | `c1ccc2c(c1)-c1nc3c` (2%) | set ✗ / any ✓ |

---

### Reaction #1354  yield=0.0%

**Source paper**: [`GreenChem/10.1039_d5gc02319j_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02319j_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.COC(=O)NN>>CCCC(CC(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.1%) | `ABSENT` (7.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (96.1%) | `carbon_generic` (2.8%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.8%) | `ABSENT` (11.7%) | `sacrificial_iron` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `ABSENT` (0.4%) | `iron_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.6%) | `undivided` (5.8%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.7%) | `ABSENT` (43.7%) | `Na` (7.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (52.6%) | `BF4` (42.3%) | `Cl` (2.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `as_solvent_polar_protic_alcoho` (17.5%) | `ABSENT` (10.5%) | `tetraaryl_borate` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (93.8%) | `Co_complex` (1.9%) | `ferrocene_mediator` (1.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (95.9%) | `polar_aprotic_nitrile` (3.0%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (42%) | `CO` (33%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (91%) | `CO` (5%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Cl-].` + `__OTHER__` + `[Br-].[Br-].[Ni+2]` | `[Fe+2].c1ccc2c(c1)` (10%) | `__OTHER__` (7%) | `c1ccc2c(c1)-c1nc3c` (2%) | set ✗ / any ✓ |

---

### Reaction #1355  yield=0.0%

**Source paper**: [`GreenChem/10.1039_d5gc02319j_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02319j_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.COC(=O)NN>>CCCC(CC(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.1%) | `ABSENT` (7.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (96.1%) | `carbon_generic` (2.8%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.8%) | `ABSENT` (11.7%) | `sacrificial_iron` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `ABSENT` (0.4%) | `iron_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.6%) | `undivided` (5.8%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.7%) | `ABSENT` (43.7%) | `Na` (7.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (52.6%) | `BF4` (42.3%) | `Cl` (2.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `as_solvent_polar_protic_alcoho` (17.5%) | `ABSENT` (10.5%) | `tetraaryl_borate` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (93.8%) | `Co_complex` (1.9%) | `ferrocene_mediator` (1.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (95.9%) | `polar_aprotic_nitrile` (3.0%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (42%) | `CO` (33%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (91%) | `CO` (5%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Cl-].` + `__OTHER__` + `[Br-].[Br-].[Ni+2]` | `[Fe+2].c1ccc2c(c1)` (10%) | `__OTHER__` (7%) | `c1ccc2c(c1)-c1nc3c` (2%) | set ✗ / any ✓ |

---

### Reaction #1356  yield=0.0%

**Source paper**: [`GreenChem/10.1039_d5gc02319j_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02319j_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.COC(=O)NN>>CCCC(CC(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.1%) | `ABSENT` (7.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (96.1%) | `carbon_generic` (2.8%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (85.8%) | `ABSENT` (11.7%) | `sacrificial_iron` (2.1%) | ✗ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `ABSENT` (0.4%) | `iron_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.6%) | `undivided` (5.8%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.7%) | `ABSENT` (43.7%) | `Na` (7.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (52.6%) | `BF4` (42.3%) | `Cl` (2.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `as_solvent_polar_protic_alcoho` (17.5%) | `ABSENT` (10.5%) | `tetraaryl_borate` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (93.8%) | `Co_complex` (1.9%) | `ferrocene_mediator` (1.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (95.9%) | `polar_aprotic_nitrile` (3.0%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (42%) | `CO` (33%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (91%) | `CO` (5%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Cl-].` + `__OTHER__` + `[Br-].[Br-].[Ni+2]` | `[Fe+2].c1ccc2c(c1)` (10%) | `__OTHER__` (7%) | `c1ccc2c(c1)-c1nc3c` (2%) | set ✗ / any ✓ |

---

### Reaction #1357  yield=88.0%

**Source paper**: [`GreenChem/10.1039_d5gc02319j_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02319j_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.COC(=O)NN>>CCCC(CC(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.1%) | `ABSENT` (7.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (96.1%) | `carbon_generic` (2.8%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.8%) | `ABSENT` (11.7%) | `sacrificial_iron` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `ABSENT` (0.4%) | `iron_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.6%) | `undivided` (5.8%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.7%) | `ABSENT` (43.7%) | `Na` (7.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (52.6%) | `BF4` (42.3%) | `Cl` (2.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (17.5%) | `ABSENT` (10.5%) | `tetraaryl_borate` (2.0%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (93.8%) | `Co_complex` (1.9%) | `ferrocene_mediator` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (95.9%) | `polar_aprotic_nitrile` (3.0%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (42%) | `CO` (33%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (91%) | `CO` (5%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Cl-].` + `__OTHER__` + `[Br-].[Br-].[Ni+2]` | `[Fe+2].c1ccc2c(c1)` (10%) | `__OTHER__` (7%) | `c1ccc2c(c1)-c1nc3c` (2%) | set ✗ / any ✓ |

---

### Reaction #1358  yield=0.0%

**Source paper**: [`GreenChem/10.1039_d5gc02319j_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02319j_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.COC(=O)NN>>CCCC(CC(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.1%) | `ABSENT` (7.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (96.1%) | `carbon_generic` (2.8%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.8%) | `ABSENT` (11.7%) | `sacrificial_iron` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `ABSENT` (0.4%) | `iron_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.6%) | `undivided` (5.8%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.7%) | `ABSENT` (43.7%) | `Na` (7.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (52.6%) | `BF4` (42.3%) | `Cl` (2.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (17.5%) | `ABSENT` (10.5%) | `tetraaryl_borate` (2.0%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (93.8%) | `Co_complex` (1.9%) | `ferrocene_mediator` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (95.9%) | `polar_aprotic_nitrile` (3.0%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (42%) | `CO` (33%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (91%) | `CO` (5%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Cl-].` + `__OTHER__` + `[Br-].[Br-].[Ni+2]` | `[Fe+2].c1ccc2c(c1)` (10%) | `__OTHER__` (7%) | `c1ccc2c(c1)-c1nc3c` (2%) | set ✗ / any ✓ |

---

### Reaction #1359  yield=0.0%

**Source paper**: [`GreenChem/10.1039_d5gc02319j_p2_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02319j_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.COC(=O)NN>>CCCC(CC(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.1%) | `ABSENT` (7.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (96.1%) | `carbon_generic` (2.8%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.8%) | `ABSENT` (11.7%) | `sacrificial_iron` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `ABSENT` (0.4%) | `iron_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (93.6%) | `undivided` (5.8%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NMe4` | `NBu4` (48.7%) | `ABSENT` (43.7%) | `Na` (7.3%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (52.6%) | `BF4` (42.3%) | `Cl` (2.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `as_solvent_polar_protic_alcoho` (17.5%) | `ABSENT` (10.5%) | `tetraaryl_borate` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (93.8%) | `Co_complex` (1.9%) | `ferrocene_mediator` (1.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (95.9%) | `polar_aprotic_nitrile` (3.0%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (42%) | `CO` (33%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (91%) | `CO` (5%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Cl-].` + `__OTHER__` + `[Br-].[Br-].[Ni+2]` | `[Fe+2].c1ccc2c(c1)` (10%) | `__OTHER__` (7%) | `c1ccc2c(c1)-c1nc3c` (2%) | set ✗ / any ✓ |

---

### Reaction #1360  yield=83.0%

**Source paper**: [`GreenChem/10.1039_d5gc02979a_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02979a_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(Cc1ccccc1)Cc1ccccc1>>CC(Cc1ccccc1)(Cc1ccccc1)C(C)(Cc1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (86.2%) | `platinum` (12.5%) | `sacrificial_zinc` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (23.4%) | `platinum_plate` (15.7%) | `reticulated_vitreous_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (82.6%) | `nickel` (10.0%) | `carbon` (6.6%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (52.6%) | `platinum_plate` (35.4%) | `nickel_foam` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.7%) | `Li` (28.8%) | `H` (6.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (38.5%) | `molecular_no_ion` (17.1%) | `Br` (12.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `o2_oxidant` (4.4%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `pyridine_organocat` (7.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.2%) | `polar_protic_alcohol` (10.5%) | `ABSENT` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (10%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (33%) | `OB(O)B(O)O` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1361  yield=18.0%

**Source paper**: [`GreenChem/10.1039_d5gc02979a_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02979a_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(Cc1ccccc1)Cc1ccccc1>>CC(Cc1ccccc1)(Cc1ccccc1)C(C)(Cc1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (86.2%) | `platinum` (12.5%) | `sacrificial_zinc` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (23.4%) | `platinum_plate` (15.7%) | `reticulated_vitreous_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (82.6%) | `nickel` (10.0%) | `carbon` (6.6%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (52.6%) | `platinum_plate` (35.4%) | `nickel_foam` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.7%) | `Li` (28.8%) | `H` (6.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (38.5%) | `molecular_no_ion` (17.1%) | `Br` (12.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `o2_oxidant` (4.4%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `pyridine_organocat` (7.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.2%) | `polar_protic_alcohol` (10.5%) | `ABSENT` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (10%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (33%) | `OB(O)B(O)O` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1362  yield=53.0%

**Source paper**: [`GreenChem/10.1039_d5gc02979a_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02979a_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(Cc1ccccc1)Cc1ccccc1>>CC(Cc1ccccc1)(Cc1ccccc1)C(C)(Cc1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_aluminum` | `carbon` (86.2%) | `platinum` (12.5%) | `sacrificial_zinc` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (23.4%) | `platinum_plate` (15.7%) | `reticulated_vitreous_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (82.6%) | `nickel` (10.0%) | `carbon` (6.6%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (52.6%) | `platinum_plate` (35.4%) | `nickel_foam` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.7%) | `Li` (28.8%) | `H` (6.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (38.5%) | `molecular_no_ion` (17.1%) | `Br` (12.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `o2_oxidant` (4.4%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `pyridine_organocat` (7.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.2%) | `polar_protic_alcohol` (10.5%) | `ABSENT` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (10%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (33%) | `OB(O)B(O)O` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1363  yield=0.5%

**Source paper**: [`GreenChem/10.1039_d5gc02979a_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02979a_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(Cc1ccccc1)Cc1ccccc1>>CC(Cc1ccccc1)(Cc1ccccc1)C(C)(Cc1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (86.2%) | `platinum` (12.5%) | `sacrificial_zinc` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (23.4%) | `platinum_plate` (15.7%) | `reticulated_vitreous_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (82.6%) | `nickel` (10.0%) | `carbon` (6.6%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (52.6%) | `platinum_plate` (35.4%) | `nickel_foam` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (43.7%) | `Li` (28.8%) | `H` (6.9%) | ✓ |
| 电解质 anion | 26 | `Br` | `ClO4` (38.5%) | `molecular_no_ion` (17.1%) | `Br` (12.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `o2_oxidant` (4.4%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `pyridine_organocat` (7.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.2%) | `polar_protic_alcohol` (10.5%) | `ABSENT` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (10%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (33%) | `OB(O)B(O)O` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1364  yield=15.0%

**Source paper**: [`GreenChem/10.1039_d5gc02979a_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02979a_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(Cc1ccccc1)Cc1ccccc1>>CC(Cc1ccccc1)(Cc1ccccc1)C(C)(Cc1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (86.2%) | `platinum` (12.5%) | `sacrificial_zinc` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (23.4%) | `platinum_plate` (15.7%) | `reticulated_vitreous_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (82.6%) | `nickel` (10.0%) | `carbon` (6.6%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (52.6%) | `platinum_plate` (35.4%) | `nickel_foam` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.7%) | `Li` (28.8%) | `H` (6.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (38.5%) | `molecular_no_ion` (17.1%) | `Br` (12.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `o2_oxidant` (4.4%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `pyridine_organocat` (7.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.2%) | `polar_protic_alcohol` (10.5%) | `ABSENT` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (10%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (33%) | `OB(O)B(O)O` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1365  yield=40.0%

**Source paper**: [`GreenChem/10.1039_d5gc02979a_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02979a_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(Cc1ccccc1)Cc1ccccc1>>CC(Cc1ccccc1)(Cc1ccccc1)C(C)(Cc1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (86.2%) | `platinum` (12.5%) | `sacrificial_zinc` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (23.4%) | `platinum_plate` (15.7%) | `reticulated_vitreous_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.6%) | `nickel` (10.0%) | `carbon` (6.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (52.6%) | `platinum_plate` (35.4%) | `nickel_foam` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.7%) | `Li` (28.8%) | `H` (6.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (38.5%) | `molecular_no_ion` (17.1%) | `Br` (12.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `o2_oxidant` (4.4%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `pyridine_organocat` (7.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.2%) | `polar_protic_alcohol` (10.5%) | `ABSENT` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (10%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (33%) | `OB(O)B(O)O` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1366  yield=72.0%

**Source paper**: [`GreenChem/10.1039_d5gc02979a_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02979a_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(Cc1ccccc1)Cc1ccccc1>>CC(Cc1ccccc1)(Cc1ccccc1)C(C)(Cc1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (86.2%) | `platinum` (12.5%) | `sacrificial_zinc` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (23.4%) | `platinum_plate` (15.7%) | `reticulated_vitreous_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (82.6%) | `nickel` (10.0%) | `carbon` (6.6%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (52.6%) | `platinum_plate` (35.4%) | `nickel_foam` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.7%) | `Li` (28.8%) | `H` (6.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `ClO4` (38.5%) | `molecular_no_ion` (17.1%) | `Br` (12.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `o2_oxidant` (4.4%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `pyridine_organocat` (7.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.2%) | `polar_protic_alcohol` (10.5%) | `ABSENT` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (10%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (33%) | `OB(O)B(O)O` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1367  yield=66.0%

**Source paper**: [`GreenChem/10.1039_d5gc02979a_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02979a_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(Cc1ccccc1)Cc1ccccc1>>CC(Cc1ccccc1)(Cc1ccccc1)C(C)(Cc1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (86.2%) | `platinum` (12.5%) | `sacrificial_zinc` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (23.4%) | `platinum_plate` (15.7%) | `reticulated_vitreous_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (82.6%) | `nickel` (10.0%) | `carbon` (6.6%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (52.6%) | `platinum_plate` (35.4%) | `nickel_foam` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.7%) | `Li` (28.8%) | `H` (6.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (38.5%) | `molecular_no_ion` (17.1%) | `Br` (12.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `o2_oxidant` (4.4%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `pyridine_organocat` (7.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.2%) | `polar_protic_alcohol` (10.5%) | `ABSENT` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (10%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (33%) | `OB(O)B(O)O` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1368  yield=75.0%

**Source paper**: [`GreenChem/10.1039_d5gc02979a_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02979a_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(Cc1ccccc1)Cc1ccccc1>>CC(Cc1ccccc1)(Cc1ccccc1)C(C)(Cc1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (86.2%) | `platinum` (12.5%) | `sacrificial_zinc` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (23.4%) | `platinum_plate` (15.7%) | `reticulated_vitreous_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (82.6%) | `nickel` (10.0%) | `carbon` (6.6%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (52.6%) | `platinum_plate` (35.4%) | `nickel_foam` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.7%) | `Li` (28.8%) | `H` (6.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `ClO4` (38.5%) | `molecular_no_ion` (17.1%) | `Br` (12.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `o2_oxidant` (4.4%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `pyridine_organocat` (7.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.2%) | `polar_protic_alcohol` (10.5%) | `ABSENT` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (10%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (33%) | `OB(O)B(O)O` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1369  yield=40.0%

**Source paper**: [`GreenChem/10.1039_d5gc02979a_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02979a_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(Cc1ccccc1)Cc1ccccc1>>CC(Cc1ccccc1)(Cc1ccccc1)C(C)(Cc1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (86.2%) | `platinum` (12.5%) | `sacrificial_zinc` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (23.4%) | `platinum_plate` (15.7%) | `reticulated_vitreous_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (82.6%) | `nickel` (10.0%) | `carbon` (6.6%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (52.6%) | `platinum_plate` (35.4%) | `nickel_foam` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.7%) | `Li` (28.8%) | `H` (6.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (38.5%) | `molecular_no_ion` (17.1%) | `Br` (12.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `o2_oxidant` (4.4%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `pyridine_organocat` (7.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.2%) | `polar_protic_alcohol` (10.5%) | `ABSENT` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (10%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (33%) | `OB(O)B(O)O` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1370  yield=0.0%

**Source paper**: [`GreenChem/10.1039_d5gc02979a_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02979a_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(Cc1ccccc1)Cc1ccccc1>>CC(Cc1ccccc1)(Cc1ccccc1)C(C)(Cc1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (86.2%) | `platinum` (12.5%) | `sacrificial_zinc` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (23.4%) | `platinum_plate` (15.7%) | `reticulated_vitreous_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (82.6%) | `nickel` (10.0%) | `carbon` (6.6%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (52.6%) | `platinum_plate` (35.4%) | `nickel_foam` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.7%) | `Li` (28.8%) | `H` (6.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (38.5%) | `molecular_no_ion` (17.1%) | `Br` (12.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `o2_oxidant` (4.4%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `pyridine_organocat` (7.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.2%) | `polar_protic_alcohol` (10.5%) | `ABSENT` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (10%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (33%) | `OB(O)B(O)O` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1371  yield=61.0%

**Source paper**: [`GreenChem/10.1039_d5gc02979a_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02979a_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(Cc1ccccc1)Cc1ccccc1>>CC(Cc1ccccc1)(Cc1ccccc1)C(C)(Cc1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (86.2%) | `platinum` (12.5%) | `sacrificial_zinc` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (23.4%) | `platinum_plate` (15.7%) | `reticulated_vitreous_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (82.6%) | `nickel` (10.0%) | `carbon` (6.6%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (52.6%) | `platinum_plate` (35.4%) | `nickel_foam` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.7%) | `Li` (28.8%) | `H` (6.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (38.5%) | `molecular_no_ion` (17.1%) | `Br` (12.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `o2_oxidant` (4.4%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `pyridine_organocat` (7.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (67.2%) | `polar_protic_alcohol` (10.5%) | `ABSENT` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (10%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (33%) | `OB(O)B(O)O` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1372  yield=0.0%

**Source paper**: [`GreenChem/10.1039_d5gc02979a_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02979a_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(Cc1ccccc1)Cc1ccccc1>>CC(Cc1ccccc1)(Cc1ccccc1)C(C)(Cc1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (86.2%) | `platinum` (12.5%) | `sacrificial_zinc` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (23.4%) | `platinum_plate` (15.7%) | `reticulated_vitreous_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (82.6%) | `nickel` (10.0%) | `carbon` (6.6%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (52.6%) | `platinum_plate` (35.4%) | `nickel_foam` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.7%) | `Li` (28.8%) | `H` (6.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (38.5%) | `molecular_no_ion` (17.1%) | `Br` (12.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `o2_oxidant` (4.4%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `pyridine_organocat` (7.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (67.2%) | `polar_protic_alcohol` (10.5%) | `ABSENT` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (10%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (33%) | `OB(O)B(O)O` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1373  yield=0.0%

**Source paper**: [`GreenChem/10.1039_d5gc02979a_p3_t0.json`](reactions_by_journal_alkene_ec_audited/GreenChem/10.1039_d5gc02979a_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(Cc1ccccc1)Cc1ccccc1>>CC(Cc1ccccc1)(Cc1ccccc1)C(C)(Cc1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (86.2%) | `platinum` (12.5%) | `sacrificial_zinc` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (23.4%) | `platinum_plate` (15.7%) | `reticulated_vitreous_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (82.6%) | `nickel` (10.0%) | `carbon` (6.6%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (52.6%) | `platinum_plate` (35.4%) | `nickel_foam` (4.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.7%) | `Li` (28.8%) | `H` (6.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (38.5%) | `molecular_no_ion` (17.1%) | `Br` (12.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.1%) | `o2_oxidant` (4.4%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `pyridine_organocat` (7.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.2%) | `polar_protic_alcohol` (10.5%) | `ABSENT` (5.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (10%) | `ClCCl` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (33%) | `OB(O)B(O)O` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `c1ccncc1` (11%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1374  yield=41.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1375  yield=83.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1376  yield=21.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1377  yield=36.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1378  yield=48.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1379  yield=27.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1380  yield=74.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1381  yield=0.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1382  yield=72.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✓ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1383  yield=75.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1384  yield=80.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✓ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1385  yield=0.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1386  yield=70.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1387  yield=80.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1388  yield=77.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1389  yield=0.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1390  yield=83.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1391  yield=21.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1392  yield=41.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1393  yield=27.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1394  yield=74.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✓ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1395  yield=48.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1396  yield=0.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1397  yield=36.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1398  yield=80.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✓ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1399  yield=72.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✓ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1400  yield=0.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✓ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1401  yield=70.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1402  yield=75.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1403  yield=0.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1404  yield=0.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (66.5%) | `platinum_generic` (31.2%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `Li` (3.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (38.9%) | `BF4` (18.2%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `water` | `azide_source` (4.9%) | `alkali_sulfonate` (4.4%) | `ABSENT` (4.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (35.9%) | `polar_aprotic_nitrile` (31.0%) | `ABSENT` (16.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `FC(F)(F)c1ccccc1` (46%) | `CC#N` (41%) | `CC(=O)O` (29%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (57%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #1405  yield=94.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_7_e202420188.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_7_e202420188.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(Cl)cc1>>Clc1ccc(C2CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (76.9%) | `platinum` (15.2%) | `ABSENT` (7.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (94.8%) | `glassy_carbon` (3.0%) | `boron_doped_diamond` (0.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.0%) | `ABSENT` (1.4%) | `stainless_steel` (0.8%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (82.5%) | `platinum_generic` (9.2%) | `platinum_wire` (4.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.3%) | `ABSENT` (1.7%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `ABSENT` (72.3%) | `NBu4` (14.2%) | `K` (8.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (79.9%) | `BF4` (8.4%) | `PF6` (6.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (14.3%) | `alkali_sulfinate` (7.3%) | `carboxylic_acid` (4.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (89.1%) | `ABSENT` (7.2%) | `Mn_complex` (1.7%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (73.8%) | `aqueous` (16.0%) | `polar_aprotic_sulfoxide` (4.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (97%) | `CC#N` (91%) | `CC(C)=O` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (80%) | `O` (61%) | `O.O.O.O.O.O.O.O.O.` (46%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #1406  yield=99.0%

**Source paper**: [`GreenChem/2012_Green_Chemistry_2012_14_8_2221-2225.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2012_Green_Chemistry_2012_14_8_2221-2225.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1ccc(F)cc1>>Fc1ccc(C2CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.3%) | `platinum` (6.1%) | `ABSENT` (3.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_paper` | `carbon_generic` (92.5%) | `graphite_rod` (1.5%) | `glassy_carbon` (1.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.3%) | `carbon` (2.1%) | `ABSENT` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (92.1%) | `platinum_generic` (4.0%) | `platinum_wire` (1.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.0%) | `ABSENT` (1.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `ABSENT` (85.6%) | `NBu4` (8.6%) | `K` (1.8%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (89.0%) | `PF6` (4.0%) | `BF4` (2.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (23.8%) | `carboxylic_acid` (5.7%) | `ABSENT` (2.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (95.8%) | `ABSENT` (2.3%) | `Mn_complex` (1.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.8%) | `ABSENT` (6.3%) | `aqueous` (4.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (96%) | `O` (54%) | `CN(C)C=O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (80%) | `__OTHER__` (59%) | `CC[Si](CC)CC` (57%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Mn+2]` | `c1ccncc1` (98%) | `__OTHER__` (92%) | `[Cl-].[Cl-].[Mn+2]` (5%) | set ✗ / any ✓ |

---

### Reaction #1407  yield=60.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCO.C=CNC(=O)c1ccccc1>>C=CCCOC1COC(c2ccccc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.7%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (71.1%) | `graphite_generic` (24.8%) | `graphite_rod` (3.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (54.2%) | `stainless_steel` (40.8%) | `nickel` (3.9%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (56.8%) | `platinum_generic` (26.9%) | `stainless_steel_generic` (9.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (58.4%) | `ABSENT` (39.8%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ABSENT` (58.2%) | `BF4` (29.5%) | `PF6` (4.5%) | ✓ |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (7.6%) | `iodide_anion` (3.5%) | `inorganic_simple` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (45.9%) | `ABSENT` (28.9%) | `organic_neutral_cat` (16.3%) | ✓ |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (97.4%) | `polar_aprotic_amide` (1.0%) | `halogenated_aliphatic` (0.7%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `O` (8%) | `ClCCl` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (60%) | `[Cl-].[Na+]` (3%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (9%) | `__OTHER__` (1%) | `__ABSENT__` (0%) | set ✗ / any ✓ |

---

### Reaction #1408  yield=60.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #1)

```
CCCCCCCCCCCCCCCC(=O)O.C=CNC(=O)c1ccccc1>>CCCCCCCCCCCCCCCC(=O)OC1COC(c2ccccc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (93.9%) | `graphite_generic` (4.0%) | `carbon_felt` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (96.4%) | `nickel` (2.0%) | `platinum` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (82.8%) | `stainless_steel_generic` (16.0%) | `platinum_plate` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.7%) | `ABSENT` (1.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.9%) | `ABSENT` (7.3%) | `Li` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (70.5%) | `Br` (17.5%) | `ABSENT` (6.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (18.1%) | `ABSENT` (5.2%) | `boron_lewis_acid` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (94.2%) | `pyridine_organocat` (1.8%) | `organic_neutral_cat` (1.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.1%) | `halogenated_aliphatic` (0.9%) | `ketone` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (5%) | `O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `[Cl-].[Na+]` (95%) | `[Cl-].[Cl-].[Mg+2]` (1%) | `[Br-].[K+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (97%) | `[I-].[K+]` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #1409  yield=55.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #2)

```
O=C(O)c1ccc(Br)cc1.C=CNC(=O)c1ccccc1>>O=C(OC1COC(c2ccccc2)=N1)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (89.0%) | `graphite_rod` (4.5%) | `graphite_generic` (3.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (66.4%) | `carbon` (11.7%) | `nickel` (11.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (87.8%) | `platinum_plate` (3.5%) | `graphite_rod` (2.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.9%) | `ABSENT` (6.0%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (68.5%) | `Br` (11.9%) | `ABSENT` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (15.7%) | `chloride_anion` (7.2%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (81.8%) | `ABSENT` (13.6%) | `pyridine_organocat` (3.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.1%) | `polar_aprotic_amide` (0.3%) | `ketone` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `[Cl-].[Na+]` (51%) | `__ABSENT__` (44%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (73%) | `__OTHER__` (0%) | `__ABSENT__` (0%) | set ✗ / any ✓ |

---

### Reaction #1410  yield=57.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #3)

```
C=CNC(=O)c1ccco1>>OC1COC(c2ccco2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (94.3%) | `graphite_generic` (3.2%) | `carbon_felt` (2.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (98.0%) | `stainless_steel_generic` (1.9%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.5%) | `ABSENT` (2.9%) | `Li` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (85.3%) | `Br` (8.7%) | `ABSENT` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (25.4%) | `ABSENT` (5.5%) | `hcl` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (98.7%) | `pyridine_organocat` (0.6%) | `ABSENT` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.7%) | `ketone` (1.5%) | `polar_aprotic_amide` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (6%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `[Br-].[K+]` (1%) | `CCOC(C)=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (100%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #1411  yield=64.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #4)

```
C=CNC(=O)c1ccc(Br)nc1>>OC1COC(c2ccc(Br)nc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.5%) | `carbon_felt` (0.3%) | `graphite_felt` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.5%) | `nickel` (0.2%) | `carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (99.6%) | `stainless_steel_generic` (0.4%) | `platinum_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (98.5%) | `ABSENT` (0.8%) | `alkyl_ammonium` (0.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (90.0%) | `Br` (7.3%) | `ABSENT` (0.9%) | ✓ |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (25.5%) | `ABSENT` (8.2%) | `hcl` (3.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (98.9%) | `pyridine_organocat` (0.6%) | `ABSENT` (0.3%) | ✓ |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (97.5%) | `polar_aprotic_amide` (1.3%) | `ketone` (0.8%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `O` (1%) | `[H+].[OH-]` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `O` (0%) | `Cl` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (100%) | `[I-].[K+]` (1%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1412  yield=68.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #5)

```
C=CNC(=O)c1cccc(Cl)c1>>OC1COC(c2cccc(Cl)c2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.0%) | `carbon_felt` (0.5%) | `graphite_generic` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.2%) | `nickel` (0.4%) | `platinum` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (97.6%) | `stainless_steel_generic` (2.2%) | `platinum_plate` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.4%) | `ABSENT` (1.8%) | `Na` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (93.5%) | `Br` (2.8%) | `ABSENT` (2.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (12.7%) | `ABSENT` (10.7%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (98.7%) | `pyridine_organocat` (0.6%) | `ABSENT` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.9%) | `ketone` (1.6%) | `polar_aprotic_amide` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (1%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `O` (0%) | `[Br-].[K+]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (98%) | `[I-].[K+]` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #1413  yield=68.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #6)

```
C=CNC(=O)c1c(C)cc(C)cc1C>>Cc1cc(C)c(C2=NC(O)CO2)c(C)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (89.1%) | `carbon_felt` (5.1%) | `graphite_generic` (2.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.8%) | `platinum` (0.1%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (72.4%) | `stainless_steel_generic` (25.0%) | `platinum_plate` (1.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (60.4%) | `NBu4` (36.0%) | `Li` (1.4%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (46.5%) | `ABSENT` (42.5%) | `Br` (8.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (17.9%) | `ABSENT` (6.3%) | `hcl` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (96.2%) | `pyridine_organocat` (1.4%) | `ABSENT` (1.0%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (93.8%) | `polar_aprotic_amide` (2.6%) | `ketone` (2.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (1%) | `CN(C)C=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `O` (1%) | `[Br-].[K+]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (99%) | `[I-].[K+]` (1%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1414  yield=66.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #7)

```
C=CNC(=O)c1ccc(OC)cc1>>COc1ccc(C2=NC(O)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (97.0%) | `carbon_felt` (2.2%) | `graphite_generic` (0.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.2%) | `nickel` (0.4%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (98.6%) | `stainless_steel_generic` (1.0%) | `platinum_plate` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.2%) | `ABSENT` (1.4%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (78.0%) | `Br` (17.1%) | `Cl` (1.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (13.6%) | `ABSENT` (12.7%) | `metal_oxide_oxidant` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (98.7%) | `ABSENT` (0.7%) | `pyridine_organocat` (0.4%) | ✓ |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (97.2%) | `polar_aprotic_amide` (1.4%) | `ketone` (0.8%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `O` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `__OTHER__` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (100%) | `[I-].[K+]` (1%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1415  yield=63.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #8)

```
C#CCCO.C=CNC(=O)c1ccccc1>>C#CCCOC1COC(c2ccccc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (66.3%) | `graphite_generic` (33.4%) | `graphite_rod` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (63.4%) | `platinum` (34.3%) | `nickel` (1.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_generic` (68.0%) | `platinum_plate` (15.7%) | `stainless_steel_plate` (9.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.1%) | `NEt4` (0.3%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (64.6%) | `PF6` (15.9%) | `I` (7.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (9.0%) | `chloride_anion` (6.4%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (87.1%) | `organic_neutral_cat` (4.6%) | `ABSENT` (4.5%) | ✓ |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (98.2%) | `ABSENT` (0.8%) | `ketone` (0.3%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (59%) | `[Cl-].[Na+]` (38%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (66%) | `[I-].[K+]` (0%) | `__ABSENT__` (0%) | set ✗ / any ✓ |

---

### Reaction #1416  yield=70.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #9)

```
Cc1ccc(C(=O)O)cc1.C=CNC(=O)c1ccccc1>>Cc1ccc(C(=O)OC2COC(c3ccccc3)=N2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.2%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (93.3%) | `graphite_generic` (2.4%) | `graphite_rod` (2.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (71.8%) | `nickel` (14.6%) | `platinum` (8.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (82.8%) | `stainless_steel_generic` (5.6%) | `platinum_plate` (5.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (87.5%) | `ABSENT` (9.5%) | `Na` (1.6%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (72.2%) | `ABSENT` (10.8%) | `Br` (8.5%) | ✓ |
| 试剂大类 | 103 | `inorganic_simple` | `ABSENT` (13.8%) | `chloride_anion` (9.7%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (93.5%) | `ABSENT` (3.2%) | `pyridine_organocat` (1.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.0%) | `halogenated_aliphatic` (1.6%) | `polar_aprotic_amide` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (2%) | `O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Na][Br]` | `__ABSENT__` (50%) | `[Cl-].[Na+]` (33%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (80%) | `[I-].[K+]` (0%) | `O=C([O-])c1ccccc1-` (0%) | set ✗ / any ✗ |

---

### Reaction #1417  yield=70.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #10)

```
C=CNC(=O)c1ccc(-c2ccccc2)cc1>>OC1COC(c2ccc(-c3ccccc3)cc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (97.9%) | `graphite_generic` (0.9%) | `carbon_felt` (0.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (98.1%) | `nickel` (1.1%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (97.8%) | `stainless_steel_generic` (1.7%) | `platinum_plate` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.6%) | `ABSENT` (1.8%) | `Li` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (68.0%) | `Br` (22.9%) | `Cl` (3.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (23.9%) | `ABSENT` (7.4%) | `hcl` (4.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (97.4%) | `pyridine_organocat` (1.9%) | `organic_neutral_cat` (0.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.8%) | `ketone` (1.1%) | `polar_aprotic_amide` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `O` (0%) | `Cl` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (87%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #1418  yield=80.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #11)

```
C=CNC(=O)c1ccc(F)cc1>>OC1COC(c2ccc(F)cc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `sacrificial_iron` (0.1%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (94.4%) | `carbon_felt` (2.6%) | `graphite_generic` (1.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.7%) | `nickel` (0.1%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (93.9%) | `stainless_steel_generic` (5.8%) | `platinum_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (80.7%) | `ABSENT` (13.3%) | `alkyl_ammonium` (2.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `BF4` (61.7%) | `Br` (23.3%) | `ABSENT` (9.7%) | ✓ |
| 试剂大类 | 103 | `boron_lewis_acid` | `chloride_anion` (22.3%) | `ABSENT` (8.3%) | `hcl` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (98.8%) | `pyridine_organocat` (0.9%) | `ABSENT` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.3%) | `polar_aprotic_amide` (1.4%) | `ketone` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (1%) | `CN(C)C=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` + `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `Cl` (1%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (100%) | `[I-].[K+]` (1%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1419  yield=80.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #12)

```
CC(C)CO.C=CNC(=O)c1ccccc1>>CC(C)COC1COC(c2ccccc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (95.5%) | `carbon_cloth` (4.4%) | `graphite_rod` (0.1%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (70.8%) | `platinum` (16.2%) | `nickel` (12.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_generic` (25.9%) | `platinum_plate` (23.6%) | `stainless_steel_plate` (19.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.0%) | `Na` (0.7%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (78.6%) | `Br` (13.6%) | `PF6` (2.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (6.4%) | `iodide_anion` (2.6%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (76.5%) | `ABSENT` (10.6%) | `organic_neutral_cat` (8.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (93.0%) | `halogenated_aliphatic` (2.6%) | `polar_aprotic_amide` (2.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (2%) | `O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (77%) | `[Cl-].[Na+]` (6%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (56%) | `__ABSENT__` (0%) | `[I-].[K+]` (0%) | set ✗ / any ✓ |

---

### Reaction #1420  yield=79.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #13)

```
OCc1ccccc1.C=CNC(=O)c1ccccc1>>c1ccc(COC2COC(c3ccccc3)=N2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `platinum` (1.0%) | `sacrificial_iron` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (48.1%) | `graphite_generic` (23.4%) | `graphite_rod` (22.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (96.1%) | `platinum` (2.1%) | `nickel` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (56.3%) | `stainless_steel_generic` (36.4%) | `platinum_plate` (4.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (50.3%) | `NBu4` (47.9%) | `Na` (0.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (68.1%) | `BF4` (23.7%) | `Br` (4.1%) | ✓ |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (12.4%) | `chloride_anion` (2.7%) | `bromide_anion` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (89.4%) | `pyridine_organocat` (7.5%) | `organic_neutral_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.5%) | `polar_aprotic_amide` (11.8%) | `halogenated_aliphatic` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (5%) | `O` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (72%) | `[Cl-].[Na+]` (25%) | `Cc1ccc(I)cc1` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (55%) | `[I-].[K+]` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #1421  yield=78.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #14)

```
C=CNC(=O)c1ccc(Cl)cc1>>OC1COC(c2ccc(Cl)cc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (88.6%) | `carbon_felt` (4.7%) | `graphite_generic` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.7%) | `platinum` (0.1%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (93.5%) | `stainless_steel_generic` (6.3%) | `platinum_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (89.2%) | `ABSENT` (7.9%) | `Li` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (85.1%) | `Br` (9.8%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (24.7%) | `ABSENT` (6.7%) | `hcl` (3.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (99.2%) | `pyridine_organocat` (0.3%) | `ABSENT` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.7%) | `polar_aprotic_amide` (0.7%) | `ketone` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (7%) | `[H+].[OH-]` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `O` (0%) | `Cl` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (100%) | `[I-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1422  yield=78.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #15)

```
C=CNC(=O)c1cccc2ccccc12>>OC1COC(c2cccc3ccccc23)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (98.6%) | `carbon_felt` (0.8%) | `graphite_generic` (0.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.3%) | `platinum` (0.4%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (85.5%) | `platinum_plate` (8.2%) | `stainless_steel_generic` (5.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (80.8%) | `ABSENT` (8.8%) | `Li` (7.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (89.2%) | `Br` (4.1%) | `ABSENT` (3.8%) | ✓ |
| 试剂大类 | 103 | `inorganic_simple` | `chloride_anion` (15.9%) | `ABSENT` (7.6%) | `boron_lewis_acid` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (96.9%) | `ABSENT` (2.0%) | `pyridine_organocat` (1.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.7%) | `polar_aprotic_amide` (0.2%) | `ketone` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Na][Br]` + `O` | `[Cl-].[Na+]` (100%) | `O` (0%) | `Cl` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (99%) | `[I-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1423  yield=78.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #16)

```
C=CNC(=O)c1ccc(C)cc1>>Cc1ccc(C2=NC(O)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `sacrificial_iron` (0.1%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (95.8%) | `graphite_felt` (1.9%) | `carbon_felt` (1.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (97.7%) | `nickel` (1.3%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (97.7%) | `stainless_steel_generic` (1.5%) | `platinum_plate` (0.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `divided` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.9%) | `ABSENT` (3.2%) | `Li` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.1%) | `Br` (6.0%) | `ABSENT` (2.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (30.7%) | `ABSENT` (5.3%) | `hcl` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (98.7%) | `pyridine_organocat` (0.8%) | `ABSENT` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.4%) | `polar_aprotic_amide` (1.4%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (1%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `O` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (99%) | `[I-].[K+]` (3%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1424  yield=72.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #17)

```
C=CNC(=O)c1ccccc1Cl>>OC1COC(c2ccccc2Cl)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.1%) | `graphite_generic` (0.6%) | `graphite_felt` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.6%) | `platinum` (0.2%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (87.2%) | `stainless_steel_generic` (11.8%) | `platinum_plate` (0.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (95.5%) | `ABSENT` (2.8%) | `NEt4` (0.6%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (94.0%) | `Br` (3.0%) | `ABSENT` (1.3%) | ✓ |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (12.3%) | `ABSENT` (10.9%) | `hcl` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (98.8%) | `pyridine_organocat` (0.6%) | `ABSENT` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.7%) | `ketone` (1.5%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `O` (0%) | `Cl` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (98%) | `[I-].[K+]` (1%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1425  yield=74.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #18)

```
C=CNC(=O)c1ccc(Cl)nc1>>OC1COC(c2ccc(Cl)nc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.7%) | `graphite_felt` (0.2%) | `carbon_felt` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.9%) | `nickel` (0.1%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (99.9%) | `stainless_steel_generic` (0.1%) | `platinum_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.3%) | `ABSENT` (0.2%) | `Li` (0.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (84.9%) | `Br` (11.1%) | `carboxylate` (1.7%) | ✗ |
| 试剂大类 | 103 | `inorganic_simple` | `chloride_anion` (26.8%) | `ABSENT` (6.8%) | `hcl` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (99.5%) | `pyridine_organocat` (0.3%) | `ABSENT` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.5%) | `ketone` (1.5%) | `polar_aprotic_amide` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (1%) | `[H+].[OH-]` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Na][Br]` + `O` | `[Cl-].[Na+]` (100%) | `O` (0%) | `Cl` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (100%) | `[I-].[K+]` (1%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1426  yield=75.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #19)

```
O=C(O)c1ccccc1.C=CNC(=O)c1ccccc1>>O=C(OC1COC(c2ccccc2)=N1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.0%) | `platinum` (0.9%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (97.2%) | `graphite_generic` (1.0%) | `carbon_felt` (0.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (96.3%) | `nickel` (1.5%) | `platinum` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (96.8%) | `stainless_steel_generic` (2.4%) | `platinum_plate` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (0.8%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (88.2%) | `ABSENT` (4.6%) | `Na` (4.5%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (68.7%) | `Br` (10.7%) | `Cl` (6.3%) | ✗ |
| 试剂大类 | 103 | `inorganic_simple` | `ABSENT` (8.9%) | `chloride_anion` (8.7%) | `hcl` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (95.6%) | `organic_neutral_cat` (1.7%) | `ABSENT` (0.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (87.2%) | `polar_aprotic_amide` (4.7%) | `halogenated_aliphatic` (3.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (33%) | `ClCCl` (5%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Na][Br]` | `[Cl-].[Na+]` (81%) | `__ABSENT__` (7%) | `CC(=O)O` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (89%) | `[I-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1427  yield=74.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #20)

```
C=CNC(=O)c1ccccc1C>>Cc1ccccc1C1=NC(O)CO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (98.9%) | `graphite_generic` (0.4%) | `carbon_felt` (0.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.7%) | `platinum` (0.1%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (98.1%) | `stainless_steel_generic` (1.5%) | `platinum_plate` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.1%) | `ABSENT` (12.1%) | `Li` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (87.2%) | `ABSENT` (6.9%) | `Br` (3.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (16.9%) | `ABSENT` (10.1%) | `hcl` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (98.8%) | `pyridine_organocat` (0.5%) | `ABSENT` (0.4%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.4%) | `ketone` (0.4%) | `polar_aprotic_amide` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `O` (0%) | `[Br-].[K+]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (100%) | `[I-].[K+]` (1%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1428  yield=71.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #21)

```
C=CNC(=O)c1cccc(C)c1>>Cc1cccc(C2=NC(O)CO2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (97.6%) | `graphite_generic` (1.3%) | `carbon_felt` (0.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (98.9%) | `nickel` (0.5%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (91.8%) | `stainless_steel_generic` (7.2%) | `platinum_plate` (0.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.6%) | `ABSENT` (10.0%) | `Li` (0.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (80.0%) | `ABSENT` (10.9%) | `Br` (4.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (13.5%) | `chloride_anion` (12.5%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (97.8%) | `pyridine_organocat` (1.3%) | `ABSENT` (0.4%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.2%) | `ketone` (0.3%) | `polar_aprotic_amide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (59%) | `__ABSENT__` (41%) | `Cl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (96%) | `[I-].[K+]` (1%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #1429  yield=87.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #22)

```
C=CNC(=O)c1cccs1>>OC1COC(c2cccs2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (91.5%) | `graphite_generic` (6.3%) | `carbon_generic` (0.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (98.8%) | `nickel` (0.4%) | `platinum` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (95.7%) | `stainless_steel_generic` (3.9%) | `platinum_plate` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (94.0%) | `ABSENT` (2.9%) | `Na` (1.8%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (67.8%) | `Br` (26.4%) | `ABSENT` (2.2%) | ✓ |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (12.3%) | `ABSENT` (5.3%) | `hcl` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (99.0%) | `ABSENT` (0.5%) | `pyridine_organocat` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.8%) | `polar_aprotic_amide` (1.7%) | `ketone` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (3%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `O` (0%) | `Cl` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (100%) | `[I-].[K+]` (1%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1430  yield=87.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #23)

```
C=CNC(=O)c1ccc(OCC)cc1>>CCOc1ccc(C2=NC(O)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (91.8%) | `carbon_felt` (5.5%) | `graphite_felt` (1.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.1%) | `nickel` (0.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (90.9%) | `stainless_steel_generic` (8.5%) | `platinum_plate` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.9%) | `ABSENT` (4.9%) | `Li` (1.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (84.9%) | `Br` (8.8%) | `ABSENT` (3.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (14.9%) | `ABSENT` (9.6%) | `hcl` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (96.4%) | `pyridine_organocat` (1.8%) | `ABSENT` (1.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.5%) | `polar_aprotic_amide` (1.1%) | `ketone` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `O` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (99%) | `[I-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1431  yield=83.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #24)

```
CC(C)O.C=CNC(=O)c1ccccc1>>CC(C)OC1COC(c2ccccc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `platinum` (1.4%) | `sacrificial_iron` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (80.0%) | `graphite_generic` (19.1%) | `carbon_felt` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (94.6%) | `platinum` (2.5%) | `nickel` (2.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (92.3%) | `stainless_steel_generic` (5.5%) | `platinum_generic` (1.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (0.9%) | `divided` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.2%) | `Na` (2.9%) | `K` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (55.6%) | `Br` (24.7%) | `PF6` (8.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (9.1%) | `chloride_anion` (5.4%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (81.6%) | `ABSENT` (7.1%) | `organic_neutral_cat` (6.4%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.1%) | `polar_aprotic_amide` (2.7%) | `ketone` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (1%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (75%) | `[Cl-].[Na+]` (17%) | `[Li+].[O-][Cl+3]([` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (98%) | `[I-].[K+]` (0%) | `[Cl-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1432  yield=86.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #25)

```
C=CNC(=O)c1ccc2ccccc2c1>>OC1COC(c2ccc3ccccc3c2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `sacrificial_iron` (0.2%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.2%) | `graphite_felt` (0.3%) | `graphite_generic` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.4%) | `nickel` (0.3%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (98.9%) | `stainless_steel_generic` (1.0%) | `platinum_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.6%) | `Li` (0.9%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (89.6%) | `Br` (7.8%) | `Cl` (0.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (17.8%) | `ABSENT` (9.6%) | `hcl` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (98.9%) | `pyridine_organocat` (0.6%) | `ABSENT` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.1%) | `polar_aprotic_amide` (3.0%) | `ketone` (2.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (1%) | `[H+].[OH-]` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `O` (0%) | `Cl` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (98%) | `[I-].[K+]` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #1433  yield=82.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #26)

```
CCCCO.C=CNC(=O)c1ccccc1>>CCCCOC1COC(c2ccccc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (89.8%) | `graphite_rod` (5.5%) | `graphite_generic` (4.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (67.2%) | `stainless_steel` (26.6%) | `nickel` (5.8%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (74.6%) | `platinum_generic` (15.7%) | `stainless_steel_plate` (6.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (73.1%) | `ABSENT` (26.4%) | `NEt4` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (59.8%) | `ABSENT` (36.3%) | `PF6` (2.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (11.9%) | `chloride_anion` (2.4%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (61.3%) | `pyridine_organocat` (21.3%) | `ABSENT` (8.4%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.9%) | `ABSENT` (1.0%) | `halogenated_aliphatic` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (2%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (92%) | `[Cl-].[Na+]` (5%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (45%) | `__OTHER__` (0%) | `__ABSENT__` (0%) | set ✗ / any ✓ |

---

### Reaction #1434  yield=86.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #27)

```
OC1CCCC1.C=CNC(=O)c1ccccc1>>c1ccc(C2=NC(OC3CCCC3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `sacrificial_iron` (0.4%) | `platinum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (81.7%) | `graphite_generic` (18.0%) | `graphite_rod` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (96.6%) | `nickel` (1.9%) | `platinum` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (79.8%) | `stainless_steel_generic` (17.4%) | `graphite_generic` (0.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.0%) | `ABSENT` (5.7%) | `NEt4` (1.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (73.7%) | `Br` (10.8%) | `ABSENT` (8.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (9.9%) | `polyhalo_radical_transfer` (7.7%) | `ABSENT` (5.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (89.5%) | `ABSENT` (5.7%) | `pyridine_organocat` (2.0%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (93.9%) | `polar_aprotic_amide` (2.6%) | `ABSENT` (2.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (2%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `[Cl-].[Na+]` (97%) | `O` (2%) | `Cl` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (94%) | `__OTHER__` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1435  yield=82.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #28)

```
C=CNC(=O)c1ccc(Br)cc1>>OC1COC(c2ccc(Br)cc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (96.7%) | `carbon_felt` (1.9%) | `graphite_generic` (0.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (98.8%) | `nickel` (0.5%) | `platinum` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (98.2%) | `stainless_steel_generic` (1.4%) | `platinum_plate` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.6%) | `ABSENT` (6.0%) | `Li` (1.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (73.5%) | `Br` (20.4%) | `ABSENT` (4.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (21.2%) | `ABSENT` (10.1%) | `hcl` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (97.8%) | `pyridine_organocat` (1.5%) | `ABSENT` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.9%) | `polar_aprotic_amide` (0.5%) | `ketone` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `[H+].[OH-]` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `Cl` (1%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (99%) | `[I-].[K+]` (1%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1436  yield=86.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #29)

```
C=CNC(=O)c1ccc(OC)c(OC)c1>>COc1ccc(C2=NC(O)CO2)cc1OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (96.9%) | `carbon_felt` (1.2%) | `graphite_felt` (1.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (98.7%) | `nickel` (0.6%) | `platinum` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (99.0%) | `stainless_steel_generic` (0.7%) | `platinum_plate` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (83.7%) | `ABSENT` (9.6%) | `Na` (3.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (87.8%) | `ABSENT` (4.6%) | `Br` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (12.1%) | `chloride_anion` (11.5%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (99.1%) | `ABSENT` (0.4%) | `pyridine_organocat` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.6%) | `ketone` (0.7%) | `polar_aprotic_amide` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (1%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (86%) | `__ABSENT__` (14%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (100%) | `[I-].[K+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1437  yield=85.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #30)

```
C=CNC(=O)c1ccc(CC)cc1>>CCc1ccc(C2=NC(O)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (97.6%) | `carbon_felt` (1.4%) | `graphite_generic` (0.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.6%) | `nickel` (0.2%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (99.2%) | `stainless_steel_generic` (0.7%) | `platinum_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.1%) | `Li` (1.3%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (87.3%) | `Br` (10.0%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (30.4%) | `ABSENT` (8.4%) | `hcl` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (99.6%) | `pyridine_organocat` (0.3%) | `ABSENT` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.9%) | `ketone` (0.4%) | `polar_aprotic_amide` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `[H+].[OH-]` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `O` (0%) | `[Br-].[K+]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (100%) | `[I-].[K+]` (1%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1438  yield=81.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #31)

```
CC(C)=CCCC(C)CCO.C=CNC(=O)c1ccccc1>>CC(C)=CCCC(C)CCOC1COC(c2ccccc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (88.0%) | `graphite_generic` (7.4%) | `graphite_rod` (4.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (57.3%) | `platinum` (36.9%) | `nickel` (5.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (71.6%) | `stainless_steel_plate` (23.1%) | `stainless_steel_generic` (2.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.8%) | `ABSENT` (2.2%) | `NEt4` (1.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (86.1%) | `PF6` (7.1%) | `ABSENT` (3.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (17.8%) | `ABSENT` (3.5%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (94.3%) | `pyridine_organocat` (2.7%) | `ABSENT` (1.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.9%) | `polar_aprotic_amide` (0.3%) | `ketone` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `[Cl-].[Na+]` (100%) | `O` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (33%) | `__OTHER__` (1%) | `[I-].[K+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1439  yield=84.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #32)

```
C=CNC(=O)c1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc(C2=NC(O)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `sacrificial_iron` (0.3%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (93.9%) | `carbon_felt` (3.4%) | `graphite_felt` (1.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (94.6%) | `nickel` (2.6%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (85.8%) | `stainless_steel_generic` (10.4%) | `platinum_plate` (2.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.4%) | `ABSENT` (13.3%) | `Li` (4.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (69.4%) | `Br` (18.0%) | `ABSENT` (7.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (16.1%) | `ABSENT` (8.0%) | `hcl` (4.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (96.5%) | `pyridine_organocat` (2.0%) | `organic_neutral_cat` (0.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.1%) | `polar_aprotic_amide` (0.8%) | `ketone` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (4%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `Cl` (6%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (96%) | `[I-].[K+]` (4%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1440  yield=90.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #33)

```
OCCO.C=CNC(=O)c1ccccc1>>OCCOC1COC(c2ccccc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (73.7%) | `carbon_cloth` (25.7%) | `graphite_rod` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (71.0%) | `platinum` (27.7%) | `nickel` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (57.1%) | `platinum_plate` (30.6%) | `stainless_steel_generic` (7.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (68.7%) | `ABSENT` (30.4%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (63.2%) | `ABSENT` (34.0%) | `PF6` (1.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (6.4%) | `chloride_anion` (4.5%) | `iodide_anion` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (82.9%) | `organic_neutral_cat` (6.5%) | `pyridine_organocat` (4.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.8%) | `polar_aprotic_amide` (1.6%) | `halogenated_aliphatic` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (5%) | `ClCCl` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `[Cl-].[Na+]` (48%) | `__ABSENT__` (40%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (33%) | `__OTHER__` (0%) | `[I-].[K+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1441  yield=90.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #34)

```
CO.C=CNC(=O)c1ccccc1>>COC1COC(c2ccccc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (0.7%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (91.4%) | `graphite_generic` (8.5%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (98.8%) | `nickel` (0.7%) | `platinum` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (51.2%) | `stainless_steel_generic` (45.7%) | `platinum_plate` (0.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.9%) | `ABSENT` (7.8%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (81.4%) | `ABSENT` (9.8%) | `Cl` (3.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (6.2%) | `ABSENT` (5.3%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (87.7%) | `ABSENT` (6.7%) | `organic_neutral_cat` (2.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.9%) | `polar_aprotic_amide` (2.6%) | `ABSENT` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `[Cl-].[Na+]` (93%) | `O` (1%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (84%) | `[I-].[K+]` (0%) | `O=C([O-])c1ccccc1-` (0%) | set ✗ / any ✗ |

---

### Reaction #1442  yield=89.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #35)

```
C=CNC(=O)c1ccccc1>>OC1COC(c2ccccc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `sacrificial_iron` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.5%) | `graphite_generic` (0.2%) | `carbon_felt` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.6%) | `nickel` (0.2%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (99.6%) | `stainless_steel_generic` (0.4%) | `platinum_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (95.3%) | `ABSENT` (2.4%) | `Na` (0.8%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (77.1%) | `Br` (16.7%) | `ABSENT` (2.4%) | ✓ |
| 试剂大类 | 103 | `inorganic_simple` | `chloride_anion` (24.1%) | `ABSENT` (10.7%) | `hcl` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (99.4%) | `pyridine_organocat` (0.4%) | `organic_neutral_cat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.9%) | `polar_aprotic_amide` (3.0%) | `ketone` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Na][Br]` + `O` | `[Cl-].[Na+]` (100%) | `Cl` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (99%) | `[I-].[K+]` (1%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1443  yield=96.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #36)

```
C=CNC(=O)c1ccc(CCCC)cc1>>CCCCc1ccc(C2=NC(O)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (98.3%) | `carbon_felt` (0.8%) | `graphite_felt` (0.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (99.0%) | `nickel` (0.8%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (96.9%) | `stainless_steel_generic` (2.8%) | `platinum_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.6%) | `ABSENT` (5.6%) | `Li` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (73.8%) | `Br` (18.4%) | `ABSENT` (4.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (23.1%) | `ABSENT` (8.4%) | `hcl` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (97.9%) | `pyridine_organocat` (1.4%) | `ABSENT` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.7%) | `ketone` (0.9%) | `polar_aprotic_amide` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` + `O` | `[Cl-].[Na+]` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Br-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (100%) | `[I-].[K+]` (1%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |

---

### Reaction #1444  yield=92.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_1_96-101.json) (反应 idx 在该 JSON 内 = #37)

```
CCO.C=CNC(=O)c1ccccc1>>CCOC1COC(c2ccccc2)=N1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (59.4%) | `graphite_generic` (39.4%) | `graphite_rod` (0.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (86.8%) | `nickel` (10.1%) | `platinum` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (78.7%) | `stainless_steel_generic` (13.3%) | `nickel_plate` (3.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NBu4` (93.2%) | `ABSENT` (4.8%) | `Na` (1.4%) | ✓ |
| 电解质 anion | 26 | `Br` | `BF4` (67.5%) | `ABSENT` (11.2%) | `Br` (11.1%) | ✓ |
| 试剂大类 | 103 | `boron_lewis_acid` | `ABSENT` (11.0%) | `chloride_anion` (3.8%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (94.5%) | `pyridine_organocat` (2.4%) | `ABSENT` (1.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.8%) | `polar_aprotic_amide` (2.6%) | `halogenated_aliphatic` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (3%) | `ClCCl` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (82%) | `[Cl-].[Na+]` (12%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (89%) | `[I-].[K+]` (0%) | `O=C([O-])c1ccccc1-` (0%) | set ✗ / any ✗ |

---

### Reaction #1445  yield=63.0%

**Source paper**: [`China/China_CN117926288_A_2024-04-26.json`](reactions_by_journal_alkene_ec_audited/China/China_CN117926288_A_2024-04-26.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1>>c1ccc(C(CCC(c2ccccc2)c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (48.1%) | `ABSENT` (30.6%) | `platinum` (13.4%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `carbon_rod` (54.8%) | `glassy_carbon` (11.0%) | `carbon_generic` (5.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (32.2%) | `ABSENT` (30.2%) | `carbon` (27.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (34.6%) | `platinum_generic` (16.2%) | `carbon_rod` (12.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (78.6%) | `ABSENT` (17.8%) | `divided` (3.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (76.6%) | `Li` (8.0%) | `NBu4` (6.7%) | ✓ |
| 电解质 anion | 26 | `I` | `ClO4` (39.5%) | `BF4` (25.0%) | `F` (7.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (10.6%) | `polyhalo_radical_transfer` (8.1%) | `inorganic_simple` (6.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (87.0%) | `Mn_complex` (4.3%) | `organic_neutral_cat` (2.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (66.9%) | `polar_protic_alcohol` (18.9%) | `ABSENT` (3.1%) | ✗ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CCO` (70%) | `CC#N` (43%) | `C1COCCO1` (40%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I)cc1` + `F.c1ccncc1` + `O=C(O)O.[Na]` + `[OH][Na]` | `O=C(O)O.[Na]` (75%) | `F.c1ccncc1` (57%) | `OB(O)B(O)O` (42%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `Brc1ccc(N(c2ccc(Br` | `c1ccncc1` (58%) | `Brc1ccc(N(c2ccc(Br` (50%) | `CC(C)(C)c1cc(C=N[C` (10%) | set ✗ / any ✓ |

---

### Reaction #1446  yield=74.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_20_5764-5769.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_20_5764-5769.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1cccc2ccccc12>>c1ccc2c(CCCCc3cccc4ccccc34)cccc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (98.0%) | `sacrificial_zinc` (1.0%) | `platinum` (0.6%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `graphite_rod` (67.3%) | `carbon_generic` (8.7%) | `glassy_carbon` (8.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (95.5%) | `platinum` (3.6%) | `stainless_steel` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_rod` (52.8%) | `carbon_generic` (37.0%) | `platinum_plate` (5.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.1%) | `divided` (2.1%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (37.3%) | `ABSENT` (27.4%) | `NEt4` (10.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `Br` (71.0%) | `ABSENT` (7.8%) | `Cl` (6.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.9%) | `bromide_anion` (2.5%) | `primary_amine` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Co_complex` (0.1%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (41.0%) | `polar_aprotic_sulfoxide` (30.5%) | `cyclic_ether` (12.8%) | ✗ |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `CC#N` (63%) | `CCOCC` (32%) | `FC(F)(F)c1ccccc1` (31%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (100%) | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (95%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Pt]` | `c1ccncc1` (87%) | `__OTHER__` (70%) | `__ABSENT__` (22%) | set ✗ / any ✗ |

---

### Reaction #1447  yield=28.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)C1CC1.C=CCCN(C#N)c1ccc(C(C)(C)C)cc1>>COCCC=C(CS(=O)(=O)OC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (99.9%) | `reticulated_vitreous_carbon` (0.0%) | `carbon_generic` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.6%) | `platinum_plate` (1.0%) | `graphite_generic` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NBu4` (90.0%) | `ABSENT` (9.6%) | `Li` (0.2%) | ✗ |
| 电解质 anion | 26 | `SO4` | `BF4` (90.5%) | `ABSENT` (6.1%) | `PF6` (2.7%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `alkali_other_salt` (13.6%) | `alkali_sulfonate` (11.0%) | `alkali_sulfinate` (8.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (57.1%) | `ABSENT` (19.8%) | `Mn_complex` (11.9%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (90.9%) | `polar_aprotic_nitrile` (8.4%) | `halogenated_aliphatic` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` | `CC#N` (85%) | `CO` (43%) | `CCO` (13%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CS(=O)(=O)O` | `O=C(O)O.[Na]` (45%) | `[Pt]` (17%) | `O.O.O.O.O.O.O.O.O.` (14%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (19%) | `__ABSENT__` (3%) | `[O]=[Fe][O][Fe]=[O` (1%) | set ✗ / any ✓ |

---

### Reaction #1448  yield=34.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json) (反应 idx 在该 JSON 内 = #1)

```
C=CCCN(C#N)c1cccc(C)c1>>COS(=O)(=O)CC1CCN2C1=NS(=O)(=O)c1c(C)cccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (69.4%) | `graphite_generic` (30.3%) | `carbon_felt` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_plate` (54.5%) | `graphite_generic` (33.6%) | `platinum_plate` (10.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `ABSENT` (56.5%) | `Na` (28.9%) | `NBu4` (11.0%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `ABSENT` (45.3%) | `molecular_no_ion` (43.3%) | `BF4` (11.0%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `alkali_sulfonate` (22.3%) | `sulfonic_acid` (14.5%) | `alkali_other_salt` (12.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ferrocene_mediator` (0.1%) | `Co_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `halogenated_aliphatic` (43.5%) | `polar_aprotic_nitrile` (22.6%) | `acyclic_ether` (16.9%) | ✗ |
| 溶剂 set | 79 | `CO` | `O` (100%) | `ClCCl` (22%) | `CC#N` (4%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CS(=O)(=O)O` | `O=S([O-])S(=O)(=O)` (92%) | `O=O` (5%) | `CS(=O)(=O)O` (4%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #1449  yield=41.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json) (反应 idx 在该 JSON 内 = #2)

```
C=CCCN(C#N)c1cccc(C)c1>>COS(=O)(=O)CC1CCN2C1=NS(=O)(=O)c1ccc(C)cc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (88.1%) | `graphite_generic` (11.7%) | `graphite_plate` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (95.8%) | `platinum` (4.2%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_plate` (78.4%) | `graphite_generic` (16.8%) | `platinum_plate` (4.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `ABSENT` (0.7%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `molecular_no_ion` | `Na` (59.5%) | `NBu4` (20.6%) | `ABSENT` (9.3%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `molecular_no_ion` (93.2%) | `BF4` (2.8%) | `ABSENT` (2.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_sulfinate` | `alkali_sulfonate` (67.0%) | `alkali_other_salt` (11.0%) | `sulfonic_acid` (3.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `Co_complex` (0.8%) | `ferrocene_mediator` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (69.6%) | `halogenated_aliphatic` (10.0%) | `acyclic_ether` (7.8%) | ✗ |
| 溶剂 set | 79 | `CO` | `O` (100%) | `CC#N` (95%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CS(=O)(=O)O` | `O=S([O-])S(=O)(=O)` (90%) | `O=O` (36%) | `CS(=O)(=O)O` (17%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `__OTHER__` (1%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #1450  yield=66.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json) (反应 idx 在该 JSON 内 = #3)

```
C=CCCN(C#N)c1ccc(F)cc1>>COS(=O)(=O)CC1CCN2C1=NS(=O)(=O)c1cc(F)ccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (55.8%) | `graphite_rod` (43.7%) | `graphite_plate` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (99.0%) | `platinum` (1.0%) | `stainless_steel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (88.5%) | `graphite_plate` (8.0%) | `platinum_plate` (2.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NBu4` (78.2%) | `Na` (19.7%) | `ABSENT` (1.1%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `BF4` (78.1%) | `molecular_no_ion` (15.7%) | `SO4` (2.2%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `alkali_sulfonate` (86.1%) | `alkali_other_salt` (1.9%) | `sulfonic_acid` (0.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Co_complex` (1.0%) | `ammonium_PTC_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `halogenated_aliphatic` (56.4%) | `polar_protic_alcohol` (28.7%) | `polar_aprotic_nitrile` (7.5%) | ✓ |
| 溶剂 set | 79 | `CO` | `O` (99%) | `ClCCl` (41%) | `CC#N` (25%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CS(=O)(=O)O` | `O=S([O-])S(=O)(=O)` (73%) | `O=O` (64%) | `O=C(O)C(F)(F)F` (43%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (94%) | `[Cl-].[Cl-].[Mn+2]` (2%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #1451  yield=65.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json) (反应 idx 在该 JSON 内 = #4)

```
C=CCCN(C#N)c1ccc(C2CCCCC2)cc1>>COS(=O)(=O)CC1CCN2C1=NS(=O)(=O)c1cc(C3CCCCC3)ccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (75.1%) | `graphite_generic` (23.5%) | `graphite_plate` (0.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (95.3%) | `platinum` (4.6%) | `ABSENT` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_plate` (49.1%) | `graphite_generic` (30.1%) | `platinum_plate` (18.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.5%) | `ABSENT` (1.0%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NBu4` (86.4%) | `Na` (7.8%) | `molecular_no_ion` (3.2%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `BF4` (74.0%) | `molecular_no_ion` (13.2%) | `SO4` (6.4%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `alkali_sulfonate` (84.3%) | `alkali_other_salt` (6.9%) | `alkali_sulfinate` (0.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (88.9%) | `Co_complex` (9.7%) | `ammonium_PTC_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `halogenated_aliphatic` (41.0%) | `polar_aprotic_nitrile` (23.3%) | `polar_protic_alcohol` (20.3%) | ✓ |
| 溶剂 set | 79 | `CO` | `O` (71%) | `CC#N` (45%) | `ClCCl` (24%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CS(=O)(=O)O` | `O=S([O-])S(=O)(=O)` (90%) | `O=O` (77%) | `O=C(O)C(F)(F)F` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (94%) | `c1ccncc1` (6%) | `__OTHER__` (4%) | set ✓ / any ✓ |

---

### Reaction #1452  yield=66.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json) (反应 idx 在该 JSON 内 = #5)

```
CO.C=CCCN(C#N)c1ccc(Br)cc1>>COS(=O)(=O)CC1CCN2C1=NS(=O)(=O)c1cc(Br)ccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (50.3%) | `graphite_generic` (49.5%) | `reticulated_vitreous_carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (63.8%) | `carbon` (36.0%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (92.3%) | `graphite_generic` (6.9%) | `graphite_plate` (0.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `molecular_no_ion` | `NBu4` (70.5%) | `molecular_no_ion` (22.5%) | `ABSENT` (2.6%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `molecular_no_ion` (69.1%) | `BF4` (22.0%) | `SO4` (2.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_sulfonate` (75.2%) | `alkali_other_salt` (16.1%) | `alkali_sulfinate` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `pyridine_organocat` (0.3%) | `Co_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `ABSENT` (75.6%) | `halogenated_aliphatic` (17.5%) | `polar_aprotic_nitrile` (6.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `__ABSENT__` | `__ABSENT__` (98%) | `O` (80%) | `CCOCC` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S([O-])S(=O)(=O)` | `O=S([O-])S(=O)(=O)` (95%) | `O=O` (43%) | `O=C(O)C(F)(F)F` (15%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1453  yield=65.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json) (反应 idx 在该 JSON 内 = #6)

```
C=CCCN(C#N)c1ccc(CC)cc1>>CCc1ccc2c(c1)S(=O)(=O)N=C1C(CS(=O)(=O)OC)CCN12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (53.7%) | `graphite_rod` (45.8%) | `reticulated_vitreous_carbon` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (99.0%) | `platinum` (1.0%) | `ABSENT` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (71.2%) | `graphite_plate` (25.3%) | `platinum_plate` (2.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (92.7%) | `divided` (4.2%) | `ABSENT` (3.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NBu4` (55.4%) | `Na` (39.5%) | `Li` (2.2%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `molecular_no_ion` (50.0%) | `BF4` (39.0%) | `SO4` (4.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `sulfonic_acid` | `alkali_sulfonate` (87.8%) | `alkali_other_salt` (4.1%) | `sulfonic_acid` (0.6%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.7%) | `Co_complex` (2.0%) | `ferrocene_mediator` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `halogenated_aliphatic` (51.5%) | `polar_aprotic_nitrile` (27.8%) | `polar_protic_alcohol` (7.7%) | ✓ |
| 溶剂 set | 79 | `CO` | `O` (98%) | `ClCCl` (17%) | `CC#N` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CS(=O)(=O)O` | `O=S([O-])S(=O)(=O)` (90%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)NC1CC2(CCCCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1454  yield=65.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json) (反应 idx 在该 JSON 内 = #7)

```
CO.C=CCCN(C#N)c1ccc(Cl)cc1>>COS(=O)(=O)CC1CCN2C1=NS(=O)(=O)c1cc(Cl)ccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (75.1%) | `graphite_generic` (24.3%) | `graphite_plate` (0.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (51.4%) | `carbon` (48.2%) | `nickel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (88.2%) | `graphite_plate` (8.5%) | `graphite_generic` (2.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `molecular_no_ion` | `NBu4` (78.3%) | `Na` (14.4%) | `ABSENT` (4.1%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `molecular_no_ion` (54.2%) | `BF4` (22.1%) | `SO4` (10.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_other_salt` (59.6%) | `alkali_sulfonate` (24.2%) | `alkali_sulfinate` (1.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Co_complex` (0.1%) | `ferrocene_mediator` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (41.2%) | `polar_aprotic_nitrile` (29.5%) | `ABSENT` (27.6%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `O` (90%) | `ClCCl` (52%) | `CC#N` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])S(=O)(=O)` | `O=S(O)S(=O)(=O)O.[` (92%) | `CCN(CC)CC` (5%) | `CS(=O)(=O)O` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1455  yield=70.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json) (反应 idx 在该 JSON 内 = #8)

```
C=CCCN(C#N)c1ccccc1>>COS(=O)(=O)CC1CCN2C1=NS(=O)(=O)c1ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (83.2%) | `graphite_generic` (12.3%) | `graphite_plate` (2.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (98.4%) | `platinum` (1.5%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_plate` (83.7%) | `graphite_generic` (12.0%) | `platinum_plate` (2.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Na` (96.0%) | `NBu4` (2.1%) | `molecular_no_ion` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `molecular_no_ion` | `molecular_no_ion` (95.7%) | `SO4` (1.9%) | `BF4` (1.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `sulfonic_acid` | `alkali_sulfonate` (38.8%) | `sulfonic_acid` (23.1%) | `alkali_other_salt` (10.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Co_complex` (0.7%) | `Mn_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (51.9%) | `halogenated_aliphatic` (17.6%) | `polar_protic_alcohol` (13.0%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `O` | `O` (100%) | `CC#N` (98%) | `FC(F)(F)c1ccccc1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CS(=O)(=O)O` | `O=O` (86%) | `O=S([O-])S(=O)(=O)` (70%) | `CS(=O)(=O)O` (64%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (82%) | `__OTHER__` (8%) | `[Pt]` (3%) | set ✓ / any ✓ |

---

### Reaction #1456  yield=71.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json) (反应 idx 在该 JSON 内 = #9)

```
C=CCCN(C#N)c1ccc(C)cc1>>COS(=O)(=O)CC1CCN2C1=NS(=O)(=O)c1cc(C)ccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_magnesium` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (77.5%) | `graphite_generic` (16.6%) | `reticulated_vitreous_carbon` (5.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (96.7%) | `platinum` (3.3%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_plate` (76.3%) | `graphite_generic` (18.5%) | `platinum_plate` (3.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (75.7%) | `divided` (13.6%) | `ABSENT` (10.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `molecular_no_ion` | `Na` (85.4%) | `NBu4` (7.0%) | `molecular_no_ion` (4.1%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `molecular_no_ion` (85.3%) | `OTf` (10.1%) | `BF4` (2.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_sulfonate` | `alkali_sulfonate` (69.0%) | `alkali_other_salt` (11.9%) | `sulfonic_acid` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.0%) | `Co_complex` (5.9%) | `ferrocene_mediator` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (47.7%) | `halogenated_aliphatic` (26.9%) | `ABSENT` (6.5%) | ✗ |
| 溶剂 set | 79 | `CO` | `O` (100%) | `CC#N` (93%) | `FC(F)(F)c1ccccc1` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S([O-])S(=O)(=O)` | `O=O` (98%) | `O=S([O-])S(=O)(=O)` (62%) | `__OTHER__` (33%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (86%) | `[Pt]` (7%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #1457  yield=73.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json) (反应 idx 在该 JSON 内 = #10)

```
C=CCCN(C#N)c1ccc(CCCC)cc1>>CCCCc1ccc2c(c1)S(=O)(=O)N=C1C(CS(=O)(=O)OC)CCN12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (92.8%) | `graphite_generic` (6.6%) | `graphite_plate` (0.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (97.8%) | `platinum` (2.0%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_plate` (83.1%) | `platinum_plate` (11.0%) | `graphite_generic` (5.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (87.2%) | `divided` (12.3%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Na` (52.5%) | `NBu4` (40.7%) | `molecular_no_ion` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `molecular_no_ion` | `molecular_no_ion` (46.8%) | `BF4` (28.2%) | `SO4` (16.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `sulfonic_acid` | `alkali_sulfonate` (74.8%) | `alkali_other_salt` (6.8%) | `sulfonic_acid` (2.1%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Co_complex` (0.9%) | `ferrocene_mediator` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `halogenated_aliphatic` (58.9%) | `polar_protic_alcohol` (15.5%) | `polar_aprotic_nitrile` (12.7%) | ✓ |
| 溶剂 set | 79 | `CO` | `O` (97%) | `OC(C(F)(F)F)C(F)(F` (27%) | `ClCCl` (11%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CS(=O)(=O)O` | `O=S([O-])S(=O)(=O)` (90%) | `O=O` (82%) | `__OTHER__` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `__OTHER__` (1%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #1458  yield=77.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_23_6825-6830.json) (反应 idx 在该 JSON 内 = #11)

```
C=CCCN(C#N)c1cc(C)cc(C)c1.O=S(O)S(=O)(=O)O.[Na]>>COS(=O)(=O)CC1CCN2C1=NS(=O)(=O)c1c(C)cc(C)cc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.1%) | `graphite_generic` (6.7%) | `graphite_plate` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `carbon` (86.5%) | `platinum` (13.5%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_plate` (81.3%) | `graphite_generic` (11.1%) | `platinum_plate` (6.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Na` (76.7%) | `NBu4` (15.5%) | `ABSENT` (6.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `molecular_no_ion` | `molecular_no_ion` (66.0%) | `BF4` (21.1%) | `ABSENT` (9.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `sulfonic_acid` | `alkali_other_salt` (38.9%) | `alkali_sulfonate` (3.2%) | `sulfonic_acid` (2.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Co_complex` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `halogenated_aliphatic` (77.4%) | `polar_aprotic_nitrile` (18.5%) | `ABSENT` (2.4%) | ✗ |
| 溶剂 set | 79 | `CO` | `O` (99%) | `ClCCl` (44%) | `CC#N` (14%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CS(=O)(=O)O` | `O=S(O)S(=O)(=O)O.[` (88%) | `O.O.O.[Li+].[O-][C` (3%) | `O=P(O)(O)O.[K]` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #1459  yield=7.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json) (反应 idx 在该 JSON 内 = #0)

```
CC#N.c1ccc([Se][Se]c2ccccc2)cc1.C=CCCCCCCCCCBr>>CC(=O)NCC(CCCCCCCCCBr)[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (65.4%) | `platinum` (34.0%) | `sacrificial_magnesium` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (97.4%) | `platinum_generic` (1.4%) | `platinum_wire` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (78.3%) | `carbon` (21.6%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_wire` (80.7%) | `platinum_generic` (17.5%) | `graphite_plate` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (93.8%) | `divided` (4.4%) | `ABSENT` (1.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (96.0%) | `NBu4` (1.9%) | `Na` (1.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ClO4` (56.9%) | `molecular_no_ion` (35.2%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (17.9%) | `carboxylic_acid` (8.4%) | `as_solvent_nitroalkane` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.0%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `ABSENT` (94.1%) | `polar_aprotic_nitrile` (4.5%) | `ketone` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `__ABSENT__` | `__ABSENT__` (97%) | `O` (2%) | `CC#N` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(S(=O)(=O)O)` | `__ABSENT__` (100%) | `O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br][Mn][Br]` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1460  yield=21.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json) (反应 idx 在该 JSON 内 = #1)

```
CC#N.C=CCc1ccccc1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NCC(Cc1ccccc1)[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (86.0%) | `platinum` (13.8%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (61.4%) | `graphite_generic` (13.6%) | `platinum_generic` (9.3%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (92.0%) | `carbon` (4.3%) | `nickel` (3.2%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_generic` (93.0%) | `platinum_plate` (4.3%) | `nickel_foam` (0.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `divided` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (90.7%) | `protonated_amine` (3.9%) | `Li` (2.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (88.9%) | `fluoride_complex` (5.1%) | `BF4` (3.5%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `water` (7.9%) | `ABSENT` (4.9%) | `aryl_iodide_mediator` (3.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `ABSENT` (99.4%) | `halogenated_aliphatic` (0.4%) | `polar_aprotic_nitrile` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `__ABSENT__` | `__ABSENT__` (100%) | `ClCCl` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(S(=O)(=O)O)` | `O` (59%) | `O=O` (15%) | `[18OH2]` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Br-].[Mn+2]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1461  yield=31.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json) (反应 idx 在该 JSON 内 = #2)

```
CC#N.C=CCc1ccccc1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC(C[Se]c1ccccc1)Cc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (53.7%) | `reticulated_vitreous_carbon` (42.2%) | `graphite_generic` (2.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.4%) | `carbon` (5.7%) | `nickel` (0.8%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (89.4%) | `platinum_generic` (7.3%) | `platinum_wire` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (97.2%) | `divided` (2.6%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (90.1%) | `ABSENT` (4.5%) | `NEt4` (1.5%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (88.4%) | `PF6` (6.1%) | `ABSENT` (2.2%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (6.3%) | `carboxylic_acid` (3.9%) | `water` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `organic_neutral_cat` (0.3%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `ABSENT` (98.9%) | `halogenated_aliphatic` (0.9%) | `polar_aprotic_nitrile` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `__ABSENT__` | `__ABSENT__` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(S(=O)(=O)O)` | `__ABSENT__` (100%) | `O=O` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #1462  yield=50.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json) (反应 idx 在该 JSON 内 = #3)

```
CC#N.C=CCCc1ccccc1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC(CCc1ccccc1)C[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (67.1%) | `graphite_rod` (22.7%) | `graphite_plate` (8.5%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (85.5%) | `carbon` (13.6%) | `ABSENT` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (92.6%) | `platinum_wire` (5.8%) | `graphite_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (86.9%) | `undivided` (12.3%) | `ABSENT` (0.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.9%) | `ABSENT` (0.6%) | `Li` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (98.2%) | `PF6` (0.7%) | `ABSENT` (0.3%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (10.2%) | `carboxylic_acid` (5.4%) | `tetraaryl_borate` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `organic_neutral_cat` (0.1%) | `nhpi_mediator` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `ABSENT` (99.2%) | `polar_aprotic_nitrile` (0.6%) | `halogenated_aliphatic` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `__ABSENT__` | `__ABSENT__` (100%) | `CC#N` (0%) | `FC(F)(F)c1ccccc1` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(S(=O)(=O)O)` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `O=C([O-])[O-].[Cs+` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=[W+4]1234[O-2][W` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #1463  yield=47.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json) (反应 idx 在该 JSON 内 = #4)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CC1CCC(C2CCC(CCC)CC2)CC1>>CCC1CCC(C2CCC(C(C[Se]c3ccccc3)NC(C)=O)CC2)CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (98.9%) | `carbon_generic` (0.4%) | `graphite_plate` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.1%) | `carbon` (1.8%) | `ABSENT` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_generic` (99.5%) | `platinum_plate` (0.3%) | `graphite_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (81.6%) | `ABSENT` (18.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (56.7%) | `Li` (33.0%) | `Na` (6.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `I` (21.3%) | `SO4` (19.0%) | `carboxylate` (18.6%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (33.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.9%) | `halogenated_aliphatic` (0.0%) | `polar_protic_alcohol` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `OCC(F)(F)F` (0%) | `CCCCO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(S(=O)(=O)O)` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C([O-])O.[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |

---

### Reaction #1464  yield=54.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json) (反应 idx 在该 JSON 内 = #5)

```
CC#N.C=CCC(C)C.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC(C[Se]c1ccccc1)CC(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (68.4%) | `reticulated_vitreous_carbon` (22.3%) | `graphite_plate` (7.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (91.8%) | `carbon` (8.0%) | `ABSENT` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (69.0%) | `platinum_wire` (28.1%) | `platinum_generic` (1.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (86.7%) | `divided` (11.2%) | `ABSENT` (2.2%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (57.4%) | `ABSENT` (27.1%) | `Li` (11.8%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (69.9%) | `ABSENT` (21.7%) | `ClO4` (3.1%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (17.0%) | `carboxylic_acid` (5.1%) | `tetraaryl_borate` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `ammonium_PTC_organocat` (0.2%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `ABSENT` (98.3%) | `polar_aprotic_nitrile` (0.9%) | `halogenated_aliphatic` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `__ABSENT__` | `__ABSENT__` (100%) | `CC#N` (0%) | `OCC(F)(F)F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(S(=O)(=O)O)` + `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=[W+4]1234[O-2][W` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #1465  yield=67.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json) (反应 idx 在该 JSON 内 = #6)

```
CC#N.c1ccc([Se][Se]c2ccccc2)cc1.C=CCCCCCCCCCBr>>CC(=O)NC(CCCCCCCCCBr)C[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.2%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (97.4%) | `graphite_rod` (1.3%) | `graphite_plate` (0.6%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (73.7%) | `carbon` (26.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_wire` (84.6%) | `platinum_plate` (12.3%) | `graphite_plate` (1.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (52.3%) | `divided` (46.9%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (73.3%) | `Li` (21.5%) | `H` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (66.8%) | `ClO4` (17.2%) | `PF6` (6.6%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (12.7%) | `carboxylic_acid` (8.9%) | `as_solvent_polar_aprotic_sulfo` (3.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `organic_neutral_cat` (0.2%) | `thianthrene_phenothiazine_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `ABSENT` (98.6%) | `polar_aprotic_nitrile` (0.8%) | `halogenated_aliphatic` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `__ABSENT__` | `__ABSENT__` (100%) | `CC#N` (2%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(S(=O)(=O)O)` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `O=C([O-])[O-].[Cs+` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=[W+4]1234[O-2][W` (0%) | `[Br][Mn][Br]` (0%) | set ✓ / any ✓ |

---

### Reaction #1466  yield=66.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json) (反应 idx 在该 JSON 内 = #7)

```
CC#N.C=CCCCCCCCCCCCCCCCC.c1ccc([Se][Se]c2ccccc2)cc1>>CCCCCCCCCCCCCCCCC(C[Se]c1ccccc1)NC(C)=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_plate` (67.2%) | `graphite_rod` (17.5%) | `reticulated_vitreous_carbon` (8.5%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (67.4%) | `carbon` (32.0%) | `ABSENT` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (91.3%) | `graphite_plate` (3.0%) | `platinum_wire` (2.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (92.7%) | `divided` (5.5%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.5%) | `NH4` (1.1%) | `NEt4` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (93.3%) | `SO4` (1.6%) | `PF6` (1.4%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (16.8%) | `tetraaryl_borate` (3.1%) | `as_solvent_cyclic_ether` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `ammonium_PTC_organocat` (0.8%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `ABSENT` (85.2%) | `halogenated_aliphatic` (9.3%) | `polar_aprotic_nitrile` (3.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `__ABSENT__` | `__ABSENT__` (100%) | `CC#N` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(S(=O)(=O)O)` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #1467  yield=64.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json) (反应 idx 在该 JSON 内 = #8)

```
CC#N.C=CCCCCCCCCCC.c1ccc([Se][Se]c2ccccc2)cc1>>CCCCCCCCCCC(C[Se]c1ccccc1)NC(C)=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_plate` (67.2%) | `graphite_rod` (17.5%) | `reticulated_vitreous_carbon` (8.5%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (67.4%) | `carbon` (32.0%) | `ABSENT` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (91.3%) | `graphite_plate` (3.0%) | `platinum_wire` (2.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (92.7%) | `divided` (5.5%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.5%) | `NH4` (1.1%) | `NEt4` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (93.3%) | `SO4` (1.6%) | `PF6` (1.4%) | ✓ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (16.8%) | `tetraaryl_borate` (3.1%) | `as_solvent_cyclic_ether` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `ammonium_PTC_organocat` (0.8%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `ABSENT` (85.2%) | `halogenated_aliphatic` (9.3%) | `polar_aprotic_nitrile` (3.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `__ABSENT__` | `__ABSENT__` (100%) | `CC#N` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(S(=O)(=O)O)` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #1468  yield=90.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json) (反应 idx 在该 JSON 内 = #9)

```
CC#N.C=CC1CCCCC1.c1ccc([Se][Se]c2ccccc2)cc1>>CC(=O)NC(C[Se]c1ccccc1)C1CCCCC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (65.0%) | `graphite_rod` (30.1%) | `graphite_generic` (2.5%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.9%) | `carbon` (1.1%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_generic` (97.0%) | `platinum_plate` (2.8%) | `platinum_wire` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.1%) | `divided` (1.4%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (59.2%) | `Li` (19.1%) | `ABSENT` (18.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (31.8%) | `I` (31.3%) | `ABSENT` (20.3%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (14.1%) | `carboxylic_acid` (7.9%) | `tetraaryl_borate` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `ABSENT` (71.7%) | `polar_aprotic_nitrile` (24.8%) | `halogenated_aliphatic` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `__ABSENT__` | `__ABSENT__` (99%) | `CC#N` (1%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(S(=O)(=O)O)` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].CC(=O)[` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1469  yield=95.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_24_7114-7121.json) (反应 idx 在该 JSON 内 = #10)

```
CC#N.C=CCCCC.c1ccc([Se][Se]c2ccccc2)cc1>>CCCCC(C[Se]c1ccccc1)NC(C)=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_plate` (54.4%) | `reticulated_vitreous_carbon` (30.7%) | `graphite_rod` (13.7%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (74.9%) | `carbon` (24.9%) | `ABSENT` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (89.8%) | `graphite_plate` (6.8%) | `platinum_generic` (1.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (95.8%) | `ABSENT` (2.5%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.4%) | `NEt4` (1.7%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (92.0%) | `SO4` (2.6%) | `I` (1.9%) | ✗ |
| 试剂大类 | 103 | `sulfonic_acid` | `ABSENT` (11.8%) | `tetraaryl_borate` (2.8%) | `ketone` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `ammonium_PTC_organocat` (0.4%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `ABSENT` (96.7%) | `halogenated_aliphatic` (2.5%) | `polar_aprotic_nitrile` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `__ABSENT__` | `__ABSENT__` (100%) | `CC#N` (2%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(S(=O)(=O)O)` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC[N+](CC)(CC)CC.F` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1470  yield=38.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCC.COC(=O)NN.Brc1ccc2ccncc2c1>>CCCC(CC(=O)OC)c1nccc2ccc(Br)cc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.3%) | `ABSENT` (2.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (99.1%) | `graphite_generic` (0.5%) | `ABSENT` (0.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `ABSENT` (4.1%) | `sacrificial_iron` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.4%) | `ABSENT` (1.6%) | `platinum_wire` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.4%) | `ABSENT` (1.5%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (95.2%) | `Na` (3.6%) | `ABSENT` (0.6%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (90.7%) | `Cl` (2.0%) | `ABSENT` (1.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.4%) | `azide_source` (2.7%) | `as_solvent_cyclic_ether` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (91.5%) | `ABSENT` (6.3%) | `Pt_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (99.3%) | `polar_aprotic_nitrile` (0.4%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (81%) | `CO` (8%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (19%) | `__OTHER__` (12%) | `__ABSENT__` (11%) | set ✗ / any ✗ |

---

### Reaction #1471  yield=45.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #1)

```
C=CCCC.COC(=O)NN.N#Cc1cccc2cnccc12>>CCCC(CC(=O)OC)c1nccc2c(C#N)cccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.2%) | `ABSENT` (2.8%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (84.1%) | `carbon_generic` (14.7%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.9%) | `sacrificial_iron` (3.6%) | `ABSENT` (2.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.9%) | `iron_generic` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (54.9%) | `undivided` (45.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.4%) | `ABSENT` (6.6%) | `Na` (2.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (92.8%) | `ABSENT` (6.4%) | `I` (0.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (22.5%) | `as_solvent_polar_protic_alcoho` (9.8%) | `azide_source` (2.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (99.4%) | `ferrocene_mediator` (0.4%) | `Co_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (99.8%) | `polar_aprotic_nitrile` (0.2%) | `cyclic_ether` (0.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CO` (92%) | `CC#N` (5%) | `C1CCOC1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `C1=CCCCC1` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `c1ccc2c(c1)-c1nc3c` (12%) | `[Fe+2].c1ccc2c(c1)` (7%) | `__ABSENT__` (2%) | set ✗ / any ✗ |

---

### Reaction #1472  yield=60.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #2)

```
COC(=O)NN.Cn1c(=O)cnc2ccccc21.C=CCCOC(=O)C(C)c1ccc2cc(OC)ccc2c1>>COC(=O)CC(CCOC(=O)C(C)c1ccc2cc(OC)ccc2c1)c1nc2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (92.4%) | `graphite_generic` (5.9%) | `reticulated_vitreous_carbon` (1.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.5%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.7%) | `platinum_wire` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (61.8%) | `NBu4` (36.9%) | `Na` (1.1%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (80.4%) | `BF4` (18.4%) | `ClO4` (0.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.2%) | `as_solvent_polar_protic_alcoho` (7.3%) | `tetraaryl_borate` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (59.5%) | `ABSENT` (29.0%) | `Co_complex` (3.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (59.4%) | `polar_protic_alcohol` (37.6%) | `ABSENT` (1.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (99%) | `COCCOC` (0%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (15%) | `c1ccc2c(c1)-c1nc3c` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #1473  yield=60.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1ccccc1Br.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(c1ccccc1Br)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `ABSENT` (0.8%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (97.5%) | `carbon_generic` (1.1%) | `reticulated_vitreous_carbon` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `ABSENT` (0.5%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.9%) | `ABSENT` (0.0%) | `platinum_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (100.0%) | `NEt4` (0.0%) | `Na` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (97.2%) | `PF6` (1.2%) | `carboxylate` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (18.3%) | `ABSENT` (8.5%) | `as_solvent_cyclic_ether` (2.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (78.9%) | `Co_complex` (5.3%) | `pyridine_organocat` (4.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (93.1%) | `polar_aprotic_nitrile` (4.6%) | `halogenated_aliphatic` (1.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (97%) | `CO` (7%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (88%) | `CO` (9%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (9%) | `[Fe+2].c1ccc2c(c1)` (5%) | `c1ccc2c(c1)-c1nc3c` (1%) | set ✗ / any ✗ |

---

### Reaction #1474  yield=60.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #4)

```
C=CCCC.COC(=O)NN.C=CCn1c(=O)cnc2ccccc21>>C=CCn1c(=O)c(C(CCC)CC(=O)OC)nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.3%) | `ABSENT` (5.6%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (53.7%) | `carbon_felt` (43.9%) | `ABSENT` (1.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.1%) | `ABSENT` (3.0%) | `sacrificial_iron` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `ABSENT` (0.2%) | `iron_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (98.1%) | `undivided` (1.8%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (53.5%) | `ABSENT` (24.0%) | `Na` (21.7%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (48.4%) | `BF4` (38.8%) | `I` (4.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.1%) | `as_solvent_polar_protic_alcoho` (11.2%) | `metal_oxide_oxidant` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (92.8%) | `ABSENT` (3.0%) | `organic_neutral_cat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (96.2%) | `polar_aprotic_nitrile` (2.8%) | `cyclic_ether` (0.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CO` (34%) | `CC#N` (22%) | `CCO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Fe]` | `__OTHER__` (5%) | `[Fe+2].c1ccc2c(c1)` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |

---

### Reaction #1475  yield=58.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #5)

```
C=CCCC.COC(=O)NN.Cc1ccc2cnccc2c1>>CCCC(CC(=O)OC)c1nccc2cc(C)ccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.9%) | `ABSENT` (2.0%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (62.0%) | `carbon_generic` (24.9%) | `ABSENT` (9.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.0%) | `ABSENT` (3.0%) | `sacrificial_iron` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.2%) | `ABSENT` (0.6%) | `iron_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (68.3%) | `undivided` (31.6%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.3%) | `ABSENT` (9.8%) | `Na` (9.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (87.5%) | `ABSENT` (7.4%) | `carboxylate` (2.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (30.2%) | `as_solvent_polar_protic_alcoho` (7.5%) | `azide_source` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (97.5%) | `ABSENT` (0.6%) | `Rh_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (99.5%) | `polar_aprotic_nitrile` (0.4%) | `tfe` (0.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (76%) | `CO` (12%) | `CCO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (11%) | `c1ccc2c(c1)-c1nc3c` (7%) | `__OTHER__` (6%) | set ✗ / any ✗ |

---

### Reaction #1476  yield=55.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #6)

```
C=CCCC.c1ccc2cnccc2c1.COC(=O)NN>>CCCC(CC(=O)OC)c1nccc2ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.0%) | `ABSENT` (6.9%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (77.7%) | `carbon_generic` (12.5%) | `ABSENT` (4.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.5%) | `ABSENT` (11.6%) | `sacrificial_iron` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.8%) | `ABSENT` (1.9%) | `iron_generic` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (62.8%) | `ABSENT` (37.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (62.3%) | `Na` (34.0%) | `Li` (1.9%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (73.7%) | `carboxylate` (11.7%) | `Br` (2.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.4%) | `as_solvent_polar_protic_alcoho` (5.1%) | `azide_source` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (84.0%) | `ABSENT` (9.9%) | `Pt_complex` (2.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (99.4%) | `polar_aprotic_nitrile` (0.5%) | `cyclic_ether` (0.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (83%) | `CO` (12%) | `O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (14%) | `[Pt]` (9%) | `__OTHER__` (7%) | set ✗ / any ✗ |

---

### Reaction #1477  yield=55.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #7)

```
COC(=O)NN.Cn1c(=O)cnc2ccccc21.C=CCCOC(=O)C(C)(C)Oc1ccc(C(=O)c2ccc(Cl)cc2)cc1>>COC(=O)CC(CCOC(=O)C(C)(C)Oc1ccc(C(=O)c2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `ABSENT` (0.5%) | `platinum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (98.3%) | `graphite_generic` (1.1%) | `graphite_rod` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.4%) | `sacrificial_iron` (2.0%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (98.8%) | `platinum_wire` (0.5%) | `iron_generic` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (0.9%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (57.2%) | `ABSENT` (34.2%) | `Na` (8.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (68.7%) | `BF4` (18.5%) | `I` (6.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.1%) | `as_solvent_polar_protic_alcoho` (5.8%) | `azide_source` (2.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (57.5%) | `ABSENT` (31.4%) | `Co_complex` (2.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (69.6%) | `polar_aprotic_nitrile` (28.6%) | `ABSENT` (0.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (91%) | `CO` (2%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__OTHER__` (8%) | `c1ccc2c(c1)-c1nc3c` (7%) | `__ABSENT__` (5%) | set ✗ / any ✗ |

---

### Reaction #1478  yield=57.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #8)

```
c1ccc2cnccc2c1.C=CCCCC.COC(=O)NN>>CCCCC(CC(=O)OC)c1nccc2ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (89.9%) | `ABSENT` (9.5%) | `platinum` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (52.6%) | `graphite_generic` (24.4%) | `reticulated_vitreous_carbon` (12.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `ABSENT` (15.0%) | `carbon` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (97.3%) | `ABSENT` (2.0%) | `platinum_plate` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (80.5%) | `Na` (18.2%) | `NEt4` (0.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (48.7%) | `carboxylate` (29.5%) | `Br` (6.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `azide_source` (4.3%) | `ketone` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (80.6%) | `Fe_complex` (13.2%) | `Pt_complex` (2.6%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (97.9%) | `polar_aprotic_nitrile` (1.8%) | `halogenated_aliphatic` (0.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (99%) | `O` (39%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[Fe+2].c1ccc2c(c1)` (0%) | set ✗ / any ✗ |

---

### Reaction #1479  yield=69.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #9)

```
COC(=O)NN.Cn1c(=O)cnc2ccccc21.C=CCCOC(=O)c1ccc(S(=O)(=O)N(CCC)CCC)cc1>>CCCN(CCC)S(=O)(=O)c1ccc(C(=O)OCCC(CC(=O)OC)c2n…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.5%) | `ABSENT` (0.8%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (84.7%) | `graphite_generic` (8.1%) | `ABSENT` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.7%) | `ABSENT` (2.9%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (61.9%) | `platinum_plate` (21.6%) | `ABSENT` (13.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.7%) | `ABSENT` (1.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.8%) | `ABSENT` (1.0%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (80.8%) | `I` (8.5%) | `ABSENT` (7.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (11.3%) | `ABSENT` (8.2%) | `as_solvent_polar_protic_alcoho` (4.3%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (71.7%) | `Fe_complex` (14.3%) | `ammonium_PTC_organocat` (9.7%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (64.5%) | `polar_aprotic_nitrile` (30.0%) | `ABSENT` (3.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (91%) | `CO` (6%) | `COCCOC` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (96%) | `__ABSENT__` (4%) | `O=P([O-])([O-])[O-` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #1480  yield=69.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #10)

```
COC(=O)NN.Cn1c(=O)cnc2ccccc21.C=CCCOC(=O)C(C)c1ccc(CC(C)C)cc1>>COC(=O)CC(CCOC(=O)C(C)c1ccc(CC(C)C)cc1)c1nc2ccccc2n(C)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `ABSENT` (0.2%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (92.6%) | `reticulated_vitreous_carbon` (3.8%) | `graphite_generic` (2.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.7%) | `nickel` (3.5%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.0%) | `platinum_plate` (0.3%) | `nickel_generic` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (79.9%) | `ABSENT` (20.0%) | `Na` (0.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (49.7%) | `BF4` (48.3%) | `PF6` (1.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (5.5%) | `cf3_source` (5.0%) | `ABSENT` (3.0%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (76.4%) | `Fe_complex` (14.1%) | `ferrocene_mediator` (3.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (45.4%) | `polar_aprotic_nitrile` (45.0%) | `halogenated_aliphatic` (5.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (91%) | `CO` (2%) | `CCO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (79%) | `C[Si](C)(C)N=[N+]=` (16%) | `CO` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Fe]` | `__ABSENT__` (100%) | `[cH]12->[Fe+2]3456` (0%) | `[Fe+2].c1ccc2c(c1)` (0%) | set ✗ / any ✗ |

---

### Reaction #1481  yield=69.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #11)

```
C=CC(=O)OC.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(C(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (74.2%) | `platinum` (21.5%) | `ABSENT` (3.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (96.4%) | `platinum_generic` (1.2%) | `ABSENT` (1.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.1%) | `nickel` (4.5%) | `ABSENT` (4.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (86.9%) | `platinum_wire` (3.5%) | `iron_generic` (2.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (64.8%) | `divided` (34.2%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.7%) | `ABSENT` (2.9%) | `Na` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (79.6%) | `Br` (9.3%) | `ABSENT` (8.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (6.0%) | `pyridine` (4.6%) | `ABSENT` (4.1%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (94.7%) | `ferrocene_mediator` (2.3%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (91.2%) | `polar_aprotic_nitrile` (5.2%) | `ketone` (0.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (95%) | `C1CCOC1` (5%) | `CO` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (73%) | `__ABSENT__` (19%) | `O=S(=O)(O)C(F)(F)F` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (32%) | `[O]=[Fe][O][Fe]=[O` (16%) | `c1ccc2c(c1)-c1nc3c` (3%) | set ✗ / any ✗ |

---

### Reaction #1482  yield=61.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #12)

```
COC(=O)NN.Cn1c(=O)cnc2ccccc21.C=CCCOC(=O)C(C)c1ccc(-c2ccccc2)c(F)c1>>COC(=O)CC(CCOC(=O)C(C)c1ccc(-c2ccccc2)c(F)c1)c1n…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.5%) | `ABSENT` (1.1%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (92.1%) | `graphite_generic` (5.6%) | `ABSENT` (1.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.4%) | `ABSENT` (7.3%) | `nickel` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.6%) | `ABSENT` (1.5%) | `nickel_generic` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `divided` (0.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (69.0%) | `ABSENT` (30.6%) | `Na` (0.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (59.0%) | `BF4` (37.4%) | `Cl` (1.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.8%) | `as_solvent_polar_protic_alcoho` (7.5%) | `cf3_source` (3.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (65.0%) | `ABSENT` (29.1%) | `Co_complex` (1.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (61.0%) | `polar_aprotic_nitrile` (35.1%) | `halogenated_aliphatic` (1.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (93%) | `CO` (1%) | `CCO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (17%) | `c1ccc2c(c1)-c1nc3c` (2%) | `__OTHER__` (2%) | set ✗ / any ✓ |

---

### Reaction #1483  yield=65.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #13)

```
C=Cc1ccccc1Cl.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(c1ccccc1Cl)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (87.1%) | `ABSENT` (9.3%) | `platinum` (3.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (97.9%) | `ABSENT` (0.8%) | `graphite_generic` (0.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.0%) | `ABSENT` (7.4%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.1%) | `ABSENT` (0.6%) | `platinum_foil` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (94.7%) | `ABSENT` (3.3%) | `divided` (2.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.2%) | `Na` (0.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (90.8%) | `Br` (4.0%) | `ClO4` (1.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.1%) | `as_solvent_polar_protic_alcoho` (4.0%) | `azide_source` (3.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (40.1%) | `ABSENT` (15.0%) | `Pt_complex` (10.7%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (77.4%) | `polar_aprotic_nitrile` (18.8%) | `halogenated_aliphatic` (2.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (96%) | `CO` (18%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (5%) | `[Fe+2].c1ccc2c(c1)` (3%) | `[O]=[Fe][O][Fe]=[O` (0%) | set ✗ / any ✗ |

---

### Reaction #1484  yield=68.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #14)

```
C=CCCC.COC(=O)NN.C=C(C)Cn1c(=O)cnc2ccccc21>>C=C(C)Cn1c(=O)c(C(CCC)CC(=O)OC)nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.0%) | `ABSENT` (4.6%) | `platinum` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_generic` (58.5%) | `carbon_felt` (40.0%) | `graphite_generic` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.7%) | `ABSENT` (3.4%) | `sacrificial_iron` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.9%) | `iron_generic` (0.1%) | `ABSENT` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (98.2%) | `undivided` (1.8%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (65.3%) | `ABSENT` (17.4%) | `Na` (15.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (53.6%) | `ABSENT` (31.9%) | `I` (5.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.5%) | `as_solvent_polar_protic_alcoho` (13.2%) | `metal_oxide_oxidant` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (91.9%) | `ABSENT` (2.5%) | `Mn_complex` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (90.0%) | `polar_aprotic_nitrile` (7.8%) | `halogenated_aliphatic` (0.8%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (70%) | `CO` (5%) | `O` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Fe]` | `[Fe+2].c1ccc2c(c1)` (4%) | `__OTHER__` (3%) | `c1ccc2c(c1)-c1nc3c` (1%) | set ✗ / any ✗ |

---

### Reaction #1485  yield=62.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #15)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.NNC(=O)OC1CCCCC1>>CCC[C@H](CC(=O)OC1CCCCC1)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (95.6%) | `carbon_generic` (3.8%) | `reticulated_vitreous_carbon` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.2%) | `nickel` (0.4%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.8%) | `nickel_foam` (0.1%) | `platinum_wire` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (71.7%) | `undivided` (24.9%) | `divided` (3.4%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (71.3%) | `NBu4` (20.8%) | `Na` (6.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (85.5%) | `BF4` (6.9%) | `I` (5.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (24.9%) | `as_solvent_polar_protic_alcoho` (4.1%) | `tetraaryl_borate` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (58.6%) | `Co_complex` (14.9%) | `Ni_complex` (12.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (89.6%) | `polar_protic_alcohol` (7.4%) | `halogenated_aliphatic` (0.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (26%) | `CO` (0%) | `COCCOC` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Fe]` | `__ABSENT__` (1%) | `__OTHER__` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #1486  yield=62.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #16)

```
COC(=O)NN.Cn1c(=O)cnc2ccccc21.C=CCCOC(=O)C(C)(C)Oc1ccc(CCNC(=O)c2ccc(Cl)cc2)cc1>>COC(=O)CC(CCOC(=O)C(C)(C)Oc1ccc(CCNC…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `ABSENT` (0.5%) | `platinum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (99.9%) | `carbon_generic` (0.0%) | `reticulated_vitreous_carbon` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.2%) | `sacrificial_iron` (0.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.6%) | `platinum_plate` (0.2%) | `platinum_wire` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.4%) | `ABSENT` (3.1%) | `divided` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.1%) | `ABSENT` (18.0%) | `Na` (4.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (47.2%) | `BF4` (46.5%) | `I` (3.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.1%) | `as_solvent_polar_protic_alcoho` (7.1%) | `tetraaryl_borate` (3.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (58.8%) | `ABSENT` (31.0%) | `Co_complex` (3.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (75.1%) | `polar_aprotic_nitrile` (23.4%) | `cyclic_ether` (0.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (78%) | `COCCOC` (7%) | `CO` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (11%) | `__OTHER__` (7%) | `c1ccc2c(c1)-c1nc3c` (2%) | set ✗ / any ✗ |

---

### Reaction #1487  yield=67.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #17)

```
C=CCCC.COC(=O)NN.O=C(Cn1c(=O)cnc2ccccc21)OCc1ccco1>>CCCC(CC(=O)OC)c1nc2ccccc2n(CC(=O)OCc2ccco2)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.9%) | `platinum` (10.3%) | `ABSENT` (4.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (50.2%) | `carbon_generic` (33.2%) | `platinum_generic` (10.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `sacrificial_iron` (0.7%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (100.0%) | `iron_generic` (0.0%) | `platinum_wire` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (81.6%) | `undivided` (16.3%) | `divided` (2.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (54.8%) | `NBu4` (35.1%) | `Na` (9.6%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (74.5%) | `BF4` (17.7%) | `Cl` (4.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (33.6%) | `as_solvent_polar_protic_alcoho` (6.4%) | `metal_oxide_oxidant` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (92.2%) | `ABSENT` (2.0%) | `organic_neutral_cat` (1.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (94.7%) | `polar_aprotic_nitrile` (2.9%) | `ketone` (0.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (18%) | `CCO` (5%) | `CO` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCOC(C)=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__OTHER__` (1%) | `[Fe+2].c1ccc2c(c1)` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |

---

### Reaction #1488  yield=61.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #18)

```
C=CCCC.c1ccc2c(c1)cnc1ccccc12.COC(=O)NN>>CCCC(CC(=O)OC)c1nc2ccccc2c2ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.3%) | `ABSENT` (5.7%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (99.1%) | `carbon_generic` (0.3%) | `ABSENT` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (81.0%) | `ABSENT` (13.0%) | `sacrificial_iron` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (97.8%) | `ABSENT` (0.8%) | `platinum_foil` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (65.9%) | `ABSENT` (33.8%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.6%) | `Na` (1.4%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (98.0%) | `Cl` (0.7%) | `ABSENT` (0.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (30.6%) | `as_solvent_polar_protic_alcoho` (5.2%) | `azide_source` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `Fe_complex` (96.0%) | `ABSENT` (2.4%) | `Co_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (99.0%) | `polar_aprotic_nitrile` (0.8%) | `cyclic_ether` (0.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CO` (46%) | `CC#N` (45%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Fe+2].c1ccc2c(c1)` (23%) | `O.[Br][Mn][Br]` (5%) | `c1ccc2c(c1)-c1nc3c` (3%) | set ✗ / any ✗ |

---

### Reaction #1489  yield=64.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #19)

```
C=CCCC.COC(=O)NN.Cn1c(-c2ccccc2)c(-c2ccccc2)ncc1=O>>CCCC(CC(=O)OC)c1nc(-c2ccccc2)c(-c2ccccc2)n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `ABSENT` (0.8%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (96.7%) | `graphite_generic` (1.8%) | `carbon_generic` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.5%) | `ABSENT` (0.3%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.9%) | `platinum_foil` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (61.1%) | `ABSENT` (38.5%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (52.8%) | `Na` (37.9%) | `NBu4` (8.1%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.5%) | `molecular_no_ion` (10.5%) | `BF4` (6.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `as_solvent_polar_protic_alcoho` (9.4%) | `azide_source` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (87.8%) | `Pt_complex` (4.6%) | `ferrocene_mediator` (3.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (91.7%) | `polar_aprotic_nitrile` (6.6%) | `cyclic_ether` (0.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (43%) | `CO` (11%) | `O` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=C([O-])[O-].[Na+` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Fe]` | `__OTHER__` (19%) | `[Fe+2].c1ccc2c(c1)` (7%) | `c1ccc2c(c1)-c1nc3c` (1%) | set ✗ / any ✗ |

---

### Reaction #1490  yield=70.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #20)

```
COC(=O)NN.Cn1c(=O)cnc2ccccc21.C=CCCOC(=O)C(C)c1cccc(C(=O)c2ccccc2)c1>>COC(=O)CC(CCOC(=O)C(C)c1cccc(C(=O)c2ccccc2)c1)c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (55.2%) | `carbon_felt` (43.2%) | `graphite_rod` (0.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.5%) | `nickel` (5.6%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (94.5%) | `nickel_generic` (1.4%) | `platinum_plate` (1.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (67.8%) | `ABSENT` (31.7%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (65.0%) | `ABSENT` (34.3%) | `PF6` (0.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (4.3%) | `as_solvent_polar_protic_alcoho` (4.1%) | `cf3_source` (3.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (62.3%) | `Fe_complex` (28.8%) | `ferrocene_mediator` (3.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (55.9%) | `polar_aprotic_nitrile` (40.1%) | `ABSENT` (1.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (88%) | `CO` (1%) | `CCO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCOC(C)=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Fe+2].c1ccc2c(c1)` (0%) | set ✗ / any ✗ |

---

### Reaction #1491  yield=70.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #21)

```
COC(=O)NN.Cn1c(=O)cnc2ccccc21.C=CCCOC(=O)c1ccccc1OC(C)=O>>COC(=O)CC(CCOC(=O)c1ccccc1OC(C)=O)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.3%) | `platinum` (4.8%) | `ABSENT` (2.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (97.2%) | `ABSENT` (1.1%) | `reticulated_vitreous_carbon` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.6%) | `ABSENT` (2.0%) | `nickel` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.6%) | `ABSENT` (1.4%) | `platinum_wire` (0.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `divided` (0.6%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `ABSENT` (2.0%) | `Na` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (95.6%) | `ABSENT` (3.9%) | `I` (0.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.8%) | `as_solvent_polar_protic_alcoho` (4.7%) | `as_solvent_halogenated_aliphat` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (74.6%) | `ABSENT` (22.7%) | `ammonium_PTC_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (94.9%) | `polar_aprotic_nitrile` (2.9%) | `halogenated_aliphatic` (1.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (66%) | `CO` (13%) | `COCCOC` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCOC(C)=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (13%) | `[Fe+2].c1ccc2c(c1)` (11%) | `c1ccc2c(c1)-c1nc3c` (10%) | set ✗ / any ✗ |

---

### Reaction #1492  yield=70.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #22)

```
C=CCCC.COC(=O)NN.Cn1c(=O)cnc2cc(Br)ccc21>>CCCC(CC(=O)OC)c1nc2cc(Br)ccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.6%) | `ABSENT` (11.2%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (96.8%) | `ABSENT` (2.3%) | `carbon_generic` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (79.3%) | `ABSENT` (19.5%) | `sacrificial_iron` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (96.0%) | `ABSENT` (3.7%) | `platinum_wire` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (80.7%) | `undivided` (17.6%) | `divided` (1.7%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.6%) | `Na` (1.0%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.7%) | `I` (0.8%) | `Cl` (0.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.9%) | `as_solvent_polar_protic_alcoho` (8.7%) | `azide_source` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (93.0%) | `ABSENT` (3.1%) | `ferrocene_mediator` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (97.2%) | `polar_aprotic_nitrile` (2.2%) | `halogenated_aliphatic` (0.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (93%) | `CO` (8%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (15%) | `__OTHER__` (11%) | `c1ccc2c(c1)-c1nc3c` (6%) | set ✗ / any ✗ |

---

### Reaction #1493  yield=70.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #23)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.Cc1ccccc1CCOC(=O)NN>>CCCC(CC(=O)OCCc1ccccc1C)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `ABSENT` (0.4%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (54.6%) | `carbon_generic` (39.0%) | `ABSENT` (2.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.2%) | `nickel` (7.5%) | `ABSENT` (1.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (95.9%) | `nickel_foam` (1.9%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (97.6%) | `divided` (1.2%) | `undivided` (1.2%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (58.2%) | `NBu4` (25.7%) | `Na` (15.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (71.8%) | `BF4` (20.4%) | `I` (4.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (13.5%) | `ABSENT` (13.4%) | `thiol` (2.1%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (29.2%) | `Co_complex` (24.4%) | `ferrocene_mediator` (22.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (70.0%) | `polar_aprotic_nitrile` (16.2%) | `polar_aprotic_sulfoxide` (4.8%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CO` (3%) | `CC#N` (2%) | `ClCCl` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (93%) | `C[Si](C)(C)N=[N+]=` (1%) | `CO` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Fe]` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Cl-].[Cl-].[Ni+2]` (0%) | set ✗ / any ✗ |

---

### Reaction #1494  yield=80.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #24)

```
C=CCCC.COC(=O)NN.Cn1ncc(=O)n(C)c1=O>>CCCC(CC(=O)OC)c1nn(C)c(=O)n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `ABSENT` (0.6%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (97.4%) | `carbon_generic` (1.6%) | `graphite_generic` (0.9%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.2%) | `ABSENT` (1.5%) | `sacrificial_iron` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.6%) | `platinum_foil` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (88.9%) | `undivided` (11.0%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (87.4%) | `NBu4` (10.3%) | `Na` (1.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (91.3%) | `BF4` (7.8%) | `I` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (12.2%) | `ABSENT` (7.9%) | `azide_source` (3.1%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (93.5%) | `ferrocene_mediator` (2.0%) | `ABSENT` (1.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (90.8%) | `polar_aprotic_nitrile` (6.1%) | `ABSENT` (2.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (12%) | `CO` (6%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (82%) | `C[Si](C)(C)N=[N+]=` (11%) | `CO` (5%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `c1ccc2c(c1)-c1nc3c` (5%) | `__OTHER__` (5%) | `__ABSENT__` (2%) | set ✗ / any ✗ |

---

### Reaction #1495  yield=73.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #25)

```
COC(=O)NN.Cn1c(=O)cnc2ccccc21.C=CCCCOC(=O)C(C)c1ccc(CC(C)C)cc1>>COC(=O)CC(CCCOC(=O)C(C)c1ccc(CC(C)C)cc1)c1nc2ccccc2n(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `ABSENT` (0.5%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (85.7%) | `reticulated_vitreous_carbon` (4.8%) | `graphite_generic` (3.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (91.5%) | `nickel` (5.4%) | `ABSENT` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.0%) | `nickel_generic` (0.5%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.8%) | `divided` (2.2%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.5%) | `ABSENT` (11.0%) | `Na` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (47.4%) | `ABSENT` (47.0%) | `PF6` (2.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (8.7%) | `alkali_carboxylate` (3.4%) | `alkali_other_salt` (3.0%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (43.7%) | `ferrocene_mediator` (26.1%) | `Fe_complex` (18.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (64.6%) | `polar_aprotic_nitrile` (24.0%) | `halogenated_aliphatic` (5.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (80%) | `CO` (14%) | `CCO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (89%) | `C[Si](C)(C)N=[N+]=` (3%) | `CC(=O)[O-].[Na+]` (2%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `[cH]12->[Fe+2]3456` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #1496  yield=79.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #26)

```
C=CCCC.COC(=O)NN.Cc1cc2ncc(=O)n(C)c2cc1C>>CCCC(CC(=O)OC)c1nc2cc(C)c(C)cc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `ABSENT` (1.2%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (99.4%) | `carbon_generic` (0.4%) | `ABSENT` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.8%) | `ABSENT` (2.2%) | `sacrificial_iron` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.8%) | `ABSENT` (0.2%) | `iron_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (94.3%) | `undivided` (5.5%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `ABSENT` (8.8%) | `Na` (6.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (88.3%) | `ABSENT` (9.0%) | `I` (1.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (23.9%) | `ABSENT` (12.1%) | `azide_source` (2.9%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (92.6%) | `ferrocene_mediator` (2.9%) | `Co_complex` (1.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (97.2%) | `polar_aprotic_nitrile` (2.3%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (60%) | `CO` (12%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `C[Si](C)(C)N=[N+]=` (3%) | `CO` (2%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `c1ccc2c(c1)-c1nc3c` (8%) | `[Fe+2].c1ccc2c(c1)` (5%) | `__OTHER__` (3%) | set ✗ / any ✗ |

---

### Reaction #1497  yield=76.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #27)

```
C=CCCC.COC(=O)NN.CCOC(=O)Cn1c(=O)cnc2ccccc21>>CCCC(CC(=O)OC)c1nc2ccccc2n(CC(=O)OCC)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `ABSENT` (4.3%) | `platinum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (63.5%) | `carbon_felt` (34.7%) | `reticulated_vitreous_carbon` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.4%) | `ABSENT` (1.7%) | `sacrificial_iron` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.7%) | `iron_generic` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (97.7%) | `undivided` (2.1%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (44.4%) | `Na` (29.9%) | `NBu4` (24.8%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (73.4%) | `BF4` (15.1%) | `I` (7.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (19.2%) | `ABSENT` (15.7%) | `amide` (1.8%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (89.2%) | `Co_complex` (1.9%) | `ferrocene_mediator` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (89.4%) | `polar_aprotic_nitrile` (7.2%) | `cyclic_ether` (1.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (30%) | `CO` (7%) | `CCO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (84%) | `CO` (10%) | `C[Si](C)(C)N=[N+]=` (3%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__OTHER__` (7%) | `[Fe+2].c1ccc2c(c1)` (2%) | `c1ccc2c(c1)-c1nc3c` (1%) | set ✗ / any ✗ |

---

### Reaction #1498  yield=78.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #28)

```
C=Cc1ccccc1C.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(c1ccccc1C)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.7%) | `ABSENT` (6.5%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (96.0%) | `ABSENT` (3.5%) | `carbon_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.5%) | `ABSENT` (3.6%) | `nickel` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.1%) | `ABSENT` (2.6%) | `platinum_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (80.5%) | `divided` (16.0%) | `ABSENT` (3.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.1%) | `ABSENT` (6.7%) | `Na` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (67.6%) | `ABSENT` (23.8%) | `PF6` (2.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.4%) | `as_solvent_polar_protic_alcoho` (11.3%) | `azide_source` (4.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (84.6%) | `Co_complex` (6.6%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (96.9%) | `polar_aprotic_nitrile` (1.9%) | `halogenated_aliphatic` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (65%) | `CO` (18%) | `CCO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (8%) | `c1ccc2c(c1)-c1nc3c` (6%) | `O.[Br][Mn][Br]` (2%) | set ✗ / any ✗ |

---

### Reaction #1499  yield=75.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #29)

```
C=CCCC.Cn1c(=O)cnc2ccccc21.Cc1ccc(CCOC(=O)NN)cc1>>CCC(CC(=O)OCCc1ccc(C)cc1)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (96.6%) | `graphite_rod` (1.3%) | `carbon_generic` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.8%) | `nickel` (13.1%) | `carbon` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (41.7%) | `nickel_foam` (22.6%) | `platinum_plate` (22.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (83.3%) | `undivided` (14.8%) | `ABSENT` (1.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.6%) | `ABSENT` (4.1%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (91.0%) | `ABSENT` (7.4%) | `OH` (0.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.7%) | `tetraaryl_borate` (2.8%) | `as_solvent_cyclic_ether` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `ferrocene_mediator` (63.6%) | `ABSENT` (25.6%) | `Fe_complex` (6.0%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (69.1%) | `ABSENT` (11.3%) | `polar_aprotic_nitrile` (7.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CO` (1%) | `COCCOC` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (69%) | `[Fe+2].c1cc[cH-]c1` (18%) | `[cH]12->[Fe+2]3456` (3%) | set ✗ / any ✗ |

---

### Reaction #1500  yield=78.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #30)

```
C=CCCC.COC(=O)NN.Cn1c(=O)cnc2cc3ccccc3cc21>>CCCC(CC(=O)OC)c1nc2cc3ccccc3cc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (89.2%) | `ABSENT` (10.6%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (98.8%) | `carbon_generic` (0.6%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.1%) | `ABSENT` (9.9%) | `sacrificial_iron` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `ABSENT` (0.6%) | `platinum_foil` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (95.8%) | `undivided` (4.0%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (65.7%) | `Na` (24.4%) | `ABSENT` (7.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (66.9%) | `ABSENT` (13.2%) | `I` (10.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (16.0%) | `ABSENT` (12.0%) | `azide_source` (2.8%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (86.0%) | `Co_complex` (3.9%) | `ABSENT` (3.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (90.5%) | `polar_aprotic_nitrile` (8.5%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (84%) | `CO` (5%) | `COCCOC` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (88%) | `CO` (7%) | `C[Si](C)(C)N=[N+]=` (3%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (7%) | `__OTHER__` (6%) | `c1ccc2c(c1)-c1nc3c` (5%) | set ✗ / any ✗ |

---

