---
title: Rational Maps & Morphisms
tag: algebraic-geometry
summary: Morphisms between varieties are polynomial maps; rational maps are partially defined morphisms given by ratios of polynomials, capturing the geometry of maps between varieties.
links:
  - affine-varieties
  - projective-varieties
  - dimension-degree
  - singularities
---

# Rational Maps & Morphisms

A **morphism** of algebraic varieties is a map defined by polynomials — the algebraic geometry analogue of a continuous map in topology or a smooth map in differential geometry. A **rational map** is more general: it is defined by ratios of polynomials and may be undefined at certain points (its base locus). Rational maps are the natural maps in algebraic geometry because they arise from algebraic functions on varieties, and they respect the Zariski topology. The distinction between morphisms (everywhere defined) and rational maps (generically defined) mirrors the difference between holomorphic and meromorphic functions in complex analysis. Birational geometry — the study of varieties up to rational equivalence — is one of the central areas of modern algebraic geometry.

## Morphisms of Affine Varieties

A **morphism** $\phi : V \to W$ between affine varieties $V \subseteq \mathbb{A}^m$ and $W \subseteq \mathbb{A}^n$ is a map given by polynomials:

$$\phi(P) = (f_1(P), \ldots, f_n(P)), \quad f_i \in k[x_1,\ldots,x_m]$$

such that $\phi(V) \subseteq W$.

Morphisms correspond to ring homomorphisms $k[W] \to k[V]$ (reversing direction).

## Rational Maps

A **rational map** $\phi : V \dashrightarrow W$ is an equivalence class of pairs $(U, \phi_U)$ where $U \subseteq V$ is a dense open set and $\phi_U : U \to W$ is a morphism. The map is undefined at some closed subset (the **base locus**).

For projective varieties: a rational map $\phi : V \dashrightarrow \mathbb{P}^n$ is given by $[f_0 : \cdots : f_n]$ where $f_i$ are rational functions on $V$, not all zero on a dense open set.

## Dominant and Birational Maps

A rational map $\phi : V \dashrightarrow W$ is:

- **Dominant** if $\overline{\phi(U)} = W$ (the image is dense)
- **Birational** if there exists a rational inverse $\psi : W \dashrightarrow V$ with $\psi \circ \phi = \text{id}_V$ and $\phi \circ \psi = \text{id}_W$ (on their domains)

Varieties $V$ and $W$ are **birationally equivalent** ($V \sim_{bir} W$) if there is a birational map between them.

## Isomorphism vs. Birational Equivalence

- **Isomorphism:** bijective morphism with morphism inverse — very restrictive
- **Birational equivalence:** same function field $k(V) \cong k(W)$ — much weaker; $\mathbb{A}^n$ and $\mathbb{P}^n$ are birationally equivalent

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Morphism $\phi : V \to W$ | everywhere-defined map given by polynomials |
| Rational map $\phi : V \dashrightarrow W$ | partially defined map given by rational functions |
| $\dashrightarrow$ | notation for a rational (possibly undefined) map |
| Base locus | the closed subset where a rational map is undefined |
| Dominant | image is Zariski-dense |
| Birational map | rational map with rational inverse |
| $V \sim_{bir} W$ | $V$ and $W$ are birationally equivalent |
| $k(V)$ | function field of $V$: the field of rational functions on $V$ |
| Coordinate ring $k[V]$ | ring of polynomial functions; morphisms correspond to ring maps |
| Dense open set | an open set whose closure is the whole variety |
| Rational function | a ratio $f/g$ of polynomials with $g \not\equiv 0$ on $V$ |
