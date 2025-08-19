# QCFT Elastic Proton–Proton Scattering (Formal Write‑Up)
**Channel:** $p p \to p p$ (elastic, small angles).  
**Framework:** Chronode braids + η‑kernel, no virtual particles; unitarized via an impact‑parameter eikonal.

---
## 1. Kinematics & Conventions
- Mandelstam invariants: $s=(p_1+p_2)^2$, $t=(p_1-p_3)^2\simeq-\mathbf q^2$ (small angle).
- CM momenta: $p_i = \tfrac{\sqrt{\lambda(s,m_p^2,m_p^2)}}{2\sqrt{s}}$, $\;\lambda$ is the Källén function.
- Differential cross‑section (2→2):  
$$\frac{d\sigma}{dt} = \frac{1}{16\pi s^2}\,|\mathcal M(s,t)|^2.$$
- Optical theorem normalization (forward/real part small, $\rho\equiv \Re/\Im\approx 0$):  
$$\left.\frac{d\sigma}{dt}\right|_{t=0}=\frac{\sigma_\text{tot}^2}{16\pi}.$$

---
## 2. Proton Chronode & η‑Kernel
- **Proton**: stable **3‑braid chronode** with rms size $R_p$ set by soliton stability: $R_p=c\,\ell_\eta$, with $\ell_\eta\equiv 1/m_\eta$.
- **Transverse profile** (Gaussian ansatz consistent with the proton form factor near $t=0$):  
$F_p(t)=\exp(t R_p^2/6)$, so the 2D profile width is $R_\perp^2=R_p^2/3$.
- **η‑kernel**: for small $|t|$, a short‑range correlator with length $\ell_\eta$; equivalently in $b$‑space a Gaussian of width $\sigma_\eta^2=2\ell_\eta^2$.

> **ASCII diagram (impact‑parameter picture)**
```
   q⊥  (Fourier)                 b–space eikonal
  <----->                     Γ(b,s) = 1 - exp[ -Ω(b,s)/2 ]
 p →  ●───────↘             A(s,t) = i∫ d²b e^{iq·b} Γ(b,s)
       ⤹        ↘            with Ω(b,s) ≃ Ω₀(s)·exp( -b² / (2Σ²) )
 p →   ●─────────→ p         Σ² = 2( R_p²/3 + ℓ_η² ) ≡ B
```

---
## 3. Born Amplitude → Forward Exponential
Product in $\mathbf q$–space of two proton form factors and the η‑kernel gives, to leading order in $|t|$:
$$\mathcal A_{\rm Born}(s,t)\;\propto\;F_p(t)^2\,G_\eta(t)
= \exp\Big[t\Big(\tfrac{R_p^2}{3}+\ell_\eta^2\Big)\Big].$$
Hence
$$\frac{d\sigma}{dt}\;\propto\;|\mathcal A|^2\;=\;\exp\Big[2t\Big(\tfrac{R_p^2}{3}+\ell_\eta^2\Big)\Big]
= \exp\big(-B|t|\big),\qquad \boxed{\;B=2\big(\tfrac{R_p^2}{3}+\ell_\eta^2\big)\;}.$$

---
## 4. Eikonal Unitarization (Impact Parameter)
Define the profile and amplitude
$$\Gamma(b,s)=1-e^{-\Omega(b,s)/2+i\chi(b,s)},\qquad \mathcal A(s,t)=i\int d^2b\,e^{i\mathbf q\cdot\mathbf b}\,\Gamma(b,s).$$
For a **Gaussian eikonal** with negligible real part ($\chi\approx 0$):
$$\Omega(b,s)=\Omega_0(s)\,e^{-b^2/(2\Sigma^2)},\qquad \Sigma^2\equiv B.$$
Total and elastic cross‑sections reduce to **1D integrals** (set $u\equiv e^{-b^2/(2\Sigma^2)}\in(0,1]$):
$$\sigma_\text{tot}(s)=4\pi\Sigma^2\int_0^1 \frac{du}{u}\Big[1-e^{-\Omega_0(s)\,u/2}\Big],$$
$$\sigma_\text{el}(s)=2\pi\Sigma^2\int_0^1 \frac{du}{u}\Big[1-e^{-\Omega_0(s)\,u/2}\Big]^2.$$
The **forward slope** remains $B=\Sigma^2$; the optical point normalization is automatic.

---
## 5. Consequences & Useful Formulas
- **Optical point:** $\;\left.\tfrac{d\sigma}{dt}\right|_{t=0}=\tfrac{\sigma_\text{tot}^2(1+\rho^2)}{16\pi}\simeq\tfrac{\sigma_\text{tot}^2}{16\pi}$.
- **Elastic fraction (pure exponential):**  
$$\frac{\sigma_\text{el}}{\sigma_\text{tot}}\simeq \frac{\sigma_\text{tot}}{16\pi B}\quad\text{(with }\sigma_\text{tot}\text{ in GeV}^{-2}\text{)}.$$
- **Topological selection**: winding, braid class, twist parity all conserved → elastic channel allowed with unit topological weight.

---
## 6. Worked Example (Numbers from A3)
- Chosen forward slope: $B_\text{ref}=14.00\;\mathrm{GeV}^{-2}$; braid factor $c=3.3$.
- Derived core scales: $\ell_\eta = 1.230\;\mathrm{GeV}^{-1} = 0.243\;\mathrm{fm}$,  $R_p=c\,\ell_\eta = 4.058\;\mathrm{GeV}^{-1} = 0.801\;\mathrm{fm}$.
- **Elastic fraction** for representative total cross‑sections:

| $\sigma_\text{tot}$ (mb) | $\sigma_\text{tot}$ (GeV$^{-2}$) | $\sigma_\text{el}/\sigma_\text{tot}$ |
|---:|---:|---:|
|  30.0 |  77.046 |  0.109 |
|  40.0 | 102.728 |  0.146 |
|  50.0 | 128.410 |  0.182 |

These values are **unitarity‑safe** (fraction $<1$) and scale as $\propto 1/B$.

---
## 7. What’s Fixed vs Derived
- **Fixed by QCFT fields:** $m_\eta \Rightarrow \ell_\eta$ (and thus $R_p=c\,\ell_\eta$ from braid torsion $c$).
- **Derived predictions:** forward slope $B=2(R_p^2/3+\ell_\eta^2)$; optical point; elastic fraction; $b$‑profile and unitarity integrals.
- **No extra knobs:** once $(c,\,\ell_\eta)$ are set (from chronode stability and one reference slope), the near‑forward elastic law is **parameter‑free**.

---
## 8. Next Step (Inelastic)
Promote one proton braid to a small excitation and couple to a pion chronode: $pp\to pp\pi^0$.  
The energy dependence follows exactly from the **3‑body phase space** and the same Gaussian overlap, with a single normalization at one point.
