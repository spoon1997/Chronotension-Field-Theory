# QCFT Redshift Equation (Current Locked-In Form)

This document summarises the currently locked-in QCFT redshift equation and its context within the theory.

---

## **Equation**
The redshift in QCFT is currently expressed as:

\[
z_{QCFT} = (1 + z_{GR})^{p} - 1
\]

where:

- **\( z_{GR} \)**: The GR/ΛCDM-derived redshift from observational data (e.g., SN1a, BAO), used as an *input* when working with datasets already reduced using GR assumptions.
- **\( p \)**: QCFT’s scaling exponent, empirically determined to lie in the range **−1.0 to −1.22** for best fits against SN1a datasets.
- **Output**: The QCFT-predicted redshift after correcting for η-field effects.

---

## **Purpose of z_GR in the Formula**
Most cosmological datasets are pre-processed assuming General Relativity (GR) or ΛCDM. Distances, magnitudes, and times are often *derived quantities* based on those assumptions.  
Therefore:

- Directly applying QCFT to raw data is not possible without back-converting these values.
- \( z_{GR} \) acts as the bridge between existing datasets and QCFT predictions.

Once *raw, assumption-free observational data* becomes available, \( z_{GR} \) can be replaced with direct observational quantities, making QCFT independent of GR.

---

## **Why This Form Works**
- **Scalability**: The exponent \( p \) can encode different cosmological sectors or epochs.
- **Compatibility**: By starting with \( z_{GR} \), the equation can be applied directly to legacy datasets without having to reprocess every observation.
- **Transition to Pure QCFT**: When fully assumption-free datasets are used, \( z_{GR} \) drops out and QCFT parameters can be applied directly to measured quantities.

---

## **Current Parameter Values**
- **p**: ~ −1.15 (range −1.0 to −1.22 depending on dataset and fitting method)
- **R***: Derived separately; relates to the rate of η-field unfurling in previous models.

---

## **Next Steps**
1. Continue refining \( p \) using BAO and CMB datasets.
2. Seek or reconstruct assumption-free SN1a and BAO datasets to remove \( z_{GR} \) from the formula entirely.
3. Investigate sector-dependent \( p \) values for anisotropic or Gradia-affected regions.

---

**Note:** This form is a *transitional* version of the QCFT redshift model, designed for maximum compatibility with current data reduction methods.
