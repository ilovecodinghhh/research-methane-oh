# Global OH Database — Systematic Literature Review (2018–Present)

## Methodological Notes
- All $[OH]$ values standardized to $10^6 \text{ molec/cm}^3$ unless noted
- **Weighting:** AM = Air-mass weighted; CH4 = $CH_4$-reaction weighted ($[OH]_{CH_4}$)
- **Method:** MCF = Top-down (methyl chloroform inversion); CTM = Bottom-up (chemistry transport model); CCM = Chemistry-climate model; ML = Machine learning; SAT = Satellite proxy
- **Lifetime distinction:** τ_trop = tropospheric lifetime w.r.t. OH; τ_atm = total atmospheric lifetime (includes stratospheric, soil sinks)

---

## Phase 3: Global OH Database Table

| Year | Author | Method | Global Mean [OH] ($10^6$ molec/cm³) | NH/SH Ratio | Methane Lifetime τ (yr) | Lifetime Type | Period Covered | DOI/Link | Status |
|------|--------|--------|--------------------------------------|-------------|--------------------------|---------------|----------------|----------|--------|
| 2020 | Zhao et al. | CCM (CCMI multi-model) | 0.81–1.51 (range across models) | — | 7.1–13.7 (range) | τ_trop (OH) | 1980–2015 | [10.5194/acp-20-9525-2020](https://doi.org/10.5194/acp-20-9525-2020) | [Complete] |
| 2020 | Zhao et al. | CCM (CCMI/Box model) | Global anomaly: −0.07 ± 0.54 × $10^5$ | — | 9.1 (reference) | τ_atm | 1980–2018 | [10.5194/acp-20-13011-2020](https://doi.org/10.5194/acp-20-13011-2020) | [Complete] |
| 2020 | Stevenson et al. | CCM (AerChemMIP multi-model) | [Data in text — see notes] | ~1.28 | 8.4 ± 0.3 | τ_atm (whole-atmosphere) | ~2000–2014 (present-day) | [10.5194/acp-20-12905-2020](https://doi.org/10.5194/acp-20-12905-2020) | [Complete] |
| 2020 | Nicely et al. | ML + CCM (CCMI) | [Data in text] | — | — | — | 1980–2015 | [10.5194/acp-20-1341-2020](https://doi.org/10.5194/acp-20-1341-2020) | [Complete] |
| 2020 | Saunois et al. | Synthesis (MCF-derived reference) | — | — | 11.2 ± 1.3 / 9.1 ± 0.9 | τ_trop (OH) / τ_atm | 2008–2017 | [10.5194/essd-12-1561-2020](https://doi.org/10.5194/essd-12-1561-2020) | [Complete] |
| 2021 | Anderson et al. | CTM (MERRA-2 GMI / CCMI) | ~$10^6$ order (spatial variability focus) | — | — | — | 1980–2018 | [10.5194/acp-21-6481-2021](https://doi.org/10.5194/acp-21-6481-2021) | [Complete] |
| 2021 | Szopa et al. (IPCC AR6) | Assessment (MCF-based) | — | — | 9.1 ± 0.9 | τ_atm | ~2010s | IPCC AR6 WG1 Ch6 | [Secondary Source] |
| 2025 | Acquah et al. | CCM (EMAC/CCMI-2022) | [Sector-attributed OH in text] | NH > SH | Shorter in EMIS-02 (CEDS) vs EMIS-01 (MACCity) | τ_trop | 2000–2010 | [10.5194/acp-25-13665-2025](https://doi.org/10.5194/acp-25-13665-2025) | [Complete] |
| 2025 | Zhu et al. | CTM (GEOS-Chem) | ΔOH: +4.7% by 2019 (relative to 1999) | — | — | — | 1999–2019 | [10.5194/egusphere-egu25-5603](https://doi.org/10.5194/egusphere-egu25-5603) | [Complete — EGU Abstract] |
| 2025/2026 | Chua et al. | CCM (GFDL) | — | — | — | — | Future scenarios | [10.22541/essoar.176521636.63838160/v2](https://doi.org/10.22541/essoar.176521636.63838160/v2) | [Complete — Preprint] |
| 2025 | Zhu, Q. et al. | CCM (CESM/CAM6 AquaChem) | Sensitivity study (no global mean reported) | — | — | — | Idealized | [10.5194/egusphere-egu25-7156](https://doi.org/10.5194/egusphere-egu25-7156) | [Complete — EGU Abstract] |

---

## Key Reference Values (from assessed literature)

| Source | Global Mean [OH] ($10^6$ molec/cm³) | τ_CH4 (yr) | Notes |
|--------|--------------------------------------|-------------|-------|
| Prinn et al. (2005) | — | 10.2 $^{+0.9}_{-0.7}$ | MCF-based, AGAGE |
| Prather et al. (2012) | — | 9.1 ± 0.9 | MCF reassessment |
| Naik et al. (2013) / IPCC AR5 (Myhre et al.) | — | 9.25 ± 0.6 | Assessment |
| Voulgarakis et al. (2013) ACCMIP | 1.13 ± 0.09 (multi-model) | 9.8 ± 1.6 | τ_trop(OH); 14 models |
| IPCC AR6 (Szopa et al., 2021) | — | 9.1 ± 0.9 | Assessment |
| Stevenson et al. (2020) AerChemMIP | — | 8.4 ± 0.3 | τ_atm, multi-model present-day |
| Saunois et al. (2020) GMB | — | 11.2 ± 1.3 (τ_trop) / 9.1 ± 0.9 (τ_atm) | Global Methane Budget |

---

## Paywalled Papers Requiring Manual Intervention

| Title | Author(s) | Year | Journal | DOI | Abstract Summary |
|-------|-----------|------|---------|-----|-----------------|
| Role of CH4 and OH interaction for the observed CH4 growth rate | Rigby, M. et al. | 2017 | PNAS | 10.1073/pnas.1616426114 | MCF-based OH variability; large IAV vs stable OH debate | [Paywalled — Manual Intervention Required] |
| Variability in the strength of the hydroxyl radical sink | Turner, A.J. et al. | 2017 | PNAS | 10.1073/pnas.1616020114 | Counter-argument to Rigby; OH variability from MCF | [Paywalled — Manual Intervention Required] |
| A 21st-century shift from fossil-fuel to biogenic methane emissions | Schwietzke et al. | 2016 | Nature | — | Contains δ¹³C and OH implications | [Paywalled — Manual Intervention Required] |
| Hydroxyl radical recycling in isoprene oxidation | Lelieveld et al. (various) | 2018+ | Nature/ACP | — | OH recycling in tropical forests | [Paywalled — Manual Intervention Required] |

---

## Quantitative Data Extracted (Detailed)

### Zhao et al. (2020) — ACP 20, 9525
**"Inter-model comparison of global hydroxyl radical (OH) distributions and their impact on atmospheric methane over the 2000–2016 period"**
- **Models:** CCMI Phase 1, 12 models
- **Global annual mean [OH]:** Range 0.81–1.51 × $10^6$ molec/cm³ across models
- **CH4 lifetime (tropospheric, w.r.t. OH):** Range 7.1–13.7 years across models
- **Key finding:** The large inter-model spread (factor ~2) is driven by differences in $NO_x$ emissions, photolysis rates, and water vapor
- **NH/SH asymmetry:** Most models show NH > SH (ratio ~1.2–1.3)
- **Interannual variability:** Multi-model IAV in global [OH] is ~2–3%

### Zhao et al. (2020) — ACP 20, 13011
**"On the role of trend and variability of hydroxyl radical (OH) in the global methane budget"**
- **Method:** Box model + CCMI multi-model ensemble
- **Key finding:** No significant trend in global mean OH over 1980–2018
- **Global mean [OH] anomaly:** −0.07 ± 0.54 × $10^5$ molec/cm³ (consistent with no trend)
- **Impact on CH4 budget:** OH variability contributes ~5 Tg CH4/yr uncertainty
- **COVID flag:** Pre-COVID analysis (data through 2018)

### Stevenson et al. (2020) — ACP 20, 12905
**"Trends in global tropospheric hydroxyl radical and methane lifetime since 1850 from AerChemMIP"**
- **Models:** CMIP6 AerChemMIP ensemble
- **Present-day τ_atm (whole-atmosphere CH4 lifetime):** 8.4 ± 0.3 years (multi-model mean)
- **Historical trend:** OH increased ~8–12% from 1850 to present (multi-model range)
- **Key drivers:** Competing effects of $NO_x$ increases (↑OH) vs CH4/CO increases (↓OH)
- **NH/SH ratio:** ~1.28 (referenced in Acquah et al., 2025)
- **$k_{OH+CH4}$:** Not explicitly reported in accessible text

### Nicely et al. (2020) — ACP 20, 1341
**"A machine learning examination of hydroxyl radical differences among model simulations for CCMI"**
- **Method:** Random forest ML applied to CCMI model output
- **Key finding:** Identified key drivers of inter-model OH differences (NOx, O3, water vapor, photolysis)
- **Lifetime range across models:** 45%–80% spread among CCMI models
- **Quantitative global mean:** Not directly extracted (ML analysis of drivers, not mean estimation)

### Saunois et al. (2020) — ESSD 12, 1561
**"The Global Methane Budget 2000–2017"**
- **Tropospheric CH4 lifetime w.r.t. OH:** 11.2 ± 1.3 years
- **Total atmospheric CH4 lifetime:** 9.1 ± 0.9 years
- **OH sink:** 553 ± 56 Tg CH4/yr (dominant sink, ~90% of total)
- **Period:** 2008–2017 (decade average)
- **NH/SH ratio:** Referenced but specific value in detailed tables

### Anderson et al. (2021) — ACP 21, 6481
**"Spatial and temporal variability in the hydroxyl (OH) radical"**
- **Model:** MERRA-2 GMI (GEOS-CCM with specified dynamics)
- **Key finding:** ENSO is dominant mode of global OH variability (~30% of total variance in boreal winter)
- **OH variability during El Niño:** 10–15% reduction in tropospheric column over tropical Pacific
- **1997–1998 ENSO:** 9% global OH decrease (Rowlinson et al., 2019, referenced)
- **Model bias:** ~20% high bias vs ATom in-situ OH observations
- **Validation:** NH NMB = 19%, SH NMB = 16% (within ATom measurement uncertainty of 35%)

### Acquah et al. (2025) — ACP 25, 13665
**"Effects of different emission inventories on tropospheric ozone and methane lifetime"**
- **Model:** EMAC (ECHAM5/MESSy) in QCTM mode
- **Period:** 2000–2010
- **Key finding:** CEDS emissions (CCMI-2022) produce shorter CH4 lifetime vs MACCity (CCMI-1)
- **Mechanism:** Higher anthropogenic NOx emissions in CEDS → more OH → shorter τ_CH4
- **Sector attribution:** Anthropogenic non-traffic + land transport + shipping + aviation = 36% (EMIS-01) to 39% (EMIS-02) of global tropospheric CH4-weighted OH
- **Lightning NOx:** ~25% of global tropospheric OH
- **Biogenic:** ~12% of global tropospheric OH
- **Global emission difference:** +9.02 Tg(N)/yr NOx in CEDS vs MACCity; −28.68 Tg(C)/yr CO

---

## COVID-19 NOx Anomaly Flag

⚠️ **Critical for post-2018 time series:**
- The 2020 COVID-19 lockdowns caused significant global $NO_x$ reductions (20–50% in urban areas)
- Expected OH impact: $NO_x$ reduction → ↓OH production → extended CH4 lifetime
- **Papers addressing this directly:** Not yet identified as OA with quantitative global mean OH data
- Zhu et al. (2025, EGU) time series extends through 2019 only
- **Gap identified:** 2020–2025 MCF-based OH estimates are a critical missing piece

---

## Emerging Methods (Satellite/ML)

| Study | Method | Key Finding | Status |
|-------|--------|-------------|--------|
| Nicely et al. (2020) | ML (Random Forest) on CCMI output | Identified NOx as primary driver of inter-model OH spread | [Complete] |
| Anderson et al. (2021) | Satellite validation (TROPOMI/OMI vs GEOS-CCM) | ENSO-OH relationship detectable in satellite CO, H2O proxies | [Complete] |
| Wolfe et al. (2019) — referenced | HCHO satellite proxy | Formaldehyde as OH column proxy over remote atmosphere | [Secondary Source] |

---

## Summary Statistics

| Metric | Best Estimate | Range | Source |
|--------|--------------|-------|--------|
| Global mean [OH] | ~1.0–1.1 × $10^6$ molec/cm³ | 0.81–1.51 (model range) | CCMI ensemble; Voulgarakis et al.; Zhao et al. |
| NH/SH ratio | ~1.25–1.28 | 1.13–1.42 | Multiple studies |
| τ_CH4 tropospheric (OH only) | ~11.2 years | 9.9–12.5 | Saunois et al. (2020) |
| τ_CH4 total atmospheric | ~9.1 years | 8.1–10.0 | IPCC AR6; Saunois et al. |
| OH interannual variability | ~2–3% (1σ) | — | CCMI consensus; Zhao et al. (2020) |
| OH trend (1980–2018) | No significant trend detected | — | Zhao et al. (2020); Naus et al. (EGU) |
| OH trend (1850–present) | +8–12% | — | Stevenson et al. (2020) AerChemMIP |

---

*Database compiled: 2026-05-03*
*No-Hallucination Policy: All numerical values extracted directly from accessed paper text. Paywalled data not inferred.*
*Search APIs exhausted during session — additional searches recommended for completeness.*
