---
title: Geodesics
tag: differential-geometry
summary: The shortest-path curves on a surface, generalising straight lines to curved geometry.
links:
  - gaussian-curvature
  - first-fundamental-form
  - arc-length
  - frenet-serret
---

# Geodesics

A **geodesic** is the generalisation of a straight line to a curved surface: it is the locally shortest path between two points when you are constrained to move along the surface. On a sphere, geodesics are **great circles** — the routes that aeroplanes follow between cities. On a flat plane, geodesics are ordinary straight lines. The study of geodesics is central to differential geometry, general relativity (where the paths of free-falling objects are geodesics in curved spacetime), and optimisation on Riemannian manifolds.

## Definition

A smooth curve $\gamma(t)$ on a surface is a **geodesic** if its acceleration vector $\gamma''(t)$ is always **normal** to the surface (i.e. has no tangential component). Equivalently, a geodesic is a curve whose **geodesic curvature** vanishes:

$$\kappa_g = 0$$

## Geodesic Equations

In local coordinates $(u, v)$, geodesics satisfy the **geodesic equations**:

$$\ddot{u} + \Gamma^u_{uu}\dot{u}^2 + 2\Gamma^u_{uv}\dot{u}\dot{v} + \Gamma^u_{vv}\dot{v}^2 = 0$$

$$\ddot{v} + \Gamma^v_{uu}\dot{u}^2 + 2\Gamma^v_{uv}\dot{u}\dot{v} + \Gamma^v_{vv}\dot{v}^2 = 0$$

where $\Gamma^k_{ij}$ are the **Christoffel symbols** computed from the first fundamental form.

## Examples

| Surface | Geodesics |
|---|---|
| Plane | Straight lines |
| Sphere | Great circles (intersections with planes through the centre) |
| Cylinder | Helices (and straight lines along the axis) |
| Cone | Straight lines in the unrolled cone |

## Variational Characterisation

Geodesics are the **critical curves** of the arc length functional:

$$L[\gamma] = \int_a^b \sqrt{E\dot{u}^2 + 2F\dot{u}\dot{v} + G\dot{v}^2}\, dt$$

They minimise (or extremise) length among nearby paths with the same endpoints.

## Gauss–Bonnet and Geodesic Triangles

For a geodesic triangle on a surface with interior angles $\alpha, \beta, \gamma$ and enclosed area $A$:

$$\alpha + \beta + \gamma = \pi + \iint_{\text{interior}} K\, dA$$

- On a sphere ($K > 0$): angles sum to **more** than $\pi$.
- On a flat plane ($K = 0$): angles sum to exactly $\pi$.
- On a hyperbolic surface ($K < 0$): angles sum to **less** than $\pi$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Geodesic | shortest-path curve on a surface; has zero geodesic curvature |
| $\kappa_g$ | geodesic curvature — tangential component of curvature |
| $\gamma(t)$ | parametric curve on the surface |
| $\dot{u}, \dot{v}$ | derivatives of the coordinates $u, v$ with respect to parameter $t$ |
| $\ddot{u}, \ddot{v}$ | second derivatives with respect to $t$ |
| $\Gamma^k_{ij}$ | Christoffel symbols — encode how the coordinate frame changes |
| Great circle | the intersection of a sphere with a plane through its centre; shortest paths on the sphere |
| Helix | a curve on a cylinder winding at a constant angle |
| Geodesic curvature | the component of $\gamma''$ that lies in the tangent plane |
| Gauss–Bonnet theorem | relates total curvature of a region to angle sums of its geodesic boundary |
| Riemannian manifold | a smooth manifold equipped with a metric tensor |
| Variational principle | finding extremals (geodesics) of a functional (arc length) |
| Christoffel symbols | quantities derived from the metric encoding intrinsic curvature |
