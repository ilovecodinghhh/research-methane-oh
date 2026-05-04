# Research Project: Global Tropospheric OH Abundance & Methane Lifetime

## Objective
Systematic review of literature (2011–2025) on global tropospheric Hydroxyl Radical ($OH$) abundance and Methane Lifetime ($\tau_{CH_4}$) to construct a reliable global time series database.

## Current Status
- **33 unique papers downloaded** (33 PDFs in `papers/`)
- **26 papers with quantitative data extracted**
- **7 older papers** pending detailed extraction
- **11 paywalled papers** identified but not obtained (see DATABASE.md)
- **2 misidentified files** (see DATABASE.md)
- Coverage: **2001–2025** (2022–2023 gap filled in Session 4)

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
| Global mean [OH] | 1.11 ± 0.17 × 10⁶ (models); ~0.9 × 10⁶ (obs-constrained) | Zhao et al. (2019, 2023) |
| OH interannual variability | 2.3 ± 1.5% (MCF obs); <1% (3D) | Montzka (2011); Naus (2021) |
| τ_CH₄ total atmospheric | 9.1–9.3 ± 0.9 yr | IPCC AR6; Saunois (2025) |
| OH trend (1980–2018) | No significant trend | Naus (2021); Nicely (2018) |
| OH chemical sink | 471–508 Tg/yr (constrained); 595 (raw models) | Zhao (2023); Saunois (2025) |
| Model OH bias | ~20% overestimate | Zhao et al. (2023) |

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
- Zhao, Y. (CCMI — multi-model OH intercomparisons; reconciliation)
- Stevenson, D.S. (AerChemMIP — historical OH trends)
- Saunois, M. (Global Methane Budget series)
- He, J. (GFDL — meteorological forcing on OH)
- Nguyen, N.H. (Caltech — chemical feedback analysis)
- Souri, A.H. (NASA — satellite TOH trends)
- Anderson, D.C. (NASA — satellite TCOH; ENSO/OH)
- Bousquet, P. (LSCE — early MCF inversion)
- Prinn, R. (MIT/AGAGE — foundational MCF measurements)
- Patra, K. (JAMSTEC — NH/SH parity; multi-model MCF)
- Lawrence, M.G. (MPI — weighting methodology)
- John, J.G. (GFDL — climate vs emission drivers)

## Critical Flags
- ⚠️ **Model bias:** CTMs overestimate global OH by ~20% vs observation-constrained (Zhao 2023)
- ⚠️ **2020–2025 sparse:** No observation-constrained global OH data post-2019
- ⚠️ **MCF decay:** Signal-to-noise degrading; future OH estimation needs satellites
- ⚠️ **COVID-19:** 2020 NOx anomaly impact on OH not yet quantified
- ⚠️ **Feedback bias:** Static OH inversions underestimate by ~25% over decade (Nguyen 2020)
- ⚠️ **Underdetermined:** Surface observations alone cannot separate emissions from OH trends (Turner 2017)
- ⚠️ **NH/SH ratio:** Contested — models say 1.2–1.3, Patra (2014) says ~1.0

---
*Project created: 2026-05-03*
*Last updated: 2026-05-03 (Phase 4 — deeper search 2002–2026; 2022–2023 gap filled)*
*No-Hallucination Policy: All numerical values sourced directly from literature.*

## MinerU PDF Processing

All 45 PDFs were processed through [MinerU](https://mineru.net) cloud API for high-quality markdown extraction.

### Results
- **39/45 PDFs** successfully converted to markdown → `papers_md/`
- **6 PDFs** failed MinerU cloud parsing (server-side errors, retried with OCR mode):
  - Anderson_2021_ACP_6481.pdf
  - Lelieveld_2016_ACP_12477.pdf
  - Mertens_2024_ACP_12079.pdf
  - Voulgarakis_2013_ACP_4839.pdf
  - Zhao_2019_ACP_13701.pdf
  - Zhao_2023_ACP_789.pdf

### Processing Script
See `scripts/mineru_process.py` for the batch processing pipeline.

*MinerU processing completed: 2026-05-04*
