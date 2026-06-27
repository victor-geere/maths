---
title: Modular Arithmetic
tag: number-theory
summary: Arithmetic on remainders; ℤ/nℤ is a ring, a field when n is prime.
links:
  - euclids-algorithm
  - bezouts-identity
---

## Key Formula

$$a \equiv b \pmod{n} \iff n \mid (a - b)$$

## Notes

Two integers are **congruent mod $n$** if they have the same remainder when divided by $n$ — equivalently, their difference is divisible by $n$.

Congruence is an equivalence relation. The equivalence classes $\{0, 1, \ldots, n-1\}$ form the ring $\mathbb{Z}/n\mathbb{Z}$.

### Arithmetic rules

$$a \equiv a' \pmod{n} \;\text{ and }\; b \equiv b' \pmod{n}$$
$$\implies a+b \equiv a'+b' \pmod{n}, \quad ab \equiv a'b' \pmod{n}$$

### When is $\mathbb{Z}/n\mathbb{Z}$ a field?

$\mathbb{Z}/n\mathbb{Z}$ is a field (every nonzero element has a multiplicative inverse) **iff $n$ is prime**.

For general $n$, $a$ has an inverse mod $n$ iff $\gcd(a,n) = 1$. The inverse is found via the [[euclids-algorithm|extended Euclidean algorithm]].

### Fermat's little theorem

For prime $p$ and $\gcd(a,p)=1$:

$$a^{p-1} \equiv 1 \pmod{p}$$

Used in RSA and primality testing.

### Chinese Remainder Theorem (CRT)

If $n_1, n_2, \ldots, n_k$ are pairwise coprime, the system

$$x \equiv a_1 \pmod{n_1}, \quad x \equiv a_2 \pmod{n_2}, \quad \ldots$$

has a unique solution mod $n_1 n_2 \cdots n_k$.

CRT is used to break computations modulo a large number into smaller modular computations.
