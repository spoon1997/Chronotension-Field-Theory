# QCFT Development Notes – Definitions v2.1

This file records **core fixes and clarifications** to QCFT’s formal structure.  
It accompanies the development files and should be read before using older drafts.  
Purpose: prevent contradictions, set clear definitions, and guide ongoing work.

---

## 🚧 High-Priority Fixes

### 1. η Redistribution vs. η² Conservation
- **Locked law:**  
  \[
  \int \eta^a \eta^a \, d^3x = \text{const.}
  \]
- **Fix:** Replace “global η decays” with **redistribution by hogging**.  
  - Galaxies and chronode clusters **pull in η locally**, leaving surrounding gaps thinner.  
  - Redshift arises because photons cross these stretched gaps.  
  - The universe **does not expand** — it remains finite and eternal, only its η-distribution evolves.

---

### 2. Scalar–Vector Mapping
- **Fix:** Define the scalar η in the emergent metric as:
  \[
  \eta(x,t) \equiv \big\langle (\eta^a \eta^a)^{1/2} \big\rangle_{\Lambda}(x,t)
  \]
  where ⟨·⟩ averages over a physical window set by the observable scale.  
- Ontology: **one field, two zoom levels** (vector fundamental, scalar effective).

---

### 3. Chronode Profile
- **Fix:** Chronodes are localized knots with extended halos.  
- Minimal ansatz:
  \[
  \eta^a(r) = \eta_\infty^a + u^a\,F(r), \quad 
  F(r) \sim r^{-p} e^{-r/\xi},\ \ p \in [0,1]
  \]
- Characteristic scale:  
  \(\xi \sim [2\sqrt{\lambda} v]^{-1}\).  
- This ensures scattering/overlap are well-defined without virtual particles.

---

### 4. No Propagators ≠ No Kernels
- QCFT has **no virtual particles**, but still uses Green kernels.  
- **Fix:** Keep linearized kernels for scattering:
  \[
  \mathcal{D}_{ab}(\bar\eta) \, G^{bc}(x-y \mid \bar\eta) 
  = \delta_a^{\ c}\,\delta^{(4)}(x-y)
  \]
- Amplitudes = overlap integrals of chronode sources linked by \(G\).

---

### 5. Photon Birefringence
- **Fix:**  
  - Cosmological propagation: **no birefringence** → \(c = 1/\eta\).  
  - Strong-Gradia zones (near compact objects, sharp η textures): allow **tiny, localized** birefringence.  
  - Parametrization:
    \[
    \frac{\delta c}{c} \;\approx\; 
    \kappa\,\frac{(\hat n \cdot \nabla \eta)^2}{\eta^2 \Lambda_b^2}
    \]

---

### 6. Local Lorentz Invariance
- **Fix:** Explicit statement:  
  - In slowly varying η patches, choose tetrads  
    \( e^0{}_0=1/\eta, \ e^i{}_j=\eta \delta^i{}_j \).  
  - Emergent metric is locally Minkowski.  
  - Lorentz symmetry holds to \(\mathcal{O}(\nabla\eta)\).

---

## ✅ Secondary Consistency Polishes

- **Redshift module:** future BAO/CMB work must **hold p = −1.15 ± 0.05 fixed**.  
- **η-lens compression:** formalize angular Jacobian (<1) with **suppressed flux magnification**.  
- **SMBH feedback:** define **Gradia Influence Radius (R\_GIR)** = radius where |∇η| drops below g\_min.

---

## 🧪 Self-Consistency Checks (to-do)

1. Verify overlap of chronode halos gives finite interaction energy.  
2. Show retarded Green kernel enforces causal signal speed \(c=1/\eta\).  
3. Confirm η-lens compression is orthogonal to the redshift exponent \(p\) (no double counting).

---

## ⚖️ Plain-English Summary
- Space is **finite and eternal** — it does not expand.  
- η is **pulled inward by galaxies**, leaving stretched gaps in between.  
- Light accumulates redshift by crossing these stretched gaps.  
- Chronodes = knots with fuzzy edges; their halos explain overlap physics.  
- No virtual particles, but Green kernels remain for rigor.  
- Light usually has one speed, but near extreme objects polarizations can differ slightly.  
- Locally, QCFT still looks like special relativity.

---

**Version:** Definitions v2.1  
**Date:** 2025-08-29  
**Status:** Active — all new work must adopt these fixes.
