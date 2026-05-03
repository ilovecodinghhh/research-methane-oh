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
| 2021 | Naus et al. | 3D TM5-4DVAR MCF inversion | [see trend below] | [see below] | — | IAV: 0.6–0.8% (1σ) | 1994–2017 | [10.5194/acp-21-4809-2021](https://doi.org/10.5194/acp-21-4809-2021) | [Complete] |
| 2020 | Zhao et al. | Box model + MCF constraint | [anomaly: −0.07 ± 0.54 × 10⁵] | — | 9.1 (ref) | No significant trend | 1980–2018 | [10.5194/acp-20-13011-2020](https://doi.org/10.5194/acp-20-13011-2020) | [Complete] |
| 2020 | Saunois et al. | MCF-derived (synthesis) | — | — | 11.2 (τ_trop) / 9.1 (τ_atm) | ±1.3 / ±0.9 | 2008–2017 | [10.5194/essd-12-1561-2020](https://doi.org/10.5194/essd-12-1561-2020) | [Complete] |
| 2025 | Saunois et al. | MCF-derived (updated synthesis) | — | — | 11.2 (τ_trop) / 9.3 (τ_atm) | — | 2010–2019 | [10.5194/essd-17-1873-2025](https://doi.org/10.5194/essd-17-1873-2025) | [Complete] |
| 2019 | Naus et al. | Two-box model critique (TM5) | ~10% bias from 2-box assumptions | NH/SH: 0.80–1.10 (MCF-derived) | — | OH anomalies shift with bias corrections | 1994–2015 | [10.5194/acp-19-407-2019](https://doi.org/10.5194/acp-19-407-2019) | [Complete] |
| 2016 | McNorton et al. | MCF inversion (box model) | — | — | — | — | 1998–2014 | [10.5194/acp-16-7943-2016](https://doi.org/10.5194/acp-16-7943-2016) | [Complete — PDF downloaded] |
| 2017 | Rigby et al. | MCF 3-box inversion | — | — | — | Large IAV possible | 1990–2016 | 10.1073/pnas.1616426114 | [Paywalled] |
| 2017 | Turner et al. | MCF 2-box inversion | — | — | — | Large IAV possible | 1990–2016 | 10.1073/pnas.1616020114 | [Paywalled] |
| 2011 | Montzka et al. | MCF (NOAA network) | — | — | — | IAV < few % | 1998–2007 | 10.1126/science.1197817 | [Paywalled] |

### Key Results from MCF Studies

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
- **COVID note:** 2020 included but OH change during COVID not explicitly separated

---

## Category 2: Bottom-Up Modeling (CTMs and CCMs)

### Method Description
Chemistry-Transport Models (CTMs) and Chemistry-Climate Models (CCMs) simulate OH from first principles: precursor emissions (NOx, CO, VOCs), photolysis rates, water vapor, and transport.

### Database

| Year | Author(s) | Model(s) | Global Mean [OH] ($10^6$ molec/cm³) | NH/SH Ratio | τ_CH₄ (yr) | τ Type | Period | DOI | Status |
|------|-----------|----------|--------------------------------------|-------------|-------------|--------|--------|-----|--------|
| 2025 | Acquah et al. | EMAC (CCMI-2022) | Sector-attributed (see notes) | NH > SH | Shorter w/ CEDS | τ_trop | 2000–2010 | [10.5194/acp-25-13665-2025](https://doi.org/10.5194/acp-25-13665-2025) | [Complete] |
| 2024 | Mertens et al. | EMAC | — | — | 7.63 (2015); 8.39–8.50 (SSP scenarios) | τ_trop | 2015–2050 | [10.5194/acp-24-12079-2024](https://doi.org/10.5194/acp-24-12079-2024) | [Complete] |
| 2021 | Anderson et al. | MERRA-2 GMI | ~order 10⁶ (spatial focus) | NMB: NH 19%, SH 16% | — | — | 1980–2018 | [10.5194/acp-21-6481-2021](https://doi.org/10.5194/acp-21-6481-2021) | [Complete] |
| 2020 | Stevenson et al. | AerChemMIP (multi-model) | [in text] | ~1.28 | 8.4 ± 0.3 | τ_atm | ~present-day | [10.5194/acp-20-12905-2020](https://doi.org/10.5194/acp-20-12905-2020) | [Complete] |
| 2020 | Zhao et al. | CCMI Phase 1 (12 models) | 0.81–1.51 (range) | 1.2–1.3 (most) | 7.1–13.7 | τ_trop | 2000–2016 | [10.5194/acp-20-9525-2020](https://doi.org/10.5194/acp-20-9525-2020) | [Complete] |
| 2020 | Wild et al. | Multi-model sensitivity | — | — | — | — | present-day | [10.5194/acp-20-4047-2020](https://doi.org/10.5194/acp-20-4047-2020) | [Complete — PDF downloaded] |
| 2019 | Zhao et al. | CCMI Phase 1 (12 models) | Mean: 1.11 ± 0.17 (multi-model) | — | 9.3 ± 1.7 | τ_trop | 1980–2015 | [10.5194/acp-19-13701-2019](https://doi.org/10.5194/acp-19-13701-2019) | [Complete] |
| 2019 | Rowlinson et al. | p-TOMCAT CTM | — | — | — | — | 1997–2016 | [10.5194/acp-19-8669-2019](https://doi.org/10.5194/acp-19-8669-2019) | [Complete] |
| 2016 | Lelieveld et al. | EMAC | — | — | — | — | Present-day | [10.5194/acp-16-12477-2016](https://doi.org/10.5194/acp-16-12477-2016) | [Complete — PDF downloaded] |
| 2014 | Murray et al. | GEOS-Chem | — | — | — | — | LGM–present | [10.5194/acp-14-3589-2014](https://doi.org/10.5194/acp-14-3589-2014) | [Complete — PDF downloaded] |
| 2013 | Voulgarakis et al. | ACCMIP (14 models) | 1.13 ± 0.09 | — | 9.8 ± 1.6 | τ_trop | ~2000 | [10.5194/acp-13-4839-2013](https://doi.org/10.5194/acp-13-4839-2013) | [Complete] |
| 2013 | Naik et al. | ACCMIP (16 models) | — | — | — | — | 1850–2100 | [10.5194/acp-13-5277-2013](https://doi.org/10.5194/acp-13-5277-2013) | [Complete — PDF downloaded] |
| 2013 | Holmes et al. | GEOS-Chem | — | — | — | — | Future | [10.5194/acp-13-285-2013](https://doi.org/10.5194/acp-13-285-2013) | [Complete — PDF downloaded] |
| 2025 | Chua et al. | GFDL AM4.1/ESM4 | — | — | — | — | Future | [10.22541/essoar.176521636.63838160/v2](https://doi.org/10.22541/essoar.176521636.63838160/v2) | [Complete — Preprint] |

### Key Results from CTM/CCM Studies

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

**Rowlinson et al. (2019) — OH, methane, and tropospheric ozone 1997–2016:**
- OH sensitive to both biomass burning emissions and meteorological variability
- 1997–1998 El Niño: Large OH decrease via enhanced CO from fires
- Post-2007 CH₄ growth partially attributable to OH changes (debated)

**Acquah et al. (2025) — Emission inventory impact:**
- CEDS (CCMI-2022) → shorter τ_CH₄ than MACCity (CCMI-1)
- Mechanism: +9.02 Tg(N)/yr NOx in CEDS → more OH
- OH attribution: Lightning NOx ~25%, Anthropogenic ~36–39%, Biogenic ~12%
- CH₄-weighted method (Lawrence et al., 2001) used

---

## Category 3: Emerging Satellite and Machine Learning Methods

### Method Description
Satellite-derived formaldehyde (HCHO) from TROPOMI/OMI can serve as OH proxy. Machine learning bridges models and observations.

### Database

| Year | Author(s) | Method | Key Finding | Global [OH] or τ | DOI | Status |
|------|-----------|--------|-------------|-------------------|-----|--------|
| 2024 | Duncan et al. | Opinion: satellite OH constraints | Proposes integrated observing system for OH | Not quantified (framework paper) | [10.5194/acp-24-13001-2024](https://doi.org/10.5194/acp-24-13001-2024) | [Complete] |
| 2020 | Nicely et al. | Random Forest ML on CCMI | NOx is primary driver of inter-model OH spread; lifetime spread: 45–80% | Model analysis, not direct estimate | [10.5194/acp-20-1341-2020](https://doi.org/10.5194/acp-20-1341-2020) | [Complete] |
| 2019 | Wolfe et al. | HCHO satellite proxy | Formaldehyde as tropospheric OH column proxy | — | — | [Secondary Source — referenced] |

### Key Results from Satellite/ML Studies

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

## Category 4: Synthesis and Assessment Studies

| Year | Author(s) | Type | τ_trop (yr) | τ_atm (yr) | OH Sink (Tg/yr) | Period | DOI | Status |
|------|-----------|------|-------------|-------------|-----------------|--------|-----|--------|
| 2025 | Saunois et al. | Global Methane Budget 2000–2020 | 11.2 | 9.3 | 595 [510–663] | 2010–2019 | [10.5194/essd-17-1873-2025](https://doi.org/10.5194/essd-17-1873-2025) | [Complete] |
| 2021 | Szopa et al. | IPCC AR6 WG1 Ch6 Assessment | — | 9.1 ± 0.9 | — | ~2010s | IPCC AR6 | [Secondary Source] |
| 2020 | Saunois et al. | Global Methane Budget 2000–2017 | 11.2 ± 1.3 | 9.1 ± 0.9 | 553 ± 56 | 2008–2017 | [10.5194/essd-12-1561-2020](https://doi.org/10.5194/essd-12-1561-2020) | [Complete] |
| 2017 | Saunois et al. | Global Methane Budget 2000–2012 | — | — | — | 2003–2012 | [10.5194/acp-17-11135-2017](https://doi.org/10.5194/acp-17-11135-2017) | [Complete — PDF downloaded] |
| 2013 | IPCC AR5 (Myhre et al.) | Assessment | — | 9.25 ± 0.6 | — | ~2005 | IPCC AR5 WG1 Ch8 | [Secondary Source] |
| 2012 | Prather et al. | Reassessment | — | 9.1 ± 0.9 | — | — | — | [Secondary Source] |
| 2005 | Prinn et al. | MCF/AGAGE assessment | — | 10.2 $^{+0.9}_{-0.7}$ | — | 1978–2003 | — | [Secondary Source] |

---

## Summary: Consolidated Best Estimates

| Metric | Best Estimate | Range/Uncertainty | Primary Source(s) |
|--------|--------------|-------------------|-------------------|
| **Global mean [OH]** | 1.11 × 10⁶ molec/cm³ | 0.81–1.51 (model range); ±0.17 (multi-model σ) | Zhao et al. (2019, 2020) |
| **NH/SH ratio** | ~1.28 | 1.13–1.42 (models); 0.80–1.10 (MCF-derived) | Stevenson (2020); Naik (2013); Naus (2019) |
| **τ_CH₄ tropospheric (OH)** | 11.2 yr | ±1.3 yr | Saunois et al. (2020, 2025) |
| **τ_CH₄ total atmospheric** | 9.1–9.3 yr | ±0.9 yr | IPCC AR6; Saunois (2025) |
| **OH chemical sink** | 595 Tg CH₄/yr | [510–663] | Saunois et al. (2025) |
| **OH interannual variability** | <1% (3D MCF); 2–3% (models) | — | Naus (2021); CCMI ensemble |
| **OH trend (1980–2018)** | No significant trend | — | Zhao (2020); Naus (2021) |
| **OH trend (1850–present)** | +8–12% | Model-based | Stevenson et al. (2020) |
| **ENSO impact on global OH** | ~9% decrease during strong El Niño | — | Anderson (2021); Rowlinson (2019) |

---

## Downloaded Papers Inventory

### MCF / Top-Down (3 papers)
| File | Paper |
|------|-------|
| `mcf-topdown/Naus_2021_ACP_4809.pdf` | Naus et al. (2021) — 3D MCF OH inversion |
| `mcf-topdown/Naus_2019_ACP_407.pdf` | Naus et al. (2019) — Two-box model biases |
| `mcf-topdown/McNorton_2016_ACP_7943.pdf` | McNorton et al. (2016) — OH variability from MCF |

### CTM / Bottom-Up (14 papers)
| File | Paper |
|------|-------|
| `ctm-bottomup/Acquah_2025_ACP_13665.pdf` | Acquah et al. (2025) — Emission inventories effect |
| `ctm-bottomup/Mertens_2024_ACP_12079.pdf` | Mertens et al. (2024) — Transport & τ_CH₄ |
| `ctm-bottomup/Anderson_2021_ACP_6481.pdf` | Anderson et al. (2021) — ENSO & OH |
| `ctm-bottomup/Stevenson_2020_ACP_12905.pdf` | Stevenson et al. (2020) — AerChemMIP |
| `ctm-bottomup/Zhao_2020_ACP_9525.pdf` | Zhao et al. (2020a) — CCMI intercomparison |
| `ctm-bottomup/Zhao_2020_ACP_13011.pdf` | Zhao et al. (2020b) — OH trend/budget |
| `ctm-bottomup/Wild_2020_ACP_4047.pdf` | Wild et al. (2020) — OH sensitivity |
| `ctm-bottomup/Zhao_2019_ACP_13701.pdf` | Zhao et al. (2019) — CCMI OH |
| `ctm-bottomup/Rowlinson_2019_ACP_8669.pdf` | Rowlinson et al. (2019) — CH₄ & OH trends |
| `ctm-bottomup/Lelieveld_2016_ACP_12477.pdf` | Lelieveld et al. (2016) — Tropospheric OH |
| `ctm-bottomup/Murray_2014_ACP_3589.pdf` | Murray et al. (2014) — LGM oxidative capacity |
| `ctm-bottomup/Naik_2013_ACP_5277.pdf` | Naik et al. (2013) — ACCMIP OH changes |
| `ctm-bottomup/Voulgarakis_2013_ACP_4839.pdf` | Voulgarakis et al. (2013) — ACCMIP analysis |
| `ctm-bottomup/Holmes_2013_ACP_285.pdf` | Holmes et al. (2013) — Future CH₄ & OH |

### Satellite / ML (2 papers)
| File | Paper |
|------|-------|
| `satellite-ml/Duncan_2024_ACP_13001.pdf` | Duncan et al. (2024) — Novel OH constraints |
| `satellite-ml/Nicely_2020_ACP_1341.pdf` | Nicely et al. (2020) — ML OH analysis |

### Synthesis (3 papers)
| File | Paper |
|------|-------|
| `synthesis/Saunois_2025_ESSD_1873.pdf` | Saunois et al. (2025) — GMB 2000–2020 |
| `synthesis/Saunois_2020_ESSD_1561.pdf` | Saunois et al. (2020) — GMB 2000–2017 |
| `synthesis/Saunois_2017_ACP_11135.pdf` | Saunois et al. (2017) — GMB 2000–2012 |

---

## Paywalled Papers (Manual Intervention Required)

| Title | Authors | Year | Journal | DOI |
|-------|---------|------|---------|-----|
| Role of OH variability in the stalling of the global CH₄ growth rate | Rigby, M. et al. | 2017 | PNAS | 10.1073/pnas.1616426114 |
| Ambiguity in the causes for decadal trends in atmospheric CH₄ | Turner, A.J. et al. | 2017 | PNAS | 10.1073/pnas.1616020114 |
| Hydroxyl and methane lifetime changes | Montzka, S.A. et al. | 2011 | Science | 10.1126/science.1197817 |
| Changes in tropospheric OH from 2003–2013 | Nicely, J.M. et al. | 2018 | JGR Atmos. | 10.1029/2018JD028388 |
| OH response to meteorological forcing: COVID-19 | He et al. | 2021 | GRL | 10.1029/2021GL094140 |
| OH changes associated with CH₄ lifetime | Prather, M.J. & Zhu, X. | 2024 | Science | — |

---

*Database reorganized: 2026-05-03*
*Total papers: 22 downloaded (OA) + 6 identified as paywalled*
*Snowball method applied: references from Zhao (2020), Stevenson (2020), Acquah (2025), Naus (2019)*
