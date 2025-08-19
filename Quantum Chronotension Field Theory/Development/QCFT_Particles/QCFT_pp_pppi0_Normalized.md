# QCFT pp→ppπ⁰ — Data-Anchored Normalization and Predictions
## Normalization choice
- **Anchor:** σ(pp→ppπ⁰) at **Q_ref = 20 MeV** set to **0.8 μb** (microbarn).
  - This is a conventional anchor within the **Indiana Cooler / CELSIUS** near-threshold range, where cross sections are at the **microbarn** level.
  - Purpose: fix the single overall factor |𝓜|² in the QCFT Gaussian-overlap model; the **energy dependence** remains a QCFT prediction.

## Fixed core scales (from A3)
- ℓ_η = 1.230 GeV⁻¹ = 0.243 fm
- R_p = c·ℓ_η = 4.058 GeV⁻¹ = 0.801 fm (with c = 3.3)

## Pion size scan and effective form factor
- a_π = 2.0 ⇒ R_π = 0.485 fm, R_eff = 0.936 fm
- a_π = 2.5 ⇒ R_π = 0.607 fm, R_eff = 1.005 fm
- a_π = 3.0 ⇒ R_π = 0.728 fm, R_eff = 1.082 fm

**Prediction:**
For each a_π we compute
\[\sigma(s)=\underbrace{\frac{1}{4F(s)}}_{\text{kinematic flux}}\;\underbrace{\Phi^{\rm eff}_3(s;R_{\rm eff})}_{\text{3-body PS}\times e^{-R_{\rm eff}^2 p_\pi^2}}\;\times \mathcal{N},\]where 𝒩 is fixed by **σ(Q_ref)=0.8 μb**. The only s‑dependence comes from the exact 3‑body phase space and the QCFT overlap form factor.

### Sample values (a_π = 2.5)
| Q (MeV) | σ_pred (μb) |
|---:|---:|
|    5 | 0.056 |
|   10 | 0.215 |
|   15 | 0.466 |
|   20 | 0.800 |
|   23 | 1.036 |
|   30 | 1.679 |
|   40 | 2.787 |
|   60 | 5.477 |
|   80 | 8.517 |
|  120 | 14.725 |
|  160 | 20.226 |
|  200 | 24.582 |
|  260 | 28.957 |
|  320 | 31.287 |

## Notes
- Changing a_π in [2.0, 3.0] mainly bends the curve at larger Q; the **Q² rise** right at threshold is robust.
- This anchor is well within the classic near-threshold datasets (Indiana Cooler, CELSIUS). We can re-anchor to a specific published point if desired.
