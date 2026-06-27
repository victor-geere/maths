---
title: Bernoulli Equations
tag: ode
summary: Nonlinear first-order ODEs of the form y' + P(x)y = Q(x)yⁿ, reduced to linear equations by the substitution v = y^(1−n).
links:
  - linear-first-order
  - separable-odes
  - exact-equations
---

# Bernoulli Equations

A **Bernoulli equation** is a nonlinear first-order ODE that, while not linear itself, can be transformed into a linear equation by a clever substitution. The equation $y' + P(x)y = Q(x)y^n$ (for $n \neq 0, 1$) is nonlinear because of the $y^n$ term on the right, but dividing by $y^n$ and substituting $v = y^{1-n}$ converts it to a standard linear first-order ODE in $v$, which can be solved by the integrating factor method. Named after Jacob Bernoulli (1695), these equations arise in population dynamics (logistic growth), fluid mechanics, and mathematical biology.

## Standard Form

$$\frac{dy}{dx} + P(x)\,y = Q(x)\,y^n, \quad n \neq 0, 1$$

- $n = 0$: already linear
- $n = 1$: separable (linear homogeneous)

## Solution Method

**Step 1 — Divide by $y^n$:**

$$y^{-n}\frac{dy}{dx} + P(x)\,y^{1-n} = Q(x)$$

**Step 2 — Substitute** $v = y^{1-n}$, so $\dfrac{dv}{dx} = (1-n)y^{-n}\dfrac{dy}{dx}$:

$$\frac{1}{1-n}\frac{dv}{dx} + P(x)\,v = Q(x)$$

$$\frac{dv}{dx} + (1-n)P(x)\,v = (1-n)Q(x)$$

This is linear in $v$ — solve by integrating factor.

**Step 3 — Back-substitute** $v = y^{1-n}$.

## Example: Logistic Equation

The logistic ODE $\dfrac{dy}{dx} = ky\!\left(1 - \dfrac{y}{K}\right) = ky - \dfrac{k}{K}y^2$ is Bernoulli with $n = 2$, $P = -k$, $Q = -k/K$.

Substitution $v = y^{-1}$ gives $v' + kv = k/K$ (linear), with solution $v = 1/K + Ce^{-kx}$, hence:

$$y = \frac{K}{1 + CKe^{-kx}}$$

the logistic (sigmoidal) growth curve.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $y' + P(x)y = Q(x)y^n$ | Bernoulli equation |
| $n$ | the exponent on $y$; the nonlinearity parameter |
| $v = y^{1-n}$ | the substitution that linearises the equation |
| $dv/dx$ | derivative of the new variable $v$ |
| Integrating factor | used after substitution to solve the resulting linear ODE |
| Logistic equation | Bernoulli with $n=2$; models bounded population growth |
| $K$ | carrying capacity in the logistic model |
| $k$ | growth rate constant |
| $y^{-n}$ | dividing by $y^n$ to prepare the Bernoulli substitution |
| Sigmoidal | S-shaped growth curve characteristic of logistic solutions |
