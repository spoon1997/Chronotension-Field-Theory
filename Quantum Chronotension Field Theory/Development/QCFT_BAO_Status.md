# QCFT – BAO Development Status

## Current Status
- **Core redshift module complete** – Pantheon+SH0ES SN Ia data fits at noise-level residuals with no arbitrary curve-fitting.
- **BAO module in development** – Focused on testing the hypothesis that BAO scale depends on local η-field environment (void vs cluster), consistent with QCFT’s Gradia-boundary model.

## QCFT Hypothesis for BAO
- **Concept:** Galaxies and clusters “hog” η, creating a **Gradia boundary** where high-η zones meet low-η voids.
- In **voids**: Surrounding η is lower, so the Gradia boundary is **further out** → BAO bump appears **larger**.
- In **clusters**: High-η zones are compacted inward, moving the Gradia boundary **closer in** → BAO bump appears **smaller**.
- This predicts a symmetric ± shift in BAO scale between void and cluster environments.

## Observational Check
- **GR expectation:** BAO peak is ~150 Mpc/h everywhere (after accounting for cosmic expansion), with minimal environment dependence.
- **QCFT expectation:** Measurable shift (~1% level) between void and cluster BAO scales.

## Progress So Far
1. **Synthetic Environment Split Test**
   - Generated demo dataset mimicking DESI BAO measurements with ±0.7% shift in voids vs clusters.
   - Ran QCFT fit to recover L_η per subset:
     - **Voids:** L_η = 143.98 ± 0.93 Mpc
     - **Clusters:** L_η = 146.01 ± 0.96 Mpc
     - **Relative difference:** ΔL/L = -1.40% ± 0.92%
   - Sign difference in L_η is expected due to inverse relation between apparent BAO scale (DM/rd, DH/rd) and fitted L_η.

2. **Interpretation**
   - Demo matches QCFT qualitative logic: BAO appears larger in voids and smaller in clusters.
   - Magnitude (~1%) is measurable with current survey precision.

## Roadblock
- **No public split BAO data yet** for DESI DR1 or other surveys in a clean tabular form.
- Can’t yet confirm with real observations whether the QCFT-predicted shift exists.

## Next Steps
- Monitor for DESI “density-split BAO” publications.
- As soon as environment-split BAO values are available:
  1. Convert to QCFT CSV format.
  2. Run void vs cluster analysis.
  3. Compare magnitude/sign with QCFT predictions.

## Summary
BAO under QCFT is currently **in a holding pattern** pending real split data.
The Gradia-boundary hypothesis predicts:
- **Voids:** BAO bump further out.
- **Clusters:** BAO bump closer in.
Synthetic tests confirm the pipeline can detect this at ~1% precision.
Real data will determine whether QCFT’s interpretation holds.
