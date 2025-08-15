# QCFT Redshift Drift (p-only)

**Locked model:** \( H_\eta(z) = H_{\eta 0} (1+z)^p \), with **p = -1.15** (SN Ia).  
**Prediction:** for a comoving source observed at redshift \(z\), the QCFT redshift drift (Sandage–Loeb signal) is
\[
\dot z(z) \,=\, (1+z)\,H_{\eta0} \, - \, H_{\eta0} (1+z)^p \,=\, H_{\eta0}\,\big[(1+z) - (1+z)^p\big].
\]
Here we identify \(H_{\eta0}\) with a local Hubble calibration (units yr\(^{-1}\)).

**Derivation sketch (QCFT):**  
Start from \(1+z = \eta_e/\eta_0 = e^{\ln\eta_e - \ln\eta_0}\). Differentiate with respect to the observer’s proper time \(t_0\):  
\[
\frac{\dot z}{1+z} = \frac{d\ln\eta_e}{dt_0} - \frac{d\ln\eta_0}{dt_0},\quad
\frac{dt_e}{dt_0} = \frac{1}{1+z}\Rightarrow \frac{d\ln\eta_e}{dt_0} = \frac{1}{1+z}\Big(\frac{d\ln\eta}{dt}\Big)_e.
\]
Defining \(H_{\eta} \equiv -\,\frac{d\ln\eta}{dt}\) (so \(H_{\eta0}>0\)), one obtains the QCFT analogue of Sandage–Loeb:
\[
\dot z = (1+z)\,H_{\eta0} - H_{\eta}(z).
\]
With the locked late-time form \(H_{\eta}(z)=H_{\eta0}(1+z)^p\), the expression above follows immediately.

---

## Numerical predictions (per year)
Values below are in **yr⁻¹**. To compare with the usual cosmology literature, multiply by \(10^{10}\) to get units of \(10^{-10}\,\text{yr}^{-1}\).

| H₀ [km/s/Mpc] | z | ẋ = dz/dt [yr⁻¹] | ẋ × 1e10 [10⁻¹⁰/yr] |
|---:|---:|---:|---:|

| 67.4 | 0.1 | 1.404903e-11 | 0.140 |
| 67.4 | 0.5 | 6.015394e-11 | 0.602 |
| 67.4 | 1.0 | 1.067996e-10 | 1.068 |
| 67.4 | 2.0 | 1.873063e-10 | 1.873 |
| 70.0 | 0.1 | 1.459098e-11 | 0.146 |
| 70.0 | 0.5 | 6.247442e-11 | 0.625 |
| 70.0 | 1.0 | 1.109195e-10 | 1.109 |
| 70.0 | 2.0 | 1.945318e-10 | 1.945 |
| 73.0 | 0.1 | 1.521630e-11 | 0.152 |
| 73.0 | 0.5 | 6.515189e-11 | 0.652 |
| 73.0 | 1.0 | 1.156732e-10 | 1.157 |
| 73.0 | 2.0 | 2.028689e-10 | 2.029 |
---

### Notes
- This is the **QCFT late-time** prediction using the locked \(p=-1.15\). For other \(p\), replace \(p\) in \(\dot z(z)\) and recompute.
- At low redshift, \(\dot z \approx H_{\eta0}\,z\) (since \((1+z)^p \approx 1 + p z\)), giving the expected linear rise.
- The sign and amplitude differ from ΛCDM’s \(\dot z = H_0(1+z) - H(z)\) when \(H_{\eta}(z) \neq H(z)\). A detection at \(z\sim 1\)–2 would cleanly discriminate.
- Convert to spectroscopic velocity drift via \(\dot v \approx c\,\dot z/(1+z)\) if needed.

