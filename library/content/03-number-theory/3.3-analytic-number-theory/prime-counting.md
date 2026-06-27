---
title: Prime Counting Function π(x)
tag: analytic-number-theory
summary: The function counting primes up to x, and estimates of its growth.
links:
  - prime-number-theorem
  - prime-factorisation
  - sieve-eratosthenes
---

## Definition

$$\pi(x) = \#\{p \leq x : p \text{ prime}\}$$

## Small Values

| $x$ | $\pi(x)$ |
|---|---|
| 10 | 4 |
| 100 | 25 |
| 1,000 | 168 |
| 10,000 | 1,229 |
| 1,000,000 | 78,498 |

## The Prime Number Theorem

$$\pi(x) \sim \frac{x}{\ln x} \quad \text{as } x \to \infty$$

meaning $\pi(x) \cdot \frac{\ln x}{x} \to 1$.

A better approximation uses the **logarithmic integral**:

$$\pi(x) \approx \text{Li}(x) = \int_2^x \frac{dt}{\ln t}$$

## Chebyshev Functions

Two auxiliary functions that are easier to work with analytically:

$$\theta(x) = \sum_{p \leq x} \ln p, \qquad \psi(x) = \sum_{p^k \leq x} \ln p$$

The PNT is equivalent to $\psi(x) \sim x$.

## Bertrand's Postulate

For every $n \geq 1$, there is a prime $p$ with $n < p \leq 2n$.

Equivalent to the rough bound $\pi(2n) > \pi(n)$ for all $n$.

## Notes

- Computing $\pi(x)$ for large $x$ uses the **Meissel–Lehmer** method: $O(x^{2/3}/\log x)$ time.
- The error term in $\pi(x) - \text{Li}(x)$ is intimately connected to the zeros of the Riemann zeta function.
