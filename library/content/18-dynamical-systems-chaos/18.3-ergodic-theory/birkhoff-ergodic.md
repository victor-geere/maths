---
title: Birkhoff's Ergodic Theorem
tag: dynamical-systems
summary: Birkhoff's ergodic theorem states that for a measure-preserving transformation, time averages of integrable functions converge almost everywhere to the conditional expectation on the invariant σ-algebra.
links:
  - measure-preserving
  - ergodicity
  - mixing-entropy
  - law-large-numbers
---

# Birkhoff's Ergodic Theorem

**Birkhoff's pointwise ergodic theorem** (1931) is the cornerstone of ergodic theory and the mathematical foundation of statistical mechanics. It states that for a measure-preserving transformation $T$ on $(X, \mu)$ and any $f \in L^1(\mu)$, the time average $\frac{1}{n}\sum_{k=0}^{n-1} f(T^k x)$ converges **almost everywhere** to a $T$-invariant function $f^*$. When $T$ is ergodic, $f^* = \int f\,d\mu$ — the time average equals the space average. This is the mathematical statement of the **ergodic hypothesis** in physics: given enough time, a system explores its energy surface uniformly, so time averages equal ensemble averages. The theorem generalises the strong law of large numbers (for i.i.d. random variables, the shift on $\{0,1\}^{\mathbb{N}}$ is the Bernoulli shift).

## Statement

**Theorem (Birkhoff, 1931)**: Let $(X, \mathcal{B}, \mu, T)$ be a measure-preserving system and $f \in L^1(X, \mu)$. Then the time average:
$$f^*(x) = \lim_{n \to \infty} \frac{1}{n} \sum_{k=0}^{n-1} f(T^k x)$$
exists for $\mu$-a.e. $x \in X$, and $f^* \in L^1(\mu)$ with $\int f^*\,d\mu = \int f\,d\mu$.

Furthermore, $f^*$ is $T$-invariant: $f^* \circ T = f^*$ a.e.

**Ergodic case**: If $T$ is ergodic, then $f^*(x) = \int f\,d\mu$ for $\mu$-a.e. $x$.

## Corollaries

- **Poincaré recurrence**: take $f = \mathbf{1}_A$; then $f^* = \mu(A)$ a.e. (if ergodic), so a.e. orbit hits $A$ a fraction $\mu(A)$ of the time.
- **Normal numbers**: Lebesgue-a.e. real number has each digit $0,\ldots,9$ appearing with frequency $1/10$.

## Comparison with Mean Ergodic Theorem

| Theorem | Convergence | Space |
|---|---|---|
| Birkhoff (pointwise) | a.e. pointwise | $L^1$ |
| von Neumann (mean) | $L^2$-norm | $L^2$ |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\frac{1}{n}\sum_{k=0}^{n-1} f(T^k x)$ | time average of $f$ along orbit of $x$ |
| $f^*(x)$ | limit of time averages; a.e. defined |
| $T$-invariant function | $f^* \circ T = f^*$ a.e. |
| $L^1(\mu)$ | integrable functions: $\int |f|\,d\mu < \infty$ |
| Ergodic hypothesis | time average $=$ space average (physics formulation) |
| Normal number | every digit sequence occurs with correct frequency |
| Pointwise convergence | limit holds at each point (a.e.) |
| $L^2$-convergence | convergence in mean square; weaker than pointwise |
| Conditional expectation $\mathbb{E}[f|\mathcal{I}]$ | projection onto $T$-invariant functions |
