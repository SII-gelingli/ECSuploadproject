# Test 预测 part 4 — 反应 #1501-#2000

[← 返回 INDEX](INDEX.md)

### Reaction #1501  yield=78.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #31)

```
C=CCCC.COC(=O)NN.Cn1c(=O)cnc2cc(F)ccc21>>CCCC(CC(=O)OC)c1nc2cc(F)ccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (73.5%) | `ABSENT` (26.3%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (93.9%) | `ABSENT` (5.0%) | `carbon_generic` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (75.4%) | `ABSENT` (24.3%) | `sacrificial_iron` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.1%) | `ABSENT` (2.8%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (84.2%) | `undivided` (13.9%) | `divided` (1.9%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (82.4%) | `ABSENT` (10.7%) | `Na` (5.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (81.8%) | `ABSENT` (13.6%) | `Cl` (1.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.0%) | `as_solvent_polar_protic_alcoho` (11.5%) | `azide_source` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (88.5%) | `Pt_complex` (3.7%) | `ABSENT` (3.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (95.8%) | `polar_aprotic_nitrile` (3.2%) | `halogenated_aliphatic` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (70%) | `CO` (6%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Fe]` | `[Fe+2].c1ccc2c(c1)` (13%) | `__OTHER__` (12%) | `c1ccc2c(c1)-c1nc3c` (3%) | set ✗ / any ✗ |

---

### Reaction #1502  yield=77.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #32)

```
C=CCCC.COC(=O)NN.CC1CCC(C(C)C)C(OC(=O)Cn2c(=O)cnc3ccccc32)C1>>CCCC(CC(=O)OC)c1nc2ccccc2n(CC(=O)O[C@H]2C[C@@H](C)CC[C@…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.3%) | `ABSENT` (2.0%) | `platinum` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (54.9%) | `graphite_generic` (30.0%) | `carbon_felt` (6.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.5%) | `sacrificial_iron` (7.6%) | `ABSENT` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.1%) | `iron_generic` (0.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (83.2%) | `undivided` (16.6%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (75.7%) | `Na` (19.9%) | `ABSENT` (3.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (36.1%) | `I` (29.5%) | `Cl` (23.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.3%) | `as_solvent_polar_protic_alcoho` (16.5%) | `metal_oxide_oxidant` (1.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (47.8%) | `ABSENT` (33.8%) | `Co_complex` (5.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (91.5%) | `polar_aprotic_nitrile` (4.3%) | `halogenated_aliphatic` (2.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (30%) | `CO` (7%) | `CCO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (10%) | `__OTHER__` (3%) | `c1ccc2c(c1)-c1nc3c` (1%) | set ✗ / any ✗ |

---

### Reaction #1503  yield=77.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #33)

```
C=Cc1cc(C)ccc1C.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(c1cc(C)ccc1C)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.1%) | `platinum` (3.8%) | `ABSENT` (1.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (90.4%) | `reticulated_vitreous_carbon` (4.4%) | `ABSENT` (2.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `ABSENT` (0.5%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.8%) | `platinum_plate` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (89.1%) | `divided` (8.1%) | `ABSENT` (2.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (89.7%) | `ABSENT` (9.5%) | `Na` (0.4%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (50.1%) | `ABSENT` (32.0%) | `Cl` (9.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.8%) | `as_solvent_polar_protic_alcoho` (6.7%) | `as_solvent_cyclic_ether` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (74.1%) | `Co_complex` (16.8%) | `ABSENT` (2.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (54.1%) | `polar_protic_alcohol` (41.7%) | `tfe` (1.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (99%) | `ClCCl` (0%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Fe]` | `__ABSENT__` (7%) | `c1ccc2c(c1)-c1nc3c` (1%) | `[O]=[Fe][O][Fe]=[O` (1%) | set ✗ / any ✗ |

---

### Reaction #1504  yield=74.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #34)

```
C=Cc1cccc(C)c1.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(c1cccc(C)c1)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (90.5%) | `graphite_generic` (4.0%) | `reticulated_vitreous_carbon` (2.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.5%) | `stainless_steel` (0.6%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (98.5%) | `platinum_plate` (1.1%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (93.8%) | `divided` (5.5%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.8%) | `Na` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (80.4%) | `PF6` (11.4%) | `Br` (2.9%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (12.0%) | `ABSENT` (10.1%) | `as_solvent_cyclic_ether` (3.6%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (60.6%) | `ABSENT` (22.9%) | `Co_complex` (7.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (72.5%) | `polar_aprotic_nitrile` (23.5%) | `cyclic_ether` (1.5%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (89%) | `CO` (1%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (96%) | `C[Si](C)(C)N=[N+]=` (2%) | `CO` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Fe]` | `c1ccc2c(c1)-c1nc3c` (4%) | `__ABSENT__` (3%) | `__OTHER__` (1%) | set ✗ / any ✗ |

---

### Reaction #1505  yield=74.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #35)

```
COC(=O)NN.Cn1c(=O)cnc2ccccc21.C=CCCC(=O)OCC(C)(C)Cc1cccc(C)c1>>COC(=O)CC(CCC(=O)OCC(C)(C)Cc1cccc(C)c1)c1nc2ccccc2n(C)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (99.9%) | `reticulated_vitreous_carbon` (0.1%) | `graphite_generic` (0.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.6%) | `nickel` (1.1%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.4%) | `platinum_plate` (0.5%) | `platinum_wire` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (92.2%) | `ABSENT` (7.6%) | `Na` (0.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (87.5%) | `ABSENT` (12.4%) | `I` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.8%) | `as_solvent_polar_protic_alcoho` (10.0%) | `azide_source` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (83.1%) | `Co_complex` (9.7%) | `ABSENT` (4.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (84.4%) | `polar_aprotic_nitrile` (12.6%) | `ABSENT` (1.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (69%) | `COCCOC` (5%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCOC(C)=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Fe]` | `__ABSENT__` (5%) | `c1ccc2c(c1)-c1nc3c` (4%) | `[Fe+2].c1ccc2c(c1)` (1%) | set ✗ / any ✗ |

---

### Reaction #1506  yield=77.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #36)

```
C=CCCCC.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>CCCCC(CC(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.5%) | `ABSENT` (4.9%) | `platinum` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (91.8%) | `reticulated_vitreous_carbon` (5.9%) | `ABSENT` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (81.4%) | `ABSENT` (16.4%) | `sacrificial_iron` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.2%) | `ABSENT` (0.6%) | `platinum_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (88.4%) | `ABSENT` (10.8%) | `divided` (0.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.8%) | `Na` (9.7%) | `ABSENT` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (72.1%) | `ABSENT` (10.5%) | `I` (9.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.1%) | `as_solvent_polar_protic_alcoho` (8.9%) | `azide_source` (4.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (68.4%) | `ABSENT` (19.1%) | `Co_complex` (4.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (90.0%) | `polar_aprotic_nitrile` (8.0%) | `halogenated_aliphatic` (1.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (97%) | `CO` (9%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (14%) | `c1ccc2c(c1)-c1nc3c` (5%) | `__OTHER__` (5%) | set ✗ / any ✗ |

---

### Reaction #1507  yield=72.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #37)

```
C=CCCC.COC(=O)NN.Cn1c(=O)cnc2cc(Cl)ccc21>>CCCC(CC(=O)OC)c1nc2cc(Cl)ccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (62.0%) | `ABSENT` (37.7%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (88.5%) | `ABSENT` (10.8%) | `carbon_generic` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (70.5%) | `ABSENT` (28.8%) | `sacrificial_iron` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (95.6%) | `ABSENT` (4.3%) | `platinum_wire` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (96.5%) | `undivided` (2.2%) | `divided` (1.3%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (53.1%) | `NBu4` (40.7%) | `Na` (5.7%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (57.3%) | `BF4` (39.6%) | `Cl` (1.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (14.4%) | `ABSENT` (12.1%) | `tetraaryl_borate` (2.8%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (92.9%) | `ABSENT` (2.6%) | `Co_complex` (1.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (96.0%) | `polar_aprotic_nitrile` (3.1%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (55%) | `CO` (8%) | `CCO` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (96%) | `C[Si](C)(C)N=[N+]=` (1%) | `O=C(O)C(F)(F)F` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (7%) | `__OTHER__` (7%) | `__ABSENT__` (2%) | set ✗ / any ✗ |

---

### Reaction #1508  yield=71.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #38)

```
C=Cc1ccccc1F.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(c1ccccc1F)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.4%) | `ABSENT` (4.8%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (96.0%) | `ABSENT` (2.0%) | `graphite_generic` (1.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `ABSENT` (5.0%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (98.9%) | `ABSENT` (1.0%) | `platinum_foil` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.3%) | `divided` (1.8%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.9%) | `ABSENT` (0.1%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (91.4%) | `PF6` (2.5%) | `Br` (2.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.3%) | `azide_source` (5.4%) | `as_solvent_polar_protic_alcoho` (4.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (77.2%) | `ABSENT` (7.9%) | `Pt_complex` (5.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (84.7%) | `polar_aprotic_nitrile` (13.8%) | `halogenated_aliphatic` (1.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (98%) | `CO` (8%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (4%) | `c1ccc2c(c1)-c1nc3c` (3%) | `__OTHER__` (3%) | set ✗ / any ✗ |

---

### Reaction #1509  yield=88.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #39)

```
C=CCCC.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>CCCC(CC(=O)OC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.1%) | `ABSENT` (7.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (96.1%) | `carbon_generic` (2.8%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.8%) | `ABSENT` (11.7%) | `sacrificial_iron` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.4%) | `ABSENT` (0.4%) | `iron_generic` (0.1%) | ✓ (T1✓) |
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

### Reaction #1510  yield=81.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #40)

```
C=Cc1cccc(OC)c1.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(c1cccc(OC)c1)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `ABSENT` (2.8%) | `sacrificial_zinc` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (78.0%) | `ABSENT` (9.7%) | `reticulated_vitreous_carbon` (7.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.9%) | `ABSENT` (7.8%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.8%) | `ABSENT` (1.7%) | `platinum_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (87.7%) | `ABSENT` (8.6%) | `divided` (3.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.7%) | `NEt4` (0.7%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (45.5%) | `BF4` (41.2%) | `Br` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.3%) | `as_solvent_polar_protic_alcoho` (7.8%) | `primary_amine` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (63.0%) | `Co_complex` (21.9%) | `ABSENT` (8.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (50.1%) | `polar_protic_alcohol` (41.7%) | `cyclic_ether` (3.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (100%) | `ClCCl` (0%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__OTHER__` (7%) | `c1ccc2c(c1)-c1nc3c` (6%) | `[Fe+2].c1ccc2c(c1)` (2%) | set ✗ / any ✗ |

---

### Reaction #1511  yield=88.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #41)

```
C=CCCC.COC(=O)NN.O=c1cnc2ccccc2n1Cc1ccc(F)cc1>>CCCC(CC(=O)OC)c1nc2ccccc2n(Cc2ccc(F)cc2)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.6%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (65.8%) | `carbon_generic` (31.0%) | `graphite_generic` (2.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.1%) | `ABSENT` (3.6%) | `sacrificial_iron` (3.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.6%) | `iron_generic` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (67.2%) | `undivided` (32.7%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (46.1%) | `NBu4` (33.2%) | `ABSENT` (19.7%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (41.7%) | `I` (27.0%) | `BF4` (14.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.4%) | `as_solvent_polar_protic_alcoho` (9.9%) | `metal_oxide_oxidant` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (94.8%) | `Co_complex` (1.2%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (91.2%) | `polar_aprotic_nitrile` (7.8%) | `cyclic_ether` (0.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (77%) | `CO` (2%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__OTHER__` (6%) | `[Fe+2].c1ccc2c(c1)` (4%) | `c1ccc2c(c1)-c1nc3c` (1%) | set ✗ / any ✗ |

---

### Reaction #1512  yield=84.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #42)

```
C=Cc1ccc(OC)cc1.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(c1ccc(OC)cc1)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `ABSENT` (0.6%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (99.3%) | `carbon_generic` (0.2%) | `graphite_generic` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.9%) | `ABSENT` (1.3%) | `sacrificial_iron` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_plate` (0.3%) | `platinum_foil` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (50.1%) | `ABSENT` (47.0%) | `divided` (2.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.5%) | `Na` (3.4%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (62.9%) | `Br` (10.7%) | `ABSENT` (7.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (11.5%) | `ABSENT` (8.9%) | `azide_source` (2.8%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (50.6%) | `Co_complex` (31.8%) | `ABSENT` (4.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (50.2%) | `polar_protic_alcohol` (46.8%) | `cyclic_ether` (1.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (100%) | `O` (1%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CO` (53%) | `__ABSENT__` (37%) | `C[Si](C)(C)N=[N+]=` (4%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (4%) | `c1ccc2c(c1)-c1nc3c` (3%) | `O.[Br][Mn][Br]` (2%) | set ✗ / any ✗ |

---

### Reaction #1513  yield=84.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #43)

```
C=CCCC.COC(=O)NN.CCCCn1c(=O)cnc2ccccc21>>CCCCn1c(=O)c(C(CCC)CC(=O)OC)nc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `ABSENT` (2.2%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (67.0%) | `carbon_felt` (31.9%) | `graphite_generic` (0.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.4%) | `ABSENT` (2.2%) | `sacrificial_iron` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.9%) | `iron_generic` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (94.1%) | `undivided` (5.9%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (50.2%) | `ABSENT` (28.2%) | `Na` (20.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (58.8%) | `BF4` (19.3%) | `I` (10.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.8%) | `as_solvent_polar_protic_alcoho` (19.6%) | `metal_oxide_oxidant` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (87.7%) | `ABSENT` (3.4%) | `Rh_complex` (1.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (89.1%) | `polar_aprotic_nitrile` (8.5%) | `cyclic_ether` (1.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (46%) | `O` (14%) | `CO` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__OTHER__` (5%) | `[Fe+2].c1ccc2c(c1)` (3%) | `[cH]12->[Fe+2]3456` (1%) | set ✗ / any ✗ |

---

### Reaction #1514  yield=87.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #44)

```
C=Cc1ccccc1.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(c1ccccc1)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (60.8%) | `ABSENT` (36.8%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (76.6%) | `ABSENT` (20.2%) | `carbon_generic` (2.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `ABSENT` (58.5%) | `platinum` (37.6%) | `nickel` (2.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (77.1%) | `ABSENT` (21.5%) | `nickel_generic` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (83.2%) | `undivided` (13.5%) | `divided` (3.3%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.1%) | `ABSENT` (2.3%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (76.3%) | `ABSENT` (7.0%) | `Br` (7.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (32.7%) | `azide_source` (4.2%) | `ABSENT` (3.8%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (73.8%) | `Co_complex` (8.6%) | `ABSENT` (6.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (75.4%) | `polar_aprotic_nitrile` (19.0%) | `cyclic_ether` (1.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (89%) | `CO` (26%) | `CCO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CO` (74%) | `__ABSENT__` (13%) | `C[Si](C)(C)N=[N+]=` (10%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `O.[Br][Mn][Br]` (24%) | `c1ccc2c(c1)-c1nc3c` (24%) | `[Fe+2].c1ccc2c(c1)` (21%) | set ✗ / any ✗ |

---

### Reaction #1515  yield=87.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #45)

```
C=CCCC.COC(=O)NN.Cn1c(=O)cnc2cc(Cl)c(Cl)cc21>>CCCC(CC(=O)OC)c1nc2cc(Cl)c(Cl)cc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `ABSENT` (1.4%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (99.8%) | `carbon_generic` (0.1%) | `ABSENT` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.5%) | `ABSENT` (2.0%) | `sacrificial_iron` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.8%) | `ABSENT` (0.1%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (70.9%) | `undivided` (28.3%) | `divided` (0.8%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.3%) | `ABSENT` (14.2%) | `Na` (4.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (89.0%) | `ABSENT` (9.9%) | `Cl` (0.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.0%) | `as_solvent_polar_protic_alcoho` (11.3%) | `azide_source` (4.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (97.7%) | `ferrocene_mediator` (0.8%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (98.6%) | `polar_aprotic_nitrile` (1.0%) | `halogenated_aliphatic` (0.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (42%) | `CO` (11%) | `COCCOC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (22%) | `__OTHER__` (9%) | `c1ccc2c(c1)-c1nc3c` (6%) | set ✗ / any ✗ |

---

### Reaction #1516  yield=83.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #46)

```
C=Cc1ccc(C(C)(C)C)cc1.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(c1ccc(C(C)(C)C)cc1)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `ABSENT` (1.0%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_felt` (99.0%) | `carbon_generic` (0.7%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.4%) | `ABSENT` (8.5%) | `sacrificial_iron` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.7%) | `ABSENT` (0.4%) | `platinum_plate` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (91.4%) | `ABSENT` (8.5%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.1%) | `Na` (0.4%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (81.7%) | `PF6` (8.0%) | `I` (3.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (48.3%) | `ABSENT` (4.9%) | `azide_source` (2.4%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (39.5%) | `Co_complex` (21.3%) | `Mn_complex` (18.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (52.7%) | `polar_aprotic_nitrile` (44.4%) | `polar_aprotic_amide` (1.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (100%) | `CO` (12%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CO` (91%) | `__ABSENT__` (8%) | `C[Si](C)(C)N=[N+]=` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__OTHER__` (25%) | `O.[Br][Mn][Br]` (12%) | `[Fe+2].c1ccc2c(c1)` (6%) | set ✗ / any ✗ |

---

### Reaction #1517  yield=86.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #47)

```
C=CCc1ccccc1.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(Cc1ccccc1)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `ABSENT` (1.0%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (98.1%) | `graphite_generic` (0.8%) | `reticulated_vitreous_carbon` (0.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.9%) | `ABSENT` (5.8%) | `nickel` (4.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.4%) | `iron_generic` (0.7%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (71.5%) | `ABSENT` (21.5%) | `Na` (6.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (60.6%) | `ABSENT` (36.7%) | `Br` (1.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (9.0%) | `ABSENT` (7.7%) | `azide_source` (3.8%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (95.8%) | `Co_complex` (2.2%) | `ferrocene_mediator` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (98.6%) | `polar_aprotic_nitrile` (1.1%) | `ABSENT` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CO` (52%) | `CC#N` (45%) | `C1CCOC1` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (80%) | `C[Si](C)(C)N=[N+]=` (13%) | `CO` (2%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (13%) | `O.[Br][Mn][Br]` (9%) | `c1ccc2c(c1)-c1nc3c` (8%) | set ✗ / any ✗ |

---

### Reaction #1518  yield=86.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #48)

```
C=CCCC.COC(=O)NN.CCn1c(=O)cnc2ccccc21>>CCCC(CC(=O)OC)c1nc2ccccc2n(CC)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (91.2%) | `ABSENT` (8.4%) | `platinum` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (70.7%) | `carbon_generic` (24.6%) | `ABSENT` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (91.8%) | `ABSENT` (6.8%) | `sacrificial_iron` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.9%) | `ABSENT` (0.1%) | `iron_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (79.5%) | `undivided` (20.2%) | `divided` (0.3%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (87.2%) | `Na` (9.3%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (80.3%) | `I` (8.1%) | `ABSENT` (4.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (25.8%) | `as_solvent_polar_protic_alcoho` (13.6%) | `metal_oxide_oxidant` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (82.6%) | `Co_complex` (4.6%) | `ABSENT` (3.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (96.8%) | `polar_aprotic_nitrile` (2.4%) | `halogenated_aliphatic` (0.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (70%) | `CO` (21%) | `O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CO` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (7%) | `__OTHER__` (3%) | `c1ccc2c(c1)-c1nc3c` (1%) | set ✗ / any ✗ |

---

### Reaction #1519  yield=86.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #49)

```
C=Cc1ccc(F)cc1.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(c1ccc(F)cc1)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `ABSENT` (0.8%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (98.2%) | `carbon_generic` (0.5%) | `graphite_generic` (0.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.0%) | `ABSENT` (3.4%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.0%) | `ABSENT` (0.7%) | `platinum_plate` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (78.1%) | `ABSENT` (21.0%) | `divided` (0.8%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (89.4%) | `ABSENT` (10.2%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (61.6%) | `ABSENT` (33.0%) | `Cl` (1.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (10.8%) | `ABSENT` (9.4%) | `azide_source` (4.2%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (72.4%) | `ABSENT` (7.3%) | `Co_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (74.7%) | `polar_aprotic_nitrile` (22.0%) | `halogenated_aliphatic` (2.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (98%) | `CO` (12%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (73%) | `C[Si](C)(C)N=[N+]=` (15%) | `CO` (8%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (8%) | `__OTHER__` (6%) | `O.[Br][Mn][Br]` (1%) | set ✗ / any ✗ |

---

### Reaction #1520  yield=82.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #50)

```
C=CCCC.COC(=O)NN.O=C(Cn1c(=O)cnc2ccccc21)c1ccccc1>>CCCC(CC(=O)OC)c1nc2ccccc2n(CC(=O)c2ccccc2)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.1%) | `ABSENT` (5.3%) | `platinum` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (58.4%) | `carbon_generic` (37.6%) | `ABSENT` (1.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.6%) | `ABSENT` (4.4%) | `sacrificial_iron` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.5%) | `ABSENT` (0.2%) | `iron_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (97.2%) | `undivided` (2.6%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (57.2%) | `ABSENT` (32.1%) | `Na` (10.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (55.1%) | `BF4` (32.3%) | `I` (6.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.8%) | `as_solvent_polar_protic_alcoho` (10.9%) | `metal_oxide_oxidant` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (86.0%) | `ABSENT` (6.5%) | `Mn_complex` (1.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (92.1%) | `polar_aprotic_nitrile` (5.0%) | `cyclic_ether` (1.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (41%) | `CO` (7%) | `O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (3%) | `__OTHER__` (1%) | `c1ccc2c(c1)-c1nc3c` (1%) | set ✗ / any ✗ |

---

### Reaction #1521  yield=85.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #51)

```
C=Cc1ccc(C)cc1.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(c1ccc(C)cc1)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `ABSENT` (0.7%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (99.3%) | `ABSENT` (0.2%) | `reticulated_vitreous_carbon` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `ABSENT` (2.7%) | `nickel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (93.3%) | `platinum_plate` (4.2%) | `ABSENT` (1.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (71.5%) | `ABSENT` (21.3%) | `divided` (7.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.4%) | `ABSENT` (7.2%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (81.9%) | `ABSENT` (12.7%) | `Br` (2.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (15.5%) | `ABSENT` (6.3%) | `azide_source` (6.2%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (73.6%) | `ABSENT` (10.5%) | `Co_complex` (5.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (71.9%) | `polar_aprotic_nitrile` (25.2%) | `ABSENT` (0.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (99%) | `CO` (19%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (66%) | `C[Si](C)(C)N=[N+]=` (20%) | `CO` (10%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `[Fe+2].c1ccc2c(c1)` (18%) | `c1ccc2c(c1)-c1nc3c` (6%) | `__OTHER__` (5%) | set ✗ / any ✗ |

---

### Reaction #1522  yield=82.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #52)

```
C=CCCC.COC(=O)NN.O=c1cnc2ccccc2n1Cc1ccc(Cl)cc1>>CCCC(CC(=O)OC)c1nc2ccccc2n(Cc2ccc(Cl)cc2)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.3%) | `ABSENT` (2.6%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (76.3%) | `carbon_generic` (21.7%) | `graphite_generic` (1.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.6%) | `ABSENT` (2.0%) | `sacrificial_iron` (1.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.7%) | `iron_generic` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (81.4%) | `undivided` (18.0%) | `divided` (0.7%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (71.9%) | `NBu4` (14.1%) | `ABSENT` (13.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (52.3%) | `I` (18.4%) | `Cl` (14.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (26.9%) | `as_solvent_polar_protic_alcoho` (8.4%) | `metal_oxide_oxidant` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (96.2%) | `ABSENT` (0.9%) | `Co_complex` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (92.3%) | `polar_aprotic_nitrile` (6.3%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (69%) | `CO` (5%) | `O` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__OTHER__` (38%) | `[Fe+2].c1ccc2c(c1)` (6%) | `[cH]12->[Fe+2]3456` (1%) | set ✗ / any ✗ |

---

### Reaction #1523  yield=81.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #53)

```
C=Cc1ccc(C(F)(F)F)cc1.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(c1ccc(C(F)(F)F)cc1)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (50.8%) | `ABSENT` (48.0%) | `sacrificial_iron` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (48.3%) | `ABSENT` (47.2%) | `unknown_electrode` (2.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `ABSENT` (73.7%) | `platinum` (23.2%) | `nickel` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `ABSENT` (60.6%) | `platinum_generic` (37.4%) | `nickel_foam` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (68.7%) | `undivided` (28.1%) | `divided` (3.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.7%) | `Na` (0.1%) | `ABSENT` (0.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (83.7%) | `PF6` (7.0%) | `Br` (4.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (8.7%) | `ABSENT` (8.5%) | `azide_source` (3.1%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (51.1%) | `Co_complex` (30.7%) | `ABSENT` (7.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (84.8%) | `polar_aprotic_nitrile` (10.9%) | `halogenated_aliphatic` (1.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (97%) | `CO` (2%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (51%) | `CO` (28%) | `C[Si](C)(C)N=[N+]=` (14%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Fe]` | `__OTHER__` (19%) | `O.[Br][Mn][Br]` (12%) | `[Fe+2][N-]C1=Nc2nc` (2%) | set ✗ / any ✗ |

---

### Reaction #1524  yield=81.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #54)

```
C=CCCC.CCOC(=O)NN.Cn1c(=O)cnc2ccccc21>>CCCC(CC(=O)OCC)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `ABSENT` (0.9%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (71.9%) | `carbon_generic` (21.0%) | `ABSENT` (2.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.0%) | `nickel` (3.1%) | `ABSENT` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.0%) | `nickel_foam` (2.0%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (93.8%) | `undivided` (4.7%) | `divided` (1.5%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (49.5%) | `NBu4` (37.1%) | `Na` (13.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (62.4%) | `BF4` (25.2%) | `I` (7.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.5%) | `as_solvent_polar_protic_alcoho` (6.4%) | `amide` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (38.5%) | `Co_complex` (20.6%) | `ferrocene_mediator` (16.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (86.8%) | `polar_aprotic_nitrile` (6.1%) | `halogenated_aliphatic` (2.8%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CO` (18%) | `CC#N` (2%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Fe]` | `__ABSENT__` (2%) | `__OTHER__` (2%) | `CC(=O)[CH-]C(C)=O.` (1%) | set ✗ / any ✗ |

---

### Reaction #1525  yield=85.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_35_10656-10663.json) (反应 idx 在该 JSON 内 = #55)

```
C=Cc1cccc(F)c1.COC(=O)NN.Cn1c(=O)cnc2ccccc21>>COC(=O)CC(c1cccc(F)c1)c1nc2ccccc2n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.4%) | `ABSENT` (18.0%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (47.2%) | `ABSENT` (46.5%) | `reticulated_vitreous_carbon` (4.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.6%) | `ABSENT` (14.3%) | `nickel` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (85.0%) | `ABSENT` (14.1%) | `nickel_generic` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (59.6%) | `divided` (26.3%) | `ABSENT` (14.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.5%) | `ABSENT` (0.3%) | `NEt4` (0.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (57.6%) | `PF6` (25.8%) | `I` (5.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_polar_protic_alcoho` (12.3%) | `ABSENT` (8.1%) | `as_solvent_cyclic_ether` (2.9%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Fe_complex` (74.6%) | `ABSENT` (8.5%) | `Co_complex` (6.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (73.5%) | `polar_aprotic_nitrile` (17.5%) | `tfe` (2.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `CC#N` | `CC#N` (24%) | `CN(C)C=O` (7%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `CO` (1%) | `C[Si](C)(C)N=[N+]=` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Fe]` | `__OTHER__` (22%) | `c1ccc2c(c1)-c1nc3c` (4%) | `[O]=[Fe][O][Fe]=[O` (4%) | set ✗ / any ✗ |

---

### Reaction #1526  yield=34.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json) (反应 idx 在该 JSON 内 = #0)

```
N=C(c1ccccc1)c1ccccc1.C=Cc1ccc(C(C)(C)C)cc1.O=S(O)C(F)(F)F.[Na]>>CC(C)(C)c1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `platinum` (1.7%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_generic` (43.8%) | `graphite_felt` (13.0%) | `carbon_felt` (9.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.5%) | `nickel` (3.1%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (97.3%) | `platinum_generic` (2.5%) | `stainless_steel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (43.7%) | `NBu4` (29.2%) | `NEt4` (16.9%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (43.6%) | `ClO4` (19.5%) | `PF6` (17.4%) | ✓ |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (22.0%) | `water` (2.9%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `Mn_complex` (0.5%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `halogenated_aliphatic` (11.4%) | `polar_aprotic_amide` (1.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (54%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `OC(C(F)(F)F)C(F)(F` + `C1CN=C2NCCCN2C1` | `__ABSENT__` (100%) | `O=O` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #1527  yield=45.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json) (反应 idx 在该 JSON 内 = #1)

```
N=C(c1ccccc1)c1ccccc1.O=S(O)C(F)(F)F.[Na].C=Cc1ccc(Oc2ccccc2)cc1>>FC(F)(F)CC(N=C(c1ccccc1)c1ccccc1)c1ccc(Oc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (1.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_generic` (89.9%) | `graphite_felt` (3.9%) | `graphite_plate` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.9%) | `nickel` (5.0%) | `stainless_steel` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.3%) | `platinum_generic` (1.2%) | `nickel_plate` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (46.0%) | `NBu4` (38.6%) | `NEt4` (9.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (37.0%) | `PF6` (36.9%) | `ClO4` (13.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (19.2%) | `water` (3.3%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `Mn_complex` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.3%) | `halogenated_aliphatic` (30.4%) | `polar_protic_acid` (3.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (96%) | `O` (13%) | `FC(F)(F)c1ccccc1` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `OC(C(F)(F)F)C(F)(F` + `C1CN=C2NCCCN2C1` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `O=C([O-])c1ccccc1-` (0%) | set ✓ / any ✓ |

---

### Reaction #1528  yield=45.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C)cc1.N=C(c1ccccc1)c1ccccc1.O=S(O)C(F)(F)F.[Na]>>Cc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_generic` (35.5%) | `carbon_generic` (19.5%) | `graphite_felt` (17.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.1%) | `nickel` (3.3%) | `carbon` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (92.4%) | `platinum_generic` (4.9%) | `nickel_plate` (1.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (26.3%) | `Li` (22.4%) | `ABSENT` (22.2%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (26.2%) | `BF4` (23.0%) | `ABSENT` (21.2%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (18.5%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Mn_complex` (0.1%) | `ionic_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.8%) | `halogenated_aliphatic` (1.9%) | `aqueous` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (99%) | `CC(=O)O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `OC(C(F)(F)F)C(F)(F` + `C1CN=C2NCCCN2C1` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1529  yield=47.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1ccc(OC)cc1.O=S(O)C(F)(F)F.[Na].COc1ccc(C(=N)c2ccc(OC)cc2)cc1>>COc1ccc(C(=NC(CC(F)(F)F)c2ccc(OC)cc2)c2ccc(OC)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_rod` (33.8%) | `carbon_generic` (22.0%) | `graphite_generic` (14.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.2%) | `nickel` (6.3%) | `stainless_steel` (3.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.7%) | `nickel_plate` (0.5%) | `stainless_steel_generic` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.4%) | `ABSENT` (9.5%) | `Li` (4.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (47.3%) | `PF6` (20.2%) | `ClO4` (12.9%) | ✓ |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (10.9%) | `water` (5.1%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.1%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (80.1%) | `halogenated_aliphatic` (14.2%) | `polar_aprotic_sulfoxide` (1.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (70%) | `FC(F)(F)c1ccccc1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `OC(C(F)(F)F)C(F)(F` + `C1CN=C2NCCCN2C1` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #1530  yield=41.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json) (反应 idx 在该 JSON 内 = #4)

```
C=Cc1ccccc1OC.N=C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>COc1ccccc1C(CC(F)(F)F)N=C(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.9%) | `platinum` (11.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_felt` (18.1%) | `carbon_generic` (16.1%) | `graphite_generic` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.5%) | `nickel` (12.0%) | `carbon` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (70.4%) | `platinum_generic` (27.0%) | `nickel_plate` (1.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (69.1%) | `Li` (15.5%) | `ABSENT` (9.0%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (48.3%) | `PF6` (22.5%) | `BF4` (15.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (33.8%) | `metal_oxide_oxidant` (1.8%) | `tellurium_reagent` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (62.8%) | `halogenated_aliphatic` (17.8%) | `ketone` (12.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (93%) | `CC(=O)O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `OC(C(F)(F)F)C(F)(F` + `C1CN=C2NCCCN2C1` | `__ABSENT__` (100%) | `O` (0%) | `[Cl-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1531  yield=60.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json) (反应 idx 在该 JSON 内 = #5)

```
N=C(c1ccccc1)c1ccccc1.O=S(O)C(F)(F)F.[Na].C=Cc1ccc(OC)c(OCc2ccccc2)c1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_plate` (53.5%) | `graphite_felt` (21.7%) | `graphite_generic` (10.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.0%) | `nickel` (0.9%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (88.4%) | `platinum_generic` (11.2%) | `nickel_plate` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (44.9%) | `NBu4` (44.9%) | `Na` (6.2%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (44.7%) | `PF6` (19.5%) | `molecular_no_ion` (17.5%) | ✓ |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (33.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (88.9%) | `halogenated_aliphatic` (7.0%) | `polar_aprotic_amide` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (97%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `OC(C(F)(F)F)C(F)(F` + `C1CN=C2NCCCN2C1` | `__ABSENT__` (100%) | `[Br-].[Na+]` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |

---

### Reaction #1532  yield=58.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json) (反应 idx 在该 JSON 内 = #6)

```
N=C(c1ccccc1)c1ccccc1.O=S(O)C(F)(F)F.[Na].C=Cc1ccc2c(c1)CCO2>>FC(F)(F)CC(N=C(c1ccccc1)c1ccccc1)c1ccc2c(c1)CCO2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_rod` (26.8%) | `carbon_generic` (25.7%) | `graphite_generic` (25.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.3%) | `nickel` (1.1%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (77.6%) | `platinum_generic` (22.2%) | `nickel_plate` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (51.6%) | `NBu4` (41.4%) | `Li` (4.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (47.3%) | `BF4` (28.4%) | `ClO4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (29.4%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (88.0%) | `halogenated_aliphatic` (10.2%) | `aqueous` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (86%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `OC(C(F)(F)F)C(F)(F` + `C1CN=C2NCCCN2C1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1533  yield=57.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json) (反应 idx 在该 JSON 内 = #7)

```
N=C(c1ccccc1)c1ccccc1.O=S(O)C(F)(F)F.[Na].C=Cc1ccc(OC)c(OC)c1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `sacrificial_aluminum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_plate` (35.3%) | `graphite_generic` (27.7%) | `graphite_felt` (12.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.4%) | `nickel` (1.3%) | `carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.8%) | `platinum_generic` (1.0%) | `nickel_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (56.7%) | `ABSENT` (30.5%) | `Li` (5.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (31.4%) | `ABSENT` (30.6%) | `ClO4` (12.1%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Mn_complex` (0.2%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (85.8%) | `halogenated_aliphatic` (9.6%) | `aqueous` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (96%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `OC(C(F)(F)F)C(F)(F` + `C1CN=C2NCCCN2C1` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |

---

### Reaction #1534  yield=53.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json) (反应 idx 在该 JSON 内 = #8)

```
N=C(c1ccccc1)c1ccccc1.O=S(O)C(F)(F)F.[Na].C=Cc1ccc(OCc2ccccc2)cc1>>FC(F)(F)CC(N=C(c1ccccc1)c1ccccc1)c1ccc(OCc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_generic` (39.6%) | `graphite_felt` (18.1%) | `graphite_plate` (15.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.1%) | `nickel` (3.4%) | `carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.5%) | `platinum_generic` (2.7%) | `nickel_plate` (0.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (42.9%) | `NBu4` (41.8%) | `NEt4` (6.4%) | ✓ |
| 电解质 anion | 26 | `PF6` | `PF6` (63.5%) | `ABSENT` (21.9%) | `ClO4` (7.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (21.0%) | `bromide_anion` (2.8%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `Mn_complex` (0.2%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.5%) | `halogenated_aliphatic` (10.1%) | `polar_protic_acid` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (74%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `OC(C(F)(F)F)C(F)(F` + `C1CN=C2NCCCN2C1` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])c1ccccc1-` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #1535  yield=61.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json) (反应 idx 在该 JSON 内 = #9)

```
C=Cc1ccc(OC)cc1.O=S(O)C(F)(F)F.[Na].N=S(=O)(c1ccccc1)c1ccccc1>>COc1ccc(C(CC(F)(F)F)N=S(=O)(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_rod` (86.6%) | `graphite_generic` (8.5%) | `carbon_felt` (1.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.9%) | `carbon` (10.1%) | `stainless_steel` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.8%) | `stainless_steel_generic` (0.0%) | `platinum_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (86.0%) | `Li` (6.6%) | `NBu4` (5.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (75.4%) | `PF6` (15.8%) | `BF4` (4.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `alkali_phosphate` (4.0%) | `alkali_carboxylate` (3.4%) | `pyridine` (3.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `pyridine_organocat` (0.3%) | `brønsted_acid_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (77.2%) | `ketone` (8.9%) | `halogenated_aliphatic` (8.5%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (92%) | `O` (31%) | `CC(C)=O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `OC(C(F)(F)F)C(F)(F` + `C1CN=C2NCCCN2C1` | `CC(=O)[O-].[Na+]` (45%) | `__ABSENT__` (3%) | `O=P([O-])([O-])[O-` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #1536  yield=65.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json) (反应 idx 在该 JSON 内 = #10)

```
N=C(c1ccccc1)c1ccccc1.O=S(O)C(F)(F)F.[Na].C=Cc1ccc(OC)cc1OC>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)c(OC)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_generic` (35.3%) | `carbon_generic` (25.9%) | `graphite_felt` (17.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.9%) | `nickel` (1.3%) | `carbon` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (82.5%) | `platinum_generic` (17.2%) | `graphite_generic` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (60.1%) | `Li` (13.5%) | `ABSENT` (12.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (56.2%) | `PF6` (19.4%) | `ABSENT` (10.9%) | ✓ |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (18.2%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (65.5%) | `halogenated_aliphatic` (28.0%) | `aqueous` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `O` (100%) | `CC#N` (78%) | `FC(F)(F)c1ccccc1` (21%) | set ✗ / any ✓ |
| 试剂 set | 545 | `OC(C(F)(F)F)C(F)(F` + `C1CN=C2NCCCN2C1` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Cl-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1537  yield=68.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json) (反应 idx 在该 JSON 内 = #11)

```
N=C(c1ccccc1)c1ccccc1.C=Cc1ccc(OCC)cc1>>CCOc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.6%) | `sacrificial_aluminum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `carbon_generic` (79.9%) | `graphite_felt` (7.0%) | `graphite_generic` (5.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `nickel` (3.3%) | `sacrificial_zinc` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (72.0%) | `platinum_generic` (26.9%) | `zinc_generic` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (86.1%) | `NBu4` (7.5%) | `NEt4` (3.9%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `ClO4` (83.7%) | `molecular_no_ion` (8.8%) | `BF4` (3.2%) | ✓ |
| 试剂大类 | 103 | `cf3_source` | `alkali_sulfinate` (16.0%) | `alkali_sulfonate` (11.3%) | `ABSENT` (3.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `Mn_complex` (1.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (90.5%) | `polar_protic_acid` (5.5%) | `polar_aprotic_sulfoxide` (1.4%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `O` (100%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `OC(C(F)(F)F)C(F)(F` + `CCCC[N+](CCCC)(CCC` + `C1CN=C2NCCCN2C1` | `O=S([O-])C(F)(F)F.` (39%) | `__ABSENT__` (14%) | `O=S([O-])O.[Na+]` (14%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Cl][Mn][Cl]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1538  yield=67.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json) (反应 idx 在该 JSON 内 = #12)

```
N=C(c1ccccc1)c1ccccc1.O=S(O)C(F)(F)F.[Na].C=Cc1cc(OC)c(OC)c(OC)c1>>COc1cc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc(OC)c1OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_felt` (37.3%) | `graphite_generic` (29.4%) | `platinum_plate` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.2%) | `nickel` (0.7%) | `sacrificial_zinc` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.7%) | `platinum_generic` (0.2%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (77.1%) | `NEt4` (8.1%) | `NBu4` (6.8%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (66.3%) | `ClO4` (14.5%) | `molecular_no_ion` (7.1%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (20.1%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (92.6%) | `halogenated_aliphatic` (3.9%) | `ketone` (0.9%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `O` (69%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `OC(C(F)(F)F)C(F)(F` + `C1CN=C2NCCCN2C1` | `__ABSENT__` (100%) | `O` (0%) | `[Cl-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #1539  yield=61.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_10994-10999.json) (反应 idx 在该 JSON 内 = #13)

```
N=C(c1ccccc1)c1ccccc1.O=S(O)C(F)(F)F.[Na].C=Cc1ccc(OC)c(C)c1>>COc1ccc(C(CC(F)(F)F)N=C(c2ccccc2)c2ccccc2)cc1C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `platinum` (2.8%) | `sacrificial_aluminum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_felt` (15.5%) | `carbon_plate` (15.3%) | `graphite_plate` (14.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.2%) | `nickel` (1.7%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.7%) | `platinum_generic` (1.2%) | `nickel_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (86.4%) | `ABSENT` (5.7%) | `Li` (2.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (38.8%) | `PF6` (31.5%) | `BF4` (6.7%) | ✓ |
| 试剂大类 | 103 | `cf3_source` | `ABSENT` (24.5%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Mn_complex` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (66.3%) | `halogenated_aliphatic` (26.7%) | `polar_aprotic_amide` (2.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (97%) | `ClCCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `OC(C(F)(F)F)C(F)(F` + `C1CN=C2NCCCN2C1` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Cl-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |

---

### Reaction #1540  yield=69.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_11000-11006.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_11000-11006.json) (反应 idx 在该 JSON 内 = #0)

```
C=C/C=C/c1ccc(-c2ccccc2)cc1.C=C/C=C\c1ccc(-c2ccccc2)cc1>>COC/C=C/C(OC)c1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (98.5%) | `platinum` (1.4%) | `sacrificial_iron` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `reticulated_vitreous_carbon` (44.2%) | `graphite_generic` (25.0%) | `carbon_felt` (18.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.9%) | `stainless_steel` (0.1%) | `nickel` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `graphite_plate` | `platinum_plate` (71.6%) | `platinum_generic` (28.3%) | `stainless_steel_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (89.3%) | `ABSENT` (10.2%) | `divided` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.1%) | `Li` (10.4%) | `Na` (2.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (35.4%) | `ClO4` (22.2%) | `I` (19.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `boron_lewis_acid` (6.3%) | `as_solvent_halogenated_aliphat` (5.5%) | `ABSENT` (5.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (63.6%) | `Mn_complex` (16.8%) | `Cu_complex` (7.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `halogenated_aliphatic` (45.5%) | `polar_protic_acid` (11.0%) | `polar_aprotic_amide` (10.1%) | ✗ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` | `O` (98%) | `CN(C)C=O` (19%) | `CC#N` (15%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `CC[Si](CC)CC` (87%) | `OB(O)B(O)O` (80%) | `__OTHER__` (73%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `COCCOC.[Br][Ni][Br` (14%) | `__ABSENT__` (2%) | `[Pt]` (1%) | set ✗ / any ✓ |

---

### Reaction #1541  yield=61.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_36_11000-11006.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_36_11000-11006.json) (反应 idx 在该 JSON 内 = #1)

```
C=C/C=C/c1ccc2ccccc2c1.C=C/C=C\c1ccc2ccccc2c1>>COC/C=C/C(OC)c1ccc2ccccc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (79.6%) | `platinum` (19.6%) | `sacrificial_magnesium` (0.3%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `carbon_felt` (32.4%) | `platinum_generic` (25.7%) | `graphite_generic` (19.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.3%) | `stainless_steel` (0.6%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `graphite_plate` | `platinum_generic` (73.8%) | `platinum_plate` (25.0%) | `stainless_steel_generic` (0.7%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (69.2%) | `undivided` (30.5%) | `divided` (0.3%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Li` (48.1%) | `NBu4` (44.3%) | `Na` (3.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (53.4%) | `PF6` (28.3%) | `BF4` (7.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `transition_metal_salt_reagent` (15.3%) | `inorganic_simple` (9.1%) | `ABSENT` (7.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (57.2%) | `ABSENT` (30.2%) | `Ni_complex` (4.5%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_sulfoxide` (48.6%) | `halogenated_aliphatic` (13.0%) | `cyclic_ether` (12.0%) | ✗ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` | `[H+].[OH-]` (99%) | `CC#N` (98%) | `C1CCOC1` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC[Si](CC)CC` (100%) | `O=O` (98%) | `OB(O)B(O)O` (95%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `CC[C@H]1CN2CC[C@H]` (100%) | `O.O.[K+].[K+].[O]=` (97%) | `__OTHER__` (1%) | set ✗ / any ✗ |

---

### Reaction #1542  yield=66.0%

**Source paper**: [`China/China_CN117926288_A_2024-04-26.json`](reactions_by_journal_alkene_ec_audited/China/China_CN117926288_A_2024-04-26.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1>>c1ccc(C(CCC(c2ccccc2)c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (48.1%) | `ABSENT` (30.6%) | `platinum` (13.4%) | ✗ |
| 阳极 (细类) | 43 | `platinum_plate` | `carbon_rod` (54.8%) | `glassy_carbon` (11.0%) | `carbon_generic` (5.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (32.2%) | `ABSENT` (30.2%) | `carbon` (27.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (34.6%) | `platinum_generic` (16.2%) | `carbon_rod` (12.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (78.6%) | `ABSENT` (17.8%) | `divided` (3.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (76.6%) | `Li` (8.0%) | `NBu4` (6.7%) | ✓ |
| 电解质 anion | 26 | `Br` | `ClO4` (39.5%) | `BF4` (25.0%) | `F` (7.6%) | ✗ |
| 试剂大类 | 103 | `hcl` | `carboxylic_acid` (10.6%) | `polyhalo_radical_transfer` (8.1%) | `inorganic_simple` (6.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (87.0%) | `Mn_complex` (4.3%) | `organic_neutral_cat` (2.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (66.9%) | `polar_protic_alcohol` (18.9%) | `ABSENT` (3.1%) | ✗ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CCO` (70%) | `CC#N` (43%) | `C1COCCO1` (40%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I)cc1` + `F.c1ccncc1` + `O=C(O)O.[Na]` + `[OH][Na]` | `O=C(O)O.[Na]` (75%) | `F.c1ccncc1` (57%) | `OB(O)B(O)O` (42%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `Brc1ccc(N(c2ccc(Br` | `c1ccncc1` (58%) | `Brc1ccc(N(c2ccc(Br` (50%) | `CC(C)(C)c1cc(C=N[C` (10%) | set ✗ / any ✓ |

---

### Reaction #1543  yield=49.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)/C=C/c1ccccc1>>COC(=O)[C@H](Br)[C@@H](Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.5%) | `platinum` (6.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (92.1%) | `platinum_wire` (4.9%) | `carbon_rod` (1.3%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (90.6%) | `stainless_steel` (7.1%) | `carbon` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_felt` | `platinum_plate` (48.2%) | `platinum_foil` (38.9%) | `platinum_wire` (4.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.3%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Na` (77.7%) | `Li` (7.4%) | `ABSENT` (4.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (71.1%) | `Br` (20.0%) | `OTs` (3.7%) | ✓ |
| 试剂大类 | 103 | `ester` | `bromide_anion` (47.6%) | `ABSENT` (3.5%) | `hbr` (3.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Mn_complex` (0.2%) | `Pt_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.1%) | `polar_protic_acid` (0.3%) | `aqueous` (0.2%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (98%) | `CC(=O)O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCOC(C)=O` + `[Na+].[OH-]` | `[Na+].[OH-]` (46%) | `[Br-].[H+]` (37%) | `CCOC(C)=O` (33%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (90%) | `[Cl][Mn][Cl]` (7%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #1544  yield=60.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #1)

```
C=CCCN1C(=O)c2ccccc2C1=O>>O=C1c2ccccc2C(=O)N1CC[C@H](Cl)CCl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (1.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (53.0%) | `graphite_generic` (24.0%) | `platinum_wire` (10.7%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (85.8%) | `platinum` (12.3%) | `nickel` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_felt` | `graphite_generic` (85.3%) | `carbon_rod` (3.8%) | `platinum_wire` (3.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.2%) | `divided` (1.6%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NEt4` (69.7%) | `Li` (12.7%) | `ABSENT` (11.1%) | ✗ |
| 电解质 anion | 26 | `Cl` | `BF4` (65.4%) | `ABSENT` (18.9%) | `ClO4` (7.1%) | ✗ |
| 试剂大类 | 103 | `ester` | `polyhalo_radical_transfer` (58.0%) | `as_solvent_halogenated_aliphat` (3.6%) | `carboxylic_acid` (3.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Mn_complex` (96.6%) | `ABSENT` (2.7%) | `brønsted_acid_cat` (0.3%) | ✓ |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (51.7%) | `halogenated_aliphatic` (32.9%) | `polar_protic_acid` (7.0%) | ✗ |
| 溶剂 set | 79 | `CC(=O)O` | `O` (93%) | `CC#N` (79%) | `ClCCl` (17%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCOC(C)=O` + `[Na+].[OH-]` | `Cc1ccc(I)cc1` (37%) | `OCCBr` (36%) | `O=P([O-])([O-])[O-` (30%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl][Mn][Cl]` (91%) | `[Cl-].[Cl-].[Mn+2]` (5%) | `O=S(=O)([O-])C(F)(` (2%) | set ✗ / any ✗ |

---

### Reaction #1545  yield=52.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #2)

```
C=CCCCCCCCCOC(=O)C(C)c1ccc(CC(C)C)cc1>>CC(C)Cc1ccc(C(C)C(=O)OCCCCCCCC[C@@H](Cl)CCl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (83.8%) | `graphite_felt` (13.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (54.7%) | `carbon` (44.3%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `graphite_felt` | `graphite_generic` (60.4%) | `platinum_plate` (14.1%) | `graphite_felt` (10.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.4%) | `ABSENT` (1.4%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NEt4` (91.4%) | `Li` (5.7%) | `NBu4` (1.2%) | ✗ |
| 电解质 anion | 26 | `Cl` | `ClO4` (55.1%) | `BF4` (19.7%) | `Cl` (13.8%) | ✓ |
| 试剂大类 | 103 | `ester` | `as_solvent_halogenated_aliphat` (4.7%) | `polyhalo_radical_transfer` (4.5%) | `alkali_other_salt` (3.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `brønsted_acid_cat` (4.8%) | `Mn_complex` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (65.5%) | `halogenated_aliphatic` (33.5%) | `polar_aprotic_sulfoxide` (0.4%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (96%) | `O` (92%) | `[H+].[OH-]` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCOC(C)=O` + `[Na+].[OH-]` | `Cl` (43%) | `OC(C(F)(F)F)C(F)(F` (30%) | `__ABSENT__` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (94%) | `CC(=O)NC1CC2(CCCCC` (5%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #1546  yield=52.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #3)

```
C=CCN(CC=C)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N(C[C@H](Cl)CCl)C[C@@H](Cl)CCl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.7%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (98.4%) | `graphite_felt` (0.9%) | `graphite_generic` (0.3%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.1%) | `carbon` (3.7%) | `stainless_steel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_felt` | `platinum_plate` (88.9%) | `platinum_generic` (8.2%) | `graphite_felt` (1.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NEt4` (99.7%) | `Li` (0.2%) | `NBu4` (0.1%) | ✗ |
| 电解质 anion | 26 | `Cl` | `Cl` (98.4%) | `BF4` (1.0%) | `ClO4` (0.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ester` | `hcl` (57.0%) | `polyhalo_radical_transfer` (4.9%) | `as_solvent_halogenated_aliphat` (1.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.8%) | `Mn_complex` (4.2%) | `organic_neutral_cat` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (97.8%) | `halogenated_aliphatic` (1.4%) | `ABSENT` (0.3%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (100%) | `CC#N` (100%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cl` + `O=C([O-])O.[Na+]` | `Cl` (100%) | `O=C([O-])O.[Na+]` (96%) | `COC(=O)c1ccc2cc(C(` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)NC1CC2(CCCCC` | `CC(=O)NC1CC2(CCCCC` (94%) | `__ABSENT__` (6%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #1547  yield=58.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #4)

```
C=Cc1ccccc1C>>Cc1ccccc1[C@H](Cl)CCl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.5%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (74.7%) | `carbon_generic` (15.5%) | `graphite_generic` (4.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (92.1%) | `carbon` (7.7%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_felt` | `platinum_generic` (70.8%) | `platinum_foil` (22.8%) | `platinum_plate` (4.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (89.1%) | `ABSENT` (7.6%) | `divided` (3.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (78.8%) | `NEt4` (8.5%) | `NBu4` (6.6%) | ✗ |
| 电解质 anion | 26 | `Cl` | `ClO4` (66.4%) | `BF4` (14.8%) | `molecular_no_ion` (5.5%) | ✗ |
| 试剂大类 | 103 | `ester` | `polyhalo_radical_transfer` (33.7%) | `carboxylic_acid` (15.9%) | `chloride_anion` (6.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (90.1%) | `Mn_complex` (7.4%) | `ABSENT` (1.6%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (78.6%) | `polar_protic_acid` (11.2%) | `ABSENT` (5.3%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (91%) | `O` (42%) | `ClCCl` (9%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `O=C(O)C(F)(F)F` | `CC(=O)O` (47%) | `O=C(O)C(F)(F)F` (42%) | `__OTHER__` (36%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)([O-])C(F)(` (65%) | `__OTHER__` (15%) | `O=S(=O)(O)C(F)(F)F` (10%) | set ✗ / any ✗ |

---

### Reaction #1548  yield=55.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #5)

```
C=CCCOS(=O)(=O)c1ccccc1>>O=S(=O)(OCC[C@H](Cl)CCl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (1.2%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (99.5%) | `reticulated_vitreous_carbon` (0.4%) | `graphite_felt` (0.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (96.9%) | `platinum` (2.9%) | `copper` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `platinum_wire` | `graphite_generic` (99.8%) | `platinum_foil` (0.1%) | `reticulated_vitreous_carbon` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NEt4` (88.2%) | `ABSENT` (10.5%) | `NBu4` (0.4%) | ✗ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (58.5%) | `BF4` (19.9%) | `Cl` (16.1%) | ✓ |
| 试剂大类 | 103 | `ester` | `polyhalo_radical_transfer` (64.5%) | `carboxylic_acid` (2.1%) | `ABSENT` (1.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Mn_complex` (50.3%) | `ABSENT` (36.6%) | `brønsted_acid_cat` (11.7%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `halogenated_aliphatic` (66.0%) | `polar_aprotic_nitrile` (18.8%) | `ABSENT` (14.7%) | ✗ |
| 溶剂 set | 79 | `O` | `ClCCl` (87%) | `CC#N` (31%) | `FC(F)(F)c1ccccc1` (21%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCOC(C)=O` + `[Na+].[OH-]` | `BrCCBr` (91%) | `OC(C(F)(F)F)C(F)(F` (37%) | `O=O` (24%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl][Mn][Cl]` (72%) | `O=S(=O)([O-])C(F)(` (16%) | `[Cl-].[Cl-].[Mn+2]` (4%) | set ✗ / any ✗ |

---

### Reaction #1549  yield=57.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #6)

```
C=CCCCCOC(=O)c1ccc(S(=O)(=O)N(CCC)CCC)cc1>>CCCN(CCC)S(=O)(=O)c1ccc(C(=O)OCCCC[C@@H](Cl)CCl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (1.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (76.0%) | `reticulated_vitreous_carbon` (20.5%) | `graphite_rod` (1.3%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.2%) | `platinum` (35.6%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_felt` | `platinum_plate` (47.1%) | `graphite_generic` (46.7%) | `carbon_felt` (2.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (97.0%) | `ABSENT` (2.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NEt4` (54.4%) | `NBu4` (28.1%) | `ABSENT` (10.3%) | ✗ |
| 电解质 anion | 26 | `Cl` | `ClO4` (44.3%) | `BF4` (26.7%) | `ABSENT` (13.4%) | ✗ |
| 试剂大类 | 103 | `ester` | `alkali_other_salt` (5.5%) | `ABSENT` (5.4%) | `as_solvent_halogenated_aliphat` (5.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.1%) | `Mn_complex` (2.3%) | `ammonium_PTC_organocat` (1.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `halogenated_aliphatic` (68.6%) | `ABSENT` (22.0%) | `polar_aprotic_nitrile` (8.9%) | ✗ |
| 溶剂 set | 79 | `[H+].[OH-]` | `ClCCl` (5%) | `ClCCCl` (4%) | `O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCOC(C)=O` + `[Na+].[OH-]` | `Cl` (24%) | `C[Si](C)(C)N=[N+]=` (21%) | `O.O.O.[Li+].[O-][C` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (1%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1550  yield=61.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #7)

```
C=CC1CCCCC1>>ClC[C@@H](Cl)C1CCCCC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (78.0%) | `platinum` (21.9%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (51.2%) | `reticulated_vitreous_carbon` (33.8%) | `platinum_generic` (11.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.9%) | `carbon` (1.0%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_felt` | `platinum_generic` (97.5%) | `platinum_plate` (1.9%) | `platinum_foil` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `divided` (0.8%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NBu4` (60.5%) | `Li` (20.6%) | `NEt4` (15.7%) | ✗ |
| 电解质 anion | 26 | `Cl` | `BF4` (57.6%) | `Cl` (17.2%) | `ClO4` (15.5%) | ✓ |
| 试剂大类 | 103 | `ester` | `carboxylic_acid` (36.3%) | `polyhalo_radical_transfer` (7.8%) | `chloride_anion` (6.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (39.8%) | `ABSENT` (39.4%) | `Mn_complex` (13.3%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (59.0%) | `polar_protic_acid` (33.8%) | `polar_aprotic_amide` (3.5%) | ✗ |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `CC#N` (96%) | `O` (86%) | `CC(=O)O` (12%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (96%) | `__OTHER__` (86%) | `OB(O)B(O)O` (69%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (46%) | `O=S(=O)([O-])C(F)(` (10%) | `__OTHER__` (5%) | set ✗ / any ✗ |

---

### Reaction #1551  yield=69.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #8)

```
C=Cc1ccc(C)cc1>>Cc1ccc([C@H](Cl)CCl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (96.4%) | `graphite_generic` (2.5%) | `carbon_generic` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (53.9%) | `platinum` (44.9%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_felt` | `platinum_foil` (97.3%) | `graphite_generic` (2.1%) | `platinum_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (53.7%) | `ABSENT` (44.2%) | `divided` (2.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (47.9%) | `NEt4` (40.1%) | `ABSENT` (4.7%) | ✗ |
| 电解质 anion | 26 | `Cl` | `ClO4` (46.1%) | `BF4` (26.7%) | `molecular_no_ion` (11.8%) | ✗ |
| 试剂大类 | 103 | `ester` | `polyhalo_radical_transfer` (51.5%) | `carboxylic_acid` (15.9%) | `inorganic_simple` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (83.1%) | `Mn_complex` (13.2%) | `ABSENT` (3.1%) | ✓ |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (81.8%) | `ABSENT` (9.2%) | `polar_protic_acid` (5.6%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (97%) | `CC#N` (95%) | `ClC(Cl)Cl` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[SiH](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (98%) | `__OTHER__` (97%) | `O=O` (95%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Pt]` | `O=S(=O)([O-])C(F)(` (41%) | `__OTHER__` (26%) | `O=S(=O)(O)C(F)(F)F` (11%) | set ✗ / any ✗ |

---

### Reaction #1552  yield=66.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #9)

```
C=CCCOC(=O)c1cccc2ccccc12>>O=C(OCC[C@@H](Cl)CCl)c1cccc2ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.1%) | `platinum` (1.6%) | `sacrificial_iron` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (87.9%) | `glassy_carbon` (4.8%) | `reticulated_vitreous_carbon` (3.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (90.2%) | `platinum` (9.7%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_felt` | `graphite_generic` (99.4%) | `platinum_plate` (0.2%) | `platinum_foil` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `ABSENT` (89.6%) | `NEt4` (4.6%) | `NBu4` (4.5%) | ✗ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (75.6%) | `BF4` (23.3%) | `Br` (0.3%) | ✗ |
| 试剂大类 | 103 | `ester` | `as_solvent_halogenated_aliphat` (23.8%) | `polyhalo_radical_transfer` (22.3%) | `ABSENT` (3.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Mn_complex` (68.1%) | `ABSENT` (31.6%) | `ammonium_PTC_organocat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (74.3%) | `halogenated_aliphatic` (23.9%) | `ABSENT` (0.7%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (98%) | `O` (85%) | `CC(=O)O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCOC(C)=O` + `[Na+].[OH-]` | `OCCBr` (100%) | `O=P([O-])([O-])[O-` (100%) | `O` (86%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl][Mn][Cl]` (99%) | `[Cl-].[Cl-].[Mn+2]` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #1553  yield=65.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #10)

```
C=CCCCCCCCCOC(=O)Cc1ccc(-c2ccccc2)c(F)c1>>O=C(Cc1ccc(-c2ccccc2)c(F)c1)OCCCCCCCC[C@H](Cl)CCl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.0%) | `sacrificial_zinc` (3.0%) | `platinum` (1.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (47.0%) | `graphite_felt` (21.6%) | `platinum_wire` (7.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (80.9%) | `platinum` (19.0%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_felt` | `reticulated_vitreous_carbon` (73.5%) | `carbon_felt` (13.1%) | `graphite_felt` (4.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (95.2%) | `divided` (4.4%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (60.0%) | `NBu4` (23.9%) | `NEt4` (10.1%) | ✗ |
| 电解质 anion | 26 | `Cl` | `Cl` (51.1%) | `ClO4` (25.4%) | `BF4` (8.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ester` | `ABSENT` (14.1%) | `carboxylic_acid` (5.3%) | `as_solvent_halogenated_aliphat` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.8%) | `Ni_complex` (2.3%) | `brønsted_acid_cat` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `ABSENT` (56.2%) | `polar_aprotic_nitrile` (39.2%) | `halogenated_aliphatic` (2.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `__ABSENT__` | `__ABSENT__` (89%) | `O` (8%) | `CCOCC` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCOC(C)=O` + `[Na+].[OH-]` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1554  yield=68.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #11)

```
C=CCCCCCl>>ClCCCC[C@H](Cl)CCl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.9%) | `platinum` (1.1%) | `sacrificial_iron` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (94.8%) | `graphite_generic` (1.5%) | `platinum_wire` (1.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.0%) | `platinum` (35.1%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_felt` | `platinum_wire` (57.3%) | `graphite_generic` (18.4%) | `platinum_generic` (14.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.5%) | `ABSENT` (1.2%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NEt4` (61.8%) | `Li` (30.7%) | `NBu4` (6.1%) | ✗ |
| 电解质 anion | 26 | `Cl` | `BF4` (65.4%) | `ClO4` (26.4%) | `Br` (2.6%) | ✗ |
| 试剂大类 | 103 | `ester` | `ABSENT` (15.3%) | `carboxylic_acid` (9.3%) | `polyhalo_radical_transfer` (6.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Mn_complex` (88.1%) | `Co_complex` (4.9%) | `ABSENT` (3.3%) | ✓ |
| 溶剂大类 | 27 | `ABSENT` | `ABSENT` (36.7%) | `polar_aprotic_nitrile` (34.7%) | `polar_protic_acid` (15.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` | `__ABSENT__` (37%) | `O` (11%) | `CC(=O)O` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCOC(C)=O` + `[Na+].[OH-]` | `__ABSENT__` (83%) | `O=P([O-])([O-])[O-` (15%) | `O=O` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br][Mn][Br]` | `[Cl][Mn][Cl]` (39%) | `[Br][Mn][Br]` (5%) | `[Br-].[Br-].[Mn+2]` (5%) | set ✗ / any ✓ |

---

### Reaction #1555  yield=62.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #12)

```
C=CCCOC(=O)C12CC3CC(CC(C3)C1)C2>>O=C(OCC[C@@H](Cl)CCl)C12CC3CC(CC(C3)C1)C2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.0%) | `platinum` (1.3%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (99.3%) | `reticulated_vitreous_carbon` (0.2%) | `carbon_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (90.3%) | `platinum` (9.5%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_felt` | `graphite_generic` (99.4%) | `platinum_foil` (0.2%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `ABSENT` (91.9%) | `NBu4` (5.6%) | `NEt4` (1.5%) | ✗ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (80.8%) | `BF4` (15.4%) | `Cl` (1.8%) | ✓ |
| 试剂大类 | 103 | `ester` | `polyhalo_radical_transfer` (16.5%) | `ABSENT` (14.8%) | `as_solvent_halogenated_aliphat` (5.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (52.5%) | `Mn_complex` (45.6%) | `ammonium_PTC_organocat` (1.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (82.4%) | `polar_aprotic_nitrile` (14.6%) | `ABSENT` (1.2%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `O` (95%) | `CC#N` (7%) | `ClCCl` (4%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCOC(C)=O` + `[Na+].[OH-]` | `OCCBr` (59%) | `Cc1ccc(I)cc1` (17%) | `ClCC(Cl)(Cl)Cl` (11%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (92%) | `[Cl][Mn][Cl]` (6%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #1556  yield=66.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #13)

```
C=Cc1ccc([N+](=O)[O-])cc1>>O=[N+]([O-])c1ccc([C@H](Cl)CCl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (58.3%) | `reticulated_vitreous_carbon` (39.9%) | `carbon_generic` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (69.2%) | `platinum` (29.6%) | `stainless_steel` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_felt` | `platinum_foil` (97.9%) | `graphite_generic` (1.6%) | `platinum_generic` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (64.9%) | `NEt4` (29.0%) | `ABSENT` (2.7%) | ✗ |
| 电解质 anion | 26 | `Cl` | `BF4` (44.0%) | `molecular_no_ion` (23.8%) | `ClO4` (15.8%) | ✗ |
| 试剂大类 | 103 | `ester` | `polyhalo_radical_transfer` (64.9%) | `transition_metal_salt_reagent` (4.5%) | `carboxylic_acid` (3.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (65.2%) | `Mn_complex` (27.8%) | `ABSENT` (6.5%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (90.9%) | `ABSENT` (3.8%) | `polar_protic_acid` (3.8%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (97%) | `O` (86%) | `ClC(Cl)Cl` (6%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCOC(C)=O` + `[Na+].[OH-]` | `__OTHER__` (54%) | `OB(O)B(O)O` (47%) | `O=O` (45%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)([O-])C(F)(` (41%) | `__OTHER__` (31%) | `c1ccncc1` (18%) | set ✗ / any ✗ |

---

### Reaction #1557  yield=62.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #14)

```
C=CCCO>>OCC[C@@H](Cl)CCl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.5%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (99.4%) | `reticulated_vitreous_carbon` (0.3%) | `carbon_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.6%) | `copper` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_felt` | `graphite_generic` (99.8%) | `platinum_foil` (0.1%) | `reticulated_vitreous_carbon` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NEt4` (83.4%) | `ABSENT` (10.4%) | `Li` (3.9%) | ✗ |
| 电解质 anion | 26 | `Cl` | `BF4` (47.1%) | `ABSENT` (34.5%) | `ClO4` (12.8%) | ✗ |
| 试剂大类 | 103 | `ester` | `polyhalo_radical_transfer` (85.8%) | `carboxylic_acid` (3.4%) | `ABSENT` (0.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Mn_complex` (61.6%) | `ABSENT` (20.1%) | `brønsted_acid_cat` (18.0%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (66.7%) | `ABSENT` (16.1%) | `halogenated_aliphatic` (15.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (62%) | `O` (59%) | `ClCCl` (32%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCOC(C)=O` + `[Na+].[OH-]` | `O=O` (57%) | `BrCCBr` (56%) | `__OTHER__` (45%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)([O-])C(F)(` (61%) | `[Cl][Mn][Cl]` (25%) | `[Cl-].[Cl-].[Mn+2]` (10%) | set ✗ / any ✗ |

---

### Reaction #1558  yield=72.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #15)

```
C=CCCOC(=O)c1ccccc1>>O=C(OCC[C@@H](Cl)CCl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `nickel` (0.3%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (98.1%) | `reticulated_vitreous_carbon` (0.8%) | `glassy_carbon` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (98.0%) | `platinum` (1.9%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_felt` | `graphite_generic` (99.8%) | `platinum_foil` (0.1%) | `graphite_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `ABSENT` (96.9%) | `NEt4` (2.2%) | `NBu4` (0.5%) | ✗ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (94.2%) | `BF4` (5.4%) | `molecular_no_ion` (0.1%) | ✗ |
| 试剂大类 | 103 | `ester` | `polyhalo_radical_transfer` (62.5%) | `as_solvent_halogenated_aliphat` (7.3%) | `ABSENT` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Mn_complex` (93.1%) | `ABSENT` (6.4%) | `brønsted_acid_cat` (0.2%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.0%) | `ABSENT` (2.2%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (96%) | `CC#N` (42%) | `ClCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `OCCBr` + `O` + `O=P([O-])([O-])[O-` | `OCCBr` (98%) | `O=P([O-])([O-])[O-` (95%) | `O` (72%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Cl][Mn][Cl]` | `[Cl][Mn][Cl]` (98%) | `[Cl-].[Cl-].[Mn+2]` (1%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #1559  yield=77.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #16)

```
C=CCCCOC(=O)c1ccccc1>>O=C(OCCC[C@H](Cl)CCl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.4%) | `ABSENT` (0.3%) | `sacrificial_magnesium` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (60.7%) | `reticulated_vitreous_carbon` (32.6%) | `carbon_generic` (1.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (98.5%) | `platinum` (1.1%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_felt` | `graphite_generic` (91.6%) | `platinum_foil` (3.3%) | `graphite_felt` (3.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (69.4%) | `ABSENT` (28.3%) | `divided` (2.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `ABSENT` (61.8%) | `NEt4` (32.2%) | `Li` (3.4%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `ABSENT` (77.4%) | `BF4` (15.2%) | `ClO4` (2.8%) | ✗ |
| 试剂大类 | 103 | `ester` | `polyhalo_radical_transfer` (29.8%) | `carboxylic_acid` (5.7%) | `as_solvent_halogenated_aliphat` (4.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Mn_complex` (50.2%) | `ABSENT` (36.1%) | `brønsted_acid_cat` (11.9%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `halogenated_aliphatic` (52.6%) | `ABSENT` (35.3%) | `polar_aprotic_nitrile` (10.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `CO` | `O` (71%) | `ClCCl` (27%) | `OCC(F)(F)F` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CS(C)=O` + `CCCC[N+](CCCC)(CCC` + `O=S(=O)(O)C(F)(F)F` + `C[O-].[Na+]` | `OCCBr` (35%) | `BrCCBr` (24%) | `ClC(Cl)(Cl)C(Cl)(C` (20%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl][Mn][Cl]` (56%) | `O=S(=O)([O-])C(F)(` (5%) | `[Cl-].[Cl-].[Mn+2]` (4%) | set ✗ / any ✗ |

---

### Reaction #1560  yield=72.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #17)

```
C=CCCOC(=O)c1ccccc1>>O=C(OCC[C@@H](Br)CBr)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (99.2%) | `carbon` (0.7%) | `sacrificial_iron` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_felt` | `platinum_wire` (99.9%) | `platinum_generic` (0.0%) | `reticulated_vitreous_carbon` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.1%) | `carbon` (2.5%) | `nickel` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `graphite_felt` | `platinum_wire` (99.8%) | `platinum_generic` (0.1%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `divided` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (93.4%) | `ABSENT` (4.6%) | `Na` (1.5%) | ✓ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (45.6%) | `Br` (33.0%) | `ABSENT` (17.1%) | ✓ |
| 试剂大类 | 103 | `ester` | `ABSENT` (21.9%) | `as_solvent_halogenated_aliphat` (13.6%) | `tetraaryl_borate` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.0%) | `Ni_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_protic_acid` (98.3%) | `ABSENT` (1.4%) | `polar_aprotic_nitrile` (0.2%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC(=O)O` (100%) | `O` (4%) | `ClC(Cl)Cl` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `OCCBr` + `O` + `O=P([O-])([O-])[O-` | `OCCBr` (51%) | `__ABSENT__` (42%) | `O` (32%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Cl][Mn][Cl]` | `__ABSENT__` (94%) | `[Cl][Mn][Cl]` (1%) | `[Br][Mn][Br]` (1%) | set ✗ / any ✓ |

---

### Reaction #1561  yield=84.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_42_13208-13213.json) (反应 idx 在该 JSON 内 = #18)

```
C=CCCCCOC(=O)c1ccccc1>>O=C(OCCCC[C@@H](Cl)CCl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.4%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (52.7%) | `graphite_generic` (38.9%) | `graphite_felt` (3.5%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (91.7%) | `platinum` (7.6%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_felt` | `graphite_generic` (70.0%) | `platinum_foil` (22.3%) | `graphite_felt` (4.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (87.9%) | `ABSENT` (11.6%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `ABSENT` (69.0%) | `NEt4` (17.6%) | `Li` (9.0%) | ✗ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (63.5%) | `BF4` (30.5%) | `ClO4` (2.8%) | ✗ |
| 试剂大类 | 103 | `ester` | `polyhalo_radical_transfer` (24.6%) | `as_solvent_halogenated_aliphat` (10.9%) | `carboxylic_acid` (5.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Mn_complex` (65.0%) | `ABSENT` (22.0%) | `brønsted_acid_cat` (11.1%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `halogenated_aliphatic` (70.3%) | `ABSENT` (20.4%) | `polar_aprotic_nitrile` (6.2%) | ✗ |
| 溶剂 set | 79 | `O` | `O` (82%) | `ClCCl` (17%) | `ClC(Cl)Cl` (9%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCOC(C)=O` + `[Na+].[OH-]` | `OCCBr` (73%) | `O=P([O-])([O-])[O-` (54%) | `__OTHER__` (12%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl][Mn][Cl]` (60%) | `O=S(=O)([O-])C(F)(` (4%) | `[Cl-].[Cl-].[Mn+2]` (2%) | set ✗ / any ✗ |

---

### Reaction #1562  yield=17.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>OC1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (98.9%) | `platinum` (0.7%) | `ABSENT` (0.4%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (42.7%) | `graphite_rod` (21.7%) | `reticulated_vitreous_carbon` (18.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `carbon` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (92.2%) | `platinum_generic` (7.3%) | `platinum_foil` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (70.6%) | `K` (10.5%) | `NBu4` (9.7%) | ✓ |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (51.3%) | `ClO4` (27.0%) | `ABSENT` (8.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.1%) | `as_solvent_halogenated_aliphat` (3.8%) | `carboxylic_acid` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (93.7%) | `organic_neutral_cat` (1.9%) | `Mn_complex` (1.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (88.2%) | `ABSENT` (6.5%) | `cyclic_ether` (1.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `CC#N` (99%) | `O` (72%) | `CC(=O)O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `__ABSENT__` (97%) | `O=O` (54%) | `__OTHER__` (50%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (83%) | `[Fe+2].c1cc[cH-]c1` (2%) | `[Pt]` (2%) | set ✗ / any ✗ |

---

### Reaction #1563  yield=51.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(F)cc1>>O=C1CCC(c2ccc(F)cc2)c2cc(F)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (74.0%) | `ABSENT` (22.8%) | `platinum` (3.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (58.3%) | `ABSENT` (22.4%) | `carbon_felt` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (59.3%) | `carbon` (25.6%) | `ABSENT` (14.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (47.1%) | `graphite_generic` (23.9%) | `carbon_felt` (8.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (95.6%) | `divided` (4.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (39.0%) | `molecular_no_ion` (21.5%) | `Li` (10.9%) | ✗ |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (91.6%) | `fluoride_complex` (2.3%) | `Br` (1.7%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (6.4%) | `aryl_iodide_mediator` (3.4%) | `o2_oxidant` (3.1%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (96.9%) | `ionic_organocat` (1.7%) | `Pt_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (41.1%) | `ABSENT` (24.3%) | `halogenated_aliphatic` (10.0%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (56%) | `ClCCl` (35%) | `O` (13%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `__ABSENT__` (83%) | `O=O` (26%) | `OB(O)B(O)O` (12%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Mn+2]` | `[Cl-].[Cl-].[Mn+2]` (65%) | `__ABSENT__` (34%) | `c1ccncc1` (1%) | set ✓ / any ✓ |

---

### Reaction #1564  yield=53.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1cccc2ccccc12>>O=C1CCC(c2cccc3ccccc23)c2ccc3ccccc3c21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_rod` (68.3%) | `glassy_carbon` (22.1%) | `graphite_rod` (7.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `stainless_steel` (0.2%) | `carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.3%) | `NEt4` (6.0%) | `K` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (98.9%) | `Br` (0.6%) | `PF6` (0.2%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (27.7%) | `carboxylic_acid` (2.7%) | `metal_oxide_oxidant` (1.9%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.4%) | `ionic_organocat` (0.4%) | `Mn_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (49.4%) | `polar_protic_alcohol` (36.7%) | `polar_aprotic_sulfoxide` (7.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `CC#N` (93%) | `CCOCC` (30%) | `ClCCl` (20%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `__ABSENT__` (91%) | `O=O` (57%) | `OB(O)B(O)O` (23%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (94%) | `[Fe+2].c1cc[cH-]c1` (2%) | `[Cl-].[Cl-].[Mn+2]` (2%) | set ✗ / any ✗ |

---

### Reaction #1565  yield=61.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1ccc(OC(C)=O)cc1>>CC(=O)Oc1ccc(C2CCC(=O)c3ccc(OC(C)=O)cc32)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (79.5%) | `platinum` (18.4%) | `ABSENT` (1.7%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (58.6%) | `carbon_rod` (22.8%) | `platinum_generic` (6.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (48.7%) | `platinum` (48.7%) | `ABSENT` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (51.7%) | `carbon_felt` (26.0%) | `platinum_generic` (8.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (46.8%) | `Li` (15.4%) | `ABSENT` (11.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `molecular_no_ion` (77.7%) | `Br` (5.6%) | `I` (4.5%) | ✗ |
| 试剂大类 | 103 | `ammonium_salt` | `ABSENT` (9.4%) | `silane_other` (3.4%) | `o2_oxidant` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `Co_complex` (0.3%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_protic_alcohol` (49.5%) | `cyclic_ether` (21.0%) | `halogenated_aliphatic` (9.7%) | ✗ |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `FC(F)(F)c1ccccc1` (85%) | `CCOCC` (38%) | `ClCCl` (20%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `__ABSENT__` (97%) | `O=O` (34%) | `OB(O)B(O)O` (25%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1566  yield=66.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #4)

```
C=Cc1ccccc1C>>Cc1ccccc1C1CCC(=O)c2c(C)cccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_rod` (91.1%) | `graphite_rod` (4.3%) | `graphite_generic` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.6%) | `nickel` (1.6%) | `carbon` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (79.5%) | `platinum_generic` (16.1%) | `nickel_plate` (4.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (56.0%) | `NBu4` (29.9%) | `ABSENT` (7.9%) | ✓ |
| 电解质 anion | 26 | `Cl` | `BF4` (35.3%) | `I` (25.3%) | `carboxylate` (15.3%) | ✗ |
| 试剂大类 | 103 | `ammonium_salt` | `ABSENT` (35.0%) | `cyanide` (2.5%) | `metal_oxide_oxidant` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (78.8%) | `ammonium_PTC_organocat` (10.0%) | `ionic_organocat` (8.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_protic_alcohol` (88.4%) | `polar_aprotic_nitrile` (6.5%) | `cyclic_ether` (3.2%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (80%) | `O` (38%) | `CO` (14%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `O=C(O)C(F)(F)F` | `__ABSENT__` (99%) | `O=O` (2%) | `O` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `__OTHER__` (1%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✓ / any ✓ |

---

### Reaction #1567  yield=65.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #5)

```
C=Cc1ccc(Br)cc1>>O=C1CCC(c2ccc(Br)cc2)c2cc(Br)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (93.6%) | `platinum` (6.0%) | `ABSENT` (0.3%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (85.3%) | `carbon_rod` (4.5%) | `platinum_generic` (2.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (79.0%) | `carbon` (19.4%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (47.4%) | `graphite_generic` (23.7%) | `platinum_generic` (18.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.8%) | `divided` (2.8%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (87.4%) | `molecular_no_ion` (6.0%) | `Li` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (60.0%) | `BF4` (14.3%) | `Br` (10.5%) | ✗ |
| 试剂大类 | 103 | `water` | `alkali_sulfonate` (5.0%) | `ABSENT` (3.3%) | `primary_amine` (2.4%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.8%) | `ionic_organocat` (0.1%) | `Pt_complex` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (49.6%) | `polar_aprotic_nitrile` (22.9%) | `cyclic_ether` (11.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (77%) | `ClCCl` (49%) | `CCOCC` (19%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (99%) | `CC[Si](CC)CC` (97%) | `OB(O)B(O)O` (85%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (81%) | `[Pt]` (11%) | `[Cl-].[Cl-].[Mn+2]` (5%) | set ✗ / any ✓ |

---

### Reaction #1568  yield=67.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #6)

```
C=Cc1ccc(Cl)cc1>>O=C1CCC(c2ccc(Cl)cc2)c2cc(Cl)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (94.4%) | `platinum` (3.4%) | `ABSENT` (2.1%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (93.3%) | `glassy_carbon` (1.4%) | `carbon_rod` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (67.3%) | `carbon` (29.7%) | `ABSENT` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (41.6%) | `platinum_plate` (40.8%) | `platinum_generic` (9.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (93.2%) | `divided` (6.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (29.8%) | `Na` (17.0%) | `molecular_no_ion` (15.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (87.0%) | `ABSENT` (2.8%) | `I` (2.5%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (6.7%) | `alkali_sulfonate` (3.3%) | `iodide_anion` (2.5%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (98.5%) | `ionic_organocat` (0.8%) | `ammonium_PTC_organocat` (0.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (83.8%) | `polar_aprotic_nitrile` (11.8%) | `cyclic_ether` (2.2%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (82%) | `O` (9%) | `ClCCl` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (69%) | `OB(O)B(O)O` (64%) | `O` (64%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `__ABSENT__` (68%) | `c1ccncc1` (50%) | `[Cl-].[Cl-].[Mn+2]` (17%) | set ✗ / any ✓ |

---

### Reaction #1569  yield=70.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #7)

```
C=Cc1ccc(OC(C)(C)C)cc1>>CC(C)(C)Oc1ccc(C2CCC(=O)c3ccc(OC(C)(C)C)cc32)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (62.4%) | `carbon` (34.6%) | `ABSENT` (1.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (62.6%) | `carbon_rod` (12.8%) | `graphite_generic` (10.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (62.1%) | `carbon` (34.9%) | `ABSENT` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (45.9%) | `carbon_felt` (25.1%) | `graphite_generic` (16.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `divided` (1.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (62.4%) | `Li` (30.4%) | `Na` (3.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (62.3%) | `ClO4` (12.6%) | `I` (8.9%) | ✗ |
| 试剂大类 | 103 | `water` | `o2_oxidant` (8.7%) | `ABSENT` (5.0%) | `silane_other` (3.0%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.0%) | `Co_complex` (0.8%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (52.4%) | `polar_aprotic_nitrile` (20.9%) | `ABSENT` (9.9%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (58%) | `FC(F)(F)c1ccccc1` (24%) | `CO` (12%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `O=O` (100%) | `OB(O)B(O)O` (94%) | `CC[Si](CC)CC` (70%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (94%) | `c1ccncc1` (10%) | `[Cl-].[Cl-].[Mn+2]` (2%) | set ✗ / any ✗ |

---

### Reaction #1570  yield=70.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #8)

```
C=Cc1ccc(OCC)cc1>>CCOc1ccc(C2CCC(=O)c3ccc(OCC)cc32)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (89.2%) | `platinum` (8.2%) | `ABSENT` (1.6%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (31.1%) | `graphite_rod` (16.8%) | `zinc_plate` (15.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (76.5%) | `carbon` (22.2%) | `nickel` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `carbon_felt` (63.0%) | `platinum_generic` (29.3%) | `platinum_plate` (2.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (96.7%) | `divided` (3.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (60.9%) | `Li` (22.5%) | `molecular_no_ion` (6.6%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (92.4%) | `ClO4` (2.9%) | `I` (1.4%) | ✗ |
| 试剂大类 | 103 | `water` | `o2_oxidant` (4.8%) | `aryl_iodide_mediator` (4.0%) | `ABSENT` (3.3%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.5%) | `Pt_complex` (0.2%) | `Co_complex` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (92.0%) | `nitroalkane` (1.9%) | `polar_protic_alcohol` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `O` | `__ABSENT__` (98%) | `CCOCC` (7%) | `O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `O=O` (100%) | `OB(O)B(O)O` (19%) | `CC[Si](CC)CC` (10%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (100%) | `c1ccncc1` (1%) | `[Pt]` (0%) | set ✗ / any ✓ |

---

### Reaction #1571  yield=80.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #9)

```
C=Cc1ccc(C)cc1>>Cc1ccc(C2CCC(=O)c3ccc(C)cc32)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (92.0%) | `platinum` (5.1%) | `ABSENT` (2.3%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (49.2%) | `graphite_rod` (18.4%) | `carbon_rod` (8.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (74.7%) | `carbon` (21.3%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (68.7%) | `graphite_generic` (14.2%) | `carbon_felt` (5.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (78.9%) | `undivided` (20.5%) | `ABSENT` (0.5%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (53.9%) | `ABSENT` (37.0%) | `protonated_amine` (3.8%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (37.8%) | `molecular_no_ion` (23.7%) | `BF4` (16.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (4.8%) | `as_solvent_polar_aprotic_sulfo` (4.7%) | `silyl_electrophile` (2.8%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (98.0%) | `ionic_organocat` (1.3%) | `Co_complex` (0.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (50.3%) | `polar_protic_alcohol` (19.5%) | `cyclic_ether` (11.8%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `__ABSENT__` (27%) | `CCOCC` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[SiH](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (91%) | `OB(O)B(O)O` (89%) | `__OTHER__` (69%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (84%) | `[Pt]` (7%) | `[Cl-].[Cl-].[Mn+2]` (6%) | set ✗ / any ✓ |

---

### Reaction #1572  yield=80.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #10)

```
C=Cc1ccccc1>>O=C1CCC(c2ccccc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (82.4%) | `platinum` (13.5%) | `ABSENT` (2.6%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (53.5%) | `carbon_rod` (16.9%) | `reticulated_vitreous_carbon` (6.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (67.3%) | `platinum` (27.0%) | `nickel` (3.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (39.1%) | `platinum_generic` (26.3%) | `nickel_plate` (10.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (53.9%) | `ABSENT` (33.6%) | `divided` (12.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (72.6%) | `Li` (6.1%) | `Na` (6.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `I` (42.4%) | `BF4` (15.2%) | `ClO4` (12.6%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (10.6%) | `alkali_sulfonate` (2.9%) | `cyanide` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (94.9%) | `ammonium_PTC_organocat` (2.2%) | `ionic_organocat` (2.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (39.2%) | `cyclic_ether` (27.4%) | `polar_protic_alcohol` (22.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C[N+](=O)[O-]` (99%) | `C1COCCO1` (92%) | `CC#N` (7%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O` (99%) | `CC[Si](CC)CC` (98%) | `OB(O)B(O)O` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (94%) | `__OTHER__` (84%) | `__ABSENT__` (11%) | set ✓ / any ✓ |

---

### Reaction #1573  yield=79.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #11)

```
C=Cc1cc(C)ccc1C>>Cc1ccc(C)c(C2CCC(=O)c3c(C)ccc(C)c32)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (70.7%) | `platinum` (28.3%) | `ABSENT` (0.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_rod` (46.9%) | `reticulated_vitreous_carbon` (27.7%) | `platinum_generic` (15.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `nickel` (0.6%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (82.6%) | `platinum_plate` (16.6%) | `nickel_plate` (0.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.8%) | `divided` (0.7%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.6%) | `ABSENT` (9.0%) | `K` (2.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (73.6%) | `ABSENT` (10.0%) | `carboxylate` (3.5%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (20.8%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (94.9%) | `ionic_organocat` (3.7%) | `Fe_complex` (0.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (34.1%) | `ABSENT` (26.7%) | `polar_aprotic_nitrile` (12.9%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (68%) | `OC(C(F)(F)F)C(F)(F` (13%) | `CO` (12%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✓ |

---

### Reaction #1574  yield=76.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #12)

```
C=Cc1ccc(CC)cc1>>CCc1ccc(C2CCC(=O)c3ccc(CC)cc32)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `ABSENT` (71.7%) | `carbon` (25.6%) | `platinum` (2.1%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `ABSENT` (73.4%) | `graphite_generic` (23.5%) | `platinum_generic` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `ABSENT` (60.8%) | `platinum` (26.9%) | `carbon` (11.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `ABSENT` (69.0%) | `graphite_generic` (15.4%) | `platinum_generic` (6.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (48.2%) | `divided` (46.2%) | `ABSENT` (5.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.9%) | `Na` (10.1%) | `Li` (3.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `I` (26.3%) | `Br` (17.5%) | `BF4` (17.1%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (7.0%) | `as_solvent_polar_aprotic_sulfo` (3.2%) | `o2_oxidant` (2.6%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (98.3%) | `Co_complex` (0.9%) | `Pt_complex` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `cyclic_ether` (39.1%) | `polar_aprotic_nitrile` (28.2%) | `polar_protic_alcohol` (13.9%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (77%) | `CC#N` (51%) | `C1CCOC1` (9%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (94%) | `O=O` (32%) | `OB(O)B(O)O` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (97%) | `[Cl-].[Cl-].[Mn+2]` (2%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #1575  yield=78.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #13)

```
C=Cc1ccc2ccccc2c1>>O=C1CCC(c2ccc3ccccc3c2)c2c1ccc1ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (94.5%) | `platinum` (4.1%) | `ABSENT` (1.2%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (53.2%) | `carbon_felt` (13.7%) | `ABSENT` (8.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (78.5%) | `carbon` (10.1%) | `nickel` (6.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (40.1%) | `platinum_plate` (18.9%) | `platinum_wire` (13.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (80.1%) | `divided` (14.6%) | `ABSENT` (5.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (76.5%) | `Li` (21.3%) | `Na` (1.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (41.8%) | `OTf` (14.7%) | `ClO4` (11.6%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (11.6%) | `silane_other` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (93.4%) | `brønsted_acid_cat` (5.1%) | `Co_complex` (1.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (67.3%) | `polar_aprotic_amide` (22.2%) | `polar_protic_alcohol` (2.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `[H+].[OH-]` | `CC#N` (99%) | `[H+].[OH-]` (11%) | `ClCCl` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (78%) | `__OTHER__` (68%) | `__ABSENT__` (57%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O.O.[K+].[K+].[O]=` + `CC[C@H]1CN2CC[C@H]` | `__ABSENT__` (83%) | `[Cl-].[Cl-].[Mn+2]` (5%) | `O.O.[K+].[K+].[O]=` (4%) | set ✗ / any ✓ |

---

### Reaction #1576  yield=75.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #14)

```
C=Cc1ccc(C)cc1C>>Cc1ccc(C2CCC(=O)c3c(C)cc(C)cc32)c(C)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_rod` (89.9%) | `graphite_generic` (7.1%) | `carbon_rod` (1.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.4%) | `stainless_steel` (2.1%) | `carbon` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (95.9%) | `platinum_generic` (2.2%) | `nickel_plate` (0.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.8%) | `divided` (2.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (60.8%) | `Na` (27.9%) | `NBu4` (6.7%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (73.8%) | `BF4` (10.4%) | `molecular_no_ion` (7.8%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (18.6%) | `cyanide` (2.3%) | `tetraaryl_borate` (2.1%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (83.3%) | `ionic_organocat` (10.3%) | `Co_complex` (3.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (51.0%) | `polar_aprotic_nitrile` (27.9%) | `aqueous` (11.8%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (83%) | `ClCCl` (55%) | `O` (20%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (97%) | `O=O` (23%) | `OB(O)B(O)O` (17%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (85%) | `CCCC[N+](CCCC)(CCC` (6%) | `[Cl-].[Cl-].[Mn+2]` (3%) | set ✗ / any ✗ |

---

### Reaction #1577  yield=75.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #15)

```
C=Cc1ccc(OC)cc1>>COc1ccc(C2CCC(=O)c3ccc(OC)cc32)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (76.6%) | `platinum` (19.2%) | `ABSENT` (4.2%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (49.2%) | `carbon_rod` (18.4%) | `graphite_rod` (8.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (70.9%) | `platinum` (25.5%) | `ABSENT` (3.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (42.5%) | `platinum_plate` (16.3%) | `carbon_felt` (14.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (89.2%) | `divided` (9.3%) | `ABSENT` (1.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.3%) | `Li` (10.9%) | `Na` (4.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (38.4%) | `molecular_no_ion` (29.0%) | `ClO4` (14.2%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (13.6%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.4%) | `Co_complex` (0.3%) | `Fe_complex` (0.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.2%) | `polar_aprotic_nitrile` (14.0%) | `nitroalkane` (9.2%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (87%) | `CO` (6%) | `ClCCl` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `N=C(c1ccccc1)c1ccc` + `C1CN=C2NCCCN2C1` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (93%) | `O=O` (13%) | `OC(C(F)(F)F)C(F)(F` (2%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (96%) | `[Fe+2].c1cc[cH-]c1` (3%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #1578  yield=77.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #16)

```
C=Cc1ccc(CCl)cc1>>O=C1CCC(c2ccc(CCl)cc2)c2cc(CCl)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (97.3%) | `platinum` (1.6%) | `ABSENT` (1.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (26.8%) | `carbon_felt` (21.0%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.8%) | `carbon` (25.3%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (77.2%) | `carbon_felt` (6.8%) | `graphite_generic` (4.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (95.8%) | `divided` (3.7%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (73.7%) | `Li` (12.5%) | `protonated_amine` (4.8%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (47.5%) | `molecular_no_ion` (22.5%) | `ClO4` (7.7%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (14.4%) | `ammonia` (2.2%) | `o2_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (98.2%) | `Fe_complex` (0.7%) | `ionic_organocat` (0.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (82.1%) | `polar_aprotic_nitrile` (7.5%) | `halogenated_aliphatic` (3.6%) | ✓ |
| 溶剂 set | 79 | `CC(C)=O` + `O` | `ClCCl` (52%) | `CC(C)=O` (41%) | `CC#N` (18%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O.O.O.O.O.O.O.O.O.` | `__ABSENT__` (99%) | `CCN(CC)CC.F.F.F` (3%) | `O=O` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Mn][Cl]` | `__ABSENT__` (99%) | `[O]=[Fe][O][Fe]=[O` (0%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✗ / any ✗ |

---

### Reaction #1579  yield=84.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #17)

```
C=Cc1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc(C2CCC(=O)c3ccc(C(C)(C)C)cc32)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (91.3%) | `platinum` (6.6%) | `ABSENT` (1.1%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (79.7%) | `platinum_generic` (8.7%) | `carbon_rod` (4.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (49.5%) | `carbon` (45.2%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (86.4%) | `platinum_generic` (7.5%) | `platinum_plate` (3.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `divided` (0.8%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.3%) | `Li` (9.9%) | `Na` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ClO4` (21.8%) | `BF4` (21.0%) | `molecular_no_ion` (17.7%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (6.2%) | `silane_other` (2.9%) | `o2_oxidant` (2.6%) | ✗ |
| 催化剂大类 | 49 | `Pt_complex` | `ABSENT` (99.7%) | `Co_complex` (0.1%) | `ionic_organocat` (0.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (46.0%) | `cyclic_ether` (25.2%) | `ABSENT` (22.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C1CCOC1` + `CC#N` | `CC#N` (100%) | `C1CCOC1` (24%) | `O` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (90%) | `CC[Si](CC)CC` (76%) | `OB(O)B(O)O` (75%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `Oc1ccccc1C=NCCN=Cc` + `O=S(=O)([O-])C(F)(` | `__ABSENT__` (67%) | `Oc1ccccc1C=NCCN=Cc` (29%) | `O=S(=O)([O-])C(F)(` (17%) | set ✗ / any ✓ |

---

### Reaction #1580  yield=83.0%

**Source paper**: [`GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2025_Green_Chemistry_2025_27_43_13644-13650.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(-c2ccccc2)cc1>>O=C1CCC(c2ccc(-c3ccccc3)cc2)c2cc(-c3ccccc3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (95.6%) | `platinum` (3.6%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_rod` (62.6%) | `graphite_generic` (14.8%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.2%) | `carbon` (3.3%) | `nickel` (1.1%) | ✓ (T1✓) |
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

### Reaction #1581  yield=25.0%

**Source paper**: [`JACS/2025_Journal_of_the_American_Chemical_Society_2025_147_1_318-330.json`](reactions_by_journal_alkene_ec_audited/JACS/2025_Journal_of_the_American_Chemical_Society_2025_147_1_318-330.json) (反应 idx 在该 JSON 内 = #0)

```
CC1(C)CCCC(C)(C)N1[O].C=C=C(C)c1ccccc1>>CC(O)(C(=O)CON1C(C)(C)CCCC1(C)C)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (63.4%) | `graphite_rod` (14.4%) | `unknown_electrode` (10.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.5%) | `ABSENT` (0.6%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (89.3%) | `platinum_plate` (6.4%) | `platinum_generic` (4.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.7%) | `ABSENT` (2.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Li` (73.6%) | `NBu4` (10.7%) | `ABSENT` (8.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (77.4%) | `ClO4` (13.1%) | `ABSENT` (3.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `selenium_reagent` (5.6%) | `alkali_phosphate` (4.6%) | `ABSENT` (4.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `brønsted_acid_cat` (1.9%) | `Pt_complex` (1.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.9%) | `polar_aprotic_sulfoxide` (0.3%) | `halogenated_aliphatic` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (94%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `c1ccc([Se][Se]c2cc` (50%) | `[Cl-].[NH4+]` (11%) | `[N-]=[N+]=[N][Na]` (10%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `CC1(C)CCCC(C)(C)N1` (0%) | set ✓ / any ✓ |

---

### Reaction #1582  yield=45.0%

**Source paper**: [`JCatal/10.1016_j.jcat.2025.116252_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JCatal/10.1016_j.jcat.2025.116252_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>C1OC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (79.0%) | `platinum` (12.7%) | `ABSENT` (7.4%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_generic` (77.8%) | `glassy_carbon` (16.7%) | `unknown_electrode` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (77.6%) | `ABSENT` (8.6%) | `stainless_steel` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (39.5%) | `platinum_plate` (28.5%) | `stainless_steel_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (73.7%) | `undivided` (26.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (52.9%) | `ABSENT` (19.7%) | `NBu4` (9.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (47.0%) | `ABSENT` (29.1%) | `PF6` (9.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (6.5%) | `alkali_sulfinate` (6.4%) | `alkali_hydroxide` (6.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (60.5%) | `ABSENT` (17.2%) | `Mn_complex` (6.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `aqueous` (36.1%) | `polar_aprotic_nitrile` (32.6%) | `polar_aprotic_sulfoxide` (15.7%) | ✓ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (96%) | `C[N+](=O)[O-]` (94%) | `O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (100%) | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (98%) | `O=S(=O)([O-])[O-].` (0%) | set ✓ / any ✓ |

---

### Reaction #1583  yield=0.0%

**Source paper**: [`JCatal/10.1016_j.jcat.2025.116252_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JCatal/10.1016_j.jcat.2025.116252_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>C1OC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (79.0%) | `platinum` (12.7%) | `ABSENT` (7.4%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_generic` (77.8%) | `glassy_carbon` (16.7%) | `unknown_electrode` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (77.6%) | `ABSENT` (8.6%) | `stainless_steel` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (39.5%) | `platinum_plate` (28.5%) | `stainless_steel_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (73.7%) | `undivided` (26.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (52.9%) | `ABSENT` (19.7%) | `NBu4` (9.5%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (47.0%) | `ABSENT` (29.1%) | `PF6` (9.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (6.5%) | `alkali_sulfinate` (6.4%) | `alkali_hydroxide` (6.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (60.5%) | `ABSENT` (17.2%) | `Mn_complex` (6.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `aqueous` (36.1%) | `polar_aprotic_nitrile` (32.6%) | `polar_aprotic_sulfoxide` (15.7%) | ✓ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (96%) | `C[N+](=O)[O-]` (94%) | `O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (100%) | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (98%) | `O=S(=O)([O-])[O-].` (0%) | set ✓ / any ✓ |

---

### Reaction #1584  yield=0.5%

**Source paper**: [`JCatal/10.1016_j.jcat.2025.116252_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JCatal/10.1016_j.jcat.2025.116252_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>C1OC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (79.0%) | `platinum` (12.7%) | `ABSENT` (7.4%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_generic` (77.8%) | `glassy_carbon` (16.7%) | `unknown_electrode` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (77.6%) | `ABSENT` (8.6%) | `stainless_steel` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (39.5%) | `platinum_plate` (28.5%) | `stainless_steel_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (73.7%) | `undivided` (26.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (52.9%) | `ABSENT` (19.7%) | `NBu4` (9.5%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (47.0%) | `ABSENT` (29.1%) | `PF6` (9.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (6.5%) | `alkali_sulfinate` (6.4%) | `alkali_hydroxide` (6.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (60.5%) | `ABSENT` (17.2%) | `Mn_complex` (6.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `aqueous` (36.1%) | `polar_aprotic_nitrile` (32.6%) | `polar_aprotic_sulfoxide` (15.7%) | ✓ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (96%) | `C[N+](=O)[O-]` (94%) | `O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (100%) | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (98%) | `O=S(=O)([O-])[O-].` (0%) | set ✓ / any ✓ |

---

### Reaction #1585  yield=75.0%

**Source paper**: [`JCatal/10.1016_j.jcat.2025.116252_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JCatal/10.1016_j.jcat.2025.116252_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>C1OC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (79.0%) | `platinum` (12.7%) | `ABSENT` (7.4%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_generic` (77.8%) | `glassy_carbon` (16.7%) | `unknown_electrode` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (77.6%) | `ABSENT` (8.6%) | `stainless_steel` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (39.5%) | `platinum_plate` (28.5%) | `stainless_steel_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (73.7%) | `undivided` (26.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (52.9%) | `ABSENT` (19.7%) | `NBu4` (9.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (47.0%) | `ABSENT` (29.1%) | `PF6` (9.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (6.5%) | `alkali_sulfinate` (6.4%) | `alkali_hydroxide` (6.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (60.5%) | `ABSENT` (17.2%) | `Mn_complex` (6.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `aqueous` (36.1%) | `polar_aprotic_nitrile` (32.6%) | `polar_aprotic_sulfoxide` (15.7%) | ✓ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (96%) | `C[N+](=O)[O-]` (94%) | `O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (100%) | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (98%) | `O=S(=O)([O-])[O-].` (0%) | set ✓ / any ✓ |

---

### Reaction #1586  yield=18.0%

**Source paper**: [`JCatal/10.1016_j.jcat.2025.116252_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JCatal/10.1016_j.jcat.2025.116252_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>C1OC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (79.0%) | `platinum` (12.7%) | `ABSENT` (7.4%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_generic` (77.8%) | `glassy_carbon` (16.7%) | `unknown_electrode` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (77.6%) | `ABSENT` (8.6%) | `stainless_steel` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (39.5%) | `platinum_plate` (28.5%) | `stainless_steel_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (73.7%) | `undivided` (26.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (52.9%) | `ABSENT` (19.7%) | `NBu4` (9.5%) | ✓ |
| 电解质 anion | 26 | `Cl` | `Br` (47.0%) | `ABSENT` (29.1%) | `PF6` (9.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (6.5%) | `alkali_sulfinate` (6.4%) | `alkali_hydroxide` (6.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (60.5%) | `ABSENT` (17.2%) | `Mn_complex` (6.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `aqueous` (36.1%) | `polar_aprotic_nitrile` (32.6%) | `polar_aprotic_sulfoxide` (15.7%) | ✓ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (96%) | `C[N+](=O)[O-]` (94%) | `O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (100%) | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (98%) | `O=S(=O)([O-])[O-].` (0%) | set ✓ / any ✓ |

---

### Reaction #1587  yield=79.0%

**Source paper**: [`JCatal/10.1016_j.jcat.2025.116252_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JCatal/10.1016_j.jcat.2025.116252_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>C1OC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (79.0%) | `platinum` (12.7%) | `ABSENT` (7.4%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_generic` (77.8%) | `glassy_carbon` (16.7%) | `unknown_electrode` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (77.6%) | `ABSENT` (8.6%) | `stainless_steel` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (39.5%) | `platinum_plate` (28.5%) | `stainless_steel_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (73.7%) | `undivided` (26.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (52.9%) | `ABSENT` (19.7%) | `NBu4` (9.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (47.0%) | `ABSENT` (29.1%) | `PF6` (9.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (6.5%) | `alkali_sulfinate` (6.4%) | `alkali_hydroxide` (6.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (60.5%) | `ABSENT` (17.2%) | `Mn_complex` (6.9%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `aqueous` (36.1%) | `polar_aprotic_nitrile` (32.6%) | `polar_aprotic_sulfoxide` (15.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (96%) | `C[N+](=O)[O-]` (94%) | `O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (100%) | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (98%) | `O=S(=O)([O-])[O-].` (0%) | set ✓ / any ✓ |

---

### Reaction #1588  yield=76.0%

**Source paper**: [`JCatal/10.1016_j.jcat.2025.116252_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JCatal/10.1016_j.jcat.2025.116252_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>C1OC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (79.0%) | `platinum` (12.7%) | `ABSENT` (7.4%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_generic` (77.8%) | `glassy_carbon` (16.7%) | `unknown_electrode` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (77.6%) | `ABSENT` (8.6%) | `stainless_steel` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (39.5%) | `platinum_plate` (28.5%) | `stainless_steel_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (73.7%) | `undivided` (26.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (52.9%) | `ABSENT` (19.7%) | `NBu4` (9.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (47.0%) | `ABSENT` (29.1%) | `PF6` (9.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (6.5%) | `alkali_sulfinate` (6.4%) | `alkali_hydroxide` (6.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (60.5%) | `ABSENT` (17.2%) | `Mn_complex` (6.9%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `aqueous` (36.1%) | `polar_aprotic_nitrile` (32.6%) | `polar_aprotic_sulfoxide` (15.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (96%) | `C[N+](=O)[O-]` (94%) | `O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (100%) | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (98%) | `O=S(=O)([O-])[O-].` (0%) | set ✓ / any ✓ |

---

### Reaction #1589  yield=0.0%

**Source paper**: [`JCatal/10.1016_j.jcat.2025.116252_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JCatal/10.1016_j.jcat.2025.116252_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>C1OC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (79.0%) | `platinum` (12.7%) | `ABSENT` (7.4%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_generic` (77.8%) | `glassy_carbon` (16.7%) | `unknown_electrode` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (77.6%) | `ABSENT` (8.6%) | `stainless_steel` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (39.5%) | `platinum_plate` (28.5%) | `stainless_steel_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (73.7%) | `undivided` (26.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (52.9%) | `ABSENT` (19.7%) | `NBu4` (9.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `Br` (47.0%) | `ABSENT` (29.1%) | `PF6` (9.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (6.5%) | `alkali_sulfinate` (6.4%) | `alkali_hydroxide` (6.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (60.5%) | `ABSENT` (17.2%) | `Mn_complex` (6.9%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `aqueous` (36.1%) | `polar_aprotic_nitrile` (32.6%) | `polar_aprotic_sulfoxide` (15.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (96%) | `C[N+](=O)[O-]` (94%) | `O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (100%) | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (98%) | `O=S(=O)([O-])[O-].` (0%) | set ✓ / any ✓ |

---

### Reaction #1590  yield=91.0%

**Source paper**: [`JCatal/10.1016_j.jcat.2025.116252_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JCatal/10.1016_j.jcat.2025.116252_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>C1OC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (79.0%) | `platinum` (12.7%) | `ABSENT` (7.4%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_generic` (77.8%) | `glassy_carbon` (16.7%) | `unknown_electrode` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (77.6%) | `ABSENT` (8.6%) | `stainless_steel` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (39.5%) | `platinum_plate` (28.5%) | `stainless_steel_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (73.7%) | `undivided` (26.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (52.9%) | `ABSENT` (19.7%) | `NBu4` (9.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (47.0%) | `ABSENT` (29.1%) | `PF6` (9.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (6.5%) | `alkali_sulfinate` (6.4%) | `alkali_hydroxide` (6.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (60.5%) | `ABSENT` (17.2%) | `Mn_complex` (6.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `aqueous` (36.1%) | `polar_aprotic_nitrile` (32.6%) | `polar_aprotic_sulfoxide` (15.7%) | ✓ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (96%) | `C[N+](=O)[O-]` (94%) | `O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (100%) | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (98%) | `O=S(=O)([O-])[O-].` (0%) | set ✓ / any ✓ |

---

### Reaction #1591  yield=0.0%

**Source paper**: [`JCatal/10.1016_j.jcat.2025.116252_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JCatal/10.1016_j.jcat.2025.116252_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>C1OC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (79.0%) | `platinum` (12.7%) | `ABSENT` (7.4%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_generic` (77.8%) | `glassy_carbon` (16.7%) | `unknown_electrode` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (77.6%) | `ABSENT` (8.6%) | `stainless_steel` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (39.5%) | `platinum_plate` (28.5%) | `stainless_steel_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (73.7%) | `undivided` (26.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (52.9%) | `ABSENT` (19.7%) | `NBu4` (9.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (47.0%) | `ABSENT` (29.1%) | `PF6` (9.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (6.5%) | `alkali_sulfinate` (6.4%) | `alkali_hydroxide` (6.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (60.5%) | `ABSENT` (17.2%) | `Mn_complex` (6.9%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `aqueous` (36.1%) | `polar_aprotic_nitrile` (32.6%) | `polar_aprotic_sulfoxide` (15.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (96%) | `C[N+](=O)[O-]` (94%) | `O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (100%) | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (98%) | `O=S(=O)([O-])[O-].` (0%) | set ✓ / any ✓ |

---

### Reaction #1592  yield=56.0%

**Source paper**: [`JCatal/10.1016_j.jcat.2025.116252_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JCatal/10.1016_j.jcat.2025.116252_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>C1OC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (79.0%) | `platinum` (12.7%) | `ABSENT` (7.4%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_generic` (77.8%) | `glassy_carbon` (16.7%) | `unknown_electrode` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (77.6%) | `ABSENT` (8.6%) | `stainless_steel` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (39.5%) | `platinum_plate` (28.5%) | `stainless_steel_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (73.7%) | `undivided` (26.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (52.9%) | `ABSENT` (19.7%) | `NBu4` (9.5%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (47.0%) | `ABSENT` (29.1%) | `PF6` (9.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (6.5%) | `alkali_sulfinate` (6.4%) | `alkali_hydroxide` (6.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (60.5%) | `ABSENT` (17.2%) | `Mn_complex` (6.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `aqueous` (36.1%) | `polar_aprotic_nitrile` (32.6%) | `polar_aprotic_sulfoxide` (15.7%) | ✓ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (96%) | `C[N+](=O)[O-]` (94%) | `O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (100%) | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (98%) | `O=S(=O)([O-])[O-].` (0%) | set ✓ / any ✓ |

---

### Reaction #1593  yield=80.0%

**Source paper**: [`JCatal/10.1016_j.jcat.2025.116252_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JCatal/10.1016_j.jcat.2025.116252_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>C1OC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (79.0%) | `platinum` (12.7%) | `ABSENT` (7.4%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_generic` (77.8%) | `glassy_carbon` (16.7%) | `unknown_electrode` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (77.6%) | `ABSENT` (8.6%) | `stainless_steel` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (39.5%) | `platinum_plate` (28.5%) | `stainless_steel_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (73.7%) | `undivided` (26.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (52.9%) | `ABSENT` (19.7%) | `NBu4` (9.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (47.0%) | `ABSENT` (29.1%) | `PF6` (9.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (6.5%) | `alkali_sulfinate` (6.4%) | `alkali_hydroxide` (6.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (60.5%) | `ABSENT` (17.2%) | `Mn_complex` (6.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `aqueous` (36.1%) | `polar_aprotic_nitrile` (32.6%) | `polar_aprotic_sulfoxide` (15.7%) | ✓ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (96%) | `C[N+](=O)[O-]` (94%) | `O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (100%) | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (98%) | `O=S(=O)([O-])[O-].` (0%) | set ✓ / any ✓ |

---

### Reaction #1594  yield=0.5%

**Source paper**: [`JCatal/10.1016_j.jcat.2025.116252_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JCatal/10.1016_j.jcat.2025.116252_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>C1OC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (79.0%) | `platinum` (12.7%) | `ABSENT` (7.4%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_generic` (77.8%) | `glassy_carbon` (16.7%) | `unknown_electrode` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (77.6%) | `ABSENT` (8.6%) | `stainless_steel` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_generic` (39.5%) | `platinum_plate` (28.5%) | `stainless_steel_generic` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (73.7%) | `undivided` (26.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (52.9%) | `ABSENT` (19.7%) | `NBu4` (9.5%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Br` (47.0%) | `ABSENT` (29.1%) | `PF6` (9.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (6.5%) | `alkali_sulfinate` (6.4%) | `alkali_hydroxide` (6.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (60.5%) | `ABSENT` (17.2%) | `Mn_complex` (6.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `aqueous` (36.1%) | `polar_aprotic_nitrile` (32.6%) | `polar_aprotic_sulfoxide` (15.7%) | ✓ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (96%) | `C[N+](=O)[O-]` (94%) | `O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (100%) | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (98%) | `O=S(=O)([O-])[O-].` (0%) | set ✓ / any ✓ |

---

### Reaction #1595  yield=19.0%

**Source paper**: [`JCatal/2025_Journal_of_Catalysis_2025_450116252.json`](reactions_by_journal_alkene_ec_audited/JCatal/2025_Journal_of_Catalysis_2025_450116252.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc2ccccc2c1>>c1ccc2cc(C3CO3)ccc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `silver` | `carbon` (93.9%) | `platinum` (5.8%) | `ABSENT` (0.2%) | ✗ |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_generic` (76.1%) | `graphite_rod` (15.1%) | `carbon_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `silver` | `platinum` (99.5%) | `carbon` (0.2%) | `stainless_steel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `silver_generic` | `platinum_plate` (86.1%) | `platinum_generic` (12.6%) | `platinum_wire` (0.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.7%) | `ABSENT` (1.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `ABSENT` (57.8%) | `NBu4` (34.0%) | `Li` (6.0%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (52.4%) | `PF6` (36.5%) | `BF4` (6.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_sulfinate` (17.4%) | `alkali_other_salt` (12.0%) | `bromide_anion` (11.7%) | ✗ |
| 催化剂大类 | 49 | `Ni_complex` | `pyridine_organocat` (90.4%) | `ABSENT` (6.6%) | `brønsted_acid_cat` (1.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.0%) | `polar_aprotic_sulfoxide` (6.2%) | `polar_aprotic_amide` (5.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `[H+].[OH-]` | `CC#N` (88%) | `CCOCC` (36%) | `O` (30%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `__OTHER__` (100%) | `CC[Si](CC)CC` (100%) | `O=O` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `O.O.[K+].[K+].[O]=` + `CC[C@H]1CN2CC[C@H]` | `c1ccncc1` (98%) | `__OTHER__` (42%) | `O.O.[K+].[K+].[O]=` (16%) | set ✗ / any ✓ |

---

### Reaction #1596  yield=83.0%

**Source paper**: [`GreenChem/2024_Green_Chemistry_2024_26_5_2922-2927.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2024_Green_Chemistry_2024_26_5_2922-2927.json) (反应 idx 在该 JSON 内 = #6)

```
C=Cc1ccc(Br)cc1>>Brc1ccc(C2CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (75.9%) | `platinum` (23.0%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (90.2%) | `boron_doped_diamond` (3.3%) | `graphite_rod` (2.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.2%) | `carbon` (0.5%) | `ABSENT` (0.2%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (50.9%) | `platinum_wire` (32.2%) | `platinum_generic` (15.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NBu4` (61.3%) | `ABSENT` (23.6%) | `Li` (5.7%) | ✗ |
| 电解质 anion | 26 | `Br` | `PF6` (34.8%) | `ABSENT` (29.2%) | `BF4` (17.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (15.1%) | `alkali_sulfinate` (13.3%) | `bromide_anion` (7.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (94.3%) | `ABSENT` (4.0%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (85.8%) | `aqueous` (4.0%) | `ABSENT` (3.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (98%) | `O` (88%) | `CCOCC` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (93%) | `__OTHER__` (86%) | `CC[Si](CC)CC` (73%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Pt]` | `c1ccncc1` (99%) | `__OTHER__` (83%) | `O=S(=O)(O)C(F)(F)F` (1%) | set ✗ / any ✗ |

---

### Reaction #1597  yield=93.0%

**Source paper**: [`JCatal/2025_Journal_of_Catalysis_2025_450116252.json`](reactions_by_journal_alkene_ec_audited/JCatal/2025_Journal_of_Catalysis_2025_450116252.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1cccc(C)c1>>Cc1cccc(C2CO2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `nickel` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✗ |
| 阳极 (细类) | 43 | `nickel_generic` | `graphite_rod` (57.1%) | `carbon_generic` (26.8%) | `glassy_carbon` (11.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.9%) | `carbon` (0.1%) | `ABSENT` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (91.8%) | `platinum_generic` (8.0%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NBu4` (44.8%) | `ABSENT` (23.8%) | `K` (22.7%) | ✗ |
| 电解质 anion | 26 | `Br` | `PF6` (38.6%) | `ABSENT` (31.5%) | `Br` (15.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (40.9%) | `alkali_sulfinate` (7.3%) | `bromide_anion` (4.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (99.3%) | `ABSENT` (0.5%) | `triarylamine_radical_cat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.5%) | `ABSENT` (0.9%) | `polar_aprotic_sulfoxide` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `CC#N` (84%) | `CCOCC` (67%) | `FC(F)(F)c1ccccc1` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (97%) | `__OTHER__` (93%) | `OB(O)B(O)O` (79%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (100%) | `__OTHER__` (95%) | `O=S(=O)(O)C(F)(F)F` (2%) | set ✗ / any ✗ |

---

### Reaction #1598  yield=37.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1599  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✓ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1600  yield=19.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1601  yield=78.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1602  yield=66.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1603  yield=74.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1604  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1605  yield=63.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1606  yield=39.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1607  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✓ |
| 电解质 anion | 26 | `Br` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✓ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1608  yield=68.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1609  yield=47.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1610  yield=2.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✓ |
| 电解质 anion | 26 | `Br` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✓ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1611  yield=61.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1612  yield=63.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1613  yield=78.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1614  yield=2.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00049_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)N2CC(=C(Br)c3ccccc3)C(C)(CBr)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (85.3%) | `platinum` (14.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `carbon_felt` (62.1%) | `platinum_plate` (15.1%) | `reticulated_vitreous_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (89.5%) | `carbon` (10.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.3%) | `graphite_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `H` (37.8%) | `Li` (36.5%) | `NBu4` (21.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `ClO4` (41.0%) | `BF4` (31.0%) | `carboxylate` (13.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (24.9%) | `o2_oxidant` (3.2%) | `ABSENT` (2.7%) | ✓ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `pyridine_organocat` (48.7%) | `ABSENT` (30.1%) | `organic_neutral_cat` (16.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (51.3%) | `polar_aprotic_nitrile` (44.5%) | `hfip` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `O` (83%) | `OC(C(F)(F)F)C(F)(F` (57%) | `ClCCl` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I(Cl)Cl)cc1` + `Cc1cc(C(C)(C)C)c(O` + `CC[NH+](CC)CC.[Cl-` | `O=S([O-])([O-])=S.` (61%) | `O=C(O)O.[Na]` (22%) | `CCN(CC)CC` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `c1ccc(-c2ccccn2)nc` (4%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1615  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C)CC(c2ccccc2)(c2ccccc2)OC1=O.COC(=O)C(C)(CC(OC)(c1ccccc1)c1ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `glassy_carbon` (43.7%) | `reticulated_vitreous_carbon` (19.2%) | `carbon_felt` (16.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `ABSENT` (0.1%) | `carbon` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (77.5%) | `platinum_generic` (22.2%) | `ABSENT` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.6%) | `Na` (0.2%) | `K` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (97.9%) | `PF6` (1.1%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `ABSENT` (4.2%) | `carboxylic_acid` (3.8%) | `tetraaryl_borate` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ferrocene_mediator` (63.4%) | `Fe_complex` (21.5%) | `ABSENT` (8.8%) | ✓ |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_protic_alcohol` (99.6%) | `polar_aprotic_nitrile` (0.2%) | `cyclic_ether` (0.1%) | ✓ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (100%) | `C1CCOC1` (26%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=C([O-])[O-].[Na+` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `O=S(=O)([O-])C(F)(` | `[cH]12->[Fe+2]3456` (49%) | `[Fe+2].c1cc[cH-]c1` (25%) | `__OTHER__` (3%) | set ✗ / any ✓ |

---

### Reaction #1616  yield=46.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C)CC(c2ccccc2)(c2ccccc2)OC1=O.COC(=O)C(C)(CC(OC)(c1ccccc1)c1ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `glassy_carbon` (43.7%) | `reticulated_vitreous_carbon` (19.2%) | `carbon_felt` (16.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `ABSENT` (0.1%) | `carbon` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (77.5%) | `platinum_generic` (22.2%) | `ABSENT` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.6%) | `Na` (0.2%) | `K` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (97.9%) | `PF6` (1.1%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (4.2%) | `carboxylic_acid` (3.8%) | `tetraaryl_borate` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (63.4%) | `Fe_complex` (21.5%) | `ABSENT` (8.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (99.6%) | `polar_aprotic_nitrile` (0.2%) | `cyclic_ether` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (100%) | `C1CCOC1` (26%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=C([O-])[O-].[Na+` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `O=S(=O)([O-])C(F)(` | `[cH]12->[Fe+2]3456` (49%) | `[Fe+2].c1cc[cH-]c1` (25%) | `__OTHER__` (3%) | set ✗ / any ✓ |

---

### Reaction #1617  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C)CC(c2ccccc2)(c2ccccc2)OC1=O.COC(=O)C(C)(CC(OC)(c1ccccc1)c1ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `glassy_carbon` (43.7%) | `reticulated_vitreous_carbon` (19.2%) | `carbon_felt` (16.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `ABSENT` (0.1%) | `carbon` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (77.5%) | `platinum_generic` (22.2%) | `ABSENT` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.6%) | `Na` (0.2%) | `K` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (97.9%) | `PF6` (1.1%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `ABSENT` (4.2%) | `carboxylic_acid` (3.8%) | `tetraaryl_borate` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (63.4%) | `Fe_complex` (21.5%) | `ABSENT` (8.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_protic_alcohol` (99.6%) | `polar_aprotic_nitrile` (0.2%) | `cyclic_ether` (0.1%) | ✓ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (100%) | `C1CCOC1` (26%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=C([O-])[O-].[Na+` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `O=S(=O)([O-])C(F)(` | `[cH]12->[Fe+2]3456` (49%) | `[Fe+2].c1cc[cH-]c1` (25%) | `__OTHER__` (3%) | set ✗ / any ✓ |

---

### Reaction #1618  yield=76.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C)CC(c2ccccc2)(c2ccccc2)OC1=O.COC(=O)C(C)(CC(OC)(c1ccccc1)c1ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `glassy_carbon` (43.7%) | `reticulated_vitreous_carbon` (19.2%) | `carbon_felt` (16.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `ABSENT` (0.1%) | `carbon` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (77.5%) | `platinum_generic` (22.2%) | `ABSENT` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.6%) | `Na` (0.2%) | `K` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (97.9%) | `PF6` (1.1%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (4.2%) | `carboxylic_acid` (3.8%) | `tetraaryl_borate` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (63.4%) | `Fe_complex` (21.5%) | `ABSENT` (8.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_protic_alcohol` (99.6%) | `polar_aprotic_nitrile` (0.2%) | `cyclic_ether` (0.1%) | ✓ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (100%) | `C1CCOC1` (26%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=C([O-])[O-].[Na+` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `O=S(=O)([O-])C(F)(` | `[cH]12->[Fe+2]3456` (49%) | `[Fe+2].c1cc[cH-]c1` (25%) | `__OTHER__` (3%) | set ✗ / any ✓ |

---

### Reaction #1619  yield=56.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C)CC(c2ccccc2)(c2ccccc2)OC1=O.COC(=O)C(C)(CC(OC)(c1ccccc1)c1ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `glassy_carbon` (43.7%) | `reticulated_vitreous_carbon` (19.2%) | `carbon_felt` (16.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `ABSENT` (0.1%) | `carbon` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (77.5%) | `platinum_generic` (22.2%) | `ABSENT` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.6%) | `Na` (0.2%) | `K` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (97.9%) | `PF6` (1.1%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (4.2%) | `carboxylic_acid` (3.8%) | `tetraaryl_borate` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (63.4%) | `Fe_complex` (21.5%) | `ABSENT` (8.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (99.6%) | `polar_aprotic_nitrile` (0.2%) | `cyclic_ether` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (100%) | `C1CCOC1` (26%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=C([O-])[O-].[Na+` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `O=S(=O)([O-])C(F)(` | `[cH]12->[Fe+2]3456` (49%) | `[Fe+2].c1cc[cH-]c1` (25%) | `__OTHER__` (3%) | set ✗ / any ✓ |

---

### Reaction #1620  yield=69.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C)CC(c2ccccc2)(c2ccccc2)OC1=O.COC(=O)C(C)(CC(OC)(c1ccccc1)c1ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `glassy_carbon` (43.7%) | `reticulated_vitreous_carbon` (19.2%) | `carbon_felt` (16.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `ABSENT` (0.1%) | `carbon` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (77.5%) | `platinum_generic` (22.2%) | `ABSENT` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.6%) | `Na` (0.2%) | `K` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (97.9%) | `PF6` (1.1%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (4.2%) | `carboxylic_acid` (3.8%) | `tetraaryl_borate` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (63.4%) | `Fe_complex` (21.5%) | `ABSENT` (8.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_protic_alcohol` (99.6%) | `polar_aprotic_nitrile` (0.2%) | `cyclic_ether` (0.1%) | ✓ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (100%) | `C1CCOC1` (26%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=C([O-])[O-].[Na+` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `O=S(=O)([O-])C(F)(` | `[cH]12->[Fe+2]3456` (49%) | `[Fe+2].c1cc[cH-]c1` (25%) | `__OTHER__` (3%) | set ✗ / any ✓ |

---

### Reaction #1621  yield=64.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C)CC(c2ccccc2)(c2ccccc2)OC1=O.COC(=O)C(C)(CC(OC)(c1ccccc1)c1ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `glassy_carbon` (43.7%) | `reticulated_vitreous_carbon` (19.2%) | `carbon_felt` (16.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `ABSENT` (0.1%) | `carbon` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (77.5%) | `platinum_generic` (22.2%) | `ABSENT` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.6%) | `Na` (0.2%) | `K` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (97.9%) | `PF6` (1.1%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (4.2%) | `carboxylic_acid` (3.8%) | `tetraaryl_borate` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (63.4%) | `Fe_complex` (21.5%) | `ABSENT` (8.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_protic_alcohol` (99.6%) | `polar_aprotic_nitrile` (0.2%) | `cyclic_ether` (0.1%) | ✓ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (100%) | `C1CCOC1` (26%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=C([O-])[O-].[Na+` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `O=S(=O)([O-])C(F)(` | `[cH]12->[Fe+2]3456` (49%) | `[Fe+2].c1cc[cH-]c1` (25%) | `__OTHER__` (3%) | set ✗ / any ✓ |

---

### Reaction #1622  yield=61.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00228_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C)CC(c2ccccc2)(c2ccccc2)OC1=O.COC(=O)C(C)(CC(OC)(c1ccccc1)c1ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `glassy_carbon` (43.7%) | `reticulated_vitreous_carbon` (19.2%) | `carbon_felt` (16.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `ABSENT` (0.1%) | `carbon` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (77.5%) | `platinum_generic` (22.2%) | `ABSENT` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.6%) | `Na` (0.2%) | `K` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (97.9%) | `PF6` (1.1%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (4.2%) | `carboxylic_acid` (3.8%) | `tetraaryl_borate` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (63.4%) | `Fe_complex` (21.5%) | `ABSENT` (8.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_protic_alcohol` (99.6%) | `polar_aprotic_nitrile` (0.2%) | `cyclic_ether` (0.1%) | ✓ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (100%) | `C1CCOC1` (26%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=C([O-])[O-].[Na+` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `O=S(=O)([O-])C(F)(` | `[cH]12->[Fe+2]3456` (49%) | `[Fe+2].c1cc[cH-]c1` (25%) | `__OTHER__` (3%) | set ✗ / any ✓ |

---

### Reaction #1623  yield=60.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1624  yield=30.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1625  yield=9.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1626  yield=80.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1627  yield=25.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1628  yield=72.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1629  yield=14.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1630  yield=78.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `PF6` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1631  yield=70.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1632  yield=66.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1633  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1634  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1635  yield=39.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1636  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1637  yield=68.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1638  yield=74.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00401_p3_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00401_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F.C[Si](C)(C)N=[N+]=[N-]>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (74.9%) | `reticulated_vitreous_carbon` (12.0%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (82.3%) | `ABSENT` (17.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (52.7%) | `NBu4` (44.4%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (68.7%) | `I` (15.9%) | `BF4` (8.6%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (99.7%) | `ketone` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (97%) | `CCCCO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1639  yield=15.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1640  yield=71.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1641  yield=82.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1642  yield=80.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1643  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1644  yield=8.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #5)

```
C=Cc1ccc(-c2ccccc2)cc1.Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_generic` (87.5%) | `graphite_rod` (11.9%) | `carbon_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `stainless_steel` (46.7%) | `carbon` (36.4%) | `platinum` (14.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `stainless_steel_generic` (61.3%) | `platinum_plate` (15.7%) | `graphite_generic` (9.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (77.6%) | `ABSENT` (22.2%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (45.5%) | `NBu4` (28.4%) | `ABSENT` (14.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `I` (43.1%) | `Cl` (31.9%) | `ABSENT` (6.9%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (27.4%) | `transition_metal_salt_reagent` (10.5%) | `ABSENT` (2.9%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (64.0%) | `ABSENT` (25.4%) | `Mn_complex` (5.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.4%) | `ABSENT` (0.5%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (45%) | `O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Fc1c(F)c(F)c(B(c2c` + `[Br-].[Li+]` + `O=[N+]([O-])[O-].[` + `__OTHER__` | `O=O` (99%) | `__OTHER__` (91%) | `OB(O)B(O)O` (64%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Co+2]` | `[Cl-].[Cl-].[Co+2]` (78%) | `c1ccncc1` (10%) | `[Cl][Co][Cl]` (2%) | set ✓ / any ✓ |

---

### Reaction #1645  yield=81.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1646  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1647  yield=35.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1648  yield=75.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1649  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1650  yield=8.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1651  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1652  yield=40.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1653  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1654  yield=78.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1655  yield=71.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1656  yield=65.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1657  yield=79.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1658  yield=77.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1659  yield=77.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1660  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c00510_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c00510_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.O=N[O-].[Na+].Cn1ccc2ccccc21>>Cn1cc(C(C[N+](=O)[O-])c2ccc(-c3ccccc3)cc2)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (65.7%) | `graphite_generic` (31.2%) | `graphite_plate` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (54.3%) | `platinum` (24.0%) | `stainless_steel` (10.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `platinum_plate` (27.5%) | `platinum_generic` (23.7%) | `stainless_steel_generic` (8.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.2%) | `ABSENT` (17.5%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (58.4%) | `NBu4` (20.1%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `OTf` | `Cl` (42.1%) | `I` (35.6%) | `molecular_no_ion` (8.3%) | ✗ |
| 试剂大类 | 103 | `alkali_nitrate` | `alkali_sulfonate` (10.5%) | `ABSENT` (8.0%) | `chloride_anion` (6.3%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (61.8%) | `ABSENT` (15.9%) | `Mn_complex` (10.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `ABSENT` (0.4%) | `ester` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (15%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=[N+]([O-])[O-].[` + `Fc1c(F)c(F)c(B(c2c` | `O=O` (69%) | `O=S(=O)([O-])C(F)(` (51%) | `Fc1c(F)c(F)c(B(c2c` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `[Cl-].[Cl-].[Co+2]` (50%) | `[Cl][Co][Cl]` (2%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1661  yield=2.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1662  yield=2.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1663  yield=2.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1664  yield=15.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1665  yield=2.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1666  yield=2.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `copper` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1667  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1668  yield=35.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1669  yield=2.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1670  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #9)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccccc1C2CC#N
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (96.6%) | `carbon` (2.6%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (52.7%) | `platinum_generic` (42.1%) | `graphite_generic` (2.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `stainless_steel` (3.6%) | `ABSENT` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_disk` (64.5%) | `platinum_generic` (34.0%) | `ABSENT` (0.6%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (58.2%) | `undivided` (40.9%) | `divided` (0.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (66.0%) | `NBu4` (32.2%) | `Na` (0.9%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (66.1%) | `carboxylate` (9.0%) | `PF6` (6.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (20.9%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.2%) | `organic_neutral_cat` (1.3%) | `ammonium_PTC_organocat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (94.3%) | `polar_aprotic_amide` (3.2%) | `halogenated_aliphatic` (1.2%) | ✓ |
| 溶剂 set | 79 | `N#CCCl` | `CO` (97%) | `O` (92%) | `ClCCCl` (65%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[NH4+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1671  yield=45.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1672  yield=70.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1673  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1674  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1675  yield=62.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1676  yield=52.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1677  yield=41.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1678  yield=10.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1679  yield=44.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1680  yield=76.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1681  yield=34.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1682  yield=76.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1683  yield=2.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `copper` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1684  yield=2.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1685  yield=2.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1686  yield=2.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1687  yield=2.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1688  yield=48.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1689  yield=54.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1690  yield=76.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1691  yield=75.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1692  yield=68.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1693  yield=75.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1694  yield=42.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1695  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #9)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccccc1C2CC#N
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (96.6%) | `carbon` (2.6%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (52.7%) | `platinum_generic` (42.1%) | `graphite_generic` (2.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `stainless_steel` (3.6%) | `ABSENT` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_disk` (64.5%) | `platinum_generic` (34.0%) | `ABSENT` (0.6%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (58.2%) | `undivided` (40.9%) | `divided` (0.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (66.0%) | `NBu4` (32.2%) | `Na` (0.9%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (66.1%) | `carboxylate` (9.0%) | `PF6` (6.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (20.9%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.2%) | `organic_neutral_cat` (1.3%) | `ammonium_PTC_organocat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (94.3%) | `polar_aprotic_amide` (3.2%) | `halogenated_aliphatic` (1.2%) | ✓ |
| 溶剂 set | 79 | `N#CCCl` | `CO` (97%) | `O` (92%) | `ClCCCl` (65%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[NH4+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1696  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1697  yield=15.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1698  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1699  yield=52.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1700  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1701  yield=2.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1702  yield=45.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1703  yield=44.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1704  yield=76.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1705  yield=34.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1706  yield=41.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1707  yield=35.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1708  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1709  yield=70.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1710  yield=62.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1711  yield=76.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01037_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01037_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(C)(C)C1=CC(=Cc2ccccc2C#Cc2ccccc2)C=C(C(C)(C)C)C1=O.N#CCCl>>CC(C)(C)C1=CC2(C=C(C(C)(C)C)C1=O)C(=C(Cl)c1ccccc1)c1ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_disk` (72.1%) | `platinum_generic` (19.3%) | `platinum_plate` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `stainless_steel` (0.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.5%) | `platinum_disk` (42.6%) | `platinum_plate` (3.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (49.6%) | `ABSENT` (49.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (66.9%) | `NBu4` (31.5%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (69.7%) | `carboxylate` (11.1%) | `Br` (5.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `organic_neutral_cat` (2.8%) | `ionic_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (89.9%) | `polar_aprotic_nitrile` (6.3%) | `polar_aprotic_amide` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CO` (79%) | `ClCCCl` (77%) | `O` (22%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1712  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1713  yield=28.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1714  yield=48.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1715  yield=54.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1716  yield=51.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1717  yield=52.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1718  yield=71.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1719  yield=59.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1720  yield=66.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1721  yield=44.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1722  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1723  yield=70.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1724  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1725  yield=74.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1726  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1727  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1728  yield=24.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1729  yield=28.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1730  yield=28.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1731  yield=40.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1732  yield=34.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1733  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1734  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1735  yield=54.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1736  yield=23.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1737  yield=48.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1738  yield=35.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1739  yield=2.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1740  yield=28.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `hfip` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1741  yield=32.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1.O=C1C(CC(F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `graphite_generic` (2.5%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.8%) | `carbon` (3.5%) | `nickel` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (83.8%) | `platinum_generic` (15.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (2.6%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.4%) | `ClO4` (16.0%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `alkali_phosphate` (6.3%) | `alkali_bicarbonate` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `halogenated_aliphatic` (56.4%) | `polar_aprotic_nitrile` (39.5%) | `ketone` (3.1%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (98%) | `CC#N` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (91%) | `CC(=O)[O-].[Na+]` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccc(-c2ccccn2)nc` (0%) | set ✓ / any ✓ |

---

### Reaction #1742  yield=51.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1743  yield=20.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1744  yield=47.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1745  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1746  yield=17.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1747  yield=52.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1748  yield=32.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1749  yield=48.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1750  yield=60.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1751  yield=65.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_zinc` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1752  yield=59.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1753  yield=59.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1754  yield=66.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1755  yield=74.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1756  yield=71.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1757  yield=16.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1758  yield=44.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1759  yield=52.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1760  yield=52.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1761  yield=59.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1762  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1763  yield=5.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1764  yield=74.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1765  yield=44.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1766  yield=74.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1767  yield=75.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1768  yield=68.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1769  yield=75.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1770  yield=74.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1771  yield=70.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1772  yield=53.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1773  yield=69.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01733_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCN(C#N)C(=O)C(c1ccccc1)c1ccccc1.O=S([O-])C(F)(F)F.[Na+]>>O=C1N2CCC(CC(F)(F)F)C2=NC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_rod` (99.1%) | `carbon_generic` (0.3%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (96.4%) | `carbon` (1.6%) | `nickel` (1.5%) | ✗ |
| 阴极 (细类) | 49 | `iron_generic` | `platinum_plate` (96.7%) | `platinum_generic` (3.2%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `NEt4` (1.3%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (96.1%) | `PF6` (1.2%) | `Br` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `alkali_bicarbonate` (3.5%) | `alkali_carbonate` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (94.9%) | `polar_aprotic_nitrile` (3.7%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `O` (100%) | `ClCCl` (99%) | `CC(=O)O` (34%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Na+]` | `__ABSENT__` (86%) | `CC(=O)[O-].[Na+]` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1774  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1775  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1776  yield=38.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1777  yield=9.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1778  yield=5.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1779  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `aromatic_hydrocarbon` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1780  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1781  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `transition_metal_salt_reagent` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1782  yield=73.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1783  yield=43.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1784  yield=42.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1785  yield=65.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1786  yield=33.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1787  yield=27.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1788  yield=59.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1789  yield=46.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1790  yield=51.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1791  yield=64.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1792  yield=70.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1793  yield=57.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1794  yield=60.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1795  yield=64.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1796  yield=55.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1797  yield=47.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1798  yield=41.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1799  yield=61.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1800  yield=48.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1801  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1802  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1803  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1804  yield=5.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1805  yield=9.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1806  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `aromatic_hydrocarbon` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1807  yield=51.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1808  yield=65.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1809  yield=42.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1810  yield=33.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1811  yield=38.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1812  yield=46.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1813  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1814  yield=45.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1815  yield=63.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1816  yield=59.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1817  yield=65.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1818  yield=47.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1819  yield=31.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1820  yield=56.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1821  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Cu_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1822  yield=62.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1823  yield=27.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1824  yield=0.5%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1825  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Cu_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1826  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1827  yield=62.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1828  yield=45.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✓ |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1829  yield=38.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `K` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1830  yield=64.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1831  yield=34.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1832  yield=57.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1833  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1834  yield=46.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1835  yield=43.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1836  yield=32.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1837  yield=41.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1838  yield=25.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1839  yield=23.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1840  yield=37.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1841  yield=45.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1842  yield=64.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1843  yield=0.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1844  yield=44.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1845  yield=47.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `chloride_anion` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1846  yield=70.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1847  yield=73.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1848  yield=55.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1849  yield=70.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1850  yield=32.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `copper` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1851  yield=78.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1852  yield=29.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `lead` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1853  yield=68.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1854  yield=74.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1855  yield=35.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `copper` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1856  yield=56.0%

**Source paper**: [`JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json`](reactions_by_journal_alkene_ec_audited/JOC/10.1021_acs.joc.5c01984_sup_1_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1.COc1ccc(S)cc1.FC(F)(F)C(F)(F)C(F)(F)C(F)(F)I>>FC(F)(F)C(F)(F)C(F)(F)C(F)(F)CC(Sc1ccc(OC)cc1)c1…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (65.0%) | `sacrificial_zinc` (24.6%) | `carbon` (3.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_generic` (63.3%) | `zinc_generic` (23.7%) | `platinum_rod` (4.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.2%) | `carbon` (1.8%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.3%) | `platinum_wire` (0.2%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (98.2%) | `undivided` (1.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.9%) | `ABSENT` (33.0%) | `NEt4` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (44.5%) | `ABSENT` (25.3%) | `Cl` (23.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (21.2%) | `boron_lewis_acid` (4.7%) | `hf_amine_complex` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `Ni_complex` (91.9%) | `ABSENT` (6.8%) | `Fe_complex` (0.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (89.6%) | `polar_aprotic_nitrile` (4.1%) | `polar_aprotic_sulfoxide` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `O` | `CN(C)C=O` (98%) | `O` (19%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CN(C)CCN(C)C` + `[Cl-].[Cl-].[Fe+2]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Fe][Cl]` | `[Ni]` (29%) | `Br[Ni](Br)(n1ccccc` (16%) | `[Br][Ni][Br].c1cc(` (1%) | set ✗ / any ✗ |

---

### Reaction #1857  yield=10.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #0)

```
CO.C=C(C)c1ccccc1.COC(=O)C(C)C(=O)OC>>COC(=O)[C@@]1(C)C[C@@](C)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.2%) | `platinum` (3.5%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (76.1%) | `reticulated_vitreous_carbon` (11.1%) | `graphite_rod` (5.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (95.4%) | `nickel` (3.1%) | `carbon` (1.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.8%) | `graphite_generic` (0.3%) | `platinum_generic` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.2%) | `ABSENT` (2.4%) | `NEt4` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (76.4%) | `PF6` (6.7%) | `ABSENT` (6.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_other_salt` | `o2_oxidant` (14.2%) | `ABSENT` (3.7%) | `as_solvent_polar_aprotic_nitri` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `triarylamine_radical_cat` (69.1%) | `ABSENT` (16.3%) | `ammonium_PTC_organocat` (3.4%) | ✗ |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (49.3%) | `ABSENT` (46.3%) | `polar_aprotic_amide` (2.3%) | ✗ |
| 溶剂 set | 79 | `C1CCOC1` + `O` | `CC#N` (88%) | `CO` (9%) | `__ABSENT__` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `Cl` | `O=O` (30%) | `__ABSENT__` (1%) | `C[Si](C)(C)N=[N+]=` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `Brc1ccc(N(c2ccc(Br` (23%) | `__ABSENT__` (18%) | `Brc1ccc(N(c2ccc(Br` (16%) | set ✗ / any ✗ |

---

### Reaction #1858  yield=15.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #1)

```
CO.COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1cccnc1>>COC(=O)[C@@]1(C)C[C@](c2ccccc2)(c2cccnc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (88.3%) | `graphite_generic` (7.5%) | `carbon_felt` (3.8%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `nickel` (0.3%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (65.5%) | `NBu4` (32.3%) | `Na` (1.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.4%) | `BF4` (16.7%) | `PF6` (3.2%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (6.7%) | `o2_oxidant` (4.7%) | `as_solvent_polar_aprotic_nitri` (3.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `triarylamine_radical_cat` (60.4%) | `ABSENT` (38.7%) | `pyridine_organocat` (0.2%) | ✗ |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (75.7%) | `ABSENT` (23.5%) | `polar_protic_alcohol` (0.3%) | ✗ |
| 溶剂 set | 79 | `C1CCOC1` + `O` | `CC#N` (70%) | `CO` (0%) | `__ABSENT__` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CC(C)C(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (53%) | `Brc1ccc(N(c2ccc(Br` (29%) | `[Cl][Mn][Cl]` (5%) | set ✗ / any ✗ |

---

### Reaction #1859  yield=15.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #2)

```
CO.COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1cccnc1>>COC(=O)C(C)(CC(OC)(c1ccccc1)c1cccnc1)C(=O)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (90.3%) | `graphite_generic` (5.3%) | `carbon_felt` (3.0%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.9%) | `nickel` (0.1%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (82.4%) | `ABSENT` (15.8%) | `Na` (0.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `I` (29.1%) | `ABSENT` (28.4%) | `OH` (19.4%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (4.9%) | `tetraaryl_borate` (2.8%) | `as_solvent_halogenated_aliphat` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.4%) | `ferrocene_mediator` (0.7%) | `triarylamine_radical_cat` (0.3%) | ✓ |
| 溶剂大类 | 27 | `cyclic_ether` | `ABSENT` (68.9%) | `polar_aprotic_nitrile` (27.6%) | `halogenated_aliphatic` (2.3%) | ✗ |
| 溶剂 set | 79 | `C1CCOC1` + `O` | `__ABSENT__` (98%) | `CC#N` (0%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `O=S([O-])O.[Na+]` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `__OTHER__` (0%) | set ✗ / any ✓ |

---

### Reaction #1860  yield=15.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #2)

```
CO.COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1cccnc1>>COC(=O)C(C)(CC(OC)(c1ccccc1)c1cccnc1)C(=O)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (90.3%) | `graphite_generic` (5.3%) | `carbon_felt` (3.0%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.9%) | `nickel` (0.1%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.4%) | `ABSENT` (15.8%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (29.1%) | `ABSENT` (28.4%) | `OH` (19.4%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (4.9%) | `tetraaryl_borate` (2.8%) | `as_solvent_halogenated_aliphat` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.4%) | `ferrocene_mediator` (0.7%) | `triarylamine_radical_cat` (0.3%) | ✓ |
| 溶剂大类 | 27 | `cyclic_ether` | `ABSENT` (68.9%) | `polar_aprotic_nitrile` (27.6%) | `halogenated_aliphatic` (2.3%) | ✗ |
| 溶剂 set | 79 | `C1CCOC1` + `O` | `__ABSENT__` (98%) | `CC#N` (0%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `O=S([O-])O.[Na+]` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `__OTHER__` (0%) | set ✗ / any ✓ |

---

### Reaction #1861  yield=12.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #4)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(C)C#N>>CC1(C#N)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `ABSENT` (0.1%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (52.3%) | `graphite_generic` (28.3%) | `reticulated_vitreous_carbon` (11.1%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (48.6%) | `platinum` (40.5%) | `carbon` (4.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (92.9%) | `nickel_plate` (2.3%) | `nickel_foam` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.3%) | `NEt4` (33.8%) | `Na` (2.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (57.5%) | `PF6` (20.9%) | `ClO4` (7.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (9.9%) | `water` (2.4%) | `diboron` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (74.9%) | `ammonium_PTC_organocat` (6.9%) | `ionic_organocat` (3.2%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (35.7%) | `polar_aprotic_nitrile` (35.0%) | `ketone` (16.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (72%) | `CC#N` (22%) | `C1CCOC1` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (98%) | `[Cl][Mn][Cl]` (1%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✗ / any ✗ |

---

### Reaction #1862  yield=18.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #5)

```
CO.C=C(c1ccccc1)c1ccccc1.CCOC(=O)C(C)C(C)=O>>CCOC(=O)[C@]1(C)CC(c2ccccc2)(c2ccccc2)O[C@]1(C)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (92.3%) | `graphite_generic` (7.5%) | `reticulated_vitreous_carbon` (0.1%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.8%) | `nickel` (1.0%) | `carbon` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (97.8%) | `platinum_generic` (1.7%) | `nickel_foam` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (98.7%) | `ABSENT` (0.7%) | `NEt4` (0.4%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (47.5%) | `ClO4` (38.8%) | `PF6` (10.8%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `o2_oxidant` (41.8%) | `alkali_other_salt` (6.0%) | `metal_oxide_oxidant` (1.3%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `triarylamine_radical_cat` (36.2%) | `ABSENT` (34.1%) | `ammonium_PTC_organocat` (14.8%) | ✗ |
| 溶剂大类 | 27 | `cyclic_ether` | `ABSENT` (95.9%) | `polar_aprotic_nitrile` (3.3%) | `cyclic_ether` (0.3%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `O` | `__ABSENT__` (100%) | `CCO` (0%) | `CC#N` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `Cl` | `O=O` (76%) | `__ABSENT__` (8%) | `C[Si](C)(C)N=[N+]=` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `Brc1ccc(N(c2ccc(Br` (97%) | `CC[N+](CC)(CC)CC.F` (1%) | `[cH]12->[Fe+2]3456` (1%) | set ✗ / any ✓ |

---

### Reaction #1863  yield=12.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #6)

```
COC(=O)C(C)C(=O)OC.C=C(C)c1ccc(Br)cc1>>COC(=O)[C@@]1(C)C[C@@](C)(c2ccc(Br)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.9%) | `platinum` (3.0%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (62.4%) | `carbon_felt` (15.6%) | `graphite_generic` (11.3%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.3%) | `carbon` (2.3%) | `nickel` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (53.6%) | `platinum_wire` (40.4%) | `platinum_generic` (4.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.6%) | `NEt4` (0.2%) | `Li` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (94.2%) | `Br` (1.7%) | `PF6` (1.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (8.6%) | `primary_amine` (3.1%) | `carboxylic_acid` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (76.5%) | `pyridine_organocat` (7.1%) | `Fe_complex` (4.6%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (84.9%) | `polar_protic_alcohol` (11.7%) | `ABSENT` (2.2%) | ✓ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CC#N` (97%) | `O` (10%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `O` (0%) | `O=P([O-])([O-])[O-` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #1864  yield=17.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #7)

```
CO.C=C(c1ccccc1)c1ccccc1.COC(=O)C(C)C(=O)OC>>COC(=O)C(C)(CC(OC)(c1ccccc1)c1ccccc1)C(=O)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (72.0%) | `graphite_generic` (14.0%) | `carbon_rod` (4.3%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.5%) | `carbon` (0.3%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `platinum_generic` (1.9%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.7%) | `NH4` (0.2%) | `K` (0.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (78.7%) | `I` (16.0%) | `OH` (2.3%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (5.2%) | `o2_oxidant` (4.3%) | `azide_source` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (83.4%) | `ferrocene_mediator` (13.5%) | `ammonium_PTC_organocat` (1.0%) | ✓ |
| 溶剂大类 | 27 | `cyclic_ether` | `ABSENT` (90.1%) | `polar_aprotic_nitrile` (5.3%) | `cyclic_ether` (2.0%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `O` | `__ABSENT__` (95%) | `CO` (2%) | `CC#N` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `Cl` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (100%) | `[cH]12->[Fe+2]3456` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #1865  yield=16.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #7)

```
CO.C=C(c1ccccc1)c1ccccc1.COC(=O)C(C)C(=O)OC>>COC(=O)C(C)(CC(OC)(c1ccccc1)c1ccccc1)C(=O)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (72.0%) | `graphite_generic` (14.0%) | `carbon_rod` (4.3%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.5%) | `carbon` (0.3%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `platinum_generic` (1.9%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.7%) | `NH4` (0.2%) | `K` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (78.7%) | `I` (16.0%) | `OH` (2.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (5.2%) | `o2_oxidant` (4.3%) | `azide_source` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (83.4%) | `ferrocene_mediator` (13.5%) | `ammonium_PTC_organocat` (1.0%) | ✓ |
| 溶剂大类 | 27 | `cyclic_ether` | `ABSENT` (90.1%) | `polar_aprotic_nitrile` (5.3%) | `cyclic_ether` (2.0%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `O` | `__ABSENT__` (95%) | `CO` (2%) | `CC#N` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `Cl` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (100%) | `[cH]12->[Fe+2]3456` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #1866  yield=28.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #9)

```
CO.C=C(C)c1ccccc1.COC(=O)C(C)C(=O)OC>>COC(=O)C(C)(CC(C)(OC)c1ccccc1)C(=O)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (28.8%) | `graphite_rod` (26.3%) | `reticulated_vitreous_carbon` (15.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.8%) | `nickel` (0.1%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (77.6%) | `platinum_generic` (22.1%) | `platinum_wire` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.5%) | `NH4` (0.2%) | `NEt4` (0.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (84.5%) | `OH` (5.7%) | `Br` (3.9%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (8.0%) | `o2_oxidant` (5.3%) | `carboxylic_acid` (3.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.4%) | `Fe_complex` (0.2%) | `ferrocene_mediator` (0.2%) | ✓ |
| 溶剂大类 | 27 | `cyclic_ether` | `ABSENT` (99.4%) | `polar_protic_alcohol` (0.3%) | `polar_aprotic_nitrile` (0.1%) | ✗ |
| 溶剂 set | 79 | `C1CCOC1` + `O` | `__ABSENT__` (98%) | `CO` (0%) | `FC(F)(F)c1ccccc1` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `Cl` | `__ABSENT__` (100%) | `O=O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |

---

### Reaction #1867  yield=28.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #10)

```
COC(=O)CC(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (71.8%) | `platinum` (25.8%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (87.3%) | `carbon_generic` (5.9%) | `glassy_carbon` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (87.7%) | `nickel` (4.4%) | `carbon` (3.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (47.3%) | `platinum_generic` (35.5%) | `platinum_wire` (3.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (95.7%) | `ABSENT` (2.9%) | `divided` (1.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (72.9%) | `NEt4` (23.0%) | `Li` (2.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (60.5%) | `ClO4` (20.7%) | `carboxylate` (6.3%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (11.9%) | `alkali_other_salt` (4.8%) | `alkali_carbonate` (3.1%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (95.0%) | `organic_neutral_cat` (1.4%) | `ammonium_PTC_organocat` (0.9%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (88.0%) | `polar_protic_alcohol` (7.5%) | `ABSENT` (1.8%) | ✓ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CC#N` (100%) | `O` (10%) | `CCO` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `O=C(O)C(F)(F)F` (18%) | `[OH][Na]` (7%) | `CC(=O)O` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (96%) | `Brc1ccc(N(c2ccc(Br` (2%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #1868  yield=26.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #11)

```
CO.C=C(c1ccccc1)c1ccccc1.CCOC(=O)C(C)C(C)=O>>CC(=O)C1(C)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.3%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (99.3%) | `graphite_generic` (0.6%) | `carbon_rod` (0.0%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.6%) | `nickel` (0.3%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (96.2%) | `platinum_generic` (3.7%) | `graphite_rod` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (85.7%) | `ABSENT` (13.6%) | `NEt4` (0.6%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (71.5%) | `ABSENT` (17.6%) | `PF6` (9.2%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `o2_oxidant` (38.7%) | `ABSENT` (2.9%) | `ammonium_salt` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `triarylamine_radical_cat` (83.5%) | `ABSENT` (14.7%) | `ferrocene_mediator` (0.8%) | ✓ |
| 溶剂大类 | 27 | `cyclic_ether` | `ABSENT` (88.1%) | `polar_aprotic_nitrile` (10.9%) | `polar_aprotic_amide` (0.5%) | ✗ |
| 溶剂 set | 79 | `C1CCOC1` + `O` | `__ABSENT__` (100%) | `CC#N` (0%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `Cl` | `O=O` (63%) | `__ABSENT__` (2%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `Brc1ccc(N(c2ccc(Br` (69%) | `CC[N+](CC)(CC)CC.F` (14%) | `[cH]12->[Fe+2]3456` (8%) | set ✗ / any ✓ |

---

### Reaction #1869  yield=26.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #12)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccc(C#N)cc1>>COC(=O)[C@@]1(C)C[C@](c2ccccc2)(c2ccc(C#N)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `ABSENT` (0.9%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (65.3%) | `graphite_generic` (11.5%) | `unknown_electrode` (9.2%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.3%) | `ABSENT` (1.0%) | `carbon` (1.0%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_wire` (35.1%) | `platinum_plate` (30.4%) | `platinum_generic` (27.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (79.2%) | `Li` (10.1%) | `ABSENT` (4.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (90.4%) | `ABSENT` (2.2%) | `Cl` (1.8%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (5.7%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Fe_complex` (73.8%) | `ABSENT` (20.5%) | `Co_complex` (2.5%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (73.8%) | `ABSENT` (18.0%) | `polar_aprotic_nitrile` (4.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (70%) | `CC#N` (6%) | `C1CCOC1` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `C[SiH](C)O[SiH](C)` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (17%) | `__OTHER__` (12%) | `[O]=[Fe][O][Fe]=[O` (4%) | set ✗ / any ✓ |

---

### Reaction #1870  yield=26.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #13)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccc(C#N)cc1>>COC(=O)[C@@]1(C)C[C@@](c2ccccc2)(c2ccc(C#N)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `ABSENT` (0.9%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (65.3%) | `graphite_generic` (11.5%) | `unknown_electrode` (9.2%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.3%) | `ABSENT` (1.0%) | `carbon` (1.0%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_wire` (35.1%) | `platinum_plate` (30.4%) | `platinum_generic` (27.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (79.2%) | `Li` (10.1%) | `ABSENT` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.4%) | `ABSENT` (2.2%) | `Cl` (1.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (5.7%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Fe_complex` (73.8%) | `ABSENT` (20.5%) | `Co_complex` (2.5%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (73.8%) | `ABSENT` (18.0%) | `polar_aprotic_nitrile` (4.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (70%) | `CC#N` (6%) | `C1CCOC1` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `C[SiH](C)O[SiH](C)` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (17%) | `__OTHER__` (12%) | `[O]=[Fe][O][Fe]=[O` (4%) | set ✗ / any ✓ |

---

### Reaction #1871  yield=26.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #14)

```
C=C(c1ccccc1)c1ccc(C(F)(F)F)cc1.COC(=O)C(C)C(=O)OC>>COC(=O)[C@@]1(C)C[C@@](c2ccccc2)(c2ccc(C(F)(F)F)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.2%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (28.9%) | `graphite_rod` (21.8%) | `unknown_electrode` (20.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.0%) | `nickel` (0.4%) | `carbon` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (59.8%) | `platinum_plate` (30.3%) | `platinum_wire` (6.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.0%) | `ABSENT` (1.0%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (94.5%) | `PF6` (3.6%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (8.1%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Fe_complex` (58.9%) | `ABSENT` (17.1%) | `Co_complex` (14.9%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (83.1%) | `polar_aprotic_nitrile` (13.6%) | `ABSENT` (2.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (59%) | `CC#N` (28%) | `C1CCOC1` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `O=O` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `__OTHER__` | `__ABSENT__` (4%) | `Brc1ccc(N(c2ccc(Br` (3%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1872  yield=26.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #15)

```
C=C(c1ccccc1)c1ccc(C(F)(F)F)cc1.COC(=O)C(C)C(=O)OC>>COC(=O)[C@]1(C)C[C@@](c2ccccc2)(c2ccc(C(F)(F)F)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.2%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (28.9%) | `graphite_rod` (21.8%) | `unknown_electrode` (20.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.0%) | `nickel` (0.4%) | `carbon` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (59.8%) | `platinum_plate` (30.3%) | `platinum_wire` (6.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (98.0%) | `ABSENT` (1.0%) | `NEt4` (0.6%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (94.5%) | `PF6` (3.6%) | `ABSENT` (1.1%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (8.1%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Fe_complex` (58.9%) | `ABSENT` (17.1%) | `Co_complex` (14.9%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (83.1%) | `polar_aprotic_nitrile` (13.6%) | `ABSENT` (2.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (59%) | `CC#N` (28%) | `C1CCOC1` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `O=O` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `__OTHER__` | `__ABSENT__` (4%) | `Brc1ccc(N(c2ccc(Br` (3%) | `CC(=O)[CH-]C(C)=O.` (2%) | set ✗ / any ✗ |

---

### Reaction #1873  yield=30.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #16)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1cccc(Br)c1>>COC(=O)[C@]1(C)C[C@@](c2ccccc2)(c2cccc(Br)c2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (51.5%) | `carbon_felt` (23.9%) | `graphite_generic` (15.3%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.8%) | `nickel` (0.1%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (50.0%) | `platinum_generic` (48.7%) | `platinum_wire` (1.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (56.6%) | `ABSENT` (38.7%) | `Na` (3.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (75.9%) | `ABSENT` (22.9%) | `molecular_no_ion` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (12.3%) | `tetraaryl_borate` (2.4%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (54.9%) | `Fe_complex` (17.5%) | `Co_complex` (8.9%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (61.9%) | `polar_aprotic_nitrile` (36.5%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (36%) | `CC#N` (31%) | `__ABSENT__` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `O=S(=O)([O-])C(F)(` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |

---

### Reaction #1874  yield=30.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #17)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1cccc(Br)c1>>COC(=O)[C@]1(C)C[C@](c2ccccc2)(c2cccc(Br)c2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (51.5%) | `carbon_felt` (23.9%) | `graphite_generic` (15.3%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.8%) | `nickel` (0.1%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (50.0%) | `platinum_generic` (48.7%) | `platinum_wire` (1.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (56.6%) | `ABSENT` (38.7%) | `Na` (3.7%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (75.9%) | `ABSENT` (22.9%) | `molecular_no_ion` (0.3%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (12.3%) | `tetraaryl_borate` (2.4%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (54.9%) | `Fe_complex` (17.5%) | `Co_complex` (8.9%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (61.9%) | `polar_aprotic_nitrile` (36.5%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (36%) | `CC#N` (31%) | `__ABSENT__` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `O=S(=O)([O-])C(F)(` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |

---

### Reaction #1875  yield=32.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #18)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(C)C#N>>COC(=O)C(C)(C#N)CC(OC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (54.5%) | `reticulated_vitreous_carbon` (37.7%) | `graphite_rod` (5.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (95.5%) | `carbon` (3.8%) | `nickel` (0.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (61.6%) | `platinum_plate` (35.0%) | `graphite_generic` (1.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.3%) | `NEt4` (0.5%) | `Na` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (96.2%) | `PF6` (2.2%) | `I` (0.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (2.5%) | `alkali_carbonate` (2.3%) | `metal_oxide_oxidant` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (44.3%) | `ABSENT` (35.4%) | `Fe_complex` (9.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (91.9%) | `polar_aprotic_nitrile` (6.8%) | `cyclic_ether` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (87%) | `C1CCOC1` (60%) | `CC#N` (13%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (98%) | `C[Si](C)(C)N=[N+]=` (1%) | `O=C([O-])[O-].[Na+` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `[Fe+2].c1cc[cH-]c1` (51%) | `Brc1ccc(N(c2ccc(Br` (27%) | `[cH]12->[Fe+2]3456` (17%) | set ✗ / any ✓ |

---

### Reaction #1876  yield=38.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #19)

```
CO.C=C(C)c1ccccc1.COC(=O)C(C)C(=O)OC>>COC(=O)[C@]1(C)C[C@@](C)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.2%) | `platinum` (3.5%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (76.1%) | `reticulated_vitreous_carbon` (11.1%) | `graphite_rod` (5.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (95.4%) | `nickel` (3.1%) | `carbon` (1.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.8%) | `graphite_generic` (0.3%) | `platinum_generic` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (96.2%) | `ABSENT` (2.4%) | `NEt4` (0.5%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (76.4%) | `PF6` (6.7%) | `ABSENT` (6.2%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `o2_oxidant` (14.2%) | `ABSENT` (3.7%) | `as_solvent_polar_aprotic_nitri` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `triarylamine_radical_cat` (69.1%) | `ABSENT` (16.3%) | `ammonium_PTC_organocat` (3.4%) | ✗ |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (49.3%) | `ABSENT` (46.3%) | `polar_aprotic_amide` (2.3%) | ✗ |
| 溶剂 set | 79 | `C1CCOC1` + `O` | `CC#N` (88%) | `CO` (9%) | `__ABSENT__` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `Cl` | `O=O` (30%) | `__ABSENT__` (1%) | `C[Si](C)(C)N=[N+]=` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `Brc1ccc(N(c2ccc(Br` (23%) | `__ABSENT__` (18%) | `Brc1ccc(N(c2ccc(Br` (16%) | set ✗ / any ✗ |

---

### Reaction #1877  yield=35.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #20)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccc(C)cc1>>COC(=O)[C@@]1(C)C[C@](c2ccccc2)(c2ccc(C)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (43.6%) | `reticulated_vitreous_carbon` (29.2%) | `carbon_felt` (21.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.6%) | `nickel` (1.1%) | `carbon` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (80.3%) | `platinum_generic` (12.3%) | `platinum_wire` (5.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (63.1%) | `NBu4` (35.9%) | `Na` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (60.0%) | `ABSENT` (38.8%) | `PF6` (0.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (7.3%) | `carboxylic_acid` (3.8%) | `as_solvent_halogenated_aliphat` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (30.9%) | `Fe_complex` (30.8%) | `ferrocene_mediator` (12.4%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (75.0%) | `polar_aprotic_nitrile` (20.6%) | `ABSENT` (3.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (76%) | `CC#N` (20%) | `C1CCOC1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (99%) | `CC(=O)O` (0%) | `O=P([O-])([O-])[O-` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `__OTHER__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #1878  yield=35.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #21)

```
COC(=O)CC(=O)OC.C=C(c1ccccc1)c1ccc(C)cc1>>COC(=O)C1(C)CC(c2ccccc2)(c2ccc(C)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (85.8%) | `graphite_rod` (6.8%) | `carbon_generic` (4.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (96.9%) | `nickel` (2.3%) | `carbon` (0.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (89.4%) | `platinum_generic` (8.8%) | `nickel_foam` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (12.7%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (87.8%) | `BF4` (8.4%) | `PF6` (2.9%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `alkali_other_salt` (9.8%) | `ABSENT` (4.9%) | `carboxylic_acid` (4.9%) | ✗ |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `Co_complex` (34.8%) | `ABSENT` (29.4%) | `thianthrene_phenothiazine_cat` (6.6%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (84.0%) | `polar_protic_alcohol` (12.5%) | `ABSENT` (1.2%) | ✓ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CC#N` (99%) | `ClCCCl` (1%) | `CO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `[Cl-].[H+]` | `O=C(O)O.[K]` (11%) | `O=S(O)O.[Na]` (6%) | `O=C(O)O.[Na]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` + `c1cc2c(c[c]1[Fe][c` | `CC(C)(C)c1ccc2[O-]` (24%) | `__ABSENT__` (8%) | `__OTHER__` (6%) | set ✗ / any ✗ |

---

### Reaction #1879  yield=38.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #22)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccc(Br)cc1>>COC(=O)[C@@]1(C)C[C@@](c2ccccc2)(c2ccc(Br)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (69.7%) | `reticulated_vitreous_carbon` (17.8%) | `carbon_felt` (7.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.3%) | `nickel` (0.4%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (58.9%) | `platinum_wire` (22.1%) | `platinum_generic` (17.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.1%) | `ABSENT` (0.5%) | `NEt4` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (98.3%) | `PF6` (0.9%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (7.4%) | `carboxylic_acid` (4.2%) | `as_solvent_halogenated_aliphat` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (67.1%) | `Fe_complex` (18.3%) | `triarylamine_radical_cat` (5.4%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (53.6%) | `polar_protic_alcohol` (37.8%) | `ABSENT` (7.5%) | ✓ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CC#N` (94%) | `CO` (1%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `__OTHER__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✗ / any ✗ |

---

### Reaction #1880  yield=38.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #23)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccc(Br)cc1>>COC(=O)[C@@]1(C)C[C@](c2ccccc2)(c2ccc(Br)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (69.7%) | `reticulated_vitreous_carbon` (17.8%) | `carbon_felt` (7.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.3%) | `nickel` (0.4%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (58.9%) | `platinum_wire` (22.1%) | `platinum_generic` (17.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.1%) | `ABSENT` (0.5%) | `NEt4` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (98.3%) | `PF6` (0.9%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (7.4%) | `carboxylic_acid` (4.2%) | `as_solvent_halogenated_aliphat` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (67.1%) | `Fe_complex` (18.3%) | `triarylamine_radical_cat` (5.4%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (53.6%) | `polar_protic_alcohol` (37.8%) | `ABSENT` (7.5%) | ✓ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CC#N` (94%) | `CO` (1%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `__OTHER__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✗ / any ✗ |

---

### Reaction #1881  yield=32.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #24)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccccc1Br>>COC(=O)[C@@]1(C)C[C@](c2ccccc2)(c2ccccc2Br)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `ABSENT` (0.8%) | `platinum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `glassy_carbon` (25.8%) | `carbon_felt` (18.9%) | `graphite_rod` (18.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.1%) | `ABSENT` (0.5%) | `carbon` (0.3%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (72.8%) | `platinum_generic` (25.6%) | `platinum_wire` (0.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.7%) | `Li` (2.6%) | `K` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (96.9%) | `PF6` (1.7%) | `ClO4` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (14.2%) | `as_solvent_halogenated_aliphat` (2.3%) | `tetraaryl_borate` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Fe_complex` (64.9%) | `ABSENT` (26.8%) | `Co_complex` (2.9%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (91.0%) | `polar_aprotic_nitrile` (7.8%) | `ketone` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (89%) | `CC#N` (10%) | `C1CCOC1` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `O=S(=O)([O-])C(F)(` | `c1ccc2c(c1)-c1nc3c` (5%) | `__ABSENT__` (3%) | `Brc1ccc(N(c2ccc(Br` (2%) | set ✗ / any ✗ |

---

### Reaction #1882  yield=32.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #25)

```
COC(=O)CC(=O)OC.C=C(c1ccccc1)c1ccc(Br)cc1>>COC(=O)C1(C)CC(c2ccccc2)(c2ccc(Br)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (51.2%) | `carbon_generic` (35.7%) | `graphite_rod` (8.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.7%) | `nickel` (1.5%) | `ABSENT` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (54.7%) | `platinum_generic` (38.9%) | `platinum_wire` (4.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (1.2%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (55.7%) | `PF6` (35.4%) | `ABSENT` (4.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (6.4%) | `carboxylic_acid` (6.4%) | `alkali_other_salt` (3.8%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (71.5%) | `Co_complex` (11.6%) | `pyridine_organocat` (4.6%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (94.2%) | `polar_protic_alcohol` (4.1%) | `ABSENT` (0.9%) | ✓ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CC#N` (100%) | `COC(C)(C)C` (4%) | `ClCCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `[Cl-].[H+]` | `__ABSENT__` (98%) | `CC(=O)O` (0%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1cc2c(c[c]1[Fe][c` + `O=S(=O)([O-])C(F)(` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #1883  yield=38.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #26)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccc(C(=O)OC)cc1>>COC(=O)c1ccc([C@@]2(c3ccccc3)C[C@](C)(C(=O)OC)C(=O)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `ABSENT` (0.3%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (61.9%) | `reticulated_vitreous_carbon` (16.5%) | `graphite_generic` (10.1%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.6%) | `nickel` (1.2%) | `carbon` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (81.7%) | `platinum_generic` (13.2%) | `platinum_wire` (3.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (89.0%) | `Na` (2.7%) | `K` (2.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (83.2%) | `PF6` (11.1%) | `I` (2.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (11.4%) | `carboxylic_acid` (3.1%) | `o2_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (61.2%) | `Fe_complex` (15.8%) | `triarylamine_radical_cat` (6.6%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (80.2%) | `polar_aprotic_nitrile` (15.4%) | `ABSENT` (3.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (91%) | `CC#N` (7%) | `__ABSENT__` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (98%) | `CCCC[N+](CCCC)(CCC` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✗ / any ✗ |

---

### Reaction #1884  yield=38.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #26)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccc(C(=O)OC)cc1>>COC(=O)c1ccc([C@@]2(c3ccccc3)C[C@](C)(C(=O)OC)C(=O)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `ABSENT` (0.3%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (61.9%) | `reticulated_vitreous_carbon` (16.5%) | `graphite_generic` (10.1%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.6%) | `nickel` (1.2%) | `carbon` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (81.7%) | `platinum_generic` (13.2%) | `platinum_wire` (3.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (89.0%) | `Na` (2.7%) | `K` (2.7%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (83.2%) | `PF6` (11.1%) | `I` (2.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (11.4%) | `carboxylic_acid` (3.1%) | `o2_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (61.2%) | `Fe_complex` (15.8%) | `triarylamine_radical_cat` (6.6%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (80.2%) | `polar_aprotic_nitrile` (15.4%) | `ABSENT` (3.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (91%) | `CC#N` (7%) | `__ABSENT__` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (98%) | `CCCC[N+](CCCC)(CCC` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✗ / any ✗ |

---

### Reaction #1885  yield=42.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #28)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1cccc(C)c1>>COC(=O)[C@@]1(C)C[C@@](c2ccccc2)(c2cccc(C)c2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (27.4%) | `reticulated_vitreous_carbon` (23.6%) | `carbon_felt` (20.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `carbon` (0.1%) | `ABSENT` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (82.4%) | `platinum_generic` (17.1%) | `platinum_wire` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (74.3%) | `ABSENT` (25.1%) | `NEt4` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (89.5%) | `ABSENT` (10.2%) | `PF6` (0.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (10.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (71.7%) | `Fe_complex` (8.8%) | `triarylamine_radical_cat` (6.9%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (76.8%) | `polar_aprotic_nitrile` (20.5%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (52%) | `CC#N` (42%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `__OTHER__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |

---

### Reaction #1886  yield=42.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #29)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1cccc(C)c1>>COC(=O)[C@@]1(C)C[C@](c2ccccc2)(c2cccc(C)c2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (27.4%) | `reticulated_vitreous_carbon` (23.6%) | `carbon_felt` (20.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `carbon` (0.1%) | `ABSENT` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (82.4%) | `platinum_generic` (17.1%) | `platinum_wire` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (74.3%) | `ABSENT` (25.1%) | `NEt4` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (89.5%) | `ABSENT` (10.2%) | `PF6` (0.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (10.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (71.7%) | `Fe_complex` (8.8%) | `triarylamine_radical_cat` (6.9%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (76.8%) | `polar_aprotic_nitrile` (20.5%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (52%) | `CC#N` (42%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `__OTHER__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |

---

### Reaction #1887  yield=45.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #30)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccccc1C>>COC(=O)[C@@]1(C)C[C@@](c2ccccc2)(c2ccccc2C)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `platinum` (1.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (34.4%) | `reticulated_vitreous_carbon` (26.5%) | `graphite_rod` (25.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `nickel` (0.1%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (97.0%) | `platinum_generic` (2.4%) | `platinum_wire` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (69.1%) | `ABSENT` (29.0%) | `NEt4` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.3%) | `ABSENT` (17.3%) | `PF6` (3.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (8.8%) | `carboxylic_acid` (7.5%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (26.2%) | `Fe_complex` (25.3%) | `triarylamine_radical_cat` (17.7%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (93.9%) | `polar_aprotic_nitrile` (5.3%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (92%) | `CC#N` (7%) | `C1CCOC1` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `__OTHER__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #1888  yield=45.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #31)

```
COC(=O)C(C)C(=O)OC.C=C(c1ccccc1)c1ccccc1C>>COC(=O)[C@@]1(C)C[C@](c2ccccc2)(c2ccccc2C)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `platinum` (1.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (34.4%) | `reticulated_vitreous_carbon` (26.5%) | `graphite_rod` (25.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `nickel` (0.1%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (97.0%) | `platinum_generic` (2.4%) | `platinum_wire` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (69.1%) | `ABSENT` (29.0%) | `NEt4` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.3%) | `ABSENT` (17.3%) | `PF6` (3.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (8.8%) | `carboxylic_acid` (7.5%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (26.2%) | `Fe_complex` (25.3%) | `triarylamine_radical_cat` (17.7%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (93.9%) | `polar_aprotic_nitrile` (5.3%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (92%) | `CC#N` (7%) | `C1CCOC1` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `__OTHER__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #1889  yield=46.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #32)

```
COC(=O)C(C)C(=O)OC.C=C(C)c1ccc(Br)cc1>>COC(=O)[C@@]1(C)C[C@](C)(c2ccc(Br)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.9%) | `platinum` (3.0%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (62.4%) | `carbon_felt` (15.6%) | `graphite_generic` (11.3%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.3%) | `carbon` (2.3%) | `nickel` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (53.6%) | `platinum_wire` (40.4%) | `platinum_generic` (4.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.6%) | `NEt4` (0.2%) | `Li` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (94.2%) | `Br` (1.7%) | `PF6` (1.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (8.6%) | `primary_amine` (3.1%) | `carboxylic_acid` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (76.5%) | `pyridine_organocat` (7.1%) | `Fe_complex` (4.6%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (84.9%) | `polar_protic_alcohol` (11.7%) | `ABSENT` (2.2%) | ✓ |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CC#N` (97%) | `O` (10%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `Cl` | `__ABSENT__` (100%) | `O` (0%) | `O=P([O-])([O-])[O-` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #1890  yield=69.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #33)

```
CO.C=C(c1ccccc1)c1ccccc1.COC(=O)C(C)C(=O)OC>>COC(=O)C1(C)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.5%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (78.0%) | `graphite_generic` (11.8%) | `reticulated_vitreous_carbon` (6.2%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (96.1%) | `nickel` (3.2%) | `ABSENT` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.1%) | `platinum_generic` (1.1%) | `nickel_plate` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.5%) | `ABSENT` (4.1%) | `NEt4` (1.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (73.2%) | `PF6` (13.6%) | `I` (5.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (7.6%) | `o2_oxidant` (5.6%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (52.8%) | `triarylamine_radical_cat` (36.0%) | `ammonium_PTC_organocat` (2.8%) | ✗ |
| 溶剂大类 | 27 | `cyclic_ether` | `ABSENT` (67.9%) | `polar_aprotic_nitrile` (28.1%) | `polar_protic_alcohol` (2.0%) | ✗ |
| 溶剂 set | 79 | `C1CCOC1` + `O` | `__ABSENT__` (97%) | `CC#N` (5%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `Cl` | `__ABSENT__` (99%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=S([O-])O.[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (99%) | `CC[N+](CC)(CC)CC.F` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |

---

### Reaction #1891  yield=64.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #34)

```
CO.C=C(c1ccccc1)c1ccccc1.COC(=O)C(C)C(=O)OC>>COC(=O)C1(C)CC(c2ccccc2)(c2ccccc2)OC1(OC)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `platinum` (1.9%) | `sacrificial_iron` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (95.1%) | `carbon_felt` (1.7%) | `graphite_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (47.0%) | `platinum` (35.3%) | `carbon` (17.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_foam` (70.8%) | `graphite_generic` (12.3%) | `platinum_plate` (6.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (80.2%) | `NEt4` (8.1%) | `NH4` (4.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (77.8%) | `I` (13.5%) | `BF4` (5.0%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `o2_oxidant` (50.8%) | `water` (2.7%) | `ABSENT` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (86.1%) | `triarylamine_radical_cat` (8.2%) | `organic_neutral_cat` (2.1%) | ✗ |
| 溶剂大类 | 27 | `cyclic_ether` | `ABSENT` (59.0%) | `cyclic_ether` (20.5%) | `polar_aprotic_nitrile` (19.7%) | ✓ |
| 溶剂 set | 79 | `C1CCOC1` + `O` | `__ABSENT__` (100%) | `CC#N` (0%) | `CCOCC` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `Cl` | `O=O` (70%) | `C[Si](C)(C)N=[N+]=` (2%) | `O` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` + `__OTHER__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #1892  yield=90.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #35)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(C)C(=O)OC>>COC(=O)C1(C)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.0%) | `ABSENT` (8.7%) | `platinum` (1.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `reticulated_vitreous_carbon` (30.7%) | `ABSENT` (20.0%) | `glassy_carbon` (16.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (89.6%) | `ABSENT` (8.9%) | `nickel` (0.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (50.6%) | `platinum_generic` (25.1%) | `platinum_wire` (11.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.7%) | `NEt4` (3.1%) | `Li` (2.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (93.0%) | `PF6` (3.8%) | `ClO4` (1.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (7.3%) | `carboxylic_acid` (2.7%) | `as_solvent_halogenated_aliphat` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (45.5%) | `Fe_complex` (29.7%) | `Co_complex` (5.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (96.7%) | `polar_aprotic_nitrile` (2.2%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (98%) | `C1CCOC1` (3%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=C([O-])[O-].[Na+` | `__ABSENT__` (99%) | `O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `O=S(=O)([O-])C(F)(` | `__ABSENT__` (93%) | `Brc1ccc(N(c2ccc(Br` (2%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1893  yield=55.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_15_5292-5300.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_15_5292-5300.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CN(CC#Cc1ccccc1)S(=O)(=O)c1ccc(C)cc1)c1ccccc1>>Cc1ccc(S(=O)(=O)N2C/C(=C(\Br)c3ccccc3)C(CBr)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (67.7%) | `platinum` (32.3%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `platinum_plate` (47.9%) | `carbon_felt` (30.9%) | `graphite_felt` (7.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (70.4%) | `carbon` (29.4%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_plate` | `platinum_plate` (69.4%) | `graphite_plate` (20.8%) | `graphite_felt` (5.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.5%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `alkyl_ammonium` | `H` (84.4%) | `Li` (13.5%) | `Na` (0.8%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (45.4%) | `ClO4` (21.6%) | `carboxylate` (20.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (24.7%) | `ABSENT` (5.9%) | `bromide_anion` (2.0%) | ✓ |
| 催化剂大类 | 49 | `aryl_iodide_mediator` | `aryl_iodide_mediator` (30.6%) | `pyridine_organocat` (21.4%) | `ABSENT` (21.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (72.1%) | `halogenated_aliphatic` (23.9%) | `hfip` (1.1%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (90%) | `O` (89%) | `OC(C(F)(F)F)C(F)(F` (10%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=S([O-])([O-])=S.` (57%) | `O=C(O)O.[Na]` (25%) | `__ABSENT__` (6%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `Cc1ccc(I)cc1` | `Cc1ccc(I)cc1` (15%) | `CC(=O)NC1CC2(CCCCC` (1%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✗ / any ✓ |

---

### Reaction #1894  yield=27.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #0)

```
N=C(c1ccccc1)c1ccccc1.COc1ccc(/C=C/CCC(=O)O)cc1OC>>COc1ccc(C(N=C(c2ccccc2)c2ccccc2)C2CCC(=O)O2)cc1OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.7%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (41.1%) | `graphite_rod` (18.1%) | `graphite_generic` (17.4%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.4%) | `nickel` (1.4%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (60.1%) | `platinum_plate` (39.0%) | `nickel_plate` (0.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (52.1%) | `NBu4` (42.8%) | `Na` (4.4%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (45.6%) | `molecular_no_ion` (38.2%) | `BF4` (12.9%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (36.0%) | `hydrosilane` (2.1%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.0%) | `polar_protic_alcohol` (1.5%) | `halogenated_aliphatic` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (100%) | `[H+].[OH-]` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)C(=O)O.[K]` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Br-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Br-].[Mn+2]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #1895  yield=29.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #1)

```
OCC/C=C/c1cccc(Br)c1>>Cl.N[C@H]1CCO[C@@H]1c1cccc(Br)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (56.0%) | `graphite_generic` (42.1%) | `reticulated_vitreous_carbon` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.0%) | `nickel` (0.4%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (78.0%) | `platinum_plate` (19.8%) | `platinum_foil` (1.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (58.8%) | `ABSENT` (41.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (55.0%) | `ABSENT` (40.2%) | `Li` (1.6%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (46.7%) | `PF6` (30.1%) | `BF4` (11.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `imine` | `alkali_sulfinate` (12.8%) | `ABSENT` (6.4%) | `carboxylic_acid` (4.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `Mn_complex` (0.4%) | `pyridine_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (66.2%) | `halogenated_aliphatic` (32.9%) | `polar_aprotic_sulfoxide` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (99%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `O=S([O-])C(F)(F)F.` (10%) | `__ABSENT__` (9%) | `C[Si](C)(C)N=[N+]=` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #1896  yield=39.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #2)

```
N=C(c1ccccc1)c1ccccc1.CCCCOc1ccc(/C=C/CCCO)cc1>>CCCCOc1ccc([C@@H](N=C(c2ccccc2)c2ccccc2)[C@@H]2CCCO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `platinum` (1.6%) | `sacrificial_aluminum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (92.2%) | `carbon_plate` (3.1%) | `reticulated_vitreous_carbon` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (68.8%) | `carbon` (15.1%) | `sacrificial_zinc` (8.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (87.3%) | `graphite_plate` (4.4%) | `zinc_generic` (3.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (96.6%) | `NBu4` (3.4%) | `Na` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.7%) | `BF4` (1.1%) | `I` (0.9%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (32.4%) | `hydrosilane` (2.2%) | `as_solvent_aromatic_hydrocarbo` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.8%) | `ketone` (1.5%) | `acyclic_ether` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (99%) | `[H+].[OH-]` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Br-].[Mn+2]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #1897  yield=34.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #3)

```
N=C(c1ccccc1)c1ccccc1.OCC/C=C/c1ccc(Br)cc1>>Brc1ccc([C@H]2OCC[C@@H]2N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (4.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (97.8%) | `graphite_rod` (0.9%) | `graphite_generic` (0.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.8%) | `sacrificial_zinc` (5.0%) | `sacrificial_iron` (4.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (94.7%) | `platinum_plate` (4.1%) | `graphite_plate` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.0%) | `NEt4` (4.1%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (82.4%) | `Br` (3.0%) | `PF6` (3.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (36.7%) | `unparseable_text` (1.8%) | `electrophilic_N_F` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.3%) | `halogenated_aliphatic` (1.8%) | `hfip` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1898  yield=34.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #4)

```
N=C(c1ccccc1)c1ccccc1.OCCC=C(c1ccccc1)c1ccccc1>>Cl.NC1CCOC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (54.8%) | `carbon_plate` (14.9%) | `graphite_generic` (10.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.6%) | `carbon` (2.9%) | `nickel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.5%) | `platinum_generic` (0.4%) | `glassy_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `K` (40.9%) | `Na` (26.3%) | `NBu4` (21.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (35.3%) | `Br` (22.5%) | `PF6` (22.1%) | ✗ |
| 试剂大类 | 103 | `hcl` | `ABSENT` (43.0%) | `carboxylic_acid` (4.4%) | `metal_oxide_oxidant` (1.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.0%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.9%) | `halogenated_aliphatic` (0.4%) | `polar_aprotic_sulfoxide` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (99%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `__ABSENT__` (100%) | `O=C([O-])O.[Na+]` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #1899  yield=38.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #5)

```
O=C(O)Cc1cc(Cl)ccc1Cl.CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2OC(=O)Cc2cc(Cl)ccc2Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (98.1%) | `glassy_carbon` (1.2%) | `graphite_rod` (0.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.4%) | `nickel` (8.2%) | `copper` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.3%) | `nickel_plate` (0.4%) | `platinum_plate` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.5%) | `K` (0.2%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (71.5%) | `Br` (18.1%) | `BF4` (9.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (24.5%) | `carboxylic_acid` (6.7%) | `primary_amine` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `pyridine_organocat` (0.3%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.5%) | `polar_protic_alcohol` (5.0%) | `hfip` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (41%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `Cc1ccc(S(=O)[O-])c` (1%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1900  yield=31.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #6)

```
O=C(O)C1CC1.OCCC/C=C/c1ccc(Oc2ccccc2)cc1>>O=C(O[C@@H](c1ccc(Oc2ccccc2)cc1)[C@@H]1CCCO1)C1CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (99.6%) | `carbon_felt` (0.2%) | `graphite_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (51.1%) | `platinum` (47.7%) | `nickel` (0.9%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `reticulated_vitreous_carbon` (79.3%) | `platinum_plate` (12.0%) | `platinum_wire` (2.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.1%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (92.4%) | `molecular_no_ion` (3.3%) | `BF4` (1.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `pyridine` (4.6%) | `tellurium_reagent` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (51.6%) | `polar_aprotic_nitrile` (37.6%) | `ketone` (10.6%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `__ABSENT__` (95%) | `CC#N` (3%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=P([O-])([O-])[O-` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1901  yield=31.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #7)

```
O=C(O)C1CC1.OCCC/C=C/c1ccc(Oc2ccccc2)cc1>>O=C(O[C@H](c1ccc(Oc2ccccc2)cc1)[C@@H]1CCCO1)C1CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (99.6%) | `carbon_felt` (0.2%) | `graphite_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (51.1%) | `platinum` (47.7%) | `nickel` (0.9%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `reticulated_vitreous_carbon` (79.3%) | `platinum_plate` (12.0%) | `platinum_wire` (2.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.1%) | `NBu4` (0.4%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (92.4%) | `molecular_no_ion` (3.3%) | `BF4` (1.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.7%) | `pyridine` (4.6%) | `tellurium_reagent` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (51.6%) | `polar_aprotic_nitrile` (37.6%) | `ketone` (10.6%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `__ABSENT__` (95%) | `CC#N` (3%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=P([O-])([O-])[O-` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1902  yield=37.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #8)

```
OCC/C=C/c1ccccc1.N=C(c1ccccc1)c1ccccc1>>c1ccc(C(=N[C@H]2CCO[C@@H]2c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (91.4%) | `platinum` (7.8%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (95.5%) | `graphite_generic` (1.1%) | `graphite_felt` (1.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (62.4%) | `sacrificial_zinc` (12.1%) | `sacrificial_iron` (9.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.1%) | `platinum_plate` (2.0%) | `iron_generic` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (91.1%) | `NEt4` (3.6%) | `ABSENT` (1.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (61.4%) | `PF6` (7.9%) | `carboxylate` (6.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.3%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `ammonium_PTC_organocat` (0.2%) | `ionic_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (76.3%) | `hfip` (14.8%) | `halogenated_aliphatic` (3.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (99%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)O` (0%) | `O=C([O-])[O-].[Na+` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `c1cc[c]([Fe][c]2cc` (0%) | set ✓ / any ✓ |

---

### Reaction #1903  yield=39.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #9)

```
CC(=O)O.COc1ccc(/C=C/CCCO)cc1OC>>COc1ccc(C(OC(C)=O)C2CCCO2)cc1OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `ABSENT` (1.1%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (91.6%) | `carbon_felt` (5.3%) | `ABSENT` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.2%) | `carbon` (7.9%) | `ABSENT` (3.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `ABSENT` (34.8%) | `platinum_generic` (34.1%) | `platinum_wire` (20.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.8%) | `NBu4` (0.2%) | `NEt4` (0.0%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (96.4%) | `molecular_no_ion` (3.0%) | `BF4` (0.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `hydrosilane` (13.5%) | `ABSENT` (11.9%) | `acid_anhydride` (7.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (78.9%) | `brønsted_acid_cat` (7.8%) | `Fe_complex` (5.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (54.4%) | `ABSENT` (23.5%) | `polar_protic_alcohol` (11.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `__OTHER__` (1%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (61%) | `C[SiH](C)O[SiH](C)` (38%) | `C[Si](C)(C)N=[N+]=` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Cc1cc(O[C@@H](C)C(` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1904  yield=40.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #10)

```
CC(=O)O.COc1ccc(/C=C/CCCO)cc1OC>>COc1ccc([C@H](OC(C)=O)[C@@H]2CCCO2)cc1OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `ABSENT` (1.1%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (91.6%) | `carbon_felt` (5.3%) | `ABSENT` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.2%) | `carbon` (7.9%) | `ABSENT` (3.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `ABSENT` (34.8%) | `platinum_generic` (34.1%) | `platinum_wire` (20.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (99.8%) | `NBu4` (0.2%) | `NEt4` (0.0%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (96.4%) | `molecular_no_ion` (3.0%) | `BF4` (0.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `hydrosilane` (13.5%) | `ABSENT` (11.9%) | `acid_anhydride` (7.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (78.9%) | `brønsted_acid_cat` (7.8%) | `Fe_complex` (5.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (54.4%) | `ABSENT` (23.5%) | `polar_protic_alcohol` (11.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `__OTHER__` (1%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (61%) | `C[SiH](C)O[SiH](C)` (38%) | `C[Si](C)(C)N=[N+]=` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Cc1cc(O[C@@H](C)C(` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1905  yield=50.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #11)

```
C=C(CCCCO)c1ccc(OC)cc1>>COc1ccc(C2(CN)CCCCO2)cc1.Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.9%) | `platinum` (5.0%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (89.7%) | `platinum_plate` (2.7%) | `platinum_generic` (2.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (56.3%) | `nickel` (31.6%) | `carbon` (10.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_plate` (35.8%) | `platinum_plate` (33.5%) | `platinum_generic` (20.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (93.6%) | `ABSENT` (6.2%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (67.9%) | `Li` (21.0%) | `ABSENT` (9.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (36.9%) | `ClO4` (34.4%) | `ABSENT` (13.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `imine` | `ABSENT` (33.0%) | `electrophilic_N_F` (2.1%) | `unparseable_text` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `ABSENT` (0.3%) | `polar_protic_alcohol` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (0%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1906  yield=50.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #12)

```
C=C(CCCO)c1ccc2c(c1)OCCO2>>Cl.NCC1(c2ccc3c(c2)OCCO3)CCCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `platinum` (1.7%) | `sacrificial_zinc` (1.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (98.4%) | `platinum_generic` (0.4%) | `reticulated_vitreous_carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `nickel` (55.3%) | `platinum` (37.9%) | `carbon` (5.3%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_plate` (52.4%) | `platinum_generic` (32.4%) | `platinum_wire` (4.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (56.7%) | `K` (19.5%) | `NBu4` (8.2%) | ✓ |
| 电解质 anion | 26 | `BF4` | `Br` (51.4%) | `ClO4` (16.9%) | `Cl` (12.7%) | ✗ |
| 试剂大类 | 103 | `imine` | `ABSENT` (32.8%) | `primary_amine` (2.0%) | `electrophilic_N_F` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (93.8%) | `ABSENT` (5.0%) | `polar_aprotic_sulfoxide` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `CO` (0%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `Cl` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1907  yield=49.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #13)

```
N=C(c1ccccc1)c1ccccc1.C=C(CCCO)c1ccc(OC)cc1>>COc1ccc(C2(CN=C(c3ccccc3)c3ccccc3)CCCO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (1.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (78.6%) | `carbon_generic` (14.1%) | `carbon_plate` (4.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (71.5%) | `nickel` (28.0%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (86.8%) | `nickel_plate` (7.3%) | `platinum_plate` (5.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (40.5%) | `NBu4` (38.3%) | `Li` (20.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (28.9%) | `Br` (17.5%) | `I` (15.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (50.5%) | `electrophilic_N_F` (1.5%) | `unparseable_text` (1.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `main_group_lewis_acid` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.6%) | `polar_protic_alcohol` (0.9%) | `polar_protic_acid` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (49%) | `O=C(O)C(F)(F)F` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1908  yield=43.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #14)

```
C=C(CCCO)c1ccc(-c2ccccc2)cc1>>Cl.NCC1(c2ccc(-c3ccccc3)cc2)CCCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.5%) | `platinum` (2.8%) | `sacrificial_zinc` (2.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (77.6%) | `carbon_generic` (11.6%) | `reticulated_vitreous_carbon` (3.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (49.8%) | `nickel` (48.3%) | `carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (73.4%) | `nickel_plate` (8.0%) | `nickel_foam` (8.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (49.1%) | `NBu4` (39.5%) | `NEt4` (3.9%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Br` (45.4%) | `ClO4` (22.0%) | `BF4` (14.1%) | ✗ |
| 试剂大类 | 103 | `imine` | `ABSENT` (29.9%) | `electrophilic_N_F` (2.0%) | `unparseable_text` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.6%) | `ABSENT` (2.3%) | `polar_aprotic_amide` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (0%) | `CN(C)C=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `[Br-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #1909  yield=43.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #15)

```
C=C(CCCO)c1ccc(OC)cc1>>COc1ccc(C2(CN)CCCO2)cc1.Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (91.6%) | `platinum` (5.9%) | `ABSENT` (2.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (94.3%) | `ABSENT` (2.1%) | `platinum_plate` (0.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `nickel` (47.7%) | `platinum` (41.6%) | `ABSENT` (4.9%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_plate` (45.0%) | `platinum_plate` (26.6%) | `platinum_generic` (11.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (93.6%) | `ABSENT` (5.5%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (44.1%) | `Li` (29.1%) | `Na` (14.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (34.2%) | `Br` (29.0%) | `ClO4` (16.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `imine` | `ABSENT` (34.8%) | `electrophilic_N_F` (1.9%) | `unparseable_text` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `pyridine_organocat` (0.1%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.1%) | `polar_protic_alcohol` (1.8%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (0%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1910  yield=41.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #16)

```
C=C(CCCO)c1ccc(OC)cc1>>COc1ccc(C2(CO)CCCO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (87.6%) | `ABSENT` (7.3%) | `platinum` (4.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.7%) | `ABSENT` (2.1%) | `unknown_electrode` (2.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `nickel` (76.9%) | `platinum` (14.8%) | `ABSENT` (4.7%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_plate` (86.9%) | `platinum_plate` (4.7%) | `platinum_generic` (2.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (89.5%) | `ABSENT` (9.9%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.5%) | `Na` (11.1%) | `Li` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (77.8%) | `Br` (17.4%) | `carboxylate` (1.4%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `main_group_lewis_acid` (0.3%) | `Co_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.4%) | `polar_protic_alcohol` (22.6%) | `polar_aprotic_amide` (4.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `CO` (1%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `__ABSENT__` (100%) | `BrC(Br)(Br)Br` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1911  yield=43.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #17)

```
C=C(CCCO)c1ccc2ccccc2c1>>Cl.NCC1(c2ccc3ccccc3c2)CCCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (2.4%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (90.7%) | `platinum_generic` (2.6%) | `carbon_generic` (2.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `nickel` (55.8%) | `platinum` (41.9%) | `carbon` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (52.8%) | `nickel_plate` (37.1%) | `platinum_plate` (4.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (74.2%) | `NEt4` (11.7%) | `NBu4` (7.9%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (60.7%) | `Br` (15.0%) | `BF4` (7.7%) | ✓ |
| 试剂大类 | 103 | `imine` | `ABSENT` (30.1%) | `diboron` (2.2%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (93.9%) | `ABSENT` (4.9%) | `polar_protic_alcohol` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `CO` (0%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `__ABSENT__` (100%) | `[Br-].[Na+]` (0%) | `BrC(Br)(Br)Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1912  yield=48.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #18)

```
O=C(O)c1ccc(Br)cc1.CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2OC(=O)c2ccc(Br)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `platinum` (1.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (95.0%) | `graphite_rod` (4.4%) | `platinum_generic` (0.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (72.7%) | `carbon` (13.8%) | `nickel` (7.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (93.1%) | `carbon_generic` (3.0%) | `platinum_plate` (2.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.4%) | `Na` (0.4%) | `NEt4` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (68.8%) | `Br` (22.1%) | `PF6` (4.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (20.4%) | `carboxylic_acid` (11.0%) | `primary_amine` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `Co_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.0%) | `polar_protic_alcohol` (1.9%) | `hfip` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (86%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (87%) | `Cc1ccc(S(=O)[O-])c` (1%) | `CC1(C)CCCC(C)(C)N1` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |

---

### Reaction #1913  yield=48.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #19)

```
C=C(CCCCO)c1ccc(OC)c(OC)c1>>COc1ccc(C2(CN)CCCCO2)cc1OC.Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.4%) | `platinum` (1.6%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (64.6%) | `reticulated_vitreous_carbon` (14.5%) | `carbon_generic` (8.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.2%) | `nickel` (16.3%) | `carbon` (9.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (55.9%) | `platinum_plate` (24.1%) | `nickel_plate` (15.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (93.0%) | `NBu4` (6.1%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (77.6%) | `BF4` (16.2%) | `ABSENT` (2.1%) | ✓ |
| 试剂大类 | 103 | `imine` | `ABSENT` (32.0%) | `electrophilic_N_F` (2.1%) | `unparseable_text` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.9%) | `polar_protic_alcohol` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (0%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1914  yield=50.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #20)

```
Cc1ccc(/C=C/CCO)cc1>>Cc1ccc([C@H]2OCC[C@@H]2O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `platinum` (2.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (53.1%) | `reticulated_vitreous_carbon` (16.4%) | `graphite_generic` (11.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.7%) | `carbon` (0.7%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.0%) | `platinum_generic` (25.4%) | `nickel_plate` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.3%) | `ABSENT` (0.5%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.7%) | `NEt4` (12.5%) | `K` (2.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (58.5%) | `carboxylate` (16.1%) | `Br` (12.8%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (7.8%) | `carboxylic_acid` (4.7%) | `alkali_sulfinate` (4.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.7%) | `ionic_organocat` (1.6%) | `organic_neutral_cat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.0%) | `halogenated_aliphatic` (2.2%) | `polar_protic_alcohol` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (100%) | `CCO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `O=C([O-])[O-].[K+]` | `__ABSENT__` (72%) | `O=C(O)C(F)(F)F` (2%) | `CC[SiH](CC)CC` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Pt]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1915  yield=53.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #21)

```
N=C(c1ccccc1)c1ccc(Br)cc1.CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2/N=C(\c2ccccc2)c2ccc(Br)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `platinum` (1.7%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (99.5%) | `graphite_rod` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.9%) | `sacrificial_zinc` (11.3%) | `sacrificial_iron` (8.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `graphite_plate` (0.2%) | `zinc_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.7%) | `NEt4` (2.9%) | `Na` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (71.8%) | `Br` (9.6%) | `SO4` (5.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (44.3%) | `unparseable_text` (1.6%) | `electrophilic_N_F` (1.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.6%) | `hfip` (2.1%) | `polar_protic_alcohol` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cc1ccc(S(=O)[O-])c` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1916  yield=59.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #22)

```
C=C(CCCCO)c1cc(C)c(OC)c(C)c1>>COc1c(C)cc(C2(CN)CCCCO2)cc1C.Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.4%) | `platinum` (1.3%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (48.2%) | `platinum_generic` (23.6%) | `graphite_rod` (13.9%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (55.7%) | `nickel` (37.9%) | `carbon` (4.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (72.2%) | `nickel_plate` (24.6%) | `nickel_generic` (0.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.3%) | `divided` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (46.6%) | `Li` (33.6%) | `NBu4` (16.9%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (45.7%) | `ClO4` (35.3%) | `BF4` (9.3%) | ✓ |
| 试剂大类 | 103 | `imine` | `ABSENT` (22.2%) | `electrophilic_N_F` (2.4%) | `unparseable_text` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.9%) | `ABSENT` (1.2%) | `polar_protic_alcohol` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `CO` (0%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `__ABSENT__` (100%) | `Cc1ccc(S(=O)(=O)O)` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #1917  yield=60.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #23)

```
O=C(O)c1ccc(F)cc1.CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2OC(=O)c2ccc(F)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (78.3%) | `graphite_rod` (20.3%) | `platinum_generic` (0.4%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (77.4%) | `nickel` (13.6%) | `carbon` (7.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (83.9%) | `nickel_plate` (10.4%) | `platinum_plate` (4.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.3%) | `Na` (2.8%) | `K` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (79.3%) | `Br` (11.8%) | `BF4` (4.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (22.3%) | `carboxylic_acid` (5.1%) | `tempo_mediator` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.1%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.5%) | `halogenated_aliphatic` (2.5%) | `polar_protic_alcohol` (1.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (40%) | `ClCCl` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (87%) | `CC(=O)O` (0%) | `CC1(C)CCCC(C)(C)N1` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl-].[Cl-].[Mn+2]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1918  yield=51.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #24)

```
N=C(c1ccccc1)c1ccccc1.Cc1ccc(/C=C/CCO)cc1>>Cc1ccc([C@H]2OCC[C@@H]2N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.0%) | `platinum` (7.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (93.2%) | `graphite_generic` (2.5%) | `graphite_rod` (2.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (70.4%) | `sacrificial_zinc` (12.4%) | `sacrificial_iron` (8.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (94.5%) | `zinc_generic` (1.3%) | `platinum_plate` (1.3%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.3%) | `NEt4` (5.5%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (66.2%) | `carboxylate` (10.3%) | `SO4` (6.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.4%) | `electrophilic_N_F` (1.8%) | `unparseable_text` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.2%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (91.5%) | `hfip` (3.3%) | `polar_protic_alcohol` (1.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (100%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cc1ccc(S(=O)[O-])c` (0%) | `O=C([O-])O.[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1919  yield=54.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #25)

```
O=C(O)c1ccccc1.CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2OC(=O)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.8%) | `platinum` (3.0%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (99.8%) | `graphite_rod` (0.1%) | `platinum_generic` (0.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (65.0%) | `carbon` (14.1%) | `nickel` (12.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (97.2%) | `carbon_generic` (2.3%) | `platinum_plate` (0.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.6%) | `Na` (3.0%) | `NEt4` (2.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (81.2%) | `Br` (8.3%) | `BF4` (5.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.6%) | `carboxylic_acid` (9.7%) | `imine` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (73.3%) | `hfip` (13.2%) | `polar_protic_alcohol` (4.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `O` (100%) | `CC#N` (100%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC1(C)CCCC(C)(C)N1` (59%) | `Cc1ccc(S(=O)[O-])c` (21%) | `__ABSENT__` (11%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1920  yield=59.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #26)

```
N=C(c1ccccc1)c1ccccc1.OCC/C=C/c1ccc(Oc2ccccc2)cc1>>c1ccc(Oc2ccc([C@H]3OCC[C@@H]3N=C(c3ccccc3)c3ccccc3)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.4%) | `platinum` (9.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (93.3%) | `graphite_generic` (3.0%) | `graphite_rod` (1.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (76.3%) | `sacrificial_zinc` (11.2%) | `nickel` (5.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (94.0%) | `platinum_plate` (3.8%) | `nickel_plate` (0.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.3%) | `NEt4` (1.4%) | `Na` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (71.6%) | `carboxylate` (6.4%) | `Br` (6.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (46.9%) | `electrophilic_N_F` (1.6%) | `unparseable_text` (1.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.5%) | `halogenated_aliphatic` (2.9%) | `polar_protic_alcohol` (2.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (99%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `N#Cc1c(C#N)c(-n2c3` (0%) | set ✓ / any ✓ |

---

### Reaction #1921  yield=56.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #27)

```
N=C(c1ccccc1)c1ccccc1.COc1ccc(/C=C/CCO)cc1Cl>>COc1ccc([C@H]2OCC[C@@H]2N=C(c2ccccc2)c2ccccc2)cc1Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (89.1%) | `graphite_generic` (8.5%) | `graphite_rod` (0.9%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (91.6%) | `carbon` (3.7%) | `nickel` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.1%) | `platinum_plate` (1.6%) | `graphite_plate` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.4%) | `NEt4` (2.4%) | `Na` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (74.2%) | `carboxylate` (8.0%) | `ClO4` (3.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (54.6%) | `electrophilic_N_F` (1.4%) | `unparseable_text` (1.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `hfip` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1922  yield=57.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #28)

```
CC(=O)O.C=C(CCCO)c1ccc(-c2ccccc2)cc1>>CC(=O)OCC1(c2ccc(-c3ccccc3)cc2)CCCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (80.2%) | `graphite_generic` (11.8%) | `unknown_electrode` (2.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.5%) | `nickel` (2.1%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.7%) | `platinum_plate` (1.1%) | `nickel_plate` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (53.7%) | `NBu4` (38.5%) | `NEt4` (4.7%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `Br` (36.0%) | `BF4` (32.3%) | `ClO4` (22.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (37.6%) | `acid_anhydride` (3.0%) | `diboron` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `pyridine_organocat` (0.1%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.5%) | `ABSENT` (1.4%) | `halogenated_aliphatic` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `CN(C)C=O` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Br-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Cc1cc(O[C@@H](C)C(` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #1923  yield=55.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #29)

```
OCC/C=C/c1ccc(Oc2ccccc2)cc1>>O[C@H]1CCO[C@@H]1c1ccc(Oc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (50.3%) | `graphite_rod` (20.7%) | `carbon_cloth` (12.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.6%) | `nickel` (1.8%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.0%) | `platinum_generic` (8.6%) | `nickel_plate` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.1%) | `NEt4` (4.3%) | `K` (1.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (32.5%) | `PF6` (26.6%) | `BF4` (23.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (13.4%) | `carboxylic_acid` (2.8%) | `electrophilic_N_F` (2.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `pyridine_organocat` (0.5%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.2%) | `polar_protic_alcohol` (1.2%) | `halogenated_aliphatic` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (81%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `O=C(O)O.[K]` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1924  yield=57.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #30)

```
C=C(CCCCO)c1ccc(OCCCC)cc1>>CCCCOc1ccc(C2(CN)CCCCO2)cc1.Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.9%) | `platinum` (1.7%) | `sacrificial_zinc` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (54.1%) | `carbon_generic` (34.6%) | `reticulated_vitreous_carbon` (5.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (60.3%) | `nickel` (32.5%) | `carbon` (5.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (81.8%) | `nickel_plate` (8.6%) | `platinum_plate` (2.6%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (93.4%) | `ABSENT` (6.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Li` (53.3%) | `NBu4` (45.1%) | `NEt4` (0.7%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (76.6%) | `BF4` (16.0%) | `Br` (2.9%) | ✗ |
| 试剂大类 | 103 | `imine` | `ABSENT` (41.4%) | `electrophilic_N_F` (1.8%) | `unparseable_text` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.4%) | `ABSENT` (0.4%) | `polar_protic_alcohol` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (0%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `[Br-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #1925  yield=55.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #31)

```
C=C(CCCCO)c1ccc(OC(C)(C)C)cc1>>Cl.NCC1(c2ccc(O)cc2)CCCCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.0%) | `sacrificial_zinc` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (97.3%) | `reticulated_vitreous_carbon` (1.0%) | `graphite_generic` (0.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (58.9%) | `nickel` (39.8%) | `copper` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (72.4%) | `nickel_plate` (15.4%) | `platinum_plate` (6.9%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (87.1%) | `ABSENT` (12.8%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (87.1%) | `NBu4` (12.2%) | `NEt4` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (92.7%) | `PF6` (2.4%) | `BF4` (2.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `imine` | `ABSENT` (32.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.9%) | `ABSENT` (7.7%) | `polar_aprotic_amide` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (99%) | `CN(C)C=O` (1%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `__ABSENT__` (100%) | `[Br-].[Na+]` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #1926  yield=65.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #32)

```
N=C(c1ccccc1)c1ccccc1.OCC/C=C/c1ccc2c(c1)CCO2>>c1ccc(C(=N[C@H]2CCO[C@@H]2c2ccc3c(c2)CCO3)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `platinum` (2.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (95.4%) | `graphite_rod` (1.7%) | `graphite_felt` (0.9%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.1%) | `carbon` (5.6%) | `sacrificial_zinc` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (94.9%) | `platinum_plate` (3.7%) | `graphite_plate` (0.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (57.9%) | `ABSENT` (35.6%) | `NEt4` (3.4%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (52.1%) | `ABSENT` (32.3%) | `carboxylate` (3.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (32.4%) | `alkali_formate` (1.8%) | `electrophilic_N_F` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.7%) | `halogenated_aliphatic` (1.7%) | `hfip` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (99%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `N#Cc1c(C#N)c(-n2c3` (0%) | set ✓ / any ✓ |

---

### Reaction #1927  yield=62.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #33)

```
N=C(c1ccccc1)c1ccccc1.COc1ccc(/C=C/CCO)cc1>>COc1ccc([C@H]2OCC[C@@H]2N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.0%) | `platinum` (4.8%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (99.5%) | `graphite_generic` (0.2%) | `graphite_rod` (0.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (66.4%) | `sacrificial_zinc` (12.1%) | `carbon` (7.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.9%) | `iron_generic` (0.3%) | `carbon_generic` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.5%) | `Na` (1.0%) | `NEt4` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (68.5%) | `carboxylate` (10.3%) | `Br` (5.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (38.7%) | `unparseable_text` (1.7%) | `electrophilic_N_F` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (90.0%) | `hfip` (3.8%) | `polar_protic_alcohol` (2.9%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `O` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C([O-])[O-].[Na+` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1cc[c]([Fe][c]2cc` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1928  yield=61.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #34)

```
N=C(c1ccccc1)c1ccccc1.COc1ccc(/C=C/CCO)cc1Br>>COc1ccc([C@H]2OCC[C@@H]2N=C(c2ccccc2)c2ccccc2)cc1Br
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.1%) | `platinum` (1.9%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (56.2%) | `graphite_generic` (20.6%) | `graphite_rod` (11.7%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.9%) | `carbon` (2.4%) | `nickel` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (82.3%) | `platinum_plate` (16.6%) | `graphite_plate` (0.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.8%) | `ABSENT` (3.0%) | `NEt4` (2.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (62.9%) | `ABSENT` (7.0%) | `PF6` (6.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (49.7%) | `electrophilic_N_F` (1.5%) | `unparseable_text` (1.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.0%) | `halogenated_aliphatic` (0.6%) | `hfip` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (100%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Na+]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1929  yield=64.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #35)

```
Cc1ccc(C(=N)c2ccccc2)cc1.CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2/N=C(\c2ccccc2)c2ccc(C)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.8%) | `platinum` (4.0%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (99.0%) | `graphite_rod` (0.5%) | `graphite_plate` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (52.9%) | `sacrificial_zinc` (22.5%) | `sacrificial_iron` (14.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.8%) | `zinc_generic` (1.2%) | `graphite_plate` (0.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.1%) | `NEt4` (4.1%) | `Na` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (60.1%) | `SO4` (14.2%) | `carboxylate` (8.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (41.2%) | `unparseable_text` (1.7%) | `electrophilic_N_F` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (91.1%) | `hfip` (4.9%) | `polar_protic_alcohol` (2.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (100%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cc1ccc(S(=O)[O-])c` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1930  yield=68.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #36)

```
COc1ccc(/C=C/CCO)cc1>>COc1ccc([C@H]2OCC[C@@H]2O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.1%) | `platinum` (1.3%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (64.2%) | `carbon_cloth` (10.8%) | `carbon_generic` (6.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.5%) | `stainless_steel` (2.2%) | `nickel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (76.0%) | `platinum_generic` (21.4%) | `platinum_wire` (1.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (0.8%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.6%) | `K` (6.8%) | `NEt4` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `Br` (35.8%) | `BF4` (33.3%) | `carboxylate` (20.1%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (10.2%) | `carboxylic_acid` (7.9%) | `electrophilic_N_F` (2.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.3%) | `ionic_organocat` (0.7%) | `pyridine_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.2%) | `polar_protic_alcohol` (0.9%) | `cyclic_ether` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (99%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `O=C([O-])[O-].[K+]` | `__ABSENT__` (80%) | `O=C(O)C(F)(F)F` (5%) | `CC(=O)[O-].[Na+]` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (1%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1931  yield=69.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #37)

```
C=C(CCCO)c1ccc(OCCCC)cc1>>CCCCOc1ccc(C2(CN)CCCO2)cc1.Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.3%) | `platinum` (3.0%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (79.7%) | `carbon_generic` (9.3%) | `reticulated_vitreous_carbon` (3.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (50.0%) | `nickel` (43.7%) | `carbon` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (72.6%) | `nickel_plate` (13.6%) | `platinum_wire` (3.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (97.1%) | `ABSENT` (2.8%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (54.1%) | `NBu4` (37.3%) | `Na` (4.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (48.8%) | `Br` (21.1%) | `BF4` (20.8%) | ✓ |
| 试剂大类 | 103 | `imine` | `ABSENT` (38.6%) | `electrophilic_N_F` (1.8%) | `unparseable_text` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.3%) | `polar_protic_alcohol` (2.0%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (0%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `[Br-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #1932  yield=63.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #38)

```
CC(=O)O.COc1ccc(/C=C/CCO)cc1OC>>COc1ccc([C@H]2OCC[C@@H]2OC(C)=O)cc1OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (83.1%) | `reticulated_vitreous_carbon` (5.0%) | `carbon_generic` (4.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.1%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (63.0%) | `platinum_generic` (37.0%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (75.5%) | `ABSENT` (14.4%) | `Na` (5.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (95.7%) | `Br` (1.4%) | `ABSENT` (1.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (27.5%) | `carboxylic_acid` (4.1%) | `unparseable_text` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `brønsted_acid_cat` (0.2%) | `Co_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.8%) | `halogenated_aliphatic` (2.7%) | `hfip` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (68%) | `ClCCl` (13%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #1933  yield=62.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #39)

```
C=C(CCCO)c1ccc(OC)c(OC)c1>>COc1ccc(C2(CN)CCCO2)cc1OC.Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.4%) | `platinum` (2.2%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (92.8%) | `reticulated_vitreous_carbon` (2.7%) | `platinum_generic` (0.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (68.7%) | `nickel` (25.6%) | `carbon` (3.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (41.1%) | `platinum_plate` (28.5%) | `nickel_plate` (25.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (84.2%) | `NBu4` (12.9%) | `NEt4` (0.9%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (52.5%) | `BF4` (34.5%) | `molecular_no_ion` (3.1%) | ✓ |
| 试剂大类 | 103 | `imine` | `ABSENT` (33.7%) | `electrophilic_N_F` (2.1%) | `unparseable_text` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.3%) | `polar_protic_alcohol` (0.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (0%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1934  yield=69.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #40)

```
N=C(c1ccc(F)cc1)c1ccc(F)cc1.CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2N=C(c2ccc(F)cc2)c2ccc(F)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.4%) | `platinum` (2.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (98.5%) | `graphite_rod` (0.7%) | `graphite_felt` (0.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.6%) | `sacrificial_zinc` (5.7%) | `sacrificial_iron` (4.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `platinum_plate` (0.2%) | `nickel_plate` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.4%) | `NEt4` (3.8%) | `Na` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (58.4%) | `Br` (13.0%) | `carboxylate` (10.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (40.7%) | `diboron` (1.8%) | `unparseable_text` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (93.6%) | `polar_protic_alcohol` (3.1%) | `hfip` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (98%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cc1ccc(S(=O)[O-])c` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1935  yield=69.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #41)

```
O=C(O)c1ccco1.CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2OC(=O)c2ccco2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (99.5%) | `graphite_rod` (0.3%) | `glassy_carbon` (0.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.9%) | `copper` (5.6%) | `nickel` (5.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.1%) | `platinum_plate` (0.9%) | `nickel_plate` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.2%) | `NEt4` (0.4%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (90.1%) | `Br` (6.7%) | `BF4` (2.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.7%) | `carboxylic_acid` (10.1%) | `imine` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `pyridine_organocat` (0.2%) | `Co_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.5%) | `polar_protic_alcohol` (2.3%) | `hfip` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (94%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `Cc1ccc(S(=O)[O-])c` (4%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1936  yield=68.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #42)

```
O=C(O)C1CC1.CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2OC(=O)C2CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (97.1%) | `graphite_rod` (2.8%) | `platinum_generic` (0.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.1%) | `nickel` (3.3%) | `copper` (1.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (95.4%) | `platinum_plate` (3.8%) | `nickel_plate` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (88.3%) | `ABSENT` (11.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (86.8%) | `ABSENT` (10.9%) | `NEt4` (1.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (88.0%) | `BF4` (4.1%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.9%) | `carboxylic_acid` (6.9%) | `imine` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `halogenated_aliphatic` (0.2%) | `hfip` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (65%) | `ClCCl` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (90%) | `Cc1ccc(S(=O)[O-])c` (2%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1937  yield=67.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #43)

```
CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2N)cc1.Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.3%) | `ABSENT` (5.5%) | `platinum` (2.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (99.8%) | `unknown_electrode` (0.1%) | `graphite_rod` (0.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (78.6%) | `ABSENT` (10.2%) | `nickel` (5.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.0%) | `zinc_generic` (0.7%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (72.4%) | `undivided` (27.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.7%) | `Li` (1.1%) | `K` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `carboxylate` (39.7%) | `BF4` (28.8%) | `PF6` (10.6%) | ✓ |
| 试剂大类 | 103 | `imine` | `imine` (24.6%) | `ABSENT` (6.8%) | `carboxylic_acid` (4.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `pyridine_organocat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.8%) | `hfip` (2.0%) | `polar_protic_alcohol` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (100%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `Cc1ccc(S(=O)[O-])c` (100%) | `O=C(O)C(F)(F)F` (0%) | `__ABSENT__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #1938  yield=66.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #44)

```
CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.9%) | `platinum` (1.5%) | `ABSENT` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (96.2%) | `graphite_rod` (1.6%) | `reticulated_vitreous_carbon` (0.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.4%) | `copper` (5.0%) | `nickel` (2.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (97.6%) | `platinum_plate` (1.1%) | `zinc_generic` (0.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (92.7%) | `ABSENT` (7.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.3%) | `K` (3.1%) | `NEt4` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (43.2%) | `Br` (30.8%) | `BF4` (17.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `carboxylic_acid` (14.5%) | `imine` (8.4%) | `ABSENT` (8.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `pyridine_organocat` (0.4%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.4%) | `polar_protic_alcohol` (1.7%) | `polar_aprotic_sulfoxide` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (100%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `N=C(c1ccccc1)c1ccc` + `Cl` | `Cc1ccc(S(=O)[O-])c` (98%) | `O=C(O)C(F)(F)F` (20%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Na+]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1939  yield=66.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #45)

```
O=C(O)c1cc2ccccc2o1.CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2OC(=O)c2cc3ccccc3o2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (80.4%) | `graphite_rod` (12.5%) | `carbon_plate` (4.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (91.2%) | `nickel` (4.6%) | `copper` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (64.5%) | `platinum_plate` (33.6%) | `nickel_plate` (1.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.0%) | `NEt4` (0.3%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (91.9%) | `BF4` (3.7%) | `Br` (2.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (29.2%) | `carboxylic_acid` (4.1%) | `unparseable_text` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `pyridine_organocat` (0.3%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `hfip` (0.9%) | `polar_protic_alcohol` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (4%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cc1ccc(S(=O)[O-])c` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1940  yield=65.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #46)

```
O=CO.CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2OC=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.1%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (33.4%) | `graphite_rod` (20.2%) | `carbon_cloth` (17.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.6%) | `nickel` (7.9%) | `copper` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (66.3%) | `platinum_generic` (32.5%) | `nickel_plate` (1.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.7%) | `ABSENT` (3.9%) | `NEt4` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `PF6` (71.6%) | `BF4` (9.1%) | `carboxylate` (8.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.4%) | `carboxylic_acid` (6.7%) | `bromide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `Cu_complex` (0.1%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.9%) | `polar_aprotic_amide` (19.5%) | `halogenated_aliphatic` (5.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `O` (71%) | `ClCCl` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (65%) | `O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #1941  yield=66.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #47)

```
OCC/C=C/c1ccc2c(c1)CCO2>>O[C@H]1CCO[C@@H]1c1ccc2c(c1)CCO2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (69.9%) | `carbon_generic` (22.4%) | `graphite_generic` (2.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.8%) | `carbon` (1.0%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (83.7%) | `platinum_generic` (16.0%) | `platinum_foil` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (39.7%) | `NBu4` (31.9%) | `NEt4` (25.4%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (41.3%) | `BF4` (29.9%) | `Br` (17.1%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (18.8%) | `carboxylic_acid` (4.6%) | `electrophilic_N_F` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.1%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CO` | `CC#N` (100%) | `O` (99%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `O=C([O-])[O-].[K+]` | `__ABSENT__` (99%) | `O=C(O)C(F)(F)F` (0%) | `[Cl-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #1942  yield=70.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #48)

```
N=C(c1ccccc1)c1ccccc1.CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.2%) | `platinum` (3.5%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (99.8%) | `graphite_generic` (0.0%) | `graphite_plate` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (50.1%) | `sacrificial_zinc` (26.4%) | `sacrificial_iron` (14.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.6%) | `iron_generic` (0.1%) | `zinc_generic` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.5%) | `NEt4` (2.3%) | `Na` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (59.5%) | `SO4` (15.8%) | `carboxylate` (9.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (37.2%) | `imine` (1.8%) | `unparseable_text` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (84.0%) | `hfip` (10.7%) | `polar_protic_alcohol` (3.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cc1ccc(S(=O)[O-])c` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `c1cc[c]([Fe][c]2cc` (0%) | set ✓ / any ✓ |

---

### Reaction #1943  yield=73.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #49)

```
N=C(c1ccccc1)c1ccccc1.COc1ccc(/C=C/CCO)cc1OC>>COc1ccc([C@H]2OCC[C@@H]2N=C(c2ccccc2)c2ccccc2)cc1OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `platinum` (2.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (60.7%) | `graphite_plate` (16.7%) | `graphite_rod` (14.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.5%) | `carbon` (2.6%) | `sacrificial_iron` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (81.9%) | `platinum_plate` (16.2%) | `graphite_plate` (0.9%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (83.1%) | `ABSENT` (9.0%) | `NEt4` (3.5%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (49.7%) | `SO4` (11.3%) | `carboxylate` (10.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (49.0%) | `electrophilic_N_F` (1.5%) | `unparseable_text` (1.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.5%) | `halogenated_aliphatic` (1.7%) | `hfip` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (99%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1944  yield=71.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #50)

```
N=C(c1ccccc1)c1ccccc1.CCCOc1ccc(/C=C/CCO)cc1>>CCCOc1ccc([C@H]2OCC[C@@H]2N=C(c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (99.7%) | `graphite_plate` (0.1%) | `graphite_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (56.6%) | `sacrificial_zinc` (24.8%) | `sacrificial_iron` (11.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.5%) | `iron_generic` (0.2%) | `zinc_generic` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (97.5%) | `NEt4` (1.7%) | `Na` (0.4%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (60.4%) | `SO4` (17.1%) | `carboxylate` (7.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (41.5%) | `unparseable_text` (1.7%) | `electrophilic_N_F` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.5%) | `hfip` (7.6%) | `polar_protic_alcohol` (4.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cc1ccc(S(=O)[O-])c` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `c1cc[c]([Fe][c]2cc` (0%) | set ✓ / any ✓ |

---

### Reaction #1945  yield=75.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #51)

```
CC(=O)O.CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2OC(C)=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (98.7%) | `graphite_rod` (0.6%) | `unknown_electrode` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.6%) | `copper` (2.4%) | `nickel` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `nickel_plate` (0.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.8%) | `K` (0.9%) | `Na` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (96.6%) | `PF6` (1.3%) | `Br` (1.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (17.4%) | `ABSENT` (14.6%) | `primary_amine` (1.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.2%) | `pyridine_organocat` (0.8%) | `Co_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (88.1%) | `hfip` (7.6%) | `polar_protic_alcohol` (3.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (70%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `Cc1ccc(S(=O)[O-])c` (39%) | `CC(=O)O` (1%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1946  yield=75.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_412-427.json) (反应 idx 在该 JSON 内 = #52)

```
COc1ccc(C(=N)c2ccc(OC)cc2)cc1.CCCCOc1ccc(/C=C/CCO)cc1>>CCCCOc1ccc([C@H]2OCC[C@@H]2N=C(c2ccc(OC)cc2)c2ccc(OC)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.8%) | `platinum` (3.0%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (99.7%) | `graphite_rod` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (63.8%) | `sacrificial_zinc` (14.3%) | `sacrificial_iron` (11.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.3%) | `zinc_generic` (0.2%) | `iron_generic` (0.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (98.5%) | `NEt4` (0.8%) | `Na` (0.4%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (66.1%) | `SO4` (10.5%) | `Br` (9.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (41.3%) | `unparseable_text` (1.7%) | `electrophilic_N_F` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.7%) | `hfip` (5.0%) | `polar_protic_alcohol` (3.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (99%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cc1ccc(S(=O)[O-])c` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `c1cc[c]([Fe][c]2cc` (0%) | set ✓ / any ✓ |

---

### Reaction #1947  yield=31.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(C=C2C(=O)c3ccccc3C2=O)cc1C>>Cc1ccc([C@@H]2[C@@H](c3ccc(C)c(C)c3)C3(C(=O)c4ccccc4C3=O)[C@@]3(O)c4ccccc4C(=O)[C@…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (61.0%) | `carbon_plate` (16.4%) | `graphite_rod` (10.4%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.3%) | `nickel` (1.1%) | `carbon` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (61.1%) | `platinum_plate` (38.7%) | `nickel_plate` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (73.3%) | `NEt4` (18.3%) | `ABSENT` (7.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (91.7%) | `ABSENT` (4.4%) | `ClO4` (2.5%) | ✓ |
| 试剂大类 | 103 | `ammonium_salt` | `ammonium_salt` (63.0%) | `ABSENT` (5.0%) | `electrophilic_N_F` (1.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ionic_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.8%) | `aqueous` (0.1%) | `cyclic_ether` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (90%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `CCCC[N+](CCCC)(CCC` (38%) | `__ABSENT__` (1%) | `[Cl-].[Na+]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #1948  yield=35.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json) (反应 idx 在该 JSON 内 = #1)

```
COc1ccc(C=C2C(=O)c3ccccc3C2=O)cc1>>COc1ccc([C@@H]2[C@@H](c3ccc(OC)cc3)C3(C(=O)c4ccccc4C3=O)[C@@]3(O)c4ccccc4C(=O)[C@@…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (92.7%) | `graphite_generic` (3.1%) | `graphite_rod` (2.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.7%) | `nickel` (2.5%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (3.4%) | `nickel_generic` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.1%) | `ABSENT` (13.3%) | `NEt4` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (82.9%) | `ABSENT` (11.3%) | `ClO4` (2.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ammonium_salt` | `ammonium_salt` (81.8%) | `ABSENT` (1.8%) | `electrophilic_N_F` (0.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ionic_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.2%) | `cyclic_ether` (0.2%) | `polar_aprotic_amide` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (98%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `CCCC[N+](CCCC)(CCC` (88%) | `O` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #1949  yield=31.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json) (反应 idx 在该 JSON 内 = #2)

```
COc1cccc(C=C2C(=O)c3ccccc3C2=O)c1>>COc1cccc([C@@H]2[C@@H](c3cccc(OC)c3)C3(C(=O)c4ccccc4C3=O)[C@@]3(O)c4ccccc4C(=O)[C@…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `graphite_generic` (53.5%) | `carbon_generic` (39.5%) | `graphite_rod` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.8%) | `carbon` (0.6%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (71.4%) | `platinum_plate` (28.3%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (47.6%) | `NBu4` (40.7%) | `ABSENT` (10.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (92.4%) | `ABSENT` (5.8%) | `ClO4` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ammonium_salt` | `ammonium_salt` (83.0%) | `ABSENT` (1.3%) | `electrophilic_N_F` (0.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ionic_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.8%) | `halogenated_aliphatic` (0.1%) | `cyclic_ether` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (99%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `CCCC[N+](CCCC)(CCC` (91%) | `CCCC[N+](CCCC)(CCC` (1%) | `__ABSENT__` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #1950  yield=41.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json) (反应 idx 在该 JSON 内 = #3)

```
Cc1ccccc1C=C1C(=O)c2ccccc2C1=O>>Cc1ccccc1[C@@H]1[C@@H](c2ccccc2C)C2(C(=O)c3ccccc3C2=O)[C@@]2(O)c3ccccc3C(=O)[C@@H]12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (1.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (69.2%) | `graphite_generic` (22.1%) | `graphite_rod` (4.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.8%) | `nickel` (2.7%) | `carbon` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.5%) | `platinum_plate` (1.3%) | `nickel_plate` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.3%) | `NEt4` (1.1%) | `Li` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (94.8%) | `ClO4` (2.0%) | `I` (1.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ammonium_salt` | `ammonium_salt` (31.6%) | `ABSENT` (7.8%) | `electrophilic_N_F` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.4%) | `polar_aprotic_amide` (0.2%) | `halogenated_aliphatic` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (58%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (3%) | `CCCC[N+](CCCC)(CCC` (2%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl][Au].c1ccc(P(c` (0%) | set ✓ / any ✓ |

---

### Reaction #1951  yield=47.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json) (反应 idx 在该 JSON 内 = #4)

```
Cc1ccc(C=C2C(=O)c3ccccc3C2=O)cc1>>Cc1ccc([C@@H]2[C@@H](c3ccc(C)cc3)C3(C(=O)c4ccccc4C3=O)[C@@]3(O)c4ccccc4C(=O)[C@@H]2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (96.0%) | `graphite_rod` (2.6%) | `graphite_generic` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.7%) | `nickel` (6.5%) | `carbon` (3.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.9%) | `platinum_plate` (2.2%) | `nickel_plate` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.3%) | `ABSENT` (13.8%) | `NEt4` (4.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (91.7%) | `ABSENT` (6.9%) | `ClO4` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ammonium_salt` | `ammonium_salt` (74.6%) | `ABSENT` (2.4%) | `chloride_anion` (0.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.3%) | `polar_aprotic_amide` (0.2%) | `aqueous` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (99%) | `CO` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `CCCC[N+](CCCC)(CCC` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #1952  yield=43.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json) (反应 idx 在该 JSON 内 = #5)

```
Cc1cccc(C=C2C(=O)c3ccccc3C2=O)c1>>Cc1cccc([C@@H]2[C@@H](c3cccc(C)c3)C3(C(=O)c4ccccc4C3=O)[C@@]3(O)c4ccccc4C(=O)[C@@H]…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (70.1%) | `graphite_rod` (15.4%) | `graphite_generic` (11.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.2%) | `nickel` (1.2%) | `carbon` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (87.8%) | `platinum_plate` (12.0%) | `nickel_plate` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.2%) | `NEt4` (7.2%) | `ABSENT` (4.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (97.8%) | `ABSENT` (1.5%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ammonium_salt` | `ammonium_salt` (83.7%) | `ABSENT` (1.7%) | `electrophilic_N_F` (0.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.1%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.8%) | `acyclic_ether` (0.0%) | `cyclic_ether` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (96%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `CCCC[N+](CCCC)(CCC` (87%) | `__ABSENT__` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #1953  yield=47.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json) (反应 idx 在该 JSON 内 = #6)

```
CC(C)(C)c1ccc(C=C2C(=O)c3ccccc3C2=O)cc1>>CC(C)(C)c1ccc([C@@H]2[C@@H](c3ccc(C(C)(C)C)cc3)C3(C(=O)c4ccccc4C3=O)[C@@]3(O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.4%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (95.8%) | `graphite_rod` (1.4%) | `graphite_felt` (0.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.8%) | `nickel` (8.2%) | `carbon` (6.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.2%) | `platinum_plate` (2.4%) | `nickel_generic` (0.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (67.6%) | `NEt4` (24.3%) | `ABSENT` (6.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (93.6%) | `ABSENT` (3.3%) | `ClO4` (1.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ammonium_salt` | `ammonium_salt` (69.4%) | `ABSENT` (2.1%) | `metal_oxide_oxidant` (0.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.4%) | `polar_aprotic_amide` (1.4%) | `cyclic_ether` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (75%) | `CO` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `CCCC[N+](CCCC)(CCC` (96%) | `__ABSENT__` (1%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1954  yield=48.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_570-579.json) (反应 idx 在该 JSON 内 = #7)

```
N#Cc1ccc(C=C2C(=O)c3ccccc3C2=O)cc1>>N#Cc1ccc([C@@H]2[C@@H](c3ccc(C#N)cc3)C3(C(=O)c4ccccc4C3=O)[C@@]3(O)c4ccccc4C(=O)[…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (96.7%) | `graphite_generic` (1.6%) | `graphite_rod` (1.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.6%) | `carbon` (4.4%) | `nickel` (1.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (97.8%) | `platinum_plate` (1.7%) | `graphite_rod` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (80.9%) | `ABSENT` (10.9%) | `NEt4` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.6%) | `ABSENT` (3.8%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ammonium_salt` | `ammonium_salt` (78.5%) | `ABSENT` (1.1%) | `chloride_anion` (0.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.1%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.6%) | `polar_aprotic_amide` (0.3%) | `halogenated_aliphatic` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (71%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `CCCC[N+](CCCC)(CCC` (74%) | `__ABSENT__` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #1955  yield=30.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #0)

```
N#CS.[Na].C=C(C)Cn1nc(-c2ccc(C)cc2)cc1-c1ccc(C)cc1>>Cc1ccc(-c2cc3n(n2)CC(C)(CSC#N)c2cc(C)ccc2-3)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.1%) | `platinum` (1.4%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (81.8%) | `graphite_felt` (14.0%) | `graphite_rod` (2.4%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.0%) | `carbon` (2.4%) | `nickel` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.0%) | `graphite_felt` (0.7%) | `platinum_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (46.5%) | `Li` (23.3%) | `K` (9.7%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `carboxylate` (67.8%) | `ClO4` (21.8%) | `BF4` (5.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.0%) | `thiocyanate` (3.0%) | `alkali_bicarbonate` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `main_group_lewis_acid` (32.9%) | `pyridine_organocat` (26.6%) | `ionic_organocat` (13.1%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `hfip` (94.7%) | `polar_aprotic_nitrile` (3.2%) | `halogenated_aliphatic` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (100%) | `O` (1%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (97%) | `N#C[S-].[Na+]` (1%) | `CC(=O)[O-].[K+]` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `F[B-](F)(F)F.c1ccc` (41%) | `CC1=Cc2ccccc2N(c2c` (10%) | `CCCC[N+](CCCC)(CCC` (7%) | set ✗ / any ✗ |

---

### Reaction #1956  yield=33.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #1)

```
O=S(=O)(S)c1ccccc1.[Na].C=C(C)Cn1nc(-c2ccc(OC)cc2)cc1-c1ccc(OC)cc1>>COc1ccc(-c2cc3n(n2)CC(C)(CS(=O)(=O)c2ccccc2)c2cc(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.7%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (50.0%) | `graphite_rod` (37.2%) | `carbon_rod` (9.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (89.5%) | `Na` (6.1%) | `K` (1.3%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `carboxylate` (57.3%) | `BF4` (18.6%) | `PF6` (12.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (36.3%) | `metal_oxide_oxidant` (1.8%) | `tellurium_reagent` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (92.0%) | `ionic_organocat` (3.3%) | `pyridine_organocat` (2.0%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (96.6%) | `halogenated_aliphatic` (1.0%) | `hfip` (0.9%) | ✓ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `ClCCl` (3%) | `O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `O=S([O-])O.[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #1957  yield=45.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #2)

```
N#CS.[Na].C=CCn1nc(-c2ccc(F)cc2)cc1-c1ccc(F)cc1>>N#CSCC1Cn2nc(-c3ccc(F)cc3)cc2-c2ccc(F)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.5%) | `platinum` (1.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_plate` (87.7%) | `graphite_felt` (5.7%) | `carbon_cloth` (2.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.3%) | `carbon` (17.5%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.1%) | `graphite_plate` (1.4%) | `graphite_generic` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Na` (53.7%) | `Li` (19.3%) | `molecular_no_ion` (11.6%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (83.2%) | `carboxylate` (12.9%) | `ClO4` (1.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (24.4%) | `carboxylic_acid` (2.5%) | `metal_oxide_oxidant` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (99.7%) | `pyridine_organocat` (0.2%) | `ionic_organocat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (89.6%) | `hfip` (3.9%) | `ABSENT` (3.4%) | ✓ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (95%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `CC1=Cc2ccccc2N(c2c` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #1958  yield=48.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #3)

```
O=S(=O)(S)c1ccccc1.[Na].C=C(C)Cn1nc(-c2ccc(Cl)cc2)cc1-c1ccc(Cl)cc1>>CC1(CS(=O)(=O)c2ccccc2)Cn2nc(-c3ccc(Cl)cc3)cc2-c2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (83.8%) | `graphite_rod` (12.7%) | `graphite_generic` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (71.9%) | `ABSENT` (9.5%) | `Na` (8.8%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `carboxylate` (68.4%) | `PF6` (9.1%) | `ABSENT` (6.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (30.0%) | `ammonium_salt` (2.3%) | `metal_oxide_oxidant` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (96.6%) | `pyridine_organocat` (1.3%) | `organic_neutral_cat` (0.6%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (98.9%) | `halogenated_aliphatic` (0.5%) | `hfip` (0.1%) | ✓ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `ClCCl` (21%) | `O` (14%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S([O-])O.[Na+]` (0%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=C1OC2(c3ccccc31)` (0%) | set ✗ / any ✗ |

---

### Reaction #1959  yield=56.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #4)

```
CS(=O)(=O)S.[Na].C=C(C)Cn1nc(-c2ccc(F)cc2)cc1-c1ccc(F)cc1>>CC1(CS(C)(=O)=O)Cn2nc(-c3ccc(F)cc3)cc2-c2ccc(F)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (57.9%) | `carbon_felt` (18.8%) | `graphite_generic` (13.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `stainless_steel` (7.7%) | `carbon` (3.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.1%) | `stainless_steel_generic` (0.3%) | `graphite_generic` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (56.3%) | `Na` (15.8%) | `NEt4` (6.4%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `BF4` (36.6%) | `carboxylate` (26.5%) | `molecular_no_ion` (11.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.8%) | `boron_lewis_acid` (9.4%) | `as_solvent_cyclic_ether` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ionic_organocat` (73.1%) | `ABSENT` (23.3%) | `pyridine_organocat` (1.1%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `halogenated_aliphatic` (46.8%) | `polar_aprotic_nitrile` (22.4%) | `polar_protic_alcohol` (10.4%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `ClCCl` (92%) | `O` (4%) | `OC(C(F)(F)F)C(F)(F` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (23%) | `[I-].[K+]` (5%) | `[Br-].[Na+]` (5%) | set ✗ / any ✗ |

---

### Reaction #1960  yield=59.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #5)

```
N#CS.[Na].C=CCCCn1cc(C(=O)O[C@H]2C[C@H]3CC[C@@H](C2)N3C)c2ccccc21>>CN1[C@@H]2CC[C@H]1C[C@@H](OC(=O)c1c3n(c4ccccc14)CC…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (85.9%) | `platinum` (9.4%) | `ABSENT` (3.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (37.7%) | `graphite_felt` (29.2%) | `unknown_electrode` (8.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `carbon` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.3%) | `platinum_generic` (0.6%) | `graphite_felt` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (85.9%) | `K` (11.5%) | `NEt4` (1.5%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `PF6` (55.5%) | `carboxylate` (21.9%) | `Br` (11.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.4%) | `alkali_carbonate` (6.3%) | `carboxylic_acid` (3.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (99.7%) | `Ir_complex` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `ketone` (89.9%) | `polar_aprotic_sulfoxide` (5.8%) | `polar_aprotic_nitrile` (2.1%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (95%) | `O` (16%) | `OC(C(F)(F)F)C(F)(F` (7%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O=C(O)C(F)(F)F` (1%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CC1=Cc2ccccc2N(c2c` (0%) | set ✗ / any ✗ |

---

### Reaction #1961  yield=57.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #6)

```
N#C[S-].[Na+].C=CCCCn1cc(C=O)c2ccccc21>>N#CSCC1CCCn2c1c(C=O)c1ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.0%) | `platinum` (26.6%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_felt` (76.4%) | `carbon_cloth` (7.5%) | `carbon_generic` (3.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.3%) | `carbon` (10.2%) | `nickel` (2.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (86.6%) | `graphite_felt` (10.1%) | `platinum_generic` (1.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (54.0%) | `ABSENT` (45.4%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (62.7%) | `K` (19.0%) | `Li` (16.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (69.3%) | `ClO4` (18.7%) | `Br` (5.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `alkali_carbonate` (5.1%) | `alkali_bicarbonate` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (88.9%) | `Ir_complex` (4.8%) | `organic_neutral_cat` (1.5%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `ketone` (80.7%) | `polar_aprotic_sulfoxide` (8.8%) | `polar_aprotic_amide` (3.6%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (96%) | `O` (90%) | `OC(C(F)(F)F)C(F)(F` (33%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=C(O)C(F)(F)F` (1%) | `O=C([O-])[O-].[K+]` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `CC1=Cc2ccccc2N(c2c` (1%) | `CC[C@H](C)[C@H]1CN` (0%) | set ✗ / any ✗ |

---

### Reaction #1962  yield=57.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #7)

```
O=S(=O)(S)c1ccccc1.[Na].C=C(C)Cn1nc(-c2ccc(F)cc2)cc1-c1ccc(F)cc1>>CC1(CS(=O)(=O)c2ccccc2)Cn2nc(-c3ccc(F)cc3)cc2-c2ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (90.8%) | `graphite_rod` (6.7%) | `graphite_generic` (1.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.1%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (54.9%) | `K` (16.0%) | `Na` (12.0%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `carboxylate` (52.4%) | `BF4` (12.3%) | `ClO4` (8.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.5%) | `boron_lewis_acid` (2.4%) | `metal_oxide_oxidant` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (87.0%) | `ionic_organocat` (7.0%) | `pyridine_organocat` (4.1%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (97.0%) | `halogenated_aliphatic` (1.2%) | `hfip` (0.5%) | ✓ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `ClCCl` (30%) | `O` (17%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `[Cl-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=C([O-])c1ccccc1-` (0%) | set ✗ / any ✗ |

---

### Reaction #1963  yield=63.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #8)

```
N#CS.[Na].C=CCn1nc(-c2ccc(Cl)cc2)cc1-c1ccc(Cl)cc1>>N#CSCC1Cn2nc(-c3ccc(Cl)cc3)cc2-c2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.4%) | `platinum` (2.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_plate` (81.5%) | `graphite_felt` (15.2%) | `graphite_generic` (0.9%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.2%) | `carbon` (11.2%) | `nickel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (93.7%) | `graphite_plate` (3.6%) | `graphite_felt` (1.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `H` (62.9%) | `Na` (23.6%) | `Li` (5.2%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `carboxylate` (89.4%) | `molecular_no_ion` (9.3%) | `OTf` (0.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (39.3%) | `metal_oxide_oxidant` (1.7%) | `tellurium_reagent` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `ionic_organocat` (0.0%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (95.4%) | `hfip` (3.4%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (98%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `[Br-].[H+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `CC1=Cc2ccccc2N(c2c` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #1964  yield=69.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #9)

```
N#CS.[Na].C=CCn1nc(-c2ccccc2)cc1-c1ccccc1>>N#CSCC1Cn2nc(-c3ccccc3)cc2-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `platinum` (1.6%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_plate` (47.2%) | `graphite_felt` (30.3%) | `carbon_cloth` (10.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.8%) | `carbon` (2.0%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.9%) | `platinum_generic` (0.5%) | `graphite_felt` (0.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `H` (36.2%) | `NBu4` (21.6%) | `Li` (16.7%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `carboxylate` (77.8%) | `molecular_no_ion` (16.3%) | `ClO4` (1.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (38.3%) | `unparseable_text` (1.8%) | `electrophilic_N_F` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (99.6%) | `pyridine_organocat` (0.2%) | `organic_neutral_cat` (0.1%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (81.0%) | `hfip` (17.0%) | `halogenated_aliphatic` (0.8%) | ✓ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (85%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `O=C([O-])O.[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `CC1=Cc2ccccc2N(c2c` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #1965  yield=68.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #10)

```
CS(=O)(=O)S.[Na].C=CCn1nc(-c2ccc(Cl)cc2)cc1-c1ccc(Cl)cc1>>CS(=O)(=O)CC1Cn2nc(-c3ccc(Cl)cc3)cc2-c2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.8%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_plate` (25.0%) | `graphite_rod` (24.0%) | `graphite_generic` (19.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (50.5%) | `carbon` (46.2%) | `nickel` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_plate` (63.5%) | `platinum_plate` (24.5%) | `graphite_generic` (5.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Na` (97.1%) | `Li` (1.8%) | `molecular_no_ion` (0.7%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (97.7%) | `carboxylate` (1.7%) | `OTf` (0.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (35.0%) | `boron_lewis_acid` (5.5%) | `sulfonic_acid` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `ionic_organocat` (0.3%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (98.5%) | `polar_protic_alcohol` (0.7%) | `aqueous` (0.3%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `O` (100%) | `[H+].[OH-]` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.[Li+].[O-][C` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].CC(=O)[` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #1966  yield=64.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #11)

```
CS(=O)(=O)S.[Na].C=CCn1nc(-c2ccc(F)cc2)cc1-c1ccc(F)cc1>>CS(=O)(=O)CC1Cn2nc(-c3ccc(F)cc3)cc2-c2ccc(F)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (50.3%) | `graphite_plate` (11.8%) | `graphite_generic` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (72.4%) | `carbon` (26.8%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_plate` (61.9%) | `platinum_plate` (32.4%) | `graphite_generic` (1.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Na` (97.7%) | `Li` (1.6%) | `molecular_no_ion` (0.5%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `molecular_no_ion` (99.8%) | `I` (0.1%) | `ClO4` (0.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.4%) | `boron_lewis_acid` (5.6%) | `sulfonic_acid` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (97.9%) | `ionic_organocat` (1.2%) | `pyridine_organocat` (0.4%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (95.1%) | `ABSENT` (1.6%) | `aqueous` (1.1%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `O` (99%) | `CC#N` (98%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CS(=O)(=O)O` (0%) | `CCN(CC)CC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `[Cl-].[Cl-].[Mn+2]` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✗ / any ✗ |

---

### Reaction #1967  yield=65.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #12)

```
O=S(=O)(S)c1ccccc1.[Na].C=C(C)Cn1nc(-c2ccccc2)cc1-c1ccccc1>>CC1(CS(=O)(=O)c2ccccc2)Cn2nc(-c3ccccc3)cc2-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `platinum` (2.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (82.8%) | `graphite_rod` (14.3%) | `graphite_generic` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.1%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.7%) | `platinum_generic` (0.3%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (39.7%) | `NEt4` (33.4%) | `K` (9.8%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `PF6` (30.4%) | `carboxylate` (27.9%) | `BF4` (9.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (24.8%) | `thiocyanate` (2.8%) | `metal_oxide_oxidant` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.0%) | `ionic_organocat` (8.9%) | `pyridine_organocat` (5.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (92.0%) | `hfip` (4.8%) | `halogenated_aliphatic` (0.8%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (98%) | `ClCCl` (5%) | `OC(C(F)(F)F)C(F)(F` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `O=S([O-])O.[Na+]` (0%) | `N#C[S-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (88%) | `CCCC[N+](CCCC)(CCC` (1%) | `F[B-](F)(F)F.c1ccc` (0%) | set ✓ / any ✓ |

---

### Reaction #1968  yield=64.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #13)

```
O=S(=O)(S)c1ccccc1.[Na].C=C(C)Cn1nc(-c2ccc(C)cc2)cc1-c1ccc(C)cc1>>Cc1ccc(-c2cc3n(n2)CC(C)(CS(=O)(=O)c2ccccc2)c2cc(C)c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.7%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (66.3%) | `graphite_rod` (28.6%) | `carbon_rod` (2.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (80.7%) | `NEt4` (14.2%) | `K` (1.6%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `PF6` (30.9%) | `carboxylate` (25.0%) | `ClO4` (23.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.3%) | `ammonium_salt` (2.3%) | `metal_oxide_oxidant` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.7%) | `pyridine_organocat` (3.3%) | `ionic_organocat` (2.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (97.4%) | `halogenated_aliphatic` (0.7%) | `ABSENT` (0.4%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `ClCCl` (3%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `O=S([O-])O.[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #1969  yield=63.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #14)

```
CS(=O)(=O)S.[Na].C=C(C)Cn1nc(-c2ccc(C)cc2)cc1-c1ccc(C)cc1>>Cc1ccc(-c2cc3n(n2)CC(C)(CS(C)(=O)=O)c2cc(C)ccc2-3)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.7%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (52.1%) | `graphite_rod` (38.3%) | `carbon_felt` (3.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `stainless_steel` (0.4%) | `carbon` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.1%) | `nickel_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (6.2%) | `ABSENT` (2.7%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `BF4` (74.9%) | `carboxylate` (8.5%) | `ClO4` (6.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (18.6%) | `boron_lewis_acid` (10.0%) | `metal_oxide_oxidant` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ionic_organocat` (48.9%) | `ABSENT` (43.2%) | `main_group_lewis_acid` (1.9%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `halogenated_aliphatic` (36.6%) | `polar_aprotic_nitrile` (25.6%) | `ABSENT` (24.6%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `ClCCl` (90%) | `OC(C(F)(F)F)C(F)(F` (17%) | `O` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (7%) | `CCCC[N+](CCCC)(CCC` (4%) | `[I-].[K+]` (2%) | set ✗ / any ✗ |

---

### Reaction #1970  yield=65.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #15)

```
CS(=O)(=O)S.[Na].C=C(C)Cn1nc(-c2ccc(Cl)cc2)cc1-c1ccc(Cl)cc1>>CC1(CS(C)(=O)=O)Cn2nc(-c3ccc(Cl)cc3)cc2-c2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (51.9%) | `graphite_rod` (22.3%) | `graphite_generic` (14.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.5%) | `carbon` (1.5%) | `stainless_steel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.3%) | `platinum_generic` (0.4%) | `nickel_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (54.8%) | `Na` (18.8%) | `ABSENT` (16.8%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `carboxylate` (45.3%) | `BF4` (26.7%) | `molecular_no_ion` (10.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (26.9%) | `boron_lewis_acid` (10.0%) | `diboron` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (81.9%) | `ionic_organocat` (14.2%) | `organic_neutral_cat` (1.1%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (59.6%) | `halogenated_aliphatic` (25.2%) | `polar_protic_alcohol` (6.1%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC#N` (83%) | `O` (51%) | `ClCCl` (10%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #1971  yield=67.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #16)

```
CS(=O)(=O)S.[Na].C=C(C)Cn1nc(-c2ccc(OC)cc2)cc1-c1ccc(OC)cc1>>COc1ccc(-c2cc3n(n2)CC(C)(CS(C)(=O)=O)c2cc(OC)ccc2-3)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (45.1%) | `carbon_cloth` (31.3%) | `carbon_felt` (10.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.4%) | `carbon` (1.4%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (91.4%) | `Na` (5.5%) | `Li` (1.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (68.6%) | `carboxylate` (18.0%) | `ClO4` (4.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (26.5%) | `boron_lewis_acid` (5.7%) | `metal_oxide_oxidant` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (58.2%) | `ionic_organocat` (33.8%) | `ferrocene_mediator` (3.4%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (42.4%) | `halogenated_aliphatic` (26.1%) | `hfip` (8.3%) | ✓ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC#N` (65%) | `OC(C(F)(F)F)C(F)(F` (31%) | `ClCCl` (16%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O=C([O-])[O-].[Na+` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (98%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #1972  yield=70.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #17)

```
O=S(=O)(S)c1ccccc1.[Na].C=CCn1nc(-c2ccc(Cl)cc2)cc1-c1ccc(Cl)cc1>>O=S(=O)(CC1Cn2nc(-c3ccc(Cl)cc3)cc2-c2ccc(Cl)cc21)c1c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `platinum` (1.1%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_plate` (47.7%) | `graphite_rod` (15.8%) | `graphite_generic` (12.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (75.1%) | `carbon` (24.5%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (83.4%) | `graphite_plate` (11.7%) | `platinum_generic` (2.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Na` (95.5%) | `Li` (3.5%) | `NBu4` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (92.8%) | `carboxylate` (4.4%) | `I` (1.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (32.9%) | `metal_oxide_oxidant` (1.8%) | `tellurium_reagent` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `ionic_organocat` (0.0%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (99.8%) | `aqueous` (0.1%) | `polar_aprotic_sulfoxide` (0.0%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (99%) | `[H+].[OH-]` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O.O.O.[Li+].[O-][C` (0%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `CC(=O)[O-].CC(=O)[` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✗ / any ✗ |

---

### Reaction #1973  yield=80.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #18)

```
CS(=O)(=O)S.[Na].C=CCCCn1cc(C(=O)OCC)cn1>>CCOC(=O)c1cnn2c1C(CS(C)(=O)=O)CCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_felt` (52.1%) | `reticulated_vitreous_carbon` (20.6%) | `carbon_cloth` (13.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (78.4%) | `nickel` (13.9%) | `carbon` (7.4%) | ✓ |
| 阴极 (细类) | 49 | `graphite_felt` | `platinum_plate` (93.4%) | `nickel_foam` (4.4%) | `graphite_rod` (1.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `divided` (1.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (55.6%) | `ABSENT` (41.9%) | `K` (1.7%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (67.5%) | `PF6` (21.8%) | `I` (3.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (90.2%) | `as_solvent_halogenated_aliphat` (0.4%) | `carboxylic_acid` (0.3%) | ✗ |
| 催化剂大类 | 49 | `organic_neutral_cat` | `Ir_complex` (51.2%) | `ABSENT` (18.2%) | `thianthrene_phenothiazine_cat` (18.2%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `ABSENT` (61.9%) | `ketone` (24.5%) | `polar_aprotic_nitrile` (10.4%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (100%) | `O` (0%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)O.[K]` (38%) | `__ABSENT__` (18%) | `CCCC[N+](CCCC)(CCC` (8%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `c1cc[c-]2->[Ir+3]3` (64%) | `__ABSENT__` (22%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✗ / any ✗ |

---

### Reaction #1974  yield=80.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #19)

```
N#CS.[Na].C=C(C)Cn1nc(-c2ccccc2)cc1-c1ccccc1>>CC1(CSC#N)Cn2nc(-c3ccccc3)cc2-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.0%) | `ABSENT` (2.3%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (65.7%) | `graphite_felt` (33.7%) | `graphite_rod` (0.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.6%) | `nickel` (2.9%) | `carbon` (2.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (58.8%) | `graphite_felt` (40.8%) | `platinum_generic` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.4%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (68.3%) | `NBu4` (9.0%) | `K` (8.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `carboxylate` (60.5%) | `ClO4` (29.2%) | `BF4` (2.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (27.1%) | `thiocyanate` (4.7%) | `alkali_bicarbonate` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `main_group_lewis_acid` (43.1%) | `pyridine_organocat` (19.1%) | `ionic_organocat` (13.9%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `hfip` (99.4%) | `polar_aprotic_nitrile` (0.3%) | `nitroalkane` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (100%) | `O` (0%) | `ClCCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)[O-].[K+]` (65%) | `__ABSENT__` (20%) | `N#C[S-].[Na+]` (14%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `CC1=Cc2ccccc2N(c2c` (84%) | `F[B-](F)(F)F.c1ccc` (17%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✗ / any ✗ |

---

### Reaction #1975  yield=71.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #20)

```
O=S(=O)(S)c1ccccc1.[Na].C=CCn1nc(-c2ccc(F)cc2)cc1-c1ccc(F)cc1>>O=S(=O)(CC1Cn2nc(-c3ccc(F)cc3)cc2-c2ccc(F)cc21)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (62.5%) | `graphite_plate` (12.4%) | `graphite_felt` (9.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (78.5%) | `carbon` (21.4%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (71.5%) | `graphite_plate` (21.9%) | `platinum_generic` (3.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Na` (92.1%) | `Li` (7.3%) | `molecular_no_ion` (0.2%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (99.5%) | `I` (0.2%) | `ClO4` (0.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.3%) | `sulfonic_acid` (3.1%) | `diboron` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `ionic_organocat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (99.5%) | `ABSENT` (0.2%) | `aqueous` (0.1%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (99%) | `[H+].[OH-]` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CS(=O)(=O)O` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `[Cl-].[Cl-].[Mn+2]` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #1976  yield=79.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #21)

```
O=S(=O)(S)c1ccccc1.[Na].C=CCCCn1cc(C(=O)O[C@H]2C[C@H]3CC[C@@H](C2)N3C)c2ccccc21>>CN1[C@@H]2CC[C@H]1C[C@@H](OC(=O)c1c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (72.0%) | `platinum` (24.9%) | `sacrificial_magnesium` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (30.2%) | `platinum_plate` (19.2%) | `graphite_felt` (10.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.7%) | `carbon` (1.9%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (52.2%) | `platinum_plate` (47.1%) | `platinum_wire` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (88.4%) | `K` (5.9%) | `Na` (4.2%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (58.6%) | `PF6` (20.5%) | `Br` (11.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.4%) | `alkali_carbonate` (7.0%) | `metal_oxide_oxidant` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (100.0%) | `triarylamine_radical_cat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `ketone` (73.3%) | `polar_aprotic_nitrile` (21.6%) | `polar_aprotic_sulfoxide` (1.8%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (91%) | `O` (13%) | `CC#N` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O=C([O-])[O-].[K+]` (0%) | `C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Ir].[c-]1ccccc1-c` (0%) | set ✗ / any ✗ |

---

### Reaction #1977  yield=76.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #22)

```
N#CS.[Na].C=CCCCn1cc(C#N)c2ccccc21>>N#CSCC1CCCn2c1c(C#N)c1ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `ABSENT` (1.2%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (56.9%) | `graphite_felt` (35.6%) | `unknown_electrode` (2.4%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.4%) | `carbon` (1.1%) | `stainless_steel` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.0%) | `graphite_felt` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (75.2%) | `K` (22.2%) | `NEt4` (1.4%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `PF6` (73.0%) | `carboxylate` (12.7%) | `Br` (7.2%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (13.8%) | `carboxylic_acid` (3.2%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (84.2%) | `Ir_complex` (4.3%) | `organic_neutral_cat` (4.1%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_sulfoxide` (55.1%) | `ketone` (25.3%) | `polar_aprotic_nitrile` (12.3%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `O` (66%) | `CS(C)=O` (44%) | `CC#N` (34%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O.O.O.[Li+].[O-][C` | `__ABSENT__` (96%) | `O=C(O)C(F)(F)F` (3%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `CC1=Cc2ccccc2N(c2c` (0%) | `O=C([O-])c1ccccc1-` (0%) | set ✗ / any ✗ |

---

### Reaction #1978  yield=75.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #23)

```
O=S(=O)(S)c1ccccc1.[Na].C=CCCCn1cc(C(=O)OC)c2ccccc21>>COC(=O)c1c2n(c3ccccc13)CCCC2CS(=O)(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (89.1%) | `platinum` (9.5%) | `sacrificial_magnesium` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (47.2%) | `platinum_plate` (26.9%) | `graphite_felt` (8.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `carbon` (2.5%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.6%) | `platinum_generic` (1.2%) | `platinum_wire` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (98.5%) | `K` (0.9%) | `Li` (0.3%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `PF6` (53.7%) | `Br` (23.1%) | `ClO4` (20.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.3%) | `alkali_carbonate` (4.6%) | `metal_oxide_oxidant` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `Ir_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `ketone` (78.4%) | `polar_aprotic_nitrile` (11.3%) | `polar_aprotic_amide` (4.0%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (30%) | `CC#N` (5%) | `O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O=C([O-])[O-].[K+]` (1%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `[Ir].[c-]1ccccc1-c` (0%) | `CC[C@H](C)[C@H]1CN` (0%) | set ✗ / any ✗ |

---

### Reaction #1979  yield=77.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #24)

```
O=S(=O)(S)c1ccccc1.[Na].C=CCn1nc(-c2ccccc2)cc1-c1ccccc1>>O=S(=O)(CC1Cn2nc(-c3ccccc3)cc2-c2ccccc21)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.0%) | `platinum` (4.6%) | `sacrificial_aluminum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (86.1%) | `graphite_generic` (4.5%) | `graphite_plate` (3.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.4%) | `carbon` (2.9%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (93.4%) | `platinum_generic` (5.4%) | `graphite_plate` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Na` (88.1%) | `Li` (7.1%) | `NBu4` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (85.1%) | `I` (9.6%) | `ClO4` (2.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.4%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (98.6%) | `ABSENT` (0.4%) | `polar_protic_alcohol` (0.2%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (94%) | `ClCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `CS(=O)(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✗ / any ✗ |

---

### Reaction #1980  yield=71.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #25)

```
CS(=O)(=O)S.[Na].C=CCCCn1cc(C=O)c2ccccc21>>CS(=O)(=O)CC1CCCn2c1c(C=O)c1ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (52.1%) | `platinum` (47.6%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_felt` (37.1%) | `platinum_plate` (29.8%) | `carbon_cloth` (15.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.7%) | `nickel` (3.5%) | `carbon` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.8%) | `nickel_foam` (1.4%) | `platinum_wire` (1.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.0%) | `divided` (2.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (65.9%) | `K` (30.1%) | `NEt4` (2.5%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (86.2%) | `PF6` (6.4%) | `BF4` (2.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.3%) | `sulfonic_acid` (4.5%) | `diboron` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `Ir_complex` (0.2%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `ketone` (53.5%) | `polar_aprotic_nitrile` (19.2%) | `polar_aprotic_sulfoxide` (15.9%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `O` (99%) | `CC(C)=O` (33%) | `CC#N` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `O` (1%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `CC[C@H](C)[C@H]1CN` (0%) | `O.O.[K+].[K+].[O]=` (0%) | set ✗ / any ✗ |

---

### Reaction #1981  yield=71.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #26)

```
CS(=O)(=O)S.[Na].C=C(C)Cn1nc(-c2ccccc2)cc1-c1ccccc1>>CC1(CS(C)(=O)=O)Cn2nc(-c3ccccc3)cc2-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `platinum` (1.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (81.9%) | `graphite_rod` (11.4%) | `graphite_generic` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.5%) | `stainless_steel` (0.9%) | `nickel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.6%) | `platinum_generic` (0.4%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (36.4%) | `ABSENT` (19.5%) | `NEt4` (18.5%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `BF4` (34.2%) | `ABSENT` (22.4%) | `carboxylate` (17.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.1%) | `boron_lewis_acid` (2.5%) | `thiocyanate` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ionic_organocat` (73.2%) | `ABSENT` (6.4%) | `organic_neutral_cat` (6.3%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (59.5%) | `hfip` (16.6%) | `halogenated_aliphatic` (7.3%) | ✓ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC#N` (68%) | `OC(C(F)(F)F)C(F)(F` (28%) | `ClCCl` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)[O-].[K+]` (0%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `CCCC[N+](CCCC)(CCC` (1%) | `O=C([O-])c1ccccc1-` (1%) | `[I-].[K+]` (1%) | set ✗ / any ✗ |

---

### Reaction #1982  yield=78.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #27)

```
N#CS.[Na].C=C(C)Cn1nc(-c2ccc(Cl)cc2)cc1-c1ccc(Cl)cc1>>CC1(CSC#N)Cn2nc(-c3ccc(Cl)cc3)cc2-c2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.1%) | `platinum` (1.2%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (84.2%) | `graphite_felt` (13.8%) | `graphite_plate` (0.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.2%) | `carbon` (4.5%) | `nickel` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (97.0%) | `graphite_felt` (2.0%) | `platinum_generic` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (29.6%) | `H` (22.5%) | `Li` (12.5%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `carboxylate` (97.1%) | `BF4` (0.8%) | `ClO4` (0.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (30.3%) | `thiocyanate` (2.4%) | `alkali_bicarbonate` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `pyridine_organocat` (33.4%) | `ABSENT` (23.5%) | `main_group_lewis_acid` (14.9%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `hfip` (95.1%) | `polar_aprotic_nitrile` (3.5%) | `halogenated_aliphatic` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (100%) | `O` (5%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)[O-].[K+]` (0%) | `N#C[S-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `F[B-](F)(F)F.c1ccc` (24%) | `CC1=Cc2ccccc2N(c2c` (11%) | `Cn1cncc1-c1c(F)cnc` (6%) | set ✗ / any ✗ |

---

### Reaction #1983  yield=72.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #28)

```
N#CS.[Na].C=C(C)Cn1nc(-c2ccc(F)cc2)cc1-c1ccc(F)cc1>>CC1(CSC#N)Cn2nc(-c3ccc(F)cc3)cc2-c2ccc(F)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `ABSENT` (0.8%) | `platinum` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (96.4%) | `graphite_felt` (1.8%) | `graphite_plate` (0.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.8%) | `carbon` (10.9%) | `stainless_steel` (4.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.0%) | `graphite_felt` (0.5%) | `graphite_generic` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (25.2%) | `K` (20.9%) | `NH4` (15.0%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `carboxylate` (79.5%) | `ClO4` (9.1%) | `BF4` (3.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.9%) | `thiocyanate` (2.8%) | `boron_lewis_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ionic_organocat` (42.7%) | `pyridine_organocat` (25.6%) | `ABSENT` (18.5%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `hfip` (88.7%) | `polar_aprotic_nitrile` (4.9%) | `halogenated_aliphatic` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (100%) | `ClCCl` (4%) | `O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `N#C[S-].[Na+]` (0%) | `[F-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `CC1=Cc2ccccc2N(c2c` (5%) | `F[B-](F)(F)F.c1ccc` (3%) | `Cc1cc(C)c(-c2c3ccc` (2%) | set ✗ / any ✗ |

---

### Reaction #1984  yield=84.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #29)

```
CS(=O)(=O)S.[Na].C=CCCCn1cc(C(C)=O)c2ccccc21>>CC(=O)c1c2n(c3ccccc13)CCCC2CS(C)(=O)=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (91.0%) | `platinum` (8.9%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_felt` (29.4%) | `platinum_plate` (19.9%) | `graphite_rod` (17.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (87.3%) | `platinum_generic` (12.6%) | `platinum_wire` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `divided` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (98.6%) | `K` (0.7%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (95.4%) | `PF6` (2.4%) | `ClO4` (1.2%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (11.2%) | `diboron` (2.5%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (50.6%) | `ketone` (21.1%) | `polar_aprotic_amide` (13.8%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `O` (68%) | `CC#N` (34%) | `CS(C)=O` (11%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O.O.O.[Li+].[O-][C` | `__ABSENT__` (99%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✗ / any ✗ |

---

### Reaction #1985  yield=83.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #30)

```
CS(=O)(=O)S.[Na].C=CCCCn1cc(C(=O)OC)c2ccccc21>>COC(=O)c1c2n(c3ccccc13)CCCC2CS(C)(=O)=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.2%) | `platinum` (2.6%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (46.8%) | `graphite_felt` (22.5%) | `reticulated_vitreous_carbon` (12.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.2%) | `nickel` (0.4%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.7%) | `platinum_generic` (0.2%) | `platinum_wire` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (95.6%) | `divided` (4.1%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (98.7%) | `K` (0.7%) | `NEt4` (0.4%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (46.6%) | `PF6` (37.4%) | `BF4` (10.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `alkali_carbonate` (6.6%) | `carboxylic_acid` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (89.5%) | `Ir_complex` (4.7%) | `organic_neutral_cat` (3.6%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `ketone` (90.8%) | `polar_aprotic_amide` (3.2%) | `polar_aprotic_nitrile` (2.5%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (68%) | `OCC(F)(F)F` (5%) | `O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O=C([O-])[O-].[K+]` (6%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `[Ir].[c-]1ccccc1-c` (0%) | `CC[C@H](C)[C@H]1CN` (0%) | set ✗ / any ✗ |

---

### Reaction #1986  yield=86.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #31)

```
N#CS.[Na].C=CCCCn1cc(C(C)=O)c2ccccc21>>CC(=O)c1c2n(c3ccccc13)CCCC2CSC#N
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.7%) | `platinum` (10.0%) | `ABSENT` (1.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_felt` (28.1%) | `platinum_plate` (24.8%) | `glassy_carbon` (10.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.5%) | `carbon` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.2%) | `platinum_generic` (0.8%) | `platinum_wire` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (99.1%) | `K` (0.4%) | `NEt4` (0.3%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `Br` (76.9%) | `PF6` (11.7%) | `carboxylate` (4.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.9%) | `carboxylic_acid` (2.4%) | `metal_oxide_oxidant` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `Fe_complex` (0.0%) | ✗ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_sulfoxide` (38.0%) | `ketone` (32.7%) | `polar_aprotic_nitrile` (15.9%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CS(C)=O` (88%) | `O` (74%) | `CC#N` (4%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `O=C(O)C(F)(F)F` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #1987  yield=81.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #32)

```
CS(=O)(=O)S.[Na].C=CCn1nc(-c2ccccc2)cc1-c1ccccc1>>CS(=O)(=O)CC1Cn2nc(-c3ccccc3)cc2-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.0%) | `platinum` (2.8%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_rod` (70.1%) | `carbon_rod` (9.8%) | `graphite_generic` (7.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.3%) | `carbon` (1.0%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (78.2%) | `platinum_generic` (19.4%) | `platinum_foil` (0.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Na` (93.6%) | `Li` (2.4%) | `NBu4` (1.6%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (95.7%) | `I` (1.2%) | `ABSENT` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.0%) | `boron_lewis_acid` (2.4%) | `sulfonic_acid` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (98.9%) | `ionic_organocat` (0.4%) | `organic_neutral_cat` (0.2%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (97.0%) | `ABSENT` (0.9%) | `polar_protic_alcohol` (0.6%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (94%) | `ClCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl-].[Cl-].[Ni+2]` (0%) | set ✗ / any ✗ |

---

### Reaction #1988  yield=90.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #33)

```
O=S(=O)(S)c1ccccc1.[Na].C=CCCCn1cc(C=O)c2ccccc21>>O=Cc1c2n(c3ccccc13)CCCC2CS(=O)(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (71.2%) | `carbon` (28.3%) | `sacrificial_aluminum` (0.2%) | ✓ |
| 阳极 (细类) | 43 | `graphite_felt` | `platinum_plate` (80.9%) | `platinum_generic` (6.8%) | `carbon_rod` (3.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.7%) | `carbon` (4.5%) | `nickel` (1.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.3%) | `platinum_generic` (0.8%) | `platinum_wire` (0.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (78.3%) | `K` (17.7%) | `Li` (1.8%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Br` (42.2%) | `PF6` (36.5%) | `ClO4` (18.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.5%) | `sulfonic_acid` (5.3%) | `alkali_bicarbonate` (2.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.0%) | `ionic_organocat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (53.6%) | `ketone` (19.1%) | `polar_aprotic_sulfoxide` (18.9%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `O` (100%) | `CC#N` (65%) | `CS(C)=O` (25%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O=C1CCC(=O)N1Br` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `O.O.[K+].[K+].[O]=` (0%) | `[Ir].[c-]1ccccc1-c` (0%) | set ✗ / any ✗ |

---

### Reaction #1989  yield=81.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #34)

```
O=S(=O)(S)c1ccccc1.[Na].C=CCCCn1cc(C(C)=O)c2ccccc21>>CC(=O)c1c2n(c3ccccc13)CCCC2CS(=O)(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (77.0%) | `platinum` (21.7%) | `sacrificial_magnesium` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `platinum_plate` (50.7%) | `platinum_generic` (13.4%) | `graphite_felt` (6.9%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.0%) | `carbon` (0.8%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (62.8%) | `platinum_generic` (37.1%) | `platinum_wire` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (98.0%) | `K` (1.1%) | `Li` (0.4%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `Br` (70.8%) | `ClO4` (17.3%) | `PF6` (9.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.3%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `Fe_complex` (0.0%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (64.9%) | `ketone` (17.9%) | `polar_aprotic_sulfoxide` (7.7%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `O` (64%) | `CC#N` (41%) | `CS(C)=O` (33%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `C` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `[Ir].[c-]1ccccc1-c` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✗ / any ✗ |

---

### Reaction #1990  yield=95.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #35)

```
N#CS.[Na].C=CCCCn1cc(C(=O)OC)c2ccccc21>>COC(=O)c1c2n(c3ccccc13)CCCC2CSC#N
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (91.8%) | `platinum` (4.5%) | `ABSENT` (3.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (60.1%) | `graphite_felt` (18.9%) | `unknown_electrode` (7.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `carbon` (2.0%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `platinum_wire` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (91.3%) | `ABSENT` (8.3%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (98.3%) | `K` (0.7%) | `NEt4` (0.7%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `PF6` (54.9%) | `BF4` (16.8%) | `carboxylate` (13.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.2%) | `carboxylic_acid` (4.1%) | `alkali_carbonate` (3.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (87.1%) | `Ir_complex` (4.4%) | `organic_neutral_cat` (2.1%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `ketone` (79.6%) | `polar_aprotic_sulfoxide` (6.0%) | `tfe` (4.1%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (79%) | `CC(C)=O` (32%) | `C1CCOC1` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `O=C(O)C(F)(F)F` (4%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `[Ir].[c-]1ccccc1-c` (0%) | `CC1=Cc2ccccc2N(c2c` (0%) | set ✗ / any ✗ |

---

### Reaction #1991  yield=93.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_1_598-613.json) (反应 idx 在该 JSON 内 = #36)

```
CS(=O)(=O)S.[Na].C=CCCCn1cc(C(=O)O[C@H]2C[C@H]3CC[C@@H](C2)N3C)c2ccccc21>>CN1[C@@H]2CC[C@H]1C[C@@H](OC(=O)c1c3n(c4ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (82.7%) | `platinum` (16.7%) | `sacrificial_zinc` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_cloth` (38.2%) | `graphite_felt` (28.8%) | `platinum_plate` (6.7%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `nickel` (0.2%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (83.6%) | `platinum_generic` (15.5%) | `nickel_foam` (0.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `divided` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (91.1%) | `K` (5.8%) | `Na` (1.9%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `PF6` (37.0%) | `Br` (36.2%) | `ClO4` (15.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (10.8%) | `ABSENT` (9.3%) | `diboron` (2.2%) | ✓ |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (99.8%) | `organic_neutral_cat` (0.1%) | `Ir_complex` (0.0%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `ketone` (90.4%) | `polar_aprotic_nitrile` (6.2%) | `polar_aprotic_amide` (1.5%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (97%) | `O` (11%) | `CC#N` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (40%) | `__ABSENT__` (1%) | `O=C([O-])[O-].[Cs+` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `S=P(Oc1ccccc1)(Oc1` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CC[C@H](C)[C@H]1CN` (0%) | set ✗ / any ✗ |

---

### Reaction #1992  yield=30.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccc(C(=O)OC)cc1)C(F)(F)F>>COC(=O)c1ccc(C(O)(CN=[N+]=[N-])C(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.4%) | `platinum` (5.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (59.4%) | `graphite_generic` (21.5%) | `carbon_rod` (12.2%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.5%) | `carbon` (0.4%) | `sacrificial_iron` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (83.3%) | `platinum_plate` (14.9%) | `platinum_foil` (1.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (94.9%) | `ABSENT` (4.8%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (66.8%) | `NBu4` (17.8%) | `K` (13.9%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (56.9%) | `BF4` (17.4%) | `molecular_no_ion` (12.2%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (13.6%) | `ABSENT` (11.1%) | `cyanide` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.6%) | `Fe_complex` (5.9%) | `Mn_complex` (1.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (96.6%) | `polar_protic_alcohol` (2.3%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `CO` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `C[Si](C)(C)N=[N+]=` (61%) | `CC(=O)O` (30%) | `[N-]=[N+]=[N-].[Na` (22%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `[Pt]` (2%) | `CC(=O)NC1CC2(CCCCC` (2%) | set ✓ / any ✓ |

---

### Reaction #1993  yield=36.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #1)

```
CC(=Cc1ccccc1)C(=O)C(c1ccccc1)C(F)(F)F>>CC1(c2ccccc2)C(=O)OC1(C(F)(F)F)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (53.1%) | `carbon` (44.9%) | `ABSENT` (1.5%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_generic` (73.5%) | `graphite_generic` (13.6%) | `carbon_generic` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (87.2%) | `carbon` (4.3%) | `ABSENT` (4.3%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (95.5%) | `graphite_generic` (1.1%) | `carbon_generic` (0.7%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (98.0%) | `undivided` (1.9%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.6%) | `Li` (5.4%) | `Na` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Br` (60.5%) | `BF4` (17.5%) | `ClO4` (15.1%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (11.8%) | `carboxylic_acid` (6.0%) | `metal_oxide_oxidant` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `organic_neutral_cat` (0.1%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (87.8%) | `polar_aprotic_amide` (7.2%) | `cyclic_ether` (1.5%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (18%) | `C1CCOC1` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `__OTHER__` | `__ABSENT__` (99%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[Br][Mn][Br]` (0%) | set ✓ / any ✓ |

---

### Reaction #1994  yield=35.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #2)

```
CC(=O)Oc1ccc(C=C(c2ccccc2)C(F)(F)F)cc1>>CC(=O)Oc1ccc(C(O)(CN=[N+]=[N-])C(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (59.6%) | `graphite_generic` (20.5%) | `reticulated_vitreous_carbon` (15.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.5%) | `carbon` (0.5%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (51.9%) | `platinum_plate` (43.0%) | `platinum_foil` (4.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.1%) | `ABSENT` (3.8%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.8%) | `NBu4` (0.1%) | `K` (0.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (55.6%) | `ClO4` (42.6%) | `BF4` (0.9%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (15.9%) | `azide_source` (6.4%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (75.3%) | `Mn_complex` (18.8%) | `Fe_complex` (3.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (98.5%) | `polar_protic_alcohol` (0.6%) | `halogenated_aliphatic` (0.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (99%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (100%) | `CC(=O)O` (3%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Br-].[Br-].[Mn+2]` (1%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #1995  yield=48.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #3)

```
C=C(c1ccc(C(C)(C)C)cc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CN=[N+]=[N-])(N=[N+]=[N-])C(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (78.0%) | `platinum` (21.4%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (90.4%) | `carbon_felt` (4.5%) | `platinum_generic` (4.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `ABSENT` (0.2%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.1%) | `platinum_foil` (2.3%) | `platinum_plate` (0.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (94.3%) | `ABSENT` (5.6%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (79.5%) | `NBu4` (12.0%) | `NEt4` (2.2%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (81.0%) | `molecular_no_ion` (9.3%) | `BF4` (5.5%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (47.9%) | `carboxylic_acid` (2.9%) | `alkali_other_salt` (2.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (70.2%) | `Mn_complex` (14.8%) | `Pt_complex` (5.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.9%) | `polar_protic_alcohol` (0.2%) | `polar_protic_acid` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (91%) | `CO` (18%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `[N-]=[N+]=[N-].[Na` (64%) | `CC(=O)O` (17%) | `C[Si](C)(C)N=[N+]=` (14%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (64%) | `Oc1ccccc1C=NCCN=Cc` (21%) | `CC(=O)NC1CC2(CCCCC` (8%) | set ✓ / any ✓ |

---

### Reaction #1996  yield=42.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #4)

```
CO.C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F>>COC(CN=[N+]=[N-])(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.7%) | `platinum` (4.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (50.2%) | `graphite_generic` (14.6%) | `carbon_felt` (10.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (93.8%) | `platinum_generic` (6.1%) | `platinum_foil` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (67.3%) | `Li` (30.8%) | `K` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (65.7%) | `BF4` (27.9%) | `Br` (2.7%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (83.5%) | `ABSENT` (0.8%) | `o2_oxidant` (0.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.7%) | `Cu_complex` (2.1%) | `Fe_complex` (1.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.5%) | `ABSENT` (3.5%) | `polar_protic_acid` (1.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `CO` (5%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `C[Si](C)(C)N=[N+]=` (93%) | `CC(=O)O` (41%) | `[N-]=[N+]=[N-].[Na` (5%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)NC1CC2(CCCCC` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #1997  yield=44.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #5)

```
C=C(c1cc(-c2ccccc2)cc(-c2ccccc2)c1)C(F)(F)F>>[N-]=[N+]=NCC(O)(c1cc(-c2ccccc2)cc(-c2ccccc2)c1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.8%) | `platinum` (5.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (92.9%) | `carbon_plate` (2.8%) | `graphite_rod` (1.3%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.9%) | `carbon` (0.1%) | `ABSENT` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (91.6%) | `platinum_plate` (7.0%) | `platinum_foil` (1.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (81.8%) | `NBu4` (7.7%) | `K` (4.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (77.0%) | `molecular_no_ion` (5.9%) | `BF4` (5.9%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (42.1%) | `ABSENT` (7.6%) | `alkali_other_salt` (1.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (64.3%) | `Mn_complex` (14.4%) | `Cu_complex` (8.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (96.3%) | `polar_protic_alcohol` (2.4%) | `polar_protic_acid` (0.7%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `CC#N` (100%) | `O` (100%) | `CO` (16%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `[N-]=[N+]=[N-].[Na` (74%) | `CC(=O)O` (32%) | `C[Si](C)(C)N=[N+]=` (17%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (83%) | `[Pt]` (5%) | `CC(C)(C)c1cc(C=N[C` (2%) | set ✓ / any ✓ |

---

### Reaction #1998  yield=41.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #6)

```
C=C(c1cc(OC)cc(OC)c1)C(F)(F)F>>COc1cc(OC)cc(C(CN=[N+]=[N-])(N=[N+]=[N-])C(F)(F)F)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.1%) | `platinum` (3.4%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (98.7%) | `carbon_felt` (0.9%) | `graphite_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `ABSENT` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (83.3%) | `platinum_plate` (9.6%) | `platinum_foil` (6.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (81.1%) | `ABSENT` (18.3%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (76.8%) | `Li` (16.2%) | `ABSENT` (4.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (71.4%) | `ClO4` (21.5%) | `ABSENT` (3.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (74.7%) | `alkali_other_salt` (3.3%) | `ketone` (1.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Cu_complex` (24.2%) | `Mn_complex` (23.0%) | `tempo_mediator` (21.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.8%) | `polar_protic_alcohol` (2.6%) | `halogenated_aliphatic` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `CO` (86%) | `O` (63%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `C[Si](C)(C)N=[N+]=` (55%) | `[N-]=[N+]=[N-].[Na` (31%) | `CC(=O)O` (5%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl][Cu][Cl]` (13%) | `[Fe+2].c1cc[cH-]c1` (13%) | `CC(=O)NC1CC2(CCCCC` (12%) | set ✗ / any ✗ |

---

### Reaction #1999  yield=45.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #7)

```
C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)C(F)(F)F>>[N-]=[N+]=NCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.9%) | `platinum` (1.9%) | `ABSENT` (1.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (68.7%) | `reticulated_vitreous_carbon` (20.8%) | `graphite_generic` (4.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.8%) | `carbon` (0.1%) | `ABSENT` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (98.3%) | `platinum_plate` (1.4%) | `platinum_foil` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (59.3%) | `undivided` (40.6%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (81.6%) | `K` (7.8%) | `NBu4` (6.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (65.9%) | `molecular_no_ion` (12.9%) | `I` (9.7%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `azide_source` (41.9%) | `ABSENT` (6.8%) | `tellurium_reagent` (1.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (84.7%) | `Fe_complex` (5.0%) | `Cu_complex` (3.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (87.5%) | `polar_protic_acid` (8.9%) | `polar_protic_alcohol` (1.8%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` | `O` (99%) | `CC#N` (99%) | `CO` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `O=C(O)C(F)(F)F` (44%) | `[N-]=[N+]=[N-].[Na` (36%) | `CC(=O)O` (23%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (92%) | `[Pt]` (3%) | `[Br-].[Br-].[Mn+2]` (1%) | set ✓ / any ✓ |

---

### Reaction #2000  yield=42.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_23_7649-7660.json) (反应 idx 在该 JSON 内 = #8)

```
C=C(c1ccc(OCc2ccccc2)cc1)C(F)(F)F>>[N-]=[N+]=NCC(N=[N+]=[N-])(c1ccc(OCc2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.0%) | `platinum` (9.9%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (90.5%) | `carbon_felt` (4.0%) | `platinum_generic` (3.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.1%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (98.7%) | `platinum_plate` (1.1%) | `platinum_foil` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (82.7%) | `ABSENT` (17.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (74.5%) | `NBu4` (16.7%) | `Na` (3.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (64.5%) | `molecular_no_ion` (21.1%) | `I` (3.6%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `alkali_other_salt` (22.2%) | `azide_source` (17.3%) | `ABSENT` (4.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (88.4%) | `Pt_complex` (4.7%) | `pyridine_organocat` (4.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.3%) | `halogenated_aliphatic` (0.2%) | `polar_protic_acid` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (99%) | `CO` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `C[Si](C)(C)N=[N+]=` | `[N-]=[N+]=[N-].[Na` (58%) | `[Pt]` (14%) | `CC(=O)O` (10%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Pt]` (0%) | `[Br][Mn][Br]` (0%) | set ✓ / any ✓ |

---

