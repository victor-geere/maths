---
title: Triple Integrals
tag: multivariable-calculus
summary: Integrating a function of three variables over a three-dimensional region, in Cartesian, cylindrical, or spherical coordinates.
links:
  - double-integrals
  - change-of-variables
  - divergence-theorem
---

# Triple Integrals

A **triple integral** extends integration to three dimensions: it sums contributions of a function $f(x, y, z)$ over a solid region $E$ in $\mathbb{R}^3$. Triple integrals compute volumes of solids, masses of three-dimensional objects with variable density, moments of inertia, and total charge or probability over a 3D region. The strategy mirrors that for double integrals — reduce to iterated single integrals using Fubini's theorem — but now we have three nested integrals, and the choice of coordinate system (Cartesian, cylindrical, or spherical) can dramatically simplify the computation.

## Definition

$$\iiint_E f(x,y,z)\,dV = \lim_{\|P\|\to 0}\sum_{i,j,k} f(x_i^*, y_j^*, z_k^*)\,\Delta V_{ijk}$$

## Iterated Integral (Cartesian)

For a box $E = [a,b]\times[c,d]\times[p,q]$:

$$\iiint_E f\,dV = \int_p^q\!\int_c^d\!\int_a^b f(x,y,z)\,dx\,dy\,dz$$

For general regions, describe the bounds of each variable as functions of the outer variables.

## Cylindrical Coordinates

$x = r\cos\theta$, $y = r\sin\theta$, $z = z$; Jacobian $= r$:

$$\iiint_E f\,dV = \int\!\int\!\int f(r\cos\theta, r\sin\theta, z)\,r\,dr\,d\theta\,dz$$

Ideal for regions with circular cross-sections (cylinders, cones).

## Spherical Coordinates

$x = \rho\sin\phi\cos\theta$, $y = \rho\sin\phi\sin\theta$, $z = \rho\cos\phi$; Jacobian $= \rho^2\sin\phi$:

$$\iiint_E f\,dV = \int\!\int\!\int f\,\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$$

where $\rho \geq 0$, $0 \leq \phi \leq \pi$, $0 \leq \theta < 2\pi$. Ideal for spheres and cones.

## Volume of a Solid

$$V = \iiint_E 1\,dV$$

**Example:** Volume of ball of radius $R$ in spherical coordinates:

$$V = \int_0^{2\pi}\!\int_0^\pi\!\int_0^R \rho^2\sin\phi\,d\rho\,d\phi\,d\theta = \frac{4}{3}\pi R^3$$

## Mass and Centre of Mass

Mass: $m = \iiint_E \rho(x,y,z)\,dV$

Centre of mass $x$-coordinate: $\bar{x} = \dfrac{1}{m}\iiint_E x\,\rho\,dV$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\iiint_E f\,dV$ | triple integral of $f$ over solid region $E$ |
| $dV$ | volume element ($dx\,dy\,dz$ in Cartesian; $r\,dr\,d\theta\,dz$ in cylindrical; $\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$ in spherical) |
| $E$ | solid region of integration in $\mathbb{R}^3$ |
| Cylindrical coordinates | $(r, \theta, z)$ — polar in $xy$-plane, $z$ unchanged |
| Spherical coordinates | $(\rho, \phi, \theta)$ — radial distance, polar angle, azimuthal angle |
| $\rho$ (rho) | radial distance from origin in spherical coordinates |
| $\phi$ (phi) | polar angle from the positive $z$-axis (colatitude) |
| $\theta$ (theta) | azimuthal angle around the $z$-axis |
| Jacobian | coordinate-change scaling factor; ensures $dV$ remains the true volume element |
| Centre of mass | weighted average position $(\bar{x}, \bar{y}, \bar{z})$ |
| Fubini's theorem | triple integral equals three nested single integrals |
