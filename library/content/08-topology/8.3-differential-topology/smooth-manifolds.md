---
title: Smooth Manifolds
tag: differential-topology
summary: Topological spaces that locally look like ℝⁿ and carry a smooth structure enabling calculus.
links:
  - topological-spaces
  - tangent-spaces
  - differential-forms
  - gaussian-curvature
---

# Smooth Manifolds

A **smooth manifold** is a topological space that locally resembles Euclidean space and is equipped with enough structure to do calculus. The key idea is that a manifold of dimension $n$ can be covered by **charts** — homeomorphisms from open patches of the manifold to open subsets of $\mathbb{R}^n$ — and wherever two charts overlap, the transition between them must be a smooth ($C^\infty$) function. This allows derivatives, tangent vectors, and differential equations to be defined intrinsically, without reference to any ambient space. Smooth manifolds are the natural setting for differential geometry, general relativity, classical mechanics (phase spaces), and the theory of Lie groups.

## Definition

An $n$-dimensional **smooth manifold** $M$ is a topological space with a **smooth atlas**: a collection $\{(U_\alpha, \varphi_\alpha)\}$ where:

- $\{U_\alpha\}$ is an open cover of $M$
- Each $\varphi_\alpha : U_\alpha \to V_\alpha \subseteq \mathbb{R}^n$ is a homeomorphism (a **chart**)
- For overlapping charts, the **transition map** $\varphi_\beta \circ \varphi_\alpha^{-1} : \varphi_\alpha(U_\alpha \cap U_\beta) \to \varphi_\beta(U_\alpha \cap U_\beta)$ is $C^\infty$

## Standard Examples

| Manifold | Dimension | Notes |
|---|---|---|
| $\mathbb{R}^n$ | $n$ | trivial atlas |
| $S^n$ (sphere) | $n$ | two stereographic projection charts |
| $T^n$ (torus) | $n$ | product of circles |
| $GL_n(\mathbb{R})$ | $n^2$ | open subset of $M_n(\mathbb{R})$ |
| $\mathbb{R}P^n$ | $n$ | projective space |

## Smooth Maps

A map $f : M \to N$ between manifolds is **smooth** if, in any pair of charts, $\psi \circ f \circ \varphi^{-1}$ is a smooth map between Euclidean spaces.

A **diffeomorphism** is a smooth bijection with smooth inverse — the "isomorphism" of smooth manifolds.

## Submanifolds

A subset $S \subseteq M$ is a **submanifold** of dimension $k$ if locally it looks like $\mathbb{R}^k \subseteq \mathbb{R}^n$. The sphere $S^{n-1} \subseteq \mathbb{R}^n$ is a submanifold.

## Whitney Embedding Theorem

Every smooth $n$-manifold embeds smoothly into $\mathbb{R}^{2n}$. This shows abstract manifolds can always be realised as subsets of Euclidean space.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $M$ | the smooth manifold |
| Chart $(U_\alpha, \varphi_\alpha)$ | a homeomorphism from an open patch of $M$ to an open set in $\mathbb{R}^n$ |
| Atlas | a compatible collection of charts covering $M$ |
| Transition map | $\varphi_\beta \circ \varphi_\alpha^{-1}$: change of coordinates between two charts |
| $C^\infty$ | infinitely differentiable (smooth) |
| Diffeomorphism | smooth bijection with smooth inverse |
| Submanifold | a subset that is itself a manifold |
| $S^n$ | the $n$-sphere |
| $T^n$ | the $n$-torus ($S^1 \times \cdots \times S^1$, $n$ times) |
| $\mathbb{R}P^n$ | real projective $n$-space |
| Whitney Embedding | every $n$-manifold embeds in $\mathbb{R}^{2n}$ |
| Lie group | a smooth manifold that is also a group with smooth operations |
