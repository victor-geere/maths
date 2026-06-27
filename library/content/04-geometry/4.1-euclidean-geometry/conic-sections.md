---
title: Conic Sections
tag: geometry
summary: Circle, ellipse, parabola, hyperbola — cross-sections of a double cone.
links:
  - completing-the-square
---

## Key Formula

$$Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$$

## Notes

Every conic section is a cross-section of a right circular double cone by a plane. The **discriminant** $\Delta = B^2 - 4AC$ classifies the type:

| Discriminant | Type |
|---|---|
| $\Delta < 0$, $A = C$, $B = 0$ | Circle |
| $\Delta < 0$ (otherwise) | Ellipse |
| $\Delta = 0$ | Parabola |
| $\Delta > 0$ | Hyperbola |

### Standard forms

**Circle** (centre $(h,k)$, radius $r$):

$$( x-h)^2 + (y-k)^2 = r^2$$

**Ellipse** (semi-axes $a > b > 0$, foci at $(\pm c, 0)$ where $c^2 = a^2 - b^2$):

$$\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1$$

**Parabola** (vertex $(h,k)$, opens upward):

$$y - k = \frac{1}{4p}(x-h)^2 \qquad \text{focus at } (h, k+p)$$

**Hyperbola** (foci at $(\pm c, 0)$, $c^2 = a^2 + b^2$):

$$\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1$$

Asymptotes: $y = \pm \dfrac{b}{a}x$.

### Converting the general form

[[completing-the-square|Complete the square]] in $x$ and $y$ separately to convert $Ax^2 + Cy^2 + Dx + Ey + F = 0$ (with $B=0$) to standard form.

### Focal definition

Each conic has a **focus-directrix** definition: the locus of points whose distance to a focus and to a directrix are in a fixed ratio $e$ (the **eccentricity**): $e = 0$ (circle), $0 < e < 1$ (ellipse), $e = 1$ (parabola), $e > 1$ (hyperbola).
