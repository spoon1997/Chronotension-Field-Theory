#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QCFT Cann Shell — Toy Model & Observables
-----------------------------------------
- Emergent metric:  ds^2 = -(dt^2)/η(r)^2 + η(r)^2 (dr^2 + r^2 dΩ^2)
- Light impact parameter: b^2(r) = η(r)^4 * r^2
- External matching: choose η_out so b^2 reproduces GR outside
  -> η_out(r) = (1 - r_s/r)^(-1/4)  (gives GR photon ring at r_ph = 1.5 r_s)
- Cann Shell: finite wall at r_cann = κ r_s with smooth thickness σ; cap η inside

Outputs
- Figures: eta_profile.png, gradia_abs.png, tidal_proxy.png, impact_b2.png
- Optional CSV (with --scan): params_scan.csv (echo delays vs κ,σ)
"""

from __future__ import annotations
import argparse
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- Physical constants (SI) for time scaling ---
G   = 6.67430e-11
c   = 299792458.0
Msun= 1.98847e30

def time_unit_seconds(M_Msun: float) -> float:
    """Characteristic time unit r_s/c, where r_s = 2GM/c^2."""
    rs_m = 2.0 * G * (M_Msun * Msun) / (c**2)
    return rs_m / c

# --- External η chosen to match GR photon ring ---
def eta_out_raw(r: np.ndarray, rs: float = 1.0) -> np.ndarray:
    """External η profile such that b^2 matches GR outside."""
    return (1.0 - rs / r) ** (-0.25)

def smooth_step(x: np.ndarray, width: float) -> np.ndarray:
    """0→1 smooth step via tanh."""
    return 0.5 * (1.0 + np.tanh(x / width))

@dataclass
class Profile:
    r:        np.ndarray
    eta:      np.ndarray
    r_cann:   float
    rs:       float

def build_profile(
    rs: float = 1.0,
    kappa: float = 1.05,
    sigma: float = 0.05,
    rmax: float = 5.0,
    N: int = 4000
) -> Profile:
    """
    Build η(r) with:
      - GR-matched η_out outside
      - finite cap at r_cann = kappa*rs inside (Cann Shell)
      - smooth join over thickness sigma
    """
    r_cann = kappa * rs
    rmin = max(0.9 * rs, r_cann - 0.1 * rs)   # start near shell; plotting convenience
    r = np.linspace(rmin, rmax * rs, N)

    # Safe evaluation (avoid using η_out below r_cann)
    r_safe = np.maximum(r, r_cann + 1e-9)
    eta_out = eta_out_raw(r_safe, rs=rs)
    eta_cap = eta_out_raw(np.array([r_cann]), rs=rs)[0]

    s = smooth_step(r - r_cann, sigma * rs)
    eta = s * eta_out + (1.0 - s) * eta_cap
    return Profile(r=r, eta=eta, r_cann=r_cann, rs=rs)

def photon_sphere(profile: Profile) -> tuple[float, float, np.ndarray]:
    """
    Photon ring for this metric is given by the MINIMUM of b^2(r) = η^4 r^2.
    Returns: (r_ph/rs, bcrit/rs, b2_profile)
    """
    r, eta, rs = profile.r, profile.eta, profile.rs
    b2 = (eta**4) * (r**2)
    idx = np.argmin(b2)
    r_ph = r[idx] / rs
    bcrit = np.sqrt(b2[idx]) / rs
    return r_ph, bcrit, b2

def echo_delay_dimless(profile: Profile, r_ph_over_rs: float) -> float:
    """
    Echo spacing (WKB proxy): Δt ≈ 2 ∫_{r_cann}^{r_ph} η(r) dr.
    Returns a dimensionless value in units of (r_s/c) if rs=1; multiply by time_unit_seconds(M).
    """
    r, eta, rs, r_cann = profile.r, profile.eta, profile.rs, profile.r_cann
    r_ph = r_ph_over_rs * rs
    mask = (r >= r_cann) & (r <= r_ph)
    if not np.any(mask):
        return 0.0
    return 2.0 * np.trapz(eta[mask], r[mask])

# --- Plot helpers (each chart on its own, no fixed colors per instructions) ---
def plot_eta(profile: Profile, r_ph_over_rs: float, outpath: str) -> None:
    r, eta, rs = profile.r, profile.eta, profile.rs
    plt.figure(figsize=(7, 4.2))
    plt.plot(r/rs, eta, linewidth=2)
    plt.axvline(profile.r_cann/rs, linestyle='--')
    plt.axvline(r_ph_over_rs, linestyle=':')
    plt.title("η(r): GR-matched outside, finite Cann Shell at r_cann")
    plt.xlabel("r / r_s"); plt.ylabel("η(r)")
    plt.tight_layout(); plt.savefig(outpath); plt.close()

def plot_gradia(profile: Profile, outpath: str) -> None:
    r, eta, rs = profile.r, profile.eta, profile.rs
    dr = r[1] - r[0]
    deta = np.gradient(eta, dr)
    plt.figure(figsize=(7, 4.2))
    plt.plot(r/rs, np.abs(deta), linewidth=2)
    plt.axvline(profile.r_cann/rs, linestyle='--')
    plt.title("|dη/dr|: Gradia peaks near the shell flanks")
    plt.xlabel("r / r_s"); plt.ylabel("|dη/dr|")
    plt.tight_layout(); plt.savefig(outpath); plt.close()

def plot_tidal_proxy(profile: Profile, outpath: str) -> None:
    r, eta, rs = profile.r, profile.eta, profile.rs
    dr = r[1] - r[0]
    deta = np.gradient(eta, dr)
    d2eta = np.gradient(deta, dr)
    plt.figure(figsize=(7, 4.2))
    plt.plot(r/rs, d2eta, linewidth=2)
    plt.axhline(0.0, linestyle='--')
    plt.axvline(profile.r_cann/rs, linestyle='--')
    plt.title("d²η/dr²: finite near the shell (tidal proxy)")
    plt.xlabel("r / r_s"); plt.ylabel("d²η/dr²")
    plt.tight_layout(); plt.savefig(outpath); plt.close()

def plot_b2(profile: Profile, b2: np.ndarray, r_ph_over_rs: float, outpath: str) -> None:
    r, rs = profile.r, profile.rs
    plt.figure(figsize=(7, 4.2))
    plt.plot(r/rs, b2/(rs**2), linewidth=2, label="QCFT b²(r)")
    plt.axvline(r_ph_over_rs, linestyle='--', label="r_ph (QCFT)")
    plt.axvline(1.5, linestyle=':', label="r_ph (GR)")
    plt.title("Impact parameter profile b²(r) (min → photon ring)")
    plt.xlabel("r / r_s"); plt.ylabel("b² / r_s²")
    plt.legend(); plt.tight_layout(); plt.savefig(outpath); plt.close()

# --- CLI ---
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="QCFT Cann Shell — toy model & observables")
    p.add_argument("--kappa", type=float, default=1.05, help="Cann Shell radius factor r_cann = kappa * r_s")
    p.add_argument("--sigma", type=float, default=0.05, help="Shell thickness (in units of r_s)")
    p.add_argument("--rmax",  type=float, default=5.0,  help="Maximum radius for plots (in units of r_s)")
    p.add_argument("--N",     type=int,   default=4000, help="Radial samples")
    p.add_argument("--scan",  action="store_true",      help="Write params_scan.csv across κ in {1.02,1.05,1.10,1.20} and σ in {0.02,0.05,0.10}")
    p.add_argument("--sgraM", type=float, default=4.0e6,help="Mass (Msun) for Sgr A* time scaling")
    p.add_argument("--stelM", type=float, default=10.0, help="Mass (Msun) for stellar BH time scaling")
    return p.parse_args()

def main() -> None:
    args = parse_args()
    os.makedirs("figures", exist_ok=True)

    # Build profile and compute key quantities
    prof = build_profile(rs=1.0, kappa=args.kappa, sigma=args.sigma, rmax=args.rmax, N=args.N)
    r_ph_over_rs, bcrit_over_rs, b2 = photon_sphere(prof)

    # Echo spacing (dimensionless), scale to seconds
    Dt_dimless = echo_delay_dimless(prof, r_ph_over_rs)
    Dt_sgra_s  = Dt_dimless * time_unit_seconds(args.sgraM)
    Dt_stel_ms = Dt_dimless * time_unit_seconds(args.stelM) * 1e3

    # Print summary
    bcrit_GR = np.sqrt((1.5**2) / (1.0 - 1.0/1.5))
    print("=== QCFT Cann Shell — Baseline ===")
    print(f"kappa = {args.kappa:.4f}, sigma = {args.sigma:.4f} r_s")
    print(f"r_cann / r_s     = {prof.r_cann/prof.rs:.4f}")
    print(f"r_ph (QCFT)/r_s  = {r_ph_over_rs:.6f}   |   r_ph (GR)/r_s = 1.500000")
    print(f"b_crit (QCFT)/r_s= {bcrit_over_rs:.6f}   |   b_crit (GR)/r_s= {bcrit_GR:.6f}")
    print(f"Echo spacing (Sgr A*, {args.sgraM:.2e} Msun): {Dt_sgra_s:.2f} s")
    print(f"Echo spacing (stellar {args.stelM:.1f} Msun): {Dt_stel_ms:.3f} ms")

    # Plots
    plot_eta(prof, r_ph_over_rs, "figures/eta_profile.png")
    plot_gradia(prof, "figures/gradia_abs.png")
    plot_tidal_proxy(prof, "figures/tidal_proxy.png")
    plot_b2(prof, b2, r_ph_over_rs, "figures/impact_b2.png")
    print("Figures written to ./figures")

    # Optional parameter scan
    if args.scan:
        kappas = [1.02, 1.05, 1.10, 1.20]
        sigmas  = [0.02, 0.05, 0.10]
        rows = []
        for sg in sigmas:
            for kp in kappas:
                P = build_profile(rs=1.0, kappa=kp, sigma=sg, rmax=args.rmax, N=args.N)
                rph, bcrit, _b2 = photon_sphere(P)
                Dt = echo_delay_dimless(P, rph)
                rows.append({
                    "kappa": kp,
                    "sigma_r_s": sg,
                    "r_ph_over_r_s": rph,
                    "bcrit_over_r_s": bcrit,
                    "Delta_t_echo_dimless": Dt,
                    "Delta_t_echo_SgrA_seconds": Dt * time_unit_seconds(args.sgraM),
                    "Delta_t_echo_10Msun_ms":   Dt * time_unit_seconds(args.stelM) * 1e3
                })
        df = pd.DataFrame(rows)
        df.to_csv("params_scan.csv", index=False)
        print("params_scan.csv written.")

if __name__ == "__main__":
    main()
