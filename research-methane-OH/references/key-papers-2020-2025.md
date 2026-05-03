# Paper: Zhao et al. (2020) — CCMI OH Inter-model Comparison

**Full Title:** Inter-model comparison of global hydroxyl radical (OH) distributions and their impact on atmospheric methane over the 2000–2016 period

**Citation:** Zhao, Y., et al., Atmos. Chem. Phys., 20, 9525–9555, 2020.

**DOI:** https://doi.org/10.5194/acp-20-9525-2020

**Method:** CCM (Chemistry-Climate Model Initiative Phase 1 — 12 models)

**Status:** [Complete] — Open Access (Copernicus)

---

## Key Data Extracted

### Global Mean [OH]
- Range across CCMI models: **0.81–1.51 × 10⁶ molec/cm³**
- This represents a factor ~2 spread among models
- Weighting: CH₄-reaction weighted ($[OH]_{CH_4}$) per Lawrence et al. (2001)

### Methane Lifetime (Tropospheric, w.r.t. OH)
- Range across models: **7.1–13.7 years**
- Corresponds to the [OH] spread above

### NH/SH Ratio
- Most models: ~1.2–1.3
- Some outliers up to 1.4

### Key Drivers of Inter-model Spread
1. NOx emissions and photochemistry
2. Photolysis rates (particularly J(O¹D))
3. Water vapor fields
4. CO burden differences

### Interannual Variability
- Multi-model OH IAV: ~2–3% (1σ)

---

## Relevance to Project
- Establishes the current state of model uncertainty for OH
- Provides the range envelope for database entries
- Confirms MCF-based constraint remains essential
- Period: 2000–2016

---

# Paper: Zhao et al. (2020) — OH Trend and Methane Budget

**Full Title:** On the role of trend and variability of hydroxyl radical (OH) in the global methane budget

**Citation:** Zhao, Y., et al., Atmos. Chem. Phys., 20, 13011–13022, 2020.

**DOI:** https://doi.org/10.5194/acp-20-13011-2020

**Method:** Box model + CCMI multi-model ensemble

**Status:** [Complete] — Open Access (Copernicus)

---

## Key Data Extracted

### OH Trend (1980–2018)
- **No significant trend detected** in global mean OH
- Global anomaly: −0.07 ± 0.54 × 10⁵ molec/cm³
- Consistent with stable OH over this period

### Impact on Methane Budget
- OH variability contributes ~5 Tg CH₄/yr uncertainty to the budget
- Reference τ: 9.1 years (used as baseline)

### Key Finding
- MCF-derived constraints suggest global OH is relatively stable
- Interannual variability is small (<3%)
- Both MCF inversions and multi-model results agree on this

---

## COVID Flag
- Analysis period ends 2018 — pre-COVID
- Does NOT address the 2020 NOx anomaly

---

# Paper: Stevenson et al. (2020) — AerChemMIP

**Full Title:** Trends in global tropospheric hydroxyl radical and methane lifetime since 1850 from AerChemMIP

**Citation:** Stevenson, D. S., et al., Atmos. Chem. Phys., 20, 12905–12920, 2020.

**DOI:** https://doi.org/10.5194/acp-20-12905-2020

**Method:** CCM (CMIP6 AerChemMIP multi-model ensemble)

**Status:** [Complete] — Open Access (Copernicus)

---

## Key Data Extracted

### Present-day CH₄ Lifetime
- **τ_atm (whole-atmosphere): 8.4 ± 0.3 years** (multi-model mean)
- This is notably shorter than IPCC AR6 (9.1 ± 0.9)

### Historical OH Trend
- OH increased **~8–12%** from 1850 to present
- Driven by competing effects:
  - ↑NOx emissions → ↑OH (dominant)
  - ↑CH₄, ↑CO → ↓OH (partially offsetting)

### NH/SH Ratio
- ~1.28 (present-day multi-model mean)

### Key Finding
- Net effect of industrialization has been to increase global OH
- But rate of increase has slowed in recent decades as NOx stabilizes
- Referenced in Acquah et al. (2025) and IPCC AR6

---

# Paper: Saunois et al. (2020) — Global Methane Budget

**Full Title:** The Global Methane Budget 2000–2017

**Citation:** Saunois, M., et al., Earth Syst. Sci. Data, 12, 1561–1623, 2020.

**DOI:** https://doi.org/10.5194/essd-12-1561-2020

**Method:** Synthesis (multi-approach: top-down inversions, bottom-up inventories, process models)

**Status:** [Complete] — Open Access (Copernicus)

---

## Key Data Extracted

### OH Sink of CH₄
- **553 ± 56 Tg CH₄/yr** (dominant sink, ~90% of total chemical sink)

### Methane Lifetimes
- **Tropospheric lifetime w.r.t. OH: 11.2 ± 1.3 years**
- **Total atmospheric lifetime: 9.1 ± 0.9 years**
- Additional sinks: stratospheric loss, soil uptake, Cl reaction

### Period
- Decade average: 2008–2017

### Key Finding
- This is THE reference document for the global methane budget
- OH-related lifetime values are derived from MCF constraints
- Serves as anchor point for all other studies

---

# Paper: Nicely et al. (2020) — ML Analysis of OH

**Full Title:** A machine learning examination of hydroxyl radical differences among model simulations for CCMI

**Citation:** Nicely, J. M., et al., Atmos. Chem. Phys., 20, 1341–1361, 2020.

**DOI:** https://doi.org/10.5194/acp-20-1341-2020

**Method:** Machine Learning (Random Forest) applied to CCMI model output

**Status:** [Complete] — Open Access (Copernicus)

---

## Key Data Extracted

### Inter-model OH Spread
- Methane lifetime spread across CCMI models: **45%–80%**
- Primary drivers of spread (ranked by importance):
  1. NOx (dominant)
  2. Tropospheric O₃ column
  3. Water vapor
  4. Photolysis rates

### Key Finding
- ML approach identifies NOx as single most important predictor of inter-model OH differences
- Suggests that emission inventory choice is critical for OH accuracy
- Models with higher NOx → higher OH → shorter τ_CH4
- This links directly to Acquah et al. (2025) findings about CEDS vs MACCity

---

# Paper: Anderson et al. (2021) — OH and Climate Variability

**Full Title:** Spatial and temporal variability in the hydroxyl (OH) radical: understanding the role of large-scale climate features and their influence on OH through its dynamical and photochemical drivers

**Citation:** Anderson, D. C., et al., Atmos. Chem. Phys., 21, 6481–6508, 2021.

**DOI:** https://doi.org/10.5194/acp-21-6481-2021

**Method:** CTM (MERRA-2 GMI) + CCMI models + ATom observations

**Status:** [Complete] — Open Access (Copernicus)

---

## Key Data Extracted

### ENSO-OH Relationship
- ENSO is the **dominant mode** of global OH variability
- Explains ~30% of total OH variance in boreal winter
- El Niño → **10–15% reduction** in tropospheric column OH over tropical Pacific/Australia

### 1997–1998 ENSO Event
- **9% global OH decrease** (from Rowlinson et al., 2019)
- Up to 20% over Indian Ocean (from Duncan et al., 2003)

### Model Validation (ATom)
- MERRA-2 GMI has ~20% high bias vs in-situ ATom OH observations
- NH normalized mean bias: 19%
- SH normalized mean bias: 16%
- Both within measurement uncertainty (35% for ATom OH)

### OH Variability Mechanisms
- Upper troposphere: NOx (lightning) changes dominate
- Lower troposphere: Water vapor + O(¹D) changes dominate
- Biomass burning CO: Major regional OH sink during El Niño

---

# Paper: Acquah et al. (2025) — Emission Inventory Effects

**Full Title:** Effects of different emission inventories on tropospheric ozone and methane lifetime

**Citation:** Acquah, C., Stecher, L., Mertens, M., and Jöckel, P., Atmos. Chem. Phys., 25, 13665–13686, 2025.

**DOI:** https://doi.org/10.5194/acp-25-13665-2025

**Method:** CCM (EMAC in QCTM mode) — CCMI-1 vs CCMI-2022 emissions

**Status:** [Complete] — Open Access (Copernicus)

---

## Key Data Extracted

### Emission Inventory Effect on CH₄ Lifetime
- CEDS (CCMI-2022) produces **shorter CH₄ lifetime** than MACCity (CCMI-1)
- Mechanism: CEDS has higher global anthropogenic NOx (+9.02 Tg(N)/yr average 2000–2010)
- More NOx → more OH → shorter τ_CH4

### OH Attribution (CH₄-weighted, Lawrence et al. 2001)
- **Anthropogenic non-traffic + land transport + shipping + aviation:** 36% (EMIS-01) to 39% (EMIS-02) of global tropospheric [OH]_{CH4}
- **Lightning NOx:** ~25%
- **Biogenic emissions:** ~12%
- **Stratospheric transport:** ~9%
- **CH₄ decomposition:** ~7%
- **N₂O:** ~4%
- **Biomass burning:** 5–6%

### Category-specific OH changes (EMIS-02 vs EMIS-01)
- Anthropogenic non-traffic: **+0.03 × 10⁶ molec/cm³**
- Shipping: **+0.02 × 10⁶ molec/cm³**
- Biomass burning: **+0.02 × 10⁶ molec/cm³**
- Land transport: **+0.01 × 10⁶ molec/cm³**
- Aviation: **−0.01 × 10⁶ molec/cm³**
- Biogenic: **−0.01 × 10⁶ molec/cm³**

### Reference Values Cited in Paper
- Prinn et al. (2005): τ = 10.2 $^{+0.9}_{-0.7}$ years (MCF-based)
- Prather et al. (2012): τ = 9.1 ± 0.9 years
- Stevenson et al. (2020) AerChemMIP: τ = 8.4 ± 0.3 years
- IPCC AR5 (Myhre et al., 2013): τ = 9.25 ± 0.6 years
- IPCC AR6 (Szopa et al., 2021): τ = 9.1 ± 0.9 years

### Tagging Methodology
- First application of tagging approach to attribute CH₄ lifetime to emission sectors
- Uses EMAC/MECCA chemistry with combinatorial tagged tracers
- Tropopause: climatological 300–215·cos²(φ) hPa (Lawrence et al., 2001)
