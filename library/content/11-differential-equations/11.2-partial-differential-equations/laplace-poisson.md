---
title: Laplace's & Poisson's Equations
tag: pde
summary: The elliptic PDEs ∇²u = 0 (Laplace) and ∇²u = f (Poisson) governing steady-state phenomena — electrostatics, gravity, fluid flow, and heat in equilibrium.
links:
  - heat-equation
  - separation-variables
  - greens-functions
  - gaussian-curvature
---

# Laplace's & Poisson's Equations

**Laplace's equation** $\nabla^2 u = 0$ and **Poisson's equation** $\nabla^2 u = f$ are the fundamental **elliptic PDEs**, governing any physical system in **steady state** (time-independent equilibrium). In electrostatics, $u$ is the electric potential and $f$ is the charge density. In fluid mechanics, $u$ is the velocity potential of irrotational flow. In heat conduction, Laplace's equation gives the equilibrium temperature distribution. Solutions to Laplace's equation — called **harmonic functions** — are infinitely smooth, satisfy the maximum principle (no interior extrema), and are uniquely determined by their boundary values (Dirichlet problem). This rigidity makes elliptic PDEs fundamentally different from their parabolic and hyperbolic cousins.

## Equations

**Laplace's equation:**
$$\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0 \quad (2D), \qquad \nabla^2 u = \sum_{i=1}^n \frac{\partial^2 u}{\partial x_i^2} = 0 \quad (nD)$$

**Poisson's equation:**
$$\nabla^2 u = f(x, y)$$

where $f$ is a given source term.

## Harmonic Functions

A function $u$ satisfying Laplace's equation on a domain $\Omega$ is **harmonic**. Key properties:

- **Mean value property:** $u(x_0) = \frac{1}{|\partial B_r|}\oint_{\partial B_r} u\,dS$ (value at centre = average over any sphere)
- **Maximum principle:** $u$ attains its max and min on the boundary $\partial\Omega$, never in the interior
- **Smoothness:** harmonic functions are $C^\infty$ inside $\Omega$
- **Uniqueness:** determined uniquely by boundary values (Dirichlet condition)

## Dirichlet Problem

Find $u$ satisfying $\nabla^2 u = 0$ in $\Omega$ with $u = g$ on $\partial\Omega$.

**Solution on a disk** (polar, radius $R$, boundary $u(R,\theta) = g(\theta)$):

$$u(r,\theta) = \frac{a_0}{2} + \sum_{n=1}^\infty \left(\frac{r}{R}\right)^n(a_n\cos n\theta + b_n\sin n\theta)$$

with Fourier coefficients of $g$.

## Fundamental Solution

$$\Phi(x) = \begin{cases}-\frac{1}{2\pi}\ln|x| & (2D)\\ \frac{1}{4\pi|x|} & (3D)\end{cases}$$

satisfies $\nabla^2\Phi = \delta$ (Dirac delta); used to construct Green's functions.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\nabla^2 u$ | Laplacian of $u$: $\sum \partial^2 u/\partial x_i^2$ |
| $\Delta u$ | alternative notation for $\nabla^2 u$ |
| Harmonic function | solution to $\nabla^2 u = 0$; infinitely smooth |
| $f(x,y)$ | source term in Poisson's equation |
| Dirichlet problem | find $u$ with $\nabla^2 u = 0$ and $u = g$ on boundary |
| Maximum principle | harmonic $u$ attains extreme values on the boundary |
| Mean value property | $u$ at a point equals its average over any surrounding sphere |
| $\partial\Omega$ | boundary of domain $\Omega$ |
| Fundamental solution $\Phi$ | solution to $\nabla^2\Phi = \delta$; singular at origin |
| $\delta$ | Dirac delta distribution — a unit point source |
| Elliptic PDE | no real characteristics; infinite propagation speed; models equilibrium |
