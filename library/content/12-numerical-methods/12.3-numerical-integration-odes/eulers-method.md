---
title: Euler's Method
tag: numerical-methods
summary: The simplest numerical ODE solver — approximate the solution by following the tangent line (the derivative) forward in small steps from an initial value.
links:
  - separable-odes
  - runge-kutta
  - taylor-series
  - big-o-notation
---

# Euler's Method

**Euler's method** is the simplest numerical algorithm for solving initial value problems (IVPs) for ordinary differential equations. Given $y' = f(x, y)$ with initial condition $y(x_0) = y_0$, it advances the solution by repeatedly following the tangent line: from $(x_n, y_n)$, move forward a step $h$ using the slope $f(x_n, y_n)$. Though only first-order accurate and rarely used in production (higher-order methods are far more efficient), Euler's method is the conceptual foundation for all numerical ODE solvers and provides an accessible entry point to the theory of numerical integration of differential equations.

## Algorithm

**Input:** $f(x,y)$, initial condition $y_0 = y(x_0)$, step size $h$, end point $x_N$.

For $n = 0, 1, 2, \ldots, N-1$:

$$x_{n+1} = x_n + h$$

$$y_{n+1} = y_n + h\,f(x_n, y_n)$$

## Derivation

From the Taylor series: $y(x+h) = y(x) + hy'(x) + \frac{h^2}{2}y''(x) + \cdots$

Euler's method keeps only the linear term: $y_{n+1} \approx y_n + h f(x_n, y_n)$.

## Error Analysis

**Local truncation error (LTE):** error made in one step:

$$\text{LTE} = \frac{h^2}{2}y''(\xi_n) = O(h^2)$$

**Global error:** accumulated over $N = (x_N - x_0)/h$ steps:

$$|y(x_N) - y_N| \leq Ch \quad \text{(first-order method)}$$

Halving $h$ halves the global error.

## Example

Solve $y' = y$, $y(0) = 1$ with $h = 0.1$ (exact: $y = e^x$):

| $n$ | $x_n$ | $y_n$ | $e^{x_n}$ | Error |
|---|---|---|---|---|
| 0 | 0.0 | 1.0000 | 1.0000 | 0 |
| 1 | 0.1 | 1.1000 | 1.1052 | 0.0052 |
| 2 | 0.2 | 1.2100 | 1.2214 | 0.0114 |

## Implicit (Backward) Euler

$$y_{n+1} = y_n + h\,f(x_{n+1}, y_{n+1})$$

Requires solving for $y_{n+1}$ (an implicit equation), but is **unconditionally stable** for stiff problems.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $y' = f(x,y)$ | the ODE (first-order, explicit) |
| $y_0 = y(x_0)$ | initial condition |
| $h$ | step size |
| $y_{n+1} = y_n + hf(x_n,y_n)$ | Euler's method update |
| LTE | local truncation error: $O(h^2)$ per step for Euler |
| Global error | total accumulated error: $O(h)$ for Euler |
| First-order method | global error $= O(h)$; halving $h$ halves the error |
| Stiff ODE | ODE with very different time scales; explicit Euler may require tiny $h$ |
| Implicit Euler | backward Euler: uses $f(x_{n+1}, y_{n+1})$; stable for stiff problems |
| Taylor expansion | source of Euler's formula and error analysis |
