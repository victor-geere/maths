---
title: Runge–Kutta Methods
tag: numerical-methods
summary: Higher-order ODE solvers that evaluate the derivative at multiple intermediate points within each step to achieve much better accuracy than Euler's method at the same cost.
links:
  - eulers-method
  - systems-odes
  - taylor-series
  - big-o-notation
---

# Runge–Kutta Methods

**Runge–Kutta (RK) methods** are a family of numerical ODE solvers that achieve higher-order accuracy than Euler's method by evaluating the derivative $f(x, y)$ at several carefully chosen intermediate points within each step, then combining these evaluations with optimal weights. The most widely used is the **classical fourth-order Runge–Kutta (RK4)** method, which achieves $O(h^5)$ local error and $O(h^4)$ global error using four function evaluations per step — a remarkable balance of accuracy and cost. Developed by Carl Runge (1895) and Wilhelm Kutta (1901), RK methods are the default ODE solvers in scientific computing environments and are implemented in Python's `scipy.integrate.solve_ivp`, MATLAB's `ode45`, and countless other tools.

## Classical RK4

For $y' = f(x,y)$, one step from $(x_n, y_n)$ to $(x_{n+1}, y_{n+1})$:

$$k_1 = f(x_n,\; y_n)$$
$$k_2 = f\!\left(x_n + \tfrac{h}{2},\; y_n + \tfrac{h}{2}k_1\right)$$
$$k_3 = f\!\left(x_n + \tfrac{h}{2},\; y_n + \tfrac{h}{2}k_2\right)$$
$$k_4 = f\!\left(x_n + h,\; y_n + hk_3\right)$$

$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

The weights $\tfrac{1}{6}(1,2,2,1)$ are designed so that $y_{n+1}$ matches the Taylor series up to $O(h^5)$ (local truncation error).

## Error and Cost Comparison

| Method | Order | LTE | Function evals/step |
|---|---|---|---|
| Euler | 1 | $O(h^2)$ | 1 |
| RK2 (midpoint/Heun) | 2 | $O(h^3)$ | 2 |
| RK4 | 4 | $O(h^5)$ | 4 |

RK4 achieves accuracy comparable to 40 Euler steps with just 4 function evaluations.

## Adaptive Step-Size Control

**RK45** (Dormand–Prince) embeds a 4th-order and 5th-order estimate in the same 6 function evaluations. The difference estimates the local error, which is used to adapt $h$:

- If error $>$ tolerance: reject step, halve $h$
- If error $\ll$ tolerance: increase $h$ for efficiency

## General Butcher Tableau

An $s$-stage RK method is defined by a **Butcher tableau** $(c, A, b)$:

$$k_i = f\!\left(x_n + c_i h,\; y_n + h\sum_{j=1}^s a_{ij}k_j\right), \quad y_{n+1} = y_n + h\sum_{i=1}^s b_i k_i$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $k_1, k_2, k_3, k_4$ | stage derivatives at intermediate points |
| $h$ | step size |
| $y_{n+1} = y_n + \frac{h}{6}(k_1+2k_2+2k_3+k_4)$ | RK4 update formula |
| Order | the power of $h$ in the global error; RK4 has order 4 |
| LTE | local truncation error: $O(h^5)$ for RK4 |
| Global error | $O(h^4)$ for RK4; one order less than LTE |
| RK45 | adaptive embedded pair; standard in `scipy.solve_ivp` |
| Butcher tableau | compact representation of a Runge–Kutta method |
| Adaptive step | automatically adjusts $h$ to meet an error tolerance |
| Stiff ODE | requires implicit methods (RK4 may need very small $h$) |
| Stage | an intermediate evaluation of $f$ within one step |
