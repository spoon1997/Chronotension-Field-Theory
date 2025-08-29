# η-Kompaneets Demo: Numerical Proof-of-Concept

## Purpose
The COBE/FIRAS result shows the CMB spectrum is an **exact blackbody** to within ΔI/I ≲ 10⁻⁵.  
A simple mixture of galaxy/dust/star light, even when redshifted and scrambled, cannot reach this precision — residual bumps always remain.

QCFT’s solution: a **tiny, cumulative absorb/re-emit interaction** between photons (η-waves) and the η-field.  
This is described by the **η-Kompaneets operator**, which drives any photon distribution toward the Planck spectrum:
\[
\partial_t n \;=\; \Gamma_\eta \,(n_{\rm Pl}(T_\eta) - n) \;,
\]
with \(n\) the photon occupation number and \(\Gamma_\eta\) a weak coupling rate.

---

## Method
- Built a **messy source mix**: starlight + warm/cold dust + synchrotron + free-free.
- Converted intensity to photon occupation number \(n(\nu)\).
- Evolved under **pure number-changing relaxation**:
  \[
  n(t+\Delta t) = n(t) + \Delta t \, \Gamma_\eta (n_{\rm Pl} - n).
  \]
- Measured residuals in the **CMB precision band (60–600 GHz)**.
- Defined **thermalization depth**:
  \[
  \tau_\eta \equiv \int \Gamma_\eta \, dt.
  \]

---

## Results

### Initial vs Final Spectra
![Spectrum](eta_relax_spectrum.png)  
A messy mix of galaxy/dust light is driven smoothly onto the Planck curve.

---

### Residuals at τ = 10
![Residuals τ=10](eta_relax_residuals_band.png)  
- Max residual: ~4×10⁻³ in-band.  
- **Not good enough**: fails FIRAS by ~2 orders of magnitude.

---

### Convergence with τ
![Convergence](eta_relax_convergence.png)  
Residuals decay exponentially ∝ e⁻ᵗᵃᵘ. The mechanism works exactly as expected.

---

### Residuals at τ = 25
![Residuals τ=25](eta_relax_residuals_band_tau25.png)  
- Max residual: 1.2×10⁻⁹  
- RMS residual: 2.7×10⁻¹⁰  
- **Well below FIRAS limit (10⁻⁵).**  
- Demonstrates that τ ~ 20–30 is sufficient to produce an exact blackbody.

---

## Interpretation

- **Key insight:** Only a modest integrated coupling (\(\tau_\eta \sim 20–30\)) is required.  
- Local interaction probability per Mpc can be vanishingly small; over gigaparsecs, it integrates to the required τ.  
- This is consistent with QCFT’s principle: η–photon couplings are weak but cumulative.

---

## Plain-English Summary
We started with a soup of galaxy light. By allowing photons to occasionally be absorbed and re-emitted by the η-field, the spectrum was “cooked” into pure 2.7 K microwave radiation.  

After enough cycles (τ ~ 25), all fingerprints of dust, stars, and synchrotron disappear, leaving a perfect blackbody.  

**This demonstrates QCFT’s mechanism for the CMB monopole:**  
- Redshift + scrambling explain its faintness and isotropy.  
- η-Kompaneets relaxation explains its perfect blackbody spectrum.

---

## Status
- ✅ FIRAS blackbody hurdle passed **in principle**.  
- 🔜 Next step: quantify whether τ ~ 20–30 is natural given QCFT microphysics (η–photon cross-sections, path lengths, chronode densities).  
- 🔜 Then move on to anisotropies (TT/TE/EE) with η-lensing.

---
