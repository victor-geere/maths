---
title: Currents
tag: measure-theory
summary: A current is a continuous linear functional on differential forms — a generalised oriented surface — enabling a rigorous framework for the calculus of variations and Plateau's problem in arbitrary codimension.
links:
  - rectifiable-sets
  - hausdorff-measure
  - area-coarea
  - differential-forms
  - stokes-manifolds
---

# Currents

**Currents** (de Rham, 1955; Federer–Fleming, 1960) are the generalisation of oriented surfaces to a distributional setting. Just as distributions generalise functions by duality with test functions, a $k$-dimensional current $T$ is a continuous linear functional on the space $\mathcal{D}^k(U)$ of smooth compactly supported $k$-forms on an open set $U \subseteq \mathbb{R}^n$. Every oriented smooth $k$-submanifold $M$ defines a current $[M](\omega) = \int_M \omega$; more general examples include the boundary $\partial T$ (defined by $\partial T(\omega) = T(d\omega)$, generalising Stokes' theorem) and **rectifiable currents** (supported on rectifiable sets with integer multiplicities). The theory of currents provides the correct framework for Plateau's problem: minimising area among surfaces spanning a given boundary curve, with solutions guaranteed by compactness theorems.

## Definitions

**$k$-current** on $U \subseteq \mathbb{R}^n$: a continuous linear functional $T: \mathcal{D}^k(U) \to \mathbb{R}$.

**Boundary**: $\partial T(\omega) = T(d\omega)$ for $(k-1)$-forms $\omega$; so $\partial\partial T = 0$ (since $d^2 = 0$).

**Mass**: $\mathbf{M}(T) = \sup\{T(\omega) : \|\omega\|_\infty \leq 1\}$ (total variation).

## Rectifiable Currents

A **$k$-rectifiable current** is of the form:
$$T(\omega) = \int_E \langle\omega(x), \xi(x)\rangle\,\theta(x)\,d\mathcal{H}^k(x)$$
where $E$ is $k$-rectifiable, $\xi$ is a unit $k$-vector orienting $T_xE$, and $\theta$ is an integer-valued multiplicity.

## Plateau's Problem

Minimise $\mathbf{M}(T)$ over all $k$-rectifiable currents $T$ with $\partial T = S$ (a given $(k-1)$-cycle). Federer–Fleming compactness theorem guarantees a solution.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $k$-current $T$ | continuous linear functional on $k$-forms |
| $\mathcal{D}^k(U)$ | smooth compactly supported $k$-forms on $U$ |
| Boundary $\partial T$ | $\partial T(\omega) = T(d\omega)$ |
| $\partial^2 = 0$ | since $d^2 = 0$ |
| Mass $\mathbf{M}(T)$ | total variation; generalises area |
| $k$-rectifiable current | current supported on rectifiable set with integer multiplicity |
| Plateau's problem | minimise mass with prescribed boundary |
| Federer–Fleming | compactness theorem; guarantees existence of minimisers |
| Normal current | finite mass and boundary mass |
| Flat norm | topology on currents suitable for convergence |
