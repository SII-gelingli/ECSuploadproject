# Test 预测 part 6 — 反应 #2501-#2947

[← 返回 INDEX](INDEX.md)

### Reaction #2501  yield=76.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #7)

```
CCCCCCCC=C=CC1(O)CCC2(CC1)OCCO2>>CCCCCCCC1=C(Br)CC2(CCC3(CC2)OCCO3)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.8%) | `platinum` (6.4%) | `ABSENT` (2.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (46.4%) | `glassy_carbon` (39.4%) | `graphite_rod` (6.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.1%) | `carbon` (5.8%) | `ABSENT` (3.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (93.2%) | `platinum_generic` (3.4%) | `graphite_generic` (1.3%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (98.8%) | `ABSENT` (1.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `Na` (73.8%) | `ABSENT` (8.5%) | `molecular_no_ion` (3.8%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (25.8%) | `Br` (23.8%) | `molecular_no_ion` (23.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (25.3%) | `bromide_anion` (3.3%) | `metal_oxide_oxidant` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `main_group_lewis_acid` (0.1%) | `ammonium_PTC_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (39.1%) | `polar_aprotic_nitrile` (38.2%) | `halogenated_aliphatic` (15.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (97%) | `ClCCl` (11%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `[Br-].[H+]` (1%) | `O=S([O-])([O-])=S.` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (1%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2502  yield=74.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #8)

```
CCCCCCCC=C=CC1(O)CCOCC1>>CCCCCCCC1=C(Br)CC2(CCOCC2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.7%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (83.4%) | `glassy_carbon` (10.6%) | `graphite_rod` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (74.8%) | `carbon` (24.4%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.0%) | `graphite_generic` (17.1%) | `glassy_carbon` (3.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `Na` (81.0%) | `molecular_no_ion` (8.8%) | `H` (4.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (61.1%) | `molecular_no_ion` (27.0%) | `ABSENT` (3.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (31.5%) | `bromide_anion` (4.2%) | `metal_oxide_oxidant` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `main_group_lewis_acid` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (74.6%) | `halogenated_aliphatic` (10.6%) | `polar_protic_alcohol` (8.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (37%) | `ClCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2503  yield=81.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #9)

```
CCCCCCCC=C=CC1(O)CCN(C(=O)OC(C)(C)C)CC1>>CCCCCCCC1=C(Br)CC2(CCN(C(=O)OC(C)(C)C)CC2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `platinum` (3.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (54.5%) | `glassy_carbon` (15.5%) | `graphite_rod` (14.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (80.6%) | `carbon` (17.3%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (82.0%) | `graphite_generic` (4.7%) | `platinum_generic` (4.5%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `K` | `Na` (96.9%) | `NBu4` (1.2%) | `molecular_no_ion` (0.9%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (53.5%) | `molecular_no_ion` (37.1%) | `I` (7.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (18.6%) | `carboxylic_acid` (7.6%) | `bromide_anion` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (48.9%) | `halogenated_aliphatic` (19.5%) | `polar_protic_alcohol` (11.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (23%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2504  yield=48.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #10)

```
OC1(C=C=CC2CC2)CCCCC1>>BrC1=C(C2CC2)OC3(CCCCC3)C1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (77.1%) | `platinum` (22.7%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (43.1%) | `graphite_rod` (36.0%) | `carbon_rod` (4.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `carbon` (3.3%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.1%) | `platinum_generic` (3.3%) | `glassy_carbon` (1.9%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `Na` (53.8%) | `ABSENT` (23.7%) | `Li` (4.7%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (77.6%) | `molecular_no_ion` (9.6%) | `ABSENT` (5.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (34.6%) | `bromide_anion` (6.3%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.5%) | `ABSENT` (22.9%) | `polar_protic_alcohol` (15.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `CO` (1%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2505  yield=62.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #11)

```
OC1(C=C=CCCc2ccccc2)CCCCC1>>BrC1=C(CCc2ccccc2)OC2(CCCCC2)C1.C=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.9%) | `platinum` (2.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (69.2%) | `graphite_generic` (10.4%) | `graphite_rod` (6.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.9%) | `carbon` (16.7%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (69.2%) | `platinum_generic` (16.2%) | `graphite_generic` (2.3%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (98.9%) | `ABSENT` (1.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `Na` (69.4%) | `molecular_no_ion` (26.6%) | `H` (0.9%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (46.8%) | `molecular_no_ion` (42.7%) | `Cl` (2.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.2%) | `bromide_anion` (3.2%) | `sulfonic_acid` (2.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `main_group_lewis_acid` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.4%) | `polar_protic_alcohol` (32.0%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (95%) | `O` (60%) | `CO` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `[Br-].[H+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2506  yield=79.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #12)

```
OC1(C=C=CCCCCCCBr)CCCCC1>>BrCCCCCCCCC1=C(Br)CC2(CCCCC2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.9%) | `platinum` (3.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (45.1%) | `graphite_rod` (20.8%) | `glassy_carbon` (9.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.4%) | `carbon` (6.6%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (82.4%) | `platinum_foil` (8.5%) | `platinum_generic` (4.9%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `Na` (80.4%) | `molecular_no_ion` (18.9%) | `K` (0.2%) | ✓ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (97.9%) | `Br` (1.2%) | `carboxylate` (0.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (46.9%) | `bromide_anion` (2.2%) | `carboxylic_acid` (1.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `brønsted_acid_cat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (76.4%) | `polar_protic_alcohol` (19.7%) | `aqueous` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (86%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `Cc1ccc(S(=O)(=O)O)` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #2507  yield=44.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #13)

```
C=CCCCCCCC=C=CC1(O)CCCCC1>>C=CCCCCCCCC1=C(Br)CC2(CCCCC2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.5%) | `platinum` (2.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (50.2%) | `graphite_rod` (37.8%) | `platinum_foil` (8.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (59.9%) | `carbon` (39.9%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (49.5%) | `graphite_rod` (23.9%) | `platinum_foil` (8.4%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `Na` (94.8%) | `molecular_no_ion` (1.7%) | `ABSENT` (1.7%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (51.1%) | `Br` (41.1%) | `ABSENT` (6.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (22.5%) | `bromide_anion` (15.3%) | `carboxylic_acid` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (67.0%) | `polar_protic_alcohol` (24.4%) | `aqueous` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (44%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2508  yield=70.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #14)

```
CCCCCCCC=C=CC(C)(C)O>>CCCCCCCC1=C(Br)CC(C)(C)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.9%) | `platinum` (5.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (91.9%) | `glassy_carbon` (4.8%) | `graphite_rod` (1.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.4%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (66.6%) | `platinum_foil` (16.7%) | `graphite_generic` (8.5%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `H` (82.9%) | `Na` (9.3%) | `molecular_no_ion` (6.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (61.7%) | `Br` (34.1%) | `carboxylate` (3.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (22.2%) | `bromide_anion` (10.6%) | `polyhalo_radical_transfer` (6.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.4%) | `halogenated_aliphatic` (4.6%) | `polar_aprotic_sulfoxide` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (92%) | `ClCCl` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (84%) | `[Br-].[H+]` (30%) | `O=S([O-])([O-])=S.` (11%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `O=S(=O)(O)C(F)(F)F` (1%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2509  yield=57.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #15)

```
C=CCC(O)(C=C=C(CCC)CCCCCC)CC=C>>CCCCCCC1=C(Br)C(CCC)(... )
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (76.1%) | `platinum` (23.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (79.8%) | `graphite_generic` (12.0%) | `platinum_plate` (4.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.9%) | `carbon` (10.3%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (54.7%) | `platinum_generic` (36.0%) | `graphite_generic` (3.5%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `NBu4` (48.7%) | `Li` (29.0%) | `ABSENT` (16.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `BF4` (35.2%) | `carboxylate` (18.8%) | `molecular_no_ion` (18.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (42.3%) | `electrophilic_N_F` (1.7%) | `unparseable_text` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `pyridine_organocat` (0.5%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.2%) | `polar_protic_alcohol` (3.6%) | `polar_aprotic_amide` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (2%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C(O)O.[Na]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2510  yield=76.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #16)

```
CCCCCCCC=C=CC(O)(Cc1ccccc1)Cc1ccccc1>>CCCCCCCC1=C(Br)CC(Cc2ccccc2)(Cc2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (65.0%) | `platinum` (34.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (41.1%) | `graphite_generic` (32.9%) | `graphite_rod` (11.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (91.2%) | `carbon` (8.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (92.4%) | `platinum_generic` (6.5%) | `graphite_generic` (0.6%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `H` (36.2%) | `NBu4` (36.2%) | `Na` (14.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `carboxylate` (50.6%) | `Br` (27.3%) | `BF4` (8.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (33.5%) | `as_solvent_halogenated_aliphat` (2.0%) | `unparseable_text` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (50.0%) | `polar_aprotic_nitrile` (45.4%) | `ABSENT` (1.2%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (55%) | `CC#N` (24%) | `ClCCl` (18%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S([O-])([O-])=S.` (0%) | `[Br-].[H+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2511  yield=57.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #14)

```
CCCCCCCC=C=CC(C)(C)O>>CCCCCCCC1=C(Br)CC(C)(C)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.9%) | `platinum` (5.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (91.9%) | `glassy_carbon` (4.8%) | `graphite_rod` (1.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.4%) | `carbon` (5.4%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (66.6%) | `platinum_foil` (16.7%) | `graphite_generic` (8.5%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `H` (82.9%) | `Na` (9.3%) | `molecular_no_ion` (6.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (61.7%) | `Br` (34.1%) | `carboxylate` (3.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (22.2%) | `bromide_anion` (10.6%) | `polyhalo_radical_transfer` (6.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.4%) | `halogenated_aliphatic` (4.6%) | `polar_aprotic_sulfoxide` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (92%) | `ClCCl` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (84%) | `[Br-].[H+]` (30%) | `O=S([O-])([O-])=S.` (11%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `O=S(=O)(O)C(F)(F)F` (1%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2512  yield=81.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #18)

```
CCCC(=C=CC(O)CCC)CCC>>CCCC1=C(Br)CC(CCC)(CCC)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (61.7%) | `platinum` (38.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (61.4%) | `platinum_foil` (9.9%) | `glassy_carbon` (9.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.4%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (86.6%) | `platinum_generic` (12.2%) | `platinum_foil` (0.6%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `NBu4` (91.5%) | `H` (4.5%) | `Na` (1.9%) | ✗ |
| 电解质 anion | 26 | `Br` | `carboxylate` (97.6%) | `BF4` (1.0%) | `Br` (0.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.3%) | `carboxylic_acid` (3.1%) | `metal_oxide_oxidant` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `Pt_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (29.7%) | `halogenated_aliphatic` (28.4%) | `polar_aprotic_nitrile` (25.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (94%) | `CC#N` (32%) | `CO` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Br-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].CC(=O)[` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #2513  yield=67.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00193_p2_t1.json) (反应 idx 在该 JSON 内 = #19)

```
OC1(C=C=CC=C=CC2(O)CCCCC2)CCCCC1>>O1C2(CCCCC2)CC(Br)=C1C1=C(Br)CC2(CCCCC2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.8%) | `platinum` (3.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (64.9%) | `glassy_carbon` (18.3%) | `graphite_generic` (6.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.5%) | `carbon` (11.8%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (72.4%) | `glassy_carbon` (7.5%) | `platinum_foil` (5.6%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `Na` (86.3%) | `molecular_no_ion` (7.9%) | `ABSENT` (4.9%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (82.2%) | `Br` (14.0%) | `ABSENT` (3.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (33.0%) | `bromide_anion` (4.1%) | `metal_oxide_oxidant` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (57.4%) | `polar_protic_alcohol` (20.6%) | `ABSENT` (16.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `CO` (1%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `Cc1ccc(S(=O)(=O)O)` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2514  yield=86.0%

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
| 电解质 cation | 23 | `ABSENT` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2515  yield=0.0%

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
| 电解质 cation | 23 | `ABSENT` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `inorganic_simple` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2516  yield=75.0%

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

### Reaction #2517  yield=25.0%

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
| 电解质 cation | 23 | `ABSENT` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `inorganic_simple` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2518  yield=47.0%

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
| 电解质 cation | 23 | `ABSENT` | `molecular_no_ion` (72.7%) | `ABSENT` (16.7%) | `Na` (5.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (79.2%) | `ABSENT` (16.0%) | `Br` (4.2%) | ✓ |
| 试剂大类 | 103 | `inorganic_simple` | `ABSENT` (15.5%) | `alkali_other_salt` (11.3%) | `carboxylic_acid` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `Mn_complex` (4.2%) | `brønsted_acid_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.5%) | `polar_aprotic_sulfoxide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (59%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `BrBr` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `O=S([O-])([O-])=S.` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2519  yield=70.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(OC(CC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.5%) | `platinum` (1.1%) | `sacrificial_iron` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (44.1%) | `graphite_rod` (23.4%) | `reticulated_vitreous_carbon` (18.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `nickel` (42.2%) | `carbon` (28.2%) | `platinum` (26.4%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (57.9%) | `graphite_rod` (25.4%) | `nickel_foam` (3.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.6%) | `ABSENT` (2.3%) | `divided` (1.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (58.5%) | `ABSENT` (33.8%) | `Li` (6.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `ABSENT` (50.8%) | `BF4` (28.7%) | `ClO4` (6.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.4%) | `carboxylic_acid` (2.6%) | `n_halo_imide` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.9%) | `Mn_complex` (1.5%) | `Fe_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (63.0%) | `ABSENT` (13.7%) | `polar_aprotic_amide` (11.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (95%) | `C1COCCO1` (1%) | `FC(F)(F)c1ccccc1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (98%) | `O` (1%) | `[Na+].[OH-]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `__OTHER__` (1%) | `c1ccncc1` (1%) | set ✓ / any ✓ |

---

### Reaction #2520  yield=64.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #1)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1C>>Cc1cccc(C(CC(=O)c2ccccc2)OC(=O)c2ccccc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (87.6%) | `carbon_generic` (8.0%) | `glassy_carbon` (0.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (62.7%) | `platinum` (25.2%) | `nickel` (10.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (65.7%) | `graphite_rod` (6.9%) | `nickel_plate` (6.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `divided` (0.6%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (62.1%) | `ABSENT` (31.9%) | `Li` (5.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `ABSENT` (59.4%) | `BF4` (20.9%) | `carboxylate` (7.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.4%) | `Fe_complex` (0.8%) | `Mn_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (50.1%) | `polar_aprotic_nitrile` (22.3%) | `polar_protic_alcohol` (15.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (69%) | `CC#N` (3%) | `FC(F)(F)c1ccccc1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2521  yield=61.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1cccc(C)c1>>Cc1ccccc1C(CC(=O)c1ccccc1)OC(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `sacrificial_magnesium` (0.4%) | `sacrificial_zinc` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `zinc_plate` (20.3%) | `graphite_rod` (17.7%) | `carbon_rod` (17.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (58.5%) | `platinum` (34.4%) | `nickel` (6.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (74.5%) | `platinum_wire` (4.0%) | `reticulated_vitreous_carbon` (3.1%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (51.3%) | `undivided` (48.5%) | `ABSENT` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.6%) | `Li` (1.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (40.1%) | `ClO4` (27.7%) | `PF6` (27.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.2%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.4%) | `Fe_complex` (3.9%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (83.7%) | `polar_aprotic_nitrile` (7.9%) | `ketone` (3.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (99%) | `CCOCC` (0%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2522  yield=76.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #3)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(C)cc1>>O=C(OC(CC(=O)c1ccccc1)c1ccc(C)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (42.7%) | `reticulated_vitreous_carbon` (23.6%) | `graphite_rod` (17.7%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (56.3%) | `platinum` (33.4%) | `nickel` (9.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (66.6%) | `graphite_rod` (17.0%) | `carbon_felt` (3.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (88.1%) | `ABSENT` (8.2%) | `divided` (3.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (52.6%) | `NBu4` (40.5%) | `Li` (6.0%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (56.9%) | `BF4` (17.3%) | `carboxylate` (16.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.4%) | `alkali_other_salt` (4.1%) | `n_halo_imide` (3.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.3%) | `Mn_complex` (2.5%) | `Co_complex` (1.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (74.1%) | `ABSENT` (14.4%) | `ketone` (4.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (22%) | `ClCCl` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (95%) | `__OTHER__` (11%) | `O=C1CCC(=O)N1Br` (3%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Pt]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2523  yield=59.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #4)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1OC>>COc1ccccc1C(CC(=O)c1ccccc1)OC(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (69.9%) | `sacrificial_iron` (25.8%) | `sacrificial_zinc` (1.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (45.6%) | `iron_plate` (40.1%) | `ABSENT` (3.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `nickel` (87.5%) | `carbon` (8.5%) | `platinum` (2.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `nickel_plate` (57.8%) | `nickel_foam` (27.7%) | `platinum_plate` (3.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (78.9%) | `divided` (20.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.2%) | `Li` (1.6%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `PF6` (54.8%) | `ClO4` (19.8%) | `BF4` (14.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (18.0%) | `tertiary_amine` (2.9%) | `water` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.5%) | `Fe_complex` (4.1%) | `Mn_complex` (1.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (91.5%) | `ketone` (6.3%) | `polar_aprotic_amide` (0.8%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (100%) | `CC(C)=O` (8%) | `OCC(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[Cs+` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `CC[C@H](C)[C@H]1CN` (0%) | set ✓ / any ✓ |

---

### Reaction #2524  yield=42.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #5)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1cccc(OC)c1>>O=C(OC(CC(=O)c1ccccc1)c1cccc(OC)c1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.3%) | `sacrificial_zinc` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (40.2%) | `graphite_rod` (22.2%) | `pencil_graphite` (19.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (60.9%) | `platinum` (25.8%) | `nickel` (11.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `graphite_rod` (33.1%) | `nickel_wire` (15.8%) | `platinum_plate` (15.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `divided` (0.8%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.6%) | `NEt4` (11.9%) | `Li` (7.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `carboxylate` (34.4%) | `PF6` (23.1%) | `BF4` (18.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.2%) | `carboxylic_acid` (2.7%) | `metal_oxide_oxidant` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `Co_complex` (0.3%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (71.5%) | `polar_aprotic_nitrile` (26.5%) | `polar_aprotic_amide` (0.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (81%) | `FC(F)(F)c1ccccc1` (24%) | `CCOCC` (9%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2525  yield=36.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #6)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(OC)cc1>>O=C(OC(CC(=O)c1ccccc1)c1ccc(OC)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `platinum` (0.9%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (65.8%) | `carbon_rod` (9.7%) | `unknown_electrode` (9.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (41.2%) | `platinum` (40.2%) | `nickel` (11.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (34.7%) | `nickel_foam` (14.2%) | `platinum_plate` (13.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (87.6%) | `divided` (8.9%) | `ABSENT` (3.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (73.5%) | `ABSENT` (14.7%) | `Li` (8.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `carboxylate` (40.9%) | `ABSENT` (18.0%) | `BF4` (13.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.2%) | `tertiary_amine` (4.0%) | `alkali_hydroxide` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.7%) | `Fe_complex` (1.7%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (43.1%) | `polar_aprotic_nitrile` (30.2%) | `ABSENT` (7.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC(C)=O` (100%) | `O` (90%) | `CC#N` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C` (90%) | `O=C1CCC(=O)N1Br` (83%) | `CC1(C)CCCC(C)(C)N1` (59%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2526  yield=62.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #7)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc([Si](C)(C)C)cc1>>O=C(OC(CC(=O)c1ccccc1)c1ccc([Si](C)(C)C)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (95.5%) | `carbon_cloth` (1.0%) | `carbon_generic` (0.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (64.3%) | `nickel` (17.7%) | `platinum` (17.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (80.3%) | `graphite_rod` (6.3%) | `nickel_plate` (5.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.4%) | `Li` (0.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (46.9%) | `PF6` (43.0%) | `ClO4` (4.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.7%) | `n_halo_imide` (2.5%) | `tertiary_amine` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.2%) | `pyridine_organocat` (0.6%) | `Mn_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (52.7%) | `polar_aprotic_nitrile` (34.9%) | `ketone` (9.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (87%) | `FC(F)(F)c1ccccc1` (5%) | `CC#N` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `C` (1%) | `O=C1CCC(=O)N1Br` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2527  yield=62.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #8)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1Cl>>O=C(CC(OC(=O)c1ccccc1)c1ccccc1Cl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `platinum` (1.1%) | `sacrificial_iron` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (55.8%) | `graphite_generic` (10.3%) | `reticulated_vitreous_carbon` (9.3%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (72.3%) | `platinum` (19.6%) | `nickel` (5.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `carbon_felt` (34.9%) | `platinum_plate` (20.9%) | `carbon_rod` (9.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (67.4%) | `divided` (31.3%) | `ABSENT` (1.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.8%) | `Li` (12.7%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `ClO4` (43.3%) | `PF6` (32.1%) | `BF4` (19.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.7%) | `acid_anhydride` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.8%) | `organic_neutral_cat` (3.6%) | `Fe_complex` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (45.8%) | `ketone` (23.4%) | `halogenated_aliphatic` (13.7%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (96%) | `ClCCl` (2%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (2%) | `CC(=O)OC(C)=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COc1c(I)cc2c(c1I)-` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2528  yield=60.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #9)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(F)cc1>>O=C(OC(CC(=O)c1ccccc1)c1ccc(F)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (82.4%) | `graphite_rod` (8.4%) | `reticulated_vitreous_carbon` (6.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (58.1%) | `carbon` (28.9%) | `nickel` (12.4%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (86.4%) | `graphite_rod` (8.2%) | `nickel_plate` (1.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (74.6%) | `ABSENT` (21.4%) | `Li` (3.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (51.7%) | `ABSENT` (37.0%) | `carboxylate` (4.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.4%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.0%) | `Mn_complex` (4.6%) | `pyridine_organocat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (68.6%) | `polar_aprotic_nitrile` (28.7%) | `halogenated_aliphatic` (1.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (78%) | `CC#N` (3%) | `FC(F)(F)c1ccccc1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (5%) | `O=O` (2%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Cl-].[Cl-].[Mn+2]` (1%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2529  yield=48.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #10)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(Br)cc1>>O=C(OC(CC(=O)c1ccccc1)c1ccc(Br)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (67.1%) | `carbon_generic` (12.1%) | `graphite_rod` (6.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (51.5%) | `carbon` (37.7%) | `nickel` (10.4%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (62.7%) | `graphite_rod` (23.2%) | `platinum_wire` (5.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.9%) | `ABSENT` (9.4%) | `Li` (5.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (52.0%) | `ABSENT` (27.6%) | `PF6` (8.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.0%) | `alkali_other_salt` (3.4%) | `n_halo_imide` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `pyridine_organocat` (1.1%) | `Mn_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (50.3%) | `ABSENT` (39.7%) | `ketone` (4.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (96%) | `O` (3%) | `ClCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (2%) | `O=C1CCC(=O)N1Br` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2530  yield=62.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #11)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(Cl)cc1>>O=C(OC(CC(=O)c1ccccc1)c1ccc(Cl)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (54.9%) | `carbon_generic` (14.8%) | `reticulated_vitreous_carbon` (10.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (43.9%) | `carbon` (38.8%) | `nickel` (14.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (80.9%) | `graphite_rod` (11.1%) | `nickel_foam` (1.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `divided` (0.7%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (79.3%) | `ABSENT` (19.5%) | `Li` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (50.6%) | `ABSENT` (42.0%) | `carboxylate` (2.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.1%) | `n_halo_imide` (3.0%) | `ammonium_salt` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.6%) | `Mn_complex` (1.8%) | `Fe_complex` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (69.3%) | `ABSENT` (14.4%) | `ketone` (7.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (11%) | `CCOCC` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (3%) | `O=O` (2%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2531  yield=46.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #12)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(C(F)(F)F)cc1>>O=C(OC(CC(=O)c1ccccc1)c1ccc(C(F)(F)F)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (96.9%) | `unknown_electrode` (1.1%) | `graphite_rod` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (52.3%) | `carbon` (38.4%) | `nickel` (5.6%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (90.9%) | `unknown_electrode` (1.9%) | `graphite_rod` (1.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.4%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (86.6%) | `ABSENT` (11.5%) | `Li` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (50.6%) | `ABSENT` (35.2%) | `carboxylate` (5.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.4%) | `bromide_anion` (3.8%) | `metal_oxide_oxidant` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.1%) | `pyridine_organocat` (1.6%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (79.2%) | `ABSENT` (13.4%) | `halogenated_aliphatic` (3.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (96%) | `ClCCl` (25%) | `FC(F)(F)c1ccccc1` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (15%) | `O=O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2532  yield=38.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #13)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(C(=O)OC)cc1>>O=C(OC(CC(=O)c1ccccc1)c1ccc(C(=O)OC)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (29.6%) | `reticulated_vitreous_carbon` (24.3%) | `carbon_rod` (20.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (42.7%) | `platinum` (42.7%) | `nickel` (13.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (71.2%) | `graphite_generic` (5.3%) | `platinum_generic` (4.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.8%) | `ABSENT` (1.1%) | `divided` (1.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.9%) | `Li` (8.3%) | `ABSENT` (1.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (28.0%) | `PF6` (21.7%) | `carboxylate` (20.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.0%) | `inorganic_simple` (2.5%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.2%) | `Mn_complex` (0.8%) | `Fe_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (41.2%) | `ABSENT` (40.2%) | `ketone` (13.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `FC(F)(F)c1ccccc1` (90%) | `CCOCC` (63%) | `CC#N` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (39%) | `O=O` (29%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `c1ccncc1` (4%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2533  yield=73.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #14)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(C)cc1C>>Cc1ccc(C(CC(=O)c2ccccc2)OC(=O)c2ccccc2)c(C)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.4%) | `sacrificial_magnesium` (0.9%) | `sacrificial_zinc` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (88.9%) | `zinc_plate` (2.2%) | `graphite_rod` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (78.1%) | `platinum` (11.2%) | `nickel` (10.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (45.3%) | `nickel_plate` (15.9%) | `graphite_generic` (12.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (92.8%) | `divided` (7.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.0%) | `Li` (1.8%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (54.2%) | `ClO4` (24.2%) | `PF6` (15.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (20.2%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.6%) | `Fe_complex` (1.6%) | `Mn_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (82.0%) | `polar_aprotic_nitrile` (8.4%) | `polar_aprotic_amide` (7.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (95%) | `FC(F)(F)c1ccccc1` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[Cs+` (0%) | `C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2534  yield=56.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #15)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(-c2ccccc2)cc1>>O=C(OC(CC(=O)c1ccccc1)c1ccc(-c2ccccc2)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (87.5%) | `reticulated_vitreous_carbon` (10.6%) | `graphite_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (84.5%) | `nickel` (8.1%) | `carbon` (6.6%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (96.4%) | `nickel_foam` (2.0%) | `platinum_wire` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `divided` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (89.0%) | `Li` (7.2%) | `ABSENT` (3.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (61.6%) | `ABSENT` (11.1%) | `PF6` (8.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.1%) | `as_solvent_halogenated_aliphat` (2.3%) | `metal_oxide_oxidant` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (77.7%) | `Mn_complex` (12.8%) | `Fe_complex` (5.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (36.1%) | `polar_aprotic_nitrile` (25.5%) | `ABSENT` (23.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC(C)=O` (93%) | `CC#N` (41%) | `CN(C)C=O` (7%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (1%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `[Cl][Mn][Cl]` (1%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2535  yield=64.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #16)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccn1>>O=C(OC(CC(=O)c1ccccc1)c1ccccn1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (46.1%) | `graphite_rod` (43.8%) | `carbon_felt` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (82.5%) | `nickel` (12.8%) | `carbon` (3.8%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (96.3%) | `nickel_plate` (1.8%) | `nickel_foam` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.0%) | `divided` (1.8%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (83.4%) | `NBu4` (14.0%) | `Na` (0.9%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (88.4%) | `BF4` (7.2%) | `Br` (2.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (13.6%) | `ABSENT` (10.5%) | `metal_oxide_oxidant` (1.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (88.6%) | `pyridine_organocat` (2.7%) | `Fe_complex` (2.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (80.9%) | `polar_aprotic_nitrile` (12.2%) | `polar_aprotic_amide` (1.5%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (79%) | `CC#N` (0%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (72%) | `CCCC[N+](CCCC)(CCC` (6%) | `CC(=O)O` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[Li+]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2536  yield=71.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #17)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1scnc1C>>Cc1ncc(C(CC(=O)c2ccccc2)OC(=O)c2ccccc2)s1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (60.6%) | `graphite_rod` (18.7%) | `carbon_felt` (9.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (86.7%) | `carbon` (8.3%) | `nickel` (4.6%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (95.0%) | `platinum_generic` (1.5%) | `carbon_rod` (1.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (66.3%) | `NBu4` (29.0%) | `NEt4` (4.3%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (74.3%) | `BF4` (13.8%) | `molecular_no_ion` (7.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.8%) | `diboron` (2.2%) | `metal_oxide_oxidant` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `organic_neutral_cat` (0.2%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.3%) | `ABSENT` (19.8%) | `ketone` (10.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (35%) | `ClCCl` (5%) | `O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #2537  yield=77.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #18)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=C(C)c1ccccc1>>O=C(OC(C)(CC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (58.5%) | `carbon_rod` (18.3%) | `graphite_rod` (16.3%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (60.9%) | `platinum` (18.8%) | `nickel` (16.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `graphite_rod` (47.5%) | `platinum_plate` (26.6%) | `nickel_foam` (4.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `divided` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.9%) | `Li` (5.0%) | `NEt4` (2.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (56.0%) | `ClO4` (20.1%) | `PF6` (12.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (10.3%) | `n_halo_imide` (9.0%) | `ABSENT` (6.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.2%) | `Mn_complex` (1.8%) | `pyridine_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (85.4%) | `ABSENT` (9.5%) | `polar_protic_alcohol` (3.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (92%) | `FC(F)(F)c1ccccc1` (6%) | `CCOCC` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C1CCC(=O)N1Br` (32%) | `CC[SiH](CC)CC` (26%) | `O=C([O-])[O-].[Cs+` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Br][Mn][Br]` (1%) | `CC(C)(C)c1cc(C=N[C` (0%) | set ✓ / any ✓ |

---

### Reaction #2538  yield=63.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #19)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=C(CCC)c1ccccc1>>O=C(OC(CCC)(CC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (65.1%) | `graphite_generic` (18.6%) | `reticulated_vitreous_carbon` (11.5%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (71.8%) | `nickel` (15.7%) | `stainless_steel` (7.6%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (68.6%) | `platinum_generic` (19.1%) | `nickel_plate` (2.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (91.8%) | `ABSENT` (8.0%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.6%) | `NEt4` (2.2%) | `Na` (0.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (82.0%) | `PF6` (7.0%) | `Br` (5.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.3%) | `n_halo_imide` (3.0%) | `amide` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `ammonium_PTC_organocat` (0.1%) | `Co_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (84.7%) | `polar_protic_alcohol` (6.6%) | `ABSENT` (4.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (98%) | `ClCCl` (1%) | `FC(F)(F)c1ccccc1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (96%) | `C` (0%) | `O=C1CCC(=O)N1Br` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #2539  yield=69.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #20)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=C(c1ccccc1)C1CCCC1>>O=C(OC(C1CCCC1)(CC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (84.4%) | `carbon_cloth` (11.8%) | `graphite_generic` (2.2%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (66.3%) | `stainless_steel` (27.8%) | `nickel` (4.9%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.3%) | `stainless_steel_generic` (0.3%) | `platinum_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.2%) | `ABSENT` (4.7%) | `Li` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `PF6` (41.8%) | `BF4` (23.3%) | `molecular_no_ion` (10.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `bromide_anion` (12.7%) | `ABSENT` (4.8%) | `carboxylic_acid` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.9%) | `pyridine_organocat` (2.0%) | `Mn_complex` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (89.6%) | `polar_protic_alcohol` (5.1%) | `ABSENT` (2.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (80%) | `ClCCl` (25%) | `FC(F)(F)c1ccccc1` (20%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `[Cl-].[Na+]` (31%) | `CCCC[N+](CCCC)(CCC` (16%) | `O` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2540  yield=74.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #21)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=C(c1ccccc1)C1CCCCC1>>O=C(OC(C1CCCCC1)(CC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (94.5%) | `carbon_cloth` (2.9%) | `graphite_rod` (1.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (80.0%) | `stainless_steel` (14.6%) | `nickel` (4.2%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (99.5%) | `platinum_generic` (0.1%) | `stainless_steel_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.4%) | `ABSENT` (7.4%) | `Li` (5.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `molecular_no_ion` (44.9%) | `PF6` (21.0%) | `BF4` (12.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `bromide_anion` (11.8%) | `ABSENT` (6.9%) | `carboxylic_acid` (2.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.0%) | `Fe_complex` (2.2%) | `Mn_complex` (1.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.3%) | `polar_protic_alcohol` (4.0%) | `ketone` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (92%) | `ClCCl` (33%) | `FC(F)(F)c1ccccc1` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CCCC[N+](CCCC)(CCC` (37%) | `[Cl-].[Na+]` (28%) | `[Br-].[K+]` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br][Mn][Br]` (0%) | set ✓ / any ✓ |

---

### Reaction #2541  yield=85.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #22)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=C(c1ccccc1)c1ccccc1>>O=C(OC(c1ccccc1)(CC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (40.0%) | `reticulated_vitreous_carbon` (36.8%) | `graphite_rod` (13.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (54.5%) | `platinum` (28.9%) | `nickel` (14.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `graphite_rod` (41.5%) | `carbon_plate` (19.4%) | `nickel_foam` (10.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (81.9%) | `divided` (15.6%) | `ABSENT` (2.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (80.5%) | `Li` (13.4%) | `NEt4` (2.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (81.6%) | `ClO4` (7.3%) | `PF6` (6.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `n_halo_imide` (21.0%) | `carboxylic_acid` (7.4%) | `tempo_mediator` (5.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `tempo_mediator` (87.0%) | `ABSENT` (6.1%) | `Mn_complex` (3.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.3%) | `polar_aprotic_amide` (3.8%) | `ABSENT` (1.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (19%) | `CCOCC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C` (99%) | `O=C1CCC(=O)N1Br` (98%) | `CC1(C)CCCC(C)(C)N1` (91%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `CC1(C)CCCC(C)(C)N1` (98%) | `[Fe+2].c1cc[cH-]c1` (1%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✗ / any ✗ |

---

### Reaction #2542  yield=55.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #23)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.CC=Cc1ccccc1>>O=C(OC(c1ccccc1)C(C)C(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (77.1%) | `graphite_rod` (8.3%) | `reticulated_vitreous_carbon` (8.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (41.2%) | `platinum` (29.2%) | `nickel` (18.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (26.5%) | `graphite_generic` (21.2%) | `platinum_wire` (16.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (75.0%) | `divided` (18.5%) | `ABSENT` (6.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (35.3%) | `Li` (32.3%) | `ABSENT` (30.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (73.0%) | `ABSENT` (20.3%) | `molecular_no_ion` (2.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.9%) | `as_solvent_polar_aprotic_sulfo` (5.3%) | `carboxylic_acid` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.6%) | `Fe_complex` (0.5%) | `ionic_organocat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (55.0%) | `polar_aprotic_nitrile` (42.5%) | `ketone` (1.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (96%) | `CC#N` (1%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2543  yield=32.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #24)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.CCC=Cc1ccccc1>>O=C(OC(c1ccccc1)C(CC)C(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_zinc` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (57.8%) | `carbon_generic` (33.3%) | `graphite_generic` (2.7%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (86.0%) | `nickel` (10.6%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (89.1%) | `platinum_wire` (5.3%) | `nickel_plate` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (83.4%) | `ABSENT` (8.5%) | `divided` (8.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.5%) | `Li` (3.0%) | `Na` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (82.3%) | `ClO4` (8.6%) | `PF6` (2.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (18.3%) | `carboxylic_acid` (10.4%) | `metal_oxide_oxidant` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Mn_complex` (0.1%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (56.4%) | `polar_aprotic_nitrile` (42.6%) | `polar_aprotic_amide` (0.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (81%) | `CC#N` (1%) | `FC(F)(F)c1ccccc1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2544  yield=50.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #25)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C1=Cc2ccccc2C1>>O=C(OC1Cc2ccccc2C1C(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (68.7%) | `carbon_generic` (16.5%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `nickel` (91.2%) | `platinum` (7.2%) | `carbon` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `nickel_foam` (90.1%) | `nickel_generic` (2.7%) | `nickel_wire` (2.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (71.0%) | `divided` (28.9%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (57.5%) | `ABSENT` (41.6%) | `Li` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `ABSENT` (61.5%) | `BF4` (31.2%) | `PF6` (4.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (13.7%) | `ABSENT` (11.6%) | `as_solvent_cyclic_ether` (2.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.3%) | `Ni_complex` (1.4%) | `lanthanide_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_amide` (36.5%) | `halogenated_aliphatic` (21.4%) | `polar_aprotic_sulfoxide` (18.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (7%) | `CC#N` (3%) | `CS(C)=O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (98%) | `O=C([O-])[O-].[Cs+` (3%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2545  yield=46.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #26)

```
Cc1ccc(C(=O)CC(=O)c2ccc(C)cc2)cc1.C=Cc1ccccc1>>O=C(OC(CC(=O)c1ccc(C)cc1)c1ccccc1)c1ccc(C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `sacrificial_zinc` (0.3%) | `platinum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (88.1%) | `carbon_rod` (5.0%) | `reticulated_vitreous_carbon` (3.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (40.5%) | `platinum` (34.7%) | `nickel` (24.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `graphite_rod` (48.7%) | `platinum_plate` (41.7%) | `nickel_plate` (2.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (95.9%) | `ABSENT` (3.6%) | `divided` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (62.4%) | `ABSENT` (35.6%) | `Li` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `ABSENT` (59.0%) | `BF4` (22.9%) | `Br` (5.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.9%) | `alkali_other_salt` (8.1%) | `n_halo_imide` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.8%) | `Co_complex` (2.0%) | `pyridine_organocat` (1.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (79.8%) | `ABSENT` (12.5%) | `polar_aprotic_amide` (2.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (97%) | `FC(F)(F)c1ccccc1` (2%) | `C1COCCO1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (1%) | `O=O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `__OTHER__` (3%) | `c1ccncc1` (2%) | set ✓ / any ✓ |

---

### Reaction #2546  yield=54.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #27)

```
COc1ccc(C(=O)CC(=O)c2ccc(OC)cc2)cc1.C=Cc1ccccc1>>O=C(OC(CC(=O)c1ccc(OC)cc1)c1ccccc1)c1ccc(OC)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.2%) | `platinum` (1.1%) | `sacrificial_zinc` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (29.0%) | `pencil_graphite` (22.1%) | `carbon_rod` (18.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (55.6%) | `nickel` (21.6%) | `platinum` (20.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `graphite_rod` (33.8%) | `platinum_plate` (18.5%) | `carbon_felt` (9.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (95.7%) | `ABSENT` (2.2%) | `divided` (2.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.3%) | `ABSENT` (15.5%) | `Li` (1.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `ABSENT` (38.3%) | `PF6` (16.4%) | `Br` (15.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.8%) | `carboxylic_acid` (3.8%) | `metal_oxide_oxidant` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Co_complex` (0.8%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.7%) | `ABSENT` (26.3%) | `polar_aprotic_amide` (5.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (90%) | `FC(F)(F)c1ccccc1` (3%) | `CN(C)C=O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `C` (1%) | `CC1(C)CCCC(C)(C)N1` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2547  yield=54.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #28)

```
O=C(CC(=O)c1ccc(F)cc1)c1ccc(F)cc1.C=Cc1ccccc1>>O=C(OC(CC(=O)c1ccc(F)cc1)c1ccccc1)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `sacrificial_iron` (0.3%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (71.8%) | `carbon_rod` (24.5%) | `iron_plate` (1.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (45.7%) | `carbon` (34.4%) | `nickel` (19.5%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `graphite_rod` (65.3%) | `platinum_plate` (27.7%) | `carbon_felt` (2.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.1%) | `ABSENT` (21.8%) | `Li` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `ABSENT` (50.5%) | `BF4` (38.5%) | `Br` (2.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.6%) | `alkali_other_salt` (2.5%) | `polyhalo_radical_transfer` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.0%) | `pyridine_organocat` (1.0%) | `Mn_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (49.2%) | `polar_aprotic_nitrile` (48.8%) | `polar_aprotic_amide` (0.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (94%) | `CC#N` (2%) | `FC(F)(F)c1ccccc1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `O=O` (1%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `__OTHER__` (3%) | `c1ccncc1` (3%) | set ✓ / any ✓ |

---

### Reaction #2548  yield=65.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #29)

```
O=C(CC(=O)c1ccc(Cl)cc1)c1ccc(Cl)cc1.C=Cc1ccccc1>>O=C(OC(CC(=O)c1ccc(Cl)cc1)c1ccccc1)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `sacrificial_zinc` (1.2%) | `sacrificial_iron` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (76.5%) | `carbon_rod` (7.0%) | `carbon_generic` (6.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (34.4%) | `carbon` (33.7%) | `nickel` (31.3%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `graphite_rod` (56.6%) | `platinum_plate` (34.1%) | `reticulated_vitreous_carbon` (2.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.7%) | `ABSENT` (13.4%) | `Li` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `ABSENT` (44.3%) | `BF4` (36.3%) | `Br` (8.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (18.9%) | `alkali_other_salt` (3.1%) | `cyanide` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `pyridine_organocat` (0.6%) | `Co_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (78.2%) | `ABSENT` (12.2%) | `polar_aprotic_amide` (6.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (84%) | `FC(F)(F)c1ccccc1` (8%) | `C1COCCO1` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (6%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (72%) | `c1ccncc1` (51%) | `__OTHER__` (28%) | set ✗ / any ✓ |

---

### Reaction #2549  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #30)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=C(C)C>>CC(C)(CC(=O)c1ccccc1)OC(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (0.6%) | `sacrificial_zinc` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (47.1%) | `carbon_rod` (36.0%) | `carbon_felt` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `nickel` (55.5%) | `platinum` (18.0%) | `stainless_steel` (17.0%) | ✗ |
| 阴极 (细类) | 49 | `graphite_generic` | `nickel_foam` (80.2%) | `platinum_plate` (8.5%) | `platinum_wire` (2.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (75.7%) | `divided` (22.6%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (71.4%) | `NBu4` (26.6%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ClO4` (56.1%) | `molecular_no_ion` (12.8%) | `carboxylate` (10.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.0%) | `carboxylic_acid` (3.9%) | `bromide_anion` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (55.7%) | `Mn_complex` (12.1%) | `Fe_complex` (10.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.6%) | `ketone` (20.3%) | `ABSENT` (6.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (87%) | `FC(F)(F)c1ccccc1` (7%) | `CC(C)=O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (96%) | `C` (18%) | `O=C([O-])[O-].[Cs+` (5%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (92%) | `[Fe+2].c1cc[cH-]c1` (2%) | `[Br-].[Br-].[Mn+2]` (2%) | set ✓ / any ✓ |

---

### Reaction #2550  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #31)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=CCc1ccccc1>>O=C(CC(CCc1ccccc1)OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.6%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `pencil_graphite` (46.2%) | `carbon_cloth` (16.7%) | `graphite_rod` (12.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (47.2%) | `carbon` (29.2%) | `stainless_steel` (14.6%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `stainless_steel_wire` (32.7%) | `platinum_plate` (28.9%) | `platinum_generic` (10.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (91.0%) | `divided` (7.8%) | `ABSENT` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (94.7%) | `NBu4` (2.5%) | `protonated_amine` (1.5%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (94.2%) | `BF4` (3.2%) | `fluoride_complex` (1.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `n_halo_imide` (6.9%) | `ABSENT` (5.5%) | `water` (5.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (94.4%) | `halogenated_aliphatic` (3.5%) | `polar_aprotic_nitrile` (1.5%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (64%) | `ClCCl` (49%) | `FC(F)(F)c1ccccc1` (45%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `O=O` (99%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (52%) | `[Br-].[Br-].[Mn+2]` (15%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2551  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #32)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=CCCCC>>CCCCC(CC(=O)c1ccccc1)OC(=O)CC(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.0%) | `platinum` (1.4%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (97.4%) | `unknown_electrode` (0.9%) | `pencil_graphite` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.3%) | `carbon` (6.9%) | `stainless_steel` (4.7%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (25.9%) | `platinum_plate` (23.8%) | `carbon_felt` (18.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (12.5%) | `divided` (1.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (79.5%) | `NEt4` (8.9%) | `NBu4` (7.6%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (85.9%) | `BF4` (5.4%) | `PF6` (3.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (7.2%) | `ABSENT` (5.0%) | `as_solvent_polar_aprotic_sulfo` (3.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.8%) | `Fe_complex` (0.8%) | `Mn_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.3%) | `polar_aprotic_nitrile` (18.6%) | `ketone` (9.7%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (45%) | `CCOCC` (13%) | `CC#N` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC[SiH](CC)CC` (36%) | `__OTHER__` (34%) | `O=O` (16%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `[Br-].[Br-].[Mn+2]` (2%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2552  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t0.json) (反应 idx 在该 JSON 内 = #33)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=CC(=O)OCC>>CCOC(=O)C(CC(=O)c1ccccc1)OC(=O)CC(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (89.7%) | `platinum` (9.8%) | `sacrificial_iron` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (50.3%) | `carbon_felt` (26.1%) | `graphite_generic` (14.2%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `nickel` (43.8%) | `platinum` (33.5%) | `carbon` (16.4%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `nickel_foam` (80.4%) | `platinum_generic` (4.3%) | `unknown_electrode` (3.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.1%) | `ABSENT` (1.4%) | `divided` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (64.1%) | `NBu4` (26.3%) | `ABSENT` (8.0%) | ✓ |
| 电解质 anion | 26 | `Cl` | `BF4` (67.7%) | `ABSENT` (13.7%) | `ClO4` (13.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (3.7%) | `boron_lewis_acid` (3.0%) | `o2_oxidant` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (78.0%) | `Fe_complex` (7.8%) | `Mn_complex` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (45.0%) | `ketone` (33.6%) | `polar_aprotic_amide` (10.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (90%) | `CN(C)C=O` (5%) | `CC(C)=O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (97%) | `[Na+].[OH-]` (2%) | `CCOC(C)=O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Cl][Mn][Cl]` (0%) | `[Br][Mn][Br]` (0%) | set ✓ / any ✓ |

---

### Reaction #2553  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2554  yield=12.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2555  yield=57.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2556  yield=56.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2557  yield=18.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2558  yield=52.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2559  yield=27.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2560  yield=44.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2561  yield=70.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2562  yield=65.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2563  yield=80.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2564  yield=65.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2565  yield=70.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2566  yield=60.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2567  yield=75.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✗ |
| 电解质 anion | 26 | `OTs` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2568  yield=55.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2569  yield=60.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2570  yield=55.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2571  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2572  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2573  yield=80.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(OC(c1ccccc1)CC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.5%) | `platinum` (1.1%) | `sacrificial_iron` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (44.1%) | `graphite_rod` (23.4%) | `reticulated_vitreous_carbon` (18.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (42.2%) | `carbon` (28.2%) | `platinum` (26.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (57.9%) | `graphite_rod` (25.4%) | `nickel_foam` (3.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.6%) | `ABSENT` (2.3%) | `divided` (1.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (58.5%) | `ABSENT` (33.8%) | `Li` (6.8%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (50.8%) | `BF4` (28.7%) | `ClO4` (6.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.4%) | `carboxylic_acid` (2.6%) | `n_halo_imide` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.9%) | `Mn_complex` (1.5%) | `Fe_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (63.0%) | `ABSENT` (13.7%) | `polar_aprotic_amide` (11.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (95%) | `C1COCCO1` (1%) | `FC(F)(F)c1ccccc1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (98%) | `O` (1%) | `[Na+].[OH-]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `__OTHER__` (1%) | `c1ccncc1` (1%) | set ✓ / any ✓ |

---

### Reaction #2574  yield=75.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(OC)cc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(OC(c1ccc(OC)cc1)CC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `platinum` (0.9%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (65.8%) | `carbon_rod` (9.7%) | `unknown_electrode` (9.0%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (41.2%) | `platinum` (40.2%) | `nickel` (11.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (34.7%) | `nickel_foam` (14.2%) | `platinum_plate` (13.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (87.6%) | `divided` (8.9%) | `ABSENT` (3.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (73.5%) | `ABSENT` (14.7%) | `Li` (8.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `carboxylate` (40.9%) | `ABSENT` (18.0%) | `BF4` (13.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.2%) | `tertiary_amine` (4.0%) | `alkali_hydroxide` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.7%) | `Fe_complex` (1.7%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (43.1%) | `polar_aprotic_nitrile` (30.2%) | `ABSENT` (7.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC(C)=O` (100%) | `O` (90%) | `CC#N` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C` (90%) | `O=C1CCC(=O)N1Br` (83%) | `CC1(C)CCCC(C)(C)N1` (59%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2575  yield=77.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(OCc2ccccc2)cc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(OC(c1ccc(OCc2ccccc2)cc1)CC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (30.7%) | `pencil_graphite` (21.8%) | `graphite_rod` (20.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (45.6%) | `nickel` (36.0%) | `carbon` (17.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (64.5%) | `nickel_foam` (19.3%) | `nickel_wire` (6.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.3%) | `divided` (1.1%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (85.7%) | `ABSENT` (9.9%) | `Li` (3.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (26.8%) | `BF4` (18.2%) | `carboxylate` (17.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.5%) | `alkali_other_salt` (5.1%) | `carboxylic_acid` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.5%) | `pyridine_organocat` (1.8%) | `Co_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (72.1%) | `ABSENT` (22.7%) | `polar_aprotic_amide` (2.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (84%) | `FC(F)(F)c1ccccc1` (12%) | `CCOCC` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (1%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2576  yield=70.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1ccc(C(C)(C)C)cc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(OC(c1ccc(C(C)(C)C)cc1)CC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (36.7%) | `carbon_felt` (34.5%) | `reticulated_vitreous_carbon` (18.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (53.1%) | `carbon` (29.1%) | `nickel` (17.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (73.6%) | `nickel_foam` (9.7%) | `carbon_felt` (6.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (62.7%) | `ABSENT` (26.9%) | `Li` (10.2%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (51.0%) | `BF4` (32.0%) | `ClO4` (8.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.8%) | `carboxylic_acid` (2.7%) | `metal_oxide_oxidant` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.6%) | `Mn_complex` (6.3%) | `brønsted_acid_cat` (1.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (61.5%) | `ABSENT` (30.2%) | `polar_aprotic_amide` (4.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `CC(C)=O` (1%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (2%) | `O=O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (95%) | `Oc1ccccc1C=NCCN=Cc` (4%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #2577  yield=78.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #4)

```
C=Cc1ccc(OCC2CC2)cc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(CC(OC(=O)c1ccccc1)c1ccc(OCC2CC2)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (95.5%) | `carbon_generic` (1.6%) | `carbon_felt` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (67.6%) | `nickel` (19.1%) | `platinum` (12.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (45.9%) | `nickel_foam` (19.5%) | `graphite_rod` (15.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (57.9%) | `Li` (26.6%) | `ABSENT` (15.2%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (36.4%) | `ClO4` (17.4%) | `molecular_no_ion` (11.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.2%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.7%) | `Mn_complex` (1.4%) | `Fe_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (78.6%) | `ketone` (7.8%) | `ABSENT` (7.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (91%) | `CC(C)=O` (27%) | `FC(F)(F)c1ccccc1` (5%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C` (1%) | `O=C1CCC(=O)N1Br` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2578  yield=72.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #5)

```
C=Cc1ccc(CCl)cc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(CC(OC(=O)c1ccccc1)c1ccc(CCl)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_felt` (46.5%) | `carbon_rod` (38.5%) | `carbon_generic` (8.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (68.3%) | `carbon` (26.7%) | `nickel` (2.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (80.0%) | `graphite_felt` (13.6%) | `platinum_wire` (1.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `ABSENT` (50.0%) | `NBu4` (45.4%) | `Li` (4.2%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (45.3%) | `BF4` (36.1%) | `Cl` (13.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.9%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.2%) | `Fe_complex` (2.1%) | `Mn_complex` (1.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (54.9%) | `polar_aprotic_nitrile` (37.2%) | `ABSENT` (4.7%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC(C)=O` (96%) | `CC#N` (2%) | `O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C1CCC(=O)N1Br` (0%) | `C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2579  yield=65.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #6)

```
C=Cc1cccc(OC(F)(F)F)c1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(CC(OC(=O)c1ccccc1)c1cccc(OC(F)(F)F)c1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.6%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (88.4%) | `reticulated_vitreous_carbon` (4.5%) | `graphite_rod` (3.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (76.5%) | `carbon` (12.5%) | `nickel` (10.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (94.4%) | `platinum_generic` (1.7%) | `carbon_felt` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (66.6%) | `NEt4` (14.9%) | `Li` (12.8%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (32.5%) | `carboxylate` (25.7%) | `ClO4` (14.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (18.7%) | `o2_oxidant` (5.6%) | `metal_oxide_oxidant` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `pyridine_organocat` (0.4%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.8%) | `ABSENT` (29.4%) | `ketone` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (91%) | `FC(F)(F)c1ccccc1` (5%) | `CC(C)=O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2580  yield=68.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #7)

```
C=Cc1ccccc1F.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(OC(c1ccccc1F)CC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (80.9%) | `reticulated_vitreous_carbon` (6.5%) | `graphite_rod` (5.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (63.5%) | `carbon` (22.6%) | `nickel` (12.9%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (93.7%) | `platinum_generic` (1.2%) | `nickel_plate` (1.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `divided` (0.7%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (98.2%) | `Li` (1.1%) | `NEt4` (0.7%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (43.9%) | `PF6` (33.8%) | `BF4` (21.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.0%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.9%) | `Fe_complex` (0.7%) | `Mn_complex` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (65.1%) | `ABSENT` (22.9%) | `ketone` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (81%) | `FC(F)(F)c1ccccc1` (4%) | `CC(C)=O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2581  yield=80.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #8)

```
C=Cc1cccc(OC)c1OC.O=C(CC(=O)c1ccccc1)c1ccccc1>>COc1cccc(C(CC(=O)c2ccccc2)OC(=O)c2ccccc2)c1OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (84.2%) | `carbon_rod` (11.1%) | `pencil_graphite` (1.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (80.5%) | `nickel` (11.8%) | `carbon` (6.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (61.1%) | `platinum_wire` (19.0%) | `platinum_generic` (6.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (92.4%) | `divided` (7.3%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (69.9%) | `Li` (26.7%) | `NEt4` (1.7%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (39.6%) | `ClO4` (35.6%) | `PF6` (17.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (24.2%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `Fe_complex` (0.4%) | `Mn_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (78.0%) | `polar_aprotic_nitrile` (18.6%) | `ketone` (2.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (98%) | `CC#N` (1%) | `CCOCC` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Br-].[Mn+2]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2582  yield=72.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #9)

```
C=Cc1c(C)cc(C)cc1C.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(OC(c1c(C)cc(C)cc1C)CC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (45.8%) | `graphite_generic` (14.5%) | `carbon_felt` (12.5%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (67.5%) | `carbon` (18.5%) | `nickel` (7.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (92.9%) | `nickel_wire` (2.1%) | `nickel_plate` (1.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.0%) | `divided` (3.8%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `ABSENT` (76.1%) | `NBu4` (23.6%) | `Li` (0.3%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (89.5%) | `BF4` (9.0%) | `PF6` (0.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (8.6%) | `carboxylic_acid` (5.1%) | `ABSENT` (3.1%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.0%) | `Mn_complex` (2.8%) | `Co_complex` (1.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (88.6%) | `polar_aprotic_nitrile` (9.9%) | `halogenated_aliphatic` (0.6%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `__ABSENT__` (90%) | `CC#N` (3%) | `FC(F)(F)c1ccccc1` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O` (89%) | `O=O` (1%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2583  yield=70.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #10)

```
C1=Cc2ccccc2C1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(OC1CC(CC(=O)c2ccccc2)c2ccccc21)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (70.1%) | `reticulated_vitreous_carbon` (11.1%) | `graphite_generic` (5.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (78.7%) | `platinum` (12.9%) | `carbon` (8.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_foam` (25.0%) | `nickel_generic` (22.4%) | `platinum_foil` (15.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (66.1%) | `divided` (33.1%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (96.9%) | `Li` (2.4%) | `ABSENT` (0.6%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (87.0%) | `PF6` (6.4%) | `ClO4` (4.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (18.7%) | `ABSENT` (10.1%) | `metal_oxide_oxidant` (1.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (79.9%) | `Mn_complex` (11.5%) | `brønsted_acid_cat` (7.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_amide` (48.6%) | `halogenated_aliphatic` (25.5%) | `polar_aprotic_nitrile` (10.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (76%) | `O` (18%) | `CN(C)C=O` (14%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (97%) | `CC(=O)O` (2%) | `CCCC[N+](CCCC)(CCC` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `O=S(=O)([O-])C(F)(` (4%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2584  yield=75.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #11)

```
C/C=C/c1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>CC(CC(=O)c1ccccc1)C(OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `sacrificial_iron` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (29.3%) | `graphite_rod` (28.2%) | `carbon_generic` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (50.8%) | `platinum` (42.5%) | `carbon` (3.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_foam` (63.2%) | `platinum_wire` (9.8%) | `platinum_generic` (9.3%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (62.2%) | `undivided` (31.2%) | `divided` (6.6%) | ✓ |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (80.3%) | `ABSENT` (15.8%) | `Li` (3.3%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (92.2%) | `ABSENT` (6.4%) | `ClO4` (0.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.6%) | `carboxylic_acid` (3.2%) | `n_halo_imide` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (83.8%) | `Mn_complex` (6.6%) | `Fe_complex` (3.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (87.5%) | `polar_aprotic_nitrile` (10.2%) | `ketone` (1.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `__ABSENT__` (95%) | `CC#N` (0%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O` (1%) | `C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2585  yield=74.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #12)

```
CCC/C=C/c1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>CCCC(CC(=O)c1ccccc1)C(OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `ABSENT` (0.9%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (41.3%) | `reticulated_vitreous_carbon` (40.8%) | `graphite_rod` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (87.3%) | `carbon` (5.8%) | `nickel` (3.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_wire` (45.6%) | `platinum_generic` (17.2%) | `platinum_foil` (17.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (58.4%) | `divided` (38.6%) | `undivided` (3.0%) | ✓ |
| 电解质 cation | 23 | `pyridinium` | `ABSENT` (83.7%) | `Li` (10.2%) | `NBu4` (5.7%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (75.1%) | `BF4` (23.2%) | `ClO4` (1.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.1%) | `carboxylic_acid` (6.1%) | `as_solvent_polar_aprotic_sulfo` (3.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (88.8%) | `Mn_complex` (4.9%) | `brønsted_acid_cat` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.7%) | `ABSENT` (26.2%) | `halogenated_aliphatic` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (94%) | `__OTHER__` (1%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (97%) | `O=C(O)C(F)(F)F` (3%) | `O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Br-].[Mn+2]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #2586  yield=78.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #13)

```
C=C(c1ccccc1)c1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(CC(OC(=O)c1ccccc1)(c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (40.0%) | `reticulated_vitreous_carbon` (36.8%) | `graphite_rod` (13.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (54.5%) | `platinum` (28.9%) | `nickel` (14.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `graphite_rod` (41.5%) | `carbon_plate` (19.4%) | `nickel_foam` (10.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (81.9%) | `divided` (15.6%) | `ABSENT` (2.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (80.5%) | `Li` (13.4%) | `NEt4` (2.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (81.6%) | `ClO4` (7.3%) | `PF6` (6.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `n_halo_imide` (21.0%) | `carboxylic_acid` (7.4%) | `tempo_mediator` (5.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `tempo_mediator` (87.0%) | `ABSENT` (6.1%) | `Mn_complex` (3.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.3%) | `polar_aprotic_amide` (3.8%) | `ABSENT` (1.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (19%) | `CCOCC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C` (99%) | `O=C1CCC(=O)N1Br` (98%) | `CC1(C)CCCC(C)(C)N1` (91%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `CC1(C)CCCC(C)(C)N1` (98%) | `[Fe+2].c1cc[cH-]c1` (1%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✗ / any ✗ |

---

### Reaction #2587  yield=82.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #14)

```
C=C(c1ccccc1)c1ccc(C)cc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>Cc1ccc(C(CC(=O)c2ccccc2)(OC(=O)c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_zinc` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (98.9%) | `carbon_felt` (0.4%) | `pencil_graphite` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (65.9%) | `nickel` (21.4%) | `platinum` (12.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `graphite_rod` (84.2%) | `nickel_wire` (10.3%) | `nickel_plate` (1.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.9%) | `divided` (11.4%) | `ABSENT` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (78.9%) | `ABSENT` (18.0%) | `Li` (1.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (69.4%) | `ABSENT` (19.2%) | `OTf` (4.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `n_halo_imide` (14.1%) | `ABSENT` (9.0%) | `primary_amine` (2.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (84.0%) | `Fe_complex` (5.5%) | `Co_complex` (2.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (83.5%) | `polar_aprotic_nitrile` (16.1%) | `polar_aprotic_amide` (0.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `__ABSENT__` (98%) | `CC#N` (16%) | `FC(F)(F)c1ccccc1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C1CCC(=O)N1Br` (75%) | `C` (56%) | `__ABSENT__` (41%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2588  yield=82.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #15)

```
C=C(C)c1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>CC(CC(=O)c1ccccc1)(OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (58.5%) | `carbon_rod` (18.3%) | `graphite_rod` (16.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (60.9%) | `platinum` (18.8%) | `nickel` (16.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `graphite_rod` (47.5%) | `platinum_plate` (26.6%) | `nickel_foam` (4.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `divided` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (90.9%) | `Li` (5.0%) | `NEt4` (2.8%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (56.0%) | `ClO4` (20.1%) | `PF6` (12.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (10.3%) | `n_halo_imide` (9.0%) | `ABSENT` (6.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.2%) | `Mn_complex` (1.8%) | `pyridine_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (85.4%) | `ABSENT` (9.5%) | `polar_protic_alcohol` (3.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (92%) | `FC(F)(F)c1ccccc1` (6%) | `CCOCC` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C1CCC(=O)N1Br` (32%) | `CC[SiH](CC)CC` (26%) | `O=C([O-])[O-].[Cs+` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Br][Mn][Br]` (1%) | `CC(C)(C)c1cc(C=N[C` (0%) | set ✓ / any ✓ |

---

### Reaction #2589  yield=75.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #16)

```
C=C(CC)c1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>CCC(CC(=O)c1ccccc1)(OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (40.8%) | `graphite_rod` (27.8%) | `carbon_rod` (17.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (59.2%) | `platinum` (36.9%) | `stainless_steel` (3.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_plate` (45.8%) | `platinum_plate` (31.7%) | `nickel_foam` (11.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.6%) | `ABSENT` (3.4%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (99.8%) | `NEt4` (0.2%) | `Li` (0.0%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (97.4%) | `Br` (1.0%) | `carboxylate` (0.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.0%) | `n_halo_imide` (2.5%) | `primary_amine` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `Mn_complex` (0.6%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.4%) | `polar_protic_alcohol` (3.5%) | `ABSENT` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `FC(F)(F)c1ccccc1` (1%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `C` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br][Mn][Br]` (0%) | set ✓ / any ✓ |

---

### Reaction #2590  yield=80.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #17)

```
C=C(Cc1ccccc1)c1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(CC(Cc1ccccc1)(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (91.8%) | `reticulated_vitreous_carbon` (2.3%) | `graphite_generic` (2.0%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (66.5%) | `stainless_steel` (21.8%) | `nickel` (6.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (97.8%) | `platinum_generic` (0.6%) | `nickel_plate` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (74.1%) | `protonated_amine` (14.6%) | `ABSENT` (4.7%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (42.0%) | `fluoride_complex` (23.5%) | `PF6` (7.9%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.1%) | `bromide_anion` (3.1%) | `inorganic_simple` (2.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `pyridine_organocat` (0.5%) | `ionic_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (80.1%) | `ABSENT` (18.9%) | `halogenated_aliphatic` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (97%) | `ClCCl` (3%) | `FC(F)(F)c1ccccc1` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Na+]` (1%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br][Mn][Br]` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2591  yield=75.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #18)

```
C=C(C)c1ccc2ccccc2c1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(OC(C)(c1ccc2ccccc2c1)CC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (46.5%) | `graphite_rod` (22.0%) | `carbon_cloth` (17.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (49.7%) | `platinum` (29.1%) | `nickel` (20.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `graphite_rod` (51.0%) | `platinum_plate` (19.8%) | `nickel_plate` (15.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.2%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (93.7%) | `ABSENT` (5.8%) | `Li` (0.3%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (60.1%) | `ABSENT` (18.2%) | `PF6` (11.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.8%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.1%) | `pyridine_organocat` (1.8%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (80.6%) | `ABSENT` (18.3%) | `polar_aprotic_amide` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `CO` (0%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CCN(CC)CC.F.F.F` (0%) | `CCN(C(C)C)C(C)C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2592  yield=65.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #19)

```
C=CC(=C)c1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(OC(C=C)(c1ccccc1)CC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (64.0%) | `graphite_rod` (10.9%) | `reticulated_vitreous_carbon` (8.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (50.7%) | `platinum` (31.9%) | `stainless_steel` (9.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (56.5%) | `nickel_foam` (24.5%) | `nickel_wire` (11.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.9%) | `ABSENT` (1.8%) | `divided` (1.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (88.3%) | `Li` (7.4%) | `Na` (1.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (53.1%) | `PF6` (19.3%) | `Br` (13.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (4.9%) | `as_solvent_halogenated_aliphat` (3.6%) | `n_halo_imide` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (70.1%) | `Fe_complex` (14.3%) | `Mn_complex` (5.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (53.5%) | `ketone` (25.2%) | `ABSENT` (6.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (84%) | `FC(F)(F)c1ccccc1` (7%) | `CCOCC` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (96%) | `C` (3%) | `O=C1CCC(=O)N1Br` (2%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `[Fe+2].c1cc[cH-]c1` (2%) | `[Br][Mn][Br]` (1%) | set ✓ / any ✓ |

---

### Reaction #2593  yield=68.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #20)

```
C=C(C)C(=C)c1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(OC(C(=C)C)(c1ccccc1)CC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (95.2%) | `graphite_rod` (3.7%) | `reticulated_vitreous_carbon` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (61.9%) | `platinum` (29.3%) | `carbon` (5.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (66.7%) | `nickel_foam` (13.2%) | `graphite_rod` (7.4%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (54.9%) | `undivided` (45.0%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (49.8%) | `Li` (36.8%) | `K` (5.6%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (35.4%) | `ClO4` (26.3%) | `PF6` (23.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `n_halo_imide` (7.9%) | `amide` (4.7%) | `ABSENT` (4.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.0%) | `tempo_mediator` (2.8%) | `Mn_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.7%) | `ketone` (2.4%) | `halogenated_aliphatic` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (66%) | `CO` (7%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC1(C)CCCC(C)(C)N1` (97%) | `C` (93%) | `O=C1CCC(=O)N1Br` (90%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CC1(C)CCCC(C)(C)N1` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2594  yield=50.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #21)

```
C=Cc1ccc(OCCCc2ccccc2)cc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(OC(c1ccc(OCCCc2ccccc2)cc1)CC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.2%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (35.0%) | `carbon_rod` (29.2%) | `graphite_rod` (10.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (44.6%) | `platinum` (34.2%) | `carbon` (20.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (43.2%) | `nickel_foam` (37.0%) | `platinum_generic` (8.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (93.8%) | `ABSENT` (4.4%) | `divided` (1.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (87.1%) | `ABSENT` (6.9%) | `Li` (5.6%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (46.3%) | `ABSENT` (20.0%) | `carboxylate` (11.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.8%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.3%) | `Co_complex` (1.8%) | `Mn_complex` (1.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (43.8%) | `polar_aprotic_amide` (17.4%) | `ABSENT` (17.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (74%) | `FC(F)(F)c1ccccc1` (23%) | `ClCCl` (7%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `O=C1CCC(=O)N1Br` (2%) | `O=O` (2%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Br-].[Br-].[Mn+2]` (1%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2595  yield=20.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #22)

```
C=C(C)c1ccccc1.CC(=O)CC(=O)c1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>CC(=O)OC(C)(c1ccccc1)CC(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_zinc` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (57.6%) | `reticulated_vitreous_carbon` (14.6%) | `graphite_rod` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (46.3%) | `stainless_steel` (27.4%) | `platinum` (13.2%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (67.4%) | `stainless_steel_generic` (11.5%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.8%) | `divided` (1.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (66.3%) | `ABSENT` (13.8%) | `NEt4` (13.8%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (83.9%) | `ABSENT` (6.4%) | `PF6` (4.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (14.1%) | `ABSENT` (5.7%) | `polyhalo_radical_transfer` (4.1%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.8%) | `pyridine_organocat` (1.0%) | `Mn_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.4%) | `polar_protic_alcohol` (19.7%) | `ABSENT` (13.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (67%) | `FC(F)(F)c1ccccc1` (27%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (18%) | `CC[SiH](CC)CC` (9%) | `O` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC(C)(C)c1cc(C=N[C` (0%) | set ✓ / any ✓ |

---

### Reaction #2596  yield=50.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #23)

```
C=C(C)c1ccccc1.CC(=O)CC(=O)c1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(OC(C)(c1ccccc1)CC(C)=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `sacrificial_magnesium` (0.4%) | `platinum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (86.3%) | `graphite_rod` (3.3%) | `zinc_plate` (3.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (91.9%) | `platinum` (5.5%) | `nickel` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `graphite_rod` (32.5%) | `graphite_generic` (11.2%) | `carbon_felt` (10.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `divided` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (90.5%) | `Li` (6.6%) | `NEt4` (1.7%) | ✗ |
| 电解质 anion | 26 | `PF6` | `BF4` (70.4%) | `ClO4` (14.0%) | `PF6` (11.9%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (10.6%) | `n_halo_imide` (7.3%) | `ABSENT` (5.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (83.9%) | `Mn_complex` (8.7%) | `Fe_complex` (2.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (83.4%) | `ABSENT` (8.4%) | `polar_aprotic_amide` (5.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (92%) | `FC(F)(F)c1ccccc1` (7%) | `CCOCC` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Cs+` (30%) | `CC[SiH](CC)CC` (19%) | `O=C1CCC(=O)N1Br` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Br][Mn][Br]` (0%) | `CC(C)(C)c1cc(C=N[C` (0%) | set ✓ / any ✓ |

---

### Reaction #2597  yield=32.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #24)

```
C=Cc1ccccc1.COC(=O)CC(=O)c1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>COC(=O)C(=O)OC(CC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.0%) | `sacrificial_zinc` (1.3%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (74.3%) | `reticulated_vitreous_carbon` (20.4%) | `pencil_graphite` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (55.9%) | `platinum` (27.4%) | `nickel` (9.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `carbon_generic` (23.1%) | `carbon_felt` (21.3%) | `platinum_generic` (12.2%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (56.8%) | `undivided` (38.4%) | `divided` (4.8%) | ✓ |
| 电解质 cation | 23 | `pyridinium` | `ABSENT` (58.8%) | `NBu4` (27.1%) | `Li` (8.3%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (47.8%) | `carboxylate` (9.6%) | `PF6` (9.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.3%) | `alkali_other_salt` (3.7%) | `tertiary_amine` (3.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.6%) | `ammonium_PTC_organocat` (0.8%) | `Mn_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (83.2%) | `halogenated_aliphatic` (4.4%) | `aqueous` (2.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `O` (73%) | `C1COCCO1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O=O` (2%) | `O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `__OTHER__` (2%) | `c1ccncc1` (1%) | set ✓ / any ✓ |

---

### Reaction #2598  yield=32.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t1.json) (反应 idx 在该 JSON 内 = #25)

```
C=Cc1ccccc1.COC(=O)CC(=O)c1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>COC(=O)C(=O)CC(OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.7%) | `sacrificial_zinc` (4.5%) | `sacrificial_iron` (2.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (39.5%) | `reticulated_vitreous_carbon` (37.2%) | `pencil_graphite` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (33.2%) | `platinum` (31.5%) | `carbon` (29.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (25.0%) | `nickel_foam` (19.4%) | `carbon_felt` (15.4%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (53.8%) | `undivided` (42.1%) | `divided` (4.1%) | ✓ |
| 电解质 cation | 23 | `pyridinium` | `NBu4` (63.8%) | `ABSENT` (26.8%) | `Li` (7.5%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (33.6%) | `Cl` (20.0%) | `PF6` (16.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `tertiary_amine` (8.2%) | `carboxylic_acid` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.2%) | `Co_complex` (0.6%) | `Mn_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (65.9%) | `ABSENT` (14.8%) | `ketone` (10.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (95%) | `CC(C)=O` (6%) | `O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O` (1%) | `CC1(C)CCCC(C)(C)N1` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2599  yield=60.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t2.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t2.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCC>>O=C(c1ccccc1)C(/C=C/CC)C(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (52.0%) | `reticulated_vitreous_carbon` (26.2%) | `carbon_generic` (18.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (73.8%) | `platinum` (16.2%) | `carbon` (9.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_generic` (35.4%) | `nickel_foam` (34.4%) | `platinum_generic` (19.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `ABSENT` (0.6%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `Li` (82.0%) | `NBu4` (16.4%) | `ABSENT` (1.5%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (41.6%) | `PF6` (21.1%) | `molecular_no_ion` (14.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (5.3%) | `tertiary_amine` (3.9%) | `metal_oxide_oxidant` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.5%) | `brønsted_acid_cat` (0.4%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.7%) | `ABSENT` (30.0%) | `polar_aprotic_amide` (6.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)(C)O` + `O` | `CC#N` (92%) | `CN(C)C=O` (0%) | `CC(=O)N(C)C` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `[I-].[NH4+]` | `__ABSENT__` (99%) | `__OTHER__` (0%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Br-].[Mn+2]` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2600  yield=65.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t2.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t2.json) (反应 idx 在该 JSON 内 = #1)

```
C=CCCCCCC>>O=C(c1ccccc1)C(/C=C/CCCCC)C(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.4%) | `sacrificial_zinc` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (61.6%) | `graphite_generic` (15.3%) | `carbon_generic` (11.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (47.2%) | `platinum` (33.1%) | `nickel` (18.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (40.7%) | `platinum_foil` (21.9%) | `carbon_felt` (9.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (93.1%) | `ABSENT` (6.1%) | `divided` (0.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `Li` (98.3%) | `NBu4` (0.9%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (40.5%) | `ClO4` (19.1%) | `carboxylate` (17.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.8%) | `carboxylic_acid` (2.3%) | `tertiary_amine` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (62.3%) | `pyridine_organocat` (16.6%) | `Co_complex` (8.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.2%) | `ABSENT` (1.6%) | `ketone` (1.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `CC#N` (99%) | `O` (0%) | `CN(C)C=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I)cc1` + `O=C([O-])[O-].[Ca+` | `__ABSENT__` (100%) | `__OTHER__` (2%) | `OB(O)B(O)O` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (95%) | `O=S(=O)(O)C(F)(F)F` (2%) | `[Cl-].[Cl-].[Ni+2]` (1%) | set ✗ / any ✗ |

---

### Reaction #2601  yield=65.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t2.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t2.json) (反应 idx 在该 JSON 内 = #2)

```
C1=CCCCC1>>O=C(c1ccccc1)C(C2CCCC=C2)C(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.4%) | `platinum` (5.7%) | `sacrificial_magnesium` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (98.6%) | `graphite_generic` (0.4%) | `carbon_felt` (0.3%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (70.3%) | `platinum` (21.8%) | `nickel` (7.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `carbon_generic` (81.5%) | `nickel_generic` (4.9%) | `platinum_foil` (4.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `pyridinium` | `Li` (54.9%) | `NBu4` (43.1%) | `ABSENT` (1.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (52.9%) | `BF4` (33.4%) | `PF6` (10.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (12.8%) | `silane_other` (2.1%) | `metal_oxide_oxidant` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.8%) | `Mn_complex` (1.8%) | `brønsted_acid_cat` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_amide` (42.9%) | `polar_aprotic_nitrile` (38.4%) | `polar_aprotic_sulfoxide` (10.1%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CC#N` (83%) | `O` (21%) | `CO` (7%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `O=C(O)C(F)(F)F` | `O=O` (43%) | `CC(=O)O` (22%) | `O=C(O)C(F)(F)F` (10%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (80%) | `[Fe+2].c1cc[cH-]c1` (7%) | `[Pt]` (3%) | set ✓ / any ✓ |

---

### Reaction #2602  yield=66.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c01237_p2_t2.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c01237_p2_t2.json) (反应 idx 在该 JSON 内 = #3)

```
C1=Cc2ccccc2C1>>O=C(c1ccccc1)C(C2CCc3ccccc23)C(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (98.1%) | `graphite_generic` (0.9%) | `carbon_felt` (0.4%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (84.6%) | `platinum` (14.0%) | `nickel` (0.9%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `carbon_generic` (70.3%) | `platinum_foil` (11.6%) | `graphite_felt` (6.5%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (67.1%) | `undivided` (21.2%) | `ABSENT` (11.7%) | ✓ |
| 电解质 cation | 23 | `pyridinium` | `Li` (74.3%) | `NBu4` (24.6%) | `ABSENT` (0.4%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ClO4` (69.4%) | `BF4` (11.2%) | `PF6` (10.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (19.2%) | `ABSENT` (7.2%) | `borohydride` (2.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.0%) | `brønsted_acid_cat` (1.0%) | `Mn_complex` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (61.7%) | `polar_aprotic_nitrile` (20.8%) | `polar_protic_acid` (5.7%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `O` (97%) | `CC#N` (78%) | `CO` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `O=C(O)C(F)(F)F` (98%) | `O=O` (1%) | `CC(=O)O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `O=S(=O)([O-])C(F)(` | `__ABSENT__` (88%) | `O=S(=O)([O-])C(F)(` (9%) | `[Pt]` (2%) | set ✗ / any ✓ |

---

### Reaction #2603  yield=70.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2604  yield=65.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2605  yield=75.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✗ |
| 电解质 anion | 26 | `OTs` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2606  yield=80.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2607  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2608  yield=60.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2609  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2610  yield=65.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c00929_p2_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2611  yield=30.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2612  yield=35.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2613  yield=14.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2614  yield=37.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2615  yield=21.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2616  yield=43.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2617  yield=26.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2618  yield=36.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2619  yield=61.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2620  yield=50.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2621  yield=92.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `lead` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2622  yield=72.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `lead` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2623  yield=42.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2624  yield=86.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_zinc` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2625  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `lead` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2626  yield=68.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `lead` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `K` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2627  yield=35.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1.O>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.0%) | `platinum` (2.8%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `reticulated_vitreous_carbon` (36.7%) | `glassy_carbon` (27.0%) | `graphite_rod` (10.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.8%) | `carbon` (0.1%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (76.5%) | `platinum_plate` (22.4%) | `platinum_foil` (0.6%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (95.2%) | `ABSENT` (4.8%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (72.6%) | `ABSENT` (14.0%) | `NBu4` (7.2%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (57.7%) | `ABSENT` (20.9%) | `PF6` (12.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (20.8%) | `alkali_other_salt` (6.7%) | `ABSENT` (3.6%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (45.3%) | `pyridine_organocat` (45.3%) | `organic_neutral_cat` (3.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (77.8%) | `polar_protic_alcohol` (17.2%) | `polar_aprotic_sulfoxide` (2.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (54%) | `CC(C)=O` (40%) | `O` (7%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (34%) | `O=C(O)C(F)(F)F` (10%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `__OTHER__` (1%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2628  yield=21.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2629  yield=25.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2630  yield=43.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2631  yield=36.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2632  yield=30.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2633  yield=32.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2634  yield=26.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2635  yield=37.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2636  yield=21.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_sup_1_p4_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_sup_1_p4_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1.O>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.0%) | `platinum` (2.8%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `reticulated_vitreous_carbon` (36.7%) | `glassy_carbon` (27.0%) | `graphite_rod` (10.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (76.5%) | `platinum_plate` (22.4%) | `platinum_foil` (0.6%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (95.2%) | `ABSENT` (4.8%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (72.6%) | `ABSENT` (14.0%) | `NBu4` (7.2%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (57.7%) | `ABSENT` (20.9%) | `PF6` (12.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (20.8%) | `alkali_other_salt` (6.7%) | `ABSENT` (3.6%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (45.3%) | `pyridine_organocat` (45.3%) | `organic_neutral_cat` (3.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (77.8%) | `polar_protic_alcohol` (17.2%) | `polar_aprotic_sulfoxide` (2.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (54%) | `CC(C)=O` (40%) | `O` (7%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (34%) | `O=C(O)C(F)(F)F` (10%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `__OTHER__` (1%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2637  yield=42.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2638  yield=14.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2639  yield=61.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2640  yield=50.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2641  yield=92.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `lead` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2642  yield=68.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `lead` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `K` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2643  yield=63.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `lead` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2644  yield=72.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `lead` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2645  yield=86.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_zinc` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2646  yield=81.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `lead` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2647  yield=45.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `lead` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2648  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c03365_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccn1>>CC(CO)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.6%) | `platinum` (13.6%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (43.0%) | `platinum_foil` (26.5%) | `platinum_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `lead` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_plate` (49.3%) | `platinum_generic` (48.0%) | `platinum_foil` (1.9%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Na` | `K` (68.1%) | `ABSENT` (16.0%) | `Li` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (54.1%) | `ABSENT` (27.5%) | `molecular_no_ion` (6.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.4%) | `alkali_other_salt` (6.5%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.3%) | `pyridine_organocat` (28.4%) | `organic_neutral_cat` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `polar_protic_alcohol` (5.9%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (71%) | `CC#N` (52%) | `CC(C)=O` (35%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (80%) | `O=O` (27%) | `O=C(O)C(F)(F)F` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Pt]` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2649  yield=11.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)c1ccc(Br)cc1.C=Cc1ccccc1.N#Cc1ccncc1>>COC(=O)c1ccc(CC(c2ccccc2)c2ccncc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `sacrificial_zinc` (5.4%) | `sacrificial_iron` (3.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (56.3%) | `zinc_generic` (32.2%) | `carbon_generic` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `platinum` (1.6%) | `nickel` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `carbon_cloth` (77.0%) | `carbon_generic` (10.6%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `flow` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✗ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (48.1%) | `ABSENT` (46.0%) | `NEt4` (4.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (50.9%) | `BF4` (31.9%) | `Br` (8.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carboxylate` (17.1%) | `ABSENT` (12.7%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (92.1%) | `ABSENT` (7.0%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.7%) | `ABSENT` (32.8%) | `polar_aprotic_sulfoxide` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `CO` | `CC#N` (91%) | `C[N+](=O)[O-]` (3%) | `C1COCCO1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (96%) | `C1CN2CCN1CC2` (85%) | `O=C[O-].[Na+]` (79%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1cnc2c(c1)ccc1ccc` (90%) | `__OTHER__` (57%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #2650  yield=0.5%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)c1ccc(Br)cc1.C=Cc1ccccc1.N#Cc1ccncc1>>COC(=O)c1ccc(CC(c2ccccc2)c2ccncc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `sacrificial_zinc` (5.4%) | `sacrificial_iron` (3.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (56.3%) | `zinc_generic` (32.2%) | `carbon_generic` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `platinum` (1.6%) | `nickel` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `carbon_cloth` (77.0%) | `carbon_generic` (10.6%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (48.1%) | `ABSENT` (46.0%) | `NEt4` (4.2%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (50.9%) | `BF4` (31.9%) | `Br` (8.2%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carboxylate` (17.1%) | `ABSENT` (12.7%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (92.1%) | `ABSENT` (7.0%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.7%) | `ABSENT` (32.8%) | `polar_aprotic_sulfoxide` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `CO` | `CC#N` (91%) | `C[N+](=O)[O-]` (3%) | `C1COCCO1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (96%) | `C1CN2CCN1CC2` (85%) | `O=C[O-].[Na+]` (79%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1cnc2c(c1)ccc1ccc` (90%) | `__OTHER__` (57%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #2651  yield=68.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)c1ccc(Br)cc1.C=Cc1ccccc1.N#Cc1ccncc1>>COC(=O)c1ccc(CC(c2ccccc2)c2ccncc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `sacrificial_zinc` (5.4%) | `sacrificial_iron` (3.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (56.3%) | `zinc_generic` (32.2%) | `carbon_generic` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `platinum` (1.6%) | `nickel` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `carbon_cloth` (77.0%) | `carbon_generic` (10.6%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `flow` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✗ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.1%) | `ABSENT` (46.0%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (50.9%) | `BF4` (31.9%) | `Br` (8.2%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carboxylate` (17.1%) | `ABSENT` (12.7%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (92.1%) | `ABSENT` (7.0%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.7%) | `ABSENT` (32.8%) | `polar_aprotic_sulfoxide` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `CO` | `CC#N` (91%) | `C[N+](=O)[O-]` (3%) | `C1COCCO1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (96%) | `C1CN2CCN1CC2` (85%) | `O=C[O-].[Na+]` (79%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1cnc2c(c1)ccc1ccc` (90%) | `__OTHER__` (57%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #2652  yield=21.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)c1ccc(Br)cc1.C=Cc1ccccc1.N#Cc1ccncc1>>COC(=O)c1ccc(CC(c2ccccc2)c2ccncc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `sacrificial_zinc` (5.4%) | `sacrificial_iron` (3.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (56.3%) | `zinc_generic` (32.2%) | `carbon_generic` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `platinum` (1.6%) | `nickel` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `carbon_cloth` (77.0%) | `carbon_generic` (10.6%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `flow` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✗ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.1%) | `ABSENT` (46.0%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ABSENT` (50.9%) | `BF4` (31.9%) | `Br` (8.2%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carboxylate` (17.1%) | `ABSENT` (12.7%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (92.1%) | `ABSENT` (7.0%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.7%) | `ABSENT` (32.8%) | `polar_aprotic_sulfoxide` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `CO` | `CC#N` (91%) | `C[N+](=O)[O-]` (3%) | `C1COCCO1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (96%) | `C1CN2CCN1CC2` (85%) | `O=C[O-].[Na+]` (79%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1cnc2c(c1)ccc1ccc` (90%) | `__OTHER__` (57%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #2653  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)c1ccc(Br)cc1.C=Cc1ccccc1.N#Cc1ccncc1>>COC(=O)c1ccc(CC(c2ccccc2)c2ccncc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `sacrificial_zinc` (5.4%) | `sacrificial_iron` (3.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (56.3%) | `zinc_generic` (32.2%) | `carbon_generic` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (96.3%) | `platinum` (1.6%) | `nickel` (1.4%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `carbon_cloth` (77.0%) | `carbon_generic` (10.6%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `flow` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✗ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.1%) | `ABSENT` (46.0%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (50.9%) | `BF4` (31.9%) | `Br` (8.2%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carboxylate` (17.1%) | `ABSENT` (12.7%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (92.1%) | `ABSENT` (7.0%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.7%) | `ABSENT` (32.8%) | `polar_aprotic_sulfoxide` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `CO` | `CC#N` (91%) | `C[N+](=O)[O-]` (3%) | `C1COCCO1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (96%) | `C1CN2CCN1CC2` (85%) | `O=C[O-].[Na+]` (79%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1cnc2c(c1)ccc1ccc` (90%) | `__OTHER__` (57%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #2654  yield=13.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)c1ccc(Br)cc1.C=Cc1ccccc1.N#Cc1ccncc1>>COC(=O)c1ccc(CC(c2ccccc2)c2ccncc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (88.8%) | `sacrificial_zinc` (5.4%) | `sacrificial_iron` (3.0%) | ✗ |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (56.3%) | `zinc_generic` (32.2%) | `carbon_generic` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `platinum` (1.6%) | `nickel` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `carbon_cloth` (77.0%) | `carbon_generic` (10.6%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `flow` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✗ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.1%) | `ABSENT` (46.0%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (50.9%) | `BF4` (31.9%) | `Br` (8.2%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carboxylate` (17.1%) | `ABSENT` (12.7%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (92.1%) | `ABSENT` (7.0%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.7%) | `ABSENT` (32.8%) | `polar_aprotic_sulfoxide` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `CO` | `CC#N` (91%) | `C[N+](=O)[O-]` (3%) | `C1COCCO1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (96%) | `C1CN2CCN1CC2` (85%) | `O=C[O-].[Na+]` (79%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1cnc2c(c1)ccc1ccc` (90%) | `__OTHER__` (57%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #2655  yield=32.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)c1ccc(Br)cc1.C=Cc1ccccc1.N#Cc1ccncc1>>COC(=O)c1ccc(CC(c2ccccc2)c2ccncc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `sacrificial_zinc` (5.4%) | `sacrificial_iron` (3.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (56.3%) | `zinc_generic` (32.2%) | `carbon_generic` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `platinum` (1.6%) | `nickel` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `carbon_cloth` (77.0%) | `carbon_generic` (10.6%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `flow` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✗ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.1%) | `ABSENT` (46.0%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (50.9%) | `BF4` (31.9%) | `Br` (8.2%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carboxylate` (17.1%) | `ABSENT` (12.7%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (92.1%) | `ABSENT` (7.0%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.7%) | `ABSENT` (32.8%) | `polar_aprotic_sulfoxide` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `CO` | `CC#N` (91%) | `C[N+](=O)[O-]` (3%) | `C1COCCO1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (96%) | `C1CN2CCN1CC2` (85%) | `O=C[O-].[Na+]` (79%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1cnc2c(c1)ccc1ccc` (90%) | `__OTHER__` (57%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #2656  yield=67.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)c1ccc(Br)cc1.C=Cc1ccccc1.N#Cc1ccncc1>>COC(=O)c1ccc(CC(c2ccccc2)c2ccncc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `sacrificial_zinc` (5.4%) | `sacrificial_iron` (3.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (56.3%) | `zinc_generic` (32.2%) | `carbon_generic` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `platinum` (1.6%) | `nickel` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `carbon_cloth` (77.0%) | `carbon_generic` (10.6%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `flow` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✗ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.1%) | `ABSENT` (46.0%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ABSENT` (50.9%) | `BF4` (31.9%) | `Br` (8.2%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carboxylate` (17.1%) | `ABSENT` (12.7%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (92.1%) | `ABSENT` (7.0%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.7%) | `ABSENT` (32.8%) | `polar_aprotic_sulfoxide` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `CO` | `CC#N` (91%) | `C[N+](=O)[O-]` (3%) | `C1COCCO1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (96%) | `C1CN2CCN1CC2` (85%) | `O=C[O-].[Na+]` (79%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1cnc2c(c1)ccc1ccc` (90%) | `__OTHER__` (57%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #2657  yield=62.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)c1ccc(Br)cc1.C=Cc1ccccc1.N#Cc1ccncc1>>COC(=O)c1ccc(CC(c2ccccc2)c2ccncc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `sacrificial_zinc` (5.4%) | `sacrificial_iron` (3.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (56.3%) | `zinc_generic` (32.2%) | `carbon_generic` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `platinum` (1.6%) | `nickel` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `carbon_cloth` (77.0%) | `carbon_generic` (10.6%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `flow` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✗ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.1%) | `ABSENT` (46.0%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (50.9%) | `BF4` (31.9%) | `Br` (8.2%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carboxylate` (17.1%) | `ABSENT` (12.7%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (92.1%) | `ABSENT` (7.0%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.7%) | `ABSENT` (32.8%) | `polar_aprotic_sulfoxide` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `CO` | `CC#N` (91%) | `C[N+](=O)[O-]` (3%) | `C1COCCO1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (96%) | `C1CN2CCN1CC2` (85%) | `O=C[O-].[Na+]` (79%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1cnc2c(c1)ccc1ccc` (90%) | `__OTHER__` (57%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #2658  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)c1ccc(Br)cc1.C=Cc1ccccc1.N#Cc1ccncc1>>COC(=O)c1ccc(CC(c2ccccc2)c2ccncc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `sacrificial_zinc` (5.4%) | `sacrificial_iron` (3.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (56.3%) | `zinc_generic` (32.2%) | `carbon_generic` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `platinum` (1.6%) | `nickel` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `carbon_cloth` (77.0%) | `carbon_generic` (10.6%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.1%) | `ABSENT` (46.0%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (50.9%) | `BF4` (31.9%) | `Br` (8.2%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carboxylate` (17.1%) | `ABSENT` (12.7%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (92.1%) | `ABSENT` (7.0%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.7%) | `ABSENT` (32.8%) | `polar_aprotic_sulfoxide` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `CO` | `CC#N` (91%) | `C[N+](=O)[O-]` (3%) | `C1COCCO1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (96%) | `C1CN2CCN1CC2` (85%) | `O=C[O-].[Na+]` (79%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1cnc2c(c1)ccc1ccc` (90%) | `__OTHER__` (57%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #2659  yield=40.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)c1ccc(Br)cc1.C=Cc1ccccc1.N#Cc1ccncc1>>COC(=O)c1ccc(CC(c2ccccc2)c2ccncc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `sacrificial_zinc` (5.4%) | `sacrificial_iron` (3.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (56.3%) | `zinc_generic` (32.2%) | `carbon_generic` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `platinum` (1.6%) | `nickel` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `carbon_cloth` (77.0%) | `carbon_generic` (10.6%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `flow` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✗ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.1%) | `ABSENT` (46.0%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (50.9%) | `BF4` (31.9%) | `Br` (8.2%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carboxylate` (17.1%) | `ABSENT` (12.7%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (92.1%) | `ABSENT` (7.0%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.7%) | `ABSENT` (32.8%) | `polar_aprotic_sulfoxide` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `CO` | `CC#N` (91%) | `C[N+](=O)[O-]` (3%) | `C1COCCO1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (96%) | `C1CN2CCN1CC2` (85%) | `O=C[O-].[Na+]` (79%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1cnc2c(c1)ccc1ccc` (90%) | `__OTHER__` (57%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #2660  yield=0.5%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)c1ccc(Br)cc1.C=Cc1ccccc1.N#Cc1ccncc1>>COC(=O)c1ccc(CC(c2ccccc2)c2ccncc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `sacrificial_zinc` (5.4%) | `sacrificial_iron` (3.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (56.3%) | `zinc_generic` (32.2%) | `carbon_generic` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `platinum` (1.6%) | `nickel` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `carbon_cloth` (77.0%) | `carbon_generic` (10.6%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `flow` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✗ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.1%) | `ABSENT` (46.0%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (50.9%) | `BF4` (31.9%) | `Br` (8.2%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carboxylate` (17.1%) | `ABSENT` (12.7%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (92.1%) | `ABSENT` (7.0%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.7%) | `ABSENT` (32.8%) | `polar_aprotic_sulfoxide` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `CO` | `CC#N` (91%) | `C[N+](=O)[O-]` (3%) | `C1COCCO1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (96%) | `C1CN2CCN1CC2` (85%) | `O=C[O-].[Na+]` (79%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1cnc2c(c1)ccc1ccc` (90%) | `__OTHER__` (57%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #2661  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)c1ccc(Br)cc1.C=Cc1ccccc1.N#Cc1ccncc1>>COC(=O)c1ccc(CC(c2ccccc2)c2ccncc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `sacrificial_zinc` (5.4%) | `sacrificial_iron` (3.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (56.3%) | `zinc_generic` (32.2%) | `carbon_generic` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `platinum` (1.6%) | `nickel` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `carbon_cloth` (77.0%) | `carbon_generic` (10.6%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.1%) | `ABSENT` (46.0%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (50.9%) | `BF4` (31.9%) | `Br` (8.2%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carboxylate` (17.1%) | `ABSENT` (12.7%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (92.1%) | `ABSENT` (7.0%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.7%) | `ABSENT` (32.8%) | `polar_aprotic_sulfoxide` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `CO` | `CC#N` (91%) | `C[N+](=O)[O-]` (3%) | `C1COCCO1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (96%) | `C1CN2CCN1CC2` (85%) | `O=C[O-].[Na+]` (79%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1cnc2c(c1)ccc1ccc` (90%) | `__OTHER__` (57%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #2662  yield=0.0%

**Source paper**: [`OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json`](reactions_by_journal_alkene_ec_audited/OrgLett/10.1021_acs.orglett.5c04052_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)c1ccc(Br)cc1.C=Cc1ccccc1.N#Cc1ccncc1>>COC(=O)c1ccc(CC(c2ccccc2)c2ccncc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `sacrificial_zinc` (5.4%) | `sacrificial_iron` (3.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (56.3%) | `zinc_generic` (32.2%) | `carbon_generic` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `platinum` (1.6%) | `nickel` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `unknown_electrode` | `carbon_cloth` (77.0%) | `carbon_generic` (10.6%) | `graphite_rod` (5.4%) | ✗ |
| 池型 | 4 | `flow` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✗ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.1%) | `ABSENT` (46.0%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (50.9%) | `BF4` (31.9%) | `Br` (8.2%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carboxylate` (17.1%) | `ABSENT` (12.7%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (92.1%) | `ABSENT` (7.0%) | `Ni_complex` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (59.7%) | `ABSENT` (32.8%) | `polar_aprotic_sulfoxide` (4.3%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `CO` | `CC#N` (91%) | `C[N+](=O)[O-]` (3%) | `C1COCCO1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCN(CC)CC` | `CC(=O)[O-].[Na+]` (96%) | `C1CN2CCN1CC2` (85%) | `O=C[O-].[Na+]` (79%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1cnc2c(c1)ccc1ccc` (90%) | `__OTHER__` (57%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #2663  yield=20.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_14_3506-3510.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_14_3506-3510.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCCCCCCC=C=CC1(O)CCCCC1>>BrCC(Br)CCCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.9%) | `platinum` (2.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (99.4%) | `platinum_wire` (0.3%) | `reticulated_vitreous_carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (69.0%) | `carbon` (31.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (65.1%) | `platinum_foil` (33.0%) | `platinum_generic` (1.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `K` | `molecular_no_ion` (44.8%) | `ABSENT` (41.3%) | `NEt4` (5.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (78.5%) | `ABSENT` (19.7%) | `Br` (1.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `polyhalo_radical_transfer` (26.9%) | `alkali_other_salt` (12.2%) | `ABSENT` (8.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (88.1%) | `Mn_complex` (6.4%) | `brønsted_acid_cat` (3.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.4%) | `polar_protic_acid` (0.6%) | `halogenated_aliphatic` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (90%) | `O` (87%) | `OC(C(F)(F)F)C(F)(F` (24%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=S([O-])([O-])=S.` (40%) | `OC(C(F)(F)F)C(F)(F` (18%) | `ClCC(Cl)(Cl)Cl` (13%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (87%) | `[Cl][Mn][Cl]` (5%) | `O=S(=O)([O-])C(F)(` (2%) | set ✓ / any ✓ |

---

### Reaction #2664  yield=20.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_14_3506-3510.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_14_3506-3510.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCCCCCCC=C=CC1(O)CCCCC1>>BrCC(Br)CCCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.9%) | `platinum` (2.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (99.4%) | `platinum_wire` (0.3%) | `reticulated_vitreous_carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (69.0%) | `carbon` (31.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (65.1%) | `platinum_foil` (33.0%) | `platinum_generic` (1.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `K` | `molecular_no_ion` (44.8%) | `ABSENT` (41.3%) | `NEt4` (5.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (78.5%) | `ABSENT` (19.7%) | `Br` (1.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `polyhalo_radical_transfer` (26.9%) | `alkali_other_salt` (12.2%) | `ABSENT` (8.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (88.1%) | `Mn_complex` (6.4%) | `brønsted_acid_cat` (3.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.4%) | `polar_protic_acid` (0.6%) | `halogenated_aliphatic` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (90%) | `O` (87%) | `OC(C(F)(F)F)C(F)(F` (24%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=S([O-])([O-])=S.` (40%) | `OC(C(F)(F)F)C(F)(F` (18%) | `ClCC(Cl)(Cl)Cl` (13%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (87%) | `[Cl][Mn][Cl]` (5%) | `O=S(=O)([O-])C(F)(` (2%) | set ✓ / any ✓ |

---

### Reaction #2665  yield=44.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_14_3506-3510.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_14_3506-3510.json) (反应 idx 在该 JSON 内 = #2)

```
C=CCCCCCCCCC=C=CC1(O)CCCCC1>>C=CCCCCCCCCC1OC2(C=C1Br)CCCCC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (88.2%) | `glassy_carbon` (9.3%) | `carbon_generic` (0.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.9%) | `carbon` (4.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (90.8%) | `platinum_plate` (5.6%) | `graphite_generic` (2.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `K` | `ABSENT` (79.8%) | `Na` (10.2%) | `molecular_no_ion` (7.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (68.9%) | `molecular_no_ion` (29.0%) | `Br` (1.9%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (32.1%) | `carboxylic_acid` (6.8%) | `ABSENT` (4.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.2%) | `Mn_complex` (4.4%) | `brønsted_acid_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.8%) | `polar_aprotic_sulfoxide` (0.6%) | `aqueous` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (96%) | `CC(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)O.[Na]` (51%) | `O=S([O-])([O-])=S.` (9%) | `__ABSENT__` (4%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Cl][Mn][Cl]` (1%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2666  yield=11.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #0)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.CCC=Cc1ccccc1>>CC[C@@H](CC(=O)c1ccccc1)[C@H](OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (58.4%) | `graphite_generic` (21.0%) | `carbon_felt` (7.3%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.3%) | `nickel` (10.3%) | `carbon` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (85.8%) | `platinum_wire` (6.7%) | `nickel_plate` (1.3%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (89.5%) | `divided` (5.5%) | `ABSENT` (5.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (55.7%) | `Li` (29.7%) | `NEt4` (7.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (85.1%) | `ClO4` (8.8%) | `ABSENT` (2.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `carboxylic_acid` (5.2%) | `inorganic_simple` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.0%) | `Mn_complex` (1.3%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (54.8%) | `polar_aprotic_nitrile` (43.8%) | `polar_aprotic_amide` (0.6%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (65%) | `CC#N` (5%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (1%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2667  yield=21.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #1)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.CCC=Cc1ccccc1>>CC[C@H](CC(=O)c1ccccc1)[C@H](OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (58.4%) | `graphite_generic` (21.0%) | `carbon_felt` (7.3%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.3%) | `nickel` (10.3%) | `carbon` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (85.8%) | `platinum_wire` (6.7%) | `nickel_plate` (1.3%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (89.5%) | `divided` (5.5%) | `ABSENT` (5.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (55.7%) | `Li` (29.7%) | `NEt4` (7.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (85.1%) | `ClO4` (8.8%) | `ABSENT` (2.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `carboxylic_acid` (5.2%) | `inorganic_simple` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.0%) | `Mn_complex` (1.3%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (54.8%) | `polar_aprotic_nitrile` (43.8%) | `polar_aprotic_amide` (0.6%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (65%) | `CC#N` (5%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (1%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2668  yield=29.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #2)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.CC=Cc1ccccc1>>CC(CC(=O)c1ccccc1)C(OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `sacrificial_iron` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (29.3%) | `graphite_rod` (28.2%) | `carbon_generic` (12.1%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `nickel` (50.8%) | `platinum` (42.5%) | `carbon` (3.4%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `nickel_foam` (63.2%) | `platinum_wire` (9.8%) | `platinum_generic` (9.3%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (62.2%) | `undivided` (31.2%) | `divided` (6.6%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (80.3%) | `ABSENT` (15.8%) | `Li` (3.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (92.2%) | `ABSENT` (6.4%) | `ClO4` (0.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.6%) | `carboxylic_acid` (3.2%) | `n_halo_imide` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (83.8%) | `Mn_complex` (6.6%) | `Fe_complex` (3.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (87.5%) | `polar_aprotic_nitrile` (10.2%) | `ketone` (1.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (95%) | `CC#N` (0%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O` (1%) | `C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2669  yield=26.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #3)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.CC=Cc1ccccc1>>C[C@@H](CC(=O)c1ccccc1)[C@H](OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `sacrificial_iron` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (29.3%) | `graphite_rod` (28.2%) | `carbon_generic` (12.1%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `nickel` (50.8%) | `platinum` (42.5%) | `carbon` (3.4%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `nickel_foam` (63.2%) | `platinum_wire` (9.8%) | `platinum_generic` (9.3%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (62.2%) | `undivided` (31.2%) | `divided` (6.6%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (80.3%) | `ABSENT` (15.8%) | `Li` (3.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (92.2%) | `ABSENT` (6.4%) | `ClO4` (0.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.6%) | `carboxylic_acid` (3.2%) | `n_halo_imide` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (83.8%) | `Mn_complex` (6.6%) | `Fe_complex` (3.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (87.5%) | `polar_aprotic_nitrile` (10.2%) | `ketone` (1.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (95%) | `CC#N` (0%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O` (1%) | `C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2670  yield=27.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #4)

```
C=Cc1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1.CC1(C)CCCC(C)(C)N1[O]>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (68.6%) | `carbon_felt` (20.1%) | `reticulated_vitreous_carbon` (6.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (90.3%) | `nickel` (8.8%) | `ABSENT` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (96.6%) | `platinum_foil` (2.7%) | `nickel_plate` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (92.0%) | `NBu4` (7.8%) | `Na` (0.1%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (96.3%) | `BF4` (3.1%) | `PF6` (0.4%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (8.9%) | `carboxylic_acid` (6.3%) | `alkali_other_salt` (3.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.2%) | `Mn_complex` (0.4%) | `pyridine_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (67.8%) | `ABSENT` (28.4%) | `halogenated_aliphatic` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (96%) | `OC(C(F)(F)F)C(F)(F` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (1%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2671  yield=36.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #12)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(OC)cc1>>COc1ccc(C(CCC(=O)c2ccccc2)OC(=O)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (50.5%) | `carbon_rod` (22.1%) | `carbon_cloth` (14.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (82.1%) | `nickel` (10.1%) | `carbon` (5.4%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (56.7%) | `platinum_generic` (38.5%) | `nickel_foam` (1.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `divided` (0.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.5%) | `ABSENT` (11.3%) | `Li` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (34.9%) | `carboxylate` (29.7%) | `ABSENT` (18.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.2%) | `carboxylic_acid` (2.5%) | `tertiary_amine` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `ionic_organocat` (0.4%) | `brønsted_acid_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (43.8%) | `ABSENT` (29.0%) | `ketone` (17.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (79%) | `CC(C)=O` (74%) | `ClCCl` (18%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C1CCC(=O)N1Br` (79%) | `C` (67%) | `__ABSENT__` (45%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2672  yield=38.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #6)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(C(=O)OC)cc1>>COC(=O)c1ccc(C(CCC(=O)c2ccccc2)OC(=O)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (53.2%) | `carbon_rod` (18.5%) | `reticulated_vitreous_carbon` (13.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (85.4%) | `nickel` (9.1%) | `carbon` (5.2%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (98.7%) | `platinum_generic` (0.6%) | `nickel_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.2%) | `ABSENT` (3.2%) | `Li` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (26.2%) | `PF6` (24.2%) | `carboxylate` (13.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.6%) | `carboxylic_acid` (3.8%) | `inorganic_simple` (3.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `Mn_complex` (0.1%) | `ammonium_PTC_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (81.7%) | `polar_aprotic_nitrile` (16.9%) | `ketone` (0.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (95%) | `FC(F)(F)c1ccccc1` (21%) | `CCOCC` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (7%) | `O=O` (5%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2673  yield=37.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #7)

```
C=Cc1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(CCC([18O]C(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.6%) | `platinum` (6.7%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (54.3%) | `graphite_rod` (24.0%) | `platinum_plate` (5.8%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (84.2%) | `platinum` (8.4%) | `nickel` (2.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (65.4%) | `carbon_felt` (11.5%) | `carbon_rod` (11.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (95.9%) | `ABSENT` (2.8%) | `divided` (1.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (53.6%) | `NEt4` (22.6%) | `NBu4` (16.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (65.1%) | `BF4` (14.8%) | `fluoride_complex` (7.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (6.8%) | `polyhalo_radical_transfer` (6.1%) | `o2_oxidant` (5.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (88.3%) | `ABSENT` (7.1%) | `halogenated_aliphatic` (2.4%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `C1COCCO1` (48%) | `CC#N` (41%) | `ClCCl` (21%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `O=O` (94%) | `O` (84%) | `OB(O)B(O)O` (84%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (82%) | `__ABSENT__` (53%) | `__OTHER__` (44%) | set ✗ / any ✓ |

---

### Reaction #2674  yield=46.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #8)

```
C=Cc1ccccc1.Cc1ccc(C(=O)CC(=O)c2ccc(C)cc2)cc1>>Cc1ccc(C(=O)CCC(OC(=O)c2ccc(C)cc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (94.3%) | `carbon_rod` (3.5%) | `reticulated_vitreous_carbon` (1.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (78.6%) | `nickel` (16.4%) | `carbon` (4.8%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (94.6%) | `graphite_rod` (3.0%) | `nickel_plate` (0.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (76.5%) | `NBu4` (23.1%) | `Li` (0.1%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (90.5%) | `BF4` (6.6%) | `PF6` (1.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.1%) | `alkali_other_salt` (6.9%) | `n_halo_imide` (6.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.2%) | `ammonium_PTC_organocat` (0.5%) | `Co_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (58.9%) | `ABSENT` (39.1%) | `halogenated_aliphatic` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (96%) | `FC(F)(F)c1ccccc1` (2%) | `C[N+](=O)[O-]` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `O` (3%) | `O=O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `c1ccncc1` (3%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #2675  yield=46.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #9)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(C(F)(F)F)cc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccc(C(F)(F)F)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (97.0%) | `graphite_rod` (2.1%) | `graphite_generic` (0.5%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (91.5%) | `carbon` (3.5%) | `nickel` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (99.7%) | `platinum_generic` (0.2%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (90.3%) | `ABSENT` (9.2%) | `Li` (0.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (55.3%) | `ABSENT` (34.3%) | `PF6` (4.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.7%) | `n_halo_imide` (2.7%) | `metal_oxide_oxidant` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `pyridine_organocat` (0.2%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (49.3%) | `polar_aprotic_nitrile` (45.7%) | `halogenated_aliphatic` (4.6%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (69%) | `ClCCl` (24%) | `CC#N` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `__OTHER__` (7%) | `O=O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2676  yield=42.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #10)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1cccc(OC)c1>>COc1cccc(C(CCC(=O)c2ccccc2)OC(=O)c2ccccc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (41.0%) | `carbon_rod` (39.8%) | `reticulated_vitreous_carbon` (8.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.1%) | `carbon` (4.1%) | `nickel` (2.6%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (90.4%) | `platinum_generic` (7.2%) | `graphite_rod` (0.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (59.8%) | `ABSENT` (30.1%) | `NEt4` (8.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (38.8%) | `BF4` (25.5%) | `PF6` (21.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.9%) | `carboxylic_acid` (4.6%) | `metal_oxide_oxidant` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (94.3%) | `polar_aprotic_nitrile` (5.5%) | `ketone` (0.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (90%) | `CCOCC` (6%) | `ClCCl` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (1%) | `O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2677  yield=48.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #11)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1cccc(Br)c1>>O=C(CCC(OC(=O)c1ccccc1)c1cccc(Br)c1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (87.5%) | `graphite_rod` (5.7%) | `graphite_generic` (2.9%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (78.6%) | `nickel` (18.2%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (99.2%) | `nickel_plate` (0.4%) | `nickel_foam` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.7%) | `ABSENT` (6.0%) | `Li` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (62.3%) | `ABSENT` (20.7%) | `PF6` (14.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.9%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `Mn_complex` (0.2%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (85.2%) | `polar_aprotic_nitrile` (13.4%) | `halogenated_aliphatic` (0.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `FC(F)(F)c1ccccc1` (4%) | `CCOCC` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2678  yield=60.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #12)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1cccc(F)c1>>O=C(CCC(OC(=O)c1ccccc1)c1cccc(F)c1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (81.0%) | `reticulated_vitreous_carbon` (6.1%) | `graphite_rod` (5.7%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.0%) | `nickel` (5.1%) | `stainless_steel` (0.9%) | ✗ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (96.6%) | `platinum_generic` (1.7%) | `nickel_foam` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (90.1%) | `ABSENT` (8.8%) | `protonated_amine` (0.4%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (56.7%) | `ABSENT` (25.1%) | `PF6` (12.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.3%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `pyridine_organocat` (0.3%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (97.5%) | `polar_aprotic_nitrile` (1.3%) | `halogenated_aliphatic` (0.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (99%) | `ClCCl` (0%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (1%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2679  yield=59.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #13)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1OC>>COc1ccccc1C(CCC(=O)c1ccccc1)OC(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.4%) | `sacrificial_iron` (2.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `iron_plate` (36.2%) | `carbon_rod` (32.7%) | `reticulated_vitreous_carbon` (17.7%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `nickel` (89.2%) | `platinum` (7.6%) | `carbon` (2.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `nickel_foam` (40.2%) | `nickel_plate` (35.6%) | `platinum_plate` (18.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (97.3%) | `divided` (2.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.6%) | `ABSENT` (1.1%) | `Li` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (55.0%) | `PF6` (22.3%) | `carboxylate` (13.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.9%) | `tertiary_amine` (2.8%) | `water` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.9%) | `Mn_complex` (1.2%) | `Fe_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (98.2%) | `ketone` (1.3%) | `polar_aprotic_nitrile` (0.2%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (100%) | `CC(C)=O` (4%) | `CCOCC` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `CC[C@H](C)[C@H]1CN` (0%) | set ✓ / any ✓ |

---

### Reaction #2680  yield=54.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #14)

```
C=Cc1ccccc1.O=C(CC(=O)c1ccc(F)cc1)c1ccc(F)cc1>>O=C(CCC(OC(=O)c1ccc(F)cc1)c1ccccc1)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (84.1%) | `carbon_rod` (15.3%) | `iron_plate` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (83.5%) | `nickel` (11.3%) | `carbon` (5.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (95.1%) | `graphite_rod` (2.9%) | `nickel_plate` (1.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (56.8%) | `ABSENT` (42.8%) | `NEt4` (0.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (73.9%) | `BF4` (21.6%) | `I` (1.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ammonium_salt` | `ABSENT` (19.9%) | `n_halo_imide` (3.2%) | `polyhalo_radical_transfer` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `pyridine_organocat` (0.3%) | `ammonium_PTC_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (88.5%) | `polar_aprotic_nitrile` (11.1%) | `halogenated_aliphatic` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (99%) | `CC#N` (0%) | `FC(F)(F)c1ccccc1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `O=O` (1%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2681  yield=54.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #15)

```
C=Cc1ccccc1.COc1ccc(C(=O)CC(=O)c2ccc(OC)cc2)cc1>>COc1ccc(C(=O)CCC(OC(=O)c2ccc(OC)cc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (69.2%) | `carbon_rod` (21.3%) | `carbon_generic` (4.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (81.7%) | `nickel` (11.9%) | `carbon` (5.9%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (89.7%) | `platinum_generic` (7.2%) | `nickel_plate` (1.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (73.0%) | `ABSENT` (25.9%) | `Na` (0.4%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (58.6%) | `BF4` (23.4%) | `PF6` (10.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.0%) | `carboxylic_acid` (5.9%) | `metal_oxide_oxidant` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `Co_complex` (0.1%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (54.1%) | `polar_aprotic_nitrile` (44.3%) | `ketone` (0.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (97%) | `ClCCl` (1%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O` (1%) | `CC1(C)CCCC(C)(C)N1` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2682  yield=56.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #16)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(-c2ccccc2)cc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccc(-c2ccccc2)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (90.5%) | `reticulated_vitreous_carbon` (5.7%) | `graphite_rod` (1.7%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.5%) | `nickel` (3.6%) | `stainless_steel` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (99.7%) | `platinum_generic` (0.2%) | `nickel_foam` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (93.7%) | `ABSENT` (5.3%) | `Li` (0.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (77.3%) | `ABSENT` (13.5%) | `PF6` (5.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.1%) | `as_solvent_halogenated_aliphat` (3.2%) | `metal_oxide_oxidant` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.0%) | `Mn_complex` (1.7%) | `Fe_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (75.5%) | `polar_aprotic_nitrile` (15.1%) | `ketone` (7.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (72%) | `CC(C)=O` (7%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Cl][Mn][Cl]` (0%) | `COCCOC.[Br][Ni][Br` (0%) | set ✓ / any ✓ |

---

### Reaction #2683  yield=62.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #17)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(Cl)cc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccc(Cl)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (54.5%) | `graphite_rod` (27.8%) | `graphite_generic` (3.6%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (68.8%) | `nickel` (20.5%) | `carbon` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (98.6%) | `graphite_rod` (0.4%) | `nickel_plate` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (70.6%) | `NBu4` (29.3%) | `Li` (0.1%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (85.0%) | `BF4` (13.8%) | `PF6` (0.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.6%) | `n_halo_imide` (6.8%) | `ammonium_salt` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `Mn_complex` (0.7%) | `pyridine_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (62.1%) | `ABSENT` (32.6%) | `halogenated_aliphatic` (2.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (88%) | `ClCCl` (4%) | `FC(F)(F)c1ccccc1` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (1%) | `__OTHER__` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2684  yield=62.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #18)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1Cl>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1Cl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (29.5%) | `carbon_rod` (28.0%) | `reticulated_vitreous_carbon` (15.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (59.8%) | `carbon` (21.0%) | `stainless_steel` (10.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (69.0%) | `platinum_generic` (9.0%) | `carbon_felt` (8.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (87.3%) | `divided` (9.1%) | `ABSENT` (3.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.5%) | `ABSENT` (10.3%) | `Li` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (44.5%) | `ABSENT` (27.0%) | `PF6` (20.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.3%) | `carboxylic_acid` (3.1%) | `acid_anhydride` (2.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.6%) | `organic_neutral_cat` (3.4%) | `Mn_complex` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (54.4%) | `ABSENT` (39.4%) | `ketone` (3.5%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `ClCCl` (99%) | `CC(=O)O` (6%) | `OC(C(F)(F)F)C(F)(F` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `O=S(=O)(O)C(F)(F)F` (1%) | `CC(=O)OC(C)=O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `COc1c(I)cc2c(c1I)-` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2685  yield=64.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #19)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1C>>Cc1ccccc1C(CCC(=O)c1ccccc1)OC(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (33.7%) | `reticulated_vitreous_carbon` (30.2%) | `graphite_plate` (8.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (74.2%) | `nickel` (23.8%) | `carbon` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (92.7%) | `nickel_plate` (2.2%) | `platinum_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (91.7%) | `divided` (7.6%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.6%) | `ABSENT` (48.1%) | `Li` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ABSENT` (68.2%) | `BF4` (26.7%) | `PF6` (3.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.1%) | `carboxylic_acid` (7.7%) | `tetraaryl_borate` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.7%) | `Mn_complex` (1.1%) | `organic_neutral_cat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (84.2%) | `halogenated_aliphatic` (9.2%) | `polar_aprotic_nitrile` (4.6%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (99%) | `ClCCl` (0%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2686  yield=64.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #20)

```
C=Cc1ccccn1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccn1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (77.1%) | `carbon_rod` (9.0%) | `carbon_felt` (6.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (60.0%) | `nickel` (36.4%) | `carbon` (2.2%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (91.1%) | `nickel_plate` (4.7%) | `nickel_foam` (2.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `divided` (0.7%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (97.1%) | `NBu4` (2.7%) | `Na` (0.1%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (98.1%) | `BF4` (1.6%) | `PF6` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (17.7%) | `ABSENT` (8.0%) | `water` (2.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.5%) | `ionic_organocat` (2.1%) | `pyridine_organocat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (98.0%) | `polar_aprotic_nitrile` (1.4%) | `halogenated_aliphatic` (0.2%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (98%) | `CC(C)=O` (0%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (42%) | `CCCC[N+](CCCC)(CCC` (2%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[I-].[Li+]` (0%) | set ✓ / any ✓ |

---

### Reaction #2687  yield=65.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #21)

```
C=Cc1ccccc1.O=C(CC(=O)c1ccc(Cl)cc1)c1ccc(Cl)cc1>>O=C(CCC(OC(=O)c1ccc(Cl)cc1)c1ccccc1)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (93.3%) | `carbon_rod` (4.5%) | `carbon_generic` (0.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (70.0%) | `nickel` (23.9%) | `carbon` (5.8%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (94.1%) | `graphite_rod` (3.8%) | `platinum_generic` (0.6%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (68.1%) | `NBu4` (31.7%) | `Li` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (91.0%) | `BF4` (6.8%) | `PF6` (1.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.0%) | `n_halo_imide` (4.9%) | `alkali_other_salt` (3.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `pyridine_organocat` (0.2%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (69.2%) | `ABSENT` (28.8%) | `halogenated_aliphatic` (1.0%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (6%) | `C[N+](=O)[O-]` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (9%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `c1ccncc1` (47%) | `__OTHER__` (9%) | set ✓ / any ✓ |

---

### Reaction #2688  yield=62.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #22)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc([Si](C)(C)C)cc1>>C[Si](C)(C)c1ccc(C(CCC(=O)c2ccccc2)OC(=O)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (86.7%) | `carbon_cloth` (8.2%) | `graphite_rod` (2.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (67.7%) | `nickel` (21.4%) | `carbon` (10.3%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (98.5%) | `nickel_plate` (1.0%) | `platinum_generic` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.8%) | `ABSENT` (0.2%) | `Li` (0.0%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (60.4%) | `PF6` (35.8%) | `ABSENT` (1.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.8%) | `n_halo_imide` (4.9%) | `carboxylic_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (93.6%) | `polar_aprotic_nitrile` (5.6%) | `ketone` (0.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (98%) | `CC(C)=O` (1%) | `FC(F)(F)c1ccccc1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `O=S([O-])O.[Na+]` (0%) | `O=C1CCC(=O)N1Br` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2689  yield=61.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #23)

```
C=Cc1cccc(C)c1.O=C(CC(=O)c1ccccc1)c1ccccc1>>Cc1cccc(C(CCC(=O)c2ccccc2)OC(=O)c2ccccc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (82.8%) | `graphite_rod` (8.0%) | `graphite_generic` (3.2%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (90.7%) | `nickel` (4.9%) | `carbon` (3.7%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (99.4%) | `platinum_generic` (0.3%) | `nickel_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (97.7%) | `ABSENT` (2.1%) | `Li` (0.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (52.0%) | `OTf` (20.2%) | `ABSENT` (13.9%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `inorganic_simple` (3.5%) | `as_solvent_cyclic_ether` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Co_complex` (0.0%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (98.5%) | `polar_aprotic_nitrile` (1.2%) | `halogenated_aliphatic` (0.2%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (96%) | `FC(F)(F)c1ccccc1` (14%) | `CCOCC` (10%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (1%) | `O=O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2690  yield=63.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #24)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=C(CCC)c1ccccc1>>CCCC(CCC(=O)c1ccccc1)(OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (48.3%) | `graphite_generic` (28.8%) | `reticulated_vitreous_carbon` (10.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (73.8%) | `stainless_steel` (14.8%) | `carbon` (5.6%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (43.7%) | `platinum_generic` (39.1%) | `stainless_steel_generic` (10.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (60.5%) | `ABSENT` (39.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (83.0%) | `NEt4` (5.2%) | `Li` (4.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (57.6%) | `PF6` (18.0%) | `Br` (5.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (6.1%) | `n_halo_imide` (4.1%) | `amide` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `organic_neutral_cat` (0.1%) | `tempo_mediator` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.2%) | `polar_protic_alcohol` (1.6%) | `halogenated_aliphatic` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (32%) | `CCO` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (90%) | `CC(=O)O` (2%) | `CC1(C)CCCC(C)(C)N1` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `Brc1ccc(N(c2ccc(Br` (0%) | `CC1(C)CCCC(C)(C)N1` (0%) | set ✓ / any ✓ |

---

### Reaction #2691  yield=69.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #25)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=C(c1ccccc1)C1CCCC1>>O=C(CCC(OC(=O)c1ccccc1)(c1ccccc1)C1CCCC1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (57.4%) | `carbon_cloth` (19.6%) | `carbon_felt` (9.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `stainless_steel` (86.7%) | `platinum` (6.2%) | `nickel` (3.6%) | ✗ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (45.2%) | `stainless_steel_generic` (42.6%) | `nickel_foam` (3.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (95.6%) | `divided` (4.3%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (66.2%) | `ABSENT` (24.0%) | `Li` (5.7%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (33.3%) | `BF4` (26.7%) | `molecular_no_ion` (16.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (6.3%) | `bromide_anion` (3.2%) | `inorganic_simple` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `pyridine_organocat` (0.4%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (81.2%) | `polar_protic_alcohol` (10.9%) | `ABSENT` (4.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (96%) | `ClCCl` (2%) | `FC(F)(F)c1ccccc1` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `[Br-].[H+]` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2692  yield=70.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #7)

```
C=Cc1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2693  yield=71.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #27)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1scnc1C>>Cc1ncsc1C(CCC(=O)c1ccccc1)OC(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (40.7%) | `carbon_rod` (33.4%) | `graphite_plate` (10.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (51.6%) | `carbon` (40.9%) | `nickel` (7.3%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (96.8%) | `graphite_rod` (1.0%) | `platinum_generic` (0.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.1%) | `Li` (3.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (31.6%) | `ClO4` (28.5%) | `PF6` (24.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (20.0%) | `n_halo_imide` (3.1%) | `amide` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `organic_neutral_cat` (0.6%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (87.4%) | `ABSENT` (10.4%) | `ketone` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (68%) | `ClCCl` (5%) | `O` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C` (0%) | `O=C1CCC(=O)N1Br` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2694  yield=76.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #28)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(C)cc1>>Cc1ccc(C(CCC(=O)c2ccccc2)OC(=O)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (43.4%) | `carbon_rod` (31.3%) | `reticulated_vitreous_carbon` (16.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (80.1%) | `nickel` (10.1%) | `carbon` (9.3%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (97.8%) | `nickel_plate` (0.6%) | `graphite_rod` (0.6%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.1%) | `divided` (0.5%) | `ABSENT` (0.3%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (79.4%) | `NBu4` (19.8%) | `Li` (0.4%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (86.3%) | `BF4` (8.6%) | `carboxylate` (2.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.2%) | `n_halo_imide` (6.9%) | `alkali_other_salt` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `pyridine_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (53.5%) | `ABSENT` (43.3%) | `halogenated_aliphatic` (1.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (98%) | `ClCCl` (10%) | `O` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (97%) | `__OTHER__` (2%) | `O=C1CCC(=O)N1Br` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2695  yield=77.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #16)

```
C=C(C)c1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>CC(CCC(=O)c1ccccc1)(OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (52.8%) | `graphite_rod` (23.3%) | `pencil_graphite` (7.7%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (32.0%) | `stainless_steel` (24.8%) | `platinum` (23.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (39.8%) | `platinum_foil` (16.4%) | `graphite_rod` (7.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (96.5%) | `divided` (3.3%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (41.0%) | `ABSENT` (35.5%) | `NEt4` (15.4%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (37.0%) | `BF4` (32.1%) | `ClO4` (8.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (13.5%) | `ABSENT` (5.0%) | `n_halo_imide` (3.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.8%) | `Mn_complex` (1.2%) | `pyridine_organocat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (91.9%) | `polar_aprotic_amide` (3.4%) | `polar_protic_alcohol` (2.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (91%) | `CCCCn1cc[n+](C)c1.` (7%) | `O` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC[SiH](CC)CC` (67%) | `O=C([O-])[O-].[Cs+` (24%) | `O=C(O)C(F)(F)F` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `CC(C)(C)c1cc(C=N[C` (3%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #2696  yield=74.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_18_4663-4668.json) (反应 idx 在该 JSON 内 = #30)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=C(c1ccccc1)C1CCCCC1>>O=C(CCC(OC(=O)c1ccccc1)(c1ccccc1)C1CCCCC1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (38.1%) | `carbon_felt` (21.5%) | `carbon_rod` (10.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `stainless_steel` (75.9%) | `platinum` (10.3%) | `carbon` (7.5%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (54.2%) | `stainless_steel_generic` (17.9%) | `nickel_foam` (8.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (92.6%) | `divided` (6.9%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (49.6%) | `ABSENT` (29.0%) | `Li` (16.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (45.4%) | `ABSENT` (25.7%) | `BF4` (11.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.0%) | `bromide_anion` (3.3%) | `as_solvent_cyclic_ether` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `pyridine_organocat` (0.3%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (84.2%) | `polar_protic_alcohol` (10.1%) | `ABSENT` (3.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (98%) | `ClCCl` (2%) | `FC(F)(F)c1ccccc1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[H+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2697  yield=20.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=O)CC(=O)c1ccccc1.C=C(c1ccccc1)c1ccccc1>>CC(=O)OC(CCC(=O)c1ccccc1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `ABSENT` (2.2%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (33.7%) | `carbon_rod` (18.8%) | `graphite_plate` (12.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (89.5%) | `platinum` (4.5%) | `ABSENT` (4.4%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `unknown_electrode` (28.3%) | `carbon_felt` (19.8%) | `graphite_rod` (13.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (95.4%) | `ABSENT` (4.1%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (57.8%) | `NBu4` (20.5%) | `ABSENT` (11.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (44.8%) | `ClO4` (36.2%) | `ABSENT` (9.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.4%) | `n_halo_imide` (4.1%) | `polyhalo_radical_transfer` (3.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.1%) | `organic_neutral_cat` (0.4%) | `pyridine_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (80.4%) | `polar_protic_alcohol` (10.4%) | `ABSENT` (3.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `CCO` (1%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `CC(=O)O` (1%) | `C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `CC1(C)CCCC(C)(C)N1` (0%) | set ✓ / any ✓ |

---

### Reaction #2698  yield=32.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccccc1.COC(=O)C(=O)CC(=O)c1ccccc1>>COC(=O)C(=O)OC(CCC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.5%) | `platinum` (4.9%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (38.7%) | `reticulated_vitreous_carbon` (26.1%) | `carbon_generic` (13.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (82.9%) | `nickel` (9.3%) | `carbon` (6.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (61.9%) | `platinum_generic` (24.3%) | `platinum_foil` (3.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (97.9%) | `divided` (1.4%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (83.4%) | `NBu4` (8.3%) | `Li` (3.4%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (79.3%) | `OTf` (6.9%) | `PF6` (3.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.9%) | `carboxylic_acid` (3.5%) | `tertiary_amine` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `ammonium_PTC_organocat` (0.1%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (54.4%) | `ABSENT` (37.3%) | `halogenated_aliphatic` (4.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (72%) | `O` (6%) | `C1COCCO1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `O` (4%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2699  yield=32.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccccc1.COC(=O)C(=O)CC(=O)c1ccccc1>>COC(=O)C(=O)CCC(OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (89.3%) | `platinum` (10.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (70.4%) | `carbon_rod` (11.2%) | `carbon_generic` (8.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (94.8%) | `carbon` (2.8%) | `nickel` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (57.3%) | `platinum_plate` (37.7%) | `platinum_wire` (1.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.6%) | `divided` (3.0%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (55.7%) | `NBu4` (40.4%) | `Li` (2.7%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (66.5%) | `BF4` (15.0%) | `PF6` (6.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.5%) | `carboxylic_acid` (5.0%) | `tertiary_amine` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `brønsted_acid_cat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (82.8%) | `polar_aprotic_nitrile` (11.5%) | `ketone` (2.6%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (98%) | `CC(C)=O` (2%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (2%) | `O=C([O-])[O-].[K+]` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2700  yield=50.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #3)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(OCCCc2ccccc2)cc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccc(OCCCc2ccccc2)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (43.6%) | `graphite_rod` (24.7%) | `carbon_cloth` (11.0%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (67.8%) | `nickel` (28.6%) | `carbon` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (96.0%) | `platinum_generic` (2.0%) | `nickel_foam` (1.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `divided` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (87.6%) | `ABSENT` (11.7%) | `Li` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (61.1%) | `ABSENT` (27.5%) | `carboxylate` (3.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.6%) | `n_halo_imide` (2.8%) | `inorganic_simple` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `ionic_organocat` (0.2%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (62.4%) | `polar_aprotic_nitrile` (26.5%) | `halogenated_aliphatic` (5.2%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (64%) | `ClCCl` (15%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O=C1CCC(=O)N1Br` (2%) | `O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2701  yield=65.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #4)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1cccc(OC(F)(F)F)c1>>O=C(CCC(OC(=O)c1ccccc1)c1cccc(OC(F)(F)F)c1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (77.2%) | `reticulated_vitreous_carbon` (9.5%) | `graphite_rod` (9.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.6%) | `nickel` (1.0%) | `carbon` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (99.2%) | `platinum_generic` (0.8%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (73.4%) | `ABSENT` (16.3%) | `NEt4` (8.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (34.4%) | `BF4` (34.0%) | `PF6` (10.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.5%) | `o2_oxidant` (3.2%) | `metal_oxide_oxidant` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (79.2%) | `polar_aprotic_nitrile` (20.3%) | `halogenated_aliphatic` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `FC(F)(F)c1ccccc1` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2702  yield=68.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #5)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccccc1F>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1F)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (38.4%) | `carbon_rod` (37.8%) | `carbon_cloth` (11.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (91.4%) | `nickel` (3.9%) | `carbon` (3.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (97.9%) | `platinum_generic` (1.7%) | `nickel_plate` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (98.8%) | `ABSENT` (0.8%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (74.5%) | `PF6` (19.0%) | `ABSENT` (3.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.5%) | `carboxylic_acid` (2.2%) | `electrophilic_N_F` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `Mn_complex` (0.2%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (38.5%) | `ABSENT` (37.1%) | `halogenated_aliphatic` (22.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (49%) | `FC(F)(F)c1ccccc1` (13%) | `ClCCl` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2703  yield=70.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #6)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc(C(CCC(=O)c2ccccc2)OC(=O)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (26.5%) | `carbon_rod` (26.4%) | `carbon_felt` (18.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (83.6%) | `nickel` (13.5%) | `carbon` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (97.0%) | `platinum_generic` (1.4%) | `nickel_foam` (0.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.3%) | `ABSENT` (45.5%) | `Li` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (69.2%) | `BF4` (26.1%) | `PF6` (2.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.9%) | `carboxylic_acid` (3.6%) | `n_halo_imide` (3.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `Mn_complex` (1.5%) | `brønsted_acid_cat` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (67.3%) | `polar_aprotic_nitrile` (31.7%) | `ketone` (0.6%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (97%) | `CC#N` (9%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (1%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `Oc1ccccc1C=NCCN=Cc` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2704  yield=80.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #7)

```
C=Cc1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_rod` (53.5%) | `carbon_rod` (36.7%) | `reticulated_vitreous_carbon` (6.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.6%) | `nickel` (22.5%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (98.0%) | `graphite_rod` (0.5%) | `nickel_plate` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (67.4%) | `NBu4` (31.7%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (77.6%) | `BF4` (18.3%) | `PF6` (2.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.4%) | `carboxylic_acid` (5.8%) | `n_halo_imide` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.4%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (58.0%) | `polar_aprotic_nitrile` (36.3%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (91%) | `C[N+](=O)[O-]` (1%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (97%) | `O` (4%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2705  yield=80.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #8)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1cccc(OC)c1OC>>COc1cccc(C(CCC(=O)c2ccccc2)OC(=O)c2ccccc2)c1OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (90.4%) | `graphite_generic` (4.5%) | `carbon_rod` (3.1%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (92.1%) | `nickel` (6.3%) | `carbon` (0.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (80.8%) | `platinum_generic` (15.5%) | `nickel_foam` (1.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `divided` (0.7%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (82.3%) | `ABSENT` (15.5%) | `Li` (1.6%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (65.8%) | `ABSENT` (21.4%) | `carboxylate` (5.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `Mn_complex` (0.3%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (92.2%) | `polar_aprotic_nitrile` (6.4%) | `ketone` (0.6%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (94%) | `CCOCC` (1%) | `ClCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Br-].[Mn+2]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #2706  yield=80.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #9)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=C(Cc1ccccc1)c1ccccc1>>O=C(CCC(Cc1ccccc1)(OC(=O)c1ccccc1)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (89.8%) | `reticulated_vitreous_carbon` (3.3%) | `pencil_graphite` (2.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `stainless_steel` (45.4%) | `platinum` (38.7%) | `nickel` (8.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (88.9%) | `stainless_steel_generic` (4.4%) | `platinum_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (49.2%) | `ABSENT` (16.4%) | `protonated_amine` (11.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (22.1%) | `PF6` (18.1%) | `ABSENT` (13.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (6.6%) | `inorganic_simple` (6.1%) | `carboxylic_acid` (3.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `pyridine_organocat` (0.4%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.6%) | `ABSENT` (0.9%) | `polar_protic_alcohol` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `ClCCl` (3%) | `FC(F)(F)c1ccccc1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Na+]` (1%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #2707  yield=75.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #10)

```
C=Cc1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>[2H]C(CC(OC(=O)c1ccccc1)c1ccccc1)C(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (73.1%) | `carbon_rod` (26.6%) | `iron_plate` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (68.4%) | `nickel` (22.8%) | `carbon` (8.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (81.7%) | `graphite_rod` (16.3%) | `nickel_plate` (1.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (58.3%) | `NBu4` (38.1%) | `Li` (2.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (72.6%) | `BF4` (15.4%) | `OTf` (2.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (16.9%) | `n_halo_imide` (7.4%) | `carboxylic_acid` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `Mn_complex` (0.1%) | `ammonium_PTC_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (94.5%) | `polar_aprotic_nitrile` (4.5%) | `polar_protic_acid` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (84%) | `CC#N` (1%) | `C[N+](=O)[O-]` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[2H]O[2H]` | `__ABSENT__` (99%) | `O` (5%) | `O=O` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `c1ccncc1` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2708  yield=72.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #11)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(CCl)cc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccc(CCl)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (64.6%) | `graphite_felt` (14.4%) | `graphite_generic` (8.5%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (91.6%) | `nickel` (3.6%) | `carbon` (3.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.6%) | `platinum_generic` (0.6%) | `graphite_felt` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (63.6%) | `NBu4` (35.9%) | `Li` (0.4%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (62.2%) | `BF4` (35.0%) | `Cl` (1.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.5%) | `tetraaryl_borate` (2.2%) | `metal_oxide_oxidant` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `Mn_complex` (0.4%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (44.1%) | `polar_aprotic_nitrile` (41.3%) | `ketone` (12.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (88%) | `CC(C)=O` (8%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C1CCC(=O)N1Br` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2709  yield=75.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #12)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(OC)cc1>>COc1ccc(C(CCC(=O)c2ccccc2)OC(=O)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (50.5%) | `carbon_rod` (22.1%) | `carbon_cloth` (14.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (82.1%) | `nickel` (10.1%) | `carbon` (5.4%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_plate` (56.7%) | `platinum_generic` (38.5%) | `nickel_foam` (1.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `divided` (0.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.5%) | `ABSENT` (11.3%) | `Li` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (34.9%) | `carboxylate` (29.7%) | `ABSENT` (18.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.2%) | `carboxylic_acid` (2.5%) | `tertiary_amine` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `ionic_organocat` (0.4%) | `brønsted_acid_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (43.8%) | `ABSENT` (29.0%) | `ketone` (17.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (79%) | `CC(C)=O` (74%) | `ClCCl` (18%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C1CCC(=O)N1Br` (79%) | `C` (67%) | `__ABSENT__` (45%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #2710  yield=77.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #13)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=Cc1ccc(OCc2ccccc2)cc1>>O=C(CCC(OC(=O)c1ccccc1)c1ccc(OCc2ccccc2)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (47.2%) | `carbon_rod` (26.5%) | `pencil_graphite` (9.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (71.6%) | `nickel` (26.2%) | `carbon` (1.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (98.1%) | `nickel_foam` (0.8%) | `nickel_plate` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (79.3%) | `ABSENT` (19.6%) | `Li` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (50.9%) | `BF4` (25.0%) | `PF6` (10.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.2%) | `n_halo_imide` (4.7%) | `carboxylic_acid` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `pyridine_organocat` (0.2%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (75.5%) | `polar_aprotic_nitrile` (23.3%) | `halogenated_aliphatic` (0.7%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (97%) | `ClCCl` (3%) | `CCOCC` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2711  yield=75.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #14)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=C(CC)c1ccccc1>>CCC(CCC(=O)c1ccccc1)(OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (40.3%) | `graphite_rod` (21.8%) | `reticulated_vitreous_carbon` (15.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (56.2%) | `platinum` (26.4%) | `stainless_steel` (16.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (29.1%) | `platinum_plate` (26.9%) | `nickel_foam` (17.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (81.0%) | `ABSENT` (18.8%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (98.8%) | `NEt4` (0.5%) | `Li` (0.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (64.7%) | `carboxylate` (21.1%) | `ClO4` (7.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.2%) | `amide` (3.0%) | `n_halo_imide` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `Mn_complex` (0.3%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.4%) | `polar_protic_alcohol` (3.3%) | `halogenated_aliphatic` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (4%) | `FC(F)(F)c1ccccc1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `CC(=O)O` (0%) | `C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #2712  yield=75.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #15)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=C(C)c1ccc2ccccc2c1>>CC(CCC(=O)c1ccccc1)(OC(=O)c1ccccc1)c1ccc2ccccc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `pencil_graphite` (31.9%) | `carbon_cloth` (23.6%) | `graphite_rod` (21.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (41.8%) | `platinum` (36.1%) | `nickel` (16.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (40.9%) | `graphite_rod` (19.1%) | `nickel_foam` (10.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (94.0%) | `ABSENT` (4.4%) | `divided` (1.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (80.9%) | `NBu4` (18.2%) | `NEt4` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (86.4%) | `BF4` (8.8%) | `PF6` (1.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.3%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.3%) | `pyridine_organocat` (1.3%) | `Co_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.1%) | `ABSENT` (6.0%) | `polar_aprotic_amide` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `ClCCl` (0%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CCN(CC)CC.F.F.F` (0%) | `CCN(C(C)C)C(C)C` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2713  yield=82.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #16)

```
C=C(C)c1ccccc1.O=C(CC(=O)c1ccccc1)c1ccccc1>>CC(CCC(=O)c1ccccc1)(OC(=O)c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (52.8%) | `graphite_rod` (23.3%) | `pencil_graphite` (7.7%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (32.0%) | `stainless_steel` (24.8%) | `platinum` (23.9%) | ✗ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (39.8%) | `platinum_foil` (16.4%) | `graphite_rod` (7.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (96.5%) | `divided` (3.3%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (41.0%) | `ABSENT` (35.5%) | `NEt4` (15.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (37.0%) | `BF4` (32.1%) | `ClO4` (8.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (13.5%) | `ABSENT` (5.0%) | `n_halo_imide` (3.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.8%) | `Mn_complex` (1.2%) | `pyridine_organocat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (91.9%) | `polar_aprotic_amide` (3.4%) | `polar_protic_alcohol` (2.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (91%) | `CCCCn1cc[n+](C)c1.` (7%) | `O` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC[SiH](CC)CC` (67%) | `O=C([O-])[O-].[Cs+` (24%) | `O=C(O)C(F)(F)F` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `CC(C)(C)c1cc(C=N[C` (3%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #2714  yield=82.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_26_6913-6918.json) (反应 idx 在该 JSON 内 = #17)

```
O=C(CC(=O)c1ccccc1)c1ccccc1.C=C(c1ccc(C)cc1)c1ccc(C)cc1>>Cc1ccc(C(CCC(=O)c2ccccc2)(OC(=O)c2ccccc2)c2ccc(C)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_zinc` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (90.2%) | `carbon_felt` (9.2%) | `pencil_graphite` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (85.7%) | `nickel` (7.2%) | `platinum` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `graphite_rod` (53.1%) | `carbon_felt` (39.4%) | `nickel_foam` (2.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (79.1%) | `divided` (17.5%) | `ABSENT` (3.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (52.4%) | `ABSENT` (34.1%) | `Li` (12.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `ABSENT` (38.4%) | `BF4` (37.7%) | `ClO4` (9.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `n_halo_imide` (14.7%) | `ABSENT` (10.6%) | `as_solvent_nitroalkane` (2.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.8%) | `pyridine_organocat` (2.1%) | `ammonium_PTC_organocat` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (85.3%) | `polar_aprotic_nitrile` (13.9%) | `halogenated_aliphatic` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (99%) | `CC#N` (2%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C` (55%) | `O=C1CCC(=O)N1Br` (30%) | `__ABSENT__` (24%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Br-].[Mn+2]` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✓ / any ✓ |

---

### Reaction #2715  yield=13.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(C)cc1.C=Cc1ccc(OC)cc1>>COc1ccc(C2CCC(c3ccc(C)cc3)=N2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.5%) | `platinum` (2.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (31.7%) | `carbon_felt` (26.9%) | `carbon_generic` (14.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (72.3%) | `carbon` (15.2%) | `nickel` (11.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (63.0%) | `platinum_generic` (8.1%) | `nickel_plate` (8.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (91.3%) | `divided` (4.4%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.2%) | `Li` (23.1%) | `Na` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (42.7%) | `molecular_no_ion` (24.9%) | `BF4` (21.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (12.9%) | `primary_amine` (2.2%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.3%) | `Co_complex` (0.7%) | `Mn_complex` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (82.2%) | `cyclic_ether` (7.5%) | `halogenated_aliphatic` (3.0%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (88%) | `CCOCC` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (98%) | `CC(=O)O` (1%) | `N=C(c1ccccc1)c1ccc` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `[Fe+2].c1cc[cH-]c1` (5%) | `[Pt]` (2%) | set ✓ / any ✓ |

---

### Reaction #2716  yield=39.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(C(F)(F)F)cc1>>FC(F)(F)c1ccc(C2=NC(c3ccc(C(F)(F)F)cc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (2.2%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (40.1%) | `carbon_rod` (30.8%) | `graphite_generic` (11.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (40.0%) | `carbon` (39.6%) | `nickel` (10.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `carbon_felt` (18.5%) | `platinum_plate` (16.6%) | `platinum_generic` (15.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.9%) | `divided` (1.4%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.4%) | `Li` (7.8%) | `NEt4` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (47.2%) | `ClO4` (35.3%) | `carboxylate` (5.4%) | ✓ |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (8.2%) | `silane_other` (5.2%) | `carboxylic_acid` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (75.9%) | `Mn_complex` (12.7%) | `Co_complex` (8.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (65.8%) | `halogenated_aliphatic` (11.3%) | `polar_aprotic_amide` (8.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` | `CC#N` (92%) | `ClCCl` (56%) | `CCOCC` (17%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `__OTHER__` (90%) | `OB(O)B(O)O` (85%) | `CC[Si](CC)CC` (71%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` | `__ABSENT__` (66%) | `c1ccncc1` (6%) | `[Cl-].[Cl-].[Mn+2]` (4%) | set ✗ / any ✓ |

---

### Reaction #2717  yield=47.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C)cc1.C=Cc1ccc(OC)cc1>>Cc1ccc(C2=NC(c3ccc(C)cc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.7%) | `platinum` (14.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (53.3%) | `reticulated_vitreous_carbon` (20.4%) | `platinum_plate` (9.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (47.0%) | `platinum` (42.9%) | `nickel` (7.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `carbon_generic` (25.5%) | `platinum_foil` (15.8%) | `platinum_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (62.3%) | `undivided` (34.5%) | `divided` (3.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (75.4%) | `Li` (14.5%) | `K` (7.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `carboxylate` (48.8%) | `BF4` (19.5%) | `ClO4` (16.1%) | ✓ |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (7.0%) | `carboxylic_acid` (4.5%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.0%) | `Co_complex` (3.4%) | `Mn_complex` (3.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (61.6%) | `polar_protic_alcohol` (16.7%) | `halogenated_aliphatic` (7.5%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (97%) | `ClCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (82%) | `__OTHER__` (18%) | `O=O` (17%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (83%) | `[Pt]` (11%) | `[Fe+2].c1cc[cH-]c1` (4%) | set ✓ / any ✓ |

---

### Reaction #2718  yield=59.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1ccc(C)cc1.C=Cc1ccc(OC)cc1>>COc1ccc(C2=NC(c3ccc(OC)cc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.7%) | `platinum` (2.8%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (40.8%) | `carbon_generic` (18.8%) | `carbon_felt` (18.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (64.1%) | `nickel` (23.9%) | `carbon` (11.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (25.5%) | `nickel_plate` (22.5%) | `nickel_generic` (13.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (86.9%) | `ABSENT` (12.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.9%) | `Li` (7.5%) | `Na` (1.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (38.6%) | `ClO4` (38.6%) | `molecular_no_ion` (9.0%) | ✓ |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (13.8%) | `primary_amine` (2.1%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.2%) | `Mn_complex` (4.7%) | `Co_complex` (2.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (78.9%) | `cyclic_ether` (10.0%) | `halogenated_aliphatic` (3.0%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (52%) | `ClCCl` (4%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (99%) | `O=S(=O)([O-])C(F)(` (0%) | `C1CN=C2NCCCN2C1` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (92%) | `[Fe+2].c1cc[cH-]c1` (5%) | `CC(=O)NC1CC2(CCCCC` (2%) | set ✓ / any ✓ |

---

### Reaction #2719  yield=54.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #4)

```
CC#N.C=Cc1ccccc1>>Cc1nnnn1C(CN=[N+]=[N-])c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.4%) | `platinum` (1.7%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_plate` (99.9%) | `reticulated_vitreous_carbon` (0.1%) | `graphite_rod` (0.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `carbon` (0.3%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (92.9%) | `ABSENT` (7.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (74.6%) | `ABSENT` (23.8%) | `Li` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (44.4%) | `ABSENT` (35.7%) | `BF4` (7.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `azide_source` (88.2%) | `ketone` (0.7%) | `hypervalent_iodine` (0.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Cu_complex` (0.1%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `hfip` | `ABSENT` (88.0%) | `polar_protic_acid` (8.0%) | `polar_aprotic_nitrile` (2.3%) | ✗ |
| 溶剂 set | 79 | `OC(C(F)(F)F)C(F)(F` | `C[N+](=O)[O-]` (94%) | `C1COCCO1` (52%) | `CC#N` (18%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (96%) | `O=O` (95%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (98%) | `c1ccncc1` (90%) | `__ABSENT__` (1%) | set ✗ / any ✓ |

---

### Reaction #2720  yield=57.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #5)

```
C=Cc1ccc(OC(C)=O)cc1>>CC(=O)Oc1ccc(C2=NC(c3ccc(O)cc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_zinc` (0.1%) | `sacrificial_aluminum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (32.0%) | `carbon_rod` (30.2%) | `carbon_felt` (16.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (60.4%) | `carbon` (18.5%) | `nickel` (17.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (43.6%) | `zinc_plate` (10.9%) | `stainless_steel_generic` (8.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (83.6%) | `Li` (9.6%) | `ABSENT` (2.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (35.3%) | `molecular_no_ion` (28.5%) | `Br` (15.6%) | ✗ |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (9.8%) | `primary_amine` (2.5%) | `hydrosilane` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.2%) | `Mn_complex` (1.3%) | `Co_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (42.4%) | `polar_aprotic_nitrile` (20.5%) | `polar_aprotic_amide` (18.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `FC(F)(F)c1ccccc1` (92%) | `CCOCC` (82%) | `ClCCl` (15%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `__ABSENT__` (99%) | `OB(O)B(O)O` (25%) | `__OTHER__` (11%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Cl][Mn][Cl]` (0%) | `[Br][Mn][Br]` (0%) | set ✓ / any ✓ |

---

### Reaction #2721  yield=54.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #6)

```
C=Cc1c(C)cc(C)cc1C>>Cc1cc(C)c(C2=NC(c3c(C)cc(C)cc3C)CC2)c(C)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.0%) | `ABSENT` (1.1%) | `platinum` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (45.2%) | `graphite_rod` (13.8%) | `graphite_generic` (8.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (42.0%) | `carbon` (27.6%) | `nickel` (20.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_plate` (50.1%) | `carbon_felt` (15.8%) | `platinum_generic` (8.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (66.6%) | `ABSENT` (31.7%) | `divided` (1.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (70.1%) | `NBu4` (26.0%) | `Na` (1.7%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (48.0%) | `ClO4` (44.4%) | `carboxylate` (2.1%) | ✓ |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (20.5%) | `hydrosilane` (2.9%) | `thiol` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (57.4%) | `ABSENT` (36.4%) | `Mn_complex` (4.6%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (97.5%) | `polar_aprotic_amide` (0.5%) | `tfe` (0.5%) | ✗ |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `CC#N` (100%) | `O` (31%) | `ClCCl` (10%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `__ABSENT__` (99%) | `O=S(=O)([O-])C(F)(` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=S(=O)(O)C(F)(F)F` | `__ABSENT__` (10%) | `[Pt]` (9%) | `[Br-].[Br-].[Mn+2]` (7%) | set ✗ / any ✗ |

---

### Reaction #2722  yield=69.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #7)

```
C=Cc1ccccc1Br>>Brc1ccccc1C1=NC(c2ccccc2Br)CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (0.9%) | `sacrificial_zinc` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (43.2%) | `carbon_felt` (23.8%) | `reticulated_vitreous_carbon` (15.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (41.8%) | `platinum` (35.7%) | `nickel` (21.4%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `carbon_felt` (53.3%) | `platinum_plate` (19.5%) | `nickel_foam` (8.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `ABSENT` (0.6%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.1%) | `Li` (2.8%) | `NEt4` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (58.5%) | `PF6` (34.0%) | `BF4` (5.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `carboxylic_acid` (14.1%) | `ABSENT` (7.0%) | `primary_amine` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (75.8%) | `Mn_complex` (11.2%) | `Co_complex` (5.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (82.5%) | `polar_aprotic_amide` (13.6%) | `halogenated_aliphatic` (1.6%) | ✓ |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `CCOCC` (78%) | `CC#N` (60%) | `FC(F)(F)c1ccccc1` (39%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (82%) | `CC[Si](CC)CC` (81%) | `O=O` (76%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `__ABSENT__` (65%) | `[Br][Mn][Br]` (22%) | `c1ccncc1` (5%) | set ✗ / any ✓ |

---

### Reaction #2723  yield=61.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #8)

```
C=Cc1cccc(F)c1>>Fc1cccc(C2=NC(c3cccc(F)c3)CC2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (96.1%) | `ABSENT` (3.2%) | `platinum` (0.3%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `carbon_generic` (80.1%) | `unknown_electrode` (9.4%) | `carbon_felt` (3.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (77.8%) | `nickel` (9.4%) | `ABSENT` (7.8%) | ✗ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_generic` (22.7%) | `ABSENT` (21.8%) | `nickel_generic` (20.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (52.9%) | `ABSENT` (43.8%) | `divided` (3.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (60.5%) | `Li` (38.3%) | `K` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (51.7%) | `PF6` (32.1%) | `BF4` (8.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `carboxylic_acid` (10.9%) | `ABSENT` (2.8%) | `hydrosilane` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (42.9%) | `Mn_complex` (19.7%) | `Co_complex` (8.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (53.3%) | `polar_aprotic_amide` (32.2%) | `halogenated_aliphatic` (5.8%) | ✓ |
| 溶剂 set | 79 | `CC(C)=O` + `O` | `O` (89%) | `CC#N` (73%) | `CN(C)C=O` (20%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Cl-].[Li+]` + `O.O.O.O.O.O.O.O.O.` | `O=C(O)C(F)(F)F` (47%) | `CC(=O)O` (24%) | `CC(C)(C)C(=O)[O-].` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `__ABSENT__` (93%) | `[Pt]` (1%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #2724  yield=63.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #9)

```
C=Cc1cccc(Br)c1>>Brc1cccc(C2=NC(c3cccc(Br)c3)CC2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (94.0%) | `sacrificial_aluminum` (3.2%) | `platinum` (1.3%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `carbon_generic` (67.4%) | `carbon_felt` (21.2%) | `boron_doped_diamond` (2.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `nickel` (47.5%) | `platinum` (31.1%) | `carbon` (14.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_rod` | `nickel_generic` (26.3%) | `nickel_foam` (20.8%) | `zinc_generic` (10.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.7%) | `ABSENT` (13.0%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.0%) | `Li` (27.3%) | `K` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (46.0%) | `PF6` (31.7%) | `molecular_no_ion` (7.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `carboxylic_acid` (9.0%) | `ABSENT` (4.6%) | `silane_other` (4.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (55.3%) | `Mn_complex` (35.1%) | `pyridine_organocat` (3.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (55.1%) | `polar_aprotic_amide` (25.3%) | `halogenated_aliphatic` (12.5%) | ✓ |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `CC#N` (78%) | `O` (47%) | `CCOCC` (35%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `CC[Si](CC)CC` (92%) | `__OTHER__` (80%) | `OB(O)B(O)O` (76%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` | `__ABSENT__` (36%) | `[Br][Mn][Br]` (8%) | `[Pt]` (2%) | set ✗ / any ✗ |

---

### Reaction #2725  yield=69.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #10)

```
C=Cc1ccc(CCl)cc1>>ClCc1ccc(C2=NC(c3ccc(CCl)cc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (45.0%) | `carbon_generic` (30.5%) | `graphite_felt` (10.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.9%) | `carbon` (14.3%) | `nickel` (8.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_wire` (31.0%) | `platinum_plate` (13.6%) | `carbon_felt` (13.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (94.9%) | `ABSENT` (4.0%) | `divided` (1.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (76.9%) | `Li` (20.2%) | `ABSENT` (2.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (74.5%) | `ClO4` (8.0%) | `carboxylate` (4.8%) | ✓ |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (14.9%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (68.8%) | `Mn_complex` (20.1%) | `organic_neutral_cat` (3.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (76.5%) | `halogenated_aliphatic` (7.1%) | `polar_aprotic_sulfoxide` (5.1%) | ✓ |
| 溶剂 set | 79 | `CC(C)=O` + `O` | `O` (92%) | `CC#N` (82%) | `CC(C)=O` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O.O.O.O.O.O.O.O.O.` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Cl][Mn][Cl]` | `__ABSENT__` (98%) | `[Cl][Mn][Cl]` (0%) | `[O]=[Fe][O][Fe]=[O` (0%) | set ✗ / any ✓ |

---

### Reaction #2726  yield=65.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #11)

```
C=Cc1cc(C)ccc1C>>Cc1ccc(C)c(C2=NC(c3cc(C)ccc3C)CC2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (57.9%) | `carbon` (41.3%) | `sacrificial_zinc` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (53.8%) | `platinum_plate` (27.6%) | `platinum_generic` (10.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (63.8%) | `nickel` (28.2%) | `carbon` (4.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_plate` (51.3%) | `platinum_plate` (29.0%) | `platinum_generic` (6.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (76.5%) | `divided` (23.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.0%) | `Li` (6.6%) | `Na` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `carboxylate` (29.8%) | `PF6` (26.3%) | `molecular_no_ion` (20.9%) | ✗ |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (12.6%) | `carboxylic_acid` (8.0%) | `hydrosilane` (4.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.3%) | `Co_complex` (4.5%) | `organic_neutral_cat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (67.2%) | `halogenated_aliphatic` (11.7%) | `polar_protic_alcohol` (8.4%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (50%) | `OC(C(F)(F)F)C(F)(F` (34%) | `FC(F)(F)c1ccccc1` (14%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (100%) | `CC(=O)O` (7%) | `OB(O)B(O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (100%) | `[Br][Mn][Br]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2727  yield=68.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #12)

```
C=Cc1ccccc1F>>Fc1ccccc1C1=NC(c2ccccc2F)CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (78.8%) | `reticulated_vitreous_carbon` (12.6%) | `carbon_felt` (3.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.8%) | `carbon` (1.0%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (90.5%) | `platinum_generic` (9.0%) | `carbon_felt` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.6%) | `Li` (6.0%) | `NEt4` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (82.9%) | `BF4` (11.1%) | `PF6` (5.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `carboxylic_acid` (14.0%) | `ABSENT` (13.6%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.4%) | `Mn_complex` (4.6%) | `organic_neutral_cat` (3.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (96.8%) | `halogenated_aliphatic` (2.2%) | `polar_aprotic_amide` (0.4%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (2%) | `CCOCC` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `O=C(O)C(F)(F)F` (53%) | `__ABSENT__` (11%) | `CC(=O)O` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Br][Mn][Br]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #2728  yield=64.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #13)

```
C=Cc1cccc(Cl)c1>>Clc1cccc(C2=NC(c3cccc(Cl)c3)CC2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (91.9%) | `ABSENT` (4.2%) | `platinum` (3.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `unknown_electrode` (42.0%) | `carbon_generic` (40.3%) | `carbon_rod` (5.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.6%) | `ABSENT` (5.7%) | `nickel` (5.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (37.1%) | `platinum_plate` (21.9%) | `platinum_wire` (8.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (88.4%) | `ABSENT` (11.4%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (74.1%) | `Li` (23.1%) | `ABSENT` (2.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (33.8%) | `ClO4` (27.6%) | `PF6` (14.7%) | ✓ |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (7.4%) | `carboxylic_acid` (5.7%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (66.0%) | `Mn_complex` (15.3%) | `Co_complex` (8.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.9%) | `polar_aprotic_amide` (14.1%) | `halogenated_aliphatic` (8.2%) | ✓ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (50%) | `ClCCl` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O` | `__ABSENT__` (98%) | `CC(=O)O` (1%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `__ABSENT__` (97%) | `__OTHER__` (1%) | `[Pt]` (0%) | set ✗ / any ✓ |

---

### Reaction #2729  yield=70.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #14)

```
C=Cc1ccc(C)cc1C>>Cc1ccc(C2=NC(c3ccc(C)cc3C)CC2)c(C)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.5%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (86.1%) | `carbon_rod` (9.0%) | `graphite_rod` (3.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (64.4%) | `carbon` (34.9%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (52.7%) | `carbon_felt` (24.4%) | `platinum_wire` (8.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (92.0%) | `divided` (8.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (67.2%) | `NBu4` (32.2%) | `ABSENT` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (41.4%) | `BF4` (33.6%) | `molecular_no_ion` (21.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (11.6%) | `carboxylic_acid` (8.6%) | `silane_other` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `Mn_complex` (0.8%) | `Co_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (92.8%) | `ABSENT` (3.6%) | `polar_aprotic_amide` (3.2%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `ClCCl` (9%) | `CCOCC` (6%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (100%) | `__OTHER__` (2%) | `CC(=O)O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (100%) | `[Br][Mn][Br]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #2730  yield=70.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #15)

```
C=Cc1ccc(F)cc1>>Fc1ccc(C2=NC(c3ccc(F)cc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.4%) | `platinum` (1.1%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (49.3%) | `carbon_felt` (17.5%) | `graphite_generic` (8.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (40.5%) | `nickel` (29.1%) | `platinum` (23.9%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `carbon_felt` (15.5%) | `nickel_plate` (13.6%) | `graphite_generic` (13.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (94.6%) | `ABSENT` (5.0%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.4%) | `Li` (11.4%) | `K` (2.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (26.4%) | `BF4` (18.8%) | `molecular_no_ion` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (9.1%) | `carboxylic_acid` (4.2%) | `primary_amine` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (78.0%) | `Mn_complex` (17.3%) | `Co_complex` (2.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (32.3%) | `polar_aprotic_nitrile` (26.8%) | `ABSENT` (14.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (39%) | `CC#N` (35%) | `ClCCl` (30%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (84%) | `CC[Si](CC)CC` (69%) | `O=O` (61%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Mn+2]` | `[Cl-].[Cl-].[Mn+2]` (61%) | `__ABSENT__` (34%) | `[Pt]` (2%) | set ✓ / any ✓ |

---

### Reaction #2731  yield=71.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #16)

```
C=Cc1ccccc1Cl>>Clc1ccccc1C1=NC(c2ccccc2Cl)CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.0%) | `platinum` (4.4%) | `sacrificial_zinc` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (49.9%) | `carbon_felt` (38.3%) | `platinum_generic` (2.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (45.8%) | `nickel` (43.8%) | `carbon` (10.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_plate` (47.5%) | `carbon_felt` (34.9%) | `nickel_foam` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (95.3%) | `divided` (4.2%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.1%) | `Li` (1.7%) | `H` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `PF6` (61.1%) | `ClO4` (24.1%) | `BF4` (7.7%) | ✓ |
| 试剂大类 | 103 | `azide_source` | `carboxylic_acid` (15.8%) | `ABSENT` (10.9%) | `thiol` (3.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.9%) | `organic_neutral_cat` (3.6%) | `pyridine_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (77.3%) | `ABSENT` (8.5%) | `halogenated_aliphatic` (8.0%) | ✓ |
| 溶剂 set | 79 | `CC(=O)O` + `OC(C(F)(F)F)C(F)(F` + `ClCCl` | `CC#N` (75%) | `OC(C(F)(F)F)C(F)(F` (21%) | `ClCCl` (21%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `O=S(=O)(O)C(F)(F)F` + `CC(=O)OC(C)=O` + `CN(C)c1ccncc1` | `CC(=O)OC(C)=O` (28%) | `O=C(O)C(F)(F)F` (26%) | `CN(C)c1ccncc1` (23%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `COc1c(I)cc2c(c1I)-` | `__ABSENT__` (93%) | `COc1c(I)cc2c(c1I)-` (3%) | `[Br][Mn][Br]` (0%) | set ✗ / any ✓ |

---

### Reaction #2732  yield=79.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #17)

```
C=Cc1ccc(OCC)cc1>>CCOc1ccc(C2=NC(c3ccc(OCC)cc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.9%) | `sacrificial_zinc` (0.8%) | `sacrificial_aluminum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (59.0%) | `reticulated_vitreous_carbon` (9.0%) | `graphite_rod` (7.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (54.2%) | `carbon` (35.8%) | `platinum` (8.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (44.7%) | `carbon_felt` (21.9%) | `platinum_wire` (10.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.0%) | `ABSENT` (2.0%) | `divided` (2.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (60.2%) | `NBu4` (37.8%) | `Na` (0.8%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (52.2%) | `ClO4` (34.5%) | `BF4` (9.5%) | ✓ |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (6.9%) | `carboxylic_acid` (6.6%) | `primary_amine` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.7%) | `Mn_complex` (5.5%) | `Co_complex` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (49.0%) | `ABSENT` (39.0%) | `polar_aprotic_amide` (3.8%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `O` | `CC#N` (80%) | `CCOCC` (48%) | `FC(F)(F)c1ccccc1` (18%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (98%) | `OB(O)B(O)O` (9%) | `CC(=O)O` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (97%) | `[Br][Mn][Br]` (1%) | `[Pt]` (1%) | set ✗ / any ✓ |

---

### Reaction #2733  yield=76.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccccc1OC>>COc1ccccc1C1=NC(c2ccccc2OC)CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.8%) | `platinum` (4.1%) | `sacrificial_zinc` (1.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (87.5%) | `carbon_felt` (9.6%) | `platinum_plate` (1.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (76.8%) | `platinum` (11.7%) | `carbon` (9.7%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_plate` (62.5%) | `carbon_felt` (22.9%) | `nickel_foam` (7.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.7%) | `ABSENT` (1.0%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (60.8%) | `Li` (38.7%) | `K` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (84.7%) | `BF4` (7.7%) | `carboxylate` (3.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (17.0%) | `primary_amine` (2.3%) | `thiol` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.3%) | `Mn_complex` (0.7%) | `pyridine_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (94.5%) | `polar_aprotic_amide` (3.4%) | `ABSENT` (1.0%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (1%) | `CCOCC` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=CO` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br][Mn][Br]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #2734  yield=75.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #19)

```
C=Cc1ccc(Br)cc1>>Brc1ccc(C2=NC(c3ccc(Br)cc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.3%) | `platinum` (5.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (36.9%) | `boron_doped_diamond` (15.7%) | `carbon_felt` (15.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (43.0%) | `carbon` (32.9%) | `nickel` (20.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_wire` (34.4%) | `carbon_felt` (12.8%) | `graphite_rod` (10.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `ABSENT` (0.6%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.3%) | `Li` (4.2%) | `Na` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (26.6%) | `Br` (25.4%) | `ClO4` (24.5%) | ✓ |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (9.8%) | `carboxylic_acid` (6.9%) | `primary_amine` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.8%) | `Mn_complex` (4.9%) | `Co_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.9%) | `halogenated_aliphatic` (15.2%) | `polar_aprotic_amide` (4.7%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (98%) | `O` (74%) | `ClCCl` (12%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `__ABSENT__` (77%) | `OB(O)B(O)O` (46%) | `__OTHER__` (36%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (73%) | `[Pt]` (13%) | `[Br][Mn][Br]` (6%) | set ✗ / any ✓ |

---

### Reaction #2735  yield=78.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #20)

```
C=Cc1ccc(OC(C)(C)C)cc1>>CC(C)(C)Oc1ccc(C2=NC(c3ccc(OC(C)(C)C)cc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.1%) | `platinum` (2.0%) | `sacrificial_zinc` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (58.0%) | `carbon_felt` (17.7%) | `graphite_generic` (6.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (49.3%) | `platinum` (31.2%) | `carbon` (17.0%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (50.6%) | `carbon_felt` (14.5%) | `platinum_wire` (12.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.3%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.1%) | `Li` (32.9%) | `Na` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (68.9%) | `BF4` (13.6%) | `molecular_no_ion` (7.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (8.0%) | `silane_other` (4.6%) | `primary_amine` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (80.7%) | `Mn_complex` (14.5%) | `Co_complex` (3.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (54.2%) | `polar_aprotic_amide` (23.8%) | `cyclic_ether` (8.1%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (91%) | `O` (37%) | `CCOCC` (12%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (85%) | `OB(O)B(O)O` (63%) | `__OTHER__` (41%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (88%) | `[Br][Mn][Br]` (4%) | `[Fe+2].c1cc[cH-]c1` (2%) | set ✗ / any ✗ |

---

### Reaction #2736  yield=72.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #21)

```
C=Cc1ccc(CC)cc1>>CCc1ccc(C2=NC(c3ccc(CC)cc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (77.5%) | `ABSENT` (11.9%) | `sacrificial_zinc` (4.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (40.2%) | `ABSENT` (13.4%) | `zinc_generic` (7.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (46.4%) | `carbon` (24.2%) | `platinum` (15.9%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `carbon_felt` (38.9%) | `platinum_wire` (12.2%) | `nickel_plate` (10.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (88.2%) | `divided` (9.1%) | `ABSENT` (2.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.4%) | `Li` (17.5%) | `K` (3.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (60.1%) | `BF4` (23.3%) | `Br` (4.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `carboxylic_acid` (10.4%) | `ABSENT` (9.9%) | `silane_other` (5.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (52.0%) | `Co_complex` (23.9%) | `Mn_complex` (21.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (78.0%) | `polar_aprotic_sulfoxide` (8.3%) | `polar_aprotic_amide` (5.1%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (96%) | `CCOCC` (20%) | `O` (16%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `CC(=O)O` (73%) | `CC[Si](CC)CC` (47%) | `O=C(O)C(F)(F)F` (21%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (87%) | `[Br][Mn][Br]` (4%) | `[Fe+2].c1cc[cH-]c1` (2%) | set ✗ / any ✗ |

---

### Reaction #2737  yield=77.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #22)

```
C=Cc1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc(C2=NC(c3ccc(C(C)(C)C)cc3)CC2)cc1.C[Si](C)(C)N=[N+]=[N-]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.7%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `reticulated_vitreous_carbon` (51.0%) | `carbon_felt` (17.7%) | `graphite_generic` (16.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.4%) | `nickel` (5.1%) | `ABSENT` (4.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (83.0%) | `platinum_foil` (11.4%) | `platinum_plate` (2.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (87.8%) | `ABSENT` (11.9%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (83.8%) | `Li` (13.9%) | `Na` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (55.5%) | `BF4` (33.2%) | `carboxylate` (3.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (26.1%) | `ABSENT` (6.0%) | `silane_other` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (63.4%) | `Mn_complex` (30.6%) | `brønsted_acid_cat` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (70.3%) | `ABSENT` (12.4%) | `polar_aprotic_amide` (5.1%) | ✗ |
| 溶剂 set | 79 | `C1CCOC1` + `CC#N` | `CC#N` (100%) | `C1CCOC1` (19%) | `O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `CC[Si](CC)CC` (84%) | `__OTHER__` (72%) | `OB(O)B(O)O` (72%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `Oc1ccccc1C=NCCN=Cc` + `O=S(=O)([O-])C(F)(` | `Oc1ccccc1C=NCCN=Cc` (92%) | `O=S(=O)([O-])C(F)(` (65%) | `__ABSENT__` (6%) | set ✓ / any ✓ |

---

### Reaction #2738  yield=72.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #23)

```
C=Cc1ccccc1C>>Cc1ccccc1C1=NC(c2ccccc2C)CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.4%) | `platinum` (1.5%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (88.5%) | `carbon_felt` (10.6%) | `reticulated_vitreous_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (55.0%) | `nickel` (39.3%) | `carbon` (5.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_plate` (42.0%) | `platinum_plate` (25.4%) | `carbon_felt` (11.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (96.7%) | `divided` (3.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (76.0%) | `Li` (12.2%) | `ABSENT` (11.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (32.0%) | `PF6` (21.6%) | `ABSENT` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (12.7%) | `carboxylic_acid` (5.2%) | `thiol` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.4%) | `Mn_complex` (1.9%) | `Co_complex` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (92.7%) | `polar_aprotic_amide` (5.1%) | `polar_protic_alcohol` (0.9%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (1%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br][Mn][Br]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #2739  yield=71.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #24)

```
C=Cc1cccc(C)c1>>Cc1cccc(C2=NC(c3cccc(C)c3)CC2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (33.0%) | `carbon_felt` (15.8%) | `carbon_rod` (10.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.4%) | `ABSENT` (4.6%) | `carbon` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (48.9%) | `platinum_generic` (31.4%) | `ABSENT` (7.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.6%) | `ABSENT` (2.2%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (51.4%) | `NBu4` (47.0%) | `K` (1.2%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (71.1%) | `PF6` (12.5%) | `BF4` (10.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (11.0%) | `carboxylic_acid` (8.3%) | `silane_other` (5.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (39.7%) | `ABSENT` (38.4%) | `Mn_complex` (13.1%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (97.4%) | `polar_aprotic_amide` (1.0%) | `polar_protic_alcohol` (0.4%) | ✗ |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `CC#N` (99%) | `CCOCC` (24%) | `O` (20%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `__ABSENT__` (99%) | `O=O` (8%) | `__OTHER__` (7%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl-].[Cl-].[Co+2]` (6%) | `CC(C)(C)c1cc2c(c(C` (4%) | `[Br][Mn][Br]` (4%) | set ✗ / any ✗ |

---

### Reaction #2740  yield=71.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #25)

```
C=Cc1ccc2c(c1)CC2>>c1cc2c(cc1C1=NC(c3ccc4c(c3)CC4)CC1)CC2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.9%) | `ABSENT` (1.6%) | `sacrificial_aluminum` (1.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (90.6%) | `carbon_felt` (4.1%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (80.6%) | `carbon` (14.2%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (34.4%) | `platinum_wire` (24.9%) | `platinum_plate` (14.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (87.3%) | `ABSENT` (8.9%) | `divided` (3.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (87.1%) | `NBu4` (12.0%) | `K` (0.5%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (78.1%) | `molecular_no_ion` (12.7%) | `PF6` (4.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `carboxylic_acid` (50.9%) | `silane_other` (3.9%) | `ABSENT` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Mn_complex` (42.6%) | `ABSENT` (31.2%) | `brønsted_acid_cat` (12.9%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (44.6%) | `polar_aprotic_amide` (31.5%) | `ABSENT` (13.2%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (94%) | `O` (32%) | `ClCCl` (15%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `O=C(O)C(F)(F)F` (59%) | `O=O` (53%) | `__OTHER__` (53%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br][Mn][Br]` (39%) | `O=S(=O)(O)C(F)(F)F` (6%) | `__OTHER__` (3%) | set ✗ / any ✗ |

---

### Reaction #2741  yield=75.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #26)

```
C=Cc1ccccc1>>c1ccc(C2=NC(c3ccccc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.9%) | `platinum` (5.2%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (38.4%) | `unknown_electrode` (18.4%) | `carbon_generic` (18.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (51.9%) | `carbon` (26.9%) | `nickel` (15.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (27.2%) | `unknown_electrode` (21.8%) | `platinum_plate` (11.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.1%) | `ABSENT` (16.4%) | `divided` (1.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (87.8%) | `Li` (9.1%) | `ABSENT` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (51.2%) | `PF6` (31.5%) | `ClO4` (9.4%) | ✓ |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (7.2%) | `carboxylic_acid` (5.5%) | `alkali_sulfonate` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (44.4%) | `Mn_complex` (35.3%) | `Co_complex` (12.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (29.4%) | `polar_aprotic_amide` (25.5%) | `halogenated_aliphatic` (12.2%) | ✓ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `CC#N` (95%) | `O` (89%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (58%) | `__ABSENT__` (46%) | `O=O` (33%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `__ABSENT__` (30%) | `__OTHER__` (9%) | `[Pt]` (7%) | set ✗ / any ✓ |

---

### Reaction #2742  yield=71.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #27)

```
C=Cc1ccc(Cl)cc1>>Clc1ccc(C2=NC(c3ccc(Cl)cc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.5%) | `sacrificial_aluminum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (66.1%) | `carbon_felt` (24.2%) | `carbon_rod` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (45.6%) | `carbon` (27.2%) | `platinum` (25.1%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_generic` (55.9%) | `platinum_plate` (12.4%) | `nickel_plate` (5.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `divided` (0.5%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (89.4%) | `Li` (9.5%) | `K` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (44.8%) | `ClO4` (33.3%) | `PF6` (11.8%) | ✓ |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (8.7%) | `boron_lewis_acid` (3.8%) | `carboxylic_acid` (3.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (71.9%) | `Mn_complex` (25.4%) | `Co_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (61.0%) | `polar_aprotic_amide` (17.5%) | `halogenated_aliphatic` (7.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (94%) | `O` (76%) | `CCOCC` (5%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `__ABSENT__` (82%) | `OB(O)B(O)O` (38%) | `CC[Si](CC)CC` (16%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `__ABSENT__` (82%) | `c1ccncc1` (10%) | `__OTHER__` (10%) | set ✗ / any ✓ |

---

### Reaction #2743  yield=76.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #28)

```
C=Cc1ccc(C)cc1>>Cc1ccc(C2=NC(c3ccc(C)cc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.0%) | `platinum` (6.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (38.7%) | `reticulated_vitreous_carbon` (20.5%) | `carbon_rod` (9.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (46.9%) | `carbon` (34.1%) | `nickel` (16.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_plate` (21.9%) | `platinum_plate` (16.7%) | `carbon_generic` (16.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (90.9%) | `divided` (5.9%) | `ABSENT` (3.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (75.0%) | `Li` (21.5%) | `K` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (39.0%) | `ClO4` (33.3%) | `molecular_no_ion` (13.4%) | ✓ |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (7.5%) | `carboxylic_acid` (4.0%) | `as_solvent_polar_aprotic_sulfo` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.3%) | `Mn_complex` (3.1%) | `Co_complex` (1.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (76.9%) | `halogenated_aliphatic` (7.6%) | `cyclic_ether` (3.5%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (99%) | `O` (97%) | `CCOCC` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[SiH](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `CC[SiH](CC)CC` (62%) | `__OTHER__` (58%) | `OB(O)B(O)O` (58%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Pt]` | `__ABSENT__` (53%) | `[Pt]` (42%) | `[Br][Mn][Br]` (1%) | set ✗ / any ✓ |

---

### Reaction #2744  yield=82.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #29)

```
C=Cc1ccc(OC(C)C)cc1>>CC(C)Oc1ccc(C2=NC(c3ccc(OC(C)C)cc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.3%) | `platinum` (1.8%) | `sacrificial_aluminum` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_felt` (26.6%) | `boron_doped_diamond` (24.9%) | `graphite_generic` (15.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (53.3%) | `carbon` (31.0%) | `platinum` (13.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_wire` (36.4%) | `nickel_foam` (23.6%) | `nickel_plate` (10.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (92.8%) | `divided` (4.2%) | `ABSENT` (3.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (55.8%) | `NBu4` (41.0%) | `Na` (2.6%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (69.5%) | `molecular_no_ion` (10.9%) | `BF4` (10.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (8.2%) | `carboxylic_acid` (3.9%) | `primary_amine` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.8%) | `Mn_complex` (5.7%) | `Co_complex` (1.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (33.6%) | `polar_aprotic_amide` (31.9%) | `ABSENT` (10.4%) | ✗ |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (80%) | `O` (64%) | `CCOCC` (26%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C[Si](C)(C)N=[N+]=` | `__ABSENT__` (96%) | `OB(O)B(O)O` (15%) | `O=O` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (94%) | `[Pt]` (2%) | `[Br][Mn][Br]` (2%) | set ✓ / any ✓ |

---

### Reaction #2745  yield=83.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_34_9489-9494.json) (反应 idx 在该 JSON 内 = #30)

```
C=Cc1ccc(OC)cc1>>COc1ccc(C2=NC(c3ccc(OC)cc3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `platinum` (2.1%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (43.2%) | `carbon_felt` (18.2%) | `carbon_generic` (15.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (35.2%) | `carbon` (30.3%) | `nickel` (29.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (16.8%) | `platinum_wire` (14.6%) | `nickel_generic` (13.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (88.9%) | `ABSENT` (8.6%) | `divided` (2.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.7%) | `Li` (13.3%) | `K` (2.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (44.2%) | `BF4` (26.2%) | `carboxylate` (11.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `azide_source` | `ABSENT` (15.0%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.0%) | `Mn_complex` (1.6%) | `Fe_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (52.8%) | `cyclic_ether` (22.0%) | `polar_aprotic_amide` (6.3%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (98%) | `O` (80%) | `CCOCC` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `N=C(c1ccccc1)c1ccc` + `C1CN=C2NCCCN2C1` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (79%) | `N=C(c1ccccc1)c1ccc` (41%) | `C1CN=C2NCCCN2C1` (39%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (55%) | `[Fe+2].c1cc[cH-]c1` (37%) | `CC(=O)NC1CC2(CCCCC` (6%) | set ✗ / any ✓ |

---

### Reaction #2746  yield=60.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_37_10502-10506.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_37_10502-10506.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCc1ccccc1>>c1ccc(CCC2CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (83.0%) | `ABSENT` (7.2%) | `platinum` (3.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `glassy_carbon` (83.5%) | `graphite_rod` (7.1%) | `pencil_graphite` (6.1%) | ✓ |
| 阴极 (材料) | 15 | `lead` | `platinum` (66.8%) | `stainless_steel` (23.1%) | `ABSENT` (5.9%) | ✗ |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_plate` (74.1%) | `stainless_steel_generic` (8.2%) | `unknown_electrode` (7.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (65.4%) | `ABSENT` (29.0%) | `divided` (5.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NBu4` (64.7%) | `ABSENT` (14.9%) | `Na` (11.6%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (58.5%) | `BF4` (26.9%) | `ABSENT` (9.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `as_solvent_halogenated_aliphat` (17.6%) | `as_solvent_polar_aprotic_sulfo` (10.5%) | `carboxylic_acid` (6.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `Mn_complex` (0.2%) | `ionic_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (78.6%) | `polar_aprotic_sulfoxide` (7.9%) | `polar_aprotic_amide` (3.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `FC(F)(F)c1ccccc1` (61%) | `CCOCC` (45%) | `O` (45%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[SiH](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (98%) | `OB(O)B(O)O` (96%) | `O` (69%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Br-].[Br-].[Mn+2]` | `__ABSENT__` (55%) | `c1ccncc1` (22%) | `__OTHER__` (14%) | set ✗ / any ✗ |

---

### Reaction #2747  yield=95.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_37_10502-10506.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_37_10502-10506.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(C(=O)OC)cc1>>COC(=O)c1ccc(C2CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (75.3%) | `platinum` (23.8%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (41.6%) | `graphite_generic` (21.5%) | `platinum_plate` (11.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `lead` | `platinum` (96.6%) | `carbon` (2.7%) | `nickel` (0.3%) | ✗ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (76.8%) | `platinum_generic` (17.3%) | `platinum_wire` (2.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.8%) | `ABSENT` (1.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (70.0%) | `K` (15.0%) | `Na` (6.3%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Br` (44.3%) | `PF6` (38.4%) | `BF4` (6.9%) | ✗ |
| 试剂大类 | 103 | `water` | `alkali_other_salt` (7.1%) | `alkali_sulfinate` (6.2%) | `ABSENT` (5.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (86.0%) | `ABSENT` (10.1%) | `Mn_complex` (1.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (69.3%) | `aqueous` (12.4%) | `ABSENT` (6.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `CCOCC` (83%) | `FC(F)(F)c1ccccc1` (49%) | `CC#N` (47%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (94%) | `__OTHER__` (90%) | `CC[Si](CC)CC` (86%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (98%) | `O=S(=O)(O)C(F)(F)F` (1%) | set ✓ / any ✓ |

---

### Reaction #2748  yield=46.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_3_778-782.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_3_778-782.json) (反应 idx 在该 JSON 内 = #0)

```
O=C=O.[C-]#[N+]c1ccccc1C=C>>O=CN1C(=O)C(CC(=O)O)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (98.9%) | `platinum` (0.7%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_generic` (94.9%) | `platinum_generic` (1.9%) | `magnesium_plate` (1.6%) | ✓ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (85.7%) | `nickel` (7.3%) | `sacrificial_iron` (4.3%) | ✓ |
| 阴极 (细类) | 49 | `iron_plate` | `platinum_generic` (96.2%) | `platinum_plate` (1.5%) | `nickel_plate` (0.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.7%) | `ABSENT` (1.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.8%) | `Li` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (80.9%) | `BF4` (15.4%) | `PF6` (2.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `hcl` | `ABSENT` (21.5%) | `ester` (6.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Ni_complex` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.5%) | `polar_aprotic_amide` (37.2%) | `polar_aprotic_sulfoxide` (2.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (89%) | `CN(C)C=O` (10%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `Br[Ni](Br)(n1cc(c2` (0%) | set ✓ / any ✓ |

---

### Reaction #2749  yield=57.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_46_12784-12789.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_46_12784-12789.json) (反应 idx 在该 JSON 内 = #0)

```
N#Cc1ccccc1.COC(=O)c1ccc(Br)cc1.C=Cc1ccc(OC(C)(C)C)cc1>>COC(=O)c1ccc(CC(c2ccc(C#N)cc2)c2ccc(OC(C)(C)C)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `sacrificial_zinc` (99.3%) | `sacrificial_magnesium` (0.3%) | `sacrificial_iron` (0.2%) | ✗ |
| 阳极 (细类) | 43 | `graphite_generic` | `zinc_generic` (99.9%) | `zinc_plate` (0.1%) | `platinum_plate` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `carbon` (92.9%) | `platinum` (3.2%) | `sacrificial_zinc` (2.5%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `reticulated_vitreous_carbon` (99.4%) | `carbon_felt` (0.2%) | `carbon_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (60.4%) | `BnNMe3` (38.7%) | `NBu4` (0.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Cl` (99.5%) | `Br` (0.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (44.0%) | `primary_amine` (3.5%) | `thiol` (1.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.5%) | `Co_complex` (1.1%) | `pyridine_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.3%) | `cyclic_ether` (0.8%) | `polar_aprotic_sulfoxide` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `CC(C)=O` (0%) | `CN(C)C=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` + `[Cl-].[Na+]` | `__ABSENT__` (100%) | `BrCCBr` (0%) | `COC(=O)c1ccc2cc(C(` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2750  yield=52.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_46_12784-12789.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_46_12784-12789.json) (反应 idx 在该 JSON 内 = #1)

```
N#Cc1ccncc1.COC(=O)c1ccc(Br)cc1.C=Cc1ccc(OC=C(C)C)cc1>>COC(=O)c1ccc(CC(c2ccncc2)c2ccc(OCC=C(C)C)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `sacrificial_zinc` (0.4%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (72.6%) | `graphite_rod` (15.0%) | `zinc_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `carbon` (91.1%) | `platinum` (8.0%) | `nickel` (0.7%) | ✗ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `carbon_cloth` (37.6%) | `graphite_rod` (17.7%) | `reticulated_vitreous_carbon` (12.7%) | ✗ |
| 池型 | 4 | `flow` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✗ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (95.3%) | `NEt4` (3.3%) | `Li` (0.7%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (64.4%) | `PF6` (17.3%) | `Cl` (8.5%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (31.2%) | `primary_amine` (3.4%) | `alkali_carboxylate` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (63.8%) | `pyridine_organocat` (32.8%) | `Co_complex` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.8%) | `ABSENT` (7.6%) | `polar_protic_alcohol` (2.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `CS(C)=O` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2751  yield=40.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #0)

```
Clc1ncnc2nc[nH]c12.C=CNC(=O)c1ccccc1>>Clc1ncnc2ncn(C3COC(c4ccccc4)=N3)c12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (67.6%) | `platinum` (32.4%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (37.2%) | `platinum_generic` (24.7%) | `graphite_rod` (11.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (99.6%) | `stainless_steel` (0.3%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (67.7%) | `platinum_generic` (29.7%) | `stainless_steel_plate` (2.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (57.8%) | `NEt4` (33.9%) | `ABSENT` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (84.6%) | `ABSENT` (9.9%) | `PF6` (2.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (29.9%) | `ABSENT` (7.6%) | `bromide_anion` (4.1%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (71.9%) | `organic_neutral_cat` (12.2%) | `ABSENT` (4.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `polar_aprotic_amide` (0.2%) | `halogenated_aliphatic` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `[Cl-].[Na+]` (100%) | `[Cl-].[Cl-].[Mg+2]` (0%) | `F.c1ccncc1` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (9%) | `__ABSENT__` (1%) | `c1ccc(-c2ccccn2)nc` (1%) | set ✗ / any ✓ |

---

### Reaction #2752  yield=40.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #1)

```
C=CNC(=O)c1ccccc1.Cc1n[nH]cc1Br>>Cc1nn(C2COC(c3ccccc3)=N2)cc1Br
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (91.9%) | `platinum` (8.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (36.6%) | `graphite_rod` (28.2%) | `carbon_cloth` (19.8%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (87.9%) | `nickel` (9.2%) | `stainless_steel` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_generic` (65.4%) | `platinum_plate` (32.4%) | `nickel_plate` (1.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.9%) | `NEt4` (0.1%) | `Li` (0.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (96.9%) | `ClO4` (1.5%) | `PF6` (0.7%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (22.1%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (76.5%) | `ABSENT` (20.5%) | `ammonium_PTC_organocat` (1.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.7%) | `halogenated_aliphatic` (6.9%) | `polar_aprotic_amide` (3.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (41%) | `[Br-].[Na+]` (26%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2753  yield=35.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #2)

```
O=[N+]([O-])c1cn[nH]c1.C=CNC(=O)c1ccccc1>>O=[N+]([O-])c1cnn(C2COC(c3ccccc3)=N2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (55.1%) | `carbon_cloth` (31.5%) | `graphite_rod` (5.8%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (73.8%) | `nickel` (13.1%) | `platinum` (12.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_generic` (39.9%) | `platinum_generic` (30.2%) | `stainless_steel_plate` (16.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (97.5%) | `ABSENT` (2.1%) | `Li` (0.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (97.3%) | `ABSENT` (1.7%) | `Br` (0.3%) | ✓ |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (10.0%) | `chloride_anion` (4.6%) | `metal_oxide_oxidant` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (83.1%) | `ABSENT` (14.3%) | `pyridine_organocat` (1.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (77.0%) | `halogenated_aliphatic` (21.0%) | `polar_aprotic_amide` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (6%) | `O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (89%) | `[Cl-].[Na+]` (10%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (56%) | `__ABSENT__` (3%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #2754  yield=37.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #3)

```
c1cn[nH]c1.C=C(c1ccccc1)c1ccccc1.C=CNC(=O)c1ccccc1>>O=CCC=C(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (91.4%) | `platinum` (7.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (65.4%) | `carbon_felt` (20.6%) | `boron_doped_diamond` (2.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (48.3%) | `stainless_steel` (44.5%) | `nickel` (4.2%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (80.2%) | `stainless_steel_plate` (12.2%) | `unknown_electrode` (5.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.7%) | `Li` (2.5%) | `NEt4` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (85.6%) | `PF6` (5.6%) | `ClO4` (5.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (9.0%) | `chloride_anion` (4.5%) | `boron_lewis_acid` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (77.7%) | `ABSENT` (14.2%) | `pyridine_organocat` (3.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.1%) | `polar_aprotic_amide` (4.4%) | `ketone` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (6%) | `ClCCl` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (86%) | `[Cl-].[Na+]` (13%) | `O=C=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (16%) | `[Br-].[Na+]` (9%) | `__ABSENT__` (1%) | set ✗ / any ✓ |

---

### Reaction #2755  yield=37.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #4)

```
c1cn[nH]c1.C=C(c1ccccc1)c1ccccc1.C=CNC(=O)c1ccccc1>>c1ccc(C2=NC(n3cccn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `platinum` (2.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (52.1%) | `carbon_felt` (27.9%) | `carbon_cloth` (11.0%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (93.0%) | `platinum` (5.8%) | `carbon` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (37.8%) | `stainless_steel_plate` (36.5%) | `stainless_steel_generic` (22.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.5%) | `ABSENT` (2.4%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.7%) | `ABSENT` (3.6%) | `NEt4` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (96.9%) | `ABSENT` (2.0%) | `Cl` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (9.2%) | `chloride_anion` (4.1%) | `cf3_source` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (93.0%) | `organic_neutral_cat` (4.1%) | `ABSENT` (1.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (64.6%) | `halogenated_aliphatic` (32.9%) | `cyclic_ether` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (12%) | `O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (94%) | `[Cl-].[Na+]` (6%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (56%) | `[I-].[K+]` (3%) | `__ABSENT__` (0%) | set ✗ / any ✓ |

---

### Reaction #2756  yield=45.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #5)

```
C=CNC(=O)c1ccccc1.CCOC(=O)c1cn[nH]c1>>CCOC(=O)c1cnn(C2COC(c3ccccc3)=N2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_rod` (47.8%) | `carbon_cloth` (23.4%) | `carbon_felt` (20.2%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (59.0%) | `stainless_steel` (30.4%) | `nickel` (9.7%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (96.1%) | `stainless_steel_plate` (1.4%) | `stainless_steel_generic` (1.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (64.8%) | `ABSENT` (33.4%) | `NEt4` (1.6%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (87.5%) | `ABSENT` (12.3%) | `PF6` (0.1%) | ✓ |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (7.9%) | `chloride_anion` (4.1%) | `metal_oxide_oxidant` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (82.5%) | `ABSENT` (15.3%) | `pyridine_organocat` (0.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.3%) | `halogenated_aliphatic` (0.3%) | `ketone` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (74%) | `[Cl-].[Na+]` (26%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (37%) | `[Br-].[Na+]` (32%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #2757  yield=43.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #6)

```
c1cn[nH]c1.CC1(C)CCCC(C)(C)N1[O].C=CNC(=O)c1ccccc1>>CC1(C)CCCC(C)(C)N1OCC=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (98.0%) | `graphite_rod` (1.2%) | `reticulated_vitreous_carbon` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (99.0%) | `nickel` (0.6%) | `stainless_steel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (88.2%) | `platinum_generic` (10.2%) | `platinum_foil` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (78.4%) | `NBu4` (20.2%) | `ABSENT` (0.9%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (45.5%) | `BF4` (41.3%) | `molecular_no_ion` (10.2%) | ✓ |
| 试剂大类 | 103 | `bromide_anion` | `chloride_anion` (16.1%) | `ABSENT` (9.5%) | `selenium_reagent` (3.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (54.6%) | `ABSENT` (23.4%) | `organic_neutral_cat` (6.4%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.9%) | `tfe` (0.0%) | `halogenated_aliphatic` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (6%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `[Cl-].[Na+]` (52%) | `[Cl-].[NH4+]` (25%) | `[Cl-].[Cl-].[Mg+2]` (11%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (24%) | `O=S(=O)(O)C(F)(F)F` (6%) | `__OTHER__` (4%) | set ✗ / any ✓ |

---

### Reaction #2758  yield=43.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #7)

```
c1cn[nH]c1.CC1(C)CCCC(C)(C)N1[O].C=CNC(=O)c1ccccc1>>c1ccc(C2=NC(n3cccn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (82.2%) | `graphite_generic` (14.7%) | `carbon_cloth` (1.7%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (95.6%) | `platinum` (4.0%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_generic` (53.6%) | `platinum_plate` (26.0%) | `stainless_steel_plate` (19.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.4%) | `ABSENT` (1.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.7%) | `ABSENT` (7.1%) | `Li` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (92.5%) | `ABSENT` (6.3%) | `Cl` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (10.6%) | `chloride_anion` (4.5%) | `cf3_source` (4.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (91.4%) | `organic_neutral_cat` (5.4%) | `ABSENT` (2.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (77.9%) | `halogenated_aliphatic` (20.6%) | `cyclic_ether` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (97%) | `[Cl-].[Na+]` (3%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (81%) | `[I-].[K+]` (2%) | `__ABSENT__` (1%) | set ✗ / any ✓ |

---

### Reaction #2759  yield=60.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #8)

```
c1cn[nH]c1.C=CNC(=O)c1ccc([N+](=O)[O-])cc1>>O=[N+]([O-])c1ccc(C2=NC(n3cccn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.7%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (33.6%) | `carbon_felt` (32.1%) | `graphite_felt` (18.2%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (72.1%) | `platinum` (25.9%) | `nickel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (92.7%) | `stainless_steel_generic` (4.2%) | `stainless_steel_plate` (1.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (98.6%) | `ABSENT` (1.1%) | `Li` (0.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (98.8%) | `ABSENT` (0.7%) | `Cl` (0.3%) | ✓ |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (12.0%) | `chloride_anion` (2.8%) | `cf3_source` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (67.1%) | `organic_neutral_cat` (21.8%) | `pyridine_organocat` (5.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.4%) | `halogenated_aliphatic` (42.5%) | `ketone` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (15%) | `__ABSENT__` (6%) | `[I-].[K+]` (0%) | set ✗ / any ✓ |

---

### Reaction #2760  yield=59.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #9)

```
c1cn[nH]c1.C=CNC(=O)c1cccs1>>c1csc(C2=NC(n3cccn3)CO2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.5%) | `platinum` (1.5%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (85.1%) | `carbon_felt` (6.6%) | `graphite_felt` (2.4%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (53.9%) | `platinum` (43.4%) | `carbon` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (89.2%) | `platinum_generic` (4.3%) | `stainless_steel_generic` (4.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (92.7%) | `ABSENT` (7.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.4%) | `ABSENT` (1.2%) | `NEt4` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (97.2%) | `ABSENT` (1.3%) | `Cl` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (8.5%) | `cf3_source` (3.4%) | `metal_oxide_oxidant` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (78.8%) | `ABSENT` (11.2%) | `organic_neutral_cat` (9.4%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (55.7%) | `polar_aprotic_nitrile` (40.6%) | `cyclic_ether` (2.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (57%) | `ClCCl` (18%) | `O` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (1%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (23%) | `__ABSENT__` (5%) | `[I-].[K+]` (1%) | set ✗ / any ✓ |

---

### Reaction #2761  yield=56.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #10)

```
C=CNC(=O)c1ccccc1.Clc1cn[nH]c1>>Clc1cnn(C2COC(c3ccccc3)=N2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (58.3%) | `carbon_cloth` (21.1%) | `graphite_rod` (11.7%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (49.8%) | `stainless_steel` (47.1%) | `nickel` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (91.3%) | `stainless_steel_plate` (4.1%) | `stainless_steel_generic` (2.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (69.3%) | `ABSENT` (30.3%) | `NEt4` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (85.9%) | `ABSENT` (13.8%) | `Cl` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (8.1%) | `chloride_anion` (6.6%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (89.7%) | `ABSENT` (8.4%) | `organic_neutral_cat` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.9%) | `halogenated_aliphatic` (4.4%) | `ketone` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (13%) | `O` (6%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (80%) | `[Cl-].[Na+]` (20%) | `CCOC(C)=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (19%) | `__ABSENT__` (6%) | `__OTHER__` (3%) | set ✗ / any ✓ |

---

### Reaction #2762  yield=55.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #11)

```
Brc1cn[nH]c1.C=CNC(=O)c1ccccc1>>Brc1cnn(C2COC(c3ccccc3)=N2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_rod` (52.5%) | `carbon_felt` (16.4%) | `carbon_cloth` (16.3%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (72.7%) | `stainless_steel` (16.2%) | `nickel` (10.9%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (88.1%) | `stainless_steel_plate` (6.5%) | `platinum_generic` (2.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.6%) | `NEt4` (1.7%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.4%) | `ABSENT` (0.3%) | `PF6` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (14.2%) | `chloride_anion` (6.9%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (95.2%) | `ABSENT` (3.8%) | `organic_neutral_cat` (0.4%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.1%) | `halogenated_aliphatic` (1.6%) | `polar_aprotic_amide` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (2%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (77%) | `[Cl-].[Na+]` (22%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (25%) | `__ABSENT__` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #2763  yield=54.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #12)

```
c1cn[nH]c1.C=CNC(=O)c1ccc(C(F)(F)F)cc1>>FC(F)(F)c1ccc(C2=NC(n3cccn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.4%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (48.1%) | `graphite_felt` (13.6%) | `graphite_generic` (12.0%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (83.1%) | `platinum` (14.4%) | `carbon` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (95.0%) | `stainless_steel_generic` (3.2%) | `stainless_steel_plate` (1.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.5%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.8%) | `ABSENT` (0.9%) | `NEt4` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (98.8%) | `ABSENT` (0.7%) | `Cl` (0.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (12.8%) | `chloride_anion` (3.0%) | `cf3_source` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (90.2%) | `organic_neutral_cat` (6.5%) | `ABSENT` (1.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (81.3%) | `halogenated_aliphatic` (15.2%) | `ketone` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (1%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (21%) | `[I-].[K+]` (5%) | `__ABSENT__` (4%) | set ✗ / any ✓ |

---

### Reaction #2764  yield=54.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #13)

```
c1ccc2[nH]nnc2c1.C=CNC(=O)c1ccccc1>>c1ccc(C2=NC(N3Nc4ccccc4N3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_rod` (87.6%) | `graphite_generic` (7.1%) | `carbon_cloth` (3.7%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (74.7%) | `stainless_steel` (22.1%) | `nickel` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (72.5%) | `stainless_steel_plate` (24.1%) | `platinum_generic` (2.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.6%) | `ABSENT` (1.5%) | `NEt4` (0.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (97.3%) | `ABSENT` (1.2%) | `Br` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (15.2%) | `chloride_anion` (11.8%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (90.7%) | `ABSENT` (7.6%) | `pyridine_organocat` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.2%) | `halogenated_aliphatic` (0.7%) | `polar_aprotic_amide` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (4%) | `O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (57%) | `[Cl-].[Na+]` (43%) | `Cc1ccc(I)cc1` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (44%) | `__ABSENT__` (1%) | `[I-].[K+]` (0%) | set ✗ / any ✓ |

---

### Reaction #2765  yield=56.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #14)

```
Cn1c(=O)c2[nH]c(Cl)nc2n(C)c1=O.C=CNC(=O)c1ccccc1>>Cn1c(=O)c2c(nc(Cl)n2C2COC(c3ccccc3)=N2)n(C)c1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `sacrificial_iron` (0.4%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (75.2%) | `graphite_generic` (12.0%) | `carbon_felt` (11.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (64.7%) | `nickel` (30.2%) | `platinum` (4.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (81.3%) | `stainless_steel_generic` (12.7%) | `nickel_foam` (2.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.7%) | `ABSENT` (2.1%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (56.8%) | `ABSENT` (18.0%) | `PF6` (10.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (17.1%) | `chloride_anion` (3.4%) | `hcl` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (92.7%) | `organic_neutral_cat` (2.4%) | `pyridine_organocat` (1.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.1%) | `polar_aprotic_amide` (3.3%) | `halogenated_aliphatic` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `O` (2%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (97%) | `[Cl-].[Na+]` (2%) | `CCOC(C)=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (78%) | `__ABSENT__` (0%) | `__OTHER__` (0%) | set ✗ / any ✓ |

---

### Reaction #2766  yield=53.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #15)

```
c1nnc[nH]1.C=CNC(=O)c1ccccc1>>c1ccc(C2=NC(n3cncn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (77.6%) | `platinum` (22.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_rod` (43.6%) | `carbon_felt` (35.3%) | `carbon_cloth` (5.2%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (71.2%) | `stainless_steel` (18.6%) | `nickel` (6.2%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (82.4%) | `stainless_steel_plate` (10.3%) | `platinum_generic` (2.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (52.3%) | `NBu4` (41.1%) | `NEt4` (5.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (78.4%) | `ABSENT` (20.3%) | `ClO4` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (12.2%) | `chloride_anion` (6.8%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (88.1%) | `ABSENT` (8.2%) | `pyridine_organocat` (1.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.1%) | `halogenated_aliphatic` (2.9%) | `polar_aprotic_amide` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (97%) | `[Cl-].[Na+]` (3%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (13%) | `__ABSENT__` (2%) | `__OTHER__` (2%) | set ✗ / any ✓ |

---

### Reaction #2767  yield=53.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #16)

```
C=CNC(=O)c1ccccc1.N#Cc1cn[nH]c1>>N#Cc1cnn(C2COC(c3ccccc3)=N2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_rod` (73.0%) | `carbon_felt` (10.3%) | `graphite_generic` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (78.0%) | `stainless_steel` (12.5%) | `nickel` (6.7%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (79.0%) | `platinum_generic` (7.5%) | `stainless_steel_plate` (5.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.7%) | `ABSENT` (7.1%) | `NEt4` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (92.1%) | `ABSENT` (6.3%) | `PF6` (0.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (7.7%) | `metal_oxide_oxidant` (2.5%) | `tellurium_reagent` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (52.7%) | `pyridine_organocat` (21.3%) | `ionic_organocat` (17.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (78.8%) | `halogenated_aliphatic` (10.5%) | `polar_aprotic_amide` (9.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `CN(C)C=O` (1%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (98%) | `[Cl-].[Na+]` (2%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2768  yield=61.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #17)

```
c1cn[nH]c1.C=CNC(=O)c1ccc(Br)nc1>>Brc1ccc(C2=NC(n3cccn3)CO2)cn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (80.2%) | `carbon_cloth` (10.8%) | `graphite_plate` (3.9%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (95.7%) | `platinum` (2.9%) | `carbon` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (68.9%) | `stainless_steel_plate` (23.1%) | `stainless_steel_generic` (7.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.5%) | `ABSENT` (0.3%) | `NEt4` (0.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (99.4%) | `ABSENT` (0.2%) | `Cl` (0.2%) | ✓ |
| 试剂大类 | 103 | `inorganic_simple` | `ABSENT` (9.9%) | `chloride_anion` (4.5%) | `cf3_source` (3.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (93.6%) | `organic_neutral_cat` (3.1%) | `ABSENT` (2.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (80.2%) | `halogenated_aliphatic` (17.0%) | `ketone` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (2%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Na][Br]` | `__ABSENT__` (96%) | `[Cl-].[Na+]` (4%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (87%) | `[I-].[K+]` (3%) | `__ABSENT__` (1%) | set ✗ / any ✓ |

---

### Reaction #2769  yield=65.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #18)

```
c1cn[nH]c1.C=CNC(=O)c1ccccc1Cl>>Clc1ccccc1C1=NC(n2cccn2)CO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (58.2%) | `carbon_felt` (26.3%) | `carbon_cloth` (10.1%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (71.5%) | `platinum` (26.5%) | `carbon` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (91.5%) | `stainless_steel_generic` (6.6%) | `platinum_generic` (0.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.3%) | `ABSENT` (3.5%) | `NEt4` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (98.4%) | `ABSENT` (1.4%) | `Cl` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (14.2%) | `cf3_source` (4.9%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (70.2%) | `organic_neutral_cat` (15.6%) | `ABSENT` (13.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (83.0%) | `halogenated_aliphatic` (14.9%) | `ketone` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (1%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (14%) | `[Br-].[Na+]` (13%) | `[I-].[K+]` (1%) | set ✗ / any ✓ |

---

### Reaction #2770  yield=68.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #19)

```
c1cn[nH]c1.C=CNC(=O)c1cccc2ccccc12>>c1ccc2c(C3=NC(n4cccn4)CO3)cccc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (67.1%) | `graphite_generic` (15.9%) | `carbon_cloth` (6.9%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (61.1%) | `platinum` (37.8%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (99.6%) | `stainless_steel_generic` (0.3%) | `stainless_steel_plate` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.3%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.8%) | `ABSENT` (3.4%) | `Li` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (98.5%) | `ABSENT` (1.2%) | `ClO4` (0.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (7.3%) | `cf3_source` (5.6%) | `boron_lewis_acid` (3.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (80.8%) | `ABSENT` (10.4%) | `organic_neutral_cat` (8.0%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.1%) | `halogenated_aliphatic` (1.6%) | `ketone` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (0%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (1%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (27%) | `__ABSENT__` (20%) | `[I-].[K+]` (2%) | set ✗ / any ✓ |

---

### Reaction #2771  yield=68.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #20)

```
C=CNC(=O)c1ccccc1.Fc1cn[nH]c1>>Fc1cnn(C2COC(c3ccccc3)=N2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_rod` (67.4%) | `carbon_felt` (13.8%) | `graphite_generic` (10.7%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (69.4%) | `stainless_steel` (26.2%) | `nickel` (4.0%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (86.4%) | `platinum_generic` (5.4%) | `stainless_steel_plate` (3.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (67.8%) | `ABSENT` (30.1%) | `NEt4` (1.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (85.6%) | `ABSENT` (14.0%) | `PF6` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (11.1%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (95.4%) | `ABSENT` (3.5%) | `organic_neutral_cat` (0.3%) | ✓ |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (98.1%) | `halogenated_aliphatic` (1.1%) | `ABSENT` (0.3%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (99%) | `ClCCl` (1%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (97%) | `[Cl-].[Na+]` (3%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (32%) | `__ABSENT__` (3%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #2772  yield=67.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #21)

```
c1cn[nH]c1.C=CNC(=O)c1ccc2ccccc2c1>>c1ccc2cc(C3=NC(n4cccn4)CO3)ccc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (1.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (53.4%) | `graphite_generic` (19.1%) | `graphite_felt` (7.8%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (69.8%) | `platinum` (25.1%) | `carbon` (4.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (92.7%) | `stainless_steel_plate` (3.9%) | `stainless_steel_generic` (2.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.8%) | `NEt4` (0.8%) | `Li` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (99.2%) | `Cl` (0.4%) | `ClO4` (0.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (13.3%) | `chloride_anion` (4.1%) | `cf3_source` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (90.8%) | `organic_neutral_cat` (4.8%) | `ABSENT` (3.7%) | ✓ |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (92.6%) | `halogenated_aliphatic` (5.5%) | `ketone` (0.8%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `O` (1%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (1%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (25%) | `__ABSENT__` (5%) | `__OTHER__` (3%) | set ✗ / any ✓ |

---

### Reaction #2773  yield=62.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #22)

```
c1ccc(-c2cc(-c3ccccc3)[nH]n2)cc1.C=CNC(=O)c1ccccc1>>c1ccc(C2=NC(n3nc(-c4ccccc4)cc3-c3ccccc3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.5%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (63.2%) | `graphite_rod` (18.6%) | `graphite_generic` (13.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (59.7%) | `nickel` (25.4%) | `stainless_steel` (14.6%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (81.9%) | `platinum_generic` (7.1%) | `stainless_steel_plate` (4.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (62.4%) | `ABSENT` (33.0%) | `NEt4` (3.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (58.7%) | `ABSENT` (37.2%) | `PF6` (1.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (10.0%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (79.6%) | `pyridine_organocat` (10.4%) | `ABSENT` (6.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `polar_aprotic_amide` (0.3%) | `halogenated_aliphatic` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (13%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (67%) | `[Cl-].[Na+]` (32%) | `Cl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (1%) | `O=C([O-])c1ccccc1-` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #2774  yield=70.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #23)

```
C=CNC(=O)c1ccccc1.c1cc(C2CC2)n[nH]1>>c1ccc(C2=NC(n3ccc(C4CC4)n3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (85.6%) | `platinum` (13.7%) | `sacrificial_iron` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (58.9%) | `carbon_felt` (22.7%) | `graphite_plate` (5.0%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (79.7%) | `platinum` (16.2%) | `nickel` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_generic` (47.7%) | `platinum_plate` (20.8%) | `platinum_generic` (13.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.5%) | `Li` (1.4%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (69.0%) | `ClO4` (16.1%) | `Cl` (4.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (21.6%) | `chloride_anion` (2.6%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (80.1%) | `ABSENT` (8.1%) | `organic_neutral_cat` (6.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.9%) | `halogenated_aliphatic` (7.3%) | `polar_aprotic_amide` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (5%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (98%) | `[Cl-].[Na+]` (2%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (20%) | `__OTHER__` (2%) | `__ABSENT__` (0%) | set ✗ / any ✓ |

---

### Reaction #2775  yield=70.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #24)

```
c1cn[nH]c1.C=CNC(=O)c1ccc(-c2ccccc2)cc1>>c1ccc(-c2ccc(C3=NC(n4cccn4)CO3)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (71.7%) | `graphite_generic` (11.6%) | `carbon_cloth` (5.9%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (49.8%) | `platinum` (48.4%) | `carbon` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (98.1%) | `stainless_steel_generic` (0.7%) | `platinum_generic` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.1%) | `ABSENT` (1.6%) | `NEt4` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (96.8%) | `ABSENT` (1.5%) | `Cl` (1.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (12.3%) | `cf3_source` (3.2%) | `chloride_anion` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (76.4%) | `organic_neutral_cat` (18.0%) | `ABSENT` (3.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (73.0%) | `halogenated_aliphatic` (22.9%) | `ketone` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (1%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (5%) | `[I-].[K+]` (2%) | `__ABSENT__` (1%) | set ✗ / any ✓ |

---

### Reaction #2776  yield=80.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #25)

```
c1cn[nH]c1.C=CNC(=O)c1ccc(F)cc1>>Fc1ccc(C2=NC(n3cccn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.4%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (60.1%) | `graphite_generic` (31.0%) | `carbon_cloth` (4.9%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (96.7%) | `platinum` (2.3%) | `carbon` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_generic` (59.2%) | `platinum_plate` (21.6%) | `stainless_steel_plate` (15.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.7%) | `ABSENT` (1.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.5%) | `ABSENT` (1.8%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.8%) | `ABSENT` (1.6%) | `Cl` (1.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (12.4%) | `chloride_anion` (5.9%) | `boron_lewis_acid` (4.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (97.6%) | `organic_neutral_cat` (1.6%) | `ammonium_PTC_organocat` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (85.8%) | `halogenated_aliphatic` (11.4%) | `cyclic_ether` (1.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (1%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (1%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (80%) | `[I-].[K+]` (3%) | `__OTHER__` (1%) | set ✗ / any ✗ |

---

### Reaction #2777  yield=78.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #26)

```
c1cn[nH]c1.C=CNC(=O)c1ccc(OC)cc1>>COc1ccc(C2=NC(n3cccn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (1.4%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (94.7%) | `carbon_cloth` (2.9%) | `graphite_plate` (0.9%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (69.9%) | `stainless_steel` (26.5%) | `carbon` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (99.2%) | `platinum_generic` (0.3%) | `stainless_steel_plate` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.4%) | `ABSENT` (1.1%) | `divided` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (98.3%) | `ABSENT` (1.4%) | `Li` (0.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (98.1%) | `ABSENT` (1.2%) | `Cl` (0.5%) | ✓ |
| 试剂大类 | 103 | `inorganic_simple` | `ABSENT` (15.2%) | `cf3_source` (3.1%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (79.3%) | `organic_neutral_cat` (10.7%) | `ABSENT` (9.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `halogenated_aliphatic` (17.2%) | `ketone` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Na][Br]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (13%) | `[Br-].[Na+]` (12%) | `[I-].[K+]` (5%) | set ✗ / any ✓ |

---

### Reaction #2778  yield=77.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #27)

```
c1cn[nH]c1.C=CNC(=O)c1ccc(OCC)cc1>>CCOc1ccc(C2=NC(n3cccn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (92.3%) | `graphite_generic` (3.8%) | `graphite_felt` (1.7%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (63.4%) | `platinum` (33.0%) | `carbon` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (90.0%) | `stainless_steel_generic` (5.7%) | `platinum_generic` (1.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.6%) | `ABSENT` (4.1%) | `Li` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (97.7%) | `ABSENT` (2.0%) | `Cl` (0.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (12.6%) | `cf3_source` (5.2%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (64.2%) | `ABSENT` (18.9%) | `organic_neutral_cat` (13.7%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (76.8%) | `halogenated_aliphatic` (22.0%) | `ketone` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (0%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (30%) | `[Br-].[Na+]` (19%) | `[I-].[K+]` (1%) | set ✗ / any ✓ |

---

### Reaction #2779  yield=72.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #28)

```
c1cn[nH]c1.C=CNC(=O)c1ccccc1C>>Cc1ccccc1C1=NC(n2cccn2)CO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.7%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (54.5%) | `carbon_cloth` (21.1%) | `graphite_plate` (9.1%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (81.4%) | `platinum` (17.2%) | `carbon` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (98.2%) | `stainless_steel_generic` (0.9%) | `stainless_steel_plate` (0.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (0.9%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (84.1%) | `ABSENT` (15.5%) | `NEt4` (0.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (91.3%) | `ABSENT` (8.3%) | `Cl` (0.2%) | ✓ |
| 试剂大类 | 103 | `inorganic_simple` | `ABSENT` (11.8%) | `cf3_source` (4.3%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (69.4%) | `organic_neutral_cat` (25.4%) | `ABSENT` (4.0%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (91.0%) | `halogenated_aliphatic` (7.7%) | `ketone` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Na][Br]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (55%) | `__ABSENT__` (4%) | `[I-].[K+]` (3%) | set ✗ / any ✓ |

---

### Reaction #2780  yield=77.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #29)

```
c1cn[nH]c1.C=CNC(=O)c1cccc(Cl)c1>>Clc1cccc(C2=NC(n3cccn3)CO2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (73.1%) | `graphite_generic` (15.5%) | `graphite_felt` (4.3%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (71.5%) | `platinum` (26.6%) | `carbon` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (89.6%) | `stainless_steel_generic` (7.1%) | `platinum_generic` (2.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `ABSENT` (0.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (95.0%) | `ABSENT` (4.8%) | `NEt4` (0.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (95.9%) | `ABSENT` (3.5%) | `Cl` (0.5%) | ✓ |
| 试剂大类 | 103 | `inorganic_simple` | `ABSENT` (13.1%) | `cf3_source` (3.8%) | `chloride_anion` (3.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (78.6%) | `organic_neutral_cat` (15.0%) | `ABSENT` (4.4%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (53.8%) | `polar_aprotic_nitrile` (41.2%) | `ketone` (2.5%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (25%) | `CC#N` (13%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Na][Br]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (5%) | `__OTHER__` (2%) | `__ABSENT__` (2%) | set ✗ / any ✓ |

---

### Reaction #2781  yield=77.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #30)

```
c1cn[nH]c1.C=CNC(=O)c1ccc(Cl)cc1>>Clc1ccc(C2=NC(n3cccn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.4%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (73.5%) | `graphite_generic` (16.1%) | `graphite_felt` (6.3%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (84.2%) | `platinum` (14.4%) | `carbon` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (84.6%) | `stainless_steel_generic` (12.2%) | `stainless_steel_plate` (2.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.7%) | `ABSENT` (1.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (86.9%) | `ABSENT` (12.6%) | `NEt4` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (94.5%) | `ABSENT` (5.1%) | `Cl` (0.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (10.1%) | `cf3_source` (5.3%) | `boron_lewis_acid` (4.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (83.7%) | `ABSENT` (7.5%) | `organic_neutral_cat` (7.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (88.2%) | `halogenated_aliphatic` (10.3%) | `ketone` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (63%) | `__ABSENT__` (5%) | `__OTHER__` (4%) | set ✗ / any ✓ |

---

### Reaction #2782  yield=77.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #31)

```
c1cn[nH]c1.C=CNC(=O)c1ccc(C)cc1>>Cc1ccc(C2=NC(n3cccn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (1.4%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (78.2%) | `graphite_felt` (9.1%) | `graphite_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (52.5%) | `stainless_steel` (42.8%) | `carbon` (3.2%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (95.1%) | `stainless_steel_generic` (1.9%) | `stainless_steel_plate` (1.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.1%) | `ABSENT` (1.5%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (97.5%) | `ABSENT` (2.1%) | `NEt4` (0.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (98.2%) | `ABSENT` (1.3%) | `Cl` (0.2%) | ✓ |
| 试剂大类 | 103 | `inorganic_simple` | `ABSENT` (11.0%) | `cf3_source` (5.8%) | `chloride_anion` (4.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (80.1%) | `organic_neutral_cat` (13.9%) | `ABSENT` (3.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.9%) | `halogenated_aliphatic` (40.9%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Na][Br]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (42%) | `__ABSENT__` (4%) | `[I-].[K+]` (1%) | set ✗ / any ✓ |

---

### Reaction #2783  yield=73.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #32)

```
c1cn[nH]c1.C=CNC(=O)c1ccc(Cl)nc1>>Clc1ccc(C2=NC(n3cccn3)CO2)cn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.4%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (53.0%) | `carbon_cloth` (22.7%) | `graphite_generic` (10.1%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (98.9%) | `platinum` (0.7%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (53.3%) | `platinum_plate` (35.2%) | `stainless_steel_generic` (11.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.7%) | `ABSENT` (1.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.4%) | `NEt4` (0.3%) | `ABSENT` (0.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (98.3%) | `Cl` (0.9%) | `Br` (0.3%) | ✗ |
| 试剂大类 | 103 | `inorganic_simple` | `ABSENT` (7.3%) | `chloride_anion` (6.0%) | `cf3_source` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (93.2%) | `organic_neutral_cat` (4.1%) | `ABSENT` (1.6%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.0%) | `halogenated_aliphatic` (14.8%) | `ketone` (2.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Na][Br]` | `__ABSENT__` (90%) | `[Cl-].[Na+]` (10%) | `CCOC(C)=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (95%) | `[I-].[K+]` (1%) | `__ABSENT__` (0%) | set ✗ / any ✓ |

---

### Reaction #2784  yield=73.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #33)

```
c1cn[nH]c1.C=CNC(=O)c1ccc(Br)cc1>>Brc1ccc(C2=NC(n3cccn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.5%) | `platinum` (1.4%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (63.3%) | `carbon_cloth` (14.8%) | `graphite_generic` (8.1%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (53.2%) | `stainless_steel` (42.4%) | `carbon` (2.8%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (96.4%) | `stainless_steel_plate` (1.7%) | `stainless_steel_generic` (0.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (97.5%) | `ABSENT` (1.9%) | `NEt4` (0.5%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (98.4%) | `ABSENT` (1.0%) | `Cl` (0.4%) | ✓ |
| 试剂大类 | 103 | `inorganic_simple` | `ABSENT` (16.7%) | `chloride_anion` (3.4%) | `cf3_source` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (86.8%) | `organic_neutral_cat` (6.7%) | `ABSENT` (5.0%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.6%) | `halogenated_aliphatic` (3.4%) | `ketone` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Na][Br]` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (1%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (19%) | `__ABSENT__` (4%) | `[I-].[K+]` (2%) | set ✗ / any ✓ |

---

### Reaction #2785  yield=74.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #34)

```
Cc1cn[nH]c1.C=CNC(=O)c1ccccc1>>Cc1cnn(C2COC(c3ccccc3)=N2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_rod` (48.5%) | `carbon_cloth` (26.9%) | `carbon_felt` (14.3%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `nickel` (49.8%) | `stainless_steel` (35.6%) | `platinum` (14.4%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `nickel_plate` (45.2%) | `stainless_steel_plate` (18.0%) | `platinum_plate` (13.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (83.4%) | `ABSENT` (16.4%) | `NEt4` (0.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (84.4%) | `ABSENT` (14.6%) | `Br` (0.4%) | ✓ |
| 试剂大类 | 103 | `inorganic_simple` | `ABSENT` (9.2%) | `chloride_anion` (3.5%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (95.5%) | `ABSENT` (2.4%) | `pyridine_organocat` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (81.3%) | `halogenated_aliphatic` (8.4%) | `polar_aprotic_amide` (6.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (1%) | `CN(C)C=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Na][Br]` | `__ABSENT__` (97%) | `[Cl-].[Na+]` (3%) | `CCOC(C)=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (88%) | `__ABSENT__` (0%) | `__OTHER__` (0%) | set ✗ / any ✓ |

---

### Reaction #2786  yield=83.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #35)

```
c1cn[nH]c1.C=CNC(=O)c1ccc(CC)cc1>>CCc1ccc(C2=NC(n3cccn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (85.4%) | `graphite_generic` (7.1%) | `carbon_cloth` (5.0%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (80.0%) | `platinum` (18.5%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (87.1%) | `stainless_steel_generic` (6.1%) | `stainless_steel_plate` (4.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.4%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.3%) | `ABSENT` (0.4%) | `Li` (0.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (99.1%) | `Cl` (0.3%) | `ABSENT` (0.3%) | ✓ |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (16.1%) | `chloride_anion` (6.3%) | `boron_lewis_acid` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (91.0%) | `organic_neutral_cat` (7.3%) | `ABSENT` (0.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.0%) | `halogenated_aliphatic` (5.3%) | `ketone` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (0%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (59%) | `__ABSENT__` (3%) | `[I-].[K+]` (1%) | set ✗ / any ✓ |

---

### Reaction #2787  yield=87.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #36)

```
c1cn[nH]c1.C=CNC(=O)c1ccc(CCCC)cc1>>CCCCc1ccc(C2=NC(n3cccn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (69.1%) | `graphite_generic` (17.4%) | `graphite_felt` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (88.6%) | `platinum` (9.5%) | `nickel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (83.9%) | `stainless_steel_generic` (11.7%) | `stainless_steel_plate` (2.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (0.9%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.9%) | `ABSENT` (4.8%) | `Li` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (96.0%) | `ABSENT` (3.3%) | `Cl` (0.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (14.4%) | `cf3_source` (4.2%) | `chloride_anion` (3.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (82.5%) | `organic_neutral_cat` (13.4%) | `ABSENT` (1.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (80.7%) | `halogenated_aliphatic` (17.0%) | `ketone` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (0%) | `CC(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (80%) | `__ABSENT__` (4%) | `[I-].[K+]` (1%) | set ✗ / any ✓ |

---

### Reaction #2788  yield=83.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #37)

```
c1cn[nH]c1.C=CNC(=O)c1cccc(C)c1>>Cc1cccc(C2=NC(n3cccn3)CO2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.8%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (52.6%) | `graphite_generic` (34.3%) | `carbon_cloth` (4.6%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (72.3%) | `platinum` (20.2%) | `carbon` (6.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (89.2%) | `stainless_steel_generic` (6.5%) | `graphite_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.4%) | `ABSENT` (3.5%) | `NEt4` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (94.1%) | `ABSENT` (4.7%) | `Cl` (0.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (16.3%) | `cf3_source` (3.7%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (67.1%) | `organic_neutral_cat` (24.8%) | `ammonium_PTC_organocat` (3.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (79.7%) | `halogenated_aliphatic` (18.3%) | `cyclic_ether` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (8%) | `__ABSENT__` (6%) | `[I-].[K+]` (1%) | set ✗ / any ✓ |

---

### Reaction #2789  yield=86.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #38)

```
c1cn[nH]c1.C=CNC(=O)c1ccc(OC)c(OC)c1>>COc1ccc(C2=NC(n3cccn3)CO2)cc1OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (75.8%) | `graphite_plate` (6.4%) | `graphite_felt` (4.2%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (50.8%) | `platinum` (45.0%) | `carbon` (3.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (98.4%) | `stainless_steel_plate` (0.8%) | `stainless_steel_generic` (0.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.3%) | `ABSENT` (8.2%) | `Li` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.1%) | `ABSENT` (3.7%) | `Cl` (0.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (17.9%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (85.7%) | `ABSENT` (6.7%) | `organic_neutral_cat` (6.0%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `halogenated_aliphatic` (0.9%) | `ketone` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (25%) | `[Br-].[Na+]` (21%) | `[I-].[K+]` (1%) | set ✗ / any ✓ |

---

### Reaction #2790  yield=90.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #39)

```
Cc1cc(C)[nH]n1.C=CNC(=O)c1ccccc1>>Cc1cc(C)n(C2COC(c3ccccc3)=N2)n1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.5%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (38.3%) | `carbon_felt` (24.9%) | `carbon_cloth` (18.4%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `platinum` (72.9%) | `stainless_steel` (18.2%) | `nickel` (8.4%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (86.4%) | `platinum_generic` (6.6%) | `nickel_plate` (3.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (92.3%) | `NBu4` (6.9%) | `Li` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (77.2%) | `BF4` (21.8%) | `ClO4` (0.7%) | ✓ |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (9.8%) | `boron_lewis_acid` (3.4%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (95.5%) | `organic_neutral_cat` (2.6%) | `ABSENT` (0.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (87.0%) | `halogenated_aliphatic` (10.4%) | `ABSENT` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (1%) | `O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (5%) | `[I-].[K+]` (2%) | `__ABSENT__` (1%) | set ✗ / any ✓ |

---

### Reaction #2791  yield=89.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #40)

```
c1cn[nH]c1.C=CNC(=O)c1c(C)cc(C)cc1C>>Cc1cc(C)c(C2=NC(n3cccn3)CO2)c(C)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (70.6%) | `graphite_generic` (15.6%) | `graphite_felt` (3.9%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (79.3%) | `platinum` (20.1%) | `carbon` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (97.0%) | `stainless_steel_generic` (2.5%) | `stainless_steel_plate` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.4%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (73.5%) | `NBu4` (26.0%) | `NEt4` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (55.9%) | `BF4` (43.6%) | `Cl` (0.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `inorganic_simple` | `cf3_source` (7.9%) | `ABSENT` (7.5%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (54.0%) | `ionic_organocat` (35.1%) | `ABSENT` (5.7%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (63.2%) | `polar_aprotic_nitrile` (33.9%) | `ketone` (1.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (45%) | `CC#N` (24%) | `ClCCCl` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Na][Br]` | `OC(C(F)(F)F)C(F)(F` (33%) | `O=S(=O)(O)C(F)(F)F` (30%) | `[Cl-].[Na+]` (13%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (19%) | `[Br-].[Na+]` (2%) | `N#Cc1c(-n2c3ccccc3` (1%) | set ✗ / any ✓ |

---

### Reaction #2792  yield=95.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #41)

```
c1cn[nH]c1.C=CNC(=O)c1ccccc1>>c1ccc(C2=NC(n3cccn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (1.4%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (50.6%) | `carbon_felt` (29.9%) | `carbon_cloth` (13.7%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (96.0%) | `platinum` (3.1%) | `carbon` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `stainless_steel_plate` (43.7%) | `stainless_steel_generic` (36.5%) | `platinum_plate` (17.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (91.0%) | `ABSENT` (8.9%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (96.7%) | `ABSENT` (2.7%) | `NEt4` (0.4%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (95.7%) | `ABSENT` (2.0%) | `Cl` (1.6%) | ✓ |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (10.8%) | `chloride_anion` (5.2%) | `cf3_source` (4.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (94.4%) | `organic_neutral_cat` (3.5%) | `ABSENT` (1.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (53.0%) | `halogenated_aliphatic` (41.6%) | `cyclic_ether` (2.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (11%) | `O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (90%) | `[Cl-].[Na+]` (9%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-].[Na+]` | `[Br-].[Na+]` (66%) | `[I-].[K+]` (2%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2793  yield=95.0%

**Source paper**: [`OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json`](reactions_by_journal_alkene_ec_audited/OrgLett/2025_Organic_Letters_2025_27_8_1841-1846.json) (反应 idx 在该 JSON 内 = #42)

```
c1cn[nH]c1.C=CNC(=O)c1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc(C2=NC(n3cccn3)CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (1.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (66.3%) | `carbon_cloth` (8.6%) | `graphite_felt` (7.4%) | ✓ |
| 阴极 (材料) | 15 | `stainless_steel` | `stainless_steel` (51.9%) | `platinum` (45.4%) | `carbon` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `stainless_steel_plate` | `platinum_plate` (96.8%) | `stainless_steel_generic` (1.8%) | `platinum_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `ABSENT` (0.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (95.5%) | `ABSENT` (3.3%) | `NEt4` (0.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (95.9%) | `ABSENT` (2.6%) | `Cl` (0.6%) | ✓ |
| 试剂大类 | 103 | `bromide_anion` | `ABSENT` (11.8%) | `cf3_source` (3.8%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ionic_organocat` (61.9%) | `organic_neutral_cat` (33.7%) | `ABSENT` (2.4%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.3%) | `halogenated_aliphatic` (2.8%) | `cyclic_ether` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (1%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Br-].[Na+]` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Na+]` (25%) | `[I-].[K+]` (5%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #2794  yield=40.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #0)

```
O=S(O)C(F)(F)F.[Na].C=C(CCCO)c1ccc2ccccc2c1>>FC(F)(F)CC1(c2ccc3ccccc3c2)CCCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (78.8%) | `graphite_rod` (11.7%) | `graphite_felt` (4.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (84.6%) | `platinum` (13.3%) | `carbon` (1.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_plate` (78.3%) | `platinum_generic` (17.3%) | `nickel_generic` (2.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NEt4` (54.2%) | `NBu4` (30.5%) | `Li` (14.1%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (36.0%) | `BF4` (32.5%) | `PF6` (24.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (42.4%) | `metal_oxide_oxidant` (1.7%) | `tellurium_reagent` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.6%) | `ABSENT` (13.7%) | `polar_protic_alcohol` (1.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `CO` (0%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O` (0%) | `O=S([O-])O.[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2795  yield=33.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #1)

```
C=CCCC(=O)O.O=S(O)C(F)(F)F.[Na]>>O=C1CCC(CC(F)(F)F)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (97.9%) | `carbon_generic` (1.1%) | `graphite_rod` (0.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (51.5%) | `platinum` (46.8%) | `carbon` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (71.9%) | `nickel_plate` (22.1%) | `nickel_generic` (4.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (82.7%) | `NBu4` (8.7%) | `Li` (4.5%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (58.0%) | `molecular_no_ion` (25.5%) | `BF4` (10.0%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (36.7%) | `hbr` (4.6%) | `metal_oxide_oxidant` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.1%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (31.6%) | `halogenated_aliphatic` (24.5%) | `polar_protic_alcohol` (17.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (94%) | `O` (63%) | `OC(C(F)(F)F)C(F)(F` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2796  yield=33.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #2)

```
O=S(O)C(F)(F)F.[Na].C=C(CCCCCO)c1ccc(-c2ccccc2)cc1>>FC(F)(F)CC1(c2ccc(-c3ccccc3)cc2)CCCCCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (79.6%) | `graphite_rod` (9.8%) | `carbon_generic` (8.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (53.4%) | `platinum` (38.2%) | `carbon` (8.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_plate` (53.9%) | `platinum_generic` (34.0%) | `platinum_plate` (9.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (75.7%) | `NBu4` (17.2%) | `ABSENT` (3.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `molecular_no_ion` | `molecular_no_ion` (58.2%) | `ClO4` (29.7%) | `BF4` (4.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (39.1%) | `electrophilic_N_F` (1.9%) | `unparseable_text` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (91.9%) | `ABSENT` (7.8%) | `polar_aprotic_amide` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O=S([O-])O.[Na+]` (0%) | `[Br-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #2797  yield=35.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #3)

```
O=C(O)CC=C(c1ccccc1)c1ccccc1.O=S(O)C(F)F.[Na]>>O=C1CC(C(F)F)C(c2ccccc2)(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (64.7%) | `graphite_plate` (23.2%) | `carbon_rod` (5.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.9%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (79.9%) | `platinum_plate` (20.0%) | `graphite_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (46.0%) | `Li` (26.5%) | `Na` (23.7%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (86.6%) | `PF6` (5.4%) | `BF4` (4.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (29.3%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.4%) | `triarylamine_radical_cat` (2.7%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.6%) | `aqueous` (0.1%) | `polar_protic_alcohol` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (100%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2798  yield=34.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #4)

```
O=S(O)C(F)(F)F.[Na].C=C(c1ccc(C)cc1)c1ccccc1CO>>Cc1ccc(C2(CC(F)(F)F)OCc3ccccc32)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `nickel` | `carbon` (98.4%) | `platinum` (1.6%) | `nickel` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `nickel_generic` | `carbon_rod` (42.4%) | `graphite_generic` (25.3%) | `carbon_generic` (17.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `nickel` (81.2%) | `platinum` (17.9%) | `carbon` (0.7%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `nickel_plate` (90.6%) | `platinum_plate` (4.9%) | `platinum_generic` (1.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (55.8%) | `NBu4` (30.5%) | `ABSENT` (10.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (59.8%) | `BF4` (23.1%) | `ABSENT` (7.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (12.1%) | `water` (6.5%) | `electrophilic_N_F` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.7%) | `polar_protic_alcohol` (0.6%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (99%) | `O` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2799  yield=35.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #5)

```
O=S(O)C(F)(F)F.[Na].C=C(CCCO)c1cccc([N+](=O)[O-])c1>>O=[N+]([O-])c1cccc(C2(CC(F)(F)F)CCCO2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `nickel` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✗ |
| 阳极 (细类) | 43 | `nickel_generic` | `graphite_generic` (99.6%) | `graphite_rod` (0.1%) | `graphite_felt` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `nickel` (51.2%) | `platinum` (34.1%) | `carbon` (14.0%) | ✓ |
| 阴极 (细类) | 49 | `graphite_generic` | `platinum_generic` (54.8%) | `nickel_plate` (32.0%) | `graphite_generic` (9.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (82.6%) | `NEt4` (10.8%) | `NBu4` (5.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `molecular_no_ion` | `ClO4` (61.3%) | `molecular_no_ion` (33.5%) | `BF4` (2.0%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (42.8%) | `electrophilic_N_F` (1.7%) | `unparseable_text` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (88.6%) | `ABSENT` (8.8%) | `halogenated_aliphatic` (1.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `Cc1cc(O[C@@H](C)C(` (0%) | set ✓ / any ✓ |

---

### Reaction #2800  yield=42.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #6)

```
C=C(CCC(=O)O)c1ccc(F)cc1.CC(F)(F)S(=O)O.[Na]>>CC(F)(F)CC1(c2ccc(F)cc2)CCC(=O)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (100.0%) | `graphite_rod` (0.0%) | `carbon_plate` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.2%) | `carbon` (0.5%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (98.7%) | `Na` (0.8%) | `K` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (79.2%) | `molecular_no_ion` (16.0%) | `OTf` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (36.9%) | `ammonia` (2.8%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ionic_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.6%) | `cyclic_ether` (0.6%) | `aqueous` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `O` (99%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `[Cl-].[Cl-].[Mg+2]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2801  yield=47.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #7)

```
O=S(O)C(F)(F)F.[Na].C=C(CCCC(=O)O)c1ccc(Cl)cc1>>O=C1CCCC(CC(F)(F)F)(c2ccc(Cl)cc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.1%) | `platinum` (5.9%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (57.7%) | `carbon_generic` (18.1%) | `graphite_generic` (13.0%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (67.8%) | `nickel` (31.3%) | `carbon` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_plate` (64.2%) | `platinum_generic` (24.6%) | `platinum_plate` (10.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (74.5%) | `Li` (10.0%) | `Na` (7.8%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (70.5%) | `molecular_no_ion` (8.9%) | `ClO4` (8.2%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.2%) | `ferrocene_mediator` (2.1%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `main_group_lewis_acid` (0.1%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.0%) | `polar_protic_alcohol` (13.2%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `CO` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `[Br-].[Na+]` (0%) | `BrC(Br)(Br)Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #2802  yield=50.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #8)

```
O=S(O)C(F)(F)F.[Na].O=C(O)CC/C=C/c1ccccc1>>O=C1CCC(C(F)(F)F)C(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.7%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (93.5%) | `graphite_generic` (5.1%) | `carbon_rod` (0.4%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.6%) | `carbon` (0.7%) | `nickel` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (86.3%) | `platinum_plate` (13.0%) | `nickel_plate` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (67.1%) | `NBu4` (15.7%) | `Li` (11.7%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (64.1%) | `BF4` (14.5%) | `ClO4` (7.4%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (23.6%) | `hbr` (2.8%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `brønsted_acid_cat` (0.0%) | `Ni_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `halogenated_aliphatic` (9.3%) | `ABSENT` (5.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (95%) | `O` (70%) | `ClCCl` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (1%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `Cc1cc(O[C@@H](C)C(` (0%) | set ✓ / any ✓ |

---

### Reaction #2803  yield=50.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #9)

```
O=S(O)C(F)(F)F.[Na].Cc1ccc(/C=C/CC(=O)O)cc1>>Cc1ccc(C2OC(=O)CC2C(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (73.1%) | `graphite_rod` (23.3%) | `graphite_plate` (1.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (76.0%) | `nickel` (22.5%) | `carbon` (1.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_plate` (45.0%) | `platinum_generic` (40.4%) | `platinum_plate` (12.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (85.5%) | `NBu4` (7.5%) | `Na` (4.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (60.1%) | `ClO4` (28.1%) | `BF4` (6.0%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (35.3%) | `metal_oxide_oxidant` (1.8%) | `tellurium_reagent` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.3%) | `ionic_organocat` (0.7%) | `pyridine_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `cyclic_ether` (0.5%) | `polar_protic_alcohol` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2804  yield=50.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #10)

```
O=S(O)C(F)(F)F.[Na].C=C(CCCC(=O)O)c1ccccc1>>O=C1CCCC(CC(F)(F)F)(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (83.6%) | `platinum` (16.1%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (50.2%) | `platinum_generic` (15.8%) | `carbon_rod` (10.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (80.4%) | `nickel` (16.8%) | `carbon` (2.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (73.8%) | `nickel_plate` (13.6%) | `platinum_plate` (11.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (64.4%) | `Li` (34.0%) | `NEt4` (0.5%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (79.1%) | `ClO4` (13.4%) | `molecular_no_ion` (5.8%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (33.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `main_group_lewis_acid` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.3%) | `polar_protic_alcohol` (1.2%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (1%) | `CO` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2805  yield=52.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #11)

```
O=S(O)C(F)(F)F.[Na].C=C(CCC(=O)O)c1ccc(OC)cc1>>COc1ccc(C2(CC(F)(F)F)CCC(=O)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (85.8%) | `platinum` (14.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (71.1%) | `platinum_plate` (10.6%) | `graphite_rod` (9.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (70.6%) | `nickel` (26.8%) | `carbon` (2.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (74.5%) | `nickel_plate` (17.2%) | `platinum_generic` (7.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (44.2%) | `NBu4` (25.4%) | `Li` (22.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (34.1%) | `PF6` (25.6%) | `ClO4` (14.4%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (22.0%) | `electrophilic_N_F` (2.2%) | `unparseable_text` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `main_group_lewis_acid` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.3%) | `ABSENT` (6.0%) | `polar_protic_alcohol` (2.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (20%) | `CO` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2806  yield=60.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #12)

```
O=S(O)C(F)(F)F.[Na].C=C(CCCO)c1ccc(C)cc1>>Cc1ccc(C2(CC(F)(F)F)CCCO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (52.4%) | `graphite_rod` (40.7%) | `graphite_felt` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (96.9%) | `platinum` (2.5%) | `carbon` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_plate` (98.2%) | `nickel_generic` (1.3%) | `platinum_generic` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (53.8%) | `Li` (18.8%) | `NEt4` (17.9%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (55.3%) | `molecular_no_ion` (16.8%) | `PF6` (7.8%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (35.5%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `main_group_lewis_acid` (0.1%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (62.3%) | `ABSENT` (27.6%) | `polar_protic_alcohol` (3.3%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `CO` (1%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `[Br-].[Na+]` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2807  yield=60.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #13)

```
O=S(O)C(F)(F)F.[Na].C=C(CC1(CC(=O)O)CCCC1)c1ccccc1>>O=C1CC2(CCCC2)CC(CC(F)(F)F)(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.4%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (93.9%) | `carbon_generic` (5.7%) | `graphite_felt` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (64.8%) | `nickel` (25.4%) | `carbon` (9.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (94.9%) | `graphite_generic` (1.8%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (83.4%) | `ABSENT` (7.0%) | `NBu4` (6.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (58.9%) | `ClO4` (27.9%) | `ABSENT` (5.8%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (44.6%) | `metal_oxide_oxidant` (1.6%) | `tellurium_reagent` (1.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (96.8%) | `halogenated_aliphatic` (1.4%) | `ketone` (0.4%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (98%) | `O` (50%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2808  yield=51.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #14)

```
O=C(O)C/C=C/c1ccccc1.O=S(O)C(F)(F)F.[Na]>>O=C1CC(C(F)(F)F)C(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `platinum` (2.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (89.8%) | `graphite_rod` (9.3%) | `graphite_plate` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (88.4%) | `nickel` (9.5%) | `carbon` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_generic` (96.5%) | `nickel_plate` (1.7%) | `platinum_plate` (1.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (48.9%) | `ABSENT` (30.4%) | `NBu4` (12.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (39.3%) | `molecular_no_ion` (22.0%) | `ClO4` (16.7%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (39.4%) | `metal_oxide_oxidant` (1.7%) | `tellurium_reagent` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `pyridine_organocat` (0.6%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.9%) | `ABSENT` (1.2%) | `cyclic_ether` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (1%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2809  yield=51.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #15)

```
O=S(O)C(F)(F)F.[Na].OCCC=C(c1ccccc1)c1ccccc1>>FC(F)(F)C1CCOC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_cloth` (26.4%) | `reticulated_vitreous_carbon` (23.7%) | `graphite_rod` (20.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.1%) | `carbon` (1.6%) | `nickel` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `nickel_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (60.1%) | `NEt4` (26.9%) | `NBu4` (7.9%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `PF6` (71.7%) | `ABSENT` (22.8%) | `ClO4` (2.7%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (20.4%) | `bromide_anion` (3.2%) | `carboxylic_acid` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (61.7%) | `triarylamine_radical_cat` (31.1%) | `pyridine_organocat` (4.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.1%) | `ketone` (0.6%) | `halogenated_aliphatic` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (25%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (99%) | `CC(C)C(=O)O` (0%) | `[Cl-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])c1ccccc1-` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #2810  yield=53.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #16)

```
O=S(O)C(F)(F)F.[Na].C=C(CCC(=O)O)c1ccc(C)cc1>>Cc1ccc(C2(CC(F)F)CCC(=O)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (85.6%) | `carbon` (14.4%) | `nickel` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_generic` | `platinum_plate` (54.7%) | `platinum_generic` (34.7%) | `graphite_rod` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (93.2%) | `nickel` (6.3%) | `carbon` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (56.5%) | `nickel_plate` (28.9%) | `platinum_generic` (14.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Na` (46.9%) | `Li` (37.4%) | `ABSENT` (12.5%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (67.4%) | `ABSENT` (13.6%) | `OTf` (7.8%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `carboxylic_acid` (17.1%) | `ABSENT` (11.3%) | `polyhalo_radical_transfer` (5.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.4%) | `main_group_lewis_acid` (1.2%) | `Co_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (89.9%) | `polar_protic_alcohol` (4.3%) | `ABSENT` (4.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (49%) | `CO` (26%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `CC(=O)O` (36%) | `O=C(O)C(F)(F)F` (10%) | `[Cl-].[Cl-].[Mg+2]` (8%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `CCCC[N+](CCCC)(CCC` (3%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #2811  yield=52.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #17)

```
O=S(O)C(F)(F)F.[Na].C=C(CCCO)c1ccc(-c2ccccc2)cc1>>FC(F)(F)CC1(c2ccc(-c3ccccc3)cc2)CCCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (62.9%) | `graphite_rod` (28.9%) | `carbon_generic` (4.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (79.7%) | `platinum` (18.8%) | `carbon` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_plate` (56.8%) | `platinum_generic` (29.0%) | `platinum_plate` (11.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (59.1%) | `Li` (21.4%) | `NEt4` (12.6%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (27.1%) | `molecular_no_ion` (25.1%) | `ClO4` (14.5%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (33.1%) | `electrophilic_N_F` (2.0%) | `unparseable_text` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (85.6%) | `ABSENT` (11.2%) | `polar_aprotic_amide` (2.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `CN(C)C=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O=S([O-])O.[Na+]` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2812  yield=63.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #18)

```
O=S(O)C(F)(F)F.[Na].O=C(O)CC=C(c1ccccc1)c1ccccc1>>O=C1CC(C(F)(F)F)C(c2ccccc2)(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (99.0%) | `platinum` (1.0%) | `nickel` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_generic` | `graphite_generic` (36.1%) | `reticulated_vitreous_carbon` (31.1%) | `graphite_rod` (14.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.0%) | `nickel` (0.6%) | `carbon` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (80.9%) | `platinum_generic` (18.7%) | `nickel_plate` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (61.5%) | `NEt4` (16.7%) | `Na` (11.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (87.7%) | `PF6` (5.7%) | `molecular_no_ion` (3.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (35.8%) | `metal_oxide_oxidant` (1.8%) | `tellurium_reagent` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `triarylamine_radical_cat` (2.3%) | `pyridine_organocat` (1.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.4%) | `ketone` (0.2%) | `aqueous` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (54%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `O=C([O-])c1ccccc1-` (0%) | set ✓ / any ✓ |

---

### Reaction #2813  yield=80.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #19)

```
O=S(O)C(F)(F)F.[Na].C=C(CCC(=O)O)c1ccccc1>>O=C1CCC(CC(F)(F)F)(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.1%) | `platinum` (15.8%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (46.7%) | `platinum_plate` (31.6%) | `graphite_rod` (14.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (71.3%) | `nickel` (25.5%) | `carbon` (3.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (92.7%) | `nickel_plate` (6.3%) | `platinum_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (78.7%) | `NBu4` (10.6%) | `ABSENT` (3.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (74.9%) | `PF6` (14.4%) | `BF4` (5.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (44.6%) | `electrophilic_N_F` (1.6%) | `unparseable_text` (1.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (93.5%) | `cyclic_ether` (2.1%) | `aqueous` (1.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (87%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O=S([O-])O.[Na+]` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2814  yield=72.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #20)

```
O=S(O)C(F)(F)F.[Na].C=C(CC(C)(C)CC(=O)O)c1ccccc1>>CC1(C)CC(=O)OC(CC(F)(F)F)(c2ccccc2)C1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.7%) | `platinum` (17.7%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (92.5%) | `graphite_rod` (3.3%) | `platinum_generic` (1.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (95.8%) | `platinum` (4.1%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_plate` (94.7%) | `nickel_foam` (2.2%) | `platinum_generic` (1.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (44.3%) | `NBu4` (28.0%) | `Li` (21.1%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (46.6%) | `BF4` (16.9%) | `ClO4` (14.1%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (25.3%) | `water` (5.1%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (80.1%) | `ABSENT` (7.2%) | `halogenated_aliphatic` (3.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (84%) | `O` (62%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2815  yield=73.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #21)

```
O=S(O)C(F)(F)F.[Na].C=C(CCC(=O)O)c1ccc(F)cc1>>O=C1CCC(CC(F)(F)F)(c2ccc(F)cc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (83.9%) | `platinum` (15.8%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (58.8%) | `platinum_plate` (19.8%) | `graphite_rod` (18.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (86.0%) | `nickel` (12.1%) | `carbon` (1.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (83.4%) | `nickel_plate` (14.2%) | `platinum_generic` (2.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (39.6%) | `Na` (28.6%) | `Li` (22.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (40.4%) | `molecular_no_ion` (20.3%) | `ClO4` (19.2%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (32.9%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `main_group_lewis_acid` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (78.0%) | `ABSENT` (15.4%) | `polar_protic_alcohol` (3.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (15%) | `CO` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O` (0%) | `BrC(Br)(Br)Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2816  yield=87.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #22)

```
O=S(O)C(F)(F)F.[Na].C=C(CCC(=O)O)c1ccc(-c2ccccc2)cc1>>O=C1CCC(CC(F)(F)F)(c2ccc(-c3ccccc3)cc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.6%) | `platinum` (9.3%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (46.6%) | `platinum_plate` (21.6%) | `graphite_rod` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (89.5%) | `nickel` (10.0%) | `carbon` (0.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (91.5%) | `platinum_generic` (5.8%) | `nickel_plate` (2.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (62.1%) | `ABSENT` (29.1%) | `Na` (4.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (35.7%) | `ABSENT` (34.7%) | `ClO4` (20.7%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (22.6%) | `electrophilic_N_F` (2.3%) | `unparseable_text` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `pyridine_organocat` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (68.1%) | `ABSENT` (30.7%) | `polar_protic_alcohol` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (3%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2817  yield=85.0%

**Source paper**: [`RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json`](reactions_by_journal_alkene_ec_audited/RSCAdv/2025_RSC_Advances_2025_15_19_15302-15309.json) (反应 idx 在该 JSON 内 = #23)

```
O=S(O)C(F)(F)F.[Na].C=C(CCC(=O)O)c1ccc(C)cc1>>Cc1ccc(C2(CC(F)(F)F)CCC(=O)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (82.9%) | `platinum` (17.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (38.1%) | `carbon_rod` (26.4%) | `platinum_plate` (17.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (54.5%) | `platinum` (45.0%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_plate` (88.3%) | `platinum_plate` (9.3%) | `platinum_generic` (2.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (60.0%) | `ABSENT` (29.7%) | `Na` (6.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (51.0%) | `ABSENT` (25.8%) | `ClO4` (15.9%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (26.0%) | `borohydride` (2.0%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.5%) | `main_group_lewis_acid` (1.1%) | `pyridine_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (83.4%) | `ABSENT` (10.0%) | `polar_protic_alcohol` (4.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `CO` (7%) | `O` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (100%) | `[Br-].[Na+]` (0%) | `BrC(Br)(Br)Br` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2818  yield=10.0%

**Source paper**: [`Reaction/2025_Reaction_Chemistry_Engineering_2025_10_7_1455-1460.json`](reactions_by_journal_alkene_ec_audited/Reaction/2025_Reaction_Chemistry_Engineering_2025_10_7_1455-1460.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.O=C=O>>O=C(O)CC(C(=O)O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (96.0%) | `sacrificial_zinc` (3.4%) | `sacrificial_aluminum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `aluminum_generic` | `magnesium_generic` (99.7%) | `magnesium_plate` (0.2%) | `zinc_generic` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `titanium` (98.6%) | `copper` (0.9%) | `stainless_steel` (0.3%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `titanium_generic` (100.0%) | `stainless_steel_generic` (0.0%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (98.9%) | `undivided` (0.6%) | `divided` (0.4%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NEt4` (98.7%) | `NBu4` (0.6%) | `Li` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `F` | `Br` (97.9%) | `Cl` (1.1%) | `BF4` (0.2%) | ✗ |
| 试剂大类 | 103 | `hcl` | `ABSENT` (20.3%) | `hcl` (6.7%) | `ester` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `polycyclic_arene_cat` (0.2%) | `Ni_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (89.1%) | `polar_aprotic_amide` (9.8%) | `aqueous` (0.3%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CN(C)C=O` (99%) | `O` (99%) | `CC#N` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cl` | `Cl` (100%) | `O` (0%) | `OB(O)B(O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__OTHER__` + `[Br-][Ni+2]1([Br-]` | `[Br-][Ni+2]1([Br-]` (100%) | `__OTHER__` (99%) | `c1ccncc1` (1%) | set ✓ / any ✓ |

---

### Reaction #2819  yield=10.0%

**Source paper**: [`Reaction/2025_Reaction_Chemistry_Engineering_2025_10_7_1455-1460.json`](reactions_by_journal_alkene_ec_audited/Reaction/2025_Reaction_Chemistry_Engineering_2025_10_7_1455-1460.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.O=C=O>>O=C(O)CC(C(=O)O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (96.0%) | `sacrificial_zinc` (3.4%) | `sacrificial_aluminum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `aluminum_generic` | `magnesium_generic` (99.7%) | `magnesium_plate` (0.2%) | `zinc_generic` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `titanium` (98.6%) | `copper` (0.9%) | `stainless_steel` (0.3%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `titanium_generic` (100.0%) | `stainless_steel_generic` (0.0%) | `unknown_electrode` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (98.9%) | `undivided` (0.6%) | `divided` (0.4%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (98.7%) | `NBu4` (0.6%) | `Li` (0.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Br` (97.9%) | `Cl` (1.1%) | `BF4` (0.2%) | ✗ |
| 试剂大类 | 103 | `hcl` | `ABSENT` (20.3%) | `hcl` (6.7%) | `ester` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `polycyclic_arene_cat` (0.2%) | `Ni_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (89.1%) | `polar_aprotic_amide` (9.8%) | `aqueous` (0.3%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CN(C)C=O` (99%) | `O` (99%) | `CC#N` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cl` | `Cl` (100%) | `O` (0%) | `OB(O)B(O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__OTHER__` + `[Br-][Ni+2]1([Br-]` | `[Br-][Ni+2]1([Br-]` (100%) | `__OTHER__` (99%) | `c1ccncc1` (1%) | set ✓ / any ✓ |

---

### Reaction #2820  yield=20.0%

**Source paper**: [`Russian/2025_Russian_Journal_of_Organic_Chemistry_2025_61_6_1056-1065.json`](reactions_by_journal_alkene_ec_audited/Russian/2025_Russian_Journal_of_Organic_Chemistry_2025_61_6_1056-1065.json) (反应 idx 在该 JSON 内 = #0)

```
C=CC(=O)OCC.CC(C)Cc1ccc(C=NO)cc1>>CCOC(=O)C1CC(Cc2ccc(CC(C)C)cc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (100.0%) | `carbon_generic` (0.0%) | `glassy_carbon` (0.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `stainless_steel` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `glassy_carbon` | `stainless_steel_generic` (100.0%) | `graphite_generic` (0.0%) | `nickel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (76.0%) | `ABSENT` (23.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (98.7%) | `NBu4` (1.1%) | `Li` (0.1%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Cl` (98.4%) | `BF4` (0.7%) | `Br` (0.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `cf3_source` (67.7%) | `electrophilic_N_F` (0.9%) | `unparseable_text` (0.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.1%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (93.9%) | `polar_aprotic_sulfoxide` (2.4%) | `cyclic_ether` (1.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (0%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `Ic1ccccc1` | `OC(C(F)(F)F)C(F)(F` (100%) | `O=C([O-])[O-].[K+]` (0%) | `[Br-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2821  yield=29.0%

**Source paper**: [`Russian/2025_Russian_Journal_of_Organic_Chemistry_2025_61_6_1056-1065.json`](reactions_by_journal_alkene_ec_audited/Russian/2025_Russian_Journal_of_Organic_Chemistry_2025_61_6_1056-1065.json) (反应 idx 在该 JSON 内 = #1)

```
C=CC(=O)OCC.CC(C)CC=NO>>CCOC(=O)C1CC(CC(C)C)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `sacrificial_zinc` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (97.6%) | `unknown_electrode` (0.7%) | `carbon_generic` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `stainless_steel` (88.7%) | `carbon` (8.3%) | `platinum` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `glassy_carbon` | `stainless_steel_generic` (98.6%) | `unknown_electrode` (1.1%) | `graphite_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.9%) | `ABSENT` (13.0%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (51.8%) | `Li` (26.1%) | `NBu4` (10.2%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Cl` (97.4%) | `Br` (1.3%) | `I` (0.7%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `alkali_other_salt` (9.3%) | `alkali_sulfonate` (6.4%) | `cf3_source` (5.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.2%) | `organic_neutral_cat` (0.8%) | `Co_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.3%) | `polar_aprotic_sulfoxide` (2.8%) | `cyclic_ether` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (17%) | `[H+].[OH-]` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `Ic1ccccc1` | `Cl` (40%) | `OC(C(F)(F)F)C(F)(F` (24%) | `O=C(O)O.[Na]` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2822  yield=25.0%

**Source paper**: [`Russian/2025_Russian_Journal_of_Organic_Chemistry_2025_61_6_1056-1065.json`](reactions_by_journal_alkene_ec_audited/Russian/2025_Russian_Journal_of_Organic_Chemistry_2025_61_6_1056-1065.json) (反应 idx 在该 JSON 内 = #2)

```
C=CC(=O)OCC.O=C(C=NO)c1ccccc1>>CCOC(=O)C1CC(C(=O)c2ccccc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (99.7%) | `unknown_electrode` (0.2%) | `boron_doped_diamond` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `stainless_steel` (80.6%) | `carbon` (16.9%) | `platinum` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `glassy_carbon` | `stainless_steel_generic` (95.4%) | `graphite_generic` (1.8%) | `boron_doped_diamond` (1.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (82.7%) | `ABSENT` (10.6%) | `Li` (2.3%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `I` (43.9%) | `Cl` (39.5%) | `molecular_no_ion` (11.0%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (14.6%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `Co_complex` (0.2%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (87.9%) | `aqueous` (3.2%) | `ester` (2.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (96%) | `O` (89%) | `[H+].[OH-]` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `Ic1ccccc1` | `__ABSENT__` (100%) | `O=S([O-])([O-])=S.` (0%) | `[Br-].[H+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #2823  yield=21.0%

**Source paper**: [`Russian/2025_Russian_Journal_of_Organic_Chemistry_2025_61_6_1056-1065.json`](reactions_by_journal_alkene_ec_audited/Russian/2025_Russian_Journal_of_Organic_Chemistry_2025_61_6_1056-1065.json) (反应 idx 在该 JSON 内 = #3)

```
C=CC#N.ON=Cc1ccc(Cl)cc1>>N#CC1CC(c2ccc(Cl)cc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `stainless_steel` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (100.0%) | `graphite_felt` (0.0%) | `carbon_cloth` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `stainless_steel` (100.0%) | `carbon` (0.0%) | `platinum` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `glassy_carbon` | `stainless_steel_generic` (100.0%) | `graphite_generic` (0.0%) | `platinum_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.3%) | `ABSENT` (1.2%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (99.2%) | `NBu4` (0.3%) | `Li` (0.2%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Cl` (98.4%) | `Br` (1.2%) | `BF4` (0.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `cf3_source` (64.1%) | `ABSENT` (1.8%) | `water` (1.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `ionic_organocat` (0.2%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.9%) | `cyclic_ether` (0.4%) | `ketone` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (4%) | `ClCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `Ic1ccccc1` | `OC(C(F)(F)F)C(F)(F` (100%) | `O` (1%) | `[Br-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Na+]` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |

---

### Reaction #2824  yield=40.0%

**Source paper**: [`Russian/2025_Russian_Journal_of_Organic_Chemistry_2025_61_6_1056-1065.json`](reactions_by_journal_alkene_ec_audited/Russian/2025_Russian_Journal_of_Organic_Chemistry_2025_61_6_1056-1065.json) (反应 idx 在该 JSON 内 = #4)

```
C=CC(=O)OCC.ON=Cc1ccc(Cl)cc1Cl>>CCOC(=O)C1CC(c2ccc(Cl)cc2Cl)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (99.9%) | `graphite_plate` (0.1%) | `carbon_felt` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `stainless_steel` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `glassy_carbon` | `stainless_steel_generic` (100.0%) | `graphite_generic` (0.0%) | `platinum_plate` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (87.3%) | `NBu4` (8.7%) | `Li` (1.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Cl` (90.7%) | `Br` (2.5%) | `BF4` (2.0%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `cf3_source` (8.8%) | `ABSENT` (8.6%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.1%) | `cyclic_ether` (1.0%) | `polar_aprotic_sulfoxide` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (7%) | `ClCCl` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `Ic1ccccc1` | `OC(C(F)(F)F)C(F)(F` (99%) | `__ABSENT__` (1%) | `[Br-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |

---

### Reaction #2825  yield=34.0%

**Source paper**: [`Russian/2025_Russian_Journal_of_Organic_Chemistry_2025_61_6_1056-1065.json`](reactions_by_journal_alkene_ec_audited/Russian/2025_Russian_Journal_of_Organic_Chemistry_2025_61_6_1056-1065.json) (反应 idx 在该 JSON 内 = #5)

```
C=CC(=O)OCC.CC(C)(C)CC=NO>>CCOC(=O)C1CC(CC(C)(C)C)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.1%) | `sacrificial_zinc` (0.7%) | `sacrificial_iron` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (99.5%) | `graphite_rod` (0.2%) | `glassy_carbon` (0.1%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `stainless_steel` (98.2%) | `nickel` (0.9%) | `carbon` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `glassy_carbon` | `stainless_steel_generic` (99.8%) | `nickel_generic` (0.1%) | `graphite_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (89.8%) | `ABSENT` (9.9%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (59.7%) | `NBu4` (35.4%) | `ABSENT` (3.1%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Cl` (95.0%) | `BF4` (3.3%) | `I` (0.9%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `cf3_source` (10.5%) | `ABSENT` (4.2%) | `as_solvent_polar_protic_alcoho` (3.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `Mn_complex` (0.3%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.8%) | `polar_aprotic_sulfoxide` (3.2%) | `polar_aprotic_amide` (3.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `CCCCO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `Ic1ccccc1` | `OC(C(F)(F)F)C(F)(F` (99%) | `Cl` (0%) | `__ABSENT__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2826  yield=48.0%

**Source paper**: [`Russian/2025_Russian_Journal_of_Organic_Chemistry_2025_61_6_1056-1065.json`](reactions_by_journal_alkene_ec_audited/Russian/2025_Russian_Journal_of_Organic_Chemistry_2025_61_6_1056-1065.json) (反应 idx 在该 JSON 内 = #6)

```
C=CC(=O)OCC.ON=Cc1ccc(Cl)cc1>>CCOC(=O)C1CC(c2ccc(Cl)cc2)=NO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `stainless_steel` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (100.0%) | `carbon_generic` (0.0%) | `carbon_cloth` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `stainless_steel` (100.0%) | `carbon` (0.0%) | `platinum` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `glassy_carbon` | `stainless_steel_generic` (100.0%) | `graphite_generic` (0.0%) | `nickel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (76.5%) | `ABSENT` (23.3%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (97.2%) | `NBu4` (1.9%) | `Li` (0.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Cl` (97.7%) | `BF4` (1.3%) | `Br` (0.5%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `cf3_source` (40.9%) | `ABSENT` (2.5%) | `as_solvent_polar_protic_alcoho` (1.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `organic_neutral_cat` (0.3%) | `ionic_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.7%) | `ABSENT` (0.6%) | `cyclic_ether` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `Ic1ccccc1` | `OC(C(F)(F)F)C(F)(F` (100%) | `CCc1ccc(B(O)O)cc1` (1%) | `[Br-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `OC(C(F)(F)F)C(F)(F` (1%) | `[Br-].[Na+]` (0%) | set ✓ / any ✓ |

---

### Reaction #2827  yield=0.5%

**Source paper**: [`Synthesis/10.1055_a-2508-9744_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Synthesis/10.1055_a-2508-9744_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.OB(O)c1ccccc1>>C1OC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (89.1%) | `platinum` (5.6%) | `ABSENT` (5.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `glassy_carbon` (56.5%) | `carbon_generic` (39.1%) | `unknown_electrode` (1.7%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.5%) | `stainless_steel` (8.7%) | `ABSENT` (4.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (73.8%) | `platinum_generic` (12.6%) | `stainless_steel_generic` (8.9%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (50.5%) | `undivided` (49.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `molecular_no_ion` | `K` (93.1%) | `NBu4` (2.7%) | `NEt4` (1.8%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `Br` (74.0%) | `PF6` (10.3%) | `BF4` (5.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (11.1%) | `alkali_sulfinate` (6.4%) | `alkali_hydroxide` (5.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (41.2%) | `ABSENT` (21.8%) | `organic_neutral_cat` (14.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.6%) | `polar_aprotic_sulfoxide` (21.9%) | `aqueous` (9.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `O` | `O` (97%) | `CC#N` (77%) | `C1COCCO1` (21%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Mg+2].[O-][Cl+3](` + `O=C([O-])[O-].[K+]` | `O=O` (90%) | `O` (83%) | `OB(O)B(O)O` (75%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (98%) | `__OTHER__` (93%) | `Cc1cc(C)c(-c2c3ccc` (1%) | set ✗ / any ✗ |

---

### Reaction #2828  yield=0.5%

**Source paper**: [`Synthesis/10.1055_a-2508-9744_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Synthesis/10.1055_a-2508-9744_p3_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccccc1.OB(O)c1ccccc1>>c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (98.3%) | `carbon_plate` (0.8%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.9%) | `carbon` (4.5%) | `stainless_steel` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.4%) | `stainless_steel_generic` (0.4%) | `glassy_carbon` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `K` (99.1%) | `NBu4` (0.4%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Br` (87.1%) | `I` (4.5%) | `PF6` (4.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (33.1%) | `ABSENT` (2.3%) | `bromide_anion` (2.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.8%) | `ionic_organocat` (8.6%) | `organic_neutral_cat` (8.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (93.4%) | `polar_aprotic_sulfoxide` (2.8%) | `cyclic_ether` (2.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Mg+2].[O-][Cl+3](` + `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (67%) | `CC(=O)O` (46%) | `O=C(O)C(F)(F)F` (43%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (77%) | `[Fe+2].c1cc[cH-]c1` (5%) | `Brc1ccc(N(c2ccc(Br` (3%) | set ✓ / any ✓ |

---

### Reaction #2829  yield=67.0%

**Source paper**: [`Synthesis/10.1055_a-2508-9744_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Synthesis/10.1055_a-2508-9744_p3_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccccc1.OB(O)c1ccccc1>>c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (98.3%) | `carbon_plate` (0.8%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.9%) | `carbon` (4.5%) | `stainless_steel` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.4%) | `stainless_steel_generic` (0.4%) | `glassy_carbon` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `K` (99.1%) | `NBu4` (0.4%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Br` (87.1%) | `I` (4.5%) | `PF6` (4.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (33.1%) | `ABSENT` (2.3%) | `bromide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.8%) | `ionic_organocat` (8.6%) | `organic_neutral_cat` (8.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (93.4%) | `polar_aprotic_sulfoxide` (2.8%) | `cyclic_ether` (2.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Mg+2].[O-][Cl+3](` + `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (67%) | `CC(=O)O` (46%) | `O=C(O)C(F)(F)F` (43%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (77%) | `[Fe+2].c1cc[cH-]c1` (5%) | `Brc1ccc(N(c2ccc(Br` (3%) | set ✓ / any ✓ |

---

### Reaction #2830  yield=0.0%

**Source paper**: [`Synthesis/10.1055_a-2508-9744_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Synthesis/10.1055_a-2508-9744_p3_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccccc1.OB(O)c1ccccc1>>c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (98.3%) | `carbon_plate` (0.8%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.9%) | `carbon` (4.5%) | `stainless_steel` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.4%) | `stainless_steel_generic` (0.4%) | `glassy_carbon` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `K` (99.1%) | `NBu4` (0.4%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Br` (87.1%) | `I` (4.5%) | `PF6` (4.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (33.1%) | `ABSENT` (2.3%) | `bromide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.8%) | `ionic_organocat` (8.6%) | `organic_neutral_cat` (8.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (93.4%) | `polar_aprotic_sulfoxide` (2.8%) | `cyclic_ether` (2.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Mg+2].[O-][Cl+3](` + `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (67%) | `CC(=O)O` (46%) | `O=C(O)C(F)(F)F` (43%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (77%) | `[Fe+2].c1cc[cH-]c1` (5%) | `Brc1ccc(N(c2ccc(Br` (3%) | set ✓ / any ✓ |

---

### Reaction #2831  yield=0.5%

**Source paper**: [`Synthesis/10.1055_a-2508-9744_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Synthesis/10.1055_a-2508-9744_p3_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccccc1.OB(O)c1ccccc1>>c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (98.3%) | `carbon_plate` (0.8%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.9%) | `carbon` (4.5%) | `stainless_steel` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.4%) | `stainless_steel_generic` (0.4%) | `glassy_carbon` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `K` (99.1%) | `NBu4` (0.4%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Br` (87.1%) | `I` (4.5%) | `PF6` (4.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (33.1%) | `ABSENT` (2.3%) | `bromide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.8%) | `ionic_organocat` (8.6%) | `organic_neutral_cat` (8.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (93.4%) | `polar_aprotic_sulfoxide` (2.8%) | `cyclic_ether` (2.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Mg+2].[O-][Cl+3](` + `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (67%) | `CC(=O)O` (46%) | `O=C(O)C(F)(F)F` (43%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (77%) | `[Fe+2].c1cc[cH-]c1` (5%) | `Brc1ccc(N(c2ccc(Br` (3%) | set ✓ / any ✓ |

---

### Reaction #2832  yield=11.0%

**Source paper**: [`Synthesis/10.1055_a-2508-9744_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Synthesis/10.1055_a-2508-9744_p3_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccccc1.OB(O)c1ccccc1>>c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (98.3%) | `carbon_plate` (0.8%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.9%) | `carbon` (4.5%) | `stainless_steel` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.4%) | `stainless_steel_generic` (0.4%) | `glassy_carbon` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (99.1%) | `NBu4` (0.4%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (87.1%) | `I` (4.5%) | `PF6` (4.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (33.1%) | `ABSENT` (2.3%) | `bromide_anion` (2.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.8%) | `ionic_organocat` (8.6%) | `organic_neutral_cat` (8.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (93.4%) | `polar_aprotic_sulfoxide` (2.8%) | `cyclic_ether` (2.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Mg+2].[O-][Cl+3](` + `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (67%) | `CC(=O)O` (46%) | `O=C(O)C(F)(F)F` (43%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (77%) | `[Fe+2].c1cc[cH-]c1` (5%) | `Brc1ccc(N(c2ccc(Br` (3%) | set ✓ / any ✓ |

---

### Reaction #2833  yield=62.0%

**Source paper**: [`Synthesis/10.1055_a-2508-9744_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Synthesis/10.1055_a-2508-9744_p3_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccccc1.OB(O)c1ccccc1>>c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (98.3%) | `carbon_plate` (0.8%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.9%) | `carbon` (4.5%) | `stainless_steel` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.4%) | `stainless_steel_generic` (0.4%) | `glassy_carbon` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `K` (99.1%) | `NBu4` (0.4%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Br` (87.1%) | `I` (4.5%) | `PF6` (4.1%) | ✗ |
| 试剂大类 | 103 | `alkaline_earth_salt` | `carboxylic_acid` (33.1%) | `ABSENT` (2.3%) | `bromide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.8%) | `ionic_organocat` (8.6%) | `organic_neutral_cat` (8.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (93.4%) | `polar_aprotic_sulfoxide` (2.8%) | `cyclic_ether` (2.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Mg+2].[O-][Cl+3](` + `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (67%) | `CC(=O)O` (46%) | `O=C(O)C(F)(F)F` (43%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (77%) | `[Fe+2].c1cc[cH-]c1` (5%) | `Brc1ccc(N(c2ccc(Br` (3%) | set ✓ / any ✓ |

---

### Reaction #2834  yield=84.0%

**Source paper**: [`Synthesis/10.1055_a-2508-9744_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Synthesis/10.1055_a-2508-9744_p3_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccccc1.OB(O)c1ccccc1>>c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (98.3%) | `carbon_plate` (0.8%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.9%) | `carbon` (4.5%) | `stainless_steel` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.4%) | `stainless_steel_generic` (0.4%) | `glassy_carbon` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (99.1%) | `NBu4` (0.4%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (87.1%) | `I` (4.5%) | `PF6` (4.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (33.1%) | `ABSENT` (2.3%) | `bromide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.8%) | `ionic_organocat` (8.6%) | `organic_neutral_cat` (8.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (93.4%) | `polar_aprotic_sulfoxide` (2.8%) | `cyclic_ether` (2.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Mg+2].[O-][Cl+3](` + `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (67%) | `CC(=O)O` (46%) | `O=C(O)C(F)(F)F` (43%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (77%) | `[Fe+2].c1cc[cH-]c1` (5%) | `Brc1ccc(N(c2ccc(Br` (3%) | set ✓ / any ✓ |

---

### Reaction #2835  yield=64.0%

**Source paper**: [`Synthesis/10.1055_a-2508-9744_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Synthesis/10.1055_a-2508-9744_p3_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccccc1.OB(O)c1ccccc1>>c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (98.3%) | `carbon_plate` (0.8%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.9%) | `carbon` (4.5%) | `stainless_steel` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.4%) | `stainless_steel_generic` (0.4%) | `glassy_carbon` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (99.1%) | `NBu4` (0.4%) | `Na` (0.2%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Br` (87.1%) | `I` (4.5%) | `PF6` (4.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (33.1%) | `ABSENT` (2.3%) | `bromide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.8%) | `ionic_organocat` (8.6%) | `organic_neutral_cat` (8.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (93.4%) | `polar_aprotic_sulfoxide` (2.8%) | `cyclic_ether` (2.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Mg+2].[O-][Cl+3](` + `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (67%) | `CC(=O)O` (46%) | `O=C(O)C(F)(F)F` (43%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (77%) | `[Fe+2].c1cc[cH-]c1` (5%) | `Brc1ccc(N(c2ccc(Br` (3%) | set ✓ / any ✓ |

---

### Reaction #2836  yield=42.0%

**Source paper**: [`Synthesis/10.1055_a-2508-9744_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Synthesis/10.1055_a-2508-9744_p3_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccccc1.OB(O)c1ccccc1>>c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (98.3%) | `carbon_plate` (0.8%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (87.9%) | `carbon` (4.5%) | `stainless_steel` (3.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.4%) | `stainless_steel_generic` (0.4%) | `glassy_carbon` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (99.1%) | `NBu4` (0.4%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (87.1%) | `I` (4.5%) | `PF6` (4.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (33.1%) | `ABSENT` (2.3%) | `bromide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.8%) | `ionic_organocat` (8.6%) | `organic_neutral_cat` (8.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (93.4%) | `polar_aprotic_sulfoxide` (2.8%) | `cyclic_ether` (2.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Mg+2].[O-][Cl+3](` + `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (67%) | `CC(=O)O` (46%) | `O=C(O)C(F)(F)F` (43%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (77%) | `[Fe+2].c1cc[cH-]c1` (5%) | `Brc1ccc(N(c2ccc(Br` (3%) | set ✓ / any ✓ |

---

### Reaction #2837  yield=57.0%

**Source paper**: [`Synthesis/10.1055_a-2508-9744_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Synthesis/10.1055_a-2508-9744_p3_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccccc1.OB(O)c1ccccc1>>c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (98.3%) | `carbon_plate` (0.8%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.9%) | `carbon` (4.5%) | `stainless_steel` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.4%) | `stainless_steel_generic` (0.4%) | `glassy_carbon` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (99.1%) | `NBu4` (0.4%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (87.1%) | `I` (4.5%) | `PF6` (4.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (33.1%) | `ABSENT` (2.3%) | `bromide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.8%) | `ionic_organocat` (8.6%) | `organic_neutral_cat` (8.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (93.4%) | `polar_aprotic_sulfoxide` (2.8%) | `cyclic_ether` (2.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Mg+2].[O-][Cl+3](` + `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (67%) | `CC(=O)O` (46%) | `O=C(O)C(F)(F)F` (43%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (77%) | `[Fe+2].c1cc[cH-]c1` (5%) | `Brc1ccc(N(c2ccc(Br` (3%) | set ✓ / any ✓ |

---

### Reaction #2838  yield=48.0%

**Source paper**: [`Synthesis/10.1055_a-2508-9744_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Synthesis/10.1055_a-2508-9744_p3_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccccc1.OB(O)c1ccccc1>>c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (98.3%) | `carbon_plate` (0.8%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.9%) | `carbon` (4.5%) | `stainless_steel` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.4%) | `stainless_steel_generic` (0.4%) | `glassy_carbon` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (99.1%) | `NBu4` (0.4%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (87.1%) | `I` (4.5%) | `PF6` (4.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (33.1%) | `ABSENT` (2.3%) | `bromide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.8%) | `ionic_organocat` (8.6%) | `organic_neutral_cat` (8.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (93.4%) | `polar_aprotic_sulfoxide` (2.8%) | `cyclic_ether` (2.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Mg+2].[O-][Cl+3](` + `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (67%) | `CC(=O)O` (46%) | `O=C(O)C(F)(F)F` (43%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (77%) | `[Fe+2].c1cc[cH-]c1` (5%) | `Brc1ccc(N(c2ccc(Br` (3%) | set ✓ / any ✓ |

---

### Reaction #2839  yield=20.0%

**Source paper**: [`Synthesis/10.1055_a-2508-9744_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Synthesis/10.1055_a-2508-9744_p3_t0.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccccc1.OB(O)c1ccccc1>>c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (98.3%) | `carbon_plate` (0.8%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.9%) | `carbon` (4.5%) | `stainless_steel` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.4%) | `stainless_steel_generic` (0.4%) | `glassy_carbon` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (99.1%) | `NBu4` (0.4%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (87.1%) | `I` (4.5%) | `PF6` (4.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (33.1%) | `ABSENT` (2.3%) | `bromide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.8%) | `ionic_organocat` (8.6%) | `organic_neutral_cat` (8.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (93.4%) | `polar_aprotic_sulfoxide` (2.8%) | `cyclic_ether` (2.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Mg+2].[O-][Cl+3](` + `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (67%) | `CC(=O)O` (46%) | `O=C(O)C(F)(F)F` (43%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (77%) | `[Fe+2].c1cc[cH-]c1` (5%) | `Brc1ccc(N(c2ccc(Br` (3%) | set ✓ / any ✓ |

---

### Reaction #2840  yield=6.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #0)

```
OB(O)c1ccccc1.C=Cc1cccnc1>>c1ccc(B2OCC(c3cccnc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_rod` (51.9%) | `glassy_carbon` (45.3%) | `carbon_felt` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.1%) | `carbon` (1.7%) | `stainless_steel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.8%) | `graphite_rod` (0.1%) | `platinum_generic` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (98.1%) | `NBu4` (1.0%) | `Na` (0.7%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (78.3%) | `I` (11.6%) | `PF6` (4.7%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (7.9%) | `bromide_anion` (3.1%) | `alkali_bicarbonate` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.3%) | `ionic_organocat` (1.3%) | `organic_neutral_cat` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.3%) | `cyclic_ether` (0.2%) | `polar_aprotic_sulfoxide` (0.2%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `CC(=O)O` (68%) | `[Cl-].[Na+]` (32%) | `O=C(O)C(F)(F)F` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)NC1CC2(CCCCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2841  yield=17.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #1)

```
OB(O)c1ccccc1.C/C=C/c1ccccc1>>C[C@H]1OB(c2ccccc2)O[C@H]1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.6%) | `platinum` (2.9%) | `sacrificial_iron` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (40.8%) | `carbon_plate` (39.5%) | `carbon_generic` (4.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (54.1%) | `stainless_steel` (20.0%) | `carbon` (18.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (87.5%) | `stainless_steel_generic` (7.6%) | `platinum_mesh` (1.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `divided` (2.3%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (57.5%) | `Na` (23.2%) | `NBu4` (9.3%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (42.7%) | `Cl` (40.3%) | `I` (4.7%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (34.3%) | `boron_lewis_acid` (4.9%) | `as_solvent_polar_aprotic_sulfo` (3.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (71.0%) | `Mn_complex` (11.7%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (50.1%) | `cyclic_ether` (20.1%) | `halogenated_aliphatic` (11.4%) | ✗ |
| 溶剂 set | 79 | `O` | `O` (100%) | `CC#N` (68%) | `CC(=O)OC(C)=O` (25%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (48%) | `O=CO` (46%) | `[Br-].[K+]` (29%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (72%) | `COC(=O)CC[C@@H]1C2` (13%) | `[Cl-][Mn+3]123[N](` (10%) | set ✓ / any ✓ |

---

### Reaction #2842  yield=50.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #2)

```
OB(O)c1ccccc1.C/C=C/c1ccccc1>>C[C@@H]1OB(c2ccccc2)O[C@H]1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.6%) | `platinum` (2.9%) | `sacrificial_iron` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (40.8%) | `carbon_plate` (39.5%) | `carbon_generic` (4.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (54.1%) | `stainless_steel` (20.0%) | `carbon` (18.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (87.5%) | `stainless_steel_generic` (7.6%) | `platinum_mesh` (1.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `divided` (2.3%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (57.5%) | `Na` (23.2%) | `NBu4` (9.3%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (42.7%) | `Cl` (40.3%) | `I` (4.7%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (34.3%) | `boron_lewis_acid` (4.9%) | `as_solvent_polar_aprotic_sulfo` (3.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (71.0%) | `Mn_complex` (11.7%) | `organic_neutral_cat` (9.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (50.1%) | `cyclic_ether` (20.1%) | `halogenated_aliphatic` (11.4%) | ✗ |
| 溶剂 set | 79 | `O` | `O` (100%) | `CC#N` (68%) | `CC(=O)OC(C)=O` (25%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (48%) | `O=CO` (46%) | `[Br-].[K+]` (29%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (72%) | `COC(=O)CC[C@@H]1C2` (13%) | `[Cl-][Mn+3]123[N](` (10%) | set ✓ / any ✓ |

---

### Reaction #2843  yield=52.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #3)

```
OB(O)c1ccccc1.C=Cc1csc2ccccc12>>c1ccc(B2OCC(c3csc4ccccc34)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (99.5%) | `carbon_rod` (0.2%) | `carbon_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.5%) | `stainless_steel` (7.0%) | `nickel` (4.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.7%) | `stainless_steel_generic` (0.9%) | `nickel_plate` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.0%) | `ABSENT` (2.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (98.4%) | `NBu4` (1.2%) | `Li` (0.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Br` (60.9%) | `ClO4` (20.9%) | `BF4` (9.7%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (39.2%) | `ammonia` (1.8%) | `water` (1.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `Mn_complex` (0.4%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (97.9%) | `cyclic_ether` (1.0%) | `polar_aprotic_sulfoxide` (0.5%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (99%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (51%) | `CC(=O)O` (43%) | `[Cl-].[Na+]` (37%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)NC1CC2(CCCCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2844  yield=57.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #4)

```
OB(O)c1ccccc1.C=Cc1ccc(C(=O)OC)cc1>>COC(=O)c1ccc(C2COB(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (81.0%) | `graphite_generic` (14.6%) | `graphite_rod` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.4%) | `carbon` (4.4%) | `nickel` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.0%) | `stainless_steel_generic` (0.4%) | `graphite_generic` (0.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `K` (99.1%) | `NBu4` (0.7%) | `Na` (0.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Br` (85.5%) | `PF6` (6.9%) | `I` (3.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (17.8%) | `ABSENT` (3.3%) | `cyanide` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.1%) | `pyridine_organocat` (1.7%) | `ionic_organocat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.1%) | `cyclic_ether` (0.4%) | `polar_aprotic_sulfoxide` (0.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (97%) | `CCOCC` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `CC(=O)O` (40%) | `[Cl-].[Na+]` (36%) | `O=C(O)C(F)(F)F` (28%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2845  yield=68.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #5)

```
C=Cc1ccccc1.COc1cccc(B(O)O)n1>>COc1cccc(B2OCC(c3ccccc3)O2)n1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_rod` (49.4%) | `graphite_rod` (27.3%) | `carbon_cloth` (12.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.4%) | `stainless_steel` (1.0%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.9%) | `nickel_plate` (0.0%) | `platinum_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (62.6%) | `K` (28.3%) | `ABSENT` (8.4%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (38.9%) | `ABSENT` (25.8%) | `BF4` (24.3%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `alkali_other_salt` (9.1%) | `carboxylic_acid` (6.8%) | `ABSENT` (5.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (77.8%) | `pyridine_organocat` (13.5%) | `ionic_organocat` (3.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.8%) | `polar_aprotic_sulfoxide` (0.1%) | `polar_aprotic_amide` (0.1%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (10%) | `ClCCl` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `CC(=O)O.[Na]` (51%) | `O=C(O)C(F)(F)F` (11%) | `__ABSENT__` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2846  yield=68.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #6)

```
OB(O)c1ccccc1.C=Cc1cccc(Cl)c1>>Clc1cccc(C2COB(c3ccccc3)O2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (57.2%) | `carbon_rod` (40.0%) | `carbon_cloth` (1.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.1%) | `stainless_steel` (0.8%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.9%) | `stainless_steel_generic` (0.0%) | `platinum_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (96.4%) | `ABSENT` (2.0%) | `NBu4` (1.4%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `Br` (39.1%) | `ABSENT` (37.9%) | `PF6` (15.2%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (13.4%) | `alkali_other_salt` (9.3%) | `water` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (77.1%) | `pyridine_organocat` (11.5%) | `organic_neutral_cat` (7.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (98.8%) | `polar_aprotic_sulfoxide` (0.7%) | `cyclic_ether` (0.2%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `O` (100%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (82%) | `[Cl-].[Na+]` (15%) | `[Br-].[K+]` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2847  yield=62.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #7)

```
C=Cc1ccccc1.OB(O)C1CCC1>>c1ccc(C2COB(C3CCC3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `sacrificial_iron` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (49.3%) | `carbon_cloth` (28.5%) | `carbon_rod` (12.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (38.9%) | `carbon` (36.8%) | `nickel` (17.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (88.7%) | `stainless_steel_generic` (5.5%) | `graphite_generic` (2.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.3%) | `ABSENT` (1.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (88.5%) | `ABSENT` (8.3%) | `NBu4` (1.7%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `ABSENT` (49.7%) | `PF6` (24.9%) | `Br` (12.3%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (7.0%) | `ABSENT` (3.9%) | `ammonia` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Mn_complex` (60.8%) | `ABSENT` (31.4%) | `pyridine_organocat` (3.1%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (98.8%) | `cyclic_ether` (0.4%) | `ketone` (0.2%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (99%) | `CCOCC` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `CC[Si](CC)CC` (44%) | `O=C(O)C(F)(F)F` (20%) | `[Cl-].[Na+]` (11%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl][Mn][Cl]` (53%) | `CC(=O)[O-].CC(=O)[` (11%) | `__OTHER__` (9%) | set ✗ / any ✗ |

---

### Reaction #2848  yield=66.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #8)

```
C=Cc1ccccc1.OB(O)C1CCCC1>>c1ccc(C2COB(C3CCCC3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `ABSENT` (0.2%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (56.2%) | `carbon_cloth` (35.2%) | `carbon_rod` (5.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (48.2%) | `carbon` (23.3%) | `nickel` (15.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (85.5%) | `stainless_steel_generic` (11.9%) | `nickel_plate` (0.8%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (97.7%) | `ABSENT` (2.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (76.0%) | `ABSENT` (21.0%) | `NBu4` (1.7%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (73.3%) | `PF6` (14.7%) | `Br` (7.6%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (8.3%) | `alkali_other_salt` (4.4%) | `ABSENT` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (41.0%) | `Mn_complex` (40.1%) | `pyridine_organocat` (11.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (98.8%) | `aqueous` (0.3%) | `polar_aprotic_amide` (0.3%) | ✓ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (99%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `CC[Si](CC)CC` (28%) | `O=C(O)C(F)(F)F` (19%) | `O` (12%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (80%) | `c1ccncc1` (14%) | `__OTHER__` (9%) | set ✓ / any ✓ |

---

### Reaction #2849  yield=61.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #9)

```
OB(O)c1ccccc1.C=C(c1ccc2ccccc2c1)C1CC1>>c1ccc(B2OCC(c3ccc4ccccc4c3)(C3CC3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (88.0%) | `graphite_generic` (5.9%) | `carbon_rod` (5.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.9%) | `stainless_steel` (3.5%) | `carbon` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (93.8%) | `platinum_generic` (4.4%) | `stainless_steel_generic` (0.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (62.3%) | `NBu4` (17.0%) | `NEt4` (16.3%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `carboxylate` (64.9%) | `Br` (17.2%) | `BF4` (11.9%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (11.7%) | `ABSENT` (9.8%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Mn_complex` (0.1%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (97.7%) | `polar_protic_alcohol` (2.1%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (92%) | `ClCCl` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `CC(=O)O` (33%) | `O=C(O)C(F)(F)F` (19%) | `[Br-].[Li+]` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2850  yield=70.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #10)

```
C=Cc1ccccc1.CC(=O)c1ccc(B(O)O)cc1>>CC(=O)c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.6%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (94.0%) | `carbon_cloth` (2.3%) | `carbon_plate` (1.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.8%) | `nickel` (3.7%) | `carbon` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.9%) | `platinum_generic` (0.0%) | `stainless_steel_generic` (0.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (99.7%) | `NBu4` (0.2%) | `Na` (0.0%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (95.7%) | `I` (1.9%) | `PF6` (1.2%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (31.4%) | `ABSENT` (4.2%) | `cyanide` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.6%) | `organic_neutral_cat` (2.5%) | `ionic_organocat` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (93.1%) | `polar_aprotic_sulfoxide` (4.8%) | `polar_aprotic_amide` (0.6%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (98%) | `ClCCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (72%) | `[Cl-].[Na+]` (72%) | `CC(=O)O` (25%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)NC1CC2(CCCCC` (0%) | `[I-].[Li+]` (0%) | set ✓ / any ✓ |

---

### Reaction #2851  yield=80.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #11)

```
OB(O)c1ccccc1.C=Cc1ccc2ccc(OC)cc2c1>>COc1ccc2ccc(C3COB(c4ccccc4)O3)cc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (73.8%) | `carbon_rod` (18.7%) | `graphite_rod` (5.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.6%) | `nickel` (6.6%) | `stainless_steel` (4.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (97.5%) | `stainless_steel_generic` (1.6%) | `nickel_plate` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (99.0%) | `NBu4` (0.9%) | `Na` (0.1%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `Br` (82.8%) | `molecular_no_ion` (5.6%) | `PF6` (5.3%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (4.2%) | `alkali_other_salt` (3.2%) | `ABSENT` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `pyridine_organocat` (0.4%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (96.3%) | `polar_aprotic_sulfoxide` (1.7%) | `cyclic_ether` (1.6%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (89%) | `ClCCl` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (25%) | `__ABSENT__` (9%) | `OC(C(F)(F)F)C(F)(F` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (1%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2852  yield=80.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #12)

```
C=Cc1ccccc1.Cn1ccc2cc(B(O)O)ccc21>>Cn1ccc2cc(B3OCC(c4ccccc4)O3)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (99.4%) | `graphite_rod` (0.4%) | `graphite_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.8%) | `carbon` (1.9%) | `stainless_steel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.0%) | `stainless_steel_generic` (0.8%) | `platinum_generic` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (75.8%) | `ABSENT` (18.0%) | `Na` (4.8%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (75.3%) | `ABSENT` (22.1%) | `Cl` (1.9%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `alkali_other_salt` (16.5%) | `as_solvent_polar_protic_alcoho` (3.1%) | `carboxylic_acid` (3.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (68.8%) | `pyridine_organocat` (10.5%) | `Mn_complex` (8.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (96.4%) | `polar_aprotic_sulfoxide` (1.9%) | `cyclic_ether` (0.6%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (83%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=O` (53%) | `CC[Si](CC)CC` (30%) | `O=C(O)O.[K]` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (71%) | `__OTHER__` (22%) | `[Cl-].[Cl-].[Mn+2]` (3%) | set ✓ / any ✓ |

---

### Reaction #2853  yield=80.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #13)

```
C=Cc1ccccc1.OB(O)c1ccc2c(c1)OCO2>>c1ccc(C2COB(c3ccc4c(c3)OCO4)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `glassy_carbon` (99.9%) | `graphite_rod` (0.1%) | `carbon_cloth` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.9%) | `nickel` (5.4%) | `carbon` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.2%) | `stainless_steel_generic` (0.3%) | `nickel_plate` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (98.4%) | `ABSENT` (1.2%) | `NBu4` (0.3%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (89.9%) | `ABSENT` (9.0%) | `BF4` (0.6%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (32.1%) | `ABSENT` (3.1%) | `cyanide` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.3%) | `pyridine_organocat` (0.7%) | `organic_neutral_cat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (95.1%) | `polar_aprotic_sulfoxide` (4.0%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (66%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (95%) | `[Cl-].[Na+]` (49%) | `[Na][Cl]` (20%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[I-].[Li+]` (0%) | set ✓ / any ✓ |

---

### Reaction #2854  yield=76.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #14)

```
OB(O)c1ccccc1.C=Cc1ccccc1C>>Cc1ccccc1C1COB(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (84.1%) | `carbon_rod` (15.3%) | `carbon_plate` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.1%) | `nickel` (9.7%) | `carbon` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (96.9%) | `nickel_plate` (1.7%) | `stainless_steel_generic` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (99.1%) | `NBu4` (0.8%) | `Li` (0.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Br` (46.4%) | `BF4` (15.2%) | `PF6` (14.3%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (24.2%) | `alkali_other_salt` (2.3%) | `water` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `Mn_complex` (0.3%) | `pyridine_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (98.2%) | `polar_aprotic_sulfoxide` (0.7%) | `cyclic_ether` (0.5%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (96%) | `ClCCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `CC(=O)O` (75%) | `[Cl-].[Na+]` (30%) | `O=C(O)C(F)(F)F` (14%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)NC1CC2(CCCCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2855  yield=79.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #15)

```
OB(O)c1ccccc1.C=Cc1ccc(OC)cc1>>COc1ccc(C2COB(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (99.5%) | `carbon_rod` (0.3%) | `graphite_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (91.4%) | `stainless_steel` (3.0%) | `carbon` (2.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.5%) | `stainless_steel_generic` (1.0%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (99.6%) | `NBu4` (0.2%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `Br` (97.3%) | `BF4` (0.6%) | `molecular_no_ion` (0.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (16.0%) | `ABSENT` (4.3%) | `water` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.2%) | `ionic_organocat` (0.7%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (93.2%) | `cyclic_ether` (3.7%) | `polar_aprotic_sulfoxide` (2.5%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (99%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (46%) | `OC(C(F)(F)F)C(F)(F` (28%) | `[Na][Cl]` (18%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (75%) | `[Fe+2].c1cc[cH-]c1` (17%) | `CC(=O)NC1CC2(CCCCC` (8%) | set ✓ / any ✓ |

---

### Reaction #2856  yield=79.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #16)

```
C=Cc1ccccc1.OB(O)c1ccc(OC(F)(F)F)cc1>>FC(F)(F)Oc1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (94.0%) | `graphite_rod` (3.3%) | `carbon_rod` (0.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.2%) | `nickel` (0.8%) | `carbon` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.9%) | `stainless_steel_generic` (0.1%) | `platinum_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (85.9%) | `ABSENT` (12.1%) | `NBu4` (1.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `Br` (58.4%) | `ABSENT` (37.7%) | `PF6` (2.0%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (19.4%) | `alkali_other_salt` (12.0%) | `ABSENT` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (81.6%) | `pyridine_organocat` (13.8%) | `organic_neutral_cat` (2.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.4%) | `polar_aprotic_sulfoxide` (0.2%) | `cyclic_ether` (0.2%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (70%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `CC(=O)O` (73%) | `[Cl-].[Na+]` (14%) | `O=C(O)C(F)(F)F` (13%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `__OTHER__` (1%) | `[I-].[Li+]` (0%) | set ✓ / any ✓ |

---

### Reaction #2857  yield=79.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #17)

```
C=Cc1ccccc1.OB(O)C1=CCCCC1>>C1=C(B2OCC(c3ccccc3)O2)CCCC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (97.8%) | `carbon_cloth` (1.0%) | `graphite_generic` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (75.6%) | `stainless_steel` (11.4%) | `carbon` (10.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (80.8%) | `stainless_steel_generic` (17.6%) | `platinum_generic` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (81.8%) | `NBu4` (16.3%) | `NEt4` (1.0%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `Br` (56.6%) | `PF6` (20.4%) | `BF4` (14.4%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `carboxylic_acid` (19.1%) | `alkali_other_salt` (2.4%) | `metal_oxide_oxidant` (1.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (88.6%) | `organic_neutral_cat` (4.7%) | `ionic_organocat` (2.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (98.3%) | `polar_aprotic_sulfoxide` (1.2%) | `cyclic_ether` (0.2%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (74%) | `C[N+](=O)[O-]` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)O.[K]` | `CC(=O)O` (42%) | `O=C(O)C(F)(F)F` (36%) | `[Br-].[K+]` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (94%) | `c1ccncc1` (5%) | `__OTHER__` (3%) | set ✓ / any ✓ |

---

### Reaction #2858  yield=73.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccccc1.O=Cc1ccc(B(O)O)cc1>>O=Cc1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (44.2%) | `graphite_rod` (22.0%) | `carbon_rod` (16.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (64.0%) | `platinum` (29.7%) | `carbon` (3.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (87.9%) | `nickel_plate` (9.4%) | `stainless_steel_generic` (1.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (95.7%) | `NBu4` (3.0%) | `Li` (0.7%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Br` (78.2%) | `BF4` (9.4%) | `PF6` (6.9%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (8.7%) | `ABSENT` (4.0%) | `alkali_sulfinate` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (81.9%) | `ionic_organocat` (8.0%) | `Mn_complex` (6.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (97.6%) | `cyclic_ether` (0.8%) | `ABSENT` (0.6%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (99%) | `O` (67%) | `CCOCC` (7%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (35%) | `[Cl-].[Na+]` (10%) | `C[Si](C)(C)N=[N+]=` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `[Cl][Mn][Cl]` (2%) | `[Br][Mn][Br]` (0%) | set ✓ / any ✓ |

---

### Reaction #2859  yield=73.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #19)

```
C=Cc1ccccc1.C[Si](C)(C)c1ccc(B(O)O)cc1>>C[Si](C)(C)c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (91.7%) | `carbon_cloth` (3.9%) | `carbon_plate` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (61.9%) | `nickel` (25.4%) | `carbon` (11.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (95.1%) | `nickel_plate` (4.3%) | `stainless_steel_generic` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (97.8%) | `NBu4` (2.0%) | `NH4` (0.1%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (74.0%) | `PF6` (19.2%) | `I` (3.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (24.6%) | `ABSENT` (3.0%) | `alkali_other_salt` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.1%) | `pyridine_organocat` (4.3%) | `organic_neutral_cat` (3.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (98.1%) | `polar_aprotic_sulfoxide` (1.3%) | `cyclic_ether` (0.2%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (73%) | `ClCCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (62%) | `[Cl-].[Na+]` (47%) | `CC(=O)O` (21%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[I-].[Li+]` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2860  yield=78.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #20)

```
OB(O)c1ccccc1.C=Cc1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc(C2COB(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.1%) | `platinum` (1.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (98.5%) | `carbon_rod` (0.5%) | `graphite_generic` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.3%) | `carbon` (5.8%) | `ABSENT` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (95.7%) | `stainless_steel_generic` (2.7%) | `platinum_generic` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (99.7%) | `Na` (0.1%) | `NBu4` (0.1%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (83.3%) | `molecular_no_ion` (5.2%) | `PF6` (3.9%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `carboxylic_acid` (12.3%) | `bromide_anion` (7.6%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.3%) | `pyridine_organocat` (2.8%) | `organic_neutral_cat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (98.6%) | `cyclic_ether` (0.8%) | `polar_aprotic_sulfoxide` (0.4%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (98%) | `C1CCOC1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)O.[K]` | `O=C(O)C(F)(F)F` (69%) | `[Cl-].[Na+]` (31%) | `[Na][Cl]` (10%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `Oc1ccccc1C=NCCN=Cc` (1%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2861  yield=78.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #21)

```
OB(O)c1ccccc1.C=Cc1cc(C)cc(C)c1>>Cc1cc(C)cc(C2COB(c3ccccc3)O2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (87.6%) | `carbon_rod` (7.2%) | `carbon_plate` (4.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `nickel` (0.4%) | `carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `nickel_plate` (0.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (99.6%) | `Na` (0.2%) | `NBu4` (0.1%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `Br` (72.2%) | `molecular_no_ion` (15.6%) | `ClO4` (6.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (23.9%) | `ABSENT` (4.3%) | `alkali_other_salt` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `organic_neutral_cat` (3.3%) | `pyridine_organocat` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.2%) | `cyclic_ether` (0.5%) | `polar_aprotic_sulfoxide` (0.2%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (94%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (49%) | `[Cl-].[Na+]` (48%) | `CC(=O)O` (23%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)NC1CC2(CCCCC` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2862  yield=78.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #22)

```
C=Cc1ccccc1.CCCCCCB(O)O>>CCCCCCB1OCC(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `ABSENT` (0.5%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (59.3%) | `graphite_rod` (19.4%) | `carbon_cloth` (7.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.8%) | `stainless_steel` (4.0%) | `copper` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (89.2%) | `platinum_generic` (7.2%) | `stainless_steel_generic` (1.9%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (99.5%) | `undivided` (0.5%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (51.2%) | `ABSENT` (41.2%) | `NBu4` (3.1%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `ABSENT` (79.7%) | `PF6` (4.7%) | `BF4` (4.6%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (4.8%) | `cyanide` (2.6%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.2%) | `Mn_complex` (2.2%) | `organic_neutral_cat` (1.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.7%) | `cyclic_ether` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `ClCCl` (77%) | `O` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `__ABSENT__` (68%) | `CC[Si](CC)CC` (7%) | `O=O` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (95%) | `Brc1ccc(N(c2ccc(Br` (1%) | `CC1(C)CCCC(C)(C)N1` (1%) | set ✓ / any ✓ |

---

### Reaction #2863  yield=77.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #23)

```
C=Cc1ccccc1.COC(=O)c1ccc(B(O)O)cc1>>COC(=O)c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (91.7%) | `graphite_rod` (5.7%) | `carbon_cloth` (1.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.9%) | `nickel` (9.0%) | `carbon` (5.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.1%) | `platinum_generic` (0.2%) | `nickel_plate` (0.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (98.5%) | `NBu4` (1.2%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (96.6%) | `I` (1.4%) | `PF6` (1.2%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (21.5%) | `ABSENT` (4.3%) | `cyanide` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.0%) | `pyridine_organocat` (1.7%) | `ionic_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (98.3%) | `polar_aprotic_sulfoxide` (0.8%) | `cyclic_ether` (0.5%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (99%) | `O` (86%) | `CCOCC` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (66%) | `[Cl-].[Na+]` (49%) | `CC(=O)O` (16%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `__OTHER__` (3%) | `c1ccncc1` (1%) | set ✓ / any ✓ |

---

### Reaction #2864  yield=74.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #24)

```
C=Cc1ccccc1.COc1ccc(B(O)O)cc1F>>COc1ccc(B2OCC(c3ccccc3)O2)cc1F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (97.7%) | `graphite_rod` (0.9%) | `carbon_cloth` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (77.4%) | `nickel` (11.7%) | `carbon` (5.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (94.2%) | `stainless_steel_generic` (2.8%) | `nickel_plate` (2.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (97.6%) | `NBu4` (2.0%) | `ABSENT` (0.1%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (87.6%) | `PF6` (5.8%) | `ABSENT` (1.8%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (6.8%) | `ABSENT` (4.7%) | `cyanide` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (55.2%) | `pyridine_organocat` (31.4%) | `Mn_complex` (3.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (96.9%) | `polar_aprotic_sulfoxide` (0.8%) | `ABSENT` (0.8%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (62%) | `CCOCC` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (23%) | `O=C(O)C(F)(F)F` (21%) | `O=S(=O)([O-])C(F)(` (12%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (92%) | `[Cl-].[Cl-].[Mn+2]` (5%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #2865  yield=74.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #25)

```
C=Cc1ccccc1.OB(O)CCc1ccccc1>>c1ccc(CCB2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.6%) | `ABSENT` (4.0%) | `platinum` (1.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (56.6%) | `graphite_generic` (14.7%) | `graphite_rod` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (55.2%) | `stainless_steel` (22.8%) | `ABSENT` (17.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (44.4%) | `stainless_steel_generic` (37.6%) | `ABSENT` (9.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `ABSENT` (99.8%) | `undivided` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (40.2%) | `K` (36.4%) | `ABSENT` (20.7%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (41.2%) | `BF4` (30.1%) | `PF6` (17.8%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `cyanide` (3.2%) | `inorganic_simple` (2.2%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.5%) | `organic_neutral_cat` (1.1%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (96.9%) | `cyclic_ether` (1.9%) | `polar_protic_alcohol` (0.5%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (98%) | `ClCCl` (21%) | `CCOCC` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[K]` | `O=O` (95%) | `CC[Si](CC)CC` (67%) | `OB(O)B(O)O` (45%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (83%) | `__OTHER__` (9%) | `c1ccncc1` (5%) | set ✓ / any ✓ |

---

### Reaction #2866  yield=76.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #26)

```
C=Cc1ccccc1.OB(O)c1ccc(C(F)(F)F)cc1>>FC(F)(F)c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (96.6%) | `carbon_rod` (1.0%) | `graphite_rod` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.4%) | `nickel` (3.9%) | `carbon` (3.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (97.4%) | `stainless_steel_generic` (1.0%) | `platinum_generic` (0.8%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (94.0%) | `NBu4` (5.2%) | `ABSENT` (0.4%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `Br` (82.5%) | `PF6` (11.9%) | `BF4` (1.9%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `carboxylic_acid` (20.8%) | `alkali_other_salt` (7.3%) | `alkali_sulfinate` (5.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (63.8%) | `ABSENT` (29.7%) | `organic_neutral_cat` (2.9%) | ✓ |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (96.4%) | `polar_aprotic_sulfoxide` (2.5%) | `cyclic_ether` (0.5%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (67%) | `ClCCl` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)O.[K]` | `O=C(O)C(F)(F)F` (69%) | `[Cl-].[Na+]` (20%) | `CC[Si](CC)CC` (13%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccncc1` (44%) | `__OTHER__` (32%) | `Cc1cccc(C)n1` (4%) | set ✗ / any ✗ |

---

### Reaction #2867  yield=76.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #27)

```
C=Cc1ccccc1.OB(O)c1ccsc1>>c1ccc(C2COB(c3ccsc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (94.9%) | `graphite_rod` (2.9%) | `carbon_generic` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.2%) | `carbon` (7.4%) | `stainless_steel` (1.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.7%) | `graphite_rod` (0.5%) | `stainless_steel_generic` (0.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (84.2%) | `NBu4` (13.5%) | `ABSENT` (1.4%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (78.9%) | `PF6` (13.5%) | `ABSENT` (2.5%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (29.9%) | `bromide_anion` (3.4%) | `ABSENT` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (62.7%) | `pyridine_organocat` (14.5%) | `Mn_complex` (9.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (95.7%) | `polar_aprotic_sulfoxide` (2.3%) | `polar_aprotic_amide` (1.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (88%) | `ClCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (61%) | `O=O` (32%) | `CC[Si](CC)CC` (17%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (73%) | `__OTHER__` (11%) | `[Cl-].[Cl-].[Mn+2]` (7%) | set ✓ / any ✓ |

---

### Reaction #2868  yield=76.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #28)

```
C=Cc1ccccc1.CCCCCCCCCCCCB(O)O>>CCCCCCCCCCCCB1OCC(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `ABSENT` (0.5%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (59.3%) | `graphite_rod` (19.4%) | `carbon_cloth` (7.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.8%) | `stainless_steel` (4.0%) | `copper` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (89.2%) | `platinum_generic` (7.2%) | `stainless_steel_generic` (1.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (99.5%) | `undivided` (0.5%) | `flow` (0.0%) | ✓ |
| 电解质 cation | 23 | `K` | `K` (51.2%) | `ABSENT` (41.2%) | `NBu4` (3.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (79.7%) | `PF6` (4.7%) | `BF4` (4.6%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (4.8%) | `cyanide` (2.6%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.2%) | `Mn_complex` (2.2%) | `organic_neutral_cat` (1.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.7%) | `cyclic_ether` (0.1%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `ClCCl` (77%) | `O` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `__OTHER__` | `__ABSENT__` (68%) | `CC[Si](CC)CC` (7%) | `O=O` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (95%) | `Brc1ccc(N(c2ccc(Br` (1%) | `CC1(C)CCCC(C)(C)N1` (1%) | set ✓ / any ✓ |

---

### Reaction #2869  yield=75.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #29)

```
C=Cc1ccccc1.OB(O)C1CCCCC1>>c1ccc(C2COB(C3CCCCC3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `ABSENT` (0.1%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (42.2%) | `carbon_cloth` (36.5%) | `carbon_rod` (15.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (56.0%) | `carbon` (25.5%) | `nickel` (11.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (95.3%) | `stainless_steel_generic` (2.4%) | `nickel_plate` (0.8%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (95.1%) | `ABSENT` (4.9%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (61.8%) | `ABSENT` (35.0%) | `NBu4` (1.3%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (83.5%) | `PF6` (6.0%) | `Br` (4.9%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (7.7%) | `alkali_other_salt` (4.1%) | `ABSENT` (3.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (46.0%) | `Mn_complex` (39.2%) | `pyridine_organocat` (9.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.2%) | `aqueous` (0.3%) | `polar_aprotic_amide` (0.2%) | ✓ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (99%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (29%) | `CC[Si](CC)CC` (9%) | `[Cl-].[Cl-].[Mg+2]` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (90%) | `c1ccncc1` (4%) | `__OTHER__` (3%) | set ✓ / any ✓ |

---

### Reaction #2870  yield=75.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #30)

```
C=Cc1ccccc1.COc1cccc(B(O)O)c1>>COc1cccc(B2OCC(c3ccccc3)O2)c1.COc1cccc(B2OCC(c3ccccc3)O2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (100.0%) | `carbon_generic` (0.0%) | `graphite_rod` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.6%) | `ABSENT` (1.1%) | `carbon` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.2%) | `stainless_steel_generic` (0.7%) | `glassy_carbon` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (99.7%) | `Na` (0.2%) | `NBu4` (0.1%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `Br` (99.2%) | `BF4` (0.3%) | `Cl` (0.2%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `carboxylic_acid` (42.6%) | `ABSENT` (2.2%) | `alkali_other_salt` (1.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.5%) | `pyridine_organocat` (0.9%) | `organic_neutral_cat` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (98.8%) | `polar_aprotic_sulfoxide` (0.8%) | `cyclic_ether` (0.2%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `CCOCC` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)O.[K]` | `[Cl-].[Na+]` (79%) | `O=C(O)C(F)(F)F` (62%) | `CC(=O)O` (19%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (94%) | `[Cl-].[Cl-].[Mn+2]` (3%) | `[Fe+2].c1cc[cH-]c1` (1%) | set ✓ / any ✓ |

---

### Reaction #2871  yield=75.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #31)

```
OB(O)c1ccccc1.C=Cc1ccc(-c2ccccc2)cc1>>c1ccc(B2OCC(c3ccc(-c4ccccc4)cc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (98.6%) | `carbon_rod` (0.9%) | `graphite_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.4%) | `nickel` (1.3%) | `stainless_steel` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.8%) | `stainless_steel_generic` (0.1%) | `platinum_generic` (0.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (99.6%) | `NBu4` (0.2%) | `Na` (0.1%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (86.3%) | `molecular_no_ion` (5.8%) | `PF6` (2.6%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (24.7%) | `boron_lewis_acid` (4.8%) | `alkali_other_salt` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.7%) | `Mn_complex` (2.4%) | `pyridine_organocat` (2.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (98.0%) | `polar_aprotic_sulfoxide` (1.1%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `CC(=O)O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (54%) | `O=C(O)C(F)(F)F` (51%) | `CC(=O)O` (28%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (67%) | `CC(=O)NC1CC2(CCCCC` (15%) | `[Fe+2].c1cc[cH-]c1` (13%) | set ✓ / any ✓ |

---

### Reaction #2872  yield=76.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #32)

```
OB(O)c1ccccc1.C=C(CC)c1ccccc1>>CCC1(c2ccccc2)COB(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.8%) | `platinum` (6.0%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (71.5%) | `graphite_generic` (20.5%) | `carbon_plate` (2.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.3%) | `nickel` (0.8%) | `stainless_steel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (69.7%) | `platinum_generic` (29.2%) | `stainless_steel_generic` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (41.7%) | `K` (29.6%) | `NEt4` (28.1%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `BF4` (58.1%) | `Br` (23.4%) | `ClO4` (6.2%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (16.4%) | `ABSENT` (5.2%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `organic_neutral_cat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (96.1%) | `polar_protic_alcohol` (1.7%) | `halogenated_aliphatic` (1.6%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (99%) | `ClCCCl` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `CC(=O)O` (74%) | `O=C(O)C(F)(F)F` (16%) | `Cc1ccc(I)cc1` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #2873  yield=74.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #33)

```
OB(O)c1ccccc1.C=C(c1ccccc1)C(C)C>>CC(C)C1(c2ccccc2)COB(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.2%) | `platinum` (9.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (42.1%) | `carbon_rod` (31.4%) | `platinum_plate` (11.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.6%) | `carbon` (1.1%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.5%) | `platinum_generic` (0.4%) | `graphite_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (65.0%) | `NEt4` (24.0%) | `Na` (8.6%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (58.1%) | `I` (17.9%) | `Cl` (8.0%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (11.1%) | `ABSENT` (7.5%) | `alkali_bicarbonate` (3.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.1%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.1%) | `halogenated_aliphatic` (0.4%) | `cyclic_ether` (0.2%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `CC(=O)O` (32%) | `O=C(O)C(F)(F)F` (27%) | `[Cl-].[Cl-].[Mg+2]` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2874  yield=73.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #34)

```
OB(O)c1ccccc1.C=C(CC(C)C)c1ccccc1>>CC(C)CC1(c2ccccc2)COB(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.0%) | `platinum` (5.5%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (90.8%) | `graphite_generic` (3.2%) | `carbon_rod` (2.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.6%) | `carbon` (5.8%) | `nickel` (4.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (58.6%) | `platinum_generic` (20.4%) | `nickel_plate` (10.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (56.4%) | `Li` (13.4%) | `NBu4` (12.5%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (47.8%) | `Br` (22.9%) | `I` (8.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_other_salt` | `carboxylic_acid` (32.1%) | `water` (1.8%) | `ABSENT` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.7%) | `polar_aprotic_amide` (0.1%) | `polar_protic_alcohol` (0.1%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (87%) | `CCO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)O.[K]` | `CC(=O)O` (88%) | `O=C(O)C(F)(F)F` (9%) | `[Cl-].[Na+]` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2875  yield=76.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #35)

```
OB(O)c1ccccc1.C=C(C)c1ccc(C)cc1>>Cc1ccccc1C1(C)COB(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `platinum` (11.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `platinum_plate` (56.9%) | `glassy_carbon` (26.3%) | `carbon_rod` (10.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.2%) | `carbon` (14.7%) | `copper` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.4%) | `platinum_generic` (0.4%) | `carbon_generic` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `K` (51.5%) | `NBu4` (43.7%) | `NEt4` (3.3%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `carboxylate` (52.4%) | `Cl` (16.3%) | `Br` (15.6%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (22.2%) | `ABSENT` (5.6%) | `primary_amine` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `tempo_mediator` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (100.0%) | `polar_protic_alcohol` (0.0%) | `polar_aprotic_sulfoxide` (0.0%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[K+].[O-][C+](=O)[` | `O=C(O)C(F)(F)F` (65%) | `CC(=O)O` (25%) | `[Cl-].[Na+]` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)NC1CC2(CCCCC` (0%) | `CC(C)(C)c1cc(C=N[C` (0%) | set ✓ / any ✓ |

---

### Reaction #2876  yield=79.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #36)

```
OB(O)c1ccccc1.C=C(C)c1ccc(C(F)(F)F)cc1>>CC1(c2ccc(C(F)(F)F)cc2)COB(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (66.4%) | `graphite_generic` (17.9%) | `carbon_cloth` (6.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (61.9%) | `platinum` (37.7%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (80.9%) | `graphite_generic` (12.6%) | `graphite_felt` (3.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (91.6%) | `K` (4.9%) | `NEt4` (2.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (27.1%) | `BF4` (24.8%) | `ClO4` (20.6%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (16.8%) | `alkali_other_salt` (8.5%) | `o2_oxidant` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.4%) | `pyridine_organocat` (1.2%) | `triarylamine_radical_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.9%) | `polar_aprotic_sulfoxide` (0.0%) | `polar_protic_alcohol` (0.0%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[K+].[O-][C+](=O)[` | `O=C(O)C(F)(F)F` (65%) | `CC(=O)O` (13%) | `O.O.O.O.O.O.O.O.O.` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)NC1CC2(CCCCC` (0%) | `CC(C)(C)c1cc(C=N[C` (0%) | set ✓ / any ✓ |

---

### Reaction #2877  yield=74.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #37)

```
OB(O)c1ccccc1.C=C(c1ccccc1)c1ccccc1>>c1ccc(B2OCC(c3ccccc3)(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.8%) | `platinum` (7.4%) | `ABSENT` (3.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (88.8%) | `carbon_rod` (7.7%) | `unknown_electrode` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (80.4%) | `carbon` (11.2%) | `ABSENT` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (96.9%) | `unknown_electrode` (1.6%) | `platinum_generic` (0.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (62.0%) | `NEt4` (31.7%) | `NBu4` (3.7%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `PF6` (47.9%) | `Br` (15.8%) | `ClO4` (13.9%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (30.5%) | `bromide_anion` (3.6%) | `ABSENT` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `organic_neutral_cat` (0.3%) | `Mn_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (98.3%) | `polar_protic_alcohol` (0.4%) | `polar_aprotic_sulfoxide` (0.4%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (98%) | `CCO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[K+].[O-][C+](=O)[` | `CC(=O)O` (88%) | `F.c1ccncc1` (15%) | `[Cl-].[Na+]` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (67%) | `Brc1ccc(N(c2ccc(Br` (28%) | `CC1(C)CCCC(C)(C)N1` (3%) | set ✓ / any ✓ |

---

### Reaction #2878  yield=76.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #38)

```
OB(O)c1ccccc1.C=C(c1ccccc1)C1CCCCC1>>c1ccc(B2OCC(c3ccccc3)(C3CCCCC3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `platinum` (1.0%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (91.4%) | `graphite_generic` (7.5%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.6%) | `stainless_steel` (3.9%) | `carbon` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (96.8%) | `stainless_steel_generic` (1.2%) | `graphite_generic` (1.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.4%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (47.4%) | `NEt4` (43.8%) | `NBu4` (5.7%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `Br` (42.2%) | `BF4` (22.2%) | `carboxylate` (11.0%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `carboxylic_acid` (38.2%) | `ABSENT` (3.9%) | `alkali_other_salt` (1.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `organic_neutral_cat` (0.2%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.2%) | `polar_protic_alcohol` (0.7%) | `halogenated_aliphatic` (0.0%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (86%) | `ClCCl` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)O.[K]` | `CC(=O)O` (83%) | `O=C(O)C(F)(F)F` (13%) | `[Cl-].[Na+]` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2879  yield=75.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #39)

```
OB(O)c1ccccc1.C=C(C)c1ccc(F)cc1>>CC1(c2ccc(F)cc2)COB(c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.3%) | `platinum` (2.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (78.5%) | `carbon_cloth` (6.4%) | `platinum_generic` (3.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.2%) | `carbon` (15.1%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (96.5%) | `platinum_generic` (1.3%) | `carbon_felt` (0.8%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (75.6%) | `K` (21.7%) | `NEt4` (2.1%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (35.4%) | `carboxylate` (20.1%) | `Br` (19.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (16.0%) | `o2_oxidant` (3.1%) | `ABSENT` (3.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.1%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.9%) | `polar_protic_alcohol` (0.0%) | `cyclic_ether` (0.0%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `CC(=O)O` (44%) | `O=C(O)C(F)(F)F` (20%) | `O.O.O.O.O.O.O.O.O.` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)NC1CC2(CCCCC` (0%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #2880  yield=82.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #40)

```
C=Cc1ccccc1.CSc1ccc(B(O)O)cc1>>CSc1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (89.2%) | `carbon_generic` (5.2%) | `graphite_rod` (2.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.9%) | `nickel` (11.0%) | `carbon` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (93.4%) | `nickel_plate` (2.9%) | `platinum_generic` (1.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (91.3%) | `NBu4` (8.1%) | `ABSENT` (0.3%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (81.9%) | `PF6` (7.3%) | `BF4` (6.8%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (6.1%) | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.3%) | `pyridine_organocat` (3.0%) | `ionic_organocat` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (98.6%) | `polar_aprotic_sulfoxide` (0.6%) | `cyclic_ether` (0.6%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (99%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (35%) | `O=C(O)C(F)(F)F` (20%) | `C[Si](C)(C)N=[N+]=` (19%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2881  yield=85.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #41)

```
C=Cc1ccccc1.CC(C)c1ccc(B(O)O)cc1>>CC(C)c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (98.8%) | `graphite_rod` (0.6%) | `graphite_generic` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (91.7%) | `nickel` (5.5%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (96.5%) | `stainless_steel_generic` (3.0%) | `nickel_plate` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (97.8%) | `NBu4` (1.9%) | `ABSENT` (0.1%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `Br` (89.3%) | `I` (4.6%) | `BF4` (3.2%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (8.4%) | `boron_lewis_acid` (5.0%) | `alkali_other_salt` (4.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.7%) | `pyridine_organocat` (3.2%) | `Mn_complex` (2.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (98.7%) | `polar_aprotic_sulfoxide` (0.9%) | `cyclic_ether` (0.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (96%) | `ClCCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (41%) | `CC(=O)O` (23%) | `[Cl-].[Na+]` (13%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2882  yield=82.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #42)

```
OB(O)c1ccccc1.C=Cc1ccc(F)cc1>>Fc1ccc(C2COB(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (97.4%) | `carbon_rod` (0.9%) | `carbon_generic` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.8%) | `carbon` (5.9%) | `nickel` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.7%) | `stainless_steel_generic` (0.4%) | `graphite_rod` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (99.6%) | `NBu4` (0.2%) | `Na` (0.1%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `Br` (84.8%) | `molecular_no_ion` (6.6%) | `PF6` (3.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (16.4%) | `alkali_other_salt` (3.1%) | `ABSENT` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.5%) | `pyridine_organocat` (2.7%) | `Mn_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.5%) | `polar_aprotic_sulfoxide` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (99%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `CC(=O)O` (51%) | `[Cl-].[Na+]` (40%) | `O=C(O)C(F)(F)F` (19%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Cl-].[Cl-].[Mn+2]` (1%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2883  yield=85.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #43)

```
C=Cc1ccccc1.OB(O)c1ccc(OCc2ccccc2)cc1>>c1ccc(COc2ccc(B3OCC(c4ccccc4)O3)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (98.8%) | `graphite_rod` (0.6%) | `carbon_cloth` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.0%) | `nickel` (8.6%) | `stainless_steel` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.0%) | `stainless_steel_generic` (1.6%) | `nickel_wire` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.8%) | `ABSENT` (1.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `K` (99.7%) | `NBu4` (0.2%) | `ABSENT` (0.1%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (91.2%) | `PF6` (6.2%) | `ABSENT` (1.9%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (23.6%) | `alkali_other_salt` (9.9%) | `ABSENT` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (75.7%) | `pyridine_organocat` (20.7%) | `organic_neutral_cat` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (94.8%) | `polar_aprotic_sulfoxide` (4.6%) | `polar_aprotic_amide` (0.2%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (96%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (95%) | `[Na][Cl]` (14%) | `[Cl-].[Na+]` (13%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (92%) | `__OTHER__` (3%) | `[I-].[Li+]` (3%) | set ✓ / any ✓ |

---

### Reaction #2884  yield=82.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #44)

```
C=Cc1ccccc1.OB(O)c1ccc(Oc2ccccc2)cc1>>c1ccc(Oc2ccc(B3OCC(c4ccccc4)O3)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (89.9%) | `carbon_cloth` (5.4%) | `graphite_rod` (1.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (75.6%) | `nickel` (21.1%) | `stainless_steel` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.1%) | `nickel_plate` (0.4%) | `stainless_steel_generic` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (96.5%) | `NBu4` (2.4%) | `ABSENT` (0.7%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (91.2%) | `ABSENT` (3.5%) | `PF6` (3.2%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (14.9%) | `alkali_other_salt` (4.5%) | `ABSENT` (3.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (88.4%) | `pyridine_organocat` (6.9%) | `organic_neutral_cat` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (98.3%) | `polar_aprotic_sulfoxide` (0.6%) | `polar_aprotic_amide` (0.5%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (62%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (43%) | `CC(=O)O` (15%) | `[Cl-].[Na+]` (14%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `O=C1OC2(c3ccccc31)` (0%) | set ✓ / any ✓ |

---

### Reaction #2885  yield=85.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #45)

```
C=Cc1ccccc1.CCOc1ccc(B(O)O)cc1>>CCOc1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (96.1%) | `graphite_rod` (2.9%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.7%) | `nickel` (10.0%) | `carbon` (4.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (97.3%) | `stainless_steel_generic` (1.1%) | `nickel_plate` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (98.8%) | `NBu4` (0.7%) | `ABSENT` (0.4%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `Br` (92.5%) | `ABSENT` (3.8%) | `BF4` (1.2%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (29.5%) | `alkali_other_salt` (5.6%) | `ABSENT` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.0%) | `pyridine_organocat` (2.2%) | `organic_neutral_cat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (98.5%) | `polar_aprotic_sulfoxide` (1.0%) | `polar_aprotic_amide` (0.2%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (92%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `O=C(O)C(F)(F)F` (87%) | `[Cl-].[Na+]` (13%) | `[Na][Cl]` (12%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[Li+]` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2886  yield=81.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #46)

```
C=Cc1ccccc1.OB(O)c1cccc2ccccc12>>c1ccc(C2COB(c3cccc4ccccc34)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (98.2%) | `carbon_generic` (0.9%) | `graphite_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (78.2%) | `carbon` (13.0%) | `stainless_steel` (4.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (92.3%) | `stainless_steel_generic` (6.5%) | `graphite_rod` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (92.8%) | `ABSENT` (7.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (84.4%) | `NBu4` (15.4%) | `ABSENT` (0.1%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (89.5%) | `BF4` (4.9%) | `PF6` (4.7%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (17.1%) | `alkali_other_salt` (2.4%) | `cyanide` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.2%) | `pyridine_organocat` (1.7%) | `organic_neutral_cat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.0%) | `polar_aprotic_sulfoxide` (0.4%) | `cyclic_ether` (0.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (96%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `CC(=O)O` (39%) | `CC[Si](CC)CC` (13%) | `O=C(O)C(F)(F)F` (12%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (86%) | `__OTHER__` (10%) | `c1ccncc1` (3%) | set ✓ / any ✓ |

---

### Reaction #2887  yield=84.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #47)

```
OB(O)c1ccccc1.C=Cc1ccccc1>>c1ccc(B2OCC(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (98.3%) | `carbon_plate` (0.8%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.9%) | `carbon` (4.5%) | `stainless_steel` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.4%) | `stainless_steel_generic` (0.4%) | `glassy_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (99.1%) | `NBu4` (0.4%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (87.1%) | `I` (4.5%) | `PF6` (4.1%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (33.1%) | `ABSENT` (2.3%) | `bromide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.8%) | `ionic_organocat` (8.6%) | `organic_neutral_cat` (8.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (93.4%) | `polar_aprotic_sulfoxide` (2.8%) | `cyclic_ether` (2.3%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Mg+2].[O-][Cl+3](` + `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (67%) | `CC(=O)O` (46%) | `O=C(O)C(F)(F)F` (43%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (77%) | `[Fe+2].c1cc[cH-]c1` (5%) | `Brc1ccc(N(c2ccc(Br` (3%) | set ✓ / any ✓ |

---

### Reaction #2888  yield=82.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #48)

```
OB(O)c1ccccc1.C=C(c1ccccc1)C1CCCC1>>c1ccc(B2OCC(c3ccccc3)(C3CCCC3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.1%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (84.6%) | `graphite_generic` (14.7%) | `carbon_rod` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.2%) | `stainless_steel` (8.1%) | `carbon` (4.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (90.5%) | `stainless_steel_generic` (5.3%) | `graphite_generic` (3.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NEt4` (52.7%) | `K` (37.4%) | `NBu4` (7.6%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `BF4` (34.1%) | `Br` (31.3%) | `carboxylate` (11.5%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (33.6%) | `ABSENT` (3.4%) | `alkali_other_salt` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `organic_neutral_cat` (0.2%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.1%) | `polar_protic_alcohol` (0.7%) | `halogenated_aliphatic` (0.1%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (76%) | `ClCCl` (11%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `CC(=O)O` (83%) | `O=C(O)C(F)(F)F` (10%) | `OC(C(F)(F)F)C(F)(F` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2889  yield=85.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2063-2074.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2063-2074.json) (反应 idx 在该 JSON 内 = #49)

```
OB(O)c1ccccc1.C=Cc1ccc(C)cc1>>Cc1ccc(C2COB(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `glassy_carbon` (79.7%) | `carbon_rod` (15.7%) | `carbon_plate` (1.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.4%) | `carbon` (5.9%) | `nickel` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.6%) | `nickel_plate` (0.1%) | `platinum_generic` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `K` (99.5%) | `Li` (0.2%) | `NBu4` (0.2%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Br` (43.5%) | `molecular_no_ion` (40.4%) | `ClO4` (6.3%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `carboxylic_acid` (21.7%) | `alkali_other_salt` (4.2%) | `ABSENT` (3.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.5%) | `ionic_organocat` (0.6%) | `organic_neutral_cat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (99.2%) | `cyclic_ether` (0.4%) | `polar_aprotic_sulfoxide` (0.2%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (100%) | `O` (100%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` | `[Cl-].[Na+]` (50%) | `O=C(O)C(F)(F)F` (46%) | `CC(=O)O` (39%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `CC(=O)NC1CC2(CCCCC` (1%) | `[Fe+2].c1cc[cH-]c1` (1%) | set ✓ / any ✓ |

---

### Reaction #2890  yield=27.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_13_2124-2130.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_13_2124-2130.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.CC(C)(C)[Si](C)(C)OC1=CCCCCC1>>c1ccc(C2CC3=C(CCCCC3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.1%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (99.8%) | `carbon_generic` (0.0%) | `platinum_plate` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `nickel` (0.1%) | `copper` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_generic` | `graphite_generic` (99.8%) | `carbon_generic` (0.1%) | `graphite_felt` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.5%) | `ABSENT` (1.3%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (91.7%) | `NBu4` (7.8%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (93.2%) | `PF6` (3.6%) | `molecular_no_ion` (1.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `pyridine` | `pyridine` (59.6%) | `ABSENT` (1.6%) | `ester` (1.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.2%) | `ketone` (1.0%) | `polar_aprotic_amide` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `CN(C)C=O` (1%) | `ClCCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` | `Cc1cccc(C)n1` (100%) | `c1ccncc1` (0%) | `O=C([O-])C(F)(F)F.` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2891  yield=8.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCc1ccc(C(F)(F)F)cc1>>CC(=O)OC[C@H](OC(C)=O)[C@H](OC(C)=O)c1ccc(C(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (0.8%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (98.7%) | `graphite_felt` (0.9%) | `graphite_generic` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (64.1%) | `copper` (32.4%) | `sacrificial_zinc` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `stainless_steel_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (95.8%) | `NBu4` (1.9%) | `Li` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `PF6` (4.2%) | `ClO4` (1.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (78.4%) | `acid_anhydride` (3.4%) | `sulfonic_acid` (1.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `brønsted_acid_cat` (0.1%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (59.3%) | `acid_anhydride_solvent` (33.8%) | `ABSENT` (4.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `ClCCl` (100%) | `[H+].[OH-]` (98%) | `OC(C(F)(F)F)C(F)(F` (96%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I)cc1` + `F.c1ccncc1` + `O=C([O-])[O-].[Ca+` | `__OTHER__` (98%) | `OB(O)B(O)O` (98%) | `O=O` (96%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (98%) | `__ABSENT__` (5%) | `O=S(=O)([O-])C(F)(` (0%) | set ✗ / any ✓ |

---

### Reaction #2892  yield=6.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCc1ccc(C(F)(F)F)cc1>>CC(=O)OC[C@H](OC(C)=O)[C@H](OC(C)=O)c1ccc(C(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (0.8%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (98.7%) | `graphite_felt` (0.9%) | `graphite_generic` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (64.1%) | `copper` (32.4%) | `sacrificial_zinc` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `stainless_steel_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (95.8%) | `NBu4` (1.9%) | `Li` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `PF6` (4.2%) | `ClO4` (1.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (78.4%) | `acid_anhydride` (3.4%) | `sulfonic_acid` (1.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `brønsted_acid_cat` (0.1%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (59.3%) | `acid_anhydride_solvent` (33.8%) | `ABSENT` (4.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `ClCCl` (100%) | `[H+].[OH-]` (98%) | `OC(C(F)(F)F)C(F)(F` (96%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I)cc1` + `F.c1ccncc1` + `O=C([O-])[O-].[Ca+` | `__OTHER__` (98%) | `OB(O)B(O)O` (98%) | `O=O` (96%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (98%) | `__ABSENT__` (5%) | `O=S(=O)([O-])C(F)(` (0%) | set ✗ / any ✓ |

---

### Reaction #2893  yield=8.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #2)

```
O=CO.C=CCc1ccccc1>>O=COC[C@H](OC=O)[C@H](OC=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_rod` (89.7%) | `carbon_cloth` (3.2%) | `carbon_felt` (3.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.1%) | `nickel` (0.6%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `stainless_steel_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (94.6%) | `ABSENT` (5.4%) | `NEt4` (0.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (95.4%) | `ABSENT` (3.6%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `water` (39.0%) | `bromide_anion` (9.5%) | `carboxylic_acid` (5.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.3%) | `Cu_complex` (2.8%) | `ionic_organocat` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_aprotic_amide` (99.8%) | `ABSENT` (0.1%) | `polar_aprotic_nitrile` (0.0%) | ✗ |
| 溶剂 set | 79 | `CC(=O)O` + `CC(=O)OC(C)=O` + `O` | `CN(C)C=O` (100%) | `CC#N` (0%) | `CC(=O)O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `O` (100%) | `[Cl-].[Na+]` (24%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (65%) | `[Cl][Cu]` (35%) | `CC(=O)[O-].[Cu+]` (0%) | set ✓ / any ✓ |

---

### Reaction #2894  yield=8.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #3)

```
O=CO.C=CCc1ccccc1>>O=COC[C@@H](OC=O)[C@H](OC=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_rod` (89.7%) | `carbon_cloth` (3.2%) | `carbon_felt` (3.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.1%) | `nickel` (0.6%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `stainless_steel_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (94.6%) | `ABSENT` (5.4%) | `NEt4` (0.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (95.4%) | `ABSENT` (3.6%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `water` (39.0%) | `bromide_anion` (9.5%) | `carboxylic_acid` (5.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.3%) | `Cu_complex` (2.8%) | `ionic_organocat` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_aprotic_amide` (99.8%) | `ABSENT` (0.1%) | `polar_aprotic_nitrile` (0.0%) | ✗ |
| 溶剂 set | 79 | `CC(=O)O` + `CC(=O)OC(C)=O` + `O` | `CN(C)C=O` (100%) | `CC#N` (0%) | `CC(=O)O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `O` (100%) | `[Cl-].[Na+]` (24%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (65%) | `[Cl][Cu]` (35%) | `CC(=O)[O-].[Cu+]` (0%) | set ✓ / any ✓ |

---

### Reaction #2895  yield=6.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #4)

```
C=CCc1ccc(C(F)(F)F)cc1>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1ccc(C(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (0.8%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (98.7%) | `graphite_felt` (0.9%) | `graphite_generic` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (64.1%) | `copper` (32.4%) | `sacrificial_zinc` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `stainless_steel_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (95.8%) | `NBu4` (1.9%) | `Li` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `PF6` (4.2%) | `ClO4` (1.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (78.4%) | `acid_anhydride` (3.4%) | `sulfonic_acid` (1.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `brønsted_acid_cat` (0.1%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (59.3%) | `acid_anhydride_solvent` (33.8%) | `ABSENT` (4.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `ClCCl` (100%) | `[H+].[OH-]` (98%) | `OC(C(F)(F)F)C(F)(F` (96%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I)cc1` + `F.c1ccncc1` + `O=C([O-])[O-].[Ca+` | `__OTHER__` (98%) | `OB(O)B(O)O` (98%) | `O=O` (96%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (98%) | `__ABSENT__` (5%) | `O=S(=O)([O-])C(F)(` (0%) | set ✗ / any ✓ |

---

### Reaction #2896  yield=6.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #5)

```
C=CCc1ccc(C(F)(F)F)cc1>>CC(=O)OCC(Cc1ccc(C(F)(F)F)cc1)OC(C)=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (89.2%) | `platinum` (7.8%) | `ABSENT` (1.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (36.0%) | `graphite_generic` (22.0%) | `platinum_generic` (19.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (52.5%) | `copper` (28.0%) | `sacrificial_zinc` (8.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (90.6%) | `platinum_plate` (3.5%) | `stainless_steel_generic` (1.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (96.3%) | `divided` (2.1%) | `ABSENT` (1.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (53.3%) | `NBu4` (19.1%) | `ABSENT` (13.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (44.5%) | `ClO4` (25.3%) | `ABSENT` (14.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (18.0%) | `carboxylic_acid` (9.6%) | `acid_anhydride` (3.6%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.8%) | `Mn_complex` (1.4%) | `organic_neutral_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (32.3%) | `ABSENT` (22.7%) | `halogenated_aliphatic` (20.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `ClCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (95%) | `[H+].[OH-]` (89%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I)cc1` + `F.c1ccncc1` + `O=C([O-])[O-].[Ca+` | `__OTHER__` (100%) | `OB(O)B(O)O` (100%) | `O=O` (99%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (30%) | `__ABSENT__` (7%) | `O=S(=O)(O)C(F)(F)F` (1%) | set ✗ / any ✓ |

---

### Reaction #2897  yield=15.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #6)

```
C=CCc1ccc(OC)cc1>>COc1ccc([C@H](OC(C)=O)[C@@H](COC(C)=O)OC(C)=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (0.9%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.0%) | `graphite_felt` (0.3%) | `carbon_felt` (0.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (78.4%) | `copper` (17.1%) | `carbon` (1.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.0%) | `platinum_plate` (0.8%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `divided` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (81.4%) | `NBu4` (7.7%) | `K` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (89.5%) | `ClO4` (2.7%) | `PF6` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (71.6%) | `acid_anhydride` (3.2%) | `sulfonic_acid` (2.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `Fe_complex` (0.1%) | `brønsted_acid_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (50.5%) | `acid_anhydride_solvent` (41.9%) | `ABSENT` (3.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `ClCCl` (98%) | `[H+].[OH-]` (94%) | `OC(C(F)(F)F)C(F)(F` (86%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `OB(O)B(O)O` (90%) | `O=O` (87%) | `__OTHER__` (85%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (94%) | `__ABSENT__` (39%) | `[Fe+2].c1cc[cH-]c1` (1%) | set ✗ / any ✓ |

---

### Reaction #2898  yield=19.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #7)

```
C=CCc1ccc(OC)cc1>>COc1ccc([C@H](OC(C)=O)[C@H](COC(C)=O)OC(C)=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (0.9%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.0%) | `graphite_felt` (0.3%) | `carbon_felt` (0.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (78.4%) | `copper` (17.1%) | `carbon` (1.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.0%) | `platinum_plate` (0.8%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `divided` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (81.4%) | `NBu4` (7.7%) | `K` (3.9%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (89.5%) | `ClO4` (2.7%) | `PF6` (2.5%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (71.6%) | `acid_anhydride` (3.2%) | `sulfonic_acid` (2.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `Fe_complex` (0.1%) | `brønsted_acid_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (50.5%) | `acid_anhydride_solvent` (41.9%) | `ABSENT` (3.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `ClCCl` (98%) | `[H+].[OH-]` (94%) | `OC(C(F)(F)F)C(F)(F` (86%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `OB(O)B(O)O` (90%) | `O=O` (87%) | `__OTHER__` (85%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (94%) | `__ABSENT__` (39%) | `[Fe+2].c1cc[cH-]c1` (1%) | set ✗ / any ✓ |

---

### Reaction #2899  yield=14.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #4)

```
C=CCc1ccc(C(F)(F)F)cc1>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1ccc(C(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (0.8%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (98.7%) | `graphite_felt` (0.9%) | `graphite_generic` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (64.1%) | `copper` (32.4%) | `sacrificial_zinc` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `stainless_steel_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (95.8%) | `NBu4` (1.9%) | `Li` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `PF6` (4.2%) | `ClO4` (1.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (78.4%) | `acid_anhydride` (3.4%) | `sulfonic_acid` (1.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `brønsted_acid_cat` (0.1%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (59.3%) | `acid_anhydride_solvent` (33.8%) | `ABSENT` (4.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `ClCCl` (100%) | `[H+].[OH-]` (98%) | `OC(C(F)(F)F)C(F)(F` (96%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I)cc1` + `F.c1ccncc1` + `O=C([O-])[O-].[Ca+` | `__OTHER__` (98%) | `OB(O)B(O)O` (98%) | `O=O` (96%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (98%) | `__ABSENT__` (5%) | `O=S(=O)([O-])C(F)(` (0%) | set ✗ / any ✓ |

---

### Reaction #2900  yield=13.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #9)

```
C=CCc1cccc(C(=O)OC)c1>>COC(=O)c1cccc([C@@H](OC(C)=O)[C@H](COC(C)=O)OC(C)=O)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (97.3%) | `graphite_felt` (1.5%) | `reticulated_vitreous_carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.3%) | `copper` (1.8%) | `carbon` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.0%) | `platinum_plate` (0.7%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (82.5%) | `NBu4` (7.8%) | `ABSENT` (4.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (78.5%) | `ClO4` (10.3%) | `PF6` (4.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (34.1%) | `carboxylic_acid` (6.2%) | `acid_anhydride` (5.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `Fe_complex` (0.2%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (58.7%) | `ABSENT` (18.4%) | `acid_anhydride_solvent` (13.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (95%) | `CC(=O)O` (57%) | `[H+].[OH-]` (37%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `CC[N+](CC)(CC)CC.F` + `[Br-].[Li+]` + `O=C1CCC(=O)N1Br` | `O=S(=O)(O)C(F)(F)F` (55%) | `__OTHER__` (46%) | `O=O` (45%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (82%) | `[Br-].[Br-].[Mn+2]` (38%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2901  yield=14.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #10)

```
C=CCc1ccc(Cl)cc1>>OC[C@@H](O)[C@H](O)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.0%) | `platinum` (5.9%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (88.4%) | `graphite_felt` (5.2%) | `carbon_cloth` (2.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `stainless_steel` (0.4%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.5%) | `platinum_generic` (0.9%) | `stainless_steel_generic` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (66.6%) | `K` (22.1%) | `Li` (7.9%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `carboxylate` (63.9%) | `ClO4` (15.7%) | `Br` (6.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `carboxylic_acid` (11.4%) | `as_solvent_polar_aprotic_sulfo` (6.9%) | `ABSENT` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `organic_neutral_cat` (0.2%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `halogenated_aliphatic` (34.4%) | `polar_aprotic_nitrile` (31.0%) | `polar_protic_alcohol` (15.5%) | ✗ |
| 溶剂 set | 79 | `CC(=O)O` + `CC(=O)OC(C)=O` + `CO` + `O` | `ClCCl` (65%) | `O` (35%) | `CC#N` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `[Br-].[Li+]` + `O=C1CCC(=O)N1Br` | `CC(=O)OC(C)=O` (24%) | `O=C(O)C(F)(F)F` (18%) | `[Br-].[Li+]` (10%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[O]=[Fe][O][Fe]=[O` (1%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #2902  yield=16.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #11)

```
C=CCc1ccc(OC(F)(F)F)cc1>>OC[C@H](O)[C@H](O)c1ccc(OC(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (77.2%) | `graphite_felt` (20.0%) | `carbon_cloth` (1.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.2%) | `carbon` (0.5%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.0%) | `platinum_generic` (2.6%) | `carbon_felt` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (66.1%) | `Li` (23.6%) | `ABSENT` (8.5%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (44.9%) | `carboxylate` (24.0%) | `molecular_no_ion` (12.0%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `carboxylic_acid` (4.7%) | `iodide_anion` (4.5%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `organic_neutral_cat` (0.4%) | `pyridine_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `halogenated_aliphatic` (75.8%) | `polar_aprotic_nitrile` (9.3%) | `polar_protic_alcohol` (6.8%) | ✗ |
| 溶剂 set | 79 | `CC(=O)O` + `CC(=O)OC(C)=O` + `CO` + `O` | `ClCCl` (99%) | `O` (1%) | `CC(=O)O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `CC[N+](CC)(CC)CC.F` (13%) | `CC(=O)OC(C)=O` (9%) | `O=S(=O)(O)C(F)(F)F` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[O]=[Fe][O][Fe]=[O` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✓ / any ✓ |

---

### Reaction #2903  yield=16.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #11)

```
C=CCc1ccc(OC(F)(F)F)cc1>>OC[C@H](O)[C@H](O)c1ccc(OC(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (77.2%) | `graphite_felt` (20.0%) | `carbon_cloth` (1.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.2%) | `carbon` (0.5%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.0%) | `platinum_generic` (2.6%) | `carbon_felt` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (66.1%) | `Li` (23.6%) | `ABSENT` (8.5%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (44.9%) | `carboxylate` (24.0%) | `molecular_no_ion` (12.0%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `carboxylic_acid` (4.7%) | `iodide_anion` (4.5%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `organic_neutral_cat` (0.4%) | `pyridine_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `halogenated_aliphatic` (75.8%) | `polar_aprotic_nitrile` (9.3%) | `polar_protic_alcohol` (6.8%) | ✗ |
| 溶剂 set | 79 | `CC(=O)O` + `CC(=O)OC(C)=O` + `CO` + `O` | `ClCCl` (99%) | `O` (1%) | `CC(=O)O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `CC[N+](CC)(CC)CC.F` (13%) | `CC(=O)OC(C)=O` (9%) | `O=S(=O)(O)C(F)(F)F` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[O]=[Fe][O][Fe]=[O` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✓ / any ✓ |

---

### Reaction #2904  yield=17.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #13)

```
C=CCc1ccc(F)cc1>>CC(=O)OC[C@H](OC(C)=O)[C@H](OC(C)=O)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.4%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (98.0%) | `graphite_felt` (1.4%) | `graphite_generic` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (81.7%) | `copper` (12.2%) | `sacrificial_zinc` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `platinum_wire` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (93.5%) | `K` (2.2%) | `NBu4` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (84.7%) | `Br` (4.6%) | `ClO4` (3.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (67.4%) | `acid_anhydride` (5.5%) | `sulfonic_acid` (2.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (58.9%) | `acid_anhydride_solvent` (38.6%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `ClCCl` (99%) | `[H+].[OH-]` (98%) | `OC(C(F)(F)F)C(F)(F` (94%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (97%) | `O=O` (94%) | `OB(O)B(O)O` (94%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (98%) | `__ABSENT__` (28%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✓ |

---

### Reaction #2905  yield=17.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #13)

```
C=CCc1ccc(F)cc1>>CC(=O)OC[C@H](OC(C)=O)[C@H](OC(C)=O)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.4%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (98.0%) | `graphite_felt` (1.4%) | `graphite_generic` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (81.7%) | `copper` (12.2%) | `sacrificial_zinc` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `platinum_wire` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (93.5%) | `K` (2.2%) | `NBu4` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (84.7%) | `Br` (4.6%) | `ClO4` (3.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (67.4%) | `acid_anhydride` (5.5%) | `sulfonic_acid` (2.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (58.9%) | `acid_anhydride_solvent` (38.6%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `ClCCl` (99%) | `[H+].[OH-]` (98%) | `OC(C(F)(F)F)C(F)(F` (94%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (97%) | `O=O` (94%) | `OB(O)B(O)O` (94%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (98%) | `__ABSENT__` (28%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✓ |

---

### Reaction #2906  yield=16.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #15)

```
C=CCc1ccccc1>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.9%) | `reticulated_vitreous_carbon` (0.0%) | `graphite_felt` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (59.6%) | `copper` (34.8%) | `sacrificial_zinc` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.9%) | `platinum_plate` (0.1%) | `carbon_cloth` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (96.3%) | `NBu4` (1.2%) | `Li` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (91.2%) | `PF6` (4.0%) | `ClO4` (2.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (68.2%) | `sulfonic_acid` (6.9%) | `acid_anhydride` (6.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `brønsted_acid_cat` (0.1%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (85.7%) | `acid_anhydride_solvent` (12.9%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `[H+].[OH-]` | `[H+].[OH-]` (100%) | `ClCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (100%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Br-].[Br-].[Mn+2]` | `[Br-].[Br-].[Mn+2]` (100%) | `c1ccncc1` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2907  yield=16.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #15)

```
C=CCc1ccccc1>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.9%) | `reticulated_vitreous_carbon` (0.0%) | `graphite_felt` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (59.6%) | `copper` (34.8%) | `sacrificial_zinc` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.9%) | `platinum_plate` (0.1%) | `carbon_cloth` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (96.3%) | `NBu4` (1.2%) | `Li` (1.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (91.2%) | `PF6` (4.0%) | `ClO4` (2.4%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (68.2%) | `sulfonic_acid` (6.9%) | `acid_anhydride` (6.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `brønsted_acid_cat` (0.1%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (85.7%) | `acid_anhydride_solvent` (12.9%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `[H+].[OH-]` | `[H+].[OH-]` (100%) | `ClCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (100%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Br-].[Br-].[Mn+2]` | `[Br-].[Br-].[Mn+2]` (100%) | `c1ccncc1` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2908  yield=16.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #17)

```
C=CCc1ccc(Br)cc1>>CC(=O)OC[C@H](OC(C)=O)[C@H](OC(C)=O)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (96.9%) | `graphite_felt` (2.5%) | `reticulated_vitreous_carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (81.1%) | `copper` (15.3%) | `carbon` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (90.8%) | `NBu4` (4.3%) | `Li` (3.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (93.1%) | `ClO4` (2.7%) | `PF6` (1.5%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (71.0%) | `sulfonic_acid` (5.6%) | `acid_anhydride` (3.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (66.5%) | `acid_anhydride_solvent` (28.7%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (99%) | `[H+].[OH-]` (95%) | `OC(C(F)(F)F)C(F)(F` (95%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (97%) | `O=O` (93%) | `OB(O)B(O)O` (92%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (95%) | `__ABSENT__` (15%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #2909  yield=16.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #17)

```
C=CCc1ccc(Br)cc1>>CC(=O)OC[C@H](OC(C)=O)[C@H](OC(C)=O)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (96.9%) | `graphite_felt` (2.5%) | `reticulated_vitreous_carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (81.1%) | `copper` (15.3%) | `carbon` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (90.8%) | `NBu4` (4.3%) | `Li` (3.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (93.1%) | `ClO4` (2.7%) | `PF6` (1.5%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (71.0%) | `sulfonic_acid` (5.6%) | `acid_anhydride` (3.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (66.5%) | `acid_anhydride_solvent` (28.7%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (99%) | `[H+].[OH-]` (95%) | `OC(C(F)(F)F)C(F)(F` (95%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (97%) | `O=O` (93%) | `OB(O)B(O)O` (92%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (95%) | `__ABSENT__` (15%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #2910  yield=20.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #19)

```
C=CCc1ccc2cc(O)ccc2c1>>CC(=O)OC[C@H](OC(C)=O)[C@H](OC(C)=O)c1ccc2cc(OC(C)=O)ccc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (1.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (89.1%) | `graphite_felt` (5.4%) | `carbon_felt` (1.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.6%) | `copper` (3.2%) | `carbon` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `platinum_wire` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (55.0%) | `NBu4` (24.4%) | `ABSENT` (10.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (93.7%) | `ABSENT` (2.5%) | `PF6` (2.3%) | ✓ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (65.8%) | `sulfonic_acid` (3.7%) | `acid_anhydride` (2.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `ferrocene_mediator` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (63.7%) | `acid_anhydride_solvent` (27.0%) | `ABSENT` (3.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (98%) | `OC(C(F)(F)F)C(F)(F` (87%) | `CC(=O)O` (39%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `O=S(=O)(O)C(F)(F)F` (69%) | `__OTHER__` (23%) | `O=O` (16%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `[Br-].[Br-].[Mn+2]` (16%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2911  yield=29.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #20)

```
C=CCc1ccccc1>>CCC(=O)OC[C@H](OC(=O)CC)[C@@H](OC(=O)CC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (87.1%) | `reticulated_vitreous_carbon` (8.9%) | `graphite_generic` (1.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.4%) | `copper` (1.8%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.8%) | `platinum_plate` (0.2%) | `stainless_steel_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (88.1%) | `NBu4` (10.8%) | `ABSENT` (0.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (97.2%) | `PF6` (1.5%) | `ClO4` (0.4%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (21.8%) | `sulfonyl_chloride` (4.3%) | `carboxylic_acid` (3.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `Mn_complex` (0.1%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (63.0%) | `ABSENT` (13.5%) | `acid_anhydride_solvent` (8.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `[H+].[OH-]` | `OC(C(F)(F)F)C(F)(F` (98%) | `[H+].[OH-]` (95%) | `ClCCl` (93%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Br-].[Br-].[Mn+2]` | `[Br-].[Br-].[Mn+2]` (97%) | `__ABSENT__` (3%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2912  yield=22.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #21)

```
C=CCc1ccccc1>>CCC(=O)OC[C@@H](OC(=O)CC)[C@@H](OC(=O)CC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (87.1%) | `reticulated_vitreous_carbon` (8.9%) | `graphite_generic` (1.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.4%) | `copper` (1.8%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.8%) | `platinum_plate` (0.2%) | `stainless_steel_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (88.1%) | `NBu4` (10.8%) | `ABSENT` (0.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (97.2%) | `PF6` (1.5%) | `ClO4` (0.4%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (21.8%) | `sulfonyl_chloride` (4.3%) | `carboxylic_acid` (3.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `Mn_complex` (0.1%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (63.0%) | `ABSENT` (13.5%) | `acid_anhydride_solvent` (8.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `[H+].[OH-]` | `OC(C(F)(F)F)C(F)(F` (98%) | `[H+].[OH-]` (95%) | `ClCCl` (93%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Br-].[Br-].[Mn+2]` | `[Br-].[Br-].[Mn+2]` (97%) | `__ABSENT__` (3%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #2913  yield=22.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #22)

```
C=CCc1ccc(-c2ccccc2)cc1>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.7%) | `graphite_felt` (0.1%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (81.5%) | `copper` (14.2%) | `sacrificial_zinc` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (89.9%) | `NBu4` (3.3%) | `Li` (3.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (87.3%) | `PF6` (3.8%) | `Br` (3.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (72.5%) | `acid_anhydride` (5.2%) | `sulfonic_acid` (4.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `brønsted_acid_cat` (0.1%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (83.5%) | `acid_anhydride_solvent` (15.6%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (99%) | `OC(C(F)(F)F)C(F)(F` (99%) | `[H+].[OH-]` (99%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (99%) | `OB(O)B(O)O` (99%) | `O=O` (99%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (100%) | `__ABSENT__` (1%) | `O=S(=O)([O-])C(F)(` (0%) | set ✗ / any ✓ |

---

### Reaction #2914  yield=21.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #23)

```
C=CCc1ccc(-c2ccccc2)cc1>>CC(=O)OC[C@H](OC(C)=O)[C@H](OC(C)=O)c1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.7%) | `graphite_felt` (0.1%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (81.5%) | `copper` (14.2%) | `sacrificial_zinc` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (89.9%) | `NBu4` (3.3%) | `Li` (3.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (87.3%) | `PF6` (3.8%) | `Br` (3.5%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (72.5%) | `acid_anhydride` (5.2%) | `sulfonic_acid` (4.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `brønsted_acid_cat` (0.1%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (83.5%) | `acid_anhydride_solvent` (15.6%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (99%) | `OC(C(F)(F)F)C(F)(F` (99%) | `[H+].[OH-]` (99%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (99%) | `OB(O)B(O)O` (99%) | `O=O` (99%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (100%) | `__ABSENT__` (1%) | `O=S(=O)([O-])C(F)(` (0%) | set ✗ / any ✓ |

---

### Reaction #2915  yield=21.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #24)

```
C=CCc1ccc2cc(O)ccc2c1>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1ccc2cc(OC(C)=O)ccc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (1.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (89.1%) | `graphite_felt` (5.4%) | `carbon_felt` (1.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.6%) | `copper` (3.2%) | `carbon` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `platinum_wire` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (55.0%) | `NBu4` (24.4%) | `ABSENT` (10.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (93.7%) | `ABSENT` (2.5%) | `PF6` (2.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (65.8%) | `sulfonic_acid` (3.7%) | `acid_anhydride` (2.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `ferrocene_mediator` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (63.7%) | `acid_anhydride_solvent` (27.0%) | `ABSENT` (3.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (98%) | `OC(C(F)(F)F)C(F)(F` (87%) | `CC(=O)O` (39%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `O=S(=O)(O)C(F)(F)F` (69%) | `__OTHER__` (23%) | `O=O` (16%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `[Br-].[Br-].[Mn+2]` (16%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2916  yield=23.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #25)

```
C=CCc1ccccc1C>>CC(=O)OC[C@@H](OC(C)=O)[C@@H](OC(C)=O)c1ccccc1C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (88.2%) | `graphite_generic` (7.6%) | `graphite_felt` (3.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.1%) | `copper` (2.4%) | `nickel` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `platinum_wire` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (38.1%) | `Li` (36.2%) | `NBu4` (13.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (70.8%) | `ClO4` (17.3%) | `PF6` (6.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (44.3%) | `acid_anhydride` (7.3%) | `sulfonic_acid` (2.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `organic_neutral_cat` (0.1%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (56.3%) | `acid_anhydride_solvent` (24.0%) | `polar_aprotic_nitrile` (13.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (98%) | `OC(C(F)(F)F)C(F)(F` (91%) | `[H+].[OH-]` (63%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `O=S(=O)(O)C(F)(F)F` (71%) | `CC[Si](CC)CC` (12%) | `__OTHER__` (10%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (72%) | `[Br-].[Br-].[Mn+2]` (11%) | `O=C1OC2(c3ccccc31)` (0%) | set ✓ / any ✓ |

---

### Reaction #2917  yield=25.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #26)

```
C=CCc1ccc(OC(C)=O)cc1>>CC(=O)OC[C@@H](OC(C)=O)[C@H](OC(C)=O)c1ccc(OC(C)=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (96.9%) | `graphite_felt` (2.7%) | `reticulated_vitreous_carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.5%) | `copper` (3.2%) | `carbon` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.4%) | `platinum_plate` (1.2%) | `platinum_wire` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (77.3%) | `NBu4` (8.3%) | `K` (4.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.4%) | `ABSENT` (2.9%) | `Br` (1.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (67.7%) | `acid_anhydride` (3.3%) | `sulfonic_acid` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.1%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `acid_anhydride_solvent` (72.3%) | `polar_protic_acid` (20.5%) | `ABSENT` (4.7%) | ✓ |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (93%) | `CC(=O)OC(C)=O` (80%) | `[H+].[OH-]` (14%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `O=S(=O)(O)C(F)(F)F` (95%) | `__OTHER__` (27%) | `O=O` (13%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `[Br-].[Br-].[Mn+2]` (41%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2918  yield=25.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #26)

```
C=CCc1ccc(OC(C)=O)cc1>>CC(=O)OC[C@@H](OC(C)=O)[C@H](OC(C)=O)c1ccc(OC(C)=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (96.9%) | `graphite_felt` (2.7%) | `reticulated_vitreous_carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.5%) | `copper` (3.2%) | `carbon` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.4%) | `platinum_plate` (1.2%) | `platinum_wire` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (77.3%) | `NBu4` (8.3%) | `K` (4.9%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (90.4%) | `ABSENT` (2.9%) | `Br` (1.8%) | ✓ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (67.7%) | `acid_anhydride` (3.3%) | `sulfonic_acid` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.1%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `acid_anhydride_solvent` (72.3%) | `polar_protic_acid` (20.5%) | `ABSENT` (4.7%) | ✓ |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (93%) | `CC(=O)OC(C)=O` (80%) | `[H+].[OH-]` (14%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `O=S(=O)(O)C(F)(F)F` (95%) | `__OTHER__` (27%) | `O=O` (13%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `[Br-].[Br-].[Mn+2]` (41%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2919  yield=30.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #28)

```
C=CCc1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc([C@@H](O)[C@@H](O)CO)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (74.8%) | `platinum` (24.7%) | `sacrificial_zinc` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_felt` (48.6%) | `platinum_generic` (25.4%) | `carbon_cloth` (12.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.2%) | `carbon` (0.6%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (82.1%) | `platinum_plate` (14.1%) | `platinum_foil` (2.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `K` (70.5%) | `Li` (12.4%) | `NBu4` (6.7%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `carboxylate` (57.2%) | `molecular_no_ion` (29.7%) | `ClO4` (8.9%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `carboxylic_acid` (6.9%) | `cf3_source` (3.8%) | `aryl_iodide_mediator` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `organic_neutral_cat` (3.5%) | `pyridine_organocat` (1.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_aprotic_nitrile` (76.6%) | `halogenated_aliphatic` (9.7%) | `cyclic_ether` (3.5%) | ✗ |
| 溶剂 set | 79 | `CC(=O)O` + `CC(=O)OC(C)=O` + `CO` + `O` | `CC#N` (98%) | `O` (48%) | `ClCCl` (42%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `[Br-].[Li+]` + `O=C1CCC(=O)N1Br` | `O=C(O)C(F)(F)F` (21%) | `CC(=O)OC(C)=O` (8%) | `O=CO` (8%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2920  yield=30.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #28)

```
C=CCc1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc([C@@H](O)[C@@H](O)CO)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (74.8%) | `platinum` (24.7%) | `sacrificial_zinc` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_felt` (48.6%) | `platinum_generic` (25.4%) | `carbon_cloth` (12.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.2%) | `carbon` (0.6%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (82.1%) | `platinum_plate` (14.1%) | `platinum_foil` (2.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (70.5%) | `Li` (12.4%) | `NBu4` (6.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (57.2%) | `molecular_no_ion` (29.7%) | `ClO4` (8.9%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `carboxylic_acid` (6.9%) | `cf3_source` (3.8%) | `aryl_iodide_mediator` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `organic_neutral_cat` (3.5%) | `pyridine_organocat` (1.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_aprotic_nitrile` (76.6%) | `halogenated_aliphatic` (9.7%) | `cyclic_ether` (3.5%) | ✗ |
| 溶剂 set | 79 | `CC(=O)O` + `CC(=O)OC(C)=O` + `CO` + `O` | `CC#N` (98%) | `O` (48%) | `ClCCl` (42%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `[Br-].[Li+]` + `O=C1CCC(=O)N1Br` | `O=C(O)C(F)(F)F` (21%) | `CC(=O)OC(C)=O` (8%) | `O=CO` (8%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2921  yield=30.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #30)

```
C=CCc1ccc(C)cc1>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1ccc(C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (1.0%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (90.9%) | `graphite_felt` (5.1%) | `reticulated_vitreous_carbon` (2.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (71.0%) | `copper` (22.4%) | `sacrificial_zinc` (2.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.6%) | `platinum_plate` (1.0%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.9%) | `divided` (1.8%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (80.8%) | `NBu4` (5.5%) | `Li` (5.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (84.6%) | `Br` (3.5%) | `ClO4` (3.4%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (67.7%) | `sulfonic_acid` (4.7%) | `acid_anhydride` (2.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `Fe_complex` (0.1%) | `ferrocene_mediator` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (46.0%) | `acid_anhydride_solvent` (31.2%) | `ABSENT` (19.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `OC(C(F)(F)F)C(F)(F` (95%) | `ClCCl` (93%) | `[H+].[OH-]` (70%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (96%) | `O=O` (90%) | `OB(O)B(O)O` (85%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (79%) | `__ABSENT__` (39%) | `[Pt]` (0%) | set ✗ / any ✓ |

---

### Reaction #2922  yield=30.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #31)

```
C=CCc1ccc(C)cc1>>CC(=O)OC[C@@H](OC(C)=O)[C@@H](OC(C)=O)c1ccc(C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (1.0%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (90.9%) | `graphite_felt` (5.1%) | `reticulated_vitreous_carbon` (2.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (71.0%) | `copper` (22.4%) | `sacrificial_zinc` (2.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.6%) | `platinum_plate` (1.0%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.9%) | `divided` (1.8%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (80.8%) | `NBu4` (5.5%) | `Li` (5.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (84.6%) | `Br` (3.5%) | `ClO4` (3.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (67.7%) | `sulfonic_acid` (4.7%) | `acid_anhydride` (2.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `Fe_complex` (0.1%) | `ferrocene_mediator` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (46.0%) | `acid_anhydride_solvent` (31.2%) | `ABSENT` (19.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `OC(C(F)(F)F)C(F)(F` (95%) | `ClCCl` (93%) | `[H+].[OH-]` (70%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (96%) | `O=O` (90%) | `OB(O)B(O)O` (85%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (79%) | `__ABSENT__` (39%) | `[Pt]` (0%) | set ✗ / any ✓ |

---

### Reaction #2923  yield=38.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #32)

```
C=CCc1cccc(C)c1>>CC(=O)OC[C@@H](OC(C)=O)[C@@H](OC(C)=O)c1cccc(C)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.4%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.0%) | `graphite_felt` (0.2%) | `glassy_carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.7%) | `copper` (5.7%) | `sacrificial_zinc` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.7%) | `platinum_plate` (1.1%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (57.8%) | `NBu4` (28.2%) | `ABSENT` (5.4%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (92.2%) | `PF6` (3.3%) | `ABSENT` (1.8%) | ✓ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (60.5%) | `acid_anhydride` (4.5%) | `sulfonic_acid` (4.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `brønsted_acid_cat` (0.1%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (48.7%) | `acid_anhydride_solvent` (45.6%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (100%) | `[H+].[OH-]` (96%) | `OC(C(F)(F)F)C(F)(F` (90%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (99%) | `OB(O)B(O)O` (99%) | `O=O` (97%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (97%) | `__ABSENT__` (26%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #2924  yield=38.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #33)

```
C=CCc1cccc(C)c1>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1cccc(C)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.4%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.0%) | `graphite_felt` (0.2%) | `glassy_carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.7%) | `copper` (5.7%) | `sacrificial_zinc` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.7%) | `platinum_plate` (1.1%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (57.8%) | `NBu4` (28.2%) | `ABSENT` (5.4%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (92.2%) | `PF6` (3.3%) | `ABSENT` (1.8%) | ✓ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (60.5%) | `acid_anhydride` (4.5%) | `sulfonic_acid` (4.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `brønsted_acid_cat` (0.1%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (48.7%) | `acid_anhydride_solvent` (45.6%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (100%) | `[H+].[OH-]` (96%) | `OC(C(F)(F)F)C(F)(F` (90%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (99%) | `OB(O)B(O)O` (99%) | `O=O` (97%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (97%) | `__ABSENT__` (26%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #2925  yield=38.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #33)

```
C=CCc1cccc(C)c1>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1cccc(C)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.4%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.0%) | `graphite_felt` (0.2%) | `glassy_carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.7%) | `copper` (5.7%) | `sacrificial_zinc` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.7%) | `platinum_plate` (1.1%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (57.8%) | `NBu4` (28.2%) | `ABSENT` (5.4%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (92.2%) | `PF6` (3.3%) | `ABSENT` (1.8%) | ✓ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (60.5%) | `acid_anhydride` (4.5%) | `sulfonic_acid` (4.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `brønsted_acid_cat` (0.1%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (48.7%) | `acid_anhydride_solvent` (45.6%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (100%) | `[H+].[OH-]` (96%) | `OC(C(F)(F)F)C(F)(F` (90%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (99%) | `OB(O)B(O)O` (99%) | `O=O` (97%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (97%) | `__ABSENT__` (26%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #2926  yield=32.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #35)

```
C=CCc1cccc(C(=O)OC)c1>>COC(=O)c1cccc([C@H](OC(C)=O)[C@H](COC(C)=O)OC(C)=O)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (97.3%) | `graphite_felt` (1.5%) | `reticulated_vitreous_carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.3%) | `copper` (1.8%) | `carbon` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.0%) | `platinum_plate` (0.7%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (82.5%) | `NBu4` (7.8%) | `ABSENT` (4.4%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (78.5%) | `ClO4` (10.3%) | `PF6` (4.9%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (34.1%) | `carboxylic_acid` (6.2%) | `acid_anhydride` (5.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `Fe_complex` (0.2%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (58.7%) | `ABSENT` (18.4%) | `acid_anhydride_solvent` (13.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (95%) | `CC(=O)O` (57%) | `[H+].[OH-]` (37%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `CC[N+](CC)(CC)CC.F` + `[Br-].[Li+]` + `O=C1CCC(=O)N1Br` | `O=S(=O)(O)C(F)(F)F` (55%) | `__OTHER__` (46%) | `O=O` (45%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (82%) | `[Br-].[Br-].[Mn+2]` (38%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #2927  yield=35.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #36)

```
C=CCc1cccs1>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1ccc(OC(C)=O)s1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (87.0%) | `graphite_generic` (3.8%) | `reticulated_vitreous_carbon` (3.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.2%) | `copper` (4.9%) | `nickel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `stainless_steel_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.4%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (95.9%) | `NBu4` (3.3%) | `ABSENT` (0.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (93.0%) | `PF6` (4.0%) | `ClO4` (1.2%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (65.7%) | `acid_anhydride` (4.8%) | `sulfonic_acid` (1.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (87.6%) | `organic_neutral_cat` (8.1%) | `Fe_complex` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (90.2%) | `acid_anhydride_solvent` (3.0%) | `halogenated_aliphatic` (2.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (98%) | `CC(=O)O` (60%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (73%) | `CC[Si](CC)CC` (63%) | `OB(O)B(O)O` (61%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (25%) | `__ABSENT__` (6%) | `COc1c(I)cc2c(c1I)-` (0%) | set ✗ / any ✓ |

---

### Reaction #2928  yield=39.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #37)

```
C=CCc1cccs1>>CC(=O)OC[C@H](OC(C)=O)[C@H](OC(C)=O)c1ccc(OC(C)=O)s1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (87.0%) | `graphite_generic` (3.8%) | `reticulated_vitreous_carbon` (3.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.2%) | `copper` (4.9%) | `nickel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.3%) | `stainless_steel_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.4%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (95.9%) | `NBu4` (3.3%) | `ABSENT` (0.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (93.0%) | `PF6` (4.0%) | `ClO4` (1.2%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (65.7%) | `acid_anhydride` (4.8%) | `sulfonic_acid` (1.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (87.6%) | `organic_neutral_cat` (8.1%) | `Fe_complex` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (90.2%) | `acid_anhydride_solvent` (3.0%) | `halogenated_aliphatic` (2.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (98%) | `CC(=O)O` (60%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (73%) | `CC[Si](CC)CC` (63%) | `OB(O)B(O)O` (61%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (25%) | `__ABSENT__` (6%) | `COc1c(I)cc2c(c1I)-` (0%) | set ✗ / any ✓ |

---

### Reaction #2929  yield=34.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #38)

```
C=CCc1ccc(Cl)c(Cl)c1>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1ccc(Cl)c(Cl)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (96.5%) | `graphite_felt` (2.0%) | `reticulated_vitreous_carbon` (0.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.0%) | `copper` (4.3%) | `carbon` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.8%) | `platinum_plate` (0.1%) | `platinum_wire` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (94.9%) | `NBu4` (1.9%) | `Li` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (92.5%) | `PF6` (2.6%) | `ClO4` (1.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (79.7%) | `sulfonic_acid` (2.7%) | `acid_anhydride` (2.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `organic_neutral_cat` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (63.7%) | `acid_anhydride_solvent` (33.1%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (98%) | `OC(C(F)(F)F)C(F)(F` (91%) | `[H+].[OH-]` (74%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (87%) | `O=O` (80%) | `OB(O)B(O)O` (75%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (94%) | `__ABSENT__` (42%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✗ / any ✓ |

---

### Reaction #2930  yield=32.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #39)

```
C=CCc1ccc(Cl)c(Cl)c1>>CC(=O)OC[C@H](OC(C)=O)[C@H](OC(C)=O)c1ccc(Cl)c(Cl)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (96.5%) | `graphite_felt` (2.0%) | `reticulated_vitreous_carbon` (0.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.0%) | `copper` (4.3%) | `carbon` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.8%) | `platinum_plate` (0.1%) | `platinum_wire` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (94.9%) | `NBu4` (1.9%) | `Li` (1.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (92.5%) | `PF6` (2.6%) | `ClO4` (1.6%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (79.7%) | `sulfonic_acid` (2.7%) | `acid_anhydride` (2.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `organic_neutral_cat` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (63.7%) | `acid_anhydride_solvent` (33.1%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (98%) | `OC(C(F)(F)F)C(F)(F` (91%) | `[H+].[OH-]` (74%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (87%) | `O=O` (80%) | `OB(O)B(O)O` (75%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (94%) | `__ABSENT__` (42%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✗ / any ✓ |

---

### Reaction #2931  yield=38.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #40)

```
C=CCc1ccc2cc(Br)ccc2c1>>CC(=O)OCC(OC(C)=O)C(OC(C)=O)c1ccc2cc(Br)ccc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `platinum` (1.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (84.5%) | `graphite_felt` (10.7%) | `carbon_felt` (3.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.7%) | `copper` (1.9%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.1%) | `platinum_wire` (0.5%) | `platinum_plate` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (69.0%) | `NBu4` (16.9%) | `Li` (8.4%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (93.2%) | `ClO4` (3.2%) | `ABSENT` (1.3%) | ✓ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (65.0%) | `sulfonic_acid` (3.2%) | `acid_anhydride` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.1%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `acid_anhydride_solvent` (49.9%) | `polar_protic_acid` (43.1%) | `ABSENT` (4.6%) | ✓ |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (87%) | `CC(=O)OC(C)=O` (73%) | `[H+].[OH-]` (19%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C(O)O.[Na]` | `O=S(=O)(O)C(F)(F)F` (85%) | `__OTHER__` (44%) | `O=O` (28%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (86%) | `[Br-].[Br-].[Mn+2]` (14%) | `O.O.[K+].[K+].[O]=` (0%) | set ✓ / any ✓ |

---

### Reaction #2932  yield=50.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #41)

```
C=CCc1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc([C@H](O)[C@@H](O)CO)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (74.8%) | `platinum` (24.7%) | `sacrificial_zinc` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_felt` (48.6%) | `platinum_generic` (25.4%) | `carbon_cloth` (12.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.2%) | `carbon` (0.6%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (82.1%) | `platinum_plate` (14.1%) | `platinum_foil` (2.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (70.5%) | `Li` (12.4%) | `NBu4` (6.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (57.2%) | `molecular_no_ion` (29.7%) | `ClO4` (8.9%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `carboxylic_acid` (6.9%) | `cf3_source` (3.8%) | `aryl_iodide_mediator` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.7%) | `organic_neutral_cat` (3.5%) | `pyridine_organocat` (1.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_aprotic_nitrile` (76.6%) | `halogenated_aliphatic` (9.7%) | `cyclic_ether` (3.5%) | ✗ |
| 溶剂 set | 79 | `CC(=O)O` + `CC(=O)OC(C)=O` + `CO` + `O` | `CC#N` (98%) | `O` (48%) | `ClCCl` (42%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `[Br-].[Li+]` + `O=C1CCC(=O)N1Br` | `O=C(O)C(F)(F)F` (21%) | `CC(=O)OC(C)=O` (8%) | `O=CO` (8%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #2933  yield=48.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #42)

```
C=CCc1ccc(Cl)cc1>>OC[C@H](O)[C@H](O)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.0%) | `platinum` (5.9%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (88.4%) | `graphite_felt` (5.2%) | `carbon_cloth` (2.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `stainless_steel` (0.4%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.5%) | `platinum_generic` (0.9%) | `stainless_steel_generic` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (66.6%) | `K` (22.1%) | `Li` (7.9%) | ✗ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (63.9%) | `ClO4` (15.7%) | `Br` (6.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `carboxylic_acid` (11.4%) | `as_solvent_polar_aprotic_sulfo` (6.9%) | `ABSENT` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `organic_neutral_cat` (0.2%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `halogenated_aliphatic` (34.4%) | `polar_aprotic_nitrile` (31.0%) | `polar_protic_alcohol` (15.5%) | ✗ |
| 溶剂 set | 79 | `CC(=O)O` + `CC(=O)OC(C)=O` + `CO` + `O` | `ClCCl` (65%) | `O` (35%) | `CC#N` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `[Br-].[Li+]` + `O=C1CCC(=O)N1Br` | `CC(=O)OC(C)=O` (24%) | `O=C(O)C(F)(F)F` (18%) | `[Br-].[Li+]` (10%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[O]=[Fe][O][Fe]=[O` (1%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #2934  yield=48.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #42)

```
C=CCc1ccc(Cl)cc1>>OC[C@H](O)[C@H](O)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.0%) | `platinum` (5.9%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (88.4%) | `graphite_felt` (5.2%) | `carbon_cloth` (2.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `stainless_steel` (0.4%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.5%) | `platinum_generic` (0.9%) | `stainless_steel_generic` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (66.6%) | `K` (22.1%) | `Li` (7.9%) | ✗ |
| 电解质 anion | 26 | `BF4` | `carboxylate` (63.9%) | `ClO4` (15.7%) | `Br` (6.3%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `carboxylic_acid` (11.4%) | `as_solvent_polar_aprotic_sulfo` (6.9%) | `ABSENT` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `organic_neutral_cat` (0.2%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `halogenated_aliphatic` (34.4%) | `polar_aprotic_nitrile` (31.0%) | `polar_protic_alcohol` (15.5%) | ✗ |
| 溶剂 set | 79 | `CC(=O)O` + `CC(=O)OC(C)=O` + `CO` + `O` | `ClCCl` (65%) | `O` (35%) | `CC#N` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `[Br-].[Li+]` + `O=C1CCC(=O)N1Br` | `CC(=O)OC(C)=O` (24%) | `O=C(O)C(F)(F)F` (18%) | `[Br-].[Li+]` (10%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[O]=[Fe][O][Fe]=[O` (1%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #2935  yield=47.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #44)

```
C=CCc1ccc(OC(F)(F)F)cc1>>OC[C@H](O)[C@@H](O)c1ccc(OC(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (77.2%) | `graphite_felt` (20.0%) | `carbon_cloth` (1.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.2%) | `carbon` (0.5%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.0%) | `platinum_generic` (2.6%) | `carbon_felt` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (66.1%) | `Li` (23.6%) | `ABSENT` (8.5%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (44.9%) | `carboxylate` (24.0%) | `molecular_no_ion` (12.0%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `carboxylic_acid` (4.7%) | `iodide_anion` (4.5%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `organic_neutral_cat` (0.4%) | `pyridine_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `halogenated_aliphatic` (75.8%) | `polar_aprotic_nitrile` (9.3%) | `polar_protic_alcohol` (6.8%) | ✗ |
| 溶剂 set | 79 | `CC(=O)O` + `CC(=O)OC(C)=O` + `CO` + `O` | `ClCCl` (99%) | `O` (1%) | `CC(=O)O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `CC[N+](CC)(CC)CC.F` (13%) | `CC(=O)OC(C)=O` (9%) | `O=S(=O)(O)C(F)(F)F` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[O]=[Fe][O][Fe]=[O` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✓ / any ✓ |

---

### Reaction #2936  yield=47.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #44)

```
C=CCc1ccc(OC(F)(F)F)cc1>>OC[C@H](O)[C@@H](O)c1ccc(OC(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_felt` (77.2%) | `graphite_felt` (20.0%) | `carbon_cloth` (1.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.2%) | `carbon` (0.5%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.0%) | `platinum_generic` (2.6%) | `carbon_felt` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (66.1%) | `Li` (23.6%) | `ABSENT` (8.5%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (44.9%) | `carboxylate` (24.0%) | `molecular_no_ion` (12.0%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `carboxylic_acid` (4.7%) | `iodide_anion` (4.5%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `organic_neutral_cat` (0.4%) | `pyridine_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `halogenated_aliphatic` (75.8%) | `polar_aprotic_nitrile` (9.3%) | `polar_protic_alcohol` (6.8%) | ✗ |
| 溶剂 set | 79 | `CC(=O)O` + `CC(=O)OC(C)=O` + `CO` + `O` | `ClCCl` (99%) | `O` (1%) | `CC(=O)O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `CC[N+](CC)(CC)CC.F` (13%) | `CC(=O)OC(C)=O` (9%) | `O=S(=O)(O)C(F)(F)F` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[O]=[Fe][O][Fe]=[O` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✓ / any ✓ |

---

### Reaction #2937  yield=44.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #46)

```
C=CCc1ccccc1C>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1ccccc1C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (88.2%) | `graphite_generic` (7.6%) | `graphite_felt` (3.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.1%) | `copper` (2.4%) | `nickel` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `platinum_wire` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (38.1%) | `Li` (36.2%) | `NBu4` (13.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (70.8%) | `ClO4` (17.3%) | `PF6` (6.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (44.3%) | `acid_anhydride` (7.3%) | `sulfonic_acid` (2.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `organic_neutral_cat` (0.1%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (56.3%) | `acid_anhydride_solvent` (24.0%) | `polar_aprotic_nitrile` (13.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (98%) | `OC(C(F)(F)F)C(F)(F` (91%) | `[H+].[OH-]` (63%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `O=S(=O)(O)C(F)(F)F` (71%) | `CC[Si](CC)CC` (12%) | `__OTHER__` (10%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (72%) | `[Br-].[Br-].[Mn+2]` (11%) | `O=C1OC2(c3ccccc31)` (0%) | set ✓ / any ✓ |

---

### Reaction #2938  yield=44.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #46)

```
C=CCc1ccccc1C>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1ccccc1C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (88.2%) | `graphite_generic` (7.6%) | `graphite_felt` (3.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.1%) | `copper` (2.4%) | `nickel` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `platinum_wire` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (38.1%) | `Li` (36.2%) | `NBu4` (13.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (70.8%) | `ClO4` (17.3%) | `PF6` (6.0%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (44.3%) | `acid_anhydride` (7.3%) | `sulfonic_acid` (2.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `organic_neutral_cat` (0.1%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (56.3%) | `acid_anhydride_solvent` (24.0%) | `polar_aprotic_nitrile` (13.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (98%) | `OC(C(F)(F)F)C(F)(F` (91%) | `[H+].[OH-]` (63%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `O=S(=O)(O)C(F)(F)F` (71%) | `CC[Si](CC)CC` (12%) | `__OTHER__` (10%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (72%) | `[Br-].[Br-].[Mn+2]` (11%) | `O=C1OC2(c3ccccc31)` (0%) | set ✓ / any ✓ |

---

### Reaction #2939  yield=42.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #48)

```
C=CCc1ccc(OC(C)=O)cc1>>CC(=O)OC[C@@H](OC(C)=O)[C@@H](OC(C)=O)c1ccc(OC(C)=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (96.9%) | `graphite_felt` (2.7%) | `reticulated_vitreous_carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.5%) | `copper` (3.2%) | `carbon` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.4%) | `platinum_plate` (1.2%) | `platinum_wire` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (77.3%) | `NBu4` (8.3%) | `K` (4.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Cl` | `BF4` (90.4%) | `ABSENT` (2.9%) | `Br` (1.8%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (67.7%) | `acid_anhydride` (3.3%) | `sulfonic_acid` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.1%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `acid_anhydride_solvent` (72.3%) | `polar_protic_acid` (20.5%) | `ABSENT` (4.7%) | ✓ |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (93%) | `CC(=O)OC(C)=O` (80%) | `[H+].[OH-]` (14%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `O=S(=O)(O)C(F)(F)F` (95%) | `__OTHER__` (27%) | `O=O` (13%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `[Br-].[Br-].[Mn+2]` (41%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2940  yield=59.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #49)

```
C=CCc1ccc(F)cc1>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.4%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (98.0%) | `graphite_felt` (1.4%) | `graphite_generic` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (81.7%) | `copper` (12.2%) | `sacrificial_zinc` (3.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `platinum_wire` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (93.5%) | `K` (2.2%) | `NBu4` (1.6%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (84.7%) | `Br` (4.6%) | `ClO4` (3.6%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (67.4%) | `acid_anhydride` (5.5%) | `sulfonic_acid` (2.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (58.9%) | `acid_anhydride_solvent` (38.6%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `ClCCl` (99%) | `[H+].[OH-]` (98%) | `OC(C(F)(F)F)C(F)(F` (94%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (97%) | `O=O` (94%) | `OB(O)B(O)O` (94%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (98%) | `__ABSENT__` (28%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✓ |

---

### Reaction #2941  yield=58.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #50)

```
C=CCc1ccccc1>>CC(=O)OC[C@@H](OC(C)=O)[C@@H](OC(C)=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (99.9%) | `reticulated_vitreous_carbon` (0.0%) | `graphite_felt` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (59.6%) | `copper` (34.8%) | `sacrificial_zinc` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.9%) | `platinum_plate` (0.1%) | `carbon_cloth` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `alkyl_ammonium` | `NEt4` (96.3%) | `NBu4` (1.2%) | `Li` (1.1%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (91.2%) | `PF6` (4.0%) | `ClO4` (2.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (68.2%) | `sulfonic_acid` (6.9%) | `acid_anhydride` (6.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `brønsted_acid_cat` (0.1%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (85.7%) | `acid_anhydride_solvent` (12.9%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `[H+].[OH-]` | `[H+].[OH-]` (100%) | `ClCCl` (100%) | `OC(C(F)(F)F)C(F)(F` (100%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Br-].[Br-].[Mn+2]` | `[Br-].[Br-].[Mn+2]` (100%) | `c1ccncc1` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #2942  yield=58.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #51)

```
C=CCc1ccc(Br)cc1>>CC(=O)OC[C@H](OC(C)=O)[C@@H](OC(C)=O)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_cloth` (96.9%) | `graphite_felt` (2.5%) | `reticulated_vitreous_carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (81.1%) | `copper` (15.3%) | `carbon` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.7%) | `platinum_plate` (0.2%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (90.8%) | `NBu4` (4.3%) | `Li` (3.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (93.1%) | `ClO4` (2.7%) | `PF6` (1.5%) | ✗ |
| 试剂大类 | 103 | `acid_anhydride` | `cf3_source` (71.0%) | `sulfonic_acid` (5.6%) | `acid_anhydride` (3.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `brønsted_acid_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_protic_acid` (66.5%) | `acid_anhydride_solvent` (28.7%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `O` | `ClCCl` (99%) | `[H+].[OH-]` (95%) | `OC(C(F)(F)F)C(F)(F` (95%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)OC(C)=O` + `O=C(O)C(F)(F)F` + `O=C([O-])[O-].[Na+` | `__OTHER__` (97%) | `O=O` (93%) | `OB(O)B(O)O` (92%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Br-].[Br-].[Mn+2]` (95%) | `__ABSENT__` (15%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #2943  yield=75.0%

**Source paper**: [`Synthesis/2025_Synthesis_2025_57_3_597-605.json`](reactions_by_journal_alkene_ec_audited/Synthesis/2025_Synthesis_2025_57_3_597-605.json) (反应 idx 在该 JSON 内 = #52)

```
C/C=C/c1ccccc1>>CC(=O)OC(C)C(OC(C)=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `ABSENT` (0.8%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `graphite_generic` (29.4%) | `carbon_generic` (22.3%) | `carbon_felt` (18.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.9%) | `sacrificial_zinc` (1.5%) | `ABSENT` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (67.0%) | `platinum_plate` (22.2%) | `platinum_foil` (5.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (81.2%) | `ABSENT` (18.2%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (62.4%) | `NBu4` (26.4%) | `ABSENT` (6.4%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (61.9%) | `ClO4` (20.5%) | `ABSENT` (5.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (48.4%) | `carboxylic_acid` (5.8%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `organic_neutral_cat` (0.4%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_acid` | `polar_aprotic_nitrile` (43.7%) | `polar_protic_acid` (25.2%) | `ABSENT` (10.2%) | ✓ |
| 溶剂 set | 79 | `CC(=O)O` + `CC(=O)OC(C)=O` + `O` | `CC#N` (62%) | `CC(=O)OC(C)=O` (31%) | `CC(=O)O` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[SiH](CC)CC` + `O=O` + `[Li+].[O-][Cl+3]([` + `OB(O)B(O)O` | `O=O` (52%) | `OC(C(F)(F)F)C(F)(F` (27%) | `[Li+].[O-][Cl+3]([` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `COC(=O)CC[C@@H]1C2` | `__ABSENT__` (87%) | `COC(=O)CC[C@@H]1C2` (8%) | `__OTHER__` (0%) | set ✗ / any ✓ |

---

### Reaction #2944  yield=81.0%

**Source paper**: [`Synthetic/2025_Synthetic_Communications_2025_55_9_661-671.json`](reactions_by_journal_alkene_ec_audited/Synthetic/2025_Synthetic_Communications_2025_55_9_661-671.json) (反应 idx 在该 JSON 内 = #0)

```
O=S(O)CF.[Na].C=C(C(=O)n1c(-c2ccccc2)nc2ccccc21)c1ccccc1>>O=C1n2c(nc3ccccc32)-c2ccccc2C1(CCF)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.1%) | `platinum` (2.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_plate` (80.9%) | `glassy_carbon` (8.3%) | `carbon_felt` (7.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (60.4%) | `platinum` (36.7%) | `carbon` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_generic` | `nickel_plate` (35.4%) | `nickel_foam` (18.8%) | `platinum_generic` (18.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (97.7%) | `Li` (0.5%) | `K` (0.5%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `Br` (36.9%) | `BF4` (29.0%) | `carboxylate` (25.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (26.3%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `lanthanide_complex` (0.2%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.3%) | `polar_protic_alcohol` (8.4%) | `polar_aprotic_sulfoxide` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `ClCCCl` (7%) | `CO` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl][Ce]([Cl])[Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #2945  yield=43.0%

**Source paper**: [`TetrahedronLett/2025_Tetrahedron_Letters_2025_154155389.json`](reactions_by_journal_alkene_ec_audited/TetrahedronLett/2025_Tetrahedron_Letters_2025_154155389.json) (反应 idx 在该 JSON 内 = #0)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCSc1ccccc1C(=O)O>>O=C1OC(C[Se]c2ccccc2)CSc2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_generic` | `platinum_plate` (85.2%) | `platinum_generic` (14.8%) | `platinum_wire` (0.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (91.0%) | `carbon` (8.8%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (64.5%) | `platinum_generic` (26.7%) | `reticulated_vitreous_carbon` (5.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (66.0%) | `ABSENT` (33.6%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (62.4%) | `NBu4` (23.4%) | `Li` (7.9%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (58.6%) | `PF6` (18.1%) | `ClO4` (8.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (25.7%) | `tellurium_reagent` (1.9%) | `metal_oxide_oxidant` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `nhpi_mediator` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (75.8%) | `halogenated_aliphatic` (19.1%) | `ABSENT` (2.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `OCC(F)(F)F` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `O=C1c2ccccc2C(=O)N` (0%) | set ✓ / any ✓ |

---

### Reaction #2946  yield=55.0%

**Source paper**: [`TetrahedronLett/2025_Tetrahedron_Letters_2025_154155389.json`](reactions_by_journal_alkene_ec_audited/TetrahedronLett/2025_Tetrahedron_Letters_2025_154155389.json) (反应 idx 在该 JSON 内 = #1)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCOc1ccc(C)cc1C(=O)O>>Cc1ccc2c(c1)C(=O)OC(C[Se]c1ccccc1)CO2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_plate` | `platinum_generic` (96.5%) | `platinum_plate` (3.4%) | `unknown_electrode` (0.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.0%) | `platinum_plate` (0.6%) | `platinum_wire` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (73.7%) | `ABSENT` (23.4%) | `divided` (2.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (95.5%) | `NBu4` (3.6%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (85.6%) | `BF4` (7.4%) | `molecular_no_ion` (2.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (26.7%) | `water` (4.4%) | `metal_oxide_oxidant` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Pt_complex` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (88.5%) | `ABSENT` (4.0%) | `polar_aprotic_amide` (3.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `C1CCOC1` (0%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C1c2ccccc2C(=O)N` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #2947  yield=53.0%

**Source paper**: [`TetrahedronLett/2025_Tetrahedron_Letters_2025_154155389.json`](reactions_by_journal_alkene_ec_audited/TetrahedronLett/2025_Tetrahedron_Letters_2025_154155389.json) (反应 idx 在该 JSON 内 = #2)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCOc1cc(Br)ccc1C(=O)O>>O=C1OC(C[Se]c2ccccc2)COc2cc(Br)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_plate` | `platinum_generic` (92.5%) | `platinum_plate` (7.3%) | `platinum_wire` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.4%) | `platinum_wire` (8.0%) | `platinum_plate` (3.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.2%) | `ABSENT` (1.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (99.0%) | `NBu4` (0.8%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (98.3%) | `molecular_no_ion` (0.4%) | `BF4` (0.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (41.4%) | `metal_oxide_oxidant` (1.7%) | `tellurium_reagent` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Pt_complex` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `polar_protic_acid` (0.4%) | `halogenated_aliphatic` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `O=C1c2ccccc2C(=O)N` (0%) | set ✓ / any ✓ |

---

