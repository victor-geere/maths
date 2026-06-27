---
title: Roots of Polynomials
tag: algebra
summary: Fundamental theorem of algebra and factorisation over ℂ.
links:
  - complex-numbers
  - quadratic-formula
---

## Key Formula

$$p(x) = a_n \prod_{k=1}^{n}(x - r_k)$$

## Notes

**Fundamental Theorem of Algebra:** every non-constant polynomial with complex coefficients has at least one complex root, and therefore exactly $n$ roots (counted with multiplicity) over $\mathbb{C}$.

### Nature of roots

- Real coefficients $\Rightarrow$ [[complex-numbers|complex roots]] come in conjugate pairs
- Degree-1 (linear): always one real root
- Degree-2: [[quadratic-formula|quadratic formula]] gives exact roots
- Degree 3–4: cubic/quartic formulas exist but are unwieldy
- Degree $\geq 5$: no general closed form (Abel–Ruffini theorem)

### Vieta's Formulas

For $p(x) = x^n + a_{n-1}x^{n-1} + \cdots + a_0$ with roots $r_1, \ldots, r_n$:

$$\sum_{i} r_i = -a_{n-1}, \qquad \prod_{i} r_i = (-1)^n a_0$$

The elementary symmetric polynomials in the roots equal (up to sign) the coefficients.

### Multiplicity

If $(x - r)^k$ divides $p(x)$ but $(x-r)^{k+1}$ does not, $r$ is a root of **multiplicity $k$**. Geometrically, the graph of $p$ is tangent to the $x$-axis at $r$ (touching but not crossing) when $k$ is even.
