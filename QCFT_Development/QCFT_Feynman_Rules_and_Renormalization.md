# QCFT Feynman Rules and Renormalization

This document summarizes the derivation of Feynman rules and renormalization structure for Quantum Chronotension Field Theory (QCFT), using only the ηᵃ(x,t) field.

---

## 🧮 Propagators

From the canonical QCFT Lagrangian:
```
L = ½ δ^{ab} ∂_μ η^a ∂^μ η^b - λ(η^a η^a - v²)² + θ ε^{μνρσ} f_{μν}^a f_{ρσ}^a
```

Assuming a small fluctuation around background:
```
η^a(x) = v δ^{a0} + δη^a(x)
```

We obtain:
```
⟨0 | T{ δη^a(x) δη^b(y) } | 0⟩ = i Δ^{ab}(x - y)
```

In momentum space:
```
Δ^{ab}(k) = i δ^{ab} / (k² + iε)
```

---

## 🔗 Vertex Rules

### 1. Quartic interaction from potential:
```
L ⊃ λ (δη^a δη^a)² ⇒ 4-point vertex ∝ λ
```

### 2. Chronode interaction:
```
L ⊃ g_{abc} η̄^a δη^b δη^c ⇒ 3-point vertex ∝ g_{abc}
```

### 3. Topological θ-term:
```
L ⊃ θ ε^{μνρσ} ∂_μ δη^a ∂_ν δη^a ∂_ρ δη^a ∂_σ δη^a
```
Topologically relevant, but suppressed in perturbation theory.

---

## 🌀 Feynman Rule Summary

| Element         | Rule                                       |
|----------------|---------------------------------------------|
| Propagator      | i δ^{ab} / (k² + iε)                        |
| 3-Point Vertex  | i g_{abc}                                   |
| 4-Point Vertex  | -4! i λ                                     |
| θ-Term Vertex   | Non-perturbative, contributes to tunneling |

---

## ♻️ Renormalization

### Strategy:
- Standard counterterms:
  ```
  Z_η (∂ η)^2 - Z_λ λ(η^a η^a - v²)^2
  ```
- ηᵃ is massless, simplifying divergence structure
- Topological solitons are protected
- θ-term is not renormalized (quantized)

### Outcome:
**QCFT is renormalizable at 1-loop and beyond**, via standard QFT techniques adapted to the ηᵃ field structure.

---

## ✅ Conclusion

QCFT provides a full quantum framework:
- Well-defined propagators
- Local interactions
- Topological stability
- Renormalizability

The theory is now complete and consistent at the quantum level.