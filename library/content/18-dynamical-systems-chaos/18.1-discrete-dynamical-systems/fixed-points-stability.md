---
title: Fixed Points & Stability
tag: dynamical-systems
summary: A fixed point of a dynamical system is stable if nearby orbits stay nearby, and asymptotically stable if they converge to it; stability is determined by the linearisation (derivative) at the fixed point.
links:
  - iterated-maps
  - lyapunov-stability
  - phase-portraits
  - chaos
---

# Fixed Points & Stability

A **fixed point** $x^*$ of a map $f$ satisfies $f(x^*) = x^*$. For a differential equation $\dot{x} = g(x)$, an **equilibrium** is a point where $g(x^*) = 0$. The central question is whether orbits starting near $x^*$ remain near $x^*$ (**Lyapunov stable**) or actually converge to $x^*$ (**asymptotically stable**). The answer is determined, for hyperbolic fixed points, by the **linearisation**: the eigenvalues of the Jacobian $Df(x^*)$ (discrete case) or $Dg(x^*)$ (continuous case). If all eigenvalues are inside the unit disk (discrete) or have negative real part (continuous), the fixed point is asymptotically stable; if any eigenvalue is outside, it is unstable.

## Discrete Maps

For $f: \mathbb{R}^n \to \mathbb{R}^n$ with fixed point $x^*$, the linearisation is the Jacobian $A = Df(x^*)$.

- **Asymptotically stable**: all eigenvalues of $A$ have $|\lambda| < 1$
- **Unstable**: some eigenvalue with $|\lambda| > 1$
- **Hyperbolic**: no eigenvalue on the unit circle $|\lambda| = 1$

## Continuous Flows

For $\dot{x} = g(x)$ with equilibrium $x^*$ and $A = Dg(x^*)$:

- **Stable**: $\mathrm{Re}(\lambda) < 0$ for all eigenvalues of $A$ (stable node/spiral)
- **Unstable**: some $\mathrm{Re}(\lambda) > 0$ (unstable node/spiral)
- **Saddle**: mixed signs
- **Centre**: purely imaginary eigenvalues (inconclusive from linearisation alone)

## Hartman–Grobman Theorem

Near a **hyperbolic** fixed point $x^*$, the nonlinear system is topologically conjugate to its linearisation. This means the qualitative orbit structure near $x^*$ is determined by the eigenvalues of $Df(x^*)$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Fixed point $x^*$ | $f(x^*) = x^*$ or $g(x^*) = 0$ |
| Equilibrium | fixed point of a continuous flow $\dot{x} = g(x)$ |
| Lyapunov stable | nearby orbits stay nearby |
| Asymptotically stable | nearby orbits converge to $x^*$ |
| Linearisation / Jacobian $A = Df(x^*)$ | best linear approximation to $f$ at $x^*$ |
| Eigenvalue $\lambda$ of $A$ | determines stability: $|\lambda|$ vs 1 (discrete) or $\mathrm{Re}(\lambda)$ (continuous) |
| Hyperbolic fixed point | no eigenvalue on unit circle or imaginary axis |
| Hartman–Grobman theorem | hyperbolic $\Rightarrow$ local conjugacy with linearisation |
| Stable manifold $W^s$ | set of points converging to $x^*$ |
| Unstable manifold $W^u$ | set of points whose backward orbit converges to $x^*$ |
