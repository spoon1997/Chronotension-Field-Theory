# qball_shell.py — Stable Cann-Shell–like soliton (QCFT-inspired scalar envelope)
# Author: Luke Cann — Independent Theoretical Physicist and Founder of QCFT
#
# Usage:
#   pip install numpy matplotlib
#   python qball_shell.py
#
# Outputs:
#   eta_profile.png   (η(r) with shell peak)
#   energy_density.png
#   gradia_abs.png
#   eta_2d.png
#   Console: Q, E, E/Q for stability (Q-ball criterion)

import numpy as np
import matplotlib.pyplot as plt

# ----- Parameters -----
v      = 1.0   # vacuum η at infinity (normalization)
m2     = 1.0   # small-fluctuation mass^2 (m = sqrt(m2))
g      = 1.5   # quartic coefficient (appears as -g φ^4/4 in V_eff)
h      = 0.2   # sextic coefficient (stabilizes large φ)
omega  = 0.9   # internal rotation frequency (0 < ω < m = 1)

# ----- Grid -----
R   = 60.0
N   = 6000
r   = np.linspace(0.0, R, N+1)
dr  = r[1] - r[0]

# ----- Effective equation & potential -----
def force(phi: np.ndarray) -> np.ndarray:
    """
    RHS nonlinear 'force' for the envelope equation:
      φ'' + (2/r) φ' = (m^2 - ω^2) φ - g φ^3 + h φ^5
    """
    return (m2 - omega**2)*phi - g*phi**3 + h*phi**5

def laplacian_radial(phi: np.ndarray) -> np.ndarray:
    """
    Spherical radial Laplacian: φ'' + (2/r) φ'
    with regularity at r=0 enforced by finite-difference stencils.
    """
    d2 = np.zeros_like(phi)
    d2[1:-1] = (phi[2:] - 2*phi[1:-1] + phi[:-2]) / dr**2
    d2[0] = 2*(phi[1] - phi[0]) / dr**2  # regularity at origin

    dp = np.zeros_like(phi)
    dp[1:-1] = (phi[2:] - phi[:-2]) / (2*dr)
    dp[0] = 0.0

    return d2 + (2.0/np.maximum(r, dr))*dp

def V_eff(phi: np.ndarray) -> np.ndarray:
    """
    Time-averaged effective potential density for the rotating envelope:
      V_eff = 1/2 m^2 φ^2 - 1/4 g φ^4 + (h/6) φ^6
    """
    return 0.5*m2*phi**2 - 0.25*g*phi**4 + (h/6.0)*phi**6

# ----- Gradient-flow relaxation -----
# Localized initial seed for φ(r); η(r) = v + φ(r)
phi = 0.8 * np.exp(-((r - 15.0)/5.0)**2)
phi[0] = phi[1]  # enforce regularity at origin

# Explicit diffusion-like relaxation to steady solution
dt = 0.1 * dr**2
max_steps = 200000
for step in range(max_steps):
    lap = laplacian_radial(phi)
    phi += dt * (lap - force(phi))

    # Boundary conditions
    phi[0]  = phi[1]   # Neumann at r=0
    phi[-1] = 0.0      # Dirichlet at r=R (vacuum)

    if step % 20000 == 0:
        print(f"[relax] step {step}")

# ----- Build η and diagnostics -----
eta  = v + phi
dphi = np.gradient(phi, dr)

# Time-averaged energy density for the rotating configuration
rho = 0.5*(dphi**2 + omega**2*phi**2) + V_eff(phi)

# Global charge Q and energy E in spherical symmetry
vol_elt = 4.0*np.pi*(r**2)*dr
Q = np.sum((omega*phi**2) * vol_elt)
E = np.sum(rho * vol_elt)
m = np.sqrt(m2)

print("\n=== Stability diagnostics ===")
print(f"Charge Q ≈ {Q:.4e}")
print(f"Energy E ≈ {E:.4e}")
print(f"E/Q ≈ {E/Q:.6f}  (compare to m = {m:.3f})")

# ----- Plots -----
# η(r)
plt.figure(figsize=(7, 4.2))
plt.plot(r, eta, linewidth=2)
plt.xlabel("r"); plt.ylabel("η(r)")
plt.title("η(r): Cann-Shell–like stable solution")
plt.tight_layout(); plt.savefig("eta_profile.png"); plt.close()

# Energy density ρ(r)
plt.figure(figsize=(7, 4.2))
plt.plot(r, rho, linewidth=2)
plt.xlabel("r"); plt.ylabel("ρ(r)")
plt.title("Energy density (localized shell)")
plt.tight_layout(); plt.savefig("energy_density.png"); plt.close()

# Gradia |dη/dr|
deta = np.gradient(eta, dr)
plt.figure(figsize=(7, 4.2))
plt.plot(r, np.abs(deta), linewidth=2)
plt.xlabel("r"); plt.ylabel("|dη/dr|")
plt.title("Gradia peaks at shell flanks")
plt.tight_layout(); plt.savefig("gradia_abs.png"); plt.close()

# 2D η(x,y) slice (annulus)
Rmax = 30.0
Nxy  = 300
xs = np.linspace(-Rmax, Rmax, Nxy)
ys = np.linspace(-Rmax, Rmax, Nxy)
X, Y = np.meshgrid(xs, ys)
RR = np.sqrt(X**2 + Y**2)
eta_2d = np.interp(RR, r, eta, left=eta[0], right=v)

plt.figure(figsize=(6, 5.5))
plt.imshow(eta_2d, extent=[-Rmax, Rmax, -Rmax, Rmax], origin='lower', aspect='equal')
plt.colorbar(label="η(x,y)")
plt.title("2D slice η(x,y): shell annulus")
plt.xlabel("x"); plt.ylabel("y")
plt.tight_layout(); plt.savefig("eta_2d.png"); plt.close()
```0
