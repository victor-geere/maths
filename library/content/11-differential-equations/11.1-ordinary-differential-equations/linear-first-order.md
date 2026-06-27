---
title: Linear First-Order ODEs & Integrating Factor
tag: ode
summary: First-order linear equations y' + P(x)y = Q(x) solved by multiplying through by an integrating factor that makes the left side an exact derivative.
links:
  - separable-odes
  - exact-equations
  - fundamental-theorem-calculus
---

# Linear First-Order ODEs & Integrating Factor

A **linear first-order ODE** has the form $y' + P(x)y = Q(x)$ — it is linear in $y$ and $y'$, though $P$ and $Q$ can be arbitrary functions of $x$. Such equations cannot in general be solved by separation of variables, but the **integrating factor method** works universally: multiplying both sides by the function $\mu(x) = e^{\int P(x)\,dx}$ converts the left side into the derivative of the product $\mu y$, enabling direct integration. This technique models drug dosages, RC circuits, mixing problems, and any system with a linear restoring term plus a forcing function.

## Standard Form

$$\frac{dy}{dx} + P(x)\,y = Q(x)$$

## Integrating Factor

Multiply both sides by $\mu(x) = e^{\int P(x)\,dx}$:

$$\frac{d}{dx}\!\left[\mu(x)\,y\right] = \mu(x)\,Q(x)$$

Integrate:

$$\mu(x)\,y = \int \mu(x)\,Q(x)\,dx + C$$

$$y = \frac{1}{\mu(x)}\left[\int \mu(x)\,Q(x)\,dx + C\right]$$

## Why It Works

The product rule gives $\frac{d}{dx}[\mu y] = \mu y' + \mu' y = \mu(y' + P y)$ when $\mu' = \mu P$. That ODE for $\mu$ gives $\mu = e^{\int P\,dx}$.

## Homogeneous vs. Particular Solution

- **Homogeneous** ($Q = 0$): $y_h = Ce^{-\int P\,dx}$
- **Particular** solution $y_p$: any single solution with $Q \neq 0$
- **General solution:** $y = y_h + y_p$

## Example

Solve $y' - 2y = e^x$:

$P = -2$, so $\mu = e^{\int -2\,dx} = e^{-2x}$.

$$\frac{d}{dx}[e^{-2x}y] = e^{-x} \implies e^{-2x}y = -e^{-x} + C \implies y = -e^x + Ce^{2x}$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $y' + P(x)y = Q(x)$ | standard form of a linear first-order ODE |
| $\mu(x) = e^{\int P\,dx}$ | integrating factor |
| $P(x)$ | coefficient of $y$ in the equation |
| $Q(x)$ | forcing function (right-hand side) |
| $y_h$ | homogeneous solution (with $Q=0$) |
| $y_p$ | particular solution (any solution with $Q \neq 0$) |
| General solution | $y_h + y_p$ — the complete family of solutions |
| $C$ | arbitrary constant, fixed by an initial condition |
| Product rule | $\frac{d}{dx}[\mu y] = \mu y' + \mu'y$ — the key identity exploited |
| Linear ODE | linear in $y$ and its derivatives; no products or powers of $y$ |
