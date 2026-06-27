---
title: Laplace Transform
tag: calculus
summary: An integral transform converting a function of time into a function of complex frequency, used to solve differential equations algebraically.
links:
  - improper-integrals
  - fourier-series
  - convergence
---

# Laplace Transform

The **Laplace transform** converts a function of time $f(t)$ into a function $F(s)$ of a complex variable $s$ by integrating $f(t)$ against $e^{-st}$. This transforms differential equations in $t$ into **algebraic equations** in $s$, which are far easier to solve. After solving for $F(s)$, the **inverse Laplace transform** recovers $f(t)$. The method is the standard engineer's tool for analysing linear time-invariant systems, electrical circuits, control systems, and mechanical vibrations — anywhere where initial-value problems for ODEs arise repeatedly and efficiency matters.

## Definition

$$\mathcal{L}\{f(t)\}(s) = F(s) = \int_0^\infty f(t)\,e^{-st}\,dt$$

The transform exists for $\text{Re}(s) > \sigma_0$, where $\sigma_0$ is the **abscissa of convergence** of $f$.

## Standard Transforms

| $f(t)$ | $F(s) = \mathcal{L}\{f\}$ | Condition |
|---|---|---|
| $1$ | $\dfrac{1}{s}$ | $s > 0$ |
| $e^{at}$ | $\dfrac{1}{s-a}$ | $s > a$ |
| $t^n$ | $\dfrac{n!}{s^{n+1}}$ | $s > 0$ |
| $\sin(\omega t)$ | $\dfrac{\omega}{s^2+\omega^2}$ | $s > 0$ |
| $\cos(\omega t)$ | $\dfrac{s}{s^2+\omega^2}$ | $s > 0$ |
| $\delta(t)$ (unit impulse) | $1$ | all $s$ |
| $u(t-a)$ (unit step) | $\dfrac{e^{-as}}{s}$ | $s > 0$ |

## Key Properties

| Property | Formula |
|---|---|
| Linearity | $\mathcal{L}\{\alpha f + \beta g\} = \alpha F + \beta G$ |
| Derivative | $\mathcal{L}\{f'\} = sF(s) - f(0)$ |
| $n$-th derivative | $s^n F(s) - s^{n-1}f(0) - \cdots - f^{(n-1)}(0)$ |
| Convolution | $\mathcal{L}\{f * g\} = F(s)\,G(s)$ |
| Shift in $s$ | $\mathcal{L}\{e^{at}f(t)\} = F(s-a)$ |

## Solving an ODE: Example

Solve $y'' + y = \sin t$, $y(0) = 0$, $y'(0) = 0$:

$$s^2 Y - 0 - 0 + Y = \frac{1}{s^2+1} \implies Y = \frac{1}{(s^2+1)^2}$$

Inverse transform: $y(t) = \dfrac{\sin t - t\cos t}{2}$.

## Inverse Transform

Partial fractions decompose $F(s)$ into standard terms; then apply the table in reverse.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathcal{L}\{f\}$ | the Laplace transform of $f$ |
| $F(s)$ | Laplace transform; function of complex frequency $s$ |
| $s$ | complex frequency variable ($s = \sigma + i\omega$) |
| $\text{Re}(s)$ | real part of $s$ |
| $\sigma_0$ | abscissa of convergence: minimum $\text{Re}(s)$ for convergence |
| $e^{-st}$ | kernel of the Laplace transform |
| $\delta(t)$ | Dirac delta function — unit impulse at $t=0$ |
| $u(t-a)$ | Heaviside unit step function, equal to 1 for $t \geq a$ |
| Convolution $f * g$ | $(f*g)(t) = \int_0^t f(\tau)g(t-\tau)\,d\tau$ |
| Initial-value problem | ODE with specified values of $y$ and its derivatives at $t=0$ |
| Partial fractions | decomposing a rational $F(s)$ into terms with known inverse transforms |
| $\omega$ | angular frequency (rad/s) |
