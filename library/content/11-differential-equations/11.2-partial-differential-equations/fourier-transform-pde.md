---
title: Fourier Transform Methods
tag: pde
summary: Applying the Fourier transform to PDEs on unbounded domains to convert them into algebraic or ODE problems in frequency space.
links:
  - heat-equation
  - wave-equation
  - fourier-series
  - laplace-transform
---

# Fourier Transform Methods

The **Fourier transform** converts a PDE on an unbounded spatial domain (like the whole real line $\mathbb{R}$) into an equation that is algebraic or an ODE in the frequency variable $\xi$. The key identity is that the Fourier transform of a spatial derivative $\partial_x^n u$ is $(i\xi)^n \hat{u}$, so spatial differentiation becomes multiplication by $(i\xi)^n$ in frequency space. This algebraic structure makes many PDEs tractable on $\mathbb{R}^n$: the heat equation becomes a first-order ODE in time for each frequency, and the wave equation becomes a second-order ODE in $\xi$. After solving in frequency space, the inverse Fourier transform recovers the solution in physical space — often in the form of a convolution integral.

## The Fourier Transform

$$\hat{u}(\xi, t) = \mathcal{F}[u](ξ,t) = \int_{-\infty}^\infty u(x,t)\,e^{-i\xi x}\,dx$$

$$u(x,t) = \mathcal{F}^{-1}[\hat{u}](x,t) = \frac{1}{2\pi}\int_{-\infty}^\infty \hat{u}(\xi,t)\,e^{i\xi x}\,d\xi$$

## Key Property: Differentiation

$$\mathcal{F}\!\left[\frac{\partial^n u}{\partial x^n}\right] = (i\xi)^n\hat{u}(\xi, t)$$

Time derivatives are unaffected: $\mathcal{F}[\partial_t u] = \partial_t \hat{u}$.

## Solving the Heat Equation on $\mathbb{R}$

$u_t = \alpha^2 u_{xx}$. Transform in $x$:

$$\hat{u}_t = -\alpha^2 \xi^2 \hat{u}$$

This is a separable ODE in $t$: $\hat{u}(\xi,t) = \hat{f}(\xi)\,e^{-\alpha^2\xi^2 t}$.

Inverse transform (convolution theorem):

$$u(x,t) = \frac{1}{\sqrt{4\pi\alpha^2 t}}\int_{-\infty}^\infty f(y)\,e^{-(x-y)^2/(4\alpha^2 t)}\,dy$$

## Convolution Theorem

$$\mathcal{F}[f * g] = \hat{f}\,\hat{g}, \qquad (f * g)(x) = \int_{-\infty}^\infty f(y)g(x-y)\,dy$$

## Solving Poisson's Equation

$-\nabla^2 u = f$ on $\mathbb{R}^n$. Transform: $|\xi|^2\hat{u} = \hat{f}$, so $\hat{u} = \hat{f}/|\xi|^2$.

Inverse transform gives the solution as convolution with the fundamental solution.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathcal{F}[u]$ or $\hat{u}$ | Fourier transform of $u$ |
| $\xi$ | frequency variable (dual to spatial variable $x$) |
| $(i\xi)^n$ | Fourier transform of $\partial^n/\partial x^n$ |
| $\mathcal{F}^{-1}$ | inverse Fourier transform |
| Convolution $f * g$ | $(f*g)(x) = \int f(y)g(x-y)\,dy$ |
| Convolution theorem | $\mathcal{F}[f*g] = \hat{f}\cdot\hat{g}$ |
| $e^{-\alpha^2\xi^2 t}$ | Fourier transform of the heat kernel |
| $\hat{f}(\xi)$ | Fourier transform of initial condition $f(x)$ |
| $i = \sqrt{-1}$ | imaginary unit |
| Plancherel theorem | $\int|u|^2\,dx = \frac{1}{2\pi}\int|\hat{u}|^2\,d\xi$ (energy conservation) |
| Physical space | the $(x,t)$ domain |
| Frequency space | the $(\xi,t)$ domain |
