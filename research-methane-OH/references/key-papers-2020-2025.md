# Paper Reference Notes — research-methane-OH

## Category 1: MCF / Top-Down Studies

---

### Montzka et al. (2011) — Science 331, 67
**"Small interannual variability of global atmospheric hydroxyl"**
- **Method:** MCF observations from NOAA global network, post-1998 (when gradients diminished)
- **Period:** 1998–2007
- **Key data:**
  - OH IAV: **2.3 ± 1.5%** (1σ) — much smaller than prior 7–9% estimates
  - Prior estimates (1980–2003) were sensitive to poorly constrained MCF emissions
  - Post-1998 MCF is emission-free → much tighter OH constraint
- **Conclusion:** Global OH is "well buffered" against perturbations
- **Impact:** Foundational paper — established that OH is more stable than previously thought
- **PDF:** `Montzka, S.A. et al.2011.pdf`

---

### Turner et al. (2017) — PNAS 114, 5367
**"Ambiguity in the causes for decadal trends in atmospheric methane and hydroxyl"**
- **Method:** Multi-species 2-box model inversion (CH₄ + MCF + δ¹³CH₄), 1983–2015
- **Key data:**
  - Most mathematically likely solution: 25 Tg/yr CH₄ emission decrease (2003–2016) + ~7% OH decrease
  - Alternative: time-invariant OH + emission increases (also fits observations)
  - τ_CH₄: 9.2 ± 0.2 yr
- **Key conclusion:** Problem is underdetermined — current observations cannot separate emissions from OH trends
- **Note:** 2-box framework; Naus et al. (2019) later showed this introduces ~10% bias
- **PDF:** `Turner, A.J. et al.2017.pdf`

---

### Naus et al. (2021) — ACP 21, 4809
**"Constraints on global OH variability from 3D MCF inversion"**
- **Method:** Full 3D TM5-4DVAR variational inversion of MCF
- **Period:** 1994–2017
- **Key data:**
  - OH IAV: 0.6–0.8% (1σ) — even smaller than Montzka (2011)
  - No significant OH trend
  - NH/SH loss ratio is species-dependent
- **Advance:** Avoids 2-box assumptions that biased Rigby (2017) and Turner (2017)
- **Limitation:** MCF signal decaying → constraint weakening post-2020
- **PDF:** `Naus_2021_ACP_4809.pdf`

---

### Naus et al. (2019) — ACP 19, 407
**"Constraints and biases in a tropospheric two-box model of OH"**
- **Key finding:** Two-box model introduces ~10% bias in absolute [OH]
- **Impact:** 1–2% shifts in apparent IAV anomalies
- **Critical insight:** NH/SH [OH] ratio from MCF ≠ ratio relevant for CH₄
- **Implication:** Rigby (2017) and Turner (2017) may overstate OH variability
- **PDF:** `Naus_2019_ACP_407.pdf`

---

### McNorton et al. (2016) — ACP 16, 7943
**"Role of OH variability in the stalling of the global atmospheric CH4 growth rate"**
- **Method:** 3D CTM + MCF-derived OH variations
- **Period:** 1998–2014
- **Key finding:** OH increases contributed to CH₄ stagnation period (1999–2006)
- **PDF:** `McNorton_2016_ACP_7943.pdf`

---

## Category 2: CTM / Bottom-Up Studies

---

### He et al. (2021) — GRL 48, e2021GL094140
**"Hydroxyl radical (OH) response to meteorological forcing and implication for the methane budget"**
- **Model:** GFDL-AM4.1 nudged to different reanalyses (MERRA-2, ERA5, JRA-55)
- **Period:** 1980–2017
- **Key data:**
  - Global OH varies ~2% depending on met reanalysis
  - → 11.2 Tg/yr difference in derived CH₄ emissions
  - → 0.24 yr difference in CH₄ lifetime
  - Met affects OH **mean** but NOT the **trend**
  - OH trend strongly correlates with reactive nitrogen emissions
- **Implication:** Meteorology sets a floor for OH uncertainty; emission inventories drive the trend
- **PDF:** `He, J. et al.2021.pdf`

---

### Nicely et al. (2018) — JGR Atmospheres 123, 12,742
**"Changes in global tropospheric OH expected as a result of climate change over the last several decades"**
- **Method:** Empirical model using observed O₃ column, reanalysis H₂O, model NOx, Hadley cell width
- **Period:** 1980–2015
- **Key data:**
  - OH trend: **+0.95 ± 0.18 %/decade** (from H₂O, NOx, O₃, tropical expansion)
  - CH₄-induced decline: −1.01 ± 0.05 %/decade
  - **94% of CH₄-induced OH decline offset** by other drivers
  - Net: near-zero OH trend — consistent with MCF observations
  - Ranked drivers: H₂O > NOx > overhead O₃ > Hadley cell
- **PDF:** `Nicely, J.M. et al.2018.pdf`

---

### Acquah et al. (2025) — ACP 25, 13665
**"Effects of different emission inventories on tropospheric ozone and methane lifetime"**
- **Model:** EMAC (ECHAM5/MESSy) in QCTM mode
- **Period:** 2000–2010
- **OH attribution (CH₄-weighted):**
  - Anthropogenic (non-traffic + transport + shipping + aviation): 36–39%
  - Lightning NOx: ~25%
  - Biogenic: ~12%
  - Stratospheric transport: ~9%
  - CH₄ decomposition: ~7%
  - Biomass burning: 5–6%
- **Key finding:** CEDS has +9.02 Tg(N)/yr NOx vs MACCity → more OH → shorter τ
- **PDF:** `Acquah_2025_ACP_13665.pdf`

---

### Mertens et al. (2024) — ACP 24, 12079
**"Impact of transport sector emissions on future ozone, methane, and OH"**
- **Model:** EMAC
- **Key data:**
  - Present-day (2015) τ_trop: 7.63 years
  - SSP1-2.6 (2050): τ_trop = 8.50 years
  - SSP3-7.0 (2050): τ_trop = 8.39 years
- **Key finding:** Clean air policies reducing NOx → less OH → longer τ_CH₄
- **PDF:** `Mertens_2024_ACP_12079.pdf`

---

### Anderson et al. (2021) — ACP 21, 6481
**"Spatial and temporal variability in tropospheric OH"**
- **Model:** MERRA-2 GMI
- **Period:** 1980–2018
- **Key data:**
  - ENSO: ~30% of global OH variability in boreal winter
  - El Niño: 10–15% reduction in tropical Pacific column OH
  - 1997–1998 El Niño: ~9% global OH decrease
  - ATom validation: ~20% high bias (within 35% measurement uncertainty)
- **PDF:** `Anderson_2021_ACP_6481.pdf`

---

### Stevenson et al. (2020) — ACP 20, 12905
**"Trends in global tropospheric hydroxyl radical and methane lifetime since 1850 from AerChemMIP"**
- **Key data:**
  - τ_atm present-day: 8.4 ± 0.3 yr
  - OH increased ~8–12% from 1850 to present
  - NH/SH ratio: ~1.28
- **PDF:** `Stevenson_2020_ACP_12905.pdf`

---

### Zhao et al. (2020a) — ACP 20, 9525
**"Inter-model comparison of global OH distributions (CCMI)"**
- **Key data:** [OH] range 0.81–1.51 × 10⁶; τ_trop range 7.1–13.7 yr
- **PDF:** `Zhao_2020_ACP_9525.pdf`

### Zhao et al. (2020b) — ACP 20, 13011
**"On the role of trend and variability of OH in the global CH₄ budget"**
- **Key data:** No significant OH trend 1980–2018; OH variability contributes ~5 Tg/yr
- **PDF:** `Zhao_2020_ACP_13011.pdf`

### Zhao et al. (2019) — ACP 19, 13701
**"Inter-model OH comparison (CCMI Phase 1)"**
- **Key data:** Multi-model mean [OH] = 1.11 ± 0.17 × 10⁶; τ = 9.3 ± 1.7 yr
- **PDF:** `Zhao_2019_ACP_13701.pdf`

---

### Rowlinson et al. (2019) — ACP 19, 8669
**"Impact of El Niño–Southern Oscillation on tropospheric ozone, methane, and OH"**
- **Model:** p-TOMCAT CTM (1997–2016)
- **Key finding:** ENSO drives strong regional OH changes; 1997–1998 fires → OH suppression
- **PDF:** `Rowlinson_2019_ACP_8669.pdf`

---

### Additional downloaded CTM/CCM papers (data extraction pending):
- Wild et al. (2020) — `Wild_2020_ACP_4047.pdf`
- Lelieveld et al. (2016) — `Lelieveld_2016_ACP_12477.pdf`
- Murray et al. (2014) — `Murray_2014_ACP_3589.pdf`
- Naik et al. (2013) — `Naik_2013_ACP_5277.pdf`
- Voulgarakis et al. (2013) — `Voulgarakis_2013_ACP_4839.pdf`
- Holmes et al. (2013) — `Holmes_2013_ACP_285.pdf`

---

## Category 3: Chemical Feedbacks

---

### Nguyen et al. (2020) — GRL 47, e2019GL085706
**"Effects of chemical feedbacks on decadal methane emissions estimates"**
- **Method:** Two-box model with coupled CH₄-CO-OH chemistry
- **Key data:**
  - Neglecting CH₄-OH feedbacks → **25% bias** in emission estimates over 10 years
  - Strong biomass burning (El Niño) → ↑CO → ↓OH → indirect CH₄ growth
  - Decadal attributions depend on both OH and CO assumptions
- **Implication:** Static OH inversions have systematic errors
- **PDF:** `Nguyen, N.H. et al.2020.pdf`

---

## Category 4: Satellite / ML

---

### Duncan et al. (2024) — ACP 24, 13001
**"Novel observational constraints on tropospheric OH"**
- **Type:** Perspective paper — no quantitative global OH
- **Proposes:** HCHO + CO + O₃ satellite columns for OH inference
- **PDF:** `Duncan_2024_ACP_13001.pdf`

### Nicely et al. (2020) — ACP 20, 1341
**"ML examination of hydroxyl radical differences among CCMI models"**
- **Key finding:** NOx is #1 predictor; O₃, H₂O, photolysis follow
- **PDF:** `Nicely_2020_ACP_1341.pdf`

---

## Category 5: Synthesis

---

### Saunois et al. (2025) — ESSD 17, 1873
**"The Global Methane Budget 2000–2020"**
- OH + Cl sink: 595 Tg/yr [510–663] (2010–2019); τ_atm: 9.3 yr
- **PDF:** `Saunois_2025_ESSD_1873.pdf`

### Saunois et al. (2020) — ESSD 12, 1561
**"The Global Methane Budget 2000–2017"**
- OH sink = 553 ± 56 Tg/yr; τ_trop = 11.2 ± 1.3; τ_atm = 9.1 ± 0.9
- **PDF:** `Saunois_2020_ESSD_1561.pdf`

### Saunois et al. (2017) — ACP 17, 11135
**"Variability and quasi-decadal changes in the methane budget"**
- **PDF:** `Saunois_2017_ACP_11135.pdf` — data extraction pending

---

## Misidentified Files

| File | Actual Content | Action Needed |
|------|---------------|--------------|
| `Rigby, M. et al.2017.pdf` | Duplicate of McNorton (2016) — identical 2,786,450 bytes | Replace with real Rigby 2017 PNAS |
| `Prather, M.J. & Zhu, X.2024.pdf` | Prather & Zhu (2024) Elementa — ozone lifetimes paper | Wrong paper; real Prather OH/CH₄ paper identity uncertain |
