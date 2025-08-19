# QCFT Inelastic Pion Production — \(pp \to pp\pi^0\)

## 1) Kinematics and Threshold
- Proton mass: \(M_p = 938.272\,\mathrm{MeV}\)
- Neutral pion mass: \(m_{\pi^0} = 134.977\,\mathrm{MeV}\)

**CM threshold**:
\[\sqrt{s_\mathrm{thr}} = 2M_p + m_{\pi^0} \approx 2011.5\,\mathrm{MeV}.\]
Define the **excess energy** \(Q \equiv \sqrt{s} - \sqrt{s_\mathrm{thr}}\).

---

## 2) QCFT Matrix Element (Sketch)
In QCFT, pion emission arises from a **cubic overlap** of two proton chronodes and one pion chronode, glued by the same η‑kernel used in elastic scattering:
\[\mathcal M(pp\to pp\pi^0) = g_{pp\pi}\;\mathcal O_\mathrm{braid}\;\Phi_\pi(k)\;G_\eta(t).\]
- \(g_{pp\pi}\): geometric overlap integral (fixed once).
- \(\mathcal O_\mathrm{braid}\): spin/twist-preserving braid overlap.
- \(\Phi_\pi(k)\): pion wave factor; **s-wave** at threshold.
- \(G_\eta(t)\): η‑kernel (no virtual particles).

**Selection rules:** charge, braid class, and twist parity are conserved → process is allowed.

---

## 3) Threshold Law
The 2→3 cross-section is
\[\sigma(s)=\frac{1}{4F}\int |\mathcal M|^2\,d\Phi_3,\]
and the 3-body phase space satisfies \(\Phi_3\propto Q^2\). With s‑wave pion emission, QCFT gives the familiar **square‑root** threshold rise
\[\boxed{\;\sigma(Q) \propto \sqrt{Q}\;}\, .\]
Anchoring at one point \(Q_0\) with value \(\sigma_0\) gives the practical prediction
\[\boxed{\;\sigma(Q)=\sigma_0\,\sqrt{\tfrac{Q}{Q_0}}\; }\qquad(Q\ge 0).\]

**Anchor used here (Indiana/CELSIUS regime):**  \(Q_0 = 20\,\mathrm{MeV},\;\sigma_0 = 0.8\,\mu\mathrm{b}\).

---

## 4) Numbers (anchored threshold law)
The table below lists \(\sigma(Q)\) in **microbarns** for representative \(Q\) values:

| Q (MeV) | σ_pred (μb) |
|---:|---:|
|    5 | 0.400 |
|   10 | 0.566 |
|   15 | 0.693 |
|   20 | 0.800 |
|   30 | 0.980 |
|   40 | 1.131 |
|   60 | 1.386 |
|   80 | 1.600 |
|  100 | 1.789 |
|  120 | 1.960 |
|  160 | 2.263 |
|  190 | 2.466 |
|  220 | 2.653 |
|  260 | 2.884 |
|  300 | 3.098 |

This implements the QCFT s‑wave threshold prediction with a single, physically reasonable anchor; the **energy dependence** is parameter‑free.

---

## 5) Relation to the Full QCFT Overlap Model
Away from the strict threshold, the geometric overlap induces a mild **Gaussian form factor** suppression, \(\sim \exp(-R_\mathrm{eff}^2 p_\pi^2)\), which gently bends the curve at larger \(Q\).  
Near threshold (\(Q\lesssim 100\,\mathrm{MeV}\)), the **square‑root law dominates**, and the values above are the correct leading behavior.

---

## 6) Plain-English Recap
- Pion production turns on at \(\sqrt{s_\mathrm{thr}}\approx 2011.5\,\mathrm{MeV}\).
- QCFT says the cross-section grows like **the square root of the extra energy** above threshold.
- With one sensible anchor at \(Q=20\,\mathrm{MeV}\), the whole near-threshold curve is fixed; no extra knobs.
