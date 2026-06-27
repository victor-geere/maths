---
title: Improper Integrals
tag: calculus
summary: Integrals over unbounded intervals or with integrand singularities, evaluated as limits of proper integrals.
links:
  - riemann-integral
  - fundamental-theorem-calculus
  - convergence
---

# Improper Integrals

A **proper** Riemann integral requires the interval $[a,b]$ to be bounded and the integrand to be bounded on it. An **improper integral** relaxes one or both of these conditions: the interval may extend to infinity, or the integrand may blow up at one or more points. Rather than being undefined, such integrals are given meaning as **limits** of proper integrals. If the limit exists and is finite, the integral **converges**; otherwise it **diverges**. Improper integrals arise throughout probability theory (normalising distributions), Fourier analysis, and physics (computing potentials and energies).

## Type I: Infinite Limits

$$\int_a^\infty f(x)\,dx = \lim_{t\to\infty}\int_a^t f(x)\,dx$$

$$\int_{-\infty}^b f(x)\,dx = \lim_{t\to-\infty}\int_t^b f(x)\,dx$$

$$\int_{-\infty}^\infty f(x)\,dx = \int_{-\infty}^c f(x)\,dx + \int_c^\infty f(x)\,dx$$

(split at any finite $c$; both parts must converge).

## Type II: Vertical Asymptote

If $f$ has a singularity at $x = a$:

$$\int_a^b f(x)\,dx = \lim_{\varepsilon\to 0^+}\int_{a+\varepsilon}^b f(x)\,dx$$

Similarly for a singularity at $b$ or in the interior.

## Key Examples

**Convergent:** $\displaystyle\int_1^\infty \frac{1}{x^2}\,dx = \lim_{t\to\infty}\left[-\frac{1}{x}\right]_1^t = 0 - (-1) = 1$

**Divergent:** $\displaystyle\int_1^\infty \frac{1}{x}\,dx = \lim_{t\to\infty}\ln t = \infty$

**$p$-integral test:**

$$\int_1^\infty \frac{dx}{x^p} \begin{cases} \text{converges to } \frac{1}{p-1} & p > 1 \\ \text{diverges} & p \leq 1 \end{cases}$$

## Comparison Test

If $0 \leq f(x) \leq g(x)$ for all $x \geq a$:
- If $\int_a^\infty g\,dx$ converges, so does $\int_a^\infty f\,dx$.
- If $\int_a^\infty f\,dx$ diverges, so does $\int_a^\infty g\,dx$.

## Gaussian Integral

$$\int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt{\pi}$$

(proved using double integrals in polar coordinates — a famous result in probability).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Improper integral | integral over an unbounded domain or with an unbounded integrand |
| Proper integral | integral over a bounded interval with bounded integrand |
| Converges | the limit defining the integral is finite |
| Diverges | the limit is $\pm\infty$ or does not exist |
| $\lim_{t\to\infty}$ | limit as $t$ grows without bound |
| $\varepsilon \to 0^+$ | $\varepsilon$ approaches 0 from the right (positive side) |
| Vertical asymptote | a value where $|f(x)| \to \infty$ |
| $p$-integral | $\int_1^\infty x^{-p}\,dx$; converges iff $p > 1$ |
| Comparison test | bounds $f$ between two functions to determine convergence |
| Gaussian integral | $\int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt{\pi}$ |
| $e^{-x^2}$ | the Gaussian (bell curve) function |
