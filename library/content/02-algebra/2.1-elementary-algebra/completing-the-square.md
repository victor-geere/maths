---
title: Completing the Square
tag: algebra
summary: Rewrite a quadratic in vertex form by adding and subtracting (b/2a)².
links:
  - quadratic-formula
  - conic-sections
---

## Key Formula

$$ax^2 + bx + c = a\!\left(x + \frac{b}{2a}\right)^2 - \frac{b^2 - 4ac}{4a}$$

## Notes

Completing the square transforms a general quadratic into **vertex form** $a(x - h)^2 + k$, where:

$$h = -\frac{b}{2a}, \qquad k = c - \frac{b^2}{4a}$$

### Steps

Given $x^2 + bx$:

1. Take half the coefficient of $x$: $\;\frac{b}{2}$
2. Square it: $\;\left(\frac{b}{2}\right)^2$
3. Add and subtract: $\;x^2 + bx + \left(\frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2 = \left(x + \frac{b}{2}\right)^2 - \frac{b^2}{4}$

### Uses

- Deriving the [[quadratic-formula|quadratic formula]]
- Finding the vertex $(h, k)$ of a parabola
- Converting [[conic-sections|conic section]] equations to standard form
- Solving integrals of the form $\int \frac{dx}{ax^2 + bx + c}$

### Example

Complete the square for $x^2 + 6x + 5$:

$$x^2 + 6x + 5 = (x+3)^2 - 9 + 5 = (x+3)^2 - 4$$

Vertex at $(-3, -4)$; roots where $(x+3)^2 = 4$, i.e. $x = -1$ or $x = -5$.
