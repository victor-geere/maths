---
title: Quadratic Formula
tag: algebra
summary: Closed-form roots of any degree-2 polynomial.
links:
  - completing-the-square
  - polynomial-roots
  - complex-numbers
---

## Key Formula

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

## Notes

Given **ax² + bx + c = 0** (a ≠ 0), the two roots are given by the formula above.

The **discriminant** $\Delta = b^2 - 4ac$ controls the nature of the roots:

- $\Delta > 0$ → two distinct real roots
- $\Delta = 0$ → one repeated real root  
- $\Delta < 0$ → two complex conjugate roots

### Derivation

Start from $ax^2 + bx + c = 0$, divide by $a$:

$$x^2 + \frac{b}{a}x = -\frac{c}{a}$$

[[completing-the-square|Complete the square]] by adding $\left(\frac{b}{2a}\right)^2$ to both sides:

$$\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}$$

Taking square roots and solving for $x$ gives the quadratic formula.

### Example

Solve $2x^2 - 4x - 6 = 0$:

$$x = \frac{4 \pm \sqrt{16 + 48}}{4} = \frac{4 \pm 8}{4}$$

So $x = 3$ or $x = -1$.

When the discriminant is negative, the roots are [[complex-numbers|complex conjugates]] of the form $\alpha \pm \beta i$.
