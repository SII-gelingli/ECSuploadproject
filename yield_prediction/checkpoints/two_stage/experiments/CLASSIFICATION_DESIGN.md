# 完整化学分类方案 (无 OTHER 桶)

**目标**: 给 6 个 SMILES head（solvent/electrolyte/catalyst/reagent/ligand/additive）每个都设计完整的化学分类树, 让**每个出现过的 SMILES 都能归到化学上合理的类**, 完全消除 OTHER 桶。

## 设计原则

1. **化学优先**: 按官能团 / 结构特征 / 反应角色分类, 不按统计频次
2. **优先级清晰**: 更具体的类优先匹配 (如 `alkali_carbonate` 优先于 `carboxylate`)
3. **兜底是有意义的子类**, 不是"杂项": 用 `miscellaneous_organic_neutral` / `miscellaneous_inorganic` 等明确化学语义
4. **匹配规则**: 全部用 RDKit SMARTS, 失败 SMILES → `unparseable` 类 (而不是 OTHER)

---

## 1. Reagent (~850 SMILES → 60 类)

按反应中的角色 + 主要官能团分类。

### 1.1 含氟 / 卤代试剂 (8 类)

| ID | 类名 | SMARTS | 例 |
|---|------|--------|---|
| R01 | `cf3_source` | `[#6;X4](F)(F)F`, 优先级低于 carboxylic_acid | CF3SO2Na, CF3I, Togni |
| R02 | `rfn_source` | `[#6;X4](F)(F)[#6;X4](F)(F)F` | C2F5SO2Na, CnF2n+1 |
| R03 | `hf_source` | `[F].[N]` 多片段含 F + amine | Et3N·3HF, KHF2, Olah |
| R04 | `fluoride_anion` | `[F-]` | KF, CsF, Bu4NF |
| R05 | `chloride_anion` | `[Cl-]` | KCl, NaCl, Bu4NCl |
| R06 | `bromide_anion` | `[Br-]` | KBr, NaBr |
| R07 | `iodide_anion` | `[I-]` | KI, NaI |
| R08 | `n_halo_succinimide` | NBS/NIS/NCS 框架 | NBS, NIS, NCS |
| R09 | `hypohalite` | `[O-][Cl,Br,I]` | NaClO, NaBrO, hypoiodite |

### 1.2 含氮试剂 (12 类)

| ID | 类名 | SMARTS | 例 |
|---|------|--------|---|
| R10 | `azide_source` | `[N-]=[N+]=[N]` 含 N3 | NaN3, TMSN3, RSO2N3 |
| R11 | `cyanide_anion` | `[C-]#N` | KCN, NaCN, TMSCN |
| R12 | `isocyanide` | `[N+]#[C-]` | RNC |
| R13 | `nitro_compound` | `[NX3](=O)=O` 作 reagent | nitromethane, nitrobenzene |
| R14 | `diazo` | `[#6]=[N+]=[N-]` | TMSCHN2, diazoester |
| R15 | `primary_amine` | `[NX3;H2;!$(NC=O);!$(N=*)]` | RNH2 |
| R16 | `secondary_amine` | `[NX3;H1;!$(NC=O);!$(N=*)]` | R2NH |
| R17 | `tertiary_amine` | `[NX3;H0;!$(NC=O);!$(N=*);!$([N+])]` | Et3N, DIPEA |
| R18 | `pyridine` | `c1ccncc1` 含吡啶环 | DMAP, 2,6-lutidine |
| R19 | `imidazole` | `c1[nH]cnc1` | NHC precursor, imidazole |
| R20 | `amide` | `[NX3][CX3](=O)` 含 -C(=O)N- | DMF (作 reagent), AcNHR |
| R21 | `guanidine` | `[NX3]C(=N)[NX3]` | TBD, MTBD |

### 1.3 含硫试剂 (8 类)

| ID | 类名 | SMARTS | 例 |
|---|------|--------|---|
| R22 | `thiocyanate` | `[S-]C#N` | KSCN, NH4SCN |
| R23 | `sulfinate` | `[S;X3](=O)[O-]` | CF3SO2Na, ArSO2Na |
| R24 | `sulfonyl_chloride` | `[S;X4](=O)(=O)Cl` | RSO2Cl |
| R25 | `sulfonyl_azide` | `[S;X4](=O)(=O)N=[N+]=[N-]` | RSO2N3 |
| R26 | `sulfonamide` | `[NX3][S;X4](=O)(=O)` | RSO2NHR' |
| R27 | `sulfonic_acid` | `[S;X4](=O)(=O)[OH]` | TsOH, MsOH |
| R28 | `thiol` | `[#6;!a][SH]` | RSH (alkanethiol/arylthiol) |
| R29 | `disulfide` | `[#6][SS][#6]` | Se2Ph2, R-S-S-R |

### 1.4 含氧试剂 (10 类)

| ID | 类名 | SMARTS | 例 |
|---|------|--------|---|
| R30 | `carboxylic_acid` | `[CX3](=O)[OH]` | AcOH, TFA, BzOH |
| R31 | `carboxylate` | `[CX3](=O)[O-]` (排除碳酸盐) | AcONa, BzOK |
| R32 | `alcohol` | `[CX4][OH]` (非苯酚) | MeOH, EtOH, iPrOH |
| R33 | `phenol` | `c[OH]` | 苯酚, BHT |
| R34 | `aldehyde` | `[CX3H1](=O)[#6]` | RCHO |
| R35 | `ketone` | `[CX3](=O)([#6])[#6]` | acetone, MEK |
| R36 | `peroxide` | `[OX2][OX2]` | H2O2, mCPBA, TBHP |
| R37 | `hypervalent_iodine` | `[I;X3]` 或 `[I+5]` | PhI(OAc)2, Togni, Koser |
| R38 | `quinone_oxidant` | `[#6]1[#6]=[#6][#6](=O)[#6]=[#6]1=O` | DDQ, p-quinone, chloranil |
| R39 | `epoxide` | `[CX4]1O[CX4]1` 含环氧 | RPO, glycidyl |

### 1.5 无机碱 / 盐 (8 类)

| ID | 类名 | SMARTS | 优先级 |
|---|------|--------|------|
| R40 | `alkali_carbonate` | `O=C([O-])[O-]` + `[Li,Na,K,Cs,Rb]` | **必须先于 carboxylate** |
| R41 | `alkali_bicarbonate` | `O=C([O-])O` + `[Li,Na,K,Cs]` | 同上 |
| R42 | `alkali_phosphate` | `O=P([O-])([O-])` + `[Li,Na,K,Cs]` | 含三价/二价磷酸盐 |
| R43 | `alkali_hydroxide` | `[OH-]` + `[Li,Na,K,Cs]` | NaOH, KOH, CsOH |
| R44 | `alkali_alkoxide` | `[CX4][O-]` + `[Li,Na,K,Cs]` | NaOtBu, KOEt |
| R45 | `alkali_amide` | `[NX2-]` 含烷基胺负 + 碱金属 | NaHMDS, LDA, LiHMDS |
| R46 | `alkaline_earth_salt` | `[Mg+2/Ca+2/Sr+2/Ba+2]` | Mg(OTf)2 等 |
| R47 | `ammonium_salt` | `[N+](C)(C)(C)C` 四级铵 | NH4Cl, Et4N-X (作 reagent) |

### 1.6 含硅 / 硼 / 磷主族 (6 类)

| ID | 类名 | SMARTS | 例 |
|---|------|--------|---|
| R48 | `silane` | `[Si]([#6])([#6])([#6])` | TMS-X, Et3SiH, PhSiH3 |
| R49 | `silyl_protector` | `[Si][O,N,S]` | TBS-OTf, TBDPSCl |
| R50 | `boronic_acid` | `[B]([OH])([OH])` | RB(OH)2, ArB(OH)2 |
| R51 | `borate_ester` | `[B]([OC])([OC])` | RBpin, RBcat |
| R52 | `phosphine` | `[P;X3]([#6])([#6])([#6])` | PPh3, PCy3 |
| R53 | `phosphoryl` | `[P;X4](=O)` | (RO)3P=O, OP(OEt)3 |

### 1.7 烷基/芳基卤代物 + 离去基团 (4 类)

| ID | 类名 | SMARTS | 例 |
|---|------|--------|---|
| R54 | `alkyl_halide` | `[CX4][F,Cl,Br,I]` 非芳基 | RBr, RI |
| R55 | `aryl_halide` | `c[F,Cl,Br,I]` 芳基卤化物 | ArBr, ArI |
| R56 | `triflate` | `OS(=O)(=O)C(F)(F)F` | RO-Tf, ArO-Tf |
| R57 | `tosylate` | `OS(=O)(=O)c1ccc(C)cc1` | RO-Ts, ArO-Ts |

### 1.8 金属配合物作 reagent (2 类)

| ID | 类名 | SMARTS | 例 |
|---|------|--------|---|
| R58 | `metallocene_reagent` | 含 `[Fe+2]/[Co+2]` + Cp | ferrocene 等 |
| R59 | `organometallic_reagent` | 含 `[Mg]/[Zn]/[Cu]` + 有机 | RMgX, RZnX, R3Cu |

### 1.9 水 / 杂项明确化学类 (2 类)

| ID | 类名 | SMARTS | 例 |
|---|------|--------|---|
| R60 | `water` | `[OX2H2]` 仅 H2O | H2O, D2O |
| R61 | `o2_oxidant` | `O=O` | 氧气 |

### 1.10 ABSENT + 兜底 (2 类)

| ID | 类名 | 说明 |
|---|------|---|
| R00 | `ABSENT` | 反应不需要 reagent |
| R62 | `unparseable` | SMILES 无法用 RDKit 解析 (而非 "OTHER") |

**总计**: 62 个有意义的化学类 + ABSENT + unparseable = **64 类** (覆盖率应 > 99%)

---

## 2. Solvent (~120 SMILES → 8 类)

按介电常数 + 质子性 + 卤代性分类：

| ID | 类名 | SMARTS / 规则 | 例 |
|---|------|--------|---|
| S01 | `aqueous` | `[OX2H2]` 仅 H2O | H2O |
| S02 | `polar_protic` | 含 -OH 或 -COOH (sp3) | MeOH, EtOH, iPrOH, AcOH, HFIP, TFE |
| S03 | `polar_aprotic_nitrogen` | 含 N=C/CN/酰胺 + 无 -OH | MeCN, DMF, DMA, NMP, DMSO |
| S04 | `polar_aprotic_sulfur` | DMSO 系 (S=O 而非 SO2) | DMSO, sulfolane |
| S05 | `halogenated_polar` | 含 X + 极性 | DCM, DCE, CHCl3, CCl4 |
| S06 | `ether_cyclic` | 含 [CX4]O[CX4] 环 | THF, dioxane, DME |
| S07 | `ether_acyclic` | 链状醚 | Et2O, MTBE |
| S08 | `nonpolar_aromatic` | 苯/甲苯/二甲苯系 | toluene, xylene, benzene |
| S09 | `nonpolar_alkane` | 直链/环烷烃 | hexane, cyclohexane, pentane |
| S10 | `ester` | `[CX3](=O)O[#6]` | EtOAc, BuOAc |
| S11 | `ketone` | `[CX3](=O)([#6])[#6]` | acetone, MEK |
| S12 | `ionic_liquid` | 含 [N+]/[P+] + 阴离子 | RTILs |

**总计**: 12 个 solvent 类 + ABSENT = 13 类

---

## 3. Electrolyte (~400 SMILES → 8 类)

按阳离子 + 阴离子双维度分类：

| ID | 类名 | 阳离子+阴离子 SMARTS | 例 |
|---|------|--------|---|
| E01 | `tetraalkylammonium_BF4` | `[N+](C)(C)(C)C` + `[B-](F)(F)(F)F` | TBABF4, Et4NBF4 |
| E02 | `tetraalkylammonium_PF6` | `[N+]` + `[P-](F)(F)(F)(F)(F)F` | TBA-PF6 |
| E03 | `tetraalkylammonium_ClO4` | `[N+]` + `[O-]Cl(=O)(=O)=O` | TBA-ClO4 |
| E04 | `tetraalkylammonium_halide` | `[N+]` + `[Cl-/Br-/I-]` | TBABr, TBAI |
| E05 | `tetraalkylammonium_sulfonate` | `[N+]` + `[S](=O)(=O)[O-]` | TBA-OTs, TBA-OTf |
| E06 | `tetraalkylammonium_other` | `[N+]` + 其他阴离子 | TBA-OAc 等 |
| E07 | `phosphonium_salt` | `[P+](C)(C)(C)C` | R4P-X |
| E08 | `lithium_perchlorate` | `[Li+]` + `[O-]Cl(=O)(=O)=O` | LiClO4 |
| E09 | `lithium_other` | `[Li+]` + 其他 | LiBF4, LiOTf, Li-NTf2 |
| E10 | `sodium_salt` | `[Na+]` + 阴离子 | NaClO4, NaOTf, NaBF4 |
| E11 | `potassium_salt` | `[K+]` + 阴离子 | KPF6, KClO4 |
| E12 | `cesium_salt` | `[Cs+]` + 阴离子 | CsF, Cs2CO3 (作 electrolyte) |
| E13 | `nh4_salt` | `[NH4+]` 或 `[N+;H4]` + X | NH4Cl, (NH4)2SO4 |
| E14 | `acid_electrolyte` | `[H+]` 形式 (H2SO4, HCl)| 罕见但有 |
| E15 | `ionic_liquid` | 大有机阳离子 | imidazolium-X |
| E16 | `inorganic_other` | 其他无机盐 | ZnCl2, BaSO4 |

**总计**: 16 个 electrolyte 类 + ABSENT = 17 类

---

## 4. Catalyst (~750 SMILES → 14 类)

按主要金属元素分类（无 OTHER）：

| ID | 类名 | 检测规则 | 例 |
|---|------|--------|---|
| C01 | `Cu_catalyst` | 含 [Cu], [Cu+], [Cu+2] | CuCl, Cu(OTf)2, Cu(OAc)2 |
| C02 | `Mn_catalyst` | 含 [Mn], [Mn+2/+3] | Mn(OAc)2, MnBr2, Mn(salen) |
| C03 | `Fe_catalyst` | 含 [Fe], [Fe+2/+3] | FeCl2, Fe(OAc)2, FeCp2 |
| C04 | `Co_catalyst` | 含 [Co], [Co+2/+3] | Co(acac)2, Co(OAc)2 |
| C05 | `Ni_catalyst` | 含 [Ni], [Ni+2] | NiCl2, Ni(dme) |
| C06 | `Pd_catalyst` | 含 [Pd], [Pd+2] | Pd(OAc)2, Pd(PPh3)4 |
| C07 | `Pt_catalyst` | 含 [Pt], [Pt+2/+4] | Pt(II) salts |
| C08 | `Ru_catalyst` | 含 [Ru] | Ru(bpy)3, RuCl3 |
| C09 | `Rh_catalyst` | 含 [Rh] | Rh(PPh3)3Cl |
| C10 | `Ir_catalyst` | 含 [Ir] | Ir(ppy)3 (photoredox) |
| C11 | `Zn_catalyst` | 含 [Zn], [Zn+2] | ZnBr2, Zn(OTf)2 |
| C12 | `Mg_catalyst` | 含 [Mg+2] (作催化剂) | Mg(OTf)2 |
| C13 | `Ag_catalyst` | 含 [Ag] | AgOTf, AgNO3 |
| C14 | `Au_catalyst` | 含 [Au] | AuCl3 |
| C15 | `main_group_catalyst` | Al/B/Sn/Bi 等主族 | BF3, AlCl3, Sn salts |
| C16 | `lanthanide_catalyst` | Sc/Y/Yb/Eu/La 等 | Sc(OTf)3, Yb(OTf)3 |
| C17 | `multi_metal` | 含 ≥2 种不同金属 | bimetallic systems |
| C18 | `metal_free_organocatalyst` | 无金属, 含 N/P/S 催化基团 | DMAP, DABCO, NHC |
| C19 | `photoredox_organic` | 有机光催化剂 (acridinium 等) | Mes-Acr+, Eosin Y |
| C20 | `polyoxometalate` | 复杂多金属氧化物 | POM |

**优先级**: 多金属时按"主要功能金属"判定 (e.g., Pd/Cu 双金属优先 Pd)

**总计**: 20 个 catalyst 类 + ABSENT = 21 类

---

## 5. Ligand (~190 SMILES → 10 类)

按配位原子 + 结构分类：

| ID | 类名 | 检测规则 | 例 |
|---|------|--------|---|
| L01 | `pyridine_monodentate` | 含 1 个 pyridine N | DMAP, lutidine |
| L02 | `bpy_phen_polypyridyl` | 含 2+ pyridine N (多齿) | bpy, phen, terpy |
| L03 | `amine_aliphatic` | 含烷基胺 N (TMEDA 等) | TMEDA, sparteine |
| L04 | `salen_salan` | salicylaldimine 结构 | salen, salan |
| L05 | `oxazoline_BOX` | 含恶唑啉环 | (S)-BOX, PyBOX, iPrPyBOX |
| L06 | `phosphine_monodentate` | 含 1 个 P (PR3) | PPh3, PCy3, P(t-Bu)3 |
| L07 | `phosphine_bidentate` | 含 2 个 P (dppX) | dppe, dppp, dppf, BINAP |
| L08 | `NHC_carbene` | 含 imidazolylidene | IPr, IMes, SIPr |
| L09 | `chiral_N_donor` | 含手性 N 配体 | (R)-BINAM 系 |
| L10 | `hybrid_PN_PO_PS` | 含 P+N 或 P+O 杂混 | P,N-ligands |
| L11 | `aminoacid_or_peptide` | 含 -C(=O)N + chiral C | proline, BPA |
| L12 | `crown_ether` | 含多 -O-CH2-CH2- 环 | 18-crown-6 |

**总计**: 12 个 ligand 类 + ABSENT = 13 类

---

## 6. Additive (~110 SMILES → 7 类)

按添加剂功能分类：

| ID | 类名 | 检测规则 | 例 |
|---|------|--------|---|
| A01 | `radical_mediator` | TEMPO 系 (含 [N]([O])) | TEMPO, AZADO |
| A02 | `radical_trap` | 烯烃/苯并菲等 | 1,1-DPE, persistent radical |
| A03 | `drying_agent` | MS, Na2SO4, MgSO4 | 3A/4A/5A MS |
| A04 | `phase_transfer_catalyst` | 四级铵盐作 PTC | TBAB, Aliquat |
| A05 | `coordination_modifier` | LiCl 等离子调节剂 | LiCl, LiBr (作 additive) |
| A06 | `protic_additive` | 少量酸 (TfOH/AcOH/PhCOOH) | TfOH, AcOH (作 additive) |
| A07 | `aprotic_modifier` | HFIP/TFE 作 co-solvent | HFIP, TFE (作 additive) |
| A08 | `base_additive` | DBU/pyridine 作 base additive | DBU, 2,6-lutidine |
| A09 | `phenol_inhibitor` | BHT, hydroquinone | BHT, HQ |
| A10 | `inert_modifier` | 真正无活性的, 仅调反应介质 | inert gas markers |

**总计**: 10 个 additive 类 + ABSENT = 11 类

---

## 全局优先级与兜底

### 优先级原则

1. **更具体的类先匹配**:
   - `cf3_source` < `carboxylic_acid` (TFA 应是 carboxylic_acid, 即使含 CF3)
   - `alkali_carbonate` 必须先于 `carboxylate`
   - `n_halo_succinimide` 先于 `halide_anion`

2. **多功能基团时按主要反应角色**:
   - 含 CF3 + COOH (TFA) → 当 reagent 时主要功能是酸 → `carboxylic_acid`
   - 含 N3 + OTs (双官能) → 主要功能是叠氮源 → `azide_source`

### 兜底机制（不叫 OTHER）

| 兜底类名 | 触发条件 |
|---------|---------|
| `unparseable` | RDKit 无法解析 SMILES (典型: "air", "Dried" 等 LLM 误抽) |
| `miscellaneous_organic_neutral` | 中性有机分子 (含 C+H, 无明确反应官能团) |
| `miscellaneous_inorganic` | 含金属/无机盐, 但金属种类太罕见 |

**这 3 个兜底类是化学上明确的概念**, 不是统计意义的 "OTHER"。

---

## 各 head 总计

| Head | 化学类数 | + ABSENT | 总 |
|------|--------|--------|---|
| reagent | 62 | 1 | 63 (+ unparseable) |
| solvent | 12 | 1 | 13 |
| electrolyte | 16 | 1 | 17 |
| catalyst | 20 | 1 | 21 |
| ligand | 12 | 1 | 13 |
| additive | 10 | 1 | 11 |
| **总和** | **132** | **6** | **~138 类** |

vs 当前: reagent 47 + 其他没分类 = 极简层次信号

---

## 实施 SMARTS 优先级表 (reagent 关键示例)

```python
REAGENT_PRIORITY = [
    # 1) 最具体 (容易误分到泛化类的): 先匹配
    'n_halo_succinimide',     # NBS/NIS 优先于 halide_anion
    'alkali_carbonate',       # K2CO3 优先于 carboxylate
    'alkali_bicarbonate',
    'alkali_phosphate',
    'alkali_hydroxide',
    'alkali_alkoxide',
    'alkali_amide',
    'silyl_protector',        # TBS-OTf 优先于 silane

    # 2) 主要官能团类: 中等优先
    'sulfonyl_azide',         # 优先于 azide_source
    'sulfonyl_chloride',
    'sulfonamide',
    'sulfonic_acid',
    'sulfinate',
    'thiocyanate',
    'azide_source',
    'cyanide_anion',
    'isocyanide',

    # 3) 含氟试剂: 在 carboxylic_acid 之后
    'carboxylic_acid',        # TFA 归 acid 而非 cf3
    'carboxylate',
    'cf3_source',
    'rfn_source',
    'hf_source',
    'fluoride_anion',

    # ... 其他类 ...

    # 4) 最后兜底
    'miscellaneous_organic_neutral',
    'miscellaneous_inorganic',
    'unparseable',
]
```

---

## 验收标准

- ✅ 每个出现过的 SMILES 都归到某个化学类 (不进 OTHER)
- ✅ alkali_carbonate / alkali_phosphate 等不再为 0
- ✅ TFA → carboxylic_acid (不是 cf3_source)
- ✅ K2CO3 → alkali_carbonate (不是 carboxylate)
- ✅ 二茂铁 → metallocene_reagent / 或 Fe_catalyst (按 head)
- ✅ Solvent / electrolyte / catalyst / ligand / additive 都有 class head
- ✅ Hier+Set 训练时 6 个 class signal 都用上

---

## 实施工程

| 步骤 | 工作量 |
|------|------|
| 1. 写 `utils/reagent_classifier_v2.py` (60 类) | 2 hr |
| 2. 写 `utils/solvent_classifier.py` (12 类) | 30 min |
| 3. 写 `utils/electrolyte_classifier.py` (16 类) | 1 hr |
| 4. 写 `utils/catalyst_classifier.py` (20 类) | 1 hr |
| 5. 写 `utils/ligand_classifier.py` (12 类) | 1 hr |
| 6. 写 `utils/additive_classifier.py` (10 类) | 30 min |
| 7. 改 augment 脚本统一跑 6 个 class | 30 min |
| 8. 改 ConditionStage1HierSet 接 6 class signal | 1.5 hr |
| 9. 训练 + eval | 1 hr |
| **总计** | **~9 hr** |

完成后预期: Hier+Set 全 head Set F1 + Top-K 全面提升 5-15%。
