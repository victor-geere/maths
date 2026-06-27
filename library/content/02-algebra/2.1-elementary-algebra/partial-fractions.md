---
title: Partial Fractions
tag: algebra
summary: Decomposing rational functions into simpler fractions for integration and analysis.
links:
  - polynomial-division
  - polynomial-roots
---

## Definition

A **partial fraction decomposition** rewrites a proper rational function $\frac{p(x)}{q(x)}$ (where $\deg p < \deg q$) as a sum of simpler fractions.

## Cases

### Distinct Linear Factors

$$\frac{p(x)}{(x-a)(x-b)} = \frac{A}{x-a} + \frac{B}{x-b}$$

### Repeated Linear Factor

$$\frac{p(x)}{(x-a)^n} = \frac{A_1}{x-a} + \frac{A_2}{(x-a)^2} + \cdots + \frac{A_n}{(x-a)^n}$$

### Irreducible Quadratic Factor

$$\frac{p(x)}{x^2+bx+c} = \frac{Ax+B}{x^2+bx+c}$$

## Method

1. Ensure degree of numerator $<$ degree of denominator (perform polynomial division first if not).
2. Factor the denominator fully over $\mathbb{R}$.
3. Write the decomposition with unknown numerators.
4. Multiply through and equate coefficients (or substitute convenient values of $x$).

## Example

$$\frac{3x+1}{(x-1)(x+2)} = \frac{A}{x-1} + \frac{B}{x+2}$$

Multiply both sides by $(x-1)(x+2)$:

$$3x+1 = A(x+2) + B(x-1)$$

- $x=1$: $4 = 3A \Rightarrow A = \tfrac{4}{3}$
- $x=-2$: $-5 = -3B \Rightarrow B = \tfrac{5}{3}$

$$\frac{3x+1}{(x-1)(x+2)} = \frac{4/3}{x-1} + \frac{5/3}{x+2}$$

## Notes

- Partial fractions are essential for integrating rational functions.
- The decomposition is unique once the denominator is fully factored.
