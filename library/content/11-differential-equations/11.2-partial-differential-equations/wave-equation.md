---
title: Wave Equation
tag: pde
summary: The hyperbolic PDE ∂²u/∂t² = c²∂²u/∂x² governing the propagation of waves with finite speed c through a medium.
links:
  - heat-equation
  - separation-variables
  - fourier-series
---

# Wave Equation

The **wave equation** governs the propagation of disturbances — sound, light, water waves, vibrating strings, seismic waves — through a medium at a finite speed $c$. Unlike the heat equation (which smooths immediately), the wave equation transmits information at exactly speed $c$: signals travel no faster than $c$, and the sharp features of an initial condition can persist indefinitely. It is the canonical **hyperbolic PDE**. D'Alembert's solution provides a beautiful closed form on the infinite line: the initial displacement splits into two waves travelling in opposite directions at speed $c$. On a finite interval, solutions are superpositions of standing waves — the overtones of a vibrating string, first analysed by Bernoulli and Euler.

## The Equation (1D)

$$\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}, \quad x \in \mathbb{R} \text{ or } (0,L), \quad t > 0$$

- $u(x,t)$: displacement
- $c$: wave speed

## D'Alembert's Solution (Infinite Line)

With initial conditions $u(x,0) = f(x)$, $u_t(x,0) = g(x)$:

$$u(x,t) = \frac{f(x+ct) + f(x-ct)}{2} + \frac{1}{2c}\int_{x-ct}^{x+ct}g(s)\,ds$$

Two waves $f(x\pm ct)$ travel in opposite directions at speed $c$.

## Solution on $[0,L]$ by Separation of Variables

With $u(0,t) = u(L,t) = 0$:

$$u(x,t) = \sum_{n=1}^\infty \sin\!\left(\frac{n\pi x}{L}\right)\!\left[A_n\cos\!\left(\frac{n\pi c\, t}{L}\right) + B_n\sin\!\left(\frac{n\pi c\, t}{L}\right)\right]$$

The **$n$-th mode** oscillates at frequency $\omega_n = n\pi c/L$ — the harmonics of the string.

## Characteristics

The wave equation has two families of **characteristics** $x \pm ct = \text{const}$. Information propagates along characteristics, explaining finite propagation speed.

## Energy Conservation

Total mechanical energy $E(t) = \int_0^L \left(\tfrac{1}{2}u_t^2 + \tfrac{c^2}{2}u_x^2\right)dx$ is constant in time.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $u(x,t)$ | displacement from equilibrium at position $x$ and time $t$ |
| $c$ | wave propagation speed |
| $\partial^2 u/\partial t^2$ | acceleration (second time derivative) |
| $\partial^2 u/\partial x^2$ | spatial curvature |
| D'Alembert's formula | closed-form solution on $\mathbb{R}$: sum of left- and right-travelling waves |
| $f(x\pm ct)$ | right/left-travelling wave components |
| Characteristic | curves $x \pm ct = C$ along which information propagates |
| Hyperbolic PDE | a PDE with two real characteristic directions; finite propagation speed |
| $\omega_n = n\pi c/L$ | $n$-th angular frequency (harmonic) |
| Standing wave | $\sin(n\pi x/L)\cos(n\pi ct/L)$ — spatially fixed oscillation |
| Energy conservation | wave equation conserves total energy $E(t)$ |
