---
title: Stokes' Theorem (Manifolds)
tag: differential-topology
summary: The grand unification of the fundamental theorem of calculus, Green's theorem, classical Stokes, and the divergence theorem — as a single formula on manifolds.
links:
  - differential-forms
  - smooth-manifolds
  - de-rham-cohomology
  - stokes-theorem
---

# Stokes' Theorem (Manifolds)

The **generalised Stokes' theorem** on smooth manifolds is one of the most beautiful theorems in all of mathematics. It states a single, uniform formula:

$$\int_M d\omega = \int_{\partial M} \omega$$

that simultaneously encompasses the **fundamental theorem of calculus**, **Green's theorem**, the **classical Stokes' theorem**, and the **divergence theorem** as special cases. Here $M$ is a compact oriented manifold with boundary $\partial M$, and $\omega$ is a differential form of degree one less than $\dim M$. The theorem says that the integral of the exterior derivative of $\omega$ over $M$ equals the integral of $\omega$ over the boundary $\partial M$ — a deep principle relating the interior of a space to its boundary.

## Statement

Let $M$ be a compact oriented smooth $n$-manifold with boundary $\partial M$ (with the induced orientation), and let $\omega \in \Omega^{n-1}(M)$. Then:

$$\int_M d\omega = \int_{\partial M} \omega$$

If $\partial M = \emptyset$, then $\int_M d\omega = 0$.

## Special Cases

| Theorem | $M$ | $\omega$ | Statement |
|---|---|---|---|
| Fundamental Theorem of Calculus | $[a,b] \subset \mathbb{R}$ | $f$ (0-form) | $\int_a^b f'\,dx = f(b) - f(a)$ |
| Green's Theorem | region $D \subset \mathbb{R}^2$ | 1-form $P\,dx + Q\,dy$ | $\iint_D (Q_x - P_y)\,dA = \oint_{\partial D} P\,dx+Q\,dy$ |
| Classical Stokes | surface $S \subset \mathbb{R}^3$ | 1-form (vector field) | $\iint_S (\nabla\times\mathbf{F})\cdot d\mathbf{S} = \oint_{\partial S}\mathbf{F}\cdot d\mathbf{r}$ |
| Divergence Theorem | solid $E \subset \mathbb{R}^3$ | 2-form | $\iiint_E \nabla\cdot\mathbf{F}\,dV = \oiint_{\partial E}\mathbf{F}\cdot d\mathbf{S}$ |

## Orientation

A manifold is **oriented** if a consistent notion of "positive direction" is chosen at every point. The boundary $\partial M$ inherits an **induced orientation**: the outward-normal-first convention ensures signs in the theorem are consistent.

## Consequence for de Rham Cohomology

Stokes' theorem shows that the pairing $(\omega, \sigma) \mapsto \int_\sigma \omega$ between closed forms and cycles is well-defined on cohomology/homology classes. This is the foundation of the de Rham isomorphism.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\int_M d\omega = \int_{\partial M}\omega$ | the generalised Stokes' theorem |
| $M$ | compact oriented smooth $n$-manifold |
| $\partial M$ | boundary of $M$, with induced orientation |
| $\omega \in \Omega^{n-1}(M)$ | a differential $(n-1)$-form on $M$ |
| $d\omega$ | exterior derivative of $\omega$: an $n$-form |
| Oriented manifold | one with a consistent choice of "positive" orientation |
| Induced orientation | orientation on $\partial M$ determined by $M$ |
| $\oiint$ | surface integral over a closed surface |
| de Rham isomorphism | the isomorphism $H^k_{\text{dR}} \cong H^k(-;\mathbb{R})$ proved using Stokes |
| Green's theorem | 2D special case: $\iint_D(Q_x-P_y)dA = \oint_{\partial D}\mathbf{F}\cdot d\mathbf{r}$ |
| Divergence theorem | 3D special case: $\iiint_E \nabla\cdot\mathbf{F}\,dV = \oiint_{\partial E}\mathbf{F}\cdot d\mathbf{S}$ |
