---
title: Convergence of Series
tag: analysis
summary: Tests for whether an infinite series has a finite sum.
links:
  - limits
  - taylor-series
---

## Key Formula

$$\sum_{n=1}^{\infty} a_n = L \iff S_N = \sum_{n=1}^{N} a_n \xrightarrow{N\to\infty} L$$

## Notes

A series **converges** if its sequence of partial sums $S_N$ approaches a finite limit $L$.

### Convergence tests

| Test | Condition for convergence |
|---|---|
| **Geometric** | $\|r\| < 1$ → sum $= \frac{a}{1-r}$ |
| **Ratio** | $\displaystyle\lim_{n\to\infty}\left\|\frac{a_{n+1}}{a_n}\right\| < 1$ |
| **Root** | $\displaystyle\lim_{n\to\infty}\|a_n\|^{1/n} < 1$ |
| **Integral** | $\int_1^\infty f(x)\,dx$ converges, where $f(n) = a_n$ |
| **Alternating (Leibniz)** | $\|a_n\| \searrow 0$ monotonically |
| **Comparison** | $0 \leq a_n \leq b_n$ and $\sum b_n$ converges |
| **$p$-series** | $\sum \frac{1}{n^p}$ converges iff $p > 1$ |

### Absolute vs. conditional convergence

- $\sum a_n$ **converges absolutely** if $\sum |a_n| < \infty$
- **Conditional convergence:** $\sum a_n$ converges but $\sum |a_n| = \infty$

The **Riemann rearrangement theorem** states that a conditionally convergent series can be rearranged to converge to *any* real number — or to diverge.

### Radius of convergence

For a power series $\sum c_n (x-a)^n$, the **radius of convergence** is:

$$R = \frac{1}{\displaystyle\limsup_{n\to\infty}|c_n|^{1/n}}$$

The series converges absolutely for $|x-a| < R$ and diverges for $|x-a| > R$. Behaviour at $|x-a| = R$ must be checked separately.

[[taylor-series|Taylor series]] are power series whose $c_n = \frac{f^{(n)}(a)}{n!}$.
