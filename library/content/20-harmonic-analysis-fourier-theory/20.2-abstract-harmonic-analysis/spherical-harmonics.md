---
title: Spherical Harmonics
tag: harmonic-analysis
summary: Spherical harmonics are the eigenfunctions of the Laplace–Beltrami operator on the sphere S²; they form an orthonormal basis of L²(S²) and are the angular part of solutions to Laplace's equation in 3D.
links:
  - fourier-series
  - fourier-on-groups
  - laplace-poisson
  - special-angles
---

# Spherical Harmonics

**Spherical harmonics** $Y_\ell^m(\theta, \varphi)$ are the natural orthonormal basis of $L^2(S^2)$ — the analogue of the Fourier basis $e^{in\theta}$ for functions on the circle, now extended to functions on the sphere. They arise as the eigenfunctions of the **Laplace–Beltrami operator** $\Delta_{S^2}$ on $S^2$, with eigenvalue $-\ell(\ell+1)$ for degree $\ell$. Spherical harmonics are the angular part of solutions to **Laplace's equation** $\Delta u = 0$ in 3D: any harmonic function in a spherical domain expands in spherical harmonics. They appear throughout physics — atomic orbitals (quantum mechanics), gravitational and electromagnetic multipoles, climate modelling — and in harmonic analysis on $SO(3)$ (the rotation group).

## Definition

In spherical coordinates $(r, \theta, \varphi)$ with $\theta \in [0,\pi]$, $\varphi \in [0,2\pi)$:

$$Y_\ell^m(\theta,\varphi) = \sqrt{\frac{(2\ell+1)}{4\pi}\frac{(\ell-m)!}{(\ell+m)!}}\,P_\ell^m(\cos\theta)\,e^{im\varphi}$$

for $\ell = 0, 1, 2, \ldots$ and $m = -\ell, -\ell+1, \ldots, \ell$, where $P_\ell^m$ are **associated Legendre polynomials**.

## Properties

- **Orthonormality**: $\int_{S^2} Y_\ell^m \overline{Y_{\ell'}^{m'}}\,d\Omega = \delta_{\ell\ell'}\delta_{mm'}$
- **Completeness**: Every $f \in L^2(S^2)$ expands as $f = \sum_{\ell=0}^\infty \sum_{m=-\ell}^\ell c_{\ell m} Y_\ell^m$
- **Eigenvalue**: $\Delta_{S^2}Y_\ell^m = -\ell(\ell+1)Y_\ell^m$
- **Addition theorem**: $\sum_{m=-\ell}^\ell Y_\ell^m(\hat{x})\overline{Y_\ell^m(\hat{y})} = \frac{2\ell+1}{4\pi}P_\ell(\hat{x}\cdot\hat{y})$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $Y_\ell^m(\theta,\varphi)$ | spherical harmonic of degree $\ell$, order $m$ |
| $\ell = 0,1,2,\ldots$ | degree (angular momentum quantum number) |
| $m = -\ell,\ldots,\ell$ | order (magnetic quantum number) |
| $P_\ell^m$ | associated Legendre polynomial |
| $\Delta_{S^2}$ | Laplace–Beltrami operator on $S^2$ |
| Eigenvalue $-\ell(\ell+1)$ | $\Delta_{S^2}Y_\ell^m = -\ell(\ell+1)Y_\ell^m$ |
| $d\Omega = \sin\theta\,d\theta\,d\varphi$ | solid angle element on $S^2$ |
| Addition theorem | $\sum_m Y_\ell^m(\hat{x})\overline{Y_\ell^m(\hat{y})} = \frac{2\ell+1}{4\pi}P_\ell(\cos\alpha)$ |
| Multipole expansion | expansion of $1/|\mathbf{r}-\mathbf{r}'|$ in spherical harmonics |
