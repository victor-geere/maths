---
title: Singularities & Smoothness
tag: algebraic-geometry
summary: A point on a variety is smooth if the Jacobian has maximal rank there; singular points are where the variety self-intersects, cusps, or otherwise fails to look locally like affine space.
links:
  - affine-varieties
  - dimension-degree
  - plane-curves
  - tangent-spaces
---

# Singularities & Smoothness

A **smooth point** on an algebraic variety is one where the variety looks locally like ordinary affine space — it has a well-defined tangent space of the correct dimension. A **singular point** is one where this breaks down: self-intersections, cusps, nodes, and pinch points are all singularities. The study of singularities is central to algebraic geometry: they arise inevitably in nature (even simple operations like taking quotients produce them), and a major programme of the field — the **minimal model programme** — aims to resolve singularities by replacing a singular variety with a smoother one. The singularity structure is detected algebraically by the Jacobian criterion, and geometrically by the tangent cone.

## Jacobian Criterion

Let $V = V(f_1,\ldots,f_r) \subseteq \mathbb{A}^n$ be a variety of dimension $d$. A point $P \in V$ is **smooth** (non-singular) if the **Jacobian matrix**:

$$J_P = \left(\frac{\partial f_i}{\partial x_j}(P)\right)_{i,j}$$

has rank $n - d$ (= codimension of $V$).

$P$ is **singular** if $\text{rank}(J_P) < n - d$.

## Tangent Space

At a smooth point $P$, the **Zariski tangent space** is:

$$T_P V = \ker(J_P) \subseteq \mathbb{A}^n$$

At a singular point, $\dim T_P V > \dim V$.

## Examples of Singularities

| Curve | Singularity at origin | Type |
|---|---|---|
| $y^2 = x^3$ | yes (cusp) | cusp |
| $y^2 = x^3 + x^2$ | yes (node) | node / ordinary double point |
| $y^2 = x^2(x+1)$ | yes | node |
| $y = x^2$ | no | smooth |

## Singular Locus

The **singular locus** $\text{Sing}(V)$ is the set of all singular points of $V$. It is a proper closed subvariety of $V$.

A variety $V$ is **smooth** if $\text{Sing}(V) = \emptyset$.

## Resolution of Singularities

A **resolution of singularities** of $V$ is a smooth variety $\tilde{V}$ with a proper birational morphism $\pi : \tilde{V} \to V$. Hironaka (1964) proved resolutions exist over characteristic 0 fields.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Smooth point | Jacobian has maximal rank; $T_PV$ has dimension $\dim V$ |
| Singular point | Jacobian has deficient rank; $\dim T_PV > \dim V$ |
| $J_P$ | Jacobian matrix of $f_i$ evaluated at $P$ |
| Zariski tangent space $T_PV$ | kernel of $J_P$; the algebraic tangent space at $P$ |
| Codimension | $\dim \mathbb{A}^n - \dim V$; the rank needed from $J_P$ |
| Cusp | a singularity like $y^2 = x^3$; one branch with a sharp point |
| Node | a singularity like $y^2 = x^2(x+1)$; two smooth branches crossing |
| Singular locus $\text{Sing}(V)$ | the closed subset of all singular points |
| Resolution of singularities | a smooth birational model $\tilde{V} \to V$ |
| Hironaka's theorem | resolutions of singularities exist over characteristic 0 |
| Ordinary double point | the simplest node singularity |
