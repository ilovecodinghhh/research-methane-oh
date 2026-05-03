# Analytical Notes — research-methane-OH

## COVID-19 NOx Anomaly Papers

⚠️ **Critical gap in post-2018 time series**

The 2020 COVID-19 lockdowns caused unprecedented global NOx reductions:
- Urban NOx dropped 20–50% in spring 2020
- Expected effect: ↓NOx → ↓OH production → ↑CH4 lifetime (positive CH4 forcing)
- Counter-effect: ↓CO from reduced traffic → ↑OH (smaller magnitude)

**No OA paper found (as of 2026-05-03) providing a quantitative global mean [OH] estimate for 2020.**

He et al. (2021) GRL is relevant but focuses on reanalysis-driven OH differences (not COVID specifically). The ~2% met-driven OH uncertainty provides a floor for detecting COVID signals.

### Papers to track:
- Any AGAGE/NOAA team publications post-2023 addressing 2020 OH
- Zhu et al. (2025, EGU) — extends to 2019 only (+4.7% OH trend vs 1999)

---

## The OH Stability Debate: Timeline

A central debate in the field resolved over ~15 years:

| Year | Paper | Claim |
|------|-------|-------|
| ~2005 | Prinn et al., Bousquet et al. | Large OH IAV (7–9%), possible trends |
| **2011** | **Montzka et al.** | **OH IAV = 2.3 ± 1.5% (post-1998); "well buffered"** |
| 2017 | Rigby et al. / Turner et al. | Re-opened debate: large OH changes possible; problem is underdetermined |
| **2018** | **Nicely et al.** | **OH trend ≈ 0 because +0.95%/dec offset by −1.01%/dec from CH₄** |
| **2019** | **Naus et al.** | **2-box models biased by ~10%; apparent IAV overstated** |
| **2021** | **Naus et al.** | **3D inversion: OH IAV = 0.6–0.8% — closes debate in favor of stability** |
| **2021** | **He et al.** | **Met uncertainty = ~2% (floor); trend driven by reactive N, not met** |

**Current consensus (post-2021):** Global OH is very stable (IAV < 2%), with no significant multi-decadal trend. Earlier claims of large variability were artifacts of MCF emission uncertainties (pre-1998) and 2-box model biases.

---

## OH Recycling Mechanism Studies

OH recycling in pristine tropical forests (isoprene-rich environments):
- **Mechanism:** HOx recycling pathways during isoprene oxidation maintain OH higher than expected
- **Relevance:** Bottom-up models may underestimate tropical OH without this
- **Key authors:** Lelieveld et al., Fuchs et al.
- **Status:** Referenced in Anderson et al. (2021) as model-observation discrepancy source

---

## Key Discrepancies Between Studies

### 1. CH4 Lifetime: τ_trop vs τ_atm
| Metric | Value | Source |
|--------|-------|--------|
| τ_trop (OH only) | 11.2 ± 1.3 yr | Saunois et al. (2020, 2025) |
| τ_atm (whole atmosphere) | 9.1 ± 0.9 yr | IPCC AR6; Prather et al. (2012) |
| τ_atm (AerChemMIP) | 8.4 ± 0.3 yr | Stevenson et al. (2020) |
| τ_atm (Turner 2-box) | 9.2 ± 0.2 yr | Turner et al. (2017) |
| τ_trop (EMAC 2015) | 7.63 yr | Mertens et al. (2024) |

**Key point:** The AerChemMIP value (8.4 yr) is notably shorter than IPCC AR6 (9.1 yr). This is because:
- AerChemMIP uses present-day simulations with coupled chemistry
- IPCC value is MCF-constrained (observationally derived)
- The ~0.7 yr difference is significant for global CH4 budget estimates
- Turner et al. (2017) 2-box value (9.2) is consistent with MCF-based IPCC value

### 2. OH Trend: Stable vs Increasing
- **Montzka et al. (2011):** Small IAV, well-buffered (MCF 1998–2007)
- **Nicely et al. (2018):** +0.95 ± 0.18 %/decade, but offset by CH₄ rise → net ≈ 0
- **Zhao et al. (2020):** No significant trend 1980–2018 from MCF
- **Naus et al. (2021):** No significant trend 1994–2017 from 3D MCF inversion
- **He et al. (2021):** OH trend correlates with reactive N, not meteorology
- **Stevenson et al. (2020):** +8–12% since 1850 (model-based, pre-industrial to present)
- **Reconciliation:** Near-zero trend in observational era because compensating factors (↑NOx, ↑H₂O offset ↑CH₄); preindustrial-to-present shows net increase from NOx dominance

### 3. The "Underdetermined" Problem (Turner 2017)
- Turner et al. (2017) demonstrated that with CH₄ + MCF + δ¹³CH₄, the inversion is still underdetermined
- Most likely mathematical solution: emissions ↓25 Tg/yr + OH ↓7%
- But time-invariant OH also fits → cannot separate without external OH constraint
- **Nguyen et al. (2020) adds:** neglecting CH₄-OH feedbacks introduces 25% emission bias
- **Implication:** Future work needs independent OH constraints (satellites, HCHO) per Duncan (2024)

### 4. Inter-model OH Spread
- **Zhao et al. (2020):** Factor ~2 range across CCMI models (0.81–1.51 × 10⁶)
- **Nicely et al. (2020):** NOx is dominant driver of spread, followed by photolysis and water vapor
- **Acquah et al. (2025):** Emission inventory choice (CEDS vs MACCity) shifts OH significantly
- **Implication:** Model-based OH estimates remain poorly constrained; MCF (while it lasts) remains essential

### 5. NH/SH Asymmetry
- Most models show NH/SH ratio ~1.2–1.3 (OH higher in NH due to NOx)
- Observation-based estimates: ~1.25–1.28
- Some models show ratio as low as 1.13 or as high as 1.42
- Acquah et al. (2025): CEDS emissions enhance NH OH more than SH
- **Naus et al. (2019):** MCF-derived NH/SH ratio ≠ CH₄-relevant ratio (species-dependent kinetics)

---

## Methodological Notes

### Temperature-dependent rate constant k(OH+CH4)
- Standard: $k = 2.45 \times 10^{-12} \exp(-1775/T)$ cm³ molec⁻¹ s⁻¹
- Used by most models following JPL/IUPAC recommendations
- Variations in T fields across models contribute to lifetime differences

### Air-mass vs CH4-weighted OH
- Air-mass weighted: Simple volume integral of [OH]
- CH4-weighted ($[OH]_{CH_4}$): Weighted by $k_{OH+CH_4} \times [air]$ — more relevant for lifetime
- **Lawrence et al. (2001)** formulation used by most studies
- Difference typically ~5–10% between methods
- Acquah et al. (2025) explicitly uses CH4-weighted formulation

### MCF Signal Decay Issue
- MCF atmospheric abundance has declined by >90% since peak (~1990)
- Post-2020 MCF observations may be insufficient for robust annual OH estimates
- **This is a fundamental limitation** — motivates Duncan et al. (2024) satellite proposal
- Naus et al. (2021): Even with 3D inversion, the MCF constraint is weakening

### Chemical Feedback Amplification (Nguyen 2020)
- Static OH fields in inversions → 25% systematic bias over decadal timescales
- CH₄ perturbation → OH change → further CH₄ change (positive feedback)
- CO acts as intermediary: biomass burning CO → OH suppression → CH₄ enhancement
- **Practical implication:** All inversions using static OH need this caveat

---

## Temporal Coverage Summary

```
1850 ████████████████████████████████████████████████ 2026
     |--- Stevenson (AerChemMIP) historical trend ---|
              |-------- John (CM3): 1860-2100 --------|
                    |-------- Zhao CCMI: 1980-2015 --------|
                    |-------- Nicely empirical: 1980-2015 ---------|
                    |-------- Zhao budget: 1980-2018 --------|
                    |-------- He met forcing: 1980-2017 --------|
                    |- Bousquet MCF: 1980-2000 -|
                         |---- Anderson ENSO: 1980-2018 ----|
                         |---- Turner 2-box: 1983-2015 ---|
                              |- Montzka: 1998-2007 -|
                              |--- Naus 3D: 1994-2017 ---|
                              |-- Saunois GMB: 2000-2020 --|
                              |-- Acquah: 2000-2010 --|
                              |-- Zhao reconcil: 2000-2009 --|
                                   |- Souri sat: 2005-2019 -|
                                        |- Anderson sat: 2005-19 -|
                                                     | SPARSE: 2020-2026 |
```

**Critical observation:** There is a significant data gap for observation-constrained global OH from 2020 onward.

---

## The Model-Observation Reconciliation (Zhao 2023)

A major advance: Zhao et al. (2023) showed that unconstrained CTMs overestimate global OH by ~20%.

| Metric | Unconstrained Models | Obs-Constrained | Top-Down (MCF) |
|--------|---------------------|-----------------|----------------|
| [OH]trop-M (×10⁵) | 9.4–14.4 | ~2×10⁵ lower | ~8–10 |
| CH₄ loss (Tg/yr) | 577–612 | **471–508** | 459–516 |

**Root causes of model bias:**
- CO underestimation (especially NH) → too much OH
- NO₂ overestimation → too much OH production
- Total ozone column underestimation → too much UV → too much OH

**Implication:** Bottom-up budget estimates need observation-constrained OH fields. Raw model OH should not be used directly.

---

## The Emerging Satellite Era (2023–2024)

Three papers in 2023–2024 mark the beginning of satellite-based OH monitoring:

1. **Anderson et al. (2023):** Proved feasibility — ML + satellite retrievals can estimate tropical column OH
2. **Souri et al. (2024):** First global 1°×1° TOH trends from satellite data fusion (2005–2019)
3. **Duncan et al. (2024):** Framework paper arguing MCF is degrading, satellites must replace it

This transition is critical because MCF abundances are approaching detection limits (>90% decline since peak). By ~2030, MCF-based OH constraints will be effectively unusable.

---

*Notes compiled: 2026-05-03 | Updated with Turner, Montzka, He, Nicely 2018, Nguyen data*
