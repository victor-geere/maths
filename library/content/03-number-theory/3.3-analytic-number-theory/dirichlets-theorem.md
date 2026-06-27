---
title: Dirichlet's Theorem on Primes in AP
tag: analytic-number-theory
summary: Every arithmetic progression a, a+d, a+2d, … with gcd(a,d)=1 contains infinitely many primes.
links:
  - prime-number-theorem
  - prime-counting
  - eulers-totient
---

## Statement

If $a, d$ are positive integers with $\gcd(a, d) = 1$, then there are **infinitely many primes** of the form:

$$a, \quad a + d, \quad a + 2d, \quad a + 3d, \quad \ldots$$

Moreover, the primes in each such progression have equal **asymptotic density**:

$$\pi(x; d, a) = \#\{p \leq x : p \equiv a \pmod{d}\} \sim \frac{1}{\phi(d)} \cdot \frac{x}{\ln x}$$

so primes are equidistributed across the $\phi(d)$ valid residue classes mod $d$.

## Key Tool: Dirichlet L-Functions

For a Dirichlet character $\chi \pmod{d}$:

$$L(s, \chi) = \sum_{n=1}^\infty \frac{\chi(n)}{n^s} = \prod_{p} \frac{1}{1 - \chi(p)p^{-s}}$$

The proof shows $L(1, \chi) \neq 0$ for non-principal characters — this is the analytic heart of the argument.

## Examples

- $d = 4$: primes $\equiv 1 \pmod{4}$ (e.g. 5, 13, 17, 29, …) and $\equiv 3 \pmod{4}$ (e.g. 3, 7, 11, 19, …) — both infinite.
- $d = 10$: primes end in 1, 3, 7, or 9 — each class is infinite and asymptotically $\tfrac{1}{4}$ of all primes.

## Coprimality is Necessary

If $\gcd(a, d) = g > 1$, then every term $a + nd$ is divisible by $g$, so at most one term can be prime.

## Notes

- Proved by Dirichlet in 1837, it was the first major theorem to use analytic methods (L-functions) to prove a purely arithmetic result.
- The equidistribution result is sometimes called the **Generalised Prime Number Theorem** for arithmetic progressions.
- The **Generalised Riemann Hypothesis** (GRH) would sharpen the error term significantly.
