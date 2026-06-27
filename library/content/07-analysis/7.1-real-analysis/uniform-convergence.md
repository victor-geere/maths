---
title: Uniform Convergence
tag: analysis
summary: A stronger form of convergence for sequences of functions where the rate of convergence is the same at every point.
links:
  - convergence
  - continuity
  - limits
---

# Uniform Convergence

When a sequence of functions $f_n$ converges to a limit function $f$, there are two fundamentally different ways this can happen. In **pointwise convergence**, each fixed point $x$ has its own rate of convergence — the sequence $f_n(x)$ approaches $f(x)$, but some points may converge arbitrarily slowly. In **uniform convergence**, the entire sequence converges at a uniform rate across all points simultaneously: for any tolerance $\varepsilon > 0$, a single $N$ works for all $x$ at once. This distinction matters enormously: uniform convergence preserves continuity, allows interchange of limits with integrals, and is the correct notion for analysing approximation errors in numerical methods and Fourier series.

## Pointwise vs. Uniform Convergence

**Pointwise:** $f_n \to f$ pointwise if for each $x$, $\lim_{n\to\infty} f_n(x) = f(x)$.

**Uniform:** $f_n \to f$ uniformly on a set $S$ if:

$$\forall\,\varepsilon > 0,\; \exists\, N \in \mathbb{N} : \forall\, n \geq N,\; \forall\, x \in S,\quad |f_n(x) - f(x)| < \varepsilon$$

Equivalently:

$$\sup_{x \in S} |f_n(x) - f(x)| \to 0 \quad \text{as } n \to \infty$$

## Key Theorems

### Uniform Limit Theorem
If $f_n$ are all continuous on $S$ and $f_n \to f$ uniformly, then $f$ is also continuous.

(Pointwise convergence alone does not guarantee this — a limit of continuous functions can be discontinuous.)

### Integration
If $f_n \to f$ uniformly on $[a, b]$:

$$\lim_{n\to\infty}\int_a^b f_n(x)\,dx = \int_a^b f(x)\,dx$$

(Limit and integral can be swapped.)

### Differentiation
If $f_n \to f$ pointwise and $f_n' \to g$ **uniformly**, then $f$ is differentiable and $f' = g$.

## Example: Pointwise but Not Uniform

$f_n(x) = x^n$ on $[0, 1]$. Pointwise limit: $f(x) = 0$ for $x \in [0,1)$ and $f(1) = 1$.

Each $f_n$ is continuous, but $f$ is not. Hence convergence cannot be uniform on $[0,1]$.

Check: $\sup_{x\in[0,1]}|x^n - f(x)| \geq |(\tfrac{1}{2})^n \cdot 2^n - 0| \to \ldots$ — indeed the sup does not go to 0.

## Weierstrass M-Test

If $|f_n(x)| \leq M_n$ for all $x \in S$ and $\sum M_n < \infty$, then $\sum f_n$ converges uniformly on $S$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $f_n \to f$ | the sequence of functions $f_n$ converges to $f$ |
| Pointwise convergence | convergence at each fixed $x$ independently |
| Uniform convergence | convergence at the same rate for all $x$ simultaneously |
| $\varepsilon$ (epsilon) | an arbitrarily small positive tolerance |
| $N \in \mathbb{N}$ | a threshold index beyond which the bound holds |
| $\sup_{x \in S}$ | supremum over all points in $S$ |
| Uniform Limit Theorem | continuous functions converging uniformly have a continuous limit |
| Weierstrass M-test | sufficient condition for uniform convergence of a series of functions |
| $M_n$ | uniform bound on $|f_n(x)|$ for all $x$ |
| Pointwise limit | the function $f$ where $f(x) = \lim_n f_n(x)$ for each $x$ |
