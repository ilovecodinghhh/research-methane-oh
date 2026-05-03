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

#### PDF Downloads (22 automated)
- **Successful OA downloads:** 22 papers from Copernicus (ACP, ESSD)
- **Failed (Wiley Cloudflare block):** Nicely 2018 JGR, Nguyen 2020 GRL, He 2021 GRL
- **False positives (removed):** Droste et al. (PFCs); Patra 2021 (wrong URL)

---

## Session 3 — 2026-05-03 (15:00–17:00 UTC)

### Manual additions by user
User manually downloaded and added 5 previously-paywalled papers + 2 others:

**Correct papers obtained (5):**
| Paper | Journal | Data Extracted |
|-------|---------|---------------|
| Turner, A.J. et al. (2017) | PNAS | ✅ τ=9.2±0.2, 7% OH decrease (most likely), underdetermined |
| He, J. et al. (2021) | GRL | ✅ 2% global OH spread, 11.2 Tg/yr emission difference |
| Nicely, J.M. et al. (2018) | JGR Atmos | ✅ +0.95±0.18 %/dec OH trend, 94% offset |
| Nguyen, N.H. et al. (2020) | GRL | ✅ 25% emission bias from neglected feedbacks |
| Montzka, S.A. et al. (2011) | Science | ✅ OH IAV = 2.3±1.5% (1998–2007) |

**Misidentified papers (2):**
| File | Expected | Actual Content |
|------|----------|---------------|
| `Rigby, M. et al.2017.pdf` | Rigby (2017) PNAS — MCF 3-box | **McNorton (2016) duplicate** — identical 2,786,450 bytes |
| `Prather, M.J. & Zhu, X.2024.pdf` | Prather OH/CH₄ paper | **Prather & Zhu (2024) Elementa** — tropospheric ozone lifetimes |

### User also reorganized directory structure
- Flattened `papers/` — removed subdirectories (ctm-bottomup/, mcf-topdown/, satellite-ml/, synthesis/)
- All 27 PDFs now in single `papers/` directory

---

## Coverage Assessment (Updated)

### By Period
| Period | Papers Found | Status |
|--------|-------------|--------|
| 2010–2014 | 4 (Montzka 2011, Naik, Voulgarakis, Holmes, Murray) | **Montzka extracted**; others pending |
| 2015–2016 | 2 (McNorton, Lelieveld) | Downloaded |
| 2017–2018 | 2 (Turner 2017, Nicely 2018) | ✅ **Both extracted** (was gap) |
| 2019 | 3 (Zhao, Naus, Rowlinson) | Complete |
| 2020 | 8 (Zhao ×2, Stevenson, Nicely ML, Saunois, Wild, Nguyen, Anderson [pub 2021]) | ✅ **Nguyen added** |
| 2021 | 3 (Naus, Anderson, He) | ✅ **He added** |
| 2022–2023 | 0 | Gap remains |
| 2024 | 2 (Duncan, Mertens) | Complete |
| 2025 | 2 (Acquah, Saunois) | Complete |

### By Method
| Method | Papers | Data Quality |
|--------|--------|-------------|
| MCF / Top-down | 5 (Montzka, Naus ×2, Turner, McNorton) + 1 still missing (Rigby) | **Excellent** — seminal + definitive papers |
| CTM / CCM | 16 (incl. He, Nicely 2018) | **Excellent** |
| Feedbacks | 1 (Nguyen) | Good — key methodological paper |
| Satellite / ML | 2 | Emerging |
| Synthesis | 3 | **Excellent** — Saunois 2025 is current |

### Papers Still Not Obtained
| # | Paper | Priority | Notes |
|---|-------|----------|-------|
| 1 | Rigby, M. et al. (2017) PNAS | **High** | File provided is McNorton duplicate |
| 2 | Prather (2024) OH/CH₄ study | **Medium** | Identity uncertain; file provided is ozone paper |

### Final Statistics (Session 3)
- **Total unique papers obtained:** 26
- **Data extracted:** 20 of 26
- **Data extraction pending:** 6 (older CTM studies: Wild, Lelieveld, Murray, Naik, Holmes, Saunois 2017)
- **Misidentified files:** 2 (Rigby duplicate, Prather wrong paper)

---

## Search Session 4 — 2026-05-03 (15:30–17:25 UTC)

### Objective: Deeper search across full 2002–2026 range

### APIs Used
1. **CrossRef API** — 12 queries (with 3–5s rate limiting between calls)
2. **Brave Web Search** — 2 queries
3. **Browser (Copernicus)** — 3 pages extracted (Zhao 2023, Souri 2024)
4. **pdftotext** — 6 papers text-extracted

### New Papers Found & Downloaded (6 OA)

| Paper | Method | Key Finding | DOI |
|-------|--------|-------------|-----|
| **Zhao et al. (2023) ACP** | Obs-constrained OH | Models overestimate OH by ~20%; constrained loss = 471–508 Tg/yr | 10.5194/acp-23-789-2023 |
| **Anderson et al. (2023) ACP** | ML + satellite TCOH | First feasibility for satellite-derived column OH | 10.5194/acp-23-6319-2023 |
| **Souri et al. (2024) ACP** | GEOS + OMI fusion | 1°×1° TOH trends 2005–2019; 65% variance from 5 drivers | 10.5194/acp-24-8677-2024 |
| **Bousquet et al. (2005) ACP** | MCF inversion | IAV = 8.5±1.0% unconstrained; 65% less with emission flexibility | 10.5194/acp-5-2635-2005 |
| **John et al. (2012) ACP** | GFDL CM3 | Climate vs emission drivers τ; +5% PI→present; −9 to +4% RCPs | 10.5194/acp-12-12021-2012 |
| **Lawrence et al. (2001) ACP** | Theory | Defines AM vs CH₄-weighted [OH]; foundational methodology | 10.5194/acp-1-37-2001 |

### New Papers Identified (Paywalled — 8)

| Paper | Journal | DOI | Priority |
|-------|---------|-----|----------|
| Prather & Zhu (2024) | Science | 10.1126/science.adn0415 | **High** — resetting OH/τ with UV |
| Patra et al. (2014) | Nature | 10.1038/nature13721 | **High** — NH/SH OH parity |
| Patra et al. (2021) | JGR Atmos | 10.1029/2020JD033862 | **High** — MCF still constrains OH |
| Prinn et al. (2001) | Science | 10.1126/science.1058673 | **Medium** — foundational MCF |
| Prinn et al. (2005) | GRL | 10.1029/2004GL022228 | **Medium** — updated MCF |
| Prather et al. (2012) | GRL | 10.1029/2012GL051440 | **Medium** — τ reassessment |
| Turner et al. (2018) | PNAS | 10.1073/pnas.1807532115 | **Medium** — ENSO/OH |
| Fiore et al. (2024) | Ann Rev Earth Planet Sci | 10.1146/annurev-earth-032320-090307 | **Medium** — comprehensive review |

### Key Gap Resolution: 2022–2023
**The 2022–2023 gap is now filled!**
- Zhao et al. (2023) — Critical reconciliation showing models overestimate OH by ~20%
- Anderson et al. (2023) — First satellite OH constraint feasibility study

### Pre-2011 Papers Added

| Period | Papers Added | Significance |
|--------|-------------|-------------|
| 2001 | Lawrence et al. (ACP) | Methodological foundation (AM vs CH₄-weighted) |
| 2005 | Bousquet et al. (ACP) | Early MCF inversion with emission uncertainty analysis |
| 2012 | John et al. (ACP) | Climate vs emissions drivers over 1860–2100 |

### Updated Coverage
| Period | Papers in DB | Status |
|--------|-------------|--------|
| 2000–2005 | 3 (Lawrence, Bousquet, Spivakovsky[pw]) | Good |
| 2005–2010 | 0 new OA | Gap (Prinn 2005, Krol 2003 are paywalled) |
| 2011–2012 | 3 (Montzka, Prather[pw], John) | **Montzka + John extracted** |
| 2013–2016 | 6 (Voulgarakis, Naik, Holmes, Murray, Patra[pw], McNorton, Lelieveld) | Good |
| 2017–2018 | 4 (Turner, Rigby[pw], Nicely 2018, Turner 2018[pw]) | Good |
| 2019 | 3 (Zhao, Naus, Rowlinson) | Complete |
| 2020–2021 | 9 | **Excellent** |
| 2022–2023 | 2 (Zhao 2023, Anderson 2023) | **Gap now filled** ✅ |
| 2024 | 4 (Duncan, Mertens, Souri, Prather[pw]) | **Excellent** |
| 2025 | 2 (Acquah, Saunois) | Complete |

### Updated Final Statistics
- **Total unique papers in database:** 44
- **Downloaded (OA):** 33 PDFs
- **Paywalled/not obtained:** 11
- **Data extracted:** 26 papers
- **Data extraction still pending:** 7 (older CTM studies + Saunois 2017)
- **Acquisition success rate:** 33/44 = 75%
