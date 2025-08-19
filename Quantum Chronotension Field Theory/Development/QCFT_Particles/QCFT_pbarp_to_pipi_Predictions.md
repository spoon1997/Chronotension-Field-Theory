# QCFT C2 — p̄p → π⁺π⁻ (Annihilation) : Absolute Predictions with One Anchor
## Setup
- Use the A3-fixed core scales: ℓ_η and R_p = c·ℓ_η with c = 3.3.
- Two-body cross-section model (S-wave proxy):
\[
\sigma(s)\;=\;\mathcal{N}\;\frac{1}{16\pi s}\;\frac{p_f}{p_i}\;\exp\big(-R_{\rm eff}^2\,p_f^2\big),
\]
where \(p_i = \frac{\sqrt{\lambda(s,m_p^2,m_p^2)}}{2\sqrt{s}}\) and \(p_f = \frac{\sqrt{\lambda(s,m_\pi^2,m_\pi^2)}}{2\sqrt{s}}\).
- Overlap scale: \(R_{\rm eff} = \sqrt{R_p^2 + R_\pi^2}\) with \(R_\pi = a_\pi\,\ell_\eta\), \(a_\pi\in\{2.0,2.5,3.0\}\).

## Normalization (single anchor)
- Set **σ(√s_ref = 2.00 GeV) = 50 μb**. This fixes \(\mathcal{N}\). The **entire energy dependence** is then a QCFT prediction.

## Radii used
- a_π = 2.0 → R_π = 0.485 fm, R_eff = 0.936 fm
- a_π = 2.5 → R_π = 0.607 fm, R_eff = 1.005 fm
- a_π = 3.0 → R_π = 0.728 fm, R_eff = 1.082 fm

## Sample values (a_π = 2.5)
| √s (GeV) | σ_pred (μb) |
|---:|---:|
| 2.00 | 50.000 |
| 2.02 | 27.215 |
| 2.04 | 14.883 |
| 2.06 | 8.159 |
| 2.08 | 4.477 |
| 2.10 | 2.456 |
| 2.12 | 1.346 |
| 2.14 | 0.736 |
| 2.16 | 0.402 |
| 2.18 | 0.219 |
| 2.20 | 0.119 |
| 2.22 | 0.064 |
| 2.24 | 0.035 |
| 2.26 | 0.019 |
| 2.28 | 0.010 |
| 2.30 | 0.005 |
| 2.32 | 0.003 |
| 2.34 | 0.001 |
| 2.36 | 0.001 |
| 2.38 | 0.000 |
| 2.40 | 0.000 |

## Notes
- The \(1/p_i\) factor in 2→2 kinematics produces a formal divergence at the **p̄p threshold**; we therefore present curves for **√s ≥ 2.00 GeV** where the formula is well-behaved.
- The Gaussian factor encodes the QCFT overlap; as √s increases, \(p_f\) grows and the overlap **suppresses** σ, giving the steep fall you see.
- Varying \(a_\pi\) in [2,3] shifts the curvature mildly; the near-threshold normalization holds by construction.
