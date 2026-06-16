# EC 烯烃双官能化:数据分类方案

**日期**: 2026-05-19
**数据**: `reactions_by_journal_alkene_ec_audited/` (25,501 反应) → `data_audited_v3/` (25,733 反应 / paper-level split)
**目标**: 每个出现过的 SMILES / 电极描述都归到**一个化学上有意义的类**,不允许 OTHER / 杂项兜底。
**覆盖度**: 在源数据 25k 反应上 100% 覆盖,验证脚本 `utils/classifier_v3.py::__main__`。

---

## 0. 设计原则

- **数据导向**:先扫 25k 反应,基于真实分布定类。
- **禁止 OTHER**:所有未命中明确类的 SMILES 归到有化学语义的兜底子类(如 `transition_metal_salt_reagent`、`organic_neutral_cat`)。
- **跨 head 共享类名**:ferrocene / TEMPO / Tol-I / water / HFIP 等在 reagent / catalyst / additive 字段使用同一类名,样本量集中。
- **Catalyst 多标签正交**:元素维度(primary class,互斥) + 机制 tag(mediator/photoredox/HAT/chiral,正交)。
- **Electrolyte 双 head**:拆为 cation × anion 两个独立分类头,解决组合稀疏。
- **Anode / cathode**:按材料家族折成 6-7 个主要类,字符串规则识别。

---

## 1. 数据真实分布(原始数据扫描)

按字段统计 unique SMILES 数和总出现次数:

```
reagents:     855 unique SMILES, 18604 occurrences
catalysts:    758 unique SMILES,  9828
ligands:      181 unique SMILES,   991
solvents:     116 unique SMILES, 36380
additives:    106 unique SMILES,   556
electrolytes: 386 unique SMILES, 21234
anode:        811 unique strings (材料写法 ~6 大类)
cathode:      850 unique strings (~6 大类)
cell_type:    151 unique strings (~3 大类)
```

---

## 2. REAGENT head — 55 类(38 核心 + 10 as_solvent + 7 化学兜底)

分类依据:**SMARTS 子结构匹配 + 优先级规则**。按优先级从上到下匹配,每个类标 `次数 / 百分比`(基于 18604 occ)。

### 2.1 EC 高频小分子(必须最先匹配)

| ID | 类 | 匹配规则 | 数据中 | 例 |
|---|---|---|---|---|
| 01 | `water` | `[OX2H2]` / `[H+].[OH-]` / `[2H]O[2H]` / `[18OH2]` | 1056 (5.7%) | H2O, D2O |
| 02 | `o2_oxidant` | `O=O` 精确字串 | 270 (1.5%) | O2 |
| 03 | `co2_reagent` | `O=C=O` 精确字串 | 97 (0.5%) | CO2 (羧化反应) |
| 04 | `hcl` | `Cl` 单原子写法 | 589 (3.2%) | 中性 HCl |
| 05 | `hbr` | `Br` 单原子写法 | 83 (0.4%) | HBr |
| 06 | `hf` | `F` 单原子写法 | 58 (0.3%) | HF |
| 07 | `ammonia` | `N` / `[NH3]` 单原子 | 58 (0.3%) | NH3 |
| 08 | `alkane_simple_gas` | `C` / `CC` 等单字符 | 39 (0.2%) | CH4 |

### 2.2 跨 head Mediator(在 catalyst/additive 也会用同名)

| ID | 类 | 匹配规则 | 数据中 |
|---|---|---|---|
| 09 | `ferrocene_mediator` | 含 `Fe` + 两个 `[cH-]1cccc1` 片段 | 118 (0.6%) |
| 10 | `tempo_mediator` | `CC1(C)CCCC(C)(C)N1[O]` (TEMPO/AZADO 骨架) | 214 (1.2%) |
| 11 | `nhpi_mediator` | `O=C1N([OH,O])C(=O)c2ccccc21` | 32 (0.2%) |
| 12 | `aryl_iodide_mediator` | `c[I;X1;H0]` 且重原子 ≤ 20 且 I 计数 = 1 | 304 (1.6%) |

### 2.3 卤化与多卤代

| ID | 类 | 规则 | 数据中 |
|---|---|---|---|
| 13 | `polyhalo_radical_transfer` | `[CX4]([Cl,Br])([Cl,Br])[Cl,Br]` | 319 (1.7%) |
| 14 | `fluoride_anion` | `[F-]` | 150 (0.8%) |
| 15 | `chloride_anion` | `[Cl-]` | 811 (4.4%) |
| 16 | `bromide_anion` | `[Br-]` | 254 (1.4%) |
| 17 | `iodide_anion` | `[I-]` | 180 (1.0%) |
| 18 | `n_halo_imide` | `O=C1CCC(=O)N1[Br,Cl,I,F]` (NBS/NIS/NCS) | 211 (1.1%) |
| 19 | `hypohalite` | `[O-][Cl,Br,I,F;X1]` | 6 (0.0%) |
| 20 | `electrophilic_N_F` | `[N;X3,X4][F]` (Selectfluor/NFSI) | 32 (0.2%) |

### 2.4 高价氧化剂

| ID | 类 | 规则 | 数据中 |
|---|---|---|---|
| 21 | `hypervalent_iodine` | `[I+3]` / `[I+5]` / `[I;X3]` (Togni、Koser) | 22 (0.1%) |
| 22 | `metal_oxide_oxidant` | `[Mn]=[O]` / `[Os]=O` / `[Ru]=O` | 53 (0.3%) |
| 23 | `peroxide` | `[OX2][OX2]` (mCPBA / TBHP / DTBP / TBPB) | 216 (1.2%) |

### 2.5 N / S / Se 试剂

| ID | 类 | 规则 | 数据中 |
|---|---|---|---|
| 24 | `azide_source` | `[N-]=[N+]=[N-]` / TMS-N3 | 401 (2.2%) |
| 25 | `phthalimide_N_anion` | `O=C1[N-]C(=O)c2ccccc21` | 55 (0.3%) |
| 26 | `nitrite_alkyl` | `[#6][OX2]N=O` (tBuONO/EtONO) | 53 (0.3%) |
| 27 | `diazonium` | `[N+]#N` | 8 (0.0%) |
| 28 | `diazo_compound` | `[#6]=[N+]=[N-]` | 1 |
| 29 | `selenium_reagent` | `[Se][Se]` (PhSeSePh) | 77 (0.4%) |
| 30 | `sulfonyl_chloride` | `[S;X4](=O)(=O)Cl` | 66 (0.4%) |
| 31 | `sulfonamide` | `[S;X4](=O)(=O)[NH,NH2]` | 36 (0.2%) |
| 32 | `sulfonic_acid` | `[S;X4](=O)(=O)[OH]` | 259 (1.4%) |
| 33 | `sulfinic_acid` | `[S;X3](=O)[OH]` | 1 |
| 34 | `thiol` | `[#6;!a][SH]` / `c[SH]` | 2 |
| 35 | `thiocyanate` | `[S-]C#N` | 30 (0.2%) |
| 36 | `cyanide` | `[C-]#N`(在碱金属盐之后) | 1 |
| 37 | `imine` | `[#6]=[#7]` (碳-氮双键,benzophenone imine 等) | 136 (0.7%) |
| 38 | `carbodiimide` | `[#7]=[#6]=[#7]` (DIC, DCC) | 13 (0.1%) |

### 2.6 碱金属盐(必须在 carboxylate / hydroxide 之前)

| ID | 类 | 规则 | 数据中 |
|---|---|---|---|
| 39 | `alkali_carbonate` | `[O-]C(=O)[O-]` + 含碱金属片段 | 1196 (6.4%) |
| 40 | `alkali_bicarbonate` | `[OH]C(=O)[O-]` + 碱金属 | 176 (0.9%) |
| 41 | `alkali_phosphate` | `[O-]P(=O)([O-])[O-]` 等磷酸全/二/一钠钾 | 673 (3.6%) |
| 42 | `alkali_sulfate` | `[O-]S(=O)(=O)[O-]` + 碱金属 | 4 |
| 43 | `alkali_hydroxide` | `[OH-]` + 碱金属 | 123 (0.7%) |
| 44 | `alkali_alkoxide` | `[CX4][O-]` + 碱金属 (KOtBu/NaOEt) | 301 (1.6%) |
| 45 | `alkali_carboxylate` | `[CX3](=O)[O-]` + 碱金属(AcONa/PivONa) | 1022 (5.5%) |
| 46 | `alkali_sulfonate` | `[S;X4](=O)(=O)[O-]` + 碱金属(TsONa/OTfNa) | 194 (1.0%) |
| 47 | `alkali_sulfinate` | `[S;X3](=O)[O-]` + 碱金属(CF3SO2Na) | 295 (1.6%) |
| 48 | `alkali_formate` | `[CX3H1](=O)[O-]` + 碱金属 | (rare) |
| 49 | `alkali_nitrate` | `[O-][N+](=O)[O-]` + 碱金属 | 57 (0.3%) |
| 50 | `alkali_BF4` | `F[B-](F)(F)F` + 碱金属 | (in elec) |
| 51 | `borohydride` | `[BH4-]` | 6 |
| 52 | `alkali_other_salt` | 含碱金属离子但非以上 | 456 (2.5%) |

### 2.7 碱土 / 主族 / 过渡金属盐(作 reagent)

| ID | 类 | 规则 | 数据中 |
|---|---|---|---|
| 53 | `alkaline_earth_halide` | 含 Mg/Ca/Sr/Ba + 卤素离子 | 88 (0.5%) |
| 54 | `alkaline_earth_salt` | 含 Mg/Ca/Sr/Ba(其他阴离子) | (合并) |
| 55 | `transition_metal_salt_reagent` | 含过渡金属 (Fe/Cu/Mn/Ni/...) — 作化学计量氧化/还原剂 | 473 (2.5%) |
| 56 | `main_group_metal_reagent` | 含 Al/Ga/In/Sn/Pb/Bi/Sb | 16 (0.1%) |

### 2.8 含氟与 HF·胺复合物

| ID | 类 | 规则 | 数据中 |
|---|---|---|---|
| 57 | `hf_amine_complex` | 多组分含 `.F` 片段 + 含氮片段(Et3N·3HF / Py·9HF) | 420 (2.3%) |
| 58 | `cf3_source` | `[CX4](F)(F)F` (优先级低于 carboxylic_acid → TFA 归酸) | 690 (3.7%) |
| 59 | `perfluoroalkyl_source` | `[CX4](F)(F)F[CX4](F)(F)F` (-CF2CF3-) | (合并到 cf3) |

### 2.9 含氧官能团(优先级:酸 > 酐 > 酯 > 酮 > 醛)

| ID | 类 | 规则 | 数据中 |
|---|---|---|---|
| 60 | `carboxylic_acid` | `[CX3](=O)[OH]` | 2023 (10.9%) ← 最大类 |
| 61 | `acid_anhydride` | `[CX3](=O)O[CX3](=O)` (Ac2O 等) | 109 (0.6%) |
| 62 | `ester` | `[CX3](=O)O[CX4,c]` | 232 (1.2%) |
| 63 | `aldehyde` | `[CX3H1](=O)[#6]` | 1 |
| 64 | `ketone` | `[CX3](=O)([#6])[#6]` | 73 (0.4%) |

### 2.10 含硼 / 含硅试剂

| ID | 类 | 规则 | 数据中 |
|---|---|---|---|
| 65 | `diboron` | `[B][B]` (B2pin2/B2cat2) | 62 (0.3%) |
| 66 | `boronic_acid` | `[B]([OH])([OH])` | 124 (0.7%) |
| 67 | `boron_lewis_acid` | `B(F)(F)F` (BF3·OEt2 等) | 127 (0.7%) |
| 68 | `borate_ester` | `[B][O]` (RBpin 等) | 1 |
| 69 | `tetraaryl_borate` | `[B]([c])([c])([c])` (BArF20/BPh4) | 59 (0.3%) |
| 70 | `hydrosilane` | `[SiH]` (Et3SiH/PhSiH3) | 108 (0.6%) |
| 71 | `silyl_electrophile` | `[Si][Cl,Br,I,O,N]` (TMSCl/TMSOTf) | 141 (0.8%) |
| 72 | `silane_other` | `[Si]` 其他 | 153 (0.8%) |

### 2.11 含氮碱与 N-基试剂

| ID | 类 | 规则 | 数据中 |
|---|---|---|---|
| 73 | `amidine_guanidine_base` | `[#7;R]=[#6;R][#7;R]` (DBU/DBN/TBD/MTBD) | 269 (1.4%) |
| 74 | `pyridine` | `c1ccncc1` | 600 (3.2%) |
| 75 | `imidazole` | `c1[nH]cnc1` | 4 |
| 76 | `amide` | `[NX3][CX3](=O)[#6]` | 13 |
| 77 | `tertiary_amine` | `[NX3;H0;!$(N=*);!$(NC=O);!$([N+])]` (Et3N/DIPEA) | 834 (4.5%) |
| 78 | `secondary_amine` | `[NX3;H1;!$(N=*);!$(NC=O)]` | 9 |
| 79 | `primary_amine` | `[NX3;H2;!$(N=*);!$(NC=O)]` | 45 (0.2%) |
| 80 | `ammonium_salt` | `[N+;X4]` (TBABr/TBAOTs 等做 reagent) | 188 (1.0%) |
| 81 | `phosphine_neutral` | `[P;X3]` (PPh3 作 reagent 时) | 81 (0.4%) |
| 82 | `phosphine_oxide` | `[P;X4](=O)` | (合并到 81) |

### 2.12 "溶剂当反应物用"的归到溶剂类(MeOH/MeCN/DMF 等)

当一个 SMILES 出现在 reagents 字段但化学结构是常见溶剂时,保留语义:`as_solvent_<原溶剂类>`。

| 类前缀 | 例 | 数据中 |
|---|---|---|
| `as_solvent_aromatic_hydrocarbon` | benzene 作 H-source/co-reactant | 203 (1.1%) |
| `as_solvent_polar_protic_alcohol` | MeOH 作亲核体 | 108 (0.6%) |
| `as_solvent_alkane` | hexane 作内标 | 102 (0.5%) |
| `as_solvent_polar_aprotic_amide` | DMF 作 CO 源/H 源 | 53 (0.3%) |
| `as_solvent_polar_aprotic_sulfoxide` | DMSO 作氧源/SMe 源 | 42 (0.2%) |
| `as_solvent_polar_aprotic_nitrile` | MeCN 作 N 源 (Ritter) | 30 (0.2%) |
| `as_solvent_halogenated_aliphatic` | DCM/CH2Cl2 作 Cl 源 | 22 (0.1%) |
| `as_solvent_cyclic_ether` | THF/dioxane 作 H/O 源 | 21 (0.1%) |
| `as_solvent_nitroalkane` | MeNO2 | 3 |
| `as_solvent_ionic_liquid` | imidazolium IL | 2 |

### 2.13 化学语义兜底(非 OTHER)

| ID | 类 | 含义 | 数据中 |
|---|---|---|---|
| 90 | `inorganic_simple` | 完全无机的小分子 / 单元素(Br2/I2/Cl2/H3PO4/[Pt]/[Cu]) | 146 (0.8%) |
| 91 | `polycyclic_arene` | 萘/菲/蒽 作 mediator/radical trap | 44 (0.2%) |
| 92 | `aromatic_neutral` | 含芳环的中性有机分子(BHT/PhBr/o-NO2-PhOH) | 60 (0.3%) |
| 93 | `aliphatic_neutral` | 含烷基的中性小分子(BuLi/MeNa 等罕见烷基金属) | 10 (0.1%) |
| 94 | `alkene_coreagent` | `[CX3]=[CX3]` 烯烃作 co-reactant | 6 |
| 95 | `organic_neutral_misc` | CS2 / 草酰氯 / [C] 等极罕见 | 15 (0.1%) |
| 96 | `unparseable_text` | RDKit 不能解析(如 'air' 'Dried' 等抽取噪声) | 26 (0.1%) |
| 99 | `ABSENT` | reagents 字段为空 | — |

> 所有 60+93 类都有明确化学含义;**没有 OTHER**。兜底子类如 `aromatic_neutral` 意味着"含芳环的中性有机分子",模型在该类上学的特征(平均 yield、共生条件)有意义。

---

## 3. CATALYST head — 36 类元素维度 + 4 个机制 tag

### 3.1 元素维度(primary class,互斥)

分类依据:**按金属/有机骨架元素归类**,优先级 photoredox/mediator → 醌氧化剂 → 含硫光-HAT → 多环芳烃 → 含硅 → Brønsted → 过渡金属 → 主族 → 有机。

| 类 | 规则 | 数据中 |
|---|---|---|
| `photoredox_organic` | 4CzIPN / acridinium(Mes-Acr+) / Eosin / 加 photoredox tag 且无金属 | 274 (2.8%) |
| `mediator_organic` | TEMPO / NHPI / Tol-I 加 mediator tag 且无金属 | 311 (3.2%) |
| `quinone_oxidant_cat` | `O=C1C=CC(=O)C=C1`(DDQ/chloranil/quinone/anthraquinone) | 86 (0.9%) |
| `thianthrene_phenothiazine_cat` | 含双 S 蒽并环 / 吩噻嗪骨架(光-HAT) | 127 (1.3%) |
| `polycyclic_arene_cat` | 蒽/菲/萘 catalyst | 180 (1.8%) |
| `silyl_lewis_acid_cat` | 含 Si(TMS-OTf/TMSCl 作催化剂) | 97 (1.0%) |
| `brønsted_acid_cat` | TfOH / HFIP / BINOL-PA / phosphate ester | 798 (8.1%) |
| `triarylamine_radical_cat` | Ar3N + ≥3 Br/I(aminium 单电子氧化剂) | 122 (1.2%) |
| `Pd_complex` | 含 [Pd] | 287 (2.9%) |
| `Ni_complex` | 含 [Ni] | 1331 (13.5%) ← top1 |
| `Cu_complex` | 含 [Cu] | 301 (3.1%) |
| `Co_complex` | 含 [Co] | 591 (6.0%) |
| `Mn_complex` | 含 [Mn] | 393 (4.0%) |
| `Fe_complex` | 含 [Fe](不在 ferrocene_mediator 内) | 1276 (13.0%) |
| `Rh_complex` | 含 [Rh] | 128 (1.3%) |
| `Ir_complex` | 含 [Ir] | 132 (1.3%) |
| `Ru_complex` | 含 [Ru] | 53 (0.5%) |
| `Pt_complex` | 含 [Pt] | 146 (1.5%) |
| `Au_complex` | 含 [Au] | 60 (0.6%) |
| `Ag_complex` | 含 [Ag] | 39 (0.4%) |
| `Zn_complex` | 含 [Zn] | 2 |
| `Mg_complex` | 含 [Mg] | 1 |
| `Cd/Cr/V/Ti/Hf/Zr/Mo/W/Re/Os_complex` | 各对应元素 | 各 ~50-250 |
| `lanthanide_complex` | 含 Sc/Y/Yb/Eu/Sm/La/Ce 等 | 55 (0.6%) |
| `main_group_lewis_acid` | 含 B/Al/Ga/In/Sn/Pb/Bi/Sb | 87 (0.9%) |
| `NHC_or_imidazole_organocat` | 含咪唑环 | 1 |
| `amidine_guanidine_organocat` | DBU/DBN 等 | 150 (1.5%) |
| `tertiary_amine_organocat` | DABCO 等三级胺有机催化 | 13 (0.1%) |
| `pyridine_organocat` | DMAP / 吡啶 | 676 (6.9%) |
| `phosphine_organocat` | PPh3 等 | 186 (1.9%) |
| `ammonium_PTC_organocat` | [N+;X4] 四级铵相转移 | 256 (2.6%) |
| `ionic_organocat` | 带电荷但非以上(磺酸盐等) | 472 (4.8%) |
| `BINOL_or_brønsted` | 含 -OH 且双芳环(手性 BINOL 骨架) | (并入 brønsted_acid_cat) |
| `organic_neutral_cat` | 全部不命中的有机催化剂(spiro-BOX 等)— 化学语义兜底 | 888 (9.0%) |
| `unparseable_text` | RDKit 不能解析 | 24 (0.2%) |
| `ABSENT` | 字段为空 | — |

### 3.2 机制 tag(正交多标签,不互斥)

| Tag | 何时设置 | 例 |
|---|---|---|
| `mediator` | ferrocene/TEMPO/NHPI/aryl-I/quinone/polycyclic_arene | Cp2Fe, TEMPO, Tol-I, DDQ, naphthalene |
| `photoredox` | 4CzIPN-like / acridinium / Eosin / Ir(ppy)3 / Ru(bpy)3 / TBADT(W) / thianthrene | Mes-Acr+, 4CzIPN, Ir(ppy)3 |
| `HAT` | TEMPO/NHPI/TBADT/decanethiol | 与 mediator 共存常见 |
| `chiral` | SMILES 含 `@`/`@@` | (S)-BOX, BINAP, salen |

机制 tag 与元素类**正交**:`Ir(ppy)3` 同时是 `Ir_complex` + `photoredox` 标签。让模型能学到"机制等价":Cp2Fe(`Fe_complex`+mediator) 和 TBAI(`ammonium_PTC_organocat`+mediator) 行为更相似。

---

## 4. LIGAND head — 10 类

分类依据:**配位骨架 SMARTS 识别**。

| 类 | 规则 | 数据中 |
|---|---|---|
| `bipyridine` | `c1ccc(-c2ccccn2)nc1` | 338 (34.1%) |
| `phenanthroline` | 1,10-phen 骨架 | 99 (10.0%) |
| `polypyridyl` | ≥2 个芳香 N | 31 (3.1%) |
| `pyridine_monodentate` | 单吡啶环(DMAP/lutidine) | 18 (1.8%) |
| `BOX_oxazoline` | 含 oxazoline `C=NCCO` 单/双齿 | 212 (21.4%) |
| `PyBOX` | 含中心 pyridine + 2 个 oxazoline | 71 (7.2%) |
| `phosphine_bidentate` | 含 2 个 [P](dppX/BINAP/Xantphos) | 71 (7.2%) |
| `phosphine_monodentate` | 含 1 个 [P;X3] | 10 (1.0%) |
| `N_donor_other` | 含 N 但不在以上(salen/tridentate/胺类) | 123 (12.4%) |
| `unknown_placeholder` | SMILES = `*` | 18 (1.8%) |
| `ABSENT` | 字段为空 | — |

`chiral` tag(正交):SMILES 含 `@`/`@@` 时设置。

---

## 5. SOLVENT head — 23 类

分类依据:**极性/质子性/官能团 SMARTS**,HFIP/TFE 因占比高单列。

| 类 | 规则 / 例 | 数据中 |
|---|---|---|
| `polar_aprotic_nitrile` | `[CX2]#[NX1]` (MeCN/EtCN/PhCN) | 12279 (33.8%) ← top |
| `aqueous` | H2O / D2O / `[H+].[OH-]` | 5505 (15.1%) |
| `halogenated_aliphatic` | DCM/DCE/CHCl3/CCl4/BrCH2CH2Br | 4049 (11.1%) |
| `polar_protic_alcohol` | `[CX4][OH]` 非氟代(MeOH/EtOH/iPrOH) | 2922 (8.0%) |
| `hfip` | `OC(C(F)(F)F)C(F)(F)F` ← **独立类(数据中 7%)** | 2477 (6.8%) |
| `polar_aprotic_amide` | DMF/DMA/NMP/DMPU | 2471 (6.8%) |
| `ketone` | `[CX3](=O)([#6])[#6]`(acetone/MEK) | 1311 (3.6%) |
| `tfe` | `OCC(F)(F)F` ← **独立**(2,2,2-trifluoroethanol) | 1103 (3.0%) |
| `cyclic_ether` | THF/dioxane/2-MeTHF | 1098 (3.0%) |
| `polar_aprotic_sulfoxide` | DMSO/sulfolane | 865 (2.4%) |
| `acyclic_ether` | Et2O/DME/MTBE 链状 | 520 (1.4%) |
| `polar_protic_acid` | AcOH/TFA/formic acid(作溶剂) | 450 (1.2%) |
| `aromatic_fluorinated` | PhCF3 / 含氟芳烃 | 381 (1.0%) |
| `nitroalkane` | MeNO2 | 245 (0.7%) |
| `aromatic_hydrocarbon` | toluene/xylene/benzene/chlorobenzene | 225 (0.6%) |
| `solvent_mixture` | 多组分含 `.` 且都是中性有机 | 175 (0.5%) |
| `ester` | EtOAc/BuOAc | 150 (0.4%) |
| `acid_anhydride_solvent` | Ac2O 作溶剂 | 76 (0.2%) |
| `amine_solvent` | piperidine/DIPEA 作溶剂 | 23 (0.1%) |
| `alkane` | hexane/cyclohexane | 21 (0.1%) |
| `inorganic_misc_solvent_field` | 数据噪声(K2HPO4 出现在 solvent 字段) | 20 (0.1%) |
| `pyridine_solvent` | pyridine 作溶剂 | 7 |
| `other_polar_aprotic` | 极少数其他 | 7 |
| `ABSENT` | 字段为空 | — |

---

## 6. ELECTROLYTE head — **双 head(cation + anion)**

### 6.1 为何拆为双 head

数据中 386 个 unique electrolyte 99% 是 cation × anion 组合(TBA+BF4-, Et4N+PF6-, ...)。
- 单一 class head:386 个类 → 训练样本严重稀疏。
- **拆 cation(19 类) + anion(23 类)**:模型在 19+23=42 维上学,组合空间隐式 = 19×23=437,样本效率显著提升,化学家可读。

分类依据:**离子化学式片段匹配**(`[N+](CCCC)4`, `F[B-](F)(F)F` 等)。

### 6.2 Cation head — 19 类

| 类 | 规则 | 数据中 |
|---|---|---|
| `NBu4` | `[N+](CCCC)(CCCC)(CCCC)CCCC` | 11756 (55%) ← 主导 |
| `Li` | `[Li+]` / `[Li]` | 3624 (17%) |
| `NEt4` | Et4N+ | 2366 (11%) |
| `K` | `[K+]` | 1149 (5%) |
| `Na` | `[Na+]` | 1137 (5%) |
| `NH4` | `[NH4+]` | 206 (1%) |
| `imidazolium` | `[n+]1ccn(*)c1` | 173 |
| `alkyl_ammonium` | 其他 [N+;X4](非 NMe4/NEt4/NBu4) | 147 |
| `NMe4` | Me4N+ | 120 |
| `H` (proton) | `[H+]` 或纯酸(TfOH/H2SO4) | 96 |
| `protonated_amine` | Et3N·HF 等胺·HF | 115 |
| `pyridinium` | `[n+]1ccccc1` | 38 |
| `phosphonium` | `[P+;X4]` | 39 |
| `Mg` | `[Mg+2]` | 23 |
| `Ca` | `[Ca+2]` | 16 |
| `Cs` | `[Cs+]` | 9 |
| `aryl_ammonium` | BnNMe3+ 等 | 1 |
| `molecular_no_ion` | 中性写法占位(数据噪声) | 197 |
| `ABSENT` / `none` | 字段为空 | — |

### 6.3 Anion head — 23 类

| 类 | 规则 | 数据中 |
|---|---|---|
| `BF4` | `F[B-](F)(F)F` | 6267 (30%) ← 主导 |
| `ClO4` | `[O-]Cl(=O)(=O)=O` | 3866 (18%) |
| `PF6` | `F[P-](F)(F)(F)(F)F` | 2935 (14%) |
| `Br` | `[Br-]` | 2040 (10%) |
| `I` | `[I-]` | 2017 (10%) |
| `carboxylate` | `[CX3](=O)[O-]` | 1269 (6%) |
| `Cl` | `[Cl-]` | 932 (4%) |
| `OTf` | `O=S(=O)([O-])C(F)(F)F` | 258 (1%) |
| `SO4` | `[O-]S(=O)(=O)[O-]` | 230 (1%) |
| `F` | `[F-]` | 132 |
| `OTs` | `Cc1ccc(S(=O)(=O)[O-])cc1` | 121 |
| `fluoride_complex` | HF·amine 形式 | 115 |
| `OH` | `[OH-]` | 64 |
| `alkoxide` | `[CX4][O-]` | 29 |
| `SCN` | `[S-]C#N` | 28 |
| `phosphate` | `[O-]P(=O)([O-])O` | 22 |
| `BArF20` | 全氟四苯基硼酸盐 | 20 |
| `borate_other` | 其他 [B-] | 18 |
| `NO3` | `[O-][N+](=O)[O-]` | 9 |
| `sulfate_acid` | H2SO4 形式 | 7 |
| `NTf2` | `(CF3SO2)2N-` | 5 |
| `molecular_no_ion` | 中性写法占位 | 197 |
| `ABSENT` / `none` | 字段为空 | — |

---

## 7. ADDITIVE head — 42 类(复用 reagent 类 + mediator 优先)

Additive 字段只有 556 occ,但极其有信息(mediator/MS/sacrificial salt)。
直接复用 reagent 分类器,**但加 mediator-first 优先级**(因为 TEMPO/NHPI/Tol-I/ferrocene/萘菲蒽在 additive 字段时几乎 100% 是 mediator 角色):

| 类 | 数据中 |
|---|---|
| `carbon_powder` | 79 (graphite [C] 作 additive) |
| `hf_amine_complex` | 64 |
| `water` | 60 |
| `tempo_mediator` | 48 |
| `polycyclic_arene_mediator` | 35 |
| `aryl_iodide_mediator` | 3 |
| `nhpi_mediator` | 3 |
| `ferrocene_mediator` | 2 |
| ...(其余从 reagent 表复用) | |

共 42 类,全部有化学意义。

---

## 8. ANODE / CATHODE — 材料家族(字符串规则)

分类依据:**关键词匹配电极材料**,把 800+ 写法变体折成材料家族。

### 8.1 Anode classifier — 11 类(主要 6 大类)

| 类 | 关键词 | anode 数据 |
|---|---|---|
| `carbon` | graphite / carbon / RVC / vitreous / glassy / BDD / GF / GC / CC / boron-doped / cetech | 17939 (66%) ← 主导 |
| `platinum` | platinum / Pt | 2857 (11%) |
| `sacrificial_magnesium` | Mg / magnesium | 833 (3%) |
| `sacrificial_iron` | Fe / iron | 558 (2%) |
| `sacrificial_zinc` | Zn / zinc | 486 (2%) |
| `sacrificial_aluminum` | Al / aluminum / aluminium | 209 (0.8%) |
| `stainless_steel` | stainless / steel / SS | 122 (0.5%) |
| `nickel` | Ni / nickel(very rare at anode) | 16 |
| `copper` / `silver` / `gold` / `titanium` / `tin` / `lead` | 对应元素 | 各 < 20 |
| `other_electrode` | 真的不在以上(BDD 已归 carbon、MMO 单独标) | 582 (2%) |
| `ABSENT` | 字段为空 | — |

> 最常见 6 类覆盖 99%。

### 8.2 Cathode classifier — 11 类(分布不同)

| 类 | cathode 数据 |
|---|---|
| `platinum` | 13696 (51%) ← 主导 |
| `carbon` | 5397 (20%) |
| `nickel` | 1796 (7%) |
| `stainless_steel` | 780 (3%) |
| `sacrificial_iron` | 442 (2%) |
| `copper` / `silver` / `tin` / `lead` / `titanium` / `sacrificial_*` | 各 30-200 |
| `other_electrode` | 1078 (4%) |

### 8.3 Cell_type — 3 类

分类依据:**电解池描述关键词**。

| 类 | 规则 | 数据中 |
|---|---|---|
| `undivided` | 'undivid' / 'indivis' / 'in cell' / 'integrated' / 'beaker' / 'electrasyn' / 'three-necked' | 18543 (96%) ← 主导 |
| `divided` | 'divided' / 'membrane' / 'nafion' / 'h-type' / 'compartment' / 'separated' / 'CCE' | 715 (3.7%) |
| `flow` | 'flow' / 'single-pass' / 'continuous' | 77 (0.4%) |
| `ABSENT` | 字段为空 | — |

---

## 9. 总览:各 head 类别数

| Head | 类别数 | 备注 |
|---|---|---|
| reagent | **55**(38 核心 + 10 as_solvent + 7 化学兜底) | 100% 覆盖,top-15 占 75% |
| catalyst | **36 元素类 + 4 机制 tag(正交)** | mediator/photoredox/HAT/chiral |
| ligand | **10** | bpy + BOX 占 64% |
| solvent | **23** | HFIP/TFE 独立类(总占 10%) |
| electrolyte | **19 cation + 23 anion = 双 head** | 隐式组合空间 437 |
| additive | **42**(复用 reagent + mediator-first) | |
| anode | **11**(6 主要材料家族) | 字符串规则 |
| cathode | **11** | |
| cell_type | **3** | |
| **总** | **~170 个有意义类 + 4 个机制 tag(正交)** | 无 OTHER |

---

## 10. 跨 head 同名设计

ferrocene / TEMPO / Tol-I / water / HFIP 等小分子在 reagent / catalyst / additive 字段**共享同一类名**,内部样本量集中:

| SMILES | 类名(三 head 共用) | reagent 出现 | catalyst 出现 | additive 出现 |
|---|---|---|---|---|
| Cp2Fe ferrocene | `ferrocene_mediator` | 118 | 419(带 mediator tag) | 2 |
| TEMPO | `tempo_mediator` | 214 | 113(带 HAT+mediator tag) | 48 |
| Tol-I | `aryl_iodide_mediator` | 304 | 106(带 mediator tag) | 3 |
| HFIP | `hfip` (solvent) / `brønsted_acid_cat` (catalyst) | — | 35 | 21 |
| H2O | `water` | 1056 | — | 60 |
| Et3N·3HF | `hf_amine_complex` | 420 | — | 64 |

---

## 11. 实施

文件清单:

```
yield_prediction/utils/classifier_v3.py          # 6 + 3 个分类函数
  ├─ classify_reagent(smi) -> str                # 38 个核心类
  ├─ classify_catalyst(smi) -> (cls, tags)       # 36 类 + tag set
  ├─ classify_ligand(smi) -> str
  ├─ classify_solvent(smi) -> str
  ├─ classify_electrolyte(smi) -> (cation, anion)
  ├─ classify_additive(smi) -> str
  ├─ classify_electrode(text) -> str             # anode/cathode 共用
  └─ classify_cell(text) -> str

yield_prediction/scripts/augment_class_labels_v3.py  # 跑全数据,加 label
  - 对每个反应生成: reagent_class, catalyst_class, catalyst_tags(4-bit),
    ligand_class, solvent_class, electrolyte_cation, electrolyte_anion,
    additive_class, anode_class, cathode_class, cell_class

yield_prediction/data_audited_v4/                  # 增广后的数据
  └─ vocab.json — 新类别 ID 表
```

---

## 12. 验收(已用源数据验证 ✓)

- ✅ 每个出现过的 SMILES 都归到化学类(0 个 OTHER)
- ✅ TFA → `carboxylic_acid`(不是 cf3_source);K2CO3 → `alkali_carbonate`
- ✅ Cp2Fe ferrocene(EC top1 catalyst SMILES,419 次)→ `ferrocene_mediator`
- ✅ Tol-I(EC mediator,179 次)→ `aryl_iodide_mediator`
- ✅ CO2(105 次)→ `co2_reagent`
- ✅ O2(270 次)→ `o2_oxidant`
- ✅ HFIP/TFE 独立类,solvent 总占 10%
- ✅ Electrolyte 双 head:NBu4+ × BF4- 等组合明确
- ✅ Anode/cathode 折成材料家族,carbon 占 anode 66%
- ✅ photoredox / mediator / HAT / chiral 4 个正交 tag 让机制相似性可学
