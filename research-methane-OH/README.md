# Research Project: Global Tropospheric OH Abundance & Methane Lifetime

## Objective
Systematic review of literature (2011–2025) on global tropospheric Hydroxyl Radical ($OH$) abundance and Methane Lifetime ($\tau_{CH_4}$) to construct a reliable global time series database.

## Current Status
- **26 unique papers obtained** (27 PDFs; 1 duplicate)
- **20 papers with quantitative data extracted**
- **6 older papers** pending detailed extraction
- **2 misidentified files** (see DATABASE.md)
- **1 paper still not obtained** (Rigby 2017 PNAS)

## Methodological Framework

### Method Categories
1. **Top-Down Proxy (MCF Inversion)** — Using $CH_3CCl_3$ decay to infer $[OH]$ (AGAGE/NOAA networks)
2. **Bottom-Up Modeling (CTM/CCM)** — Chemistry-Transport/Climate Models (GEOS-Chem, EMAC, CCMI ensemble)
3. **Chemical Feedbacks** — CH₄-CO-OH coupled chemistry effects on inversions
4. **Emerging Methods (Satellite/ML)** — TROPOMI/OMI $HCHO$ proxies, machine learning
5. **Synthesis & Assessment** — Global Methane Budgets, IPCC assessments

### Key Findings (Consolidated)
| Metric | Best Estimate | Source(s) |
|--------|--------------|-----------|
| Global mean [OH] | 1.11 ± 0.17 × 10⁶ molec/cm³ | Zhao et al. (2019) |
| OH interannual variability | 2.3 ± 1.5% (MCF obs); <1% (3D) | Montzka (2011); Naus (2021) |
| τ_CH₄ total atmospheric | 9.1–9.3 ± 0.9 yr | IPCC AR6; Saunois (2025) |
| OH trend (1980–2018) | No significant trend | Naus (2021); Nicely (2018) |
| OH chemical sink | 595 Tg CH₄/yr [510–663] | Saunois et al. (2025) |

### Search Strategy
- **Primary sources:** Copernicus OA journals (ACP, ESSD, GMD), AGU journals (JGR, GRL), Science, PNAS
- **Methods:** API search (Tavily, CrossRef, Semantic Scholar), snowball from reference lists, manual additions
- **Date range:** 2011–2025
- **Keywords:** hydroxyl radical, OH abundance, OH trend, methane lifetime, CH4 oxidation, interannual variability, methyl chloroform, MCF inversion, global methane budget

### Data Standards
- All $[OH]$ standardized to $10^6 \text{ molec/cm}^3$
- Weighting method recorded: air-mass weighted vs $CH_4$-reaction weighted ($[OH]_{CH_4}$)
- Rate constant $k_{OH+CH_4} = 2.45 \times 10^{-12} \exp(-1775/T)$ cm³ molec⁻¹ s⁻¹
- Uncertainty ($\pm \sigma$) always extracted
- Distinguish tropospheric (τ_trop) vs total atmospheric (τ_atm) lifetime

## Project Structure
```
research-methane-OH/
├── README.md                  # This file
├── DATABASE.md                # Main OH database (by method category)
├── SEARCH-LOG.md              # Search queries, screening, and download log
├── NOTES.md                   # Analytical notes, debates, and methodological flags
├── papers/                    # All downloaded PDFs (flat directory)
│   ├── [27 PDF files]
│   └── ...
└── references/
    └── key-papers-2020-2025.md  # Detailed per-paper reference notes
```

## Key Authors
- Montzka, S.A. (NOAA — seminal MCF/OH stability paper)
- Naus, S. (TM5 — definitive 3D MCF inversion)
- Turner, A.J. (Harvard — underdetermined problem)
- Nicely, J.M. (NASA — empirical OH trends & ML analysis)
- Zhao, Y. (CCMI — multi-model OH intercomparisons)
- Stevenson, D.S. (AerChemMIP — historical OH trends)
- Saunois, M. (Global Methane Budget series)
- He, J. (GFDL — meteorological forcing on OH)
- Nguyen, N.H. (Caltech — chemical feedback analysis)

## Critical Flags
- ⚠️ **2020–2025 gap:** No observation-constrained global OH data post-2019
- ⚠️ **MCF decay:** Signal-to-noise degrading; future OH estimation needs new methods
- ⚠️ **COVID-19:** 2020 NOx anomaly impact on OH not yet quantified
- ⚠️ **Feedback bias:** Static OH inversions underestimate by ~25% over decade (Nguyen 2020)
- ⚠️ **Underdetermined:** Surface observations alone cannot separate emissions from OH trends (Turner 2017)

---
*Project created: 2026-05-03*
*Last updated: 2026-05-03 (Phase 3 — manual additions integrated)*
*No-Hallucination Policy: All numerical values sourced directly from literature.*
