---
title: Gaussian Curvature
tag: differential-geometry
summary: An intrinsic measure of how a surface curves in two directions simultaneously, invariant under bending.
links:
  - first-fundamental-form
  - curvature
  - geodesics
  - frenet-serret
---

# Gaussian Curvature

**Gaussian curvature** $K$ measures how a surface curves in two independent directions at once. It is the product of the two **principal curvatures** — the maximum and minimum curvatures over all directions through a point. What makes Gaussian curvature remarkable is Gauss's *Theorema Egregium* ("remarkable theorem"): $K$ is an **intrinsic** property, meaning it can be measured by beings living entirely within the surface without any reference to the surrounding 3D space. This discovery laid the conceptual groundwork for general relativity, where spacetime curvature is an intrinsic property of the universe itself.

## Principal Curvatures

At each point of a surface, there are two orthogonal directions of **extreme normal curvature**:

- $\kappa_1$ = maximum normal curvature (**first principal curvature**)
- $\kappa_2$ = minimum normal curvature (**second principal curvature**)

The directions achieving these extremes are the **principal directions**.

## Gaussian and Mean Curvature

$$K = \kappa_1 \kappa_2 \qquad \text{(Gaussian curvature)}$$

$$H = \frac{\kappa_1 + \kappa_2}{2} \qquad \text{(Mean curvature)}$$

## Signs of $K$

| $K > 0$ | $K = 0$ | $K < 0$ |
|---|---|---|
| Elliptic point: surface curves the same way in all directions (like a sphere) | Parabolic point: flat in one direction (like a cylinder) | Hyperbolic point: saddle-shaped (curves up in one direction, down in another) |

## Examples

| Surface | $K$ |
|---|---|
| Sphere of radius $R$ | $K = 1/R^2$ (constant positive) |
| Plane | $K = 0$ |
| Cylinder of radius $R$ | $K = 0$ |
| Saddle surface $z = xy$ | $K = -1/(1+x^2+y^2)^2 < 0$ |
| Pseudosphere | $K = -1$ (constant negative) |

## Theorema Egregium

$K$ can be computed entirely from the **first fundamental form** (the metric $E, F, G$). It does not change when the surface is bent without stretching. This means a flat sheet of paper cannot be rolled into a sphere without distortion.

## Gauss–Bonnet Theorem

For a compact surface $S$ with Euler characteristic $\chi$:

$$\iint_S K\, dA = 2\pi\chi$$

For a sphere: $\chi = 2$ and $K = 1/R^2$, so $\iint K\, dA = 4\pi$. ✓

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $K$ | Gaussian curvature ($= \kappa_1 \kappa_2$) |
| $H$ | mean curvature ($= (\kappa_1 + \kappa_2)/2$) |
| $\kappa_1, \kappa_2$ | principal curvatures (max and min normal curvatures) |
| Principal directions | orthogonal directions of extreme curvature |
| Normal curvature | curvature of the curve formed by intersecting the surface with a normal plane |
| Elliptic point | point where $K > 0$ (bowl-shaped) |
| Hyperbolic point | point where $K < 0$ (saddle-shaped) |
| Parabolic point | point where $K = 0$ (curved in at most one direction) |
| Theorema Egregium | Gauss's theorem: $K$ is intrinsic (depends only on the metric) |
| Gauss–Bonnet theorem | $\iint_S K\,dA = 2\pi\chi(S)$ |
| $\chi$ (chi) | Euler characteristic of the surface |
| Intrinsic | measurable without leaving the surface |
| Pseudosphere | a surface of constant negative Gaussian curvature |
