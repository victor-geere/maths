---
title: Double Integrals
tag: multivariable-calculus
summary: Integrating a function of two variables over a planar region, computed as an iterated integral.
links:
  - riemann-integral
  - change-of-variables
  - triple-integrals
---

# Double Integrals

A **double integral** extends the idea of a single integral to functions of two variables: instead of summing infinitesimal areas under a curve, we sum infinitesimal volumes under a surface $z = f(x, y)$ over a region $R$ in the $xy$-plane. Just as a single integral computes area, a double integral computes volume, mass, average values, moments of inertia, and probabilities over two-dimensional regions. The key computational tool is **Fubini's theorem**, which allows the double integral to be evaluated as two successive single integrals — an iterated integral.

## Definition

$$\iint_R f(x, y)\,dA = \lim_{\|P\|\to 0}\sum_{i,j} f(x_i^*, y_j^*)\,\Delta x_i\,\Delta y_j$$

where the sum is over a partition $P$ of $R$ and $(x_i^*, y_j^*)$ is any sample point in each sub-rectangle.

## Fubini's Theorem

For a rectangle $R = [a,b]\times[c,d]$:

$$\iint_R f(x,y)\,dA = \int_c^d\!\int_a^b f(x,y)\,dx\,dy = \int_a^b\!\int_c^d f(x,y)\,dy\,dx$$

The order of integration may be swapped freely when $f$ is continuous.

## General Regions

**Type I** (bounded by functions of $x$): $R = \{(x,y): a \leq x \leq b,\; g_1(x) \leq y \leq g_2(x)\}$

$$\iint_R f\,dA = \int_a^b\!\int_{g_1(x)}^{g_2(x)} f(x,y)\,dy\,dx$$

**Type II** (bounded by functions of $y$): integrate in the opposite order.

## Switching the Order of Integration

Sketching the region $R$ and re-describing it in the other order often converts an impossible inner integral into a tractable one.

## Polar Coordinates

For regions with circular symmetry, let $x = r\cos\theta$, $y = r\sin\theta$:

$$\iint_R f(x,y)\,dA = \int_\alpha^\beta\!\int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta$$

The factor $r$ is the Jacobian of the polar coordinate change.

## Applications

- **Volume** under surface $z = f(x,y)$: $V = \iint_R f\,dA$
- **Area** of region $R$: $A = \iint_R 1\,dA$
- **Average value:** $\bar{f} = \dfrac{1}{A(R)}\iint_R f\,dA$
- **Mass** (density $\rho$): $m = \iint_R \rho(x,y)\,dA$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\iint_R f\,dA$ | double integral of $f$ over region $R$ |
| $dA$ | area element ($= dx\,dy$ in Cartesian, $= r\,dr\,d\theta$ in polar) |
| $R$ | the region of integration in the $xy$-plane |
| Fubini's theorem | allows swapping the order of iterated integration |
| Iterated integral | a double integral written as two nested single integrals |
| Type I region | region described by $g_1(x) \leq y \leq g_2(x)$ |
| Type II region | region described by $h_1(y) \leq x \leq h_2(y)$ |
| Partition $P$ | a grid dividing $R$ into small sub-rectangles |
| Jacobian | scaling factor when changing variables; $r$ in polar coordinates |
| Polar coordinates | $(r, \theta)$ system where $x = r\cos\theta$, $y = r\sin\theta$ |
