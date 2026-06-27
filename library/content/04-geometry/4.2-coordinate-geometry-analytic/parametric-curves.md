---
title: Parametric Curves
tag: geometry
summary: Describing curves by expressing coordinates as functions of an independent parameter t.
links:
  - lines-plane
  - polar-coordinates
  - arc-length
---

# Parametric Curves

A **parametric curve** describes the position of a point as it moves through the plane (or space) by giving each coordinate as a function of a shared **parameter** $t$, typically thought of as time. This approach can represent curves that are not functions of $x$ (such as circles or loops) and makes it natural to encode direction of travel, speed, and orientation. Parametric descriptions are indispensable in physics, computer graphics, and the differential geometry of curves.

## Definition

A **parametric curve** in $\mathbb{R}^2$ is a pair of functions:

$$x = f(t), \quad y = g(t), \quad t \in [a, b]$$

The curve is the set of points $\{(f(t), g(t)) : t \in [a,b]\}$.

## Common Examples

### Line through $(x_0, y_0)$ with direction $(p, q)$:
$$x = x_0 + pt, \quad y = y_0 + qt$$

### Circle of radius $r$ centred at origin:
$$x = r\cos t, \quad y = r\sin t, \quad t \in [0, 2\pi)$$

### Ellipse with semi-axes $a, b$:
$$x = a\cos t, \quad y = b\sin t$$

### Cycloid (point on rolling circle of radius $r$):
$$x = r(t - \sin t), \quad y = r(1 - \cos t)$$

## Eliminating the Parameter

To convert to a Cartesian equation, solve one equation for $t$ and substitute, or use a trigonometric identity.

**Example (circle):** $x^2 + y^2 = r^2\cos^2 t + r^2\sin^2 t = r^2$.

## Arc Length

The length of a parametric curve from $t = a$ to $t = b$:

$$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\, dt$$

## Tangent Vector and Slope

The **tangent vector** at $t$ is $(f'(t), g'(t))$. The slope of the tangent line is:

$$\frac{dy}{dx} = \frac{g'(t)}{f'(t)} \quad (f'(t) \neq 0)$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $t$ | the parameter (often represents time) |
| $f(t),\, g(t)$ | coordinate functions |
| $[a, b]$ | parameter interval |
| Parametric curve | a curve defined by $(x,y) = (f(t), g(t))$ |
| Cycloid | curve traced by a point on the rim of a rolling circle |
| Arc length | total length of the curve |
| Tangent vector | $(f'(t), g'(t))$ — direction of motion at parameter $t$ |
| Cartesian equation | an equation relating $x$ and $y$ directly (no parameter) |
| Eliminating the parameter | rewriting the parametric form as a Cartesian equation |
| Orientation | the direction the curve is traced as $t$ increases |
