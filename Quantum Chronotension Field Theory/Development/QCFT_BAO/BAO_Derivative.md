# QCFT_BAO: Derivation and Predictions

**Author:** Luke Cann — Independent Theoretical Physicist and Founder of QCFT  
**Status:** Consolidated draft (Milestones 1–5 complete)  

---

## 🔑 Core Mechanism

- **ΛCDM view:** BAO are relic sound waves in the primordial plasma at recombination (~150 Mpc).  
- **QCFT view:** BAO are the **universal eigenmode of the η-field** (time viscosity).  
- Galaxies and halos only **excite** this resonance; they do not set its scale.  

In QCFT, BAO are not a historical accident (“frozen sound”), but a **fundamental oscillatory mode** of the field that underpins time itself.  

---

## 🎯 Step-by-Step Derivation

### Milestone 1 — Operator Factorization
Start from a minimal QCFT energy density with gradient and curvature terms:

\[
\mathcal{E}[\eta]
= \tfrac{\kappa}{2}(\nabla \eta)^2
+ \tfrac{\xi}{2}(\nabla^2 \eta)^2
+ \tfrac{m^2}{2}(\eta-\eta_0)^2
- J\,\eta.
\]

Linearizing \(\eta = \eta_0 + \delta\eta\) and varying gives:

\[
(-\kappa\nabla^2 + \xi\nabla^4 + m^2)\,\delta\eta = J.
\]

Divide by \(\xi\) and factorize:

\[
(\nabla^2 - \lambda_g^{-2})(\nabla^2 + k_0^2)\,\delta\eta = -\tfrac{J}{\xi},
\]

with the parameter map:

\[
\lambda_g^{-2} - k_0^2 = \kappa/\xi, \qquad -\lambda_g^{-2}k_0^2 = m^2/\xi.
\]

**Interpretation:**  
- \(\lambda_g\): **short-range Yukawa branch** (halo/GIR scale, ~Mpc).  
- \(k_0^{-1}\): **long-range oscillatory branch** (BAO scale, ~129 Mpc).  

---

### Milestone 2 — Green’s Function
Fourier inversion yields the 3D Green’s function:

\[
G(r) = \frac{C}{4\pi r}\,\Big[-\cos(k_0 r+\delta) - e^{-r/\lambda_g}\Big],
\quad C=\frac{1}{\xi(\lambda_g^{-2}+k_0^2)}.
\]

- **Yukawa term**: decays as \(e^{-r/\lambda_g}/r\), dominates near halos.  
- **Oscillatory term**: \(\cos(k_0 r+\delta)/r\), dominates at cosmological scales.  

---

### Milestone 3 — Position and Width

- **Position:**  
  BAO bump occurs at the first oscillatory maximum:  
  \[
  r_{\rm BAO} \approx \frac{\pi-\delta}{k_0} \;\simeq\; \frac{\pi}{k_0}.
  \]  
  Locking this to observation: \(k_0^{-1} \approx 129\) Mpc.

- **Width:**  
  Coherence length \(L_{\rm coh}\) damps the oscillation:  
  \[
  \text{FWHM}_r \approx 1.386\,L_{\rm coh}.
  \]  
  With \(L_{\rm coh}\sim 15{-}25\) Mpc → bump width \(\sim 20{-}30\) Mpc.  
  Equivalent k-space Gaussian envelope:  
  \(\text{FWHM}_r \approx 2.355/\sigma_k\).  

**Result:** BAO is naturally **narrow** without fine-tuning, set by η-stiffness \(\xi\).  

---

### Milestone 4 — Redshift Anisotropy

QCFT redshift law:
\[
1+z_{\rm QCFT} = (1+z_{\rm GR})^{p}, \quad p \approx -1.15.
\]

Implication for GR-reduced catalogs:

- **Transverse scale:**  
  \(\alpha_\perp(z) = D_M^{\rm GR}(z_{\rm GR}) / D_M^{\rm QCFT}(z_{\rm QCFT})\).  
  ≈ unity (small stretch).

- **Radial scale:**  
  \[
  \alpha_\parallel(z) = \frac{H_{\rm QCFT}(z_{\rm QCFT})}{H_{\rm GR}(z_{\rm GR})}
  \;\frac{1}{p(1+z_{\rm GR})^{p-1}}.
  \]  
  Predicts **radial shrinkage** with redshift.

- **Anisotropy ratio:**  
  \[
  \epsilon(z)=\alpha_\parallel(z)/\alpha_\perp(z) < 1.
  \]

**Result:** QCFT predicts BAO spheres appear **squashed along the line of sight** in GR analyses, with anisotropy growing with redshift.  

---

### Milestone 5 — Secondary Effects

- **Mass dependence (λg):**  
  Halo mass changes λg, which alters **amplitude only**, not BAO position.

- **Environment dependence:**  
  BAO amplitude stronger near Gradia walls, weaker in voids.  
  Position remains universal.

**Result:**  
- Position locked at ~129 Mpc.  
- Only amplitude varies with mass/environment.  

---

## 📌 Locked Principles

1. **BAO = η-field resonance** (not sound horizon).  
2. **λg (halo scale):** mass-dependent, short-range (~Mpc).  
3. **k₀⁻¹ (BAO scale):** universal, long-range (~129 Mpc).  
4. **Position:** fixed.  
5. **Width:** narrow, set by η-stiffness.  
6. **Anisotropy:** radial shrinkage in GR reductions.  
7. **Secondary effects:** amplitude only.  

---

## 🚨 Falsifiability

QCFT would fail if:
- BAO position drifts with halo mass, environment, or tracer.  
- BAO bump is broad and incoherent without ad hoc damping.  
- Radial anisotropy absent or opposite after controlling for systematics.  
- Small-scale oscillations (~Mpc BAO) observed (would mean \(k₀^{-1}\approx λ_g\)).  

---

## ✅ Summary

**QCFT Prediction:**  
> *BAO is not a fossil sound wave. It is the cosmos ringing at its natural η-field frequency. Galaxies only excite it — the note itself never changes.*  

- Position fixed at ~129 Mpc.  
- Width narrow (~20–30 Mpc).  
- Radial anisotropy with redshift in GR catalogs.  
- Amplitude varies, position does not.  

This makes BAO one of QCFT’s clearest falsifiable wins against ΛCDM.
