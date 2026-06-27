---
title: Green's Functions
tag: pde
summary: The impulse response of a linear differential operator — the solution due to a point source, from which the solution for any source is obtained by superposition.
links:
  - laplace-poisson
  - heat-equation
  - fourier-transform-pde
  - separation-variables
---

# Green's Functions

A **Green's function** $G(x, y)$ for a linear differential operator $\mathcal{L}$ is the solution to the equation $\mathcal{L}G = \delta(x-y)$ — the response at position $x$ due to a point source (Dirac delta) at position $y$. Once $G$ is known, the solution to $\mathcal{L}u = f$ for **any** source $f$ is given by superposition:

$$u(x) = \int G(x,y)\,f(y)\,dy$$

This transforms a PDE with an arbitrary source into an integral, replacing the need to solve a new equation for each $f$. Green's functions are the analogue of matrix inverses for differential operators: just as $A\mathbf{x} = \mathbf{b}$ is solved by $\mathbf{x} = A^{-1}\mathbf{b}$, the PDE $\mathcal{L}u = f$ is solved by $u = \mathcal{L}^{-1}f$, with $G$ representing $\mathcal{L}^{-1}$.

## Definition

The **Green's function** for operator $\mathcal{L}$ on domain $\Omega$ with boundary conditions is the function $G(x,y)$ satisfying:

$$\mathcal{L}_x G(x,y) = \delta(x-y), \quad x,y \in \Omega$$

with the same homogeneous boundary conditions as the original problem.

## Representation Formula

The solution to $\mathcal{L}u = f$ (with homogeneous BC) is:

$$u(x) = \int_\Omega G(x,y)\,f(y)\,dy$$

## Examples

### 1D: $-u'' = f$ on $[0,1]$, $u(0) = u(1) = 0$

$$G(x,y) = \begin{cases} y(1-x) & 0 \leq y \leq x \leq 1 \\ x(1-y) & 0 \leq x \leq y \leq 1\end{cases}$$

### 3D Laplacian: $-\nabla^2 G = \delta(x-y)$ on $\mathbb{R}^3$

$$G(x,y) = \frac{1}{4\pi|x-y|}$$

This is the **Coulomb potential** — the electric potential of a unit charge at $y$.

### Heat Equation

The **heat kernel** $G(x,t;y,s) = \frac{1}{\sqrt{4\pi\alpha^2(t-s)}}e^{-(x-y)^2/(4\alpha^2(t-s))}$ is the Green's function for the heat operator.

## Symmetry

For self-adjoint operators: $G(x,y) = G(y,x)$ (reciprocity principle — same as source-receptor symmetry in acoustics).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $G(x,y)$ | Green's function: response at $x$ to a unit source at $y$ |
| $\mathcal{L}$ | linear differential operator |
| $\delta(x-y)$ | Dirac delta: a unit point source at $y$ |
| $\mathcal{L}_x G = \delta(x-y)$ | the defining equation for the Green's function |
| Representation formula | $u(x) = \int G(x,y)f(y)\,dy$ |
| Point source | a source concentrated at a single point |
| Superposition | solution for any $f$ is the integral of Green's function times $f$ |
| Coulomb potential | $1/(4\pi|x-y|)$: Green's function for Laplacian in 3D |
| Heat kernel | Green's function for the heat equation |
| Self-adjoint | $G(x,y) = G(y,x)$: reciprocity holds |
| Homogeneous BC | boundary conditions where $u = 0$ (or $\partial u/\partial n = 0$) on $\partial\Omega$ |
