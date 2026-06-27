---
title: Polar Coordinates
tag: geometry
summary: Describing points in the plane by distance from the origin and angle from the positive x-axis.
links:
  - parametric-curves
  - lines-plane
  - conic-sections
---

# Polar Coordinates

**Polar coordinates** describe a point in the plane by how far it is from the origin (its **radius** $r$) and what angle it makes with the positive $x$-axis (its **angle** $\theta$). While Cartesian coordinates are natural for horizontal-vertical layouts, polar coordinates are ideal for circular symmetry, spiral curves, and problems in physics where distances from a central point matter. Many curves that have complicated Cartesian equations become elegant in polar form.

## Definition

A point $(r, \theta)$ in polar coordinates corresponds to the Cartesian point:

$$x = r\cos\theta, \quad y = r\sin\theta$$

Conversely:

$$r = \sqrt{x^2 + y^2}, \quad \theta = \arctan\!\left(\frac{y}{x}\right) \quad (\text{with quadrant adjustment})$$

## Conventions

- $r \geq 0$ (non-negative radius); negative $r$ reflects through the origin.
- $\theta$ is measured counter-clockwise from the positive $x$-axis.
- Points are not unique: $(r, \theta) = (r, \theta + 2\pi k)$ for any integer $k$, and $(r, \theta) = (-r, \theta + \pi)$.

## Common Polar Curves

| Curve | Equation | Shape |
|---|---|---|
| Circle (centred at origin) | $r = a$ | circle of radius $a$ |
| Line through origin | $\theta = \alpha$ | ray at angle $\alpha$ |
| Cardioid | $r = a(1 + \cos\theta)$ | heart-shaped loop |
| Rose curve | $r = a\cos(n\theta)$ | $n$ or $2n$ petals |
| Archimedean spiral | $r = a\theta$ | evenly-spaced spiral |
| Lemniscate | $r^2 = a^2\cos(2\theta)$ | figure-eight |

## Area in Polar Coordinates

The area swept by the curve from $\theta = \alpha$ to $\theta = \beta$:

$$A = \frac{1}{2}\int_\alpha^\beta r^2\, d\theta$$

## Arc Length in Polar Coordinates

$$L = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\, d\theta$$

## Conics in Polar Form (focus at origin)

$$r = \frac{ed}{1 + e\cos\theta}$$

where $e$ is the eccentricity and $d$ is the distance to the directrix.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $r$ | radial distance from the origin |
| $\theta$ | angle from the positive $x$-axis (in radians) |
| Origin (pole) | the reference point $(0,0)$ in polar coordinates |
| Polar axis | the positive $x$-direction from which $\theta$ is measured |
| Cardioid | a curve with equation $r = a(1 \pm \cos\theta)$ or $r = a(1 \pm \sin\theta)$ |
| Rose curve | petal-shaped polar curve $r = a\cos(n\theta)$ or $r = a\sin(n\theta)$ |
| Archimedean spiral | spiral where $r$ increases linearly with $\theta$ |
| Lemniscate | figure-eight curve; $r^2 = a^2 \cos(2\theta)$ |
| Eccentricity $e$ | parameter classifying conics ($e<1$: ellipse, $e=1$: parabola, $e>1$: hyperbola) |
| $\arctan$ | inverse tangent function |
