---
title: Binomial Theorem
tag: algebra
summary: Expanding powers of a binomial sum using combinatorial coefficients.
links:
  - arithmetic-sequences
  - geometric-sequences
  - mathematical-induction
---

## Statement

For $n \in \mathbb{N}$ and any $a, b$:

$$(a + b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$$

where the **binomial coefficient** is:

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$$

## Pascal's Triangle

The coefficients for successive powers form Pascal's triangle:

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

Row $n$: $1, n, \binom{n}{2}, \ldots, n, 1$.

## Common Expansions

$$(a+b)^2 = a^2 + 2ab + b^2$$
$$(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$$
$$(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$$

## General Term

The $(k+1)$-th term (counting from $k=0$) in $(a+b)^n$ is:

$$T_{k+1} = \binom{n}{k} a^{n-k} b^k$$

## Example

Expand $(2x - 3)^4$:

$$\sum_{k=0}^4 \binom{4}{k}(2x)^{4-k}(-3)^k = 16x^4 - 96x^3 + 216x^2 - 216x + 81$$

## Notes

- Setting $a = b = 1$: $\sum_{k=0}^n \binom{n}{k} = 2^n$.
- Setting $a = 1, b = -1$: $\sum_{k=0}^n (-1)^k \binom{n}{k} = 0$.
- The generalised binomial theorem extends to non-integer $n$ as a power series.
