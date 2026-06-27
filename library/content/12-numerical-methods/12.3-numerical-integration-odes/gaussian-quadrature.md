---
title: Gaussian Quadrature
tag: numerical-methods
summary: Optimal quadrature rules that choose both node positions and weights to exactly integrate polynomials of the highest possible degree for a given number of evaluations.
links:
  - numerical-integration
  - orthogonality
  - legendre-polynomials
---

# Gaussian Quadrature

**Gaussian quadrature** is the most accurate numerical integration method for smooth functions: with $n$ function evaluations, it exactly integrates polynomials of degree up to $2n-1$. The key insight is that both the **positions** (nodes) and **weights** of the quadrature rule are free to be chosen optimally, rather than being fixed at evenly-spaced points as in the trapezoidal and Simpson's rules. The optimal nodes turn out to be the **roots of orthogonal polynomials** (Legendre polynomials on $[-1,1]$, Chebyshev, Hermite, or Laguerre polynomials for other weight functions). Gaussian quadrature achieves exponential convergence for analytic integrands, making it the method of choice in finite-element codes, computational physics, and spectral methods.

## Gauss–Legendre Quadrature on $[-1,1]$

$$\int_{-1}^1 f(x)\,dx \approx \sum_{i=1}^n w_i f(x_i)$$

- **Nodes** $x_1, \ldots, x_n$: roots of the Legendre polynomial $P_n(x)$
- **Weights** $w_i = \dfrac{2}{(1-x_i^2)[P_n'(x_i)]^2}$
- **Exact** for all polynomials of degree $\leq 2n-1$
- **Error:** $\dfrac{2^{2n+1}(n!)^4}{(2n+1)[(2n)!]^3}f^{(2n)}(\xi)$ for some $\xi \in (-1,1)$

## Changing Interval

To integrate over $[a,b]$, substitute $x = \frac{a+b}{2} + \frac{b-a}{2}t$:

$$\int_a^b f(x)\,dx = \frac{b-a}{2}\int_{-1}^1 f\!\left(\frac{a+b}{2} + \frac{b-a}{2}t\right)dt \approx \frac{b-a}{2}\sum_{i=1}^n w_i f(x_i^{[a,b]})$$

## Nodes and Weights (Small $n$)

| $n$ | Nodes $x_i$ | Weights $w_i$ |
|---|---|---|
| 1 | $0$ | $2$ |
| 2 | $\pm 1/\sqrt{3}$ | $1, 1$ |
| 3 | $0,\, \pm\sqrt{3/5}$ | $8/9,\, 5/9,\, 5/9$ |

## Variants for Other Weight Functions

| Rule | Weight | Interval |
|---|---|---|
| Gauss–Legendre | $1$ | $[-1,1]$ |
| Gauss–Chebyshev | $1/\sqrt{1-x^2}$ | $(-1,1)$ |
| Gauss–Hermite | $e^{-x^2}$ | $(-\infty,\infty)$ |
| Gauss–Laguerre | $e^{-x}$ | $[0,\infty)$ |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $x_i$ | quadrature nodes (positions of function evaluations) |
| $w_i$ | quadrature weights |
| $P_n(x)$ | Legendre polynomial of degree $n$ |
| $n$ | number of quadrature points |
| $2n-1$ | degree of polynomials exactly integrated by $n$-point Gauss rule |
| Weight function | $w(x)$ appearing in $\int w(x)f(x)\,dx$; determines the family of orthogonal polynomials |
| Gauss–Legendre | the standard rule on $[-1,1]$ with weight $w=1$ |
| Exponential convergence | error decreases as $e^{-cn}$ for analytic $f$; much faster than $O(h^k)$ |
| Spectral method | numerical PDE method using Gaussian quadrature and global polynomials |
