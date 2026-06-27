---
title: Limit Cycles & Poincaré–Bendixson
tag: dynamical-systems
summary: "The Poincaré–Bendixson theorem classifies the possible long-term behaviours of bounded orbits in the plane: they must converge to an equilibrium, a limit cycle, or a cycle-saddle connection."
links:
  - vector-fields-flows
  - phase-portraits
  - fixed-points-stability
  - stable-unstable-manifolds
---

# Limit Cycles & Poincaré–Bendixson

The **Poincaré–Bendixson theorem** is the fundamental theorem about the long-term behaviour of smooth flows in the plane. It states that if a trajectory of $\dot{x} = g(x)$ in $\mathbb{R}^2$ remains in a compact region and accumulates on a set with no fixed points, then its $\omega$-limit set is a **periodic orbit** (limit cycle). This dramatically constrains what planar systems can do: chaos is impossible in $\mathbb{R}^2$ — bounded orbits must converge to equilibria or periodic orbits. The theorem is a uniquely two-dimensional result; in $\mathbb{R}^3$ or higher, chaotic strange attractors are possible. **Limit cycles** — isolated periodic orbits — are the generic attractors/repellers in planar systems and occur ubiquitously in biology, chemistry, and engineering.

## Limit Cycles

A **limit cycle** is an isolated closed orbit $\Gamma$ (isolated in the sense that no other closed orbit is nearby). It is:
- **Stable** (attracting) if nearby orbits spiral toward $\Gamma$.
- **Unstable** (repelling) if nearby orbits spiral away.
- **Semi-stable** if attracting from one side, repelling from the other.

## Poincaré–Bendixson Theorem

Let $g \in C^1(\mathbb{R}^2)$ and suppose the orbit $\{\phi_t(x_0) : t \geq 0\}$ is bounded and the $\omega$-limit set $\omega(x_0)$ contains no equilibrium. Then $\omega(x_0)$ is a **periodic orbit**.

**Corollary**: If $\omega(x_0)$ is compact, connected, and contains no equilibrium, it is a limit cycle.

## Dulac's Criterion (No Limit Cycles)

If there exists a $C^1$ function $B(x,y)$ on a simply connected region $D$ such that $\nabla \cdot (Bg)$ does not change sign in $D$, then there is no limit cycle in $D$.

**Special case (Bendixson)**: $B = 1$; if $\nabla \cdot g = \partial f/\partial x + \partial h/\partial y$ does not change sign, no limit cycles exist.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Limit cycle | isolated periodic orbit |
| Stable limit cycle | nearby orbits converge to it |
| $\omega$-limit set $\omega(x_0)$ | set of accumulation points of forward orbit |
| Poincaré–Bendixson theorem | bounded orbit in $\mathbb{R}^2$ with no equilibria $\Rightarrow$ $\omega$-set is periodic |
| Simply connected | no holes; every loop is contractible |
| Dulac's criterion | divergence criterion for absence of limit cycles |
| $\nabla \cdot g$ | divergence of vector field $g$ |
| Poincaré return map | first return map to a transverse section $\Sigma$ |
| Cycle-saddle connection | heteroclinic or homoclinic orbit; boundary case in P–B |
