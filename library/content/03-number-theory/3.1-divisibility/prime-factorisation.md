---
title: Prime Numbers & Unique Factorisation
tag: number-theory
summary: Primes as the atoms of multiplication and the Fundamental Theorem of Arithmetic.
links:
  - divisibility-rules
  - sieve-eratosthenes
  - euclids-algorithm
---

## Primes

A natural number $p > 1$ is **prime** if its only positive divisors are $1$ and $p$ itself.

A number $n > 1$ that is not prime is **composite**.

The first primes: $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, \ldots$

## Fundamental Theorem of Arithmetic

Every integer $n > 1$ can be written **uniquely** (up to order) as a product of primes:

$$n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}, \quad p_1 < p_2 < \cdots < p_k \text{ prime},\; a_i \geq 1$$

## Infinitely Many Primes (Euclid)

**Proof:** Suppose there are finitely many primes $p_1, \ldots, p_k$. Let $N = p_1 p_2 \cdots p_k + 1$. Then $N$ is divisible by some prime $p$; but $p \neq p_i$ for any $i$ (each $p_i$ leaves remainder 1). Contradiction. $\square$

## GCD and LCM via Factorisation

If $a = \prod p_i^{a_i}$ and $b = \prod p_i^{b_i}$:

$$\gcd(a,b) = \prod p_i^{\min(a_i,b_i)}, \qquad \text{lcm}(a,b) = \prod p_i^{\max(a_i,b_i)}$$

$$\gcd(a,b) \cdot \text{lcm}(a,b) = ab$$

## Notes

- Primes are the **multiplicative atoms**: every positive integer is a unique product of primes.
- The prime factorisation of $n$ can be found in $O(\sqrt{n})$ trial divisions.
- Efficient factorisation of large numbers is computationally hard (basis of RSA cryptography).
