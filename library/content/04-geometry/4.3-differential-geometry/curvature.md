---
title: Curvature of a Plane Curve
tag: differential-geometry
summary: A measure of how sharply a curve bends at each point, defined via the rate of turning of the unit tangent.
links:
  - arc-length
  - frenet-serret
  - parametric-curves
---

# Curvature of a Plane Curve

**Curvature** quantifies how rapidly a curve is turning at a given point. A straight line has zero curvature everywhere; a circle has constant curvature equal to the reciprocal of its radius. For a general curve, curvature varies from point to point and captures the local geometry — how tightly the path bends. It is the most fundamental intrinsic property of a curve, and its generalisation to surfaces and higher dimensions is the gateway to Riemannian geometry.

## Definition

The **curvature** $\kappa$ of a smooth plane curve at a point is the magnitude of the rate of change of the unit tangent vector $\mathbf{T}$ with respect to arc length $s$:

$$\kappa = \left\|\frac{d\mathbf{T}}{ds}\right\|$$

## Formulas

### For a parametric curve $(x(t), y(t))$:

$$\kappa = \frac{|x'y'' - y'x''|}{\left(x'^2 + y'^2\right)^{3/2}}$$

### For a Cartesian graph $y = f(x)$:

$$\kappa = \frac{|f''(x)|}{\left(1 + f'(x)^2\right)^{3/2}}$$

### For a circle of radius $R$:

$$\kappa = \frac{1}{R}$$

A larger circle bends less steeply and has smaller curvature.

## Radius of Curvature

The **radius of curvature** at a point is:

$$R = \frac{1}{\kappa}$$

The **osculating circle** at a point is the unique circle of radius $R$ that best approximates the curve there — it shares the same tangent and curvature.

## Sign Convention (Signed Curvature)

For a plane curve, one can assign a **signed curvature** $\kappa_s$: positive if the curve bends left (counter-clockwise), negative if it bends right. The unsigned curvature is $\kappa = |\kappa_s|$.

## Example

For $y = x^2$: $f'(x) = 2x$, $f''(x) = 2$.

$$\kappa = \frac{2}{(1 + 4x^2)^{3/2}}$$

At $x = 0$ (the vertex): $\kappa = 2$, so $R = \tfrac{1}{2}$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\kappa$ (kappa) | curvature — rate of turning of the unit tangent |
| $R$ | radius of curvature ($R = 1/\kappa$) |
| $s$ | arc length parameter |
| $\mathbf{T}$ | unit tangent vector |
| $x', y'$ | $dx/dt$, $dy/dt$ (derivatives with respect to parameter $t$) |
| $x'', y''$ | second derivatives with respect to $t$ |
| $f'(x), f''(x)$ | first and second derivatives of $y = f(x)$ |
| Osculating circle | the circle of radius $R$ that best fits the curve at a point |
| Signed curvature | curvature with a sign indicating left (+) or right (−) bending |
| Smooth curve | a curve with continuous derivatives |
| Unit tangent vector | $\mathbf{T} = \mathbf{r}'(s)$; always has magnitude 1 |
