---
title: Prime Number Theorem
tag: analytic-number-theory
summary: "The asymptotic density of primes: π(x) ~ x/ln(x)."
links:
  - prime-counting
  - riemann-hypothesis
  - dirichlets-theorem
---

## Statement

$$\lim_{x \to \infty} \frac{\pi(x)}{x / \ln x} = 1$$

Equivalently, the $n$-th prime $p_n$ satisfies $p_n \sim n \ln n$.

## History

- **Gauss** and **Legendre** conjectured the result (late 18th century) from empirical data.
- **Hadamard** and **de la Vallée-Poussin** independently proved it in 1896 using complex analysis.
- An **elementary proof** (without complex analysis) was given by Selberg and Erdős in 1948.

## Proof Strategy (Analytic)

1. Relate $\pi(x)$ to the Chebyshev function $\psi(x) = \sum_{p^k \leq x} \ln p$.
2. Connect $\psi(x)$ to the Riemann zeta function via the **explicit formula**:

$$\psi(x) = x - \sum_\rho \frac{x^\rho}{\rho} - \ln(2\pi)$$

where the sum runs over non-trivial zeros $\rho$ of $\zeta(s)$.

3. Show that $\zeta(s) \neq 0$ on the line $\text{Re}(s)=1$ to conclude $\psi(x) \sim x$.

## Error Term

The best known bound is:

$$\pi(x) = \text{Li}(x) + O\!\left(x \exp\bigl(-c\sqrt{\ln x}\bigr)\right)$$

Under the **Riemann Hypothesis**, the error improves to $O(\sqrt{x}\ln x)$.

## Consequences

- On average, the gap between primes near $x$ is $\approx \ln x$.
- Primes become sparser but never stop (infinitely many primes).
