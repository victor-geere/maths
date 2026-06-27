---
title: Constant-Coefficient Linear ODEs
tag: ode
summary: Higher-order linear ODEs with constant coefficients solved via the characteristic equation, whose roots determine exponential, oscillatory, or resonant solutions.
links:
  - linear-first-order
  - undetermined-coefficients
  - laplace-transform
---

# Constant-Coefficient Linear ODEs

A **constant-coefficient linear ODE** is a higher-order linear differential equation in which the coefficients of $y, y', y'', \ldots$ are all constants:

$$a_n y^{(n)} + a_{n-1}y^{(n-1)} + \cdots + a_1 y' + a_0 y = f(x)$$

These equations arise throughout physics and engineering: the simple harmonic oscillator ($y'' + \omega^2 y = 0$), damped oscillator, RLC circuits, and mechanical vibrations. The strategy is to guess exponential solutions $y = e^{rx}$, substitute, and solve the resulting polynomial — the **characteristic equation** — for $r$. The structure of the roots (real distinct, repeated, or complex) completely determines the form of the general homogeneous solution.

## Characteristic Equation

For the homogeneous equation $a_n y^{(n)} + \cdots + a_0 y = 0$, substitute $y = e^{rx}$:

$$a_n r^n + a_{n-1}r^{n-1} + \cdots + a_1 r + a_0 = 0$$

## Solution by Root Type (2nd order: $y'' + by' + cy = 0$)

Characteristic equation: $r^2 + br + c = 0$, with roots $r_{1,2} = \frac{-b \pm \sqrt{b^2-4c}}{2}$.

| Root type | Condition | General solution |
|---|---|---|
| Two distinct real | $b^2-4c > 0$ | $y = C_1 e^{r_1 x} + C_2 e^{r_2 x}$ |
| Repeated real $r$ | $b^2-4c = 0$ | $y = (C_1 + C_2 x)e^{rx}$ |
| Complex $\alpha \pm \beta i$ | $b^2-4c < 0$ | $y = e^{\alpha x}(C_1\cos\beta x + C_2\sin\beta x)$ |

## Non-Homogeneous: General Solution

$$y = y_h + y_p$$

where $y_h$ is the homogeneous solution and $y_p$ is a particular solution. Find $y_p$ by undetermined coefficients or variation of parameters.

## Physical Interpretations

- **Underdamped** ($b^2 < 4c$): oscillations with decaying amplitude
- **Overdamped** ($b^2 > 4c$): exponential decay without oscillation
- **Critically damped** ($b^2 = 4c$): fastest return to equilibrium

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $y^{(n)}$ | $n$-th derivative of $y$ |
| $a_n, \ldots, a_0$ | constant coefficients |
| Characteristic equation | polynomial $a_n r^n + \cdots + a_0 = 0$ from substituting $y=e^{rx}$ |
| $r_1, r_2$ | roots of the characteristic equation |
| $C_1, C_2$ | arbitrary constants set by initial conditions |
| Repeated root | $r_1 = r_2 = r$; solution includes $xe^{rx}$ |
| $\alpha \pm \beta i$ | complex conjugate roots; $\alpha$ = real part, $\beta$ = imaginary part |
| $y_h$ | homogeneous (complementary) solution |
| $y_p$ | particular solution |
| Underdamped | complex roots; oscillatory decay |
| Overdamped | two distinct negative real roots; no oscillation |
| Critically damped | repeated root; borderline case |
