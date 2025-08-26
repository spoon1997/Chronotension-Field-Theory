# QCFT Lensing Anisotropy Test (Along the CMB Hot–Cold Axis)

## 1. Hypothesis (QCFT)
- **Hot CMB lobes ≡ lower background η → stronger Gradia → *slightly stronger weak lensing*.**  
- **Cold CMB lobes ≡ higher background η → weaker Gradia → *slightly weaker weak lensing*.**

**Prediction:**  
\[
S_8^{\rm hot} > S_8^{\rm cold} \quad \text{and/or} \quad A_\kappa^{\rm hot} > A_\kappa^{\rm cold}
\]
where \(S_8 \equiv \sigma_8(\Omega_m/0.3)^{0.5}\) and \(A_\kappa\) is a shear amplitude parameter.

---

## 2. Datasets
- **Weak lensing**: DES Y3/Y6, KiDS-1000, HSC-PDR3 (and later Euclid).  
- **CMB map**: Planck SMICA/Commander temperature maps (low-ℓ cleaned).

---

## 3. Axis definition & sky split
- Extract the **hot–cold axis** from Planck low-ℓ maps (ℓ=2–3) or adopt literature values (within ±10°).  
- Split the sky into two hemispheres (“hot” vs “cold”) by the great circle perpendicular to this axis.  
- Apply the split within each survey’s footprint.

---

## 4. Measurement pipelines
**A. Configuration space (2pt correlations):**
- Compute tomographic \(\xi_+(\theta), \xi_-(\theta)\) in **hot** and **cold** hemispheres.  
- Fit ΛCDM shear models with independent amplitude parameters: \(S_8^{\rm hot}, S_8^{\rm cold}\).  
- Report \(\Delta S_8 = S_8^{\rm hot} - S_8^{\rm cold}\).

**B. Harmonic space (pseudo-\(C_\ell\)):**
- Build E/B-mode power spectra per hemisphere.  
- Fit amplitude \(A_E\).  
- Verify B-modes ≈ 0 in both hemispheres.

**Complementary:** galaxy–galaxy lensing and cluster lensing stacks by hemisphere.

---

## 5. Tomography & scales
- Use each survey’s tomographic bins.  
- Apply standard cosmic shear scale cuts (e.g., DES Y3).  
- Inspect large angular scales explicitly (effect may be broad/low-ℓ).

---

## 6. Systematics controls
- **Footprint & depth:** match depth/seeing/stars across hemispheres; use footprint-aware mocks.  
- **PSF & calibration:** check shear biases per hemisphere.  
- **Dust/extinction:** include templates; mask high-extinction zones.  
- **Photo-z:** test with alternative \(n(z)\); widen priors; check stability.  
- **Axis choice:** rotate split axis ±10–20°; effect should peak at the true CMB axis.

---

## 7. Null tests & significance
- **Random-axis nulls:** repeat with ≈500 random splits; build distribution of \(\Delta S_8\).  
- **Flip test:** swap hot/cold labels → no change.  
- **Jackknife by tiles:** ensure no single patch drives result.  
- **Injection test:** add synthetic 1–2% asymmetry to mocks; verify recovery.

---

## 8. Cross-correlation bonus
- Compute **cross-power \(C_{\ell}^{\kappa T}\)** between shear-based κ maps and CMB temperature (ℓ≲30).  
- QCFT expects a **positive correlation** (more lensing in hotter regions), distinct from ΛCDM’s ISW effect.

---

## 9. Effect size & detectability
- Current \(\sigma(S_8) \sim 0.02{-}0.04\) (full footprint).  
- Splitting sky doubles error (~√2).  
- A **1–2% asymmetry** may be detectable by combining DES+KiDS+HSC or with Euclid early data.  

---

## 10. Reporting
- Primary result: \(\Delta S_8\) (or \(\Delta A_E\)) with error, plus p-value from random-axis nulls.  
- Show robustness vs. photo-z, scale cuts, PSF/seeing, and axis rotations.  
- Provide hot/cold footprint maps and E/B spectra.  
- If signal found: give Bayes factor for QCFT η-gradient vs isotropic ΛCDM.

---

## Expected outcomes
- **QCFT confirmation:** \(S_8^{\rm hot} > S_8^{\rm cold}\), ≥2–3σ, robust to systematics, peaking at the real CMB axis.  
- **ΛCDM null:** no preferred-axis difference; hemispheres consistent within noise.

---

## Stretch goals
- Repeat with **CMB lensing κ** (Planck/ACT/SPT) along same axis.  
- Extend to **BAO amplitude** and **SN Ia Hubble residuals** split by the axis, checking for consistent asymmetry.

---

## Plain English Summary
Split the weak-lensing sky along the CMB’s hot–cold axis and ask:  
**Is lensing stronger in the hot side?**  

- **QCFT says yes** (lower η there → stronger bending).  
- **ΛCDM says no** (universe is isotropic).  

It’s a simple, falsifiable test using existing survey data. Even a tiny hemispheric difference would shake ΛCDM’s foundations.
