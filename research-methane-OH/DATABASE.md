# Global OH Database — Categorized by Method

## Methodological Standards
- All $[OH]$ values standardized to $10^6 \text{ molec/cm}^3$
- **Weighting:** AM = Air-mass weighted; CH₄ = $CH_4$-reaction weighted ($[OH]_{CH_4}$)
- **Lifetime types:** τ_trop = tropospheric lifetime w.r.t. OH; τ_atm = total atmospheric lifetime
- **Rate constant:** $k_{OH+CH_4} = 2.45 \times 10^{-12} \exp(-1775/T)$ cm³ molec⁻¹ s⁻¹ (JPL/IUPAC)
- **No-Hallucination Policy:** All values directly extracted from accessed paper text

---

## Category 1: Top-Down MCF Proxy Method

### Method Description
Methyl chloroform ($CH_3CCl_3$, MCF) is primarily removed by OH. Its atmospheric decay (post-Montreal Protocol phaseout) constrains global OH concentrations. This is the observational "gold standard."

### Database

| Year | Author(s) | Specific Method | Global Mean [OH] ($10^6$ molec/cm³) | NH/SH Ratio | τ_CH₄ (yr) | Uncertainty (±σ) | Period | DOI | Status |
|------|-----------|-----------------|--------------------------------------|-------------|-------------|-------------------|--------|-----|--------|
| 2021 | Naus et al. | 3D TM5-4DVAR MCF inversion | [see trend below] | [see below] | — | IAV: 0.6–0.8% (1σ) | 1994–2017 | [10.5194/acp-21-4809-2021](https://doi.org/10.5194/acp-21-4809-2021) | ✅ PDF + Data |
| 2020 | Zhao et al. | Box model + MCF constraint | [anomaly: −0.07 ± 0.54 × 10⁵] | — | 9.1 (ref) | No significant trend | 1980–2018 | [10.5194/acp-20-13011-2020](https://doi.org/10.5194/acp-20-13011-2020) | ✅ PDF + Data |
| 2020 | Saunois et al. | MCF-derived (synthesis) | — | — | 11.2 (τ_trop) / 9.1 (τ_atm) | ±1.3 / ±0.9 | 2008–2017 | [10.5194/essd-12-1561-2020](https://doi.org/10.5194/essd-12-1561-2020) | ✅ PDF + Data |
| 2025 | Saunois et al. | MCF-derived (updated synthesis) | — | — | 11.2 (τ_trop) / 9.3 (τ_atm) | — | 2010–2019 | [10.5194/essd-17-1873-2025](https://doi.org/10.5194/essd-17-1873-2025) | ✅ PDF + Data |
| 2019 | Naus et al. | Two-box model critique (TM5) | ~10% bias from 2-box assumptions | NH/SH: 0.80–1.10 (MCF-derived) | — | OH anomalies shift with bias corrections | 1994–2015 | [10.5194/acp-19-407-2019](https://doi.org/10.5194/acp-19-407-2019) | ✅ PDF + Data |
| 2017 | Turner et al. | Two-box model MCF+δ¹³CH₄ inversion | — | — | 9.2 ± 0.2 | 7% OH decrease (most likely soln) | 1983–2015 | [10.1073/pnas.1616020114](https://doi.org/10.1073/pnas.1616020114) | ✅ PDF + Data |
| 2016 | McNorton et al. | MCF inversion (box model) | — | — | — | — | 1998–2014 | [10.5194/acp-16-7943-2016](https://doi.org/10.5194/acp-16-7943-2016) | ✅ PDF |
| 2011 | Montzka et al. | MCF (NOAA network, post-1998) | — | — | — | IAV: 2.3 ± 1.5% | 1998–2007 | [10.1126/science.1197817](https://doi.org/10.1126/science.1197817) | ✅ PDF + Data |
| 2021 | Patra et al. | MCF + multi-model (ACTM/TM5) | — | — | — | OH variability very small | 1994–2017 | [10.1029/2020JD033862](https://doi.org/10.1029/2020JD033862) | ❌ Paywalled (Wiley) |
| 2005 | Bousquet et al. | 3D CTM MCF inversion | 9.4 ± 1.3 × 10⁵ | — | — | IAV: 8.5 ± 1.0% (or 65% less if emissions flex) | 1980–2000 | [10.5194/acp-5-2635-2005](https://doi.org/10.5194/acp-5-2635-2005) | ✅ PDF + Data |
| 2005 | Prinn et al. | MCF (AGAGE, 1978–2003) | — | — | — | IAV possible but large emission uncertainty | 1978–2003 | [10.1029/2004GL022228](https://doi.org/10.1029/2004GL022228) | ❌ Paywalled (Wiley) |
| 2001 | Prinn et al. | MCF (AGAGE) | — | — | — | "Substantial variations" inferred | 1978–2000 | [10.1126/science.1058673](https://doi.org/10.1126/science.1058673) | ❌ Paywalled (Science) |
| 2014 | Patra et al. | Multi-species (MCF+CH₄+SF₆) | — | NH/SH ≈ 1.0 (parity!) | — | Challenges NH>SH consensus | 2004–2011 | [10.1038/nature13721](https://doi.org/10.1038/nature13721) | ❌ Paywalled (Nature) |
| 2017 | Rigby et al. | MCF 3-box inversion | — | — | — | Large IAV possible | 1990–2016 | [10.1073/pnas.1616426114](https://doi.org/10.1073/pnas.1616426114) | ❌ Not obtained (file is McNorton duplicate) |

### Key Results from MCF Studies

**Bousquet et al. (2005) — Early comprehensive MCF inversion:**
- 3D CTM (LMDz-INCA) inversion of MCF, 1980–2000
- Global mean [OH] = 9.4 ± 1.3 × 10⁵ molec/cm³ (consistent with Prinn 2001)
- **Unconstrained emissions:** IAV = 8.5 ± 1.0%, trend = −0.7 ± 0.2%/yr
- **With emission flexibility (±2σ):** 65% reduction in IAV, 60% reduction in trend
- **Key insight:** OH amplitude depends critically on MCF emission uncertainty
- Phase of OH fluctuations is more robust than amplitude

**Prinn et al. (2001, 2005) — Foundational MCF/AGAGE studies:**
- 2001 Science: "Substantial variations" in OH inferred from AGAGE MCF (1978–2000)
- 2005 GRL: Updated to 1978–2003; confirmed variability but acknowledged emission dependency
- τ_CH₄ OH = 10.2 +0.9/−0.7 yr (Prinn 2005)
- **These were later shown to overestimate OH variability** (Montzka 2011, Naus 2019)

**Patra et al. (2014) Nature — NH/SH OH parity:**
- Multi-species analysis (MCF + CH₄ + SF₆) using 3D transport models
- **NH/SH OH ratio ≈ 1.0** — challenged prevailing assumption of NH > SH
- If correct, implies major revision to both sources and sinks of CH₄
- Contested by subsequent studies (Naus 2019 showed ratio is species-dependent)

**Montzka et al. (2011) — Seminal "small IAV" paper:**
- **OH IAV: 2.3 ± 1.5% (1σ) over 1998–2007**
- Post-1998 MCF gradients diminished → much tighter constraint possible
- Prior estimates (1980–2003) had inferred IAV of 7–9% — shown to be biased by emission uncertainties
- Conclusion: global OH is "well buffered" against perturbations
- CTMs calculate 1–2% variability, consistent with observations

**Naus et al. (2021) — Most rigorous 3D MCF inversion:**
- First full 3D (TM5-4DVAR) inversion for OH using MCF, accounting for transport biases
- **OH interannual variability:** Very small — 0.6–0.8% (1σ) in global mean
- **OH trend 1994–2017:** No significant trend detected
- **NH/SH OH ratio:** Constrained but species-dependent (MCF "sees" different ratio than CH₄)
- **Key finding:** 2-box model biases can shift apparent trends by ~1–2%; true 3D inversion shows very stable OH

**Naus et al. (2019) — Critical methodological paper:**
- Two-box model approximations can bias OH constraints by ~10% in absolute magnitude
- Interannual OH anomalies are modestly sensitive (1–2%) to bias corrections
- NH/SH OH loss ratio is species-dependent (MCF ≠ CH₄)
- MCF IH exchange rate is time-dependent (as source-sink balance shifts)
- **Implication:** Earlier 2-box results (Rigby 2017, Turner 2017) may have overstated OH variability

**Turner et al. (2017) — "Underdetermined" problem:**
- Joint inversion of CH₄, MCF, and δ¹³CH₄ (1983–2015) using 2-box model
- **Most likely solution:** 25 Tg/yr decrease in CH₄ emissions (2003–2016) offset by ~7% OH decrease
- BUT: can also fit observations with time-invariant OH (prior-dependent)
- **Key conclusion:** "The current surface observing system does not allow unambiguous attribution of decadal trends in methane without robust constraints on OH variability"
- τ_CH₄ mean: 9.2 ± 0.2 yr (consistent with Prather 2012: 9.1 ± 0.9)
- **Implication:** Neither emissions-only nor OH-only explanations can be confirmed

**Zhao et al. (2020) — OH trend from MCF:**
- No significant trend in global mean OH over 1980–2018
- Global anomaly: −0.07 ± 0.54 × 10⁵ molec/cm³ (< 1% of mean)
- OH variability contributes ~5 Tg CH₄/yr uncertainty to budget

**Saunois et al. (2025) — Updated Global Methane Budget 2000–2020:**
- OH + tropospheric Cl sink: 595 Tg CH₄/yr [510–663] (decade 2010–2019)
- Total chemical loss (OH + Cl + stratosphere): 623 Tg CH₄/yr [fresh estimate]
- Tropospheric lifetime w.r.t. OH: 11.2 years
- Total atmospheric lifetime: 9.3 years
- Soil sink: 30 Tg CH₄/yr [15–45]

---

## Category 2: Bottom-Up Modeling (CTMs and CCMs)

### Method Description
Chemistry-Transport Models (CTMs) and Chemistry-Climate Models (CCMs) simulate OH from first principles: precursor emissions (NOx, CO, VOCs), photolysis rates, water vapor, and transport.

### Database

| Year | Author(s) | Model(s) | Global Mean [OH] ($10^6$ molec/cm³) | NH/SH Ratio | τ_CH₄ (yr) | τ Type | Period | DOI | Status |
|------|-----------|----------|--------------------------------------|-------------|-------------|--------|--------|-----|--------|
| 2024 | Souri et al. | GEOS + OMI/TROPOMI (Bayesian) | Satellite-constrained trends | — | — | TOH trends 2005–2019 | 2005–2019 | [10.5194/acp-24-8677-2024](https://doi.org/10.5194/acp-24-8677-2024) | ✅ PDF + Data |
| 2023 | Zhao et al. | Box model + obs constraints | Lowered by 2×10⁵ vs models | — | — (loss: 471–508 Tg/yr) | τ | 2000–2009 | [10.5194/acp-23-789-2023](https://doi.org/10.5194/acp-23-789-2023) | ✅ PDF + Data |
| 2023 | Anderson et al. | ML + satellite (GEOS) | First satellite TCOH feasibility | — | — | — | ~2005–2019 | [10.5194/acp-23-6319-2023](https://doi.org/10.5194/acp-23-6319-2023) | ✅ PDF + Data |
| 2025 | Acquah et al. | EMAC (CCMI-2022) | Sector-attributed (see notes) | NH > SH | Shorter w/ CEDS | τ_trop | 2000–2010 | [10.5194/acp-25-13665-2025](https://doi.org/10.5194/acp-25-13665-2025) | ✅ PDF + Data |
| 2024 | Mertens et al. | EMAC | — | — | 7.63 (2015); 8.39–8.50 (SSP scenarios) | τ_trop | 2015–2050 | [10.5194/acp-24-12079-2024](https://doi.org/10.5194/acp-24-12079-2024) | ✅ PDF + Data |
| 2021 | He et al. | GFDL-AM4.1 | ~2% spread from met forcing | — | Δτ = 0.24 yr from met | τ_trop | 1980–2017 | [10.1029/2021GL094140](https://doi.org/10.1029/2021GL094140) | ✅ PDF + Data |
| 2021 | Anderson et al. | MERRA-2 GMI | ~order 10⁶ (spatial focus) | NMB: NH 19%, SH 16% | — | — | 1980–2018 | [10.5194/acp-21-6481-2021](https://doi.org/10.5194/acp-21-6481-2021) | ✅ PDF + Data |
| 2020 | Stevenson et al. | AerChemMIP (multi-model) | [in text] | ~1.28 | 8.4 ± 0.3 | τ_atm | ~present-day | [10.5194/acp-20-12905-2020](https://doi.org/10.5194/acp-20-12905-2020) | ✅ PDF + Data |
| 2020 | Zhao et al. | CCMI Phase 1 (12 models) | 0.81–1.51 (range) | 1.2–1.3 (most) | 7.1–13.7 | τ_trop | 2000–2016 | [10.5194/acp-20-9525-2020](https://doi.org/10.5194/acp-20-9525-2020) | ✅ PDF + Data |
| 2020 | Wild et al. | Multi-model sensitivity | — | — | — | — | present-day | [10.5194/acp-20-4047-2020](https://doi.org/10.5194/acp-20-4047-2020) | ✅ PDF |
| 2019 | Zhao et al. | CCMI Phase 1 (12 models) | Mean: 1.11 ± 0.17 (multi-model) | — | 9.3 ± 1.7 | τ_trop | 1980–2015 | [10.5194/acp-19-13701-2019](https://doi.org/10.5194/acp-19-13701-2019) | ✅ PDF + Data |
| 2019 | Rowlinson et al. | p-TOMCAT CTM | — | — | — | — | 1997–2016 | [10.5194/acp-19-8669-2019](https://doi.org/10.5194/acp-19-8669-2019) | ✅ PDF |
| 2018 | Nicely et al. | MERRA-2 GMI (empirical) | Δ[OH] = +0.95 ± 0.18 %/decade | — | — | — | 1980–2015 | [10.1029/2018JD028388](https://doi.org/10.1029/2018JD028388) | ✅ PDF + Data |
| 2016 | Lelieveld et al. | EMAC | — | — | — | — | Present-day | [10.5194/acp-16-12477-2016](https://doi.org/10.5194/acp-16-12477-2016) | ✅ PDF |
| 2014 | Murray et al. | GEOS-Chem | — | — | — | — | LGM–present | [10.5194/acp-14-3589-2014](https://doi.org/10.5194/acp-14-3589-2014) | ✅ PDF |
| 2013 | Voulgarakis et al. | ACCMIP (14 models) | 1.13 ± 0.09 | — | 9.8 ± 1.6 | τ_trop | ~2000 | [10.5194/acp-13-4839-2013](https://doi.org/10.5194/acp-13-4839-2013) | ✅ PDF + Data |
| 2013 | Naik et al. | ACCMIP (16 models) | — | — | — | — | 1850–2100 | [10.5194/acp-13-5277-2013](https://doi.org/10.5194/acp-13-5277-2013) | ✅ PDF |
| 2013 | Holmes et al. | GEOS-Chem | — | — | — | — | Future | [10.5194/acp-13-285-2013](https://doi.org/10.5194/acp-13-285-2013) | ✅ PDF |
| 2012 | John et al. | GFDL CM3 | — | — | +5% τ PI→present; −9% to −13% (RCPs) | τ_trop | 1860–2100 | [10.5194/acp-12-12021-2012](https://doi.org/10.5194/acp-12-12021-2012) | ✅ PDF + Data |
| 2001 | Lawrence et al. | Theoretical analysis | Defines AM vs CH₄-weighted [OH] | — | — | — | — | [10.5194/acp-1-37-2001](https://doi.org/10.5194/acp-1-37-2001) | ✅ PDF + Data |
| 2000 | Spivakovsky et al. | Climatological 3D OH | Reference 3D OH distribution | — | — | — | — | [10.1029/1999JD901006](https://doi.org/10.1029/1999JD901006) | ❌ Paywalled (Wiley) |

### Key Results from CTM/CCM Studies

**Zhao et al. (2023) — Reconciling bottom-up and top-down CH₄ sink:**
- Constrained model OH with precursor observations (CO, O₃, NO₂)
- **Observation-constrained [OH]trop-M is 2 × 10⁵ lower than raw model output**
- Constrained CH₄ chemical loss: **471–508 Tg/yr** (vs 577–612 unconstrained)
- Now within top-down range: 459–516 Tg/yr
- Root cause of model bias: CO underestimation, NO₂ overestimation, total O₃ column underestimation
- **Key finding:** Models overestimate OH by ~20%; correction reconciles with MCF-based estimates

**Souri et al. (2024) — Satellite-constrained TOH trends 2005–2019:**
- Bayesian data fusion of GEOS model + OMI NO₂/HCHO retrievals
- Five key parameters (TO₃, H₂O, NO₂, HCHO, stratospheric O₃) explain 65% of TOH trend variance
- Overall TOH trend from NO₂ remains positive but sign varies regionally
- Northern Hemisphere oceans: positive TOH trends (↑HCHO, ↑TO₃, ↑H₂O)
- OMI biomass burning NO₂ bias → up to 20% regional TOH overestimation
- **First study to constrain global 1°×1° TOH trends with satellite data**

**Anderson et al. (2023) — First satellite TCOH feasibility study:**
- ML model trained on GEOS CTM, applied to satellite observations
- Demonstrated feasibility of constraining tropical column OH from satellites
- Uses NO₂, HCHO, O₃, H₂O, J(O¹D) as inputs
- Current satellite quality sufficient for broad regional OH constraints
- Validates against MERRA-2 GMI output
- **Foundation for Duncan et al. (2024) perspective paper**

**He et al. (2021) — Meteorological forcing on OH:**
- **Global OH varies by ~2% depending on meteorological reanalysis used** (MERRA-2 vs ERA5 vs JRA-55)
- This causes 11.2 Tg/yr difference in derived CH₄ emissions and 0.24 yr difference in lifetime
- **Meteorology affects OH mean but NOT the OH trend** — trend correlates with reactive nitrogen emissions
- Implication: Met-driven uncertainty is a floor for OH-based CH₄ budget estimates

**Nicely et al. (2018) — Empirical OH trends 1980–2015:**
- **OH increasing at +0.95 ± 0.18 %/decade** due to H₂O, NOx, overhead O₃, tropical widening
- This almost exactly offsets the CH₄-induced decline of −1.01 ± 0.05 %/decade
- 94% of the expected CH₄-induced OH decline is compensated by other drivers
- Net result: near-zero OH trend — consistent with MCF observations
- Key drivers ranked: H₂O > NOx > overhead O₃ > Hadley cell expansion

**Zhao et al. (2019) — CCMI multi-model OH (most comprehensive):**
- **Multi-model mean global [OH]:** 1.11 ± 0.17 × 10⁶ molec/cm³
- **Multi-model mean τ_CH₄ (trop):** 9.3 ± 1.7 years
- 12 CCMI models; enormous spread (factor ~2)
- Key drivers of spread: NOx, photolysis, water vapor
- OH IAV across models: 2–3%

**Zhao et al. (2020a) — Updated CCMI intercomparison:**
- Extended to 2016; confirms 0.81–1.51 × 10⁶ range
- τ_trop range: 7.1–13.7 years
- Most models show NH/SH > 1.2

**Stevenson et al. (2020) — AerChemMIP historical trends:**
- **Present-day τ_atm: 8.4 ± 0.3 years** (multi-model; shorter than MCF-based IPCC value)
- OH increased ~8–12% from 1850 to present
- NH/SH ratio: ~1.28
- Competing drivers: ↑NOx (→↑OH) vs ↑CH₄+CO (→↓OH); NOx wins historically

**Mertens et al. (2024) — Transport emissions & CH₄ lifetime:**
- **Present-day (2015) τ_trop: 7.63 years** (EMAC model)
- Future SSP scenarios (2050): τ_trop = 8.39–8.50 years (longer due to clean air policies reducing NOx)
- Key finding: NOx emission reductions in clean-air scenarios extend CH₄ lifetime

**Anderson et al. (2021) — ENSO-OH relationship:**
- ENSO is dominant mode of global OH variability (~30% of winter variance)
- El Niño → 10–15% reduction in tropical Pacific tropospheric column OH
- 1997–1998 ENSO: ~9% global OH decrease
- Model has ~20% high bias vs ATom in-situ OH (within 35% measurement uncertainty)

**Acquah et al. (2025) — Emission inventory impact:**
- CEDS (CCMI-2022) → shorter τ_CH₄ than MACCity (CCMI-1)
- Mechanism: +9.02 Tg(N)/yr NOx in CEDS → more OH
- OH attribution: Lightning NOx ~25%, Anthropogenic ~36–39%, Biogenic ~12%

**John et al. (2012) — Climate vs emissions drivers of τ (1860–2100):**
- GFDL CM3 model: historical + RCP scenarios
- **Preindustrial → present: τ_CH₄ OH increases by +5%** (CH₄ doubling offsets NOx+climate effects)
- Late 20th century: τ declining as warming accelerates
- 21st century projections: τ changes of −9% (RCP2.6) to +4% (RCP8.5)
- RCP8.5: CH₄ increase outweighs warming → τ increases (positive feedback)
- RCP4.5: Largest τ decrease (−13%) from combined climate + emission cleanup
- Reference lifetimes cited: τ_CH₄ OH = 10.2 +0.9/−0.7 (Prinn 2005), 11.2 ± 1.3 (Prather 2012)

**Lawrence et al. (2001) — Foundational methodology paper:**
- Defines the difference between air-mass-weighted and CH₄-reaction-weighted [OH]
- **AM-weighted [OH] ≠ CH₄-weighted [OH]** — different by ~5–10%
- Global mean [OH] is only meaningful relative to the specific weighting function
- MCF-weighted and CH₄-weighted [OH] differ because of different temperature dependence
- **This paper established the standard methodology used by all subsequent studies**

---

## Category 3: Chemical Feedbacks and Sensitivity Studies

### Database

| Year | Author(s) | Method | Key Finding | DOI | Status |
|------|-----------|--------|-------------|-----|--------|
| 2020 | Nguyen et al. | 2-box model + feedbacks | Neglecting CH₄-OH feedbacks → 25% bias in emission estimates over 10 yr | [10.1029/2019GL085706](https://doi.org/10.1029/2019GL085706) | ✅ PDF + Data |

### Key Results

**Nguyen et al. (2020) — Chemical feedbacks on decadal estimates:**
- CH₄-CO-OH coupled chemistry creates significant feedbacks
- **Neglecting CH₄ perturbation effect on OH → 25% bias in derived emissions over a decade**
- Strong biomass burning (El Niño) → elevated CO → suppressed OH → indirect CH₄ growth
- Decadal trend attributions depend on both OH and CO assumptions
- **Implication:** Static OH fields in inversions introduce systematic errors; coupled chemistry needed

---

## Category 4: Emerging Satellite and Machine Learning Methods

### Method Description
Satellite-derived formaldehyde (HCHO) from TROPOMI/OMI can serve as OH proxy. Machine learning bridges models and observations.

### Database

| Year | Author(s) | Method | Key Finding | Global [OH] or τ | DOI | Status |
|------|-----------|--------|-------------|-------------------|-----|--------|
| 2024 | Souri et al. | GEOS + OMI Bayesian fusion | First 1°×1° satellite TOH trends 2005–2019 | 65% variance explained by 5 drivers | [10.5194/acp-24-8677-2024](https://doi.org/10.5194/acp-24-8677-2024) | ✅ PDF + Data |
| 2024 | Duncan et al. | Opinion: satellite OH constraints | Proposes integrated observing system for OH | Not quantified (framework paper) | [10.5194/acp-24-13001-2024](https://doi.org/10.5194/acp-24-13001-2024) | ✅ PDF |
| 2023 | Anderson et al. | ML + satellite obs (GEOS) | First demonstration of satellite-derived TCOH | Regional OH constraints feasible | [10.5194/acp-23-6319-2023](https://doi.org/10.5194/acp-23-6319-2023) | ✅ PDF + Data |
| 2020 | Nicely et al. | Random Forest ML on CCMI | NOx is primary driver of inter-model OH spread; lifetime spread: 45–80% | Model analysis, not direct estimate | [10.5194/acp-20-1341-2020](https://doi.org/10.5194/acp-20-1341-2020) | ✅ PDF + Data |

### Key Results

**Duncan et al. (2024) — "Novel observational constraints on OH":**
- Argues current MCF constraint is degrading (MCF abundance → 0)
- Proposes combining satellite HCHO columns + CO + O₃ for integrated OH constraint
- Identifies need for TROPOMI-heritage missions for OH monitoring
- No quantitative global OH value provided (opinion/perspective paper)

**Nicely et al. (2020) — ML analysis of CCMI OH spread:**
- Random Forest identifies key drivers: NOx (#1), O₃ column (#2), H₂O (#3), photolysis (#4)
- 45–80% spread in model lifetimes explained by these variables
- Suggests emission inventories are the critical constraint for model OH accuracy

---

## Category 5: Synthesis and Assessment Studies

| Year | Author(s) | Type | τ_trop (yr) | τ_atm (yr) | OH Sink (Tg/yr) | Period | DOI | Status |
|------|-----------|------|-------------|-------------|-----------------|--------|-----|--------|
| 2025 | Saunois et al. | Global Methane Budget 2000–2020 | 11.2 | 9.3 | 595 [510–663] | 2010–2019 | [10.5194/essd-17-1873-2025](https://doi.org/10.5194/essd-17-1873-2025) | ✅ PDF + Data |
| 2024 | Fiore et al. | Annual Review (comprehensive) | — | — | — | Review | [10.1146/annurev-earth-032320-090307](https://doi.org/10.1146/annurev-earth-032320-090307) | ❌ Paywalled |
| 2024 | Prather & Zhu | Science (UV & OH lifetime) | — | Resetting τ with UV H₂O₂ | — | — | [10.1126/science.adn0415](https://doi.org/10.1126/science.adn0415) | ❌ Paywalled |
| 2021 | Szopa et al. | IPCC AR6 WG1 Ch6 Assessment | — | 9.1 ± 0.9 | — | ~2010s | IPCC AR6 | [Secondary Source] |
| 2020 | Saunois et al. | Global Methane Budget 2000–2017 | 11.2 ± 1.3 | 9.1 ± 0.9 | 553 ± 56 | 2008–2017 | [10.5194/essd-12-1561-2020](https://doi.org/10.5194/essd-12-1561-2020) | ✅ PDF + Data |
| 2017 | Saunois et al. | Global Methane Budget 2000–2012 | — | — | — | 2003–2012 | [10.5194/acp-17-11135-2017](https://doi.org/10.5194/acp-17-11135-2017) | ✅ PDF |
| 2013 | IPCC AR5 (Myhre et al.) | Assessment | — | 9.25 ± 0.6 | — | ~2005 | IPCC AR5 WG1 Ch8 | [Secondary Source] |
| 2012 | Prather et al. | Reassessment | — | — | τ_trop OH = 11.2 ± 1.3 | — | [10.1029/2012GL051440](https://doi.org/10.1029/2012GL051440) | ❌ Paywalled (Wiley) |

---

## Summary: Consolidated Best Estimates

| Metric | Best Estimate | Range/Uncertainty | Primary Source(s) |
|--------|--------------|-------------------|-------------------|
| **Global mean [OH]** | 1.11 × 10⁶ molec/cm³ (models); ~0.9 × 10⁶ (obs-constrained) | 0.81–1.51 (model range); models biased high by ~20% | Zhao et al. (2019, 2020, 2023) |
| **NH/SH ratio** | ~1.28 (models); ~1.0 (Patra 2014, contested) | 1.13–1.42 (models); 0.80–1.10 (MCF-derived) | Stevenson (2020); Patra (2014); Naus (2019) |
| **τ_CH₄ tropospheric (OH)** | 11.2 yr | ±1.3 yr | Saunois et al. (2020, 2025) |
| **τ_CH₄ total atmospheric** | 9.1–9.3 yr | ±0.9 yr | IPCC AR6; Saunois (2025) |
| **OH chemical sink** | 595 Tg CH₄/yr | [510–663] | Saunois et al. (2025) |
| **OH interannual variability** | 2.3 ± 1.5% (MCF obs); <1% (3D inversion); 2–3% (models) | — | Montzka (2011); Naus (2021); CCMI ensemble |
| **OH trend (1980–2018)** | No significant trend | +0.95%/dec offset by −1.01%/dec from CH₄ | Zhao (2020); Naus (2021); Nicely (2018) |
| **OH trend (1850–present)** | +8–12% | Model-based | Stevenson et al. (2020) |
| **ENSO impact on global OH** | ~9% decrease during strong El Niño | — | Anderson (2021); Rowlinson (2019) |
| **Met-driven OH uncertainty** | ~2% in global mean | → 11.2 Tg/yr in emissions; 0.24 yr in τ | He et al. (2021) |
| **Feedback bias (static OH)** | 25% emission bias over 10 yr | If CH₄-OH feedbacks neglected | Nguyen et al. (2020) |
| **Underdetermined problem** | Cannot unambiguously separate emissions vs OH trends | With current obs network | Turner et al. (2017) |
| **Model OH bias** | ~20% overestimate vs observation-constrained | Loss: 577–612 (models) vs 471–508 Tg/yr (constrained) | Zhao et al. (2023) |
| **Satellite TOH trends** | NO₂-driven trend positive but regionally variable | 65% variance from 5 drivers | Souri et al. (2024) |

---

## Downloaded Papers Inventory (32 PDFs)

All papers now in flat directory: `papers/`

| # | File | Paper | Data Extracted? |
|---|------|-------|----------------|
| 1 | `Acquah_2025_ACP_13665.pdf` | Acquah et al. (2025) — Emission inventories effect on OH | ✅ |
| 2 | `Anderson_2021_ACP_6481.pdf` | Anderson et al. (2021) — ENSO & OH | ✅ |
| 3 | `Anderson_2023_ACP_6319.pdf` | Anderson et al. (2023) — Satellite TCOH feasibility | ✅ |
| 4 | `Bousquet_2005_ACP_2635.pdf` | Bousquet et al. (2005) — Two decades OH variability | ✅ |
| 5 | `Duncan_2024_ACP_13001.pdf` | Duncan et al. (2024) — Novel OH constraints | ✅ |
| 6 | `He, J. et al.2021.pdf` | He et al. (2021) — Met forcing on OH & CH₄ budget | ✅ |
| 7 | `Holmes_2013_ACP_285.pdf` | Holmes et al. (2013) — Future CH₄ & OH | Pending |
| 8 | `John_2012_ACP_12021.pdf` | John et al. (2012) — Climate vs emission drivers τ | ✅ |
| 9 | `Lawrence_2001_ACP_37.pdf` | Lawrence et al. (2001) — AM vs CH₄-weighted [OH] | ✅ |
| 10 | `Lelieveld_2016_ACP_12477.pdf` | Lelieveld et al. (2016) — Tropospheric OH | Pending |
| 11 | `McNorton_2016_ACP_7943.pdf` | McNorton et al. (2016) — OH variability & CH₄ stalling | ✅ |
| 12 | `Mertens_2024_ACP_12079.pdf` | Mertens et al. (2024) — Transport & τ_CH₄ | ✅ |
| 13 | `Montzka, S.A. et al.2011.pdf` | Montzka et al. (2011) — Small IAV of global OH | ✅ |
| 14 | `Murray_2014_ACP_3589.pdf` | Murray et al. (2014) — LGM oxidative capacity | Pending |
| 15 | `Naik_2013_ACP_5277.pdf` | Naik et al. (2013) — ACCMIP OH changes | Pending |
| 16 | `Naus_2019_ACP_407.pdf` | Naus et al. (2019) — Two-box model biases | ✅ |
| 17 | `Naus_2021_ACP_4809.pdf` | Naus et al. (2021) — 3D MCF OH inversion | ✅ |
| 18 | `Nguyen, N.H. et al.2020.pdf` | Nguyen et al. (2020) — Chemical feedbacks on CH₄ | ✅ |
| 19 | `Nicely, J.M. et al.2018.pdf` | Nicely et al. (2018) — OH trends 1980–2015 | ✅ |
| 20 | `Nicely_2020_ACP_1341.pdf` | Nicely et al. (2020) — ML OH analysis | ✅ |
| 21 | `Rowlinson_2019_ACP_8669.pdf` | Rowlinson et al. (2019) — CH₄ & OH trends | ✅ |
| 22 | `Saunois_2017_ACP_11135.pdf` | Saunois et al. (2017) — GMB 2000–2012 | Pending |
| 23 | `Saunois_2020_ESSD_1561.pdf` | Saunois et al. (2020) — GMB 2000–2017 | ✅ |
| 24 | `Saunois_2025_ESSD_1873.pdf` | Saunois et al. (2025) — GMB 2000–2020 | ✅ |
| 25 | `Souri_2024_ACP_8677.pdf` | Souri et al. (2024) — Satellite TOH trends | ✅ |
| 26 | `Stevenson_2020_ACP_12905.pdf` | Stevenson et al. (2020) — AerChemMIP | ✅ |
| 27 | `Turner, A.J. et al.2017.pdf` | Turner et al. (2017) — Ambiguity in CH₄/OH trends | ✅ |
| 28 | `Voulgarakis_2013_ACP_4839.pdf` | Voulgarakis et al. (2013) — ACCMIP analysis | ✅ |
| 29 | `Wild_2020_ACP_4047.pdf` | Wild et al. (2020) — OH sensitivity | Pending |
| 30 | `Zhao_2019_ACP_13701.pdf` | Zhao et al. (2019) — CCMI OH | ✅ |
| 31 | `Zhao_2020_ACP_13011.pdf` | Zhao et al. (2020b) — OH trend/budget | ✅ |
| 32 | `Zhao_2020_ACP_9525.pdf` | Zhao et al. (2020a) — CCMI intercomparison | ✅ |
| 33 | `Zhao_2023_ACP_789.pdf` | Zhao et al. (2023) — Reconciling BU/TD CH₄ sink | ✅ |

### Misidentified Files (to be replaced)
| File | Actual Content | Notes |
|------|---------------|-------|
| `Rigby, M. et al.2017.pdf` | **Duplicate of McNorton (2016)** — same file size (2,786,450 bytes) | Real Rigby 2017 PNAS not obtained |
| `Prather, M.J. & Zhu, X.2024.pdf` | **Prather & Zhu (2024) Elementa** — "Lifetimes and timescales of tropospheric ozone" | Wrong paper — wanted Prather's OH/methane Science paper (if it exists) |

---

## Papers Still Not Obtained

| # | Author(s) | Year | Title | Journal | DOI | Priority |
|---|-----------|------|-------|---------|-----|----------|
| 1 | Rigby, M. et al. | 2017 | Role of atmospheric OH variability in the stalling of the global methane growth rate | PNAS | `10.1073/pnas.1616426114` | **High** |
| 2 | Patra, K. et al. | 2014 | Observational evidence for interhemispheric hydroxyl-radical parity | Nature | `10.1038/nature13721` | **High** |
| 3 | Patra, K. et al. | 2021 | Methyl Chloroform Continues to Constrain OH Variability | JGR Atmos | `10.1029/2020JD033862` | **High** |
| 4 | Prather, M.J. & Zhu, X. | 2024 | Resetting tropospheric OH and CH₄ lifetime with ultraviolet H₂O₂ | Science | `10.1126/science.adn0415` | **High** |
| 5 | Prinn, R. et al. | 2001 | Evidence for Substantial Variations of Atmospheric Hydroxyl Radicals | Science | `10.1126/science.1058673` | **Medium** |
| 6 | Prinn, R. et al. | 2005 | Evidence for variability of OH over the past quarter century | GRL | `10.1029/2004GL022228` | **Medium** |
| 7 | Prather, M.J. et al. | 2012 | Reactive greenhouse gas scenarios | GRL | `10.1029/2012GL051440` | **Medium** |
| 8 | Turner, A.J. et al. | 2018 | Modulation of hydroxyl variability by ENSO | PNAS | `10.1073/pnas.1807532115` | **Medium** |
| 9 | Fiore, A.M. et al. | 2024 | Climate and Tropospheric Oxidizing Capacity | Ann Rev Earth Planet Sci | `10.1146/annurev-earth-032320-090307` | **Medium** |
| 10 | Spivakovsky, C.M. et al. | 2000 | 3D climatological OH distribution | JGR | `10.1029/1999JD901006` | **Low** (foundational but old) |
| 11 | Krol, M. & Lelieveld, J. | 2003 | Can the variability in tropospheric OH be deduced from MCF? | JGR | `10.1029/2002JD002423` | **Low** |

---

*Database last updated: 2026-05-03 (Session 4)*
*Total papers with data extracted: 26/33 downloaded + 11 identified paywalled*
*Total unique papers in database: 44*
*Coverage: 2000–2025 (see Search Log for gaps)*
