# Test 预测 part 1 — 反应 #1-#500

[← 返回 INDEX](INDEX.md)

### Reaction #1  yield=11.0%

**Source paper**: [`ACSCatal/2025_ACS_Catalysis_2025_15_6_4450-4459.json`](reactions_by_journal_alkene_ec_audited/ACSCatal/2025_ACS_Catalysis_2025_15_6_4450-4459.json) (反应 idx 在该 JSON 内 = #0)

```
Brc1ccc(C=C2CC2)cc1.C/C(=N\Nc1ccccn1)c1ccc(I)cc1>>C[C@@]1(/N=N/c2ccccn2)c2ccc(I)cc2C2(CC2)[C@@H]1c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.6%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (98.0%) | `carbon_felt` (1.2%) | `graphite_felt` (0.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.5%) | `nickel` (0.7%) | `carbon` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (82.5%) | `platinum_wire` (10.4%) | `platinum_plate` (4.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Na` (80.9%) | `Li` (16.9%) | `K` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (93.0%) | `I` (3.2%) | `Br` (2.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (32.0%) | `primary_amine` (2.3%) | `as_solvent_polar_aprotic_nitri` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (99.2%) | `Pt_complex` (0.5%) | `ionic_organocat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (86.8%) | `ABSENT` (7.8%) | `polar_protic_alcohol` (4.4%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC(C)=O` | `CC#N` (96%) | `O` (1%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Co]` + `__OTHER__` | `__ABSENT__` (100%) | `CC(=O)[O-].CC(=O)[` (0%) | `__OTHER__` (0%) | set ✗ / any ✓ |

---

### Reaction #2  yield=15.0%

**Source paper**: [`ACSCatal/2025_ACS_Catalysis_2025_15_6_4450-4459.json`](reactions_by_journal_alkene_ec_audited/ACSCatal/2025_ACS_Catalysis_2025_15_6_4450-4459.json) (反应 idx 在该 JSON 内 = #1)

```
Brc1ccc(C=C2CC2)cc1.CSc1ccc(/C(C)=N/Nc2ccccn2)cc1>>CSc1ccc2c(c1)C1(CC1)[C@H](c1ccc(Br)cc1)[C@]2(C)/N=N/c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.8%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (58.3%) | `carbon_felt` (34.9%) | `graphite_rod` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `carbon` (0.6%) | `nickel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_wire` (64.0%) | `platinum_generic` (32.2%) | `platinum_plate` (1.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (70.9%) | `ABSENT` (20.4%) | `NBu4` (5.2%) | ✗ |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (31.6%) | `ABSENT` (26.7%) | `ClO4` (23.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.9%) | `as_solvent_polar_aprotic_nitri` (3.0%) | `primary_amine` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.2%) | `pyridine_organocat` (0.9%) | `Pt_complex` (0.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `ABSENT` (91.8%) | `polar_aprotic_nitrile` (7.6%) | `ketone` (0.3%) | ✗ |
| 溶剂 set | 79 | `CCO` + `CC(C)=O` | `__ABSENT__` (100%) | `CC#N` (0%) | `O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` + `__OTHER__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✗ / any ✓ |

---

### Reaction #3  yield=16.0%

**Source paper**: [`ACSCatal/2025_ACS_Catalysis_2025_15_6_4450-4459.json`](reactions_by_journal_alkene_ec_audited/ACSCatal/2025_ACS_Catalysis_2025_15_6_4450-4459.json) (反应 idx 在该 JSON 内 = #2)

```
Brc1ccc(C=C2CC2)cc1.C/C(=N\Nc1ccccn1)c1ccc(C)cc1>>Cc1ccc2c(c1)C1(CC1)[C@H](c1ccc(Br)cc1)[C@]2(C)/N=N/c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.1%) | `platinum` (1.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (69.3%) | `carbon_felt` (20.1%) | `reticulated_vitreous_carbon` (5.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (69.9%) | `platinum_plate` (25.8%) | `platinum_wire` (3.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (39.3%) | `Na` (38.6%) | `ABSENT` (16.8%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (83.1%) | `ABSENT` (8.0%) | `ClO4` (3.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (27.3%) | `as_solvent_polar_aprotic_nitri` (3.3%) | `primary_amine` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.0%) | `Pt_complex` (0.9%) | `pyridine_organocat` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (87.4%) | `ABSENT` (11.5%) | `polar_protic_alcohol` (0.7%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC(C)=O` | `CC#N` (94%) | `__ABSENT__` (0%) | `O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` + `__OTHER__` | `__ABSENT__` (100%) | `CC(=O)[O-].CC(=O)[` (0%) | `__OTHER__` (0%) | set ✗ / any ✓ |

---

### Reaction #4  yield=34.0%

**Source paper**: [`ACSCatal/2025_ACS_Catalysis_2025_15_6_4450-4459.json`](reactions_by_journal_alkene_ec_audited/ACSCatal/2025_ACS_Catalysis_2025_15_6_4450-4459.json) (反应 idx 在该 JSON 内 = #3)

```
Brc1ccc(C=C2CC2)cc1.C/C(=N\Nc1ccccn1)c1ccc(I)cc1>>C[C@]1(/N=N/c2ccccn2)c2ccc(I)cc2C2(CC2)[C@@H]1c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.6%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (98.0%) | `carbon_felt` (1.2%) | `graphite_felt` (0.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.5%) | `nickel` (0.7%) | `carbon` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (82.5%) | `platinum_wire` (10.4%) | `platinum_plate` (4.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Na` (80.9%) | `Li` (16.9%) | `K` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (93.0%) | `I` (3.2%) | `Br` (2.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (32.0%) | `primary_amine` (2.3%) | `as_solvent_polar_aprotic_nitri` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (99.2%) | `Pt_complex` (0.5%) | `ionic_organocat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (86.8%) | `ABSENT` (7.8%) | `polar_protic_alcohol` (4.4%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC(C)=O` | `CC#N` (96%) | `O` (1%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Co]` + `__OTHER__` | `__ABSENT__` (100%) | `CC(=O)[O-].CC(=O)[` (0%) | `__OTHER__` (0%) | set ✗ / any ✓ |

---

### Reaction #5  yield=44.0%

**Source paper**: [`ACSCatal/2025_ACS_Catalysis_2025_15_6_4450-4459.json`](reactions_by_journal_alkene_ec_audited/ACSCatal/2025_ACS_Catalysis_2025_15_6_4450-4459.json) (反应 idx 在该 JSON 内 = #4)

```
Brc1ccc(C=C2CC2)cc1.CSc1ccc(/C(C)=N/Nc2ccccn2)cc1>>CSc1ccc2c(c1)C1(CC1)[C@H](c1ccc(Br)cc1)[C@@]2(C)/N=N/c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.8%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (58.3%) | `carbon_felt` (34.9%) | `graphite_rod` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `carbon` (0.6%) | `nickel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_wire` (64.0%) | `platinum_generic` (32.2%) | `platinum_plate` (1.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (70.9%) | `ABSENT` (20.4%) | `NBu4` (5.2%) | ✗ |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (31.6%) | `ABSENT` (26.7%) | `ClO4` (23.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.9%) | `as_solvent_polar_aprotic_nitri` (3.0%) | `primary_amine` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.2%) | `pyridine_organocat` (0.9%) | `Pt_complex` (0.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `ABSENT` (91.8%) | `polar_aprotic_nitrile` (7.6%) | `ketone` (0.3%) | ✗ |
| 溶剂 set | 79 | `CCO` + `CC(C)=O` | `__ABSENT__` (100%) | `CC#N` (0%) | `O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` + `__OTHER__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✗ / any ✓ |

---

### Reaction #6  yield=49.0%

**Source paper**: [`ACSCatal/2025_ACS_Catalysis_2025_15_6_4450-4459.json`](reactions_by_journal_alkene_ec_audited/ACSCatal/2025_ACS_Catalysis_2025_15_6_4450-4459.json) (反应 idx 在该 JSON 内 = #5)

```
Brc1ccc(C=C2CC2)cc1.C/C(=N\Nc1ccccn1)c1ccc(C)cc1>>Cc1ccc2c(c1)C1(CC1)[C@H](c1ccc(Br)cc1)[C@@]2(C)/N=N/c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.1%) | `platinum` (1.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (69.3%) | `carbon_felt` (20.1%) | `reticulated_vitreous_carbon` (5.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (69.9%) | `platinum_plate` (25.8%) | `platinum_wire` (3.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Li` (39.3%) | `Na` (38.6%) | `ABSENT` (16.8%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `molecular_no_ion` (83.1%) | `ABSENT` (8.0%) | `ClO4` (3.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (27.3%) | `as_solvent_polar_aprotic_nitri` (3.3%) | `primary_amine` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (98.0%) | `Pt_complex` (0.9%) | `pyridine_organocat` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (87.4%) | `ABSENT` (11.5%) | `polar_protic_alcohol` (0.7%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC(C)=O` | `CC#N` (94%) | `__ABSENT__` (0%) | `O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` + `__OTHER__` | `__ABSENT__` (100%) | `CC(=O)[O-].CC(=O)[` (0%) | `__OTHER__` (0%) | set ✗ / any ✓ |

---

### Reaction #7  yield=51.0%

**Source paper**: [`ChemRxiv/2025_ChemRxiv_2025_1-11.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/2025_ChemRxiv_2025_1-11.json) (反应 idx 在该 JSON 内 = #2)

```
Brc1ccc2c3c(ccc(Br)c13)C=C2.C/C(=N\Nc1ccccn1)c1ccc(C)cc1>>Cc1ccc2c(c1)[C@@H]1c3ccc(Br)c4c(Br)ccc(c34)[C@@H]1[C@@]2(C)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `graphite_generic` (46.3%) | `carbon_felt` (34.5%) | `graphite_rod` (9.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (87.4%) | `platinum_generic` (12.6%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NBu4` (47.5%) | `Na` (34.2%) | `Li` (7.1%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `I` (49.5%) | `molecular_no_ion` (17.3%) | `Cl` (17.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (22.1%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (89.9%) | `brønsted_acid_cat` (4.1%) | `organic_neutral_cat` (2.1%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.0%) | `cyclic_ether` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `CC(C)=O` | `CC#N` (100%) | `O` (58%) | `[H+].[OH-]` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Co]` + `__OTHER__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✗ / any ✓ |

---

### Reaction #8  yield=96.0%

**Source paper**: [`AIChE/2025_AIChE_Journal_2025_71_10_e18930.json`](reactions_by_journal_alkene_ec_audited/AIChE/2025_AIChE_Journal_2025_71_10_e18930.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCOCc1ccccc1>>c1ccc(COCC2CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (61.8%) | `platinum` (37.7%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_paper` | `graphite_rod` (34.0%) | `boron_doped_diamond` (30.9%) | `platinum_wire` (10.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.5%) | `carbon` (2.5%) | `stainless_steel` (1.2%) | ✓ |
| 阴极 (细类) | 49 | `unknown_electrode` | `platinum_wire` (54.4%) | `platinum_generic` (25.0%) | `platinum_plate` (15.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.6%) | `ABSENT` (1.3%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `molecular_no_ion` | `Na` (98.9%) | `Li` (0.6%) | `NBu4` (0.3%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `carboxylate` (80.0%) | `molecular_no_ion` (14.3%) | `Br` (3.0%) | ✓ |
| 试剂大类 | 103 | `o2_oxidant` | `ABSENT` (18.5%) | `as_solvent_polar_aprotic_sulfo` (6.6%) | `as_solvent_halogenated_aliphat` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.3%) | `Co_complex` (1.8%) | `Mn_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (57.2%) | `polar_protic_alcohol` (26.9%) | `aqueous` (9.7%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` + `O` | `CC#N` (92%) | `O` (51%) | `ClCCl` (46%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I)cc1` + `F.c1ccncc1` + `CCN(CC)CC.F.F.F` + `O=C([O-])[O-].[Ca+` | `__ABSENT__` (56%) | `O=O` (29%) | `CS(C)=O` (25%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (94%) | `[Fe+2].c1cc[cH-]c1` (2%) | `[Pt]` (1%) | set ✓ / any ✓ |

---

### Reaction #9  yield=62.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #10  yield=31.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #11  yield=51.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #12  yield=54.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #13  yield=38.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #14  yield=56.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #15  yield=51.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NMe4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #16  yield=63.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #17  yield=62.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #18  yield=84.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #19  yield=83.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #20  yield=83.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #21  yield=58.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #22  yield=79.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #23  yield=83.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #24  yield=45.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #25  yield=57.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #26  yield=71.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #27  yield=79.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #28  yield=85.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #29  yield=0.5%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #30  yield=69.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #31  yield=0.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #32  yield=36.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #33  yield=64.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #34  yield=80.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #35  yield=73.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #36  yield=83.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #37  yield=84.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401108_sup_1_p8_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COc1cc(C)cc(OC)c1I.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_generic` (44.3%) | `graphite_generic` (39.3%) | `graphite_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (14.4%) | `stainless_steel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.2%) | `platinum_generic` (11.2%) | `carbon_generic` (3.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `ABSENT` (90.9%) | `undivided` (8.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.9%) | `ABSENT` (27.1%) | `NEt4` (15.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (67.6%) | `ABSENT` (18.4%) | `I` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `azide_source` (13.5%) | `hf_amine_complex` (6.3%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `Cu_complex` (3.2%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (68.1%) | `polar_protic_alcohol` (24.7%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OCC(F)(F)F` | `CC#N` (99%) | `ClCCl` (7%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (60%) | `CCN(CC)CC.F.F.F` (7%) | `O=O` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #38  yield=5.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCCCCCCCC.OCC(F)(F)C(F)(F)C(F)(F)F>>CCCCCCCCCCC(I)COCC(F)(F)C(F)(F)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (69.6%) | `platinum` (29.3%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (65.0%) | `platinum_generic` (13.7%) | `carbon_generic` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.8%) | `carbon` (2.1%) | `nickel` (1.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.1%) | `platinum_plate` (1.4%) | `platinum_foil` (0.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (94.9%) | `divided` (4.5%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (39.9%) | `NBu4` (28.1%) | `Li` (15.2%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (31.5%) | `BF4` (26.7%) | `ABSENT` (22.0%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `ABSENT` (14.8%) | `iodide_anion` (3.4%) | `tertiary_amine` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `main_group_lewis_acid` (0.2%) | `pyridine_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (33.9%) | `ABSENT` (29.8%) | `polar_aprotic_nitrile` (14.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (67%) | `O` (13%) | `CCN(CC)CC.F.F.F` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `__ABSENT__` (98%) | `O=C([O-])[O-].[Ca+` (16%) | `[Br-].[H+]` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Cl-].[Cl-].[Ni+2]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #39  yield=6.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #1)

```
C=CCCCCCCCCCC.OCC(F)(F)C(F)(F)F>>CCCCCCCCCCC(I)COCC(F)(F)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (61.1%) | `platinum` (38.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (69.4%) | `platinum_generic` (17.8%) | `carbon_plate` (4.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `carbon` (0.5%) | `nickel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (95.6%) | `platinum_plate` (3.5%) | `platinum_foil` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (62.1%) | `NBu4` (30.1%) | `Li` (6.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (50.4%) | `BF4` (30.7%) | `I` (12.4%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `ABSENT` (9.5%) | `iodide_anion` (3.2%) | `azide_source` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.1%) | `pyridine_organocat` (1.3%) | `main_group_lewis_acid` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (27.6%) | `polar_protic_acid` (25.5%) | `polar_aprotic_nitrile` (23.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (45%) | `O` (5%) | `OC(C(F)(F)F)C(F)(F` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `__ABSENT__` (99%) | `O=C([O-])[O-].[Ca+` (10%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl-].[Cl-].[Ni+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #40  yield=6.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #2)

```
OCC(F)(F)F.C=CCCCCO[Si](c1ccccc1)(c1ccccc1)C(C)(C)C>>CC(C)(C)[Si](OCCCCC(I)COCC(F)(F)F)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (98.7%) | `reticulated_vitreous_carbon` (0.4%) | `graphite_rod` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.5%) | `carbon` (15.1%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (42.0%) | `graphite_generic` (34.3%) | `platinum_generic` (22.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.2%) | `NBu4` (22.8%) | `NEt4` (3.6%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (57.2%) | `BF4` (39.1%) | `I` (2.6%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `ABSENT` (14.7%) | `iodide_anion` (5.8%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `Mn_complex` (0.8%) | `brønsted_acid_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (74.0%) | `ABSENT` (14.9%) | `polar_aprotic_nitrile` (9.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (28%) | `CC#N` (1%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `__ABSENT__` (100%) | `BrCCBr` (0%) | `O=C([O-])[O-].[Ca+` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #41  yield=3.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #3)

```
OCC(F)(F)F.C=CCCCCCCCC>>CCCCCCCCC(I)COCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (86.5%) | `platinum` (12.7%) | `sacrificial_iron` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (93.6%) | `platinum_generic` (2.4%) | `carbon_plate` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.2%) | `carbon` (3.2%) | `nickel` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.7%) | `platinum_plate` (1.1%) | `graphite_generic` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.3%) | `divided` (3.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.5%) | `ABSENT` (9.4%) | `Li` (7.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (61.0%) | `BF4` (21.0%) | `ABSENT` (6.2%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `ABSENT` (17.7%) | `iodide_anion` (3.6%) | `azide_source` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `main_group_lewis_acid` (0.3%) | `Mn_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (73.2%) | `ABSENT` (10.3%) | `polar_aprotic_nitrile` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (93%) | `O` (5%) | `CCN(CC)CC.F.F.F` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `__ABSENT__` (98%) | `O=C([O-])[O-].[Ca+` (14%) | `[Br-].[H+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl-].[Cl-].[Ni+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #42  yield=6.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #4)

```
OCC(F)(F)F.C=CCCCCCC>>CCCCCCC(I)COCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (86.5%) | `platinum` (12.7%) | `sacrificial_iron` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.6%) | `platinum_generic` (2.4%) | `carbon_plate` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.2%) | `carbon` (3.2%) | `nickel` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.7%) | `platinum_plate` (1.1%) | `graphite_generic` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.3%) | `divided` (3.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.5%) | `ABSENT` (9.4%) | `Li` (7.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (61.0%) | `BF4` (21.0%) | `ABSENT` (6.2%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `ABSENT` (17.7%) | `iodide_anion` (3.6%) | `azide_source` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `main_group_lewis_acid` (0.3%) | `Mn_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (73.2%) | `ABSENT` (10.3%) | `polar_aprotic_nitrile` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (93%) | `O` (5%) | `CCN(CC)CC.F.F.F` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `__ABSENT__` (98%) | `O=C([O-])[O-].[Ca+` (14%) | `[Br-].[H+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl-].[Cl-].[Ni+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #43  yield=6.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #5)

```
OCC(F)(F)F.C=CCCCCCCCCCC>>CCCCCCCCCCC(I)COCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (86.5%) | `platinum` (12.7%) | `sacrificial_iron` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (93.6%) | `platinum_generic` (2.4%) | `carbon_plate` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.2%) | `carbon` (3.2%) | `nickel` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.7%) | `platinum_plate` (1.1%) | `graphite_generic` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.3%) | `divided` (3.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.5%) | `ABSENT` (9.4%) | `Li` (7.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (61.0%) | `BF4` (21.0%) | `ABSENT` (6.2%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `ABSENT` (17.7%) | `iodide_anion` (3.6%) | `azide_source` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `main_group_lewis_acid` (0.3%) | `Mn_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (73.2%) | `ABSENT` (10.3%) | `polar_aprotic_nitrile` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (93%) | `O` (5%) | `CCN(CC)CC.F.F.F` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `__ABSENT__` (98%) | `O=C([O-])[O-].[Ca+` (14%) | `[Br-].[H+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl-].[Cl-].[Ni+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #44  yield=8.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #6)

```
OCC(F)(F)F.C=CCCCCCCBr>>FC(F)(F)COCC(I)CCCCCCBr
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (79.1%) | `platinum` (13.2%) | `sacrificial_magnesium` (7.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (38.9%) | `magnesium_plate` (22.4%) | `reticulated_vitreous_carbon` (22.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.1%) | `carbon` (1.8%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (99.1%) | `platinum_plate` (0.4%) | `platinum_foil` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `divided` (0.7%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (49.0%) | `NBu4` (41.5%) | `Na` (7.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (50.5%) | `I` (19.6%) | `ClO4` (12.1%) | ✗ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `ABSENT` (19.3%) | `iodide_anion` (4.0%) | `carboxylic_acid` (3.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.1%) | `brønsted_acid_cat` (4.4%) | `Ni_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_amide` (66.3%) | `polar_aprotic_nitrile` (15.1%) | `ABSENT` (8.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CN(C)C=O` (83%) | `O` (25%) | `CC#N` (10%) | set ✗ / any ✗ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `__ABSENT__` (100%) | `O=C([O-])[O-].[Ca+` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `COCCOC.[Br][Ni][Br` (0%) | set ✓ / any ✓ |

---

### Reaction #45  yield=16.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #7)

```
C=CCCCCCCCCCC.CC(O)C(F)(F)F>>CCCCCCCCCC[C@@H](CI)O[C@@H](C)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (63.0%) | `ABSENT` (18.6%) | `carbon` (18.0%) | ✓ |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (42.0%) | `platinum_generic` (34.6%) | `ABSENT` (17.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (62.5%) | `ABSENT` (32.9%) | `stainless_steel` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (66.7%) | `ABSENT` (22.6%) | `platinum_plate` (7.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (75.3%) | `ABSENT` (14.8%) | `undivided` (9.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (67.7%) | `NEt4` (17.6%) | `ABSENT` (11.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (71.8%) | `BF4` (15.5%) | `ABSENT` (7.9%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `hf_amine_complex` (15.7%) | `ABSENT` (11.3%) | `iodide_anion` (7.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `ammonium_PTC_organocat` (0.4%) | `main_group_lewis_acid` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (48.3%) | `polar_protic_alcohol` (24.8%) | `halogenated_aliphatic` (13.6%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `ClCCl` (11%) | `OC(C(F)(F)F)C(F)(F` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `OC(C(F)(F)F)C(F)(F` (14%) | `CCN(CC)CC.F.F.F` (7%) | `CCN(CC)CC.F` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (1%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #46  yield=16.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #8)

```
C=CCCCCCCCCCC.CC(O)C(F)(F)F>>CCCCCCCCCC[C@H](CI)O[C@@H](C)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (63.0%) | `ABSENT` (18.6%) | `carbon` (18.0%) | ✓ |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (42.0%) | `platinum_generic` (34.6%) | `ABSENT` (17.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (62.5%) | `ABSENT` (32.9%) | `stainless_steel` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (66.7%) | `ABSENT` (22.6%) | `platinum_plate` (7.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (75.3%) | `ABSENT` (14.8%) | `undivided` (9.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (67.7%) | `NEt4` (17.6%) | `ABSENT` (11.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (71.8%) | `BF4` (15.5%) | `ABSENT` (7.9%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `hf_amine_complex` (15.7%) | `ABSENT` (11.3%) | `iodide_anion` (7.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `ammonium_PTC_organocat` (0.4%) | `main_group_lewis_acid` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (48.3%) | `polar_protic_alcohol` (24.8%) | `halogenated_aliphatic` (13.6%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `ClCCl` (11%) | `OC(C(F)(F)F)C(F)(F` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `OC(C(F)(F)F)C(F)(F` (14%) | `CCN(CC)CC.F.F.F` (7%) | `CCN(CC)CC.F` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl-].[Cl-].[Ni+2]` (1%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #47  yield=17.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #9)

```
OCC(F)(F)F.C=CCCCN1C(=O)c2ccccc2C1=O>>O=C1c2ccccc2C(=O)N1CCCC(I)COCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (75.3%) | `platinum` (24.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (97.0%) | `carbon_rod` (1.4%) | `platinum_plate` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.0%) | `carbon` (5.3%) | `stainless_steel` (3.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (68.4%) | `graphite_generic` (15.2%) | `platinum_generic` (13.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.0%) | `divided` (2.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.2%) | `H` (7.7%) | `NEt4` (6.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (31.0%) | `carboxylate` (21.7%) | `I` (14.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `iodide_anion` (11.8%) | `aryl_iodide_mediator` (6.3%) | `ABSENT` (6.1%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `Mn_complex` (0.3%) | `brønsted_acid_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (47.9%) | `halogenated_aliphatic` (47.4%) | `polar_protic_alcohol` (2.4%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (97%) | `ClCCl` (25%) | `O` (21%) | set ✗ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `Cc1ccc(I)cc1` (88%) | `[OH][Na]` (61%) | `F.c1ccncc1` (55%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `[Cl-].[Cl-].[Mn+2]` (2%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #48  yield=23.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #10)

```
OCC(F)(F)F.C=CCc1ccc(F)cc1>>Fc1ccc(CC(I)COCC(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (89.5%) | `platinum` (5.5%) | `ABSENT` (2.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (54.5%) | `reticulated_vitreous_carbon` (14.9%) | `platinum_generic` (10.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (78.0%) | `stainless_steel` (15.8%) | `carbon` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (78.7%) | `stainless_steel_generic` (7.2%) | `platinum_plate` (5.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (54.7%) | `undivided` (44.8%) | `ABSENT` (0.6%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (38.2%) | `NEt4` (23.4%) | `NBu4` (20.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (29.3%) | `ClO4` (19.1%) | `I` (19.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `iodide_anion` (15.8%) | `ABSENT` (10.5%) | `aryl_iodide_mediator` (2.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.1%) | `Mn_complex` (0.8%) | `ionic_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (43.5%) | `polar_aprotic_nitrile` (25.0%) | `ABSENT` (23.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (95%) | `O` (10%) | `CC#N` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `O` (20%) | `O=C(O)C(F)(F)F` (19%) | `[I-].[Na+]` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Br-].[Mn+2]` (0%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #49  yield=23.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #10)

```
OCC(F)(F)F.C=CCc1ccc(F)cc1>>Fc1ccc(CC(I)COCC(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (89.5%) | `platinum` (5.5%) | `ABSENT` (2.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (54.5%) | `reticulated_vitreous_carbon` (14.9%) | `platinum_generic` (10.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (78.0%) | `stainless_steel` (15.8%) | `carbon` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (78.7%) | `stainless_steel_generic` (7.2%) | `platinum_plate` (5.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (54.7%) | `undivided` (44.8%) | `ABSENT` (0.6%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (38.2%) | `NEt4` (23.4%) | `NBu4` (20.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (29.3%) | `ClO4` (19.1%) | `I` (19.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `iodide_anion` (15.8%) | `ABSENT` (10.5%) | `aryl_iodide_mediator` (2.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.1%) | `Mn_complex` (0.8%) | `ionic_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (43.5%) | `polar_aprotic_nitrile` (25.0%) | `ABSENT` (23.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (95%) | `O` (10%) | `CC#N` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `O` (20%) | `O=C(O)C(F)(F)F` (19%) | `[I-].[Na+]` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-].[Br-].[Mn+2]` (0%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #50  yield=47.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #12)

```
C=CCCCCCCCCCC.OCC(F)(F)C(F)(F)C(F)(F)F>>CCCCCCCCCCC(CI)OCC(F)(F)C(F)(F)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (50.6%) | `ABSENT` (45.4%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `glassy_carbon` | `platinum_generic` (71.7%) | `ABSENT` (18.9%) | `carbon_generic` (3.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (65.9%) | `ABSENT` (29.3%) | `stainless_steel` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (86.8%) | `ABSENT` (9.2%) | `platinum_plate` (2.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (89.5%) | `ABSENT` (10.0%) | `undivided` (0.5%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (35.5%) | `ABSENT` (20.9%) | `NBu4` (16.8%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `I` (77.8%) | `BF4` (11.7%) | `ABSENT` (6.5%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `iodide_anion` (15.5%) | `ABSENT` (8.7%) | `hf_amine_complex` (7.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.4%) | `main_group_lewis_acid` (0.9%) | `ionic_organocat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `solvent_mixture` (47.4%) | `halogenated_aliphatic` (21.9%) | `polar_protic_alcohol` (17.5%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (46%) | `CCN(CC)CC.F.F.F` (45%) | `O` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `O=O` (59%) | `O=C([O-])[O-].[Ca+` (57%) | `OB(O)B(O)O` (26%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl-].[Cl-].[Ni+2]` (68%) | `__ABSENT__` (27%) | `CCCC[N+](CCCC)(CCC` (4%) | set ✗ / any ✓ |

---

### Reaction #51  yield=47.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #12)

```
C=CCCCCCCCCCC.OCC(F)(F)C(F)(F)C(F)(F)F>>CCCCCCCCCCC(CI)OCC(F)(F)C(F)(F)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (50.6%) | `ABSENT` (45.4%) | `carbon` (3.9%) | ✓ |
| 阳极 (细类) | 43 | `glassy_carbon` | `platinum_generic` (71.7%) | `ABSENT` (18.9%) | `carbon_generic` (3.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (65.9%) | `ABSENT` (29.3%) | `stainless_steel` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (86.8%) | `ABSENT` (9.2%) | `platinum_plate` (2.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (89.5%) | `ABSENT` (10.0%) | `undivided` (0.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NEt4` (35.5%) | `ABSENT` (20.9%) | `NBu4` (16.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (77.8%) | `BF4` (11.7%) | `ABSENT` (6.5%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `iodide_anion` (15.5%) | `ABSENT` (8.7%) | `hf_amine_complex` (7.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.4%) | `main_group_lewis_acid` (0.9%) | `ionic_organocat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `solvent_mixture` (47.4%) | `halogenated_aliphatic` (21.9%) | `polar_protic_alcohol` (17.5%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (46%) | `CCN(CC)CC.F.F.F` (45%) | `O` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `O=O` (59%) | `O=C([O-])[O-].[Ca+` (57%) | `OB(O)B(O)O` (26%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl-].[Cl-].[Ni+2]` (68%) | `__ABSENT__` (27%) | `CCCC[N+](CCCC)(CCC` (4%) | set ✗ / any ✓ |

---

### Reaction #52  yield=45.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #14)

```
C=CCCCCCCCCCC.OCC(F)(F)C(F)(F)F>>CCCCCCCCCCC(CI)OCC(F)(F)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (64.8%) | `ABSENT` (31.6%) | `carbon` (3.6%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `platinum_generic` (88.6%) | `ABSENT` (5.8%) | `platinum_plate` (1.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.6%) | `ABSENT` (14.1%) | `stainless_steel` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (88.8%) | `platinum_plate` (5.4%) | `ABSENT` (4.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (92.3%) | `ABSENT` (5.1%) | `undivided` (2.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (39.1%) | `NBu4` (32.9%) | `Li` (15.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (75.2%) | `ABSENT` (10.6%) | `BF4` (10.5%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `iodide_anion` (15.8%) | `hf_amine_complex` (11.0%) | `ABSENT` (6.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.3%) | `main_group_lewis_acid` (0.5%) | `ionic_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (37.1%) | `polar_protic_alcohol` (21.5%) | `solvent_mixture` (13.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (95%) | `O` (29%) | `CCN(CC)CC.F.F.F` (12%) | set ✓ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `O=C([O-])[O-].[Ca+` (70%) | `O=O` (32%) | `__OTHER__` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (75%) | `[Cl-].[Cl-].[Ni+2]` (22%) | `CCCC[N+](CCCC)(CCC` (3%) | set ✓ / any ✓ |

---

### Reaction #53  yield=43.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #15)

```
OCC(F)(F)F.C=CCCCCO[Si](c1ccccc1)(c1ccccc1)C(C)(C)C>>CC(C)(C)[Si](OCCCCC(CI)OCC(F)(F)F)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `platinum` (0.7%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `reticulated_vitreous_carbon` (63.9%) | `graphite_generic` (21.6%) | `carbon_rod` (6.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.8%) | `carbon` (3.7%) | `stainless_steel` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.2%) | `platinum_generic` (1.3%) | `stainless_steel_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (89.2%) | `divided` (10.6%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (77.9%) | `NBu4` (12.7%) | `NEt4` (8.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (63.3%) | `BF4` (26.3%) | `I` (9.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `iodide_anion` (16.8%) | `hf_amine_complex` (16.5%) | `ABSENT` (5.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `Mn_complex` (0.3%) | `Cu_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (85.2%) | `ABSENT` (10.3%) | `polar_aprotic_nitrile` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (89%) | `O` (1%) | `CC#N` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `BrCCBr` (17%) | `OC(C(F)(F)F)C(F)(F` (9%) | `O=C([O-])[O-].[Ca+` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #54  yield=43.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #15)

```
OCC(F)(F)F.C=CCCCCO[Si](c1ccccc1)(c1ccccc1)C(C)(C)C>>CC(C)(C)[Si](OCCCCC(CI)OCC(F)(F)F)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `platinum` (0.7%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `reticulated_vitreous_carbon` (63.9%) | `graphite_generic` (21.6%) | `carbon_rod` (6.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.8%) | `carbon` (3.7%) | `stainless_steel` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.2%) | `platinum_generic` (1.3%) | `stainless_steel_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (89.2%) | `divided` (10.6%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (77.9%) | `NBu4` (12.7%) | `NEt4` (8.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (63.3%) | `BF4` (26.3%) | `I` (9.2%) | ✓ |
| 试剂大类 | 103 | `as_solvent_halogenated_aliphat` | `iodide_anion` (16.8%) | `hf_amine_complex` (16.5%) | `ABSENT` (5.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `Mn_complex` (0.3%) | `Cu_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (85.2%) | `ABSENT` (10.3%) | `polar_aprotic_nitrile` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (89%) | `O` (1%) | `CC#N` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `BrCCBr` (17%) | `OC(C(F)(F)F)C(F)(F` (9%) | `O=C([O-])[O-].[Ca+` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #55  yield=59.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #17)

```
OCC(F)(F)F.C=CCCCN1C(=O)c2ccccc2C1=O>>O=C1c2ccccc2C(=O)N1CCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (63.0%) | `carbon` (33.5%) | `ABSENT` (3.5%) | ✓ |
| 阳极 (细类) | 43 | `glassy_carbon` | `platinum_plate` (62.4%) | `graphite_generic` (16.3%) | `carbon_rod` (10.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (68.4%) | `stainless_steel` (17.3%) | `ABSENT` (8.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.3%) | `platinum_generic` (0.5%) | `carbon_rod` (0.5%) | ✓ |
| 池型 | 4 | `undivided` | `divided` (62.7%) | `undivided` (36.3%) | `ABSENT` (1.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NEt4` (45.7%) | `NBu4` (39.5%) | `protonated_amine` (5.4%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (43.1%) | `BF4` (21.8%) | `fluoride_complex` (13.9%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `iodide_anion` (19.7%) | `inorganic_simple` (16.6%) | `azide_source` (6.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `ionic_organocat` (0.3%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (48.0%) | `polar_aprotic_nitrile` (45.8%) | `polar_protic_alcohol` (4.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (93%) | `CC#N` (73%) | `FC(F)(F)c1ccccc1` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `F.c1ccncc1` (94%) | `[OH][Na]` (94%) | `Cc1ccc(I)cc1` (89%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (59%) | `[Cl-].[Cl-].[Mn+2]` (25%) | `Brc1ccc(N(c2ccc(Br` (10%) | set ✓ / any ✓ |

---

### Reaction #56  yield=68.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #18)

```
OCC(F)(F)F.C=CCCCCCCCC>>CCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `ABSENT` (40.6%) | `carbon` (37.2%) | `platinum` (22.0%) | ✓ |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (44.7%) | `platinum_generic` (16.5%) | `carbon_generic` (7.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (65.2%) | `ABSENT` (21.8%) | `stainless_steel` (7.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (51.9%) | `platinum_generic` (40.8%) | `ABSENT` (2.6%) | ✓ |
| 池型 | 4 | `undivided` | `divided` (93.3%) | `undivided` (4.5%) | `ABSENT` (2.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (44.6%) | `NEt4` (22.5%) | `ABSENT` (12.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (81.1%) | `BF4` (11.0%) | `ABSENT` (3.4%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `iodide_anion` (16.5%) | `hf_amine_complex` (9.9%) | `ABSENT` (9.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `main_group_lewis_acid` (0.7%) | `ionic_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (48.8%) | `polar_aprotic_nitrile` (14.1%) | `solvent_mixture` (14.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (99%) | `CCN(CC)CC.F.F.F` (24%) | `O` (21%) | set ✓ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `O=C([O-])[O-].[Ca+` (75%) | `O=O` (45%) | `__OTHER__` (21%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (74%) | `[Cl-].[Cl-].[Ni+2]` (17%) | `CCCC[N+](CCCC)(CCC` (8%) | set ✓ / any ✓ |

---

### Reaction #57  yield=65.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #19)

```
OCC(F)(F)F.C=CCCCCCC>>CCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `ABSENT` (40.6%) | `carbon` (37.2%) | `platinum` (22.0%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (44.7%) | `platinum_generic` (16.5%) | `carbon_generic` (7.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (65.2%) | `ABSENT` (21.8%) | `stainless_steel` (7.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (51.9%) | `platinum_generic` (40.8%) | `ABSENT` (2.6%) | ✓ |
| 池型 | 4 | `undivided` | `divided` (93.3%) | `undivided` (4.5%) | `ABSENT` (2.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (44.6%) | `NEt4` (22.5%) | `ABSENT` (12.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (81.1%) | `BF4` (11.0%) | `ABSENT` (3.4%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `iodide_anion` (16.5%) | `hf_amine_complex` (9.9%) | `ABSENT` (9.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `main_group_lewis_acid` (0.7%) | `ionic_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (48.8%) | `polar_aprotic_nitrile` (14.1%) | `solvent_mixture` (14.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (99%) | `CCN(CC)CC.F.F.F` (24%) | `O` (21%) | set ✓ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `O=C([O-])[O-].[Ca+` (75%) | `O=O` (45%) | `__OTHER__` (21%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (74%) | `[Cl-].[Cl-].[Ni+2]` (17%) | `CCCC[N+](CCCC)(CCC` (8%) | set ✓ / any ✓ |

---

### Reaction #58  yield=65.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #20)

```
OCC(F)(F)F.C=CCCCCCCCCCC>>CCCCCCCCCCC(CI)OCC(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `ABSENT` (40.6%) | `carbon` (37.2%) | `platinum` (22.0%) | ✓ |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (44.7%) | `platinum_generic` (16.5%) | `carbon_generic` (7.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (65.2%) | `ABSENT` (21.8%) | `stainless_steel` (7.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (51.9%) | `platinum_generic` (40.8%) | `ABSENT` (2.6%) | ✓ |
| 池型 | 4 | `undivided` | `divided` (93.3%) | `undivided` (4.5%) | `ABSENT` (2.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (44.6%) | `NEt4` (22.5%) | `ABSENT` (12.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (81.1%) | `BF4` (11.0%) | `ABSENT` (3.4%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `iodide_anion` (16.5%) | `hf_amine_complex` (9.9%) | `ABSENT` (9.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `main_group_lewis_acid` (0.7%) | `ionic_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (48.8%) | `polar_aprotic_nitrile` (14.1%) | `solvent_mixture` (14.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (99%) | `CCN(CC)CC.F.F.F` (24%) | `O` (21%) | set ✓ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `O=C([O-])[O-].[Ca+` (75%) | `O=O` (45%) | `__OTHER__` (21%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (74%) | `[Cl-].[Cl-].[Ni+2]` (17%) | `CCCC[N+](CCCC)(CCC` (8%) | set ✓ / any ✓ |

---

### Reaction #59  yield=66.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #21)

```
OCC(F)(F)F.C=Cc1ccc(C(F)(F)F)cc1>>FC(F)(F)COC(CI)c1ccc(C(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.1%) | `platinum` (1.6%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_rod` (82.2%) | `graphite_generic` (15.2%) | `graphite_rod` (0.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.3%) | `stainless_steel` (15.0%) | `carbon` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.0%) | `platinum_generic` (0.5%) | `stainless_steel_generic` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (90.0%) | `divided` (10.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (49.6%) | `ABSENT` (47.3%) | `NEt4` (1.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ABSENT` (47.2%) | `I` (38.4%) | `BF4` (9.6%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `hf_amine_complex` (14.1%) | `ABSENT` (8.6%) | `iodide_anion` (7.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `ionic_organocat` (0.1%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (57.1%) | `halogenated_aliphatic` (24.3%) | `ABSENT` (15.1%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `ClCCl` (98%) | `CC#N` (86%) | `FC(F)(F)c1ccccc1` (13%) | set ✗ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `CCN(CC)CC.F.F.F` (67%) | `OC(C(F)(F)F)C(F)(F` (22%) | `Cc1ccc(I)cc1` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `c1ccncc1` (0%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #60  yield=64.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #22)

```
OCC(F)(F)F.C=Cc1cccc(Br)c1>>FC(F)(F)COC(CI)c1cccc(Br)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `carbon_rod` (57.8%) | `graphite_generic` (39.9%) | `graphite_rod` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.5%) | `stainless_steel` (4.5%) | `nickel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.3%) | `platinum_generic` (1.2%) | `nickel_plate` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (95.0%) | `divided` (5.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.2%) | `ABSENT` (12.2%) | `NEt4` (2.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (85.6%) | `ABSENT` (4.8%) | `BF4` (4.3%) | ✓ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `hf_amine_complex` (26.3%) | `ABSENT` (19.2%) | `inorganic_simple` (3.1%) | ✗ |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (99.8%) | `ionic_organocat` (0.1%) | `ammonium_PTC_organocat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (66.7%) | `polar_aprotic_nitrile` (19.4%) | `ABSENT` (10.9%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `ClCCl` (99%) | `FC(F)(F)c1ccccc1` (8%) | `CC#N` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `CCN(CC)CC.F.F.F` (49%) | `CCN(CC)CC.F` (19%) | `__ABSENT__` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `ClCCl` | `__ABSENT__` (100%) | `[Br-].[Br-].[Mn+2]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |

---

### Reaction #61  yield=75.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #23)

```
OCC(F)(F)F.C=CCc1ccc(F)cc1.COc1cc(C)cc(OC)c1I>>Fc1ccc(CC(CI)OCC(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `graphite_generic` (80.8%) | `reticulated_vitreous_carbon` (7.0%) | `graphite_rod` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (51.6%) | `platinum` (35.2%) | `stainless_steel` (9.3%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `graphite_generic` (38.9%) | `platinum_plate` (24.0%) | `nickel_plate` (10.9%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (51.6%) | `undivided` (40.9%) | `divided` (7.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (81.4%) | `NEt4` (10.5%) | `NBu4` (7.6%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (72.3%) | `BF4` (26.5%) | `PF6` (0.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (9.9%) | `ABSENT` (8.1%) | `boron_lewis_acid` (3.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.0%) | `Cu_complex` (0.9%) | `Mn_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (86.8%) | `ABSENT` (6.1%) | `polar_protic_alcohol` (4.7%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (80%) | `CC(C)=O` (18%) | `ClCCl` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `[I-].[Na+]` (39%) | `CCN(CC)CC.F.F.F` (1%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #62  yield=74.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_8_e202401108.json) (反应 idx 在该 JSON 内 = #24)

```
OCC(F)(F)F.C=CCCCCCCBr>>FC(F)(F)COC(CI)CCCCCCBr
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (61.4%) | `platinum` (37.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `glassy_carbon` | `reticulated_vitreous_carbon` (86.1%) | `platinum_plate` (5.0%) | `platinum_generic` (4.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.9%) | `carbon` (1.6%) | `stainless_steel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (53.0%) | `platinum_generic` (45.2%) | `platinum_wire` (0.7%) | ✓ |
| 池型 | 4 | `undivided` | `divided` (90.6%) | `undivided` (9.2%) | `ABSENT` (0.2%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (39.3%) | `Li` (35.5%) | `NEt4` (13.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `I` (61.6%) | `ClO4` (17.2%) | `molecular_no_ion` (12.3%) | ✗ |
| 试剂大类 | 103 | `aryl_iodide_mediator` | `iodide_anion` (19.7%) | `ABSENT` (11.4%) | `azide_source` (5.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.5%) | `brønsted_acid_cat` (0.6%) | `Cu_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (35.4%) | `polar_protic_alcohol` (14.6%) | `polar_protic_acid` (12.8%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (87%) | `O` (81%) | `ClCCl` (13%) | set ✗ / any ✓ |
| 试剂 set | 545 | `COc1cc(C)cc(OC)c1I` | `O=C([O-])[O-].[Ca+` (20%) | `O=C(O)C(F)(F)F` (16%) | `[I-].[NH4+]` (14%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `O=S(=O)([O-])C(F)(` (1%) | `[Pt]` (1%) | set ✓ / any ✓ |

---

### Reaction #63  yield=42.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #64  yield=17.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #65  yield=18.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #66  yield=39.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #67  yield=0.5%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #68  yield=39.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #69  yield=58.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #70  yield=11.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #71  yield=35.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #72  yield=41.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #73  yield=0.5%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #74  yield=0.5%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #75  yield=0.5%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #76  yield=35.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #77  yield=32.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #78  yield=0.5%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #79  yield=39.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #80  yield=54.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #81  yield=35.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #82  yield=36.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202401225_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21.O=S([O-])C(F)(F)F.[Na+]>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.5%) | `carbon_generic` (4.9%) | `reticulated_vitreous_carbon` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.8%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (97.5%) | `platinum_plate` (2.3%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.4%) | `NEt4` (11.1%) | `Li` (4.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (70.4%) | `PF6` (13.4%) | `BF4` (12.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.6%) | `electrophilic_N_F` (2.2%) | `aldehyde` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.2%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (57.0%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (7.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (20%) | `CCO` (8%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #83  yield=38.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #0)

```
O=S(O)C(F)(F)F.[Na].C=C(C)C(=O)n1c(-c2ccc(Cl)cc2)cc2ccccc21>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccc(Cl)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (99.1%) | `carbon_generic` (0.6%) | `graphite_rod` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.2%) | `nickel` (1.2%) | `stainless_steel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (75.5%) | `platinum_generic` (16.1%) | `nickel_plate` (4.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (54.4%) | `NBu4` (39.7%) | `Li` (1.8%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `ABSENT` (48.6%) | `carboxylate` (23.7%) | `BF4` (17.7%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (21.3%) | `water` (3.2%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `pyridine_organocat` (0.2%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (73.8%) | `halogenated_aliphatic` (19.4%) | `polar_protic_alcohol` (5.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (88%) | `O` (5%) | `ClCCl` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |

---

### Reaction #84  yield=37.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #1)

```
O=S(O)C(F)(F)F.[Na].C=C(C)C(=O)n1c(-c2cccc(Cl)c2)cc2ccccc21>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2cc(Cl)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (99.1%) | `carbon_generic` (0.7%) | `graphite_rod` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (58.0%) | `platinum_generic` (40.2%) | `platinum_wire` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (71.0%) | `Li` (18.1%) | `ABSENT` (6.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `molecular_no_ion` (32.7%) | `ClO4` (23.0%) | `BF4` (18.2%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (19.9%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.8%) | `Mn_complex` (0.7%) | `pyridine_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.7%) | `polar_protic_alcohol` (7.9%) | `halogenated_aliphatic` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (97%) | `CC(C)=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #85  yield=36.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #2)

```
O=S([O-])C(F)(F)F.[Na+].C=C(C)C(=O)n1c(-c2ccc(Cl)cc2)cc2cc(Cl)ccc21>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3cc(Cl)ccc32)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `reticulated_vitreous_carbon` (37.2%) | `carbon_generic` (24.0%) | `graphite_generic` (16.9%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `stainless_steel` (0.2%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (83.1%) | `platinum_generic` (16.3%) | `stainless_steel_generic` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (51.8%) | `NEt4` (19.5%) | `ABSENT` (17.6%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `BF4` (40.6%) | `ClO4` (32.2%) | `ABSENT` (17.8%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.5%) | `electrophilic_N_F` (2.2%) | `unparseable_text` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ionic_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (75.3%) | `polar_protic_alcohol` (16.4%) | `halogenated_aliphatic` (3.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (97%) | `O` (51%) | `CCO` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #86  yield=50.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #3)

```
O=S(O)C(F)(F)F.[Na].C=C(C)C(=O)n1c(-c2ccc(C)cc2)cc2ccccc21>>Cc1ccc2c(c1)C(C)(CC(F)(F)F)C(=O)n1c-2c(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (94.8%) | `carbon_generic` (4.6%) | `carbon_felt` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.1%) | `nickel` (1.2%) | `carbon` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (59.3%) | `platinum_generic` (32.1%) | `stainless_steel_generic` (3.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (45.2%) | `NEt4` (21.5%) | `Li` (18.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (56.0%) | `ABSENT` (31.4%) | `PF6` (6.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `water` (20.9%) | `ABSENT` (14.9%) | `metal_oxide_oxidant` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.1%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.8%) | `ABSENT` (30.5%) | `polar_protic_alcohol` (6.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (53%) | `FC(F)(F)c1ccccc1` (2%) | `CC(C)=O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `O` (98%) | `__ABSENT__` (13%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #87  yield=50.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #4)

```
O=S(O)C(F)(F)F.[Na].C=C(C)C(=O)n1c(-c2ccccc2)cc2cc(Br)ccc21>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3cc(Br)ccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (97.6%) | `glassy_carbon` (0.8%) | `carbon_felt` (0.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.2%) | `stainless_steel` (1.3%) | `nickel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.8%) | `stainless_steel_generic` (0.5%) | `nickel_plate` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (73.9%) | `ABSENT` (14.4%) | `Li` (5.1%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (23.9%) | `Br` (23.0%) | `ClO4` (16.9%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (16.2%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (80.3%) | `polar_protic_alcohol` (6.1%) | `ABSENT` (6.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (87%) | `O` (4%) | `CC(C)=O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `__OTHER__` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #88  yield=43.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #5)

```
O=S(O)C(F)(F)F.[Na].C=C(C)C(=O)n1c(-c2ccccc2)cc2cc(C(C)(C)C)ccc21>>CC(C)(C)c1ccc2c(c1)c(C(F)(F)F)c1n2C(=O)C(C)(CC(F)(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (98.7%) | `carbon_felt` (0.5%) | `carbon_plate` (0.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.4%) | `stainless_steel` (2.6%) | `nickel` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (99.0%) | `stainless_steel_generic` (0.7%) | `nickel_plate` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (76.0%) | `ABSENT` (14.1%) | `K` (5.9%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (22.7%) | `ABSENT` (21.1%) | `PF6` (19.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (20.3%) | `water` (3.4%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `Mn_complex` (0.2%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (76.6%) | `cyclic_ether` (5.8%) | `halogenated_aliphatic` (5.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (92%) | `ClCCCl` (0%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #89  yield=44.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #6)

```
O=S(O)C(F)(F)F.[Na].C=C(C)C(=O)n1c(-c2ccc(F)cc2)cc2ccccc21>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccc(F)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (99.9%) | `carbon_generic` (0.0%) | `carbon_felt` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.3%) | `carbon` (2.3%) | `stainless_steel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (34.7%) | `stainless_steel_generic` (19.3%) | `platinum_generic` (18.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (43.7%) | `NBu4` (40.6%) | `ABSENT` (7.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (74.7%) | `BF4` (11.4%) | `molecular_no_ion` (5.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (27.4%) | `water` (6.2%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `ionic_organocat` (0.2%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (72.2%) | `halogenated_aliphatic` (15.7%) | `polar_protic_alcohol` (5.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (11%) | `CC#N` (6%) | `ClCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #90  yield=47.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #7)

```
O=S(O)C(F)(F)F.[Na].C=C(C)C(=O)n1c(-c2cccc(Br)c2)cc2ccccc21>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2cc(Br)ccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (99.1%) | `graphite_rod` (0.3%) | `carbon_generic` (0.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `nickel` (0.3%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (76.3%) | `platinum_generic` (20.6%) | `platinum_wire` (2.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (59.6%) | `ABSENT` (19.7%) | `NBu4` (13.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (60.9%) | `molecular_no_ion` (19.9%) | `ABSENT` (12.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (13.4%) | `water` (2.4%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `pyridine_organocat` (0.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.0%) | `polar_protic_alcohol` (1.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (91%) | `CC(C)=O` (2%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #91  yield=46.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #8)

```
O=S(O)C(F)(F)F.[Na].C=C(C)C(=O)n1c(-c2ccccc2)cc2cc(F)ccc21>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3cc(F)ccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (100.0%) | `carbon_felt` (0.0%) | `carbon_generic` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.2%) | `stainless_steel` (9.9%) | `nickel` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (62.3%) | `stainless_steel_generic` (33.1%) | `platinum_generic` (2.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (67.7%) | `ABSENT` (26.5%) | `Li` (2.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (37.0%) | `BF4` (24.5%) | `carboxylate` (21.4%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (18.5%) | `water` (2.9%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `organic_neutral_cat` (0.2%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (53.7%) | `halogenated_aliphatic` (24.9%) | `polar_protic_alcohol` (16.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (56%) | `O` (34%) | `CC(C)=O` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #92  yield=45.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #9)

```
O=S(O)C(F)(F)F.[Na].C=C(C)C(=O)n1c(-c2ccccc2)cc2ccc(F)cc21>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccc(F)cc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (99.7%) | `reticulated_vitreous_carbon` (0.1%) | `carbon_cloth` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.2%) | `nickel` (4.5%) | `stainless_steel` (3.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (66.2%) | `platinum_generic` (18.0%) | `stainless_steel_generic` (8.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.6%) | `ABSENT` (1.4%) | `K` (0.7%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `BF4` (47.3%) | `PF6` (26.4%) | `ClO4` (10.2%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `water` (17.5%) | `ABSENT` (10.3%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.5%) | `ionic_organocat` (0.5%) | `pyridine_organocat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (51.6%) | `halogenated_aliphatic` (19.5%) | `ABSENT` (10.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (3%) | `CC(C)=O` (1%) | `FC(F)(F)c1ccccc1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `O` (81%) | `__ABSENT__` (9%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[O]=[Fe][O][Fe]=[O` (0%) | set ✓ / any ✓ |

---

### Reaction #93  yield=47.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #10)

```
O=S(O)C(F)(F)F.[Na].C=C(C)C(=O)n1c(-c2ccc(F)cc2)cc2cc(Cl)ccc21>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3cc(Cl)ccc32)-c2cc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (98.2%) | `carbon_generic` (0.9%) | `carbon_felt` (0.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.5%) | `stainless_steel` (11.8%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `stainless_steel_generic` (49.0%) | `platinum_plate` (46.5%) | `platinum_generic` (1.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (42.7%) | `ABSENT` (27.5%) | `Li` (19.9%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (46.9%) | `ABSENT` (22.8%) | `ClO4` (12.3%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (31.4%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ionic_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (48.3%) | `polar_protic_alcohol` (34.6%) | `halogenated_aliphatic` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (75%) | `CC#N` (51%) | `CC(C)=O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #94  yield=58.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #11)

```
O=S(O)C(F)(F)F.[Na].C=C(C)C(=O)n1c(-c2ccccc2)cc2ccccc21>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (99.9%) | `carbon_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.7%) | `stainless_steel` (4.2%) | `nickel` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (50.8%) | `platinum_generic` (27.8%) | `stainless_steel_generic` (15.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (62.3%) | `ABSENT` (31.1%) | `NEt4` (3.0%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (40.4%) | `BF4` (17.4%) | `PF6` (17.2%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (12.6%) | `water` (8.3%) | `o2_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.0%) | `Mn_complex` (1.5%) | `pyridine_organocat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (65.0%) | `polar_protic_alcohol` (20.3%) | `halogenated_aliphatic` (10.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (75%) | `CC(C)=O` (4%) | `FC(F)(F)c1ccccc1` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #95  yield=56.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #12)

```
O=S(O)C(F)(F)F.[Na].C=C(C)C(=O)n1c(-c2ccc(Br)cc2)cc2ccccc21>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccccc32)-c2ccc(Br)cc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (90.1%) | `carbon_generic` (6.9%) | `graphite_rod` (1.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.6%) | `nickel` (4.3%) | `carbon` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (92.4%) | `platinum_generic` (2.9%) | `nickel_plate` (2.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (45.3%) | `ABSENT` (21.3%) | `NEt4` (17.8%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (49.6%) | `BF4` (25.8%) | `ABSENT` (17.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (18.8%) | `water` (4.0%) | `primary_amine` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `pyridine_organocat` (0.1%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (79.4%) | `ABSENT` (15.3%) | `polar_protic_alcohol` (2.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (69%) | `FC(F)(F)c1ccccc1` (1%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #96  yield=52.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #13)

```
O=S(O)C(F)(F)F.[Na].C=C(C)C(=O)n1c(-c2ccccc2)cc2ccc(Br)cc21>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3ccc(Br)cc32)-c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (96.2%) | `reticulated_vitreous_carbon` (1.2%) | `glassy_carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.7%) | `nickel` (12.0%) | `stainless_steel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.1%) | `platinum_generic` (9.8%) | `nickel_plate` (8.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (97.7%) | `NEt4` (1.2%) | `K` (0.4%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `BF4` (43.0%) | `PF6` (37.1%) | `ClO4` (10.4%) | ✓ |
| 试剂大类 | 103 | `carboxylic_acid` | `water` (11.4%) | `ABSENT` (8.0%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `pyridine_organocat` (0.3%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (62.0%) | `polar_aprotic_nitrile` (22.8%) | `halogenated_aliphatic` (6.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (99%) | `CCOCC` (0%) | `FC(F)(F)c1ccccc1` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(=O)O` | `O` (68%) | `__ABSENT__` (6%) | `C[Si](C)(C)N=[N+]=` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[O]=[Fe][O][Fe]=[O` (0%) | set ✓ / any ✓ |

---

### Reaction #97  yield=52.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_3_e202401225.json) (反应 idx 在该 JSON 内 = #14)

```
O=S(O)C(F)(F)F.[Na].C=C(C)C(=O)n1c(-c2ccc(Cl)cc2)cc2cc(F)ccc21>>CC1(CC(F)(F)F)C(=O)n2c(c(C(F)(F)F)c3cc(F)ccc32)-c2ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (99.3%) | `carbon_felt` (0.2%) | `carbon_generic` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.1%) | `stainless_steel` (4.2%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (84.3%) | `stainless_steel_generic` (12.9%) | `platinum_generic` (1.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (74.7%) | `NBu4` (17.4%) | `Na` (2.9%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (58.7%) | `BF4` (21.3%) | `carboxylate` (12.0%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (20.8%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (42.4%) | `halogenated_aliphatic` (36.1%) | `polar_protic_alcohol` (18.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (89%) | `CC#N` (76%) | `CC(C)=O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` | `__ABSENT__` (100%) | `O` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |

---

### Reaction #98  yield=0.5%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #29)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (43.0%) | `carbon_felt` (39.4%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (46.8%) | `nickel` (33.2%) | `platinum` (10.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_mesh` | `nickel_generic` (54.2%) | `glassy_carbon` (12.9%) | `unknown_electrode` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.0%) | `Li` (16.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `ClO4` (6.8%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (6.2%) | `as_solvent_halogenated_aliphat` (3.6%) | `alkali_carbonate` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (0.6%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.3%) | `aqueous` (25.4%) | `polar_aprotic_amide` (6.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC#N` | `CC#N` (93%) | `O` (90%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (2%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #99  yield=78.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #29)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (43.0%) | `carbon_felt` (39.4%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (46.8%) | `nickel` (33.2%) | `platinum` (10.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_mesh` | `nickel_generic` (54.2%) | `glassy_carbon` (12.9%) | `unknown_electrode` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.0%) | `Li` (16.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `ClO4` (6.8%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_bicarbonate` | `ABSENT` (6.2%) | `as_solvent_halogenated_aliphat` (3.6%) | `alkali_carbonate` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (0.6%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.3%) | `aqueous` (25.4%) | `polar_aprotic_amide` (6.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC#N` | `CC#N` (93%) | `O` (90%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (2%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #100  yield=23.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #29)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (43.0%) | `carbon_felt` (39.4%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (46.8%) | `nickel` (33.2%) | `platinum` (10.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_mesh` | `nickel_generic` (54.2%) | `glassy_carbon` (12.9%) | `unknown_electrode` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (82.0%) | `Li` (16.5%) | `ABSENT` (0.8%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (90.9%) | `ClO4` (6.8%) | `I` (0.7%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (6.2%) | `as_solvent_halogenated_aliphat` (3.6%) | `alkali_carbonate` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (0.6%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.3%) | `aqueous` (25.4%) | `polar_aprotic_amide` (6.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC#N` | `CC#N` (93%) | `O` (90%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (2%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #101  yield=48.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #29)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (43.0%) | `carbon_felt` (39.4%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (46.8%) | `nickel` (33.2%) | `platinum` (10.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_mesh` | `nickel_generic` (54.2%) | `glassy_carbon` (12.9%) | `unknown_electrode` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.0%) | `Li` (16.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `ClO4` (6.8%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `pyridine` | `ABSENT` (6.2%) | `as_solvent_halogenated_aliphat` (3.6%) | `alkali_carbonate` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (0.6%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.3%) | `aqueous` (25.4%) | `polar_aprotic_amide` (6.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC#N` | `CC#N` (93%) | `O` (90%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (2%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #102  yield=36.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #29)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (43.0%) | `carbon_felt` (39.4%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (46.8%) | `nickel` (33.2%) | `platinum` (10.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_mesh` | `nickel_generic` (54.2%) | `glassy_carbon` (12.9%) | `unknown_electrode` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (82.0%) | `Li` (16.5%) | `ABSENT` (0.8%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (90.9%) | `ClO4` (6.8%) | `I` (0.7%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (6.2%) | `as_solvent_halogenated_aliphat` (3.6%) | `alkali_carbonate` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (0.6%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.3%) | `aqueous` (25.4%) | `polar_aprotic_amide` (6.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC#N` | `CC#N` (93%) | `O` (90%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (2%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #103  yield=18.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #29)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (43.0%) | `carbon_felt` (39.4%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (46.8%) | `nickel` (33.2%) | `platinum` (10.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_mesh` | `nickel_generic` (54.2%) | `glassy_carbon` (12.9%) | `unknown_electrode` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.0%) | `Li` (16.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `ClO4` (6.8%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (6.2%) | `as_solvent_halogenated_aliphat` (3.6%) | `alkali_carbonate` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (0.6%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.3%) | `aqueous` (25.4%) | `polar_aprotic_amide` (6.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC#N` | `CC#N` (93%) | `O` (90%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (2%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #104  yield=0.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #29)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (43.0%) | `carbon_felt` (39.4%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (46.8%) | `nickel` (33.2%) | `platinum` (10.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_mesh` | `nickel_generic` (54.2%) | `glassy_carbon` (12.9%) | `unknown_electrode` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.0%) | `Li` (16.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `ClO4` (6.8%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (6.2%) | `as_solvent_halogenated_aliphat` (3.6%) | `alkali_carbonate` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (0.6%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.3%) | `aqueous` (25.4%) | `polar_aprotic_amide` (6.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC#N` | `CC#N` (93%) | `O` (90%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (2%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #105  yield=52.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #29)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (43.0%) | `carbon_felt` (39.4%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (46.8%) | `nickel` (33.2%) | `platinum` (10.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_mesh` | `nickel_generic` (54.2%) | `glassy_carbon` (12.9%) | `unknown_electrode` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.0%) | `Li` (16.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `ClO4` (6.8%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (6.2%) | `as_solvent_halogenated_aliphat` (3.6%) | `alkali_carbonate` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (0.6%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.3%) | `aqueous` (25.4%) | `polar_aprotic_amide` (6.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC#N` | `CC#N` (93%) | `O` (90%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (2%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #106  yield=42.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #29)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (43.0%) | `carbon_felt` (39.4%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (46.8%) | `nickel` (33.2%) | `platinum` (10.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_mesh` | `nickel_generic` (54.2%) | `glassy_carbon` (12.9%) | `unknown_electrode` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.0%) | `Li` (16.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `ClO4` (6.8%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (6.2%) | `as_solvent_halogenated_aliphat` (3.6%) | `alkali_carbonate` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (0.6%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.3%) | `aqueous` (25.4%) | `polar_aprotic_amide` (6.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC#N` | `CC#N` (93%) | `O` (90%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (2%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #107  yield=0.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #29)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (43.0%) | `carbon_felt` (39.4%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (46.8%) | `nickel` (33.2%) | `platinum` (10.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_mesh` | `nickel_generic` (54.2%) | `glassy_carbon` (12.9%) | `unknown_electrode` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.0%) | `Li` (16.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `ClO4` (6.8%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (6.2%) | `as_solvent_halogenated_aliphat` (3.6%) | `alkali_carbonate` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (0.6%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.3%) | `aqueous` (25.4%) | `polar_aprotic_amide` (6.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC#N` | `CC#N` (93%) | `O` (90%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (2%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #108  yield=0.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #29)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (43.0%) | `carbon_felt` (39.4%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (46.8%) | `nickel` (33.2%) | `platinum` (10.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_mesh` | `nickel_generic` (54.2%) | `glassy_carbon` (12.9%) | `unknown_electrode` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.0%) | `Li` (16.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `ClO4` (6.8%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (6.2%) | `as_solvent_halogenated_aliphat` (3.6%) | `alkali_carbonate` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (0.6%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.3%) | `aqueous` (25.4%) | `polar_aprotic_amide` (6.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC#N` | `CC#N` (93%) | `O` (90%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (2%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #109  yield=0.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #29)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (43.0%) | `carbon_felt` (39.4%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (46.8%) | `nickel` (33.2%) | `platinum` (10.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_mesh` | `nickel_generic` (54.2%) | `glassy_carbon` (12.9%) | `unknown_electrode` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.0%) | `Li` (16.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `ClO4` (6.8%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (6.2%) | `as_solvent_halogenated_aliphat` (3.6%) | `alkali_carbonate` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (0.6%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.3%) | `aqueous` (25.4%) | `polar_aprotic_amide` (6.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC#N` | `CC#N` (93%) | `O` (90%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (2%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #110  yield=21.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #29)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (43.0%) | `carbon_felt` (39.4%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (46.8%) | `nickel` (33.2%) | `platinum` (10.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_mesh` | `nickel_generic` (54.2%) | `glassy_carbon` (12.9%) | `unknown_electrode` (5.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.0%) | `Li` (16.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `ClO4` (6.8%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (6.2%) | `as_solvent_halogenated_aliphat` (3.6%) | `alkali_carbonate` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (0.6%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.3%) | `aqueous` (25.4%) | `polar_aprotic_amide` (6.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC#N` | `CC#N` (93%) | `O` (90%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (2%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #111  yield=15.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #0)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccccc1)c1ccc(OC)cc1>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccc(OC)cc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (71.9%) | `carbon_generic` (12.0%) | `glassy_carbon` (10.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (55.9%) | `platinum` (31.6%) | `nickel` (7.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `unknown_electrode` (45.6%) | `nickel_generic` (12.5%) | `platinum_wire` (7.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (86.7%) | `Li` (12.1%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (92.5%) | `ClO4` (4.9%) | `Br` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (5.9%) | `boron_lewis_acid` (2.8%) | `alkali_carbonate` (2.6%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.6%) | `Fe_complex` (3.0%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.8%) | `aqueous` (11.2%) | `polar_aprotic_amide` (6.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (90%) | `O` (87%) | `CO` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #112  yield=13.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #1)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(F)cc1)c1ccc(OC)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(OC)cc1)c1ccc(F)cc1)(C(=O)OCC)C(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (71.1%) | `carbon_generic` (16.2%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (81.3%) | `platinum` (15.8%) | `sacrificial_iron` (1.2%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `unknown_electrode` (30.8%) | `glassy_carbon` (12.1%) | `platinum_plate` (9.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (78.0%) | `Li` (14.9%) | `Na` (5.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (80.3%) | `molecular_no_ion` (5.9%) | `ClO4` (3.9%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (13.2%) | `boron_lewis_acid` (4.6%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.3%) | `Fe_complex` (2.6%) | `Mn_complex` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (90.5%) | `polar_protic_alcohol` (2.3%) | `aqueous` (1.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (88%) | `O` (83%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl-].[Cl-].[Mn+2]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #113  yield=34.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #2)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC1(O)c2ccccc2-c2ccccc21>>CCOC(=O)C(CC1C(=O)c2ccccc2-c2ccccc21)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `platinum` (1.4%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (25.5%) | `glassy_carbon` (15.4%) | `carbon_generic` (15.0%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.5%) | `carbon` (0.5%) | `ABSENT` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_generic` (59.1%) | `platinum_plate` (40.8%) | `graphite_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (69.8%) | `NBu4` (19.2%) | `Li` (8.4%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (94.6%) | `BF4` (3.1%) | `I` (1.9%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (11.9%) | `carboxylic_acid` (5.0%) | `boron_lewis_acid` (4.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.9%) | `organic_neutral_cat` (1.7%) | `ammonium_PTC_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (82.8%) | `ABSENT` (7.2%) | `cyclic_ether` (6.5%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (1%) | `ClCCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br][Mn][Br]` (0%) | set ✓ / any ✓ |

---

### Reaction #114  yield=39.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #3)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC1(O)c2cc(C(C)(C)C)ccc2-c2ccc(C(C)(C)C)cc21>>CCOC(=O)C(CC1C(=O)c2cc(C(C)(C)C)ccc2-c2cc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `ABSENT` (1.2%) | `sacrificial_magnesium` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (43.8%) | `ABSENT` (20.4%) | `glassy_carbon` (10.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (52.2%) | `platinum` (38.5%) | `ABSENT` (8.6%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (31.7%) | `platinum_plate` (28.0%) | `ABSENT` (20.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (49.2%) | `NEt4` (42.0%) | `Li` (6.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (62.6%) | `I` (32.4%) | `BF4` (3.9%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (16.3%) | `ketone` (2.6%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (68.3%) | `cyclic_ether` (15.9%) | `ABSENT` (13.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `C1CCOC1` (3%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `Oc1ccccc1C=NCCN=Cc` (0%) | set ✓ / any ✓ |

---

### Reaction #115  yield=47.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #4)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(Cc1ccccc1)c1ccccc1>>CCOC(=O)C(CC(C(=O)Cc1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (89.4%) | `platinum` (6.9%) | `sacrificial_zinc` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (89.3%) | `zinc_plate` (7.6%) | `glassy_carbon` (1.0%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `sacrificial_zinc` (33.3%) | `platinum` (26.7%) | `carbon` (19.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `zinc_plate` (32.7%) | `unknown_electrode` (27.2%) | `stainless_steel_generic` (10.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (67.0%) | `NBu4` (20.4%) | `Li` (11.7%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Br` (46.6%) | `Cl` (27.0%) | `ClO4` (13.3%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `o2_oxidant` (25.5%) | `ABSENT` (6.6%) | `boron_lewis_acid` (4.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `Mn_complex` (0.5%) | `ammonium_PTC_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (55.0%) | `halogenated_aliphatic` (14.9%) | `polar_protic_alcohol` (10.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (58%) | `ClCCl` (12%) | `CCCCn1cc[n+](C)c1.` (6%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `O` | `O=O` (100%) | `CC[SiH](CC)CC` (11%) | `OB(O)B(O)O` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Cl][Mn][Cl]` (0%) | `CC(C)(C)c1cc(C=N[C` (0%) | set ✓ / any ✓ |

---

### Reaction #116  yield=53.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #5)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccccc1)c1ccc(OC)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(OC)cc1)c1ccccc1)(C(=O)OCC)C(=O)OCC…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (64.9%) | `carbon_generic` (21.0%) | `glassy_carbon` (10.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (64.1%) | `platinum` (24.6%) | `nickel` (7.9%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `unknown_electrode` (30.4%) | `nickel_generic` (21.9%) | `platinum_plate` (8.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (87.1%) | `Li` (11.8%) | `ABSENT` (0.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (90.6%) | `ClO4` (6.0%) | `Br` (1.0%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (8.2%) | `boron_lewis_acid` (2.7%) | `as_solvent_halogenated_aliphat` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.9%) | `Fe_complex` (1.1%) | `Mn_complex` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (78.6%) | `aqueous` (7.8%) | `polar_aprotic_amide` (4.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (96%) | `O` (76%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #117  yield=51.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #1)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(F)cc1)c1ccc(OC)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(OC)cc1)c1ccc(F)cc1)(C(=O)OCC)C(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (71.1%) | `carbon_generic` (16.2%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (81.3%) | `platinum` (15.8%) | `sacrificial_iron` (1.2%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `unknown_electrode` (30.8%) | `glassy_carbon` (12.1%) | `platinum_plate` (9.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.0%) | `Li` (14.9%) | `Na` (5.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (80.3%) | `molecular_no_ion` (5.9%) | `ClO4` (3.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (13.2%) | `boron_lewis_acid` (4.6%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.3%) | `Fe_complex` (2.6%) | `Mn_complex` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (90.5%) | `polar_protic_alcohol` (2.3%) | `aqueous` (1.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (88%) | `O` (83%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl-].[Cl-].[Mn+2]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #118  yield=56.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #7)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(OCCCCl)cc1)c1ccc(OCCCCl)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(OCCCCl)cc1)c1ccc(OCCCC…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `sacrificial_iron` (0.5%) | `sacrificial_magnesium` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_generic` (81.3%) | `carbon_felt` (8.8%) | `magnesium_plate` (4.0%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (90.3%) | `nickel` (5.1%) | `platinum` (3.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_plate` (29.8%) | `nickel_generic` (24.0%) | `nickel_foam` (15.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (66.3%) | `NBu4` (33.2%) | `Na` (0.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (64.7%) | `ClO4` (28.7%) | `I` (2.3%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (12.7%) | `as_solvent_halogenated_aliphat` (3.6%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.9%) | `Mn_complex` (2.2%) | `Fe_complex` (2.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (92.1%) | `aqueous` (2.8%) | `polar_aprotic_amide` (1.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (81%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `[Na+].[OH-]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #119  yield=59.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #8)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(OCCCCC(=O)OC)cc1)c1ccc(OCCCCC(=O)OC)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(OCCCCC(=O)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.1%) | `sacrificial_magnesium` (7.8%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (45.1%) | `carbon_generic` (35.0%) | `reticulated_vitreous_carbon` (8.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (56.0%) | `carbon` (31.0%) | `nickel` (6.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `unknown_electrode` (32.3%) | `platinum_generic` (21.4%) | `nickel_generic` (20.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (83.2%) | `NBu4` (16.7%) | `ABSENT` (0.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (86.1%) | `BF4` (12.8%) | `molecular_no_ion` (0.6%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (3.8%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (88.5%) | `Fe_complex` (6.9%) | `Mn_complex` (2.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.4%) | `polar_aprotic_amide` (18.7%) | `ABSENT` (4.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (97%) | `O` (77%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `Cl` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #120  yield=58.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #9)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCC(C(=O)OC)C(=O)OC>>CCC(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OC)C(=O)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (71.8%) | `carbon_generic` (14.8%) | `reticulated_vitreous_carbon` (6.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (61.6%) | `nickel` (23.3%) | `sacrificial_iron` (11.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (77.2%) | `iron_generic` (8.3%) | `nickel_generic` (7.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (92.1%) | `Li` (7.0%) | `Mg` (0.4%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (84.0%) | `ClO4` (14.5%) | `molecular_no_ion` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (16.7%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.5%) | `Fe_complex` (4.8%) | `Cu_complex` (3.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (60.6%) | `polar_aprotic_nitrile` (20.8%) | `polar_aprotic_amide` (12.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CO` (79%) | `CC#N` (18%) | `O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `[Cl-].[Na+]` (0%) | `O=P([O-])([O-])[O-` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #121  yield=53.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #10)

```
COC(=O)CC(=O)OC.C=CC(O)(c1ccccc1)c1ccccc1>>COC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)C(=O)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `sacrificial_iron` (1.0%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_generic` (46.4%) | `graphite_plate` (36.0%) | `reticulated_vitreous_carbon` (6.8%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (61.3%) | `nickel` (26.6%) | `platinum` (7.6%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `nickel_generic` (59.8%) | `graphite_plate` (27.6%) | `glassy_carbon` (1.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (76.4%) | `Li` (22.1%) | `Na` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (57.0%) | `carboxylate` (15.2%) | `molecular_no_ion` (10.9%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (16.2%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.9%) | `ammonium_PTC_organocat` (6.1%) | `Mn_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (53.3%) | `ketone` (15.1%) | `acyclic_ether` (8.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (86%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `[H+].[OH-]` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #122  yield=56.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #11)

```
COC(=O)C(C)C(=O)OC.C=CC(O)(c1ccccc1)c1ccccc1>>COC(=O)C(C)(CC(C(=O)c1ccccc1)c1ccccc1)C(=O)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `sacrificial_iron` (0.4%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_generic` (54.4%) | `glassy_carbon` (23.4%) | `carbon_plate` (6.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (44.9%) | `platinum` (38.8%) | `carbon` (13.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_foam` | `nickel_generic` (56.4%) | `glassy_carbon` (25.5%) | `platinum_plate` (5.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.7%) | `Li` (0.8%) | `Mg` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (84.7%) | `Br` (5.0%) | `I` (4.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (22.9%) | `as_solvent_halogenated_aliphat` (4.7%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.2%) | `Fe_complex` (1.8%) | `ammonium_PTC_organocat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_protic_alcohol` (50.0%) | `polar_aprotic_nitrile` (36.7%) | `halogenated_aliphatic` (3.5%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `O` (87%) | `CC#N` (61%) | `CO` (37%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (1%) | `CCN(CC)CC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #123  yield=56.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #12)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccccc1)c1ccccc1Cl>>CCOC(=O)C(CC(C(=O)c1ccccc1Cl)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `sacrificial_iron` (1.1%) | `platinum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (61.1%) | `graphite_generic` (15.9%) | `glassy_carbon` (13.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (74.8%) | `platinum` (14.6%) | `nickel` (6.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (27.1%) | `carbon_felt` (22.3%) | `graphite_felt` (7.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (83.6%) | `Li` (8.4%) | `NEt4` (7.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (76.8%) | `Br` (9.5%) | `ClO4` (8.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (7.9%) | `o2_oxidant` (3.1%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `Mn_complex` (0.1%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (94.5%) | `polar_aprotic_amide` (2.0%) | `ABSENT` (1.8%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (94%) | `O` (12%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #124  yield=56.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #13)

```
CCOC(=O)CC(=O)OCC.C=CC(O)(c1ccccc1)c1ccccc1>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `sacrificial_iron` (0.9%) | `sacrificial_aluminum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (69.3%) | `carbon_generic` (12.0%) | `graphite_generic` (4.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (54.3%) | `nickel` (41.1%) | `platinum` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `nickel_generic` (58.8%) | `graphite_plate` (17.0%) | `nickel_foam` (11.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (59.8%) | `NBu4` (39.9%) | `Na` (0.2%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (83.8%) | `BF4` (7.6%) | `molecular_no_ion` (6.7%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (8.2%) | `alkali_carbonate` (3.1%) | `as_solvent_halogenated_aliphat` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (82.8%) | `ammonium_PTC_organocat` (9.9%) | `Co_complex` (1.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `ketone` (28.5%) | `polar_aprotic_nitrile` (26.3%) | `polar_aprotic_amide` (11.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (13%) | `O` (4%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `CCN(CC)CC` (0%) | `O=P([O-])([O-])[O-` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #125  yield=67.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #14)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(OCC(F)F)cc1)c1ccc(OCC(F)F)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(OCC(F)F)cc1)c1ccc(OC…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `sacrificial_iron` (0.2%) | `sacrificial_aluminum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_generic` (66.0%) | `carbon_felt` (15.2%) | `graphite_generic` (7.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (92.2%) | `nickel` (3.4%) | `platinum` (3.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `nickel_generic` (35.4%) | `unknown_electrode` (18.3%) | `glassy_carbon` (10.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (80.2%) | `Li` (18.3%) | `Na` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (85.3%) | `ClO4` (7.9%) | `I` (2.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (10.9%) | `boron_lewis_acid` (4.6%) | `hcl` (4.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `Mn_complex` (0.5%) | `Fe_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (76.3%) | `aqueous` (7.6%) | `polar_aprotic_sulfoxide` (4.3%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `O` (99%) | `CC#N` (92%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `Cl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #126  yield=64.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #15)

```
CCOC(=O)C(F)C(=O)OCC.C=CC(O)(c1ccccc1)c1ccccc1>>CCOC(=O)C(F)(CC(C(=O)c1ccccc1)c1ccccc1)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_iron` | `carbon` (99.8%) | `sacrificial_iron` (0.1%) | `platinum` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `iron_plate` | `reticulated_vitreous_carbon` (52.9%) | `carbon_felt` (37.0%) | `carbon_generic` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (57.8%) | `carbon` (33.5%) | `platinum` (7.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_foam` | `nickel_foam` (45.2%) | `nickel_generic` (36.5%) | `platinum_plate` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.0%) | `Li` (3.9%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (97.6%) | `ClO4` (1.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (8.8%) | `alkali_carbonate` (6.6%) | `as_solvent_halogenated_aliphat` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.5%) | `Fe_complex` (2.0%) | `Mn_complex` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (40.7%) | `aqueous` (22.8%) | `polar_protic_alcohol` (18.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (51%) | `CO` (44%) | `O` (42%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (3%) | `O=C([O-])[O-].[Cs+` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #127  yield=64.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #16)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(OCCCOc2ccccc2)cc1)c1ccc(OCCCOc2ccccc2)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(OCCCOc2c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `sacrificial_iron` (0.3%) | `sacrificial_magnesium` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (55.0%) | `carbon_felt` (36.6%) | `reticulated_vitreous_carbon` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (50.4%) | `nickel` (33.1%) | `platinum` (14.9%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `nickel_foam` (58.4%) | `nickel_generic` (27.2%) | `platinum_generic` (3.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (50.3%) | `Li` (49.2%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (52.9%) | `ClO4` (38.1%) | `I` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (7.6%) | `as_solvent_halogenated_aliphat` (3.9%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.5%) | `Mn_complex` (1.5%) | `Fe_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (77.3%) | `polar_aprotic_amide` (8.4%) | `aqueous` (6.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (92%) | `O` (64%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #128  yield=63.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #17)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(OCCOC)cc1)c1ccc(OCCOC)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(OCCOC)cc1)c1ccc(OCCOC)cc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.1%) | `platinum` (3.7%) | `sacrificial_magnesium` (1.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_generic` (60.0%) | `carbon_felt` (22.2%) | `glassy_carbon` (4.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (42.9%) | `platinum` (35.6%) | `nickel` (19.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `nickel_generic` (24.7%) | `nickel_foam` (20.7%) | `platinum_generic` (19.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (67.2%) | `Li` (32.6%) | `K` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (63.9%) | `ClO4` (34.6%) | `I` (0.6%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (8.2%) | `metal_oxide_oxidant` (2.5%) | `tellurium_reagent` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.4%) | `Fe_complex` (2.4%) | `Co_complex` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (54.6%) | `polar_aprotic_amide` (24.4%) | `polar_protic_alcohol` (11.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (93%) | `O` (56%) | `CO` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `Cl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #129  yield=63.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #18)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(F)cc1)c1ccc(F)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(F)cc1)c1ccc(F)cc1)(C(=O)OCC)C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `sacrificial_iron` (0.3%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (58.8%) | `graphite_generic` (20.8%) | `carbon_generic` (12.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (97.6%) | `platinum` (1.2%) | `sacrificial_iron` (0.7%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (40.1%) | `unknown_electrode` (14.8%) | `glassy_carbon` (13.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.6%) | `Li` (42.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (73.5%) | `ClO4` (8.0%) | `molecular_no_ion` (7.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (10.8%) | `boron_lewis_acid` (4.9%) | `as_solvent_halogenated_aliphat` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.8%) | `Mn_complex` (3.1%) | `Fe_complex` (2.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (87.1%) | `polar_protic_alcohol` (2.9%) | `aqueous` (2.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `O` (82%) | `CC#N` (74%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `Cl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #130  yield=69.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #19)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(OCCCO[Si](c2ccccc2)(c2ccccc2)C(C)(C)C)cc1)c1ccc(OCCCO[Si](c2ccccc2)(c2ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_magnesium` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (51.6%) | `carbon_felt` (31.5%) | `magnesium_plate` (6.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (94.5%) | `platinum` (3.5%) | `nickel` (1.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (55.7%) | `graphite_plate` (16.8%) | `nickel_generic` (7.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (60.7%) | `NBu4` (30.0%) | `Li` (8.4%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (69.6%) | `ABSENT` (27.6%) | `ClO4` (1.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (14.0%) | `boron_lewis_acid` (3.1%) | `electrophilic_N_F` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (84.4%) | `Mn_complex` (15.1%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (95.2%) | `aqueous` (1.6%) | `polar_aprotic_amide` (1.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (7%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #131  yield=66.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #20)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccccc1)c1ccc(C(F)(F)F)cc1>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccc(C(F)(F)F)cc1)(C(=O)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (44.0%) | `graphite_generic` (42.8%) | `carbon_generic` (7.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (76.7%) | `platinum` (15.9%) | `nickel` (5.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (18.4%) | `carbon_felt` (18.0%) | `unknown_electrode` (14.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.4%) | `Li` (3.8%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (94.7%) | `ClO4` (3.5%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (5.9%) | `as_solvent_polar_aprotic_amide` (2.8%) | `o2_oxidant` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.5%) | `Fe_complex` (0.9%) | `Mn_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (75.1%) | `polar_protic_alcohol` (8.9%) | `aqueous` (7.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (93%) | `O` (60%) | `CO` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #132  yield=62.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #21)

```
CCOC(=O)C(C(=O)OCC)C(=O)c1ccccc1.C=CC(O)(c1ccccc1)c1ccccc1>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `ABSENT` (0.2%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_generic` (55.8%) | `carbon_felt` (32.6%) | `glassy_carbon` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (59.5%) | `platinum` (20.9%) | `carbon` (15.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_foam` | `nickel_generic` (54.6%) | `platinum_plate` (12.4%) | `glassy_carbon` (8.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (80.3%) | `Li` (17.5%) | `ABSENT` (1.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (92.6%) | `ClO4` (5.0%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `as_solvent_halogenated_aliphat` (6.4%) | `ABSENT` (3.7%) | `alkali_carbonate` (3.6%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.7%) | `Mn_complex` (1.2%) | `Cu_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (36.7%) | `aqueous` (34.8%) | `polar_protic_alcohol` (11.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `O` (91%) | `CC#N` (89%) | `CO` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `O=P([O-])([O-])[O-` (66%) | `CS(C)=O` (17%) | `__ABSENT__` (13%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Pt]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #133  yield=61.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #22)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(Br)cc1)c1ccc(Br)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(Br)cc1)c1ccc(Br)cc1)(C(=O)OCC)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `sacrificial_iron` (0.5%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (45.4%) | `carbon_generic` (42.2%) | `graphite_generic` (5.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (86.8%) | `platinum` (7.0%) | `nickel` (3.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `carbon_felt` (19.4%) | `unknown_electrode` (11.2%) | `nickel_generic` (10.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (79.3%) | `Li` (19.1%) | `ABSENT` (1.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.0%) | `ClO4` (9.7%) | `I` (5.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (9.8%) | `as_solvent_halogenated_aliphat` (3.2%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.1%) | `Fe_complex` (3.9%) | `Mn_complex` (2.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (95.0%) | `aqueous` (1.5%) | `polar_protic_alcohol` (0.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (88%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #134  yield=61.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #23)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)CS(=O)(=O)c1ccccc1>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)S(=O)(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_generic` (92.9%) | `graphite_plate` (4.5%) | `carbon_felt` (1.5%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (82.9%) | `platinum` (8.2%) | `nickel` (8.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (52.0%) | `nickel_generic` (31.3%) | `graphite_plate` (9.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (94.3%) | `Li` (4.9%) | `Na` (0.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (80.9%) | `ClO4` (9.5%) | `molecular_no_ion` (4.9%) | ✗ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (25.2%) | `boron_lewis_acid` (2.1%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.4%) | `ammonium_PTC_organocat` (2.8%) | `Mn_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (67.0%) | `polar_protic_alcohol` (24.1%) | `halogenated_aliphatic` (2.5%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (97%) | `O` (1%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #135  yield=62.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #24)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(OCCCOCc2ccccc2)cc1)c1ccc(OCCCOCc2ccccc2)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(OCCCOC…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `sacrificial_iron` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_generic` (84.5%) | `carbon_felt` (11.2%) | `graphite_generic` (1.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (43.0%) | `platinum` (23.5%) | `nickel` (20.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_generic` (24.3%) | `iron_generic` (23.4%) | `nickel_foam` (22.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (67.6%) | `NBu4` (29.3%) | `Na` (2.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (33.2%) | `I` (23.4%) | `BF4` (23.2%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (25.1%) | `as_solvent_halogenated_aliphat` (2.8%) | `borohydride` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.1%) | `Fe_complex` (2.7%) | `Mn_complex` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (88.7%) | `aqueous` (6.0%) | `ketone` (2.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (80%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #136  yield=61.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #25)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccccc1)c1ccncc1>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccncc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (69.3%) | `carbon_generic` (23.1%) | `graphite_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (47.7%) | `platinum` (34.1%) | `nickel` (12.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (23.6%) | `nickel_generic` (13.4%) | `unknown_electrode` (11.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.4%) | `Li` (3.7%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (98.4%) | `ClO4` (1.1%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (3.7%) | `alkali_carbonate` (2.7%) | `electrophilic_N_F` (2.6%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (88.5%) | `pyridine_organocat` (8.4%) | `Mn_complex` (1.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (91.6%) | `aqueous` (3.2%) | `polar_protic_alcohol` (2.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (72%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #137  yield=71.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #26)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(OCCCCCCCC)cc1)c1ccc(OCCCCCCCC)cc1>>CCCCCCCCOc1ccc(C(=O)C(CC(C(=O)OCC)(C(=O)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `sacrificial_iron` (0.3%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_generic` (70.7%) | `carbon_felt` (20.7%) | `graphite_generic` (2.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (65.6%) | `platinum` (14.3%) | `sacrificial_iron` (10.1%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `unknown_electrode` (42.2%) | `nickel_generic` (32.1%) | `iron_generic` (3.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (87.1%) | `NBu4` (12.4%) | `Na` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (48.0%) | `BF4` (20.0%) | `molecular_no_ion` (19.8%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (8.7%) | `as_solvent_halogenated_aliphat` (3.7%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.9%) | `Fe_complex` (1.9%) | `Mn_complex` (1.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (90.2%) | `aqueous` (2.3%) | `polar_aprotic_amide` (1.8%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (93%) | `O` (77%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #138  yield=73.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #27)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(OC)cc1)c1ccc(OC)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(OC)cc1)c1ccc(OC)cc1)(C(=O)OCC)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (53.9%) | `carbon_generic` (25.6%) | `glassy_carbon` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (71.4%) | `platinum` (20.7%) | `nickel` (4.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `unknown_electrode` (70.5%) | `nickel_generic` (9.1%) | `glassy_carbon` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (72.1%) | `Li` (26.3%) | `Na` (0.7%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (79.9%) | `ClO4` (13.5%) | `molecular_no_ion` (2.6%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `boron_lewis_acid` (8.0%) | `ABSENT` (6.4%) | `hcl` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.1%) | `Fe_complex` (3.3%) | `Mn_complex` (2.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (75.0%) | `aqueous` (10.9%) | `polar_aprotic_amide` (3.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (97%) | `O` (95%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `O` | `CCCC[N+](CCCC)(CCC` (38%) | `Cl` (10%) | `__ABSENT__` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #139  yield=76.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #28)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(C)cc1)c1ccc(C)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(C)cc1)c1ccc(C)cc1)(C(=O)OCC)C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `sacrificial_iron` (0.7%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (41.9%) | `carbon_generic` (25.6%) | `glassy_carbon` (16.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (86.5%) | `nickel` (8.4%) | `platinum` (4.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `glassy_carbon` (33.5%) | `nickel_generic` (21.4%) | `unknown_electrode` (8.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.3%) | `Li` (25.7%) | `ABSENT` (1.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (84.5%) | `ClO4` (10.9%) | `ABSENT` (1.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `boron_lewis_acid` (11.0%) | `as_solvent_halogenated_aliphat` (6.8%) | `ABSENT` (4.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.0%) | `Mn_complex` (3.3%) | `Fe_complex` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (65.2%) | `aqueous` (17.9%) | `polar_aprotic_amide` (7.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `O` (97%) | `CC#N` (97%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `CCCC[N+](CCCC)(CCC` (48%) | `Cl` (11%) | `O=P([O-])([O-])[O-` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #140  yield=78.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #29)

```
C=CC(O)(c1ccccc1)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_plate` | `carbon_generic` (43.0%) | `carbon_felt` (39.4%) | `glassy_carbon` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (46.8%) | `nickel` (33.2%) | `platinum` (10.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_mesh` | `nickel_generic` (54.2%) | `glassy_carbon` (12.9%) | `unknown_electrode` (5.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.0%) | `Li` (16.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.9%) | `ClO4` (6.8%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (6.2%) | `as_solvent_halogenated_aliphat` (3.6%) | `alkali_carbonate` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (0.6%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (58.3%) | `aqueous` (25.4%) | `polar_aprotic_amide` (6.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` + `CC#N` | `CC#N` (93%) | `O` (90%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (99%) | `O=P([O-])([O-])[O-` (2%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #141  yield=71.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #30)

```
COC(=O)C(C(=O)OC)C(=O)OC.C=CC(O)(c1ccccc1)c1ccccc1>>COC(=O)C(CC(C(=O)c1ccccc1)c1ccccc1)(C(=O)OC)C(=O)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `sacrificial_iron` (0.2%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_generic` (56.4%) | `carbon_felt` (29.5%) | `glassy_carbon` (6.4%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (39.0%) | `nickel` (27.3%) | `carbon` (25.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `nickel_generic` (43.0%) | `platinum_plate` (18.7%) | `platinum_foil` (12.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.9%) | `Li` (5.1%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (94.2%) | `ClO4` (3.9%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (7.0%) | `as_solvent_halogenated_aliphat` (6.9%) | `alkali_carbonate` (3.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (69.0%) | `Mn_complex` (19.9%) | `Fe_complex` (6.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `aqueous` (42.4%) | `polar_aprotic_nitrile` (31.2%) | `polar_protic_alcohol` (13.5%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `O` (96%) | `CC#N` (82%) | `CC(=O)OC(C)=O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (98%) | `O=P([O-])([O-])[O-` (26%) | `O` (4%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `[Cl][Mn][Cl]` (3%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #142  yield=76.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #31)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(Cl)cc1)c1ccc(Cl)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(Cl)cc1)c1ccc(Cl)cc1)(C(=O)OCC)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (53.5%) | `carbon_generic` (30.6%) | `graphite_generic` (8.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (87.8%) | `platinum` (9.2%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (26.6%) | `nickel_generic` (12.8%) | `graphite_generic` (10.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (51.7%) | `NBu4` (43.8%) | `ABSENT` (3.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (72.1%) | `ClO4` (14.2%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (7.8%) | `boron_lewis_acid` (7.6%) | `as_solvent_halogenated_aliphat` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.4%) | `Mn_complex` (5.8%) | `Fe_complex` (2.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (88.9%) | `aqueous` (6.9%) | `polar_aprotic_amide` (1.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `O` (97%) | `CC#N` (97%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #143  yield=71.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #32)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(OC[Si](C)(C)C)cc1)c1ccc(OC[Si](C)(C)C)cc1>>CCOC(=O)C(CC(C(=O)c1ccc(OC[Si](C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `sacrificial_magnesium` (0.2%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_felt` (86.4%) | `graphite_generic` (5.4%) | `carbon_generic` (3.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (87.1%) | `nickel` (7.5%) | `platinum` (4.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `nickel_generic` (37.7%) | `nickel_foam` (9.0%) | `graphite_generic` (8.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (70.1%) | `Li` (29.1%) | `Na` (0.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (63.7%) | `ClO4` (30.2%) | `molecular_no_ion` (3.0%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (10.6%) | `boron_lewis_acid` (7.8%) | `hcl` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.9%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (83.9%) | `aqueous` (4.9%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `O` (86%) | `CC#N` (85%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C(O)O.[Na]` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `Cl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #144  yield=72.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_9_e202401522.json) (反应 idx 在该 JSON 内 = #33)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=CC(O)(c1ccc(OCCO[Si](C)(C)C(C)(C)C)cc1)c1ccc(OCCO[Si](C)(C)C(C)(C)C)cc1>>CCOC(=O)C(CC(C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.5%) | `platinum` (0.7%) | `sacrificial_magnesium` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_generic` (77.7%) | `carbon_felt` (7.0%) | `glassy_carbon` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (89.4%) | `platinum` (4.5%) | `nickel` (3.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_rod` (25.4%) | `glassy_carbon` (16.5%) | `nickel_generic` (13.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.6%) | `Li` (14.9%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (77.9%) | `ClO4` (13.7%) | `I` (6.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (11.9%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Fe_complex` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (86.3%) | `polar_aprotic_amide` (3.9%) | `aqueous` (3.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (77%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O` | `__ABSENT__` (100%) | `O=P([O-])([O-])[O-` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #145  yield=0.5%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #146  yield=77.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #147  yield=36.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #148  yield=12.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #149  yield=0.5%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #150  yield=29.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #151  yield=19.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #152  yield=0.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #153  yield=42.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #154  yield=23.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #155  yield=0.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #156  yield=0.5%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `solvent_mixture` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #157  yield=0.5%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #158  yield=0.5%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `pyridine` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #159  yield=0.0%

**Source paper**: [`AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/10.1002_adsc.202500174_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1.CCOC(=O)C(C(=O)OCC)C(=O)OCC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #160  yield=39.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #0)

```
CCOC(=O)C(CC)C(=O)OCC.C=C(C)c1ccccc1NC(=O)c1ccccc1>>CCOC(=O)C(CC)(CC1(C)OC(c2ccccc2)=Nc2ccccc21)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `platinum` (0.9%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (86.8%) | `graphite_rod` (11.2%) | `graphite_plate` (1.0%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (52.0%) | `nickel` (30.9%) | `sacrificial_aluminum` (11.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (99.1%) | `ABSENT` (0.3%) | `platinum_generic` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (60.4%) | `ABSENT` (38.9%) | `NEt4` (0.4%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `PF6` (68.3%) | `ABSENT` (23.7%) | `BF4` (7.2%) | ✗ |
| 试剂大类 | 103 | `alkali_alkoxide` | `alkali_sulfinate` (22.1%) | `ABSENT` (5.1%) | `bromide_anion` (3.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.1%) | `Cu_complex` (4.8%) | `organic_neutral_cat` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (36.6%) | `polar_protic_alcohol` (27.3%) | `polar_aprotic_amide` (15.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CO` (99%) | `O=C(O)C(F)(F)F` (43%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)[O-].[K+]` | `O=S(=O)(O)O` (88%) | `N#C[S-].[NH4+]` (85%) | `__ABSENT__` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (83%) | `CC(C)c1cc(C(C)C)c(` (16%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #161  yield=38.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #1)

```
CCOC(=O)C(CCC#N)C(=O)OCC.C=C(c1ccccc1)c1ccccc1NC(=O)c1ccc(OC)cc1>>CCOC(=O)C(CCC#N)(CC1(c2ccccc2)OC(c2ccc(OC)cc2)=Nc2c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.5%) | `platinum` (11.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (47.4%) | `platinum_plate` (45.9%) | `graphite_rod` (2.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `carbon` (0.3%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (99.1%) | `platinum_generic` (0.9%) | `carbon_rod` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (90.7%) | `ABSENT` (6.8%) | `Li` (2.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (54.9%) | `ClO4` (21.6%) | `ABSENT` (13.9%) | ✓ |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (19.7%) | `alkali_bicarbonate` (3.3%) | `tetraaryl_borate` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (84.5%) | `organic_neutral_cat` (9.7%) | `Cu_complex` (3.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.7%) | `ABSENT` (0.1%) | `halogenated_aliphatic` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (1%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)[O-].[K+]` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `Cc1ccc([P+](=O)c2c` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC[N+](CC)(CC)CC.F` (0%) | `N#Cc1c(C#N)c(-n2c3` (0%) | set ✓ / any ✓ |

---

### Reaction #162  yield=42.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #2)

```
CCOC(=O)C(C(=O)OCC)C(=O)c1ccccc1.C=C(c1ccccc1)c1ccccc1NC(=O)c1ccc(OC)cc1>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccc(OC)cc2)=Nc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.2%) | `platinum` (3.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (84.6%) | `carbon_felt` (7.1%) | `platinum_plate` (4.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.9%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (99.0%) | `platinum_generic` (1.0%) | `ABSENT` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (79.6%) | `Li` (15.6%) | `ABSENT` (2.6%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (65.4%) | `ClO4` (21.5%) | `PF6` (8.0%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (8.0%) | `carboxylic_acid` (7.3%) | `electrophilic_N_F` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.8%) | `organic_neutral_cat` (38.5%) | `ionic_organocat` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (88.9%) | `halogenated_aliphatic` (3.2%) | `nitroalkane` (1.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (94%) | `O` (21%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (95%) | `[Fe+2].c1cc[cH-]c1` (2%) | `CC[N+](CC)(CC)CC.F` (1%) | set ✓ / any ✓ |

---

### Reaction #163  yield=41.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #3)

```
CCOC(=O)C(C(=O)OCC)C(=O)c1ccc(C)cc1.C=C(c1ccccc1)c1ccccc1NC(=O)c1ccc(OC)cc1>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccc(OC)cc2)=…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (4.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (93.8%) | `platinum_plate` (2.4%) | `carbon_felt` (1.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (99.7%) | `platinum_generic` (0.3%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (85.1%) | `Li` (9.6%) | `ABSENT` (2.8%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (71.8%) | `ClO4` (18.2%) | `PF6` (5.6%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `carboxylic_acid` (10.4%) | `ABSENT` (6.6%) | `electrophilic_N_F` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (83.3%) | `organic_neutral_cat` (11.3%) | `triarylamine_radical_cat` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.1%) | `halogenated_aliphatic` (1.6%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (97%) | `O` (1%) | `CO` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `O=C(O)C(F)(F)F` (29%) | `[Cl-].[Cl-].[Mg+2]` (20%) | `OC(C(F)(F)F)C(F)(F` (12%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Fe+2].c1cc[cH-]c1` (1%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #164  yield=42.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #4)

```
CCOC(=O)CC(=O)OCC.C=C(C)c1ccccc1NC(=O)c1ccccc1>>CCOC(=O)C(CC1(C)OC(c2ccccc2)=Nc2ccccc21)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (87.1%) | `ABSENT` (7.7%) | `platinum` (3.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `reticulated_vitreous_carbon` (50.1%) | `ABSENT` (17.4%) | `graphite_plate` (12.7%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (90.9%) | `ABSENT` (3.5%) | `nickel` (2.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (69.5%) | `platinum_generic` (28.9%) | `ABSENT` (1.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (93.1%) | `ABSENT` (6.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (79.0%) | `ABSENT` (18.7%) | `K` (0.8%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `PF6` (36.9%) | `BF4` (27.7%) | `ABSENT` (26.1%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `alkali_sulfinate` (11.1%) | `alkali_carbonate` (5.7%) | `ABSENT` (3.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (44.3%) | `organic_neutral_cat` (33.2%) | `Ir_complex` (4.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (85.5%) | `polar_protic_alcohol` (7.5%) | `polar_aprotic_amide` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `O=C(O)C(F)(F)F` (90%) | `CO` (73%) | `CC#N` (27%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `O=S(=O)(O)O` (98%) | `N#C[S-].[NH4+]` (95%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `CC(C)c1cc(C(C)C)c(` (78%) | `__ABSENT__` (20%) | `N#Cc1c(C#N)c(-n2c3` (0%) | set ✗ / any ✓ |

---

### Reaction #165  yield=45.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #5)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1C(=O)NC1CC1>>CCOC(=O)C(CC1(c2ccccc2)O/C(=N\C2CC2)c2ccccc21)(C(=O)OCC…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (76.9%) | `carbon_rod` (8.5%) | `carbon_generic` (8.3%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.1%) | `carbon` (1.5%) | `nickel` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (96.7%) | `platinum_generic` (1.9%) | `carbon_rod` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (95.1%) | `Li` (4.4%) | `ABSENT` (0.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (92.5%) | `ClO4` (6.4%) | `PF6` (0.9%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `azide_source` (5.0%) | `ABSENT` (4.1%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.3%) | `Fe_complex` (3.3%) | `ferrocene_mediator` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (99.6%) | `polar_protic_alcohol` (0.2%) | `polar_aprotic_nitrile` (0.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `__ABSENT__` (94%) | `CO` (1%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `C[Si](C)(C)N=[N+]=` (91%) | `__ABSENT__` (4%) | `OC(C(F)(F)F)C(F)(F` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #166  yield=49.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #6)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1C(=O)Nc1ccncc1>>CCOC(=O)C(CC1(c2ccccc2)O/C(=N\c2ccncc2)c2ccccc21)(C(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (75.7%) | `carbon_felt` (10.3%) | `carbon_generic` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.6%) | `carbon` (0.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (97.7%) | `platinum_generic` (2.0%) | `platinum_foil` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (62.7%) | `NBu4` (35.1%) | `Li` (1.9%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (67.9%) | `BF4` (28.9%) | `PF6` (2.4%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (4.7%) | `carboxylic_acid` (3.6%) | `electrophilic_N_F` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (73.3%) | `pyridine_organocat` (25.9%) | `triarylamine_radical_cat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.7%) | `polar_aprotic_amide` (0.5%) | `polar_protic_alcohol` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (3%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (99%) | `CC(=O)O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #167  yield=47.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #7)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1NC(=O)c1ccc(C(=O)OC)cc1>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccc(C(=O)OC)cc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (86.0%) | `platinum` (13.9%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (46.6%) | `graphite_generic` (19.2%) | `platinum_plate` (18.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.6%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (95.6%) | `platinum_generic` (4.3%) | `graphite_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (92.5%) | `NEt4` (4.3%) | `Li` (2.6%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (38.4%) | `PF6` (34.4%) | `ClO4` (25.3%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (7.7%) | `carboxylic_acid` (4.9%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.6%) | `triarylamine_radical_cat` (1.2%) | `organic_neutral_cat` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (91.8%) | `ABSENT` (3.2%) | `polar_aprotic_amide` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (60%) | `FC(F)(F)c1ccccc1` (28%) | `CO` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (100%) | `O=O` (0%) | `OB(O)B(O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (86%) | `__OTHER__` (10%) | `[Br][Mn][Br]` (1%) | set ✓ / any ✓ |

---

### Reaction #168  yield=46.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #8)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1C(=O)Nc1cccc2ncccc12>>CCOC(=O)C(CC1(c2ccccc2)O/C(=N\c2cccc3ncccc23)c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (80.0%) | `carbon_felt` (9.8%) | `graphite_felt` (4.0%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.7%) | `nickel` (0.2%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (94.8%) | `platinum_generic` (5.1%) | `platinum_foil` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (63.0%) | `ABSENT` (18.8%) | `Li` (12.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (55.5%) | `ABSENT` (27.5%) | `molecular_no_ion` (8.7%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `carboxylic_acid` (5.4%) | `ABSENT` (3.9%) | `electrophilic_N_F` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.8%) | `pyridine_organocat` (3.3%) | `Fe_complex` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (62.3%) | `polar_protic_alcohol` (26.1%) | `ABSENT` (5.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (51%) | `CO` (24%) | `O` (7%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `CC(=O)O` (30%) | `__ABSENT__` (3%) | `[Cl-].[Cl-].[Mg+2]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #169  yield=49.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #9)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1NC(=O)c1ccc(OC)cc1OC>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccc(OC)cc2OC)=Nc2c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.4%) | `platinum` (1.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (91.7%) | `carbon_felt` (5.4%) | `graphite_rod` (1.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (99.0%) | `platinum_generic` (1.0%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (86.1%) | `Li` (13.5%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (86.8%) | `ClO4` (11.4%) | `PF6` (1.4%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (6.7%) | `carboxylic_acid` (5.3%) | `electrophilic_N_F` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `triarylamine_radical_cat` (0.2%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.4%) | `polar_aprotic_amide` (0.7%) | `polar_protic_alcohol` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `FC(F)(F)c1ccccc1` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #170  yield=52.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #10)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1C(=O)Nc1ccc(C)cc1>>CCOC(=O)C(CC1(c2ccccc2)O/C(=N\c2ccc(C)cc2)c2ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (71.3%) | `carbon_generic` (12.1%) | `carbon_rod` (9.2%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (98.8%) | `carbon` (1.0%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (95.7%) | `platinum_generic` (3.5%) | `platinum_foil` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (60.0%) | `NBu4` (34.7%) | `Li` (4.9%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (68.7%) | `BF4` (24.6%) | `PF6` (3.7%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (5.8%) | `carboxylic_acid` (3.1%) | `electrophilic_N_F` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.5%) | `pyridine_organocat` (4.2%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.8%) | `ABSENT` (2.2%) | `polar_protic_alcohol` (1.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (97%) | `CO` (1%) | `CN(C)C=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Cl-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #171  yield=56.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #11)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1NC(=O)c1ccc(C#N)cc1>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccc(C#N)cc2)=Nc2ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (73.9%) | `platinum` (26.0%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (80.7%) | `platinum_plate` (14.2%) | `graphite_cloth` (2.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.8%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (94.2%) | `platinum_generic` (5.7%) | `carbon_rod` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (80.9%) | `Li` (8.0%) | `NEt4` (7.7%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (48.6%) | `ClO4` (34.0%) | `PF6` (7.3%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (7.2%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (75.0%) | `organic_neutral_cat` (14.5%) | `pyridine_organocat` (4.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.2%) | `ABSENT` (1.7%) | `polar_aprotic_amide` (1.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (97%) | `OC(C(F)(F)F)C(F)(F` (1%) | `CN(C)C=O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `BrCCBr` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #172  yield=52.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #12)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(CC)c1ccccc1NC(=O)c1ccc(OC)cc1>>CCOC(=O)C(CC1(CC)OC(c2ccc(OC)cc2)=Nc2ccccc21)(C(=O)OCC…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (84.6%) | `carbon` (15.3%) | `sacrificial_magnesium` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (50.0%) | `platinum_plate` (38.4%) | `platinum_generic` (5.0%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.9%) | `stainless_steel` (0.0%) | `carbon` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (99.5%) | `platinum_generic` (0.5%) | `carbon_rod` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (83.4%) | `Na` (8.0%) | `ABSENT` (5.7%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `Br` (36.4%) | `BF4` (34.0%) | `carboxylate` (10.9%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `bromide_anion` (24.1%) | `ABSENT` (4.8%) | `boron_lewis_acid` (4.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (68.5%) | `ABSENT` (28.0%) | `pyridine_organocat` (2.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (63.2%) | `polar_protic_alcohol` (9.9%) | `polar_aprotic_amide` (7.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (73%) | `CO` (19%) | `O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (19%) | `O=C(O)C(F)(F)F` (9%) | `OC(C(F)(F)F)C(F)(F` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (63%) | `N#Cc1c(C#N)c(-n2c3` (6%) | `[Fe+2].c1cc[cH-]c1` (4%) | set ✗ / any ✗ |

---

### Reaction #173  yield=54.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #13)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1C(=O)NCCCC>>CCCC/N=C1\OC(CC(C(=O)OCC)(C(=O)OCC)C(=O)OCC)(c2ccccc2)c2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (1.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (71.0%) | `carbon_felt` (21.6%) | `carbon_generic` (4.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.2%) | `carbon` (0.7%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (88.3%) | `platinum_generic` (9.3%) | `platinum_foil` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (77.8%) | `ABSENT` (13.2%) | `Li` (8.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (52.9%) | `ABSENT` (20.1%) | `PF6` (12.9%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `carboxylic_acid` (9.9%) | `azide_source` (3.5%) | `ABSENT` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.4%) | `pyridine_organocat` (0.9%) | `Fe_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (65.1%) | `polar_protic_alcohol` (26.5%) | `polar_aprotic_amide` (4.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (64%) | `O` (53%) | `CO` (31%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `CC(=O)O` (87%) | `OC(C(F)(F)F)C(F)(F` (1%) | `O=O` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `__OTHER__` (1%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #174  yield=64.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #14)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1NC(=O)C1CC1>>CCOC(=O)C(CC1(c2ccccc2)OC(C2CC2)=Nc2ccccc21)(C(=O)OCC)C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (91.3%) | `platinum` (8.7%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (69.4%) | `platinum_plate` (12.5%) | `graphite_generic` (10.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.6%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (98.7%) | `platinum_generic` (1.2%) | `graphite_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (94.6%) | `NEt4` (4.2%) | `ABSENT` (0.9%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `PF6` (46.7%) | `BF4` (46.4%) | `ClO4` (4.7%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (13.0%) | `electrophilic_N_F` (2.5%) | `unparseable_text` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.4%) | `organic_neutral_cat` (2.9%) | `Cu_complex` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (89.7%) | `ABSENT` (2.7%) | `halogenated_aliphatic` (2.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `OC(C(F)(F)F)C(F)(F` (0%) | `CN(C)C=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC[N+](CC)(CC)CC.F` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #175  yield=61.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #15)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1NC(=O)c1ccc(C)cc1>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccc(C)cc2)=Nc2ccccc21…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (73.7%) | `platinum` (26.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (93.5%) | `platinum_plate` (4.3%) | `graphite_rod` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (97.4%) | `platinum_generic` (2.6%) | `carbon_rod` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (95.2%) | `Li` (2.1%) | `NEt4` (1.7%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (67.7%) | `ClO4` (18.0%) | `PF6` (12.2%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (5.3%) | `metal_oxide_oxidant` (2.5%) | `tellurium_reagent` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.6%) | `organic_neutral_cat` (4.4%) | `Cu_complex` (1.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.5%) | `polar_aprotic_amide` (3.0%) | `ABSENT` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (93%) | `CO` (3%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CC[N+](CC)(CC)CC.F` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #176  yield=66.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #16)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1C(=O)Nc1ccc(Br)cc1>>CCOC(=O)C(CC1(c2ccccc2)O/C(=N\c2ccc(Br)cc2)c2ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.7%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (92.2%) | `carbon_generic` (4.1%) | `carbon_felt` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.6%) | `carbon` (0.4%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (93.3%) | `platinum_generic` (6.2%) | `platinum_wire` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (57.9%) | `ABSENT` (37.0%) | `Li` (4.7%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (48.8%) | `BF4` (44.0%) | `ClO4` (3.9%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (4.2%) | `carboxylic_acid` (3.5%) | `electrophilic_N_F` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (79.8%) | `pyridine_organocat` (18.8%) | `triarylamine_radical_cat` (1.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (75.9%) | `polar_aprotic_nitrile` (23.6%) | `polar_aprotic_amide` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `__ABSENT__` (86%) | `CC#N` (2%) | `CN(C)C=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #177  yield=67.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #17)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1NC(=O)c1ccc(Cl)cc1>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccc(Cl)cc2)=Nc2ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (76.1%) | `platinum` (23.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (89.2%) | `platinum_plate` (9.1%) | `carbon_felt` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (99.4%) | `platinum_generic` (0.5%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (66.9%) | `ABSENT` (27.5%) | `Li` (3.9%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (46.7%) | `ABSENT` (34.7%) | `ClO4` (10.9%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (6.3%) | `boron_lewis_acid` (3.3%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (81.1%) | `organic_neutral_cat` (7.1%) | `pyridine_organocat` (5.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.8%) | `polar_aprotic_amide` (0.7%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (4%) | `CN(C)C=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (1%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #178  yield=67.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #18)

```
COC(=O)C(C(=O)OC)C(=O)OC.C=C(c1ccccc1)c1ccccc1NC(=O)c1ccc(OC)cc1>>COC(=O)C(CC1(c2ccccc2)OC(c2ccc(OC)cc2)=Nc2ccccc21)(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (86.9%) | `platinum` (13.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (92.6%) | `platinum_plate` (4.9%) | `graphite_rod` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (96.2%) | `platinum_generic` (3.8%) | `platinum_foil` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (94.9%) | `Li` (2.8%) | `ABSENT` (1.1%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (79.0%) | `ClO4` (10.2%) | `PF6` (6.4%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (11.9%) | `electrophilic_N_F` (2.4%) | `unparseable_text` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (70.2%) | `organic_neutral_cat` (22.2%) | `pyridine_organocat` (1.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (87.3%) | `halogenated_aliphatic` (6.0%) | `polar_aprotic_amide` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `O` (14%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Fe+2].c1cc[cH-]c1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #179  yield=69.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #19)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccc(C)cc1)c1ccccc1NC(=O)c1ccc(OC)cc1>>CCOC(=O)C(CC1(c2ccc(C)cc2)OC(c2ccc(OC)cc2)=Nc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (69.0%) | `platinum` (31.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (93.2%) | `platinum_plate` (5.9%) | `carbon_felt` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (99.8%) | `platinum_generic` (0.2%) | `carbon_rod` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (94.4%) | `ABSENT` (4.1%) | `Li` (1.2%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (83.4%) | `ABSENT` (7.0%) | `ClO4` (5.6%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (6.6%) | `boron_lewis_acid` (3.3%) | `electrophilic_N_F` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (88.2%) | `organic_neutral_cat` (8.9%) | `pyridine_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.4%) | `ABSENT` (0.9%) | `polar_aprotic_amide` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #180  yield=66.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #20)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccc(C(C)(C)C)cc1)c1ccccc1NC(=O)c1ccc(OC)cc1>>CCOC(=O)C(CC1(c2ccc(C(C)(C)C)cc2)OC(c2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (64.2%) | `carbon` (35.8%) | `sacrificial_magnesium` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (60.7%) | `platinum_plate` (37.6%) | `platinum_generic` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (98.4%) | `platinum_generic` (1.6%) | `carbon_rod` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (87.9%) | `ABSENT` (6.0%) | `Li` (4.6%) | ✓ |
| 电解质 anion | 26 | `molecular_no_ion` | `BF4` (60.1%) | `ABSENT` (13.8%) | `PF6` (11.1%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (8.8%) | `carboxylic_acid` (3.5%) | `electrophilic_N_F` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (73.7%) | `organic_neutral_cat` (22.4%) | `pyridine_organocat` (2.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.6%) | `ABSENT` (0.2%) | `polar_aprotic_amide` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (1%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br][Mn][Br]` (0%) | set ✓ / any ✓ |

---

### Reaction #181  yield=65.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #21)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1NC(C)=O>>CCOC(=O)C(CC1(c2ccccc2)OC(C)=Nc2ccccc21)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (81.1%) | `platinum` (18.7%) | `sacrificial_magnesium` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_rod` (21.3%) | `platinum_plate` (16.5%) | `reticulated_vitreous_carbon` (15.8%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (100.0%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_generic` (57.8%) | `platinum_plate` (42.1%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (71.3%) | `NEt4` (11.6%) | `Li` (11.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (49.8%) | `BF4` (33.8%) | `PF6` (7.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_other_salt` | `carboxylic_acid` (9.2%) | `o2_oxidant` (5.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.5%) | `triarylamine_radical_cat` (0.7%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (45.1%) | `ABSENT` (45.0%) | `polar_protic_acid` (5.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (96%) | `CN(C)C=O` (1%) | `CO` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `O=C(O)C(F)(F)F` (33%) | `__ABSENT__` (25%) | `CC(=O)O` (21%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Br][Mn][Br]` (0%) | set ✓ / any ✓ |

---

### Reaction #182  yield=71.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #22)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(C)c1ccccc1NC(=O)c1ccccc1>>CCOC(=O)C(CC1(C)OC(c2ccccc2)=Nc2ccccc21)(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (86.2%) | `platinum` (11.0%) | `ABSENT` (1.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (49.4%) | `graphite_rod` (33.6%) | `ABSENT` (11.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (88.8%) | `nickel` (7.1%) | `ABSENT` (1.7%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (91.5%) | `platinum_generic` (5.4%) | `ABSENT` (2.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (77.5%) | `ABSENT` (18.9%) | `NEt4` (1.6%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `PF6` (59.2%) | `BF4` (24.7%) | `ABSENT` (13.4%) | ✗ |
| 试剂大类 | 103 | `alkali_other_salt` | `alkali_sulfinate` (19.1%) | `ABSENT` (3.4%) | `alkali_sulfonate` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (81.2%) | `organic_neutral_cat` (10.1%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (32.0%) | `polar_protic_alcohol` (26.7%) | `polar_aprotic_amide` (16.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CO` (99%) | `O=C(O)C(F)(F)F` (47%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `O=S(=O)(O)O` (96%) | `N#C[S-].[NH4+]` (96%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `CC(C)c1cc(C(C)C)c(` (75%) | `__ABSENT__` (23%) | `CC[N+](CC)(CC)CC.F` (1%) | set ✗ / any ✓ |

---

### Reaction #183  yield=77.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #23)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1NC(=O)c1ccccc1>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccccc2)=Nc2ccccc21)(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (19.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (75.7%) | `graphite_rod` (19.3%) | `graphite_generic` (2.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.4%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (59.8%) | `platinum_generic` (40.0%) | `ABSENT` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (86.3%) | `NEt4` (11.7%) | `Li` (1.3%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `PF6` (57.5%) | `BF4` (30.5%) | `ClO4` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (4.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.1%) | `organic_neutral_cat` (15.8%) | `Cu_complex` (4.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.2%) | `polar_aprotic_amide` (15.1%) | `polar_protic_alcohol` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (43%) | `CO` (39%) | `CN(C)C=O` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` + `O=C([O-])O.[Na+]` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (1%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (84%) | `CC[N+](CC)(CC)CC.F` (12%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #184  yield=73.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #24)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1NC(=O)c1ccc(OC)cc1>>CCOC(=O)C(CC1(c2ccccc2)OC(c2ccc(OC)cc2)=Nc2ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (87.1%) | `platinum` (12.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (95.7%) | `platinum_plate` (2.7%) | `graphite_rod` (0.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (98.8%) | `platinum_generic` (1.2%) | `carbon_rod` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (93.3%) | `Li` (3.2%) | `ABSENT` (1.7%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (71.7%) | `ClO4` (14.1%) | `PF6` (10.2%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (9.8%) | `boron_lewis_acid` (2.5%) | `electrophilic_N_F` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.8%) | `organic_neutral_cat` (18.6%) | `pyridine_organocat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.7%) | `polar_aprotic_amide` (1.3%) | `halogenated_aliphatic` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `O` (3%) | `CN(C)C=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CC[N+](CC)(CC)CC.F` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #185  yield=79.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_10_e202500174.json) (反应 idx 在该 JSON 内 = #25)

```
CCOC(=O)C(C(=O)OCC)C(=O)OCC.C=C(c1ccc(OC)cc1)c1ccccc1NC(=O)c1ccc(OC)cc1>>CCOC(=O)C(CC1(c2ccc(OC)cc2)OC(c2ccc(OC)cc2)=…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (74.5%) | `platinum` (25.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (93.3%) | `platinum_plate` (5.6%) | `graphite_rod` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (99.5%) | `platinum_generic` (0.4%) | `carbon_rod` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (95.7%) | `ABSENT` (2.0%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `BF4` (80.6%) | `ClO4` (6.9%) | `PF6` (6.7%) | ✓ |
| 试剂大类 | 103 | `alkali_other_salt` | `ABSENT` (8.1%) | `boron_lewis_acid` (2.8%) | `electrophilic_N_F` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.9%) | `organic_neutral_cat` (18.7%) | `pyridine_organocat` (1.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `polar_aprotic_amide` (1.0%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (1%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(C)(C)O.[K]` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #186  yield=28.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #0)

```
N#CS.[K].C=C(C(=O)OCCC(C)CCC=C(C)C)c1ccccc1>>CC(C)=CCCC(C)CCOC(=O)C(O)(CSC(N)=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (1.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (53.6%) | `graphite_felt` (34.8%) | `graphite_plate` (3.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.1%) | `carbon` (1.1%) | `nickel` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (65.6%) | `platinum_generic` (34.2%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.4%) | `K` (10.8%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (68.9%) | `carboxylate` (11.3%) | `molecular_no_ion` (5.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (19.9%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `pyridine_organocat` (0.1%) | `ionic_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (75.4%) | `ABSENT` (14.0%) | `halogenated_aliphatic` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (97%) | `OC(C(F)(F)F)C(F)(F` (56%) | `CC#N` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (99%) | `c1ccc(N(c2ccccc2)c` (0%) | `[Cl-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].CC(=O)[` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #187  yield=33.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #1)

```
N#C[S-].[K+].C=C(C(=O)OCc1ccsc1)c1ccccc1>>NC(=O)SCC(O)(C(=O)OCc1ccsc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.5%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (99.6%) | `reticulated_vitreous_carbon` (0.2%) | `carbon_generic` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.2%) | `carbon` (6.4%) | `nickel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (82.7%) | `platinum_plate` (16.8%) | `graphite_plate` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (97.2%) | `Li` (1.4%) | `ABSENT` (1.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (86.8%) | `ClO4` (5.8%) | `BF4` (4.5%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (18.0%) | `unparseable_text` (2.1%) | `electrophilic_N_F` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Fe_complex` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (86.6%) | `nitroalkane` (5.1%) | `halogenated_aliphatic` (2.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` | `CC(C)=O` (100%) | `OC(C(F)(F)F)C(F)(F` (97%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (80%) | `c1ccc(N(c2ccccc2)c` (16%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #188  yield=50.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #2)

```
N#CS.[K].C=C(C(=O)OC)c1c(Cl)cccc1Cl>>COC(=O)C(O)(CSC(N)=O)c1c(Cl)cccc1Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (88.6%) | `graphite_generic` (5.3%) | `unknown_electrode` (1.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.7%) | `nickel` (1.5%) | `carbon` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (93.3%) | `platinum_plate` (6.6%) | `nickel_plate` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.6%) | `K` (7.6%) | `Na` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (44.9%) | `BF4` (33.8%) | `Br` (7.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (37.6%) | `electrophilic_N_F` (1.8%) | `unparseable_text` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `Fe_complex` (0.2%) | `Ni_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (79.4%) | `polar_aprotic_nitrile` (8.8%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (76%) | `CC(C)=O` (68%) | `CC#N` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (98%) | `c1ccc(N(c2ccccc2)c` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #189  yield=42.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #3)

```
N#CS.[K].C=C(C(=O)OC)c1ccc(C(C)(C)C)cc1>>COC(=O)C(O)(CSC(N)=O)c1ccc(C(C)(C)C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (77.2%) | `platinum` (21.4%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (94.3%) | `platinum_plate` (1.8%) | `graphite_generic` (1.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.0%) | `carbon` (10.6%) | `nickel` (2.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (87.6%) | `platinum_plate` (10.9%) | `graphite_generic` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (48.5%) | `NBu4` (35.7%) | `NEt4` (7.5%) | ✓ |
| 电解质 anion | 26 | `PF6` | `PF6` (57.6%) | `carboxylate` (13.9%) | `molecular_no_ion` (8.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (24.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Ni_complex` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (57.4%) | `ABSENT` (20.7%) | `polar_aprotic_nitrile` (11.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (84%) | `OC(C(F)(F)F)C(F)(F` (73%) | `CC#N` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (99%) | `c1ccc(N(c2ccccc2)c` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #190  yield=43.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #4)

```
N#CS.[K].C=C(C(=O)OC(C)(C)C)c1ccccc1>>CC(C)(C)OC(=O)C(O)(CSC(N)=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (67.0%) | `carbon_cloth` (22.4%) | `graphite_felt` (2.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (79.7%) | `nickel` (18.4%) | `carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (90.3%) | `platinum_generic` (8.4%) | `nickel_foam` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (79.0%) | `K` (12.6%) | `NEt4` (4.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (69.5%) | `BF4` (15.1%) | `Br` (4.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (32.4%) | `metal_oxide_oxidant` (1.8%) | `tellurium_reagent` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `organic_neutral_cat` (0.1%) | `ionic_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (88.4%) | `ABSENT` (4.0%) | `nitroalkane` (1.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (99%) | `OC(C(F)(F)F)C(F)(F` (39%) | `FC(F)(F)c1ccccc1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (98%) | `c1ccc(N(c2ccccc2)c` (0%) | `O=C([O-])[O-].[Cs+` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CC[C@H](C)[C@H]1CN` (0%) | set ✓ / any ✓ |

---

### Reaction #191  yield=49.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #5)

```
N#CS.[K].C=C(C(=O)OCC)c1ccc(Br)cc1>>CCOC(=O)C(O)(CSC(N)=O)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.4%) | `platinum` (4.3%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `graphite_generic` (29.5%) | `carbon_rod` (29.0%) | `graphite_plate` (9.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.3%) | `carbon` (3.8%) | `nickel` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (76.4%) | `platinum_generic` (22.1%) | `graphite_rod` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.4%) | `K` (2.9%) | `NEt4` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (47.3%) | `BF4` (26.8%) | `I` (12.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (25.4%) | `primary_amine` (2.1%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.5%) | `ammonium_PTC_organocat` (1.2%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ABSENT` (62.0%) | `halogenated_aliphatic` (27.4%) | `ketone` (3.5%) | ✓ |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (98%) | `OC(C(F)(F)F)C(F)(F` (1%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #192  yield=59.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #6)

```
N#CS.[K].C=C(C(=O)OC)c1cccc(OC)c1>>COC(=O)C(O)(CSC(N)=O)c1cccc(OC)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.0%) | `platinum` (1.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (91.1%) | `graphite_generic` (7.7%) | `graphite_felt` (0.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (79.9%) | `carbon` (16.9%) | `nickel` (3.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (91.2%) | `platinum_plate` (6.4%) | `graphite_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (41.9%) | `ABSENT` (21.3%) | `K` (12.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `molecular_no_ion` (54.7%) | `PF6` (15.1%) | `Br` (12.7%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (37.3%) | `electrophilic_N_F` (1.7%) | `unparseable_text` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Fe_complex` (0.0%) | `Ni_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (64.2%) | `ABSENT` (15.5%) | `polar_aprotic_nitrile` (12.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (63%) | `CC(C)=O` (59%) | `CC#N` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (99%) | `c1ccc(N(c2ccccc2)c` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #193  yield=58.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #7)

```
N#CS.[K].C=C(C(=O)O[C@H]1CC[C@@]2(C)[C@@H](CC[C@]3(C)[C@@H]2CC[C@]2(C)C(=O)CC[C@@H]32)C1)c1ccccc1>>C[C@]12CC[C@H](OC(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.5%) | `platinum` (4.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (83.5%) | `carbon_cloth` (9.2%) | `reticulated_vitreous_carbon` (2.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.0%) | `carbon` (5.6%) | `nickel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (60.6%) | `platinum_generic` (38.5%) | `nickel_foam` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (87.6%) | `K` (8.2%) | `ABSENT` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (69.7%) | `BF4` (16.7%) | `carboxylate` (4.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (26.6%) | `electrophilic_N_F` (2.0%) | `unparseable_text` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (79.1%) | `ABSENT` (13.3%) | `polar_aprotic_nitrile` (2.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (90%) | `OC(C(F)(F)F)C(F)(F` (6%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (99%) | `c1ccc(N(c2ccccc2)c` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #194  yield=57.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #8)

```
N#CS.[K].C=C(C(=O)OC)c1ccc(Cl)c(Cl)c1>>COC(=O)C(O)(CSC(N)=O)c1ccc(Cl)c(Cl)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.4%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (96.9%) | `graphite_generic` (1.6%) | `graphite_rod` (0.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (62.9%) | `nickel` (19.2%) | `carbon` (17.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (47.6%) | `platinum_generic` (39.8%) | `nickel_plate` (8.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (70.5%) | `K` (22.3%) | `ABSENT` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (59.8%) | `BF4` (21.5%) | `I` (4.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (29.4%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `Ni_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (65.2%) | `polar_aprotic_nitrile` (11.2%) | `ABSENT` (8.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (92%) | `CC(C)=O` (73%) | `CC#N` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (98%) | `c1ccc(N(c2ccccc2)c` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #195  yield=60.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #9)

```
N#CS.[K].C=C(C(=O)OCC1CC1)c1ccccc1>>NC(=O)SCC(O)(C(=O)OCC1CC1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (47.8%) | `graphite_generic` (34.8%) | `graphite_felt` (9.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (81.6%) | `carbon` (13.3%) | `stainless_steel` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (76.7%) | `platinum_generic` (20.5%) | `graphite_generic` (0.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.9%) | `ABSENT` (18.4%) | `protonated_amine` (14.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (38.1%) | `molecular_no_ion` (21.3%) | `ABSENT` (12.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (20.7%) | `hf_amine_complex` (2.1%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `halogenated_aliphatic` (44.0%) | `ketone` (30.1%) | `ABSENT` (16.2%) | ✓ |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (85%) | `CC(C)=O` (6%) | `ClCCl` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #196  yield=55.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #10)

```
N#CS.[K].C=C(C(=O)OC)c1ccc(C)cc1>>COC(=O)C(O)(CSC(N)=O)c1ccc(C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (86.0%) | `platinum` (13.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (98.2%) | `graphite_felt` (0.8%) | `platinum_plate` (0.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.6%) | `nickel` (1.2%) | `carbon` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (77.1%) | `platinum_plate` (22.7%) | `nickel_plate` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (71.3%) | `K` (12.7%) | `ABSENT` (10.8%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (58.3%) | `BF4` (18.6%) | `ABSENT` (10.0%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (21.8%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.3%) | `Ni_complex` (0.6%) | `main_group_lewis_acid` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (61.5%) | `polar_aprotic_sulfoxide` (13.5%) | `polar_aprotic_nitrile` (7.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (98%) | `CC(C)=O` (83%) | `CC#N` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (90%) | `c1ccc(N(c2ccccc2)c` (1%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #197  yield=52.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #11)

```
N#CS.[K].C=C(C(=O)OC)c1cccc(C)c1>>COC(=O)C(O)(CSC(N)=O)c1cccc(C)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (98.5%) | `graphite_generic` (0.7%) | `platinum_plate` (0.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.0%) | `carbon` (4.5%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (62.6%) | `platinum_generic` (36.9%) | `graphite_rod` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (97.1%) | `ABSENT` (0.9%) | `K` (0.8%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (54.9%) | `BF4` (18.2%) | `carboxylate` (10.8%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (34.7%) | `electrophilic_N_F` (1.8%) | `unparseable_text` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `Ni_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (55.4%) | `polar_aprotic_nitrile` (27.0%) | `ABSENT` (10.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (63%) | `CC(C)=O` (35%) | `CC#N` (23%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (99%) | `c1ccc(N(c2ccccc2)c` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #198  yield=53.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #12)

```
N#CS.[K].C=C(C(=O)OCc1ccccc1)c1ccccc1.O>>NC(=O)SCC(O)(C(=O)OCc1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (77.2%) | `graphite_plate` (17.2%) | `graphite_generic` (2.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.8%) | `carbon` (3.3%) | `nickel` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (82.4%) | `platinum_generic` (16.9%) | `graphite_plate` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.4%) | `K` (8.1%) | `NEt4` (3.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (56.4%) | `ClO4` (11.5%) | `molecular_no_ion` (10.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.4%) | `as_solvent_cyclic_ether` (2.0%) | `metal_oxide_oxidant` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `ammonium_PTC_organocat` (0.1%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (31.2%) | `halogenated_aliphatic` (25.6%) | `ABSENT` (22.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (94%) | `CC(C)=O` (66%) | `FC(F)(F)c1ccccc1` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccc(N(c2ccccc2)c` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #199  yield=51.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #13)

```
N#CS.[K].C=C(C(=O)OCC)c1ccc(F)cc1.O>>CCOC(=O)C(O)(CSC(N)=O)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.5%) | `platinum` (1.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (46.1%) | `graphite_cloth` (20.8%) | `graphite_generic` (9.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.3%) | `nickel` (9.9%) | `carbon` (6.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (89.1%) | `platinum_generic` (6.1%) | `nickel_plate` (2.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (64.1%) | `K` (27.2%) | `NEt4` (5.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (44.6%) | `carboxylate` (19.7%) | `BF4` (16.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (29.3%) | `boron_lewis_acid` (2.2%) | `diboron` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `ammonium_PTC_organocat` (0.1%) | `ionic_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `halogenated_aliphatic` (47.1%) | `ABSENT` (39.2%) | `ketone` (3.3%) | ✓ |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (4%) | `__ABSENT__` (2%) | `ClCCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #200  yield=55.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #14)

```
N#CS.[K].C=C(C(=O)OCc1ccc(C)cc1)c1ccccc1>>Cc1ccc(COC(=O)C(O)(CSC(N)=O)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (1.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (92.9%) | `graphite_felt` (1.9%) | `reticulated_vitreous_carbon` (1.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.5%) | `nickel` (1.6%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (87.7%) | `platinum_generic` (11.9%) | `nickel_plate` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (74.3%) | `ABSENT` (9.3%) | `K` (8.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (46.3%) | `BF4` (16.3%) | `carboxylate` (13.2%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (32.4%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `ammonium_PTC_organocat` (0.2%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (57.7%) | `ABSENT` (20.1%) | `halogenated_aliphatic` (6.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (65%) | `CC(C)=O` (54%) | `CC#N` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `c1ccc(N(c2ccccc2)c` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #201  yield=56.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #15)

```
N#CS.[K].C=C(c1ccc(-c2ccccc2)cc1)C(F)(F)F>>NC(=O)SCC(O)(c1ccc(-c2ccccc2)cc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (49.1%) | `graphite_generic` (47.1%) | `reticulated_vitreous_carbon` (1.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.3%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (50.7%) | `platinum_generic` (49.2%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `K` (76.0%) | `NBu4` (17.0%) | `Li` (4.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `carboxylate` (48.9%) | `I` (20.2%) | `molecular_no_ion` (19.2%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (30.9%) | `borohydride` (1.9%) | `metal_oxide_oxidant` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Fe_complex` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `polar_aprotic_nitrile` (94.1%) | `ketone` (1.8%) | `polar_protic_alcohol` (1.4%) | ✓ |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (97%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #202  yield=65.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #16)

```
N#CS.[K].C=C(c1ccccc1)C(F)(F)F>>NC(=O)SCC(O)(c1ccccc1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (88.9%) | `graphite_generic` (8.5%) | `graphite_plate` (1.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.5%) | `carbon` (2.2%) | `stainless_steel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (95.5%) | `platinum_generic` (4.1%) | `graphite_generic` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (75.3%) | `K` (12.5%) | `Li` (4.8%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `carboxylate` (36.8%) | `BF4` (21.8%) | `PF6` (14.1%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (30.0%) | `electrophilic_N_F` (2.0%) | `unparseable_text` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `polar_aprotic_nitrile` (87.9%) | `polar_protic_alcohol` (3.4%) | `halogenated_aliphatic` (2.2%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (95%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (99%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #203  yield=63.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #17)

```
N#CS.[K].C=C(C(=O)OC)c1ccc(Br)cc1>>COC(=O)C(O)(CSC(N)=O)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.7%) | `platinum` (10.7%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (95.4%) | `platinum_plate` (1.2%) | `graphite_generic` (0.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.9%) | `carbon` (2.5%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (54.5%) | `platinum_plate` (45.2%) | `graphite_rod` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (75.9%) | `K` (20.6%) | `NEt4` (1.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (74.1%) | `BF4` (9.0%) | `Br` (7.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (27.6%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `Fe_complex` (0.1%) | `Ni_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (65.9%) | `ABSENT` (10.7%) | `polar_aprotic_nitrile` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (72%) | `OC(C(F)(F)F)C(F)(F` (66%) | `CC#N` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (98%) | `c1ccc(N(c2ccccc2)c` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #204  yield=63.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #18)

```
N#CS.[K].C=C(C(=O)OC)c1ccc(-c2ccccc2)cc1>>COC(=O)C(O)(CSC(N)=O)c1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.2%) | `platinum` (6.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (96.5%) | `graphite_felt` (1.7%) | `graphite_generic` (0.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.9%) | `carbon` (2.4%) | `nickel` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (97.5%) | `platinum_plate` (2.4%) | `nickel_foam` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (64.9%) | `K` (27.4%) | `Li` (3.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (70.3%) | `carboxylate` (5.7%) | `Br` (5.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (30.8%) | `metal_oxide_oxidant` (1.7%) | `tellurium_reagent` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `Fe_complex` (0.1%) | `Ni_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (96.6%) | `polar_aprotic_nitrile` (1.2%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (100%) | `OC(C(F)(F)F)C(F)(F` (97%) | `CC#N` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (93%) | `c1ccc(N(c2ccccc2)c` (5%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COCCOC.[Br][Ni][Br` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #205  yield=62.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #19)

```
N#CS.[K].C=C(C(=O)OC)c1cccc2ccccc12>>COC(=O)C(O)(CSC(N)=O)c1cccc2ccccc12
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `platinum` (2.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (77.5%) | `reticulated_vitreous_carbon` (7.5%) | `graphite_generic` (6.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.8%) | `carbon` (1.6%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.5%) | `platinum_plate` (1.5%) | `platinum_wire` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.2%) | `Li` (4.2%) | `NEt4` (2.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (82.4%) | `ClO4` (8.3%) | `BF4` (4.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (24.9%) | `ammonium_salt` (2.4%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Fe_complex` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (66.8%) | `polar_aprotic_nitrile` (12.7%) | `ABSENT` (12.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (67%) | `CC(C)=O` (57%) | `CC#N` (11%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (99%) | `c1ccc(N(c2ccccc2)c` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #206  yield=63.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #20)

```
N#CS.[K].C=C(C(=O)OC)c1cccc(C(F)(F)F)c1>>COC(=O)C(O)(CSC(N)=O)c1cccc(C(F)(F)F)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.9%) | `platinum` (3.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (96.7%) | `graphite_generic` (2.6%) | `graphite_felt` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `carbon` (9.8%) | `nickel` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (93.2%) | `platinum_plate` (6.4%) | `graphite_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.6%) | `ABSENT` (1.3%) | `NEt4` (1.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (76.5%) | `BF4` (4.9%) | `carboxylate` (3.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (31.1%) | `electrophilic_N_F` (1.9%) | `unparseable_text` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Fe_complex` (0.0%) | `Ni_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (40.6%) | `halogenated_aliphatic` (36.5%) | `ABSENT` (13.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (95%) | `CC(C)=O` (78%) | `FC(F)(F)c1ccccc1` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (99%) | `c1ccc(N(c2ccccc2)c` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Cc1cc(O[C@@H](C)C(` (0%) | set ✓ / any ✓ |

---

### Reaction #207  yield=67.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #21)

```
C=C(C(=O)OCC)c1ccccc1>>CCOC(=O)C(O)(CSC(N)=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (82.0%) | `platinum` (17.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (96.5%) | `carbon_generic` (1.9%) | `graphite_generic` (0.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.4%) | `carbon` (12.0%) | `nickel` (2.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `platinum_plate` (0.4%) | `carbon_generic` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `K` | `NBu4` (92.3%) | `Li` (3.3%) | `K` (2.2%) | ✓ |
| 电解质 anion | 26 | `SCN` | `PF6` (72.1%) | `ClO4` (9.7%) | `BF4` (9.4%) | ✗ |
| 试剂大类 | 103 | `ammonium_salt` | `ABSENT` (27.9%) | `alkali_hydroxide` (2.0%) | `electrophilic_N_F` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (47.5%) | `polar_aprotic_nitrile` (10.1%) | `nitroalkane` (9.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (94%) | `CC(C)=O` (55%) | `O` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` + `O` | `__ABSENT__` (75%) | `c1ccc(N(c2ccccc2)c` (8%) | `CC(=O)O` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #208  yield=67.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #22)

```
N#CS.[K].C=C(C(=O)OC)c1ccc(C(=O)OC)cc1>>COC(=O)c1ccc(C(O)(CSC(N)=O)C(=O)OC)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (78.2%) | `platinum` (19.7%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (84.9%) | `graphite_generic` (10.3%) | `carbon_cloth` (1.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.0%) | `carbon` (11.3%) | `nickel` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (91.7%) | `platinum_plate` (7.0%) | `graphite_generic` (0.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (68.2%) | `K` (24.3%) | `NH4` (2.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (80.5%) | `Br` (7.0%) | `I` (5.4%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (23.8%) | `tempo_mediator` (1.9%) | `metal_oxide_oxidant` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `Ni_complex` (0.5%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (79.9%) | `ABSENT` (6.9%) | `polar_aprotic_sulfoxide` (3.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (91%) | `OC(C(F)(F)F)C(F)(F` (87%) | `FC(F)(F)c1ccccc1` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (77%) | `c1ccc(N(c2ccccc2)c` (5%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #209  yield=61.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #23)

```
N#CS.[K].C=C(C(=O)OC)c1ccc(COc2ccccc2)cc1>>COC(=O)C(O)(CSC(N)=O)c1ccc(COc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.0%) | `platinum` (7.9%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (80.2%) | `unknown_electrode` (4.5%) | `graphite_felt` (3.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (72.1%) | `nickel` (22.9%) | `carbon` (4.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (89.0%) | `platinum_plate` (4.1%) | `nickel_foam` (3.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `K` (64.4%) | `NBu4` (28.4%) | `Na` (3.2%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (79.9%) | `carboxylate` (5.4%) | `Br` (4.5%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (37.9%) | `metal_oxide_oxidant` (1.7%) | `tellurium_reagent` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `Ni_complex` (0.1%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (90.5%) | `polar_aprotic_sulfoxide` (4.2%) | `polar_aprotic_nitrile` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (96%) | `OC(C(F)(F)F)C(F)(F` (75%) | `CC#N` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `c1ccc(N(c2ccccc2)c` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC[C@H](C)[C@H]1CN` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #210  yield=68.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #24)

```
N#CS.[K].C=C(C(=O)OCc1ccc(C(=O)OC)cc1)c1ccccc1>>COC(=O)c1ccc(COC(=O)C(O)(CSC(N)=O)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.7%) | `platinum` (3.2%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (53.4%) | `graphite_generic` (33.1%) | `reticulated_vitreous_carbon` (5.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.8%) | `carbon` (4.9%) | `nickel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (59.9%) | `platinum_generic` (36.8%) | `graphite_generic` (1.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (52.2%) | `K` (32.5%) | `NEt4` (4.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (86.3%) | `carboxylate` (3.3%) | `I` (3.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (29.5%) | `as_solvent_cyclic_ether` (1.9%) | `primary_amine` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `ammonium_PTC_organocat` (0.2%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ABSENT` (52.0%) | `ketone` (30.2%) | `nitroalkane` (8.3%) | ✓ |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (98%) | `OC(C(F)(F)F)C(F)(F` (1%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CC(=O)[O-].CC(=O)[` (0%) | set ✓ / any ✓ |

---

### Reaction #211  yield=70.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #25)

```
N#CS.[K].C=C(C(=O)OCc1ccc(Cl)cc1)c1ccccc1>>NC(=O)SCC(O)(C(=O)OCc1ccc(Cl)cc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.3%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (85.9%) | `graphite_plate` (4.4%) | `graphite_felt` (2.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.5%) | `carbon` (2.7%) | `nickel` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (64.8%) | `platinum_generic` (32.9%) | `nickel_plate` (0.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (72.5%) | `K` (13.7%) | `ABSENT` (4.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (30.6%) | `molecular_no_ion` (22.1%) | `BF4` (14.8%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (28.2%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (41.1%) | `ABSENT` (22.9%) | `halogenated_aliphatic` (15.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (58%) | `CC(C)=O` (19%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].CC(=O)[` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #212  yield=70.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #26)

```
N#CS.[K].C=C(C(=O)OC)c1ccccc1Cl>>COC(=O)C(O)(CSC(N)=O)c1ccccc1Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (81.1%) | `graphite_generic` (13.4%) | `graphite_felt` (3.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.3%) | `carbon` (15.4%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (78.4%) | `platinum_generic` (19.4%) | `graphite_generic` (1.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.3%) | `NEt4` (2.2%) | `NH4` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (68.9%) | `BF4` (18.8%) | `OTf` (3.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (35.8%) | `electrophilic_N_F` (1.9%) | `unparseable_text` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Fe_complex` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ABSENT` (63.2%) | `ketone` (27.6%) | `polar_aprotic_nitrile` (5.4%) | ✓ |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `__ABSENT__` (78%) | `OC(C(F)(F)F)C(F)(F` (39%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `c1ccc(N(c2ccccc2)c` (0%) | `O=S([O-])O.[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #213  yield=73.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #27)

```
N#CS.[K].C=C(C(=O)OC)c1ccccc1>>COC(=O)C(O)(CSC(N)=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.4%) | `platinum` (6.3%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (99.2%) | `graphite_felt` (0.4%) | `graphite_generic` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (91.3%) | `carbon` (5.8%) | `nickel` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (97.6%) | `platinum_plate` (2.3%) | `nickel_plate` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.2%) | `K` (13.0%) | `Li` (2.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (79.8%) | `BF4` (5.0%) | `OTf` (3.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (29.7%) | `tempo_mediator` (2.0%) | `electrophilic_N_F` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `Ni_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (94.8%) | `polar_aprotic_sulfoxide` (1.4%) | `polar_aprotic_nitrile` (1.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (100%) | `OC(C(F)(F)F)C(F)(F` (99%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `c1ccc(N(c2ccccc2)c` (66%) | `__ABSENT__` (36%) | `CC1(C)CCCC(C)(C)N1` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `CC(C)(C)c1cccc(C2=` (0%) | set ✓ / any ✓ |

---

### Reaction #214  yield=77.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #28)

```
N#CS.[K].C=C(C(=O)OC(C)C)c1ccccc1>>CC(C)OC(=O)C(O)(CSC(N)=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (68.5%) | `graphite_generic` (16.6%) | `reticulated_vitreous_carbon` (7.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.3%) | `carbon` (2.5%) | `nickel` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (80.0%) | `platinum_plate` (19.2%) | `graphite_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `K` (63.0%) | `NBu4` (17.1%) | `Li` (5.7%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (56.4%) | `molecular_no_ion` (31.0%) | `carboxylate` (7.1%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (25.3%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (90.0%) | `ABSENT` (6.4%) | `polar_aprotic_nitrile` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (95%) | `OC(C(F)(F)F)C(F)(F` (65%) | `FC(F)(F)c1ccccc1` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `c1ccc(N(c2ccccc2)c` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].CC(=O)[` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #215  yield=71.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #29)

```
N#CS.[K].C=C(C(=O)OC)c1ccc(Cl)cc1>>COC(=O)C(O)(CSC(N)=O)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.2%) | `platinum` (9.4%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (96.0%) | `graphite_felt` (1.3%) | `graphite_generic` (0.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.8%) | `carbon` (2.8%) | `nickel` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (76.8%) | `platinum_plate` (22.8%) | `nickel_plate` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (58.1%) | `K` (31.2%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (58.4%) | `BF4` (15.6%) | `Br` (7.2%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (27.1%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `Fe_complex` (0.1%) | `Ni_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (72.9%) | `polar_aprotic_nitrile` (12.0%) | `halogenated_aliphatic` (4.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (87%) | `CC(C)=O` (73%) | `CC#N` (5%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (98%) | `c1ccc(N(c2ccccc2)c` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #216  yield=71.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #30)

```
N#CS.[K].C=C(C(=O)OC)c1ccc(F)cc1>>COC(=O)C(O)(CSC(N)=O)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.6%) | `platinum` (5.2%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (95.3%) | `graphite_felt` (1.0%) | `platinum_plate` (0.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.2%) | `carbon` (7.9%) | `nickel` (2.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (69.4%) | `platinum_generic` (29.2%) | `graphite_rod` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (50.0%) | `K` (35.3%) | `ABSENT` (5.5%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (62.6%) | `Br` (11.3%) | `carboxylate` (8.2%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (28.1%) | `disulfide` (1.9%) | `metal_oxide_oxidant` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Ni_complex` (0.1%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (47.2%) | `ABSENT` (18.8%) | `polar_aprotic_nitrile` (10.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (83%) | `OC(C(F)(F)F)C(F)(F` (49%) | `CC#N` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (94%) | `c1ccc(N(c2ccccc2)c` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #217  yield=76.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #31)

```
N#CS.[K].C=C(C(=O)OC)c1cccc(Cl)c1>>COC(=O)C(O)(CSC(N)=O)c1cccc(Cl)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.5%) | `platinum` (1.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (98.1%) | `graphite_generic` (0.7%) | `graphite_felt` (0.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.5%) | `carbon` (6.5%) | `nickel` (3.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (95.7%) | `platinum_plate` (4.0%) | `nickel_plate` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (95.4%) | `ABSENT` (2.2%) | `K` (0.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (72.8%) | `BF4` (16.4%) | `carboxylate` (3.1%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (32.7%) | `electrophilic_N_F` (2.0%) | `unparseable_text` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `Ni_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (82.5%) | `polar_aprotic_nitrile` (10.2%) | `halogenated_aliphatic` (2.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `CC(C)=O` (91%) | `OC(C(F)(F)F)C(F)(F` (88%) | `CC#N` (5%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (91%) | `c1ccc(N(c2ccccc2)c` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #218  yield=76.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #32)

```
N#CS.[K].C=C(C(=O)OC)c1ccc(Cl)cc1Cl>>COC(=O)C(O)(CSC(N)=O)c1ccc(Cl)cc1Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (91.1%) | `platinum` (8.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (92.6%) | `graphite_felt` (2.5%) | `graphite_generic` (2.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.1%) | `carbon` (4.7%) | `nickel` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (60.9%) | `platinum_generic` (37.5%) | `graphite_generic` (0.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (88.1%) | `K` (4.8%) | `Li` (3.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (47.7%) | `PF6` (18.6%) | `molecular_no_ion` (10.6%) | ✗ |
| 试剂大类 | 103 | `water` | `ABSENT` (31.3%) | `alkali_formate` (2.0%) | `electrophilic_N_F` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Fe_complex` (0.0%) | `main_group_lewis_acid` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (45.4%) | `polar_aprotic_nitrile` (33.3%) | `polar_protic_alcohol` (7.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (84%) | `CC#N` (15%) | `CC(C)=O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `c1ccc(N(c2ccccc2)c` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #219  yield=82.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_14_e9600.json) (反应 idx 在该 JSON 内 = #33)

```
N#CS.[K].C=C(C(=O)OC)c1ccccc1F>>COC(=O)C(O)(CSC(N)=O)c1ccccc1F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.0%) | `platinum` (4.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_rod` | `carbon_rod` (95.6%) | `graphite_generic` (1.2%) | `platinum_plate` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.6%) | `carbon` (1.3%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (55.6%) | `platinum_generic` (44.4%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.8%) | `NEt4` (1.4%) | `K` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `PF6` (67.7%) | `BF4` (21.3%) | `carboxylate` (3.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (28.8%) | `electrophilic_N_F` (2.0%) | `unparseable_text` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `Fe_complex` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `ketone` (60.6%) | `polar_aprotic_nitrile` (20.8%) | `ABSENT` (9.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(C)=O` + `OC(C(F)(F)F)C(F)(F` | `OC(C(F)(F)F)C(F)(F` (64%) | `CC(C)=O` (30%) | `CC#N` (13%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (99%) | `c1ccc(N(c2ccccc2)c` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #220  yield=36.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #0)

```
CO.C=COCC.c1ccc(SSc2ccccn2)nc1>>CCOC(CSc1ccccn1)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (79.3%) | `platinum` (20.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (83.9%) | `carbon_generic` (5.4%) | `platinum_generic` (4.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (70.8%) | `platinum` (22.0%) | `nickel` (3.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (97.1%) | `carbon_generic` (1.4%) | `platinum_generic` (1.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (79.1%) | `NEt4` (7.1%) | `ABSENT` (5.7%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (92.9%) | `PF6` (3.3%) | `ABSENT` (2.0%) | ✓ |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (43.3%) | `pyridine` (7.2%) | `alkali_carbonate` (6.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (75.6%) | `polar_protic_alcohol` (8.1%) | `polar_aprotic_amide` (7.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (5%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (99%) | `O` (2%) | `O=CO` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #221  yield=36.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #1)

```
OC1CCCC1.C=COCC.c1ccc(SSc2ccccc2)cc1>>CCOC(CSc1ccccc1)OC1CCCC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.8%) | `platinum` (3.0%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (99.6%) | `graphite_generic` (0.1%) | `reticulated_vitreous_carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (94.1%) | `platinum` (3.0%) | `nickel` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (100.0%) | `graphite_generic` (0.0%) | `platinum_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.5%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (79.0%) | `Li` (8.2%) | `NMe4` (7.9%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (93.9%) | `ClO4` (3.1%) | `PF6` (1.8%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (60.9%) | `pyridine` (4.1%) | `tertiary_amine` (3.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.2%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (40.6%) | `halogenated_aliphatic` (38.9%) | `ABSENT` (3.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `OC(C(F)(F)F)C(F)(F` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #222  yield=34.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #2)

```
OCc1ccccc1.C=COCC.c1ccc(SSc2ccccc2)cc1>>CCOC(CSc1ccccc1)OCc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.3%) | `platinum` (2.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (99.9%) | `reticulated_vitreous_carbon` (0.0%) | `carbon_felt` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (94.3%) | `platinum` (3.7%) | `nickel` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (100.0%) | `graphite_generic` (0.0%) | `platinum_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.6%) | `NMe4` (12.3%) | `ABSENT` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.9%) | `ClO4` (1.1%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (51.6%) | `pyridine` (3.9%) | `tertiary_amine` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.1%) | `ammonium_PTC_organocat` (2.7%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (53.5%) | `polar_aprotic_nitrile` (40.7%) | `polar_aprotic_amide` (1.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (9%) | `OC(C(F)(F)F)C(F)(F` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `OC(C(F)(F)F)C(F)(F` (2%) | `CC(=O)O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #223  yield=32.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #3)

```
CO.c1ccc(SSc2ccccc2)cc1.C=CN1CCCCCC1=O>>COC(CSc1ccccc1)N1CCCCCC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.4%) | `platinum` (1.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `reticulated_vitreous_carbon` (79.5%) | `graphite_plate` (7.1%) | `graphite_generic` (4.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (56.1%) | `platinum` (42.4%) | `nickel` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `platinum_plate` (46.5%) | `graphite_rod` (15.8%) | `graphite_plate` (14.0%) | ✓ |
| 池型 | 4 | `undivided` | `divided` (71.5%) | `undivided` (23.2%) | `ABSENT` (5.3%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NEt4` (53.2%) | `NBu4` (45.9%) | `ABSENT` (0.4%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (62.9%) | `OTs` (29.7%) | `PF6` (3.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (9.4%) | `ABSENT` (6.7%) | `tetraaryl_borate` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `ferrocene_mediator` (0.1%) | `Cu_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (63.4%) | `ABSENT` (19.1%) | `ketone` (12.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (97%) | `CO` (1%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `O=S(=O)(O)C(F)(F)F` (55%) | `OC(C(F)(F)F)C(F)(F` (9%) | `__ABSENT__` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✓ / any ✓ |

---

### Reaction #224  yield=32.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #4)

```
C=COCC.OCCF.c1ccc(SSc2ccccc2)cc1>>CCOC(CSc1ccccc1)OCCF
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `platinum` (1.7%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (99.9%) | `graphite_felt` (0.1%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.6%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (100.0%) | `graphite_generic` (0.0%) | `carbon_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.8%) | `divided` (0.9%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.6%) | `NMe4` (2.6%) | `Li` (2.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (96.0%) | `ClO4` (1.7%) | `PF6` (1.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (57.7%) | `pyridine` (3.3%) | `tertiary_amine` (1.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `ammonium_PTC_organocat` (0.4%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (58.9%) | `polar_aprotic_nitrile` (28.4%) | `polar_protic_alcohol` (4.7%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (81%) | `OC(C(F)(F)F)C(F)(F` (11%) | `CO` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `CC(=O)O` (1%) | `O=S([O-])S(=O)(=O)` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #225  yield=39.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #5)

```
CO.C=CN1CCCC1=O.c1ccc(SSc2ccccc2)cc1>>COC(CSc1ccccc1)N1CCCC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.5%) | `platinum` (2.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `reticulated_vitreous_carbon` (80.7%) | `graphite_generic` (11.4%) | `graphite_plate` (4.1%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (82.5%) | `platinum` (16.4%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_rod` (21.0%) | `platinum_plate` (20.2%) | `carbon_rod` (18.6%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (64.5%) | `undivided` (24.5%) | `ABSENT` (11.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NEt4` (57.8%) | `NBu4` (40.0%) | `ABSENT` (1.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (62.0%) | `OTs` (16.9%) | `PF6` (14.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (6.0%) | `ABSENT` (5.4%) | `o2_oxidant` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ferrocene_mediator` (0.1%) | `Cu_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (54.3%) | `ABSENT` (39.1%) | `ketone` (3.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `CO` (1%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `OC(C(F)(F)F)C(F)(F` (36%) | `O=S(=O)(O)C(F)(F)F` (27%) | `__ABSENT__` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CC1[CH-]C(C)=[O]->` (0%) | set ✓ / any ✓ |

---

### Reaction #226  yield=38.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #6)

```
C=COCC.c1ccc(SSc2ccccc2)cc1.OC1CC1>>CCOC(CSc1ccccc1)OC1CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.7%) | `platinum` (5.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (99.7%) | `graphite_generic` (0.1%) | `reticulated_vitreous_carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (94.0%) | `nickel` (3.4%) | `platinum` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (100.0%) | `graphite_generic` (0.0%) | `carbon_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.5%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (68.4%) | `NMe4` (13.8%) | `Li` (12.8%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (94.1%) | `ClO4` (3.0%) | `PF6` (1.7%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (58.1%) | `pyridine` (5.0%) | `tertiary_amine` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `ammonium_PTC_organocat` (0.2%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (51.2%) | `halogenated_aliphatic` (27.2%) | `polar_protic_alcohol` (4.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `O` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #227  yield=42.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #7)

```
OCCO.C=COCC.c1ccc(SSc2ccccc2)cc1>>CCOC(CSc1ccccc1)OCCO
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (1.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (99.9%) | `graphite_felt` (0.0%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (97.9%) | `platinum` (1.4%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (100.0%) | `graphite_generic` (0.0%) | `carbon_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (91.4%) | `NMe4` (5.4%) | `Li` (1.6%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (98.0%) | `PF6` (1.0%) | `ClO4` (0.6%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (63.5%) | `pyridine` (2.6%) | `tertiary_amine` (1.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `ammonium_PTC_organocat` (0.3%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (54.2%) | `polar_aprotic_nitrile` (34.7%) | `polar_aprotic_sulfoxide` (3.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (87%) | `OC(C(F)(F)F)C(F)(F` (8%) | `CO` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #228  yield=47.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #8)

```
CO.C=COCC.Fc1ccc(SSc2ccc(F)cc2)cc1>>CCOC(CSc1ccc(F)cc1)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.2%) | `platinum` (9.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (96.2%) | `graphite_generic` (1.7%) | `reticulated_vitreous_carbon` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (60.8%) | `platinum` (29.4%) | `nickel` (6.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (96.3%) | `platinum_generic` (2.0%) | `nickel_plate` (0.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `divided` (0.6%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (78.6%) | `NMe4` (16.6%) | `NEt4` (4.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (98.1%) | `PF6` (0.6%) | `BArF20` (0.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (74.8%) | `pyridine` (2.8%) | `tertiary_amine` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (68.1%) | `polar_aprotic_nitrile` (22.3%) | `polar_aprotic_sulfoxide` (1.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (73%) | `ClCCl` (34%) | `O` (2%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `O=S(=O)(O)C(F)(F)F` (2%) | `O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #229  yield=55.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #9)

```
CO.c1ccc(SSc2ccccc2)cc1.C=COCc1ccccc1>>COC(CSc1ccccc1)OCc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (89.6%) | `platinum` (10.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (98.9%) | `reticulated_vitreous_carbon` (0.7%) | `graphite_generic` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (70.6%) | `platinum` (24.9%) | `nickel` (4.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (99.8%) | `platinum_plate` (0.1%) | `platinum_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.4%) | `Li` (6.6%) | `NEt4` (5.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (80.2%) | `PF6` (12.5%) | `ClO4` (4.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (25.9%) | `ABSENT` (12.3%) | `tertiary_amine` (3.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.5%) | `ketone` (1.6%) | `ABSENT` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (96%) | `__ABSENT__` (1%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #230  yield=54.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #10)

```
COCCO.C=COCC.c1ccc(SSc2ccccc2)cc1>>CCOC(CSc1ccccc1)OCCOC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.5%) | `platinum` (3.4%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (99.4%) | `graphite_felt` (0.2%) | `graphite_generic` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (94.1%) | `platinum` (4.0%) | `nickel` (1.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (99.8%) | `carbon_generic` (0.1%) | `graphite_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (94.1%) | `NMe4` (3.8%) | `Li` (1.4%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (98.4%) | `ClO4` (0.8%) | `PF6` (0.7%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (54.0%) | `pyridine` (3.0%) | `tertiary_amine` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (71.0%) | `polar_aprotic_amide` (6.6%) | `polar_protic_alcohol` (5.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `CO` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `CC(=O)O` (0%) | `O=CO` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #231  yield=69.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #11)

```
CO.C=COCC.CS(=O)(=O)Oc1ccc(SSc2ccc(OS(C)(=O)=O)cc2)cc1>>CCOC(CSc1ccc(OS(C)(=O)=O)cc1)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (91.7%) | `platinum` (8.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (99.9%) | `carbon_rod` (0.0%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (68.2%) | `platinum` (16.2%) | `nickel` (15.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (100.0%) | `platinum_plate` (0.0%) | `platinum_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (55.3%) | `NMe4` (38.8%) | `NEt4` (3.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (93.1%) | `PF6` (3.5%) | `ABSENT` (0.9%) | ✓ |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (83.0%) | `pyridine` (2.9%) | `tertiary_amine` (0.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (72.7%) | `halogenated_aliphatic` (18.4%) | `ketone` (3.1%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `ClCCl` (0%) | `O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `O` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #232  yield=69.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #12)

```
CO.Cc1ccc(SSc2ccc(C)cc2)cc1.C=COCC>>CCOC(CSc1ccc(C)cc1)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.0%) | `platinum` (19.8%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (97.0%) | `reticulated_vitreous_carbon` (1.7%) | `carbon_rod` (0.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (61.7%) | `platinum` (29.2%) | `nickel` (7.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (99.4%) | `platinum_generic` (0.2%) | `platinum_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.5%) | `divided` (1.2%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (81.6%) | `NMe4` (14.2%) | `NEt4` (1.8%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (95.0%) | `PF6` (2.6%) | `ClO4` (1.5%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (75.7%) | `tertiary_amine` (3.1%) | `pyridine` (2.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (63.9%) | `halogenated_aliphatic` (20.6%) | `polar_aprotic_sulfoxide` (6.0%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `O` (1%) | `ClCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `O` (1%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #233  yield=68.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #13)

```
CO.C=COCC.CC(C)(C)c1ccc(SSc2ccc(C(C)(C)C)cc2)cc1>>CCOC(CSc1ccc(C(C)(C)C)cc1)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (74.7%) | `platinum` (24.8%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (98.9%) | `platinum_generic` (0.3%) | `reticulated_vitreous_carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (63.2%) | `platinum` (25.8%) | `nickel` (6.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (99.1%) | `platinum_generic` (0.5%) | `platinum_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (62.5%) | `NMe4` (29.7%) | `NEt4` (6.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (94.5%) | `PF6` (2.5%) | `ClO4` (1.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (81.0%) | `pyridine` (3.5%) | `tertiary_amine` (1.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (73.3%) | `halogenated_aliphatic` (14.4%) | `ketone` (3.5%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `ClCCl` (0%) | `C1CCOC1` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `OC(C(F)(F)F)C(F)(F` (1%) | `O=S(=O)(O)C(F)(F)F` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #234  yield=70.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #14)

```
CO.c1ccc(SSc2ccccc2)cc1.C=COC(C)(C)C>>COC(CSc1ccccc1)OC(C)(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (65.1%) | `platinum` (34.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (96.6%) | `graphite_generic` (1.7%) | `carbon_rod` (0.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (66.7%) | `carbon` (29.5%) | `nickel` (3.1%) | ✓ |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (71.9%) | `platinum_plate` (18.0%) | `platinum_generic` (7.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.2%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.2%) | `NEt4` (8.1%) | `NMe4` (3.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (82.6%) | `ClO4` (6.2%) | `I` (4.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (46.4%) | `tertiary_amine` (5.8%) | `o2_oxidant` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (31.6%) | `halogenated_aliphatic` (28.6%) | `ABSENT` (19.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `C1CCOC1` (0%) | `ClCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (89%) | `OC(C(F)(F)F)C(F)(F` (7%) | `O=S(=O)(O)C(F)(F)F` (7%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #235  yield=70.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #15)

```
CO.C=COCC.CC(=O)Oc1ccc(SSc2ccc(OC(C)=O)cc2)cc1>>CCOC(CSc1ccc(OC(C)=O)cc1)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.5%) | `platinum` (9.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (99.6%) | `reticulated_vitreous_carbon` (0.2%) | `carbon_rod` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (60.0%) | `platinum` (29.8%) | `nickel` (9.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (99.8%) | `platinum_generic` (0.1%) | `platinum_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (83.1%) | `NMe4` (13.7%) | `NEt4` (1.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.5%) | `PF6` (2.5%) | `ClO4` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (80.3%) | `pyridine` (3.0%) | `tertiary_amine` (0.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (52.4%) | `polar_aprotic_nitrile` (39.0%) | `ketone` (2.6%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (92%) | `ClCCl` (33%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `O` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #236  yield=80.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #16)

```
CO.C=COCCCC.c1ccc(SSc2ccccc2)cc1>>CCCCOC(CSc1ccccc1)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (85.5%) | `platinum` (14.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (99.7%) | `reticulated_vitreous_carbon` (0.1%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (88.2%) | `platinum` (7.8%) | `nickel` (3.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (99.8%) | `platinum_generic` (0.1%) | `carbon_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (91.2%) | `NMe4` (5.6%) | `NEt4` (1.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (85.4%) | `PF6` (11.5%) | `ClO4` (1.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (23.1%) | `ABSENT` (10.7%) | `pyridine` (3.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (85.0%) | `polar_aprotic_amide` (4.3%) | `ketone` (2.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (99%) | `__ABSENT__` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O.[Co]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #237  yield=79.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #17)

```
CO.C=COCC.c1ccc([Te][Te]c2ccccc2)cc1>>CCOC(C[Te]c1ccccc1)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (50.5%) | `platinum` (49.1%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_generic` (76.4%) | `graphite_plate` (13.4%) | `graphite_generic` (3.4%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (48.8%) | `platinum` (48.4%) | `nickel` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `platinum_generic` (61.2%) | `graphite_plate` (37.4%) | `carbon_generic` (0.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `ABSENT` (0.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (68.3%) | `NBu4` (26.0%) | `NEt4` (3.4%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.0%) | `ABSENT` (46.8%) | `PF6` (1.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (11.8%) | `ABSENT` (10.1%) | `hf_amine_complex` (3.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Ni_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (94.1%) | `halogenated_aliphatic` (3.6%) | `polar_aprotic_amide` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (5%) | `O=CO` (1%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #238  yield=79.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #18)

```
CO.C=COCC.Fc1cccc(SSc2cccc(F)c2)c1>>CCOC(CSc1cccc(F)c1)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.0%) | `platinum` (4.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (99.1%) | `graphite_generic` (0.6%) | `graphite_felt` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (72.7%) | `platinum` (20.0%) | `nickel` (6.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (99.4%) | `platinum_generic` (0.4%) | `graphite_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.8%) | `NMe4` (2.2%) | `NEt4` (0.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `BF4` (95.4%) | `PF6` (2.6%) | `ClO4` (0.9%) | ✓ |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (69.3%) | `pyridine` (4.0%) | `tertiary_amine` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (74.6%) | `halogenated_aliphatic` (18.9%) | `ketone` (1.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #239  yield=71.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #19)

```
CO.C=COCC.Brc1ccc(SSc2ccc(Br)cc2)cc1>>CCOC(CSc1ccc(Br)cc1)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (87.4%) | `platinum` (12.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (98.1%) | `graphite_generic` (0.9%) | `reticulated_vitreous_carbon` (0.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (59.5%) | `platinum` (30.5%) | `nickel` (8.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (97.6%) | `platinum_generic` (1.7%) | `nickel_plate` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (91.3%) | `NMe4` (6.7%) | `NEt4` (1.6%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (97.6%) | `PF6` (1.4%) | `ClO4` (0.6%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (81.6%) | `pyridine` (2.5%) | `tertiary_amine` (0.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (60.1%) | `halogenated_aliphatic` (30.9%) | `polar_aprotic_amide` (2.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `O` (1%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #240  yield=88.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #20)

```
CO.C=COCC.Fc1ccccc1SSc1ccccc1F>>CCOC(CSc1ccccc1F)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (85.1%) | `platinum` (14.8%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (75.7%) | `graphite_generic` (10.3%) | `carbon_rod` (6.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (65.4%) | `platinum` (31.5%) | `nickel` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (66.9%) | `platinum_generic` (29.2%) | `carbon_generic` (1.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.9%) | `NEt4` (1.5%) | `NMe4` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.5%) | `PF6` (3.8%) | `ClO4` (0.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (63.6%) | `pyridine` (4.2%) | `alkali_carbonate` (1.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (84.5%) | `halogenated_aliphatic` (10.0%) | `polar_aprotic_amide` (1.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (91%) | `O` (1%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #241  yield=83.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #21)

```
CO.c1ccc(SSc2ccccc2)cc1.C=COC1CCCCC1>>COC(CSc1ccccc1)OC1CCCCC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.8%) | `platinum` (4.1%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (97.7%) | `reticulated_vitreous_carbon` (1.0%) | `graphite_felt` (0.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (55.6%) | `carbon` (39.5%) | `nickel` (4.8%) | ✓ |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (88.6%) | `platinum_generic` (7.9%) | `platinum_plate` (2.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.8%) | `ABSENT` (9.5%) | `Li` (2.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (68.2%) | `ABSENT` (11.1%) | `I` (6.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (27.9%) | `tertiary_amine` (7.1%) | `ABSENT` (6.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (78.9%) | `polar_aprotic_nitrile` (9.5%) | `ketone` (5.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `__ABSENT__` (87%) | `CC#N` (3%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (49%) | `O=S(=O)(O)C(F)(F)F` (2%) | `__ABSENT__` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #242  yield=86.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #22)

```
CO.C=COCC.c1ccc([Se][Se]c2ccccc2)cc1>>CCOC(C[Se]c1ccccc1)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.4%) | `platinum` (2.8%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (90.5%) | `graphite_generic` (6.8%) | `carbon_rod` (1.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (90.1%) | `carbon` (6.2%) | `stainless_steel` (1.3%) | ✓ |
| 阴极 (细类) | 49 | `graphite_plate` | `platinum_plate` (76.8%) | `platinum_generic` (20.3%) | `stainless_steel_generic` (1.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (79.2%) | `ABSENT` (9.7%) | `NMe4` (5.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (46.7%) | `I` (40.1%) | `ABSENT` (6.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_other_salt` | `water` (7.4%) | `cf3_source` (6.6%) | `ABSENT` (5.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `ammonium_PTC_organocat` (0.3%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.0%) | `halogenated_aliphatic` (1.7%) | `polar_aprotic_amide` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `CO` (0%) | `C1CCOC1` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Li+].[O-][Cl+3]([` + `FC(F)(F)c1ccncc1` | `O` (57%) | `[18OH2]` (2%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #243  yield=90.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #23)

```
CO.C=COCC.Clc1ccc(SSc2ccc(Cl)cc2)cc1>>CCOC(CSc1ccc(Cl)cc1)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (83.1%) | `platinum` (16.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (98.4%) | `reticulated_vitreous_carbon` (0.5%) | `platinum_generic` (0.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (48.4%) | `platinum` (46.1%) | `nickel` (4.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (99.6%) | `platinum_generic` (0.2%) | `platinum_plate` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.2%) | `NMe4` (7.4%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (98.0%) | `PF6` (0.9%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (78.6%) | `pyridine` (2.9%) | `tertiary_amine` (1.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (59.3%) | `halogenated_aliphatic` (32.0%) | `polar_aprotic_amide` (3.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (0%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #244  yield=85.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #24)

```
CO.C=COCCC.c1ccc(SSc2ccccc2)cc1>>CCCOC(CSc1ccccc1)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.9%) | `platinum` (10.9%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (99.7%) | `reticulated_vitreous_carbon` (0.1%) | `graphite_generic` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (79.9%) | `platinum` (15.0%) | `nickel` (4.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (98.4%) | `platinum_plate` (1.0%) | `nickel_plate` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (86.6%) | `NMe4` (6.6%) | `NEt4` (5.7%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (81.5%) | `PF6` (14.1%) | `ClO4` (3.2%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (37.8%) | `ABSENT` (7.5%) | `pyridine` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.6%) | `polar_aprotic_sulfoxide` (4.0%) | `ABSENT` (3.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `OB(O)c1ccccc1` (1%) | `__ABSENT__` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O.[Co]` (0%) | `CC1=Cc2ccccc2N(c2c` (0%) | set ✓ / any ✓ |

---

### Reaction #245  yield=89.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #25)

```
CCO.C=COCC.c1ccc(SSc2ccccc2)cc1>>CCOC(CSc1ccccc1)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `platinum` (1.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (99.9%) | `graphite_generic` (0.0%) | `graphite_felt` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `platinum` (0.9%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (100.0%) | `graphite_generic` (0.0%) | `carbon_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.3%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (89.2%) | `NMe4` (7.7%) | `Li` (1.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (96.2%) | `PF6` (1.5%) | `ClO4` (1.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (59.8%) | `pyridine` (3.0%) | `tertiary_amine` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `ammonium_PTC_organocat` (0.4%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (57.2%) | `polar_aprotic_nitrile` (32.2%) | `polar_protic_alcohol` (2.8%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (93%) | `OC(C(F)(F)F)C(F)(F` (4%) | `ClCCl` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)(O)C(F)(F)F` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #246  yield=92.0%

**Source paper**: [`AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json`](reactions_by_journal_alkene_ec_audited/AdvSynthCatal/2025_Advanced_Synthesis_Catalysis_2025_367_22_e70132.json) (反应 idx 在该 JSON 内 = #26)

```
CO.C=COCC.c1ccc(SSc2ccccc2)cc1>>CCOC(CSc1ccccc1)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (83.0%) | `platinum` (16.6%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `graphite_plate` (99.9%) | `reticulated_vitreous_carbon` (0.0%) | `graphite_generic` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `carbon` (89.1%) | `platinum` (5.0%) | `nickel` (5.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_plate` | `graphite_plate` (100.0%) | `graphite_generic` (0.0%) | `carbon_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (59.5%) | `NMe4` (33.7%) | `NEt4` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.4%) | `PF6` (6.6%) | `ClO4` (1.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `cf3_source` | `cf3_source` (71.5%) | `pyridine` (5.8%) | `tertiary_amine` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (74.8%) | `polar_aprotic_sulfoxide` (5.9%) | `polar_aprotic_amide` (5.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `FC(F)(F)c1ccncc1` | `FC(F)(F)c1ccncc1` (100%) | `O` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC(=O)O.[Co]` (0%) | set ✓ / any ✓ |

---

### Reaction #247  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #248  yield=0.5%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #249  yield=91.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #250  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #251  yield=67.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `Br` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✗ |
| 试剂大类 | 103 | `ferrocene_mediator` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #252  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #253  yield=78.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #254  yield=34.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #255  yield=53.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #256  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #257  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #258  yield=83.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #259  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✗ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #260  yield=88.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #261  yield=15.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p10_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p10_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC#N>>CCOC(=O)C1(C#N)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.8%) | `sacrificial_iron` (6.0%) | `sacrificial_zinc` (5.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `reticulated_vitreous_carbon` (97.8%) | `carbon_generic` (0.9%) | `unknown_electrode` (0.4%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (74.5%) | `nickel` (23.8%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (73.9%) | `platinum_generic` (24.3%) | `platinum_wire` (1.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (86.0%) | `divided` (10.9%) | `ABSENT` (3.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (91.9%) | `NEt4` (3.6%) | `Li` (2.2%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (49.0%) | `PF6` (23.4%) | `I` (15.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.1%) | `carboxylic_acid` (5.8%) | `primary_amine` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `thianthrene_phenothiazine_cat` (45.4%) | `ABSENT` (18.0%) | `organic_neutral_cat` (14.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (79.2%) | `tfe` (8.6%) | `polar_aprotic_nitrile` (7.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CN(C)C=O` (52%) | `CC#N` (37%) | `O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` | `__ABSENT__` (99%) | `O` (1%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `COc1ccc2c(c1)Sc1cc` (8%) | `COc1ccc2c(c1)Sc1cc` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |

---

### Reaction #262  yield=0.5%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p10_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p10_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC#N>>CCOC(=O)C1(C#N)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.8%) | `sacrificial_iron` (6.0%) | `sacrificial_zinc` (5.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `reticulated_vitreous_carbon` (97.8%) | `carbon_generic` (0.9%) | `unknown_electrode` (0.4%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (74.5%) | `nickel` (23.8%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (73.9%) | `platinum_generic` (24.3%) | `platinum_wire` (1.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (86.0%) | `divided` (10.9%) | `ABSENT` (3.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (91.9%) | `NEt4` (3.6%) | `Li` (2.2%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (49.0%) | `PF6` (23.4%) | `I` (15.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.1%) | `carboxylic_acid` (5.8%) | `primary_amine` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `thianthrene_phenothiazine_cat` (45.4%) | `ABSENT` (18.0%) | `organic_neutral_cat` (14.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (79.2%) | `tfe` (8.6%) | `polar_aprotic_nitrile` (7.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CN(C)C=O` (52%) | `CC#N` (37%) | `O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` | `__ABSENT__` (99%) | `O` (1%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `COc1ccc2c(c1)Sc1cc` (8%) | `COc1ccc2c(c1)Sc1cc` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |

---

### Reaction #263  yield=0.5%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p10_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p10_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC#N>>CCOC(=O)C1(C#N)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.8%) | `sacrificial_iron` (6.0%) | `sacrificial_zinc` (5.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `reticulated_vitreous_carbon` (97.8%) | `carbon_generic` (0.9%) | `unknown_electrode` (0.4%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (74.5%) | `nickel` (23.8%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (73.9%) | `platinum_generic` (24.3%) | `platinum_wire` (1.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (86.0%) | `divided` (10.9%) | `ABSENT` (3.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (91.9%) | `NEt4` (3.6%) | `Li` (2.2%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (49.0%) | `PF6` (23.4%) | `I` (15.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.1%) | `carboxylic_acid` (5.8%) | `primary_amine` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `thianthrene_phenothiazine_cat` (45.4%) | `ABSENT` (18.0%) | `organic_neutral_cat` (14.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (79.2%) | `tfe` (8.6%) | `polar_aprotic_nitrile` (7.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CN(C)C=O` (52%) | `CC#N` (37%) | `O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` | `__ABSENT__` (99%) | `O` (1%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `COc1ccc2c(c1)Sc1cc` (8%) | `COc1ccc2c(c1)Sc1cc` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |

---

### Reaction #264  yield=0.5%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p10_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p10_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC#N>>CCOC(=O)C1(C#N)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.8%) | `sacrificial_iron` (6.0%) | `sacrificial_zinc` (5.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `reticulated_vitreous_carbon` (97.8%) | `carbon_generic` (0.9%) | `unknown_electrode` (0.4%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (74.5%) | `nickel` (23.8%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (73.9%) | `platinum_generic` (24.3%) | `platinum_wire` (1.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (86.0%) | `divided` (10.9%) | `ABSENT` (3.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (91.9%) | `NEt4` (3.6%) | `Li` (2.2%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (49.0%) | `PF6` (23.4%) | `I` (15.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (11.1%) | `carboxylic_acid` (5.8%) | `primary_amine` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `thianthrene_phenothiazine_cat` (45.4%) | `ABSENT` (18.0%) | `organic_neutral_cat` (14.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (79.2%) | `tfe` (8.6%) | `polar_aprotic_nitrile` (7.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CN(C)C=O` (52%) | `CC#N` (37%) | `O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` | `__ABSENT__` (99%) | `O` (1%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `COc1ccc2c(c1)Sc1cc` (8%) | `COc1ccc2c(c1)Sc1cc` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |

---

### Reaction #265  yield=12.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p10_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p10_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC#N>>CCOC(=O)C1(C#N)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.8%) | `sacrificial_iron` (6.0%) | `sacrificial_zinc` (5.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `reticulated_vitreous_carbon` (97.8%) | `carbon_generic` (0.9%) | `unknown_electrode` (0.4%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (74.5%) | `nickel` (23.8%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (73.9%) | `platinum_generic` (24.3%) | `platinum_wire` (1.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (86.0%) | `divided` (10.9%) | `ABSENT` (3.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (91.9%) | `NEt4` (3.6%) | `Li` (2.2%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (49.0%) | `PF6` (23.4%) | `I` (15.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (11.1%) | `carboxylic_acid` (5.8%) | `primary_amine` (2.4%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `thianthrene_phenothiazine_cat` (45.4%) | `ABSENT` (18.0%) | `organic_neutral_cat` (14.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (79.2%) | `tfe` (8.6%) | `polar_aprotic_nitrile` (7.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CN(C)C=O` (52%) | `CC#N` (37%) | `O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` | `__ABSENT__` (99%) | `O` (1%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `COc1ccc2c(c1)Sc1cc` (8%) | `COc1ccc2c(c1)Sc1cc` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |

---

### Reaction #266  yield=0.5%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #267  yield=0.5%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #268  yield=58.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #269  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #270  yield=91.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #271  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #272  yield=45.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p11_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p11_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.N#CCC#N>>N#CC1(C#N)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.5%) | `sacrificial_zinc` (6.3%) | `sacrificial_iron` (1.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `pencil_graphite` (56.9%) | `reticulated_vitreous_carbon` (39.1%) | `carbon_generic` (1.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (65.3%) | `nickel` (32.9%) | `carbon` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (56.2%) | `nickel_wire` (32.7%) | `platinum_wire` (8.0%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (98.0%) | `undivided` (1.6%) | `ABSENT` (0.3%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `ABSENT` (68.2%) | `Li` (16.6%) | `NBu4` (9.0%) | ✗ |
| 电解质 anion | 26 | `I` | `ABSENT` (56.3%) | `I` (15.4%) | `molecular_no_ion` (11.4%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `carboxylic_acid` (47.1%) | `ABSENT` (4.7%) | `iodide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (42.9%) | `thianthrene_phenothiazine_cat` (21.3%) | `pyridine_organocat` (9.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (74.3%) | `polar_aprotic_nitrile` (17.8%) | `ABSENT` (4.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CN(C)C=O` (57%) | `CC#N` (32%) | `CC(=O)N(C)C` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Cs+]` | `O=C(O)C(F)(F)F` (99%) | `O=C([O-])[O-].[Cs+` (82%) | `c1ccc2c(c1)Sc1cccc` (38%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `F[P-](F)(F)(F)(F)F` | `__ABSENT__` (82%) | `[Br-].[Br-].[Mn+2]` (2%) | `CC#N.CC(c1ccccn1)(` (2%) | set ✗ / any ✗ |

---

### Reaction #273  yield=37.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p11_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p11_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.N#CCC#N>>N#CC1(C#N)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.5%) | `sacrificial_zinc` (6.3%) | `sacrificial_iron` (1.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `pencil_graphite` (56.9%) | `reticulated_vitreous_carbon` (39.1%) | `carbon_generic` (1.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (65.3%) | `nickel` (32.9%) | `carbon` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (56.2%) | `nickel_wire` (32.7%) | `platinum_wire` (8.0%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (98.0%) | `undivided` (1.6%) | `ABSENT` (0.3%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `ABSENT` (68.2%) | `Li` (16.6%) | `NBu4` (9.0%) | ✗ |
| 电解质 anion | 26 | `I` | `ABSENT` (56.3%) | `I` (15.4%) | `molecular_no_ion` (11.4%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `carboxylic_acid` (47.1%) | `ABSENT` (4.7%) | `iodide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (42.9%) | `thianthrene_phenothiazine_cat` (21.3%) | `pyridine_organocat` (9.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (74.3%) | `polar_aprotic_nitrile` (17.8%) | `ABSENT` (4.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CN(C)C=O` (57%) | `CC#N` (32%) | `CC(=O)N(C)C` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Cs+]` | `O=C(O)C(F)(F)F` (99%) | `O=C([O-])[O-].[Cs+` (82%) | `c1ccc2c(c1)Sc1cccc` (38%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `F[P-](F)(F)(F)(F)F` | `__ABSENT__` (82%) | `[Br-].[Br-].[Mn+2]` (2%) | `CC#N.CC(c1ccccn1)(` (2%) | set ✗ / any ✗ |

---

### Reaction #274  yield=47.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p11_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p11_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.N#CCC#N>>N#CC1(C#N)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.5%) | `sacrificial_zinc` (6.3%) | `sacrificial_iron` (1.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `pencil_graphite` (56.9%) | `reticulated_vitreous_carbon` (39.1%) | `carbon_generic` (1.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (65.3%) | `nickel` (32.9%) | `carbon` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (56.2%) | `nickel_wire` (32.7%) | `platinum_wire` (8.0%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (98.0%) | `undivided` (1.6%) | `ABSENT` (0.3%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `ABSENT` (68.2%) | `Li` (16.6%) | `NBu4` (9.0%) | ✗ |
| 电解质 anion | 26 | `I` | `ABSENT` (56.3%) | `I` (15.4%) | `molecular_no_ion` (11.4%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `carboxylic_acid` (47.1%) | `ABSENT` (4.7%) | `iodide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (42.9%) | `thianthrene_phenothiazine_cat` (21.3%) | `pyridine_organocat` (9.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (74.3%) | `polar_aprotic_nitrile` (17.8%) | `ABSENT` (4.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CN(C)C=O` (57%) | `CC#N` (32%) | `CC(=O)N(C)C` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Cs+]` | `O=C(O)C(F)(F)F` (99%) | `O=C([O-])[O-].[Cs+` (82%) | `c1ccc2c(c1)Sc1cccc` (38%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `F[P-](F)(F)(F)(F)F` | `__ABSENT__` (82%) | `[Br-].[Br-].[Mn+2]` (2%) | `CC#N.CC(c1ccccn1)(` (2%) | set ✗ / any ✗ |

---

### Reaction #275  yield=61.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p11_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p11_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.N#CCC#N>>N#CC1(C#N)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.5%) | `sacrificial_zinc` (6.3%) | `sacrificial_iron` (1.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `pencil_graphite` (56.9%) | `reticulated_vitreous_carbon` (39.1%) | `carbon_generic` (1.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (65.3%) | `nickel` (32.9%) | `carbon` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (56.2%) | `nickel_wire` (32.7%) | `platinum_wire` (8.0%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (98.0%) | `undivided` (1.6%) | `ABSENT` (0.3%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `ABSENT` (68.2%) | `Li` (16.6%) | `NBu4` (9.0%) | ✗ |
| 电解质 anion | 26 | `I` | `ABSENT` (56.3%) | `I` (15.4%) | `molecular_no_ion` (11.4%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `carboxylic_acid` (47.1%) | `ABSENT` (4.7%) | `iodide_anion` (2.0%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (42.9%) | `thianthrene_phenothiazine_cat` (21.3%) | `pyridine_organocat` (9.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (74.3%) | `polar_aprotic_nitrile` (17.8%) | `ABSENT` (4.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CN(C)C=O` (57%) | `CC#N` (32%) | `CC(=O)N(C)C` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Cs+]` | `O=C(O)C(F)(F)F` (99%) | `O=C([O-])[O-].[Cs+` (82%) | `c1ccc2c(c1)Sc1cccc` (38%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `F[P-](F)(F)(F)(F)F` | `__ABSENT__` (82%) | `[Br-].[Br-].[Mn+2]` (2%) | `CC#N.CC(c1ccccn1)(` (2%) | set ✗ / any ✗ |

---

### Reaction #276  yield=85.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #277  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `nhpi_mediator` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #278  yield=0.5%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #279  yield=68.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #280  yield=91.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #281  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #282  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #283  yield=66.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #284  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #285  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #286  yield=0.5%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #287  yield=83.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #288  yield=91.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #289  yield=58.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #290  yield=34.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #291  yield=53.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #292  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #293  yield=31.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #294  yield=66.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #295  yield=51.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_iron` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✗ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #296  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✗ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #297  yield=55.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✗ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #298  yield=91.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #299  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #300  yield=91.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #301  yield=85.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #302  yield=66.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #303  yield=68.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #304  yield=0.5%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #305  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #306  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #307  yield=0.5%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #308  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #309  yield=91.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #310  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `Cl` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #311  yield=67.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `Br` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #312  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `OH` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #313  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #314  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #315  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✗ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `Fe_complex` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #316  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ferrocene_mediator` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #317  yield=17.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #318  yield=51.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #319  yield=91.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #320  yield=91.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #321  yield=33.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #322  yield=43.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #323  yield=76.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #324  yield=83.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #325  yield=55.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #326  yield=78.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carboxylate` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #327  yield=32.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #328  yield=23.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #329  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #330  yield=69.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #331  yield=56.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #332  yield=89.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #333  yield=91.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #334  yield=87.0%

**Source paper**: [`Angew/10.1002_anie.202425634_sup_1_p6_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202425634_sup_1_p6_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCOc1ccc(-c2ccccc2)cc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #335  yield=5.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #0)

```
CCOC(=O)CC#N.C=Cc1ccc(-c2ccccc2)cc1>>CCOC(=O)[C@]1(C#N)C[C@@H]1c1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `sacrificial_iron` (0.7%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (99.7%) | `graphite_generic` (0.1%) | `unknown_electrode` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.9%) | `carbon` (3.5%) | `nickel` (2.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (56.7%) | `platinum_plate` (14.5%) | `platinum_wire` (13.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (95.0%) | `ABSENT` (4.3%) | `divided` (0.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `molecular_no_ion` | `NBu4` (85.2%) | `NEt4` (7.6%) | `Li` (4.3%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `BF4` (67.9%) | `PF6` (7.6%) | `ClO4` (7.3%) | ✗ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (19.2%) | `alkali_other_salt` (2.8%) | `primary_amine` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `thianthrene_phenothiazine_cat` (66.6%) | `ABSENT` (14.8%) | `organic_neutral_cat` (6.5%) | ✗ |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (45.4%) | `tfe` (29.3%) | `ABSENT` (9.3%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (94%) | `CN(C)C=O` (5%) | `COC(C)(C)C` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Cs+]` | `__ABSENT__` (100%) | `O` (0%) | `O=C([O-])[O-].[Cs+` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `COc1ccc2c(c1)Sc1cc` (48%) | `__ABSENT__` (29%) | `COc1ccc2c(c1)Sc1cc` (2%) | set ✗ / any ✗ |

---

### Reaction #336  yield=28.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #1)

```
CCOC(=O)CC(=O)OCC.C=CC(=O)CCCCC>>CCCCCC(=O)C1CC1(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.3%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_felt` (40.5%) | `reticulated_vitreous_carbon` (39.0%) | `carbon_generic` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (58.0%) | `nickel` (23.4%) | `carbon` (16.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (33.6%) | `carbon_felt` (31.5%) | `platinum_generic` (13.3%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (94.0%) | `undivided` (5.4%) | `divided` (0.5%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (47.7%) | `ABSENT` (32.0%) | `Li` (18.9%) | ✗ |
| 电解质 anion | 26 | `I` | `ClO4` (42.0%) | `ABSENT` (39.9%) | `PF6` (9.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (8.7%) | `tertiary_amine` (5.4%) | `alkali_other_salt` (4.8%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `pyridine_organocat` (49.1%) | `Mn_complex` (22.4%) | `Cu_complex` (9.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (88.3%) | `polar_aprotic_amide` (4.8%) | `polar_protic_alcohol` (2.2%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (98%) | `O` (0%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `C[Si](C)(C)N=[N+]=` (11%) | `CC(=O)O` (6%) | `O=S([O-])([O-])=S.` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)C(F)(F)F` (8%) | `c1ccc(-c2ccccn2)nc` (2%) | `__OTHER__` (2%) | set ✗ / any ✗ |

---

### Reaction #337  yield=29.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #2)

```
CCOC(=O)CS(=O)(=O)c1ccccc1.C=CCCCOc1ccc(-c2ccccc2)cc1>>CCOC(=O)[C@]1(S(=O)(=O)c2ccccc2)C[C@@H]1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (72.2%) | `platinum` (11.5%) | `sacrificial_iron` (9.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (7.7%) | `unknown_electrode` (4.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.9%) | `carbon` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (55.5%) | `nickel_foam` (42.8%) | `platinum_wire` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (95.3%) | `Li` (2.1%) | `ABSENT` (1.3%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (41.1%) | `ClO4` (29.3%) | `I` (12.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.4%) | `iodide_anion` (3.1%) | `as_solvent_halogenated_aliphat` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (85.8%) | `organic_neutral_cat` (4.8%) | `Mn_complex` (1.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.5%) | `polar_aprotic_amide` (22.8%) | `ABSENT` (20.6%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (78%) | `CC(=O)O` (21%) | `O` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCOC(C)=O` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (94%) | `[Br-].[Br-].[Mn+2]` (0%) | `[Cl-].[Cl-].[Ni+2]` (0%) | set ✗ / any ✗ |

---

### Reaction #338  yield=29.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #3)

```
CCOC(=O)CS(=O)(=O)c1ccccc1.C=CCCCOc1ccc(-c2ccccc2)cc1>>CCOC(=O)[C@@]1(S(=O)(=O)c2ccccc2)C[C@@H]1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (72.2%) | `platinum` (11.5%) | `sacrificial_iron` (9.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (7.7%) | `unknown_electrode` (4.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.9%) | `carbon` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (55.5%) | `nickel_foam` (42.8%) | `platinum_wire` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (95.3%) | `Li` (2.1%) | `ABSENT` (1.3%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (41.1%) | `ClO4` (29.3%) | `I` (12.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.4%) | `iodide_anion` (3.1%) | `as_solvent_halogenated_aliphat` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (85.8%) | `organic_neutral_cat` (4.8%) | `Mn_complex` (1.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.5%) | `polar_aprotic_amide` (22.8%) | `ABSENT` (20.6%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (78%) | `CC(=O)O` (21%) | `O` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCOC(C)=O` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (94%) | `[Br-].[Br-].[Mn+2]` (0%) | `[Cl-].[Cl-].[Ni+2]` (0%) | set ✗ / any ✗ |

---

### Reaction #339  yield=30.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #4)

```
CCOC(=O)CC(=O)OCC.C=CC(C)CCC>>CCC[C@@H](C)[C@H]1CC1(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.4%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (78.3%) | `carbon_generic` (10.9%) | `graphite_generic` (6.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.7%) | `nickel` (8.7%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.9%) | `nickel_foam` (2.4%) | `nickel_generic` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.8%) | `ABSENT` (3.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (93.2%) | `Li` (6.3%) | `NEt4` (0.2%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (42.4%) | `ClO4` (39.4%) | `I` (11.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (20.4%) | `ABSENT` (4.0%) | `metal_oxide_oxidant` (2.0%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ammonium_PTC_organocat` (36.0%) | `ABSENT` (24.3%) | `ionic_organocat` (14.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (55.1%) | `polar_protic_alcohol` (42.7%) | `cyclic_ether` (1.1%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (75%) | `CO` (25%) | `O` (10%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (30%) | `[Fe+2].c1cc[cH-]c1` (2%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (75%) | `CCCC[N+](CCCC)(CCC` (8%) | `CCCC[N+](CCCC)(CCC` (7%) | set ✗ / any ✗ |

---

### Reaction #340  yield=30.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #5)

```
CCOC(=O)CC(=O)OCC.C=CC(C)CCC>>CCC[C@@H](C)[C@@H]1CC1(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.4%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (78.3%) | `carbon_generic` (10.9%) | `graphite_generic` (6.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.7%) | `nickel` (8.7%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.9%) | `nickel_foam` (2.4%) | `nickel_generic` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.8%) | `ABSENT` (3.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (93.2%) | `Li` (6.3%) | `NEt4` (0.2%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (42.4%) | `ClO4` (39.4%) | `I` (11.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (20.4%) | `ABSENT` (4.0%) | `metal_oxide_oxidant` (2.0%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ammonium_PTC_organocat` (36.0%) | `ABSENT` (24.3%) | `ionic_organocat` (14.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (55.1%) | `polar_protic_alcohol` (42.7%) | `cyclic_ether` (1.1%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (75%) | `CO` (25%) | `O` (10%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (30%) | `[Fe+2].c1cc[cH-]c1` (2%) | `CC(=O)[O-].[Na+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (75%) | `CCCC[N+](CCCC)(CCC` (8%) | `CCCC[N+](CCCC)(CCC` (7%) | set ✗ / any ✗ |

---

### Reaction #341  yield=36.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #6)

```
COC(=O)CC(=O)OCc1ccccc1.C=CCCCOc1ccc(-c2ccccc2)cc1>>COC(=O)[C@]1(C(=O)OCc2ccccc2)C[C@@H]1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (98.4%) | `carbon_generic` (1.2%) | `carbon_felt` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.5%) | `nickel` (1.6%) | `carbon` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.1%) | `nickel_foam` (0.8%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (79.3%) | `ABSENT` (19.3%) | `divided` (1.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (95.9%) | `ABSENT` (1.2%) | `Na` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (34.0%) | `PF6` (17.5%) | `Cl` (17.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (24.1%) | `ABSENT` (5.5%) | `alkali_other_salt` (4.3%) | ✓ |
| 催化剂大类 | 49 | `Fe_complex` | `Co_complex` (43.1%) | `organic_neutral_cat` (16.0%) | `ABSENT` (12.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (40.5%) | `ketone` (19.2%) | `tfe` (13.0%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (96%) | `COC(C)(C)C` (4%) | `CC(=O)O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (57%) | `O=C([O-])[O-].[K+]` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cccc1.c1c` | `CC(C)(C)c1ccc2[O-]` (5%) | `[O-]1c2cc(cc2C=[N+` (4%) | `CC(=O)[CH-]C(C)=O.` (1%) | set ✗ / any ✗ |

---

### Reaction #342  yield=36.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #6)

```
COC(=O)CC(=O)OCc1ccccc1.C=CCCCOc1ccc(-c2ccccc2)cc1>>COC(=O)[C@]1(C(=O)OCc2ccccc2)C[C@@H]1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (98.4%) | `carbon_generic` (1.2%) | `carbon_felt` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.5%) | `nickel` (1.6%) | `carbon` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.1%) | `nickel_foam` (0.8%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (79.3%) | `ABSENT` (19.3%) | `divided` (1.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (95.9%) | `ABSENT` (1.2%) | `Na` (1.0%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (34.0%) | `PF6` (17.5%) | `Cl` (17.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (24.1%) | `ABSENT` (5.5%) | `alkali_other_salt` (4.3%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (43.1%) | `organic_neutral_cat` (16.0%) | `ABSENT` (12.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (40.5%) | `ketone` (19.2%) | `tfe` (13.0%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (96%) | `COC(C)(C)C` (4%) | `CC(=O)O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (57%) | `O=C([O-])[O-].[K+]` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cccc1.c1c` | `CC(C)(C)c1ccc2[O-]` (5%) | `[O-]1c2cc(cc2C=[N+` (4%) | `CC(=O)[CH-]C(C)=O.` (1%) | set ✗ / any ✗ |

---

### Reaction #343  yield=34.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #8)

```
CCOC(=O)CC(=O)OCC.C=CCCCOC(=O)C(C)c1ccc(CC(C)C)cc1>>CCOC(=O)C1(C(=O)OCC)C[C@@H]1CCCOC(=O)[C@H](C)c1ccc(CC(C)C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (59.1%) | `reticulated_vitreous_carbon` (26.1%) | `graphite_generic` (9.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.0%) | `nickel` (5.4%) | `stainless_steel` (3.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.4%) | `stainless_steel_generic` (2.4%) | `nickel_generic` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (60.9%) | `undivided` (33.1%) | `ABSENT` (6.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (95.6%) | `NEt4` (2.0%) | `Li` (1.1%) | ✓ |
| 电解质 anion | 26 | `I` | `PF6` (45.2%) | `BF4` (29.4%) | `ClO4` (16.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (12.5%) | `alkali_carbonate` (6.8%) | `as_solvent_polar_aprotic_sulfo` (5.6%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (91.9%) | `organic_neutral_cat` (4.6%) | `Co_complex` (1.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (58.0%) | `halogenated_aliphatic` (20.1%) | `cyclic_ether` (14.5%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (98%) | `O` (38%) | `ClCCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CCN(CC)CC` (55%) | `Cl` (10%) | `O=C([O-])[O-].[Na+` (10%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (1%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✗ / any ✓ |

---

### Reaction #344  yield=34.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #9)

```
CCOC(=O)CC(=O)OCC.C=CCCCOC(=O)C(C)c1ccc(CC(C)C)cc1>>CCOC(=O)C1(C(=O)OCC)C[C@@H]1CCCOC(=O)[C@@H](C)c1ccc(CC(C)C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (59.1%) | `reticulated_vitreous_carbon` (26.1%) | `graphite_generic` (9.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.0%) | `nickel` (5.4%) | `stainless_steel` (3.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.4%) | `stainless_steel_generic` (2.4%) | `nickel_generic` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (60.9%) | `undivided` (33.1%) | `ABSENT` (6.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (95.6%) | `NEt4` (2.0%) | `Li` (1.1%) | ✓ |
| 电解质 anion | 26 | `I` | `PF6` (45.2%) | `BF4` (29.4%) | `ClO4` (16.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (12.5%) | `alkali_carbonate` (6.8%) | `as_solvent_polar_aprotic_sulfo` (5.6%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (91.9%) | `organic_neutral_cat` (4.6%) | `Co_complex` (1.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (58.0%) | `halogenated_aliphatic` (20.1%) | `cyclic_ether` (14.5%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (98%) | `O` (38%) | `ClCCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CCN(CC)CC` (55%) | `Cl` (10%) | `O=C([O-])[O-].[Na+` (10%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (1%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✗ / any ✓ |

---

### Reaction #345  yield=32.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #10)

```
CC(C)(C)OC(=O)CC(=O)OCc1ccccc1.C=CCCCOc1ccc(-c2ccccc2)cc1>>CC(C)(C)OC(=O)[C@]1(C(=O)OCc2ccccc2)C[C@@H]1CCCOc1ccc(-c2c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.2%) | `sacrificial_zinc` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (95.8%) | `carbon_generic` (2.3%) | `carbon_felt` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.7%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (97.3%) | `nickel_foam` (2.2%) | `platinum_wire` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (70.3%) | `ABSENT` (19.2%) | `divided` (10.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (86.3%) | `ABSENT` (7.1%) | `Li` (4.4%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (32.0%) | `PF6` (27.7%) | `ABSENT` (14.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (8.8%) | `ABSENT` (6.4%) | `iodide_anion` (3.6%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (48.0%) | `thianthrene_phenothiazine_cat` (16.4%) | `organic_neutral_cat` (12.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (32.0%) | `ketone` (23.3%) | `ABSENT` (20.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (4%) | `CC(=O)O` (2%) | `CN(C)C=O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (8%) | `O=C([O-])[O-].[K+]` (2%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (83%) | `[Br-].[Br-].[Mn+2]` (0%) | `CC#N.CC(c1ccccn1)(` (0%) | set ✗ / any ✗ |

---

### Reaction #346  yield=32.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #11)

```
CC(C)(C)OC(=O)CC(=O)OCc1ccccc1.C=CCCCOc1ccc(-c2ccccc2)cc1>>CC(C)(C)OC(=O)[C@@]1(C(=O)OCc2ccccc2)C[C@@H]1CCCOc1ccc(-c2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.2%) | `sacrificial_zinc` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (95.8%) | `carbon_generic` (2.3%) | `carbon_felt` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (0.7%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (97.3%) | `nickel_foam` (2.2%) | `platinum_wire` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (70.3%) | `ABSENT` (19.2%) | `divided` (10.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (86.3%) | `ABSENT` (7.1%) | `Li` (4.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (32.0%) | `PF6` (27.7%) | `ABSENT` (14.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (8.8%) | `ABSENT` (6.4%) | `iodide_anion` (3.6%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (48.0%) | `thianthrene_phenothiazine_cat` (16.4%) | `organic_neutral_cat` (12.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (32.0%) | `ketone` (23.3%) | `ABSENT` (20.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (4%) | `CC(=O)O` (2%) | `CN(C)C=O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (8%) | `O=C([O-])[O-].[K+]` (2%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (83%) | `[Br-].[Br-].[Mn+2]` (0%) | `CC#N.CC(c1ccccn1)(` (0%) | set ✗ / any ✗ |

---

### Reaction #347  yield=31.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #12)

```
CCOC(=O)CC(=O)OCC.C=CCCCOC(=O)[C@@H](C)c1ccc2cc(OC)ccc2c1>>CCOC(=O)C1(C(=O)OCC)C[C@@H]1CCCOC(=O)[C@@H](C)c1ccc2cc(OC)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (59.4%) | `graphite_generic` (38.0%) | `carbon_felt` (0.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.9%) | `stainless_steel` (2.1%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.7%) | `stainless_steel_generic` (2.3%) | `platinum_plate` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (81.3%) | `divided` (15.9%) | `ABSENT` (2.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (83.7%) | `Li` (8.9%) | `NEt4` (4.2%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (33.0%) | `ClO4` (29.5%) | `Cl` (16.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (14.7%) | `alkali_carbonate` (10.1%) | `as_solvent_polar_aprotic_sulfo` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (90.9%) | `organic_neutral_cat` (3.7%) | `Co_complex` (3.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (97.3%) | `cyclic_ether` (1.0%) | `halogenated_aliphatic` (0.8%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (100%) | `O` (3%) | `ClCCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `Cl` (30%) | `O=C(O)O.[Na]` (21%) | `O=C(O)O.[K]` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✗ / any ✗ |

---

### Reaction #348  yield=31.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #13)

```
CCOC(=O)CC(=O)OCC.C=CCCCOC(=O)[C@@H](C)c1ccc2cc(OC)ccc2c1>>CCOC(=O)C1(C(=O)OCC)C[C@H]1CCCOC(=O)[C@@H](C)c1ccc2cc(OC)c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (59.4%) | `graphite_generic` (38.0%) | `carbon_felt` (0.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.9%) | `stainless_steel` (2.1%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.7%) | `stainless_steel_generic` (2.3%) | `platinum_plate` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (81.3%) | `divided` (15.9%) | `ABSENT` (2.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (83.7%) | `Li` (8.9%) | `NEt4` (4.2%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (33.0%) | `ClO4` (29.5%) | `Cl` (16.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (14.7%) | `alkali_carbonate` (10.1%) | `as_solvent_polar_aprotic_sulfo` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (90.9%) | `organic_neutral_cat` (3.7%) | `Co_complex` (3.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (97.3%) | `cyclic_ether` (1.0%) | `halogenated_aliphatic` (0.8%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (100%) | `O` (3%) | `ClCCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `Cl` (30%) | `O=C(O)O.[Na]` (21%) | `O=C(O)O.[K]` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✗ / any ✗ |

---

### Reaction #349  yield=47.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #14)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccc(-c2ccccc2)cc1>>CCOC(=O)C(CC(I)CCCOc1ccc(-c2ccccc2)cc1)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (81.2%) | `sacrificial_zinc` (11.1%) | `sacrificial_aluminum` (3.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (42.0%) | `zinc_plate` (20.1%) | `carbon_felt` (15.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (69.1%) | `carbon` (29.3%) | `nickel` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (60.5%) | `carbon_felt` (15.2%) | `nickel_foam` (13.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `divided` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (86.6%) | `NBu4` (12.4%) | `Na` (0.8%) | ✗ |
| 电解质 anion | 26 | `I` | `ClO4` (71.9%) | `I` (14.3%) | `molecular_no_ion` (8.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (8.5%) | `ABSENT` (7.2%) | `alkali_carbonate` (4.1%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (75.9%) | `Co_complex` (6.5%) | `Fe_complex` (4.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `ketone` (47.9%) | `polar_aprotic_amide` (27.3%) | `polar_aprotic_nitrile` (6.8%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC(C)=O` (86%) | `CC#N` (5%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `[I-].[Na+]` (9%) | `O` (7%) | `O=C(O)C(F)(F)F` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (95%) | `COCCOC.[Br][Ni][Br` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✗ / any ✗ |

---

### Reaction #350  yield=42.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #15)

```
CCOC(=O)CC(=O)OCC.C=CCCCCCCCOc1ccc(-c2ccccc2)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCCCCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.8%) | `sacrificial_zinc` (1.3%) | `platinum` (1.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (77.7%) | `carbon_generic` (15.2%) | `unknown_electrode` (2.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.9%) | `nickel` (3.5%) | `carbon` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (94.8%) | `nickel_foam` (4.5%) | `platinum_wire` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (90.9%) | `divided` (7.7%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (76.0%) | `Li` (14.3%) | `NEt4` (3.9%) | ✓ |
| 电解质 anion | 26 | `I` | `ClO4` (27.9%) | `I` (25.6%) | `PF6` (21.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (8.9%) | `alkali_carbonate` (6.7%) | `ABSENT` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (35.0%) | `Co_complex` (25.4%) | `ABSENT` (11.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (42.2%) | `polar_aprotic_nitrile` (34.8%) | `tfe` (11.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (48%) | `CN(C)C=O` (16%) | `CC(=O)O` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (28%) | `CC(C)(C)C(=O)[O-].` (17%) | `CC(=O)O` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `CC(C)(C)c1cccc(C2=` (3%) | `CC(=O)[CH-]C(C)=O.` (2%) | `O=S(=O)(O)O` (1%) | set ✗ / any ✗ |

---

### Reaction #351  yield=48.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #16)

```
CCOC(=O)CC(=O)OCC.C=CCCCCCCCCCC>>CCCCCCCCCCC1CC1(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (3.6%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (33.5%) | `reticulated_vitreous_carbon` (33.4%) | `carbon_cloth` (13.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (57.2%) | `carbon` (14.8%) | `stainless_steel` (14.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (86.1%) | `nickel_foam` (2.2%) | `stainless_steel_wire` (2.0%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (77.0%) | `undivided` (16.0%) | `ABSENT` (7.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (79.0%) | `Na` (5.4%) | `Li` (5.4%) | ✗ |
| 电解质 anion | 26 | `I` | `PF6` (30.9%) | `BF4` (19.8%) | `I` (11.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (13.6%) | `carboxylic_acid` (13.4%) | `ABSENT` (4.5%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (21.9%) | `Co_complex` (19.6%) | `ABSENT` (16.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (79.0%) | `halogenated_aliphatic` (3.6%) | `tfe` (3.0%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (98%) | `O` (3%) | `CC(=O)O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (84%) | `O=C([O-])[O-].[Na+` (12%) | `O=S([O-])([O-])=S.` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)C(F)(F)F` (5%) | `CC(C)(C)c1cccc(C2=` (4%) | `O=S(=O)(O)O` (3%) | set ✗ / any ✗ |

---

### Reaction #352  yield=55.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #17)

```
CCOC(=O)CC#N.C=Cc1ccc(-c2ccccc2)cc1>>CCOC(=O)[C@@]1(C#N)C[C@@H]1c1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `sacrificial_iron` (0.7%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (99.7%) | `graphite_generic` (0.1%) | `unknown_electrode` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.9%) | `carbon` (3.5%) | `nickel` (2.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (56.7%) | `platinum_plate` (14.5%) | `platinum_wire` (13.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (95.0%) | `ABSENT` (4.3%) | `divided` (0.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Cs` | `NBu4` (85.2%) | `NEt4` (7.6%) | `Li` (4.3%) | ✗ |
| 电解质 anion | 26 | `carboxylate` | `BF4` (67.9%) | `PF6` (7.6%) | `ClO4` (7.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.2%) | `alkali_other_salt` (2.8%) | `primary_amine` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `thianthrene_phenothiazine_cat` (66.6%) | `ABSENT` (14.8%) | `organic_neutral_cat` (6.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (45.4%) | `tfe` (29.3%) | `ABSENT` (9.3%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (94%) | `CN(C)C=O` (5%) | `COC(C)(C)C` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Cs+]` | `__ABSENT__` (100%) | `O` (0%) | `O=C([O-])[O-].[Cs+` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `COc1ccc2c(c1)Sc1cc` (48%) | `__ABSENT__` (29%) | `COc1ccc2c(c1)Sc1cc` (2%) | set ✗ / any ✗ |

---

### Reaction #353  yield=51.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #18)

```
CCOC(=O)CC(=O)OCC.C=CCCCOC(=O)C(C)c1ccc(CC2CCCC2=O)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOC(=O)C(C)c1ccc(CC2CCCC2=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.2%) | `platinum` (9.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `platinum_generic` (54.6%) | `carbon_generic` (29.8%) | `graphite_generic` (9.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (77.4%) | `stainless_steel` (15.8%) | `nickel` (3.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (95.9%) | `stainless_steel_generic` (3.1%) | `platinum_wire` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (49.1%) | `ABSENT` (27.2%) | `undivided` (23.7%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (96.9%) | `Li` (1.8%) | `NEt4` (0.7%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (64.4%) | `ClO4` (20.3%) | `PF6` (7.0%) | ✗ |
| 试剂大类 | 103 | `iodide_anion` | `alkali_carbonate` (17.2%) | `alkali_other_salt` (4.6%) | `tertiary_amine` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (88.6%) | `organic_neutral_cat` (5.1%) | `Co_complex` (2.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (90.2%) | `cyclic_ether` (4.1%) | `polar_aprotic_amide` (2.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (99%) | `O` (1%) | `CC(=O)OC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[N+](CC)(CC)CC.[` | `O=C([O-])[O-].[K+]` (92%) | `O=C([O-])[O-].[Na+` (7%) | `CCN(CC)CC` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC1(C)O[C@@H](c2cc` (0%) | set ✗ / any ✓ |

---

### Reaction #354  yield=58.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #19)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccc(C(F)(F)F)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(C(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (91.9%) | `platinum` (3.9%) | `ABSENT` (3.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `unknown_electrode` (54.7%) | `reticulated_vitreous_carbon` (34.8%) | `carbon_generic` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.6%) | `nickel` (4.9%) | `stainless_steel` (3.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (95.0%) | `nickel_foam` (4.1%) | `carbon_felt` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (42.4%) | `divided` (41.6%) | `ABSENT` (16.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (82.5%) | `ABSENT` (7.3%) | `NEt4` (5.1%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (34.5%) | `PF6` (22.4%) | `ClO4` (13.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (10.1%) | `carboxylic_acid` (6.7%) | `alkali_other_salt` (5.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (50.8%) | `ABSENT` (29.0%) | `organic_neutral_cat` (9.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (62.7%) | `polar_aprotic_amide` (11.0%) | `tfe` (6.6%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (99%) | `O` (12%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (80%) | `O=C([O-])[O-].[Na+` (5%) | `O=C([O-])[O-].[Cs+` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `CC(=O)[CH-]C(C)=O.` (4%) | `CC1[CH-]C(C)=[O]->` (3%) | `CC(C)(C)c1ccc2[O-]` (2%) | set ✗ / any ✗ |

---

### Reaction #355  yield=55.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #20)

```
CCOC(=O)CC(=O)OCC.C=CCCCCCCCC>>CCCCCCCCC1CC1(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (3.6%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (33.5%) | `reticulated_vitreous_carbon` (33.4%) | `carbon_cloth` (13.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (57.2%) | `carbon` (14.8%) | `stainless_steel` (14.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (86.1%) | `nickel_foam` (2.2%) | `stainless_steel_wire` (2.0%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (77.0%) | `undivided` (16.0%) | `ABSENT` (7.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (79.0%) | `Na` (5.4%) | `Li` (5.4%) | ✗ |
| 电解质 anion | 26 | `I` | `PF6` (30.9%) | `BF4` (19.8%) | `I` (11.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (13.6%) | `carboxylic_acid` (13.4%) | `ABSENT` (4.5%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (21.9%) | `Co_complex` (19.6%) | `ABSENT` (16.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (79.0%) | `halogenated_aliphatic` (3.6%) | `tfe` (3.0%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (98%) | `O` (3%) | `CC(=O)O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (84%) | `O=C([O-])[O-].[Na+` (12%) | `O=S([O-])([O-])=S.` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)C(F)(F)F` (5%) | `CC(C)(C)c1cccc(C2=` (4%) | `O=S(=O)(O)O` (3%) | set ✗ / any ✗ |

---

### Reaction #356  yield=51.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #21)

```
CCOC(=O)CC(=O)OCC.C=CCCCOC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12>>CCOC(=O)C1(C(=O)OCC)CC1CCCOC(=O)Cc1c(C)n(C(=O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (37.5%) | `carbon_felt` (32.4%) | `carbon_generic` (20.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `nickel` (0.3%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.0%) | `platinum_plate` (1.8%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `divided` (89.4%) | `undivided` (10.5%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (99.8%) | `Li` (0.1%) | `ABSENT` (0.1%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (86.7%) | `ClO4` (5.5%) | `I` (3.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (48.5%) | `as_solvent_polar_aprotic_sulfo` (4.0%) | `as_solvent_cyclic_ether` (1.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (90.9%) | `Co_complex` (8.1%) | `organic_neutral_cat` (0.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `ABSENT` (62.5%) | `halogenated_aliphatic` (21.6%) | `polar_aprotic_nitrile` (5.7%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `__ABSENT__` (99%) | `CC(=O)O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (52%) | `O=C([O-])[O-].[K+]` (13%) | `CC(C)(C)C(=O)[O-].` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✓ |

---

### Reaction #357  yield=53.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #22)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccc(C#N)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(C#N)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (85.3%) | `platinum` (7.7%) | `ABSENT` (5.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (69.9%) | `unknown_electrode` (22.3%) | `carbon_generic` (3.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (78.8%) | `carbon` (12.5%) | `stainless_steel` (4.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.7%) | `nickel_foam` (1.7%) | `carbon_felt` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (63.8%) | `undivided` (27.1%) | `ABSENT` (9.1%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (66.4%) | `Li` (12.6%) | `ABSENT` (10.1%) | ✗ |
| 电解质 anion | 26 | `I` | `I` (28.5%) | `ClO4` (25.2%) | `Cl` (12.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (11.1%) | `carboxylic_acid` (10.6%) | `alkali_carbonate` (9.7%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (52.5%) | `ABSENT` (20.7%) | `organic_neutral_cat` (17.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (68.6%) | `polar_aprotic_amide` (12.8%) | `tfe` (3.8%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (98%) | `O` (2%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(C)(C)C(=O)O.[Na` (20%) | `O=C(O)O.[K]` (7%) | `O=C(O)C(F)(F)F` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `CC(C)(C)c1ccc2[O-]` (10%) | `[O-]1c2cc(cc2C=[N+` (9%) | `CC1[CH-]C(C)=[O]->` (4%) | set ✗ / any ✗ |

---

### Reaction #358  yield=53.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #23)

```
CCOC(=O)CC(=O)OCC.C=CCCCCCCOc1ccc(-c2ccccc2)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCCCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.8%) | `sacrificial_zinc` (1.3%) | `platinum` (1.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (77.7%) | `carbon_generic` (15.2%) | `unknown_electrode` (2.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.9%) | `nickel` (3.5%) | `carbon` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (94.8%) | `nickel_foam` (4.5%) | `platinum_wire` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (90.9%) | `divided` (7.7%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (76.0%) | `Li` (14.3%) | `NEt4` (3.9%) | ✓ |
| 电解质 anion | 26 | `I` | `ClO4` (27.9%) | `I` (25.6%) | `PF6` (21.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (8.9%) | `alkali_carbonate` (6.7%) | `ABSENT` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (35.0%) | `Co_complex` (25.4%) | `ABSENT` (11.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (42.2%) | `polar_aprotic_nitrile` (34.8%) | `tfe` (11.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (48%) | `CN(C)C=O` (16%) | `CC(=O)O` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (28%) | `CC(C)(C)C(=O)[O-].` (17%) | `CC(=O)O` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `CC(C)(C)c1cccc(C2=` (3%) | `CC(=O)[CH-]C(C)=O.` (2%) | `O=S(=O)(O)O` (1%) | set ✗ / any ✗ |

---

### Reaction #359  yield=69.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #24)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccc2ccccc2c1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc2ccccc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (91.8%) | `platinum` (3.0%) | `ABSENT` (2.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (69.6%) | `unknown_electrode` (15.9%) | `carbon_generic` (9.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.9%) | `nickel` (6.6%) | `carbon` (4.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (84.0%) | `nickel_foam` (14.6%) | `platinum_wire` (0.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (47.7%) | `ABSENT` (33.5%) | `divided` (18.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (87.8%) | `Li` (3.9%) | `ABSENT` (3.1%) | ✗ |
| 电解质 anion | 26 | `I` | `I` (25.1%) | `PF6` (20.1%) | `BF4` (19.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (13.3%) | `alkali_other_salt` (8.0%) | `carboxylic_acid` (4.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (56.3%) | `organic_neutral_cat` (20.5%) | `ABSENT` (9.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (52.6%) | `polar_aprotic_amide` (12.1%) | `tfe` (10.3%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (95%) | `O` (8%) | `CC(=O)O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (77%) | `O=C([O-])[O-].[Cs+` (2%) | `O=C([O-])[O-].[Na+` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `CC(=O)[CH-]C(C)=O.` (7%) | `CC(=O)[O-].CC(=O)[` (3%) | `[O-]1c2cc(cc2C=[N+` (1%) | set ✗ / any ✗ |

---

### Reaction #360  yield=66.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #25)

```
CCOC(=O)CC(=O)OCC.C=CCCCOC(=O)C(C)(C)Oc1ccc(CCNC(=O)c2ccc(Cl)cc2)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOC(=O)C(C)(C)Oc1ccc(C…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `carbon_felt` (86.4%) | `reticulated_vitreous_carbon` (9.5%) | `carbon_generic` (3.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.8%) | `nickel` (0.8%) | `carbon` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `graphite_felt` | `platinum_generic` (68.9%) | `platinum_plate` (27.3%) | `nickel_foam` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (52.8%) | `ABSENT` (44.7%) | `divided` (2.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (97.5%) | `Li` (1.3%) | `ABSENT` (0.7%) | ✗ |
| 电解质 anion | 26 | `I` | `ClO4` (38.1%) | `BF4` (36.4%) | `I` (14.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (8.3%) | `ABSENT` (5.9%) | `alkali_other_salt` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (75.6%) | `Co_complex` (7.6%) | `organic_neutral_cat` (6.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (84.9%) | `cyclic_ether` (6.5%) | `polar_protic_alcohol` (3.9%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (94%) | `CO` (1%) | `C1CCOC1` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (55%) | `__ABSENT__` (6%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #361  yield=66.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #26)

```
CCOC(=O)CC(=O)OCC.C=CCCCCC>>CCCCCC1CC1(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.6%) | `platinum` (4.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (41.4%) | `carbon_generic` (38.1%) | `pencil_graphite` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (60.8%) | `stainless_steel` (16.1%) | `nickel` (14.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (87.7%) | `nickel_foam` (4.2%) | `stainless_steel_wire` (1.8%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (74.5%) | `undivided` (19.1%) | `ABSENT` (6.4%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (90.6%) | `ABSENT` (3.6%) | `Na` (1.8%) | ✗ |
| 电解质 anion | 26 | `I` | `PF6` (33.9%) | `BF4` (26.7%) | `I` (11.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (19.6%) | `carboxylic_acid` (12.1%) | `ABSENT` (3.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (26.5%) | `organic_neutral_cat` (18.9%) | `ABSENT` (14.6%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (70.7%) | `polar_aprotic_amide` (7.4%) | `tfe` (6.8%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (99%) | `O` (2%) | `CC(=O)O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (86%) | `O=C([O-])[O-].[Na+` (19%) | `O=C([O-])[O-].[Cs+` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[O-]1c2cc(cc2C=[N+` (4%) | `CC(C)(C)c1ccc2[O-]` (3%) | `CC(=O)[CH-]C(C)=O.` (3%) | set ✗ / any ✗ |

---

### Reaction #362  yield=63.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #27)

```
CCOC(=O)CC(=O)OCC.C=CCCCOC(=O)c1cc2ccccc2s1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOC(=O)c1cc2ccccc2s1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `ABSENT` (0.4%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (91.0%) | `unknown_electrode` (4.9%) | `carbon_generic` (3.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.4%) | `nickel` (5.9%) | `stainless_steel` (4.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (57.3%) | `nickel_foam` (29.8%) | `platinum_wire` (4.2%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (41.9%) | `undivided` (38.7%) | `divided` (19.3%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (95.4%) | `ABSENT` (3.8%) | `NEt4` (0.4%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (64.6%) | `PF6` (17.3%) | `ABSENT` (12.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (33.6%) | `alkali_other_salt` (11.9%) | `carboxylic_acid` (3.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (41.2%) | `ABSENT` (32.6%) | `organic_neutral_cat` (11.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (78.1%) | `polar_protic_alcohol` (5.4%) | `polar_aprotic_amide` (4.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (96%) | `ClCCCl` (5%) | `OCC(F)(F)F` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (72%) | `O=C([O-])[O-].[Na+` (15%) | `O=C([O-])[O-].[Cs+` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `CC(C)(C)c1ccc2[O-]` (25%) | `[O-]1c2cc(cc2C=[N+` (14%) | `__ABSENT__` (10%) | set ✗ / any ✗ |

---

### Reaction #363  yield=69.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #28)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccc(C(=O)OC)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(C(=O)OC)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.5%) | `platinum` (8.9%) | `sacrificial_zinc` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (94.9%) | `carbon_generic` (3.3%) | `platinum_generic` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (57.6%) | `nickel` (29.7%) | `carbon` (12.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (57.8%) | `platinum_generic` (39.9%) | `carbon_felt` (0.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (48.6%) | `divided` (38.7%) | `ABSENT` (12.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (94.7%) | `Li` (2.7%) | `Na` (1.3%) | ✗ |
| 电解质 anion | 26 | `I` | `I` (29.6%) | `PF6` (26.6%) | `BF4` (16.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (13.0%) | `alkali_carbonate` (6.6%) | `ABSENT` (3.3%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (51.9%) | `Co_complex` (32.3%) | `Ni_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (56.4%) | `polar_aprotic_amide` (13.4%) | `cyclic_ether` (8.5%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (85%) | `O` (39%) | `CC(=O)O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Cs+` (26%) | `O=C(O)C(F)(F)F` (13%) | `CC(=O)O` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (91%) | `[Br][Mn][Br]` (1%) | `[Cl-].[Cl-].[Ni+2]` (1%) | set ✗ / any ✗ |

---

### Reaction #364  yield=68.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #29)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccc(F)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.7%) | `platinum` (2.5%) | `ABSENT` (2.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (85.3%) | `carbon_generic` (9.9%) | `unknown_electrode` (2.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.3%) | `nickel` (6.5%) | `stainless_steel` (5.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.5%) | `nickel_foam` (1.0%) | `stainless_steel_generic` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (58.6%) | `divided` (31.4%) | `ABSENT` (10.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (90.3%) | `NEt4` (4.2%) | `Na` (2.4%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (37.5%) | `I` (28.4%) | `carboxylate` (6.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (8.4%) | `alkali_carbonate` (8.2%) | `alkali_other_salt` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (47.9%) | `Co_complex` (21.6%) | `organic_neutral_cat` (14.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (43.3%) | `halogenated_aliphatic` (19.0%) | `polar_aprotic_amide` (11.7%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (97%) | `O` (55%) | `CC(=O)O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (18%) | `O=C([O-])[O-].[Cs+` (4%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (93%) | `[Pt]` (0%) | `[Cl-].[Cl-].[Ni+2]` (0%) | set ✗ / any ✗ |

---

### Reaction #365  yield=62.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #30)

```
CCOC(=O)CC#N.C=CCCCOc1ccc(-c2ccccc2)cc1>>CCOC(=O)[C@]1(C#N)C[C@H]1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.8%) | `sacrificial_iron` (6.0%) | `sacrificial_zinc` (5.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (97.8%) | `carbon_generic` (0.9%) | `unknown_electrode` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (74.5%) | `nickel` (23.8%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (73.9%) | `platinum_generic` (24.3%) | `platinum_wire` (1.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.0%) | `divided` (10.9%) | `ABSENT` (3.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (91.9%) | `NEt4` (3.6%) | `Li` (2.2%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (49.0%) | `PF6` (23.4%) | `I` (15.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.1%) | `carboxylic_acid` (5.8%) | `primary_amine` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `thianthrene_phenothiazine_cat` (45.4%) | `ABSENT` (18.0%) | `organic_neutral_cat` (14.9%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (79.2%) | `tfe` (8.6%) | `polar_aprotic_nitrile` (7.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CN(C)C=O` (52%) | `CC#N` (37%) | `O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[Na+` | `__ABSENT__` (99%) | `O` (1%) | `O=C(O)C(F)(F)F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `COc1ccc2c(c1)Sc1cc` (8%) | `COc1ccc2c(c1)Sc1cc` (1%) | `__ABSENT__` (1%) | set ✗ / any ✗ |

---

### Reaction #366  yield=65.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #31)

```
CCOC(=O)CC(=O)OCC.C=CC1CCCCC1>>CCOC(=O)C1(C(=O)OCC)CC1C1CCCCC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (66.8%) | `reticulated_vitreous_carbon` (21.8%) | `carbon_cloth` (6.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.4%) | `nickel` (6.1%) | `stainless_steel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (84.8%) | `platinum_plate` (12.2%) | `nickel_foam` (2.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (68.8%) | `ABSENT` (19.9%) | `divided` (11.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (97.4%) | `ABSENT` (2.3%) | `Li` (0.2%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (91.9%) | `ABSENT` (4.3%) | `PF6` (1.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (15.7%) | `alkali_carbonate` (13.3%) | `alkali_carboxylate` (5.6%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (54.6%) | `Co_complex` (31.0%) | `pyridine_organocat` (4.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_alcohol` (41.1%) | `polar_aprotic_nitrile` (36.5%) | `polar_aprotic_amide` (6.5%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CO` (45%) | `CC#N` (37%) | `CCO` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (45%) | `CC(=O)O` (12%) | `CC(=O)[O-].[Na+]` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |

---

### Reaction #367  yield=67.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #32)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccccc1-c1ccccc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccccc1-c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.8%) | `platinum` (2.9%) | `sacrificial_iron` (1.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (97.4%) | `unknown_electrode` (1.0%) | `iron_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (68.4%) | `nickel` (18.0%) | `stainless_steel` (9.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (61.8%) | `platinum_generic` (35.4%) | `stainless_steel_generic` (0.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (85.5%) | `divided` (10.8%) | `ABSENT` (3.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (93.3%) | `NEt4` (3.3%) | `ABSENT` (1.8%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (34.3%) | `PF6` (20.9%) | `I` (14.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (18.9%) | `alkali_other_salt` (7.1%) | `ABSENT` (2.9%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (42.5%) | `Co_complex` (17.9%) | `ABSENT` (15.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (44.0%) | `polar_aprotic_amide` (26.5%) | `tfe` (11.3%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (96%) | `ClCCCl` (20%) | `CC(=O)O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (47%) | `O=C([O-])[O-].[Cs+` (7%) | `O=C([O-])[O-].[Na+` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `O=S(=O)(O)O` (11%) | `[O-]1c2cc(cc2C=[N+` (4%) | `CC(C)(C)c1cccc(C2=` (2%) | set ✗ / any ✗ |

---

### Reaction #368  yield=67.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #33)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccc2c(c1)OCO2>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc2c(c1)OCO2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.5%) | `platinum` (5.4%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (50.4%) | `unknown_electrode` (22.2%) | `reticulated_vitreous_carbon` (19.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.4%) | `nickel` (3.7%) | `carbon` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.8%) | `nickel_foam` (0.8%) | `stainless_steel_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (59.4%) | `divided` (29.6%) | `undivided` (10.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (71.2%) | `ABSENT` (24.0%) | `Na` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `SO4` | `ABSENT` (31.2%) | `BF4` (22.4%) | `I` (21.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (10.5%) | `carboxylic_acid` (9.4%) | `alkali_other_salt` (3.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (52.2%) | `organic_neutral_cat` (16.6%) | `Co_complex` (12.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (37.4%) | `cyclic_ether` (28.6%) | `polar_aprotic_amide` (14.9%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (74%) | `O` (6%) | `CO` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (75%) | `O=C([O-])[O-].[Na+` (6%) | `O=C([O-])[O-].[Cs+` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Fe+2].c1cc[cH-]c1` (1%) | `[Cl-].[Cl-].[Ni+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #369  yield=61.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #34)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccc(Br)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.5%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (65.5%) | `carbon_generic` (25.4%) | `unknown_electrode` (4.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (79.8%) | `nickel` (9.9%) | `carbon` (8.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (78.8%) | `nickel_foam` (14.9%) | `platinum_wire` (4.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (45.7%) | `ABSENT` (27.9%) | `divided` (26.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (96.1%) | `Li` (1.4%) | `ABSENT` (1.3%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (33.3%) | `I` (20.2%) | `PF6` (13.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (8.8%) | `carboxylic_acid` (8.1%) | `alkali_carbonate` (7.0%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (42.7%) | `ABSENT` (42.0%) | `organic_neutral_cat` (6.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (64.8%) | `polar_aprotic_amide` (8.8%) | `polar_protic_alcohol` (7.0%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (96%) | `O` (33%) | `CC(=O)O` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(C)(C)C(=O)O.[Na` (16%) | `O=C(O)O.[K]` (6%) | `CS(C)=O` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `CC(=O)[CH-]C(C)=O.` (3%) | `[O-]1c2cc(cc2C=[N+` (2%) | `CC(C)(C)c1ccc2[O-]` (2%) | set ✗ / any ✗ |

---

### Reaction #370  yield=61.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #35)

```
CCOC(=O)CC(=O)OCC.C=CCCCCCC>>CCCCCCC1CC1(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (3.6%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (33.5%) | `reticulated_vitreous_carbon` (33.4%) | `carbon_cloth` (13.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (57.2%) | `carbon` (14.8%) | `stainless_steel` (14.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (86.1%) | `nickel_foam` (2.2%) | `stainless_steel_wire` (2.0%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (77.0%) | `undivided` (16.0%) | `ABSENT` (7.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (79.0%) | `Na` (5.4%) | `Li` (5.4%) | ✗ |
| 电解质 anion | 26 | `I` | `PF6` (30.9%) | `BF4` (19.8%) | `I` (11.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (13.6%) | `carboxylic_acid` (13.4%) | `ABSENT` (4.5%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (21.9%) | `Co_complex` (19.6%) | `ABSENT` (16.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (79.0%) | `halogenated_aliphatic` (3.6%) | `tfe` (3.0%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (98%) | `O` (3%) | `CC(=O)O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (84%) | `O=C([O-])[O-].[Na+` (12%) | `O=S([O-])([O-])=S.` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `O=S(=O)(O)C(F)(F)F` (5%) | `CC(C)(C)c1cccc(C2=` (4%) | `O=S(=O)(O)O` (3%) | set ✗ / any ✗ |

---

### Reaction #371  yield=64.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #36)

```
CCOC(=O)CC(=O)OCC.C=CCCC>>CCCC1CC1(C(=O)OCC)C(=O)OCC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.5%) | `platinum` (1.1%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (65.0%) | `unknown_electrode` (15.7%) | `carbon_generic` (12.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.2%) | `nickel` (7.3%) | `stainless_steel` (5.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (81.9%) | `nickel_foam` (16.2%) | `platinum_plate` (0.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (51.3%) | `ABSENT` (34.2%) | `divided` (14.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (89.1%) | `ABSENT` (8.6%) | `Li` (0.9%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (50.4%) | `ABSENT` (18.6%) | `Cl` (8.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (40.4%) | `alkali_other_salt` (5.1%) | `tertiary_amine` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (33.8%) | `ABSENT` (28.5%) | `organic_neutral_cat` (17.6%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (41.9%) | `tfe` (15.6%) | `ketone` (11.9%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (94%) | `ClCCCl` (6%) | `CC(=O)O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (76%) | `O=C([O-])[O-].[Na+` (9%) | `O=C([O-])[O-].[Cs+` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[O-]1c2cc(cc2C=[N+` (11%) | `CC(C)(C)c1ccc2[O-]` (11%) | `CC1[CH-]C(C)=[O]->` (5%) | set ✗ / any ✗ |

---

### Reaction #372  yield=66.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #37)

```
CCOC(=O)CC(=O)OCC.C=CCCCCCCCCCC(=O)OC>>CCOC(=O)C1(C(=O)OCC)CC1CCCCCCCCCC(=O)OC
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (1.0%) | `sacrificial_magnesium` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (98.1%) | `carbon_generic` (0.9%) | `carbon_felt` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.3%) | `carbon` (14.0%) | `stainless_steel` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (84.9%) | `platinum_foil` (10.4%) | `carbon_generic` (1.0%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (95.8%) | `undivided` (2.1%) | `ABSENT` (2.1%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (60.7%) | `Li` (29.8%) | `NEt4` (4.6%) | ✓ |
| 电解质 anion | 26 | `I` | `ClO4` (74.1%) | `PF6` (10.9%) | `BF4` (8.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (30.1%) | `alkali_carbonate` (5.0%) | `tertiary_amine` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (29.1%) | `organic_neutral_cat` (23.9%) | `brønsted_acid_cat` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (77.4%) | `polar_aprotic_amide` (18.2%) | `cyclic_ether` (1.2%) | ✗ |
| 溶剂 set | 79 | `O` | `CC#N` (98%) | `O` (22%) | `CN(C)C=O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (42%) | `OC(C(F)(F)F)C(F)(F` (23%) | `BrCCBr` (18%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (54%) | `CC(=O)NC1CC2(CCCCC` (41%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #373  yield=63.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #38)

```
CCOC(=O)CC(=O)OCC.C=CCCCCCCCCCCl>>CCOC(=O)C1(C(=O)OCC)CC1CCCCCCCCCCl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.5%) | `platinum` (5.4%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (90.6%) | `carbon_generic` (5.5%) | `platinum_generic` (1.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.8%) | `nickel` (5.9%) | `carbon` (2.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (93.7%) | `nickel_foam` (5.3%) | `platinum_wire` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `divided` (59.6%) | `undivided` (38.6%) | `ABSENT` (1.8%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (79.4%) | `Li` (12.4%) | `Na` (3.8%) | ✗ |
| 电解质 anion | 26 | `I` | `Cl` (47.3%) | `ClO4` (18.4%) | `PF6` (11.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (13.5%) | `carboxylic_acid` (9.4%) | `ABSENT` (9.1%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (78.5%) | `organic_neutral_cat` (9.8%) | `ionic_organocat` (3.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (65.6%) | `tfe` (20.5%) | `polar_aprotic_amide` (6.0%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (96%) | `CC(=O)O` (13%) | `ClCCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (66%) | `O=C([O-])[O-].[Na+` (33%) | `O=C([O-])[O-].[Cs+` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[O-]1c2cc(cc2C=[N+` (43%) | `CC(C)(C)c1ccc2[O-]` (12%) | `CC(=O)[O-].CC(=O)[` (3%) | set ✗ / any ✗ |

---

### Reaction #374  yield=61.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #39)

```
N#CCC#N.C=CCCCOc1ccc(-c2ccccc2)cc1>>N#CC1(C#N)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.5%) | `sacrificial_zinc` (6.3%) | `sacrificial_iron` (1.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `pencil_graphite` (56.9%) | `reticulated_vitreous_carbon` (39.1%) | `carbon_generic` (1.9%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_zinc` | `platinum` (65.3%) | `nickel` (32.9%) | `carbon` (1.2%) | ✗ |
| 阴极 (细类) | 49 | `zinc_plate` | `nickel_foam` (56.2%) | `nickel_wire` (32.7%) | `platinum_wire` (8.0%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (98.0%) | `undivided` (1.6%) | `ABSENT` (0.3%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `ABSENT` (68.2%) | `Li` (16.6%) | `NBu4` (9.0%) | ✗ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (56.3%) | `I` (15.4%) | `molecular_no_ion` (11.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (47.1%) | `ABSENT` (4.7%) | `iodide_anion` (2.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (42.9%) | `thianthrene_phenothiazine_cat` (21.3%) | `pyridine_organocat` (9.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (74.3%) | `polar_aprotic_nitrile` (17.8%) | `ABSENT` (4.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CN(C)C=O` (57%) | `CC#N` (32%) | `CC(=O)N(C)C` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)[O-].[Cs+]` | `O=C(O)C(F)(F)F` (99%) | `O=C([O-])[O-].[Cs+` (82%) | `c1ccc2c(c1)Sc1cccc` (38%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `F[P-](F)(F)(F)(F)F` | `__ABSENT__` (82%) | `[Br-].[Br-].[Mn+2]` (2%) | `CC#N.CC(c1ccccn1)(` (2%) | set ✗ / any ✗ |

---

### Reaction #375  yield=66.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #40)

```
CCOC(=O)CC(=O)OCC.C=CCCCOC(=O)CCc1nc(-c2ccccc2)c(-c2ccccc2)o1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOC(=O)CCc1nc(-c2ccccc2)c(-c2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (82.1%) | `platinum` (9.9%) | `ABSENT` (3.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `unknown_electrode` (59.0%) | `reticulated_vitreous_carbon` (29.6%) | `carbon_generic` (6.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.8%) | `carbon` (11.6%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.9%) | `reticulated_vitreous_carbon` (2.4%) | `nickel_foam` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (56.2%) | `undivided` (39.1%) | `divided` (4.7%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `ABSENT` (53.1%) | `Li` (14.0%) | `molecular_no_ion` (9.7%) | ✗ |
| 电解质 anion | 26 | `I` | `Cl` (41.7%) | `I` (25.1%) | `ABSENT` (13.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (17.0%) | `alkali_other_salt` (5.5%) | `ABSENT` (3.1%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (46.9%) | `ABSENT` (17.5%) | `organic_neutral_cat` (13.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (90.1%) | `cyclic_ether` (4.1%) | `polar_aprotic_amide` (1.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (95%) | `O` (23%) | `CC(C)=O` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (71%) | `O=C([O-])[O-].[K+]` (2%) | `O=C(O)O.[Na]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `CC(C)(C)c1ccc2[O-]` (9%) | `CC1[CH-]C(C)=[O]->` (6%) | `[O-]1c2cc(cc2C=[N+` (4%) | set ✗ / any ✗ |

---

### Reaction #376  yield=70.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #41)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccc(Cl)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.9%) | `platinum` (3.3%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (79.8%) | `carbon_generic` (12.9%) | `carbon_felt` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.6%) | `stainless_steel` (1.7%) | `carbon` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (97.3%) | `nickel_foam` (1.0%) | `platinum_plate` (0.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (52.4%) | `divided` (34.9%) | `ABSENT` (12.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (92.4%) | `ABSENT` (3.8%) | `Li` (1.7%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (37.7%) | `ClO4` (19.3%) | `ABSENT` (11.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (12.4%) | `alkali_other_salt` (9.6%) | `carboxylic_acid` (3.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (36.2%) | `Co_complex` (35.8%) | `organic_neutral_cat` (11.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (65.7%) | `polar_aprotic_amide` (9.7%) | `polar_protic_alcohol` (6.0%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (97%) | `O` (8%) | `CC(=O)O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (23%) | `O=C([O-])[O-].[Na+` (13%) | `O=C([O-])[O-].[Cs+` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (93%) | `__OTHER__` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #377  yield=80.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #42)

```
CCOC(=O)CC(=O)OCC.C=CCCCOC(=O)C(C)(C)CCCOc1cc(C)ccc1C>>CCOC(=O)C1(C(=O)OCC)CC1CCCOC(=O)C(C)(C)CCCOc1cc(C)ccc1C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (89.6%) | `sacrificial_zinc` (4.8%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (47.3%) | `carbon_felt` (12.0%) | `carbon_cloth` (9.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (60.6%) | `nickel` (17.3%) | `stainless_steel` (13.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (46.6%) | `platinum_generic` (42.8%) | `stainless_steel_generic` (6.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (89.2%) | `divided` (8.9%) | `ABSENT` (1.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (98.3%) | `ABSENT` (0.9%) | `Li` (0.5%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (45.1%) | `ClO4` (26.2%) | `PF6` (17.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (8.5%) | `hcl` (6.5%) | `carboxylic_acid` (4.7%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (64.6%) | `organic_neutral_cat` (13.3%) | `pyridine_organocat` (10.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (63.3%) | `polar_aprotic_nitrile` (27.9%) | `tfe` (3.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (31%) | `O` (5%) | `CN(C)C=O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (52%) | `O=C([O-])[O-].[Cs+` (3%) | `CCN(CC)CC` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `CC(=O)[CH-]C(C)=O.` (16%) | `[O-]1c2cc(cc2C=[N+` (3%) | `CC1[CH-]C(C)=[O]->` (2%) | set ✗ / any ✗ |

---

### Reaction #378  yield=73.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #43)

```
CCOC(=O)CC(=O)OCC.C=CCCCCCOc1ccc(-c2ccccc2)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.8%) | `sacrificial_zinc` (1.3%) | `platinum` (1.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (77.7%) | `carbon_generic` (15.2%) | `unknown_electrode` (2.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.9%) | `nickel` (3.5%) | `carbon` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (94.8%) | `nickel_foam` (4.5%) | `platinum_wire` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (90.9%) | `divided` (7.7%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (76.0%) | `Li` (14.3%) | `NEt4` (3.9%) | ✓ |
| 电解质 anion | 26 | `I` | `ClO4` (27.9%) | `I` (25.6%) | `PF6` (21.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (8.9%) | `alkali_carbonate` (6.7%) | `ABSENT` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (35.0%) | `Co_complex` (25.4%) | `ABSENT` (11.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (42.2%) | `polar_aprotic_nitrile` (34.8%) | `tfe` (11.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (48%) | `CN(C)C=O` (16%) | `CC(=O)O` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (28%) | `CC(C)(C)C(=O)[O-].` (17%) | `CC(=O)O` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `CC(C)(C)c1cccc(C2=` (3%) | `CC(=O)[CH-]C(C)=O.` (2%) | `O=S(=O)(O)O` (1%) | set ✗ / any ✗ |

---

### Reaction #379  yield=75.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #44)

```
CCOC(=O)CC(=O)OCC.C=CCCC(=O)OCC12CC3CC(CC(C3)C1)C2>>CCOC(=O)C1(C(=O)OCC)CC1CCC(=O)OCC12CC3CC(CC(C3)C1)C2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `platinum` (1.6%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (87.1%) | `reticulated_vitreous_carbon` (4.6%) | `unknown_electrode` (2.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (51.3%) | `nickel` (41.7%) | `carbon` (7.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (51.5%) | `platinum_generic` (45.9%) | `platinum_plate` (0.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (99.5%) | `Li` (0.3%) | `Na` (0.1%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (62.0%) | `carboxylate` (15.9%) | `I` (7.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (23.3%) | `ABSENT` (7.0%) | `as_solvent_halogenated_aliphat` (3.3%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (92.0%) | `Co_complex` (3.9%) | `pyridine_organocat` (1.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (86.9%) | `polar_aprotic_amide` (4.0%) | `ketone` (2.3%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (100%) | `O` (1%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (20%) | `CC(=O)[O-].[Na+]` (15%) | `O=C([O-])[O-].[K+]` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✗ / any ✓ |

---

### Reaction #380  yield=72.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #45)

```
CCOC(=O)CC(=O)OCC.C=CCCC(=O)OC1CCCCCCCCCCC1>>CCOC(=O)C1(C(=O)OCC)CC1CCC(=O)OC1CCCCCCCCCCC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (45.0%) | `carbon_felt` (27.7%) | `reticulated_vitreous_carbon` (23.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (76.1%) | `carbon` (17.1%) | `nickel` (6.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (83.2%) | `nickel_foam` (11.2%) | `platinum_wire` (3.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (89.8%) | `divided` (6.9%) | `ABSENT` (3.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (89.3%) | `ABSENT` (5.9%) | `Li` (4.1%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (54.4%) | `ABSENT` (16.0%) | `ClO4` (14.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (28.0%) | `alkali_other_salt` (5.9%) | `ABSENT` (2.6%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (72.7%) | `Co_complex` (15.5%) | `Fe_complex` (2.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (89.4%) | `polar_protic_alcohol` (4.3%) | `polar_aprotic_amide` (1.4%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (98%) | `O` (0%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (59%) | `CC(=O)[O-].[Na+]` (13%) | `O=C([O-])[O-].[K+]` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✓ |

---

### Reaction #381  yield=77.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #46)

```
CCOC(=O)CC(=O)OCC.C=CCCCOS(=O)(=O)c1ccc(C)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOS(=O)(=O)c1ccc(C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.4%) | `platinum` (5.8%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (96.9%) | `unknown_electrode` (0.9%) | `carbon_generic` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.8%) | `carbon` (7.3%) | `stainless_steel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (92.7%) | `stainless_steel_generic` (2.1%) | `platinum_plate` (1.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (72.7%) | `divided` (22.5%) | `ABSENT` (4.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (51.8%) | `ABSENT` (40.5%) | `NEt4` (5.1%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (46.6%) | `BF4` (35.7%) | `PF6` (8.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (41.2%) | `alkali_carbonate` (16.5%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (52.3%) | `ABSENT` (15.2%) | `organic_neutral_cat` (9.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `halogenated_aliphatic` (26.7%) | `polar_aprotic_nitrile` (26.3%) | `polar_aprotic_amide` (17.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `O` (87%) | `CC#N` (17%) | `CC(=O)O` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(C)(C)C(=O)O.[Na` (56%) | `O=O` (20%) | `CS(C)=O` (18%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `CC1[CH-]C(C)=[O]->` (6%) | `CC(C)(C)c1ccc2[O-]` (6%) | `CC(=O)[CH-]C(C)=O.` (3%) | set ✗ / any ✗ |

---

### Reaction #382  yield=77.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #47)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1cc(Cl)ccc1Oc1ccc(Cl)cc1Cl>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1cc(Cl)ccc1Oc1ccc(Cl)cc1Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.6%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (64.1%) | `carbon_generic` (20.0%) | `carbon_felt` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `stainless_steel` (49.1%) | `platinum` (34.5%) | `nickel` (13.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `stainless_steel_generic` (43.1%) | `nickel_foam` (22.1%) | `platinum_plate` (21.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (96.3%) | `divided` (2.7%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (95.1%) | `ABSENT` (4.3%) | `NEt4` (0.4%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (70.0%) | `ABSENT` (14.9%) | `PF6` (6.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (16.4%) | `alkali_other_salt` (5.1%) | `alkali_carboxylate` (4.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (77.0%) | `organic_neutral_cat` (9.7%) | `Co_complex` (3.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (63.1%) | `polar_aprotic_nitrile` (19.0%) | `halogenated_aliphatic` (8.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (74%) | `CN(C)C=O` (32%) | `O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (60%) | `O=C([O-])[O-].[Na+` (7%) | `CC(=O)[O-].[Na+]` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #383  yield=77.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #48)

```
CCOC(=O)CC(=O)OCC.C=CCOc1ccc(-c2ccccc2)cc1>>CCOC(=O)C1(C(=O)OCC)CC1COc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.5%) | `platinum` (9.9%) | `sacrificial_iron` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (93.4%) | `platinum_wire` (1.1%) | `graphite_felt` (0.9%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.6%) | `nickel` (7.7%) | `carbon` (2.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (57.7%) | `platinum_generic` (40.9%) | `platinum_wire` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `divided` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (55.3%) | `Li` (33.3%) | `NEt4` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `ClO4` (29.8%) | `molecular_no_ion` (28.4%) | `BF4` (12.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (12.6%) | `alkali_other_salt` (11.6%) | `carboxylic_acid` (3.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (67.0%) | `organic_neutral_cat` (10.8%) | `pyridine_organocat` (7.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (58.0%) | `ketone` (10.9%) | `polar_aprotic_amide` (8.5%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (96%) | `CC(=O)O` (52%) | `OCC(F)(F)F` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (74%) | `O=C([O-])[O-].[Na+` (1%) | `O` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (95%) | `COCCOC.[Br][Ni][Br` (0%) | `[Br][Mn][Br]` (0%) | set ✗ / any ✗ |

---

### Reaction #384  yield=77.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #49)

```
CCOC(=O)CC(=O)OCC.C=CCCCCCCCCCBr>>CCOC(=O)C1(C(=O)OCC)CC1CCCCCCCCCBr
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.1%) | `platinum` (2.5%) | `sacrificial_zinc` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (91.5%) | `carbon_generic` (4.7%) | `pencil_graphite` (1.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (78.0%) | `nickel` (11.5%) | `carbon` (6.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (76.3%) | `nickel_foam` (12.0%) | `nickel_wire` (3.8%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (92.5%) | `undivided` (5.2%) | `ABSENT` (2.3%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (82.7%) | `Li` (8.8%) | `Na` (5.6%) | ✗ |
| 电解质 anion | 26 | `I` | `PF6` (48.6%) | `ClO4` (24.9%) | `I` (11.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (25.2%) | `alkali_carbonate` (4.7%) | `ABSENT` (2.8%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (29.6%) | `Co_complex` (26.8%) | `ABSENT` (13.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (49.5%) | `polar_aprotic_nitrile` (43.9%) | `tfe` (2.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (79%) | `O` (38%) | `CN(C)C=O` (17%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (55%) | `O=C([O-])[O-].[Cs+` (41%) | `Cl` (10%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `O=S(=O)(O)C(F)(F)F` (6%) | `CC(=O)NC1CC2(CCCCC` (5%) | `[O-]1c2cc(cc2C=[N+` (4%) | set ✗ / any ✗ |

---

### Reaction #385  yield=81.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #50)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccc(Cl)c(C)c1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(Cl)c(C)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (81.2%) | `platinum` (14.5%) | `ABSENT` (3.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (56.1%) | `unknown_electrode` (20.3%) | `platinum_generic` (13.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.6%) | `nickel` (2.9%) | `carbon` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.1%) | `nickel_foam` (0.8%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (54.0%) | `undivided` (29.1%) | `ABSENT` (16.9%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (95.7%) | `NEt4` (2.4%) | `Na` (0.9%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (59.5%) | `I` (17.2%) | `PF6` (11.5%) | ✓ |
| 试剂大类 | 103 | `iodide_anion` | `alkali_carbonate` (7.6%) | `ABSENT` (5.0%) | `carboxylic_acid` (4.6%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (32.5%) | `ABSENT` (23.5%) | `Co_complex` (19.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (29.4%) | `cyclic_ether` (26.8%) | `polar_aprotic_amide` (14.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (86%) | `O` (7%) | `CC(=O)O` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[N+](CC)(CC)CC.[` | `O=C([O-])[O-].[K+]` (71%) | `O=C([O-])[O-].[Na+` (3%) | `O=C([O-])[O-].[Cs+` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (5%) | `CC1[CH-]C(C)=[O]->` (4%) | `[O-]1c2cc(cc2C=[N+` (3%) | set ✗ / any ✓ |

---

### Reaction #386  yield=84.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #51)

```
CCOC(=O)CC(=O)OCC.C=CCCCCBr>>CCOC(=O)C1(C(=O)OCC)CC1CCCCBr
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.3%) | `sacrificial_zinc` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (94.5%) | `carbon_generic` (2.9%) | `pencil_graphite` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (77.3%) | `nickel` (14.5%) | `stainless_steel` (5.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (66.5%) | `nickel_foam` (24.8%) | `nickel_wire` (3.8%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (90.0%) | `undivided` (7.6%) | `ABSENT` (2.4%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (95.2%) | `Li` (1.8%) | `Na` (1.4%) | ✗ |
| 电解质 anion | 26 | `I` | `PF6` (63.0%) | `ClO4` (14.4%) | `I` (10.6%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (17.4%) | `alkali_carbonate` (7.4%) | `alkali_carboxylate` (5.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (31.5%) | `organic_neutral_cat` (26.4%) | `ABSENT` (8.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (72.9%) | `polar_aprotic_nitrile` (20.2%) | `tfe` (3.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (74%) | `O` (25%) | `CN(C)C=O` (22%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (63%) | `O=C([O-])[O-].[Cs+` (48%) | `Cl` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[O-]1c2cc(cc2C=[N+` (17%) | `CC(=O)[CH-]C(C)=O.` (3%) | `CC1[CH-]C(C)=[O]->` (2%) | set ✗ / any ✗ |

---

### Reaction #387  yield=88.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #52)

```
CCOC(=O)CC(=O)OCC.C=CCCCCOc1ccc(-c2ccccc2)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.7%) | `platinum` (1.3%) | `sacrificial_zinc` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (86.7%) | `carbon_generic` (8.3%) | `unknown_electrode` (2.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.6%) | `nickel` (3.5%) | `carbon` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (91.3%) | `nickel_foam` (8.2%) | `platinum_wire` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (93.0%) | `divided` (5.9%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (90.0%) | `Li` (4.6%) | `NEt4` (3.0%) | ✓ |
| 电解质 anion | 26 | `I` | `PF6` (25.6%) | `I` (24.0%) | `BF4` (20.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (9.2%) | `carboxylic_acid` (6.9%) | `alkali_other_salt` (4.6%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.7%) | `Co_complex` (31.5%) | `ABSENT` (8.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (51.9%) | `tfe` (20.4%) | `polar_aprotic_nitrile` (17.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (40%) | `CN(C)C=O` (19%) | `CC(=O)O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (13%) | `O=C(O)C(F)(F)F` (6%) | `O=C([O-])[O-].[Na+` (6%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `CC(=O)[CH-]C(C)=O.` (3%) | `CC(C)(C)c1cccc(C2=` (2%) | `O=S(=O)(O)O` (1%) | set ✗ / any ✗ |

---

### Reaction #388  yield=87.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #53)

```
CCOC(=O)CC(=O)OCC.C=CCCC(=O)Nc1ccccc1>>CCOC(=O)C1(C(=O)OCC)CC1CCC(=O)Nc1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (99.3%) | `carbon_generic` (0.3%) | `graphite_generic` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.6%) | `carbon` (2.7%) | `stainless_steel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.0%) | `platinum_plate` (2.4%) | `nickel_foam` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.5%) | `ABSENT` (1.4%) | `divided` (1.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (85.5%) | `ABSENT` (9.0%) | `NEt4` (2.3%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (44.1%) | `Cl` (16.5%) | `carboxylate` (14.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (34.4%) | `alkali_other_salt` (5.4%) | `ABSENT` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (64.4%) | `Co_complex` (16.7%) | `Mn_complex` (8.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (90.5%) | `tfe` (2.6%) | `polar_protic_alcohol` (1.8%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (100%) | `O` (89%) | `CC(=O)O` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (40%) | `O=C([O-])[O-].[K+]` (39%) | `CC(=O)[O-].[Na+]` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #389  yield=83.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #54)

```
CCOC(=O)CC(=O)OCC.C=CCCc1ccc(-c2ccccc2)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.5%) | `sacrificial_iron` (0.5%) | `sacrificial_zinc` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (85.4%) | `carbon_generic` (3.9%) | `carbon_felt` (3.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (68.6%) | `nickel` (23.1%) | `stainless_steel` (6.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `nickel_foam` (83.1%) | `platinum_generic` (7.8%) | `platinum_plate` (5.4%) | ✓ |
| 池型 | 4 | `undivided` | `divided` (62.0%) | `ABSENT` (26.0%) | `undivided` (11.9%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (96.4%) | `ABSENT` (2.0%) | `NEt4` (0.7%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (69.2%) | `PF6` (10.7%) | `ABSENT` (6.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (14.2%) | `alkali_other_salt` (6.1%) | `carboxylic_acid` (4.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (52.9%) | `organic_neutral_cat` (22.5%) | `thianthrene_phenothiazine_cat` (4.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (45.4%) | `ketone` (28.8%) | `polar_aprotic_amide` (12.6%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (94%) | `CN(C)C=O` (2%) | `O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (30%) | `O=C([O-])[O-].[Na+` (5%) | `O=C([O-])[O-].[Cs+` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (99%) | `[Br-].[Br-].[Mn+2]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #390  yield=87.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #55)

```
CCOC(=O)CC(=O)OCC.C=CCCCc1cccs1>>CCOC(=O)C1(C(=O)OCC)CC1CCCc1cccs1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.6%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `carbon_generic` (63.2%) | `reticulated_vitreous_carbon` (32.4%) | `carbon_felt` (1.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (76.9%) | `stainless_steel` (11.7%) | `carbon` (5.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (87.0%) | `stainless_steel_generic` (4.3%) | `nickel_foam` (3.7%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (80.0%) | `divided` (14.2%) | `undivided` (5.8%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (72.5%) | `ABSENT` (25.4%) | `Li` (1.1%) | ✗ |
| 电解质 anion | 26 | `I` | `ABSENT` (45.1%) | `PF6` (33.0%) | `BF4` (8.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (9.9%) | `alkali_other_salt` (8.4%) | `carboxylic_acid` (6.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (29.5%) | `ABSENT` (21.5%) | `Co_complex` (20.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (81.1%) | `halogenated_aliphatic` (8.1%) | `polar_aprotic_amide` (5.9%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (98%) | `O` (56%) | `CC(=O)O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (41%) | `O=C([O-])[O-].[Na+` (17%) | `CCN(CC)CC` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (6%) | `__OTHER__` (6%) | `[Br-].[Br-].[Mn+2]` (4%) | set ✗ / any ✗ |

---

### Reaction #391  yield=86.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #56)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccc(OC)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(OC)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.9%) | `ABSENT` (3.4%) | `platinum` (2.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (64.7%) | `carbon_generic` (17.0%) | `unknown_electrode` (14.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (91.1%) | `nickel` (2.8%) | `stainless_steel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.4%) | `nickel_foam` (0.6%) | `platinum_wire` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (45.2%) | `ABSENT` (31.1%) | `divided` (23.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (82.2%) | `Na` (5.3%) | `Li` (5.1%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (42.6%) | `PF6` (12.6%) | `ClO4` (12.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (13.0%) | `carboxylic_acid` (6.6%) | `alkali_carboxylate` (3.6%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (40.6%) | `Co_complex` (28.4%) | `organic_neutral_cat` (11.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (64.3%) | `cyclic_ether` (11.2%) | `polar_aprotic_amide` (6.6%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (96%) | `O` (82%) | `CO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (26%) | `O=C([O-])[O-].[K+]` (15%) | `N=C(c1ccccc1)c1ccc` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (88%) | `[Fe+2].c1cc[cH-]c1` (6%) | `CC#N.CC(c1ccccn1)(` (0%) | set ✗ / any ✓ |

---

### Reaction #392  yield=86.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #57)

```
O=C(CC(=O)OCc1ccccc1)OCc1ccccc1.C=CCCCOc1ccc(-c2ccccc2)cc1>>O=C(OCc1ccccc1)C1(C(=O)OCc2ccccc2)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.4%) | `sacrificial_zinc` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (93.7%) | `carbon_generic` (2.6%) | `carbon_felt` (2.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.3%) | `nickel` (2.7%) | `carbon` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (87.3%) | `nickel_foam` (11.6%) | `platinum_wire` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (81.8%) | `divided` (11.6%) | `ABSENT` (6.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (94.1%) | `Li` (2.2%) | `ABSENT` (1.4%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (32.4%) | `PF6` (28.1%) | `I` (17.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (8.5%) | `alkali_other_salt` (5.7%) | `ABSENT` (4.0%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (26.4%) | `ABSENT` (22.0%) | `Co_complex` (12.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (48.5%) | `polar_aprotic_nitrile` (15.9%) | `tfe` (10.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (27%) | `CC(=O)O` (8%) | `CN(C)C=O` (7%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (16%) | `O=C([O-])[O-].[K+]` (5%) | `O=C(O)C(F)(F)F` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `CC(=O)[CH-]C(C)=O.` (1%) | `O=S(=O)(O)O` (1%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✗ |

---

### Reaction #393  yield=84.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #58)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1cc(OC)ccc1C(=O)c1ccccc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1cc(OC)ccc1C(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (88.4%) | `carbon_generic` (4.9%) | `carbon_felt` (2.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.7%) | `nickel` (8.4%) | `carbon` (5.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (74.3%) | `nickel_foam` (17.1%) | `platinum_plate` (4.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `divided` (1.0%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (62.3%) | `ABSENT` (29.6%) | `Na` (4.4%) | ✗ |
| 电解质 anion | 26 | `I` | `ABSENT` (46.8%) | `BF4` (19.8%) | `PF6` (10.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (22.9%) | `alkali_other_salt` (14.0%) | `ABSENT` (2.8%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (64.5%) | `Co_complex` (27.5%) | `ionic_organocat` (2.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (81.1%) | `cyclic_ether` (5.2%) | `polar_aprotic_amide` (3.7%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (94%) | `O` (7%) | `ClCCCl` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[K+]` (48%) | `O=C([O-])[O-].[Na+` (34%) | `O=C([O-])[O-].[Cs+` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC#N.CC(c1ccccn1)(` (0%) | set ✗ / any ✓ |

---

### Reaction #394  yield=83.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #59)

```
COC(=O)CC(=O)OC.C=CCCCOc1ccc(-c2ccccc2)cc1>>COC(=O)C1(C(=O)OC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `ABSENT` (0.5%) | `platinum` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (96.8%) | `carbon_generic` (2.7%) | `unknown_electrode` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.0%) | `nickel` (2.2%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `nickel_foam` (0.6%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (89.0%) | `ABSENT` (9.7%) | `divided` (1.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (79.3%) | `NEt4` (12.2%) | `Na` (4.3%) | ✓ |
| 电解质 anion | 26 | `I` | `Cl` (37.9%) | `I` (36.0%) | `BF4` (12.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (22.7%) | `ABSENT` (4.0%) | `iodide_anion` (2.7%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (46.9%) | `ABSENT` (20.1%) | `organic_neutral_cat` (15.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (51.6%) | `polar_aprotic_amide` (11.3%) | `tfe` (11.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (98%) | `O` (31%) | `CC(=O)O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (46%) | `O=C(O)C(F)(F)F` (3%) | `O=C([O-])[O-].[K+]` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `CC(C)(C)c1ccc2[O-]` (5%) | `[O-]1c2cc(cc2C=[N+` (5%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✗ / any ✗ |

---

### Reaction #395  yield=82.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #60)

```
C=CCc1ccc(OC(C)=O)c(OC)c1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC1Cc1ccc(OC(C)=O)c(OC)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.9%) | `platinum` (5.1%) | `ABSENT` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (67.1%) | `unknown_electrode` (10.7%) | `platinum_generic` (8.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (71.0%) | `nickel` (27.1%) | `carbon` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (81.1%) | `nickel_foam` (16.7%) | `nickel_generic` (0.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `divided` (0.3%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (96.3%) | `K` (1.6%) | `ABSENT` (1.2%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (54.3%) | `PF6` (18.9%) | `carboxylate` (16.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (14.7%) | `alkali_other_salt` (4.1%) | `ABSENT` (3.5%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (79.2%) | `ABSENT` (11.5%) | `organic_neutral_cat` (4.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (67.1%) | `polar_protic_alcohol` (19.7%) | `halogenated_aliphatic` (5.7%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (96%) | `ClCCCl` (17%) | `O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (4%) | `CC(C)(C)C(=O)[O-].` (3%) | `O=C(O)C(F)(F)F` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (34%) | `CC1[CH-]C(C)=[O]->` (13%) | `[O-]1c2cc(cc2C=[N+` (12%) | set ✗ / any ✗ |

---

### Reaction #396  yield=90.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #61)

```
CC(C)(C)OC(=O)CC(=O)OC(C)(C)C.C=CCCCOc1ccc(-c2ccccc2)cc1>>CC(C)(C)OC(=O)C1(C(=O)OC(C)(C)C)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.9%) | `sacrificial_zinc` (2.3%) | `ABSENT` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (93.3%) | `carbon_generic` (4.9%) | `unknown_electrode` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.1%) | `nickel` (1.1%) | `carbon` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.5%) | `nickel_foam` (3.3%) | `platinum_wire` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (89.7%) | `ABSENT` (5.3%) | `divided` (5.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (62.8%) | `NEt4` (15.0%) | `ABSENT` (13.2%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (27.8%) | `BF4` (22.5%) | `ABSENT` (17.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (9.7%) | `iodide_anion` (6.1%) | `ABSENT` (4.7%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (60.9%) | `organic_neutral_cat` (12.5%) | `thianthrene_phenothiazine_cat` (6.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (40.5%) | `ABSENT` (26.8%) | `polar_aprotic_nitrile` (13.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CN(C)C=O` (11%) | `CC#N` (9%) | `CC(=O)O` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (6%) | `O=C(O)C(F)(F)F` (6%) | `O=C([O-])[O-].[K+]` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (80%) | `[Br-].[Br-].[Mn+2]` (0%) | `CC#N.CC(c1ccccn1)(` (0%) | set ✗ / any ✗ |

---

### Reaction #397  yield=89.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #62)

```
CCOC(=O)CC(=O)OCC.C=CCCC(C)=O>>CCOC(=O)C1(C(=O)OCC)CC1CCC(C)=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `platinum` (3.0%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (50.0%) | `carbon_generic` (31.2%) | `unknown_electrode` (13.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (75.7%) | `carbon` (10.1%) | `stainless_steel` (9.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (86.5%) | `platinum_wire` (3.0%) | `stainless_steel_generic` (2.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (77.2%) | `ABSENT` (13.7%) | `divided` (9.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (67.9%) | `Li` (18.3%) | `Na` (4.4%) | ✗ |
| 电解质 anion | 26 | `I` | `ClO4` (26.0%) | `Cl` (24.7%) | `BF4` (17.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (26.5%) | `alkali_other_salt` (8.5%) | `carboxylic_acid` (3.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (54.3%) | `ABSENT` (32.4%) | `organic_neutral_cat` (4.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (86.8%) | `polar_protic_alcohol` (5.5%) | `polar_aprotic_amide` (2.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (99%) | `O` (3%) | `CC(=O)O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C([O-])[O-].[Na+` (55%) | `O=C([O-])[O-].[K+]` (49%) | `CC(=O)[O-].[Na+]` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[O-]1c2cc(cc2C=[N+` (40%) | `CC(C)(C)c1ccc2[O-]` (22%) | `__ABSENT__` (5%) | set ✗ / any ✗ |

---

### Reaction #398  yield=89.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #63)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccc(C(C)=O)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(C(C)=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (84.2%) | `platinum` (13.4%) | `sacrificial_zinc` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (62.0%) | `unknown_electrode` (15.3%) | `platinum_generic` (7.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (69.2%) | `nickel` (20.0%) | `carbon` (8.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (82.3%) | `nickel_foam` (17.0%) | `carbon_felt` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (63.3%) | `divided` (33.9%) | `ABSENT` (2.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (87.1%) | `Li` (8.0%) | `Na` (2.5%) | ✗ |
| 电解质 anion | 26 | `I` | `I` (56.2%) | `Cl` (19.6%) | `ClO4` (13.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (15.0%) | `alkali_carbonate` (7.4%) | `ABSENT` (3.8%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (59.1%) | `Co_complex` (24.8%) | `organic_neutral_cat` (10.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (48.8%) | `polar_aprotic_nitrile` (34.2%) | `polar_protic_alcohol` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (85%) | `O` (11%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (46%) | `O=C(O)C(F)(F)F` (21%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (95%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[O-]1c2cc(cc2C=[N+` (0%) | set ✗ / any ✗ |

---

### Reaction #399  yield=89.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #64)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccc(C)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.9%) | `platinum` (3.8%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (88.1%) | `carbon_generic` (8.7%) | `unknown_electrode` (1.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (72.0%) | `nickel` (18.8%) | `carbon` (6.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (75.6%) | `nickel_foam` (21.7%) | `stainless_steel_generic` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (40.9%) | `undivided` (34.1%) | `ABSENT` (25.1%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (63.2%) | `ABSENT` (22.5%) | `Li` (6.3%) | ✗ |
| 电解质 anion | 26 | `I` | `ABSENT` (28.6%) | `BF4` (20.3%) | `I` (18.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_other_salt` (11.4%) | `alkali_carbonate` (11.1%) | `carboxylic_acid` (7.7%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Co_complex` (51.6%) | `ABSENT` (23.2%) | `organic_neutral_cat` (8.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `polar_aprotic_amide` (26.7%) | `cyclic_ether` (10.6%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (95%) | `O` (85%) | `CC(=O)O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(C)(C)C(=O)O.[Na` (44%) | `O=C(O)C(F)(F)F` (10%) | `O=O` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[O-]1c2cc(cc2C=[N+` (5%) | `CC(C)(C)c1ccc2[O-]` (4%) | `CC1[CH-]C(C)=[O]->` (3%) | set ✗ / any ✗ |

---

### Reaction #400  yield=81.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #65)

```
CCOC(=O)CC(=O)OCC.C=CCCOc1ccc(-c2ccccc2)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `platinum` (1.1%) | `sacrificial_iron` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (56.8%) | `carbon_generic` (30.7%) | `unknown_electrode` (4.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (79.2%) | `nickel` (15.8%) | `carbon` (4.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (55.1%) | `nickel_foam` (43.9%) | `platinum_wire` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (91.3%) | `ABSENT` (6.8%) | `divided` (1.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (95.8%) | `ABSENT` (2.2%) | `NEt4` (0.7%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (52.8%) | `I` (14.3%) | `PF6` (8.8%) | ✓ |
| 试剂大类 | 103 | `iodide_anion` | `alkali_carbonate` (18.0%) | `alkali_other_salt` (11.2%) | `as_solvent_halogenated_aliphat` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (64.9%) | `Co_complex` (9.8%) | `organic_neutral_cat` (6.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (36.2%) | `polar_aprotic_nitrile` (31.8%) | `ketone` (9.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (68%) | `CC(=O)O` (11%) | `CN(C)C=O` (7%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[N+](CC)(CC)CC.[` | `O=C([O-])[O-].[K+]` (46%) | `O=C([O-])[O-].[Na+` (4%) | `O=C(O)C(F)(F)F` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (90%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC#N.CC(c1ccccn1)(` (0%) | set ✗ / any ✗ |

---

### Reaction #401  yield=88.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #66)

```
CCOC(=O)CC(=O)OCC.C=CCCCCCCCCCO>>CCOC(=O)C1(C(=O)OCC)CC1CCCCCCCCCO
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `platinum` (2.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (50.3%) | `carbon_generic` (33.1%) | `graphite_generic` (12.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (58.2%) | `nickel` (20.6%) | `carbon` (16.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (78.1%) | `nickel_foam` (5.1%) | `graphite_generic` (4.5%) | ✗ |
| 池型 | 4 | `undivided` | `divided` (65.5%) | `undivided` (33.8%) | `ABSENT` (0.8%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (94.0%) | `Li` (1.9%) | `NEt4` (1.9%) | ✓ |
| 电解质 anion | 26 | `I` | `BF4` (39.1%) | `ClO4` (21.9%) | `PF6` (16.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (20.1%) | `alkali_carbonate` (6.4%) | `alkali_carboxylate` (6.0%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (40.2%) | `Co_complex` (17.0%) | `organic_neutral_cat` (13.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (79.9%) | `polar_aprotic_amide` (9.9%) | `halogenated_aliphatic` (4.1%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (97%) | `ClCCCl` (4%) | `O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=C(O)C(F)(F)F` (35%) | `CC(=O)O` (20%) | `O=C([O-])[O-].[Cs+` (17%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (98%) | `O=S(=O)([O-])C(F)(` (1%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✗ / any ✗ |

---

### Reaction #402  yield=91.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_9_e202425634.json) (反应 idx 在该 JSON 内 = #67)

```
CCOC(=O)CC(=O)OCC.C=CCCCOc1ccc(-c2ccccc2)cc1>>CCOC(=O)C1(C(=O)OCC)CC1CCCOc1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.6%) | `platinum` (1.1%) | `sacrificial_zinc` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (81.3%) | `carbon_generic` (15.6%) | `unknown_electrode` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (7.5%) | `carbon` (2.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.2%) | `nickel_foam` (11.4%) | `platinum_wire` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (86.2%) | `ABSENT` (7.8%) | `divided` (6.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.5%) | `NEt4` (5.9%) | `ABSENT` (4.7%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (33.8%) | `BF4` (24.5%) | `PF6` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carbonate` (15.8%) | `alkali_other_salt` (6.4%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `organic_neutral_cat` (31.9%) | `Co_complex` (20.4%) | `ABSENT` (19.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (43.9%) | `polar_aprotic_nitrile` (29.5%) | `tfe` (7.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `O` (17%) | `CN(C)C=O` (9%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C([O-])[O-].[K+]` (18%) | `O=C(O)C(F)(F)F` (11%) | `O=C([O-])[O-].[Na+` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `O=S(=O)(O)O` (1%) | `CC(C)(C)c1cccc(C2=` (1%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #403  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202500203_sup_1_p16_t1.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202500203_sup_1_p16_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C1C=CC(c2ccccc2)(c2ccccc2)CC1>>O=C1CCC(c2ccccc2)(c2ccccc2)C2CC12.CC1=CC(=O)CCC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.8%) | `platinum` (3.4%) | `ABSENT` (0.8%) | ✓ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `glassy_carbon` (65.5%) | `carbon_generic` (15.3%) | `unknown_electrode` (4.7%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `platinum` (98.5%) | `carbon` (0.7%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `platinum_generic` (63.9%) | `platinum_plate` (33.0%) | `unknown_electrode` (2.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `ABSENT` (1.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (97.2%) | `PF6` (2.4%) | `ClO4` (0.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (29.9%) | `carboxylic_acid` (3.5%) | `electrophilic_N_F` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `Co_complex` (0.0%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (77.8%) | `polar_aprotic_nitrile` (22.0%) | `polar_aprotic_amide` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `CC(=O)N(C)C` | `CC#N` (93%) | `CO` (7%) | `CCO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #404  yield=23.0%

**Source paper**: [`Angew/10.1002_anie.202500203_sup_1_p16_t1.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202500203_sup_1_p16_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C1C=CC(c2ccccc2)(c2ccccc2)CC1>>O=C1CCC(c2ccccc2)(c2ccccc2)C2CC12.CC1=CC(=O)CCC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.8%) | `platinum` (3.4%) | `ABSENT` (0.8%) | ✓ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `glassy_carbon` (65.5%) | `carbon_generic` (15.3%) | `unknown_electrode` (4.7%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `platinum` (98.5%) | `carbon` (0.7%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `platinum_generic` (63.9%) | `platinum_plate` (33.0%) | `unknown_electrode` (2.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `ABSENT` (1.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (97.2%) | `PF6` (2.4%) | `ClO4` (0.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (29.9%) | `carboxylic_acid` (3.5%) | `electrophilic_N_F` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `Co_complex` (0.0%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (77.8%) | `polar_aprotic_nitrile` (22.0%) | `polar_aprotic_amide` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `CC(=O)N(C)C` | `CC#N` (93%) | `CO` (7%) | `CCO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #405  yield=17.0%

**Source paper**: [`Angew/10.1002_anie.202500203_sup_1_p16_t1.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202500203_sup_1_p16_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C1C=CC(c2ccccc2)(c2ccccc2)CC1>>O=C1CCC(c2ccccc2)(c2ccccc2)C2CC12.CC1=CC(=O)CCC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.8%) | `platinum` (3.4%) | `ABSENT` (0.8%) | ✓ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `glassy_carbon` (65.5%) | `carbon_generic` (15.3%) | `unknown_electrode` (4.7%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `platinum` (98.5%) | `carbon` (0.7%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `platinum_generic` (63.9%) | `platinum_plate` (33.0%) | `unknown_electrode` (2.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `ABSENT` (1.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (97.2%) | `PF6` (2.4%) | `ClO4` (0.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (29.9%) | `carboxylic_acid` (3.5%) | `electrophilic_N_F` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `Co_complex` (0.0%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (77.8%) | `polar_aprotic_nitrile` (22.0%) | `polar_aprotic_amide` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `CC(=O)N(C)C` | `CC#N` (93%) | `CO` (7%) | `CCO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #406  yield=81.0%

**Source paper**: [`Angew/10.1002_anie.202500203_sup_1_p16_t1.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202500203_sup_1_p16_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C1C=CC(c2ccccc2)(c2ccccc2)CC1>>O=C1CCC(c2ccccc2)(c2ccccc2)C2CC12.CC1=CC(=O)CCC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.8%) | `platinum` (3.4%) | `ABSENT` (0.8%) | ✓ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `glassy_carbon` (65.5%) | `carbon_generic` (15.3%) | `unknown_electrode` (4.7%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `platinum` (98.5%) | `carbon` (0.7%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `platinum_generic` (63.9%) | `platinum_plate` (33.0%) | `unknown_electrode` (2.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `ABSENT` (1.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (97.2%) | `PF6` (2.4%) | `ClO4` (0.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (29.9%) | `carboxylic_acid` (3.5%) | `electrophilic_N_F` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `Co_complex` (0.0%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (77.8%) | `polar_aprotic_nitrile` (22.0%) | `polar_aprotic_amide` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `CC(=O)N(C)C` | `CC#N` (93%) | `CO` (7%) | `CCO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #407  yield=77.0%

**Source paper**: [`Angew/10.1002_anie.202500203_sup_1_p16_t1.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202500203_sup_1_p16_t1.json) (反应 idx 在该 JSON 内 = #0)

```
O=C1C=CC(c2ccccc2)(c2ccccc2)CC1>>O=C1CCC(c2ccccc2)(c2ccccc2)C2CC12.CC1=CC(=O)CCC1(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.8%) | `platinum` (3.4%) | `ABSENT` (0.8%) | ✓ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `glassy_carbon` (65.5%) | `carbon_generic` (15.3%) | `unknown_electrode` (4.7%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `platinum` (98.5%) | `carbon` (0.7%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `platinum_generic` (63.9%) | `platinum_plate` (33.0%) | `unknown_electrode` (2.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `ABSENT` (1.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.7%) | `NEt4` (0.2%) | `Li` (0.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (97.2%) | `PF6` (2.4%) | `ClO4` (0.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (29.9%) | `carboxylic_acid` (3.5%) | `electrophilic_N_F` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.9%) | `Fe_complex` (0.0%) | `Co_complex` (0.0%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (77.8%) | `polar_aprotic_nitrile` (22.0%) | `polar_aprotic_amide` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `CC(=O)N(C)C` | `CC#N` (93%) | `CO` (7%) | `CCO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)O` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #408  yield=96.0%

**Source paper**: [`Angew/10.1002_anie.202500203_sup_1_p21_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202500203_sup_1_p21_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>c1ccc(-c2ccc(C3CC3)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (48.1%) | `sacrificial_iron` (26.0%) | `ABSENT` (14.8%) | ✓ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `reticulated_vitreous_carbon` (29.1%) | `carbon_generic` (19.3%) | `iron_generic` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (51.0%) | `ABSENT` (18.9%) | `stainless_steel` (9.4%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (22.3%) | `platinum_foil` (18.7%) | `stainless_steel_generic` (13.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (41.0%) | `ABSENT` (13.4%) | `Na` (11.7%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `Br` (29.3%) | `carboxylate` (20.6%) | `PF6` (11.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_halogenated_aliphat` (5.1%) | `ABSENT` (3.4%) | `secondary_amine` (2.7%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `Fe_complex` (19.8%) | `Mn_complex` (17.2%) | `ABSENT` (16.0%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (21.4%) | `polar_aprotic_amide` (19.8%) | `polar_protic_acid` (12.5%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC#N` (70%) | `CC(=O)O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `CC[Si](CC)CC` (93%) | `OB(O)B(O)O` (90%) | `O=O` (76%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (94%) | `__OTHER__` (3%) | `c1ccncc1` (3%) | set ✓ / any ✓ |

---

### Reaction #409  yield=93.0%

**Source paper**: [`Angew/10.1002_anie.202500203_sup_1_p21_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202500203_sup_1_p21_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>c1ccc(-c2ccc(C3CC3)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (48.1%) | `sacrificial_iron` (26.0%) | `ABSENT` (14.8%) | ✓ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `reticulated_vitreous_carbon` (29.1%) | `carbon_generic` (19.3%) | `iron_generic` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (51.0%) | `ABSENT` (18.9%) | `stainless_steel` (9.4%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (22.3%) | `platinum_foil` (18.7%) | `stainless_steel_generic` (13.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (41.0%) | `ABSENT` (13.4%) | `Na` (11.7%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `Br` (29.3%) | `carboxylate` (20.6%) | `PF6` (11.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_halogenated_aliphat` (5.1%) | `ABSENT` (3.4%) | `secondary_amine` (2.7%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `Fe_complex` (19.8%) | `Mn_complex` (17.2%) | `ABSENT` (16.0%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (21.4%) | `polar_aprotic_amide` (19.8%) | `polar_protic_acid` (12.5%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC#N` (70%) | `CC(=O)O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `CC[Si](CC)CC` (93%) | `OB(O)B(O)O` (90%) | `O=O` (76%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (94%) | `__OTHER__` (3%) | `c1ccncc1` (3%) | set ✓ / any ✓ |

---

### Reaction #410  yield=75.0%

**Source paper**: [`Angew/10.1002_anie.202500203_sup_1_p21_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202500203_sup_1_p21_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>c1ccc(-c2ccc(C3CC3)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (48.1%) | `sacrificial_iron` (26.0%) | `ABSENT` (14.8%) | ✓ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `reticulated_vitreous_carbon` (29.1%) | `carbon_generic` (19.3%) | `iron_generic` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (51.0%) | `ABSENT` (18.9%) | `stainless_steel` (9.4%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (22.3%) | `platinum_foil` (18.7%) | `stainless_steel_generic` (13.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (41.0%) | `ABSENT` (13.4%) | `Na` (11.7%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `Br` (29.3%) | `carboxylate` (20.6%) | `PF6` (11.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_halogenated_aliphat` (5.1%) | `ABSENT` (3.4%) | `secondary_amine` (2.7%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `Fe_complex` (19.8%) | `Mn_complex` (17.2%) | `ABSENT` (16.0%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (21.4%) | `polar_aprotic_amide` (19.8%) | `polar_protic_acid` (12.5%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC#N` (70%) | `CC(=O)O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `CC[Si](CC)CC` (93%) | `OB(O)B(O)O` (90%) | `O=O` (76%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (94%) | `__OTHER__` (3%) | `c1ccncc1` (3%) | set ✓ / any ✓ |

---

### Reaction #411  yield=94.0%

**Source paper**: [`Angew/10.1002_anie.202500203_sup_1_p21_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202500203_sup_1_p21_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(-c2ccccc2)cc1>>c1ccc(-c2ccc(C3CC3)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (48.1%) | `sacrificial_iron` (26.0%) | `ABSENT` (14.8%) | ✓ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `reticulated_vitreous_carbon` (29.1%) | `carbon_generic` (19.3%) | `iron_generic` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (51.0%) | `ABSENT` (18.9%) | `stainless_steel` (9.4%) | ✗ |
| 阴极 (细类) | 49 | `nickel_generic` | `platinum_plate` (22.3%) | `platinum_foil` (18.7%) | `stainless_steel_generic` (13.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (41.0%) | `ABSENT` (13.4%) | `Na` (11.7%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `Br` (29.3%) | `carboxylate` (20.6%) | `PF6` (11.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_halogenated_aliphat` (5.1%) | `ABSENT` (3.4%) | `secondary_amine` (2.7%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `Fe_complex` (19.8%) | `Mn_complex` (17.2%) | `ABSENT` (16.0%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (21.4%) | `polar_aprotic_amide` (19.8%) | `polar_protic_acid` (12.5%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `O` (95%) | `CC#N` (70%) | `CC(=O)O` (57%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `CC[Si](CC)CC` (93%) | `OB(O)B(O)O` (90%) | `O=O` (76%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (94%) | `__OTHER__` (3%) | `c1ccncc1` (3%) | set ✓ / any ✓ |

---

### Reaction #412  yield=30.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #0)

```
[2H]C([2H])(Cl)Cl.C=Cc1ccc(-c2ccccc2)cc1>>[2H]C1([2H])CC1c1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (80.0%) | `sacrificial_iron` (8.7%) | `ABSENT` (3.6%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `reticulated_vitreous_carbon` (44.5%) | `carbon_rod` (10.8%) | `graphite_generic` (10.0%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `platinum` (83.0%) | `carbon` (10.8%) | `stainless_steel` (2.2%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `platinum_plate` (71.8%) | `platinum_wire` (8.5%) | `platinum_generic` (2.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (33.0%) | `Li` (27.5%) | `NEt4` (24.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Br` (19.5%) | `molecular_no_ion` (17.1%) | `carboxylate` (16.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (6.7%) | `as_solvent_halogenated_aliphat` (3.5%) | `secondary_amine` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `Mn_complex` (34.8%) | `Fe_complex` (19.7%) | `Cu_complex` (10.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (41.8%) | `polar_aprotic_amide` (25.4%) | `polar_protic_acid` (11.8%) | ✓ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (74%) | `CC(=O)O` (38%) | `CN(C)C=O` (24%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (90%) | `OB(O)B(O)O` (24%) | `O=O` (22%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Br-][Ni+2]1([Br-]` + `CC(C)[C@H]1COC(c2c` | `COCCOC.[Br][Ni][Br` (20%) | `[Cl][Mn][Cl]` (17%) | `__OTHER__` (8%) | set ✗ / any ✗ |

---

### Reaction #413  yield=37.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #1)

```
ClCCl.C=C(c1ccccc1)c1cccs1>>c1ccc(C2(c3cccs3)CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (89.2%) | `sacrificial_magnesium` (5.2%) | `sacrificial_zinc` (2.6%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `graphite_generic` (26.5%) | `zinc_plate` (24.5%) | `magnesium_plate` (10.8%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `platinum` (71.6%) | `carbon` (22.0%) | `nickel` (4.0%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `platinum_wire` (31.2%) | `platinum_generic` (26.1%) | `graphite_generic` (13.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `divided` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (72.2%) | `NEt4` (24.9%) | `NBu4` (2.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (99.7%) | `BF4` (0.1%) | `Br` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.2%) | `o2_oxidant` (2.5%) | `acid_anhydride` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (94.3%) | `Mn_complex` (2.2%) | `Co_complex` (0.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (96.2%) | `ABSENT` (2.2%) | `polar_protic_alcohol` (0.4%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (95%) | `ClCCl` (1%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)[C@H]1COC(c2c` + `COCCOC.[Br][Ni][Br` | `__ABSENT__` (100%) | `[Br][Mn][Br]` (0%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✗ |

---

### Reaction #414  yield=47.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #2)

```
ClCCl.O=C(C=Cc1ccccc1)c1ccccc1>>O=C(c1ccccc1)C1CC1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (35.0%) | `sacrificial_iron` (22.5%) | `ABSENT` (19.9%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `graphite_generic` (30.6%) | `unknown_electrode` (28.7%) | `pencil_graphite` (19.6%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (71.9%) | `stainless_steel` (15.9%) | `nickel` (4.5%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `graphite_generic` (38.2%) | `stainless_steel_rod` (20.2%) | `unknown_electrode` (9.8%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (48.5%) | `undivided` (38.8%) | `divided` (12.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (50.0%) | `NBu4` (20.6%) | `ABSENT` (18.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (39.0%) | `Cl` (20.2%) | `ABSENT` (18.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.0%) | `tertiary_amine` (8.8%) | `iodide_anion` (4.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (95.6%) | `Mn_complex` (2.2%) | `Ni_complex` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (77.8%) | `polar_aprotic_nitrile` (10.6%) | `polar_protic_alcohol` (6.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `O` (87%) | `CC#N` (72%) | `CN(C)C=O` (27%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `[Br-].[H+]` (11%) | `O=S([O-])([O-])=S.` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)[C@H]1COC(c2c` + `[Br-][Ni+2]1([Br-]` | `__ABSENT__` (89%) | `O=S(=O)([O-])C(F)(` (11%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #415  yield=43.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #3)

```
[2H]C(Cl)(Cl)Cl.C=Cc1ccc(-c2ccccc2)cc1>>[2H]C1(Cl)CC1c1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `sacrificial_zinc` (99.3%) | `sacrificial_magnesium` (0.3%) | `sacrificial_aluminum` (0.2%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `zinc_plate` (100.0%) | `magnesium_plate` (0.0%) | `zinc_generic` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (99.4%) | `nickel` (0.2%) | `sacrificial_zinc` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `graphite_felt` (99.4%) | `zinc_plate` (0.2%) | `carbon_felt` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.2%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (97.8%) | `NBu4` (0.8%) | `molecular_no_ion` (0.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `OTf` (84.6%) | `molecular_no_ion` (11.3%) | `ClO4` (3.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `hcl` (78.9%) | `ABSENT` (1.8%) | `thiol` (0.7%) | ✓ |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (99.3%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (99.3%) | `ABSENT` (0.4%) | `polar_aprotic_nitrile` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CN(C)C=O` (50%) | `CC(=O)N(C)C` (49%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` + `O` | `Cl` (100%) | `O` (99%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)[C@H]1COC(c2c` + `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (96%) | `CC(C)[C@H]1COC(c2c` (96%) | `__ABSENT__` (4%) | set ✓ / any ✓ |

---

### Reaction #416  yield=58.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #4)

```
ClCCl.C=Cc1ccc(Cl)nc1>>Clc1ccc(C2CC2)cn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (95.8%) | `ABSENT` (1.9%) | `platinum` (1.4%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `graphite_generic` (79.0%) | `boron_doped_diamond` (4.3%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `stainless_steel` (71.4%) | `carbon` (21.2%) | `platinum` (6.3%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `stainless_steel_generic` (65.8%) | `graphite_generic` (13.5%) | `platinum_wire` (2.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.4%) | `divided` (1.2%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (45.3%) | `NBu4` (41.0%) | `Na` (7.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `Cl` (28.4%) | `carboxylate` (24.6%) | `Br` (15.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.8%) | `polyhalo_radical_transfer` (3.4%) | `iodide_anion` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (86.7%) | `organic_neutral_cat` (2.5%) | `Fe_complex` (2.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (45.8%) | `polar_protic_alcohol` (22.2%) | `cyclic_ether` (12.6%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (90%) | `ClCCl` (31%) | `O` (29%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (96%) | `O=S(=O)(O)C(F)(F)F` (4%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Br-][Ni+2]1([Br-]` + `CC(C)[C@H]1COC(c2c` | `__ABSENT__` (96%) | `c1ccncc1` (2%) | `[O]=[Fe][O][Fe]=[O` (1%) | set ✗ / any ✗ |

---

### Reaction #417  yield=51.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #5)

```
ClC(Cl)Cl.C=Cc1ccc(-c2ccccc2)cc1>>ClC1CC1c1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `sacrificial_zinc` (38.8%) | `carbon` (30.9%) | `sacrificial_iron` (20.1%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `zinc_plate` (78.5%) | `graphite_generic` (7.7%) | `magnesium_plate` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (85.3%) | `nickel` (9.7%) | `platinum` (3.5%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `graphite_generic` (36.9%) | `nickel_foam` (28.6%) | `graphite_felt` (27.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `divided` (0.7%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (69.3%) | `Li` (23.6%) | `NEt4` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `PF6` (26.8%) | `ClO4` (24.9%) | `molecular_no_ion` (11.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `hcl` (16.9%) | `ABSENT` (6.3%) | `water` (4.1%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (89.4%) | `Mn_complex` (3.2%) | `Fe_complex` (2.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (95.8%) | `ABSENT` (1.7%) | `polar_protic_acid` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CN(C)C=O` (100%) | `CC(=O)O` (29%) | `O=CO` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `Cl` (96%) | `O` (62%) | `O=O` (19%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Br-][Ni+2]1([Br-]` + `CC(C)[C@H]1COC(c2c` | `COCCOC.[Br][Ni][Br` (94%) | `__ABSENT__` (63%) | `CC(C)[C@H]1COC(c2c` (27%) | set ✗ / any ✓ |

---

### Reaction #418  yield=57.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #6)

```
ClCCl.C=CS(=O)(=O)c1ccccc1>>O=S(=O)(c1ccccc1)C1CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (99.5%) | `sacrificial_magnesium` (0.2%) | `sacrificial_zinc` (0.1%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `graphite_generic` (97.2%) | `unknown_electrode` (1.8%) | `graphite_rod` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (99.5%) | `stainless_steel` (0.2%) | `nickel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `graphite_generic` (91.5%) | `unknown_electrode` (4.5%) | `carbon_felt` (2.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (80.4%) | `divided` (16.8%) | `ABSENT` (2.8%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (74.8%) | `Na` (12.8%) | `NBu4` (7.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `Cl` (89.2%) | `molecular_no_ion` (7.5%) | `ClO4` (0.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.4%) | `ammonia` (2.3%) | `hcl` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (99.8%) | `Mn_complex` (0.1%) | `Fe_complex` (0.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (66.8%) | `aqueous` (12.0%) | `ABSENT` (7.5%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (87%) | `O` (12%) | `CN(C)C=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `[Na+].[OH-]` (1%) | `CCN(CC)CC.F.F.F` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)[C@H]1COC(c2c` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #419  yield=68.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #7)

```
ClCCl.C=CC(=O)OC[C@H]1O[C@@H](OC(C)=O)[C@H](OC(C)=O)[C@@H](OC(C)=O)[C@@H]1OC(C)=O>>CC(=O)O[C@@H]1O[C@H](COC(=O)C2CC2)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_zinc` (0.1%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `carbon_rod` (49.7%) | `graphite_generic` (46.4%) | `graphite_felt` (1.2%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (97.1%) | `stainless_steel` (1.6%) | `nickel` (0.7%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `graphite_generic` (56.8%) | `unknown_electrode` (13.0%) | `carbon_felt` (10.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (58.5%) | `NBu4` (36.8%) | `ABSENT` (3.6%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `Cl` (76.3%) | `BF4` (23.1%) | `ABSENT` (0.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.8%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (100.0%) | `Mn_complex` (0.0%) | `Fe_complex` (0.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (89.3%) | `ketone` (5.1%) | `cyclic_ether` (2.0%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (83%) | `CN(C)C=O` (0%) | `FC(F)(F)c1ccccc1` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)[C@H]1COC(c2c` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✗ / any ✗ |

---

### Reaction #420  yield=62.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #8)

```
ClCCl.C=Cc1ccccc1OC>>COc1ccccc1C1CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (90.4%) | `sacrificial_iron` (5.1%) | `sacrificial_zinc` (3.2%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `magnesium_plate` (41.6%) | `carbon_rod` (21.9%) | `iron_plate` (7.1%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (99.3%) | `platinum` (0.4%) | `nickel` (0.2%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `carbon_felt` (81.0%) | `graphite_generic` (8.7%) | `graphite_felt` (6.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (68.5%) | `NBu4` (21.4%) | `NEt4` (6.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Cl` (78.0%) | `ClO4` (13.4%) | `BF4` (2.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (30.3%) | `acid_anhydride` (1.8%) | `metal_oxide_oxidant` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (98.5%) | `Mn_complex` (0.6%) | `ammonium_PTC_organocat` (0.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `ABSENT` (47.3%) | `polar_aprotic_nitrile` (34.7%) | `halogenated_aliphatic` (6.1%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `__ABSENT__` (98%) | `O` (0%) | `CCOCC` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `[I-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Br-][Ni+2]1([Br-]` + `CC(C)[C@H]1COC(c2c` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC[C@H](C)[C@H]1CN` (0%) | set ✗ / any ✗ |

---

### Reaction #421  yield=69.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #9)

```
ClCCl.C=C(B1OC(C)(C)C(C)(C)O1)c1ccccc1>>CC1(C)OB(C2(c3ccccc3)CC2)OC1(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (60.3%) | `sacrificial_magnesium` (20.2%) | `sacrificial_zinc` (11.4%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `carbon_generic` (59.2%) | `zinc_plate` (14.1%) | `magnesium_plate` (7.8%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (95.2%) | `platinum` (4.1%) | `nickel` (0.5%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `carbon_generic` (41.5%) | `graphite_plate` (26.2%) | `graphite_generic` (14.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.8%) | `ABSENT` (1.0%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (64.1%) | `NBu4` (35.0%) | `Na` (0.5%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (97.8%) | `OTf` (1.1%) | `BF4` (0.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (30.3%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.9%) | `organic_neutral_cat` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `cyclic_ether` (52.8%) | `polar_protic_alcohol` (12.5%) | `ABSENT` (9.3%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `C1CCOC1` (98%) | `O` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (97%) | `O` (17%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Br-][Ni+2]1([Br-]` + `CC(C)[C@H]1COC(c2c` | `__ABSENT__` (100%) | `COc1c(I)cc2c(c1I)-` (0%) | `COCCOC.[Br][Ni][Br` (0%) | set ✗ / any ✗ |

---

### Reaction #422  yield=70.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #10)

```
ClCCl.C=Cc1ccc(F)cc1>>Fc1ccc(C2CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (79.1%) | `ABSENT` (10.0%) | `sacrificial_iron` (4.1%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `graphite_generic` (63.0%) | `reticulated_vitreous_carbon` (15.1%) | `ABSENT` (4.6%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (59.5%) | `stainless_steel` (17.8%) | `ABSENT` (10.6%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `graphite_generic` (67.8%) | `stainless_steel_generic` (21.0%) | `graphite_felt` (2.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (73.5%) | `NBu4` (7.6%) | `ABSENT` (6.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (22.7%) | `Br` (18.9%) | `Cl` (18.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.7%) | `polyhalo_radical_transfer` (4.1%) | `secondary_amine` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (40.8%) | `ammonium_PTC_organocat` (14.6%) | `Mn_complex` (11.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (49.5%) | `cyclic_ether` (15.3%) | `ABSENT` (10.9%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (96%) | `O` (5%) | `CC(C)=O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (94%) | `O=O` (3%) | `CC[Si](CC)CC` (2%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Br-][Ni+2]1([Br-]` + `CC(C)[C@H]1COC(c2c` | `__ABSENT__` (55%) | `[Cl-].[Cl-].[Mn+2]` (35%) | `__OTHER__` (6%) | set ✗ / any ✗ |

---

### Reaction #423  yield=70.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #11)

```
ClCCl.C=Cc1ccc(OC)cc1>>COc1ccc(C2CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (77.1%) | `ABSENT` (17.1%) | `sacrificial_magnesium` (2.6%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `graphite_generic` (34.8%) | `boron_doped_diamond` (34.0%) | `unknown_electrode` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (38.5%) | `stainless_steel` (21.5%) | `platinum` (20.7%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `stainless_steel_generic` (21.9%) | `unknown_electrode` (15.4%) | `graphite_generic` (13.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.9%) | `ABSENT` (2.6%) | `divided` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (37.2%) | `NBu4` (23.1%) | `Li` (18.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `Br` (24.8%) | `ClO4` (19.3%) | `Cl` (18.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.2%) | `water` (5.2%) | `secondary_amine` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (51.3%) | `Fe_complex` (24.4%) | `brønsted_acid_cat` (4.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (45.6%) | `cyclic_ether` (26.3%) | `aqueous` (17.0%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (99%) | `O` (47%) | `ClCCl` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (59%) | `OC(C(F)(F)F)C(F)(F` (38%) | `N=C(c1ccccc1)c1ccc` (9%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)[C@H]1COC(c2c` + `[Br-][Ni+2]1([Br-]` | `__ABSENT__` (85%) | `[Fe+2].c1cc[cH-]c1` (12%) | `__OTHER__` (1%) | set ✗ / any ✗ |

---

### Reaction #424  yield=76.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #12)

```
ClCCl.C=Cc1cccc(OC)c1>>COc1cccc(C2CC2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (99.3%) | `sacrificial_magnesium` (0.4%) | `sacrificial_zinc` (0.2%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `graphite_generic` (90.8%) | `carbon_rod` (3.4%) | `reticulated_vitreous_carbon` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (89.7%) | `stainless_steel` (5.1%) | `platinum` (4.8%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `graphite_generic` (70.5%) | `stainless_steel_generic` (7.7%) | `graphite_felt` (6.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `divided` (0.4%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (35.7%) | `Li` (33.3%) | `NBu4` (14.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Cl` (43.6%) | `molecular_no_ion` (26.1%) | `carboxylate` (16.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.4%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (86.1%) | `Fe_complex` (6.0%) | `Mn_complex` (3.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (75.7%) | `cyclic_ether` (9.9%) | `ABSENT` (6.8%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (70%) | `CCOCC` (59%) | `FC(F)(F)c1ccccc1` (15%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (3%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)[C@H]1COC(c2c` + `[Br-][Ni+2]1([Br-]` | `__ABSENT__` (98%) | `c1ccncc1` (3%) | `[Cl][Mn][Cl]` (1%) | set ✗ / any ✗ |

---

### Reaction #425  yield=79.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #13)

```
CC(Cl)Cl.C=Cc1ccc(-c2ccccc2)cc1>>CC1CC1c1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (43.1%) | `sacrificial_iron` (32.4%) | `sacrificial_zinc` (18.0%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `zinc_plate` (22.4%) | `magnesium_plate` (21.0%) | `reticulated_vitreous_carbon` (18.3%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (72.2%) | `platinum` (18.2%) | `nickel` (9.2%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `nickel_foam` (52.1%) | `graphite_generic` (25.3%) | `carbon_felt` (10.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.3%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (72.0%) | `Li` (24.6%) | `Na` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `PF6` (37.0%) | `ClO4` (35.0%) | `molecular_no_ion` (11.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.0%) | `secondary_amine` (2.2%) | `as_solvent_halogenated_aliphat` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (92.2%) | `Ni_complex` (2.9%) | `Mn_complex` (1.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_amide` (64.1%) | `polar_aprotic_nitrile` (19.8%) | `ABSENT` (11.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CN(C)C=O` (95%) | `CC(=O)O` (5%) | `CC#N` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (1%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)[C@H]1COC(c2c` | `__ABSENT__` (99%) | `COCCOC.[Br][Ni][Br` (14%) | `CC(C)[C@H]1COC(c2c` (0%) | set ✗ / any ✓ |

---

### Reaction #426  yield=73.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #14)

```
ClCCl.C=Cc1ccc(N)cc1>>Nc1ccc(C2CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (75.8%) | `sacrificial_magnesium` (9.3%) | `ABSENT` (7.9%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `graphite_generic` (54.6%) | `graphite_rod` (14.7%) | `magnesium_generic` (8.2%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (63.7%) | `platinum` (17.2%) | `stainless_steel` (7.6%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `graphite_generic` (51.0%) | `unknown_electrode` (11.8%) | `stainless_steel_generic` (9.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (52.7%) | `NBu4` (24.8%) | `Li` (15.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (42.9%) | `Cl` (20.3%) | `I` (9.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `polyhalo_radical_transfer` (2.1%) | `secondary_amine` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (61.4%) | `ammonium_PTC_organocat` (12.1%) | `Mn_complex` (8.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (68.2%) | `cyclic_ether` (17.3%) | `polar_aprotic_sulfoxide` (3.4%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (99%) | `O` (4%) | `ClCCl` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O=O` (1%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)[C@H]1COC(c2c` + `[Br-][Ni+2]1([Br-]` | `__ABSENT__` (95%) | `c1ccncc1` (1%) | `__OTHER__` (1%) | set ✗ / any ✗ |

---

### Reaction #427  yield=87.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #15)

```
ClCCl.C=Cc1ccc(NC(C)=O)cc1>>CC(=O)Nc1ccc(C2CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (88.3%) | `sacrificial_zinc` (3.4%) | `sacrificial_magnesium` (2.6%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `graphite_generic` (44.1%) | `reticulated_vitreous_carbon` (34.0%) | `magnesium_plate` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `stainless_steel` | `carbon` (68.8%) | `platinum` (17.3%) | `stainless_steel` (8.6%) | ✓ |
| 阴极 (细类) | 49 | `stainless_steel_generic` | `graphite_generic` (54.8%) | `stainless_steel_generic` (15.7%) | `reticulated_vitreous_carbon` (8.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `divided` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (86.7%) | `Li` (3.9%) | `Na` (2.5%) | ✗ |
| 电解质 anion | 26 | `BF4` | `Cl` (78.0%) | `Br` (9.0%) | `molecular_no_ion` (4.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.1%) | `polyhalo_radical_transfer` (2.8%) | `secondary_amine` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (52.0%) | `Mn_complex` (11.6%) | `ammonium_PTC_organocat` (11.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (69.9%) | `cyclic_ether` (8.0%) | `aqueous` (6.8%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (97%) | `O` (15%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `BrCCBr` (3%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)[C@H]1COC(c2c` | `__ABSENT__` (93%) | `[Cl][Mn][Cl]` (2%) | `__OTHER__` (2%) | set ✗ / any ✗ |

---

### Reaction #428  yield=82.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #16)

```
ClCCl.C=CC(=O)Nc1ccccc1>>O=C(Nc1ccccc1)C1CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `graphite_generic` (72.1%) | `carbon_rod` (25.4%) | `reticulated_vitreous_carbon` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (82.7%) | `platinum` (12.3%) | `stainless_steel` (4.9%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `platinum_plate` (69.5%) | `graphite_generic` (21.7%) | `graphite_felt` (2.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (89.3%) | `NBu4` (10.5%) | `Li` (0.2%) | ✓ |
| 电解质 anion | 26 | `BF4` | `Cl` (67.0%) | `BF4` (28.9%) | `carboxylate` (2.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.7%) | `o2_oxidant` (4.9%) | `cyanide` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (98.8%) | `Mn_complex` (0.4%) | `ferrocene_mediator` (0.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (71.6%) | `cyclic_ether` (14.5%) | `polar_protic_alcohol` (5.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC(C)=O` (53%) | `CC#N` (43%) | `O` (17%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)[C@H]1COC(c2c` | `__ABSENT__` (99%) | `[Cl][Mn][Cl]` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #429  yield=84.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #17)

```
ClCCl.C=Cc1ccc(C(=O)OC)cc1>>COC(=O)c1ccc(C2CC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (86.2%) | `sacrificial_iron` (4.7%) | `ABSENT` (3.6%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `graphite_generic` (98.3%) | `iron_generic` (0.4%) | `reticulated_vitreous_carbon` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (80.4%) | `platinum` (9.7%) | `stainless_steel` (5.3%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `graphite_generic` (94.8%) | `stainless_steel_generic` (2.8%) | `reticulated_vitreous_carbon` (0.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (46.4%) | `NEt4` (38.9%) | `Na` (4.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Br` (34.3%) | `PF6` (16.3%) | `ClO4` (11.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.5%) | `secondary_amine` (2.2%) | `primary_amine` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `pyridine_organocat` | `ammonium_PTC_organocat` (38.9%) | `ABSENT` (33.0%) | `Fe_complex` (10.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (46.7%) | `cyclic_ether` (26.2%) | `ABSENT` (6.7%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (91%) | `CCOCC` (9%) | `FC(F)(F)c1ccccc1` (6%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (97%) | `O=O` (3%) | `OC(C(F)(F)F)C(F)(F` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)[C@H]1COC(c2c` + `__OTHER__` | `__OTHER__` (73%) | `c1ccncc1` (28%) | `CCCC[N+](CCCC)(CCC` (11%) | set ✗ / any ✓ |

---

### Reaction #430  yield=85.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #18)

```
ClCCl.C=C(c1ccccc1)C(F)(F)F>>FC(F)(F)C1(c2ccccc2)CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (75.3%) | `platinum` (23.2%) | `ABSENT` (0.6%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `platinum_generic` (33.0%) | `reticulated_vitreous_carbon` (25.2%) | `carbon_felt` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `platinum` (71.7%) | `carbon` (26.7%) | `ABSENT` (0.8%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `platinum_generic` (66.3%) | `platinum_plate` (8.0%) | `carbon_felt` (7.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (45.1%) | `divided` (27.9%) | `ABSENT` (27.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (53.7%) | `NBu4` (36.9%) | `NEt4` (7.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (82.1%) | `BF4` (10.3%) | `Cl` (3.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.1%) | `carboxylic_acid` (2.6%) | `polyhalo_radical_transfer` (2.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (93.9%) | `Mn_complex` (1.7%) | `Co_complex` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (85.1%) | `polar_protic_alcohol` (6.6%) | `cyclic_ether` (5.8%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (97%) | `O` (96%) | `CCCCn1cc[n+](C)c1.` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (80%) | `[Na+].[OH-]` (7%) | `F.c1ccncc1` (5%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)[C@H]1COC(c2c` | `__ABSENT__` (83%) | `[Pt]` (4%) | `CC(C)(C)c1cc(C=N[C` (4%) | set ✗ / any ✗ |

---

### Reaction #431  yield=86.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #19)

```
ClCCl.CCOC(=O)/C=C/c1ccc(F)c(F)c1>>CCOC(=O)C1CC1c1ccc(F)c(F)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (97.4%) | `sacrificial_iron` (1.4%) | `sacrificial_magnesium` (0.4%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `graphite_generic` (95.6%) | `carbon_rod` (1.6%) | `graphite_rod` (1.3%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `carbon` (99.1%) | `nickel` (0.5%) | `stainless_steel` (0.2%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `graphite_generic` (93.3%) | `graphite_rod` (4.9%) | `carbon_rod` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (64.8%) | `NBu4` (22.0%) | `ABSENT` (12.6%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (44.1%) | `ABSENT` (33.0%) | `Cl` (15.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (27.6%) | `hypervalent_iodine` (2.1%) | `polyhalo_radical_transfer` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (99.7%) | `Mn_complex` (0.1%) | `Fe_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (47.3%) | `ABSENT` (21.0%) | `cyclic_ether` (11.1%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (88%) | `ClCCl` (0%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)[C@H]1COC(c2c` + `__OTHER__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✗ / any ✗ |

---

### Reaction #432  yield=81.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #20)

```
ClCCl.C=CC(=O)O[C@@H]1C[C@H](C)CC[C@H]1C(C)C>>CC(C)[C@@H]1CC[C@@H](C)C[C@H]1OC(=O)C1CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (88.1%) | `platinum` (10.4%) | `sacrificial_zinc` (1.1%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `carbon_rod` (98.7%) | `graphite_generic` (0.4%) | `platinum_plate` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `nickel` (38.9%) | `carbon` (35.1%) | `platinum` (20.2%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `nickel_plate` (28.9%) | `platinum_plate` (28.0%) | `nickel_foam` (8.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NEt4` (51.3%) | `NBu4` (43.9%) | `ABSENT` (2.6%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `Cl` (52.4%) | `BF4` (41.4%) | `ClO4` (1.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.9%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (55.2%) | `polar_aprotic_amide` (20.6%) | `ketone` (9.6%) | ✓ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (54%) | `FC(F)(F)c1ccccc1` (1%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Br-][Ni+2]1([Br-]` + `CC(C)[C@H]1COC(c2c` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✓ |

---

### Reaction #433  yield=96.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_15_e202500203.json) (反应 idx 在该 JSON 内 = #21)

```
ClCCl.C=Cc1ccc(-c2ccccc2)cc1>>c1ccc(-c2ccc(C3CC3)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (51.7%) | `sacrificial_iron` (31.8%) | `sacrificial_magnesium` (7.2%) | ✗ |
| 阳极 (细类) | 43 | `stainless_steel_generic` | `reticulated_vitreous_carbon` (38.4%) | `graphite_generic` (14.8%) | `magnesium_plate` (12.0%) | ✗ |
| 阴极 (材料) | 15 | `copper` | `platinum` (57.8%) | `carbon` (18.3%) | `stainless_steel` (10.0%) | ✗ |
| 阴极 (细类) | 49 | `copper_generic` | `platinum_plate` (19.9%) | `stainless_steel_generic` (14.2%) | `platinum_foil` (13.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (40.5%) | `NEt4` (29.9%) | `Li` (11.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `Cl` (19.7%) | `Br` (16.7%) | `carboxylate` (15.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (5.3%) | `as_solvent_halogenated_aliphat` (3.9%) | `secondary_amine` (3.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `Fe_complex` (27.0%) | `Mn_complex` (26.0%) | `Cu_complex` (12.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (32.4%) | `polar_protic_acid` (19.4%) | `polar_aprotic_amide` (15.6%) | ✓ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `O` (79%) | `CC#N` (77%) | `CC(=O)O` (41%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (78%) | `OB(O)B(O)O` (48%) | `O=O` (29%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Br-][Ni+2]1([Br-]` + `CC(C)[C@H]1COC(c2c` | `COCCOC.[Br][Ni][Br` (87%) | `[Cl][Fe]([Cl])[Cl]` (4%) | `c1ccncc1` (4%) | set ✗ / any ✗ |

---

### Reaction #434  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #435  yield=39.0%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #436  yield=13.0%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #437  yield=88.0%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #438  yield=0.5%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #439  yield=41.0%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #440  yield=0.5%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #441  yield=59.0%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #442  yield=74.0%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #443  yield=73.0%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✓ |
| 电解质 anion | 26 | `Cl` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #444  yield=75.0%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #445  yield=66.0%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #446  yield=67.0%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #447  yield=61.0%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #448  yield=0.0%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #449  yield=66.0%

**Source paper**: [`Angew/10.1002_anie.202501424_p3_t0.json`](reactions_by_journal_alkene_ec_audited/Angew/10.1002_anie.202501424_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccccc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.0%) | `platinum` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (39.3%) | `unknown_electrode` (16.5%) | `reticulated_vitreous_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.0%) | `nickel` (15.5%) | `sacrificial_iron` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (1.7%) | `nickel_generic` (1.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (83.9%) | `ABSENT` (15.5%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (67.0%) | `NBu4` (28.2%) | `Li` (2.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (50.7%) | `PF6` (22.2%) | `ClO4` (18.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.7%) | `amide` (3.3%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (49.5%) | `ferrocene_mediator` (9.3%) | `V_complex` (7.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.9%) | `cyclic_ether` (5.2%) | `polar_aprotic_sulfoxide` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (89%) | `O` (34%) | `CO` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (95%) | `O=S(=O)([O-])C(F)(` (4%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (79%) | `[Fe+2].c1cc[cH-]c1` (12%) | `CC(=O)NC1CC2(CCCCC` (7%) | set ✓ / any ✓ |

---

### Reaction #450  yield=22.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccc1.Cc1ccc(S(=O)(=O)NCCCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCCCOC(C)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (70.3%) | `graphite_rod` (22.8%) | `carbon_generic` (2.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (71.1%) | `nickel` (23.8%) | `sacrificial_iron` (2.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (75.8%) | `platinum_generic` (13.2%) | `nickel_generic` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (93.7%) | `Li` (3.3%) | `ABSENT` (2.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (78.2%) | `PF6` (11.0%) | `ClO4` (6.4%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (14.6%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (47.2%) | `triarylamine_radical_cat` (16.5%) | `organic_neutral_cat` (16.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (97.1%) | `polar_aprotic_amide` (0.8%) | `ABSENT` (0.6%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `CO` (1%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #451  yield=24.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #1)

```
Cc1ccc(S(=O)(=O)NCCCO)cc1.C=C(C)c1cccc(OC)c1>>COc1cccc(C2(C)CN(S(=O)(=O)c3ccc(C)cc3)CCCO2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (73.5%) | `graphite_rod` (23.8%) | `carbon_generic` (1.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (78.4%) | `nickel` (16.4%) | `sacrificial_iron` (3.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (46.3%) | `nickel_generic` (40.2%) | `platinum_generic` (4.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (39.8%) | `Li` (33.8%) | `ABSENT` (11.6%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (37.4%) | `molecular_no_ion` (26.8%) | `ClO4` (16.5%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (11.4%) | `boron_lewis_acid` (2.9%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.8%) | `ferrocene_mediator` (5.9%) | `pyridine_organocat` (5.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (92.9%) | `polar_protic_alcohol` (3.1%) | `ABSENT` (1.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `CO` (4%) | `O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=P([O-])([O-])O.[` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #452  yield=29.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #2)

```
C=C(C)c1ccccc1Cl.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3Cl)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (36.2%) | `graphite_generic` (27.0%) | `graphite_rod` (17.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (76.7%) | `nickel` (19.2%) | `carbon` (4.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (64.7%) | `nickel_foam` (18.8%) | `platinum_plate` (5.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (84.1%) | `ABSENT` (15.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `K` (39.3%) | `NBu4` (36.1%) | `Li` (10.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `PF6` (82.9%) | `Br` (6.8%) | `ABSENT` (3.3%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (18.7%) | `primary_amine` (3.2%) | `as_solvent_halogenated_aliphat` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.9%) | `pyridine_organocat` (3.4%) | `organic_neutral_cat` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.4%) | `ABSENT` (0.6%) | `polar_aprotic_sulfoxide` (0.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (97%) | `O` (1%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Br][Mn][Br]` (0%) | set ✓ / any ✓ |

---

### Reaction #453  yield=28.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #3)

```
C=C(C)c1cccc(C(F)(F)F)c1.Cc1ccc(S(=O)(=O)NCCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCCOC(C)(c3cccc(C(F)(F)F)c3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (91.4%) | `graphite_rod` (6.8%) | `carbon_generic` (1.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.7%) | `carbon` (3.0%) | `nickel` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (80.6%) | `platinum_generic` (14.5%) | `nickel_generic` (2.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (71.9%) | `Li` (13.0%) | `NEt4` (8.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `PF6` (32.4%) | `BF4` (29.0%) | `ClO4` (26.6%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (10.9%) | `ammonium_salt` (9.5%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (65.9%) | `triarylamine_radical_cat` (9.5%) | `ferrocene_mediator` (9.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (94.0%) | `cyclic_ether` (1.4%) | `polar_protic_alcohol` (1.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (95%) | `CO` (9%) | `O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `O=P([O-])([O-])O.[` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #454  yield=30.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #4)

```
C=CCOC=C.Cc1ccc(S(=O)(=O)NCCO)cc1>>C=CCOC1CN(S(=O)(=O)c2ccc(C)cc2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (34.1%) | `carbon_generic` (26.3%) | `graphite_rod` (20.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.3%) | `carbon` (2.5%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (95.0%) | `platinum_plate` (3.8%) | `platinum_wire` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (56.7%) | `ABSENT` (43.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (61.7%) | `NEt4` (20.4%) | `NBu4` (11.6%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (52.0%) | `ClO4` (39.2%) | `molecular_no_ion` (3.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (20.7%) | `tellurium_reagent` (2.1%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.2%) | `organic_neutral_cat` (0.8%) | `ammonium_PTC_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (91.7%) | `polar_protic_alcohol` (3.9%) | `ABSENT` (1.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (22%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `Cl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #455  yield=30.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #5)

```
C=C(C)c1cccc(C(F)(F)F)c1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3cccc(C(F)(F)F)c3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (82.8%) | `carbon_generic` (10.5%) | `graphite_rod` (4.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.6%) | `carbon` (2.6%) | `nickel` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (83.3%) | `platinum_plate` (10.9%) | `platinum_foil` (2.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.6%) | `ABSENT` (2.2%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (47.3%) | `ABSENT` (25.5%) | `NBu4` (10.7%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (41.5%) | `ABSENT` (20.7%) | `ClO4` (19.0%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (10.8%) | `ammonium_salt` (6.7%) | `primary_amine` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (87.5%) | `pyridine_organocat` (3.3%) | `triarylamine_radical_cat` (2.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (94.4%) | `ABSENT` (1.4%) | `cyclic_ether` (1.2%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (86%) | `O` (27%) | `CO` (11%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O=P([O-])([O-])O.[` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #456  yield=34.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #6)

```
C=COCc1ccccc1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(OCc3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (49.5%) | `graphite_rod` (35.8%) | `graphite_generic` (10.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.6%) | `carbon` (0.9%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `platinum_plate` (0.4%) | `nickel_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (58.2%) | `undivided` (41.8%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `Li` (41.3%) | `NBu4` (40.7%) | `Na` (6.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (62.0%) | `ClO4` (18.4%) | `molecular_no_ion` (5.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (42.1%) | `metal_oxide_oxidant` (1.8%) | `tellurium_reagent` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.6%) | `pyridine_organocat` (1.5%) | `ammonium_PTC_organocat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (94.0%) | `polar_protic_alcohol` (3.5%) | `cyclic_ether` (1.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (15%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O=C(O)O.[Na]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #457  yield=33.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #7)

```
C=Cc1ccc(C(C)(C)C)cc1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(c3ccc(C(C)(C)C)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.6%) | `platinum` (5.0%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (45.6%) | `graphite_generic` (21.7%) | `graphite_rod` (16.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.9%) | `carbon` (2.2%) | `sacrificial_iron` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (90.2%) | `platinum_plate` (8.8%) | `graphite_rod` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (58.4%) | `ABSENT` (41.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (35.7%) | `Li` (24.8%) | `NBu4` (16.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (51.4%) | `I` (18.4%) | `molecular_no_ion` (12.5%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (16.4%) | `primary_amine` (2.3%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.7%) | `organic_neutral_cat` (1.5%) | `pyridine_organocat` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.3%) | `cyclic_ether` (0.9%) | `ABSENT` (0.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (4%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #458  yield=33.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #8)

```
C=Cc1ccc(Cl)cc1.Cc1ccc(S(=O)(=O)NCCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCCOC(c3ccc(Cl)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `reticulated_vitreous_carbon` (87.8%) | `graphite_rod` (6.7%) | `carbon_generic` (2.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.5%) | `carbon` (0.3%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.1%) | `platinum_generic` (3.8%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `ABSENT` (0.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (58.2%) | `NEt4` (13.4%) | `Na` (12.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `I` (24.9%) | `BF4` (22.6%) | `PF6` (19.3%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (17.5%) | `ammonium_salt` (3.7%) | `as_solvent_halogenated_aliphat` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.9%) | `organic_neutral_cat` (3.8%) | `triarylamine_radical_cat` (3.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (96.1%) | `polar_protic_alcohol` (1.7%) | `cyclic_ether` (0.7%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (1%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=P([O-])([O-])O.[` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #459  yield=31.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #9)

```
C=Cc1ccccc1Cl.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(c3ccc(Cl)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (70.8%) | `graphite_generic` (10.1%) | `reticulated_vitreous_carbon` (9.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `nickel` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (60.9%) | `platinum_generic` (38.3%) | `nickel_foam` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (68.0%) | `undivided` (32.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (32.4%) | `Li` (19.5%) | `ABSENT` (17.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (52.5%) | `ClO4` (18.2%) | `ABSENT` (12.8%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (13.9%) | `alkali_other_salt` (5.7%) | `ammonium_salt` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (37.2%) | `ABSENT` (33.6%) | `organic_neutral_cat` (11.7%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (93.0%) | `ketone` (2.4%) | `polar_protic_alcohol` (2.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (88%) | `CC(C)=O` (8%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (22%) | `[Br-][Ni+2]1([Br-]` (7%) | `Cc1cc(C)cc(-n2c3cc` (3%) | set ✗ / any ✓ |

---

### Reaction #460  yield=32.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #10)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccc(C(=O)OC)cc1>>COC(=O)c1ccc(C2(C)CN(S(=O)(=O)c3ccc(C)cc3)CCO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `reticulated_vitreous_carbon` (57.6%) | `graphite_rod` (20.3%) | `graphite_generic` (16.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (68.1%) | `nickel` (25.4%) | `carbon` (5.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (41.6%) | `platinum_plate` (27.8%) | `nickel_foam` (11.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (55.3%) | `ABSENT` (44.6%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (53.7%) | `K` (24.3%) | `Li` (15.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `PF6` (45.5%) | `I` (18.4%) | `BF4` (13.6%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (13.1%) | `primary_amine` (4.1%) | `as_solvent_halogenated_aliphat` (4.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.0%) | `Fe_complex` (8.5%) | `pyridine_organocat` (3.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.1%) | `polar_protic_alcohol` (0.6%) | `ABSENT` (0.6%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (3%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=P([O-])([O-])[O-` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br][Mn][Br]` (0%) | set ✓ / any ✓ |

---

### Reaction #461  yield=36.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #11)

```
C=C(C)c1ccccc1.N#Cc1ccc(S(=O)(=O)NCCO)cc1>>CC1(c2ccccc2)CN(S(=O)(=O)c2ccc(C#N)cc2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (76.6%) | `carbon_cloth` (12.9%) | `reticulated_vitreous_carbon` (8.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.4%) | `carbon` (6.7%) | `sacrificial_iron` (3.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (48.7%) | `platinum_plate` (36.1%) | `platinum_foil` (3.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (31.5%) | `ABSENT` (26.9%) | `NBu4` (20.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (39.9%) | `ABSENT` (22.7%) | `molecular_no_ion` (11.4%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.9%) | `o2_oxidant` (2.5%) | `primary_amine` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (45.0%) | `pyridine_organocat` (43.2%) | `Fe_complex` (2.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (92.9%) | `ABSENT` (3.8%) | `ketone` (1.6%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (92%) | `CC(C)=O` (1%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[O]=[Ti]=[O]` (0%) | set ✓ / any ✓ |

---

### Reaction #462  yield=47.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #12)

```
C=Cc1cccc(Cl)c1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(c3cccc(Cl)c3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `unknown_electrode` (51.8%) | `carbon_generic` (27.7%) | `reticulated_vitreous_carbon` (6.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (82.1%) | `platinum_plate` (17.8%) | `reticulated_vitreous_carbon` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (56.7%) | `ABSENT` (43.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (71.5%) | `NBu4` (18.0%) | `Li` (6.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (72.6%) | `molecular_no_ion` (11.7%) | `PF6` (5.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (14.8%) | `tellurium_reagent` (2.3%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (50.8%) | `pyridine_organocat` (29.1%) | `organic_neutral_cat` (15.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (93.5%) | `ketone` (1.8%) | `halogenated_aliphatic` (1.7%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (1%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `N#Cc1c(C#N)c(-n2c3` (0%) | set ✓ / any ✓ |

---

### Reaction #463  yield=46.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #13)

```
C=COCc1ccccc1.Cc1ccc(S(=O)(=O)NCCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCCOC(OCc3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (66.3%) | `graphite_generic` (25.9%) | `carbon_generic` (4.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `carbon` (0.8%) | `nickel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (71.7%) | `platinum_plate` (27.3%) | `nickel_generic` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (51.8%) | `Na` (25.9%) | `Li` (8.9%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (68.0%) | `I` (18.2%) | `molecular_no_ion` (4.1%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (41.6%) | `as_solvent_halogenated_aliphat` (1.9%) | `metal_oxide_oxidant` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (48.5%) | `ammonium_PTC_organocat` (42.8%) | `ferrocene_mediator` (2.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (66.8%) | `polar_protic_alcohol` (28.4%) | `cyclic_ether` (2.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (4%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #464  yield=46.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #14)

```
C=COCCCC.Cc1ccc(S(=O)(=O)NCCCO)cc1>>CCCCOC1CN(S(=O)(=O)c2ccc(C)cc2)CCCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (85.1%) | `graphite_generic` (9.8%) | `carbon_generic` (2.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.4%) | `carbon` (9.0%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (59.8%) | `platinum_generic` (31.6%) | `graphite_plate` (5.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `K` | `NBu4` (80.8%) | `NEt4` (13.0%) | `ABSENT` (2.7%) | ✗ |
| 电解质 anion | 26 | `OH` | `BF4` (95.3%) | `PF6` (1.7%) | `I` (1.0%) | ✗ |
| 试剂大类 | 103 | `boron_lewis_acid` | `ABSENT` (24.9%) | `as_solvent_halogenated_aliphat` (2.4%) | `as_solvent_polar_protic_alcoho` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ammonium_PTC_organocat` (64.2%) | `ABSENT` (31.8%) | `ferrocene_mediator` (2.6%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (52.3%) | `polar_protic_alcohol` (41.1%) | `ABSENT` (3.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC[N+](CC)(CC)CC.F` + `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `[N-]=[N+]=[N-].[Na` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (49%) | `CCCC[N+](CCCC)(CCC` (42%) | `CC[N+](CC)(CC)CC.F` (4%) | set ✓ / any ✓ |

---

### Reaction #465  yield=45.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #15)

```
C=COCCCl.Cc1ccc(S(=O)(=O)NCCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCCOC(OCCCl)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (50.9%) | `graphite_rod` (33.1%) | `carbon_generic` (9.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `carbon` (6.6%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (48.7%) | `platinum_generic` (48.4%) | `graphite_generic` (1.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (54.1%) | `NEt4` (37.2%) | `Li` (3.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (90.5%) | `PF6` (3.1%) | `ClO4` (1.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (33.0%) | `as_solvent_halogenated_aliphat` (2.3%) | `metal_oxide_oxidant` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (71.7%) | `ammonium_PTC_organocat` (20.2%) | `ferrocene_mediator` (3.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (88.6%) | `polar_protic_alcohol` (10.0%) | `cyclic_ether` (0.8%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (5%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `[N-]=[N+]=[N-].[Na` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #466  yield=43.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #16)

```
C=COCC(C)C.Cc1ccc(S(=O)(=O)NCCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCCOC(OCC(C)C)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (41.4%) | `graphite_generic` (36.2%) | `reticulated_vitreous_carbon` (15.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.5%) | `carbon` (4.8%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (85.7%) | `platinum_generic` (12.5%) | `nickel_generic` (0.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `ABSENT` (0.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (51.0%) | `NBu4` (45.7%) | `ABSENT` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (93.4%) | `PF6` (4.1%) | `ClO4` (1.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (15.4%) | `as_solvent_polar_aprotic_sulfo` (2.3%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (65.4%) | `ammonium_PTC_organocat` (25.1%) | `ferrocene_mediator` (6.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (59.7%) | `polar_protic_alcohol` (25.5%) | `ABSENT` (7.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (17%) | `CO` (12%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #467  yield=45.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #17)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(c1ccccc1)C1CCCC1>>Cc1ccc(S(=O)(=O)N2CCOC(c3ccccc3)(C3CCCC3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (95.5%) | `carbon_cloth` (1.7%) | `reticulated_vitreous_carbon` (1.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.1%) | `stainless_steel` (6.4%) | `nickel` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (52.6%) | `platinum_generic` (32.0%) | `stainless_steel_generic` (12.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (79.5%) | `ABSENT` (20.1%) | `divided` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (56.7%) | `NBu4` (20.2%) | `K` (7.7%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (33.6%) | `ClO4` (30.9%) | `PF6` (15.5%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (11.0%) | `carboxylic_acid` (3.9%) | `inorganic_simple` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.5%) | `main_group_lewis_acid` (0.6%) | `pyridine_organocat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (96.6%) | `polar_protic_alcohol` (2.5%) | `ABSENT` (0.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `CO` (0%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #468  yield=46.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #18)

```
C=C(C)c1ccc(F)cc1.Cc1ccc(S(=O)(=O)NCCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCCOC(C)(c3ccc(F)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (53.2%) | `reticulated_vitreous_carbon` (37.6%) | `graphite_generic` (5.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.7%) | `nickel` (1.9%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (97.6%) | `platinum_generic` (2.1%) | `nickel_generic` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (71.4%) | `NEt4` (15.6%) | `ABSENT` (5.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (38.2%) | `PF6` (22.1%) | `I` (14.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (11.3%) | `as_solvent_halogenated_aliphat` (2.8%) | `primary_amine` (2.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (78.6%) | `pyridine_organocat` (3.6%) | `ammonium_PTC_organocat` (2.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.4%) | `polar_protic_alcohol` (0.3%) | `ABSENT` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (33%) | `CO` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #469  yield=46.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #19)

```
C=C(C)c1ccccc1.Cc1ccc(S(=O)(=O)NCC(C)(C)O)cc1>>Cc1ccc(S(=O)(=O)N2CC(C)(C)OC(C)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (31.8%) | `carbon_felt` (28.1%) | `graphite_generic` (19.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.5%) | `nickel` (12.8%) | `sacrificial_iron` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (90.4%) | `platinum_generic` (7.5%) | `nickel_generic` (1.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (85.9%) | `Li` (12.3%) | `K` (1.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (80.9%) | `BF4` (14.9%) | `Br` (2.9%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `azide_source` (5.1%) | `ABSENT` (5.0%) | `alkali_sulfinate` (4.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `ferrocene_mediator` (0.1%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (97.3%) | `polar_protic_alcohol` (1.7%) | `polar_aprotic_sulfoxide` (0.8%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (99%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `C[Si](C)(C)N=[N+]=` (67%) | `O=O` (7%) | `[N-]=[N+]=[N-].[Na` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (96%) | `[Fe+2].c1cc[cH-]c1` (2%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✓ / any ✓ |

---

### Reaction #470  yield=41.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #20)

```
C=C(C)c1ccccc1.Cc1ccc(S(=O)(=O)NCC(C)O)cc1>>Cc1ccc(S(=O)(=O)N2C[C@@H](C)O[C@](C)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (48.5%) | `graphite_generic` (43.6%) | `carbon_rod` (4.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (75.9%) | `carbon` (10.6%) | `nickel` (8.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (71.8%) | `platinum_plate` (23.6%) | `graphite_generic` (1.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (72.8%) | `Li` (20.3%) | `K` (2.3%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (81.8%) | `ClO4` (10.7%) | `molecular_no_ion` (5.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `o2_oxidant` (5.7%) | `hydrosilane` (5.3%) | `azide_source` (3.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.3%) | `Mn_complex` (17.3%) | `triarylamine_radical_cat` (3.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.8%) | `polar_protic_alcohol` (1.0%) | `ABSENT` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (72%) | `CO` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `O=O` (93%) | `C[Si](C)(C)N=[N+]=` (1%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `CC(=O)NC1CC2(CCCCC` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #471  yield=41.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #21)

```
C=C(C)c1ccccc1.Cc1ccc(S(=O)(=O)NCC(C)O)cc1>>Cc1ccc(S(=O)(=O)N2C[C@H](C)O[C@](C)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (48.5%) | `graphite_generic` (43.6%) | `carbon_rod` (4.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (75.9%) | `carbon` (10.6%) | `nickel` (8.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (71.8%) | `platinum_plate` (23.6%) | `graphite_generic` (1.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (72.8%) | `Li` (20.3%) | `K` (2.3%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (81.8%) | `ClO4` (10.7%) | `molecular_no_ion` (5.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `o2_oxidant` (5.7%) | `hydrosilane` (5.3%) | `azide_source` (3.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (72.3%) | `Mn_complex` (17.3%) | `triarylamine_radical_cat` (3.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.8%) | `polar_protic_alcohol` (1.0%) | `ABSENT` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (72%) | `CO` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `O=O` (93%) | `C[Si](C)(C)N=[N+]=` (1%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `CC(=O)NC1CC2(CCCCC` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #472  yield=49.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #22)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(CCCC)c1ccccc1>>CCCCC1(c2ccccc2)CN(S(=O)(=O)c2ccc(C)cc2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `ABSENT` (0.4%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (38.5%) | `graphite_rod` (35.7%) | `graphite_generic` (12.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (58.7%) | `platinum` (39.5%) | `carbon` (0.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (63.0%) | `nickel_generic` (32.8%) | `nickel_foam` (1.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (90.5%) | `ABSENT` (9.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (70.6%) | `K` (11.6%) | `Na` (8.4%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (37.0%) | `molecular_no_ion` (20.5%) | `Br` (14.0%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (22.7%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.8%) | `ferrocene_mediator` (2.3%) | `organic_neutral_cat` (2.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (63.9%) | `cyclic_ether` (11.1%) | `ABSENT` (5.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (91%) | `O` (2%) | `CO` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `[Br-].[Na+]` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #473  yield=50.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #23)

```
C=C(C)c1ccccc1.O=S(=O)(NCCO)c1ccc(-c2ccccc2)cc1>>CC1(c2ccccc2)CN(S(=O)(=O)c2ccc(-c3ccccc3)cc2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (52.9%) | `graphite_generic` (21.1%) | `reticulated_vitreous_carbon` (9.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.5%) | `nickel` (0.8%) | `sacrificial_iron` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (83.6%) | `platinum_plate` (15.7%) | `platinum_foil` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (61.1%) | `Li` (19.9%) | `K` (13.7%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (32.3%) | `ClO4` (26.4%) | `I` (17.5%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (10.0%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (83.3%) | `organic_neutral_cat` (3.9%) | `Fe_complex` (2.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (92.8%) | `polar_protic_alcohol` (1.6%) | `ketone` (1.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (95%) | `O` (55%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #474  yield=48.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #24)

```
C=Cc1ccc(CCl)cc1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(c3ccc(CCl)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (92.9%) | `graphite_felt` (2.6%) | `graphite_generic` (1.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `sacrificial_iron` (0.6%) | `carbon` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (94.7%) | `platinum_plate` (4.8%) | `iron_generic` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (91.2%) | `undivided` (8.8%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `ABSENT` (46.4%) | `Li` (32.0%) | `NBu4` (14.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (60.5%) | `ClO4` (16.0%) | `BF4` (9.9%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (21.5%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (77.9%) | `organic_neutral_cat` (10.3%) | `pyridine_organocat` (4.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (96.9%) | `ketone` (1.7%) | `cyclic_ether` (0.8%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (93%) | `O` (71%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC1CCCC(C)N1C1C(N2` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #475  yield=47.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #25)

```
C=COCC.Cc1ccc(S(=O)(=O)NCCCO)cc1>>CCOC1CN(S(=O)(=O)c2ccc(C)cc2)CCCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (64.5%) | `graphite_rod` (11.6%) | `carbon_generic` (11.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (69.3%) | `carbon` (28.5%) | `nickel` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (41.3%) | `platinum_plate` (22.4%) | `graphite_plate` (14.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (49.2%) | `NBu4` (29.0%) | `NEt4` (15.8%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (59.1%) | `ClO4` (32.5%) | `molecular_no_ion` (4.1%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (11.4%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (54.9%) | `ammonium_PTC_organocat` (42.7%) | `ferrocene_mediator` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (57.4%) | `polar_protic_alcohol` (34.3%) | `cyclic_ether` (3.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (46%) | `CO` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (99%) | `C[Si](C)(C)N=[N+]=` (0%) | `Cl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (1%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #476  yield=52.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #26)

```
C=COCCC.Cc1ccc(S(=O)(=O)NCCCO)cc1>>CCCOC1CN(S(=O)(=O)c2ccc(C)cc2)CCCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (78.8%) | `graphite_generic` (18.8%) | `reticulated_vitreous_carbon` (1.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.2%) | `carbon` (12.6%) | `nickel` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (95.6%) | `graphite_generic` (1.5%) | `platinum_generic` (1.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (68.5%) | `NEt4` (30.7%) | `Li` (0.4%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (93.3%) | `ClO4` (3.5%) | `PF6` (2.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (23.9%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (63.6%) | `ammonium_PTC_organocat` (33.8%) | `ferrocene_mediator` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_alcohol` (57.5%) | `polar_aprotic_nitrile` (38.7%) | `ABSENT` (1.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (85%) | `CO` (14%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `[N-]=[N+]=[N-].[Na` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CC[N+](CC)(CC)CC.F` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #477  yield=59.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #27)

```
C=Cc1ccc(F)cc1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(c3ccc(F)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `ABSENT` (0.2%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (41.7%) | `reticulated_vitreous_carbon` (32.0%) | `graphite_rod` (18.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `carbon` (0.3%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (62.3%) | `platinum_plate` (37.2%) | `platinum_foil` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (72.1%) | `undivided` (27.9%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Li` (26.8%) | `NBu4` (20.0%) | `Na` (19.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (35.2%) | `ClO4` (33.6%) | `I` (12.0%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (14.3%) | `primary_amine` (2.4%) | `diboron` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (84.5%) | `pyridine_organocat` (6.2%) | `organic_neutral_cat` (2.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.7%) | `ABSENT` (0.9%) | `polar_protic_alcohol` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (10%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (99%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #478  yield=59.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #28)

```
C=Cc1ccc(Br)cc1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(c3ccc(Br)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (0.7%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (77.4%) | `graphite_rod` (14.8%) | `reticulated_vitreous_carbon` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.0%) | `sacrificial_iron` (0.4%) | `carbon` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (79.1%) | `platinum_plate` (20.5%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (83.3%) | `undivided` (16.7%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (49.0%) | `Li` (17.5%) | `K` (13.4%) | ✗ |
| 电解质 anion | 26 | `BF4` | `I` (30.1%) | `ClO4` (28.4%) | `PF6` (23.4%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (23.5%) | `primary_amine` (2.5%) | `metal_oxide_oxidant` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.9%) | `pyridine_organocat` (1.9%) | `organic_neutral_cat` (1.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.0%) | `cyclic_ether` (0.2%) | `halogenated_aliphatic` (0.2%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (49%) | `ClCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #479  yield=51.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #29)

```
C=Cc1cccc(Br)c1.Cc1ccc(S(=O)(=O)NCCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCCOC(c3cccc(Br)c3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (56.2%) | `carbon_generic` (24.2%) | `graphite_generic` (14.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `nickel` (0.4%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (97.1%) | `platinum_generic` (2.8%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (60.6%) | `K` (12.1%) | `NH4` (7.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `PF6` (65.0%) | `I` (18.7%) | `molecular_no_ion` (5.4%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `alkali_sulfinate` (14.3%) | `ABSENT` (12.3%) | `primary_amine` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (67.4%) | `pyridine_organocat` (20.4%) | `ammonium_PTC_organocat` (3.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (93.9%) | `ABSENT` (2.2%) | `cyclic_ether` (1.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (97%) | `O` (78%) | `CO` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (64%) | `C[Si](C)(C)N=[N+]=` (14%) | `O=S([O-])O.[Na+]` (13%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #480  yield=53.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #30)

```
C=COCC(C)C.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(OCC(C)C)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (48.0%) | `graphite_rod` (31.2%) | `graphite_generic` (11.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.1%) | `carbon` (4.9%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (88.4%) | `platinum_plate` (10.1%) | `unknown_electrode` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (85.7%) | `undivided` (14.2%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NEt4` (46.3%) | `NBu4` (33.9%) | `Li` (10.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (79.8%) | `ClO4` (10.6%) | `PF6` (5.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (11.6%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.0%) | `ammonium_PTC_organocat` (0.7%) | `organic_neutral_cat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (85.1%) | `polar_protic_alcohol` (6.0%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (97%) | `O` (59%) | `CO` (6%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #481  yield=56.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #31)

```
C=C(Cc1ccccc1)c1ccccc1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(Cc3ccccc3)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (90.4%) | `graphite_generic` (4.9%) | `unknown_electrode` (2.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (54.2%) | `platinum` (40.7%) | `carbon` (2.9%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (82.0%) | `nickel_generic` (17.2%) | `nickel_foam` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (52.3%) | `ABSENT` (47.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (65.2%) | `K` (19.0%) | `NBu4` (7.1%) | ✗ |
| 电解质 anion | 26 | `BF4` | `molecular_no_ion` (20.1%) | `carboxylate` (19.9%) | `ClO4` (18.3%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (36.3%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.6%) | `organic_neutral_cat` (0.3%) | `ionic_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (72.2%) | `polar_protic_alcohol` (12.7%) | `cyclic_ether` (6.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (97%) | `O` (16%) | `CO` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (99%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #482  yield=52.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #32)

```
C=C(C)c1ccccc1.Cc1ccc(S(=O)(=O)NCCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCCOC(C)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (61.3%) | `graphite_rod` (27.7%) | `reticulated_vitreous_carbon` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.6%) | `nickel` (8.6%) | `sacrificial_iron` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (86.6%) | `platinum_generic` (9.7%) | `nickel_generic` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (85.6%) | `K` (6.4%) | `Li` (3.6%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (58.5%) | `PF6` (20.2%) | `ClO4` (8.3%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (10.6%) | `as_solvent_halogenated_aliphat` (3.5%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (58.8%) | `triarylamine_radical_cat` (9.1%) | `ferrocene_mediator` (7.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (92.3%) | `polar_protic_alcohol` (2.8%) | `polar_aprotic_sulfoxide` (1.6%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (20%) | `CO` (4%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=S([O-])O.[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #483  yield=63.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #33)

```
C=COCCCl.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(OCCCl)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (73.0%) | `graphite_rod` (15.0%) | `graphite_generic` (9.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.4%) | `carbon` (6.5%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.8%) | `platinum_plate` (2.6%) | `graphite_plate` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (90.9%) | `ABSENT` (9.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (51.0%) | `Li` (25.9%) | `NEt4` (19.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (80.7%) | `ClO4` (11.2%) | `PF6` (3.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (26.6%) | `tellurium_reagent` (2.2%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.8%) | `ammonium_PTC_organocat` (1.0%) | `Fe_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.1%) | `polar_protic_alcohol` (1.3%) | `cyclic_ether` (0.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (63%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #484  yield=66.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #34)

```
C=COCCCC.Cc1ccc(S(=O)(=O)NCCO)cc1>>CCCCOC1CN(S(=O)(=O)c2ccc(C)cc2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (67.8%) | `carbon_generic` (27.6%) | `unknown_electrode` (1.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (77.0%) | `carbon` (21.3%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (94.0%) | `graphite_plate` (2.6%) | `platinum_plate` (1.2%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (58.2%) | `undivided` (41.8%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (77.2%) | `NEt4` (6.9%) | `ABSENT` (6.6%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (88.4%) | `ClO4` (3.7%) | `ABSENT` (3.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (24.0%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.8%) | `ammonium_PTC_organocat` (6.7%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (83.5%) | `polar_protic_alcohol` (11.9%) | `ABSENT` (1.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (16%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #485  yield=69.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #35)

```
C=COCCC.Cc1ccc(S(=O)(=O)NCCO)cc1>>CCCOC1CN(S(=O)(=O)c2ccc(C)cc2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (94.9%) | `graphite_generic` (3.5%) | `graphite_plate` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.6%) | `carbon` (14.0%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (86.6%) | `platinum_generic` (8.6%) | `graphite_rod` (1.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (70.7%) | `NEt4` (27.1%) | `Li` (1.9%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (89.1%) | `ClO4` (8.6%) | `PF6` (1.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (23.8%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.3%) | `ammonium_PTC_organocat` (3.6%) | `main_group_lewis_acid` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (75.3%) | `polar_protic_alcohol` (22.7%) | `ABSENT` (0.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (24%) | `CCO` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC[N+](CC)(CC)CC.F` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #486  yield=62.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #36)

```
C=COC(C)(C)C.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(OC(C)(C)C)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `ABSENT` (0.3%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (50.7%) | `graphite_rod` (36.0%) | `graphite_generic` (11.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.8%) | `nickel` (10.9%) | `carbon` (4.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (85.3%) | `nickel_generic` (7.9%) | `platinum_plate` (3.3%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (79.4%) | `undivided` (20.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (63.6%) | `Li` (19.1%) | `NEt4` (13.9%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (82.8%) | `ClO4` (7.3%) | `I` (4.0%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (19.0%) | `tellurium_reagent` (2.2%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.3%) | `ferrocene_mediator` (0.5%) | `ammonium_PTC_organocat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (93.5%) | `polar_protic_alcohol` (4.3%) | `cyclic_ether` (0.8%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (20%) | `CO` (10%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #487  yield=64.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #37)

```
C=Cc1ccc(C(F)(F)F)cc1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(c3ccc(C(F)(F)F)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.0%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (72.8%) | `unknown_electrode` (12.6%) | `graphite_generic` (8.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.1%) | `carbon` (1.2%) | `sacrificial_iron` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (91.3%) | `platinum_plate` (8.3%) | `unknown_electrode` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (66.3%) | `undivided` (33.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (68.7%) | `ABSENT` (13.0%) | `Li` (6.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `PF6` (33.5%) | `ClO4` (27.0%) | `BF4` (18.2%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (16.6%) | `alkali_sulfinate` (2.5%) | `primary_amine` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (73.7%) | `pyridine_organocat` (18.2%) | `organic_neutral_cat` (4.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (95.5%) | `ABSENT` (1.2%) | `cyclic_ether` (1.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `ClCCl` (6%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (99%) | `CCN(CC)CC.F.F.F` (1%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #488  yield=61.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #38)

```
C=COCC.Cc1ccc(S(=O)(=O)NCCO)cc1>>CCOC1CN(S(=O)(=O)c2ccc(C)cc2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `ABSENT` (0.2%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (84.6%) | `graphite_generic` (6.8%) | `graphite_rod` (3.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (61.6%) | `carbon` (35.1%) | `ABSENT` (1.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (85.6%) | `graphite_plate` (4.2%) | `unknown_electrode` (2.4%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (76.9%) | `undivided` (23.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Li` (87.8%) | `NBu4` (6.1%) | `NEt4` (3.6%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (75.1%) | `BF4` (19.1%) | `molecular_no_ion` (3.9%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.0%) | `electrophilic_N_F` (2.5%) | `aldehyde` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.3%) | `ammonium_PTC_organocat` (1.8%) | `pyridine_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (88.1%) | `polar_protic_alcohol` (7.3%) | `cyclic_ether` (1.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (93%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (97%) | `Cl` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #489  yield=69.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #39)

```
C=C(C)c1ccc(F)cc1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccc(F)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `reticulated_vitreous_carbon` (63.2%) | `graphite_rod` (22.8%) | `graphite_generic` (6.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.9%) | `nickel` (3.4%) | `carbon` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (59.5%) | `platinum_generic` (36.9%) | `platinum_foil` (1.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (93.6%) | `ABSENT` (6.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (42.5%) | `NBu4` (28.1%) | `K` (13.1%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (38.3%) | `molecular_no_ion` (21.6%) | `I` (11.2%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (9.7%) | `primary_amine` (3.0%) | `as_solvent_halogenated_aliphat` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.8%) | `pyridine_organocat` (3.1%) | `Fe_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.5%) | `ABSENT` (0.2%) | `polar_protic_alcohol` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (55%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `Cl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[I-].[Li+]` (0%) | set ✓ / any ✓ |

---

### Reaction #490  yield=68.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #40)

```
C=C(C)c1ccc(Cl)cc1.Cc1ccc(S(=O)(=O)NCCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCCOC(C)(c3ccc(Cl)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `reticulated_vitreous_carbon` (52.0%) | `graphite_rod` (38.9%) | `carbon_generic` (5.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.1%) | `nickel` (1.5%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (97.8%) | `platinum_generic` (2.0%) | `nickel_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (80.5%) | `NEt4` (13.5%) | `Li` (1.9%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (41.6%) | `PF6` (34.9%) | `ClO4` (8.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (14.1%) | `ammonium_salt` (5.9%) | `as_solvent_halogenated_aliphat` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (73.9%) | `ferrocene_mediator` (7.5%) | `pyridine_organocat` (5.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.1%) | `polar_protic_alcohol` (0.6%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (18%) | `CO` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=P([O-])([O-])O.[` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #491  yield=64.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #41)

```
C=C(C)c1ccc(Cl)cc1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccc(Cl)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `reticulated_vitreous_carbon` (71.3%) | `graphite_rod` (14.8%) | `carbon_generic` (10.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `nickel` (0.9%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (81.8%) | `platinum_generic` (17.8%) | `platinum_foil` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (94.1%) | `ABSENT` (5.8%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (44.8%) | `NBu4` (37.6%) | `ABSENT` (8.1%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (34.2%) | `BF4` (17.8%) | `PF6` (17.6%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (12.8%) | `as_solvent_halogenated_aliphat` (3.1%) | `ammonium_salt` (3.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (87.5%) | `pyridine_organocat` (4.9%) | `Fe_complex` (2.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.4%) | `ketone` (0.3%) | `polar_protic_alcohol` (0.2%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (74%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=P([O-])([O-])O.[` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #492  yield=63.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #42)

```
Cc1ccc(S(=O)(=O)NCCO)cc1.C=C(C)c1ccc(C(F)(F)F)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccc(C(F)(F)F)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (58.6%) | `graphite_rod` (17.8%) | `graphite_generic` (13.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.5%) | `nickel` (5.5%) | `carbon` (3.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (79.4%) | `platinum_plate` (18.6%) | `nickel_foam` (0.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (91.1%) | `ABSENT` (8.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (67.9%) | `Li` (15.6%) | `ABSENT` (13.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `PF6` (30.9%) | `BF4` (28.0%) | `ABSENT` (20.9%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (15.0%) | `primary_amine` (2.4%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.4%) | `pyridine_organocat` (3.7%) | `Fe_complex` (3.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.1%) | `ketone` (0.5%) | `ABSENT` (0.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (5%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #493  yield=67.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #43)

```
C=C(C)c1ccccc1.CC(C)(C)c1ccc(S(=O)(=O)NCCO)cc1>>CC(C)(C)c1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (57.8%) | `carbon_generic` (15.4%) | `carbon_cloth` (10.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.3%) | `sacrificial_iron` (1.7%) | `carbon` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (57.1%) | `platinum_plate` (41.4%) | `platinum_foil` (0.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.8%) | `ABSENT` (1.2%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (42.9%) | `ABSENT` (26.9%) | `K` (15.8%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (31.5%) | `BF4` (28.8%) | `ClO4` (24.6%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (7.8%) | `alkali_nitrate` (2.6%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.2%) | `triarylamine_radical_cat` (3.6%) | `pyridine_organocat` (2.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (97.9%) | `cyclic_ether` (0.5%) | `polar_aprotic_sulfoxide` (0.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (4%) | `C1CCOC1` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (99%) | `CO` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Oc1ccccc1C=NCCN=Cc` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #494  yield=66.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #44)

```
C=C(C)c1ccccc1.O=S(=O)(NCCO)c1ccccc1Cl>>CC1(c2ccccc2)CN(S(=O)(=O)c2ccccc2Cl)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `reticulated_vitreous_carbon` (61.7%) | `carbon_cloth` (31.8%) | `graphite_generic` (4.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.3%) | `nickel` (7.1%) | `carbon` (6.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (84.8%) | `platinum_plate` (9.9%) | `nickel_foam` (2.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (96.6%) | `ABSENT` (3.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (57.9%) | `ABSENT` (23.8%) | `Li` (7.8%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (41.2%) | `ABSENT` (23.4%) | `ClO4` (16.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (11.2%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (75.3%) | `pyridine_organocat` (7.5%) | `triarylamine_radical_cat` (5.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (93.4%) | `ketone` (3.9%) | `ABSENT` (1.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (90%) | `O` (17%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (99%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #495  yield=65.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #45)

```
C=C(C)c1ccccc1.Cc1ccc(S(=O)(=O)NCCO)cc1C>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_magnesium` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (82.3%) | `carbon_generic` (12.0%) | `carbon_felt` (2.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.8%) | `nickel` (6.0%) | `carbon` (5.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (65.5%) | `platinum_plate` (30.2%) | `platinum_foil` (1.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (46.3%) | `NBu4` (38.3%) | `K` (10.6%) | ✗ |
| 电解质 anion | 26 | `BF4` | `PF6` (40.8%) | `ClO4` (37.6%) | `Br` (5.7%) | ✗ |
| 试剂大类 | 103 | `boron_lewis_acid` | `ABSENT` (17.2%) | `primary_amine` (2.3%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (83.6%) | `organic_neutral_cat` (5.5%) | `pyridine_organocat` (5.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (97.4%) | `ketone` (0.7%) | `polar_aprotic_amide` (0.6%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (82%) | `O` (3%) | `CO` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC[N+](CC)(CC)CC.F` + `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #496  yield=61.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #46)

```
C=C(C)c1ccccc1.O=S(=O)(NCCO)c1cccc(Cl)c1>>CC1(c2ccccc2)CN(S(=O)(=O)c2cccc(Cl)c2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_iron` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (90.0%) | `reticulated_vitreous_carbon` (4.7%) | `carbon_generic` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (72.2%) | `nickel` (25.5%) | `carbon` (2.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (50.5%) | `platinum_plate` (31.2%) | `nickel_foam` (8.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (42.0%) | `NBu4` (34.1%) | `ABSENT` (9.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (30.0%) | `molecular_no_ion` (26.6%) | `PF6` (26.5%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (21.3%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.5%) | `Ni_complex` (2.4%) | `organic_neutral_cat` (1.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (96.0%) | `ketone` (1.4%) | `ABSENT` (1.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (74%) | `CO` (1%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #497  yield=80.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #47)

```
C=C(c1ccccc1)C1CC1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(c3ccccc3)(C3CC3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (85.7%) | `carbon_cloth` (4.6%) | `graphite_rod` (3.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.6%) | `stainless_steel` (2.9%) | `nickel` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (52.5%) | `platinum_generic` (42.8%) | `stainless_steel_generic` (4.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (77.3%) | `ABSENT` (22.4%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (31.6%) | `K` (27.7%) | `NBu4` (16.3%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (38.4%) | `ClO4` (16.0%) | `PF6` (14.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (9.3%) | `carboxylic_acid` (5.1%) | `cyanide` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.2%) | `main_group_lewis_acid` (0.5%) | `organic_neutral_cat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (95.2%) | `polar_protic_alcohol` (4.0%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (4%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (99%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #498  yield=78.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #48)

```
C=Cc1ccccc1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.8%) | `platinum` (2.6%) | `ABSENT` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (68.2%) | `unknown_electrode` (16.7%) | `graphite_generic` (4.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.4%) | `carbon` (6.6%) | `sacrificial_iron` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (95.8%) | `platinum_plate` (2.8%) | `carbon_generic` (0.6%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (98.6%) | `undivided` (1.4%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `K` (22.0%) | `Na` (19.6%) | `NBu4` (17.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `I` (35.2%) | `ABSENT` (19.1%) | `PF6` (10.3%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (16.1%) | `metal_oxide_oxidant` (2.0%) | `tellurium_reagent` (2.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (86.0%) | `organic_neutral_cat` (7.0%) | `pyridine_organocat` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (63.9%) | `cyclic_ether` (15.7%) | `hfip` (5.8%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (50%) | `CO` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (98%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #499  yield=77.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #49)

```
C=Cc1ccc(Cl)cc1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(c3ccc(Cl)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `platinum` (1.3%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (51.9%) | `reticulated_vitreous_carbon` (37.6%) | `graphite_generic` (3.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `carbon` (0.3%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (65.8%) | `platinum_plate` (33.9%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (62.0%) | `undivided` (37.9%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NEt4` | `NBu4` (43.7%) | `Li` (31.6%) | `ABSENT` (9.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (50.0%) | `molecular_no_ion` (14.2%) | `BF4` (11.0%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (14.7%) | `primary_amine` (2.3%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (82.6%) | `pyridine_organocat` (5.4%) | `organic_neutral_cat` (3.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (97.9%) | `ketone` (0.9%) | `polar_protic_alcohol` (0.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (15%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #500  yield=75.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #50)

```
C=C(C)c1ccccc1.O=S(=O)(NCCO)c1cccs1>>CC1(c2ccccc2)CN(S(=O)(=O)c2cccs2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (80.9%) | `carbon_generic` (9.6%) | `graphite_felt` (4.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.2%) | `nickel` (1.5%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (80.7%) | `platinum_plate` (19.0%) | `platinum_foil` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (95.8%) | `ABSENT` (4.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (61.8%) | `NBu4` (17.8%) | `ABSENT` (11.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `PF6` (39.2%) | `ClO4` (31.0%) | `ABSENT` (13.7%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (13.3%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (39.1%) | `ABSENT` (34.9%) | `organic_neutral_cat` (19.0%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.0%) | `ketone` (0.3%) | `ABSENT` (0.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (0%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CC(=O)[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (6%) | `O=S(=O)(O)C(F)(F)F` (5%) | `c1ccc(-c2ccccn2)nc` (4%) | set ✗ / any ✓ |

---

