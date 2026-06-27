---
title: Plane Curves & Bézout's Theorem
tag: algebraic-geometry
summary: Algebraic curves in the projective plane, classified by their degree, and Bézout's theorem counting their intersection points.
links:
  - projective-varieties
  - dimension-degree
  - singularities
  - elliptic-curves
---

# Plane Curves & Bézout's Theorem

A **plane curve** is the zero locus of a single homogeneous polynomial in $\mathbb{P}^2$. Lines are degree-1 curves, conics degree-2, cubics degree-3, and so on. Plane curves are the simplest positive-dimensional projective varieties and already exhibit extraordinary richness: their topology (genus), singularities, and group law (for cubics) are all determined by their defining polynomial. **Bézout's theorem** is the crown jewel of intersection theory for plane curves: two curves of degrees $d$ and $e$ in $\mathbb{P}^2$ meet in exactly $de$ points, counted with multiplicity — a clean formula that would fail without projective space (parallel lines) or without counting multiplicities (tangencies).

## Definition

A **plane curve** of degree $d$ in $\mathbb{P}^2$ is:

$$C = V(F) = \{[X:Y:Z] \in \mathbb{P}^2 : F(X,Y,Z) = 0\}$$

for a homogeneous polynomial $F \in k[X,Y,Z]$ of degree $d$.

## Classification by Degree

| Degree | Name | Example |
|---|---|---|
| 1 | Line | $aX + bY + cZ = 0$ |
| 2 | Conic | $X^2 + Y^2 - Z^2 = 0$ (circle) |
| 3 | Cubic | $Y^2Z = X^3 - XZ^2$ (elliptic curve) |
| 4 | Quartic | $X^4 + Y^4 = Z^4$ (Fermat) |

## Bézout's Theorem

If $C = V(F)$ and $D = V(G)$ are plane curves in $\mathbb{P}^2_{\bar{k}}$ with $\deg F = d$, $\deg G = e$, and $C \cap D$ is a finite set:

$$\sum_{P \in C \cap D} I_P(C, D) = d \cdot e$$

where $I_P(C,D)$ is the **intersection multiplicity** at $P$.

## Intersection Multiplicity

$I_P(C,D) \geq 1$ for each $P \in C \cap D$. Higher multiplicity occurs at:
- **Tangency:** the two curves share a tangent direction at $P$
- **Singularity:** $P$ is singular on $C$ or $D$

## Genus Formula

For a smooth plane curve of degree $d$:

$$g = \frac{(d-1)(d-2)}{2}$$

| Degree | Genus |
|---|---|
| 1 (line) | 0 |
| 2 (conic) | 0 |
| 3 (cubic) | 1 |
| 4 (quartic) | 3 |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $V(F) \subseteq \mathbb{P}^2$ | plane curve: zero locus of homogeneous polynomial $F$ |
| $\deg F = d$ | degree of the plane curve |
| $I_P(C,D)$ | intersection multiplicity of curves $C$ and $D$ at point $P$ |
| Bézout's theorem | $\sum I_P(C,D) = \deg C \cdot \deg D$ |
| Tangency | two curves share a tangent line; multiplicity $\geq 2$ |
| Genus $g$ | topological handle number; $g=(d-1)(d-2)/2$ for smooth degree-$d$ curves |
| Conic | degree-2 curve; $g=0$ (rational curve) |
| Cubic | degree-3 curve; $g=1$ (elliptic curve if smooth) |
| $\bar{k}$ | algebraic closure of $k$ (needed for Bézout to hold with correct count) |
| Homogeneous polynomial | a polynomial where all terms have the same total degree |
