---
title: Riemann Hypothesis (Overview)
tag: analytic-number-theory
summary: The conjecture that all non-trivial zeros of ζ(s) lie on the critical line Re(s) = 1/2.
links:
  - prime-number-theorem
  - prime-counting
  - dirichlets-theorem
---

## The Riemann Zeta Function

For $\text{Re}(s) > 1$:

$$\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s} = \prod_{p \text{ prime}} \frac{1}{1-p^{-s}}$$

The **Euler product** (right-hand side) encodes the distribution of primes.

By analytic continuation, $\zeta(s)$ extends to all $s \in \mathbb{C}$ except $s = 1$ (simple pole).

## Zeros of $\zeta(s)$

- **Trivial zeros:** $s = -2, -4, -6, \ldots$ (negative even integers)
- **Non-trivial zeros:** complex numbers $\rho$ with $0 < \text{Re}(\rho) < 1$ (the **critical strip**)

The **functional equation** $\zeta(s) = 2^s \pi^{s-1} \sin(\tfrac{\pi s}{2}) \Gamma(1-s) \zeta(1-s)$ shows zeros come in pairs $\rho$ and $1-\rho$.

## The Hypothesis

**Riemann Hypothesis (1859):** All non-trivial zeros $\rho$ of $\zeta(s)$ satisfy $\text{Re}(\rho) = \tfrac{1}{2}$.

The line $\text{Re}(s) = \tfrac{1}{2}$ is called the **critical line**.

## Status

- Over $10^{13}$ non-trivial zeros have been numerically verified to lie on the critical line.
- The hypothesis remains **unproven** — one of the Millennium Prize Problems (\$1 million prize).

## Consequences if True

- The prime counting function satisfies: $\pi(x) = \text{Li}(x) + O(\sqrt{x}\ln x)$
- Gaps between primes are tightly controlled.
- Improved bounds in many areas of analytic number theory and cryptography.

## Notes

- The hypothesis was originally stated by Bernhard Riemann in his 1859 paper *Über die Anzahl der Primzahlen unter einer gegebenen Größe*.
- Generalisations (GRH) extend the conjecture to Dirichlet $L$-functions and other $L$-functions.
