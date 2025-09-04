# Cann Shell Scaling Laws — Chronodes and Black Holes

**Author:** Luke Cann — Independent Theoretical Physicist and Founder of QCFT  
**Date:** Sept 2025  

---

## 1. Why a Scaling Law?

In QCFT, **chronodes and black holes are the same species**: solitons of the η-field stabilized by Gradia tension and η² conservation.  
The difference is scale. To unify their description, we need **dimensionless, η-aware scaling laws** that apply to both.

---

## 2. The Three Radii (Which Size Do We Mean?)

In QCFT’s emergent metric  
\[
ds^2 = -\frac{dt^2}{\eta^2} + \eta^2 dx^2,
\]  
the notion of “radius” depends on how you measure:

1. **Coordinate radius** \(r\): convenient for math, but not invariant.  
2. **Proper radius**:  
   \[
   R_{\rm prop}(r) = \int_0^r \eta(\tilde r)\,d\tilde r,
   \]  
   what you measure with rods/clocks.  
3. **Optical radius** (impact parameter for photons):  
   \[
   b^2(r) = \eta^4(r)\,r^2,\quad b_{\rm crit}\text{ at photon sphere.}
   \]  

**Universal scaling must be expressed in proper or optical terms.**

---

## 3. Two Universal Knobs

Define:

- **Contrast:**  
  \[
  \chi \equiv \frac{\eta_{\max}}{\eta_\infty} \geq 1
  \]  
  Peak η at the Cann Shell vs far-field value.  

- **Location:**  
  \[
  \kappa \equiv \frac{r_{\rm Cann}}{r_s}
  \]  
  Shell radius vs Schwarzschild radius (GR reference).

---

## 4. Universal χ–κ Law (U1)

Matching GR lensing outside the shell gives:

\[
\boxed{\;\kappa(\chi) = \frac{1}{1-\chi^{-4}} \;}
\]

Examples:
- \(\chi=1.5 \Rightarrow \kappa=1.245\)  
- \(\chi=2.0 \Rightarrow \kappa=1.067\)  
- \(\chi=2.7 \Rightarrow \kappa=1.019\)  

This is **mass-independent**. The same \(\chi\) gives the same \(\kappa\) for an electron chronode or a supermassive black hole.

---

## 5. Echo-Gap Scaling (U2)

The echo cavity (gap between Cann Shell and photon sphere):

\[
\Delta t_{\rm echo} \approx 2 \int_{r_{\rm Cann}}^{r_{\rm ph}} \eta(r)\,dr
\;\approx\; 2 \,\bar\eta_{\rm gap}\,(r_{\rm ph}-r_{\rm Cann}),
\]

with \(r_{\rm ph} \approx 1.5\,r_s\).  

Normalize by \(r_s/c\) for a dimensionless observable:

\[
\boxed{\;\tilde\Delta t \equiv \frac{\Delta t_{\rm echo}}{r_s/c}
\;\approx\; 2\,\bar\eta_{\rm gap}\,(1.5-\kappa) \;}
\]

Interpretation: **Echo spacing** tells you how wide and “thick” the gap is in η-time units. The only mass dependence is the trivial factor \(r_s/c\).

---

## 6. Chronode vs Black Hole Regimes (U3)

From soliton/Q-ball theory:

### (a) Thick-wall regime (small chronodes, \(\omega\to m^{-}\))
\[
R_{\rm prop}/\lambda_\eta \sim \frac{c_R}{\sqrt{\varepsilon}}, \quad 
\chi-1 \sim c_A \sqrt{\varepsilon}, \quad 
\lambda_\eta = 1/m, \quad \varepsilon = 1-\omega^2/m^2.
\]

So:
\[
\boxed{\;(\chi-1)\,(R_{\rm prop}/\lambda_\eta) \approx \text{const} \;}
\]

### (b) Thin-wall regime (large BHs, large charge Q)
\[
R_{\rm prop}/\lambda_\eta \propto Q^{1/3}, \qquad \chi \to \chi_{\rm sat}.
\]

So:
\[
\boxed{\;R_{\rm prop} \propto Q^{1/3},\;\; \chi \approx \text{constant}\;}
\]

**Together:** Small chronodes trade contrast for radius (U3a). Large BHs grow with \(Q^{1/3}\) at constant contrast (U3b).

---

## 7. Numbers You Can Use

- **χ–κ mapping (U1):**
  - \(\chi=1.5 \Rightarrow \kappa=1.245\)  
  - \(\chi=2.0 \Rightarrow \kappa=1.067\)  
  - \(\chi=2.7 \Rightarrow \kappa=1.019\)

- **Echo gap (U2):**  
  For \(\chi=2.0\), \(\kappa=1.067\), \(\bar\eta_{\rm gap}\approx 2\):  
  \(\tilde\Delta t \approx 1.73\).  
  → Sgr A* (\(r_s/c\sim 40\) s) → \(\Delta t_{\rm echo}\sim 69\) s.  
  → \(10 M_\odot\) BH (\(r_s/c\sim 10^{-4}\) s) → \(\Delta t_{\rm echo}\sim 0.17\) ms.  

- **Chronode example (U3a):**  
  From a solved lump: \(R_{\rm prop}\sim 11\), \(\chi\sim 1.75\), \(\varepsilon\sim 0.19\).  
  Gives \((\chi-1)R_{\rm prop} \sim 8\), constant across small solitons.

---

## 8. Plain-English Summary

- **Universal χ–κ law:** The Cann Shell sits just inside the GR horizon by an amount set only by η-contrast.  
- **Echo-gap law:** Echo spacings scale with \(r_s/c\), modulated by η in the gap.  
- **Chronode–BH continuum:** Small chronodes obey a contrast–radius tradeoff, big BHs grow as \(Q^{1/3}\) with constant contrast.  

**Bottom line:** Chronodes and black holes lie on the *same soliton family curve*. Their “sizes” differ only in η scaling, not in kind. This is QCFT’s unification of microphysics and astrophysics.
