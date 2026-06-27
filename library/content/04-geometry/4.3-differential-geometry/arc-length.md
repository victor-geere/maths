---
title: Arc Length
tag: differential-geometry
summary: The total length along a curve, computed by integrating the speed of a parametric traversal.
links:
  - parametric-curves
  - curvature
  - frenet-serret
---

# Arc Length

The **arc length** of a curve is its intrinsic one-dimensional measure — the total distance you would travel if you walked along the curve from one end to the other. Unlike the straight-line distance between endpoints, arc length captures every twist and turn. It is computed by breaking the curve into infinitesimally small straight segments, each of length $\sqrt{dx^2 + dy^2}$, and integrating. Arc length is the natural parameter for differential geometry: reparametrising a curve by arc length gives the cleanest formulas for curvature and the Frenet–Serret frame.

## Formulas

### Parametric curve $(x(t), y(t))$, $t \in [a, b]$:

$$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\, dt = \int_a^b \|\mathbf{r}'(t)\|\, dt$$

### Cartesian graph $y = f(x)$, $x \in [a, b]$:

$$L = \int_a^b \sqrt{1 + f'(x)^2}\, dx$$

### Polar curve $r = r(\theta)$, $\theta \in [\alpha, \beta]$:

$$L = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\, d\theta$$

### Space curve $\mathbf{r}(t) = (x(t), y(t), z(t))$:

$$L = \int_a^b \sqrt{x'^2 + y'^2 + z'^2}\, dt$$

## Arc Length as a Parameter

Reparametrising by arc length $s$ (measured from $t = a$):

$$s(t) = \int_a^t \|\mathbf{r}'(u)\|\, du$$

This gives $\|\mathbf{r}'(s)\| = 1$ (unit-speed parametrisation), simplifying the definition of curvature to $\kappa = \|\mathbf{r}''(s)\|$.

## Example

Length of one arch of the cycloid $x = t - \sin t$, $y = 1 - \cos t$, $t \in [0, 2\pi]$:

$$\frac{dx}{dt} = 1 - \cos t, \quad \frac{dy}{dt} = \sin t$$

$$L = \int_0^{2\pi} \sqrt{(1-\cos t)^2 + \sin^2 t}\, dt = \int_0^{2\pi} \sqrt{2 - 2\cos t}\, dt = 8$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $L$ | arc length |
| $s$ | arc length parameter (distance along the curve from a reference point) |
| $\mathbf{r}(t)$ | position vector as a function of parameter $t$ |
| $\mathbf{r}'(t)$ | velocity vector (tangent to the curve) |
| $\|\mathbf{r}'(t)\|$ | speed (magnitude of the velocity vector) |
| $f'(x)$ | derivative of $y = f(x)$ with respect to $x$ |
| Unit-speed parametrisation | reparametrisation with $\|\mathbf{r}'(s)\| = 1$ |
| Cycloid | curve traced by a point on the rim of a rolling circle |
| Polar curve | curve given in polar coordinates $r = r(\theta)$ |
| Integrand | the expression being integrated |
