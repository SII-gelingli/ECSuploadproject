# Test 预测 part 2 — 反应 #501-#1000

[← 返回 INDEX](INDEX.md)

### Reaction #501  yield=71.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #51)

```
C=C(C)c1ccccc1.O=S(=O)(NCCO)c1ccc(OC(F)(F)F)cc1>>CC1(c2ccccc2)CN(S(=O)(=O)c2ccc(OC(F)(F)F)cc2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (63.8%) | `carbon_cloth` (29.9%) | `reticulated_vitreous_carbon` (2.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.3%) | `carbon` (1.3%) | `sacrificial_iron` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (71.2%) | `platinum_plate` (28.2%) | `iron_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.5%) | `ABSENT` (1.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `ABSENT` (37.3%) | `NBu4` (28.9%) | `Li` (22.2%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (41.2%) | `ClO4` (31.1%) | `I` (7.8%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (13.4%) | `o2_oxidant` (7.8%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.1%) | `triarylamine_radical_cat` (2.0%) | `pyridine_organocat` (1.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.9%) | `polar_protic_alcohol` (0.3%) | `cyclic_ether` (0.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (94%) | `O` (8%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `O=C1OC2(c3ccccc31)` (0%) | set ✓ / any ✓ |

---

### Reaction #502  yield=78.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #52)

```
C=C(c1ccccc1)c1ccccc1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(c3ccccc3)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.0%) | `platinum` (1.6%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (34.5%) | `reticulated_vitreous_carbon` (24.8%) | `graphite_generic` (20.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.4%) | `nickel` (2.6%) | `sacrificial_iron` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (95.9%) | `platinum_plate` (2.6%) | `platinum_foil` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (82.7%) | `ABSENT` (17.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Li` (47.4%) | `K` (27.2%) | `Na` (18.9%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `ClO4` (43.5%) | `PF6` (23.1%) | `molecular_no_ion` (15.3%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (10.9%) | `carboxylic_acid` (4.4%) | `as_solvent_halogenated_aliphat` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (46.2%) | `organic_neutral_cat` (17.2%) | `pyridine_organocat` (10.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (92.6%) | `cyclic_ether` (2.3%) | `polar_protic_alcohol` (1.8%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (89%) | `CO` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (98%) | `CC(=O)O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (87%) | `Brc1ccc(N(c2ccc(Br` (5%) | `[Fe+2].c1cc[cH-]c1` (1%) | set ✓ / any ✓ |

---

### Reaction #503  yield=87.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #53)

```
C=Cc1ccc(C(C)(C)C)cc1.Cc1ccc(S(=O)(=O)NCCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCCOC(c3ccc(C(C)(C)C)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.1%) | `platinum` (1.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (63.5%) | `graphite_rod` (21.7%) | `carbon_generic` (6.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.7%) | `carbon` (4.5%) | `sacrificial_iron` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (57.6%) | `platinum_generic` (37.8%) | `graphite_rod` (2.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NEt4` (36.4%) | `NBu4` (25.2%) | `Na` (24.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (60.8%) | `ClO4` (12.9%) | `BF4` (11.2%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (19.8%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.9%) | `ammonium_PTC_organocat` (6.7%) | `organic_neutral_cat` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (95.8%) | `cyclic_ether` (2.5%) | `polar_protic_alcohol` (0.6%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (5%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #504  yield=88.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #54)

```
C=C(C)c1ccccc1.Cc1ccc(S(=O)(=O)NCCO)cc1>>Cc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_generic` (39.3%) | `graphite_generic` (24.0%) | `graphite_rod` (21.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.3%) | `nickel` (9.5%) | `sacrificial_iron` (2.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (68.4%) | `platinum_plate` (23.7%) | `platinum_foil` (3.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (91.9%) | `ABSENT` (8.0%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (36.5%) | `K` (28.4%) | `NBu4` (27.1%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (30.9%) | `BF4` (17.8%) | `PF6` (14.4%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (9.6%) | `as_solvent_halogenated_aliphat` (2.9%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (87.1%) | `triarylamine_radical_cat` (2.0%) | `Fe_complex` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (95.5%) | `polar_aprotic_sulfoxide` (1.3%) | `cyclic_ether` (0.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (76%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (99%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #505  yield=83.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #55)

```
C=C(C)c1ccccc1.O=S(=O)(NCCO)c1ccccc1>>CC1(c2ccccc2)CN(S(=O)(=O)c2ccccc2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (63.0%) | `graphite_rod` (13.1%) | `carbon_cloth` (8.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.5%) | `sacrificial_iron` (4.4%) | `nickel` (4.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (71.3%) | `platinum_plate` (25.3%) | `platinum_foil` (1.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (94.1%) | `ABSENT` (5.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (32.6%) | `K` (29.8%) | `NBu4` (25.6%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (46.6%) | `I` (19.7%) | `PF6` (9.0%) | ✗ |
| 试剂大类 | 103 | `boron_lewis_acid` | `ABSENT` (10.7%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (77.5%) | `triarylamine_radical_cat` (7.5%) | `pyridine_organocat` (3.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.2%) | `polar_aprotic_sulfoxide` (0.4%) | `ABSENT` (0.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (97%) | `O` (11%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC[N+](CC)(CC)CC.F` + `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CO` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #506  yield=83.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #56)

```
C=C(C)c1ccccc1.COC(=O)c1ccc(S(=O)(=O)NCCO)cc1>>COC(=O)c1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (76.9%) | `carbon_generic` (8.1%) | `graphite_rod` (5.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.4%) | `carbon` (5.7%) | `sacrificial_iron` (5.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (56.3%) | `platinum_generic` (37.5%) | `iron_generic` (1.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.3%) | `ABSENT` (3.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (48.8%) | `K` (25.3%) | `Li` (10.8%) | ✗ |
| 电解质 anion | 26 | `BF4` | `PF6` (44.8%) | `I` (25.4%) | `ClO4` (9.3%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (12.1%) | `primary_amine` (2.8%) | `cyanide` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (86.8%) | `pyridine_organocat` (3.4%) | `triarylamine_radical_cat` (2.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (97.8%) | `ketone` (0.5%) | `polar_protic_alcohol` (0.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (1%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (1%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #507  yield=82.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #57)

```
C=C(C)c1ccccc1.O=S(=O)(NCCO)c1ccc(F)cc1>>CC1(c2ccccc2)CN(S(=O)(=O)c2ccc(F)cc2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (73.8%) | `reticulated_vitreous_carbon` (13.2%) | `carbon_cloth` (10.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.8%) | `nickel` (0.5%) | `carbon` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (61.7%) | `platinum_plate` (37.4%) | `platinum_foil` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (44.1%) | `Li` (26.2%) | `ABSENT` (10.4%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (50.3%) | `I` (19.7%) | `PF6` (8.3%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (12.9%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.3%) | `pyridine_organocat` (4.0%) | `triarylamine_radical_cat` (2.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.3%) | `ABSENT` (0.2%) | `polar_protic_alcohol` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (93%) | `O` (16%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CO` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #508  yield=82.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #58)

```
C=C(C)c1ccccc1.O=S(=O)(NCCO)c1ccc(C(F)(F)F)cc1>>CC1(c2ccccc2)CN(S(=O)(=O)c2ccc(C(F)(F)F)cc2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `ABSENT` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (77.5%) | `carbon_generic` (16.0%) | `graphite_rod` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.6%) | `sacrificial_iron` (3.8%) | `carbon` (1.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (2.7%) | `unknown_electrode` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.1%) | `ABSENT` (1.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (76.5%) | `Li` (14.9%) | `ABSENT` (3.5%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (31.9%) | `ClO4` (28.9%) | `PF6` (26.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (10.6%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (86.1%) | `pyridine_organocat` (6.2%) | `triarylamine_radical_cat` (3.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (97.8%) | `polar_protic_alcohol` (0.4%) | `polar_aprotic_sulfoxide` (0.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (99%) | `O` (0%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #509  yield=81.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #59)

```
C=C(C)c1ccccc1.O=S(=O)(NCCO)c1ccc2c(c1)CCO2>>CC1(c2ccccc2)CN(S(=O)(=O)c2ccc3c(c2)CCO3)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (52.4%) | `carbon_generic` (40.6%) | `graphite_rod` (3.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (74.0%) | `nickel` (23.1%) | `carbon` (1.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (94.2%) | `nickel_generic` (3.3%) | `platinum_plate` (1.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (77.6%) | `Li` (15.8%) | `K` (4.8%) | ✗ |
| 电解质 anion | 26 | `BF4` | `BF4` (40.6%) | `ClO4` (29.6%) | `PF6` (10.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (20.4%) | `metal_oxide_oxidant` (2.3%) | `tellurium_reagent` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `pyridine_organocat` (0.5%) | `Fe_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (97.1%) | `polar_protic_alcohol` (1.1%) | `polar_aprotic_sulfoxide` (0.7%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (90%) | `CO` (7%) | `O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #510  yield=84.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #60)

```
Cc1ccc(S(=O)(=O)NCCCO)cc1.C=C(C)c1ccc(C(C)(C)C)cc1>>Cc1ccc(S(=O)(=O)N2CCCOC(C)(c3ccc(C(C)(C)C)cc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (36.4%) | `graphite_rod` (34.4%) | `carbon_generic` (20.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.8%) | `nickel` (9.2%) | `carbon` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (71.0%) | `platinum_generic` (22.7%) | `nickel_generic` (3.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (74.3%) | `NEt4` (10.6%) | `K` (6.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (62.6%) | `I` (12.7%) | `ClO4` (8.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (8.9%) | `as_solvent_polar_protic_alcoho` (5.7%) | `primary_amine` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.6%) | `organic_neutral_cat` (5.1%) | `ferrocene_mediator` (4.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.6%) | `polar_protic_alcohol` (0.6%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `CO` (2%) | `O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CO` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #511  yield=90.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #61)

```
C=C(C)c1ccccc1.O=S(=O)(NCCO)c1ccc(Br)cc1>>CC1(c2ccccc2)CN(S(=O)(=O)c2ccc(Br)cc2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_cloth` (66.0%) | `carbon_generic` (19.9%) | `graphite_generic` (8.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.0%) | `sacrificial_iron` (2.7%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (58.7%) | `platinum_plate` (40.6%) | `iron_generic` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (94.7%) | `ABSENT` (5.3%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (40.6%) | `ABSENT` (20.3%) | `Li` (15.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `PF6` (28.7%) | `ABSENT` (25.5%) | `ClO4` (18.9%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (13.5%) | `primary_amine` (2.6%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.0%) | `pyridine_organocat` (2.3%) | `triarylamine_radical_cat` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.5%) | `polar_aprotic_sulfoxide` (0.2%) | `ketone` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (100%) | `O` (20%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `O=C1OC2(c3ccccc31)` (0%) | set ✓ / any ✓ |

---

### Reaction #512  yield=96.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #62)

```
C=C(C)c1ccccc1.COc1ccc(S(=O)(=O)NCCO)cc1>>COc1ccc(S(=O)(=O)N2CCOC(C)(c3ccccc3)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_cloth` (43.1%) | `graphite_generic` (17.3%) | `carbon_generic` (17.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (91.3%) | `sacrificial_iron` (6.1%) | `nickel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (79.5%) | `platinum_plate` (16.2%) | `iron_generic` (3.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.1%) | `ABSENT` (1.9%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Li` (31.8%) | `K` (30.1%) | `NBu4` (29.4%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ClO4` (53.7%) | `I` (13.6%) | `BF4` (12.6%) | ✓ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ABSENT` (15.4%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (70.5%) | `pyridine_organocat` (8.5%) | `triarylamine_radical_cat` (6.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (96.6%) | `polar_protic_alcohol` (0.7%) | `polar_aprotic_sulfoxide` (0.7%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (97%) | `O` (8%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `__ABSENT__` (99%) | `CO` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #513  yield=95.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_19_e202501424.json) (反应 idx 在该 JSON 内 = #63)

```
C=C(C)c1ccccc1.O=S(=O)(NCCO)c1ccc(Cl)cc1>>CC1(c2ccccc2)CN(S(=O)(=O)c2ccc(Cl)cc2)CCO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_cloth` (80.1%) | `graphite_generic` (8.3%) | `reticulated_vitreous_carbon` (6.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.8%) | `sacrificial_iron` (0.6%) | `carbon` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (78.8%) | `platinum_generic` (20.9%) | `iron_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `ABSENT` (44.6%) | `NBu4` (21.0%) | `K` (12.0%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (52.6%) | `PF6` (13.0%) | `ClO4` (8.7%) | ✗ |
| 试剂大类 | 103 | `amidine_guanidine_base` | `ammonium_salt` (10.0%) | `ABSENT` (9.7%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.0%) | `triarylamine_radical_cat` (4.2%) | `pyridine_organocat` (3.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.1%) | `polar_protic_alcohol` (0.3%) | `polar_aprotic_sulfoxide` (0.2%) | ✗ |
| 溶剂 set | 79 | `ClCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (98%) | `O` (57%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `C1CCC2=NCCCN2CC1` | `CCCC[N+](CCCC)(CCC` (23%) | `__ABSENT__` (4%) | `O=P([O-])([O-])O.[` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #514  yield=22.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(c1ccccc1)c1ccccc1.CCCC[N+](CCCC)(CCCC)CCCC.O=C([O-])CC1CC1>>C=CCCCC(OCC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (83.1%) | `platinum` (11.7%) | `ABSENT` (4.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_rod` (61.8%) | `graphite_generic` (30.0%) | `platinum_generic` (2.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (70.9%) | `platinum` (23.3%) | `ABSENT` (5.5%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (42.1%) | `unknown_electrode` (17.9%) | `graphite_generic` (13.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (34.8%) | `Na` (33.5%) | `Li` (18.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (45.0%) | `ABSENT` (30.3%) | `ClO4` (10.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `alkali_hydroxide` (18.7%) | `ABSENT` (10.4%) | `o2_oxidant` (7.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `Pt_complex` (0.2%) | `ferrocene_mediator` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (84.0%) | `polar_protic_alcohol` (9.9%) | `ABSENT` (3.3%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (99%) | `CO` (1%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `[K+].[OH-]` (62%) | `__ABSENT__` (32%) | `[Na+].[OH-]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #515  yield=30.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #1)

```
CC(C)O.C=C(c1ccccc1)c1ccccc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCC(OC(C)C)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (89.4%) | `platinum` (8.9%) | `sacrificial_magnesium` (1.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_generic` (74.9%) | `graphite_rod` (24.0%) | `platinum_generic` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (88.4%) | `platinum` (10.9%) | `ABSENT` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (62.7%) | `graphite_rod` (28.0%) | `platinum_generic` (3.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (57.8%) | `NEt4` (25.7%) | `Na` (7.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `OH` (31.5%) | `BF4` (17.4%) | `molecular_no_ion` (14.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (46.0%) | `ABSENT` (5.9%) | `diboron` (1.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.7%) | `ferrocene_mediator` (4.9%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (93.8%) | `polar_protic_alcohol` (4.1%) | `cyclic_ether` (1.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `CO` (0%) | `C1CCOC1` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (77%) | `__ABSENT__` (3%) | `[OH][Na]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✓ / any ✓ |

---

### Reaction #516  yield=30.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #2)

```
C=C(c1ccccc1)c1ccccc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCC(F)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (87.8%) | `ABSENT` (7.9%) | `carbon` (4.1%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (92.7%) | `platinum_plate` (5.5%) | `ABSENT` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `ABSENT` (40.9%) | `platinum` (34.2%) | `carbon` (13.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (44.9%) | `unknown_electrode` (23.6%) | `platinum_plate` (16.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (93.6%) | `ABSENT` (6.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (57.7%) | `protonated_amine` (20.0%) | `NBu4` (9.4%) | ✓ |
| 电解质 anion | 26 | `F` | `ABSENT` (51.2%) | `fluoride_complex` (26.0%) | `ClO4` (11.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (27.9%) | `inorganic_simple` (5.2%) | `ABSENT` (3.1%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `pyridine_organocat` (0.3%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.9%) | `halogenated_aliphatic` (0.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CC(C)(C)O` | `CC#N` (100%) | `CCO` (22%) | `ClCCl` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `O=O` (87%) | `[OH][Na]` (7%) | `Cc1ccc(I)cc1` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #517  yield=40.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1cc(C)ccc1C.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCOC(CC)c1cc(C)ccc1C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (84.6%) | `carbon` (10.4%) | `ABSENT` (5.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (55.0%) | `platinum_plate` (29.9%) | `unknown_electrode` (5.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.2%) | `ABSENT` (4.4%) | `stainless_steel` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (92.6%) | `platinum_plate` (4.1%) | `ABSENT` (1.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `ABSENT` (0.5%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.6%) | `Li` (37.4%) | `ABSENT` (9.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (28.3%) | `ClO4` (21.3%) | `Cl` (17.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (36.9%) | `hydrosilane` (3.1%) | `metal_oxide_oxidant` (1.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (48.3%) | `organic_neutral_cat` (33.2%) | `Co_complex` (4.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (95.5%) | `polar_protic_alcohol` (4.2%) | `cyclic_ether` (0.1%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (100%) | `ClCCCl` (0%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `Cc1ccc(S(=O)(=O)O)` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `N#Cc1c(C#N)c(-n2c3` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #518  yield=33.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #4)

```
C=Cc1ccc(C)cc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCOC(CC)c1ccc(C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (40.3%) | `carbon` (34.4%) | `ABSENT` (24.8%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `ABSENT` (79.2%) | `platinum_generic` (10.7%) | `graphite_generic` (3.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.9%) | `ABSENT` (22.1%) | `carbon` (1.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `ABSENT` (61.0%) | `platinum_generic` (28.1%) | `platinum_plate` (6.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (92.3%) | `ABSENT` (7.3%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.5%) | `Li` (16.3%) | `NEt4` (7.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (28.9%) | `BF4` (20.3%) | `ClO4` (19.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.2%) | `hydrosilane` (4.9%) | `metal_oxide_oxidant` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (82.0%) | `organic_neutral_cat` (5.3%) | `Co_complex` (3.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (63.8%) | `polar_protic_alcohol` (34.8%) | `cyclic_ether` (0.8%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (100%) | `ClCCl` (2%) | `CCO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Pt]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #519  yield=33.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #5)

```
C=C(c1ccccc1)c1ccccc1.CCCCCCCCCC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCCCCCCCCCC(OCC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (62.2%) | `ABSENT` (34.7%) | `platinum` (2.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_rod` (72.8%) | `ABSENT` (15.7%) | `graphite_generic` (5.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `ABSENT` (57.6%) | `platinum` (38.7%) | `carbon` (3.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (73.1%) | `ABSENT` (24.8%) | `unknown_electrode` (1.2%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (65.2%) | `undivided` (34.8%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (62.1%) | `Na` (11.7%) | `ABSENT` (10.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (38.2%) | `carboxylate` (14.0%) | `OH` (12.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.7%) | `o2_oxidant` (6.3%) | `alkali_hydroxide` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `Co_complex` (0.2%) | `ferrocene_mediator` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (52.1%) | `polar_aprotic_nitrile` (45.5%) | `cyclic_ether` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` + `__OTHER__` | `CC#N` (92%) | `CO` (7%) | `C1CCOC1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #520  yield=38.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #6)

```
C=C(C)c1ccccc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCC(C)(F)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (44.4%) | `ABSENT` (43.9%) | `carbon` (9.8%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (84.7%) | `carbon_cloth` (6.7%) | `unknown_electrode` (4.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (43.2%) | `ABSENT` (24.4%) | `copper` (14.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (83.3%) | `unknown_electrode` (5.6%) | `carbon_generic` (4.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (95.6%) | `ABSENT` (4.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (82.3%) | `molecular_no_ion` (10.4%) | `protonated_amine` (3.4%) | ✗ |
| 电解质 anion | 26 | `F` | `ABSENT` (90.7%) | `fluoride_complex` (3.8%) | `Cl` (1.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (23.0%) | `hf_amine_complex` (8.5%) | `ammonium_salt` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `pyridine_organocat` (0.2%) | `polycyclic_arene_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (91.1%) | `halogenated_aliphatic` (3.1%) | `polar_protic_alcohol` (2.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CC(C)(C)O` | `CC#N` (98%) | `ClCCl` (49%) | `CCO` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (97%) | `O=P([O-])([O-])O.[` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #521  yield=38.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #7)

```
C=C(c1ccccc1)c1ccccc1.CCCC[N+](CCCC)(CCCC)CCCC.CCOCCC(=O)[O-]>>CCOCCCC(OCC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (67.9%) | `ABSENT` (24.0%) | `platinum` (7.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_rod` (73.3%) | `ABSENT` (7.9%) | `platinum_generic` (6.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (66.3%) | `carbon` (18.4%) | `ABSENT` (15.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (92.0%) | `ABSENT` (4.9%) | `unknown_electrode` (2.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (93.5%) | `ABSENT` (6.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NH4` | `NBu4` (35.1%) | `Na` (32.9%) | `ABSENT` (19.2%) | ✗ |
| 电解质 anion | 26 | `I` | `ClO4` (20.5%) | `ABSENT` (18.8%) | `BF4` (14.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (15.2%) | `o2_oxidant` (13.4%) | `alkali_hydroxide` (6.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `ferrocene_mediator` (0.2%) | `Co_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (72.7%) | `polar_protic_alcohol` (22.1%) | `cyclic_ether` (3.6%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` + `__OTHER__` | `CC#N` (99%) | `O` (3%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `[K+].[OH-]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #522  yield=38.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #8)

```
C=C(c1ccccc1)c1ccccc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCC(O)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.9%) | `ABSENT` (25.7%) | `carbon` (8.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (88.5%) | `unknown_electrode` (6.6%) | `ABSENT` (2.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `ABSENT` (63.2%) | `platinum` (23.2%) | `carbon` (6.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `unknown_electrode` (70.9%) | `platinum_generic` (18.9%) | `ABSENT` (7.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (63.3%) | `ABSENT` (36.3%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (58.2%) | `Li` (22.5%) | `NBu4` (13.4%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (44.4%) | `ClO4` (43.0%) | `PF6` (5.3%) | ✗ |
| 试剂大类 | 103 | `water` | `o2_oxidant` (17.3%) | `ABSENT` (10.2%) | `alkali_hydroxide` (5.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.6%) | `polycyclic_arene_cat` (0.1%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.8%) | `polar_protic_alcohol` (1.8%) | `cyclic_ether` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `O=O` (54%) | `[K+].[OH-]` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `CC1(C)O[C@@H](c2cc` (0%) | set ✓ / any ✓ |

---

### Reaction #523  yield=35.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #9)

```
C=C(c1ccccc1)c1ccccc1.CCCCCCCCCCCC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCCCCCCCCCCCC(OCC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (62.2%) | `ABSENT` (34.7%) | `platinum` (2.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_rod` (72.8%) | `ABSENT` (15.7%) | `graphite_generic` (5.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `ABSENT` (57.6%) | `platinum` (38.7%) | `carbon` (3.2%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (73.1%) | `ABSENT` (24.8%) | `unknown_electrode` (1.2%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (65.2%) | `undivided` (34.8%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NH4` | `NBu4` (62.1%) | `Na` (11.7%) | `ABSENT` (10.3%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (38.2%) | `carboxylate` (14.0%) | `OH` (12.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.7%) | `o2_oxidant` (6.3%) | `alkali_hydroxide` (1.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.1%) | `Co_complex` (0.2%) | `ferrocene_mediator` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (52.1%) | `polar_aprotic_nitrile` (45.5%) | `cyclic_ether` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` + `__OTHER__` | `CC#N` (92%) | `CO` (7%) | `C1CCOC1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #524  yield=45.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #10)

```
C=C(C)c1ccc(Br)cc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCOC(C)(CC)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (79.8%) | `carbon` (15.0%) | `ABSENT` (4.8%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (91.8%) | `platinum_plate` (2.6%) | `graphite_generic` (1.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.4%) | `carbon` (1.0%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.8%) | `platinum_plate` (0.7%) | `platinum_wire` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.4%) | `NEt4` (1.1%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (36.2%) | `Cl` (22.3%) | `ClO4` (20.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.9%) | `o2_oxidant` (12.2%) | `tetraaryl_borate` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.9%) | `Fe_complex` (2.2%) | `pyridine_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (80.6%) | `polar_protic_alcohol` (16.7%) | `ABSENT` (1.5%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (100%) | `ClCCl` (2%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #525  yield=47.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #11)

```
C=C(C)c1ccccc1.OCc1ccccc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCC(C)(OCc1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (92.9%) | `carbon` (6.7%) | `ABSENT` (0.2%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (83.8%) | `platinum_plate` (12.2%) | `graphite_rod` (1.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (50.9%) | `copper` (32.2%) | `carbon` (7.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (45.3%) | `platinum_plate` (21.8%) | `unknown_electrode` (14.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (75.4%) | `NBu4` (10.6%) | `Li` (8.9%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (65.1%) | `ClO4` (15.4%) | `molecular_no_ion` (9.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (20.4%) | `ABSENT` (7.1%) | `metal_oxide_oxidant` (1.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `pyridine_organocat` (0.4%) | `Pt_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.4%) | `polar_protic_alcohol` (6.7%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (3%) | `CCO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (86%) | `__ABSENT__` (1%) | `[Pt]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #526  yield=45.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #12)

```
C=C(C)c1ccccc1.OCc1ccccc1F>>CCC(C)(OCc1ccccc1F)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `platinum` (1.7%) | `sacrificial_zinc` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_generic` (48.8%) | `glassy_carbon` (17.1%) | `graphite_rod` (12.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (78.6%) | `carbon` (16.4%) | `copper` (1.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (40.3%) | `platinum_plate` (21.0%) | `graphite_generic` (15.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (68.2%) | `NEt4` (20.4%) | `K` (8.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (65.2%) | `Cl` (12.1%) | `carboxylate` (9.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.4%) | `water` (2.4%) | `primary_amine` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Mn_complex` (0.1%) | `Co_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.8%) | `polar_protic_alcohol` (8.2%) | `polar_aprotic_sulfoxide` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `O` (32%) | `CCOCC` (6%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (1%) | `O=O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(C)(C)c1cc(C=N[C` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #527  yield=45.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #13)

```
C=C(CCC)c1ccccc1>>CCCC(CC)(OCC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.7%) | `platinum` (10.8%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (38.4%) | `graphite_generic` (34.8%) | `glassy_carbon` (13.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.0%) | `ABSENT` (0.5%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.9%) | `platinum_plate` (0.1%) | `ABSENT` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (63.6%) | `ABSENT` (36.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.2%) | `Na` (0.5%) | `Li` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (88.1%) | `Br` (5.1%) | `carboxylate` (3.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.5%) | `transition_metal_salt_reagent` (3.3%) | `metal_oxide_oxidant` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `Co_complex` (0.4%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (84.7%) | `polar_aprotic_nitrile` (14.5%) | `cyclic_ether` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (99%) | `O` (7%) | `CO` (4%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Pt]` | `__ABSENT__` (89%) | `[Pt]` (3%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #528  yield=48.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #14)

```
C=C(c1ccccc1)c1ccccc1.CCCCCC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCCCCCC(OCC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (47.6%) | `ABSENT` (47.1%) | `platinum` (4.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_rod` (70.2%) | `ABSENT` (21.2%) | `graphite_generic` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `ABSENT` (63.2%) | `platinum` (34.2%) | `carbon` (2.3%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (72.9%) | `ABSENT` (25.2%) | `unknown_electrode` (1.3%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (67.7%) | `undivided` (32.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NH4` | `NBu4` (54.4%) | `ABSENT` (18.2%) | `Na` (11.5%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (33.0%) | `ABSENT` (16.9%) | `OH` (16.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (24.0%) | `o2_oxidant` (6.8%) | `alkali_hydroxide` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `Co_complex` (0.2%) | `ammonium_PTC_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (68.0%) | `polar_aprotic_nitrile` (30.1%) | `cyclic_ether` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` + `__OTHER__` | `CC#N` (88%) | `CO` (11%) | `C1CCOC1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #529  yield=48.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #15)

```
CO.C=C(c1ccccc1)c1ccccc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCC(OC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (69.9%) | `platinum` (29.2%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_rod` (53.2%) | `graphite_generic` (28.5%) | `platinum_generic` (15.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.9%) | `carbon` (2.3%) | `nickel` (2.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (93.5%) | `platinum_plate` (3.7%) | `carbon_rod` (1.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.9%) | `Li` (1.8%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (68.6%) | `OH` (12.4%) | `BF4` (10.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (75.4%) | `ABSENT` (1.6%) | `alkali_hydroxide` (1.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ferrocene_mediator` (64.8%) | `ABSENT` (26.7%) | `pyridine_organocat` (4.6%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (72.9%) | `ABSENT` (10.9%) | `polar_protic_alcohol` (9.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `C1CCOC1` (1%) | `CO` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (76%) | `__ABSENT__` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[cH]12->[Fe+2]3456` (79%) | `[Fe+2].c1cc[cH-]c1` (18%) | `__ABSENT__` (1%) | set ✗ / any ✓ |

---

### Reaction #530  yield=46.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #16)

```
C=C(c1ccccc1)c1ccccc1.CCCC[N+](CCCC)(CCCC)CCCC.COCCC(=O)[O-]>>CCOC(CCCOC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (48.4%) | `carbon` (28.4%) | `ABSENT` (22.8%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (55.9%) | `ABSENT` (18.3%) | `graphite_rod` (18.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (76.7%) | `ABSENT` (21.1%) | `carbon` (1.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (91.0%) | `ABSENT` (8.4%) | `unknown_electrode` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.8%) | `ABSENT` (3.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NH4` | `Na` (36.9%) | `NBu4` (30.4%) | `ABSENT` (24.7%) | ✗ |
| 电解质 anion | 26 | `I` | `OH` (22.9%) | `ClO4` (18.8%) | `ABSENT` (17.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (29.0%) | `ABSENT` (9.6%) | `alkali_hydroxide` (4.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.1%) | `ferrocene_mediator` (3.8%) | `Co_complex` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (75.3%) | `polar_aprotic_nitrile` (20.8%) | `cyclic_ether` (2.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` + `__OTHER__` | `CC#N` (70%) | `CO` (29%) | `CCO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (65%) | `[K+].[OH-]` (3%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #531  yield=50.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #17)

```
CCO.C=C(c1ccccc1)c1ccc(C)cc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCOC(CC)(c1ccccc1)c1ccc(C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (67.9%) | `platinum` (31.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_rod` (49.5%) | `platinum_generic` (25.9%) | `platinum_plate` (10.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.9%) | `carbon` (4.1%) | `nickel` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (63.7%) | `platinum_plate` (31.9%) | `carbon_rod` (1.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (92.2%) | `K` (3.2%) | `Li` (1.8%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (37.3%) | `OH` (23.6%) | `ClO4` (12.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (17.9%) | `ABSENT` (14.5%) | `alkali_hydroxide` (4.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.1%) | `ferrocene_mediator` (8.0%) | `pyridine_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (79.5%) | `polar_protic_alcohol` (14.7%) | `ABSENT` (4.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `CO` (0%) | `C1CCOC1` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (23%) | `O=O` (10%) | `[K+].[OH-]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #532  yield=42.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1ccc(Oc2ccccc2)cc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCOC(CC)c1ccc(Oc2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (51.6%) | `carbon` (43.3%) | `ABSENT` (4.7%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (36.6%) | `graphite_generic` (35.9%) | `unknown_electrode` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.5%) | `ABSENT` (3.5%) | `nickel` (1.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (95.9%) | `platinum_plate` (1.9%) | `ABSENT` (0.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.7%) | `ABSENT` (1.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (45.3%) | `Na` (23.1%) | `ABSENT` (18.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (30.8%) | `Cl` (23.4%) | `carboxylate` (15.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (17.1%) | `ABSENT` (15.4%) | `hydrosilane` (3.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (65.4%) | `Co_complex` (13.7%) | `ferrocene_mediator` (9.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (77.1%) | `polar_protic_alcohol` (21.8%) | `cyclic_ether` (0.8%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (96%) | `CO` (4%) | `CN(C)C=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (5%) | `__ABSENT__` (1%) | `[K+].[OH-]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `N#Cc1c(C#N)c(-n2c3` (0%) | set ✓ / any ✓ |

---

### Reaction #533  yield=60.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #19)

```
CC(=O)O.C=C(c1ccccc1)c1ccccc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCC(OC(C)=O)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (39.5%) | `ABSENT` (39.2%) | `platinum` (21.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `unknown_electrode` (30.5%) | `platinum_generic` (29.6%) | `graphite_generic` (15.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (54.7%) | `ABSENT` (32.4%) | `carbon` (12.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (62.7%) | `unknown_electrode` (27.5%) | `ABSENT` (6.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (39.8%) | `NBu4` (36.5%) | `ABSENT` (7.1%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (77.5%) | `BF4` (7.5%) | `molecular_no_ion` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.0%) | `o2_oxidant` (4.3%) | `alkali_hydroxide` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (86.3%) | `pyridine_organocat` (4.4%) | `organic_neutral_cat` (2.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (84.4%) | `polar_protic_alcohol` (13.9%) | `cyclic_ether` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCl` (0%) | `CCO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C(O)O.[Na]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #534  yield=54.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #20)

```
CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC.C=C(C)c1ccc(CCC)cc1>>CCCc1ccc(C(C)(CC)OCC)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (70.5%) | `carbon` (20.2%) | `ABSENT` (8.1%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (64.1%) | `graphite_rod` (20.2%) | `ABSENT` (4.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.5%) | `ABSENT` (1.5%) | `carbon` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (95.3%) | `platinum_plate` (4.1%) | `ABSENT` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.7%) | `ABSENT` (2.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.1%) | `NEt4` (2.0%) | `Na` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `OH` (37.5%) | `BF4` (32.5%) | `Cl` (9.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.5%) | `o2_oxidant` (17.8%) | `diboron` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.3%) | `Fe_complex` (1.0%) | `ferrocene_mediator` (1.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (51.0%) | `polar_aprotic_nitrile` (39.3%) | `ABSENT` (5.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (80%) | `CO` (10%) | `CC(C)=O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #535  yield=58.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #21)

```
C=C(c1ccccc1)c1ccccc1.CCCC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCCCC(OCC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (51.6%) | `ABSENT` (36.8%) | `platinum` (11.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_rod` (83.7%) | `ABSENT` (8.2%) | `graphite_generic` (3.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (55.1%) | `ABSENT` (36.5%) | `carbon` (8.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (79.8%) | `ABSENT` (15.5%) | `unknown_electrode` (2.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (95.6%) | `ABSENT` (4.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NH4` | `Na` (38.4%) | `NBu4` (34.0%) | `ABSENT` (15.8%) | ✗ |
| 电解质 anion | 26 | `I` | `OH` (28.4%) | `ABSENT` (17.0%) | `BF4` (15.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.7%) | `o2_oxidant` (12.6%) | `alkali_hydroxide` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `ferrocene_mediator` (0.2%) | `Pt_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (59.5%) | `polar_aprotic_nitrile` (36.0%) | `ABSENT` (2.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` + `__OTHER__` | `CC#N` (85%) | `CO` (14%) | `CCO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `[K+].[OH-]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #536  yield=57.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #22)

```
C=C(c1ccccc1)c1ccccc1.CCCCC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCCCCC(OCC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `ABSENT` (65.8%) | `carbon` (30.8%) | `platinum` (2.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `ABSENT` (58.0%) | `graphite_rod` (33.9%) | `unknown_electrode` (2.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `ABSENT` (84.0%) | `platinum` (12.8%) | `carbon` (2.7%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `ABSENT` (68.2%) | `platinum_generic` (28.8%) | `unknown_electrode` (2.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (74.9%) | `undivided` (25.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NH4` | `NBu4` (72.1%) | `ABSENT` (8.5%) | `Na` (8.2%) | ✗ |
| 电解质 anion | 26 | `I` | `BF4` (45.0%) | `OH` (16.3%) | `ClO4` (11.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.7%) | `o2_oxidant` (6.2%) | `alkali_hydroxide` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `Co_complex` (0.3%) | `ferrocene_mediator` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (72.1%) | `polar_aprotic_nitrile` (18.4%) | `ABSENT` (6.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` + `__OTHER__` | `CC#N` (70%) | `CO` (28%) | `C1CCOC1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC[N+](CC)(CC)CC.F` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #537  yield=58.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #23)

```
CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC.C=C(c1ccccc1)C1CCCC1>>CCOC(CC)(c1ccccc1)C1CCCC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (58.8%) | `platinum` (40.7%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (69.6%) | `graphite_generic` (21.8%) | `unknown_electrode` (4.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.8%) | `ABSENT` (0.5%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.8%) | `platinum_plate` (0.1%) | `unknown_electrode` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (47.9%) | `NBu4` (24.7%) | `ABSENT` (14.4%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (50.1%) | `carboxylate` (16.2%) | `OH` (9.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.1%) | `o2_oxidant` (8.8%) | `alkali_hydroxide` (6.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.1%) | `ferrocene_mediator` (1.7%) | `pyridine_organocat` (1.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (74.1%) | `polar_aprotic_nitrile` (25.6%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (99%) | `CO` (4%) | `CCO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `[Pt]` (0%) | `[K+].[OH-]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #538  yield=58.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #24)

```
C=C(c1ccccc1)c1ccc(F)cc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCOC(CC)(c1ccccc1)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (62.6%) | `platinum` (36.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_rod` (44.6%) | `platinum_generic` (43.6%) | `graphite_generic` (5.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.2%) | `carbon` (0.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (97.0%) | `platinum_plate` (2.7%) | `ABSENT` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (80.2%) | `Na` (13.2%) | `K` (3.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `OH` (63.4%) | `BF4` (11.7%) | `carboxylate` (7.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (26.6%) | `ABSENT` (13.1%) | `alkali_hydroxide` (4.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (86.6%) | `ferrocene_mediator` (12.1%) | `pyridine_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (57.8%) | `polar_protic_alcohol` (34.3%) | `cyclic_ether` (5.2%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (99%) | `ClCCl` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (44%) | `__ABSENT__` (9%) | `[K+].[OH-]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #539  yield=52.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #25)

```
C=C(c1ccc(Cl)cc1)c1ccc(Cl)cc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCOC(CC)(c1ccc(Cl)cc1)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (83.0%) | `carbon` (15.8%) | `ABSENT` (1.1%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (54.5%) | `platinum_plate` (29.2%) | `graphite_rod` (10.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `carbon` (1.0%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (86.1%) | `platinum_plate` (13.0%) | `ABSENT` (0.4%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (82.8%) | `Na` (10.6%) | `K` (3.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `OH` (28.6%) | `ClO4` (19.8%) | `I` (14.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (29.8%) | `ABSENT` (12.3%) | `alkali_hydroxide` (6.1%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (88.3%) | `ferrocene_mediator` (8.3%) | `pyridine_organocat` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (79.5%) | `polar_protic_alcohol` (18.3%) | `cyclic_ether` (1.3%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (100%) | `C1CCOC1` (0%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (38%) | `O=O` (14%) | `[K+].[OH-]` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #540  yield=56.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #26)

```
C=C(C)c1ccc(B2OC(C)(C)C(C)(C)O2)cc1>>CCOC(C)(CC)c1ccc(B2OC(C)(C)C(C)(C)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (74.6%) | `platinum` (22.2%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (41.2%) | `unknown_electrode` (31.7%) | `graphite_generic` (10.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.8%) | `carbon` (1.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.9%) | `platinum_wire` (0.0%) | `platinum_plate` (0.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.1%) | `Na` (3.0%) | `Li` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `I` (48.1%) | `BF4` (20.9%) | `ClO4` (18.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (19.8%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.3%) | `Fe_complex` (3.6%) | `Co_complex` (1.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `ABSENT` (48.1%) | `polar_protic_alcohol` (25.8%) | `polar_aprotic_nitrile` (22.0%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `__ABSENT__` (74%) | `CC#N` (5%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[O]=[Ti]=[O]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #541  yield=66.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #27)

```
C=Cc1ccc(C(C)(C)C)cc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCOC(CC)c1ccc(C(C)(C)C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (44.9%) | `ABSENT` (32.1%) | `platinum` (22.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (46.9%) | `graphite_generic` (23.2%) | `ABSENT` (15.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (77.6%) | `ABSENT` (21.6%) | `carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.1%) | `ABSENT` (2.7%) | `platinum_plate` (0.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `molecular_no_ion` | `NBu4` (57.5%) | `Li` (19.8%) | `NEt4` (8.2%) | ✗ |
| 电解质 anion | 26 | `molecular_no_ion` | `ClO4` (37.5%) | `carboxylate` (20.4%) | `molecular_no_ion` (13.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.5%) | `silane_other` (5.4%) | `o2_oxidant` (3.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (77.0%) | `organic_neutral_cat` (7.9%) | `Co_complex` (3.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (95.0%) | `polar_protic_alcohol` (4.1%) | `cyclic_ether` (0.5%) | ✓ |
| 溶剂 set | 79 | `CCO` | `CC#N` (100%) | `C1CCOC1` (1%) | `CO` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=S(=O)([O-])C(F)(` (0%) | `Oc1ccccc1C=NCCN=Cc` (0%) | set ✓ / any ✓ |

---

### Reaction #542  yield=67.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #28)

```
C=C(c1ccccc1)c1ccccc1.CC(C)CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCOC(CCC(C)C)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (85.2%) | `platinum` (12.9%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_generic` (44.8%) | `platinum_generic` (24.2%) | `graphite_rod` (14.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (57.4%) | `carbon` (41.1%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `graphite_generic` (1.5%) | `ABSENT` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (94.4%) | `ABSENT` (5.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (41.4%) | `NBu4` (28.0%) | `Na` (21.4%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (47.9%) | `ClO4` (13.6%) | `molecular_no_ion` (12.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.4%) | `o2_oxidant` (13.0%) | `alkali_hydroxide` (9.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `organic_neutral_cat` (0.1%) | `Co_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (93.4%) | `polar_protic_alcohol` (4.2%) | `cyclic_ether` (1.1%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (100%) | `ClCCl` (0%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `[K+].[OH-]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #543  yield=67.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #29)

```
CCCO.C=C(c1ccccc1)c1ccccc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCCOC(CC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (58.9%) | `carbon` (39.7%) | `ABSENT` (0.9%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (69.8%) | `graphite_generic` (13.5%) | `graphite_rod` (11.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (84.7%) | `carbon` (8.8%) | `ABSENT` (3.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (78.6%) | `unknown_electrode` (10.4%) | `platinum_plate` (4.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.5%) | `Li` (3.9%) | `ABSENT` (2.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (40.6%) | `OH` (21.0%) | `Cl` (11.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (58.0%) | `ABSENT` (4.7%) | `alkali_hydroxide` (2.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `ferrocene_mediator` (0.6%) | `pyridine_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (80.7%) | `polar_protic_alcohol` (14.9%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `CO` (2%) | `C1CCOC1` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (43%) | `__ABSENT__` (1%) | `[Pt]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[cH]12->[Fe+2]3456` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #544  yield=66.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #30)

```
C=C(c1ccccc1)c1ccccc1.CCC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCCC(OCC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (50.8%) | `carbon` (34.0%) | `ABSENT` (14.9%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (49.4%) | `graphite_rod` (32.6%) | `ABSENT` (8.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.1%) | `ABSENT` (13.9%) | `carbon` (2.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (90.8%) | `ABSENT` (6.6%) | `unknown_electrode` (1.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (79.5%) | `ABSENT` (20.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (66.1%) | `NBu4` (19.0%) | `Na` (9.0%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (50.3%) | `OH` (26.2%) | `BF4` (5.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (29.0%) | `ABSENT` (7.5%) | `alkali_hydroxide` (4.1%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `ferrocene_mediator` (0.2%) | `Pt_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (47.9%) | `polar_aprotic_nitrile` (46.7%) | `cyclic_ether` (3.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (85%) | `CO` (14%) | `C1CCOC1` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (98%) | `[Pt]` (0%) | `[K+].[OH-]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #545  yield=65.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #31)

```
C=C(c1ccccc1)c1ccccc1.CC(C)(C)CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCOC(CCC(C)(C)C)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (51.4%) | `platinum` (24.7%) | `ABSENT` (23.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_generic` (40.2%) | `graphite_rod` (26.5%) | `ABSENT` (17.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (62.8%) | `ABSENT` (27.4%) | `carbon` (8.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (85.0%) | `ABSENT` (12.3%) | `unknown_electrode` (0.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (78.3%) | `ABSENT` (21.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (70.6%) | `Na` (16.7%) | `NBu4` (6.8%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (68.4%) | `OH` (15.7%) | `Cl` (4.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (22.9%) | `ABSENT` (10.4%) | `alkali_hydroxide` (6.6%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.7%) | `ferrocene_mediator` (1.5%) | `Co_complex` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (67.8%) | `polar_protic_alcohol` (24.8%) | `cyclic_ether` (6.2%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` + `__OTHER__` | `CC#N` (98%) | `ClCCl` (2%) | `CO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (84%) | `[K+].[OH-]` (1%) | `__ABSENT__` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #546  yield=64.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #32)

```
CCCCO.C=C(c1ccccc1)c1ccccc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCCCOC(CC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (79.3%) | `platinum` (19.8%) | `sacrificial_magnesium` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (33.0%) | `graphite_rod` (29.9%) | `graphite_generic` (23.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.3%) | `carbon` (2.7%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (97.4%) | `platinum_plate` (1.8%) | `carbon_rod` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.6%) | `NEt4` (1.8%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (66.0%) | `OH` (11.5%) | `Cl` (7.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (19.8%) | `ABSENT` (12.0%) | `polyhalo_radical_transfer` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.5%) | `ferrocene_mediator` (1.9%) | `Fe_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ABSENT` (38.8%) | `polar_aprotic_nitrile` (37.7%) | `polar_protic_alcohol` (22.6%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `__ABSENT__` (92%) | `CC#N` (35%) | `CO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (11%) | `__ABSENT__` (2%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✓ / any ✓ |

---

### Reaction #547  yield=62.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #33)

```
C=C(c1ccccc1)c1ccccc1.CCCC[N+](CCCC)(CCCC)CCCC.[2H]C([2H])([2H])C(=O)[O-]>>[2H]C([2H])([2H])CC(OCC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (75.4%) | `carbon` (23.6%) | `ABSENT` (1.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (86.1%) | `graphite_rod` (6.2%) | `platinum_plate` (3.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.9%) | `carbon` (1.6%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (89.4%) | `platinum_plate` (4.1%) | `unknown_electrode` (3.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.2%) | `Li` (6.1%) | `NEt4` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (72.9%) | `OH` (10.4%) | `carboxylate` (4.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (35.3%) | `ABSENT` (10.5%) | `alkali_hydroxide` (5.1%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `ferrocene_mediator` (0.3%) | `pyridine_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (74.4%) | `polar_aprotic_nitrile` (17.0%) | `ABSENT` (8.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (62%) | `CO` (36%) | `CN(C)C=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (70%) | `[OH][Na]` (2%) | `[Pt]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #548  yield=67.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #34)

```
C=C(C)c1ccc(C(C)(C)C)cc1>>CCOC(C)(CC)c1ccc(C(C)(C)C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (87.2%) | `platinum` (10.1%) | `ABSENT` (2.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (52.0%) | `reticulated_vitreous_carbon` (27.6%) | `graphite_generic` (13.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.6%) | `carbon` (1.0%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.9%) | `platinum_foil` (0.0%) | `platinum_plate` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (68.8%) | `NEt4` (26.5%) | `Li` (3.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (75.0%) | `BF4` (23.6%) | `carboxylate` (0.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (6.6%) | `primary_amine` (2.6%) | `polyhalo_radical_transfer` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.9%) | `Co_complex` (0.7%) | `Mn_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (36.1%) | `ABSENT` (34.1%) | `polar_aprotic_nitrile` (28.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (83%) | `CCO` (16%) | `CO` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O=O` (1%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Oc1ccccc1C=NCCN=Cc` (0%) | `O=S(=O)([O-])C(F)(` (0%) | set ✓ / any ✓ |

---

### Reaction #549  yield=62.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #35)

```
C=C(c1ccccc1)C1CCC1>>CCOC(CC)(c1ccccc1)C1CCC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.9%) | `platinum` (6.0%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_generic` (58.9%) | `platinum_generic` (18.3%) | `carbon_rod` (9.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `stainless_steel` (0.1%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.8%) | `platinum_plate` (0.1%) | `platinum_wire` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.8%) | `Li` (10.5%) | `K` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (39.6%) | `ClO4` (36.4%) | `carboxylate` (21.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.1%) | `polyhalo_radical_transfer` (5.6%) | `transition_metal_salt_reagent` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.8%) | `Mn_complex` (3.1%) | `Co_complex` (1.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (98.9%) | `polar_aprotic_nitrile` (1.1%) | `cyclic_ether` (0.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (98%) | `CO` (71%) | `CCO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (57%) | `[Pt]` (34%) | `O.O.O.O.O.O.O.O.O.` (3%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `Brc1ccc(N(c2ccc(Br` (1%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #550  yield=64.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #36)

```
C=C(C)c1ccccc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCOC(C)(CC)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.3%) | `carbon` (33.1%) | `ABSENT` (1.4%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (94.1%) | `graphite_generic` (2.1%) | `carbon_generic` (1.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (90.5%) | `carbon` (5.8%) | `ABSENT` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.7%) | `unknown_electrode` (0.4%) | `carbon_generic` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (70.4%) | `NBu4` (16.8%) | `Na` (4.0%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (63.4%) | `ClO4` (11.6%) | `molecular_no_ion` (7.4%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (27.0%) | `ABSENT` (8.9%) | `selenium_reagent` (2.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `pyridine_organocat` (0.0%) | `Fe_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (61.5%) | `polar_aprotic_nitrile` (36.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CC(C)(C)O` | `CC#N` (95%) | `CO` (5%) | `ClCCl` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (99%) | `[Pt]` (1%) | `[Li+].[O-][Cl+3]([` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #551  yield=68.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #37)

```
CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC.C=C(C)c1ccc(C(=O)OC)cc1>>CCOC(C)(CC)c1ccc(C(=O)OC)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (79.2%) | `carbon` (19.6%) | `ABSENT` (1.1%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (48.9%) | `graphite_generic` (41.3%) | `platinum_plate` (7.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.1%) | `carbon` (2.1%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (97.7%) | `platinum_plate` (1.5%) | `graphite_generic` (0.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.4%) | `Na` (4.7%) | `NEt4` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (33.4%) | `Br` (28.7%) | `Cl` (13.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (21.8%) | `ABSENT` (15.3%) | `tetraaryl_borate` (1.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.0%) | `Fe_complex` (2.7%) | `pyridine_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (77.6%) | `polar_protic_alcohol` (20.2%) | `ABSENT` (0.8%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (99%) | `ClCCl` (2%) | `CC(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (85%) | `__ABSENT__` (3%) | `O.O.O.O.O.O.O.O.O.` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #552  yield=65.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #38)

```
CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC.C=C(c1ccccc1)c1cccc(F)c1>>CCOC(CC)(c1ccccc1)c1cccc(F)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (64.3%) | `platinum` (35.6%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (73.0%) | `graphite_rod` (13.5%) | `graphite_generic` (10.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.3%) | `carbon` (1.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.7%) | `platinum_plate` (0.9%) | `carbon_rod` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (76.4%) | `ABSENT` (9.5%) | `Na` (7.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (22.3%) | `molecular_no_ion` (21.3%) | `BF4` (18.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (17.5%) | `ABSENT` (14.9%) | `alkali_hydroxide` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.2%) | `ferrocene_mediator` (8.0%) | `pyridine_organocat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (68.9%) | `polar_aprotic_nitrile` (30.0%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (97%) | `CO` (3%) | `CCO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (25%) | `O=O` (5%) | `[Pt]` (2%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #553  yield=64.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #39)

```
CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC.C=C(c1ccccc1)c1ccc(Cl)cc1>>CCOC(CC)(c1ccccc1)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (72.0%) | `carbon` (27.6%) | `ABSENT` (0.3%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (61.4%) | `platinum_plate` (23.9%) | `graphite_rod` (10.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.3%) | `carbon` (2.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (83.3%) | `platinum_plate` (15.8%) | `carbon_rod` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (71.6%) | `Na` (18.7%) | `ABSENT` (4.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `Cl` (25.1%) | `OH` (22.8%) | `carboxylate` (21.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (31.9%) | `ABSENT` (12.3%) | `alkali_hydroxide` (5.6%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.1%) | `pyridine_organocat` (1.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (89.9%) | `polar_protic_alcohol` (8.9%) | `cyclic_ether` (0.5%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (100%) | `C1CCOC1` (0%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (23%) | `O=O` (22%) | `[K+].[OH-]` (6%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #554  yield=61.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #40)

```
C=C(c1ccc(F)cc1)c1ccc(F)cc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCOC(CC)(c1ccc(F)cc1)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (59.7%) | `carbon` (35.9%) | `ABSENT` (4.2%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (53.1%) | `graphite_rod` (30.7%) | `ABSENT` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.1%) | `ABSENT` (0.5%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (95.8%) | `platinum_plate` (3.3%) | `ABSENT` (0.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.3%) | `Na` (7.0%) | `K` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `OH` (66.0%) | `BF4` (14.3%) | `carboxylate` (4.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (23.6%) | `ABSENT` (11.7%) | `alkali_hydroxide` (4.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (68.8%) | `ferrocene_mediator` (28.3%) | `Fe_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (51.0%) | `polar_aprotic_nitrile` (31.9%) | `cyclic_ether` (14.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (92%) | `CO` (3%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (45%) | `__ABSENT__` (6%) | `[K+].[OH-]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl-].[Cl-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #555  yield=69.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #41)

```
CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC.C=C(C)c1ccc(OC(F)(F)F)cc1>>CCOC(C)(CC)c1ccc(OC(F)(F)F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (83.5%) | `carbon` (15.0%) | `ABSENT` (1.4%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (79.1%) | `platinum_plate` (10.6%) | `graphite_rod` (5.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `carbon` (0.3%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.4%) | `platinum_plate` (3.5%) | `unknown_electrode` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `ABSENT` (1.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (53.8%) | `ABSENT` (25.2%) | `NEt4` (11.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `Cl` (68.4%) | `ABSENT` (14.5%) | `BF4` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (43.9%) | `ABSENT` (11.2%) | `metal_oxide_oxidant` (1.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.9%) | `organic_neutral_cat` (0.4%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (82.2%) | `polar_protic_alcohol` (16.2%) | `cyclic_ether` (0.9%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (100%) | `ClCCl` (2%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (43%) | `__ABSENT__` (18%) | `[Pt]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `N#Cc1c(C#N)c(-n2c3` (0%) | set ✓ / any ✓ |

---

### Reaction #556  yield=72.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #42)

```
CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC.C=C(c1ccccc1)c1cccc(Br)c1>>CCOC(CC)(c1ccccc1)c1cccc(Br)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.3%) | `platinum` (6.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `graphite_generic` (49.7%) | `graphite_rod` (25.7%) | `platinum_generic` (15.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.4%) | `nickel` (0.9%) | `carbon` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.2%) | `platinum_plate` (3.4%) | `nickel_plate` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (85.4%) | `Na` (11.4%) | `ABSENT` (1.5%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (39.9%) | `BF4` (16.1%) | `carboxylate` (10.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (37.4%) | `ABSENT` (6.7%) | `alkali_hydroxide` (1.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.0%) | `ferrocene_mediator` (5.8%) | `pyridine_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (54.9%) | `polar_protic_alcohol` (40.5%) | `ABSENT` (3.4%) | ✓ |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (100%) | `CO` (0%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (28%) | `__ABSENT__` (10%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[cH]12->[Fe+2]3456` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #557  yield=75.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #43)

```
C=C(c1ccccc1)c1ccccc1>>CCC(OC(C)=O)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (87.7%) | `platinum` (8.6%) | `sacrificial_magnesium` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `glassy_carbon` (49.9%) | `graphite_generic` (17.6%) | `carbon_rod` (15.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (73.9%) | `platinum` (20.5%) | `stainless_steel` (2.4%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `unknown_electrode` (33.1%) | `graphite_generic` (20.2%) | `carbon_generic` (11.6%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (77.5%) | `ABSENT` (22.1%) | `divided` (0.4%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.7%) | `NEt4` (7.6%) | `Li` (1.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (59.1%) | `ClO4` (30.4%) | `PF6` (6.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (5.9%) | `polyhalo_radical_transfer` (5.7%) | `o2_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (87.3%) | `Mn_complex` (8.4%) | `organic_neutral_cat` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (55.2%) | `polar_aprotic_nitrile` (42.3%) | `cyclic_ether` (1.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CCO` (93%) | `CC#N` (87%) | `CO` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1ccc(I)cc1` + `F.c1ccncc1` + `O=C(O)O.[Na]` + `[OH][Na]` | `O=C(O)O.[Na]` (91%) | `Cc1ccc(I)cc1` (83%) | `F.c1ccncc1` (79%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `Brc1ccc(N(c2ccc(Br` | `Brc1ccc(N(c2ccc(Br` (97%) | `c1ccncc1` (15%) | `CC(C)(C)c1cc(C=N[C` (1%) | set ✓ / any ✓ |

---

### Reaction #558  yield=75.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #44)

```
C=C(c1ccccc1)c1ccccc1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCOC(CC)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (65.6%) | `carbon` (31.4%) | `ABSENT` (2.9%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (78.4%) | `graphite_rod` (15.2%) | `ABSENT` (1.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.1%) | `ABSENT` (3.4%) | `carbon` (2.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `carbon_rod` (1.1%) | `ABSENT` (1.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.3%) | `ABSENT` (1.7%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (57.2%) | `Na` (18.8%) | `Li` (9.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `OH` (53.4%) | `ClO4` (18.2%) | `molecular_no_ion` (7.6%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (43.9%) | `alkali_hydroxide` (9.7%) | `ABSENT` (4.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (87.5%) | `ferrocene_mediator` (9.7%) | `unparseable_text` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (71.8%) | `polar_aprotic_nitrile` (25.6%) | `cyclic_ether` (1.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CC(C)(C)O` | `CC#N` (71%) | `CO` (28%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O` | `O=O` (80%) | `[K+].[OH-]` (4%) | `[OH][Na]` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #559  yield=79.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #45)

```
C=C(c1ccccc1)C1CCCCC1.CC(=O)[O-].CCCC[N+](CCCC)(CCCC)CCCC>>CCOC(CC)(c1ccccc1)C1CCCCC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (65.5%) | `platinum` (34.0%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (67.8%) | `graphite_generic` (15.4%) | `unknown_electrode` (9.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.0%) | `ABSENT` (0.4%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.8%) | `platinum_plate` (0.1%) | `unknown_electrode` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.2%) | `ABSENT` (0.8%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Na` (65.3%) | `NBu4` (12.9%) | `ABSENT` (9.4%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (73.0%) | `carboxylate` (9.2%) | `OH` (4.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (17.6%) | `o2_oxidant` (5.4%) | `alkali_hydroxide` (4.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.2%) | `ferrocene_mediator` (2.1%) | `pyridine_organocat` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (68.3%) | `polar_aprotic_nitrile` (31.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC#N` (99%) | `CO` (5%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `[K+].[OH-]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #560  yield=78.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_31_e202506639.json) (反应 idx 在该 JSON 内 = #46)

```
C=C(C)c1ccc(C2CCCCC2)cc1>>CCOC(C)(CC)c1ccc(C2CCCCC2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `ABSENT` (48.6%) | `carbon` (34.8%) | `platinum` (12.9%) | ✓ |
| 阳极 (细类) | 43 | `graphite_cloth` | `platinum_generic` (34.5%) | `unknown_electrode` (30.6%) | `graphite_generic` (10.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `ABSENT` (0.8%) | `carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.9%) | `platinum_wire` (0.0%) | `platinum_plate` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.7%) | `NEt4` (4.4%) | `Li` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `BF4` (70.9%) | `ClO4` (21.7%) | `Br` (3.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.9%) | `hydrosilane` (3.0%) | `primary_amine` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (62.8%) | `Co_complex` (14.4%) | `ammonium_PTC_organocat` (11.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (52.5%) | `polar_aprotic_nitrile` (30.2%) | `ABSENT` (7.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCO` + `CC#N` | `CC(C)=O` (45%) | `CC#N` (29%) | `CCO` (21%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[O]=[Ti]=[O]` (0%) | `[O]=[Fe][O][Fe]=[O` (0%) | set ✓ / any ✓ |

---

### Reaction #561  yield=40.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #0)

```
O=C=O.C=CC1OC1/C=C/c1ccccc1>>O=C(O)C/C=C/C=C/C(C(=O)O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (97.3%) | `sacrificial_iron` (0.8%) | `sacrificial_zinc` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_rod` (63.8%) | `magnesium_generic` (16.3%) | `magnesium_plate` (14.5%) | ✓ |
| 阴极 (材料) | 15 | `other_electrode` | `nickel` (33.8%) | `platinum` (23.4%) | `ABSENT` (14.9%) | ✗ |
| 阴极 (细类) | 49 | `niobium_plate` | `platinum_generic` (18.8%) | `unknown_electrode` (17.6%) | `carbon_rod` (16.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (95.5%) | `ABSENT` (4.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (71.0%) | `ABSENT` (24.1%) | `Li` (3.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (33.4%) | `ABSENT` (29.5%) | `BF4` (28.9%) | ✗ |
| 试剂大类 | 103 | `hcl` | `ester` (8.1%) | `pyridine` (4.5%) | `ABSENT` (4.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.3%) | `Ni_complex` (5.8%) | `brønsted_acid_cat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (97.4%) | `polar_aprotic_nitrile` (2.3%) | `polar_aprotic_sulfoxide` (0.1%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (100%) | `O` (36%) | `CCOCC` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `Cl` (99%) | `COC(=O)c1ccc(C(C)(` (10%) | `O=C([O-])[O-].[K+]` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `__OTHER__` (1%) | `[Br-][Ni+2]12([Br-` (0%) | set ✓ / any ✓ |

---

### Reaction #562  yield=34.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #1)

```
O=C=O.C=C[C@@H]1O[C@]1(C)CCc1ccc(OC)cc1.C=C[C@@H]1O[C@@]1(C)CCc1ccc(OC)cc1>>COc1ccc(CCC(C)(/C=C/CC(=O)O)C(=O)O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (72.8%) | `sacrificial_aluminum` (13.1%) | `sacrificial_zinc` (10.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `aluminum_plate` (48.1%) | `magnesium_generic` (28.0%) | `magnesium_plate` (8.1%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (70.2%) | `platinum` (26.1%) | `carbon` (2.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_plate` | `nickel_foam` (65.8%) | `platinum_generic` (26.5%) | `nickel_generic` (4.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (71.7%) | `ABSENT` (28.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.9%) | `Na` (9.8%) | `K` (7.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `I` (61.3%) | `ClO4` (8.0%) | `PF6` (7.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `hcl` | `ABSENT` (12.3%) | `ester` (4.7%) | `phthalimide_N_anion` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.6%) | `Ni_complex` (2.2%) | `amidine_guanidine_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (80.2%) | `polar_aprotic_sulfoxide` (11.7%) | `polar_aprotic_nitrile` (7.3%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (82%) | `O` (19%) | `CS(C)=O` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `__ABSENT__` (99%) | `Cl` (1%) | `Cc1ccc(S(=O)(=O)O)` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #563  yield=34.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #2)

```
O=C=O.C=C[C@@H]1O[C@]1(C)CCc1ccccc1.C=C[C@@H]1O[C@@]1(C)CCc1ccccc1>>CC(/C=C/CC(=O)O)(CCc1ccccc1)C(=O)O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (89.5%) | `sacrificial_zinc` (7.9%) | `sacrificial_aluminum` (1.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_plate` (63.0%) | `aluminum_plate` (16.7%) | `magnesium_generic` (7.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `platinum` (55.6%) | `nickel` (39.6%) | `carbon` (3.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_plate` | `nickel_foam` (51.8%) | `platinum_generic` (42.0%) | `platinum_foil` (2.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (80.5%) | `ABSENT` (19.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (60.6%) | `NBu4` (21.6%) | `Na` (7.0%) | ✓ |
| 电解质 anion | 26 | `I` | `ABSENT` (43.3%) | `Cl` (19.0%) | `I` (14.8%) | ✓ |
| 试剂大类 | 103 | `hcl` | `ester` (10.6%) | `ABSENT` (8.1%) | `hcl` (4.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.0%) | `Ni_complex` (3.6%) | `amidine_guanidine_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (85.6%) | `polar_aprotic_nitrile` (10.3%) | `polar_aprotic_sulfoxide` (3.6%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (97%) | `O` (38%) | `CN1CCCC1=O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `Cl` (99%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #564  yield=31.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #3)

```
O=C=O.C=C[C@@H]1O[C@]1(C)c1ccc(SC)cc1.C=C[C@@H]1O[C@@]1(C)c1ccc(SC)cc1>>CSc1ccc(C(C)(/C=C/CC(=O)O)C(=O)O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (98.7%) | `sacrificial_aluminum` (0.7%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_plate` (78.2%) | `magnesium_generic` (19.1%) | `aluminum_plate` (1.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (74.8%) | `carbon` (15.3%) | `platinum` (9.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_plate` | `nickel_foam` (39.0%) | `nickel_generic` (30.4%) | `graphite_generic` (12.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.9%) | `Li` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (65.4%) | `ClO4` (14.9%) | `PF6` (12.5%) | ✗ |
| 试剂大类 | 103 | `hcl` | `ABSENT` (20.5%) | `ester` (10.5%) | `water` (3.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.1%) | `Ni_complex` (0.8%) | `amidine_guanidine_organocat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (83.5%) | `ABSENT` (8.8%) | `cyclic_ether` (2.3%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (94%) | `O` (1%) | `__ABSENT__` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #565  yield=41.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #4)

```
O=C=O.C=C[C@@H]1O[C@@H]1/C(C)=C/c1ccccc1.C=C[C@@H]1O[C@H]1/C(C)=C/c1ccccc1>>C/C(=C\C=C\CC(=O)O)C(C(=O)O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (96.7%) | `sacrificial_zinc` (2.3%) | `sacrificial_aluminum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_plate` (88.0%) | `magnesium_generic` (11.0%) | `magnesium_rod` (0.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `other_electrode` | `carbon` (70.0%) | `nickel` (15.4%) | `platinum` (7.5%) | ✗ |
| 阴极 (细类) | 49 | `niobium_plate` | `graphite_felt` (75.8%) | `graphite_generic` (10.4%) | `carbon_felt` (2.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (74.1%) | `ABSENT` (25.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (56.2%) | `NEt4` (35.4%) | `Li` (8.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (45.3%) | `Cl` (25.4%) | `Br` (17.3%) | ✓ |
| 试剂大类 | 103 | `hcl` | `ABSENT` (25.6%) | `hcl` (9.1%) | `ester` (4.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `Ni_complex` (0.2%) | `organic_neutral_cat` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (74.5%) | `polar_aprotic_nitrile` (23.5%) | `cyclic_ether` (0.8%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (97%) | `O` (64%) | `CC#N` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `__ABSENT__` (92%) | `Cl` (8%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #566  yield=54.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #5)

```
O=C=O.C=C[C@@H]1O[C@]1(C)c1ccc2c(c1)OCO2.C=C[C@@H]1O[C@@]1(C)c1ccc2c(c1)OCO2>>CC(/C=C/CC(=O)O)(C(=O)O)c1ccc2c(c1)OCO2
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (96.7%) | `nickel` (1.1%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_generic` (49.3%) | `magnesium_plate` (36.5%) | `carbon_rod` (5.0%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (47.7%) | `platinum` (30.6%) | `carbon` (20.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_plate` | `nickel_foam` (42.9%) | `platinum_plate` (33.5%) | `nickel_plate` (6.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.5%) | `ABSENT` (1.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (59.2%) | `ABSENT` (38.1%) | `K` (2.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `ABSENT` (57.4%) | `I` (29.0%) | `PF6` (6.6%) | ✓ |
| 试剂大类 | 103 | `hcl` | `ABSENT` (13.8%) | `water` (8.1%) | `ester` (6.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `Ni_complex` (0.5%) | `amidine_guanidine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (80.9%) | `polar_aprotic_sulfoxide` (9.9%) | `cyclic_ether` (4.3%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `O` (64%) | `CN(C)C=O` (42%) | `CS(C)=O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `__ABSENT__` (100%) | `Cl` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #567  yield=61.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #6)

```
O=C=O.C=C[C@@H]1O[C@]1(C)c1ccc2ccccc2c1.C=C[C@@H]1O[C@@]1(C)c1ccc2ccccc2c1>>CC(/C=C/CC(=O)O)(C(=O)O)c1ccc2ccccc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (98.6%) | `nickel` (0.6%) | `sacrificial_iron` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_plate` (88.9%) | `magnesium_generic` (7.9%) | `magnesium_rod` (0.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (50.8%) | `carbon` (35.5%) | `platinum` (11.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_plate` | `nickel_foam` (53.1%) | `graphite_generic` (9.4%) | `nickel_generic` (8.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.2%) | `ABSENT` (2.2%) | `K` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `I` (53.1%) | `BF4` (25.5%) | `ABSENT` (8.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `hcl` | `ABSENT` (14.2%) | `ester` (10.6%) | `water` (10.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `Ni_complex` (0.5%) | `amidine_guanidine_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (92.3%) | `ABSENT` (2.3%) | `cyclic_ether` (2.2%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (89%) | `O` (16%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `__ABSENT__` (100%) | `Cl` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #568  yield=63.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #7)

```
O=C=O.C=C[C@@H]1O[C@@H]1c1ccc(F)c(C)c1.C=C[C@@H]1O[C@H]1c1ccc(F)c(C)c1>>Cc1cc(C(/C=C/CC(=O)O)C(=O)O)ccc1F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (99.5%) | `platinum` (0.2%) | `sacrificial_aluminum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_plate` (92.9%) | `magnesium_generic` (3.5%) | `graphite_generic` (2.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `other_electrode` | `platinum` (61.7%) | `carbon` (36.7%) | `nickel` (0.7%) | ✗ |
| 阴极 (细类) | 49 | `niobium_plate` | `graphite_generic` (94.3%) | `platinum_generic` (3.8%) | `graphite_felt` (0.8%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.2%) | `NEt4` (3.5%) | `Li` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `I` (49.5%) | `Cl` (19.7%) | `ClO4` (11.6%) | ✗ |
| 试剂大类 | 103 | `hcl` | `ester` (10.4%) | `iodide_anion` (7.4%) | `ABSENT` (3.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `organic_neutral_cat` (0.4%) | `Ni_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (49.9%) | `polar_aprotic_amide` (44.0%) | `cyclic_ether` (4.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `O` (86%) | `CC#N` (85%) | `CN(C)C=O` (11%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `Cl` (98%) | `O=C([O-])[O-].[K+]` (4%) | `__ABSENT__` (2%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Br][Ni][Br].c1cc(` (0%) | set ✓ / any ✓ |

---

### Reaction #569  yield=69.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #8)

```
O=C=O.C=C[C@@H]1O[C@@]1(c1ccccc1)C1CC1.C=C[C@@H]1O[C@]1(c1ccccc1)C1CC1>>O=C(O)C/C=C/C(C(=O)O)(c1ccccc1)C1CC1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (98.8%) | `sacrificial_iron` (0.7%) | `sacrificial_zinc` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_plate` (85.7%) | `magnesium_generic` (10.7%) | `magnesium_rod` (1.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (61.5%) | `platinum` (29.1%) | `carbon` (7.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_plate` | `nickel_foam` (57.7%) | `carbon_felt` (9.4%) | `nickel_plate` (7.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `NBu4` (81.4%) | `ABSENT` (15.0%) | `Li` (3.3%) | ✗ |
| 电解质 anion | 26 | `I` | `ABSENT` (41.8%) | `ClO4` (23.3%) | `I` (13.4%) | ✓ |
| 试剂大类 | 103 | `hcl` | `ester` (11.1%) | `ABSENT` (9.7%) | `secondary_amine` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (82.3%) | `Ni_complex` (13.3%) | `Mn_complex` (1.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (48.5%) | `ABSENT` (34.6%) | `polar_aprotic_nitrile` (14.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (88%) | `CC#N` (4%) | `CC(=O)N(C)C` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `Cl` | `Cl` (90%) | `O=C([O-])[O-].[K+]` (24%) | `__ABSENT__` (8%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (0%) | `[Br-][Ni+2]12([Br-` (0%) | set ✓ / any ✓ |

---

### Reaction #570  yield=65.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #9)

```
O=C=O.C=CC1OC1(C)c1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc(C(C)(/C=C/CC(=O)O)C(=O)O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (97.7%) | `nickel` (1.3%) | `sacrificial_aluminum` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_plate` (96.6%) | `magnesium_generic` (2.3%) | `aluminum_plate` (0.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `carbon` (77.7%) | `nickel` (13.5%) | `platinum` (7.9%) | ✓ |
| 阴极 (细类) | 49 | `nickel_plate` | `graphite_generic` (70.8%) | `graphite_felt` (9.5%) | `nickel_foam` (5.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.2%) | `NEt4` (0.9%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `ClO4` (43.1%) | `BF4` (27.6%) | `I` (18.5%) | ✓ |
| 试剂大类 | 103 | `hcl` | `ester` (14.5%) | `ABSENT` (13.0%) | `hcl` (7.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `amidine_guanidine_organocat` (0.3%) | `Mn_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (85.5%) | `ABSENT` (6.1%) | `polar_aprotic_nitrile` (5.4%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (62%) | `CC#N` (17%) | `O` (13%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `Cl` (97%) | `__ABSENT__` (3%) | `O=C([O-])[O-].[K+]` (3%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #571  yield=65.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #10)

```
O=C=O.C=C[C@@H]1O[C@]1(C)c1cccc(F)c1.C=C[C@@H]1O[C@@]1(C)c1cccc(F)c1>>CC(/C=C/CC(=O)O)(C(=O)O)c1cccc(F)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (99.3%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_plate` (96.5%) | `magnesium_generic` (2.8%) | `nickel_plate` (0.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `carbon` (92.7%) | `nickel` (4.7%) | `platinum` (2.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_plate` | `graphite_felt` (45.7%) | `graphite_generic` (38.8%) | `carbon_generic` (5.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.1%) | `ABSENT` (2.7%) | `Li` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `ClO4` (36.4%) | `BF4` (18.0%) | `ABSENT` (12.4%) | ✗ |
| 试剂大类 | 103 | `hcl` | `ester` (29.0%) | `ABSENT` (8.5%) | `metal_oxide_oxidant` (1.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `amidine_guanidine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (59.4%) | `polar_aprotic_sulfoxide` (17.9%) | `polar_aprotic_nitrile` (9.9%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (47%) | `O` (32%) | `CC#N` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `Cl` (79%) | `__ABSENT__` (20%) | `O=C([O-])[O-].[K+]` (9%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #572  yield=68.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #11)

```
O=C=O.C=C[C@@H]1O[C@@H]1c1cc(C)cc(C)c1.C=C[C@@H]1O[C@H]1c1cc(C)cc(C)c1>>Cc1cc(C)cc(C(/C=C/CC(=O)O)C(=O)O)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `sacrificial_magnesium` (96.4%) | `platinum` (2.9%) | `sacrificial_aluminum` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `unknown_electrode` | `magnesium_plate` (39.6%) | `magnesium_generic` (34.0%) | `platinum_generic` (17.8%) | ✗ |
| 阴极 (材料) | 15 | `other_electrode` | `platinum` (48.7%) | `carbon` (47.2%) | `nickel` (3.0%) | ✗ |
| 阴极 (细类) | 49 | `niobium_plate` | `graphite_generic` (85.3%) | `carbon_rod` (7.6%) | `platinum_generic` (4.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.7%) | `Li` (2.6%) | `NEt4` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `ClO4` (87.2%) | `BF4` (5.7%) | `PF6` (4.2%) | ✗ |
| 试剂大类 | 103 | `bromide_anion` | `ester` (8.5%) | `silane_other` (7.8%) | `ABSENT` (4.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.5%) | `brønsted_acid_cat` (1.8%) | `organic_neutral_cat` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (92.0%) | `polar_aprotic_nitrile` (3.8%) | `cyclic_ether` (1.9%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (84%) | `O` (7%) | `CC#N` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` + `Cl` | `Cl` (99%) | `O=C([O-])[O-].[K+]` (24%) | `CCCC[N+](CCCC)(CCC` (2%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Br][Ni][Br].c1cc(` (0%) | set ✓ / any ✓ |

---

### Reaction #573  yield=62.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #12)

```
O=C=O.C=C[C@@H]1O[C@@H]1c1cccc(OC)c1F.C=C[C@@H]1O[C@H]1c1cccc(OC)c1F>>COc1cccc(C(/C=C/CC(=O)O)C(=O)O)c1F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (98.8%) | `platinum` (0.3%) | `carbon` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_plate` (83.0%) | `magnesium_generic` (8.7%) | `platinum_generic` (4.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `other_electrode` | `carbon` (58.2%) | `platinum` (26.2%) | `nickel` (14.4%) | ✗ |
| 阴极 (细类) | 49 | `niobium_plate` | `graphite_generic` (69.2%) | `graphite_felt` (10.4%) | `platinum_generic` (5.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.2%) | `NEt4` (0.4%) | `Li` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `I` (39.3%) | `Cl` (28.1%) | `ClO4` (14.9%) | ✗ |
| 试剂大类 | 103 | `hcl` | `ester` (22.7%) | `ABSENT` (3.6%) | `thiol` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.4%) | `Ni_complex` (0.9%) | `organic_neutral_cat` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (55.6%) | `polar_aprotic_nitrile` (28.7%) | `cyclic_ether` (12.6%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (60%) | `CC#N` (16%) | `O` (16%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `Cl` (98%) | `O=C([O-])[O-].[K+]` (3%) | `__ABSENT__` (2%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #574  yield=61.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #13)

```
O=C=O.C=C[C@@H]1O[C@]1(C)c1ccc(F)c(C)c1.C=C[C@@H]1O[C@@]1(C)c1ccc(F)c(C)c1>>Cc1cc(C(C)(/C=C/CC(=O)O)C(=O)O)ccc1F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (99.8%) | `sacrificial_aluminum` (0.1%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_plate` (86.9%) | `magnesium_generic` (12.9%) | `nickel_plate` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `carbon` (89.1%) | `platinum` (9.9%) | `nickel` (0.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_plate` | `graphite_generic` (68.9%) | `graphite_felt` (18.3%) | `platinum_plate` (5.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.5%) | `NEt4` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `I` (36.5%) | `BF4` (31.6%) | `ClO4` (9.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `hcl` | `ABSENT` (18.0%) | `ester` (14.1%) | `hcl` (3.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Ni_complex` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (77.6%) | `polar_aprotic_nitrile` (9.4%) | `polar_aprotic_sulfoxide` (4.8%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (81%) | `O` (40%) | `CC#N` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `__ABSENT__` (100%) | `Cl` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `[Br][Ni][Br].c1cc(` (0%) | set ✓ / any ✓ |

---

### Reaction #575  yield=70.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #14)

```
O=C=O.C=C[C@@H]1O[C@]1(C)c1ccc(C)cc1.C=C[C@@H]1O[C@@]1(C)c1ccc(C)cc1>>Cc1ccc(C(C)(/C=C/CC(=O)O)C(=O)O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (94.4%) | `sacrificial_zinc` (2.0%) | `nickel` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_plate` (86.0%) | `magnesium_generic` (7.8%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `carbon` (59.4%) | `nickel` (32.2%) | `platinum` (6.3%) | ✓ |
| 阴极 (细类) | 49 | `nickel_plate` | `graphite_generic` (21.2%) | `nickel_foam` (20.3%) | `nickel_plate` (15.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.9%) | `NEt4` (0.5%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `BF4` (72.3%) | `ClO4` (12.5%) | `I` (5.3%) | ✓ |
| 试剂大类 | 103 | `hcl` | `ABSENT` (13.6%) | `hcl` (4.7%) | `water` (4.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `ammonium_PTC_organocat` (0.2%) | `Ni_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (87.7%) | `ABSENT` (4.4%) | `polar_aprotic_nitrile` (3.0%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (95%) | `O` (2%) | `CC#N` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `__ABSENT__` (98%) | `Cl` (2%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #576  yield=71.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #15)

```
O=C=O.C=C[C@H]1O[C@]1(C)c1ccccc1.C=C[C@@H]1O[C@]1(C)c1ccccc1>>CC(/C=C/CC(=O)O)(C(=O)O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (97.4%) | `sacrificial_aluminum` (1.1%) | `sacrificial_zinc` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_plate` (91.4%) | `magnesium_generic` (5.8%) | `aluminum_plate` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `carbon` (53.5%) | `nickel` (41.4%) | `platinum` (1.8%) | ✓ |
| 阴极 (细类) | 49 | `nickel_plate` | `nickel_foam` (43.3%) | `graphite_felt` (27.1%) | `graphite_generic` (7.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.9%) | `NEt4` (0.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `ClO4` (26.8%) | `I` (22.5%) | `BF4` (16.4%) | ✓ |
| 试剂大类 | 103 | `hcl` | `ester` (17.1%) | `ABSENT` (8.5%) | `hcl` (5.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `amidine_guanidine_organocat` (0.5%) | `Ni_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (90.5%) | `polar_aprotic_sulfoxide` (2.6%) | `polar_aprotic_nitrile` (2.6%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (96%) | `O` (60%) | `CN1CCCC1=O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `Cl` (99%) | `O=C([O-])[O-].[K+]` (28%) | `COC(=O)c1ccccc1` (3%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #577  yield=76.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #16)

```
O=C=O.C=C[C@@H]1O[C@]1(C)c1ccc(-c2ccccc2)cc1.C=C[C@@H]1O[C@@]1(C)c1ccc(-c2ccccc2)cc1>>CC(/C=C/CC(=O)O)(C(=O)O)c1ccc(-…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (91.4%) | `sacrificial_iron` (4.5%) | `sacrificial_zinc` (1.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_plate` (96.8%) | `magnesium_generic` (1.1%) | `aluminum_plate` (0.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (51.2%) | `platinum` (27.1%) | `carbon` (20.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_plate` | `nickel_foam` (91.1%) | `graphite_felt` (4.4%) | `platinum_plate` (1.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.1%) | `NEt4` (0.3%) | `Li` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `I` (51.2%) | `BF4` (15.2%) | `ClO4` (11.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `hcl` | `ester` (23.1%) | `ABSENT` (10.7%) | `hcl` (4.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.8%) | `amidine_guanidine_organocat` (2.5%) | `Ni_complex` (1.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (92.7%) | `ABSENT` (3.2%) | `polar_aprotic_nitrile` (2.8%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CN(C)C=O` (99%) | `O` (46%) | `CN1CCCC1=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `Cl` (98%) | `O=C([O-])[O-].[K+]` (2%) | `__ABSENT__` (2%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COCCOC.[Br][Ni][Br` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #578  yield=78.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #17)

```
O=C=O.C=C[C@@H]1O[C@]1(C)c1ccc(F)cc1.C=C[C@@H]1O[C@@]1(C)c1ccc(F)cc1>>CC(/C=C/CCCC(=O)O)(C(=O)O)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (56.2%) | `nickel` (29.0%) | `sacrificial_zinc` (10.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `nickel_plate` (52.4%) | `magnesium_plate` (32.3%) | `carbon_rod` (6.9%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `carbon` (74.4%) | `nickel` (11.2%) | `platinum` (10.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_plate` | `graphite_generic` (29.9%) | `platinum_plate` (16.8%) | `graphite_felt` (13.5%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.2%) | `ABSENT` (0.8%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (45.2%) | `NBu4` (42.3%) | `ABSENT` (6.2%) | ✓ |
| 电解质 anion | 26 | `I` | `I` (69.9%) | `PF6` (11.0%) | `carboxylate` (10.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `hcl` | `ABSENT` (11.9%) | `water` (10.1%) | `ester` (4.0%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `Ni_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (83.4%) | `polar_aprotic_sulfoxide` (5.5%) | `ABSENT` (4.8%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `O` (58%) | `CN(C)C=O` (54%) | `CC(C)=O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `__ABSENT__` (99%) | `Cl` (1%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #579  yield=72.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #18)

```
O=C=O.C=C[C@@H]1O[C@@H]1c1ccc(NC(C)=O)cc1.C=C[C@@H]1O[C@H]1c1ccc(NC(C)=O)cc1>>CC(=O)Nc1ccc(C(/C=C/CC(=O)O)C(=O)O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (98.6%) | `sacrificial_aluminum` (0.5%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_generic` | `magnesium_plate` (73.5%) | `magnesium_generic` (17.1%) | `graphite_generic` (3.7%) | ✓ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (73.7%) | `carbon` (18.5%) | `nickel` (4.4%) | ✓ |
| 阴极 (细类) | 49 | `nickel_generic` | `graphite_generic` (61.6%) | `platinum_generic` (15.3%) | `graphite_felt` (7.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (83.9%) | `NEt4` (8.5%) | `Li` (6.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `ClO4` (45.1%) | `BF4` (26.6%) | `Cl` (9.9%) | ✗ |
| 试剂大类 | 103 | `chloride_anion` | `ester` (7.5%) | `ABSENT` (3.3%) | `hcl` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.2%) | `Ni_complex` (2.2%) | `organic_neutral_cat` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_amide` (69.6%) | `polar_aprotic_nitrile` (26.6%) | `cyclic_ether` (1.8%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `O` (88%) | `CN(C)C=O` (87%) | `CC#N` (11%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Cl-].[H+]` | `Cl` (99%) | `O=C([O-])[O-].[K+]` (6%) | `COC(=O)c1ccc2cc(C(` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[Br][Ni][Br].c1cc(` (0%) | set ✓ / any ✓ |

---

### Reaction #580  yield=83.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #19)

```
O=C=O.C=C[C@@H]1O[C@@H]1c1ccccc1F.C=C[C@H]1O[C@@H]1c1ccccc1F>>O=C(O)C/C=C/C(C(=O)O)c1ccccc1F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (87.5%) | `platinum` (10.9%) | `sacrificial_iron` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `platinum_generic` (72.3%) | `magnesium_plate` (15.8%) | `platinum_plate` (7.1%) | ✓ |
| 阴极 (材料) | 15 | `other_electrode` | `carbon` (74.8%) | `platinum` (15.5%) | `nickel` (6.6%) | ✗ |
| 阴极 (细类) | 49 | `niobium_plate` | `graphite_generic` (72.7%) | `graphite_felt` (16.9%) | `carbon_rod` (4.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.2%) | `NEt4` (2.4%) | `Li` (1.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Cl` (33.0%) | `ClO4` (31.8%) | `BF4` (22.9%) | ✗ |
| 试剂大类 | 103 | `hcl` | `ester` (10.3%) | `pyridine` (3.7%) | `ABSENT` (3.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (87.3%) | `Ni_complex` (5.0%) | `brønsted_acid_cat` (4.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (52.7%) | `polar_aprotic_amide` (45.4%) | `cyclic_ether` (0.8%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CC#N` (94%) | `O` (54%) | `CN(C)C=O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `Cl` (99%) | `O=C([O-])[O-].[K+]` (5%) | `COC(=O)c1ccc2cc(C(` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #581  yield=83.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_5_e202419702.json) (反应 idx 在该 JSON 内 = #20)

```
O=C=O.C=C[C@@H]1O[C@]1(C)c1ccccc1F.C=C[C@@H]1O[C@@]1(C)c1ccccc1F>>CC(/C=C/CC(=O)O)(C(=O)O)c1ccccc1F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `sacrificial_magnesium` (99.3%) | `carbon` (0.4%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `magnesium_plate` | `magnesium_plate` (95.9%) | `magnesium_generic` (3.1%) | `platinum_plate` (0.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `carbon` (84.2%) | `platinum` (13.1%) | `nickel` (2.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_plate` | `graphite_felt` (37.9%) | `graphite_generic` (33.9%) | `carbon_rod` (10.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.8%) | `NEt4` (2.4%) | `Li` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `Cl` (30.3%) | `BF4` (27.7%) | `I` (19.5%) | ✓ |
| 试剂大类 | 103 | `hcl` | `ester` (33.6%) | `ABSENT` (7.6%) | `metal_oxide_oxidant` (1.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `organic_neutral_cat` (0.1%) | `Ni_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (92.4%) | `polar_aprotic_amide` (4.3%) | `polar_aprotic_sulfoxide` (2.4%) | ✓ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CC#N` (100%) | `O` (90%) | `CS(C)=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cl` | `Cl` (90%) | `__ABSENT__` (9%) | `COC(=O)c1ccc2cc(C(` (3%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `COCCOC.[Cl][Ni][Cl` (0%) | `[Br][Ni][Br].c1cc(` (0%) | set ✓ / any ✓ |

---

### Reaction #582  yield=32.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_6_e202418147.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_6_e202418147.json) (反应 idx 在该 JSON 内 = #0)

```
CCCOC(=O)Cl.COc1ccc(I)cc1.C=CCCC1CO1>>COc1ccc(C(=O)C[C@@H]2CC[C@@H](O)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `platinum` (91.1%) | `carbon` (7.9%) | `sacrificial_magnesium` (0.9%) | ✗ |
| 阳极 (细类) | 43 | `zinc_generic` | `platinum_generic` (53.7%) | `platinum_plate` (38.3%) | `magnesium_plate` (4.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (85.8%) | `platinum` (13.7%) | `nickel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_felt` | `carbon_felt` (50.8%) | `platinum_generic` (10.9%) | `graphite_felt` (9.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.8%) | `ABSENT` (15.0%) | `Li` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `Cl` (84.5%) | `ABSENT` (7.3%) | `ClO4` (3.9%) | ✗ |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (6.8%) | `ester` (2.9%) | `o2_oxidant` (2.9%) | ✗ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.8%) | `Ni_complex` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (92.2%) | `halogenated_aliphatic` (3.9%) | `cyclic_ether` (2.1%) | ✓ |
| 溶剂 set | 79 | `C1COCCO1` + `CC(=O)N(C)C` + `O` | `CC#N` (83%) | `O` (56%) | `[H+].[OH-]` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)I` + `Cl` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `[Na+].[OH-]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` + `CC(C)(C)c1ccnc(-c2` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #583  yield=32.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_6_e202418147.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_6_e202418147.json) (反应 idx 在该 JSON 内 = #1)

```
CCCOC(=O)Cl.COc1ccc(I)cc1.C=CCCC1CO1>>COc1ccc(C(=O)C[C@H]2CC[C@@H](O)C2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `platinum` (91.1%) | `carbon` (7.9%) | `sacrificial_magnesium` (0.9%) | ✗ |
| 阳极 (细类) | 43 | `zinc_generic` | `platinum_generic` (53.7%) | `platinum_plate` (38.3%) | `magnesium_plate` (4.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (85.8%) | `platinum` (13.7%) | `nickel` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_felt` | `carbon_felt` (50.8%) | `platinum_generic` (10.9%) | `graphite_felt` (9.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (81.8%) | `ABSENT` (15.0%) | `Li` (2.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `Cl` (84.5%) | `ABSENT` (7.3%) | `ClO4` (3.9%) | ✗ |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (6.8%) | `ester` (2.9%) | `o2_oxidant` (2.9%) | ✗ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.8%) | `Ni_complex` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (92.2%) | `halogenated_aliphatic` (3.9%) | `cyclic_ether` (2.1%) | ✓ |
| 溶剂 set | 79 | `C1COCCO1` + `CC(=O)N(C)C` + `O` | `CC#N` (83%) | `O` (56%) | `[H+].[OH-]` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)I` + `Cl` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `[Na+].[OH-]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` + `CC(C)(C)c1ccnc(-c2` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #584  yield=50.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_7_e202420188.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_7_e202420188.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCCCCCCCCCC>>CCCCCCCCCCCCC1CO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (43.7%) | `carbon` (35.7%) | `ABSENT` (18.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_plate` | `glassy_carbon` (30.3%) | `carbon_generic` (13.3%) | `platinum_generic` (10.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (67.6%) | `stainless_steel` (11.6%) | `carbon` (8.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `unknown_electrode` (66.3%) | `platinum_plate` (11.7%) | `platinum_mesh` (8.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (60.3%) | `ABSENT` (25.5%) | `divided` (14.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (63.5%) | `NBu4` (16.1%) | `Li` (7.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `Br` (57.2%) | `BF4` (18.5%) | `I` (12.9%) | ✓ |
| 试剂大类 | 103 | `water` | `boron_lewis_acid` (28.0%) | `as_solvent_polar_aprotic_sulfo` (11.5%) | `carboxylic_acid` (6.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.2%) | `Mn_complex` (5.3%) | `ionic_organocat` (1.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (42.5%) | `polar_aprotic_nitrile` (28.0%) | `polar_aprotic_sulfoxide` (12.2%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `ClCCl` (84%) | `CCN(CC)CC.F.F.F` (40%) | `O` (16%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O` | `O=O` (93%) | `__OTHER__` (89%) | `OB(O)B(O)O` (86%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl-].[Cl-].[Ni+2]` (70%) | `__ABSENT__` (10%) | `[Cl-].[Cl-].[Mn+2]` (5%) | set ✗ / any ✓ |

---

### Reaction #585  yield=49.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_7_e202420188.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_7_e202420188.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1cccc(Cl)c1>>Clc1cccc(C2CO2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.7%) | `platinum` (3.7%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (93.6%) | `unknown_electrode` (2.9%) | `glassy_carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `stainless_steel` (0.2%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (82.2%) | `platinum_generic` (17.2%) | `platinum_wire` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.7%) | `ABSENT` (1.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (90.5%) | `NBu4` (7.6%) | `K` (1.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (92.8%) | `PF6` (4.7%) | `BF4` (1.3%) | ✓ |
| 试剂大类 | 103 | `water` | `alkali_other_salt` (30.3%) | `alkali_sulfinate` (6.1%) | `bromide_anion` (3.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (99.0%) | `ABSENT` (0.8%) | `Mn_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (84.3%) | `aqueous` (5.7%) | `polar_aprotic_sulfoxide` (5.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `CC#N` (78%) | `O` (53%) | `CC(C)=O` (12%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O` | `O.O.O.O.O.O.O.O.O.` (49%) | `[Cl-].[Li+]` (31%) | `O=C(O)O.[K]` (10%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (99%) | `__OTHER__` (99%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #586  yield=42.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_7_e202420188.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_7_e202420188.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(Cl)cc1>>Clc1ccc(C2CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (76.9%) | `platinum` (15.2%) | `ABSENT` (7.2%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (94.8%) | `glassy_carbon` (3.0%) | `boron_doped_diamond` (0.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.4%) | `stainless_steel` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_foam` | `platinum_plate` (82.5%) | `platinum_generic` (9.2%) | `platinum_wire` (4.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.3%) | `ABSENT` (1.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (72.3%) | `NBu4` (14.2%) | `K` (8.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (79.9%) | `BF4` (8.4%) | `PF6` (6.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `alkali_other_salt` (14.3%) | `alkali_sulfinate` (7.3%) | `carboxylic_acid` (4.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (89.1%) | `ABSENT` (7.2%) | `Mn_complex` (1.7%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (73.8%) | `aqueous` (16.0%) | `polar_aprotic_sulfoxide` (4.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (97%) | `CC#N` (91%) | `CC(C)=O` (4%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `O=O` (80%) | `O` (61%) | `O.O.O.O.O.O.O.O.O.` (46%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #587  yield=56.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_7_e202420188.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_7_e202420188.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1ccccc1Cl>>Clc1ccccc1C1CO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (80.5%) | `platinum` (18.9%) | `ABSENT` (0.5%) | ✓ |
| 阳极 (细类) | 43 | `boron_doped_diamond` | `carbon_generic` (62.3%) | `glassy_carbon` (13.6%) | `platinum_generic` (9.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.5%) | `carbon` (1.1%) | `stainless_steel` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_wire` | `platinum_plate` (57.2%) | `platinum_generic` (37.0%) | `platinum_wire` (1.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (94.9%) | `ABSENT` (5.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (73.6%) | `K` (10.7%) | `H` (5.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `PF6` (39.4%) | `Br` (38.4%) | `ClO4` (7.4%) | ✗ |
| 试剂大类 | 103 | `water` | `alkali_other_salt` (34.0%) | `carboxylic_acid` (6.7%) | `bromide_anion` (5.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (91.1%) | `organic_neutral_cat` (4.1%) | `ABSENT` (4.0%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (77.2%) | `polar_protic_acid` (11.6%) | `halogenated_aliphatic` (3.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC(=O)O` + `OC(C(F)(F)F)C(F)(F` + `ClCCl` | `ClCCl` (80%) | `CC(=O)O` (74%) | `CC#N` (74%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `O=S(=O)(O)C(F)(F)F` + `CC(=O)OC(C)=O` + `CN(C)c1ccncc1` | `O=S(=O)(O)C(F)(F)F` (96%) | `CN(C)c1ccncc1` (93%) | `CC(=O)OC(C)=O` (71%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COc1c(I)cc2c(c1I)-` | `COc1c(I)cc2c(c1I)-` (64%) | `c1ccncc1` (34%) | `__OTHER__` (10%) | set ✓ / any ✓ |

---

### Reaction #588  yield=51.0%

**Source paper**: [`Angew/2025_Angewandte_Chemie_International_Edition_2025_64_7_e202420188.json`](reactions_by_journal_alkene_ec_audited/Angew/2025_Angewandte_Chemie_International_Edition_2025_64_7_e202420188.json) (反应 idx 在该 JSON 内 = #4)

```
C=CCCCCCCCC>>CCCCCCCCC1CO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `platinum` (43.7%) | `carbon` (35.7%) | `ABSENT` (18.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_plate` | `glassy_carbon` (30.3%) | `carbon_generic` (13.3%) | `platinum_generic` (10.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (67.6%) | `stainless_steel` (11.6%) | `carbon` (8.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `unknown_electrode` (66.3%) | `platinum_plate` (11.7%) | `platinum_mesh` (8.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (60.3%) | `ABSENT` (25.5%) | `divided` (14.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (63.5%) | `NBu4` (16.1%) | `Li` (7.7%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Br` (57.2%) | `BF4` (18.5%) | `I` (12.9%) | ✗ |
| 试剂大类 | 103 | `water` | `boron_lewis_acid` (28.0%) | `as_solvent_polar_aprotic_sulfo` (11.5%) | `carboxylic_acid` (6.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.2%) | `Mn_complex` (5.3%) | `ionic_organocat` (1.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `halogenated_aliphatic` (42.5%) | `polar_aprotic_nitrile` (28.0%) | `polar_aprotic_sulfoxide` (12.2%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `ClCCl` (84%) | `CCN(CC)CC.F.F.F` (40%) | `O` (16%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[H+]` + `O=S([O-])([O-])=S.` | `O=O` (93%) | `__OTHER__` (89%) | `OB(O)B(O)O` (86%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=S(=O)(O)C(F)(F)F` | `[Cl-].[Cl-].[Ni+2]` (70%) | `__ABSENT__` (10%) | `[Cl-].[Cl-].[Mn+2]` (5%) | set ✗ / any ✗ |

---

### Reaction #589  yield=32.0%

**Source paper**: [`ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json`](reactions_by_journal_alkene_ec_audited/ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCOc1ccccc1.O>>c1ccc(OCC2CO2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (87.2%) | `platinum` (12.2%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `glassy_carbon` (46.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (8.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.3%) | `stainless_steel` (2.6%) | `nickel` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_wire` (46.3%) | `platinum_generic` (42.6%) | `platinum_plate` (7.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `ABSENT` (1.0%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `K` | `Na` (30.5%) | `Li` (27.6%) | `NBu4` (27.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (37.7%) | `BF4` (30.9%) | `carboxylate` (13.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `as_solvent_halogenated_aliphat` (7.7%) | `ABSENT` (6.8%) | `carboxylic_acid` (4.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.0%) | `Mn_complex` (0.6%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (59.0%) | `polar_protic_alcohol` (33.2%) | `halogenated_aliphatic` (2.7%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` | `CC#N` (86%) | `CC(=O)O` (33%) | `ClCCl` (16%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O` (51%) | `O=O` (41%) | `CS(C)=O` (24%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `c1ccncc1` (4%) | `[O]=[Fe][O][Fe]=[O` (1%) | set ✓ / any ✓ |

---

### Reaction #590  yield=46.0%

**Source paper**: [`ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json`](reactions_by_journal_alkene_ec_audited/ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json) (反应 idx 在该 JSON 内 = #1)

```
C=CCCCCCCCCCCCCCCCC>>CCCCCCCCCCCCCCCCC1CO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (43.7%) | `carbon` (35.7%) | `ABSENT` (18.8%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `glassy_carbon` (30.3%) | `carbon_generic` (13.3%) | `platinum_generic` (10.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (67.6%) | `stainless_steel` (11.6%) | `carbon` (8.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `unknown_electrode` (66.3%) | `platinum_plate` (11.7%) | `platinum_mesh` (8.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (60.3%) | `ABSENT` (25.5%) | `divided` (14.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `Na` (63.5%) | `NBu4` (16.1%) | `Li` (7.7%) | ✗ |
| 电解质 anion | 26 | `BF4` | `Br` (57.2%) | `BF4` (18.5%) | `I` (12.9%) | ✓ |
| 试剂大类 | 103 | `bromide_anion` | `boron_lewis_acid` (28.0%) | `as_solvent_polar_aprotic_sulfo` (11.5%) | `carboxylic_acid` (6.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.2%) | `Mn_complex` (5.3%) | `ionic_organocat` (1.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `halogenated_aliphatic` (42.5%) | `polar_aprotic_nitrile` (28.0%) | `polar_aprotic_sulfoxide` (12.2%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `ClCCl` (84%) | `CCN(CC)CC.F.F.F` (40%) | `O` (16%) | set ✗ / any ✓ |
| 试剂 set | 545 | `[Br-].[K+]` | `O=O` (93%) | `__OTHER__` (89%) | `OB(O)B(O)O` (86%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `[Cl-].[Cl-].[Ni+2]` (70%) | `__ABSENT__` (10%) | `[Cl-].[Cl-].[Mn+2]` (5%) | set ✗ / any ✓ |

---

### Reaction #591  yield=46.0%

**Source paper**: [`ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json`](reactions_by_journal_alkene_ec_audited/ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json) (反应 idx 在该 JSON 内 = #2)

```
CC(=O)O.N.C=Cc1ccccc1>>CCC(O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `sacrificial_zinc` (40.7%) | `ABSENT` (25.5%) | `carbon` (22.5%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `ABSENT` (53.0%) | `graphite_generic` (13.0%) | `reticulated_vitreous_carbon` (8.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `ABSENT` (45.3%) | `platinum` (35.1%) | `carbon` (15.9%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `ABSENT` (42.6%) | `zinc_plate` (26.3%) | `platinum_generic` (8.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (96.1%) | `ABSENT` (3.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NH4` | `Li` (56.0%) | `K` (16.1%) | `NEt4` (12.8%) | ✗ |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (68.9%) | `ClO4` (20.4%) | `carboxylate` (4.9%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (23.5%) | `hydrosilane` (6.5%) | `cyanide` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (89.6%) | `Co_complex` (7.1%) | `Pt_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (60.4%) | `polar_protic_alcohol` (12.9%) | `acyclic_ether` (8.2%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (65%) | `C1COCCO1` (23%) | `CN(C)C=O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `c1ccncc1` (3%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #592  yield=43.0%

**Source paper**: [`ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json`](reactions_by_journal_alkene_ec_audited/ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1ccccc1.CCC(=O)O.N>>CCCC(O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `sacrificial_zinc` (46.9%) | `carbon` (39.2%) | `ABSENT` (11.2%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `zinc_generic` (32.2%) | `ABSENT` (26.6%) | `reticulated_vitreous_carbon` (21.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (75.1%) | `ABSENT` (20.6%) | `nickel` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (70.6%) | `ABSENT` (11.0%) | `platinum_foil` (7.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (89.4%) | `undivided` (10.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NH4` | `Li` (30.0%) | `K` (27.8%) | `Na` (18.3%) | ✗ |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (36.2%) | `carboxylate` (21.0%) | `BF4` (11.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (18.9%) | `cyanide` (5.6%) | `water` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.8%) | `Pt_complex` (0.9%) | `Co_complex` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.2%) | `polar_protic_alcohol` (36.8%) | `cyclic_ether` (9.4%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `C1COCCO1` (54%) | `CC#N` (34%) | `C[N+](=O)[O-]` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (1%) | `O=O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `c1ccncc1` (3%) | `__OTHER__` (1%) | set ✓ / any ✓ |

---

### Reaction #593  yield=49.0%

**Source paper**: [`ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json`](reactions_by_journal_alkene_ec_audited/ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json) (反应 idx 在该 JSON 内 = #4)

```
C=C(C)c1ccccc1>>COC(C)(CCl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (89.8%) | `platinum` (10.0%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (60.0%) | `glassy_carbon` (24.5%) | `reticulated_vitreous_carbon` (6.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.1%) | `carbon` (14.3%) | `copper` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (74.4%) | `platinum_foil` (19.8%) | `carbon_generic` (4.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `NBu4` (44.2%) | `NEt4` (21.5%) | `Li` (17.2%) | ✗ |
| 电解质 anion | 26 | `Cl` | `BF4` (76.1%) | `ClO4` (14.4%) | `Cl` (3.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `polyhalo_radical_transfer` (48.0%) | `carboxylic_acid` (7.6%) | `transition_metal_salt_reagent` (5.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.6%) | `brønsted_acid_cat` (7.1%) | `Mn_complex` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (97.8%) | `polar_aprotic_nitrile` (1.6%) | `polar_aprotic_sulfoxide` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `O` + `CCCCn1cc[n+](C)c1.` | `CCCCn1cc[n+](C)c1.` (98%) | `O` (98%) | `CO` (10%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[SiH](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `CC[SiH](CC)CC` (98%) | `OB(O)B(O)O` (96%) | `O=O` (96%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)(C)c1cc(C=N[C` | `CC(C)(C)c1cc(C=N[C` (99%) | `[Pt]` (1%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #594  yield=64.0%

**Source paper**: [`Reaction/2012_Reaction_Kinetics_Mechanisms_and_Catalysis_2012_106_1_37-47.json`](reactions_by_journal_alkene_ec_audited/Reaction/2012_Reaction_Kinetics_Mechanisms_and_Catalysis_2012_106_1_37-47.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccc1>>CC1(c2ccccc2)CO1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (87.3%) | `platinum` (8.8%) | `sacrificial_magnesium` (1.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `platinum_plate` | `reticulated_vitreous_carbon` (34.8%) | `glassy_carbon` (21.4%) | `carbon_felt` (8.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (65.1%) | `carbon` (30.1%) | `ABSENT` (1.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `reticulated_vitreous_carbon` | `carbon_felt` (56.6%) | `platinum_plate` (15.5%) | `platinum_generic` (7.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `divided` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `K` | `NBu4` (83.8%) | `NEt4` (8.7%) | `Li` (5.2%) | ✗ |
| 电解质 anion | 26 | `Br` | `ClO4` (72.2%) | `BF4` (21.5%) | `PF6` (3.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (16.5%) | `o2_oxidant` (10.3%) | `alkali_sulfinate` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (38.5%) | `Co_complex` (26.5%) | `triarylamine_radical_cat` (18.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (86.2%) | `polar_protic_alcohol` (5.8%) | `polar_aprotic_amide` (2.2%) | ✓ |
| 溶剂 set | 79 | `O` + `CCCCn1cc[n+](C)c1.` | `CCCCn1cc[n+](C)c1.` (87%) | `O` (57%) | `CCO` (36%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[SiH](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (97%) | `__OTHER__` (78%) | `OB(O)B(O)O` (67%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(C)(C)c1cc(C=N[C` | `CC(C)(C)c1cc(C=N[C` (89%) | `c1ccncc1` (12%) | `Brc1ccc(N(c2ccc(Br` (5%) | set ✓ / any ✓ |

---

### Reaction #595  yield=70.0%

**Source paper**: [`ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json`](reactions_by_journal_alkene_ec_audited/ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json) (反应 idx 在该 JSON 内 = #6)

```
C=C(C)c1ccc(F)cc1.CC(=O)O.N>>CCC(C)(O)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `ABSENT` (98.6%) | `carbon` (0.9%) | `sacrificial_zinc` (0.3%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (50.2%) | `ABSENT` (44.5%) | `zinc_plate` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.1%) | `ABSENT` (12.6%) | `carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (82.3%) | `ABSENT` (13.3%) | `platinum_plate` (1.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.2%) | `ABSENT` (1.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `H` | `K` (92.4%) | `Li` (4.5%) | `NBu4` (2.2%) | ✗ |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (45.1%) | `ClO4` (32.4%) | `molecular_no_ion` (10.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.5%) | `hydrosilane` (5.5%) | `acid_anhydride` (3.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (70.4%) | `V_complex` (9.8%) | `Pt_complex` (8.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (89.8%) | `cyclic_ether` (5.4%) | `polar_protic_alcohol` (2.6%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC(C)=O` (52%) | `CC#N` (45%) | `ClCCl` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O.O.O.O.O.O.O.O.O.` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[O]=[Ti]=[O]` (0%) | `CC(=O)NC1CC2(CCCCC` (0%) | set ✓ / any ✓ |

---

### Reaction #596  yield=79.0%

**Source paper**: [`ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json`](reactions_by_journal_alkene_ec_audited/ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json) (反应 idx 在该 JSON 内 = #7)

```
C=C(C)c1ccccc1>>CC(O)(CCl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (81.3%) | `ABSENT` (10.3%) | `platinum` (6.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `reticulated_vitreous_carbon` (67.3%) | `graphite_generic` (10.2%) | `unknown_electrode` (4.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.4%) | `ABSENT` (0.8%) | `stainless_steel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (67.5%) | `platinum_generic` (30.0%) | `platinum_plate` (2.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (91.9%) | `ABSENT` (7.7%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (42.4%) | `Li` (24.7%) | `K` (12.7%) | ✗ |
| 电解质 anion | 26 | `Cl` | `Cl` (31.4%) | `carboxylate` (21.2%) | `ClO4` (14.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (12.1%) | `ABSENT` (5.6%) | `polyhalo_radical_transfer` (3.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (56.3%) | `ABSENT` (35.1%) | `Mn_complex` (6.8%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (77.0%) | `aqueous` (6.2%) | `polar_aprotic_sulfoxide` (5.2%) | ✗ |
| 溶剂 set | 79 | `O` + `CCCCn1cc[n+](C)c1.` | `O` (99%) | `CCCCn1cc[n+](C)c1.` (88%) | `CC#N` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[SiH](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `CC[SiH](CC)CC` (94%) | `O=O` (90%) | `__OTHER__` (53%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `CC(C)(C)c1cc(C=N[C` | `CC(C)(C)c1cc(C=N[C` (93%) | `O=S(=O)(O)C(F)(F)F` (3%) | `__OTHER__` (3%) | set ✓ / any ✓ |

---

### Reaction #597  yield=78.0%

**Source paper**: [`ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json`](reactions_by_journal_alkene_ec_audited/ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json) (反应 idx 在该 JSON 内 = #8)

```
C=C(C)c1ccccc1.CCC(=O)O.N>>CCCC(C)(O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `ABSENT` (71.9%) | `carbon` (19.4%) | `sacrificial_zinc` (4.9%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (29.2%) | `graphite_generic` (27.8%) | `glassy_carbon` (12.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (69.5%) | `ABSENT` (17.0%) | `stainless_steel` (10.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (42.2%) | `platinum_plate` (23.6%) | `stainless_steel_generic` (10.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.8%) | `ABSENT` (1.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NH4` | `K` (62.9%) | `NEt4` (10.2%) | `molecular_no_ion` (9.9%) | ✗ |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (54.5%) | `molecular_no_ion` (28.2%) | `Br` (8.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (16.1%) | `iodide_anion` (9.1%) | `hydrosilane` (4.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `Pt_complex` (0.4%) | `V_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (80.3%) | `polar_protic_alcohol` (9.0%) | `cyclic_ether` (3.9%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `O` (92%) | `CC#N` (63%) | `CC(C)=O` (20%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (97%) | `CC[SiH](CC)CC` (2%) | `CC(=O)O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `CC(C)(C)c1cc(C=N[C` (1%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #598  yield=75.0%

**Source paper**: [`ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json`](reactions_by_journal_alkene_ec_audited/ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json) (反应 idx 在该 JSON 内 = #9)

```
CC(=O)O.N.C=C(C)c1ccc(Cl)cc1>>CCC(C)(O)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `ABSENT` (95.5%) | `carbon` (2.8%) | `platinum` (1.4%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (87.0%) | `ABSENT` (8.3%) | `platinum_generic` (1.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.4%) | `ABSENT` (2.5%) | `carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (92.9%) | `platinum_plate` (4.8%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (98.5%) | `ABSENT` (1.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `K` (95.4%) | `Li` (2.9%) | `NBu4` (1.0%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `carboxylate` (88.5%) | `ClO4` (4.7%) | `molecular_no_ion` (2.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (21.6%) | `acid_anhydride` (3.5%) | `hydrosilane` (3.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `V_complex` (43.7%) | `ABSENT` (37.6%) | `Fe_complex` (7.4%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (97.8%) | `polar_protic_alcohol` (1.2%) | `cyclic_ether` (0.4%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `O` (86%) | `CC(C)=O` (54%) | `CC#N` (46%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (98%) | `O.O.O.O.O.O.O.O.O.` (2%) | `CC(=O)O` (2%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `[O]=[Ti]=[O]` (93%) | `__ABSENT__` (6%) | `CC(=O)NC1CC2(CCCCC` (1%) | set ✗ / any ✓ |

---

### Reaction #599  yield=82.0%

**Source paper**: [`ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json`](reactions_by_journal_alkene_ec_audited/ChemCatChem/2025_ChemCatChem_2025_17_12_e202500069.json) (反应 idx 在该 JSON 内 = #10)

```
C=C(C)c1ccccc1.CC(=O)O.N>>CCC(C)(O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `ABSENT` (51.6%) | `carbon` (37.2%) | `sacrificial_zinc` (7.3%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `ABSENT` (25.0%) | `carbon_rod` (19.3%) | `graphite_generic` (18.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (85.4%) | `ABSENT` (8.6%) | `carbon` (3.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (43.7%) | `platinum_plate` (16.6%) | `unknown_electrode` (12.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `H` | `K` (46.6%) | `Li` (31.9%) | `NBu4` (12.2%) | ✗ |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (60.2%) | `ClO4` (23.9%) | `molecular_no_ion` (9.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.6%) | `hydrosilane` (11.2%) | `cyanide` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.4%) | `Co_complex` (0.9%) | `Pt_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (89.8%) | `cyclic_ether` (4.6%) | `polar_protic_alcohol` (3.1%) | ✗ |
| 溶剂 set | 79 | `CN(C)C=O` + `O` | `CC#N` (76%) | `O` (72%) | `CCCCn1cc[n+](C)c1.` (12%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(=O)O` (2%) | `O=O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CC(C)(C)c1cc(C=N[C` (0%) | `[Pt]` (0%) | set ✓ / any ✓ |

---

### Reaction #600  yield=75.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(C[Si](C)(C)C)c1ccccc1>>C=C(CC1(C(=O)OC)Cc2ccccc2C1=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `sacrificial_iron` (1.2%) | `sacrificial_aluminum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (98.3%) | `unknown_electrode` (0.4%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (99.9%) | `stainless_steel` (0.1%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (98.8%) | `nickel_generic` (1.2%) | `stainless_steel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (51.7%) | `undivided` (45.8%) | `divided` (2.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (90.4%) | `NBu4` (8.4%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (76.2%) | `molecular_no_ion` (8.3%) | `BF4` (8.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `pyridine` (50.3%) | `ABSENT` (3.0%) | `imine` (1.6%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (97.5%) | `amidine_guanidine_organocat` (0.8%) | `Mn_complex` (0.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (94.7%) | `polar_aprotic_amide` (3.5%) | `polar_aprotic_nitrile` (0.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` | `CC(C)=O` (100%) | `O` (42%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)c1cccc(C(C` | `Cc1cccc(C)n1` (89%) | `__OTHER__` (20%) | `c1ccncc1` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `__ABSENT__` (97%) | `COCCOC.[Cl][Ni][Cl` (3%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #601  yield=0.5%

**Source paper**: [`ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(C[Si](C)(C)C)c1ccccc1>>C=C(CC1(C(=O)OC)Cc2ccccc2C1=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `sacrificial_iron` (1.2%) | `sacrificial_aluminum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (98.3%) | `unknown_electrode` (0.4%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (99.9%) | `stainless_steel` (0.1%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (98.8%) | `nickel_generic` (1.2%) | `stainless_steel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (51.7%) | `undivided` (45.8%) | `divided` (2.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (90.4%) | `NBu4` (8.4%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (76.2%) | `molecular_no_ion` (8.3%) | `BF4` (8.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `pyridine` (50.3%) | `ABSENT` (3.0%) | `imine` (1.6%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.5%) | `amidine_guanidine_organocat` (0.8%) | `Mn_complex` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (94.7%) | `polar_aprotic_amide` (3.5%) | `polar_aprotic_nitrile` (0.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` | `CC(C)=O` (100%) | `O` (42%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)c1cccc(C(C` | `Cc1cccc(C)n1` (89%) | `__OTHER__` (20%) | `c1ccncc1` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `__ABSENT__` (97%) | `COCCOC.[Cl][Ni][Cl` (3%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #602  yield=68.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(C[Si](C)(C)C)c1ccccc1>>C=C(CC1(C(=O)OC)Cc2ccccc2C1=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `sacrificial_iron` (1.2%) | `sacrificial_aluminum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (98.3%) | `unknown_electrode` (0.4%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (99.9%) | `stainless_steel` (0.1%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (98.8%) | `nickel_generic` (1.2%) | `stainless_steel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (51.7%) | `undivided` (45.8%) | `divided` (2.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (90.4%) | `NBu4` (8.4%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (76.2%) | `molecular_no_ion` (8.3%) | `BF4` (8.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `pyridine` (50.3%) | `ABSENT` (3.0%) | `imine` (1.6%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (97.5%) | `amidine_guanidine_organocat` (0.8%) | `Mn_complex` (0.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (94.7%) | `polar_aprotic_amide` (3.5%) | `polar_aprotic_nitrile` (0.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` | `CC(C)=O` (100%) | `O` (42%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)c1cccc(C(C` | `Cc1cccc(C)n1` (89%) | `__OTHER__` (20%) | `c1ccncc1` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `__ABSENT__` (97%) | `COCCOC.[Cl][Ni][Cl` (3%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #603  yield=0.5%

**Source paper**: [`ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(C[Si](C)(C)C)c1ccccc1>>C=C(CC1(C(=O)OC)Cc2ccccc2C1=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `sacrificial_iron` (1.2%) | `sacrificial_aluminum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (98.3%) | `unknown_electrode` (0.4%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (99.9%) | `stainless_steel` (0.1%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (98.8%) | `nickel_generic` (1.2%) | `stainless_steel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (51.7%) | `undivided` (45.8%) | `divided` (2.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (90.4%) | `NBu4` (8.4%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (76.2%) | `molecular_no_ion` (8.3%) | `BF4` (8.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `pyridine` (50.3%) | `ABSENT` (3.0%) | `imine` (1.6%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (97.5%) | `amidine_guanidine_organocat` (0.8%) | `Mn_complex` (0.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (94.7%) | `polar_aprotic_amide` (3.5%) | `polar_aprotic_nitrile` (0.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` | `CC(C)=O` (100%) | `O` (42%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)c1cccc(C(C` | `Cc1cccc(C)n1` (89%) | `__OTHER__` (20%) | `c1ccncc1` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `__ABSENT__` (97%) | `COCCOC.[Cl][Ni][Cl` (3%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #604  yield=68.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(C[Si](C)(C)C)c1ccccc1>>C=C(CC1(C(=O)OC)Cc2ccccc2C1=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `sacrificial_iron` (1.2%) | `sacrificial_aluminum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (98.3%) | `unknown_electrode` (0.4%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (99.9%) | `stainless_steel` (0.1%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (98.8%) | `nickel_generic` (1.2%) | `stainless_steel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (51.7%) | `undivided` (45.8%) | `divided` (2.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (90.4%) | `NBu4` (8.4%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (76.2%) | `molecular_no_ion` (8.3%) | `BF4` (8.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `pyridine` (50.3%) | `ABSENT` (3.0%) | `imine` (1.6%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (97.5%) | `amidine_guanidine_organocat` (0.8%) | `Mn_complex` (0.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (94.7%) | `polar_aprotic_amide` (3.5%) | `polar_aprotic_nitrile` (0.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` | `CC(C)=O` (100%) | `O` (42%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)c1cccc(C(C` | `Cc1cccc(C)n1` (89%) | `__OTHER__` (20%) | `c1ccncc1` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `__ABSENT__` (97%) | `COCCOC.[Cl][Ni][Cl` (3%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #605  yield=70.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(C[Si](C)(C)C)c1ccccc1>>C=C(CC1(C(=O)OC)Cc2ccccc2C1=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `sacrificial_iron` (1.2%) | `sacrificial_aluminum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (98.3%) | `unknown_electrode` (0.4%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (99.9%) | `stainless_steel` (0.1%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (98.8%) | `nickel_generic` (1.2%) | `stainless_steel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (51.7%) | `undivided` (45.8%) | `divided` (2.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (90.4%) | `NBu4` (8.4%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (76.2%) | `molecular_no_ion` (8.3%) | `BF4` (8.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `pyridine` (50.3%) | `ABSENT` (3.0%) | `imine` (1.6%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (97.5%) | `amidine_guanidine_organocat` (0.8%) | `Mn_complex` (0.8%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ketone` (94.7%) | `polar_aprotic_amide` (3.5%) | `polar_aprotic_nitrile` (0.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` | `CC(C)=O` (100%) | `O` (42%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)c1cccc(C(C` | `Cc1cccc(C)n1` (89%) | `__OTHER__` (20%) | `c1ccncc1` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `__ABSENT__` (97%) | `COCCOC.[Cl][Ni][Cl` (3%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #606  yield=0.5%

**Source paper**: [`ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(C[Si](C)(C)C)c1ccccc1>>C=C(CC1(C(=O)OC)Cc2ccccc2C1=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (97.8%) | `sacrificial_iron` (1.2%) | `sacrificial_aluminum` (0.3%) | ✗ |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (98.3%) | `unknown_electrode` (0.4%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (99.9%) | `stainless_steel` (0.1%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (98.8%) | `nickel_generic` (1.2%) | `stainless_steel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (51.7%) | `undivided` (45.8%) | `divided` (2.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (90.4%) | `NBu4` (8.4%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (76.2%) | `molecular_no_ion` (8.3%) | `BF4` (8.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `pyridine` (50.3%) | `ABSENT` (3.0%) | `imine` (1.6%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (97.5%) | `amidine_guanidine_organocat` (0.8%) | `Mn_complex` (0.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (94.7%) | `polar_aprotic_amide` (3.5%) | `polar_aprotic_nitrile` (0.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` | `CC(C)=O` (100%) | `O` (42%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)c1cccc(C(C` | `Cc1cccc(C)n1` (89%) | `__OTHER__` (20%) | `c1ccncc1` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `__ABSENT__` (97%) | `COCCOC.[Cl][Ni][Cl` (3%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #607  yield=19.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(C[Si](C)(C)C)c1ccccc1>>C=C(CC1(C(=O)OC)Cc2ccccc2C1=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `sacrificial_iron` (1.2%) | `sacrificial_aluminum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (98.3%) | `unknown_electrode` (0.4%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (99.9%) | `stainless_steel` (0.1%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (98.8%) | `nickel_generic` (1.2%) | `stainless_steel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (51.7%) | `undivided` (45.8%) | `divided` (2.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (90.4%) | `NBu4` (8.4%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ClO4` (76.2%) | `molecular_no_ion` (8.3%) | `BF4` (8.0%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `pyridine` (50.3%) | `ABSENT` (3.0%) | `imine` (1.6%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (97.5%) | `amidine_guanidine_organocat` (0.8%) | `Mn_complex` (0.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (94.7%) | `polar_aprotic_amide` (3.5%) | `polar_aprotic_nitrile` (0.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` | `CC(C)=O` (100%) | `O` (42%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)c1cccc(C(C` | `Cc1cccc(C)n1` (89%) | `__OTHER__` (20%) | `c1ccncc1` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `__ABSENT__` (97%) | `COCCOC.[Cl][Ni][Cl` (3%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #608  yield=74.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(C[Si](C)(C)C)c1ccccc1>>C=C(CC1(C(=O)OC)Cc2ccccc2C1=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `sacrificial_iron` (1.2%) | `sacrificial_aluminum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (98.3%) | `unknown_electrode` (0.4%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (99.9%) | `stainless_steel` (0.1%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (98.8%) | `nickel_generic` (1.2%) | `stainless_steel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (51.7%) | `undivided` (45.8%) | `divided` (2.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (90.4%) | `NBu4` (8.4%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (76.2%) | `molecular_no_ion` (8.3%) | `BF4` (8.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `pyridine` (50.3%) | `ABSENT` (3.0%) | `imine` (1.6%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (97.5%) | `amidine_guanidine_organocat` (0.8%) | `Mn_complex` (0.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (94.7%) | `polar_aprotic_amide` (3.5%) | `polar_aprotic_nitrile` (0.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` | `CC(C)=O` (100%) | `O` (42%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)c1cccc(C(C` | `Cc1cccc(C)n1` (89%) | `__OTHER__` (20%) | `c1ccncc1` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `__ABSENT__` (97%) | `COCCOC.[Cl][Ni][Cl` (3%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #609  yield=34.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(C[Si](C)(C)C)c1ccccc1>>C=C(CC1(C(=O)OC)Cc2ccccc2C1=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (97.8%) | `sacrificial_iron` (1.2%) | `sacrificial_aluminum` (0.3%) | ✗ |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (98.3%) | `unknown_electrode` (0.4%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `nickel` (99.9%) | `stainless_steel` (0.1%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (98.8%) | `nickel_generic` (1.2%) | `stainless_steel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (51.7%) | `undivided` (45.8%) | `divided` (2.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (90.4%) | `NBu4` (8.4%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (76.2%) | `molecular_no_ion` (8.3%) | `BF4` (8.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `pyridine` (50.3%) | `ABSENT` (3.0%) | `imine` (1.6%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (97.5%) | `amidine_guanidine_organocat` (0.8%) | `Mn_complex` (0.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (94.7%) | `polar_aprotic_amide` (3.5%) | `polar_aprotic_nitrile` (0.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` | `CC(C)=O` (100%) | `O` (42%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)c1cccc(C(C` | `Cc1cccc(C)n1` (89%) | `__OTHER__` (20%) | `c1ccncc1` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `__ABSENT__` (97%) | `COCCOC.[Cl][Ni][Cl` (3%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #610  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(C[Si](C)(C)C)c1ccccc1>>C=C(CC1(C(=O)OC)Cc2ccccc2C1=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `sacrificial_iron` (1.2%) | `sacrificial_aluminum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (98.3%) | `unknown_electrode` (0.4%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (99.9%) | `stainless_steel` (0.1%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (98.8%) | `nickel_generic` (1.2%) | `stainless_steel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (51.7%) | `undivided` (45.8%) | `divided` (2.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (90.4%) | `NBu4` (8.4%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (76.2%) | `molecular_no_ion` (8.3%) | `BF4` (8.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `pyridine` (50.3%) | `ABSENT` (3.0%) | `imine` (1.6%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (97.5%) | `amidine_guanidine_organocat` (0.8%) | `Mn_complex` (0.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (94.7%) | `polar_aprotic_amide` (3.5%) | `polar_aprotic_nitrile` (0.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` | `CC(C)=O` (100%) | `O` (42%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)c1cccc(C(C` | `Cc1cccc(C)n1` (89%) | `__OTHER__` (20%) | `c1ccncc1` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `__ABSENT__` (97%) | `COCCOC.[Cl][Ni][Cl` (3%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #611  yield=65.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(C[Si](C)(C)C)c1ccccc1>>C=C(CC1(C(=O)OC)Cc2ccccc2C1=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `sacrificial_iron` (1.2%) | `sacrificial_aluminum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (98.3%) | `unknown_electrode` (0.4%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (99.9%) | `stainless_steel` (0.1%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (98.8%) | `nickel_generic` (1.2%) | `stainless_steel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (51.7%) | `undivided` (45.8%) | `divided` (2.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (90.4%) | `NBu4` (8.4%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (76.2%) | `molecular_no_ion` (8.3%) | `BF4` (8.0%) | ✓ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (50.3%) | `ABSENT` (3.0%) | `imine` (1.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (97.5%) | `amidine_guanidine_organocat` (0.8%) | `Mn_complex` (0.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (94.7%) | `polar_aprotic_amide` (3.5%) | `polar_aprotic_nitrile` (0.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` | `CC(C)=O` (100%) | `O` (42%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)c1cccc(C(C` | `Cc1cccc(C)n1` (89%) | `__OTHER__` (20%) | `c1ccncc1` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `__ABSENT__` (97%) | `COCCOC.[Cl][Ni][Cl` (3%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #612  yield=54.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03082J_sup_1_p3_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(C[Si](C)(C)C)c1ccccc1>>C=C(CC1(C(=O)OC)Cc2ccccc2C1=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.8%) | `sacrificial_iron` (1.2%) | `sacrificial_aluminum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (98.3%) | `unknown_electrode` (0.4%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (99.9%) | `stainless_steel` (0.1%) | `sacrificial_zinc` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (98.8%) | `nickel_generic` (1.2%) | `stainless_steel_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `ABSENT` (51.7%) | `undivided` (45.8%) | `divided` (2.5%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (90.4%) | `NBu4` (8.4%) | `ABSENT` (0.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (76.2%) | `molecular_no_ion` (8.3%) | `BF4` (8.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `pyridine` (50.3%) | `ABSENT` (3.0%) | `imine` (1.6%) | ✓ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (97.5%) | `amidine_guanidine_organocat` (0.8%) | `Mn_complex` (0.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (94.7%) | `polar_aprotic_amide` (3.5%) | `polar_aprotic_nitrile` (0.9%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `ClCCl` | `CC(C)=O` (100%) | `O` (42%) | `CN(C)C=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)c1cccc(C(C` | `Cc1cccc(C)n1` (89%) | `__OTHER__` (20%) | `c1ccncc1` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `__ABSENT__` (97%) | `COCCOC.[Cl][Ni][Cl` (3%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✗ / any ✓ |

---

### Reaction #613  yield=71.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✓ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #614  yield=18.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `cyclic_ether` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✓ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #615  yield=75.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #616  yield=0.5%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #617  yield=43.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `PF6` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #618  yield=79.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #619  yield=75.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `brønsted_acid_cat` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #620  yield=20.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ClO4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #621  yield=20.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #622  yield=54.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #623  yield=70.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #624  yield=78.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #625  yield=65.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #626  yield=18.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✗ |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #627  yield=65.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #628  yield=76.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #629  yield=57.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #630  yield=38.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #631  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc03082j_si2_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C1Cc2ccccc2C1=O.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(C=C(c2ccccc2)c2ccccc2)Cc2ccccc2C1=O.O=C1OC(c2ccccc2)(c2ccccc2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (68.9%) | `ABSENT` (28.1%) | `platinum` (1.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (63.0%) | `graphite_generic` (36.1%) | `carbon_felt` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (92.2%) | `sacrificial_zinc` (6.8%) | `carbon` (0.4%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (83.8%) | `nickel_generic` (15.9%) | `platinum_generic` (0.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.9%) | `K` (0.0%) | `NBu4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (96.5%) | `molecular_no_ion` (3.2%) | `I` (0.1%) | ✗ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (90.1%) | `ABSENT` (0.7%) | `hydrosilane` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.4%) | `Ni_complex` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (99.3%) | `halogenated_aliphatic` (0.2%) | `cyclic_ether` (0.1%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `O` (94%) | `__OTHER__` (72%) | set ✗ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `Cc1cccc(C)n1` (100%) | `CCOCC.FB(F)F` (88%) | `__OTHER__` (83%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (79%) | `__ABSENT__` (18%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #632  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #633  yield=10.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #634  yield=47.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #635  yield=41.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #636  yield=0.5%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #637  yield=36.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #638  yield=8.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #639  yield=28.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silane_other` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #640  yield=78.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #641  yield=65.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #642  yield=52.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #643  yield=56.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #644  yield=0.5%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #645  yield=44.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #646  yield=0.5%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `cyclic_ether` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #647  yield=0.5%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #648  yield=50.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #649  yield=53.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #650  yield=57.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03812J_sup_1_p4_t1.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C(=O)N(C)c1ccccc1)C(F)(F)F.OCCBr>>CN1C(=O)C(CCO)(C(F)(F)F)c2ccccc21
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `ABSENT` (2.8%) | `platinum` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (91.0%) | `ABSENT` (3.2%) | `carbon_rod` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (3.7%) | `carbon` (1.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.5%) | `platinum_plate` (13.0%) | `ABSENT` (4.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (96.0%) | `Li` (3.3%) | `K` (0.4%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (63.4%) | `BF4` (30.9%) | `carboxylate` (4.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (18.0%) | `alkali_phosphate` (2.9%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `quinone_oxidant_cat` | `quinone_oxidant_cat` (53.1%) | `ferrocene_mediator` (26.1%) | `ABSENT` (17.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (82.3%) | `cyclic_ether` (8.8%) | `polar_protic_alcohol` (7.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `C1CCOC1` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1c2ccccc2C(=O)c` | `O=C1c2ccccc2C(=O)c` (64%) | `[Fe+2].c1cc[cH-]c1` (16%) | `__ABSENT__` (10%) | set ✓ / any ✓ |

---

### Reaction #651  yield=0.5%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #652  yield=85.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #653  yield=20.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #654  yield=66.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #655  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `stainless_steel` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✗ |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #656  yield=48.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #657  yield=75.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #658  yield=56.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #659  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #660  yield=28.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #661  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `alkali_carbonate` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #662  yield=45.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #663  yield=60.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #664  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #665  yield=72.0%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #666  yield=58.5%

**Source paper**: [`ChemCommun/10.1039_D5CC03899E_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC03899E_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.O=[PH](c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✗ |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #667  yield=43.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1.ClCC(Br)c1ccccc1.ClCC(Cl)c1ccccc1.BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.3%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.9%) | `reticulated_vitreous_carbon` (3.7%) | `glassy_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.7%) | `carbon` (18.4%) | `nickel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (99.6%) | `platinum_generic` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (75.3%) | `ABSENT` (24.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (53.7%) | `Li` (18.6%) | `NEt4` (17.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (63.2%) | `BF4` (16.8%) | `Br` (10.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `hbr` (36.3%) | `polyhalo_radical_transfer` (14.1%) | `carboxylic_acid` (3.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.0%) | `brønsted_acid_cat` (10.9%) | `Mn_complex` (8.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (52.6%) | `aqueous` (37.8%) | `polar_protic_acid` (5.4%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (99%) | `C[N+](=O)[O-]` (98%) | `O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✓ / any ✓ |

---

### Reaction #668  yield=42.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1.ClCC(Br)c1ccccc1.ClCC(Cl)c1ccccc1.BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.3%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.9%) | `reticulated_vitreous_carbon` (3.7%) | `glassy_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.7%) | `carbon` (18.4%) | `nickel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (99.6%) | `platinum_generic` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (75.3%) | `ABSENT` (24.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (53.7%) | `Li` (18.6%) | `NEt4` (17.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (63.2%) | `BF4` (16.8%) | `Br` (10.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `hbr` (36.3%) | `polyhalo_radical_transfer` (14.1%) | `carboxylic_acid` (3.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.0%) | `brønsted_acid_cat` (10.9%) | `Mn_complex` (8.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (52.6%) | `aqueous` (37.8%) | `polar_protic_acid` (5.4%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (99%) | `C[N+](=O)[O-]` (98%) | `O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✓ / any ✓ |

---

### Reaction #669  yield=75.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1.ClCC(Br)c1ccccc1.ClCC(Cl)c1ccccc1.BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.3%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.9%) | `reticulated_vitreous_carbon` (3.7%) | `glassy_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.7%) | `carbon` (18.4%) | `nickel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (99.6%) | `platinum_generic` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (75.3%) | `ABSENT` (24.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (53.7%) | `Li` (18.6%) | `NEt4` (17.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (63.2%) | `BF4` (16.8%) | `Br` (10.7%) | ✓ |
| 试剂大类 | 103 | `alkene_coreagent` | `hbr` (36.3%) | `polyhalo_radical_transfer` (14.1%) | `carboxylic_acid` (3.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.0%) | `brønsted_acid_cat` (10.9%) | `Mn_complex` (8.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (52.6%) | `aqueous` (37.8%) | `polar_protic_acid` (5.4%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (99%) | `C[N+](=O)[O-]` (98%) | `O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✓ / any ✓ |

---

### Reaction #670  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1.ClCC(Br)c1ccccc1.ClCC(Cl)c1ccccc1.BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.3%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.9%) | `reticulated_vitreous_carbon` (3.7%) | `glassy_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.7%) | `carbon` (18.4%) | `nickel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (99.6%) | `platinum_generic` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (75.3%) | `ABSENT` (24.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (53.7%) | `Li` (18.6%) | `NEt4` (17.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (63.2%) | `BF4` (16.8%) | `Br` (10.7%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `hbr` (36.3%) | `polyhalo_radical_transfer` (14.1%) | `carboxylic_acid` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.0%) | `brønsted_acid_cat` (10.9%) | `Mn_complex` (8.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (52.6%) | `aqueous` (37.8%) | `polar_protic_acid` (5.4%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (99%) | `C[N+](=O)[O-]` (98%) | `O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✓ / any ✓ |

---

### Reaction #671  yield=29.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1.ClCC(Br)c1ccccc1.ClCC(Cl)c1ccccc1.BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.3%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.9%) | `reticulated_vitreous_carbon` (3.7%) | `glassy_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.7%) | `carbon` (18.4%) | `nickel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (99.6%) | `platinum_generic` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (75.3%) | `ABSENT` (24.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (53.7%) | `Li` (18.6%) | `NEt4` (17.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (63.2%) | `BF4` (16.8%) | `Br` (10.7%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `hbr` (36.3%) | `polyhalo_radical_transfer` (14.1%) | `carboxylic_acid` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.0%) | `brønsted_acid_cat` (10.9%) | `Mn_complex` (8.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (52.6%) | `aqueous` (37.8%) | `polar_protic_acid` (5.4%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (99%) | `C[N+](=O)[O-]` (98%) | `O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✓ / any ✓ |

---

### Reaction #672  yield=2.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1.ClCC(Br)c1ccccc1.ClCC(Cl)c1ccccc1.BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.3%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.9%) | `reticulated_vitreous_carbon` (3.7%) | `glassy_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.7%) | `carbon` (18.4%) | `nickel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (99.6%) | `platinum_generic` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (75.3%) | `ABSENT` (24.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (53.7%) | `Li` (18.6%) | `NEt4` (17.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (63.2%) | `BF4` (16.8%) | `Br` (10.7%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `hbr` (36.3%) | `polyhalo_radical_transfer` (14.1%) | `carboxylic_acid` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.0%) | `brønsted_acid_cat` (10.9%) | `Mn_complex` (8.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (52.6%) | `aqueous` (37.8%) | `polar_protic_acid` (5.4%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (99%) | `C[N+](=O)[O-]` (98%) | `O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✓ / any ✓ |

---

### Reaction #673  yield=59.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1.ClCC(Br)c1ccccc1.ClCC(Cl)c1ccccc1.BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.3%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.9%) | `reticulated_vitreous_carbon` (3.7%) | `glassy_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.7%) | `carbon` (18.4%) | `nickel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (99.6%) | `platinum_generic` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (75.3%) | `ABSENT` (24.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (53.7%) | `Li` (18.6%) | `NEt4` (17.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (63.2%) | `BF4` (16.8%) | `Br` (10.7%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `hbr` (36.3%) | `polyhalo_radical_transfer` (14.1%) | `carboxylic_acid` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.0%) | `brønsted_acid_cat` (10.9%) | `Mn_complex` (8.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (52.6%) | `aqueous` (37.8%) | `polar_protic_acid` (5.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (99%) | `C[N+](=O)[O-]` (98%) | `O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✓ / any ✓ |

---

### Reaction #674  yield=30.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1.ClCC(Br)c1ccccc1.ClCC(Cl)c1ccccc1.BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.3%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.9%) | `reticulated_vitreous_carbon` (3.7%) | `glassy_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.7%) | `carbon` (18.4%) | `nickel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (99.6%) | `platinum_generic` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (75.3%) | `ABSENT` (24.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (53.7%) | `Li` (18.6%) | `NEt4` (17.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (63.2%) | `BF4` (16.8%) | `Br` (10.7%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `hbr` (36.3%) | `polyhalo_radical_transfer` (14.1%) | `carboxylic_acid` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.0%) | `brønsted_acid_cat` (10.9%) | `Mn_complex` (8.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (52.6%) | `aqueous` (37.8%) | `polar_protic_acid` (5.4%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (99%) | `C[N+](=O)[O-]` (98%) | `O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✓ / any ✓ |

---

### Reaction #675  yield=70.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1.ClCC(Br)c1ccccc1.ClCC(Cl)c1ccccc1.BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.3%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.9%) | `reticulated_vitreous_carbon` (3.7%) | `glassy_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.7%) | `carbon` (18.4%) | `nickel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (99.6%) | `platinum_generic` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (75.3%) | `ABSENT` (24.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (53.7%) | `Li` (18.6%) | `NEt4` (17.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (63.2%) | `BF4` (16.8%) | `Br` (10.7%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `hbr` (36.3%) | `polyhalo_radical_transfer` (14.1%) | `carboxylic_acid` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.0%) | `brønsted_acid_cat` (10.9%) | `Mn_complex` (8.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (52.6%) | `aqueous` (37.8%) | `polar_protic_acid` (5.4%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (99%) | `C[N+](=O)[O-]` (98%) | `O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✓ / any ✓ |

---

### Reaction #676  yield=24.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1.ClCC(Br)c1ccccc1.ClCC(Cl)c1ccccc1.BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.3%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.9%) | `reticulated_vitreous_carbon` (3.7%) | `glassy_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.7%) | `carbon` (18.4%) | `nickel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (99.6%) | `platinum_generic` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (75.3%) | `ABSENT` (24.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (53.7%) | `Li` (18.6%) | `NEt4` (17.6%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (63.2%) | `BF4` (16.8%) | `Br` (10.7%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `hbr` (36.3%) | `polyhalo_radical_transfer` (14.1%) | `carboxylic_acid` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.0%) | `brønsted_acid_cat` (10.9%) | `Mn_complex` (8.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (52.6%) | `aqueous` (37.8%) | `polar_protic_acid` (5.4%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (99%) | `C[N+](=O)[O-]` (98%) | `O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✓ / any ✓ |

---

### Reaction #677  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1.ClCC(Br)c1ccccc1.ClCC(Cl)c1ccccc1.BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (95.3%) | `platinum` (3.3%) | `nickel` (0.5%) | ✗ |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.9%) | `reticulated_vitreous_carbon` (3.7%) | `glassy_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (73.7%) | `carbon` (18.4%) | `nickel` (2.2%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (99.6%) | `platinum_generic` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (75.3%) | `ABSENT` (24.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (53.7%) | `Li` (18.6%) | `NEt4` (17.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (63.2%) | `BF4` (16.8%) | `Br` (10.7%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `hbr` (36.3%) | `polyhalo_radical_transfer` (14.1%) | `carboxylic_acid` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.0%) | `brønsted_acid_cat` (10.9%) | `Mn_complex` (8.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (52.6%) | `aqueous` (37.8%) | `polar_protic_acid` (5.4%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (99%) | `C[N+](=O)[O-]` (98%) | `O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✓ / any ✓ |

---

### Reaction #678  yield=19.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1.ClCC(Br)c1ccccc1.ClCC(Cl)c1ccccc1.BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.3%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.9%) | `reticulated_vitreous_carbon` (3.7%) | `glassy_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.7%) | `carbon` (18.4%) | `nickel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (99.6%) | `platinum_generic` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (75.3%) | `ABSENT` (24.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (53.7%) | `Li` (18.6%) | `NEt4` (17.6%) | ✗ |
| 电解质 anion | 26 | `PF6` | `ABSENT` (63.2%) | `BF4` (16.8%) | `Br` (10.7%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `hbr` (36.3%) | `polyhalo_radical_transfer` (14.1%) | `carboxylic_acid` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.0%) | `brønsted_acid_cat` (10.9%) | `Mn_complex` (8.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (52.6%) | `aqueous` (37.8%) | `polar_protic_acid` (5.4%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (99%) | `C[N+](=O)[O-]` (98%) | `O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✓ / any ✓ |

---

### Reaction #679  yield=35.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t0.json) (反应 idx 在该 JSON 内 = #12)

```
C=Cc1ccccc1>>ClCC(Br)c1ccccc1.ClCC(Br)c1ccccc1.ClCC(Cl)c1ccccc1.BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.3%) | `platinum` (4.3%) | `sacrificial_magnesium` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (90.0%) | `reticulated_vitreous_carbon` (8.0%) | `glassy_carbon` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `lead` | `platinum` (82.7%) | `carbon` (12.5%) | `nickel` (1.3%) | ✗ |
| 阴极 (细类) | 49 | `lead_generic` | `platinum_foil` (99.8%) | `platinum_generic` (0.1%) | `graphite_generic` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (93.1%) | `ABSENT` (6.8%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (55.6%) | `Li` (21.1%) | `NEt4` (13.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (67.9%) | `BF4` (11.4%) | `Br` (10.0%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `hbr` (44.6%) | `polyhalo_radical_transfer` (9.6%) | `carboxylic_acid` (4.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.2%) | `Mn_complex` (10.8%) | `brønsted_acid_cat` (8.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (49.3%) | `aqueous` (44.2%) | `polar_protic_acid` (4.1%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (99%) | `C[N+](=O)[O-]` (99%) | `CN(C)C=O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (100%) | `O=O` (96%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✓ / any ✓ |

---

### Reaction #680  yield=62.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1.ClCC(Br)c1ccccc1.ClCC(Cl)c1ccccc1.BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.3%) | `platinum` (3.3%) | `nickel` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.9%) | `reticulated_vitreous_carbon` (3.7%) | `glassy_carbon` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (73.7%) | `carbon` (18.4%) | `nickel` (2.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (99.6%) | `platinum_generic` (0.2%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (75.3%) | `ABSENT` (24.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (53.7%) | `Li` (18.6%) | `NEt4` (17.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (63.2%) | `BF4` (16.8%) | `Br` (10.7%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `hbr` (36.3%) | `polyhalo_radical_transfer` (14.1%) | `carboxylic_acid` (3.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.0%) | `brønsted_acid_cat` (10.9%) | `Mn_complex` (8.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (52.6%) | `aqueous` (37.8%) | `polar_protic_acid` (5.4%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (99%) | `C[N+](=O)[O-]` (98%) | `O` (8%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `CC[Si](CC)CC` (100%) | `OB(O)B(O)O` (100%) | `O=O` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (100%) | `__OTHER__` (99%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✓ / any ✓ |

---

### Reaction #681  yield=85.0%

**Source paper**: [`China/China_CN119061410_A_2024-12-03.json`](reactions_by_journal_alkene_ec_audited/China/China_CN119061410_A_2024-12-03.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `platinum` (1.5%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (54.4%) | `glassy_carbon` (29.8%) | `reticulated_vitreous_carbon` (8.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.0%) | `carbon` (12.5%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (76.1%) | `platinum_plate` (9.5%) | `platinum_generic` (8.8%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (53.8%) | `ABSENT` (46.0%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NEt4` (25.3%) | `NBu4` (18.6%) | `ABSENT` (14.7%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (78.5%) | `BF4` (9.6%) | `ABSENT` (4.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (60.8%) | `carboxylic_acid` (15.3%) | `inorganic_simple` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.1%) | `Mn_complex` (2.0%) | `brønsted_acid_cat` (1.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (55.1%) | `ABSENT` (17.5%) | `polar_protic_acid` (12.3%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (74%) | `O` (62%) | `C[N+](=O)[O-]` (53%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (100%) | `O=O` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (99%) | `__OTHER__` (96%) | `O=S(=O)([O-])C(F)(` (3%) | set ✓ / any ✓ |

---

### Reaction #682  yield=86.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t1.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(C)cc1>>ClC(CBr)c1ccc(C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.0%) | `platinum` (2.8%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `glassy_carbon` (59.5%) | `graphite_generic` (18.4%) | `reticulated_vitreous_carbon` (8.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.7%) | `carbon` (9.4%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (39.0%) | `platinum_plate` (33.0%) | `platinum_generic` (17.4%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (70.4%) | `ABSENT` (25.9%) | `divided` (3.7%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `H` (41.3%) | `NEt4` (25.0%) | `NBu4` (13.9%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (76.7%) | `BF4` (18.5%) | `molecular_no_ion` (1.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (51.8%) | `carboxylic_acid` (15.7%) | `inorganic_simple` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.8%) | `brønsted_acid_cat` (4.1%) | `Mn_complex` (1.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (50.5%) | `halogenated_aliphatic` (16.2%) | `polar_aprotic_nitrile` (14.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (94%) | `CC#N` (59%) | `FC(F)(F)c1ccccc1` (15%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[SiH](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (99%) | `__OTHER__` (98%) | `O=O` (95%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Pt]` | `[Pt]` (29%) | `[Cl-].[Cl-].[Mn+2]` (26%) | `O=S(=O)([O-])C(F)(` (23%) | set ✓ / any ✓ |

---

### Reaction #683  yield=74.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t1.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(OC(C)=O)cc1>>ClC(CBr)c1ccc(OC(C)=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.7%) | `glassy_carbon` (2.9%) | `carbon_rod` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.5%) | `carbon` (11.9%) | `stainless_steel` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `graphite_generic` (41.4%) | `platinum_plate` (36.9%) | `platinum_foil` (11.1%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (29.7%) | `NEt4` (22.1%) | `H` (20.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (89.1%) | `BF4` (8.0%) | `molecular_no_ion` (2.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (78.0%) | `carboxylic_acid` (4.1%) | `n_halo_imide` (1.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `Mn_complex` (0.8%) | `brønsted_acid_cat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (31.8%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (22.5%) | ✓ |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `FC(F)(F)c1ccccc1` (96%) | `CCOCC` (95%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (98%) | `__OTHER__` (97%) | `CC[Si](CC)CC` (85%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (38%) | `[Cl][Mn][Cl]` (29%) | `[Cl-].[Cl-].[Mn+2]` (23%) | set ✓ / any ✓ |

---

### Reaction #684  yield=68.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t1.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1ccc(OC(=O)OC(C)(C)C)cc1>>ClC(CBr)c1ccc(OC(=O)OC(C)(C)C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (89.2%) | `glassy_carbon` (6.3%) | `carbon_rod` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (52.2%) | `carbon` (36.5%) | `nickel` (5.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `graphite_generic` (57.4%) | `platinum_foil` (14.2%) | `platinum_generic` (7.8%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (95.9%) | `ABSENT` (4.0%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NEt4` (37.2%) | `NBu4` (32.8%) | `Li` (8.8%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (88.1%) | `BF4` (10.4%) | `molecular_no_ion` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (74.5%) | `n_halo_imide` (3.3%) | `carboxylic_acid` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.8%) | `Mn_complex` (1.0%) | `brønsted_acid_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (77.2%) | `polar_aprotic_nitrile` (11.5%) | `polar_protic_acid` (4.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `FC(F)(F)c1ccccc1` (45%) | `CCOCC` (40%) | `O` (26%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `OB(O)B(O)O` (79%) | `CC[Si](CC)CC` (76%) | `__OTHER__` (64%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (55%) | `[Cl][Mn][Cl]` (28%) | `[Cl-].[Cl-].[Mn+2]` (7%) | set ✓ / any ✓ |

---

### Reaction #685  yield=72.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t1.json) (反应 idx 在该 JSON 内 = #4)

```
C=Cc1ccc(C(=O)OC)cc1>>ClC(CBr)c1ccc(C(=O)OC)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.3%) | `platinum` (2.6%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (93.0%) | `glassy_carbon` (5.3%) | `reticulated_vitreous_carbon` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.5%) | `carbon` (16.1%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `graphite_generic` (52.0%) | `platinum_foil` (20.0%) | `platinum_generic` (17.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (85.1%) | `ABSENT` (14.7%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (66.1%) | `NEt4` (10.0%) | `H` (7.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (91.2%) | `BF4` (7.0%) | `molecular_no_ion` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (51.4%) | `carboxylic_acid` (10.9%) | `inorganic_simple` (4.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.8%) | `brønsted_acid_cat` (3.1%) | `Mn_complex` (1.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (54.4%) | `polar_aprotic_nitrile` (18.7%) | `halogenated_aliphatic` (15.3%) | ✓ |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `CCOCC` (94%) | `FC(F)(F)c1ccccc1` (85%) | `O` (15%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | `__OTHER__` (97%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (64%) | `__OTHER__` (46%) | `O=S(=O)([O-])C(F)(` (19%) | set ✓ / any ✓ |

---

### Reaction #686  yield=75.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #14)

```
C=Cc1ccc(-c2ccccc2)cc1>>ClC(CBr)c1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.1%) | `platinum` (1.4%) | `sacrificial_iron` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `glassy_carbon` (71.1%) | `graphite_generic` (22.3%) | `reticulated_vitreous_carbon` (2.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.4%) | `carbon` (5.4%) | `stainless_steel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (54.1%) | `platinum_plate` (27.8%) | `platinum_generic` (15.9%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (92.0%) | `ABSENT` (7.4%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (40.1%) | `H` (36.4%) | `NEt4` (12.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (88.4%) | `BF4` (9.4%) | `molecular_no_ion` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (36.1%) | `carboxylic_acid` (10.6%) | `as_solvent_halogenated_aliphat` (6.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (75.7%) | `brønsted_acid_cat` (14.6%) | `Mn_complex` (7.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_acid` (80.8%) | `ABSENT` (6.7%) | `halogenated_aliphatic` (6.5%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `CC(=O)O` (98%) | `O=CO` (97%) | `O` (91%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (100%) | `__OTHER__` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (99%) | `[Cl-].[Cl-].[Mn+2]` (6%) | `O.O.[K+].[K+].[O]=` (5%) | set ✓ / any ✓ |

---

### Reaction #687  yield=65.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t1.json) (反应 idx 在该 JSON 内 = #6)

```
C=Cc1ccc(F)cc1>>ClC(CBr)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.0%) | `platinum` (1.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (46.4%) | `glassy_carbon` (39.7%) | `reticulated_vitreous_carbon` (6.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.6%) | `carbon` (14.4%) | `stainless_steel` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (44.3%) | `graphite_generic` (36.4%) | `platinum_foil` (12.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `ABSENT` (56.3%) | `undivided` (42.8%) | `divided` (0.9%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `H` (33.7%) | `NEt4` (29.3%) | `NBu4` (27.4%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (80.6%) | `BF4` (17.2%) | `ClO4` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (78.9%) | `carboxylic_acid` (5.0%) | `transition_metal_salt_reagent` (1.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.1%) | `brønsted_acid_cat` (4.0%) | `Mn_complex` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (82.9%) | `polar_aprotic_nitrile` (7.8%) | `halogenated_aliphatic` (4.7%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `CC#N` (75%) | `O` (69%) | `CCOCC` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `__OTHER__` (100%) | `CC[Si](CC)CC` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Cl-].[Cl-].[Mn+2]` | `[Cl-].[Cl-].[Mn+2]` (96%) | `c1ccncc1` (3%) | `O=S(=O)([O-])C(F)(` (2%) | set ✓ / any ✓ |

---

### Reaction #688  yield=78.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #15)

```
C=Cc1ccc(Br)cc1>>ClC(CBr)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.1%) | `platinum` (3.7%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (38.7%) | `reticulated_vitreous_carbon` (23.4%) | `platinum_wire` (15.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.7%) | `carbon` (6.6%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (45.5%) | `platinum_wire` (23.8%) | `platinum_generic` (21.6%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (85.3%) | `ABSENT` (13.6%) | `divided` (1.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (52.1%) | `Li` (21.7%) | `NEt4` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (57.5%) | `BF4` (27.8%) | `ClO4` (5.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (27.1%) | `carboxylic_acid` (22.4%) | `n_halo_imide` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (84.9%) | `brønsted_acid_cat` (8.3%) | `Mn_complex` (4.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (36.0%) | `polar_protic_acid` (32.4%) | `halogenated_aliphatic` (15.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (64%) | `CC#N` (51%) | `CC(=O)O` (20%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | `__OTHER__` (98%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Pt]` | `O=S(=O)([O-])C(F)(` (20%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #689  yield=93.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t1.json) (反应 idx 在该 JSON 内 = #8)

```
C=Cc1ccc(Cl)cc1>>ClC(CBr)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `glassy_carbon` (72.9%) | `graphite_generic` (12.6%) | `reticulated_vitreous_carbon` (11.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.9%) | `carbon` (8.6%) | `stainless_steel` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (56.7%) | `platinum_foil` (29.8%) | `platinum_generic` (6.3%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (53.0%) | `ABSENT` (46.6%) | `divided` (0.4%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.2%) | `ABSENT` (25.5%) | `Na` (12.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (75.3%) | `BF4` (16.7%) | `ABSENT` (5.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (55.6%) | `carboxylic_acid` (11.3%) | `inorganic_simple` (3.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.1%) | `Mn_complex` (5.4%) | `brønsted_acid_cat` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (33.0%) | `ABSENT` (19.6%) | `polar_aprotic_sulfoxide` (15.4%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (96%) | `CC#N` (93%) | `FC(F)(F)c1ccccc1` (6%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | `O=O` (92%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (96%) | `__OTHER__` (86%) | `[Cl-].[Cl-].[Mn+2]` (10%) | set ✓ / any ✓ |

---

### Reaction #690  yield=87.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t1.json) (反应 idx 在该 JSON 内 = #9)

```
C=Cc1cccc(Cl)c1>>ClC(CBr)c1cccc(Cl)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.5%) | `platinum` (1.3%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (86.3%) | `glassy_carbon` (7.5%) | `carbon_generic` (1.7%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.2%) | `carbon` (2.3%) | `nickel` (1.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (94.1%) | `platinum_plate` (3.2%) | `platinum_foil` (1.5%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.3%) | `H` (1.5%) | `ABSENT` (1.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (94.2%) | `BF4` (4.6%) | `PF6` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (73.3%) | `carboxylic_acid` (2.2%) | `alkali_other_salt` (1.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.3%) | `pyridine_organocat` (3.6%) | `brønsted_acid_cat` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (83.9%) | `polar_aprotic_sulfoxide` (5.7%) | `polar_protic_acid` (3.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCCl` + `OC(C(F)(F)F)C(F)(F` | `ClCCCl` (83%) | `OC(C(F)(F)F)C(F)(F` (52%) | `FC(F)(F)c1ccccc1` (32%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O.O.O.O.O.O.O.O.O.` (28%) | `CC[Si](CC)CC` (20%) | `O` (17%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `__OTHER__` (92%) | `c1ccncc1` (81%) | `__ABSENT__` (6%) | set ✓ / any ✓ |

---

### Reaction #691  yield=67.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t1.json) (反应 idx 在该 JSON 内 = #10)

```
C=Cc1ccccc1Cl>>ClC(CBr)c1ccccc1Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.3%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `glassy_carbon` (67.6%) | `graphite_generic` (26.8%) | `platinum_foil` (3.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.9%) | `carbon` (1.7%) | `stainless_steel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (46.9%) | `platinum_plate` (29.5%) | `platinum_foil` (16.7%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (96.1%) | `ABSENT` (3.7%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.1%) | `H` (37.9%) | `Na` (9.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (93.2%) | `BF4` (5.5%) | `molecular_no_ion` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (64.2%) | `carboxylic_acid` (5.5%) | `bromide_anion` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.6%) | `brønsted_acid_cat` (2.7%) | `Mn_complex` (2.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_acid` (54.9%) | `halogenated_aliphatic` (31.5%) | `polar_aprotic_sulfoxide` (3.8%) | ✓ |
| 溶剂 set | 79 | `CC(=O)O` + `OC(C(F)(F)F)C(F)(F` + `ClCCl` | `CC(=O)O` (100%) | `OC(C(F)(F)F)C(F)(F` (82%) | `ClCCl` (76%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `O=S(=O)(O)C(F)(F)F` + `CC(=O)OC(C)=O` + `CN(C)c1ccncc1` | `O=S(=O)(O)C(F)(F)F` (98%) | `CC(=O)OC(C)=O` (95%) | `CN(C)c1ccncc1` (80%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COc1c(I)cc2c(c1I)-` | `COc1c(I)cc2c(c1I)-` (92%) | `__ABSENT__` (11%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #692  yield=58.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t1.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t1.json) (反应 idx 在该 JSON 内 = #11)

```
C=Cc1ccccn1>>ClC(CBr)c1ccccn1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.3%) | `platinum` (2.4%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `glassy_carbon` (96.7%) | `platinum_foil` (1.2%) | `graphite_rod` (0.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.2%) | `carbon` (0.3%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (80.1%) | `platinum_generic` (10.2%) | `platinum_foil` (7.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (89.3%) | `divided` (8.6%) | `ABSENT` (2.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (34.6%) | `K` (33.4%) | `NBu4` (14.4%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (99.2%) | `ABSENT` (0.2%) | `BF4` (0.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `carboxylic_acid` (79.4%) | `polyhalo_radical_transfer` (7.8%) | `alkali_other_salt` (0.6%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.8%) | `brønsted_acid_cat` (2.3%) | `pyridine_organocat` (0.6%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_sulfoxide` (79.9%) | `ABSENT` (10.6%) | `polar_aprotic_nitrile` (5.1%) | ✗ |
| 溶剂 set | 79 | `CS(C)=O` + `O` | `CS(C)=O` (98%) | `O` (97%) | `CC#N` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `O=C(O)C(F)(F)F` | `O=C(O)C(F)(F)F` (96%) | `CC(=O)O` (94%) | `O=O` (19%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[I-].[Li+]` | `O=S(=O)([O-])C(F)(` (52%) | `__ABSENT__` (19%) | `[I-].[Li+]` (17%) | set ✗ / any ✓ |

---

### Reaction #693  yield=73.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #13)

```
C=Cc1scnc1C>>Cc1ncsc1C(Cl)CBr
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.0%) | `platinum` (9.9%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `glassy_carbon` (88.3%) | `graphite_generic` (7.0%) | `graphite_rod` (1.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `carbon` (0.5%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (93.0%) | `platinum_generic` (5.6%) | `platinum_foil` (1.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (38.5%) | `NBu4` (30.0%) | `Na` (13.0%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (99.1%) | `molecular_no_ion` (0.3%) | `BF4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `carboxylic_acid` (25.5%) | `polyhalo_radical_transfer` (11.3%) | `bromide_anion` (5.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.1%) | `organic_neutral_cat` (2.1%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (34.6%) | `polar_aprotic_sulfoxide` (28.0%) | `polar_protic_acid` (25.8%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `O` (96%) | `CC#N` (93%) | `CC(=O)O` (20%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `O=C(O)C(F)(F)F` (33%) | `CC(=O)O` (32%) | `CC(=O)OC(C)=O` (18%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (85%) | `O=S(=O)([O-])C(F)(` (3%) | `CC(=O)NC1CC2(CCCCC` (2%) | set ✓ / any ✓ |

---

### Reaction #694  yield=93.0%

**Source paper**: [`China/China_CN119061410_A_2024-12-03.json`](reactions_by_journal_alkene_ec_audited/China/China_CN119061410_A_2024-12-03.json) (反应 idx 在该 JSON 内 = #6)

```
C=COC(=O)c1ccccc1>>O=C(OC(Cl)CBr)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (97.3%) | `glassy_carbon` (1.1%) | `graphite_felt` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (78.9%) | `platinum` (20.7%) | `nickel` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `graphite_generic` (97.8%) | `platinum_plate` (0.7%) | `platinum_foil` (0.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NEt4` (71.8%) | `ABSENT` (9.1%) | `H` (7.2%) | ✗ |
| 电解质 anion | 26 | `Br` | `BF4` (87.1%) | `Br` (8.6%) | `ABSENT` (3.1%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (91.9%) | `n_halo_imide` (1.7%) | `carboxylic_acid` (0.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Mn_complex` (0.1%) | `brønsted_acid_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (98.0%) | `polar_aprotic_nitrile` (1.1%) | `halogenated_aliphatic` (0.5%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `O` (52%) | `ClCCl` (29%) | `FC(F)(F)c1ccccc1` (11%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `ClC(Cl)(Cl)C(Cl)(C` (35%) | `Cc1ccc(I)cc1` (31%) | `O=S(=O)(O)C(F)(F)F` (19%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (88%) | `[Cl][Mn][Cl]` (8%) | `O=S(=O)([O-])C(F)(` (2%) | set ✓ / any ✓ |

---

### Reaction #695  yield=87.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #20)

```
C=COC(=O)CCCCCCCCCCC>>CCCCCCCCCCCC(=O)OC(Cl)CBr
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (77.3%) | `graphite_rod` (7.7%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (17.3%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (95.6%) | `platinum_plate` (1.6%) | `graphite_generic` (1.5%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (95.4%) | `ABSENT` (4.0%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (57.1%) | `H` (20.5%) | `NEt4` (19.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (42.4%) | `BF4` (36.7%) | `ClO4` (17.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (64.1%) | `carboxylic_acid` (7.6%) | `transition_metal_salt_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (61.8%) | `brønsted_acid_cat` (37.0%) | `Mn_complex` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (51.5%) | `ABSENT` (42.9%) | `polar_protic_acid` (4.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (97%) | `O` (32%) | `CCOCC` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `OC(C(F)(F)F)C(F)(F` (48%) | `BrCCBr` (19%) | `CC(=O)O` (18%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (56%) | `O=S(=O)([O-])C(F)(` (23%) | `CC(=O)NC1CC2(CCCCC` (10%) | set ✓ / any ✓ |

---

### Reaction #696  yield=90.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #0)

```
C1=Cc2ccccc2C1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>ClC1Cc2ccccc2C1Br
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (1.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_generic` (92.0%) | `graphite_generic` (3.2%) | `carbon_felt` (2.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (55.7%) | `carbon` (42.9%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (91.5%) | `platinum_foil` (2.3%) | `graphite_felt` (1.2%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `ABSENT` (92.3%) | `undivided` (7.6%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (72.4%) | `Li` (20.4%) | `Na` (4.8%) | ✗ |
| 电解质 anion | 26 | `Br` | `ABSENT` (68.2%) | `ClO4` (17.1%) | `Cl` (7.3%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (10.0%) | `chloride_anion` (7.3%) | `alkali_hydroxide` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (29.6%) | `Mn_complex` (28.3%) | `ABSENT` (10.7%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_acid` (48.8%) | `polar_aprotic_nitrile` (32.0%) | `cyclic_ether` (5.6%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `O` (25%) | `CC#N` (11%) | `CS(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `O=C([O-])[O-].[Na+` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)([O-])C(F)(` (12%) | `__ABSENT__` (8%) | `__OTHER__` (4%) | set ✗ / any ✓ |

---

### Reaction #697  yield=84.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #1)

```
CC1=Cc2ccccc2C1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>CC1(Br)Cc2ccccc2C1Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (87.6%) | `sacrificial_iron` (6.2%) | `platinum` (3.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (75.6%) | `carbon_felt` (8.9%) | `iron_plate` (3.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (94.2%) | `nickel` (3.4%) | `platinum` (2.0%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `graphite_generic` (46.9%) | `reticulated_vitreous_carbon` (19.8%) | `carbon_generic` (9.4%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (98.2%) | `ABSENT` (1.7%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (48.5%) | `ABSENT` (43.5%) | `NBu4` (7.0%) | ✓ |
| 电解质 anion | 26 | `Br` | `ABSENT` (47.0%) | `Cl` (36.3%) | `molecular_no_ion` (12.4%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (25.3%) | `metal_oxide_oxidant` (1.9%) | `tellurium_reagent` (1.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Ni_complex` (52.1%) | `ABSENT` (28.5%) | `ferrocene_mediator` (8.6%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (75.8%) | `polar_aprotic_amide` (6.1%) | `ABSENT` (5.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (95%) | `CO` (1%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `[Cl-].[Li+]` (0%) | `[Na+].[OH-]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (3%) | `__OTHER__` (1%) | `[Br-][Ni+2]1([Br-]` (1%) | set ✗ / any ✓ |

---

### Reaction #698  yield=71.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #2)

```
C1=Cc2ccccc2CC1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>ClC1CCc2ccccc2C1Br
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.5%) | `platinum` (2.8%) | `sacrificial_magnesium` (1.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (95.8%) | `carbon_generic` (1.5%) | `carbon_felt` (0.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (98.9%) | `platinum` (0.9%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `graphite_generic` (80.4%) | `graphite_felt` (11.4%) | `unknown_electrode` (3.3%) | ✗ |
| 池型 | 4 | `ABSENT` | `ABSENT` (52.9%) | `undivided` (46.9%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (92.0%) | `NBu4` (3.1%) | `Na` (2.6%) | ✓ |
| 电解质 anion | 26 | `Br` | `ABSENT` (70.0%) | `Cl` (23.6%) | `molecular_no_ion` (3.3%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (7.9%) | `o2_oxidant` (4.7%) | `alkali_carbonate` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (36.0%) | `ferrocene_mediator` (31.5%) | `Fe_complex` (12.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (53.0%) | `polar_protic_alcohol` (16.0%) | `polar_aprotic_amide` (12.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (75%) | `CO` (16%) | `CN(C)C=O` (4%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `O=C([O-])[O-].[Na+` (0%) | `Cl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `COCCOC.[Cl][Ni][Cl` (0%) | set ✓ / any ✓ |

---

### Reaction #699  yield=79.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #3)

```
OC/C=C/c1ccccc1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>OCC(Cl)C(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (62.2%) | `platinum` (31.5%) | `ABSENT` (5.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (59.3%) | `platinum_generic` (8.8%) | `reticulated_vitreous_carbon` (8.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `ABSENT` (0.1%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (53.2%) | `platinum_foil` (46.1%) | `platinum_wire` (0.4%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (95.5%) | `ABSENT` (3.8%) | `divided` (0.7%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (59.1%) | `Li` (29.0%) | `ABSENT` (8.8%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (92.0%) | `ABSENT` (3.5%) | `ClO4` (2.9%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (13.6%) | `carboxylic_acid` (5.1%) | `hbr` (3.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (27.9%) | `Co_complex` (26.0%) | `Mn_complex` (13.4%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.2%) | `polar_protic_alcohol` (0.3%) | `aqueous` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (97%) | `CN(C)C=O` (0%) | `O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Cl-].[Cl-].[Mg+2]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (61%) | `__OTHER__` (26%) | `__ABSENT__` (4%) | set ✗ / any ✓ |

---

### Reaction #700  yield=72.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #4)

```
Cc1ccc(/C=C/CO)cc1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>OCC(Cl)C(Br)c1ccc(C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (53.8%) | `platinum` (45.9%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (29.2%) | `platinum_plate` (23.5%) | `graphite_generic` (16.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (36.1%) | `platinum_generic` (26.1%) | `platinum_wire` (19.6%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.4%) | `divided` (0.4%) | `ABSENT` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (81.5%) | `Na` (15.1%) | `ABSENT` (1.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (88.1%) | `ClO4` (8.2%) | `Br` (1.9%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (11.1%) | `carboxylic_acid` (3.3%) | `metal_oxide_oxidant` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (48.4%) | `brønsted_acid_cat` (12.5%) | `Mn_complex` (9.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.2%) | `polar_protic_alcohol` (0.2%) | `ABSENT` (0.1%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (100%) | `O` (1%) | `OCC(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Na+].[OH-]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `[Pt]` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #701  yield=70.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #5)

```
OC/C=C/c1ccc(F)cc1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>OCC(Cl)C(Br)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (63.2%) | `carbon` (35.8%) | `ABSENT` (0.9%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `platinum_generic` (33.7%) | `platinum_plate` (29.3%) | `graphite_generic` (22.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (84.4%) | `platinum_foil` (9.1%) | `platinum_plate` (4.9%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (77.8%) | `Na` (18.7%) | `NBu4` (1.7%) | ✓ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (74.2%) | `ClO4` (16.7%) | `Cl` (2.9%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (12.3%) | `diboron` (2.4%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (48.8%) | `ABSENT` (31.7%) | `Mn_complex` (4.9%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.9%) | `polar_protic_alcohol` (0.3%) | `cyclic_ether` (0.2%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (100%) | `O` (2%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (53%) | `O=S(=O)(O)C(F)(F)F` (38%) | `[Cl-].[Cl-].[Mn+2]` (2%) | set ✓ / any ✓ |

---

### Reaction #702  yield=80.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #6)

```
OC/C=C/c1ccc(Cl)cc1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>OCC(Cl)C(Br)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (53.2%) | `platinum` (44.4%) | `ABSENT` (2.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (27.1%) | `platinum_plate` (20.2%) | `graphite_generic` (16.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `ABSENT` (0.0%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (54.0%) | `platinum_foil` (21.6%) | `platinum_plate` (19.4%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.2%) | `divided` (0.5%) | `ABSENT` (0.3%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (51.2%) | `Li` (31.6%) | `ABSENT` (14.9%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (89.7%) | `ABSENT` (6.2%) | `ClO4` (1.8%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (8.8%) | `carboxylic_acid` (2.7%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (21.7%) | `Mn_complex` (20.9%) | `brønsted_acid_cat` (20.8%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (97.7%) | `polar_protic_alcohol` (1.1%) | `polar_protic_acid` (0.2%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (98%) | `O` (4%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (15%) | `__OTHER__` (7%) | `__ABSENT__` (6%) | set ✗ / any ✓ |

---

### Reaction #703  yield=88.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #7)

```
OC/C=C/c1ccc(Br)cc1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>OCC(Cl)C(Br)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (94.7%) | `carbon` (4.5%) | `ABSENT` (0.6%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `platinum_generic` (47.0%) | `platinum_plate` (34.8%) | `carbon_felt` (11.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (45.4%) | `platinum_wire` (44.7%) | `platinum_foil` (6.1%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (97.9%) | `ABSENT` (1.2%) | `divided` (0.9%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (86.0%) | `Na` (6.3%) | `ABSENT` (5.8%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (67.5%) | `ClO4` (24.1%) | `ABSENT` (4.4%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (12.6%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (29.2%) | `Pt_complex` (18.8%) | `Co_complex` (13.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (0.3%) | `polar_aprotic_amide` (0.2%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (99%) | `O` (0%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #704  yield=88.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #8)

```
OC/C=C/c1cccc(F)c1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>OCC(Cl)C(Br)c1cccc(F)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (58.9%) | `platinum` (29.1%) | `ABSENT` (11.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (49.2%) | `carbon_felt` (28.1%) | `platinum_generic` (7.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `ABSENT` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (81.4%) | `platinum_foil` (17.7%) | `platinum_wire` (0.5%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (96.4%) | `divided` (1.9%) | `ABSENT` (1.7%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (52.5%) | `Li` (29.6%) | `ABSENT` (9.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (83.5%) | `ClO4` (7.9%) | `ABSENT` (3.6%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (10.0%) | `metal_oxide_oxidant` (2.4%) | `tellurium_reagent` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (37.8%) | `Pt_complex` (33.3%) | `ABSENT` (8.9%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (97.9%) | `polar_protic_alcohol` (0.6%) | `polar_aprotic_amide` (0.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (65%) | `O` (4%) | `CN(C)C=O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (68%) | `O=S(=O)(O)C(F)(F)F` (20%) | `__ABSENT__` (7%) | set ✗ / any ✓ |

---

### Reaction #705  yield=93.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #9)

```
OC/C=C/c1cccc(Cl)c1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>OCC(Cl)C(Br)c1cccc(Cl)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (60.3%) | `platinum` (35.3%) | `ABSENT` (4.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (51.6%) | `carbon_felt` (19.3%) | `platinum_generic` (8.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `ABSENT` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (75.1%) | `platinum_foil` (22.1%) | `platinum_plate` (1.5%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (98.3%) | `ABSENT` (0.9%) | `divided` (0.8%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (59.7%) | `Na` (29.0%) | `Li` (9.3%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (68.4%) | `ABSENT` (28.8%) | `Cl` (1.7%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (11.4%) | `hbr` (2.6%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `Co_complex` (15.4%) | `brønsted_acid_cat` (15.3%) | `Mn_complex` (14.4%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (93.2%) | `polar_protic_alcohol` (2.9%) | `aqueous` (0.7%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (54%) | `CN(C)C=O` (1%) | `O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Cl-].[Li+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (14%) | `__ABSENT__` (7%) | `O=S(=O)(O)C(F)(F)F` (6%) | set ✗ / any ✓ |

---

### Reaction #706  yield=80.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #10)

```
OC/C=C/c1cccc(C(F)(F)F)c1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>OCC(Cl)C(Br)c1cccc(C(F)(F)F)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (86.6%) | `platinum` (11.5%) | `ABSENT` (1.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (94.7%) | `carbon_felt` (2.2%) | `unknown_electrode` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (80.6%) | `platinum_foil` (17.8%) | `platinum_plate` (0.8%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (77.8%) | `ABSENT` (14.0%) | `divided` (8.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (43.6%) | `ABSENT` (20.3%) | `Li` (19.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (69.1%) | `Cl` (18.9%) | `ABSENT` (6.1%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (9.4%) | `o2_oxidant` (3.1%) | `hbr` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `aryl_iodide_mediator` (32.9%) | `Co_complex` (22.1%) | `brønsted_acid_cat` (15.1%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (98.1%) | `polar_protic_alcohol` (0.6%) | `polar_aprotic_sulfoxide` (0.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (82%) | `CN(C)C=O` (1%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O.O.O.[Li+].[O-][C` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (24%) | `__ABSENT__` (13%) | `__OTHER__` (4%) | set ✗ / any ✓ |

---

### Reaction #707  yield=85.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #11)

```
OC/C=C/c1ccccc1Cl.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>OCC(Cl)C(Br)c1ccccc1Cl
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (59.2%) | `carbon` (39.9%) | `ABSENT` (0.8%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (88.6%) | `platinum_generic` (6.3%) | `carbon_felt` (1.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `carbon` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (72.9%) | `platinum_foil` (21.4%) | `platinum_wire` (4.6%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (99.4%) | `ABSENT` (0.4%) | `divided` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (70.8%) | `Na` (26.2%) | `ABSENT` (1.4%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (95.8%) | `ClO4` (2.7%) | `Cl` (1.0%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (16.7%) | `acid_anhydride` (3.2%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `aryl_iodide_mediator` (42.8%) | `brønsted_acid_cat` (15.8%) | `organic_neutral_cat` (14.3%) | ✗ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (99.0%) | `polar_protic_alcohol` (0.3%) | `polar_protic_acid` (0.2%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `CN(C)C=O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `O.O.O.[Li+].[O-][C` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (5%) | `__ABSENT__` (1%) | `Ic1ccccc1` (1%) | set ✗ / any ✓ |

---

### Reaction #708  yield=70.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #12)

```
COC/C=C/c1ccccc1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>COCC(Cl)C(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (64.6%) | `platinum` (33.8%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (89.0%) | `platinum_generic` (3.3%) | `carbon_felt` (2.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.2%) | `carbon` (0.5%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (87.5%) | `platinum_foil` (4.4%) | `platinum_plate` (3.6%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (95.6%) | `ABSENT` (3.1%) | `divided` (1.3%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (44.1%) | `Na` (29.4%) | `Li` (24.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (47.8%) | `ABSENT` (41.3%) | `Cl` (4.8%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (13.4%) | `o2_oxidant` (3.6%) | `chloride_anion` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (39.9%) | `brønsted_acid_cat` (27.3%) | `Co_complex` (11.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (91.0%) | `polar_protic_alcohol` (2.1%) | `polar_protic_acid` (2.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (96%) | `CC(=O)O` (1%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `O=O` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✓ / any ✓ |

---

### Reaction #709  yield=90.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #13)

```
CC(=O)OC/C=C/c1ccccc1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>CC(=O)OCC(Cl)C(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.8%) | `ABSENT` (3.1%) | `platinum` (1.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (96.1%) | `carbon_generic` (2.0%) | `carbon_felt` (0.8%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.2%) | `carbon` (1.6%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_generic` (67.2%) | `platinum_foil` (30.6%) | `platinum_plate` (1.0%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (83.8%) | `ABSENT` (15.8%) | `divided` (0.4%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Li` (79.7%) | `ABSENT` (9.3%) | `Na` (5.3%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (37.0%) | `ClO4` (31.4%) | `ABSENT` (12.0%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (11.5%) | `acid_anhydride` (5.3%) | `chloride_anion` (3.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (92.9%) | `ABSENT` (3.8%) | `Mn_complex` (1.4%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (89.1%) | `halogenated_aliphatic` (7.9%) | `polar_protic_acid` (1.2%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (93%) | `ClCCl` (2%) | `CN(C)C=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (49%) | `O=S(=O)(O)C(F)(F)F` (27%) | `__ABSENT__` (11%) | set ✗ / any ✓ |

---

### Reaction #710  yield=84.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t2.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t2.json) (反应 idx 在该 JSON 内 = #14)

```
OC/C=C/c1ccccc1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>ClCC(Br)C(Cl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (54.3%) | `platinum` (43.6%) | `sacrificial_zinc` (1.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (86.9%) | `platinum_generic` (4.2%) | `reticulated_vitreous_carbon` (2.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.5%) | `carbon` (0.4%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (77.7%) | `platinum_generic` (21.9%) | `platinum_plate` (0.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.6%) | `divided` (0.3%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `Na` (40.7%) | `ABSENT` (39.2%) | `molecular_no_ion` (17.1%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (72.7%) | `ABSENT` (16.4%) | `Cl` (7.7%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (9.0%) | `hbr` (7.2%) | `polyhalo_radical_transfer` (2.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (42.5%) | `ABSENT` (25.9%) | `Mn_complex` (8.8%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (97.5%) | `ABSENT` (1.3%) | `polar_protic_acid` (0.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (98%) | `O` (10%) | `O=C(O)C(F)(F)F` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `O.O.O.[Li+].[O-][C` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (52%) | `O=S(=O)(O)C(F)(F)F` (28%) | `O=S(=O)(O)C(F)(F)F` (6%) | set ✗ / any ✗ |

---

### Reaction #711  yield=65.0%

**Source paper**: [`China/China_CN119061410_A_2024-12-03.json`](reactions_by_journal_alkene_ec_audited/China/China_CN119061410_A_2024-12-03.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(C(=O)O[C@@H]2C[C@H](C)CC[C@H]2C(C)C)cc1>>CC(C)[C@@H]1CC[C@@H](C)C[C@H]1OC(=O)c1ccc(C(Cl)CBr)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.4%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (98.6%) | `glassy_carbon` (0.9%) | `carbon_rod` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.2%) | `platinum` (22.5%) | `nickel` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `graphite_generic` (97.5%) | `platinum_plate` (1.4%) | `platinum_generic` (0.4%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `ABSENT` (0.4%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.3%) | `NEt4` (30.9%) | `H` (15.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (80.5%) | `BF4` (18.1%) | `PF6` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (77.7%) | `carboxylic_acid` (3.9%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `brønsted_acid_cat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (45.0%) | `halogenated_aliphatic` (17.8%) | `polar_aprotic_nitrile` (14.5%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `CCOCC` (57%) | `O` (31%) | `FC(F)(F)c1ccccc1` (29%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `CC[Si](CC)CC` (45%) | `OB(O)B(O)O` (35%) | `__OTHER__` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (87%) | `O=S(=O)([O-])C(F)(` (10%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #712  yield=39.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t3.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t3.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(C(=O)O[C@H]2CC[C@@]3(C)C(=CC[C@H]4[C@@H]5CC[C@H]([C@H](C)CCCC(C)C)[C@]5(C)CC[C@@H]43)C2)cc1>>CC(C)CCC[C@@H](…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `sacrificial_iron` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (87.5%) | `reticulated_vitreous_carbon` (5.0%) | `graphite_rod` (2.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (52.7%) | `nickel` (42.7%) | `carbon` (2.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `nickel_foam` (48.0%) | `platinum_generic` (26.5%) | `platinum_plate` (13.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `divided` (0.2%) | `ABSENT` (0.2%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.8%) | `Li` (0.1%) | `Na` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `BF4` (88.0%) | `Br` (8.2%) | `I` (1.5%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (24.5%) | `carboxylic_acid` (9.1%) | `inorganic_simple` (2.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.0%) | `brønsted_acid_cat` (0.5%) | `pyridine_organocat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (98.3%) | `polar_aprotic_nitrile` (1.0%) | `halogenated_aliphatic` (0.5%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `__ABSENT__` (93%) | `CCOCC` (17%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__OTHER__` (21%) | `C[Si](C)(C)N=[N+]=` (17%) | `O=O` (12%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `COCCOC.[Br][Ni][Br` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #713  yield=90.0%

**Source paper**: [`ChemCommun/10.1039_D5CC04608D_p2_t3.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_D5CC04608D_p2_t3.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1cc(C[C@H](NC(=O)OCC2c3ccccc3-c3ccccc32)C(=O)O)ccc1OC>>CC(C)CC(NC(=O)OCC1c2ccccc2-c2ccccc21)C(=O)OC(C)C(Cl)CBr
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `carbon_felt` (99.8%) | `graphite_generic` (0.1%) | `carbon_rod` (0.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.7%) | `platinum_wire` (0.7%) | `platinum_generic` (0.3%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (42.3%) | `Li` (31.0%) | `ABSENT` (25.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `BF4` (57.6%) | `ABSENT` (28.3%) | `Br` (8.3%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `carboxylic_acid` (3.9%) | `diboron` (3.6%) | `ABSENT` (3.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `Mn_complex` (0.6%) | `brønsted_acid_cat` (0.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (91.3%) | `ketone` (3.6%) | `ABSENT` (1.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (91%) | `O` (18%) | `__OTHER__` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (17%) | `O=S(=O)(O)C(F)(F)F` (16%) | `[Cl-].[Cl-].[Mg+2]` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✓ / any ✓ |

---

### Reaction #714  yield=56.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (38.1%) | `ABSENT` (26.4%) | `sacrificial_zinc` (19.7%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `zinc_generic` (54.5%) | `reticulated_vitreous_carbon` (16.9%) | `ABSENT` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (59.6%) | `carbon` (25.4%) | `ABSENT` (14.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (51.2%) | `platinum_generic` (30.0%) | `carbon_felt` (8.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.8%) | `NEt4` (44.3%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (34.9%) | `PF6` (21.1%) | `Cl` (14.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `alkali_sulfonate` (10.3%) | `ABSENT` (3.8%) | `ketone` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.3%) | `organic_neutral_cat` (1.3%) | `Co_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (36.1%) | `ABSENT` (35.6%) | `halogenated_aliphatic` (24.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `CN(C)C=O` | `CC#N` (99%) | `ClCCl` (7%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `OC(C(F)(F)F)C(F)(F` (50%) | `CC[Si](CC)CC` (26%) | `BrCCBr` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COC(=O)c1ccc(C(=O)` + `N#Cc1c2ccccc2c(C#N` + `O=C1C=CC(=O)c2cccc` + `__OTHER__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #715  yield=88.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (38.1%) | `ABSENT` (26.4%) | `sacrificial_zinc` (19.7%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `zinc_generic` (54.5%) | `reticulated_vitreous_carbon` (16.9%) | `ABSENT` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (59.6%) | `carbon` (25.4%) | `ABSENT` (14.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (51.2%) | `platinum_generic` (30.0%) | `carbon_felt` (8.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.8%) | `NEt4` (44.3%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (34.9%) | `PF6` (21.1%) | `Cl` (14.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `alkali_sulfonate` (10.3%) | `ABSENT` (3.8%) | `ketone` (2.3%) | ✗ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (97.3%) | `organic_neutral_cat` (1.3%) | `Co_complex` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (36.1%) | `ABSENT` (35.6%) | `halogenated_aliphatic` (24.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `CN(C)C=O` | `CC#N` (99%) | `ClCCl` (7%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `OC(C(F)(F)F)C(F)(F` (50%) | `CC[Si](CC)CC` (26%) | `BrCCBr` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COC(=O)c1ccc(C(=O)` + `N#Cc1c2ccccc2c(C#N` + `O=C1C=CC(=O)c2cccc` + `__OTHER__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #716  yield=73.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #717  yield=35.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (38.1%) | `ABSENT` (26.4%) | `sacrificial_zinc` (19.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `zinc_generic` (54.5%) | `reticulated_vitreous_carbon` (16.9%) | `ABSENT` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (59.6%) | `carbon` (25.4%) | `ABSENT` (14.5%) | ✗ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (51.2%) | `platinum_generic` (30.0%) | `carbon_felt` (8.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.8%) | `NEt4` (44.3%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (34.9%) | `PF6` (21.1%) | `Cl` (14.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `alkali_sulfonate` (10.3%) | `ABSENT` (3.8%) | `ketone` (2.3%) | ✗ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (97.3%) | `organic_neutral_cat` (1.3%) | `Co_complex` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (36.1%) | `ABSENT` (35.6%) | `halogenated_aliphatic` (24.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `CN(C)C=O` | `CC#N` (99%) | `ClCCl` (7%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `OC(C(F)(F)F)C(F)(F` (50%) | `CC[Si](CC)CC` (26%) | `BrCCBr` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COC(=O)c1ccc(C(=O)` + `N#Cc1c2ccccc2c(C#N` + `O=C1C=CC(=O)c2cccc` + `__OTHER__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #718  yield=53.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (38.1%) | `ABSENT` (26.4%) | `sacrificial_zinc` (19.7%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `zinc_generic` (54.5%) | `reticulated_vitreous_carbon` (16.9%) | `ABSENT` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (59.6%) | `carbon` (25.4%) | `ABSENT` (14.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (51.2%) | `platinum_generic` (30.0%) | `carbon_felt` (8.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.8%) | `NEt4` (44.3%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (34.9%) | `PF6` (21.1%) | `Cl` (14.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `alkali_sulfonate` (10.3%) | `ABSENT` (3.8%) | `ketone` (2.3%) | ✗ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (97.3%) | `organic_neutral_cat` (1.3%) | `Co_complex` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (36.1%) | `ABSENT` (35.6%) | `halogenated_aliphatic` (24.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `CN(C)C=O` | `CC#N` (99%) | `ClCCl` (7%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `OC(C(F)(F)F)C(F)(F` (50%) | `CC[Si](CC)CC` (26%) | `BrCCBr` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COC(=O)c1ccc(C(=O)` + `N#Cc1c2ccccc2c(C#N` + `O=C1C=CC(=O)c2cccc` + `__OTHER__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #719  yield=0.5%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #720  yield=86.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #721  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (38.1%) | `ABSENT` (26.4%) | `sacrificial_zinc` (19.7%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `zinc_generic` (54.5%) | `reticulated_vitreous_carbon` (16.9%) | `ABSENT` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (59.6%) | `carbon` (25.4%) | `ABSENT` (14.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (51.2%) | `platinum_generic` (30.0%) | `carbon_felt` (8.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.8%) | `NEt4` (44.3%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (34.9%) | `PF6` (21.1%) | `Cl` (14.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `alkali_sulfonate` (10.3%) | `ABSENT` (3.8%) | `ketone` (2.3%) | ✗ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (97.3%) | `organic_neutral_cat` (1.3%) | `Co_complex` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (36.1%) | `ABSENT` (35.6%) | `halogenated_aliphatic` (24.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `CN(C)C=O` | `CC#N` (99%) | `ClCCl` (7%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `OC(C(F)(F)F)C(F)(F` (50%) | `CC[Si](CC)CC` (26%) | `BrCCBr` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COC(=O)c1ccc(C(=O)` + `N#Cc1c2ccccc2c(C#N` + `O=C1C=CC(=O)c2cccc` + `__OTHER__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #722  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #723  yield=76.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (38.1%) | `ABSENT` (26.4%) | `sacrificial_zinc` (19.7%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `zinc_generic` (54.5%) | `reticulated_vitreous_carbon` (16.9%) | `ABSENT` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (59.6%) | `carbon` (25.4%) | `ABSENT` (14.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (51.2%) | `platinum_generic` (30.0%) | `carbon_felt` (8.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.8%) | `NEt4` (44.3%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (34.9%) | `PF6` (21.1%) | `Cl` (14.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `alkali_sulfonate` (10.3%) | `ABSENT` (3.8%) | `ketone` (2.3%) | ✗ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (97.3%) | `organic_neutral_cat` (1.3%) | `Co_complex` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (36.1%) | `ABSENT` (35.6%) | `halogenated_aliphatic` (24.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CN(C)C=O` | `CC#N` (99%) | `ClCCl` (7%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `OC(C(F)(F)F)C(F)(F` (50%) | `CC[Si](CC)CC` (26%) | `BrCCBr` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COC(=O)c1ccc(C(=O)` + `N#Cc1c2ccccc2c(C#N` + `O=C1C=CC(=O)c2cccc` + `__OTHER__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #724  yield=72.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `cf3_source` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✗ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #725  yield=72.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (38.1%) | `ABSENT` (26.4%) | `sacrificial_zinc` (19.7%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `zinc_generic` (54.5%) | `reticulated_vitreous_carbon` (16.9%) | `ABSENT` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (59.6%) | `carbon` (25.4%) | `ABSENT` (14.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (51.2%) | `platinum_generic` (30.0%) | `carbon_felt` (8.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.8%) | `NEt4` (44.3%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (34.9%) | `PF6` (21.1%) | `Cl` (14.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `alkali_sulfonate` (10.3%) | `ABSENT` (3.8%) | `ketone` (2.3%) | ✗ |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (97.3%) | `organic_neutral_cat` (1.3%) | `Co_complex` (0.4%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (36.1%) | `ABSENT` (35.6%) | `halogenated_aliphatic` (24.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `CN(C)C=O` | `CC#N` (99%) | `ClCCl` (7%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `OC(C(F)(F)F)C(F)(F` (50%) | `CC[Si](CC)CC` (26%) | `BrCCBr` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COC(=O)c1ccc(C(=O)` + `N#Cc1c2ccccc2c(C#N` + `O=C1C=CC(=O)c2cccc` + `__OTHER__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #726  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (38.1%) | `ABSENT` (26.4%) | `sacrificial_zinc` (19.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `zinc_generic` (54.5%) | `reticulated_vitreous_carbon` (16.9%) | `ABSENT` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (59.6%) | `carbon` (25.4%) | `ABSENT` (14.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (51.2%) | `platinum_generic` (30.0%) | `carbon_felt` (8.5%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.8%) | `NEt4` (44.3%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (34.9%) | `PF6` (21.1%) | `Cl` (14.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `alkali_sulfonate` (10.3%) | `ABSENT` (3.8%) | `ketone` (2.3%) | ✗ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (97.3%) | `organic_neutral_cat` (1.3%) | `Co_complex` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_sulfoxide` | `polar_aprotic_nitrile` (36.1%) | `ABSENT` (35.6%) | `halogenated_aliphatic` (24.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `CN(C)C=O` | `CC#N` (99%) | `ClCCl` (7%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `OC(C(F)(F)F)C(F)(F` (50%) | `CC[Si](CC)CC` (26%) | `BrCCBr` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COC(=O)c1ccc(C(=O)` + `N#Cc1c2ccccc2c(C#N` + `O=C1C=CC(=O)c2cccc` + `__OTHER__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #727  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #728  yield=12.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_magnesium` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✗ |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #729  yield=16.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (38.1%) | `ABSENT` (26.4%) | `sacrificial_zinc` (19.7%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `zinc_generic` (54.5%) | `reticulated_vitreous_carbon` (16.9%) | `ABSENT` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (59.6%) | `carbon` (25.4%) | `ABSENT` (14.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (51.2%) | `platinum_generic` (30.0%) | `carbon_felt` (8.5%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.8%) | `NEt4` (44.3%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `I` | `ClO4` (34.9%) | `PF6` (21.1%) | `Cl` (14.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `alkali_sulfonate` (10.3%) | `ABSENT` (3.8%) | `ketone` (2.3%) | ✗ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (97.3%) | `organic_neutral_cat` (1.3%) | `Co_complex` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (36.1%) | `ABSENT` (35.6%) | `halogenated_aliphatic` (24.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `CN(C)C=O` | `CC#N` (99%) | `ClCCl` (7%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `OC(C(F)(F)F)C(F)(F` (50%) | `CC[Si](CC)CC` (26%) | `BrCCBr` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COC(=O)c1ccc(C(=O)` + `N#Cc1c2ccccc2c(C#N` + `O=C1C=CC(=O)c2cccc` + `__OTHER__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #730  yield=19.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `Br` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #731  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #732  yield=15.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #733  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (38.1%) | `ABSENT` (26.4%) | `sacrificial_zinc` (19.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `zinc_generic` (54.5%) | `reticulated_vitreous_carbon` (16.9%) | `ABSENT` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (59.6%) | `carbon` (25.4%) | `ABSENT` (14.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (51.2%) | `platinum_generic` (30.0%) | `carbon_felt` (8.5%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.8%) | `NEt4` (44.3%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (34.9%) | `PF6` (21.1%) | `Cl` (14.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `alkali_sulfonate` (10.3%) | `ABSENT` (3.8%) | `ketone` (2.3%) | ✗ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (97.3%) | `organic_neutral_cat` (1.3%) | `Co_complex` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (36.1%) | `ABSENT` (35.6%) | `halogenated_aliphatic` (24.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `CN(C)C=O` | `CC#N` (99%) | `ClCCl` (7%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `OC(C(F)(F)F)C(F)(F` (50%) | `CC[Si](CC)CC` (26%) | `BrCCBr` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COC(=O)c1ccc(C(=O)` + `N#Cc1c2ccccc2c(C#N` + `O=C1C=CC(=O)c2cccc` + `__OTHER__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #734  yield=0.5%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #735  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (38.1%) | `ABSENT` (26.4%) | `sacrificial_zinc` (19.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `zinc_generic` (54.5%) | `reticulated_vitreous_carbon` (16.9%) | `ABSENT` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (59.6%) | `carbon` (25.4%) | `ABSENT` (14.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (51.2%) | `platinum_generic` (30.0%) | `carbon_felt` (8.5%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.8%) | `NEt4` (44.3%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (34.9%) | `PF6` (21.1%) | `Cl` (14.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `alkali_sulfonate` (10.3%) | `ABSENT` (3.8%) | `ketone` (2.3%) | ✗ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (97.3%) | `organic_neutral_cat` (1.3%) | `Co_complex` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (36.1%) | `ABSENT` (35.6%) | `halogenated_aliphatic` (24.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `CN(C)C=O` | `CC#N` (99%) | `ClCCl` (7%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `OC(C(F)(F)F)C(F)(F` (50%) | `CC[Si](CC)CC` (26%) | `BrCCBr` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COC(=O)c1ccc(C(=O)` + `N#Cc1c2ccccc2c(C#N` + `O=C1C=CC(=O)c2cccc` + `__OTHER__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #736  yield=21.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #737  yield=13.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_iron` | `carbon` (38.1%) | `ABSENT` (26.4%) | `sacrificial_zinc` (19.7%) | ✗ |
| 阳极 (细类) | 43 | `carbon_generic` | `zinc_generic` (54.5%) | `reticulated_vitreous_carbon` (16.9%) | `ABSENT` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (59.6%) | `carbon` (25.4%) | `ABSENT` (14.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (51.2%) | `platinum_generic` (30.0%) | `carbon_felt` (8.5%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.8%) | `NEt4` (44.3%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (34.9%) | `PF6` (21.1%) | `Cl` (14.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `alkali_sulfonate` (10.3%) | `ABSENT` (3.8%) | `ketone` (2.3%) | ✗ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (97.3%) | `organic_neutral_cat` (1.3%) | `Co_complex` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (36.1%) | `ABSENT` (35.6%) | `halogenated_aliphatic` (24.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `CN(C)C=O` | `CC#N` (99%) | `ClCCl` (7%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `OC(C(F)(F)F)C(F)(F` (50%) | `CC[Si](CC)CC` (26%) | `BrCCBr` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COC(=O)c1ccc(C(=O)` + `N#Cc1c2ccccc2c(C#N` + `O=C1C=CC(=O)c2cccc` + `__OTHER__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #738  yield=16.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #739  yield=27.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #740  yield=13.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_aluminum` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✗ |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #741  yield=0.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (38.1%) | `ABSENT` (26.4%) | `sacrificial_zinc` (19.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `zinc_generic` (54.5%) | `reticulated_vitreous_carbon` (16.9%) | `ABSENT` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (59.6%) | `carbon` (25.4%) | `ABSENT` (14.5%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (51.2%) | `platinum_generic` (30.0%) | `carbon_felt` (8.5%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.8%) | `NEt4` (44.3%) | `ABSENT` (2.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (34.9%) | `PF6` (21.1%) | `Cl` (14.3%) | ✗ |
| 试剂大类 | 103 | `cf3_source` | `alkali_sulfonate` (10.3%) | `ABSENT` (3.8%) | `ketone` (2.3%) | ✗ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (97.3%) | `organic_neutral_cat` (1.3%) | `Co_complex` (0.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (36.1%) | `ABSENT` (35.6%) | `halogenated_aliphatic` (24.9%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `CN(C)C=O` | `CC#N` (99%) | `ClCCl` (7%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `OC(C(F)(F)F)C(F)(F` (50%) | `CC[Si](CC)CC` (26%) | `BrCCBr` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `COC(=O)c1ccc(C(=O)` + `N#Cc1c2ccccc2c(C#N` + `O=C1C=CC(=O)c2cccc` + `__OTHER__` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✗ / any ✓ |

---

### Reaction #742  yield=13.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✗ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #743  yield=20.0%

**Source paper**: [`ChemCommun/10.1039_d5cc00744e_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/10.1039_d5cc00744e_p2_t0.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(C)(C)C)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccc1)C(F)(F)F>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ |
| 阳极 (细类) | 43 | `zinc_generic` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_generic` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #744  yield=40.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #0)

```
C=C(C)c1ccccc1.O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1>>CC(CC(F)(F)F)(c1ccccc1)c1ccc(C#N)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (85.2%) | `sacrificial_zinc` (7.7%) | `ABSENT` (4.1%) | ✓ |
| 阳极 (细类) | 43 | `zinc_plate` | `zinc_plate` (38.5%) | `unknown_electrode` (19.5%) | `graphite_generic` (15.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.1%) | `stainless_steel` (0.6%) | `carbon` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (95.7%) | `platinum_generic` (1.9%) | `unknown_electrode` (1.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (97.5%) | `divided` (2.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (41.9%) | `NEt4` (41.3%) | `NBu4` (7.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (45.5%) | `BF4` (38.0%) | `molecular_no_ion` (7.7%) | ✓ |
| 试剂大类 | 103 | `boron_lewis_acid` | `water` (17.6%) | `boron_lewis_acid` (8.8%) | `ABSENT` (7.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (96.4%) | `Cu_complex` (1.2%) | `Mn_complex` (1.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (75.9%) | `ABSENT` (11.6%) | `polar_aprotic_amide` (6.7%) | ✓ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC(C)=O` (63%) | `CC#N` (16%) | `CN(C)C=O` (13%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `O` (68%) | `__ABSENT__` (3%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #745  yield=43.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #1)

```
N#Cc1ccc(C#N)cc1.C=C(c1ccccc1)C1CC1c1ccccc1.O=S(=O)(c1ccccn1)C(F)F>>N#Cc1ccc(C(C/C=C(/CC(F)F)c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `sacrificial_zinc` (98.7%) | `carbon` (0.7%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `zinc_plate` | `zinc_generic` (62.4%) | `zinc_plate` (35.2%) | `platinum_plate` (0.5%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `carbon` (80.5%) | `platinum` (17.9%) | `nickel` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `carbon_cloth` | `carbon_felt` (51.1%) | `reticulated_vitreous_carbon` (40.8%) | `platinum_plate` (2.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `divided` (1.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (84.0%) | `NBu4` (6.0%) | `ABSENT` (5.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (61.8%) | `molecular_no_ion` (18.6%) | `Cl` (8.8%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `thiol` (12.7%) | `ABSENT` (6.2%) | `pyridine` (2.6%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (99.6%) | `pyridine_organocat` (0.3%) | `organic_neutral_cat` (0.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (90.2%) | `ABSENT` (7.6%) | `polar_aprotic_amide` (1.9%) | ✓ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (98%) | `__OTHER__` (1%) | `CS(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (16%) | `Sc1ccccc1` (9%) | `O` (6%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `CC(C)(C)c1ccnc(-c2` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✗ / any ✗ |

---

### Reaction #746  yield=50.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #2)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1cccc(Cl)c1>>N#Cc1ccc(C(CC(F)(F)F)c2cccc(Cl)c2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (56.5%) | `ABSENT` (24.1%) | `platinum` (9.6%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (80.2%) | `graphite_cloth` (6.7%) | `unknown_electrode` (4.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.6%) | `carbon` (2.8%) | `ABSENT` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (92.8%) | `platinum_generic` (1.9%) | `carbon_rod` (1.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (57.9%) | `NBu4` (25.7%) | `NEt4` (11.6%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (53.0%) | `BF4` (25.8%) | `ClO4` (6.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.9%) | `water` (4.0%) | `boron_lewis_acid` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (95.6%) | `Cu_complex` (1.4%) | `Co_complex` (1.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `halogenated_aliphatic` (46.4%) | `polar_aprotic_nitrile` (38.2%) | `ABSENT` (10.9%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `ClCCCl` (74%) | `ClCCl` (16%) | `O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `BrCCBr` (0%) | `O=C(O)C(F)(F)F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #747  yield=50.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1ccccc1F.O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1>>N#Cc1ccc(C(CC(F)(F)F)c2ccccc2F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (92.6%) | `ABSENT` (6.3%) | `platinum` (1.0%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (86.5%) | `graphite_generic` (4.5%) | `unknown_electrode` (3.3%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.6%) | `carbon` (2.7%) | `stainless_steel` (1.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (99.0%) | `platinum_generic` (0.3%) | `platinum_mesh` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (50.9%) | `ABSENT` (37.3%) | `NEt4` (10.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (51.6%) | `ABSENT` (34.1%) | `ClO4` (8.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `water` (7.0%) | `hf_amine_complex` (5.2%) | `ABSENT` (5.0%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (89.4%) | `Cu_complex` (3.9%) | `organic_neutral_cat` (2.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `halogenated_aliphatic` (56.1%) | `polar_aprotic_nitrile` (38.4%) | `ABSENT` (1.8%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `ClCCCl` (40%) | `ClCCl` (18%) | `OC(C(F)(F)F)C(F)(F` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O` (20%) | `CCN(CC)CC.F.F.F` (4%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #748  yield=49.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #4)

```
O=S(=O)(c1ccccc1)C(F)(F)F.C=Cc1ccc(C(C)(C)C)cc1.CCOC(=O)c1ccc(C#N)cc1>>CCOC(=O)c1ccc(C(CC(F)(F)F)c2ccc(C(C)(C)C)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (97.4%) | `ABSENT` (1.1%) | `platinum` (0.8%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `reticulated_vitreous_carbon` (43.5%) | `carbon_felt` (30.5%) | `carbon_rod` (12.3%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.5%) | `nickel` (1.4%) | `carbon` (0.7%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (98.6%) | `nickel_foam` (0.6%) | `carbon_felt` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (76.8%) | `NBu4` (18.5%) | `NEt4` (2.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (64.7%) | `BF4` (22.3%) | `ClO4` (10.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `water` (6.4%) | `ABSENT` (5.7%) | `alkali_other_salt` (2.8%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `pyridine_organocat` (46.5%) | `ABSENT` (25.5%) | `Mn_complex` (9.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `ABSENT` (50.3%) | `polar_aprotic_nitrile` (40.1%) | `halogenated_aliphatic` (8.3%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O` (25%) | `__ABSENT__` (2%) | `[H+].[OH-]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (49%) | `__OTHER__` (10%) | `CC(=O)[O-].CC(=O)[` (9%) | set ✗ / any ✗ |

---

### Reaction #749  yield=56.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #5)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1ccc(OC(=O)[C@@H](C)c2ccc3cc(OC)ccc3c2)cc1>>COc1ccc2cc([C@H](C)C(=O)Oc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (99.3%) | `ABSENT` (0.3%) | `sacrificial_zinc` (0.2%) | ✓ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (95.8%) | `graphite_cloth` (1.4%) | `reticulated_vitreous_carbon` (1.1%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.1%) | `carbon` (0.7%) | `ABSENT` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (99.6%) | `platinum_generic` (0.2%) | `carbon_rod` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (48.9%) | `NBu4` (46.8%) | `NEt4` (4.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (62.2%) | `ABSENT` (35.9%) | `PF6` (0.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `water` (8.3%) | `boron_lewis_acid` (7.0%) | `ABSENT` (7.0%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (50.0%) | `Cu_complex` (40.9%) | `Co_complex` (2.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (38.2%) | `halogenated_aliphatic` (31.6%) | `ABSENT` (23.8%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (31%) | `CC(C)=O` (11%) | `OC(C(F)(F)F)C(F)(F` (7%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O` (41%) | `__ABSENT__` (5%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #750  yield=51.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #6)

```
N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccn1)C(F)F.C=Cc1ccc(OC(=O)C23CC4CC(CC(C4)C2)C3)cc1>>N#Cc1ccc(C(CC(F)F)c2ccc(OC(=O)C34CC5…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `sacrificial_zinc` (100.0%) | `sacrificial_aluminum` (0.0%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `zinc_plate` | `zinc_generic` (98.5%) | `zinc_plate` (1.4%) | `unknown_electrode` (0.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (82.0%) | `carbon` (17.7%) | `ABSENT` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `reticulated_vitreous_carbon` (60.4%) | `carbon_felt` (24.9%) | `platinum_generic` (14.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (96.7%) | `divided` (3.1%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `BnNMe3` (87.5%) | `Li` (7.3%) | `NBu4` (3.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `Cl` (43.2%) | `ClO4` (37.2%) | `ABSENT` (8.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `thiol` (16.9%) | `ABSENT` (6.9%) | `water` (3.7%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (97.6%) | `Co_complex` (1.2%) | `pyridine_organocat` (0.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (94.9%) | `polar_aprotic_amide` (2.8%) | `ABSENT` (2.2%) | ✓ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (89%) | `__OTHER__` (0%) | `__ABSENT__` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (9%) | `O` (8%) | `Sc1ccccc1` (7%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1cnc2c(c1)ccc1ccc` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #751  yield=51.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #7)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1ccc2c(c1)CC[C@@H]1[C@@H]2CC[C@]2(C)C(=O)CC[C@@H]12>>C[C@]12CC[C@@H]3c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (92.3%) | `ABSENT` (4.2%) | `sacrificial_zinc` (2.5%) | ✓ |
| 阳极 (细类) | 43 | `zinc_plate` | `reticulated_vitreous_carbon` (51.2%) | `carbon_rod` (23.1%) | `unknown_electrode` (12.7%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.8%) | `carbon` (0.9%) | `ABSENT` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (97.3%) | `platinum_generic` (2.2%) | `carbon_felt` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (46.5%) | `NBu4` (26.8%) | `ABSENT` (25.2%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (52.6%) | `ABSENT` (29.4%) | `PF6` (9.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (18.5%) | `water` (2.9%) | `thiol` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (58.3%) | `Cu_complex` (23.9%) | `Co_complex` (8.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (86.1%) | `halogenated_aliphatic` (6.2%) | `ABSENT` (3.7%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `CC(C)=O` (18%) | `FC(F)(F)c1ccccc1` (6%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `BrCCBr` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #752  yield=55.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #8)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1cc(OC)cc(OC)c1>>COc1cc(OC)cc(C(CC(F)(F)F)c2ccc(C#N)cc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `ABSENT` (66.4%) | `carbon` (29.5%) | `platinum` (2.1%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (61.9%) | `ABSENT` (22.2%) | `reticulated_vitreous_carbon` (6.3%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (90.7%) | `ABSENT` (7.6%) | `carbon` (1.4%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (76.8%) | `ABSENT` (17.1%) | `platinum_generic` (4.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (51.8%) | `NEt4` (30.5%) | `ABSENT` (16.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (51.8%) | `PF6` (27.3%) | `ABSENT` (16.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `water` (10.6%) | `ABSENT` (7.7%) | `hydrosilane` (3.0%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `Co_complex` (56.0%) | `ABSENT` (31.6%) | `Cu_complex` (7.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (73.9%) | `halogenated_aliphatic` (14.7%) | `ABSENT` (4.5%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (49%) | `CC(C)=O` (18%) | `FC(F)(F)c1ccccc1` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O` (22%) | `O=O` (2%) | `CCN(CC)CC.F.F.F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__OTHER__` (31%) | `CC(C)(C)c1cc2c(c(C` (20%) | `__ABSENT__` (20%) | set ✗ / any ✗ |

---

### Reaction #753  yield=57.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #9)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1ccc(Br)cc1>>N#Cc1ccc(C(CC(F)(F)F)c2ccc(Br)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (81.7%) | `ABSENT` (14.6%) | `platinum` (1.9%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (61.9%) | `unknown_electrode` (14.4%) | `reticulated_vitreous_carbon` (8.3%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (93.3%) | `carbon` (3.9%) | `ABSENT` (2.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (98.5%) | `ABSENT` (0.6%) | `platinum_generic` (0.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (0.9%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (64.5%) | `NBu4` (28.0%) | `NEt4` (7.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (58.8%) | `BF4` (34.3%) | `PF6` (5.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `water` (23.5%) | `ABSENT` (4.7%) | `hf_amine_complex` (2.5%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (67.5%) | `Cu_complex` (26.0%) | `Mn_complex` (2.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `halogenated_aliphatic` (36.8%) | `ABSENT` (32.9%) | `polar_aprotic_nitrile` (24.3%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `ClCCl` (22%) | `ClCCCl` (21%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O` (74%) | `CCN(CC)CC.F.F.F` (0%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #754  yield=53.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #10)

```
N#Cc1ccc(C#N)cc1.C=Cc1ccc(C(C)(C)C)cc1.O=C1OI(C(F)(F)F)c2ccccc21>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `sacrificial_zinc` (46.1%) | `carbon` (25.1%) | `platinum` (17.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `zinc_plate` | `zinc_generic` (42.2%) | `platinum_generic` (15.2%) | `platinum_plate` (13.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (78.2%) | `carbon` (18.6%) | `ABSENT` (1.9%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_generic` (48.6%) | `platinum_plate` (25.3%) | `carbon_rod` (8.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (74.9%) | `NEt4` (16.1%) | `BnNMe3` (3.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (31.9%) | `Cl` (23.6%) | `BF4` (20.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.7%) | `thiol` (3.0%) | `metal_oxide_oxidant` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (98.1%) | `organic_neutral_cat` (0.8%) | `Co_complex` (0.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (80.2%) | `ABSENT` (12.1%) | `polar_aprotic_amide` (2.9%) | ✓ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (99%) | `__OTHER__` (1%) | `ClCCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `BrCCBr` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `O.O.O.O.[Br-].[Br-` (0%) | set ✗ / any ✗ |

---

### Reaction #755  yield=53.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #11)

```
O=S(=O)(c1ccccc1)C(F)(F)F.C=Cc1ccc(C(C)(C)C)cc1.CC(C)[C@@H]1CC[C@@H](C)C[C@H]1OC(=O)c1ccc(C#N)cc1>>CC(C)[C@@H]1CC[C@@…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (90.3%) | `platinum` (4.3%) | `sacrificial_zinc` (4.2%) | ✓ |
| 阳极 (细类) | 43 | `zinc_plate` | `reticulated_vitreous_carbon` (46.8%) | `carbon_rod` (26.6%) | `graphite_cloth` (15.3%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (94.6%) | `carbon` (3.1%) | `nickel` (2.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (97.9%) | `carbon_felt` (1.0%) | `nickel_foam` (0.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (76.7%) | `NBu4` (20.3%) | `ABSENT` (1.6%) | ✓ |
| 电解质 anion | 26 | `BF4` | `BF4` (40.5%) | `PF6` (32.4%) | `ClO4` (20.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (26.5%) | `water` (5.1%) | `thiol` (1.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (97.1%) | `organic_neutral_cat` (1.2%) | `Mn_complex` (0.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (46.9%) | `halogenated_aliphatic` (31.6%) | `ABSENT` (15.6%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (5%) | `ClCCCl` (4%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #756  yield=52.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #12)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1cccs1>>N#Cc1ccc(C(CC(F)(F)F)c2cccs2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (74.3%) | `ABSENT` (18.3%) | `platinum` (5.2%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (82.5%) | `graphite_cloth` (6.7%) | `reticulated_vitreous_carbon` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.3%) | `carbon` (1.7%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (98.0%) | `ABSENT` (0.9%) | `platinum_generic` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (0.8%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (99.3%) | `NEt4` (0.3%) | `NBu4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (99.2%) | `BF4` (0.4%) | `ClO4` (0.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (12.0%) | `hf_amine_complex` (5.8%) | `ABSENT` (4.5%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (72.0%) | `Cu_complex` (14.6%) | `organic_neutral_cat` (6.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (33.1%) | `ABSENT` (29.5%) | `halogenated_aliphatic` (25.5%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (34%) | `CC(C)=O` (22%) | `OC(C(F)(F)F)C(F)(F` (11%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O` (48%) | `[H+].[OH-]` (1%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (99%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #757  yield=53.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #13)

```
O=S(=O)(c1ccccc1)C(F)(F)F.COC(=O)c1ccc(C#N)cc1.C=Cc1ccc(C(C)(C)C)cc1>>COC(=O)c1ccc(C(CC(F)(F)F)c2ccc(C(C)(C)C)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (97.1%) | `platinum` (1.8%) | `ABSENT` (0.9%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (62.3%) | `graphite_cloth` (19.9%) | `reticulated_vitreous_carbon` (12.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.5%) | `carbon` (0.3%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (99.9%) | `platinum_generic` (0.0%) | `carbon_felt` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (59.5%) | `NEt4` (23.7%) | `ABSENT` (14.5%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (41.9%) | `PF6` (25.7%) | `ABSENT` (15.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (20.6%) | `water` (3.6%) | `phosphine_neutral` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (78.3%) | `Cu_complex` (7.9%) | `pyridine_organocat` (5.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (38.6%) | `ABSENT` (36.7%) | `halogenated_aliphatic` (18.9%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (9%) | `ClCCCl` (4%) | `CC(C)=O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `C[Si](C)(C)N=[N+]=` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #758  yield=52.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #14)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=C(c1ccccc1)C1CC1c1ccccc1>>N#Cc1ccc(C(C/C=C(/CC(F)(F)F)c2ccccc2)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (97.0%) | `ABSENT` (1.5%) | `platinum` (0.9%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (80.8%) | `reticulated_vitreous_carbon` (6.8%) | `graphite_generic` (3.8%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (75.6%) | `carbon` (23.8%) | `nickel` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (98.2%) | `reticulated_vitreous_carbon` (0.7%) | `platinum_mesh` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (64.1%) | `Li` (28.8%) | `NEt4` (5.1%) | ✗ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (45.2%) | `molecular_no_ion` (42.2%) | `ClO4` (5.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.3%) | `metal_oxide_oxidant` (2.5%) | `tellurium_reagent` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (92.0%) | `Mn_complex` (3.8%) | `pyridine_organocat` (1.2%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (79.7%) | `ABSENT` (15.4%) | `aqueous` (1.5%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (97%) | `O` (1%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `BrCCBr` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #759  yield=63.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #15)

```
C=Cc1ccccc1.O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1>>N#Cc1ccc(C(CC(F)(F)F)c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (52.7%) | `ABSENT` (24.7%) | `sacrificial_zinc` (12.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_rod` (65.1%) | `graphite_cloth` (8.2%) | `reticulated_vitreous_carbon` (7.7%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_zinc` | `platinum` (87.0%) | `carbon` (7.2%) | `ABSENT` (3.7%) | ✗ |
| 阴极 (细类) | 49 | `zinc_plate` | `platinum_plate` (94.6%) | `platinum_mesh` (1.5%) | `carbon_felt` (1.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.4%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `ABSENT` (89.7%) | `NBu4` (7.5%) | `NEt4` (2.3%) | ✗ |
| 电解质 anion | 26 | `Cl` | `ABSENT` (86.8%) | `BF4` (10.7%) | `ClO4` (1.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `water` (8.5%) | `ABSENT` (5.8%) | `boron_lewis_acid` (3.0%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (76.1%) | `Cu_complex` (16.6%) | `Mn_complex` (2.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `halogenated_aliphatic` (46.1%) | `ABSENT` (41.9%) | `polar_aprotic_nitrile` (6.4%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `ClCCCl` (60%) | `__ABSENT__` (3%) | `ClCCl` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O` (60%) | `BrCCBr` (3%) | `[H+].[OH-]` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (95%) | `__OTHER__` (5%) | `c1ccncc1` (5%) | set ✗ / any ✗ |

---

### Reaction #760  yield=61.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #16)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1ccc(OC(=O)C(C)c2ccc(CC(C)C)cc2)cc1>>CC(C)Cc1ccc(C(C)C(=O)Oc2ccc(C(CC(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (93.3%) | `ABSENT` (4.8%) | `sacrificial_zinc` (1.1%) | ✓ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (87.1%) | `graphite_cloth` (3.5%) | `reticulated_vitreous_carbon` (3.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.5%) | `nickel` (2.5%) | `carbon` (1.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (97.9%) | `nickel_plate` (0.8%) | `platinum_generic` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (59.6%) | `ABSENT` (37.6%) | `NEt4` (2.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (46.1%) | `BF4` (44.9%) | `PF6` (5.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (9.5%) | `alkali_carboxylate` (3.5%) | `thiol` (3.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (74.4%) | `Cu_complex` (20.9%) | `organic_neutral_cat` (2.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `halogenated_aliphatic` (63.6%) | `ABSENT` (18.6%) | `polar_aprotic_nitrile` (8.4%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `ClCCl` (29%) | `ClCCCl` (27%) | `OC(C(F)(F)F)C(F)(F` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #761  yield=69.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #17)

```
N#Cc1ccc(C#N)cc1.C=Cc1cccc(OC)c1.O=S(=O)(c1ccccn1)C(F)F>>COc1cccc(C(CC(F)F)c2ccc(C#N)cc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `sacrificial_zinc` (99.7%) | `carbon` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `zinc_plate` | `zinc_generic` (99.4%) | `zinc_plate` (0.6%) | `carbon_cloth` (0.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (69.5%) | `carbon` (30.1%) | `sacrificial_zinc` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `reticulated_vitreous_carbon` (91.5%) | `platinum_generic` (6.8%) | `carbon_felt` (1.2%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `divided` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `BnNMe3` (93.1%) | `Li` (2.7%) | `NBu4` (2.2%) | ✓ |
| 电解质 anion | 26 | `BF4` | `Cl` (47.8%) | `ClO4` (30.6%) | `I` (12.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `thiol` (11.8%) | `ABSENT` (8.2%) | `o2_oxidant` (2.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.0%) | `Co_complex` (1.0%) | `organic_neutral_cat` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (98.6%) | `ABSENT` (1.1%) | `polar_aprotic_amide` (0.2%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `FC(F)(F)c1ccccc1` (0%) | `__ABSENT__` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (18%) | `Sc1ccccc1` (11%) | `O` (7%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1cnc2c(c1)ccc1ccc` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #762  yield=65.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #18)

```
C=Cc1cccc(F)c1.O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1>>N#Cc1ccc(C(CC(F)(F)F)c2cccc(F)c2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (46.3%) | `sacrificial_zinc` (33.8%) | `ABSENT` (14.1%) | ✓ |
| 阳极 (细类) | 43 | `zinc_plate` | `reticulated_vitreous_carbon` (31.7%) | `graphite_cloth` (26.2%) | `carbon_rod` (18.2%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.0%) | `ABSENT` (1.3%) | `carbon` (1.0%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (93.7%) | `ABSENT` (2.3%) | `platinum_generic` (1.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.1%) | `divided` (1.6%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (72.1%) | `NBu4` (20.4%) | `Li` (3.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (41.9%) | `BF4` (19.3%) | `I` (14.8%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.6%) | `boron_lewis_acid` (6.3%) | `water` (5.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (69.1%) | `Cu_complex` (16.0%) | `organic_neutral_cat` (5.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `halogenated_aliphatic` (35.8%) | `polar_aprotic_nitrile` (31.7%) | `ABSENT` (22.8%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `ClCCCl` (21%) | `ClCCl` (6%) | `O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `BrCCBr` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (98%) | `__OTHER__` (2%) | `c1ccncc1` (1%) | set ✗ / any ✗ |

---

### Reaction #763  yield=65.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #19)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1ccc(OC(=O)C23CC4CC(CC(C4)C2)C3)cc1>>N#Cc1ccc(C(CC(F)(F)F)c2ccc(OC(=O)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (51.1%) | `ABSENT` (24.9%) | `sacrificial_zinc` (20.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_rod` (27.6%) | `unknown_electrode` (27.2%) | `zinc_generic` (11.7%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_zinc` | `platinum` (97.8%) | `ABSENT` (1.0%) | `carbon` (0.9%) | ✗ |
| 阴极 (细类) | 49 | `zinc_plate` | `platinum_plate` (84.5%) | `platinum_generic` (10.4%) | `carbon_felt` (2.9%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.1%) | `ABSENT` (1.4%) | `divided` (0.5%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (63.9%) | `NBu4` (34.7%) | `NEt4` (0.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (71.0%) | `BF4` (22.8%) | `ClO4` (2.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.4%) | `water` (7.7%) | `hf_amine_complex` (2.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (74.5%) | `Cu_complex` (10.9%) | `Co_complex` (9.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `halogenated_aliphatic` (81.0%) | `polar_aprotic_nitrile` (11.0%) | `polar_aprotic_amide` (3.1%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `ClCCl` (23%) | `ClCCCl` (9%) | `__ABSENT__` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #764  yield=67.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #20)

```
O=S(=O)(c1ccccc1)C(F)(F)F.C=Cc1ccc(C(C)(C)C)cc1.Cc1cc(C#N)c(C)cc1C#N>>Cc1cc(C(CC(F)(F)F)c2ccc(C(C)(C)C)cc2)c(C)cc1C#N
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (79.6%) | `ABSENT` (7.3%) | `sacrificial_zinc` (6.4%) | ✓ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (43.1%) | `reticulated_vitreous_carbon` (32.2%) | `graphite_cloth` (9.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.7%) | `carbon` (0.2%) | `ABSENT` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (99.1%) | `platinum_generic` (0.9%) | `ABSENT` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (65.6%) | `NEt4` (21.3%) | `ABSENT` (11.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (47.7%) | `ABSENT` (19.0%) | `ClO4` (14.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (18.1%) | `water` (11.2%) | `thiol` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (39.5%) | `organic_neutral_cat` (25.1%) | `Cu_complex` (19.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (93.6%) | `halogenated_aliphatic` (4.3%) | `tfe` (0.5%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (96%) | `ClCCCl` (5%) | `__OTHER__` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `O.O.O.O.[Br-].[Br-` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #765  yield=80.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #21)

```
C=Cc1ccc(F)cc1.O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1>>N#Cc1ccc(C(CC(F)(F)F)c2ccc(F)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (85.6%) | `ABSENT` (11.9%) | `sacrificial_zinc` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_cloth` | `carbon_rod` (69.3%) | `graphite_cloth` (9.8%) | `reticulated_vitreous_carbon` (9.4%) | ✗ |
| 阴极 (材料) | 15 | `sacrificial_zinc` | `platinum` (90.6%) | `carbon` (5.9%) | `ABSENT` (2.9%) | ✗ |
| 阴极 (细类) | 49 | `zinc_plate` | `platinum_plate` (98.5%) | `ABSENT` (0.6%) | `carbon_felt` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NEt4` | `ABSENT` (52.7%) | `NBu4` (30.7%) | `NEt4` (15.7%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (51.8%) | `BF4` (40.3%) | `Cl` (1.8%) | ✓ |
| 试剂大类 | 103 | `boron_lewis_acid` | `water` (11.0%) | `ABSENT` (8.0%) | `boron_lewis_acid` (2.4%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (67.4%) | `Cu_complex` (19.4%) | `Mn_complex` (4.5%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `halogenated_aliphatic` (62.4%) | `polar_aprotic_nitrile` (19.5%) | `ABSENT` (14.1%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `ClCCCl` (27%) | `ClCCl` (24%) | `__ABSENT__` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `O` (44%) | `__ABSENT__` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #766  yield=73.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #22)

```
O=S(=O)(c1ccccc1)C(F)(F)F.C=Cc1ccccc1C.N#Cc1ccc(C#N)cc1>>Cc1ccccc1C(CC(F)(F)F)c1ccc(C#N)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (89.2%) | `ABSENT` (8.5%) | `platinum` (2.1%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (84.6%) | `unknown_electrode` (8.2%) | `reticulated_vitreous_carbon` (3.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.5%) | `carbon` (0.8%) | `nickel` (0.4%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (99.4%) | `platinum_generic` (0.4%) | `platinum_mesh` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.4%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (95.7%) | `NBu4` (3.8%) | `Li` (0.4%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (92.8%) | `BF4` (5.8%) | `ClO4` (0.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (6.1%) | `water` (5.2%) | `hf_amine_complex` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (76.4%) | `Cu_complex` (14.7%) | `organic_neutral_cat` (3.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `halogenated_aliphatic` (73.9%) | `polar_aprotic_nitrile` (11.0%) | `ABSENT` (10.1%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `ClCCCl` (96%) | `OC(C(F)(F)F)C(F)(F` (24%) | `ClCCl` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)[O-].[Na+]` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #767  yield=73.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #23)

```
C=Cc1ccc(F)cc1.N#Cc1ccc(C#N)cc1.O=S(=O)(c1ccccn1)C(F)F>>N#Cc1ccc(C(CC(F)F)c2ccc(F)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `sacrificial_zinc` (99.8%) | `carbon` (0.1%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `zinc_plate` | `zinc_generic` (91.4%) | `zinc_plate` (8.5%) | `carbon_cloth` (0.0%) | ✓ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (54.4%) | `carbon` (45.2%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `reticulated_vitreous_carbon` (94.6%) | `carbon_felt` (3.9%) | `platinum_generic` (1.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `BnNMe3` (87.1%) | `Li` (8.9%) | `NBu4` (2.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (45.3%) | `Cl` (34.4%) | `ABSENT` (5.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `thiol` (13.9%) | `water` (7.7%) | `ABSENT` (4.1%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (98.9%) | `pyridine_organocat` (0.7%) | `organic_neutral_cat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (91.4%) | `ABSENT` (8.1%) | `polar_aprotic_amide` (0.5%) | ✓ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (97%) | `__OTHER__` (1%) | `__ABSENT__` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O` (34%) | `Sc1ccccc1` (6%) | `__ABSENT__` (4%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1cnc2c(c1)ccc1ccc` (0%) | `CC(C)(C)c1ccnc(-c2` (0%) | set ✗ / any ✗ |

---

### Reaction #768  yield=78.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #24)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1cc(C)ccc1C>>Cc1ccc(C)c(C(CC(F)(F)F)c2ccc(C#N)cc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (77.8%) | `ABSENT` (16.3%) | `platinum` (4.5%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (57.8%) | `unknown_electrode` (15.0%) | `reticulated_vitreous_carbon` (13.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.0%) | `carbon` (1.1%) | `ABSENT` (0.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (96.3%) | `platinum_generic` (2.3%) | `ABSENT` (0.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.4%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.0%) | `NBu4` (20.8%) | `Li` (4.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (67.0%) | `BF4` (21.8%) | `ClO4` (6.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (12.6%) | `ABSENT` (10.1%) | `metal_oxide_oxidant` (2.0%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (86.9%) | `organic_neutral_cat` (5.3%) | `Cu_complex` (3.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (62.7%) | `halogenated_aliphatic` (31.7%) | `ABSENT` (1.9%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (72%) | `ClCCCl` (17%) | `OC(C(F)(F)F)C(F)(F` (9%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O` (62%) | `__ABSENT__` (1%) | `O.O.O.[Li+].[O-][C` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #769  yield=73.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #25)

```
O=S(=O)(c1ccccc1)C(F)(F)F.C=Cc1ccccc1OC.N#Cc1ccc(C#N)cc1>>COc1ccccc1C(CC(F)(F)F)c1ccc(C#N)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (53.3%) | `ABSENT` (28.2%) | `sacrificial_zinc` (9.8%) | ✓ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (64.1%) | `unknown_electrode` (15.5%) | `reticulated_vitreous_carbon` (5.0%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.0%) | `carbon` (2.9%) | `ABSENT` (0.8%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (93.0%) | `platinum_mesh` (1.5%) | `reticulated_vitreous_carbon` (1.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `divided` (0.5%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (59.0%) | `ABSENT` (33.4%) | `NEt4` (3.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (47.1%) | `ABSENT` (31.9%) | `Cl` (8.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `water` (9.3%) | `ABSENT` (8.3%) | `o2_oxidant` (3.4%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (85.0%) | `Cu_complex` (7.6%) | `organic_neutral_cat` (2.7%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (38.5%) | `halogenated_aliphatic` (31.4%) | `ABSENT` (22.4%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC(C)=O` (18%) | `CC#N` (12%) | `ClCCCl` (6%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O` (34%) | `__ABSENT__` (2%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #770  yield=75.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #26)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1ccc2ccccc2c1>>N#Cc1ccc(C(CC(F)(F)F)c2ccc3ccccc3c2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (91.7%) | `sacrificial_zinc` (3.4%) | `platinum` (2.6%) | ✓ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (97.0%) | `graphite_cloth` (0.8%) | `reticulated_vitreous_carbon` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (96.4%) | `carbon` (3.4%) | `nickel` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (99.6%) | `carbon_rod` (0.2%) | `platinum_generic` (0.1%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (61.7%) | `NEt4` (28.4%) | `ABSENT` (6.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (63.9%) | `ABSENT` (10.0%) | `ClO4` (10.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.0%) | `boron_lewis_acid` (9.8%) | `water` (6.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (83.2%) | `Cu_complex` (10.9%) | `Mn_complex` (3.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (64.7%) | `ABSENT` (17.5%) | `halogenated_aliphatic` (12.0%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (56%) | `CC(C)=O` (6%) | `CN(C)C=O` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #771  yield=72.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #27)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1ccc(-c2ccccc2)cc1>>N#Cc1ccc(C(CC(F)(F)F)c2ccc(-c3ccccc3)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (94.3%) | `sacrificial_iron` (2.3%) | `ABSENT` (2.2%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (92.0%) | `reticulated_vitreous_carbon` (3.7%) | `unknown_electrode` (1.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (99.3%) | `carbon` (0.5%) | `ABSENT` (0.1%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (99.6%) | `platinum_generic` (0.3%) | `carbon_rod` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.6%) | `ABSENT` (0.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (77.3%) | `NBu4` (21.7%) | `NEt4` (0.8%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (70.9%) | `BF4` (27.9%) | `PF6` (0.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.9%) | `water` (7.9%) | `hf_amine_complex` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `Cu_complex` (58.4%) | `ABSENT` (36.6%) | `Mn_complex` (3.6%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `ABSENT` (44.8%) | `halogenated_aliphatic` (38.3%) | `polar_aprotic_nitrile` (10.0%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `__ABSENT__` (97%) | `ClCCl` (0%) | `CC(C)=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `BrCCBr` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (34%) | `CC(=O)O.[Cu]` (8%) | `CC(=O)[O-].[Cu+]` (5%) | set ✗ / any ✗ |

---

### Reaction #772  yield=78.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #28)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1ccc(OC)cc1>>COc1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (92.6%) | `ABSENT` (6.0%) | `platinum` (0.9%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (87.2%) | `reticulated_vitreous_carbon` (7.6%) | `carbon_cloth` (1.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (91.7%) | `carbon` (6.2%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (93.0%) | `platinum_generic` (2.9%) | `carbon_rod` (1.4%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (98.2%) | `ABSENT` (1.5%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (64.0%) | `ABSENT` (34.7%) | `NEt4` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (59.0%) | `ABSENT` (35.3%) | `PF6` (4.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `alkali_carboxylate` (7.8%) | `water` (7.6%) | `ABSENT` (4.0%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `Co_complex` (40.6%) | `Cu_complex` (30.8%) | `ABSENT` (25.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (37.2%) | `ABSENT` (23.9%) | `halogenated_aliphatic` (20.4%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (48%) | `CC(C)=O` (14%) | `FC(F)(F)c1ccccc1` (6%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)[O-].[Na+]` (63%) | `CC(C)(C)C(=O)[O-].` (9%) | `O=S(=O)([O-])C(F)(` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__OTHER__` (61%) | `__ABSENT__` (9%) | `CC1[CH-][C](=O)[Co` (4%) | set ✗ / any ✗ |

---

### Reaction #773  yield=74.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #29)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1cccc(OC)c1>>COc1cccc(C(CC(F)(F)F)c2ccc(C#N)cc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (71.5%) | `sacrificial_zinc` (14.7%) | `ABSENT` (8.3%) | ✓ |
| 阳极 (细类) | 43 | `zinc_plate` | `reticulated_vitreous_carbon` (38.0%) | `carbon_rod` (35.1%) | `graphite_cloth` (9.4%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (94.4%) | `carbon` (4.0%) | `ABSENT` (1.2%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (84.7%) | `platinum_generic` (8.2%) | `carbon_rod` (2.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (94.8%) | `NBu4` (3.5%) | `ABSENT` (0.6%) | ✓ |
| 电解质 anion | 26 | `BF4` | `PF6` (36.9%) | `BF4` (26.3%) | `carboxylate` (10.9%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.7%) | `hydrosilane` (4.5%) | `water` (4.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (87.3%) | `Co_complex` (6.7%) | `Cu_complex` (1.9%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (71.9%) | `ABSENT` (14.8%) | `halogenated_aliphatic` (10.5%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (50%) | `CC(C)=O` (19%) | `FC(F)(F)c1ccccc1` (19%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `BrCCBr` (1%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (99%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #774  yield=71.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #30)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1ccc(Cl)cc1>>N#Cc1ccc(C(CC(F)(F)F)c2ccc(Cl)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (79.8%) | `ABSENT` (11.4%) | `platinum` (5.7%) | ✗ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (87.7%) | `graphite_cloth` (3.6%) | `reticulated_vitreous_carbon` (3.6%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (98.0%) | `carbon` (1.1%) | `ABSENT` (0.7%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (98.2%) | `platinum_generic` (0.9%) | `ABSENT` (0.3%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `ABSENT` (0.7%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (91.1%) | `NBu4` (4.6%) | `NEt4` (4.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (85.3%) | `BF4` (13.4%) | `Cl` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `water` (7.6%) | `ABSENT` (5.6%) | `hf_amine_complex` (5.6%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (12.9%) | `Co_complex` (3.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `halogenated_aliphatic` (46.8%) | `polar_aprotic_nitrile` (41.8%) | `ABSENT` (4.8%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `ClCCl` (57%) | `ClCCCl` (7%) | `O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `O` (43%) | `BrCCBr` (1%) | `CCN(CC)CC.F.F.F` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (99%) | `c1ccncc1` (2%) | `__OTHER__` (1%) | set ✗ / any ✗ |

---

### Reaction #775  yield=88.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #31)

```
O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1.C=Cc1ccc(C(C)(C)C)cc1>>CC(C)(C)c1ccc(C(CC(F)(F)F)c2ccc(C#N)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (63.3%) | `ABSENT` (17.1%) | `sacrificial_zinc` (11.9%) | ✓ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (62.1%) | `reticulated_vitreous_carbon` (11.4%) | `unknown_electrode` (7.9%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (95.7%) | `carbon` (2.5%) | `ABSENT` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (94.6%) | `platinum_generic` (1.9%) | `carbon_felt` (1.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (73.9%) | `NBu4` (22.2%) | `NEt4` (3.1%) | ✓ |
| 电解质 anion | 26 | `Br` | `ABSENT` (70.1%) | `BF4` (20.0%) | `ClO4` (7.3%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.5%) | `ABSENT` (9.0%) | `thiol` (2.3%) | ✓ |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (79.1%) | `Cu_complex` (9.0%) | `Mn_complex` (4.3%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (39.1%) | `halogenated_aliphatic` (37.4%) | `ABSENT` (18.2%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `CC#N` (45%) | `ClCCCl` (6%) | `CC(C)=O` (2%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O=S(=O)(c1ccccc1)C` | `O` (36%) | `__ABSENT__` (1%) | `O=O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #776  yield=81.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_39_7105-7108.json) (反应 idx 在该 JSON 内 = #32)

```
C=Cc1cccc(C)c1.O=S(=O)(c1ccccc1)C(F)(F)F.N#Cc1ccc(C#N)cc1>>Cc1cccc(C(CC(F)(F)F)c2ccc(C#N)cc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_zinc` | `carbon` (80.1%) | `sacrificial_zinc` (12.0%) | `platinum` (5.0%) | ✓ |
| 阳极 (细类) | 43 | `zinc_plate` | `carbon_rod` (37.8%) | `reticulated_vitreous_carbon` (13.1%) | `graphite_cloth` (11.5%) | ✗ |
| 阴极 (材料) | 15 | `carbon` | `platinum` (97.3%) | `carbon` (2.2%) | `ABSENT` (0.2%) | ✓ |
| 阴极 (细类) | 49 | `carbon_cloth` | `platinum_plate` (97.1%) | `platinum_generic` (1.4%) | `carbon_felt` (0.6%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `divided` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (67.7%) | `NEt4` (19.6%) | `ABSENT` (7.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (58.7%) | `ClO4` (19.5%) | `ABSENT` (7.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.8%) | `water` (3.5%) | `hydrosilane` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `polycyclic_arene_cat` | `ABSENT` (96.2%) | `Co_complex` (2.0%) | `Mn_complex` (0.8%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_aprotic_nitrile` (59.4%) | `halogenated_aliphatic` (22.5%) | `ABSENT` (13.4%) | ✗ |
| 溶剂 set | 79 | `CC(=O)N(C)C` | `FC(F)(F)c1ccccc1` (43%) | `CC#N` (17%) | `CCOCC` (11%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=O` (0%) | `BrCCBr` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccc2c(c1)ccc1ccc` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✗ / any ✗ |

---

### Reaction #777  yield=96.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_66_12357-12360.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_66_12357-12360.json) (反应 idx 在该 JSON 内 = #0)

```
c1ccc([Se][Se]c2ccccc2)cc1.O=C(O)CC=Cc1ccccc1>>O=C1C[C@@H]([Se]c2ccccc2)[C@H](c2ccccc2)O1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (95.4%) | `platinum` (4.4%) | `ABSENT` (0.2%) | ✓ |
| 阳极 (细类) | 43 | `platinum_plate` | `graphite_generic` (98.2%) | `graphite_rod` (0.7%) | `graphite_plate` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `carbon` (0.3%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (98.0%) | `platinum_plate` (1.9%) | `graphite_generic` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.2%) | `ABSENT` (0.7%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.3%) | `NH4` (2.4%) | `Li` (2.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `PF6` | `I` (97.2%) | `BF4` (1.3%) | `ClO4` (0.6%) | ✗ |
| 试剂大类 | 103 | `carboxylic_acid` | `ABSENT` (43.1%) | `electrophilic_N_F` (1.8%) | `unparseable_text` (1.8%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.5%) | `ammonium_PTC_organocat` (0.5%) | `ionic_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.1%) | `polar_protic_alcohol` (1.1%) | `cyclic_ether` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O=C(O)C(F)(F)F` | `__ABSENT__` (99%) | `CC(=O)O` (0%) | `O=S([O-])O.[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `N#Cc1c(C#N)c(-n2c3` (0%) | set ✓ / any ✓ |

---

### Reaction #778  yield=60.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #0)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)C(C)(C)CCCOc1cc(C)ccc1C)c1ccccc1>>Cc1ccc(C)c(OCCCC(C)(C)C2=NCC(CP(=O)(c3ccccc3)c3…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.5%) | `platinum` (5.5%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_plate` (83.7%) | `platinum_plate` (7.6%) | `carbon_rod` (2.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (75.9%) | `nickel` (23.9%) | `stainless_steel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (95.3%) | `nickel_generic` (3.8%) | `platinum_generic` (0.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.8%) | `Li` (0.1%) | `K` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.1%) | `ClO4` (0.4%) | `BF4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (19.6%) | `ABSENT` (7.1%) | `aromatic_neutral` (5.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (59.1%) | `pyridine_organocat` (40.2%) | `Mn_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (65.4%) | `halogenated_aliphatic` (32.8%) | `polar_protic_alcohol` (1.0%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `CO` (1%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (38%) | `[Fe+2].c1cc[cH-]c1` (23%) | `[cH]12->[Fe+2]3456` (22%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #779  yield=68.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #1)

```
COc1ccc([PH](=O)c2ccc(OC)cc2)cc1.C=C(CNC(=O)c1ccccc1)c1ccccc1>>COc1ccc(P(=O)(CC2(c3ccccc3)CN=C(c3ccccc3)O2)c2ccc(OC)c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.8%) | `platinum` (5.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (95.5%) | `carbon_plate` (3.4%) | `glassy_carbon` (0.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `nickel` (1.1%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.5%) | `K` (4.0%) | `H` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.3%) | `BF4` (0.3%) | `SO4` (0.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (11.7%) | `ferrocene_mediator` (10.7%) | `aromatic_neutral` (5.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.8%) | `ferrocene_mediator` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (44.8%) | `halogenated_aliphatic` (32.4%) | `polar_protic_alcohol` (16.0%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `ClCCl` (15%) | `O` (14%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (5%) | `O=C([O-])[O-].[Na+` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #780  yield=80.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #2)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1ccc(Cl)cc1Cl)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccc(Cl)cc2Cl)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (50.1%) | `carbon` (49.9%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_plate` | `platinum_plate` (53.6%) | `carbon_plate` (40.6%) | `carbon_rod` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `nickel` (1.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `nickel_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.3%) | `K` (0.9%) | `Li` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.5%) | `BF4` (0.2%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (19.4%) | `ferrocene_mediator` (7.2%) | `carboxylic_acid` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.2%) | `pyridine_organocat` (1.6%) | `organic_neutral_cat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (59.5%) | `halogenated_aliphatic` (29.6%) | `polar_protic_alcohol` (8.9%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `ClCCl` (1%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #781  yield=80.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #3)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1ccc(C)cc1)c1ccccc1>>Cc1ccc(C2=NCC(CP(=O)(c3ccccc3)c3ccccc3)(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (53.6%) | `carbon_plate` (32.0%) | `glassy_carbon` (10.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.1%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (88.2%) | `K` (6.6%) | `H` (3.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.5%) | `BF4` (0.3%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (17.3%) | `ferrocene_mediator` (8.6%) | `alkali_other_salt` (5.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.1%) | `pyridine_organocat` (0.6%) | `ferrocene_mediator` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (82.4%) | `halogenated_aliphatic` (9.1%) | `polar_protic_alcohol` (6.5%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `CO` (7%) | `O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #782  yield=80.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #4)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1cccc(Br)c1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2cccc(Br)c2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_plate` (48.1%) | `glassy_carbon` (30.3%) | `carbon_rod` (18.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.0%) | `K` (14.3%) | `H` (3.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.5%) | `BF4` (0.2%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (20.2%) | `alkali_other_salt` (6.7%) | `ABSENT` (5.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (92.1%) | `pyridine_organocat` (7.0%) | `ferrocene_mediator` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (82.4%) | `polar_protic_alcohol` (11.6%) | `halogenated_aliphatic` (4.5%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `CO` (2%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `[cH]12->[Fe+2]3456` (53%) | `__ABSENT__` (29%) | `[Fe+2].c1cc[cH-]c1` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #783  yield=76.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #5)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.Cc1cccc([PH](=O)c2cccc(C)c2)c1>>Cc1cccc(P(=O)(CC2(c3ccccc3)CN=C(c3ccccc3)O2)c2cccc(C)c2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (76.8%) | `glassy_carbon` (11.8%) | `carbon_plate` (10.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.3%) | `ABSENT` (5.8%) | `K` (4.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.3%) | `BF4` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_other_salt` (15.5%) | `ferrocene_mediator` (12.6%) | `ABSENT` (6.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.7%) | `pyridine_organocat` (0.2%) | `ferrocene_mediator` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (81.9%) | `halogenated_aliphatic` (10.2%) | `polar_protic_alcohol` (3.8%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `CO` (3%) | `ClCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C(O)O.[K]` (75%) | `__ABSENT__` (10%) | `O=C(O)O.[Na]` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #784  yield=79.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #6)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1ccccc1Cl)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2Cl)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `platinum` (1.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_plate` (86.8%) | `glassy_carbon` (8.2%) | `carbon_rod` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.5%) | `nickel` (0.5%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.1%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.5%) | `H` (3.3%) | `K` (2.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.9%) | `BF4` (0.0%) | `Br` (0.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (14.6%) | `ABSENT` (13.9%) | `carboxylic_acid` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.1%) | `pyridine_organocat` (5.3%) | `Mn_complex` (0.2%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (48.1%) | `halogenated_aliphatic` (38.8%) | `polar_protic_alcohol` (12.3%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `CO` (9%) | `ClCCl` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (42%) | `[cH]12->[Fe+2]3456` (27%) | `[Fe+2].c1cc[cH-]c1` (24%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #785  yield=78.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #7)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1cccc(C)c1)c1ccccc1>>Cc1cccc(C2=NCC(CP(=O)(c3ccccc3)c3ccccc3)(c3ccccc3)O2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.4%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (47.0%) | `carbon_plate` (36.3%) | `glassy_carbon` (14.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.0%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.3%) | `K` (2.9%) | `H` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.5%) | `BF4` (0.4%) | `ClO4` (0.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (10.9%) | `ABSENT` (10.9%) | `carboxylic_acid` (7.8%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.5%) | `pyridine_organocat` (0.4%) | `ferrocene_mediator` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (92.5%) | `polar_protic_alcohol` (3.3%) | `halogenated_aliphatic` (3.2%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `CO` (3%) | `ClCCCl` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (70%) | `[cH]12->[Fe+2]3456` (15%) | `CC(=O)[O-].[Na+]` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #786  yield=78.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #8)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1ccccc1)c1ccc(Br)cc1>>O=P(CC1(c2ccc(Br)cc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_plate` (47.0%) | `glassy_carbon` (38.4%) | `carbon_generic` (7.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `nickel` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.6%) | `platinum_generic` (0.4%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (90.2%) | `K` (5.7%) | `H` (1.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.5%) | `Br` (0.3%) | `BF4` (0.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (20.2%) | `ABSENT` (12.2%) | `alkali_other_salt` (5.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.2%) | `pyridine_organocat` (1.7%) | `ferrocene_mediator` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (85.5%) | `polar_protic_alcohol` (12.9%) | `halogenated_aliphatic` (1.0%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `CO` (10%) | `O` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `[cH]12->[Fe+2]3456` (31%) | `__ABSENT__` (30%) | `[Fe+2].c1cc[cH-]c1` (22%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #787  yield=76.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #9)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1ccccc1)c1ccc(Cl)cc1>>O=P(CC1(c2ccc(Cl)cc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_plate` (51.7%) | `glassy_carbon` (26.7%) | `carbon_rod` (12.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (86.2%) | `K` (5.4%) | `H` (4.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.7%) | `BF4` (0.1%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (16.1%) | `ABSENT` (11.0%) | `alkali_other_salt` (6.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (97.6%) | `pyridine_organocat` (2.2%) | `ferrocene_mediator` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (92.8%) | `polar_protic_alcohol` (5.0%) | `halogenated_aliphatic` (1.7%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `O` (3%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (51%) | `[cH]12->[Fe+2]3456` (29%) | `[Fe+2].c1cc[cH-]c1` (7%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #788  yield=75.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #10)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1ccccc1F)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2F)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.8%) | `platinum` (3.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_plate` (98.0%) | `platinum_plate` (1.1%) | `carbon_rod` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.3%) | `H` (1.8%) | `K` (0.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.4%) | `BF4` (0.2%) | `Br` (0.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (31.0%) | `ABSENT` (9.8%) | `metal_oxide_oxidant` (1.6%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (97.5%) | `pyridine_organocat` (2.2%) | `Mn_complex` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (68.2%) | `halogenated_aliphatic` (20.7%) | `polar_protic_alcohol` (10.2%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `CO` (33%) | `O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `[cH]12->[Fe+2]3456` (50%) | `__ABSENT__` (31%) | `[Fe+2].c1cc[cH-]c1` (16%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #789  yield=74.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #11)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1c(C)cc(C)cc1C)c1ccccc1>>Cc1cc(C)c(C2=NCC(CP(=O)(c3ccccc3)c3ccccc3)(c3ccccc3)O2)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (60.8%) | `carbon_plate` (32.7%) | `glassy_carbon` (5.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `stainless_steel` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (75.6%) | `ABSENT` (11.2%) | `K` (8.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.8%) | `BF4` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (19.7%) | `ferrocene_mediator` (6.4%) | `alkali_other_salt` (5.6%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.9%) | `pyridine_organocat` (0.8%) | `organic_neutral_cat` (0.2%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (90.3%) | `polar_protic_alcohol` (6.4%) | `halogenated_aliphatic` (2.8%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `O` (4%) | `CO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #790  yield=74.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #12)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1ccc(CCC)cc1)c1ccccc1>>CCCc1ccc(C2=NCC(CP(=O)(c3ccccc3)c3ccccc3)(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_plate` (76.8%) | `carbon_rod` (17.8%) | `glassy_carbon` (4.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `nickel_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.1%) | `K` (2.8%) | `H` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.6%) | `BF4` (0.2%) | `SO4` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (23.0%) | `ferrocene_mediator` (8.5%) | `metal_oxide_oxidant` (2.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.3%) | `ferrocene_mediator` (0.3%) | `pyridine_organocat` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (78.1%) | `polar_protic_alcohol` (11.6%) | `halogenated_aliphatic` (7.9%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `ClCCCl` (9%) | `CO` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #791  yield=72.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #13)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1cccc2ccccc12)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2cccc3ccccc23)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (1.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_plate` (80.8%) | `carbon_rod` (10.6%) | `glassy_carbon` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.0%) | `K` (2.3%) | `Li` (1.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (98.6%) | `Br` (0.6%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (14.2%) | `ABSENT` (10.5%) | `carboxylic_acid` (4.1%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.1%) | `pyridine_organocat` (1.8%) | `Mn_complex` (0.0%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (90.9%) | `halogenated_aliphatic` (6.2%) | `polar_protic_alcohol` (2.3%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `O` (2%) | `CO` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (63%) | `[cH]12->[Fe+2]3456` (24%) | `[Fe+2].c1cc[cH-]c1` (4%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #792  yield=71.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #14)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1ccc(C#N)cc1)c1ccccc1>>N#Cc1ccc(C2=NCC(CP(=O)(c3ccccc3)c3ccccc3)(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (92.2%) | `carbon_plate` (4.4%) | `glassy_carbon` (1.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.1%) | `ABSENT` (0.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (52.8%) | `K` (28.6%) | `H` (11.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.7%) | `molecular_no_ion` (0.1%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (16.4%) | `ferrocene_mediator` (8.2%) | `alkali_other_salt` (6.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (96.8%) | `pyridine_organocat` (3.0%) | `organic_neutral_cat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (96.1%) | `polar_protic_alcohol` (2.1%) | `halogenated_aliphatic` (1.5%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `CO` (2%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #793  yield=78.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #15)

```
O=[PH](c1ccc(Cl)cc1)c1ccc(Cl)cc1.C=C(CNC(=O)c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccc(Cl)cc1)c1ccc(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.0%) | `platinum` (3.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_plate` (47.9%) | `carbon_rod` (40.2%) | `platinum_plate` (7.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.8%) | `nickel` (1.1%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (87.1%) | `ABSENT` (8.0%) | `H` (2.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (98.8%) | `BF4` (0.4%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (9.7%) | `ABSENT` (8.7%) | `alkali_other_salt` (3.6%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.4%) | `pyridine_organocat` (0.5%) | `ferrocene_mediator` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (52.3%) | `halogenated_aliphatic` (43.3%) | `polar_protic_alcohol` (2.5%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `ClCCl` (8%) | `O` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `[cH]12->[Fe+2]3456` (40%) | `__ABSENT__` (34%) | `CC(=O)[O-].[Na+]` (9%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✗ |

---

### Reaction #794  yield=83.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #16)

```
C=C(CNC(=O)c1ccccc1)c1ccccc1.COc1cccc([PH](=O)c2cccc(OC)c2)c1>>COc1cccc(P(=O)(CC2(c3ccccc3)CN=C(c3ccccc3)O2)c2cccc(OC…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (91.7%) | `glassy_carbon` (5.9%) | `carbon_plate` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `stainless_steel` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.2%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.7%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (55.9%) | `K` (18.7%) | `NBu4` (15.0%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (95.5%) | `ABSENT` (2.9%) | `molecular_no_ion` (0.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `alkali_other_salt` (12.7%) | `ferrocene_mediator` (10.9%) | `ABSENT` (6.2%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.8%) | `pyridine_organocat` (0.1%) | `Mn_complex` (0.0%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (95.2%) | `halogenated_aliphatic` (1.9%) | `polar_protic_alcohol` (1.8%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `CO` (2%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `O=C(O)O.[K]` (82%) | `O=C(O)O.[Na]` (10%) | `[Pt]` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #795  yield=86.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #17)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1ccccc1)c1ccc(C)cc1>>Cc1ccc(C2(CP(=O)(c3ccccc3)c3ccccc3)CN=C(c3ccccc3)O2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (83.0%) | `carbon_plate` (8.9%) | `glassy_carbon` (5.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `nickel` (0.2%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.9%) | `platinum_generic` (0.1%) | `nickel_generic` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (93.5%) | `K` (3.0%) | `H` (1.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.4%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (13.8%) | `ABSENT` (11.8%) | `alkali_other_salt` (7.0%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (97.8%) | `pyridine_organocat` (1.5%) | `ferrocene_mediator` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (71.3%) | `polar_protic_alcohol` (18.8%) | `halogenated_aliphatic` (7.9%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `CO` (9%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (27%) | `[cH]12->[Fe+2]3456` (27%) | `[Fe+2].c1cc[cH-]c1` (11%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #796  yield=85.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #18)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1ccc(Cl)cc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccc(Cl)cc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_plate` (80.0%) | `glassy_carbon` (10.3%) | `carbon_rod` (6.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `nickel` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.5%) | `K` (7.2%) | `H` (4.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.7%) | `Br` (0.1%) | `BF4` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (16.7%) | `ferrocene_mediator` (11.2%) | `alkali_other_salt` (4.0%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.7%) | `pyridine_organocat` (1.1%) | `ferrocene_mediator` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (94.5%) | `halogenated_aliphatic` (2.6%) | `polar_protic_alcohol` (2.5%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `O` (5%) | `CO` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #797  yield=85.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #19)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1ccccc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.2%) | `platinum` (0.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (56.6%) | `carbon_plate` (27.2%) | `glassy_carbon` (15.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.0%) | `ABSENT` (1.0%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.5%) | `K` (6.6%) | `ABSENT` (3.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.2%) | `BF4` (0.5%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (23.7%) | `alkali_other_salt` (7.4%) | `ABSENT` (4.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.8%) | `pyridine_organocat` (0.7%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (56.1%) | `polar_protic_alcohol` (24.9%) | `halogenated_aliphatic` (16.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `CCO` + `CC(C)O` + `CC(C)(C)O` | `CC#N` (100%) | `CO` (6%) | `ClCCCl` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=C([O-])[O-].[K+]` + `Cc1cccc(C)n1` | `[cH]12->[Fe+2]3456` (44%) | `O=C([O-])[O-].[K+]` (33%) | `[Fe+2].c1cc[cH-]c1` (27%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #798  yield=84.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #20)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1ccccc1)c1ccc2ccccc2c1>>O=P(CC1(c2ccc3ccccc3c2)CN=C(c2ccccc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_rod` (56.2%) | `carbon_plate` (39.5%) | `glassy_carbon` (3.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `nickel_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.7%) | `K` (8.4%) | `H` (4.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.8%) | `BF4` (0.1%) | `Br` (0.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ferrocene_mediator` (17.6%) | `ABSENT` (11.0%) | `alkali_other_salt` (2.4%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.7%) | `pyridine_organocat` (0.2%) | `ferrocene_mediator` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (89.7%) | `polar_protic_alcohol` (9.3%) | `halogenated_aliphatic` (0.7%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `CO` (7%) | `O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `[cH]12->[Fe+2]3456` (56%) | `__ABSENT__` (28%) | `[Fe+2].c1cc[cH-]c1` (5%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (3%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #799  yield=82.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #21)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1ccc(Br)cc1)c1ccccc1>>O=P(CC1(c2ccccc2)CN=C(c2ccc(Br)cc2)O1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_plate` (63.1%) | `glassy_carbon` (31.0%) | `carbon_generic` (3.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `nickel` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.7%) | `platinum_generic` (0.3%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (78.1%) | `K` (12.7%) | `H` (6.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.5%) | `Br` (0.4%) | `BF4` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (17.5%) | `ferrocene_mediator` (12.5%) | `alkali_other_salt` (4.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.9%) | `pyridine_organocat` (1.0%) | `ferrocene_mediator` (0.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (92.2%) | `polar_protic_alcohol` (5.0%) | `halogenated_aliphatic` (2.1%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `O` (17%) | `CO` (13%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #800  yield=82.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_76_14717-14720.json) (反应 idx 在该 JSON 内 = #22)

```
O=[PH](c1ccccc1)c1ccccc1.C=C(CNC(=O)c1ccc(C(C)(C)C)cc1)c1ccccc1>>CC(C)(C)c1ccc(C2=NCC(CP(=O)(c3ccccc3)c3ccccc3)(c3ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_plate` | `carbon_plate` (76.2%) | `carbon_rod` (16.8%) | `glassy_carbon` (5.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `nickel` (0.0%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.2%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `K` (44.5%) | `NBu4` (37.7%) | `H` (12.0%) | ✓ |
| 电解质 anion | 26 | `carboxylate` | `carboxylate` (99.6%) | `molecular_no_ion` (0.2%) | `Br` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (14.5%) | `ferrocene_mediator` (9.7%) | `alkali_other_salt` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (99.0%) | `pyridine_organocat` (0.8%) | `organic_neutral_cat` (0.1%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (96.7%) | `polar_protic_alcohol` (1.9%) | `halogenated_aliphatic` (0.6%) | ✓ |
| 溶剂 set | 79 | `CO` + `CC#N` | `CC#N` (100%) | `CO` (19%) | `O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCN(CC)CC` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `CC(=O)[O-].[Na+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #801  yield=35.0%

**Source paper**: [`GreenChem/2024_Green_Chemistry_2024_26_11_6553-6558.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2024_Green_Chemistry_2024_26_11_6553-6558.json) (反应 idx 在该 JSON 内 = #18)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C1Cc2ccccc2C1=O>>O=C1OC(c2ccccc2)(c2ccccc2)CC12Cc1ccccc1C2=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `ABSENT` (98.4%) | `carbon` (1.3%) | `platinum` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (99.6%) | `graphite_generic` (0.3%) | `ABSENT` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (82.1%) | `sacrificial_zinc` (15.8%) | `ABSENT` (1.2%) | ✗ |
| 阴极 (细类) | 49 | `platinum_disk` | `nickel_generic` (99.5%) | `nickel_foam` (0.4%) | `platinum_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (53.4%) | `ABSENT` (46.5%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (99.6%) | `NBu4` (0.2%) | `K` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `molecular_no_ion` | `ClO4` (98.0%) | `PF6` (0.9%) | `molecular_no_ion` (0.6%) | ✓ |
| 试剂大类 | 103 | `pyridine` | `pyridine` (81.4%) | `ABSENT` (2.4%) | `transition_metal_salt_reagent` (0.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Ni_complex` | `ABSENT` (99.4%) | `Fe_complex` (0.3%) | `Ni_complex` (0.2%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (96.4%) | `cyclic_ether` (1.5%) | `polar_protic_alcohol` (1.0%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `__OTHER__` (100%) | `ClCCCl` (100%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `CCOCC.FB(F)F` (100%) | `Cc1cccc(C)n1` (100%) | `__OTHER__` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (100%) | `__ABSENT__` (1%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #802  yield=35.0%

**Source paper**: [`GreenChem/2024_Green_Chemistry_2024_26_11_6553-6558.json`](reactions_by_journal_alkene_ec_audited/GreenChem/2024_Green_Chemistry_2024_26_11_6553-6558.json) (反应 idx 在该 JSON 内 = #18)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C1Cc2ccccc2C1=O>>O=C1OC(c2ccccc2)(c2ccccc2)CC12Cc1ccccc1C2=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `ABSENT` (98.4%) | `carbon` (1.3%) | `platinum` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `carbon_generic` | `unknown_electrode` (99.6%) | `graphite_generic` (0.3%) | `ABSENT` (0.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `nickel` (82.1%) | `sacrificial_zinc` (15.8%) | `ABSENT` (1.2%) | ✗ |
| 阴极 (细类) | 49 | `platinum_disk` | `nickel_generic` (99.5%) | `nickel_foam` (0.4%) | `platinum_generic` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (53.4%) | `ABSENT` (46.5%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (99.6%) | `NBu4` (0.2%) | `K` (0.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ClO4` (98.0%) | `PF6` (0.9%) | `molecular_no_ion` (0.6%) | ✗ |
| 试剂大类 | 103 | `secondary_amine` | `pyridine` (81.4%) | `ABSENT` (2.4%) | `transition_metal_salt_reagent` (0.5%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.4%) | `Fe_complex` (0.3%) | `Ni_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `ketone` (96.4%) | `cyclic_ether` (1.5%) | `polar_protic_alcohol` (1.0%) | ✗ |
| 溶剂 set | 79 | `CC(C)=O` + `__OTHER__` + `ClCCCl` | `CC(C)=O` (100%) | `__OTHER__` (100%) | `ClCCCl` (100%) | set ✓ / any ✓ |
| 试剂 set | 545 | `Cc1cccc(C)n1` + `__OTHER__` + `CCOCC.FB(F)F` | `CCOCC.FB(F)F` (100%) | `Cc1cccc(C)n1` (100%) | `__OTHER__` (100%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Cl][Ni][Cl` | `COCCOC.[Cl][Ni][Cl` (100%) | `__ABSENT__` (1%) | `[Br-].[Br-].[Mn+2]` (0%) | set ✓ / any ✓ |

---

### Reaction #803  yield=51.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_83_16270-16273.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_83_16270-16273.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCCCBr.C=C(C(=O)N(CCO)c1ccccc1)C(F)(F)F>>O=C1N(CCO)c2ccccc2C1(CCC1CCCC1)C(F)(F)F
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.2%) | `sacrificial_magnesium` (1.2%) | `sacrificial_zinc` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (99.9%) | `graphite_generic` (0.0%) | `carbon_felt` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.0%) | `nickel` (6.4%) | `carbon` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (73.4%) | `nickel_foam` (23.8%) | `platinum_plate` (1.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NBu4` (55.9%) | `Li` (42.3%) | `K` (1.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (97.7%) | `PF6` (1.0%) | `BF4` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (17.6%) | `primary_amine` (4.4%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `organic_neutral_cat` | `quinone_oxidant_cat` (77.5%) | `organic_neutral_cat` (9.2%) | `ABSENT` (8.5%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (86.8%) | `cyclic_ether` (4.7%) | `polar_aprotic_amide` (3.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=C([O-])[O-].[Cs+` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1C(=O)c2ccccc2-` | `O=C1c2ccccc2C(=O)c` (74%) | `__ABSENT__` (2%) | `[Fe+2].c1cc[cH-]c1` (2%) | set ✗ / any ✗ |

---

### Reaction #804  yield=71.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_83_16270-16273.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_83_16270-16273.json) (反应 idx 在该 JSON 内 = #1)

```
O=C(NCCBr)OCC1c2ccccc2-c2ccccc21.C=C(C(=O)N(C)c1ccccc1)C(F)(F)F>>CN1C(=O)C(CCCNC(=O)OCC2c3ccccc3-c3ccccc32)(C(F)(F)F)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `reticulated_vitreous_carbon` | `reticulated_vitreous_carbon` (95.4%) | `carbon_felt` (4.4%) | `graphite_generic` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.5%) | `platinum_plate` (3.5%) | `platinum_wire` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `Li` (84.2%) | `NBu4` (15.5%) | `Na` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `molecular_no_ion` | `ClO4` (98.9%) | `BF4` (0.7%) | `molecular_no_ion` (0.2%) | ✓ |
| 试剂大类 | 103 | `silyl_electrophile` | `ABSENT` (32.9%) | `metal_oxide_oxidant` (1.8%) | `tellurium_reagent` (1.8%) | ✗ |
| 催化剂大类 | 49 | `organic_neutral_cat` | `quinone_oxidant_cat` (63.9%) | `ferrocene_mediator` (23.7%) | `ABSENT` (8.4%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (93.1%) | `polar_protic_alcohol` (3.0%) | `cyclic_ether` (2.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `COCCOC` (0%) | `C1CCOC1` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `C[Si](C)(C)[Si](O)` | `__ABSENT__` (100%) | `O=C([O-])[O-].[Na+` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `O=C1C(=O)c2ccccc2-` | `O=C1c2ccccc2C(=O)c` (87%) | `[Fe+2].c1cc[cH-]c1` (10%) | `__ABSENT__` (1%) | set ✗ / any ✗ |

---

### Reaction #805  yield=12.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccccc1.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>BrCC(Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (91.5%) | `carbon` (8.0%) | `sacrificial_magnesium` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (59.4%) | `platinum_generic` (14.9%) | `platinum_foil` (8.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (69.1%) | `carbon` (29.3%) | `sacrificial_aluminum` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (75.2%) | `platinum_generic` (16.5%) | `platinum_wire` (1.3%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (95.1%) | `ABSENT` (4.8%) | `divided` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (96.6%) | `Na` (1.4%) | `molecular_no_ion` (1.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (96.9%) | `molecular_no_ion` (2.2%) | `Br` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `hbr` (41.6%) | `ABSENT` (3.1%) | `sulfonic_acid` (2.9%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (84.2%) | `main_group_lewis_acid` (3.4%) | `pyridine_organocat` (3.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (55.1%) | `aqueous` (34.5%) | `polar_protic_acid` (3.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `C1COCCO1` (97%) | `C[N+](=O)[O-]` (94%) | `CC#N` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `CC[Si](CC)CC` (90%) | `O=O` (77%) | `OB(O)B(O)O` (75%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (93%) | `c1ccncc1` (90%) | `__ABSENT__` (5%) | set ✗ / any ✓ |

---

### Reaction #806  yield=20.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #1)

```
C=Cc1ccc(C(=O)O[C@H]2CC[C@@]3(C)C(=CC[C@@H]4[C@@H]3CC[C@]3(C)C(C(C)=O)CC[C@@H]43)C2)cc1>>CC(=O)C1CC[C@H]2[C@@H]3CC=C4…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (95.8%) | `glassy_carbon` (2.3%) | `reticulated_vitreous_carbon` (1.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (4.4%) | `stainless_steel` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (82.3%) | `platinum_plate` (6.4%) | `platinum_foil` (5.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (55.5%) | `ABSENT` (44.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.8%) | `NEt4` (0.0%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `BF4` (90.6%) | `Br` (7.7%) | `ClO4` (0.6%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (30.1%) | `carboxylic_acid` (6.4%) | `ABSENT` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `Mn_complex` (0.6%) | `brønsted_acid_cat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (71.7%) | `polar_aprotic_nitrile` (13.6%) | `polar_protic_alcohol` (6.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `__ABSENT__` (68%) | `CC#N` (10%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `C[Si](C)(C)N=[N+]=` (81%) | `O.O.O.O.O.O.O.O.O.` (2%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #807  yield=20.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #2)

```
C=Cc1ccc(C(=O)O[C@H]2CC[C@@]3(C)C(=CC[C@@H]4[C@@H]3CC[C@]3(C)C(C(C)=O)CC[C@@H]43)C2)cc1>>CC(=O)C1CC[C@H]2[C@@H]3CC=C4…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.0%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (95.8%) | `glassy_carbon` (2.3%) | `reticulated_vitreous_carbon` (1.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.3%) | `nickel` (4.4%) | `stainless_steel` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (82.3%) | `platinum_plate` (6.4%) | `platinum_foil` (5.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (55.5%) | `ABSENT` (44.5%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.8%) | `NEt4` (0.0%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `BF4` (90.6%) | `Br` (7.7%) | `ClO4` (0.6%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (30.1%) | `carboxylic_acid` (6.4%) | `ABSENT` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `Mn_complex` (0.6%) | `brønsted_acid_cat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (71.7%) | `polar_aprotic_nitrile` (13.6%) | `polar_protic_alcohol` (6.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `__ABSENT__` (68%) | `CC#N` (10%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `C[Si](C)(C)N=[N+]=` (81%) | `O.O.O.O.O.O.O.O.O.` (2%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #808  yield=21.0%

**Source paper**: [`OrgBiomolChem/2021_Organic_Biomolecular_Chemistry_2021_19_31_6892-6896.json`](reactions_by_journal_alkene_ec_audited/OrgBiomolChem/2021_Organic_Biomolecular_Chemistry_2021_19_31_6892-6896.json) (反应 idx 在该 JSON 内 = #19)

```
CO.C=Cc1ccccc1>>COC(CBr)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `glassy_carbon` (76.3%) | `graphite_rod` (17.0%) | `carbon_rod` (4.7%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.8%) | `platinum_generic` (0.2%) | `platinum_foil` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `K` (90.3%) | `NH4` (4.0%) | `NBu4` (1.8%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `Br` (96.3%) | `ABSENT` (1.7%) | `molecular_no_ion` (0.6%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `carboxylic_acid` (35.3%) | `polyhalo_radical_transfer` (4.6%) | `ABSENT` (3.7%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `pyridine_organocat` (0.5%) | `organic_neutral_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (77.9%) | `polar_aprotic_sulfoxide` (12.1%) | `ABSENT` (6.8%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `C[N+](=O)[O-]` (64%) | `CC#N` (53%) | `C1COCCO1` (46%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S([O-])([O-])=S.` | `CC[Si](CC)CC` (91%) | `O=O` (79%) | `OB(O)B(O)O` (72%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (62%) | `c1ccncc1` (53%) | `__ABSENT__` (36%) | set ✗ / any ✓ |

---

### Reaction #809  yield=27.0%

**Source paper**: [`JACS/2017_Journal_of_the_American_Chemical_Society_2017_139_43_15548-15553.json`](reactions_by_journal_alkene_ec_audited/JACS/2017_Journal_of_the_American_Chemical_Society_2017_139_43_15548-15553.json) (反应 idx 在该 JSON 内 = #14)

```
C=Cc1ccccc1>>ClCC(Cl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.4%) | `platinum` (1.1%) | `sacrificial_magnesium` (0.9%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_felt` | `reticulated_vitreous_carbon` (89.3%) | `graphite_generic` (6.9%) | `carbon_generic` (2.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (60.2%) | `carbon` (37.0%) | `ABSENT` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `graphite_rod` | `platinum_foil` (99.1%) | `platinum_generic` (0.5%) | `graphite_generic` (0.2%) | ✗ |
| 池型 | 4 | `ABSENT` | `ABSENT` (56.6%) | `undivided` (43.0%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (41.2%) | `NEt4` (34.1%) | `ABSENT` (18.3%) | ✗ |
| 电解质 anion | 26 | `Br` | `ClO4` (57.5%) | `ABSENT` (17.7%) | `BF4` (11.5%) | ✗ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (52.1%) | `carboxylic_acid` (15.0%) | `inorganic_simple` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `brønsted_acid_cat` (85.6%) | `Mn_complex` (9.1%) | `ABSENT` (4.5%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (89.0%) | `polar_protic_acid` (5.9%) | `ABSENT` (2.6%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (60%) | `CC#N` (37%) | `C[N+](=O)[O-]` (28%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (100%) | `O=O` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (99%) | `__OTHER__` (98%) | `O=S(=O)(O)C(F)(F)F` (1%) | set ✓ / any ✓ |

---

### Reaction #810  yield=30.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #5)

```
CO.C=Cc1ccccc1>>ClC(CBr)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.5%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (71.3%) | `graphite_rod` (24.9%) | `glassy_carbon` (1.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.9%) | `carbon` (2.9%) | `nickel` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (63.2%) | `platinum_foil` (26.4%) | `platinum_generic` (7.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (55.9%) | `NBu4` (15.1%) | `H` (6.9%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (58.3%) | `ABSENT` (27.8%) | `BF4` (4.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (32.2%) | `carboxylic_acid` (16.2%) | `alkali_other_salt` (4.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `pyridine_organocat` (0.4%) | `Mn_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (57.3%) | `polar_aprotic_nitrile` (40.0%) | `halogenated_aliphatic` (1.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (55%) | `CC#N` (27%) | `C1COCCO1` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S([O-])([O-])=S.` | `CC[Si](CC)CC` (96%) | `OB(O)B(O)O` (90%) | `O=O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (73%) | `c1ccncc1` (68%) | `__ABSENT__` (18%) | set ✗ / any ✓ |

---

### Reaction #811  yield=30.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #5)

```
CO.C=Cc1ccccc1>>ClC(CBr)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.5%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (71.3%) | `graphite_rod` (24.9%) | `glassy_carbon` (1.3%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.9%) | `carbon` (2.9%) | `nickel` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (63.2%) | `platinum_foil` (26.4%) | `platinum_generic` (7.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (55.9%) | `NBu4` (15.1%) | `H` (6.9%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (58.3%) | `ABSENT` (27.8%) | `BF4` (4.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (32.2%) | `carboxylic_acid` (16.2%) | `alkali_other_salt` (4.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.7%) | `pyridine_organocat` (0.4%) | `Mn_complex` (0.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (57.3%) | `polar_aprotic_nitrile` (40.0%) | `halogenated_aliphatic` (1.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `__ABSENT__` (55%) | `CC#N` (27%) | `C1COCCO1` (15%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S([O-])([O-])=S.` | `CC[Si](CC)CC` (96%) | `OB(O)B(O)O` (90%) | `O=O` (68%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (73%) | `c1ccncc1` (68%) | `__ABSENT__` (18%) | set ✗ / any ✓ |

---

### Reaction #812  yield=33.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #7)

```
C=Cc1ccc(C(=O)O[C@@H]2C[C@H](C)CC[C@H]2C(C)C)cc1>>CC(C)[C@@H]1CC[C@@H](C)C[C@H]1OC(=O)c1ccc([C@@H](Cl)CBr)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.4%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (98.6%) | `glassy_carbon` (0.9%) | `carbon_rod` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.2%) | `platinum` (22.5%) | `nickel` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (97.5%) | `platinum_plate` (1.4%) | `platinum_generic` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.4%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.3%) | `NEt4` (30.9%) | `H` (15.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (80.5%) | `BF4` (18.1%) | `PF6` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (77.7%) | `carboxylic_acid` (3.9%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `brønsted_acid_cat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (45.0%) | `halogenated_aliphatic` (17.8%) | `polar_aprotic_nitrile` (14.5%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `CCOCC` (57%) | `O` (31%) | `FC(F)(F)c1ccccc1` (29%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `CC[Si](CC)CC` (45%) | `OB(O)B(O)O` (35%) | `__OTHER__` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (87%) | `O=S(=O)([O-])C(F)(` (10%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #813  yield=33.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #8)

```
C=Cc1ccc(C(=O)O[C@@H]2C[C@H](C)CC[C@H]2C(C)C)cc1>>CC(C)[C@@H]1CC[C@@H](C)C[C@H]1OC(=O)c1ccc([C@H](Cl)CBr)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.4%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (98.6%) | `glassy_carbon` (0.9%) | `carbon_rod` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (75.2%) | `platinum` (22.5%) | `nickel` (1.6%) | ✓ |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (97.5%) | `platinum_plate` (1.4%) | `platinum_generic` (0.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.4%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (48.3%) | `NEt4` (30.9%) | `H` (15.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (80.5%) | `BF4` (18.1%) | `PF6` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (77.7%) | `carboxylic_acid` (3.9%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `brønsted_acid_cat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (45.0%) | `halogenated_aliphatic` (17.8%) | `polar_aprotic_nitrile` (14.5%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `CCOCC` (57%) | `O` (31%) | `FC(F)(F)c1ccccc1` (29%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `CC[Si](CC)CC` (45%) | `OB(O)B(O)O` (35%) | `__OTHER__` (27%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (87%) | `O=S(=O)([O-])C(F)(` (10%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #814  yield=60.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #9)

```
C=Cc1ccccc1Cl>>Clc1ccccc1C(Cl)CBr
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.3%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `glassy_carbon` (67.6%) | `graphite_generic` (26.8%) | `platinum_foil` (3.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.9%) | `carbon` (1.7%) | `stainless_steel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (46.9%) | `platinum_plate` (29.5%) | `platinum_foil` (16.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (96.1%) | `ABSENT` (3.7%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.1%) | `H` (37.9%) | `Na` (9.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (93.2%) | `BF4` (5.5%) | `molecular_no_ion` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (64.2%) | `carboxylic_acid` (5.5%) | `bromide_anion` (3.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.6%) | `brønsted_acid_cat` (2.7%) | `Mn_complex` (2.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_acid` (54.9%) | `halogenated_aliphatic` (31.5%) | `polar_aprotic_sulfoxide` (3.8%) | ✓ |
| 溶剂 set | 79 | `CC(=O)O` + `OC(C(F)(F)F)C(F)(F` + `ClCCl` | `CC(=O)O` (100%) | `OC(C(F)(F)F)C(F)(F` (82%) | `ClCCl` (76%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC(=O)O` + `O=S(=O)(O)C(F)(F)F` + `CC(=O)OC(C)=O` + `CN(C)c1ccncc1` | `O=S(=O)(O)C(F)(F)F` (98%) | `CC(=O)OC(C)=O` (95%) | `CN(C)c1ccncc1` (80%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COc1c(I)cc2c(c1I)-` | `COc1c(I)cc2c(c1I)-` (92%) | `__ABSENT__` (11%) | `__OTHER__` (11%) | set ✓ / any ✓ |

---

### Reaction #815  yield=70.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #10)

```
OCC=Cc1ccc(F)cc1>>OC[C@H](Br)[C@H](Cl)c1ccc(F)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (77.0%) | `glassy_carbon` (9.4%) | `graphite_felt` (9.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (83.2%) | `platinum_foil` (15.1%) | `platinum_plate` (1.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `H` (65.9%) | `Li` (25.0%) | `Na` (5.2%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (77.8%) | `molecular_no_ion` (8.7%) | `ClO4` (5.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (71.1%) | `carboxylic_acid` (6.3%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (87.4%) | `brønsted_acid_cat` (12.4%) | `Mn_complex` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (90.5%) | `ABSENT` (3.7%) | `polar_protic_acid` (3.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (99%) | `O` (99%) | `CCOCC` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__OTHER__` (25%) | `CC(=O)O` (20%) | `CC[SiH](CC)CC` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (76%) | `[Cl-].[Cl-].[Mn+2]` (19%) | `O=S(=O)([O-])C(F)(` (3%) | set ✓ / any ✓ |

---

### Reaction #816  yield=70.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #11)

```
COCC=Cc1ccccc1>>COC[C@H](Br)[C@H](Cl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.1%) | `platinum` (9.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (58.1%) | `glassy_carbon` (36.1%) | `carbon_generic` (1.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.5%) | `carbon` (1.1%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (94.5%) | `platinum_plate` (3.8%) | `platinum_foil` (0.8%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.6%) | `divided` (0.2%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (85.1%) | `H` (8.8%) | `NEt4` (2.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (47.6%) | `BF4` (39.1%) | `Cl` (9.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (82.7%) | `carboxylic_acid` (1.5%) | `as_solvent_halogenated_aliphat` (1.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `brønsted_acid_cat` (0.8%) | `Mn_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (49.3%) | `ABSENT` (19.2%) | `polar_protic_acid` (11.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `ClCCl` | `FC(F)(F)c1ccccc1` (86%) | `O` (65%) | `CC(=O)O` (54%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `O=O` (99%) | `__OTHER__` (91%) | `OB(O)B(O)O` (91%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (71%) | `O=S(=O)([O-])C(F)(` (12%) | `[Cl-].[Cl-].[Mn+2]` (7%) | set ✓ / any ✓ |

---

### Reaction #817  yield=80.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #12)

```
OCC=Cc1ccc(Cl)cc1>>OC[C@H](Br)[C@H](Cl)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (56.1%) | `glassy_carbon` (28.8%) | `reticulated_vitreous_carbon` (9.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (47.5%) | `platinum_foil` (46.2%) | `platinum_plate` (6.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `H` (50.5%) | `Na` (23.0%) | `Li` (13.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (80.7%) | `molecular_no_ion` (10.7%) | `BF4` (3.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (53.4%) | `carboxylic_acid` (10.8%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.2%) | `brønsted_acid_cat` (7.6%) | `Mn_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (87.4%) | `polar_protic_alcohol` (4.9%) | `polar_protic_acid` (4.8%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (99%) | `CC(=O)O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `O.O.O.O.O.O.O.O.O.` (22%) | `CC(=O)O` (19%) | `CC[SiH](CC)CC` (12%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (93%) | `O=S(=O)([O-])C(F)(` (4%) | `[Cl-].[Cl-].[Mn+2]` (1%) | set ✓ / any ✓ |

---

### Reaction #818  yield=73.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #13)

```
C=Cc1scnc1C>>Cc1ncsc1C(Cl)CBr
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.0%) | `platinum` (9.9%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `glassy_carbon` (88.3%) | `graphite_generic` (7.0%) | `graphite_rod` (1.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `carbon` (0.5%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (93.0%) | `platinum_generic` (5.6%) | `platinum_foil` (1.2%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `K` (38.5%) | `NBu4` (30.0%) | `Na` (13.0%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (99.1%) | `molecular_no_ion` (0.3%) | `BF4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `carboxylic_acid` (25.5%) | `polyhalo_radical_transfer` (11.3%) | `bromide_anion` (5.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (97.1%) | `organic_neutral_cat` (2.1%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (34.6%) | `polar_aprotic_sulfoxide` (28.0%) | `polar_protic_acid` (25.8%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `O` (96%) | `CC#N` (93%) | `CC(=O)O` (20%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `O=C(O)C(F)(F)F` (33%) | `CC(=O)O` (32%) | `CC(=O)OC(C)=O` (18%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (85%) | `O=S(=O)([O-])C(F)(` (3%) | `CC(=O)NC1CC2(CCCCC` (2%) | set ✓ / any ✓ |

---

### Reaction #819  yield=75.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #14)

```
C=Cc1ccc(-c2ccccc2)cc1>>ClC(CBr)c1ccc(-c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.1%) | `platinum` (1.4%) | `sacrificial_iron` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `glassy_carbon` (71.1%) | `graphite_generic` (22.3%) | `reticulated_vitreous_carbon` (2.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.4%) | `carbon` (5.4%) | `stainless_steel` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (54.1%) | `platinum_plate` (27.8%) | `platinum_generic` (15.9%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (92.0%) | `ABSENT` (7.4%) | `divided` (0.6%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (40.1%) | `H` (36.4%) | `NEt4` (12.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (88.4%) | `BF4` (9.4%) | `molecular_no_ion` (0.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (36.1%) | `carboxylic_acid` (10.6%) | `as_solvent_halogenated_aliphat` (6.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (75.7%) | `brønsted_acid_cat` (14.6%) | `Mn_complex` (7.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_protic_acid` (80.8%) | `ABSENT` (6.7%) | `halogenated_aliphatic` (6.5%) | ✓ |
| 溶剂 set | 79 | `CN(C)C=O` + `O=CO` + `CC(=O)O` + `O` | `CC(=O)O` (98%) | `O=CO` (97%) | `O` (91%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (100%) | `__OTHER__` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `COCCOC.[Br][Ni][Br` | `COCCOC.[Br][Ni][Br` (99%) | `[Cl-].[Cl-].[Mn+2]` (6%) | `O.O.[K+].[K+].[O]=` (5%) | set ✓ / any ✓ |

---

### Reaction #820  yield=78.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #15)

```
C=Cc1ccc(Br)cc1>>ClC(CBr)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.1%) | `platinum` (3.7%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (38.7%) | `reticulated_vitreous_carbon` (23.4%) | `platinum_wire` (15.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.7%) | `carbon` (6.6%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (45.5%) | `platinum_wire` (23.8%) | `platinum_generic` (21.6%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (85.3%) | `ABSENT` (13.6%) | `divided` (1.1%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (52.1%) | `Li` (21.7%) | `NEt4` (13.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (57.5%) | `BF4` (27.8%) | `ClO4` (5.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (27.1%) | `carboxylic_acid` (22.4%) | `n_halo_imide` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (84.9%) | `brønsted_acid_cat` (8.3%) | `Mn_complex` (4.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (36.0%) | `polar_protic_acid` (32.4%) | `halogenated_aliphatic` (15.0%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (64%) | `CC#N` (51%) | `CC(=O)O` (20%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (99%) | `CC[Si](CC)CC` (99%) | `__OTHER__` (98%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Pt]` | `O=S(=O)([O-])C(F)(` (20%) | `c1ccncc1` (16%) | `[Cl-].[Cl-].[Mn+2]` (11%) | set ✗ / any ✗ |

---

### Reaction #821  yield=72.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #16)

```
C=Cc1ccc(C(=O)OC)cc1.ClC(Cl)(Cl)C(Cl)(Cl)Cl.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>COC(=O)c1ccc(C(Cl)CBr)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (88.0%) | `platinum` (11.7%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (94.7%) | `carbon_felt` (2.5%) | `platinum_plate` (1.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (83.3%) | `carbon` (15.9%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (27.2%) | `platinum_generic` (26.0%) | `graphite_generic` (25.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.0%) | `ABSENT` (3.9%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (74.1%) | `NBu4` (17.3%) | `Li` (5.0%) | ✓ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (50.2%) | `Br` (46.3%) | `OTs` (0.7%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (15.0%) | `ABSENT` (5.7%) | `alkali_other_salt` (3.6%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (29.3%) | `ABSENT` (25.1%) | `brønsted_acid_cat` (11.3%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (55.2%) | `ABSENT` (29.5%) | `cyclic_ether` (5.8%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (68%) | `C1CCOC1` (1%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (98%) | `O.O.O.[Li+].[O-][C` (4%) | `CC[Si](CC)CC` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `O=S(=O)(O)C(F)(F)F` (28%) | `c1ccncc1` (14%) | `__OTHER__` (9%) | set ✗ / any ✗ |

---

### Reaction #822  yield=74.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #17)

```
C=Cc1ccc(OC(C)=O)cc1>>CC(=O)Oc1ccc(C(Cl)CBr)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (94.7%) | `glassy_carbon` (2.9%) | `carbon_rod` (1.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.5%) | `carbon` (11.9%) | `stainless_steel` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `graphite_generic` (41.4%) | `platinum_plate` (36.9%) | `platinum_foil` (11.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (29.7%) | `NEt4` (22.1%) | `H` (20.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (89.1%) | `BF4` (8.0%) | `molecular_no_ion` (2.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (78.0%) | `carboxylic_acid` (4.1%) | `n_halo_imide` (1.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `Mn_complex` (0.8%) | `brønsted_acid_cat` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (31.8%) | `polar_aprotic_nitrile` (30.9%) | `halogenated_aliphatic` (22.5%) | ✓ |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `FC(F)(F)c1ccccc1` (96%) | `CCOCC` (95%) | `O` (13%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (98%) | `__OTHER__` (97%) | `CC[Si](CC)CC` (85%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (38%) | `[Cl][Mn][Cl]` (29%) | `[Cl-].[Cl-].[Mn+2]` (23%) | set ✓ / any ✓ |

---

### Reaction #823  yield=79.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #18)

```
OCC=Cc1ccccc1>>OC[C@H](Br)[C@H](Cl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.7%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (96.7%) | `glassy_carbon` (1.8%) | `reticulated_vitreous_carbon` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (75.4%) | `platinum_generic` (24.2%) | `platinum_plate` (0.3%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `H` (77.1%) | `Na` (12.3%) | `Li` (6.2%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (77.2%) | `molecular_no_ion` (17.2%) | `ClO4` (2.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (71.0%) | `carboxylic_acid` (7.7%) | `hbr` (4.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (82.6%) | `brønsted_acid_cat` (16.5%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (90.8%) | `polar_protic_alcohol` (2.6%) | `polar_protic_acid` (2.4%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `O` (99%) | `CC#N` (95%) | `FC(F)(F)c1ccccc1` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `CC(=O)O` (65%) | `CC[SiH](CC)CC` (40%) | `OB(O)B(O)O` (18%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (41%) | `O=S(=O)([O-])C(F)(` (34%) | `O=S(=O)(O)C(F)(F)F` (16%) | set ✓ / any ✓ |

---

### Reaction #824  yield=72.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #19)

```
Cc1ccc(C=CCO)cc1>>Cc1ccc([C@@H](Cl)[C@@H](Br)CO)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.7%) | `platinum` (1.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (77.6%) | `glassy_carbon` (13.7%) | `platinum_foil` (4.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (65.8%) | `platinum_generic` (29.4%) | `platinum_plate` (4.4%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.9%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `H` (77.4%) | `Li` (8.7%) | `Na` (8.0%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (87.3%) | `molecular_no_ion` (7.6%) | `BF4` (2.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (67.3%) | `carboxylic_acid` (6.7%) | `as_solvent_halogenated_aliphat` (1.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.3%) | `brønsted_acid_cat` (1.4%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (89.8%) | `polar_protic_alcohol` (5.3%) | `ABSENT` (2.5%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (98%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `CC[SiH](CC)CC` (80%) | `CC(=O)O` (40%) | `__OTHER__` (23%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (86%) | `[Pt]` (7%) | `O=S(=O)([O-])C(F)(` (4%) | set ✓ / any ✓ |

---

### Reaction #825  yield=87.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #20)

```
C=COC(=O)CCCCCCCCCCC>>CCCCCCCCCCCC(=O)OC(Cl)CBr
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (77.3%) | `graphite_rod` (7.7%) | `glassy_carbon` (6.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (82.0%) | `carbon` (17.3%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (95.6%) | `platinum_plate` (1.6%) | `graphite_generic` (1.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (95.4%) | `ABSENT` (4.0%) | `divided` (0.6%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (57.1%) | `H` (20.5%) | `NEt4` (19.5%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (42.4%) | `BF4` (36.7%) | `ClO4` (17.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (64.1%) | `carboxylic_acid` (7.6%) | `transition_metal_salt_reagent` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (61.8%) | `brønsted_acid_cat` (37.0%) | `Mn_complex` (0.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (51.5%) | `ABSENT` (42.9%) | `polar_protic_acid` (4.0%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (97%) | `O` (32%) | `CCOCC` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `OC(C(F)(F)F)C(F)(F` (48%) | `BrCCBr` (19%) | `CC(=O)O` (18%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (56%) | `O=S(=O)([O-])C(F)(` (23%) | `CC(=O)NC1CC2(CCCCC` (10%) | set ✓ / any ✓ |

---

### Reaction #826  yield=86.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #21)

```
C=Cc1ccc(C)cc1>>Cc1ccc(C(Cl)CBr)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.0%) | `platinum` (2.8%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `glassy_carbon` (59.5%) | `graphite_generic` (18.4%) | `reticulated_vitreous_carbon` (8.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.7%) | `carbon` (9.4%) | `nickel` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (39.0%) | `platinum_plate` (33.0%) | `platinum_generic` (17.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (70.4%) | `ABSENT` (25.9%) | `divided` (3.7%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `H` (41.3%) | `NEt4` (25.0%) | `NBu4` (13.9%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (76.7%) | `BF4` (18.5%) | `molecular_no_ion` (1.5%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (51.8%) | `carboxylic_acid` (15.7%) | `inorganic_simple` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.8%) | `brønsted_acid_cat` (4.1%) | `Mn_complex` (1.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (50.5%) | `halogenated_aliphatic` (16.2%) | `polar_aprotic_nitrile` (14.1%) | ✓ |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (94%) | `CC#N` (59%) | `FC(F)(F)c1ccccc1` (15%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[SiH](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `OB(O)B(O)O` (99%) | `__OTHER__` (98%) | `O=O` (95%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Pt]` | `[Pt]` (29%) | `[Cl-].[Cl-].[Mn+2]` (26%) | `O=S(=O)([O-])C(F)(` (23%) | set ✓ / any ✓ |

---

### Reaction #827  yield=85.0%

**Source paper**: [`China/China_CN119061410_A_2024-12-03.json`](reactions_by_journal_alkene_ec_audited/China/China_CN119061410_A_2024-12-03.json) (反应 idx 在该 JSON 内 = #3)

```
C=Cc1ccccc1>>ClC(CBr)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `platinum` (1.5%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (54.4%) | `glassy_carbon` (29.8%) | `reticulated_vitreous_carbon` (8.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (86.0%) | `carbon` (12.5%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_foil` (76.1%) | `platinum_plate` (9.5%) | `platinum_generic` (8.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (53.8%) | `ABSENT` (46.0%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (25.3%) | `NBu4` (18.6%) | `ABSENT` (14.7%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (78.5%) | `BF4` (9.6%) | `ABSENT` (4.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (60.8%) | `carboxylic_acid` (15.3%) | `inorganic_simple` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.1%) | `Mn_complex` (2.0%) | `brønsted_acid_cat` (1.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (55.1%) | `ABSENT` (17.5%) | `polar_protic_acid` (12.3%) | ✗ |
| 溶剂 set | 79 | `C[N+](=O)[O-]` + `C1COCCO1` | `C1COCCO1` (74%) | `O` (62%) | `C[N+](=O)[O-]` (53%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (100%) | `O=O` (99%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (99%) | `__OTHER__` (96%) | `O=S(=O)([O-])C(F)(` (3%) | set ✓ / any ✓ |

---

### Reaction #828  yield=84.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #23)

```
ClCC=Cc1ccccc1>>ClC[C@H](Br)[C@H](Cl)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (88.5%) | `glassy_carbon` (5.8%) | `graphite_felt` (3.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.0%) | `carbon` (0.8%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (89.7%) | `platinum_foil` (5.2%) | `platinum_plate` (3.9%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (64.4%) | `NBu4` (19.5%) | `NEt4` (8.9%) | ✓ |
| 电解质 anion | 26 | `Br` | `BF4` (57.2%) | `ABSENT` (25.7%) | `Br` (15.0%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (86.6%) | `n_halo_imide` (2.6%) | `carboxylic_acid` (1.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (96.1%) | `brønsted_acid_cat` (2.4%) | `Mn_complex` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (55.0%) | `ABSENT` (20.8%) | `halogenated_aliphatic` (18.1%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `O` (97%) | `CC#N` (88%) | `FC(F)(F)c1ccccc1` (8%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `O=O` (55%) | `OB(O)B(O)O` (33%) | `__OTHER__` (23%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (80%) | `O=S(=O)([O-])C(F)(` (13%) | `[Cl][Mn][Cl]` (1%) | set ✓ / any ✓ |

---

### Reaction #829  yield=88.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #24)

```
OCC=Cc1cccc(F)c1>>OC[C@H](Br)[C@H](Cl)c1cccc(F)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.9%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (94.8%) | `reticulated_vitreous_carbon` (2.2%) | `glassy_carbon` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (72.9%) | `platinum_foil` (26.4%) | `platinum_plate` (0.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (39.2%) | `Li` (22.2%) | `H` (13.3%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (78.0%) | `molecular_no_ion` (12.3%) | `ClO4` (3.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (42.4%) | `carboxylic_acid` (11.2%) | `hbr` (7.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.5%) | `brønsted_acid_cat` (6.0%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (96.6%) | `polar_protic_acid` (1.3%) | `aqueous` (0.9%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `O` (100%) | `CC#N` (97%) | `CC(C)=O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `CC(=O)O` (66%) | `O=C(O)C(F)(F)F` (18%) | `[Cl-].[Cl-].[Mg+2]` (18%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (91%) | `O=S(=O)([O-])C(F)(` (4%) | `__OTHER__` (2%) | set ✓ / any ✓ |

---

### Reaction #830  yield=88.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #25)

```
OCC=Cc1ccc(Br)cc1>>OC[C@H](Br)[C@H](Cl)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.4%) | `platinum` (1.6%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (40.7%) | `reticulated_vitreous_carbon` (34.2%) | `glassy_carbon` (7.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_foil` (54.0%) | `platinum_generic` (37.3%) | `platinum_wire` (7.5%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (82.1%) | `NBu4` (9.8%) | `H` (4.4%) | ✓ |
| 电解质 anion | 26 | `Br` | `Br` (47.7%) | `ClO4` (23.8%) | `molecular_no_ion` (19.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `carboxylic_acid` (23.6%) | `polyhalo_radical_transfer` (17.3%) | `ABSENT` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (95.7%) | `brønsted_acid_cat` (3.9%) | `Mn_complex` (0.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (86.9%) | `polar_protic_acid` (7.0%) | `polar_protic_alcohol` (3.8%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `O` (99%) | `CC#N` (99%) | `CC(=O)O` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `CC(=O)O` (18%) | `[Br-].[Li+]` (15%) | `[Cl-].[Cl-].[Mg+2]` (10%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Pt]` (1%) | `O=S(=O)([O-])C(F)(` (1%) | set ✓ / any ✓ |

---

### Reaction #831  yield=85.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #26)

```
OCC=Cc1ccccc1Br>>OC[C@H](Br)[C@H](Cl)c1ccccc1Br
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.3%) | `platinum` (0.6%) | `sacrificial_zinc` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (64.4%) | `reticulated_vitreous_carbon` (23.3%) | `zinc_plate` (3.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (83.5%) | `platinum_foil` (13.3%) | `platinum_plate` (2.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Li` (94.9%) | `Na` (2.2%) | `H` (1.6%) | ✗ |
| 电解质 anion | 26 | `Br` | `molecular_no_ion` (41.3%) | `ClO4` (35.0%) | `Br` (14.8%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (13.7%) | `carboxylic_acid` (13.5%) | `polyhalo_radical_transfer` (5.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.3%) | `brønsted_acid_cat` (8.5%) | `Mn_complex` (0.9%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (57.4%) | `polar_protic_acid` (36.5%) | `ABSENT` (4.3%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (96%) | `O` (85%) | `CCOCC` (5%) | set ✗ / any ✗ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `__OTHER__` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `O=S(=O)(O)C(F)(F)F` (1%) | `[Cl][Mn][Cl]` (1%) | set ✓ / any ✓ |

---

### Reaction #832  yield=82.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #27)

```
C=Cc1cccc(Cl)c1.CCCC[N+](CCCC)(CCCC)CCCC.[Br-]>>Clc1cccc(C(Cl)CBr)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (53.7%) | `platinum` (46.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (79.7%) | `platinum_generic` (8.7%) | `platinum_plate` (6.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.1%) | `carbon` (4.7%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.0%) | `platinum_plate` (2.8%) | `platinum_foil` (0.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (85.5%) | `ABSENT` (9.6%) | `Na` (2.0%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `Br` (33.1%) | `molecular_no_ion` (16.9%) | `ABSENT` (16.7%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `ABSENT` (6.8%) | `o2_oxidant` (6.0%) | `alkali_other_salt` (3.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (42.4%) | `ABSENT` (39.5%) | `organic_neutral_cat` (8.6%) | ✓ |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (47.1%) | `halogenated_aliphatic` (46.2%) | `cyclic_ether` (2.3%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `CC#N` (94%) | `ClCCl` (1%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `__ABSENT__` (99%) | `O=S([O-])([O-])=S.` (0%) | `O=C([O-])[O-].[K+]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__OTHER__` (29%) | `O=S(=O)(O)C(F)(F)F` (6%) | `c1ccncc1` (3%) | set ✗ / any ✗ |

---

### Reaction #833  yield=82.0%

**Source paper**: [`ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json`](reactions_by_journal_alkene_ec_audited/ChemCommun/2025_Chemical_Communications_Cambridge_United_Kingdom_2025_61_84_16456-16459.json) (反应 idx 在该 JSON 内 = #28)

```
CC(=O)OCC=Cc1ccccc1>>CC(=O)OC[C@H](Br)[C@H](Cl)c1ccccc1.CC(=O)OC[C@H](Cl)[C@H](Br)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.3%) | `platinum` (1.5%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (97.4%) | `glassy_carbon` (1.8%) | `carbon_generic` (0.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.1%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.4%) | `platinum_plate` (0.5%) | `platinum_foil` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (74.8%) | `NEt4` (10.2%) | `H` (9.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (88.5%) | `BF4` (9.1%) | `ClO4` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (48.6%) | `transition_metal_salt_reagent` (4.5%) | `n_halo_imide` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (93.5%) | `brønsted_acid_cat` (6.4%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `halogenated_aliphatic` (97.9%) | `polar_protic_acid` (0.9%) | `polar_aprotic_nitrile` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CCOCC` + `FC(F)(F)c1ccccc1` | `FC(F)(F)c1ccccc1` (82%) | `CC(=O)O` (62%) | `O` (40%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CC[SiH](CC)CC` + `O=O` + `__OTHER__` + `OB(O)B(O)O` | `O=O` (81%) | `__OTHER__` (73%) | `OB(O)B(O)O` (54%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (87%) | `O=S(=O)([O-])C(F)(` (10%) | `COC(=O)CC[C@@H]1C2` (1%) | set ✓ / any ✓ |

---

### Reaction #834  yield=93.0%

**Source paper**: [`China/China_CN119061410_A_2024-12-03.json`](reactions_by_journal_alkene_ec_audited/China/China_CN119061410_A_2024-12-03.json) (反应 idx 在该 JSON 内 = #5)

```
OCC=Cc1cccc(Cl)c1>>OC[C@H](Br)[C@H](Cl)c1cccc(Cl)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (1.0%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_generic` (98.4%) | `glassy_carbon` (0.7%) | `platinum_foil` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `nickel` (0.2%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (57.2%) | `platinum_foil` (42.4%) | `platinum_plate` (0.3%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `Na` (62.4%) | `H` (13.0%) | `ABSENT` (12.7%) | ✗ |
| 电解质 anion | 26 | `Br` | `Br` (76.8%) | `molecular_no_ion` (15.3%) | `ABSENT` (4.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (52.2%) | `hbr` (12.8%) | `carboxylic_acid` (4.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `brønsted_acid_cat` (0.8%) | `Mn_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (87.8%) | `polar_protic_alcohol` (3.1%) | `polar_protic_acid` (2.6%) | ✗ |
| 溶剂 set | 79 | `ClCCl` | `O` (99%) | `CC#N` (98%) | `ClCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `CC(=O)O` (30%) | `O=C(O)C(F)(F)F` (23%) | `O=S([O-])([O-])=S.` (15%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (97%) | `O=S(=O)([O-])C(F)(` (2%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #835  yield=93.0%

**Source paper**: [`China/China_CN119061410_A_2024-12-03.json`](reactions_by_journal_alkene_ec_audited/China/China_CN119061410_A_2024-12-03.json) (反应 idx 在该 JSON 内 = #6)

```
C=COC(=O)c1ccccc1>>O=C(OC(Cl)CBr)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_generic` | `graphite_generic` (97.3%) | `glassy_carbon` (1.1%) | `graphite_felt` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `carbon` (78.9%) | `platinum` (20.7%) | `nickel` (0.3%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `graphite_generic` (97.8%) | `platinum_plate` (0.7%) | `platinum_foil` (0.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NEt4` (71.8%) | `ABSENT` (9.1%) | `H` (7.2%) | ✗ |
| 电解质 anion | 26 | `Br` | `BF4` (87.1%) | `Br` (8.6%) | `ABSENT` (3.1%) | ✓ |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (91.9%) | `n_halo_imide` (1.7%) | `carboxylic_acid` (0.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Mn_complex` (0.1%) | `brønsted_acid_cat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `ABSENT` (98.0%) | `polar_aprotic_nitrile` (1.1%) | `halogenated_aliphatic` (0.5%) | ✓ |
| 溶剂 set | 79 | `ClCCl` | `O` (52%) | `ClCCl` (29%) | `FC(F)(F)c1ccccc1` (11%) | set ✗ / any ✓ |
| 试剂 set | 545 | `ClC(Cl)(Cl)C(Cl)(C` | `ClC(Cl)(Cl)C(Cl)(C` (35%) | `Cc1ccc(I)cc1` (31%) | `O=S(=O)(O)C(F)(F)F` (19%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (88%) | `[Cl][Mn][Cl]` (8%) | `O=S(=O)([O-])C(F)(` (2%) | set ✓ / any ✓ |

---

### Reaction #836  yield=93.0%

**Source paper**: [`China/China_CN119061410_A_2024-12-03.json`](reactions_by_journal_alkene_ec_audited/China/China_CN119061410_A_2024-12-03.json) (反应 idx 在该 JSON 内 = #7)

```
C=Cc1ccc(Cl)cc1>>Clc1ccc(C(Cl)CBr)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `glassy_carbon` (72.9%) | `graphite_generic` (12.6%) | `reticulated_vitreous_carbon` (11.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.9%) | `carbon` (8.6%) | `stainless_steel` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (56.7%) | `platinum_foil` (29.8%) | `platinum_generic` (6.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (53.0%) | `ABSENT` (46.6%) | `divided` (0.4%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (43.2%) | `ABSENT` (25.5%) | `Na` (12.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (75.3%) | `BF4` (16.7%) | `ABSENT` (5.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `polyhalo_radical_transfer` | `polyhalo_radical_transfer` (55.6%) | `carboxylic_acid` (11.3%) | `inorganic_simple` (3.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (92.1%) | `Mn_complex` (5.4%) | `brønsted_acid_cat` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `halogenated_aliphatic` | `polar_aprotic_nitrile` (33.0%) | `ABSENT` (19.6%) | `polar_aprotic_sulfoxide` (15.4%) | ✗ |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (96%) | `CC#N` (93%) | `FC(F)(F)c1ccccc1` (6%) | set ✓ / any ✓ |
| 试剂 set | 545 | `CC[Si](CC)CC` + `O=O` + `OB(O)B(O)O` + `O` | `OB(O)B(O)O` (100%) | `CC[Si](CC)CC` (99%) | `O=O` (92%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `c1ccncc1` + `__OTHER__` | `c1ccncc1` (96%) | `__OTHER__` (86%) | `[Cl-].[Cl-].[Mn+2]` (10%) | set ✓ / any ✓ |

---

### Reaction #837  yield=79.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #838  yield=59.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #839  yield=57.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #840  yield=66.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #841  yield=72.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #842  yield=16.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #843  yield=73.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #844  yield=52.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #845  yield=80.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #846  yield=22.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #847  yield=45.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #848  yield=20.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #849  yield=16.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #850  yield=64.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #851  yield=15.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #852  yield=53.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #853  yield=25.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #854  yield=19.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #855  yield=20.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #856  yield=10.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #857  yield=0.5%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #858  yield=18.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #859  yield=15.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #860  yield=0.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #861  yield=41.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #862  yield=50.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `ketone` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #863  yield=34.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #864  yield=52.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #865  yield=58.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #866  yield=47.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `ketone` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #867  yield=0.5%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #868  yield=0.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #869  yield=0.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #870  yield=46.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #871  yield=80.0%

**Source paper**: [`ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/10.26434_chemrxiv-2025-8zr6h_si2_p25_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CC(=NNc1ccccn1)c1ccc(C)cc1.C1=Cc2cccc3cccc1c23>>CC1(N=Nc2ccccn2)c2ccc(C)cc2C2([H])c3cccc4cccc(c34)C12[H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `ABSENT` | `carbon_felt` (47.6%) | `graphite_generic` (33.7%) | `graphite_rod` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✗ |
| 阴极 (细类) | 49 | `ABSENT` | `platinum_plate` (97.6%) | `platinum_generic` (2.4%) | `platinum_wire` (0.0%) | ✗ |
| 池型 | 4 | `ABSENT` | `undivided` (99.5%) | `divided` (0.4%) | `ABSENT` (0.1%) | ✓ |
| 电解质 cation | 23 | `ABSENT` | `Na` (45.6%) | `ABSENT` (26.6%) | `NBu4` (13.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `molecular_no_ion` (65.2%) | `ABSENT` (11.0%) | `Br` (10.5%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (18.2%) | `alkali_other_salt` (3.0%) | `metal_oxide_oxidant` (2.2%) | ✗ |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `brønsted_acid_cat` (3.0%) | `triarylamine_radical_cat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (1.1%) | `aqueous` (0.0%) | ✗ |
| 溶剂 set | 79 | `CCO` + `Cc1ccccc1` | `CC#N` (100%) | `O` (37%) | `[H+].[OH-]` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CC(C)(C)C(=O)[O-].` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `__OTHER__` (0%) | `[Pt]` (0%) | set ✗ / any ✗ |

---

### Reaction #872  yield=40.0%

**Source paper**: [`ChemRxiv/2025_ChemRxiv_2025_1-11.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/2025_ChemRxiv_2025_1-11.json) (反应 idx 在该 JSON 内 = #0)

```
C=C/C=C\c1ccccc1.COc1ccc(/C(C)=N/Nc2ccccn2)cc1>>C=C1c2cc(OC)ccc2[C@@](C)(/N=N/c2ccccn2)[C@H]1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (37.1%) | `graphite_rod` (30.1%) | `graphite_generic` (28.3%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.5%) | `platinum_generic` (2.9%) | `platinum_wire` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (88.0%) | `divided` (11.7%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Na` | `Na` (59.1%) | `ABSENT` (15.7%) | `K` (11.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (73.7%) | `Br` (11.2%) | `ABSENT` (6.1%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (28.6%) | `alkali_other_salt` (2.3%) | `metal_oxide_oxidant` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (88.4%) | `organic_neutral_cat` (3.7%) | `Pt_complex` (3.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (97.7%) | `ABSENT` (1.7%) | `polar_aprotic_sulfoxide` (0.2%) | ✗ |
| 溶剂 set | 79 | `CCO` + `CC(C)=O` | `CC#N` (97%) | `O` (39%) | `ClCCl` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C(O)C(F)(F)F` (0%) | `CCN(CC)CC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` | `__ABSENT__` (100%) | `[Pt]` (0%) | `O=S(=O)(O)C(F)(F)F` (0%) | set ✗ / any ✗ |

---

### Reaction #873  yield=50.0%

**Source paper**: [`ChemRxiv/2025_ChemRxiv_2025_1-11.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/2025_ChemRxiv_2025_1-11.json) (反应 idx 在该 JSON 内 = #1)

```
C=C/C=C\c1ccccc1.C/C(=N\Nc1ccccn1)c1ccc(C)cc1>>C=C1c2cc(C)ccc2[C@@](C)(/N=N/c2ccccn2)[C@H]1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.4%) | `platinum` (0.9%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_felt` (36.9%) | `graphite_rod` (30.6%) | `graphite_generic` (14.9%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `nickel` (0.2%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (98.0%) | `platinum_generic` (1.7%) | `platinum_wire` (0.1%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (70.2%) | `divided` (29.5%) | `ABSENT` (0.3%) | ✓ |
| 电解质 cation | 23 | `Na` | `Na` (81.5%) | `K` (12.3%) | `ABSENT` (1.6%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `molecular_no_ion` (42.5%) | `I` (32.3%) | `Br` (20.9%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.6%) | `carboxylic_acid` (3.9%) | `metal_oxide_oxidant` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (72.4%) | `Pt_complex` (12.4%) | `ionic_organocat` (4.8%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (82.9%) | `ABSENT` (5.9%) | `cyclic_ether` (3.5%) | ✗ |
| 溶剂 set | 79 | `CCO` + `CC(C)=O` | `CC#N` (78%) | `O` (43%) | `ClCCl` (16%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CC(=O)O` (1%) | `CCN(CC)CC` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)O.[Co]` + `__OTHER__` | `__ABSENT__` (99%) | `[Pt]` (0%) | `[I-].[Li+]` (0%) | set ✗ / any ✗ |

---

### Reaction #874  yield=51.0%

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

### Reaction #875  yield=52.0%

**Source paper**: [`ChemRxiv/2025_ChemRxiv_2025_1-11.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/2025_ChemRxiv_2025_1-11.json) (反应 idx 在该 JSON 内 = #3)

```
C=C/C=C\c1ccccc1.CCC/C(=N\Nc1ccccn1)c1ccc(C)cc1>>C=C1c2cc(C)ccc2[C@@](CCC)(/N=N/c2ccccn2)[C@H]1c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `sacrificial_zinc` (0.0%) | `platinum` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_rod` (96.5%) | `graphite_generic` (1.8%) | `carbon_felt` (1.4%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `nickel` (0.5%) | `carbon` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (89.2%) | `platinum_generic` (10.1%) | `nickel_plate` (0.5%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (96.6%) | `ABSENT` (3.0%) | `divided` (0.4%) | ✓ |
| 电解质 cation | 23 | `Na` | `Na` (61.8%) | `ABSENT` (17.7%) | `NBu4` (10.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ABSENT` (25.8%) | `I` (25.3%) | `molecular_no_ion` (20.2%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (27.3%) | `as_solvent_polar_aprotic_nitri` (2.3%) | `metal_oxide_oxidant` (2.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Co_complex` | `ABSENT` (91.9%) | `organic_neutral_cat` (3.0%) | `ionic_organocat` (1.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (93.7%) | `cyclic_ether` (3.3%) | `polar_aprotic_sulfoxide` (1.7%) | ✗ |
| 溶剂 set | 79 | `CCO` + `CC(C)=O` | `CC#N` (95%) | `O` (60%) | `ClCCl` (6%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `CC(=O)[O-].CC(=O)[` + `__OTHER__` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `O=C1OC2(c3ccccc31)` (0%) | set ✗ / any ✗ |

---

### Reaction #876  yield=69.0%

**Source paper**: [`ChemRxiv/2025_ChemRxiv_2025_1-20.json`](reactions_by_journal_alkene_ec_audited/ChemRxiv/2025_ChemRxiv_2025_1-20.json) (反应 idx 在该 JSON 内 = #0)

```
C=Cc1ccc(Cl)cc1.CC1(C)CCCC(C)(C)N1[O]>>CC1(C)CCCC(C)(C)N1OC(CN=[N+]=[N-])c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `ABSENT` (0.6%) | `sacrificial_zinc` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (99.7%) | `graphite_plate` (0.1%) | `reticulated_vitreous_carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (91.8%) | `ABSENT` (7.8%) | `carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_foil` | `platinum_foil` (100.0%) | `ABSENT` (0.0%) | `platinum_plate` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `ABSENT` (77.1%) | `undivided` (22.9%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `Li` | `Li` (99.5%) | `Na` (0.3%) | `NBu4` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `molecular_no_ion` | `ClO4` (64.7%) | `molecular_no_ion` (35.2%) | `ABSENT` (0.0%) | ✓ |
| 试剂大类 | 103 | `azide_source` | `azide_source` (93.7%) | `alkali_other_salt` (0.3%) | `carboxylic_acid` (0.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `Pt_complex` (99.8%) | `Mn_complex` (0.1%) | `ABSENT` (0.1%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.0%) | `halogenated_aliphatic` (0.7%) | `acyclic_ether` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` + `O` | `O` (100%) | `CC#N` (100%) | `ClC(Cl)Cl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[N-]=[N+]=[N-].[Na` | `[N-]=[N+]=[N-].[Na` (94%) | `[N-]=[N+]=[N][Na]` (5%) | `C[Si](C)(C)N=[N+]=` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Pt]` + `__OTHER__` | `[Pt]` (100%) | `__OTHER__` (100%) | `[Fe+2].c1ccc2c(c1)` (1%) | set ✓ / any ✓ |

---

### Reaction #877  yield=67.0%

**Source paper**: [`ChemSci/2025_Chemical_Science_2025_16_15_6317-6324.json`](reactions_by_journal_alkene_ec_audited/ChemSci/2025_Chemical_Science_2025_16_15_6317-6324.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCOC1OCCC1Br.C=C(COC(=O)OCC)c1ccc(OC)cc1>>C=C(CCC1COC2OCCC12)c1ccc(OC)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `sacrificial_iron` | `stainless_steel` (64.9%) | `sacrificial_iron` (28.1%) | `carbon` (5.3%) | ✓ |
| 阳极 (细类) | 43 | `iron_rod` | `iron_generic` (54.5%) | `stainless_steel_generic` (24.8%) | `stainless_steel_rod` (19.6%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `nickel` (59.5%) | `stainless_steel` (38.8%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_foam` | `stainless_steel_generic` (89.5%) | `nickel_foam` (9.4%) | `nickel_generic` (0.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (98.9%) | `ABSENT` (0.7%) | `K` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `Br` (96.8%) | `BF4` (1.9%) | `I` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.3%) | `silyl_electrophile` (5.7%) | `bromide_anion` (5.6%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `pyridine_organocat` (82.0%) | `ABSENT` (13.4%) | `ionic_organocat` (1.4%) | ✓ |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_amide` (98.5%) | `polar_aprotic_nitrile` (0.8%) | `polar_aprotic_sulfoxide` (0.2%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CN(C)C=O` (86%) | `CC(=O)N(C)C` (8%) | `CC#N` (3%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (99%) | `[Cl-].[Na+]` (0%) | `CCO` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `c1ccc(-c2ccccn2)nc` (36%) | `[Br-][Ni+2]1([Br-]` (1%) | `__OTHER__` (1%) | set ✗ / any ✗ |

---

### Reaction #878  yield=0.0%

**Source paper**: [`ChemSelect/10.1002_slct.202503086_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSelect/10.1002_slct.202503086_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1.c1ccc([Se][Se]c2ccccc2)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (52.0%) | `platinum` (47.9%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (41.9%) | `carbon_rod` (29.0%) | `graphite_plate` (21.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.3%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.2%) | `platinum_generic` (1.7%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (87.6%) | `ABSENT` (8.6%) | `Li` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (87.8%) | `I` (8.2%) | `ABSENT` (3.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `water` (26.8%) | `as_solvent_halogenated_aliphat` (5.1%) | `ABSENT` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (0.4%) | `polar_protic_alcohol` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `CO` (1%) | `ClCCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (92%) | `[18OH2]` (5%) | `CO` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #879  yield=0.0%

**Source paper**: [`ChemSelect/10.1002_slct.202503086_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSelect/10.1002_slct.202503086_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1.c1ccc([Se][Se]c2ccccc2)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (52.0%) | `platinum` (47.9%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (41.9%) | `carbon_rod` (29.0%) | `graphite_plate` (21.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.3%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.2%) | `platinum_generic` (1.7%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (87.6%) | `ABSENT` (8.6%) | `Li` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (87.8%) | `I` (8.2%) | `ABSENT` (3.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `water` (26.8%) | `as_solvent_halogenated_aliphat` (5.1%) | `ABSENT` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (0.4%) | `polar_protic_alcohol` (0.3%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `CO` (1%) | `ClCCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (92%) | `[18OH2]` (5%) | `CO` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #880  yield=81.0%

**Source paper**: [`ChemSelect/10.1002_slct.202503086_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSelect/10.1002_slct.202503086_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1.c1ccc([Se][Se]c2ccccc2)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (52.0%) | `platinum` (47.9%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (41.9%) | `carbon_rod` (29.0%) | `graphite_plate` (21.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.3%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.2%) | `platinum_generic` (1.7%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (87.6%) | `ABSENT` (8.6%) | `Li` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (87.8%) | `I` (8.2%) | `ABSENT` (3.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `water` (26.8%) | `as_solvent_halogenated_aliphat` (5.1%) | `ABSENT` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (0.4%) | `polar_protic_alcohol` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `CO` (1%) | `ClCCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (92%) | `[18OH2]` (5%) | `CO` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #881  yield=62.0%

**Source paper**: [`ChemSelect/10.1002_slct.202503086_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSelect/10.1002_slct.202503086_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1.c1ccc([Se][Se]c2ccccc2)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (52.0%) | `platinum` (47.9%) | `ABSENT` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (41.9%) | `carbon_rod` (29.0%) | `graphite_plate` (21.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.3%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.2%) | `platinum_generic` (1.7%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (87.6%) | `ABSENT` (8.6%) | `Li` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (87.8%) | `I` (8.2%) | `ABSENT` (3.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `water` (26.8%) | `as_solvent_halogenated_aliphat` (5.1%) | `ABSENT` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (0.4%) | `polar_protic_alcohol` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `CO` (1%) | `ClCCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (92%) | `[18OH2]` (5%) | `CO` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #882  yield=70.0%

**Source paper**: [`ChemSelect/10.1002_slct.202503086_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSelect/10.1002_slct.202503086_p2_t0.json) (反应 idx 在该 JSON 内 = #4)

```
C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1.c1ccc([Se][Se]c2ccccc2)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2ccccc2)cc1.Cc1ccc(S(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (52.0%) | `platinum` (47.9%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (41.9%) | `carbon_rod` (29.0%) | `graphite_plate` (21.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.3%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.2%) | `platinum_generic` (1.7%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (87.6%) | `ABSENT` (8.6%) | `Li` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (87.8%) | `I` (8.2%) | `ABSENT` (3.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `water` (26.8%) | `as_solvent_halogenated_aliphat` (5.1%) | `ABSENT` (3.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (0.4%) | `polar_protic_alcohol` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `CO` (1%) | `ClCCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (92%) | `[18OH2]` (5%) | `CO` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #883  yield=0.0%

**Source paper**: [`ChemSelect/10.1002_slct.202503086_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSelect/10.1002_slct.202503086_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1.c1ccc([Se][Se]c2ccccc2)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (52.0%) | `platinum` (47.9%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (41.9%) | `carbon_rod` (29.0%) | `graphite_plate` (21.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.3%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.2%) | `platinum_generic` (1.7%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (87.6%) | `ABSENT` (8.6%) | `Li` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `Br` | `BF4` (87.8%) | `I` (8.2%) | `ABSENT` (3.2%) | ✗ |
| 试剂大类 | 103 | `water` | `water` (26.8%) | `as_solvent_halogenated_aliphat` (5.1%) | `ABSENT` (3.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.8%) | `ABSENT` (0.4%) | `polar_protic_alcohol` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `CO` (1%) | `ClCCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (92%) | `[18OH2]` (5%) | `CO` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #884  yield=0.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #885  yield=0.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #886  yield=0.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #887  yield=68.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #888  yield=58.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `nickel` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✗ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #889  yield=50.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_aprotic_amide` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✗ |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #890  yield=55.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #891  yield=20.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #892  yield=70.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #893  yield=40.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `tertiary_amine` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #894  yield=0.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #895  yield=47.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `alkali_carboxylate` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #896  yield=14.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #897  yield=0.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #898  yield=0.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `ABSENT` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `peroxide` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #899  yield=80.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p5_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O.CO.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (76.0%) | `ABSENT` (23.3%) | `platinum` (0.4%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (53.3%) | `unknown_electrode` (15.7%) | `carbon_rod` (15.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (2.2%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (69.1%) | `platinum_generic` (20.0%) | `ABSENT` (7.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.0%) | `ABSENT` (3.8%) | `NEt4` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.0%) | `ABSENT` (2.2%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.6%) | `boron_lewis_acid` (8.2%) | `water` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.5%) | `ferrocene_mediator` (3.3%) | `unparseable_text` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (38.6%) | `cyclic_ether` (21.0%) | `halogenated_aliphatic` (13.5%) | ✗ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (2%) | `ClCCCl` (1%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #900  yield=40.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p5_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O.CO.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (76.0%) | `ABSENT` (23.3%) | `platinum` (0.4%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (53.3%) | `unknown_electrode` (15.7%) | `carbon_rod` (15.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (2.2%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (69.1%) | `platinum_generic` (20.0%) | `ABSENT` (7.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.0%) | `ABSENT` (3.8%) | `NEt4` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.0%) | `ABSENT` (2.2%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.6%) | `boron_lewis_acid` (8.2%) | `water` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (94.5%) | `ferrocene_mediator` (3.3%) | `unparseable_text` (0.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (38.6%) | `cyclic_ether` (21.0%) | `halogenated_aliphatic` (13.5%) | ✗ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (2%) | `ClCCCl` (1%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #901  yield=25.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p5_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O.CO.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (76.0%) | `ABSENT` (23.3%) | `platinum` (0.4%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (53.3%) | `unknown_electrode` (15.7%) | `carbon_rod` (15.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (2.2%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (69.1%) | `platinum_generic` (20.0%) | `ABSENT` (7.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.0%) | `ABSENT` (3.8%) | `NEt4` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.0%) | `ABSENT` (2.2%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.6%) | `boron_lewis_acid` (8.2%) | `water` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `triarylamine_radical_cat` | `ABSENT` (94.5%) | `ferrocene_mediator` (3.3%) | `unparseable_text` (0.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (38.6%) | `cyclic_ether` (21.0%) | `halogenated_aliphatic` (13.5%) | ✗ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (2%) | `ClCCCl` (1%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #902  yield=41.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p5_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O.CO.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (76.0%) | `ABSENT` (23.3%) | `platinum` (0.4%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (53.3%) | `unknown_electrode` (15.7%) | `carbon_rod` (15.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (2.2%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (69.1%) | `platinum_generic` (20.0%) | `ABSENT` (7.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.0%) | `ABSENT` (3.8%) | `NEt4` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.0%) | `ABSENT` (2.2%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.6%) | `boron_lewis_acid` (8.2%) | `water` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (94.5%) | `ferrocene_mediator` (3.3%) | `unparseable_text` (0.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (38.6%) | `cyclic_ether` (21.0%) | `halogenated_aliphatic` (13.5%) | ✗ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (2%) | `ClCCCl` (1%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #903  yield=28.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p5_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O.CO.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (76.0%) | `ABSENT` (23.3%) | `platinum` (0.4%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (53.3%) | `unknown_electrode` (15.7%) | `carbon_rod` (15.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (2.2%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (69.1%) | `platinum_generic` (20.0%) | `ABSENT` (7.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.0%) | `ABSENT` (3.8%) | `NEt4` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.0%) | `ABSENT` (2.2%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.6%) | `boron_lewis_acid` (8.2%) | `water` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `organic_neutral_cat` | `ABSENT` (94.5%) | `ferrocene_mediator` (3.3%) | `unparseable_text` (0.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (38.6%) | `cyclic_ether` (21.0%) | `halogenated_aliphatic` (13.5%) | ✗ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (2%) | `ClCCCl` (1%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #904  yield=5.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #905  yield=6.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #906  yield=0.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p5_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O.CO.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (76.0%) | `ABSENT` (23.3%) | `platinum` (0.4%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (53.3%) | `unknown_electrode` (15.7%) | `carbon_rod` (15.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (2.2%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (69.1%) | `platinum_generic` (20.0%) | `ABSENT` (7.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.0%) | `ABSENT` (3.8%) | `NEt4` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.0%) | `ABSENT` (2.2%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.6%) | `boron_lewis_acid` (8.2%) | `water` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (94.5%) | `ferrocene_mediator` (3.3%) | `unparseable_text` (0.3%) | ✗ |
| 溶剂大类 | 27 | `aqueous` | `polar_aprotic_nitrile` (38.6%) | `cyclic_ether` (21.0%) | `halogenated_aliphatic` (13.5%) | ✗ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (2%) | `ClCCCl` (1%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #907  yield=0.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p5_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O.CO.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (76.0%) | `ABSENT` (23.3%) | `platinum` (0.4%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (53.3%) | `unknown_electrode` (15.7%) | `carbon_rod` (15.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (2.2%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (69.1%) | `platinum_generic` (20.0%) | `ABSENT` (7.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.0%) | `ABSENT` (3.8%) | `NEt4` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.0%) | `ABSENT` (2.2%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.6%) | `boron_lewis_acid` (8.2%) | `water` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (94.5%) | `ferrocene_mediator` (3.3%) | `unparseable_text` (0.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (38.6%) | `cyclic_ether` (21.0%) | `halogenated_aliphatic` (13.5%) | ✗ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (2%) | `ClCCCl` (1%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #908  yield=4.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p5_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O.CO.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (76.0%) | `ABSENT` (23.3%) | `platinum` (0.4%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (53.3%) | `unknown_electrode` (15.7%) | `carbon_rod` (15.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (2.2%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (69.1%) | `platinum_generic` (20.0%) | `ABSENT` (7.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.0%) | `ABSENT` (3.8%) | `NEt4` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.0%) | `ABSENT` (2.2%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.6%) | `boron_lewis_acid` (8.2%) | `water` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.5%) | `ferrocene_mediator` (3.3%) | `unparseable_text` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (38.6%) | `cyclic_ether` (21.0%) | `halogenated_aliphatic` (13.5%) | ✗ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (2%) | `ClCCCl` (1%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #909  yield=68.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p5_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O.CO.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (76.0%) | `ABSENT` (23.3%) | `platinum` (0.4%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (53.3%) | `unknown_electrode` (15.7%) | `carbon_rod` (15.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (2.2%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (69.1%) | `platinum_generic` (20.0%) | `ABSENT` (7.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.0%) | `ABSENT` (3.8%) | `NEt4` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.0%) | `ABSENT` (2.2%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.6%) | `boron_lewis_acid` (8.2%) | `water` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.5%) | `ferrocene_mediator` (3.3%) | `unparseable_text` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (38.6%) | `cyclic_ether` (21.0%) | `halogenated_aliphatic` (13.5%) | ✗ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (2%) | `ClCCCl` (1%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #910  yield=19.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p5_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O.CO.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (76.0%) | `ABSENT` (23.3%) | `platinum` (0.4%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (53.3%) | `unknown_electrode` (15.7%) | `carbon_rod` (15.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (2.2%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (69.1%) | `platinum_generic` (20.0%) | `ABSENT` (7.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.0%) | `ABSENT` (3.8%) | `NEt4` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.0%) | `ABSENT` (2.2%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.6%) | `boron_lewis_acid` (8.2%) | `water` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `Fe_complex` | `ABSENT` (94.5%) | `ferrocene_mediator` (3.3%) | `unparseable_text` (0.3%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (38.6%) | `cyclic_ether` (21.0%) | `halogenated_aliphatic` (13.5%) | ✗ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (2%) | `ClCCCl` (1%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #911  yield=0.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p5_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O.CO.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (76.0%) | `ABSENT` (23.3%) | `platinum` (0.4%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (53.3%) | `unknown_electrode` (15.7%) | `carbon_rod` (15.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (2.2%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (69.1%) | `platinum_generic` (20.0%) | `ABSENT` (7.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.0%) | `ABSENT` (3.8%) | `NEt4` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.0%) | `ABSENT` (2.2%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.6%) | `boron_lewis_acid` (8.2%) | `water` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.5%) | `ferrocene_mediator` (3.3%) | `unparseable_text` (0.3%) | ✓ |
| 溶剂大类 | 27 | `hfip` | `polar_aprotic_nitrile` (38.6%) | `cyclic_ether` (21.0%) | `halogenated_aliphatic` (13.5%) | ✗ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (2%) | `ClCCCl` (1%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #912  yield=0.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p5_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p5_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O.CO.[H][H]
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (76.0%) | `ABSENT` (23.3%) | `platinum` (0.4%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `graphite_rod` (53.3%) | `unknown_electrode` (15.7%) | `carbon_rod` (15.5%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (2.2%) | `nickel` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (69.1%) | `platinum_generic` (20.0%) | `ABSENT` (7.7%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.9%) | `ABSENT` (2.1%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (94.0%) | `ABSENT` (3.8%) | `NEt4` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (95.0%) | `ABSENT` (2.2%) | `PF6` (1.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.6%) | `boron_lewis_acid` (8.2%) | `water` (2.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.5%) | `ferrocene_mediator` (3.3%) | `unparseable_text` (0.3%) | ✓ |
| 溶剂大类 | 27 | `tfe` | `polar_aprotic_nitrile` (38.6%) | `cyclic_ether` (21.0%) | `halogenated_aliphatic` (13.5%) | ✗ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (2%) | `ClCCCl` (1%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `O=O` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✗ / any ✗ |

---

### Reaction #913  yield=80.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #914  yield=47.0%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #915  yield=0.5%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `alkali_alkoxide` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #916  yield=0.5%

**Source paper**: [`ChemSusChem/10.1002_cssc.202402224_p2_t0.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/10.1002_cssc.202402224_p2_t0.json) (反应 idx 在该 JSON 内 = #0)

```
COC(=O)C(Cc1ccc(F)cc1)C(=O)OC.C=C(c1ccccc1)c1ccccc1>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `ABSENT` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ |
| 阳极 (细类) | 43 | `unknown_electrode` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #917  yield=29.0%

**Source paper**: [`ChinJChem/2023_Chinese_Journal_of_Catalysis_2023_52144-153.json`](reactions_by_journal_alkene_ec_audited/ChinJChem/2023_Chinese_Journal_of_Catalysis_2023_52144-153.json) (反应 idx 在该 JSON 内 = #18)

```
C=CC(=O)OCc1ccccc1.COC(=O)C(Cc1ccc(OC)cc1)C(=O)OC>>COC(=O)C1(C(=O)OC)Cc2ccc(OC)cc2C(C(=O)OCc2ccccc2)C1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (100.0%) | `graphite_felt` (0.0%) | `carbon_generic` (0.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `carbon` (0.5%) | `sacrificial_iron` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (99.3%) | `platinum_plate` (0.6%) | `carbon_felt` (0.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (99.4%) | `ABSENT` (0.3%) | `Li` (0.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (98.5%) | `ABSENT` (0.5%) | `carboxylate` (0.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (35.6%) | `alkali_carboxylate` (2.9%) | `unparseable_text` (1.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `Fe_complex` (98.6%) | `ABSENT` (0.8%) | `ferrocene_mediator` (0.3%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (99.8%) | `polar_aprotic_nitrile` (0.1%) | `polar_aprotic_amide` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `COCCOC` | `COCCOC` (100%) | `CO` (100%) | `CC#N` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (99%) | `__ABSENT__` (1%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[cH]12->[Fe+2]3456` (98%) | `c1cc[c]([Fe][c]2cc` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #918  yield=25.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #1)

```
C=C(c1ccccc1)c1ccc(C)cc1.COC(=O)C(Cc1ccc(OC)cc1)C(=O)OC>>COC(=O)[C@@]1(Cc2ccc(OC)cc2)C[C@@](c2ccccc2)(c2ccc(C)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (98.2%) | `carbon_generic` (0.6%) | `graphite_rod` (0.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.9%) | `nickel` (1.5%) | `carbon` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (65.7%) | `platinum_generic` (26.2%) | `nickel_foam` (5.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `ABSENT` (1.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (99.1%) | `NBu4` (0.9%) | `Na` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (98.7%) | `BF4` (1.2%) | `molecular_no_ion` (0.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `water` (9.9%) | `ABSENT` (7.8%) | `metal_oxide_oxidant` (2.1%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (50.1%) | `ABSENT` (34.8%) | `Fe_complex` (10.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (63.6%) | `polar_aprotic_nitrile` (26.6%) | `ABSENT` (3.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `CO` (44%) | `COCCOC` (33%) | `CC#N` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O` (52%) | `N` (2%) | `O=C(O)O.[K]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Fe+2].c1cc[cH-]c1` (50%) | `__ABSENT__` (8%) | `[cH]12->[Fe+2]3456` (3%) | set ✗ / any ✓ |

---

### Reaction #919  yield=22.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #2)

```
COC(=O)C(Cc1ccc(OC)cc1)C(=O)OC.C=C(c1ccccc1)c1ccc(C)c(C)c1>>COC(=O)[C@@]1(Cc2ccc(OC)cc2)C[C@@](c2ccccc2)(c2ccc(C)c(C)…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (94.7%) | `carbon_generic` (1.6%) | `graphite_rod` (1.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `nickel` (2.1%) | `carbon` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (61.1%) | `platinum_plate` (36.2%) | `nickel_foam` (1.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (99.3%) | `NBu4` (0.7%) | `Na` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (98.9%) | `BF4` (1.1%) | `Br` (0.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.1%) | `water` (7.3%) | `metal_oxide_oxidant` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (95.6%) | `Fe_complex` (1.9%) | `ferrocene_mediator` (0.9%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (58.5%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_sulfoxide` (4.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `CO` (20%) | `CC#N` (12%) | `COCCOC` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C(O)O.[K]` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[cH]12->[Fe+2]3456` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✗ / any ✓ |

---

### Reaction #920  yield=23.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #3)

```
COC(=O)C(Cc1ccc(OC)cc1)C(=O)OC.C=C(c1ccc(Cl)cc1)c1ccc(Br)cc1>>COC(=O)[C@@]1(Cc2ccc(OC)cc2)C[C@@](c2ccc(Cl)cc2)(c2ccc(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (82.8%) | `graphite_rod` (13.2%) | `carbon_rod` (1.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.1%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (85.3%) | `platinum_generic` (13.0%) | `platinum_wire` (1.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.0%) | `ABSENT` (2.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (97.2%) | `NBu4` (2.8%) | `Na` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (93.0%) | `BF4` (7.0%) | `PF6` (0.0%) | ✓ |
| 试剂大类 | 103 | `boron_lewis_acid` | `ABSENT` (9.2%) | `alkali_other_salt` (4.1%) | `water` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (71.3%) | `ferrocene_mediator` (15.7%) | `pyridine_organocat` (4.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (90.5%) | `polar_protic_alcohol` (5.4%) | `ABSENT` (2.7%) | ✓ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (60%) | `COCCOC` (7%) | `__ABSENT__` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #921  yield=23.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #3)

```
COC(=O)C(Cc1ccc(OC)cc1)C(=O)OC.C=C(c1ccc(Cl)cc1)c1ccc(Br)cc1>>COC(=O)[C@@]1(Cc2ccc(OC)cc2)C[C@@](c2ccc(Cl)cc2)(c2ccc(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (82.8%) | `graphite_rod` (13.2%) | `carbon_rod` (1.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.1%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (85.3%) | `platinum_generic` (13.0%) | `platinum_wire` (1.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.0%) | `ABSENT` (2.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (97.2%) | `NBu4` (2.8%) | `Na` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (93.0%) | `BF4` (7.0%) | `PF6` (0.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `boron_lewis_acid` | `ABSENT` (9.2%) | `alkali_other_salt` (4.1%) | `water` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (71.3%) | `ferrocene_mediator` (15.7%) | `pyridine_organocat` (4.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (90.5%) | `polar_protic_alcohol` (5.4%) | `ABSENT` (2.7%) | ✓ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (60%) | `COCCOC` (7%) | `__ABSENT__` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (100%) | `O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `CC(=O)[CH-]C(C)=O.` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #922  yield=30.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #5)

```
C=C(c1ccccc1)c1ccc(C)cc1.COC(=O)C(Cc1ccc(OC)cc1)C(=O)OC>>COC(=O)[C@]1(Cc2ccc(OC)cc2)C[C@@](c2ccccc2)(c2ccc(C)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (98.2%) | `carbon_generic` (0.6%) | `graphite_rod` (0.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.9%) | `nickel` (1.5%) | `carbon` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (65.7%) | `platinum_generic` (26.2%) | `nickel_foam` (5.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.9%) | `ABSENT` (1.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (99.1%) | `NBu4` (0.9%) | `Na` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (98.7%) | `BF4` (1.2%) | `molecular_no_ion` (0.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (9.9%) | `ABSENT` (7.8%) | `metal_oxide_oxidant` (2.1%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (50.1%) | `ABSENT` (34.8%) | `Fe_complex` (10.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (63.6%) | `polar_aprotic_nitrile` (26.6%) | `ABSENT` (3.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `CO` (44%) | `COCCOC` (33%) | `CC#N` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O` (52%) | `N` (2%) | `O=C(O)O.[K]` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Fe+2].c1cc[cH-]c1` (50%) | `__ABSENT__` (8%) | `[cH]12->[Fe+2]3456` (3%) | set ✗ / any ✓ |

---

### Reaction #923  yield=30.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #6)

```
COC(=O)C(Cc1ccc(OC)cc1)C(=O)OC.C=C(c1ccccc1)c1ccc(C)c(C)c1>>COC(=O)[C@]1(Cc2ccc(OC)cc2)C[C@@](c2ccccc2)(c2ccc(C)c(C)c…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.9%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (94.7%) | `carbon_generic` (1.6%) | `graphite_rod` (1.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `nickel` (2.1%) | `carbon` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (61.1%) | `platinum_plate` (36.2%) | `nickel_foam` (1.1%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (99.3%) | `NBu4` (0.7%) | `Na` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (98.9%) | `BF4` (1.1%) | `Br` (0.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.1%) | `water` (7.3%) | `metal_oxide_oxidant` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (95.6%) | `Fe_complex` (1.9%) | `ferrocene_mediator` (0.9%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (58.5%) | `polar_aprotic_nitrile` (33.9%) | `polar_aprotic_sulfoxide` (4.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `CO` (20%) | `CC#N` (12%) | `COCCOC` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C(O)O.[K]` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[cH]12->[Fe+2]3456` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✗ / any ✓ |

---

### Reaction #924  yield=40.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #7)

```
C=C(c1ccc(OC)cc1)c1ccc(OC)cc1.COC(=O)C(Cc1ccc(OC)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(OC)cc2)CC(c2ccc(OC)cc2)(c2ccc(OC)cc2)O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `ABSENT` (0.6%) | `platinum` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (93.7%) | `graphite_rod` (3.4%) | `carbon_generic` (1.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.9%) | `nickel` (1.1%) | `carbon` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (57.4%) | `platinum_generic` (28.7%) | `platinum_wire` (3.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (92.5%) | `ABSENT` (7.5%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (63.2%) | `NBu4` (36.4%) | `Na` (0.2%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (53.9%) | `BF4` (45.7%) | `I` (0.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (10.8%) | `ABSENT` (7.9%) | `boron_lewis_acid` (3.1%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (76.0%) | `ferrocene_mediator` (19.1%) | `Fe_complex` (3.4%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (81.8%) | `polar_aprotic_nitrile` (9.8%) | `ABSENT` (2.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (80%) | `CO` (29%) | `CC#N` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O` (38%) | `N` (1%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #925  yield=40.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #8)

```
C=C(C)c1ccccc1.COC(=O)C(Cc1ccc(F)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(F)cc2)CC(C)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (99.6%) | `graphite_generic` (0.1%) | `reticulated_vitreous_carbon` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.9%) | `carbon` (5.9%) | `nickel` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (64.5%) | `carbon_felt` (21.0%) | `nickel_foam` (5.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (62.6%) | `NBu4` (37.3%) | `NEt4` (0.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (68.2%) | `BF4` (31.4%) | `ClO4` (0.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.3%) | `o2_oxidant` (3.3%) | `metal_oxide_oxidant` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (64.9%) | `ABSENT` (27.8%) | `Fe_complex` (2.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (75.0%) | `polar_aprotic_nitrile` (13.1%) | `cyclic_ether` (6.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `CO` (18%) | `COCCOC` (4%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (48%) | `[Fe+2].c1cc[cH-]c1` (14%) | `[cH]12->[Fe+2]3456` (5%) | set ✗ / any ✓ |

---

### Reaction #926  yield=49.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #9)

```
C=C(c1ccc(F)cc1)c1ccc(F)cc1.COC(=O)C(Cc1ccc(OC)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(OC)cc2)CC(c2ccc(F)cc2)(c2ccc(F)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.8%) | `ABSENT` (0.9%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_rod` (47.1%) | `carbon_felt` (45.8%) | `carbon_rod` (2.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.4%) | `ABSENT` (1.2%) | `carbon` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (87.8%) | `platinum_generic` (7.7%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (71.3%) | `NBu4` (28.1%) | `Na` (0.3%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (67.0%) | `BF4` (32.2%) | `I` (0.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (11.5%) | `water` (5.9%) | `boron_lewis_acid` (4.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (92.7%) | `ferrocene_mediator` (6.3%) | `Fe_complex` (0.4%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (51.4%) | `ABSENT` (21.9%) | `polar_aprotic_nitrile` (17.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (13%) | `CC#N` (2%) | `CO` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `O=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #927  yield=47.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #10)

```
C=C(c1ccc(Br)cc1)c1ccc(Br)cc1.COC(=O)C(Cc1ccc(OC)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(OC)cc2)CC(c2ccc(Br)cc2)(c2ccc(Br)cc2)O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (90.0%) | `graphite_rod` (8.5%) | `carbon_generic` (0.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.1%) | `nickel` (0.4%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (57.8%) | `platinum_generic` (23.2%) | `platinum_wire` (15.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.2%) | `ABSENT` (2.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (82.2%) | `NBu4` (17.8%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (65.1%) | `BF4` (34.9%) | `Br` (0.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `water` (10.3%) | `ABSENT` (8.2%) | `as_solvent_alkane` (2.2%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (87.8%) | `ferrocene_mediator` (6.6%) | `Fe_complex` (3.3%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (53.3%) | `polar_protic_alcohol` (28.4%) | `ABSENT` (15.5%) | ✓ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (27%) | `COCCOC` (20%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O` (38%) | `N` (1%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[cH]12->[Fe+2]3456` (0%) | `CC(=O)[CH-]C(C)=O.` (0%) | set ✗ / any ✗ |

---

### Reaction #928  yield=45.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #11)

```
C=C(c1ccc(Cl)cc1)c1ccc(Cl)cc1.COC(=O)C(Cc1ccc(OC)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(OC)cc2)CC(c2ccc(Cl)cc2)(c2ccc(Cl)cc2)O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (93.4%) | `graphite_rod` (4.3%) | `carbon_rod` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.8%) | `nickel` (0.7%) | `carbon` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (91.6%) | `platinum_generic` (6.9%) | `nickel_generic` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.3%) | `ABSENT` (1.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (98.6%) | `NBu4` (1.4%) | `Na` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (98.0%) | `BF4` (2.0%) | `PF6` (0.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.5%) | `water` (4.0%) | `boron_lewis_acid` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (51.1%) | `ABSENT` (42.8%) | `Fe_complex` (2.4%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (56.4%) | `polar_protic_alcohol` (35.1%) | `ABSENT` (2.7%) | ✓ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (57%) | `COCCOC` (28%) | `CO` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `O=P([O-])([O-])O.[` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (82%) | `__ABSENT__` (5%) | `[cH]12->[Fe+2]3456` (2%) | set ✓ / any ✓ |

---

### Reaction #929  yield=41.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #12)

```
C=C(c1ccccc1)c1ccccc1.C#CCC(C(=O)OC)C(=O)OC>>C#CCC1(C(=O)OC)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (63.6%) | `carbon_felt` (31.2%) | `carbon_rod` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.6%) | `stainless_steel` (3.7%) | `carbon` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (77.6%) | `platinum_generic` (14.5%) | `platinum_wire` (3.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `divided` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (75.1%) | `Na` (17.2%) | `ABSENT` (4.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (61.1%) | `I` (15.8%) | `ABSENT` (8.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (10.2%) | `iodide_anion` (2.5%) | `as_solvent_halogenated_aliphat` (2.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (92.2%) | `ferrocene_mediator` (2.8%) | `Fe_complex` (1.2%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (35.3%) | `polar_aprotic_nitrile` (34.2%) | `ketone` (12.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (14%) | `CO` (11%) | `COCCOC` (5%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `CCOC(C)=O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (98%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✓ |

---

### Reaction #930  yield=50.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #13)

```
C=C(c1ccc(C)cc1)c1ccc(C)cc1.COC(=O)C(Cc1ccc(OC)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(OC)cc2)CC(c2ccc(C)cc2)(c2ccc(C)cc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `platinum` (0.7%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (97.3%) | `graphite_rod` (1.7%) | `carbon_rod` (0.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.7%) | `nickel` (0.7%) | `carbon` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (87.1%) | `platinum_generic` (10.8%) | `nickel_foam` (0.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.5%) | `divided` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (98.5%) | `NBu4` (1.5%) | `Na` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (97.1%) | `BF4` (2.9%) | `OH` (0.0%) | ✓ |
| 试剂大类 | 103 | `boron_lewis_acid` | `ABSENT` (5.7%) | `water` (5.6%) | `as_solvent_polar_protic_alcoho` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (69.9%) | `ABSENT` (23.0%) | `Fe_complex` (3.8%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (62.5%) | `polar_aprotic_nitrile` (24.4%) | `ABSENT` (6.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (51%) | `CO` (29%) | `CC#N` (8%) | set ✗ / any ✓ |
| 试剂 set | 545 | `CCCC[N+](CCCC)(CCC` | `__ABSENT__` (99%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (80%) | `[cH]12->[Fe+2]3456` (4%) | `__ABSENT__` (3%) | set ✓ / any ✓ |

---

### Reaction #931  yield=60.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #14)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc(OC(F)(F)F)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(OC(F)(F)F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.4%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (98.0%) | `carbon_rod` (0.6%) | `graphite_generic` (0.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `carbon` (0.3%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (82.0%) | `platinum_generic` (14.7%) | `unknown_electrode` (1.6%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (97.1%) | `NBu4` (2.9%) | `NEt4` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (93.9%) | `BF4` (6.1%) | `ClO4` (0.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (7.7%) | `ABSENT` (4.7%) | `o2_oxidant` (4.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (76.2%) | `ferrocene_mediator` (21.3%) | `Mn_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (91.2%) | `polar_aprotic_nitrile` (2.9%) | `halogenated_aliphatic` (1.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (82%) | `CO` (24%) | `ClCCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `[I-].[Na+]` (53%) | `__ABSENT__` (1%) | `O=C(O)O.[Na]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[cH]12->[Fe+2]3456` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #932  yield=60.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #15)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(C(=O)OC)C1CCCC1>>COC(=O)C1(C2CCCC2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.2%) | `platinum` (4.8%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (48.1%) | `reticulated_vitreous_carbon` (23.4%) | `carbon_felt` (20.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.6%) | `nickel` (3.8%) | `carbon` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (70.9%) | `platinum_generic` (26.9%) | `nickel_foam` (0.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.4%) | `divided` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.9%) | `ABSENT` (1.2%) | `Na` (0.8%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (57.5%) | `PF6` (23.1%) | `ClO4` (8.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `carboxylic_acid` (6.9%) | `ABSENT` (6.1%) | `alkali_carbonate` (3.3%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (95.7%) | `ferrocene_mediator` (1.1%) | `triarylamine_radical_cat` (0.9%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (70.3%) | `halogenated_aliphatic` (6.9%) | `polar_protic_alcohol` (6.8%) | ✓ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (65%) | `CO` (21%) | `O` (10%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CC(=O)O` (13%) | `O=C([O-])[O-].[Cs+` (2%) | `O=CO` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (99%) | `[Fe+2].c1cc[cH-]c1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✗ / any ✗ |

---

### Reaction #933  yield=60.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #16)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)c1cccc(CC(C(=O)OC)C(=O)OC)c1>>COC(=O)c1cccc(CC2(C(=O)OC)CC(c3ccccc3)(c3ccccc3)OC2=O)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (100.0%) | `platinum` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (90.3%) | `graphite_rod` (8.0%) | `graphite_generic` (0.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.1%) | `platinum_generic` (0.9%) | `platinum_wire` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (72.5%) | `NBu4` (27.5%) | `NEt4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (52.6%) | `BF4` (47.2%) | `PF6` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (7.0%) | `ABSENT` (6.1%) | `as_solvent_polar_aprotic_sulfo` (3.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (56.3%) | `ferrocene_mediator` (38.8%) | `triarylamine_radical_cat` (1.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (79.3%) | `polar_aprotic_nitrile` (6.2%) | `ABSENT` (5.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (83%) | `CO` (12%) | `__ABSENT__` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `[I-].[Na+]` (59%) | `__ABSENT__` (2%) | `CC[N+](CC)(CC)CC.F` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (98%) | `[Cl][Mn][Cl]` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #934  yield=55.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #17)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc(OCc2ccccc2)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(OCc3ccccc3)cc2)CC(c2ccccc2)(c2ccccc2)O…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.2%) | `ABSENT` (1.4%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (96.7%) | `glassy_carbon` (1.0%) | `graphite_rod` (0.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (92.7%) | `ABSENT` (4.0%) | `nickel` (2.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (59.8%) | `platinum_generic` (15.1%) | `nickel_foam` (9.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (95.3%) | `ABSENT` (4.6%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (81.9%) | `NBu4` (17.8%) | `Na` (0.2%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (84.1%) | `BF4` (15.2%) | `PF6` (0.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (6.7%) | `ABSENT` (6.3%) | `iodide_anion` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (62.3%) | `ferrocene_mediator` (35.3%) | `Fe_complex` (1.5%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (93.3%) | `polar_aprotic_nitrile` (2.7%) | `polar_aprotic_sulfoxide` (1.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (84%) | `CO` (47%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O` (5%) | `__ABSENT__` (4%) | `[I-].[Na+]` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #935  yield=55.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #18)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1cccc2ccccc12)C(=O)OC>>COC(=O)C1(Cc2cccc3ccccc23)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.7%) | `sacrificial_magnesium` (0.2%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (80.7%) | `graphite_rod` (8.9%) | `glassy_carbon` (6.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (95.1%) | `carbon` (4.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (31.6%) | `platinum_generic` (31.5%) | `platinum_wire` (18.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (79.2%) | `ABSENT` (19.0%) | `Li` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (88.0%) | `ABSENT` (11.0%) | `ClO4` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (6.4%) | `iodide_anion` (3.2%) | `metal_oxide_oxidant` (2.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (70.3%) | `ferrocene_mediator` (20.8%) | `Fe_complex` (7.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (76.9%) | `polar_aprotic_nitrile` (11.0%) | `acyclic_ether` (4.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `[H+].[OH-]` | `CO` (94%) | `COCCOC` (32%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (1%) | `[I-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (98%) | `[Fe+2].c1cc[cH-]c1` (1%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✓ |

---

### Reaction #936  yield=53.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #19)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc(C(F)(F)F)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(C(F)(F)F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.4%) | `platinum` (0.8%) | `ABSENT` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (82.6%) | `unknown_electrode` (5.3%) | `glassy_carbon` (3.6%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.1%) | `carbon` (1.3%) | `ABSENT` (0.9%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (56.9%) | `platinum_generic` (19.9%) | `unknown_electrode` (16.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (87.6%) | `ABSENT` (12.3%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (74.2%) | `NBu4` (25.6%) | `NEt4` (0.2%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (68.0%) | `BF4` (31.5%) | `PF6` (0.3%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (6.5%) | `metal_oxide_oxidant` (2.2%) | `tellurium_reagent` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (65.3%) | `ferrocene_mediator` (17.7%) | `Fe_complex` (5.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (73.1%) | `polar_aprotic_nitrile` (10.8%) | `halogenated_aliphatic` (6.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `CO` (37%) | `CN(C)C=O` (17%) | `COCCOC` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C([O-])[O-].[K+]` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (99%) | `[Cl][Mn][Cl]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✗ / any ✓ |

---

### Reaction #937  yield=52.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #20)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc(SC)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(SC)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `platinum` (0.2%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (98.0%) | `reticulated_vitreous_carbon` (0.9%) | `carbon_generic` (0.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `nickel` (0.4%) | `stainless_steel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (57.6%) | `platinum_plate` (36.9%) | `platinum_foil` (3.5%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (73.7%) | `NBu4` (26.3%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (70.6%) | `BF4` (28.9%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `water` (4.8%) | `ABSENT` (3.4%) | `iodide_anion` (2.2%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (76.4%) | `ferrocene_mediator` (13.2%) | `Fe_complex` (6.8%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (75.5%) | `ABSENT` (6.8%) | `halogenated_aliphatic` (6.0%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (61%) | `CO` (13%) | `CC#N` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O` (47%) | `C[Si](C)(C)N=[N+]=` (5%) | `[I-].[Na+]` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[cH]12->[Fe+2]3456` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✓ |

---

### Reaction #938  yield=66.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #21)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc(C)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(C)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.4%) | `platinum` (1.2%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (96.7%) | `carbon_generic` (1.1%) | `graphite_rod` (0.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.3%) | `carbon` (0.8%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (89.1%) | `platinum_generic` (8.3%) | `nickel_foam` (0.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.6%) | `ABSENT` (3.3%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (99.2%) | `NBu4` (0.8%) | `Na` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (97.6%) | `BF4` (2.4%) | `PF6` (0.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (5.6%) | `water` (4.5%) | `boron_lewis_acid` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (48.9%) | `ABSENT` (43.7%) | `Fe_complex` (2.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (86.7%) | `polar_aprotic_nitrile` (7.1%) | `polar_aprotic_amide` (1.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `CO` (93%) | `COCCOC` (25%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `[I-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Fe+2].c1cc[cH-]c1` (19%) | `[cH]12->[Fe+2]3456` (3%) | `__ABSENT__` (3%) | set ✗ / any ✓ |

---

### Reaction #939  yield=62.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #22)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc(I)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(I)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.6%) | `platinum` (1.5%) | `ABSENT` (0.8%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (88.3%) | `graphite_generic` (3.1%) | `glassy_carbon` (2.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.6%) | `ABSENT` (0.8%) | `carbon` (0.7%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (83.3%) | `platinum_generic` (8.1%) | `nickel_generic` (2.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (95.5%) | `ABSENT` (4.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (94.2%) | `NBu4` (5.2%) | `Na` (0.5%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (88.6%) | `BF4` (11.1%) | `PF6` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.6%) | `boron_lewis_acid` (3.0%) | `water` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (90.1%) | `ferrocene_mediator` (6.5%) | `Mn_complex` (1.3%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (93.0%) | `polar_aprotic_nitrile` (3.1%) | `halogenated_aliphatic` (1.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `CO` (84%) | `COCCOC` (42%) | `ClCCCl` (7%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=C(O)O.[K]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[cH]12->[Fe+2]3456` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #940  yield=62.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #23)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc2ccccc2c1)C(=O)OC>>COC(=O)C1(Cc2ccc3ccccc3c2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.7%) | `ABSENT` (1.7%) | `platinum` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (88.3%) | `graphite_rod` (5.7%) | `unknown_electrode` (1.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (94.9%) | `ABSENT` (3.4%) | `nickel` (1.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (75.3%) | `platinum_generic` (8.9%) | `unknown_electrode` (7.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (79.8%) | `ABSENT` (19.9%) | `NEt4` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (90.7%) | `ABSENT` (8.9%) | `PF6` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (5.7%) | `water` (4.7%) | `boron_lewis_acid` (3.9%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (86.7%) | `ferrocene_mediator` (6.9%) | `Fe_complex` (2.5%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (88.0%) | `ABSENT` (3.1%) | `polar_aprotic_nitrile` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (67%) | `CO` (39%) | `CC#N` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `[I-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (99%) | `Brc1ccc(N(c2ccc(Br` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #941  yield=62.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #24)

```
C=C(c1ccccc1)c1ccccc1.CCOC(=O)C(CCCCl)C(=O)OCC>>CCOC(=O)C1(CCCCl)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.8%) | `sacrificial_magnesium` (2.0%) | `sacrificial_zinc` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (77.6%) | `carbon_generic` (9.9%) | `zinc_plate` (3.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (91.5%) | `carbon` (7.0%) | `ABSENT` (1.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (51.1%) | `platinum_plate` (31.9%) | `unknown_electrode` (6.2%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.3%) | `divided` (0.2%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (55.0%) | `ABSENT` (42.7%) | `Li` (2.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ABSENT` (59.5%) | `BF4` (23.8%) | `ClO4` (15.4%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (12.4%) | `carboxylic_acid` (3.8%) | `ABSENT` (3.6%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (95.1%) | `organic_neutral_cat` (1.0%) | `Fe_complex` (0.9%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `ABSENT` (43.9%) | `polar_protic_alcohol` (26.8%) | `polar_aprotic_amide` (12.8%) | ✓ |
| 溶剂 set | 79 | `CO` + `O` | `__ABSENT__` (95%) | `CC(=O)O` (0%) | `CN(C)C=O` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `__ABSENT__` | `[I-].[Na+]` (25%) | `O` (2%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (99%) | `__OTHER__` (0%) | `[O]=[Fe][O][Fe]=[O` (0%) | set ✗ / any ✗ |

---

### Reaction #942  yield=70.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #25)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)c1ccc(CC(C(=O)OC)C(=O)OC)cc1>>COC(=O)c1ccc(CC2(C(=O)OC)CC(c3ccccc3)(c3ccccc3)OC2=O)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `platinum` (0.6%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (93.8%) | `graphite_rod` (2.9%) | `glassy_carbon` (1.8%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.8%) | `ABSENT` (0.4%) | `carbon` (0.4%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (93.8%) | `platinum_generic` (5.3%) | `platinum_wire` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.7%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (81.2%) | `NBu4` (18.3%) | `Na` (0.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (73.1%) | `BF4` (26.5%) | `PF6` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (8.9%) | `inorganic_simple` (3.4%) | `water` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (85.4%) | `ferrocene_mediator` (11.8%) | `Fe_complex` (1.0%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (91.9%) | `polar_aprotic_nitrile` (3.4%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (87%) | `CO` (70%) | `ClCCCl` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `[I-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (99%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #943  yield=70.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #26)

```
C=C(c1ccccc1)c1ccccc1.CCCC(C(=O)OC)C(=O)OC>>CCCC1(C(=O)OC)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `graphite_generic` (57.7%) | `graphite_rod` (32.4%) | `carbon_felt` (7.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (87.0%) | `nickel` (10.3%) | `carbon` (1.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (80.6%) | `platinum_generic` (12.2%) | `nickel_foam` (2.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.6%) | `ABSENT` (2.4%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (98.8%) | `NBu4` (1.1%) | `Na` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (99.4%) | `BF4` (0.4%) | `I` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `water` (11.8%) | `ABSENT` (10.6%) | `metal_oxide_oxidant` (2.2%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (98.9%) | `organic_neutral_cat` (0.4%) | `triarylamine_radical_cat` (0.2%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `ABSENT` (57.8%) | `polar_aprotic_nitrile` (36.7%) | `halogenated_aliphatic` (2.4%) | ✗ |
| 溶剂 set | 79 | `CO` + `O` | `__ABSENT__` (98%) | `ClCCl` (0%) | `O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O` (26%) | `[18OH2]` (0%) | `Cl` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #944  yield=80.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #27)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc(OC)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(OC)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (92.6%) | `ABSENT` (6.2%) | `platinum` (1.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (89.4%) | `unknown_electrode` (4.8%) | `carbon_generic` (3.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (93.9%) | `ABSENT` (3.4%) | `nickel` (1.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (79.1%) | `platinum_plate` (7.4%) | `unknown_electrode` (5.4%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (93.5%) | `ABSENT` (6.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (55.5%) | `NBu4` (39.0%) | `Na` (4.6%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (53.1%) | `BF4` (43.9%) | `I` (1.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `water` (25.4%) | `ABSENT` (8.8%) | `as_solvent_alkane` (2.2%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (80.1%) | `ferrocene_mediator` (8.9%) | `Fe_complex` (7.4%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (86.8%) | `polar_aprotic_nitrile` (3.6%) | `polar_aprotic_sulfoxide` (2.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (81%) | `CO` (67%) | `O` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O` (60%) | `C[O-].[Na+]` (9%) | `N` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (98%) | `[Fe+2].c1cc[cH-]c1` (1%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #945  yield=80.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #28)

```
C=C(c1ccccc1)c1ccccc1.CCOC(=O)C(Cc1ccccc1)C(=O)OCC>>CCOC(=O)C1(Cc2ccccc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.4%) | `sacrificial_magnesium` (0.6%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (86.2%) | `carbon_generic` (5.7%) | `graphite_rod` (4.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.7%) | `ABSENT` (0.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (62.7%) | `platinum_generic` (22.2%) | `unknown_electrode` (12.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.8%) | `ABSENT` (1.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (97.2%) | `NBu4` (2.8%) | `Li` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (95.9%) | `BF4` (4.1%) | `PF6` (0.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (14.2%) | `ABSENT` (3.1%) | `boron_lewis_acid` (2.5%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (91.8%) | `ferrocene_mediator` (3.8%) | `Fe_complex` (1.3%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (68.2%) | `polar_aprotic_amide` (11.2%) | `polar_aprotic_nitrile` (6.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `CO` (50%) | `COCCOC` (49%) | `CN(C)C=O` (12%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `[I-].[Na+]` (40%) | `O=O` (1%) | `__ABSENT__` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (98%) | `__OTHER__` (0%) | `c1ccncc1` (0%) | set ✗ / any ✗ |

---

### Reaction #946  yield=78.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #29)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc(Cl)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(Cl)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (98.6%) | `carbon_generic` (0.7%) | `glassy_carbon` (0.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (94.3%) | `platinum_generic` (5.0%) | `platinum_wire` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (99.7%) | `NBu4` (0.3%) | `Na` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (99.3%) | `BF4` (0.7%) | `PF6` (0.0%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (5.3%) | `water` (3.8%) | `iodide_anion` (3.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (72.9%) | `ABSENT` (19.8%) | `Fe_complex` (3.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (88.2%) | `polar_aprotic_nitrile` (6.5%) | `acyclic_ether` (1.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (88%) | `CO` (31%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (2%) | `[I-].[Na+]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `[Fe+2].c1cc[cH-]c1` (20%) | `[Cl][Mn][Cl]` (4%) | `[cH]12->[Fe+2]3456` (3%) | set ✗ / any ✓ |

---

### Reaction #947  yield=78.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #30)

```
CCOC(=O)C(CC)C(=O)OCC.C=C(c1ccccc1)c1ccccc1>>CCOC(=O)C1(CC)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `ABSENT` (0.2%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_rod` (29.6%) | `reticulated_vitreous_carbon` (27.4%) | `graphite_rod` (11.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.9%) | `stainless_steel` (0.5%) | `carbon` (0.3%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (96.3%) | `platinum_generic` (2.7%) | `unknown_electrode` (0.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (96.2%) | `ABSENT` (3.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (98.4%) | `NBu4` (1.6%) | `NEt4` (0.0%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (98.2%) | `BF4` (1.6%) | `PF6` (0.2%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (4.5%) | `water` (3.0%) | `alkali_other_salt` (2.5%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (67.8%) | `ferrocene_mediator` (16.0%) | `organic_neutral_cat` (3.5%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (63.5%) | `polar_aprotic_amide` (17.2%) | `polar_aprotic_nitrile` (8.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `CN(C)C=O` (55%) | `CO` (35%) | `C1CCOC1` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `[I-].[Na+]` (14%) | `O` (4%) | `O=C([O-])[O-].[K+]` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (98%) | `__OTHER__` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✗ / any ✗ |

---

### Reaction #948  yield=74.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #31)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc(F)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (96.3%) | `ABSENT` (2.7%) | `platinum` (0.7%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (79.6%) | `graphite_rod` (6.5%) | `carbon_rod` (3.5%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.0%) | `ABSENT` (1.9%) | `carbon` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (78.8%) | `platinum_generic` (11.9%) | `ABSENT` (3.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (97.4%) | `ABSENT` (2.6%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (89.5%) | `NBu4` (10.2%) | `NEt4` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (78.0%) | `BF4` (21.7%) | `ClO4` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (13.2%) | `boron_lewis_acid` (8.3%) | `iodide_anion` (2.7%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (94.2%) | `ferrocene_mediator` (4.4%) | `Mn_complex` (0.7%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (65.8%) | `ABSENT` (16.1%) | `polar_aprotic_nitrile` (7.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (27%) | `CO` (6%) | `__ABSENT__` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #949  yield=73.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #32)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(CC(C)C)C(=O)OC>>COC(=O)C1(CC(C)C)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.7%) | `platinum` (3.2%) | `sacrificial_magnesium` (0.4%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (72.1%) | `graphite_generic` (12.0%) | `carbon_generic` (6.9%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (80.2%) | `carbon` (12.5%) | `nickel` (2.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (55.8%) | `platinum_generic` (16.6%) | `unknown_electrode` (8.4%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (81.6%) | `ABSENT` (9.7%) | `Na` (3.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (55.9%) | `ABSENT` (13.8%) | `ClO4` (13.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (12.1%) | `iodide_anion` (4.3%) | `water` (3.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (97.3%) | `Mn_complex` (1.0%) | `ferrocene_mediator` (0.5%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_amide` (38.5%) | `polar_aprotic_nitrile` (18.2%) | `polar_protic_alcohol` (17.7%) | ✓ |
| 溶剂 set | 79 | `CO` + `O` | `CN(C)C=O` (23%) | `O` (8%) | `CC#N` (6%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[Br-].[Br-].[Mn+2]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #950  yield=73.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #33)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc(C#N)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(C#N)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.4%) | `ABSENT` (3.5%) | `sacrificial_zinc` (0.6%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (66.5%) | `graphite_generic` (8.4%) | `graphite_rod` (6.4%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (88.7%) | `ABSENT` (7.2%) | `carbon` (2.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (48.5%) | `platinum_generic` (17.0%) | `unknown_electrode` (16.7%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.2%) | `ABSENT` (0.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (89.7%) | `NBu4` (9.9%) | `NEt4` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (77.6%) | `BF4` (21.5%) | `Cl` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.3%) | `iodide_anion` (3.9%) | `water` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (82.6%) | `ferrocene_mediator` (11.6%) | `Fe_complex` (4.9%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (76.6%) | `ABSENT` (17.3%) | `polar_aprotic_nitrile` (1.8%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `CO` (39%) | `COCCOC` (25%) | `CN(C)C=O` (2%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O=C(O)O.[K]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[cH]12->[Fe+2]3456` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✓ |

---

### Reaction #951  yield=72.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #34)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc(-c2ccccc2)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(-c3ccccc3)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.6%) | `platinum` (0.8%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (96.0%) | `glassy_carbon` (1.2%) | `carbon_generic` (1.0%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `nickel` (0.3%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (85.3%) | `platinum_generic` (10.8%) | `nickel_foam` (1.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.4%) | `ABSENT` (1.5%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (75.6%) | `NBu4` (24.3%) | `Li` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (71.5%) | `BF4` (28.2%) | `PF6` (0.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `boron_lewis_acid` (7.5%) | `ABSENT` (6.6%) | `iodide_anion` (4.7%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (62.9%) | `ferrocene_mediator` (32.9%) | `Fe_complex` (1.9%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (77.8%) | `ABSENT` (5.2%) | `polar_aprotic_nitrile` (3.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (89%) | `CO` (39%) | `CN(C)C=O` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `CCCC[N+](CCCC)(CCC` (21%) | `__ABSENT__` (12%) | `[I-].[Na+]` (8%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (99%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✓ |

---

### Reaction #952  yield=71.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #35)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc(C(C)(C)C)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(C(C)(C)C)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.9%) | `ABSENT` (0.5%) | `platinum` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (97.6%) | `glassy_carbon` (0.7%) | `graphite_rod` (0.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (96.0%) | `ABSENT` (2.0%) | `nickel` (1.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (90.8%) | `platinum_generic` (6.0%) | `nickel_foam` (1.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.5%) | `ABSENT` (1.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (95.6%) | `NBu4` (4.2%) | `NEt4` (0.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (89.9%) | `BF4` (10.0%) | `PF6` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (6.6%) | `water` (4.0%) | `as_solvent_polar_protic_alcoho` (3.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (73.2%) | `ferrocene_mediator` (19.8%) | `Mn_complex` (3.5%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_aprotic_nitrile` (47.7%) | `polar_protic_alcohol` (22.6%) | `polar_aprotic_amide` (9.3%) | ✓ |
| 溶剂 set | 79 | `CO` + `O` | `CC#N` (45%) | `COCCOC` (10%) | `CO` (7%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `O` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✗ / any ✗ |

---

### Reaction #953  yield=71.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #36)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc(Br)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(Br)cc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.6%) | `platinum` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (97.8%) | `carbon_generic` (1.3%) | `graphite_rod` (0.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.3%) | `carbon` (0.4%) | `nickel` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (43.9%) | `platinum_generic` (33.8%) | `platinum_wire` (18.8%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (98.4%) | `ABSENT` (1.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (86.6%) | `NBu4` (13.4%) | `Li` (0.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (66.3%) | `BF4` (33.7%) | `PF6` (0.0%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (5.9%) | `water` (4.5%) | `alkali_other_salt` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (77.8%) | `ferrocene_mediator` (12.9%) | `Fe_complex` (4.6%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (64.7%) | `polar_aprotic_nitrile` (25.1%) | `ABSENT` (5.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (61%) | `CO` (7%) | `CC#N` (3%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `__ABSENT__` (100%) | `[cH]12->[Fe+2]3456` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✓ |

---

### Reaction #954  yield=71.0%

**Source paper**: [`JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json`](reactions_by_journal_alkene_ec_audited/JOC/2025_Journal_of_Organic_Chemistry_2025_90_12_4450-4457.json) (反应 idx 在该 JSON 内 = #35)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(C)C(=O)OC>>COC(=O)C1(C)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (90.0%) | `ABSENT` (8.7%) | `platinum` (1.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `reticulated_vitreous_carbon` (30.7%) | `ABSENT` (20.0%) | `glassy_carbon` (16.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (89.6%) | `ABSENT` (8.9%) | `nickel` (0.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (50.6%) | `platinum_generic` (25.1%) | `platinum_wire` (11.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (91.7%) | `NEt4` (3.1%) | `Li` (2.1%) | ✗ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (93.0%) | `PF6` (3.8%) | `ClO4` (1.7%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (7.3%) | `carboxylic_acid` (2.7%) | `as_solvent_halogenated_aliphat` (2.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (45.5%) | `Fe_complex` (29.7%) | `Co_complex` (5.1%) | ✗ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (96.7%) | `polar_aprotic_nitrile` (2.2%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `C1CCOC1` + `O` | `CO` (98%) | `C1CCOC1` (3%) | `CC#N` (1%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])C(F)(` + `O=C([O-])[O-].[Na+` | `__ABSENT__` (99%) | `O` (0%) | `C[Si](C)(C)N=[N+]=` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` + `O=S(=O)([O-])C(F)(` | `__ABSENT__` (93%) | `Brc1ccc(N(c2ccc(Br` (2%) | `CCCC[N+](CCCC)(CCC` (1%) | set ✗ / any ✗ |

---

### Reaction #955  yield=86.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #38)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccc(F)cc1)C(=O)OC>>COC(=O)C1(Cc2ccc(F)cc2)CC(c2ccccc2)(c2ccccc2)[18O]C1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.1%) | `ABSENT` (0.5%) | `sacrificial_magnesium` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (99.2%) | `glassy_carbon` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (77.2%) | `carbon` (22.2%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (40.3%) | `carbon_felt` (23.5%) | `platinum_generic` (13.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (95.9%) | `ABSENT` (4.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (65.5%) | `ABSENT` (34.3%) | `Li` (0.1%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (75.5%) | `ABSENT` (24.1%) | `ClO4` (0.3%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (12.0%) | `o2_oxidant` (3.4%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ferrocene_mediator` (85.1%) | `ABSENT` (13.6%) | `Fe_complex` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (96.7%) | `cyclic_ether` (2.1%) | `halogenated_aliphatic` (0.7%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `COCCOC` (74%) | `CO` (60%) | `__ABSENT__` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `O=S(=O)([O-])OOS(=` + `__OTHER__` + `O=O` | `__ABSENT__` (100%) | `[I-].[Na+]` (0%) | `N` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[cH]12->[Fe+2]3456` | `[Fe+2].c1cc[cH-]c1` (44%) | `__ABSENT__` (20%) | `[cH]12->[Fe+2]3456` (4%) | set ✗ / any ✓ |

---

### Reaction #956  yield=85.0%

**Source paper**: [`ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json`](reactions_by_journal_alkene_ec_audited/ChemSusChem/2025_ChemSusChem_2025_18_8_e202402224.json) (反应 idx 在该 JSON 内 = #39)

```
C=C(c1ccccc1)c1ccccc1.COC(=O)C(Cc1ccccc1)C(=O)OC>>COC(=O)C1(Cc2ccccc2)CC(c2ccccc2)(c2ccccc2)OC1=O
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (98.5%) | `ABSENT` (0.9%) | `platinum` (0.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `carbon_felt` | `carbon_felt` (94.0%) | `glassy_carbon` (2.0%) | `graphite_rod` (1.7%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `platinum` | `platinum` (97.4%) | `ABSENT` (1.3%) | `carbon` (0.5%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (83.1%) | `platinum_generic` (9.4%) | `unknown_electrode` (5.5%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (89.0%) | `NBu4` (10.8%) | `Na` (0.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (77.9%) | `BF4` (21.9%) | `PF6` (0.1%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `iodide_anion` (9.7%) | `ABSENT` (4.8%) | `water` (3.3%) | ✓ |
| 催化剂大类 | 49 | `ferrocene_mediator` | `ABSENT` (64.1%) | `ferrocene_mediator` (25.4%) | `Fe_complex` (5.5%) | ✓ |
| 溶剂大类 | 27 | `polar_protic_alcohol` | `polar_protic_alcohol` (92.1%) | `polar_aprotic_nitrile` (2.0%) | `acyclic_ether` (1.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CO` + `O` | `CO` (94%) | `COCCOC` (85%) | `CN(C)C=O` (0%) | set ✗ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `[I-].[Na+]` (82%) | `O` (1%) | `O=C([O-])[O-].[Na+` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `[Fe+2].c1cc[cH-]c1` | `__ABSENT__` (80%) | `Brc1ccc(N(c2ccc(Br` (1%) | `[Cl][Mn][Cl]` (1%) | set ✗ / any ✗ |

---

### Reaction #957  yield=62.0%

**Source paper**: [`Chemistry/2025_Chemistry_-_A_European_Journal_2025_31_41_e202501779.json`](reactions_by_journal_alkene_ec_audited/Chemistry/2025_Chemistry_-_A_European_Journal_2025_31_41_e202501779.json) (反应 idx 在该 JSON 内 = #0)

```
CO.O=C(CC(=O)c1ccccc1)c1ccccc1.C=C(c1ccccc1)c1ccccc1>>COC1(c2ccccc2)OC(c2ccccc2)(c2ccccc2)CC1C(=O)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (94.5%) | `platinum` (3.5%) | `ABSENT` (1.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (66.1%) | `reticulated_vitreous_carbon` (18.3%) | `graphite_rod` (9.3%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `nickel` (64.4%) | `stainless_steel` (13.6%) | `carbon` (9.8%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `nickel_foam` | `nickel_foam` (26.2%) | `platinum_plate` (19.3%) | `nickel_plate` (15.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (93.1%) | `divided` (6.5%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `ABSENT` (60.5%) | `NBu4` (32.8%) | `NEt4` (3.0%) | ✗ |
| 电解质 anion | 26 | `ClO4` | `ABSENT` (58.0%) | `ClO4` (18.6%) | `PF6` (14.9%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `o2_oxidant` (5.3%) | `water` (4.3%) | `ABSENT` (2.9%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (94.9%) | `pyridine_organocat` (1.8%) | `organic_neutral_cat` (0.7%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `ABSENT` (98.5%) | `polar_aprotic_nitrile` (1.2%) | `polar_aprotic_amide` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `__ABSENT__` | `__ABSENT__` (99%) | `CC#N` (2%) | `CCO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O=O` (54%) | `c1ccc2c(c1)Sc1cccc` (3%) | `CCCC[N+](CCCC)(CCC` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `Brc1ccc(N(c2ccc(Br` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #958  yield=90.0%

**Source paper**: [`Chemistry/2025_Chemistry_-_A_European_Journal_2025_31_41_e202501779.json`](reactions_by_journal_alkene_ec_audited/Chemistry/2025_Chemistry_-_A_European_Journal_2025_31_41_e202501779.json) (反应 idx 在该 JSON 内 = #1)

```
C=C(c1ccccc1)c1ccccc1.CC(C)(C)C(=O)CC(=O)C(C)(C)C>>CC(C)(C)C(=O)C1CC(c2ccccc2)(c2ccccc2)OC1(O)C(C)(C)C
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.8%) | `ABSENT` (0.1%) | `platinum` (0.1%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `graphite_generic` (94.8%) | `carbon_rod` (1.4%) | `reticulated_vitreous_carbon` (1.2%) | ✓ (T1✓) |
| 阴极 (材料) | 15 | `nickel` | `carbon` (55.2%) | `platinum` (42.6%) | `nickel` (1.5%) | ✓ |
| 阴极 (细类) | 49 | `nickel_foam` | `graphite_generic` (49.2%) | `unknown_electrode` (25.9%) | `platinum_plate` (15.7%) | ✗ |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `divided` (0.0%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `Li` | `NEt4` (49.6%) | `Li` (46.2%) | `NBu4` (3.0%) | ✓ |
| 电解质 anion | 26 | `ClO4` | `ClO4` (95.3%) | `molecular_no_ion` (2.9%) | `BF4` (0.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (5.7%) | `metal_oxide_oxidant` (2.1%) | `tellurium_reagent` (2.1%) | ✗ |
| 催化剂大类 | 49 | `pyridine_organocat` | `ABSENT` (94.5%) | `Mn_complex` (1.9%) | `triarylamine_radical_cat` (1.0%) | ✗ |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.4%) | `ABSENT` (2.9%) | `polar_protic_alcohol` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `O` (2%) | `ClCCCl` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `Cc1ccc(I)cc1` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `Cc1cccc(C)n1` | `__ABSENT__` (99%) | `Brc1ccc(N(c2ccc(Br` (0%) | `[Cl][Mn][Cl]` (0%) | set ✗ / any ✗ |

---

### Reaction #959  yield=34.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #0)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCCOC(=O)c1ccc(Br)cc1>>O=C(OCCC(O)C[Se]c1ccccc1)c1ccc(Br)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (94.3%) | `carbon` (5.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_generic` (75.3%) | `platinum_plate` (22.2%) | `platinum_wire` (0.8%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (69.4%) | `platinum_plate` (29.6%) | `platinum_wire` (0.7%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (70.1%) | `Li` (18.4%) | `ABSENT` (10.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (52.6%) | `BF4` (23.8%) | `ABSENT` (17.3%) | ✓ |
| 试剂大类 | 103 | `water` | `as_solvent_halogenated_aliphat` (25.9%) | `ABSENT` (10.2%) | `water` (10.1%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.1%) | `ABSENT` (0.3%) | `halogenated_aliphatic` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `CC(=O)O` (1%) | `C1CCOC1` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `OCCBr` (82%) | `O=P([O-])([O-])[O-` (15%) | `__ABSENT__` (8%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #960  yield=41.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #1)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCCOC(=O)c1ccc(I)cc1>>O=C(OCCC(O)C[Se]c1ccccc1)c1ccc(I)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (93.1%) | `carbon` (6.8%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (85.7%) | `platinum_generic` (10.7%) | `graphite_plate` (0.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.3%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.3%) | `platinum_generic` (26.2%) | `reticulated_vitreous_carbon` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (59.8%) | `Li` (27.6%) | `ABSENT` (6.7%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `I` (89.3%) | `BF4` (6.4%) | `ABSENT` (2.1%) | ✓ |
| 试剂大类 | 103 | `water` | `as_solvent_halogenated_aliphat` (21.9%) | `ABSENT` (11.2%) | `o2_oxidant` (4.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `ammonium_PTC_organocat` (0.8%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.7%) | `ABSENT` (0.9%) | `halogenated_aliphatic` (0.6%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `CO` (0%) | `ClCCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (66%) | `OCCBr` (30%) | `O=P([O-])([O-])[O-` (2%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #961  yield=46.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #2)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCCOC(=O)c1ccco1>>O=C(OCCC(O)C[Se]c1ccccc1)c1ccco1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (89.2%) | `carbon` (10.7%) | `ABSENT` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (61.3%) | `platinum_generic` (31.7%) | `glassy_carbon` (2.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (83.0%) | `platinum_generic` (16.6%) | `platinum_wire` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (60.6%) | `Li` (29.2%) | `ABSENT` (9.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (62.0%) | `I` (18.5%) | `ABSENT` (13.8%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `as_solvent_halogenated_aliphat` (16.2%) | `water` (15.8%) | `ABSENT` (10.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `halogenated_aliphatic` (0.6%) | `polar_aprotic_amide` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (97%) | `CO` (1%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `OCCBr` (42%) | `__ABSENT__` (21%) | `O` (3%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #962  yield=44.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #3)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCCOC(=O)c1cc(C)cc(C)c1>>Cc1cc(C)cc(C(=O)OCCC(O)C[Se]c2ccccc2)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (91.2%) | `carbon` (8.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (69.3%) | `platinum_generic` (11.7%) | `graphite_plate` (10.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.8%) | `carbon` (1.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (92.9%) | `platinum_generic` (6.1%) | `platinum_wire` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (47.3%) | `ABSENT` (45.0%) | `Li` (7.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ABSENT` (45.6%) | `BF4` (31.4%) | `I` (18.3%) | ✓ |
| 试剂大类 | 103 | `water` | `water` (25.3%) | `as_solvent_halogenated_aliphat` (14.5%) | `o2_oxidant` (5.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (67.0%) | `ABSENT` (30.5%) | `halogenated_aliphatic` (0.9%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (90%) | `CC(=O)O` (2%) | `CO` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (94%) | `O=O` (2%) | `OCCBr` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #963  yield=43.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #4)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCCOC(=O)c1cccc(F)c1>>O=C(OCCC(O)C[Se]c1ccccc1)c1cccc(F)c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (61.6%) | `carbon` (38.0%) | `ABSENT` (0.3%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (44.4%) | `reticulated_vitreous_carbon` (19.2%) | `platinum_generic` (16.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.6%) | `carbon` (0.3%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (93.5%) | `platinum_generic` (6.1%) | `platinum_wire` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (86.3%) | `NBu4` (11.5%) | `Li` (1.4%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (85.8%) | `BF4` (7.8%) | `I` (5.1%) | ✓ |
| 试剂大类 | 103 | `water` | `water` (18.2%) | `as_solvent_halogenated_aliphat` (10.3%) | `ABSENT` (6.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.3%) | `ABSENT` (4.6%) | `halogenated_aliphatic` (2.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (60%) | `__ABSENT__` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (94%) | `[18OH2]` (0%) | `__ABSENT__` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #964  yield=44.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #5)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCCOC(=O)c1ccc(Cl)cc1>>O=C(OCCC(O)C[Se]c1ccccc1)c1ccc(Cl)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (96.7%) | `carbon` (3.3%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_generic` (56.9%) | `platinum_plate` (42.1%) | `carbon_felt` (0.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.2%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (64.8%) | `platinum_generic` (35.1%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.6%) | `ABSENT` (9.4%) | `Li` (4.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (68.3%) | `BF4` (19.1%) | `ABSENT` (9.2%) | ✓ |
| 试剂大类 | 103 | `water` | `as_solvent_halogenated_aliphat` (21.6%) | `ABSENT` (10.6%) | `water` (5.0%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `halogenated_aliphatic` (0.8%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (97%) | `C[N+](=O)[O-]` (0%) | `CC(=O)O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `OCCBr` (59%) | `__ABSENT__` (27%) | `O` (9%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #965  yield=49.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #6)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCCOC(=O)c1ccc(OC)cc1>>COc1ccc(C(=O)OCCC(O)C[Se]c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (74.5%) | `carbon` (25.3%) | `ABSENT` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_generic` (45.5%) | `platinum_plate` (38.3%) | `glassy_carbon` (3.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.2%) | `carbon` (0.8%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (54.6%) | `platinum_plate` (43.8%) | `platinum_wire` (0.8%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (75.4%) | `ABSENT` (13.2%) | `Li` (10.3%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (55.9%) | `I` (22.2%) | `ABSENT` (18.5%) | ✓ |
| 试剂大类 | 103 | `water` | `water` (16.8%) | `as_solvent_halogenated_aliphat` (16.3%) | `ABSENT` (9.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.2%) | `ABSENT` (2.2%) | `halogenated_aliphatic` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (97%) | `CO` (0%) | `C1CCOC1` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (53%) | `O=O` (1%) | `[18OH2]` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `__OTHER__` (0%) | set ✓ / any ✓ |

---

### Reaction #966  yield=48.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #7)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCCOC(=O)c1ccc2ccccc2c1>>O=C(OCCC(O)C[Se]c1ccccc1)c1ccc2ccccc2c1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (95.9%) | `carbon` (4.0%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (63.1%) | `platinum_generic` (34.3%) | `platinum_wire` (0.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.4%) | `carbon` (1.5%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (55.7%) | `platinum_generic` (41.4%) | `reticulated_vitreous_carbon` (0.9%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (64.7%) | `ABSENT` (23.5%) | `Li` (10.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (36.5%) | `I` (31.4%) | `ABSENT` (26.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `water` (14.1%) | `as_solvent_halogenated_aliphat` (11.8%) | `o2_oxidant` (8.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.2%) | `ABSENT` (3.1%) | `halogenated_aliphatic` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `CC(=O)O` (0%) | `CO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (80%) | `O=O` (1%) | `[18OH2]` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #967  yield=59.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #8)

```
C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1.c1cc([Se][Se]c2ccsc2)cs1>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2ccsc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (98.2%) | `carbon` (1.8%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (47.1%) | `platinum_generic` (46.9%) | `carbon_rod` (5.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.2%) | `carbon` (1.7%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (89.6%) | `platinum_generic` (9.4%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.3%) | `ABSENT` (0.6%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (99.2%) | `Li` (0.6%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (98.7%) | `I` (0.9%) | `ClO4` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `water` (20.9%) | `as_solvent_halogenated_aliphat` (4.8%) | `o2_oxidant` (4.8%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Co_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (92.3%) | `halogenated_aliphatic` (4.6%) | `ABSENT` (1.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `CO` (0%) | `ClCCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (76%) | `O=O` (7%) | `[18OH2]` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Pt]` (0%) | `[Cl][Mn][Cl]` (0%) | set ✓ / any ✓ |

---

### Reaction #968  yield=55.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #9)

```
FC(F)(F)c1ccc([Se][Se]c2ccc(C(F)(F)F)cc2)cc1.C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2cc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (57.6%) | `carbon` (42.2%) | `ABSENT` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (63.8%) | `carbon_rod` (29.6%) | `platinum_generic` (3.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.5%) | `carbon` (0.5%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.1%) | `platinum_generic` (1.7%) | `reticulated_vitreous_carbon` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (71.4%) | `ABSENT` (26.9%) | `Li` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (63.1%) | `ABSENT` (29.3%) | `I` (5.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (6.8%) | `o2_oxidant` (5.4%) | `water` (5.1%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.8%) | `ABSENT` (7.6%) | `halogenated_aliphatic` (1.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCl` (0%) | `FC(F)(F)c1ccccc1` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #969  yield=51.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #10)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCCOC(=O)c1ccccc1C>>Cc1ccccc1C(=O)OCCC(O)C[Se]c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (81.2%) | `carbon` (18.6%) | `ABSENT` (0.2%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_generic` (44.1%) | `platinum_plate` (37.8%) | `graphite_plate` (5.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.7%) | `carbon` (0.2%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (75.2%) | `platinum_generic` (24.1%) | `nickel_rod` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.3%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.2%) | `ABSENT` (13.1%) | `Li` (8.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `I` (43.5%) | `BF4` (42.4%) | `ABSENT` (10.3%) | ✓ |
| 试剂大类 | 103 | `water` | `water` (26.5%) | `as_solvent_halogenated_aliphat` (18.8%) | `o2_oxidant` (5.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.2%) | `ammonium_PTC_organocat` (0.8%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.7%) | `halogenated_aliphatic` (1.0%) | `nitroalkane` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `CO` (1%) | `C[N+](=O)[O-]` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (97%) | `[18OH2]` (2%) | `CO` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CCCC[N+](CCCC)(CCC` (0%) | `O=C1c2ccccc2C(=O)N` (0%) | set ✓ / any ✓ |

---

### Reaction #970  yield=57.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #11)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCC(C)OC(=O)NS(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OC(C)CC(O)C[Se]c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (65.8%) | `platinum` (32.3%) | `ABSENT` (1.5%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_generic` (25.4%) | `carbon_rod` (23.8%) | `unknown_electrode` (13.5%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.5%) | `carbon` (0.8%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (50.2%) | `platinum_plate` (48.5%) | `reticulated_vitreous_carbon` (0.6%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.1%) | `divided` (0.1%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (64.7%) | `ABSENT` (29.2%) | `Li` (4.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (88.6%) | `ABSENT` (9.3%) | `I` (0.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `water` (22.2%) | `ABSENT` (6.8%) | `o2_oxidant` (2.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.3%) | `organic_neutral_cat` (0.3%) | `ionic_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (95.4%) | `polar_protic_alcohol` (3.8%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (70%) | `CO` (29%) | `ClCCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (75%) | `CCN(CC)CC.F.F.F` (1%) | `N` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `O=C1c2ccccc2C(=O)N` (0%) | set ✓ / any ✓ |

---

### Reaction #971  yield=69.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #12)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCC(OC(=O)NS(=O)(=O)c1ccc(C)cc1)c1ccc(Br)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OC(CC(O)C[Se]c2ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (97.0%) | `platinum` (2.8%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (76.7%) | `carbon_rod` (7.9%) | `graphite_rod` (6.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `carbon` (0.3%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (96.3%) | `platinum_plate` (3.6%) | `ABSENT` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `ABSENT` (66.6%) | `undivided` (33.4%) | `divided` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (89.9%) | `ABSENT` (9.6%) | `Li` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (86.6%) | `ABSENT` (11.3%) | `PF6` (1.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (16.5%) | `water` (6.1%) | `metal_oxide_oxidant` (2.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (98.0%) | `polar_protic_alcohol` (1.2%) | `halogenated_aliphatic` (0.4%) | ✗ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (100%) | `CO` (0%) | `ClCCl` (0%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `CC[N+](CC)(CC)CC.F` (0%) | set ✓ / any ✓ |

---

### Reaction #972  yield=68.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #13)

```
C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1.Cc1ccc([Se][Se]c2ccc(C)c(C)c2)cc1C>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2ccc(C)c(C)c2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (71.4%) | `carbon` (28.6%) | `sacrificial_magnesium` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (70.3%) | `carbon_rod` (28.5%) | `platinum_generic` (0.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.6%) | `platinum_generic` (0.4%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (80.4%) | `NBu4` (18.7%) | `Li` (0.7%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (69.1%) | `BF4` (20.0%) | `I` (10.6%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `water` (9.8%) | `ABSENT` (8.8%) | `as_solvent_halogenated_aliphat` (4.1%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `ABSENT` (0.3%) | `halogenated_aliphatic` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `ClCCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (61%) | `__ABSENT__` (5%) | `CO` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `[Br-][Ni+2]1([Br-]` (0%) | set ✓ / any ✓ |

---

### Reaction #973  yield=64.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #14)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCCOC(=O)c1ccc(C)cc1>>Cc1ccc(C(=O)OCCC(O)C[Se]c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (82.2%) | `carbon` (17.7%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (67.1%) | `platinum_generic` (12.7%) | `graphite_plate` (7.7%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.1%) | `carbon` (0.9%) | `nickel` (0.1%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (94.8%) | `platinum_generic` (4.7%) | `platinum_wire` (0.2%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (74.6%) | `Li` (12.7%) | `ABSENT` (11.2%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (52.5%) | `I` (32.2%) | `ABSENT` (10.2%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `as_solvent_halogenated_aliphat` (37.3%) | `water` (9.9%) | `ABSENT` (4.5%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.7%) | `ammonium_PTC_organocat` (0.2%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ABSENT` | `polar_aprotic_nitrile` (97.2%) | `ABSENT` (1.2%) | `halogenated_aliphatic` (0.7%) | ✓ |
| 溶剂 set | 79 | `__ABSENT__` | `CC#N` (97%) | `CC(=O)O` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 试剂 set | 545 | `O` | `OCCBr` (96%) | `O` (46%) | `O=P([O-])([O-])[O-` (42%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #974  yield=66.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #15)

```
Clc1ccc([Se][Se]c2ccc(Cl)cc2)cc1.C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2ccc(Cl)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (91.5%) | `carbon` (8.5%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (79.0%) | `platinum_generic` (11.3%) | `carbon_rod` (8.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (100.0%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (95.2%) | `platinum_generic` (4.8%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.7%) | `ABSENT` (6.0%) | `Li` (1.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (94.1%) | `ABSENT` (3.5%) | `I` (1.7%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `water` (7.5%) | `ABSENT` (6.8%) | `as_solvent_halogenated_aliphat` (5.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.1%) | `halogenated_aliphatic` (0.4%) | `ABSENT` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `OC(C(F)(F)F)C(F)(F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (78%) | `__ABSENT__` (1%) | `CO` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #975  yield=79.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #16)

```
Cc1ccc([Se][Se]c2ccc(C)cc2)cc1.C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1>>Cc1ccc([Se]CC(O)CCOC(=O)NS(=O)(=O)c2ccc(C)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (78.0%) | `carbon` (21.9%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (67.3%) | `carbon_rod` (26.3%) | `platinum_generic` (2.9%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.5%) | `platinum_generic` (1.5%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (88.8%) | `ABSENT` (8.8%) | `Li` (1.7%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (86.8%) | `I` (8.5%) | `ABSENT` (4.0%) | ✓ |
| 试剂大类 | 103 | `water` | `water` (20.0%) | `as_solvent_halogenated_aliphat` (5.4%) | `ABSENT` (4.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `Mn_complex` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.7%) | `ABSENT` (2.6%) | `halogenated_aliphatic` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCCl` (0%) | `O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (91%) | `O=O` (1%) | `CO` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[I-].[K+]` (0%) | set ✓ / any ✓ |

---

### Reaction #976  yield=75.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #17)

```
Cc1ccccc1[Se][Se]c1ccccc1C.C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2ccccc2C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.4%) | `platinum` (19.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (38.9%) | `carbon_rod` (26.7%) | `reticulated_vitreous_carbon` (13.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.7%) | `platinum_generic` (1.3%) | `platinum_wire` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (92.6%) | `ABSENT` (5.8%) | `Li` (1.4%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (92.4%) | `ABSENT` (4.2%) | `ClO4` (2.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `water` (9.6%) | `as_solvent_halogenated_aliphat` (9.4%) | `ABSENT` (5.0%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `Mn_complex` (0.0%) | `ammonium_PTC_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.6%) | `polar_protic_alcohol` (0.1%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `CC(=O)O` (0%) | `ClCCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (68%) | `O=P([O-])([O-])[O-` (1%) | `O=O` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #977  yield=78.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #18)

```
Brc1ccc([Se][Se]c2ccc(Br)cc2)cc1.C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2ccc(Br)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (84.2%) | `carbon` (15.7%) | `ABSENT` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (58.9%) | `platinum_generic` (34.2%) | `carbon_rod` (4.4%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (73.8%) | `platinum_generic` (26.1%) | `platinum_wire` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.5%) | `ABSENT` (0.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (97.4%) | `ABSENT` (1.5%) | `Li` (1.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (91.2%) | `I` (6.7%) | `ABSENT` (1.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `water` (23.2%) | `ABSENT` (7.2%) | `as_solvent_halogenated_aliphat` (5.3%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.7%) | `ABSENT` (0.8%) | `halogenated_aliphatic` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `C1CCOC1` (0%) | `ClCCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (90%) | `[18OH2]` (1%) | `__ABSENT__` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #978  yield=77.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #19)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCC(OC(=O)NS(=O)(=O)c1ccc(C)cc1)c1ccc(Cl)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OC(CC(O)C[Se]c2ccccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.4%) | `platinum` (0.6%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_generic` | `carbon_generic` (82.6%) | `carbon_rod` (12.3%) | `graphite_rod` (2.0%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (80.5%) | `platinum_plate` (19.4%) | `carbon_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (72.2%) | `ABSENT` (27.8%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (72.2%) | `NBu4` (27.5%) | `Li` (0.1%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (57.3%) | `BF4` (42.3%) | `PF6` (0.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (16.1%) | `water` (3.7%) | `metal_oxide_oxidant` (2.3%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (98.9%) | `ferrocene_mediator` (0.3%) | `Fe_complex` (0.2%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (97.9%) | `polar_protic_alcohol` (1.8%) | `ketone` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `CO` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Fe+2].c1cc[cH-]c1` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✓ / any ✓ |

---

### Reaction #979  yield=77.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #20)

```
c1ccc2c([Se][Se]c3cccc4ccccc34)cccc2c1.C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2cccc3ccc…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (72.2%) | `platinum` (27.8%) | `sacrificial_magnesium` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (55.8%) | `carbon_rod` (32.1%) | `platinum_generic` (3.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.0%) | `platinum_generic` (2.0%) | `platinum_wire` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (95.8%) | `ABSENT` (3.2%) | `Li` (0.9%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (93.5%) | `ABSENT` (3.3%) | `ClO4` (1.5%) | ✓ |
| 试剂大类 | 103 | `water` | `as_solvent_halogenated_aliphat` (5.9%) | `ABSENT` (4.8%) | `o2_oxidant` (2.6%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `triarylamine_radical_cat` (0.0%) | `ferrocene_mediator` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.6%) | `halogenated_aliphatic` (0.2%) | `ABSENT` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `FC(F)(F)c1ccccc1` (0%) | `C1CCOC1` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (48%) | `C[Si](C)(C)N=[N+]=` (6%) | `[Pt]` (3%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #980  yield=88.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #21)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCC(OC(=O)NS(=O)(=O)c1ccc(C)cc1)c1ccc(OC)cc1>>COc1ccc(C(CC(O)C[Se]c2ccccc2)OC(=O)NS(=O)(…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.0%) | `platinum` (0.8%) | `ABSENT` (0.2%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_generic` (42.4%) | `carbon_rod` (40.7%) | `graphite_rod` (8.0%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.6%) | `carbon` (0.9%) | `sacrificial_iron` (0.2%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_generic` (75.1%) | `platinum_plate` (24.7%) | `carbon_generic` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (63.5%) | `ABSENT` (36.5%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `ABSENT` (90.2%) | `NBu4` (9.5%) | `Li` (0.1%) | ✓ |
| 电解质 anion | 26 | `BF4` | `ABSENT` (84.0%) | `BF4` (15.4%) | `Cl` (0.2%) | ✓ |
| 试剂大类 | 103 | `water` | `ABSENT` (18.2%) | `water` (5.7%) | `as_solvent_polar_protic_alcoho` (3.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.2%) | `polar_protic_alcohol` (2.8%) | `cyclic_ether` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `CO` (1%) | `CC(C)=O` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Br-][Ni+2]1([Br-]` (0%) | `[cH]12->[Fe+2]3456` (0%) | set ✓ / any ✓ |

---

### Reaction #981  yield=87.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #22)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCC(OC(=O)NS(=O)(=O)c1ccc(C)cc1)c1ccccc1>>Cc1ccc(S(=O)(=O)NC(=O)OC(CC(O)C[Se]c2ccccc2)c2…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (95.8%) | `platinum` (3.8%) | `ABSENT` (0.3%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (49.8%) | `carbon_generic` (29.0%) | `graphite_rod` (10.6%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (98.1%) | `carbon` (0.7%) | `nickel` (0.6%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (54.1%) | `platinum_generic` (45.4%) | `carbon_generic` (0.1%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (82.1%) | `ABSENT` (17.9%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (77.3%) | `ABSENT` (22.0%) | `Li` (0.3%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (87.7%) | `ABSENT` (11.5%) | `PF6` (0.4%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (12.7%) | `water` (8.9%) | `metal_oxide_oxidant` (2.2%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.9%) | `ammonium_PTC_organocat` (0.1%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (90.3%) | `polar_protic_alcohol` (8.4%) | `polar_aprotic_amide` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `CO` (1%) | `ClCCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (99%) | `O` (0%) | `CCN(CC)CC.F.F.F` (0%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `O=C1c2ccccc2C(=O)N` (0%) | `CCCC[N+](CCCC)(CCC` (0%) | set ✓ / any ✓ |

---

### Reaction #982  yield=85.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #23)

```
C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1.c1ccc(Oc2ccc([Se][Se]c3ccc(Oc4ccccc4)cc3)cc2)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]…
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (58.8%) | `carbon` (41.2%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `platinum_plate` (71.1%) | `carbon_rod` (19.6%) | `graphite_plate` (7.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.3%) | `platinum_generic` (0.7%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.9%) | `ABSENT` (0.1%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.2%) | `ABSENT` (14.7%) | `Li` (0.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (85.3%) | `ABSENT` (10.6%) | `I` (3.3%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `o2_oxidant` (19.3%) | `water` (12.1%) | `ABSENT` (5.8%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `ferrocene_mediator` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.4%) | `ABSENT` (0.9%) | `halogenated_aliphatic` (0.3%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `CO` (0%) | `ClCCCl` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O=O` (25%) | `O` (5%) | `__ABSENT__` (2%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #983  yield=89.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #24)

```
COc1ccc([Se][Se]c2ccc(OC)cc2)cc1.C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1>>COc1ccc([Se]CC(O)CCOC(=O)NS(=O)(=O)c2ccc(C)cc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `platinum` (52.1%) | `carbon` (47.8%) | `ABSENT` (0.1%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (50.0%) | `platinum_plate` (46.9%) | `graphite_rod` (1.1%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.0%) | `platinum_generic` (2.0%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (82.0%) | `ABSENT` (16.1%) | `Li` (1.5%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (86.3%) | `ABSENT` (9.1%) | `I` (4.0%) | ✓ |
| 试剂大类 | 103 | `water` | `water` (19.9%) | `ABSENT` (6.8%) | `as_solvent_halogenated_aliphat` (3.2%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `organic_neutral_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (96.8%) | `ABSENT` (3.0%) | `halogenated_aliphatic` (0.2%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `C1CCOC1` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (71%) | `CO` (1%) | `__ABSENT__` (1%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `[Fe+2].c1cc[cH-]c1` (0%) | set ✓ / any ✓ |

---

### Reaction #984  yield=81.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #25)

```
COc1ccccc1[Se][Se]c1ccccc1OC.C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1>>COc1ccccc1[Se]CC(O)CCOC(=O)NS(=O)(=O)c1ccc(C)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (93.8%) | `platinum` (6.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `graphite_plate` (81.9%) | `reticulated_vitreous_carbon` (5.7%) | `platinum_plate` (5.6%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.4%) | `carbon` (0.5%) | `sacrificial_iron` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.2%) | `platinum_generic` (0.7%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.7%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `ABSENT` (68.2%) | `NBu4` (25.4%) | `Li` (6.0%) | ✓ (T1✓) |
| 电解质 anion | 26 | `ABSENT` | `ABSENT` (65.1%) | `BF4` (29.2%) | `molecular_no_ion` (2.9%) | ✓ (T1✓) |
| 试剂大类 | 103 | `water` | `ABSENT` (7.5%) | `as_solvent_halogenated_aliphat` (4.3%) | `metal_oxide_oxidant` (2.3%) | ✗ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (99.8%) | `Mn_complex` (0.1%) | `ammonium_PTC_organocat` (0.1%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.2%) | `ABSENT` (0.6%) | `polar_protic_alcohol` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `ClCCCl` (0%) | `CCCCO` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `__ABSENT__` (100%) | `CC(=O)O` (0%) | `O=P([O-])([O-])[O-` (0%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[Cl][Mn][Cl]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #985  yield=81.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #26)

```
Cc1cccc([Se][Se]c2cccc(C)c2)c1.C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2cccc(C)c2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (86.2%) | `platinum` (13.8%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (78.6%) | `platinum_plate` (17.2%) | `graphite_plate` (2.1%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.9%) | `carbon` (0.0%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (99.7%) | `platinum_generic` (0.3%) | `reticulated_vitreous_carbon` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (100.0%) | `ABSENT` (0.0%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `ABSENT` | `NBu4` (95.9%) | `ABSENT` (3.7%) | `Li` (0.2%) | ✓ |
| 电解质 anion | 26 | `ABSENT` | `BF4` (74.5%) | `I` (20.7%) | `ABSENT` (4.3%) | ✓ |
| 试剂大类 | 103 | `water` | `water` (6.7%) | `ABSENT` (5.9%) | `as_solvent_halogenated_aliphat` (4.4%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `triarylamine_radical_cat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (99.5%) | `ABSENT` (0.4%) | `halogenated_aliphatic` (0.1%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (100%) | `FC(F)(F)c1ccccc1` (0%) | `OC(C(F)(F)F)C(F)(F` (0%) | set ✓ / any ✓ |
| 试剂 set | 545 | `O` | `O` (43%) | `O=O` (1%) | `CO` (1%) | set ✗ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `[I-].[K+]` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #986  yield=81.0%

**Source paper**: [`ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json`](reactions_by_journal_alkene_ec_audited/ChemistrySelect/2025_ChemistrySelect_2025_10_34_e03086.json) (反应 idx 在该 JSON 内 = #27)

```
c1ccc([Se][Se]c2ccccc2)cc1.C=CCCOC(=O)NS(=O)(=O)c1ccc(C)cc1.O>>Cc1ccc(S(=O)(=O)NC(=O)OCCC(O)C[Se]c2ccccc2)cc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (80.9%) | `platinum` (19.1%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (45.6%) | `graphite_plate` (22.1%) | `platinum_plate` (19.2%) | ✗ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `nickel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_plate` | `platinum_plate` (98.4%) | `platinum_generic` (1.6%) | `graphite_rod` (0.0%) | ✓ (T1✓) |
| 池型 | 4 | `undivided` | `undivided` (99.8%) | `ABSENT` (0.2%) | `divided` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (96.2%) | `ABSENT` (2.4%) | `Li` (0.5%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `BF4` (94.0%) | `I` (4.1%) | `ABSENT` (1.1%) | ✓ (T1✓) |
| 试剂大类 | 103 | `ABSENT` | `water` (16.1%) | `ABSENT` (6.9%) | `as_solvent_halogenated_aliphat` (4.4%) | ✓ |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `ammonium_PTC_organocat` (0.0%) | `nhpi_mediator` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.0%) | `polar_protic_alcohol` (0.9%) | `ABSENT` (0.5%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (99%) | `ClCCCl` (1%) | `CO` (1%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `O` (88%) | `[18OH2]` (3%) | `CO` (1%) | set ✗ / any ✗ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `CC[N+](CC)(CC)CC.F` (0%) | `c1ccncc1` (0%) | set ✓ / any ✓ |

---

### Reaction #987  yield=47.0%

**Source paper**: [`ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CS(=O)(=O)n1cc(-c2ccccc2)nn1.C=C(c1ccccc1)c1ccccc1.O>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (98.6%) | `graphite_rod` (0.9%) | `graphite_plate` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.4%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.3%) | `K` (7.2%) | `Li` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (35.6%) | `PF6` (21.3%) | `carboxylate` (14.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.3%) | `boron_lewis_acid` (3.0%) | `o2_oxidant` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `halogenated_aliphatic` (0.4%) | `ketone` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (19%) | `O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #988  yield=89.0%

**Source paper**: [`ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CS(=O)(=O)n1cc(-c2ccccc2)nn1.C=C(c1ccccc1)c1ccccc1.O>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (98.6%) | `graphite_rod` (0.9%) | `graphite_plate` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.4%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.3%) | `K` (7.2%) | `Li` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (35.6%) | `PF6` (21.3%) | `carboxylate` (14.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.3%) | `boron_lewis_acid` (3.0%) | `o2_oxidant` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `halogenated_aliphatic` (0.4%) | `ketone` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (19%) | `O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #989  yield=61.0%

**Source paper**: [`ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CS(=O)(=O)n1cc(-c2ccccc2)nn1.C=C(c1ccccc1)c1ccccc1.O>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (98.6%) | `graphite_rod` (0.9%) | `graphite_plate` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.4%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.3%) | `K` (7.2%) | `Li` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (35.6%) | `PF6` (21.3%) | `carboxylate` (14.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.3%) | `boron_lewis_acid` (3.0%) | `o2_oxidant` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `halogenated_aliphatic` (0.4%) | `ketone` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (19%) | `O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #990  yield=75.0%

**Source paper**: [`ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CS(=O)(=O)n1cc(-c2ccccc2)nn1.C=C(c1ccccc1)c1ccccc1.O>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (98.6%) | `graphite_rod` (0.9%) | `graphite_plate` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.4%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.3%) | `K` (7.2%) | `Li` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (35.6%) | `PF6` (21.3%) | `carboxylate` (14.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.3%) | `boron_lewis_acid` (3.0%) | `o2_oxidant` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `halogenated_aliphatic` (0.4%) | `ketone` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (19%) | `O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #991  yield=0.0%

**Source paper**: [`ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CS(=O)(=O)n1cc(-c2ccccc2)nn1.C=C(c1ccccc1)c1ccccc1.O>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `platinum` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (98.6%) | `graphite_rod` (0.9%) | `graphite_plate` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.4%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.3%) | `K` (7.2%) | `Li` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (35.6%) | `PF6` (21.3%) | `carboxylate` (14.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.3%) | `boron_lewis_acid` (3.0%) | `o2_oxidant` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `halogenated_aliphatic` (0.4%) | `ketone` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (19%) | `O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #992  yield=0.0%

**Source paper**: [`ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CS(=O)(=O)n1cc(-c2ccccc2)nn1.C=C(c1ccccc1)c1ccccc1.O>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (98.6%) | `graphite_rod` (0.9%) | `graphite_plate` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.4%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.3%) | `K` (7.2%) | `Li` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (35.6%) | `PF6` (21.3%) | `carboxylate` (14.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.3%) | `boron_lewis_acid` (3.0%) | `o2_oxidant` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `halogenated_aliphatic` (0.4%) | `ketone` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (19%) | `O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #993  yield=36.0%

**Source paper**: [`ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CS(=O)(=O)n1cc(-c2ccccc2)nn1.C=C(c1ccccc1)c1ccccc1.O>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (98.6%) | `graphite_rod` (0.9%) | `graphite_plate` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.4%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.3%) | `K` (7.2%) | `Li` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (35.6%) | `PF6` (21.3%) | `carboxylate` (14.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.3%) | `boron_lewis_acid` (3.0%) | `o2_oxidant` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `ketone` | `polar_aprotic_nitrile` (98.5%) | `halogenated_aliphatic` (0.4%) | `ketone` (0.4%) | ✓ |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (19%) | `O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #994  yield=38.0%

**Source paper**: [`ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CS(=O)(=O)n1cc(-c2ccccc2)nn1.C=C(c1ccccc1)c1ccccc1.O>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (98.6%) | `graphite_rod` (0.9%) | `graphite_plate` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.4%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.3%) | `K` (7.2%) | `Li` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `BF4` | `ClO4` (35.6%) | `PF6` (21.3%) | `carboxylate` (14.5%) | ✗ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.3%) | `boron_lewis_acid` (3.0%) | `o2_oxidant` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `halogenated_aliphatic` (0.4%) | `ketone` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (19%) | `O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #995  yield=74.0%

**Source paper**: [`ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CS(=O)(=O)n1cc(-c2ccccc2)nn1.C=C(c1ccccc1)c1ccccc1.O>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (98.6%) | `graphite_rod` (0.9%) | `graphite_plate` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `undivided` | `undivided` (98.6%) | `ABSENT` (1.4%) | `flow` (0.0%) | ✓ (T1✓) |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.3%) | `K` (7.2%) | `Li` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (35.6%) | `PF6` (21.3%) | `carboxylate` (14.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.3%) | `boron_lewis_acid` (3.0%) | `o2_oxidant` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `halogenated_aliphatic` (0.4%) | `ketone` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (19%) | `O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #996  yield=0.5%

**Source paper**: [`ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CS(=O)(=O)n1cc(-c2ccccc2)nn1.C=C(c1ccccc1)c1ccccc1.O>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (98.6%) | `graphite_rod` (0.9%) | `graphite_plate` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (98.6%) | `ABSENT` (1.4%) | `flow` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.3%) | `K` (7.2%) | `Li` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (35.6%) | `PF6` (21.3%) | `carboxylate` (14.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.3%) | `boron_lewis_acid` (3.0%) | `o2_oxidant` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `halogenated_aliphatic` (0.4%) | `ketone` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (19%) | `O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #997  yield=0.0%

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

### Reaction #998  yield=15.0%

**Source paper**: [`ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json`](reactions_by_journal_alkene_ec_audited/ChinChemLett/10.1016_j.cclet.2025.110822_sup_1_p15_t0.json) (反应 idx 在该 JSON 内 = #0)

```
CS(=O)(=O)n1cc(-c2ccccc2)nn1.C=C(c1ccccc1)c1ccccc1.O>>OC(Cn1ncc(-c2ccccc2)n1)(c1ccccc1)c1ccccc1
```

| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |
|------|------|----|---------------|-------|-------|-----|
| 阳极 (材料) | 15 | `carbon` | `carbon` (99.5%) | `platinum` (0.5%) | `ABSENT` (0.0%) | ✓ (T1✓) |
| 阳极 (细类) | 43 | `graphite_rod` | `carbon_rod` (98.6%) | `graphite_rod` (0.9%) | `graphite_plate` (0.2%) | ✓ |
| 阴极 (材料) | 15 | `platinum` | `platinum` (99.8%) | `carbon` (0.1%) | `stainless_steel` (0.0%) | ✓ (T1✓) |
| 阴极 (细类) | 49 | `platinum_generic` | `platinum_plate` (100.0%) | `platinum_generic` (0.0%) | `graphite_rod` (0.0%) | ✓ |
| 池型 | 4 | `ABSENT` | `undivided` (98.6%) | `ABSENT` (1.4%) | `flow` (0.0%) | ✓ |
| 电解质 cation | 23 | `NBu4` | `NBu4` (84.3%) | `K` (7.2%) | `Li` (3.9%) | ✓ (T1✓) |
| 电解质 anion | 26 | `carboxylate` | `ClO4` (35.6%) | `PF6` (21.3%) | `carboxylate` (14.5%) | ✓ |
| 试剂大类 | 103 | `ABSENT` | `ABSENT` (14.3%) | `boron_lewis_acid` (3.0%) | `o2_oxidant` (2.5%) | ✓ (T1✓) |
| 催化剂大类 | 49 | `ABSENT` | `ABSENT` (100.0%) | `organic_neutral_cat` (0.0%) | `pyridine_organocat` (0.0%) | ✓ (T1✓) |
| 溶剂大类 | 27 | `polar_aprotic_nitrile` | `polar_aprotic_nitrile` (98.5%) | `halogenated_aliphatic` (0.4%) | `ketone` (0.4%) | ✓ (T1✓) |
| 溶剂 set | 79 | `CC#N` | `CC#N` (98%) | `ClCCl` (19%) | `O` (3%) | set ✓ / any ✓ |
| 试剂 set | 545 | `__ABSENT__` | `__ABSENT__` (100%) | `CCN(CC)CC.F.F.F` (0%) | `O` (0%) | set ✓ / any ✓ |
| 催化剂 set | 526 | `__ABSENT__` | `__ABSENT__` (100%) | `c1ccncc1` (0%) | `Brc1ccc(N(c2ccc(Br` (0%) | set ✓ / any ✓ |

---

### Reaction #999  yield=8.0%

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

### Reaction #1000  yield=0.5%

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

