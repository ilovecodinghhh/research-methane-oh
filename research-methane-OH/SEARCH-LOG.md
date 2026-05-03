# Search Log — research-methane-OH

## Search Session 1 — 2026-05-03 (13:00–13:30 UTC)

### APIs Used
1. **Tavily Search** — exhausted after 4 queries (credit limit)
2. **Brave Web Search** — shares Tavily backend, also exhausted
3. **Semantic Scholar API** — 2 queries, rate-limited
4. **CrossRef API** — 2 queries, successful
5. **Direct URL Fetching** — Copernicus OA journals
6. **Browser-based extraction** — JavaScript on Copernicus HTML

### Papers Found: 7 (Zhao 2020 ×2, Stevenson 2020, Nicely 2020, Saunois 2020, Anderson 2021, Acquah 2025)

---

## Search Session 2 — 2026-05-03 (13:30–14:40 UTC)

### Strategy: Snowball + Targeted Download

#### Snowball Sources
1. Zhao et al. (2020b) ACP 20, 13011 — reference list
2. Stevenson et al. (2020) ACP 20, 12905 — reference list
3. Acquah et al. (2025) ACP 25, 13665 — reference list (most recent → yielded 2024 papers)

#### Snowball Findings (new papers identified)
From Zhao (2020b) references:
- McNorton et al. (2016) ACP — OH variability & CH₄ stalling
- Lelieveld et al. (2016) ACP — Global tropospheric OH
- Rowlinson et al. (2019) ACP — ENSO, CH₄, and OH
- Naus et al. (2019) ACP — Two-box model biases

From Stevenson (2020) references:
- Wild et al. (2020) ACP — OH sensitivity
- Voulgarakis et al. (2013) — ACCMIP
- Naik et al. (2013) — ACCMIP OH changes

From Acquah (2025) references:
- **Duncan et al. (2024) ACP** — Novel OH constraints (satellite)
- **Mertens et al. (2024) ACP** — Transport emissions & τ_CH₄
- Prather & Zhu (2024) — Science (paywalled)

#### CrossRef API Searches (Session 2)
1. `Patra methyl chloroform OH 2021` → Found Naus et al. (2021) ACP 21, 4809
2. `methane OH hydroxyl lifetime trend global budget` (2022–2025) → Found Saunois et al. (2025) ESSD 17, 1873; Chua et al. (2025 preprint)

#### Direct Browser Extraction (quantitative data)
- Naus et al. (2021) — OH IAV 0.6–0.8%, no trend
- Zhao et al. (2019) — Mean [OH] = 1.11 ± 0.17; τ = 9.3 ± 1.7
- Saunois et al. (2025) — OH sink = 595 Tg/yr [510–663]; τ_atm = 9.3
- Mertens et al. (2024) — τ_trop(2015) = 7.63; τ_trop(2050) = 8.39–8.50
- Rowlinson et al. (2019) — ENSO/biomass burning OH impact

#### PDF Downloads (22 total)
- **Successful OA downloads:** 22 papers from Copernicus (ACP, ESSD)
- **Failed (Wiley Cloudflare block):** Nicely 2018 JGR, Nguyen 2020 GRL, He 2021 GRL
- **False positives (removed):** Droste et al. (PFCs); Patra 2021 (wrong URL)

---

## Coverage Assessment

### By Period
| Period | Papers Found | Status |
|--------|-------------|--------|
| 2010–2014 | 4 (Naik, Voulgarakis, Holmes, Murray) | Downloaded; data extraction pending |
| 2015–2016 | 2 (McNorton, Lelieveld) | Downloaded |
| 2017–2018 | 0 OA papers with global OH data | Gap (Rigby & Turner are paywalled PNAS) |
| 2019 | 3 (Zhao, Naus, Rowlinson) | Complete extraction |
| 2020 | 7 (Zhao ×2, Stevenson, Nicely, Saunois, Wild, Anderson [pub 2021]) | Complete |
| 2021 | 2 (Naus, Anderson) | Complete extraction |
| 2022–2023 | 0 OA papers found with quantitative global OH | Gap |
| 2024 | 2 (Duncan, Mertens) | Complete |
| 2025 | 2 (Acquah, Saunois) | Complete |

### By Method
| Method | Papers | Data Quality |
|--------|--------|-------------|
| MCF / Top-down | 3 downloaded + 3 paywalled | Good — Naus (2021) is definitive |
| CTM / CCM | 14 downloaded | Excellent — multi-model ensembles |
| Satellite / ML | 2 downloaded | Emerging — no quantitative global estimate yet |
| Synthesis | 3 downloaded | Excellent — Saunois 2025 is current reference |

### Remaining Gaps
1. **2022–2023:** No OA papers found with fresh global OH/τ quantitative data
2. **COVID-19 OH impact:** No OA paper found quantifying 2020 global OH anomaly
3. **Paywalled papers:** 6 critical papers need manual access (see below)
4. **Data extraction pending:** 6 papers downloaded but not yet extracted (older CTM studies)

---

## Papers Not Downloaded — Requires Manual Intervention

### Paywalled (no OA version found)

| # | Author(s) | Year | Title | Journal | DOI | Reason | Priority |
|---|-----------|------|-------|---------|-----|--------|----------|
| 1 | Rigby, M. et al. | 2017 | Role of OH variability in the stalling of the global atmospheric CH₄ growth rate from 1999 to 2006 | PNAS | `10.1073/pnas.1616426114` | PNAS paywall | **High** — foundational MCF study; large OH IAV claim |
| 2 | Turner, A.J. et al. | 2017 | Ambiguity in the causes for decadal trends in atmospheric methane | PNAS | `10.1073/pnas.1616020114` | PNAS paywall | **High** — counter-argument to Rigby; independent OH IAV estimate |
| 3 | Montzka, S.A. et al. | 2011 | Small interannual variability of global atmospheric hydroxyl | Science | `10.1126/science.1197817` | Science paywall | **High** — seminal MCF constraint paper; "small IAV" conclusion |
| 4 | Prather, M.J. & Zhu, X. | 2024 | [OH and methane lifetime changes] | Science | — (DOI not confirmed) | Science paywall | **High** — most recent high-impact OH study |
| 5 | Nicely, J.M. et al. | 2018 | Changes in the tropical photochemical environment from 2003 to 2013 | JGR Atmospheres | `10.1029/2018JD028388` | Wiley paywall | **Medium** — quantitative global OH changes from satellite-constrained CTM |
| 6 | He, J. et al. | 2021 | Methane short-lived climate forcer role: OH response to meteorological forcing | GRL | `10.1029/2021GL094140` | Wiley paywall | **Medium** — OH response to met variability; potential COVID insights |

### Download Blocked (Cloudflare / bot protection)

| # | Author(s) | Year | Title | Journal | DOI | Blocker | Notes |
|---|-----------|------|-------|---------|-----|---------|-------|
| 7 | Nicely, J.M. et al. | 2018 | (same as #5 above) | JGR Atmospheres | `10.1029/2018JD028388` | Wiley Cloudflare | Returned 5.5K HTML instead of PDF |
| 8 | Nguyen, N.H. et al. | 2020 | Chemical feedbacks on the future CH₄ lifetime | GRL | `10.1029/2019GL085706` | Wiley Cloudflare | Returned HTML block page |
| 9 | He, J. et al. | 2021 | (same as #6 above) | GRL | `10.1029/2021GL094140` | Wiley Cloudflare | Returned HTML block page |

**Note:** Items 7–9 overlap with the paywalled list. Wiley/AGU journals (JGR, GRL) block automated downloads via Cloudflare even for OA articles. Manual browser download may succeed if the paper is actually OA.

### False Positives (wrong paper at URL)

| # | Attempted Target | Actual Paper Found | URL Tried | Action Taken |
|---|-----------------|-------------------|-----------|-------------|
| 10 | Patra et al. (2021) TransCom MCF | HTML error page (79K) | `acp.copernicus.org/articles/21/6024/2021/` | Deleted |
| 11 | Naus et al. (2020) "OH variability" | Droste et al. (2020) — PFC trends | `acp.copernicus.org/articles/20/4787/2020/` | Deleted |

### Summary
- **Total papers identified:** 28
- **Successfully downloaded:** 22 (all Copernicus OA journals)
- **Not downloadable:** 6 (paywall/Cloudflare)
- **Download success rate:** 79%
- **Blocker pattern:** All failed downloads are Wiley (AGU) or AAAS (Science/PNAS) journals
