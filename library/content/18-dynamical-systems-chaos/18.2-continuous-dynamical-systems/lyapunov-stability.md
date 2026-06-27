---
title: Stability of Equilibria (Lyapunov)
tag: dynamical-systems
summary: Lyapunov's direct method proves stability of an equilibrium without solving the ODE by finding a Lyapunov function — an energy-like function that decreases along trajectories.
links:
  - fixed-points-stability
  - vector-fields-flows
  - phase-portraits
  - lyapunov-exponents
---

# Stability of Equilibria (Lyapunov)

Aleksandr Lyapunov's **direct method** (1892) is the most powerful general tool for proving stability of equilibria in dynamical systems. Instead of explicitly solving the ODE $\dot{x} = g(x)$, one seeks a **Lyapunov function** $V: U \to \mathbb{R}$ — an energy-like function that is positive definite near the equilibrium $x^* = 0$ and decreases along trajectories (i.e., $\dot{V} = \nabla V \cdot g(x) \leq 0$). If $V$ strictly decreases, the equilibrium is **asymptotically stable**: all nearby orbits converge to $x^*$. The method is far more general than eigenvalue analysis, applying to nonlinear systems and even infinite-dimensional PDEs, and it forms the basis of modern control theory and Lyapunov optimisation.

## Definitions

Let $x^* = 0$ be an equilibrium of $\dot{x} = g(x)$.

A function $V: U \to \mathbb{R}$ on a neighbourhood $U$ of $0$ is a **Lyapunov function** if:
1. $V(0) = 0$ and $V(x) > 0$ for $x \neq 0$ (**positive definite**)
2. $\dot{V}(x) = \nabla V(x) \cdot g(x) \leq 0$ for $x \in U \setminus \{0\}$ (**non-increasing along orbits**)

## Stability Theorems

**Lyapunov's Stability Theorem**: If a Lyapunov function $V$ exists with $\dot{V} \leq 0$, then $x^* = 0$ is **Lyapunov stable**.

**Lyapunov's Asymptotic Stability Theorem**: If additionally $\dot{V}(x) < 0$ for $x \neq 0$ (**negative definite**), then $x^*$ is **asymptotically stable**.

**LaSalle's Invariance Principle**: If $\dot{V} \leq 0$ and the largest invariant set in $\{\dot{V} = 0\}$ is $\{0\}$, then $x^* = 0$ is asymptotically stable.

## Example

For $\dot{x} = -x^3$, take $V(x) = x^2/2$. Then $\dot{V} = x(-x^3) = -x^4 < 0$ for $x \neq 0$. So $x^* = 0$ is asymptotically stable.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Lyapunov function $V$ | positive definite function with $\dot{V} \leq 0$ along orbits |
| Positive definite $V$ | $V(0)=0$ and $V(x)>0$ for $x\neq 0$ |
| $\dot{V}(x) = \nabla V \cdot g(x)$ | time derivative of $V$ along solutions of $\dot{x}=g(x)$ |
| Negative definite $\dot{V}$ | $\dot{V}(x) < 0$ for $x \neq 0$ |
| Lyapunov stable | nearby orbits stay nearby |
| Asymptotically stable | nearby orbits converge to $x^*$ |
| LaSalle's principle | asymptotic stability from $\{\dot{V}=0\}$ containing no orbit but $\{0\}$ |
| Basin of attraction | set of $x_0$ with $\phi_t(x_0) \to 0$ as $t\to\infty$ |
| Global asymptotic stability | basin of attraction is all of $\mathbb{R}^n$ |
