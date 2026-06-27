---
title: Euclid's Algorithm
tag: number-theory
summary: Efficient computation of gcd(a, b) by repeated remainder.
links:
  - modular-arithmetic
  - bezouts-identity
---

## Key Formula

$$\gcd(a,b) = \gcd(b,\; a \bmod b)$$

## Notes

Euclid's algorithm is one of the oldest known algorithms (~300 BCE) and remains one of the most efficient.

### Algorithm

```
gcd(a, b):
  while b ≠ 0:
    (a, b) ← (b, a mod b)
  return a
```

### Example: gcd(252, 105)

| $a$ | $b$ | $a \bmod b$ |
|---|---|---|
| 252 | 105 | 42 |
| 105 | 42 | 21 |
| 42 | 21 | 0 |
| 21 | 0 | — |

$\gcd(252, 105) = 21$.

### Correctness

$\gcd(a,b) = \gcd(b, a \bmod b)$ because any common divisor of $a$ and $b$ also divides $a \bmod b = a - \lfloor a/b \rfloor b$, and vice versa.

### Complexity

$O(\log \min(a,b))$ divisions. The worst case is consecutive Fibonacci numbers.

### Extended Euclidean algorithm

Backtracking through the steps gives integers $s, t$ such that $as + bt = \gcd(a,b)$ — see [[bezouts-identity|Bézout's identity]].

This is used to compute modular inverses: if $\gcd(a,n) = 1$, then $as \equiv 1 \pmod{n}$ so $a^{-1} \equiv s \pmod{n}$.
