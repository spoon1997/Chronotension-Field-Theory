# QCFT A3 & C1 — Fixing ℓ_η and Setting Up pp→ppπ⁰ Near Threshold
## A3. Fixing the η correlation length ℓ_η from one forward-slope reference
- Chosen reference forward slope: **B_ref = 14.00 GeV⁻²** (moderate-energy point).
- Dimensionless braid size factor from A2: **c = 3.30**.
\[ \ell_\eta = \sqrt{\frac{B_{\rm ref}}{2(1+c^2/3)}} ,\qquad R_p = c\,\ell_\eta. \]
- Result: **ℓ_η = 1.230 GeV⁻¹ = 0.243 fm**,  **R_p = 4.058 GeV⁻¹ = 0.801 fm**.
> These numbers are purely *derived* from the single slope input and the braid torsion factor; no extra knobs.

---
## C1. Kinematics for pp→ppπ⁰ near threshold (3-body phase space)
The exact 3-body phase space for two protons and a π⁰ in the CM frame is
\[ \Phi_3(s;m_p,m_p,m_{\pi^0}) = \frac{1}{256\,\pi^3 s} \int_{(2m_p)^2}^{(\sqrt{s}-m_{\pi^0})^2} ds_{pp}\;\frac{\lambda^{1/2}(s,s_{pp},m_{\pi^0}^2)\,\lambda^{1/2}(s_{pp},m_p^2,m_p^2)}{s_{pp}} . \]
We evaluate this numerically as a function of the CM **excess energy** \(Q = \sqrt{s} - (2m_p + m_{\pi^0})\).
Near threshold, \(\Phi_3 \propto Q^2\) for S-wave emission; the exact integral confirms this scaling.

**Table — Φ₃ vs Q for pp→ppπ⁰ (normalized at Q=40 MeV)**
| Q (MeV) | Φ₃ (GeV⁻²) | Φ₃ / Φ₃(40 MeV) | Q² (MeV²) |
|---:|---:|---:|---:|
|    5 | 2.396e-09 | 0.015 |     25 |
|   10 | 9.601e-09 | 0.062 |    100 |
|   20 | 3.854e-08 | 0.248 |    400 |
|   40 | 1.552e-07 | 1.000 |   1600 |
|   80 | 6.283e-07 | 4.048 |   6400 |
|  120 | 1.428e-06 | 9.201 |  14400 |
|  160 | 2.561e-06 | 16.497 |  25600 |
|  200 | 4.030e-06 | 25.966 |  40000 |

**Use in QCFT amplitude**
The production cross-section with a contact-like overlap amplitude \(\mathcal M_{pp\to pp\pi^0}\) reads
\[ \sigma_{pp\to pp\pi^0}(s) = \frac{1}{4F}\,|\mathcal M|^2\,\Phi_3(s)\,\mathcal{T}_{\rm topo} , \]
with the usual CM flux \(F\) and a topological weight \(\mathcal{T}_{\rm topo}\). In our Gaussian chronode model, the **cubic overlap** \(g^{(3)}_{pp\pi}\) scales geometrically with the proton size \(R_p=c\,\ell_\eta\) and the pion size \(R_\pi \sim a_\pi\,\ell_\eta\) (with \(a_\pi=\mathcal{O}(1)\)). Thus, up to an overall constant fixed at a single reference energy, the **energy dependence** is fully predicted by Φ₃.

---
## Plain-English
We just fixed the η correlation length ℓ_η (and hence the proton size) from **one** forward-slope point. Then we set up the exact 3-body phase space for \(pp\to pp\pi^0\) and showed how the cross-section’s energy dependence near threshold is driven by Φ₃ ∝ Q². Next we’ll plug in the **Gaussian overlap** to get the absolute normalization at one energy and then **predict the full \(s\)-dependence** with no new knobs.
