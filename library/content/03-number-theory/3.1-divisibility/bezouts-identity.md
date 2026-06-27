---
title: Bézout's Identity
tag: number-theory
summary: gcd(a,b) = sa + tb — the foundation of modular inverses.
links:
  - euclids-algorithm
  - modular-arithmetic
---

## Key Formula

$$\gcd(a,b) = sa + tb, \qquad s,t \in \mathbb{Z}$$

## Notes

For any integers $a, b$ (not both zero), there exist integers $s$ and $t$ — called **Bézout coefficients** — such that $sa + tb = \gcd(a,b)$.

The coefficients $s,t$ are **not unique**: $(s + kb/d,\; t - ka/d)$ is also a solution for any $k \in \mathbb{Z}$, where $d = \gcd(a,b)$.

### Computing $s$ and $t$

The **extended Euclidean algorithm** back-substitutes through the steps of [[euclids-algorithm|Euclid's algorithm]]:

**Example:** find $s,t$ such that $252s + 105t = 21$.

Back-substitute from $\gcd(252,105) = 21$:

$$21 = 42 - 1\cdot 21 = 42 - (105 - 2\cdot 42) = 3\cdot 42 - 105 = 3(252-2\cdot 105) - 105 = 3\cdot 252 - 7\cdot 105$$

So $s = 3$, $t = -7$.

### Modular inverse

$a$ has a multiplicative inverse mod $n$ **iff** $\gcd(a,n) = 1$.

When it exists: from $sa + tn = 1$, reducing mod $n$ gives $sa \equiv 1 \pmod{n}$, so $a^{-1} \equiv s \pmod{n}$.

### Application: RSA key generation

RSA relies on finding $e \cdot d \equiv 1 \pmod{\phi(n)}$, i.e. computing $d = e^{-1} \bmod \phi(n)$ using the extended Euclidean algorithm. This is the [[modular-arithmetic|modular]] inverse.
