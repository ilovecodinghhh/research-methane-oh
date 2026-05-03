# Analytical Notes — research-methane-OH

## COVID-19 NOx Anomaly Papers

⚠️ **Critical gap in post-2018 time series**

The 2020 COVID-19 lockdowns caused unprecedented global NOx reductions:
- Urban NOx dropped 20–50% in spring 2020
- Expected effect: ↓NOx → ↓OH production → ↑CH4 lifetime (positive CH4 forcing)
- Counter-effect: ↓CO from reduced traffic → ↑OH (smaller magnitude)

**No OA paper found (as of 2026-05-03) providing a quantitative global mean [OH] estimate for 2020.**

This represents the single most important gap in the post-2018 time series. The COVID signal is expected to be detectable in MCF-based inversions but the MCF signal-to-noise ratio may be too low given MCF's ongoing atmospheric decay.

### Papers to track:
- Any AGAGE/NOAA team publications post-2023 addressing 2020 OH
- Zhu et al. (2025, EGU) — extends to 2019 only (+4.7% OH trend vs 1999)

---

## OH Recycling Mechanism Studies

OH recycling in pristine tropical forests (isoprene-rich environments):
- **Mechanism:** HOx recycling pathways during isoprene oxidation can maintain OH at higher levels than expected from pure NOx-dependent chemistry
- **Relevance:** Bottom-up models that don't capture this recycling may underestimate tropical OH
- **Key authors:** Lelieveld et al., Fuchs et al.
- **Status:** Referenced in Anderson et al. (2021) as causing model-observation discrepancy in Amazon outflow regions

---

## Key Discrepancies Between Studies

### 1. CH4 Lifetime: τ_trop vs τ_atm
| Metric | Value | Source |
|--------|-------|--------|
| τ_trop (OH only) | 11.2 ± 1.3 yr | Saunois et al. (2020) |
| τ_atm (whole atmosphere) | 9.1 ± 0.9 yr | IPCC AR6; Prather et al. (2012) |
| τ_atm (AerChemMIP) | 8.4 ± 0.3 yr | Stevenson et al. (2020) |

**Key point:** The AerChemMIP value (8.4 yr) is notably shorter than IPCC AR6 (9.1 yr). This is because:
- AerChemMIP uses present-day simulations with coupled chemistry
- IPCC value is MCF-constrained (observationally derived)
- The ~0.7 yr difference is significant for global CH4 budget estimates

### 2. OH Trend: Stable vs Increasing
- **Zhao et al. (2020):** No significant trend 1980–2018 from MCF
- **Stevenson et al. (2020):** +8–12% since 1850 (model-based, pre-industrial to present)
- **Zhu et al. (2025):** +4.7% 1999–2019 (GEOS-Chem)
- **Reconciliation:** MCF signal may be too noisy to detect small trends; satellite era shows possible increase

### 3. Inter-model OH Spread
- **Zhao et al. (2020):** Factor ~2 range across CCMI models (0.81–1.51 × 10⁶)
- **Nicely et al. (2020):** NOx is dominant driver of spread, followed by photolysis and water vapor
- **Implication:** Model-based OH estimates remain poorly constrained; MCF remains essential

### 4. NH/SH Asymmetry
- Most models show NH/SH ratio ~1.2–1.3 (OH higher in NH due to NOx)
- Observation-based estimates: ~1.25–1.28
- Some models show ratio as low as 1.13 or as high as 1.42
- Acquah et al. (2025) shows CEDS emissions enhance NH OH more than SH

---

## Methodological Notes

### Temperature-dependent rate constant k(OH+CH4)
- Standard expression: $k = 2.45 \times 10^{-12} \exp(-1775/T)$ cm³ molec⁻¹ s⁻¹
- Used by most models following JPL/IUPAC recommendations
- Variations in T fields across models contribute to lifetime differences
- **Not explicitly reported in most accessed papers** — typically referenced to JPL kinetics

### Air-mass vs CH4-weighted OH
- Air-mass weighted: Simple volume integral of [OH]
- CH4-weighted ($[OH]_{CH_4}$): Weighted by $k_{OH+CH_4} \times [air]$ — more relevant for lifetime
- **Lawrence et al. (2001)** formulation used by most studies
- Difference typically ~5–10% between methods
- Acquah et al. (2025) explicitly uses CH4-weighted formulation per Lawrence et al. (2001)

### MCF Signal Decay Issue
- MCF atmospheric abundance has declined by >90% since peak (~1990)
- As MCF → 0, signal-to-noise for OH constraint degrades
- Post-2020 MCF observations may be insufficient for robust annual OH estimates
- Naus et al. (2020, EGU): 4DVAR inversion of MCF using TM5 CTM finds no large IAV (>2%) or trend needed
- **This is a fundamental limitation for future top-down OH estimation**

---

## Temporal Coverage Summary

```
1850 ████████████████████████████████████████████████ 2025
     |--- Stevenson (AerChemMIP) historical trend ---|
                    |-------- Zhao CCMI: 1980-2015 --------|
                    |-------- Zhao budget: 1980-2018 --------|
                         |---- Anderson ENSO: 1980-2018 ----|
                              |-- Saunois GMB: 2000-2017 --|
                              |-- Acquah: 2000-2010 --|
                                        |-- Zhu: 1999-2019 --|
                                                     | GAP: 2020-2025 |
```

**Critical observation:** There is a significant data gap for observation-constrained global OH from 2020 onward.

---

*Notes compiled: 2026-05-03*
