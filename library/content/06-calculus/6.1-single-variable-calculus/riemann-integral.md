---
title: Riemann Integral
tag: calculus
summary: Area under a curve as the limit of rectangular approximations.
links:
  - fundamental-theorem-calculus
  - limits
  - continuity
---

## Key Formula

$$\int_a^b f(x)\,dx = \lim_{n\to\infty} \sum_{k=1}^{n} f(x_k^*)\,\Delta x, \qquad \Delta x = \frac{b-a}{n}$$

## Notes

Partition $[a,b]$ into $n$ sub-intervals of width $\Delta x$. Choose a **sample point** $x_k^*$ in each sub-interval $[x_{k-1}, x_k]$.

### Riemann sums

| Name | Sample point $x_k^*$ |
|---|---|
| Left | $x_{k-1}$ |
| Right | $x_k$ |
| Midpoint | $\frac{x_{k-1}+x_k}{2}$ |

The signed area is approximated by $S_n = \sum_{k=1}^n f(x_k^*)\Delta x$.

$f$ is **Riemann-integrable** on $[a,b]$ if $\lim_{n\to\infty} S_n$ exists independently of the partition and sample choices.

### Integrability criteria

- Every continuous function on $[a,b]$ is Riemann-integrable.
- Every monotone bounded function is Riemann-integrable.
- Functions with finitely many discontinuities are Riemann-integrable.

### Properties

$$\int_a^b [f(x)+g(x)]\,dx = \int_a^b f(x)\,dx + \int_a^b g(x)\,dx$$

$$\int_a^b f(x)\,dx + \int_b^c f(x)\,dx = \int_a^c f(x)\,dx$$

The [[fundamental-theorem-calculus|Fundamental Theorem]] converts this limit into a practical computation via antiderivatives. The Lebesgue integral extends Riemann integration to a broader class of functions using measure theory.
