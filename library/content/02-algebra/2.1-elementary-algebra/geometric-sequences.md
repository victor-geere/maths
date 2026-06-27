---
title: Geometric Sequences
tag: algebra
summary: Sequences with a constant ratio between consecutive terms.
links:
  - arithmetic-sequences
  - convergence
  - binomial-theorem
---

## Definition

A sequence $(a_n)$ is **geometric** with **common ratio** $r \neq 0$ if:

$$a_n = a_{n-1} \cdot r \quad \text{for all } n \geq 2$$

## General Term

$$a_n = a_1 \cdot r^{n-1}$$

## Sum of First $n$ Terms

$$S_n = a_1 \cdot \frac{1 - r^n}{1 - r} \quad (r \neq 1)$$

When $r = 1$: $S_n = n a_1$.

## Infinite Geometric Series

If $|r| < 1$, the series converges:

$$S_\infty = \sum_{n=1}^\infty a_1 r^{n-1} = \frac{a_1}{1-r}$$

If $|r| \geq 1$ (and $r \neq 1$), the series diverges.

## Example

Sequence: $2, 6, 18, 54, \ldots$ ($a_1 = 2$, $r = 3$).

- $a_5 = 2 \cdot 3^4 = 162$
- $S_5 = 2 \cdot \tfrac{1-243}{1-3} = 242$

Infinite series: $1 + \tfrac{1}{2} + \tfrac{1}{4} + \cdots = \tfrac{1}{1 - 1/2} = 2$.

## Geometric Mean

For three terms in GP: $a, b, c$ geometric $\iff b^2 = ac$ (equivalently $b = \sqrt{ac}$ for positive terms).

## Notes

- Geometric sequences model exponential growth or decay.
- The ratio test for series convergence generalises the geometric series idea.
