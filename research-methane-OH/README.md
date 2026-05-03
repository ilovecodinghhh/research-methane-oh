# Research Project: Global Tropospheric OH Abundance & Methane Lifetime

## Objective
Systematic review of Open-Access literature (2018–present) on global tropospheric Hydroxyl Radical ($OH$) abundance and Methane Lifetime ($\tau_{CH_4}$) to construct a reliable global time series database.

## Methodological Framework

### Method Categories
1. **Top-Down Proxy (MCF Inversion)** — Using $CH_3CCl_3$ decay to infer $[OH]$ (AGAGE/NOAA networks)
2. **Bottom-Up Modeling (CTM/CCM)** — Chemistry-Transport/Climate Models (GEOS-Chem, CCMI)
3. **Emerging Methods (Satellite/ML)** — TROPOMI/OMI $HCHO$ proxies, machine learning approaches

### Search Strategy
- **Repositories:** Google Scholar, arXiv (physics.ao-ph), ESSD, Nature Communications, ACP, GMD
- **Date range:** 2018–Present
- **Keywords:** "Hydroxyl radical" AND ("OH abundance" OR "OH trend") AND ("Methane lifetime" OR "CH4 oxidation") AND ("interannual variability") AND ("methyl chloroform" OR "MCF inversion")
- **Secondary:** "Global Methane Budget"

### Data Standards
- All $[OH]$ standardized to $10^6 \text{ molec/cm}^3$
- Weighting method recorded: air-mass weighted vs $CH_4$-reaction weighted ($[OH]_{CH_4}$)
- Rate constant $k_{OH+CH_4}$ captured when stated
- Uncertainty ($\pm \sigma$) always extracted
- Distinguish tropospheric vs total atmospheric lifetime

### Status Labels
- `[Complete]` — Full OA data extracted
- `[Secondary Source]` — Data summarized from another paper
- `[Paywalled - Manual Intervention Required]` — Title, DOI, Abstract only

## Project Structure
```
research-methane-OH/
├── README.md                  # This file
├── DATABASE.md                # Main OH database table
├── SEARCH-LOG.md              # Search queries and screening results
├── NOTES.md                   # Analytical notes and flags
├── data/                      # Extracted data files
├── references/                # Paper summaries and notes
└── scripts/                   # Any processing scripts
```

## Key Authors to Track
- Prinn, R.G. (MCF/AGAGE)
- Montzka, S.A. (NOAA/MCF)
- Rigby, M. (MCF inversions)
- Saunois, M. (Global Methane Budget)

## Critical Flags
- COVID-19 2020 $NO_x$ anomaly impact on $OH$ trends
- $OH$ recycling in pristine tropical forests
- Updates to CEDS emission inventories
- MCF data revisions

---
*Project created: 2026-05-03*
*No-Hallucination Policy: All numerical values sourced directly from literature. No inferred/guessed data.*
