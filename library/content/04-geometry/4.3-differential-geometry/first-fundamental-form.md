---
title: Surfaces & First Fundamental Form
tag: differential-geometry
summary: Parametric surfaces in 3D and the metric tensor encoding lengths and areas on the surface.
links:
  - frenet-serret
  - arc-length
  - gaussian-curvature
  - geodesics
---

# Surfaces & First Fundamental Form

A **surface** in three-dimensional space is a two-dimensional geometric object — think of a sphere, a cylinder, or a saddle. Locally it can be described by two parameters $(u, v)$, giving a mapping $\mathbf{r}(u, v)$ from a patch of the plane into $\mathbb{R}^3$. The **first fundamental form** is the metric structure induced on the surface by this embedding: it encodes how to measure lengths of curves, angles between directions, and areas of regions entirely from within the surface itself, without reference to the surrounding 3D space. It is the foundation of intrinsic differential geometry.

## Parametric Surface

A surface patch is a smooth map $\mathbf{r} : U \subset \mathbb{R}^2 \to \mathbb{R}^3$:

$$\mathbf{r}(u, v) = \bigl(x(u,v),\; y(u,v),\; z(u,v)\bigr)$$

The **tangent vectors** at a point are:

$$\mathbf{r}_u = \frac{\partial \mathbf{r}}{\partial u}, \qquad \mathbf{r}_v = \frac{\partial \mathbf{r}}{\partial v}$$

## The First Fundamental Form

The **metric coefficients** (components of the metric tensor):

$$E = \mathbf{r}_u \cdot \mathbf{r}_u, \quad F = \mathbf{r}_u \cdot \mathbf{r}_v, \quad G = \mathbf{r}_v \cdot \mathbf{r}_v$$

The **first fundamental form** $\mathbf{I}$ is the quadratic form:

$$ds^2 = E\, du^2 + 2F\, du\, dv + G\, dv^2$$

## Arc Length and Area

**Arc length** of a curve $(u(t), v(t))$ on the surface:

$$L = \int \sqrt{E\dot{u}^2 + 2F\dot{u}\dot{v} + G\dot{v}^2}\, dt$$

**Area element:**

$$dA = \|\mathbf{r}_u \times \mathbf{r}_v\|\, du\, dv = \sqrt{EG - F^2}\, du\, dv$$

## Example: Sphere of Radius $R$

$$\mathbf{r}(\theta, \phi) = (R\sin\phi\cos\theta,\; R\sin\phi\sin\theta,\; R\cos\phi)$$

$$E = R^2\sin^2\phi, \quad F = 0, \quad G = R^2$$

$$ds^2 = R^2\sin^2\!\phi\, d\theta^2 + R^2\, d\phi^2$$

Area of the whole sphere: $\int_0^{2\pi}\!\int_0^\pi R^2\sin\phi\, d\phi\, d\theta = 4\pi R^2$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathbf{r}(u,v)$ | parametric description of the surface |
| $u, v$ | surface parameters (coordinates on the surface) |
| $\mathbf{r}_u, \mathbf{r}_v$ | partial derivatives of $\mathbf{r}$ — tangent vectors |
| $E, F, G$ | metric coefficients of the first fundamental form |
| $ds^2$ | infinitesimal squared arc length on the surface |
| $dA$ | area element on the surface |
| First fundamental form $\mathbf{I}$ | the metric tensor $E\,du^2 + 2F\,du\,dv + G\,dv^2$ |
| Metric tensor | a bilinear form measuring distances in a tangent space |
| $\theta, \phi$ | spherical coordinates (longitude and colatitude) |
| Intrinsic geometry | geometric properties measurable within the surface itself |
| $\times$ | cross product |
| $\cdot$ | dot product |
| Tangent plane | the plane spanned by $\mathbf{r}_u$ and $\mathbf{r}_v$ at a point |
