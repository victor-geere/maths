---
title: Divergence Theorem
tag: multivariable-calculus
summary: Relates the flux of a vector field through a closed surface to the volume integral of the divergence inside.
links:
  - stokes-theorem
  - greens-theorem
  - grad-div-curl
  - triple-integrals
---

# Divergence Theorem

The **Divergence Theorem** (also called Gauss's Theorem) is the three-dimensional analogue of the fundamental theorem of calculus and the companion to Stokes' Theorem. It states that the net outward **flux** of a vector field through a closed surface $\partial E$ equals the total **divergence** (sources minus sinks) inside the enclosed volume $E$. Physically, it says that the total flow out of a region equals the sum of all the local sources within it — a statement of conservation. The Divergence Theorem is central to electrostatics (Gauss's law), fluid dynamics, and heat transfer, and it is one of the most frequently applied theorems in mathematical physics.

## Statement

Let $E$ be a solid region bounded by a closed surface $\partial E$ (with outward unit normal $\mathbf{n}$). For a vector field $\mathbf{F}$ with continuous first partial derivatives:

$$\oiint_{\partial E} \mathbf{F}\cdot d\mathbf{S} = \iiint_E (\nabla\cdot\mathbf{F})\,dV$$

## Intuition

Divergence $\nabla \cdot \mathbf{F}$ at a point measures the local "spreading out" of the field. The theorem says: sum all the local spreadings over the volume $=$ net flux out through the boundary.

## Example

Compute $\oiint_S \mathbf{F}\cdot d\mathbf{S}$ for $\mathbf{F} = (x^3, y^3, z^3)$ over the sphere $x^2+y^2+z^2=1$.

$$\nabla\cdot\mathbf{F} = 3x^2 + 3y^2 + 3z^2 = 3\rho^2$$

$$\iiint_E 3\rho^2\,dV = 3\int_0^{2\pi}\!\int_0^\pi\!\int_0^1 \rho^2\cdot\rho^2\sin\phi\,d\rho\,d\phi\,d\theta = 3\cdot\frac{1}{5}\cdot 2\cdot 2\pi = \frac{12\pi}{5}$$

## Application: Gauss's Law

For the electric field $\mathbf{E}$ and charge density $\rho_e$:

$$\oiint_{\partial E}\mathbf{E}\cdot d\mathbf{S} = \frac{1}{\varepsilon_0}\iiint_E \rho_e\,dV$$

This is Gauss's law in integral form; its differential form $\nabla\cdot\mathbf{E} = \rho_e/\varepsilon_0$ follows by the Divergence Theorem.

## Comparison: The Three Integral Theorems

| Theorem | Dimension | Left side | Right side |
|---|---|---|---|
| Fundamental Theorem of Calculus | 1D | $f(b)-f(a)$ | $\int_a^b f'\,dx$ |
| Green's Theorem | 2D | line integral on $\partial D$ | double integral on $D$ |
| Stokes' Theorem | 3D | line integral on $\partial S$ | surface integral on $S$ |
| Divergence Theorem | 3D | surface integral on $\partial E$ | volume integral on $E$ |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\oiint_{\partial E} \mathbf{F}\cdot d\mathbf{S}$ | outward flux through closed surface $\partial E$ |
| $\iiint_E (\nabla\cdot\mathbf{F})\,dV$ | volume integral of divergence over $E$ |
| $\nabla\cdot\mathbf{F}$ | divergence: $\partial P/\partial x + \partial Q/\partial y + \partial R/\partial z$ |
| $\partial E$ | the boundary surface of region $E$ |
| $d\mathbf{S}$ | outward vector area element $= \mathbf{n}\,dA$ |
| $\mathbf{n}$ | unit outward normal to the surface |
| Flux | the integral $\iint \mathbf{F}\cdot\mathbf{n}\,dA$ measuring flow through a surface |
| Source | a point where divergence is positive (field spreads out) |
| Sink | a point where divergence is negative (field flows in) |
| Gauss's law | physical law relating electric flux to enclosed charge; a consequence of the Divergence Theorem |
| $\varepsilon_0$ | permittivity of free space |
