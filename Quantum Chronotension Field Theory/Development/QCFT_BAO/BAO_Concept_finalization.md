# QCFT_BAO — Reflection & Consolidation (Sept 2025)

**Author:** Luke Cann — Independent Theoretical Physicist and Founder of QCFT  
**Status:** Conceptual layer locked; math derivation next

---

## Executive summary (plain-English)

- **What BAO is (in QCFT):** not a fossil sound wave from a hot plasma, but a **universal resonance** of the η-field (time-viscosity) itself.  
- **Two natural scales:**  
  - **Short (halo) scale:** \( \lambda_g \sim \) Mpc — sets a galaxy’s Gradia Influence Radius (GIR); **varies with mass**.  
  - **Long (BAO) scale:** \( k_0^{-1} \approx 129\ \mathrm{Mpc} \) — the field’s **eigenmode**; **universal** (independent of galaxy mass/environment).  
- **Why BAO doesn’t drift:** galaxies only **excite** the resonance; they do **not** set its pitch. Like dropping a **ping-pong ball** vs a **lead ball** of the same size into water: different splash amplitudes, **same ripple wavelength** set by the medium.  
- **Core predictions QCFT will deliver:** (i) **fixed BAO position** \(\sim 129\ \mathrm{Mpc}\); (ii) **narrow BAO width** from η-stiffness; (iii) **line-of-sight BAO anisotropy** under GR reconstructions due to the QCFT redshift law.  
- **Contrast with ΛCDM:** BAO is **not** a recombination sound horizon; it is a **present-day field mode** of time’s viscosity. ΛCDM’s “frozen sound wave” narrative is replaced, not reinterpreted.

---

## Locked principles

1. **BAO = η-field resonance (official).**  
   The “Goldilocks separation” story remains a **teaching analogy**, not the mechanism.

2. **Scale separation:**  
   - \( \lambda_g \) (GIR/halo) **depends on halo mass**.  
   - \( k_0^{-1} \) (BAO) is **universal** and **\(\gg \lambda_g\)**.

3. **Insensitivity to local viscosity:**  
   Local η distortions inside/around halos do not shift the BAO resonance; they affect **amplitudes**, not **position**.

4. **QCFT redshift law (locked):**  
   \[
   1+z_{\mathrm{QCFT}} \;=\; (1+z_{\mathrm{GR}})^{\,p}, \qquad p = -1.15 \pm 0.05.
   \]
   This mapping will induce **apparent radial BAO anisotropy** when data are reduced in GR units.

5. **Replacement claim:**  
   ΛCDM’s “sound horizon at recombination” is **not** the cause of BAO; QCFT **replaces** that mechanism with η-resonance.

---

## Mathematical skeleton (what the derivation will show)

Start from a minimal QCFT energy for small deviations \( \delta\eta \) around a calm background \( \eta_0 \):
\[
\mathcal{E}[\eta] \;=\; 
\frac{\kappa}{2}\,(\nabla \eta)^2 
\;+\; \frac{\xi}{2}\,(\nabla^2 \eta)^2
\;+\; \frac{m^2}{2}\,(\eta-\eta_0)^2
\;-\; J\,\eta.
\]

Linearize: \( \eta = \eta_0 + \delta\eta \) and vary:
\[
\big(-\kappa \nabla^2 + \xi \nabla^4 + m^2\big)\,\delta\eta \;=\; J.
\]

Factorize the operator (in 3-D, isotropic case):
\[
\underbrace{\big(\nabla^2 - \lambda_g^{-2}\big)}_{\text{Yukawa/halo}}
\;\underbrace{\big(\nabla^2 + k_0^{2}\big)}_{\text{oscillatory/BAO}}
\;\delta\eta \;=\; -\,J/\xi,
\]
with the parameter map
\[
\lambda_g^{-2} + k_0^2 \;=\; \kappa/\xi,
\qquad
\lambda_g^{-2} k_0^2 \;=\; m^2/\xi.
\]

**Green’s function response** to a compact source is then a **two-scale** superposition:
- **Short-range Yukawa tail** \(\propto e^{-r/\lambda_g}/r\) → halo/GIR structure.  
- **Long-range oscillatory tail** \(\propto \cos(k_0 r + \delta)/r\) → **BAO resonance** at
  \[
  r_{\mathrm{BAO}} \simeq \frac{\pi - \delta}{k_0} \;\approx\; 129\ \mathrm{Mpc}
  \quad (\text{with small phase } \delta).
  \]

**Key hierarchy (data-driven and natural here):**  
\[
k_0^{-1} \;\gg\; \lambda_g 
\quad\Rightarrow\quad
\text{no BAO wiggles at halo scales; the oscillation appears only at }\sim 10^2\ \mathrm{Mpc}.
\]

> **Interpretation:** \(k_0\) is **fixed by QCFT coefficients** \((\kappa,\xi,m)\) and thus **universal**; \( \lambda_g \) scales with source/halo properties (mild mass dependence).

---

## Why BAO does not depend on galaxy size

- Galaxies differ mainly by how strongly they **excite** the field (source \(J\)), which changes **local GIR** and **amplitudes**.  
- The **wavelength** of the far-field oscillation is **set by the field operator** via \(k_0\), not by the source.  
- **Analogy (locked):** ping-pong vs lead ball (same size) dropped into the same water → different splash strengths, **same ripple wavelength** governed by the medium.

---

## Core predictions (discriminants)

1. **Fixed BAO position**  
   \[
   r_{\mathrm{BAO}} \simeq 129\ \mathrm{Mpc}\quad\text{(universal, tracer-independent up to small projection effects)}.
   \]
   If high-precision surveys found a genuine **drift** or **split** of the BAO ruler beyond projection/systematic effects, QCFT would be falsified.

2. **Narrow BAO width**  
   Controlled by the curvature of the oscillatory branch and η-stiffness (the \(\xi \nabla^4\) term). Predicts a **sharp bump** in \(\xi(r)\) and an **acoustic-like wiggle** in \(P(k)\) centered at \(k_0 \approx \pi/129\ \mathrm{Mpc}^{-1}\approx 0.024\ \mathrm{Mpc}^{-1}\), with a small (\(\sigma_k\)) damping width from finite coherence and projection.

3. **Redshift anisotropy under GR mapping**  
   With the redshift law \(1+z_{\mathrm{QCFT}}=(1+z_{\mathrm{GR}})^p\) ( \(p \simeq -1.15\) ), distances inferred **assuming GR** will **mis-place** the BAO scale **along the line-of-sight** relative to transverse.  
   **QCFT forecast:** an apparent **radial shrinkage with \(z\)** in GR-reduced catalogs, while the **transverse** BAO remains closer to the universal scale.

**Secondary predictions (nice-to-have):**
- **Amplitude–mass trend:** heavier halos (larger \( \lambda_g \)) modestly modulate **amplitude**, not **position**.  
- **Environment coupling:** BAO strength correlates with **Gradia walls** vs **voids** (resonance excited more efficiently near walls).

---

## What counts as a win (vs ΛCDM)

- **Mechanism:** BAO reproduced as an **η-field eigenmode**, *no* recombination-era acoustics required.  
- **Position & width:** matched without baryon tuning; width explained by η-stiffness rather than plasma diffusion.  
- **Anisotropy with \(z\):** a **clean, quantitative** prediction from the QCFT redshift law that ΛCDM does not naturally mirror.

---

## Observational program (concise)

- **Data:** modern LSS catalogs (e.g., BOSS/eBOSS/DESI-like) across tracers (LRGs/ELGs/quasars) and redshift bins.  
- **Pipelines:**  
  1) Re-measure BAO peak **transverse vs radial** with careful control of reconstruction assumptions.  
  2) Check **tracer independence** of the **position** and **narrow width** (allowing amplitude differences).  
  3) Test for **redshift-dependent radial offset** predicted by QCFT’s \(p\)-law.  
- **Environment test:** split by Gradia-proxy density (filaments/walls vs voids) to see expected **amplitude** modulation; **position** should remain fixed.

---

## Failure modes (how QCFT could be falsified here)

- **BAO position drifts** with tracer/environment in a way inconsistent with a fixed \(k_0\).  
- **Width** requires ad-hoc, fine-tuned damping not derivable from η-stiffness.  
- **No sign** of the predicted **radial anisotropy** with redshift under GR reconstructions (after robust systematics control).  
- Discovery of **strong small-scale oscillations** (\(\mathcal{O}(\mathrm{Mpc})\)) in the two-point function attributable to BAO physics (would imply \(k_0^{-1}\not\gg\lambda_g\), contradicting the QCFT hierarchy).

---

## Open questions (to be addressed in the derivation)

- **Phase \( \delta \):** obtain its sign/magnitude from core matching; show \( |\delta| \ll 1 \) so that \( r_{\mathrm{BAO}} \approx \pi/k_0 \) holds to high accuracy.  
- **Parameter map:** provide example \((\kappa,\xi,m)\) that yields \((\lambda_g, k_0^{-1}) \approx (\mathrm{Mpc}, 129\ \mathrm{Mpc})\) and discuss naturalness.  
- **Weak mass-dependence:** quantify how \( \lambda_g(M) \) modulates amplitudes, not positions.  
- **Redshift projection:** produce explicit **radial vs transverse BAO** formulas under the QCFT→GR distance map using the locked exponent \(p\).

---

## Minimal math to include next (scoped)

1. **From \(\mathcal{E}\) to factorization:** derive  
   \((\nabla^2 - \lambda_g^{-2})(\nabla^2 + k_0^2)\delta\eta = -J/\xi\)  
   and the relations linking \(\lambda_g, k_0\) to \(\kappa,\xi,m\).

2. **Green’s function:** write the Yukawa + oscillatory terms explicitly; fix overall normalization to a fiducial source \(J\).

3. **Two-point imprint:** demonstrate a **narrow BAO bump** in \(\xi(r)\) when the oscillatory component of \(P(k)\) peaks at \(k_0\) with small \(\sigma_k\).

4. **Anisotropy mapping:** propagate distances with \(p\)-law to obtain a quantitative **radial shrinkage curve** testable against redshift-binned data.

---

## Glossary (symbols & terms)

- **η (eta):** time-viscosity field; the substrate of QCFT.  
- **Gradia:** \( |\nabla \eta| \); driver of what GR calls “gravity.”  
- **GIR (Gradia Influence Radius):** practical radius where a halo’s Gradia becomes negligible.  
- \( \lambda_g \): **short length scale** (Mpc), controls GIR/halo decay (Yukawa tail).  
- \( k_0 \): **BAO wavenumber**; \( k_0^{-1} \) is the **universal BAO scale** (\(\approx\) 129 Mpc).  
- **Stiffness (\(\xi\)):** coefficient penalizing sharp η curvature (\(\nabla^2\eta\)^2); makes BAO **narrow** and forbids Planck-scale wiggles.  
- **QCFT redshift law:** \( 1+z_{\mathrm{QCFT}}=(1+z_{\mathrm{GR}})^p \), \( p\simeq -1.15\).  
- **Goldilocks (analogy):** pair-separation intuition; not the mechanism.

---

## One-liner for the repo

> **BAO in QCFT is the drumbeat of time’s viscosity:** halos excite it with different amplitudes, but the beat’s wavelength is the same everywhere because it belongs to the field, not the galaxies.

---

## Next file to create

- `bao_gir_theory.md` — step-by-step derivation (factorization, Green’s function, parameter map) with the redshift-anisotropy formula.  
- (Optional) `bao_predictions.md` — concise plots: \(P(k)\) oscillation at \(k_0\), \(\xi(r)\) bump at \(\sim 129\ \mathrm{Mpc}\), and a schematic radial-vs-transverse drift vs \(z\) under GR mapping.

--- 

*End of consolidation note.*
