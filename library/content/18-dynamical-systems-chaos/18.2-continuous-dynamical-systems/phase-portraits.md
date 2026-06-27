---
title: Phase Portraits
tag: dynamical-systems
summary: A phase portrait is a geometric picture of the orbits of a dynamical system in phase space, revealing fixed points, limit cycles, separatrices, and basins of attraction at a glance.
links:
  - vector-fields-flows
  - fixed-points-stability
  - poincare-bendixson
  - systems-odes
---

# Phase Portraits

A **phase portrait** is a picture of the orbits $\{\phi_t(x_0)\}$ of a dynamical system $\dot{x} = g(x)$ drawn in **phase space** $\mathbb{R}^n$ (or on a manifold). For 2-dimensional systems $\dot{x} = f(x,y)$, $\dot{y} = h(x,y)$, the phase portrait is a planar picture showing trajectories as directed curves, with **equilibria** as special points, **limit cycles** as isolated closed curves, and **separatrices** as curves dividing the plane into regions of qualitatively different behaviour. Phase portraits give immediate geometric insight into the qualitative behaviour of a system without solving it analytically. The Poincaré–Bendixson theorem constrains what can happen in the plane: the long-term behaviour is either an equilibrium, a periodic orbit, or a connection between saddles.

## Key Features of a Phase Portrait

- **Equilibria (fixed points)**: $g(x^*) = 0$; appear as nodes, spirals, saddles, or centres.
- **Nullclines**: curves where $\dot{x} = 0$ or $\dot{y} = 0$; their intersections are equilibria.
- **Limit cycles**: isolated closed orbits that attract or repel nearby orbits.
- **Separatrices**: stable/unstable manifolds of saddle points dividing basins.
- **Basins of attraction**: sets of initial conditions converging to a given attractor.

## Classification of Equilibria in $\mathbb{R}^2$

For eigenvalues $\lambda_{1,2}$ of $Dg(x^*)$:

| Eigenvalues | Type |
|---|---|
| Both $\lambda < 0$ | stable node |
| Both $\lambda > 0$ | unstable node |
| $\lambda_1 < 0 < \lambda_2$ | saddle point |
| $\lambda = \alpha \pm i\beta$, $\alpha < 0$ | stable spiral |
| $\lambda = \alpha \pm i\beta$, $\alpha > 0$ | unstable spiral |
| $\lambda = \pm i\beta$ | centre (inconclusive) |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Phase space | the space of all possible states $(x_1,\ldots,x_n)$ |
| Orbit / Trajectory | curve traced by a solution in phase space |
| Equilibrium | point where $g(x^*) = 0$; fixed point of flow |
| Stable node | both eigenvalues real negative; all orbits approach |
| Saddle | eigenvalues of mixed sign; unstable in one direction |
| Stable spiral | complex eigenvalues with $\mathrm{Re}<0$; orbits spiral in |
| Centre | purely imaginary eigenvalues; closed orbits (neutrally stable) |
| Limit cycle | isolated closed orbit; attracting or repelling |
| Separatrix | boundary curve between different qualitative behaviours |
| Basin of attraction | set of initial conditions converging to an attractor |
| Nullcline | curve where $\dot{x}_i = 0$ |
