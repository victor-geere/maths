---
title: Moduli Spaces
tag: algebraic-geometry
summary: Parameter spaces whose points classify geometric objects — curves, vector bundles, maps — up to isomorphism, giving geometry to the set of all such objects.
links:
  - schemes
  - elliptic-curves
  - riemann-roch
  - functors
---

# Moduli Spaces

A **moduli space** is a geometric space whose points parametrise a family of mathematical objects — algebraic curves, vector bundles, maps between varieties — up to isomorphism. Rather than just saying "there exist many elliptic curves," we want to understand the **space of all elliptic curves**: its dimension, geometry, and compactification. A moduli space $\mathcal{M}$ represents a **moduli problem**: a functor $F : \text{Sch}^{\text{op}} \to \text{Set}$ sending a scheme $S$ to the set of families of the geometric objects over $S$. When the functor is representable, $\mathcal{M} = F$ is a scheme. When it only has a **coarse** moduli space, $\mathcal{M}$ is a scheme approximating the functor. Moduli spaces — of curves, sheaves, maps — are the central objects of study in modern algebraic geometry and string theory.

## The Moduli Problem

A **moduli problem** asks: classify all objects of type $X$ up to isomorphism. Geometrically, this means finding a scheme $\mathcal{M}$ such that:

- Points of $\mathcal{M}(k)$ correspond to isomorphism classes of $X$-objects over $k$
- Families over $S$ correspond to morphisms $S \to \mathcal{M}$

## Examples

| Objects | Moduli space | Dimension |
|---|---|---|
| Elliptic curves | $\mathcal{M}_{1,1}$ (affine line $j$-line) | 1 |
| Genus-$g$ curves | $\mathcal{M}_g$ | $3g-3$ (for $g\geq2$) |
| Genus-$g$ curves with $n$ marked points | $\mathcal{M}_{g,n}$ | $3g-3+n$ |
| Vector bundles of rank $r$ and degree $d$ on $C$ | moduli of stable bundles | $r^2(g-1)+1$ |

## $j$-Invariant and $\mathcal{M}_{1,1}$

Every elliptic curve $E: y^2 = x^3 + ax + b$ has a **$j$-invariant**:

$$j(E) = 1728 \cdot \frac{4a^3}{4a^3 + 27b^2} \in k$$

Two elliptic curves over $\bar{k}$ are isomorphic iff they have the same $j$-invariant. So $\mathcal{M}_{1,1} \cong \mathbb{A}^1$ (the $j$-line).

## Compactification

The moduli space $\mathcal{M}_g$ of smooth genus-$g$ curves has a compactification $\overline{\mathcal{M}}_g$ (Deligne–Mumford) that includes **nodal curves** — curves with mild singularities. This compactification is fundamental for intersection theory and Gromov–Witten theory.

## Stacks

When objects have non-trivial automorphisms (e.g. elliptic curves have a $\pm 1$ automorphism), the moduli problem is better represented by an **algebraic stack** (Deligne–Mumford stack) rather than a scheme.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Moduli space $\mathcal{M}$ | parameter space classifying geometric objects up to isomorphism |
| Moduli problem | a functor $F : \text{Sch}^{\text{op}} \to \text{Set}$ classifying families |
| $\mathcal{M}_g$ | moduli space of smooth projective genus-$g$ curves |
| $\mathcal{M}_{g,n}$ | moduli of genus-$g$ curves with $n$ marked points |
| $\overline{\mathcal{M}}_g$ | Deligne–Mumford compactification; includes nodal curves |
| $j$-invariant | complete invariant of elliptic curves up to isomorphism over $\bar{k}$ |
| $j$-line | $\mathcal{M}_{1,1} \cong \mathbb{A}^1$; parametrises elliptic curves via $j$ |
| Fine moduli space | the functor is representable by a scheme |
| Coarse moduli space | scheme approximating the functor, not representing it exactly |
| Algebraic stack | generalisation of a scheme allowing objects with automorphisms |
| Nodal curve | a curve with node singularities (two branches crossing) |
