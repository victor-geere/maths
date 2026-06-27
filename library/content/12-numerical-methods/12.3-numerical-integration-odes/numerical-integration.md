---
title: Trapezoidal & Simpson's Rules
tag: numerical-methods
summary: Simple quadrature rules that approximate a definite integral by replacing the integrand with piecewise linear (trapezoidal) or piecewise quadratic (Simpson's) interpolants.
links:
  - riemann-integral
  - gaussian-quadrature
  - taylor-series
  - big-o-notation
---

# Trapezoidal & Simpson's Rules

**Numerical integration** (quadrature) approximates a definite integral $\int_a^b f(x)\,dx$ when an exact antiderivative is unavailable or impractical. The simplest rules replace $f$ by a polynomial interpolant on each sub-interval and integrate that polynomial exactly. The **Trapezoidal Rule** interpolates with line segments (degree 1), giving an error of order $O(h^2)$. **Simpson's Rule** uses parabolas (degree 2), gaining two extra orders of accuracy: $O(h^4)$. Both rules are composite — apply the basic formula to $n$ equal subintervals of width $h = (b-a)/n$ — and they underlie the numerical integration routines in every scientific computing package, from `scipy.integrate` to MATLAB's `integral`.

## Trapezoidal Rule

**Basic (one interval $[a,b]$):**

$$\int_a^b f(x)\,dx \approx \frac{b-a}{2}\bigl[f(a) + f(b)\bigr]$$

**Composite (n subintervals, $h = (b-a)/n$, $x_i = a + ih$):**

$$\int_a^b f(x)\,dx \approx h\left[\frac{f(x_0)}{2} + f(x_1) + \cdots + f(x_{n-1}) + \frac{f(x_n)}{2}\right]$$

**Error:** $-\dfrac{(b-a)^3}{12n^2}f''(\xi)$ for some $\xi \in (a,b)$; so $O(h^2)$.

## Simpson's Rule

**Basic (over two subintervals $[a, m, b]$ where $m = (a+b)/2$):**

$$\int_a^b f(x)\,dx \approx \frac{b-a}{6}\bigl[f(a) + 4f(m) + f(b)\bigr]$$

**Composite ($n$ even, $h = (b-a)/n$):**

$$\int_a^b f(x)\,dx \approx \frac{h}{3}\bigl[f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \cdots + 4f(x_{n-1}) + f(x_n)\bigr]$$

**Error:** $-\dfrac{(b-a)^5}{180n^4}f^{(4)}(\xi)$; so $O(h^4)$.

## Comparison

| Rule | Polynomial degree | Error order |
|---|---|---|
| Rectangle (midpoint) | 0 | $O(h^2)$ |
| Trapezoidal | 1 | $O(h^2)$ |
| Simpson's | 2 | $O(h^4)$ |
| Simpson's 3/8 | 3 | $O(h^4)$ |
| Boole's | 4 | $O(h^6)$ |

## Richardson Extrapolation

Combine two trapezoidal estimates with step sizes $h$ and $h/2$:

$$I \approx \frac{4 T(h/2) - T(h)}{3}$$

This cancels the leading error term and recovers Simpson's rule.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $h = (b-a)/n$ | step size (subinterval width) |
| $x_i = a + ih$ | quadrature nodes |
| $f(x_i)$ | function evaluations at nodes |
| Trapezoidal rule | piecewise-linear approximation; error $O(h^2)$ |
| Simpson's rule | piecewise-quadratic approximation; error $O(h^4)$ |
| Composite rule | applying a basic rule on each of $n$ subintervals |
| $O(h^k)$ | the error decreases as $h^k$ when $h \to 0$ |
| $f''(\xi)$ | second derivative at some unknown point $\xi$; appears in error bound |
| Richardson extrapolation | combining two estimates to cancel leading error |
| Quadrature | numerical integration |
| Convergence rate | how fast the error decreases as $n \to \infty$ (or $h \to 0$) |
