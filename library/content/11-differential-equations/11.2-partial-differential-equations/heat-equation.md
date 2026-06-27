---
title: Heat Equation
tag: pde
summary: The parabolic PDE ∂u/∂t = α²∂²u/∂x² governing diffusion of heat (and many other quantities) through a medium over time.
links:
  - separation-variables
  - fourier-series
  - laplace-poisson
  - wave-equation
---

# Heat Equation

The **heat equation** (or diffusion equation) describes how heat — or any diffusing quantity such as concentration, probability, or electric potential — spreads through a medium over time. It is the canonical **parabolic PDE**: it smooths initial data immediately (no finite propagation speed), and solutions are infinitely differentiable for $t > 0$ regardless of how rough the initial condition was. Fourier's solution using separation of variables and trigonometric series was the historical origin of Fourier analysis. The heat equation appears in thermodynamics, finance (Black–Scholes is a disguised heat equation), random walks (the heat kernel is the transition density of Brownian motion), and image processing.

## The Equation (1D)

$$\frac{\partial u}{\partial t} = \alpha^2 \frac{\partial^2 u}{\partial x^2}, \quad 0 < x < L, \quad t > 0$$

- $u(x,t)$: temperature at position $x$ and time $t$
- $\alpha^2$: **thermal diffusivity** (material constant)

## Boundary and Initial Conditions (Dirichlet)

$$u(0,t) = 0, \quad u(L,t) = 0, \quad u(x,0) = f(x)$$

## Solution by Separation of Variables

Assume $u(x,t) = X(x)T(t)$. Substituting gives:

$$\frac{T'}{α^2 T} = \frac{X''}{X} = -\lambda$$

**Spatial problem (Sturm–Liouville):** $X'' + \lambda X = 0$ with $X(0) = X(L) = 0$:

$$\lambda_n = \left(\frac{n\pi}{L}\right)^2, \quad X_n(x) = \sin\!\left(\frac{n\pi x}{L}\right)$$

**Time equation:** $T_n(t) = e^{-\alpha^2 \lambda_n t}$

**General solution (Fourier series):**

$$u(x,t) = \sum_{n=1}^\infty B_n \sin\!\left(\frac{n\pi x}{L}\right) e^{-\alpha^2(n\pi/L)^2 t}$$

with $B_n = \dfrac{2}{L}\displaystyle\int_0^L f(x)\sin\!\left(\frac{n\pi x}{L}\right)dx$.

## Heat Kernel (Infinite Line)

On $\mathbb{R}$:

$$u(x,t) = \frac{1}{\sqrt{4\pi\alpha^2 t}}\int_{-\infty}^\infty f(y)\,e^{-(x-y)^2/(4\alpha^2 t)}\,dy$$

The **heat kernel** $G(x,t) = \frac{1}{\sqrt{4\pi\alpha^2 t}}e^{-x^2/(4\alpha^2 t)}$ is a Gaussian.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $u(x,t)$ | temperature (or concentration) at position $x$, time $t$ |
| $\alpha^2$ | thermal diffusivity — rate of heat spread |
| $\partial u/\partial t$ | rate of change of $u$ in time |
| $\partial^2 u/\partial x^2$ | second spatial derivative — measures spatial curvature |
| Dirichlet conditions | boundary conditions specifying the value of $u$ |
| Separation of variables | $u = X(x)T(t)$; reduces PDE to two ODEs |
| Eigenvalue $\lambda_n$ | $(n\pi/L)^2$; from the spatial ODE |
| $B_n$ | Fourier sine coefficients determined by initial condition $f(x)$ |
| Heat kernel $G(x,t)$ | fundamental solution: response to a point source at the origin |
| Parabolic PDE | a PDE with one time-like and one space-like derivative |
| Sturm–Liouville problem | eigenvalue problem $X''+\lambda X=0$ with boundary conditions |
