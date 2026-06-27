---
title: Vector Fields & Flows
tag: dynamical-systems
summary: A vector field on a manifold assigns a tangent vector to each point; integrating it produces a flow — a family of diffeomorphisms encoding the continuous time evolution of an autonomous dynamical system.
links:
  - phase-portraits
  - lyapunov-stability
  - poincare-bendixson
  - smooth-manifolds
  - systems-odes
---

# Vector Fields & Flows

A **vector field** $g: M \to TM$ on a smooth manifold $M$ assigns a tangent vector $g(x) \in T_xM$ to each point $x$, encoding the instantaneous velocity of a dynamical system $\dot{x} = g(x)$. **Integrating** the vector field — solving the ODE system — produces a **flow** $\phi_t: M \to M$ for each time $t$: the map sending a starting point to where it is after time $t$. The collection $\{\phi_t\}_{t \in \mathbb{R}}$ is a one-parameter group of diffeomorphisms ($\phi_0 = \mathrm{id}$, $\phi_{s+t} = \phi_s \circ \phi_t$). The interplay between the vector field's local linear structure (Jacobian) and its global topology governs the long-term behaviour of the dynamical system.

## Autonomous ODE System

$$\dot{x} = g(x), \quad x \in \mathbb{R}^n$$

A solution $\gamma: \mathbb{R} \to \mathbb{R}^n$ with $\gamma(0) = x_0$ is a **trajectory** or **orbit** of $g$ through $x_0$.

## The Flow

The **flow** of $g$ is the map $\phi: \mathbb{R} \times M \to M$ defined by $\phi(t, x_0) = \phi_t(x_0) = $ the solution at time $t$ starting from $x_0$.

Properties:
- $\phi_0 = \mathrm{id}_M$
- $\phi_{s+t} = \phi_s \circ \phi_t$ (group law)
- $\frac{d}{dt}\phi_t(x)\big|_{t=0} = g(x)$

## Invariant Sets

A set $S \subseteq M$ is **invariant** under the flow if $\phi_t(S) = S$ for all $t$. Key invariant sets: equilibria, periodic orbits, limit cycles, invariant tori, stable/unstable manifolds.

## Poincaré Map

For a periodic orbit $\Gamma$, choose a **cross-section** $\Sigma$ transverse to $\Gamma$. The **Poincaré return map** $P: \Sigma \to \Sigma$ maps $x \mapsto \phi_{T(x)}(x)$ where $T(x)$ is the first return time. Fixed points of $P$ correspond to periodic orbits of the flow.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Vector field $g: M \to TM$ | assigns tangent vector $g(x)$ to each point |
| Autonomous ODE $\dot{x} = g(x)$ | $g$ independent of time |
| Flow $\phi_t$ | solution map: $\phi_t(x_0) = $ position at time $t$ from $x_0$ |
| One-parameter group | $\phi_0 = \mathrm{id}$, $\phi_{s+t} = \phi_s \circ \phi_t$ |
| Orbit / Trajectory | curve $\{\phi_t(x_0) : t \in \mathbb{R}\}$ |
| Invariant set | $\phi_t(S) = S$ for all $t$ |
| Poincaré map $P$ | return map to a cross-section; fixed pts = periodic orbits |
| Divergence $\nabla \cdot g$ | $\sum_i \partial g_i/\partial x_i$; Liouville: $\frac{d}{dt}\mathrm{Vol} = \int \nabla\cdot g$ |
| Lie derivative $\mathcal{L}_g$ | derivative of functions along orbits of $g$ |
