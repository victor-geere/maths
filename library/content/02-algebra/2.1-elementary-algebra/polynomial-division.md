---
title: Polynomial Division & Remainder Theorem
tag: algebra
summary: Dividing polynomials and the key theorem linking roots to remainders.
links:
  - polynomial-roots
  - quadratic-formula
---

## Key Formula

For polynomials $f(x)$ and $d(x)$ with $\deg(d) \geq 1$:

$$f(x) = d(x) \cdot q(x) + r(x), \quad \deg(r) < \deg(d)$$

## Remainder Theorem

When dividing $f(x)$ by $(x - c)$, the remainder is $f(c)$.

**Corollary (Factor Theorem):** $(x - c)$ is a factor of $f(x)$ if and only if $f(c) = 0$.

## Long Division

To divide $2x^3 - 3x^2 + x - 5$ by $x - 2$:

1. Divide the leading term: $2x^3 \div x = 2x^2$
2. Multiply and subtract: $2x^3 - 3x^2 - (2x^3 - 4x^2) = x^2$
3. Bring down, repeat until remainder degree $< 1$

Result: $2x^2 + x + 3$ remainder $1$.

## Synthetic Division

A shorthand for dividing by $(x - c)$: write coefficients of $f$, use $c$ as the divisor, and apply the "multiply-and-add" sweep.

## Notes

- **Degree constraint:** the remainder $r(x)$ always has degree strictly less than the divisor $d(x)$.
- Polynomial division mirrors integer division: $f = dq + r$.
- The Factor Theorem gives an efficient root-checking procedure.

## Example

Is $(x - 3)$ a factor of $f(x) = x^3 - 6x^2 + 11x - 6$?

$$f(3) = 27 - 54 + 33 - 6 = 0 \checkmark$$

Yes — and by long division, $f(x) = (x-3)(x^2 - 3x + 2) = (x-3)(x-1)(x-2)$.
