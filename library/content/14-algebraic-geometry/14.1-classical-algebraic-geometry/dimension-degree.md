---
title: Dimension & Degree
tag: algebraic-geometry
summary: Dimension measures the "size" of a variety intrinsically; degree measures how many points it meets a generic linear subspace of complementary dimension.
links:
  - affine-varieties
  - projective-varieties
  - singularities
  - plane-curves
---

# Dimension & Degree

The **dimension** and **degree** of an algebraic variety are its two most fundamental numerical invariants. The **dimension** is the algebraic analogue of the geometric notion of dimension: a point has dimension 0, a curve dimension 1, a surface dimension 2, and so on. It is defined algebraically as the Krull dimension of the coordinate ring. The **degree** measures how many points a variety in projective space meets a generic linear subspace of complementary dimension — for example, the degree of a plane curve is the number of intersections with a generic line. Together, dimension and degree classify the simplest varieties and appear in Bézout's theorem, the Hilbert polynomial, and the classification of algebraic surfaces.

## Dimension

The **Krull dimension** of a ring $R$ is the supremum of lengths of chains of prime ideals $\mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \cdots \subsetneq \mathfrak{p}_n$.

The **dimension** of an irreducible affine variety $V$ is:

$$\dim V = \dim k[V] = \text{Krull dim of the coordinate ring}$$

Equivalently: the transcendence degree of $k(V)$ over $k$.

## Examples of Dimensions

| Variety | Dimension |
|---|---|
| A point | 0 |
| A curve (e.g. $y=x^2$) | 1 |
| A surface (e.g. $z=xy$) | 2 |
| $\mathbb{A}^n$ | $n$ |
| A hypersurface $V(f)$ in $\mathbb{A}^n$ | $n-1$ |

## Codimension

$\text{codim}_X V = \dim X - \dim V$.

A **hypersurface** in $\mathbb{A}^n$ has codimension 1.

## Degree

For an irreducible projective variety $V \subseteq \mathbb{P}^n$ of dimension $d$:

$$\deg V = \#(V \cap H_1 \cap \cdots \cap H_d)$$

for generic hyperplanes $H_1,\ldots,H_d$ — the number of intersection points (which is constant for generic choice).

## Hilbert Polynomial

The **Hilbert polynomial** $P_V(t) \in \mathbb{Q}[t]$ of a projective variety has:

- $\deg P_V = \dim V$
- Leading coefficient: $(\deg V)/(\dim V)!$

## Bézout's Theorem

If $V \subseteq \mathbb{P}^n$ and $W \subseteq \mathbb{P}^n$ intersect properly:

$$\deg(V \cap W) = \deg V \cdot \deg W$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\dim V$ | dimension of variety $V$ |
| Krull dimension | length of the longest chain of prime ideals |
| $k[V]$ | coordinate ring of $V$ |
| $k(V)$ | function field of $V$ |
| Transcendence degree | number of algebraically independent generators of $k(V)$ over $k$ |
| $\deg V$ | degree: number of points in a generic linear section of complementary dimension |
| Codimension | $\text{codim}_X V = \dim X - \dim V$ |
| Hypersurface | a variety of codimension 1 |
| Hilbert polynomial $P_V(t)$ | polynomial encoding $\dim V$ and $\deg V$ |
| Bézout's theorem | $\deg(V \cap W) = \deg V \cdot \deg W$ for proper intersection |
| Proper intersection | $\dim(V\cap W) = \dim V + \dim W - \dim\mathbb{P}^n$ |
