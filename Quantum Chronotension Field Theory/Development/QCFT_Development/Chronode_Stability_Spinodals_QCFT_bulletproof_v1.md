# Chronode Stability & Spinodals (QCFT) — Bulletproof Derivation

**Status:** stabilized draft with explicit derivation from the QCFT Lagrangian, analytical spinodal conditions, and a numerical classifier.

---

## Notation (all defined once)

| Symbol | Meaning |
|---|---|
| \(\eta^a(x)\) | QCFT time-viscosity field (vector in internal space) |
| \(V(\eta)\) | field potential from QCFT |
| \(\lambda, v\) | parameters in \(V\) (see below) |
| \(Q\) | topological charge / winding class of chronode |
| \(n\) | harmonic/generation index |
| \(\eta_{\rm env}\) | environmental/background field setting |
| \(R\) | chronode radius (collective coordinate) |
| \(R_*\) | stationary radius solving \(E'(R_*) = 0\) |
| \(\bar\sigma\) | effective wall tension (depends on \(Q,n,\eta_{\rm env}\)) |
| \(\kappa\) | wall bending rigidity (curvature correction) |
| \(\bar{\Delta\Pi}\) | inside–outside pressure contrast derived from \(V\) and environment |
| \(\alpha(Q,n)\) | core/topological (and mode) energy coefficient (\(>0\)) |

**Units:** \([\bar\sigma] = E/L^2\), \([\kappa] = E\), \([\bar{\Delta\Pi}] = E/L^3\), \([\alpha] = E\cdot L\).

---

## QCFT Lagrangian → static energy

Start from the QCFT Lagrangian density (papers I–VII):

\[
\mathcal{L}_{\rm QCFT} = \tfrac{1}{2} \, \delta^{ab} \, \partial_\mu \eta^a \, \partial^\mu \eta^b
\; - \; \lambda\, (\eta^a \eta^a - v^2)^2
\; + \; \theta \, \epsilon^{\mu\nu\rho\sigma} f^a_{\mu\nu} f^a_{\rho\sigma} \, .
\]

For static, finite-energy configurations (chronodes), the energy functional is

\[
E[\eta] = \int d^3x \left[ \tfrac{1}{2} (\nabla \eta^a)^2 + V(\eta) \right] + E_\theta[\eta] ,
\quad V(\eta) = \lambda (\eta^a \eta^a - v^2)^2 .
\]

We approximate a **spherical soliton (chronode)** by a thin-wall ansatz: interior field near \(\eta_{\rm in}\), exterior near \(\eta_{\rm out}\), with a profile across a wall of thickness \(\delta \ll R\). The energy splits into:

1) **Surface energy** from gradients across the wall (and potential across the transition):
\[
E_\text{surf} \approx 4\pi R^2 \, \bar\sigma, 
\quad
\bar\sigma(Q,n,\eta_{\rm env}) = \int_{\rm wall} \! dr \; \left[ (\partial_r \eta)^2 + 2 V(\eta) \right] .
\]

2) **Curvature (bending) correction** from wall curvature (Helfrich-like from the gradient term on curved surfaces):
\[
E_\text{bend} \approx 8\pi \kappa(Q,n,\eta_{\rm env}) \, R .
\]
This arises from next-to-leading corrections in a wall-thickness expansion of the gradient term on a curved interface.

3) **Volume/pressure work** from interior vs exterior free-energy density (pressure) difference derived from \(V\) *and* the environment (\(\eta_{\rm env}\), background Gradia, etc.). Defining \(\bar{\Delta\Pi} = \Pi_\text{in}-\Pi_\text{out}\) (positive when the interior “pushes out”):
\[
E_\text{vol} = - \tfrac{4\pi}{3} R^3 \, \bar{\Delta\Pi}, 
\quad
\bar{\Delta\Pi} \simeq - \Delta V = -\big(V(\eta_{\rm in})-V(\eta_{\rm out})\big) + \cdots
\]

4) **Topological/core & mode energy** from winding/harmonics and trapped \(\eta\)-modes. The leading collective-coordinate scaling is *repulsive at small \(R\)*:
\[
E_\text{core} \approx \frac{\alpha(Q,n)}{R}, \qquad \alpha(Q,n)>0.
\]
This combines quantized winding energy and zero-point/standing-mode costs enforced by the chronode topology.

Putting it together, the **effective energy vs radius** is
\[
\boxed{\; E(R) = 4\pi \bar\sigma \, R^2 \; + \; 8\pi \kappa \, R \; + \; \frac{\alpha(Q,n)}{R} \; - \; \tfrac{4\pi}{3} \, \bar{\Delta\Pi} \, R^3 \;} \tag{1}
\]

> **Why all four terms are needed.** With only \(R^2\) and \(R^3\) (surface vs pressure), the stationary point is a **maximum** (Coleman-like bubble barrier). A **stable** finite \(R_*\) requires an additional short-distance repulsion (\(\alpha/R\)) and/or curvature rigidity (\(\kappa\)).

---

## Stationary radius and stability

Differentiate (1):
\[
E'(R) = 8\pi \bar\sigma R + 8\pi\kappa - \frac{\alpha}{R^2} - 4\pi\bar{\Delta\Pi} R^2 .
\]
Set \(E'(R_*)=0\) to get the stationary radius \(R_*\). The curvature test is
\[
E''(R) = 8\pi \bar\sigma + \frac{2\alpha}{R^3} - 8\pi \bar{\Delta\Pi} R .
\]
**Stable:** \(E''(R_*)>0\). **Metastable:** local minimum exists but \(E(R_*)>E(\infty)\).

---

## Analytical spinodals (where the minimum disappears)

At a spinodal, the extremum is inflectional: \(E'(R_s)=0\) **and** \(E''(R_s)=0\). Writing
\(A=4\pi\bar\sigma,\; B=8\pi\kappa,\; C=\alpha,\; D=\tfrac{4\pi}{3}\bar{\Delta\Pi}\),
we have
\[
E = A R^2 + B R + \frac{C}{R} - D R^3, \quad
E' = 2 A R + B - \frac{C}{R^2} - 3 D R^2, \quad
E'' = 2A + \frac{2C}{R^3} - 6 D R.
\]

Solving \(E'=E''=0\) yields a **parametric spinodal curve** in terms of \(R\):
\[
\boxed{\; D_s(R) = \frac{3 A R + B}{6 R^2} , \qquad
C_s(R) = \frac{A R^3 + B R^2}{2} . \;} \tag{2}
\]
Translated back: for each \(R\), the boundary between **soft/hard/snap/melt** is
\[
\bar{\Delta\Pi}_s(R) = \frac{3\bar\sigma}{2R} + \frac{\kappa}{R^2}, 
\qquad
\alpha_s(R) = 2\pi \bar\sigma R^3 + 4\pi \kappa R^2 .
\]

- **Melt spinodal:** \(\bar\sigma\!\to\!0,\;\alpha\!\to\!0,\;\bar{\Delta\Pi}\!\to\!0\) — no finite \(R_*\), the chronode dissolves.
- **Soft spinodal:** small contrast \(\bar{\Delta\Pi}\) and tension \(\bar\sigma\); minimum disappears at large \(R\).
- **Hard spinodal:** growing contrast/tension squeezes \(R_*\) downward until \(E''\to0^+\).
- **Snap spinodal:** high contrast or low \(\alpha\) drives \(R_*\to 0\); beyond, no positive solution: catastrophic collapse (FCE risk).

---

## Mapping to QCFT quantities

- \(\bar\sigma\) and \(\kappa\) are **functionals of the wall profile** induced by \(V(\eta)\) and depend on \(Q,n,\eta_{\rm env}\). For the canonical \(V=\lambda(\eta^2-v^2)^2\), a thin-wall estimate gives \(\bar\sigma \sim \tfrac{2\sqrt{2}}{3} v^3 \sqrt{\lambda}\) (as in \(\phi^4\) kinks), while \(\kappa\) scales with the wall thickness and gradient energy curvature correction.
- \(\bar{\Delta\Pi}\) encodes **η-contrast**: approximately minus the potential-density gap, plus environmental contributions from background Gradia and anisotropy.
- \(\alpha(Q,n)\) gathers **topological winding energy** and **trapped-mode zero-point energy**, both repulsive at small \(R\). \(\alpha\) increases with \(Q\) and harmonic index \(n\).

> This \(R_*\) is the same effective core radius used elsewhere in QCFT (redshift/lensing modules); here it arises via the stability extremum of the chronode energy.

---

## Practical classifier (algorithm)

Given \((Q,n,\eta_{\rm env})\Rightarrow (\bar\sigma,\kappa,\bar{\Delta\Pi},\alpha)\):

1. Solve \(E'(R)=0\) for \(R>0\) (bracket and root-find).
2. If no positive root:  
   - if \(\bar\sigma,\bar{\Delta\Pi}\approx0\) → **Melt**, else → **Snap**.
3. If a root exists, compute \(E''(R_*),\;E(R_*),\;E(\infty)\):  
   - **Stable:** \(E''(R_*)>0\) and \(E(R_*)<E(\infty)\).  
   - **Metastable:** \(E''(R_*)>0\) and \(E(R_*)>E(\infty)\).  
   - Otherwise: **Snap**.

---

## Worked example (toy numbers; symbolic structure is general)

Let \(\bar\sigma=1\), \(\kappa=0.2\), \(\alpha=2\), \(\bar{\Delta\Pi}=0.3\) in arbitrary units.

- \(A=4\pi\), \(B=8\pi\,0.2\), \(C=2\), \(D=\tfrac{4\pi}{3}\,0.3\).  
- Numeric root of \(E'(R)=0\) gives a positive \(R_*\) and \(E''(R_*)>0\) → **Stable**.  
Change \(\bar{\Delta\Pi}\to0.8\) (harder contrast): \(R_*\) shrinks; beyond the spinodal from (2), no root → **Snap**.

---

## Dimensional & sign checks (sanity)

- Every term in (1) has energy dimension.  
- For outward-pushing interior (\(\bar{\Delta\Pi}>0\)) the \(-R^3\) term *lowers* energy with larger \(R\), as it should.  
- Without \(\alpha\) and \(\kappa\), the extremum is a **maximum** → finite, stable chronodes **require** short-distance repulsion and/or curvature stiffness.

---

## References to the QCFT canon (for readers)

- QCFT Lagrangian and chronodes: Papers I, II, IV, V, IX.  
- Emergent geometry & Gradia: Papers I, III, VIII.  
- S-matrix/topology & conserved winding: Papers V, VII, IX.

---

## Appendix A — Spinodal derivation details

Let \(E = A R^2 + B R + C/R - D R^3\).  
At the spinodal, \(E'=0\) and \(E''=0\). One finds
\[
2C/R^3 = 6DR - 2A \;\Rightarrow\; C = 3 D R^4 - A R^3 .
\]
Plugging into \(E'=0\) yields
\[
6 D R^2 = 3 A R + B \;\Rightarrow\; D_s(R) = \frac{3AR+B}{6R^2},\quad
C_s(R) = \frac{A R^3 + B R^2}{2}.
\]
As stated in (2).

---

## Appendix B — Estimating \(\bar\sigma\), \(\kappa\) from \(V(\eta)\)

For \(V=\lambda(\eta^2-v^2)^2\), a thin-wall profile \(\eta(r)\) across the wall gives
\[
\bar\sigma \sim \int_{-\infty}^{\infty} \! dr \big[(\partial_r\eta)^2 + 2V(\eta)\big] 
\sim \tfrac{2\sqrt{2}}{3} v^3 \sqrt{\lambda},
\]
and \(\kappa\) scales as the wall-thickness times \(\bar\sigma\): \(\kappa\propto \delta\,\bar\sigma\) (geometry-dependent). Exact values require solving the 1D wall Euler–Lagrange equation in \(V\).

---

### Plain-English takeaway
We start from QCFT’s energy and treat a chronode like a spherical “bubble” with a wall and a pressure difference. That alone gives a hill, not a valley—so the chronode would either shrink or grow without stopping. Real chronodes are stabilized by two extra, physically required ingredients: (i) **topology/modes** that strongly resist being squeezed (a \(1/R\) term), and (ii) **wall stiffness** on curved surfaces (a bending term \(\propto R\)). With these, the energy has a genuine minimum at a finite size \(R_*\). We derive exact formulas for when that minimum vanishes (the **spinodals**), which cleanly separate **melt**, **soft**, **hard**, and **snap** failure modes.
