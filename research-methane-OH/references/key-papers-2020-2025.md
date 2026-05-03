# Paper Reference Notes — research-methane-OH

## Category 1: MCF / Top-Down Studies

---

### Naus et al. (2021) — ACP 21, 4809
**"Constraints on global OH variability from 3D MCF inversion"**
- **Method:** Full 3D TM5-4DVAR variational inversion of MCF
- **Period:** 1994–2017
- **Key data:**
  - OH interannual variability: 0.6–0.8% (1σ) — very small
  - No significant OH trend over study period
  - NH/SH loss ratio is species-dependent (MCF vs CH₄)
- **Advance over prior work:** Avoids 2-box model assumptions that biased Rigby (2017) and Turner (2017)
- **Limitation:** MCF signal decaying → constraint weakening post-2020
- **PDF:** `mcf-topdown/Naus_2021_ACP_4809.pdf`

---

### Naus et al. (2019) — ACP 19, 407
**"Constraints and biases in a tropospheric two-box model of OH"**
- **Key finding:** Two-box model approximations introduce ~10% bias in absolute [OH]
- **Impact:** 1–2% shifts in apparent interannual anomalies
- **Critical insight:** NH/SH [OH] ratio derived from MCF is not the same ratio relevant for CH₄
  - MCF has different T-dependent kinetics than CH₄ → "sees" different OH
  - Interhemispheric exchange rate varies with time (as MCF source/sink balance shifts)
- **Implication:** Previous large IAV claims (Rigby 2017, Turner 2017) may be biased high
- **PDF:** `mcf-topdown/Naus_2019_ACP_407.pdf`

---

### McNorton et al. (2016) — ACP 16, 7943
**"Role of OH variability in the stalling of the global atmospheric CH4 growth rate from 1999 to 2006"**
- **Method:** Box model MCF inversion
- **Period:** 1998–2014
- **Key finding:** OH increases may have contributed to CH₄ stagnation period (1999–2006)
- **PDF:** `mcf-topdown/McNorton_2016_ACP_7943.pdf`

---

## Category 2: CTM / Bottom-Up Studies

---

### Acquah et al. (2025) — ACP 25, 13665
**"Effects of different emission inventories on tropospheric ozone and methane lifetime"**
- **Model:** EMAC (ECHAM5/MESSy) in QCTM mode
- **Period:** 2000–2010
- **OH attribution (CH₄-weighted):**
  - Anthropogenic non-traffic + transport + shipping + aviation: 36–39%
  - Lightning NOx: ~25%
  - Biogenic: ~12%
  - Stratospheric transport: ~9%
  - CH₄ decomposition: ~7%
  - Biomass burning: 5–6%
- **Key finding:** CEDS has +9.02 Tg(N)/yr NOx vs MACCity → more OH → shorter τ
- **PDF:** `ctm-bottomup/Acquah_2025_ACP_13665.pdf`

---

### Mertens et al. (2024) — ACP 24, 12079
**"Impact of transport sector emissions on future ozone, methane, and OH"**
- **Model:** EMAC
- **Key data:**
  - Present-day (2015) τ_trop: 7.63 years
  - SSP1-2.6 (2050): τ_trop = 8.50 years
  - SSP3-7.0 (2050): τ_trop = 8.39 years
- **Key finding:** Clean air policies reducing NOx → less OH → longer τ_CH₄
- **Implication:** Methane mitigation becomes harder as NOx declines
- **PDF:** `ctm-bottomup/Mertens_2024_ACP_12079.pdf`

---

### Anderson et al. (2021) — ACP 21, 6481
**"Spatial and temporal variability in tropospheric OH"**
- **Model:** MERRA-2 GMI (specified dynamics)
- **Period:** 1980–2018
- **Key data:**
  - ENSO explains ~30% of global OH variability in boreal winter
  - El Niño: 10–15% reduction in tropical Pacific column OH
  - 1997–1998 El Niño: ~9% global OH decrease
  - ATom validation: ~20% high bias (within 35% measurement uncertainty)
- **PDF:** `ctm-bottomup/Anderson_2021_ACP_6481.pdf`

---

### Stevenson et al. (2020) — ACP 20, 12905
**"Trends in global tropospheric hydroxyl radical and methane lifetime since 1850 from AerChemMIP"**
- **Key data:**
  - τ_atm present-day: 8.4 ± 0.3 yr (multi-model; notably shorter than MCF-based)
  - OH increased ~8–12% from 1850 to present
  - NH/SH ratio: ~1.28
- **PDF:** `ctm-bottomup/Stevenson_2020_ACP_12905.pdf`

---

### Zhao et al. (2020a) — ACP 20, 9525
**"Inter-model comparison of global OH distributions and impact on CH₄ over 2000–2016"**
- **Models:** 12 CCMI Phase 1
- **Key data:** [OH] range 0.81–1.51 × 10⁶; τ_trop range 7.1–13.7 yr
- **PDF:** `ctm-bottomup/Zhao_2020_ACP_9525.pdf`

---

### Zhao et al. (2020b) — ACP 20, 13011
**"On the role of trend and variability of OH in the global CH₄ budget"**
- **Key data:** No significant OH trend 1980–2018; OH variability contributes ~5 Tg/yr to budget uncertainty
- **PDF:** `ctm-bottomup/Zhao_2020_ACP_13011.pdf`

---

### Zhao et al. (2019) — ACP 19, 13701
**"Inter-model OH comparison and impact on CH₄ (CCMI Phase 1)"**
- **Key data:** Multi-model mean [OH] = 1.11 ± 0.17 × 10⁶; τ = 9.3 ± 1.7 yr
- **PDF:** `ctm-bottomup/Zhao_2019_ACP_13701.pdf`

---

### Rowlinson et al. (2019) — ACP 19, 8669
**"Impact of El Niño–Southern Oscillation on tropospheric ozone, methane, and OH"**
- **Model:** p-TOMCAT CTM
- **Period:** 1997–2016
- **Key finding:** ENSO drives strong regional OH changes; 1997–1998 fires → massive OH suppression
- **PDF:** `ctm-bottomup/Rowlinson_2019_ACP_8669.pdf`

---

### Wild et al. (2020) — ACP 20, 4047
**"Global sensitivity analysis of chemistry-climate models"**
- **PDF:** `ctm-bottomup/Wild_2020_ACP_4047.pdf`
- **Status:** PDF downloaded; quantitative OH data not yet extracted

---

### Voulgarakis et al. (2013) — ACP 13, 4839
**"Analysis of present-day and future OH and methane lifetime in the ACCMIP"**
- **Models:** 14 ACCMIP models
- **Key data:** Multi-model mean [OH] = 1.13 ± 0.09 × 10⁶; τ_trop = 9.8 ± 1.6 yr
- **PDF:** `ctm-bottomup/Voulgarakis_2013_ACP_4839.pdf`

---

### Additional downloaded CTM/CCM papers (data extraction pending):
- Naik et al. (2013) — `ctm-bottomup/Naik_2013_ACP_5277.pdf`
- Holmes et al. (2013) — `ctm-bottomup/Holmes_2013_ACP_285.pdf`
- Lelieveld et al. (2016) — `ctm-bottomup/Lelieveld_2016_ACP_12477.pdf`
- Murray et al. (2014) — `ctm-bottomup/Murray_2014_ACP_3589.pdf`

---

## Category 3: Satellite / ML

---

### Duncan et al. (2024) — ACP 24, 13001
**"Novel observational constraints on tropospheric OH"**
- **Type:** Perspective/opinion paper
- **Key argument:** MCF constraint is degrading; need integrated satellite observing system
- **Proposes:** Combining HCHO + CO + O₃ satellite columns for OH inference
- **No quantitative global OH value** — framework paper
- **PDF:** `satellite-ml/Duncan_2024_ACP_13001.pdf`

---

### Nicely et al. (2020) — ACP 20, 1341
**"ML examination of hydroxyl radical differences among CCMI models"**
- **Method:** Random Forest ML on CCMI model outputs
- **Key finding:** NOx is #1 predictor; O₃, H₂O, photolysis follow
- **PDF:** `satellite-ml/Nicely_2020_ACP_1341.pdf`

---

## Category 4: Synthesis

---

### Saunois et al. (2025) — ESSD 17, 1873
**"The Global Methane Budget 2000–2020"**
- **Key data:**
  - OH + Cl sink: 595 Tg/yr [510–663] (2010–2019)
  - Total chemical: 623 Tg/yr
  - τ_trop: 11.2 yr; τ_atm: 9.3 yr
  - Soil: 30 Tg/yr [15–45]
- **Period:** Extends to 2020 (first synthesis including COVID year)
- **PDF:** `synthesis/Saunois_2025_ESSD_1873.pdf`

---

### Saunois et al. (2020) — ESSD 12, 1561
**"The Global Methane Budget 2000–2017"**
- **Key data:** OH sink = 553 ± 56 Tg/yr; τ_trop = 11.2 ± 1.3; τ_atm = 9.1 ± 0.9
- **PDF:** `synthesis/Saunois_2020_ESSD_1561.pdf`

---

### Saunois et al. (2017) — ACP 17, 11135  
**"Variability and quasi-decadal changes in the methane budget"**
- **PDF:** `synthesis/Saunois_2017_ACP_11135.pdf`
- **Status:** PDF downloaded; data extraction pending
