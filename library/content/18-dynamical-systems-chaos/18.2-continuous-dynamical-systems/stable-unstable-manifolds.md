---
title: Stable & Unstable Manifolds
tag: dynamical-systems
summary: The stable manifold of a hyperbolic fixed point is the set of points converging to it under forward iteration; the unstable manifold consists of points converging under backward iteration; together they organise the global geometry of phase space.
links:
  - fixed-points-stability
  - vector-fields-flows
  - poincare-bendixson
  - phase-portraits
  - chaos
---

# Stable & Unstable Manifolds

The **stable manifold** $W^s(x^*)$ of a hyperbolic fixed point $x^*$ is the set of all initial conditions whose forward orbits converge to $x^*$ as $t \to \infty$. The **unstable manifold** $W^u(x^*)$ is the set whose backward orbits ($t \to -\infty$) converge to $x^*$. By the **Stable Manifold Theorem**, these are smooth embedded submanifolds, tangent at $x^*$ to the stable/unstable subspaces of the linearisation $Dg(x^*)$. Stable and unstable manifolds organise the global geometry of phase space: they act as separatrices, their intersections (**homoclinic points**) generate the complex, chaotic dynamics discovered by Poincaré in the three-body problem, and their dimensions add up to $n$ (the dimension of phase space) at a hyperbolic fixed point.

## Stable Manifold Theorem

Let $x^* = 0$ be a hyperbolic equilibrium of $\dot{x} = g(x)$ with linearisation $A = Dg(0)$. Let $E^s$ (resp. $E^u$) be the stable (resp. unstable) eigenspace of $A$.

**Theorem**: There exist smooth embedded submanifolds $W^s_{\mathrm{loc}}$ and $W^u_{\mathrm{loc}}$ near $0$, tangent to $E^s$ and $E^u$ at $0$, such that:
$$W^s_{\mathrm{loc}} = \{x : \phi_t(x) \to 0 \text{ as } t\to+\infty, \text{ for small } t\}$$
$$W^u_{\mathrm{loc}} = \{x : \phi_t(x) \to 0 \text{ as } t\to-\infty, \text{ for small } t\}$$

The **global** stable manifold $W^s = \bigcup_{t \leq 0} \phi_t(W^s_{\mathrm{loc}})$.

## Homoclinic & Heteroclinic Orbits

- **Homoclinic orbit**: $\phi_t(x) \to x^*$ as $t \to \pm\infty$ — an orbit in $W^s(x^*) \cap W^u(x^*)$.
- **Heteroclinic orbit**: connects two different equilibria $x_1^*, x_2^*$.
- Transverse homoclinic intersections imply the existence of a **Smale horseshoe** — hence chaos.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Stable manifold $W^s(x^*)$ | $\{x : \phi_t(x) \to x^*$ as $t \to +\infty\}$ |
| Unstable manifold $W^u(x^*)$ | $\{x : \phi_t(x) \to x^*$ as $t \to -\infty\}$ |
| Hyperbolic equilibrium | no eigenvalue of $Dg(x^*)$ has zero real part |
| Stable eigenspace $E^s$ | eigenspace of $A$ for eigenvalues with $\mathrm{Re}<0$ |
| Unstable eigenspace $E^u$ | eigenspace for $\mathrm{Re}>0$ |
| Stable Manifold Theorem | $W^s, W^u$ are smooth manifolds tangent to $E^s, E^u$ |
| Homoclinic orbit | $W^s(x^*) \cap W^u(x^*)$; orbit connecting $x^*$ to itself |
| Heteroclinic orbit | orbit from $x_1^*$ to $x_2^*$; in $W^u(x_1^*) \cap W^s(x_2^*)$ |
| Smale horseshoe | canonical chaotic invariant set from transverse homoclinic point |
| Separatrix | stable or unstable manifold dividing phase space |
