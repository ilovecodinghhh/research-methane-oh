# Search Log — research-methane-OH

## Search Session 1 — 2026-05-03

### APIs Used
1. **Tavily Search** — exhausted after 4 queries (credit limit)
2. **Brave Web Search** — shares Tavily backend, also exhausted
3. **Semantic Scholar API** — 2 queries, rate-limited after
4. **CrossRef API** — 2 queries, successful
5. **Direct URL Fetching** — Copernicus OA journals, Nature (paywall), ESSD
6. **Browser-based extraction** — JavaScript scraping of Copernicus HTML for quantitative data

### Search Queries Executed

#### Query 1 (Tavily): Primary OH + MCF search
- `global tropospheric hydroxyl radical OH abundance methane lifetime methyl chloroform MCF inversion 2018-2025`
- Advanced depth, 15 results requested
- **Result:** Credits exhausted mid-query

#### Query 2 (Tavily): Author-targeted
- `Prinn Montzka Rigby AGAGE methyl chloroform OH concentration global mean interannual variability`
- **Result:** Credits exhausted

#### Query 3 (Tavily): CTM/CCM
- `CCMI GEOS-Chem chemistry transport model global OH concentration methane oxidation bottom-up 2018-2025`
- **Result:** Credits exhausted

#### Query 4 (Tavily): Satellite/ML
- `satellite TROPOMI formaldehyde HCHO machine learning OH radical proxy tropospheric`
- **Result:** Credits exhausted

#### Query 5 (Semantic Scholar): Primary search
- `global tropospheric OH hydroxyl radical methane lifetime methyl chloroform`
- year=2018-2026, 20 results
- **Result:** Found Chua et al. (2023 preprint)

#### Query 6 (Semantic Scholar): CCMI
- `CCMI OH concentration chemistry climate model intercomparison`
- **Result:** Rate-limited

#### Query 7 (CrossRef): 2018-2026 relevance
- `global OH hydroxyl methane lifetime tropospheric`
- filter: 2018–2026
- **Result:** 20 items; found Acquah et al. (2025), Zhao et al. DOIs

#### Query 8 (CrossRef): 2021-2026 MCF/AGAGE
- `methyl chloroform OH concentration AGAGE global trend`
- filter: 2020–2026
- **Result:** Found Naus et al. (EGU abstract), review references to key DOIs

### Papers Accessed (Full Text or Significant Portions)

| Paper | URL | Data Extracted? |
|-------|-----|-----------------|
| Zhao et al. (2020) ACP 20, 9525 | acp.copernicus.org/articles/20/9525/2020/ | ✅ Quantitative OH ranges, lifetime ranges |
| Zhao et al. (2020) ACP 20, 13011 | acp.copernicus.org/articles/20/13011/2020/ | ✅ OH trend/variability, budget impact |
| Stevenson et al. (2020) ACP 20, 12905 | acp.copernicus.org/articles/20/12905/2020/ | ✅ AerChemMIP τ, historical trends |
| Nicely et al. (2020) ACP 20, 1341 | acp.copernicus.org/articles/20/1341/2020/ | ✅ ML drivers of OH inter-model spread |
| Saunois et al. (2020) ESSD 12, 1561 | essd.copernicus.org/articles/12/1561/2020/ | ✅ Global Methane Budget OH sink, τ |
| Anderson et al. (2021) ACP 21, 6481 | acp.copernicus.org/articles/21/6481/2021/ | ✅ ENSO-OH relationship, ATom validation |
| Acquah et al. (2025) ACP 25, 13665 | acp.copernicus.org/articles/25/13665/2025/ | ✅ Emission inventory impact on τ |

### Papers Not Accessible (Paywall or Not Found)

| Paper | Issue |
|-------|-------|
| Rigby et al. (2017) PNAS | Paywall |
| Turner et al. (2017) PNAS | Paywall |
| Montzka et al. (2011, 2018) | Not found in OA; paywall likely |
| Prinn et al. (2018+) | No post-2018 AGAGE-specific OH paper found in OA |

### Known Gaps
1. **2020–2025 MCF-based OH estimates** — No post-2019 OA papers with updated MCF inversions found
2. **COVID-19 NOx anomaly impact on OH** — Referenced but no OA paper with quantitative global OH data
3. **TROPOMI HCHO-OH proxy papers** — Wolfe et al. (2019) referenced but not directly accessed
4. **Patra et al. (2021)** — Not found at expected URL
5. **Search credit limitation** — Tavily credits exhausted early, limiting discovery of newer (2023–2026) papers
