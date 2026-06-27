---
title: Lines in the Plane
tag: geometry
summary: Equations, slopes, and intercepts of straight lines in the Cartesian plane.
links:
  - distance-midpoint
  - parametric-curves
  - conic-sections
---

# Lines in the Plane

A **straight line** in the Cartesian plane is the simplest geometric curve — the set of all points satisfying a single linear equation in $x$ and $y$. Lines encode constant rates of change, and every linear relationship in mathematics or science has a line as its graph. Understanding their equations, slopes, and mutual relationships (parallel, perpendicular, intersecting) is the starting point of analytic geometry.

## Equations of a Line

### Slope–Intercept Form
$$y = mx + c$$

- $m$ = **slope** (rise over run)
- $c$ = **y-intercept** (value of $y$ when $x = 0$)

### Point–Slope Form
Given slope $m$ and a point $(x_1, y_1)$:
$$y - y_1 = m(x - x_1)$$

### Standard (General) Form
$$ax + by + c = 0 \quad (a, b \text{ not both zero})$$

### Intercept Form
$$\frac{x}{a} + \frac{y}{b} = 1$$

where $(a, 0)$ and $(0, b)$ are the x- and y-intercepts.

## Slope

The slope of the line through $(x_1, y_1)$ and $(x_2, y_2)$:

$$m = \frac{y_2 - y_1}{x_2 - x_1} \quad (x_1 \neq x_2)$$

- Positive slope: rises left to right
- Negative slope: falls left to right
- Zero slope: horizontal line
- Undefined slope: vertical line ($x = k$)

## Parallel and Perpendicular Lines

- **Parallel:** same slope, $m_1 = m_2$ (and different intercepts)
- **Perpendicular:** slopes multiply to $-1$: $m_1 m_2 = -1$, i.e. $m_2 = -1/m_1$

## Distance from a Point to a Line

Distance from point $(x_0, y_0)$ to line $ax + by + c = 0$:

$$d = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}$$

## Intersection of Two Lines

Solve the system $\{y = m_1 x + c_1,\; y = m_2 x + c_2\}$:

$$x = \frac{c_2 - c_1}{m_1 - m_2} \quad (m_1 \neq m_2)$$

If $m_1 = m_2$ the lines are parallel (no intersection, or identical).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $m$ | slope of a line (rise/run) |
| $c$ | y-intercept |
| $(x_1, y_1)$, $(x_2, y_2)$ | two points on the line |
| $ax + by + c = 0$ | general (standard) form of a line |
| Slope | rate of change of $y$ with respect to $x$; $\Delta y / \Delta x$ |
| y-intercept | the $y$-value where the line crosses the $y$-axis |
| x-intercept | the $x$-value where the line crosses the $x$-axis |
| Parallel lines | lines with equal slopes that do not intersect |
| Perpendicular lines | lines whose slopes satisfy $m_1 m_2 = -1$ |
| Cartesian plane | the $xy$-plane with coordinates |
| Undefined slope | slope of a vertical line (division by zero) |
