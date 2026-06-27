---
title: Separable Equations
tag: ode
summary: First-order ODEs that can be split into a product of a function of x and a function of y, solved by separating variables and integrating both sides.
links:
  - linear-first-order
  - exact-equations
  - fundamental-theorem-calculus
---

# Separable Equations

A **separable ODE** is the simplest type of first-order differential equation that can be solved by direct integration. The key is that the equation can be written so that all the $y$-terms are on one side and all the $x$-terms are on the other — the variables are **separated**. Once separated, integrate each side independently to obtain an implicit (or explicit) solution. This technique handles a surprisingly wide class of equations including exponential growth and decay, logistic growth, Newton's law of cooling, and many elementary physics models.

## General Form

$$\frac{dy}{dx} = f(x)\,g(y)$$

or equivalently: $M(x)\,dx + N(y)\,dy = 0$.

## Method

**Step 1 — Separate variables** (divide by $g(y)$, assuming $g(y) \neq 0$):

$$\frac{dy}{g(y)} = f(x)\,dx$$

**Step 2 — Integrate both sides:**

$$\int \frac{dy}{g(y)} = \int f(x)\,dx + C$$

**Step 3 — Solve** for $y$ (if possible) to get an explicit solution. Otherwise leave implicit.

## Examples

### Exponential Growth / Decay

$$\frac{dy}{dx} = ky \implies \frac{dy}{y} = k\,dx \implies \ln|y| = kx + C \implies y = Ae^{kx}$$

where $A = e^C$ absorbs the constant.

### Separable with Both Sides Nontrivial

$$\frac{dy}{dx} = \frac{x^2}{1-y^2}$$

Separate: $(1-y^2)\,dy = x^2\,dx$

$$y - \frac{y^3}{3} = \frac{x^3}{3} + C$$

## Equilibrium Solutions

When $g(y) = 0$, the equation gives constant solutions $y = y_0$ (equilibria). These must be checked separately since division by $g(y)$ is invalid at these points.

## Autonomous ODEs

An ODE $dy/dx = g(y)$ (no $x$ on the right) is separable and **autonomous** — the rate of change depends only on the current state $y$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $dy/dx$ | derivative of $y$ with respect to $x$ |
| Separable ODE | equation of the form $dy/dx = f(x)g(y)$ |
| $C$ | constant of integration — determined by initial condition |
| Equilibrium (steady state) | a constant solution $y = y_0$ where $g(y_0) = 0$ |
| Autonomous ODE | $dy/dx = g(y)$: right side depends only on $y$ |
| Implicit solution | a relation $F(x,y) = C$ rather than an explicit $y = f(x)$ |
| $k$ | growth/decay constant in exponential models |
| $A = e^C$ | constant of integration after exponentiation |
