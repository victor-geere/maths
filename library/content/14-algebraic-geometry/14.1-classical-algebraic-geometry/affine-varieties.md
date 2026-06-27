---
title: Affine Varieties
tag: algebraic-geometry
summary: The zero sets of systems of polynomial equations in affine n-space — the fundamental objects of classical algebraic geometry.
links:
  - projective-varieties
  - polynomial-rings
  - ideals
  - rational-maps
---

# Affine Varieties

An **affine variety** is the solution set of a system of polynomial equations in $n$ variables over a field $k$. Just as a line or circle in the plane is defined by polynomial equations, an affine variety is the geometric object attached to any system of polynomial constraints. Algebraic geometry studies these varieties using two complementary perspectives: the **geometric** (the set of points) and the **algebraic** (the ring of polynomial functions on the variety, the coordinate ring). The **Nullstellensatz** (Hilbert's theorem) makes this correspondence precise: there is a bijection between radical ideals in the polynomial ring and affine varieties. This algebraic-geometric dictionary — translating between equations and geometry — is the foundation of the entire subject.

## Definition

The **affine $n$-space** over a field $k$ is:

$$\mathbb{A}^n_k = k^n = \{(a_1, \ldots, a_n) : a_i \in k\}$$

Given polynomials $f_1, \ldots, f_r \in k[x_1, \ldots, x_n]$, the **affine variety** they define is:

$$V(f_1, \ldots, f_r) = \{(a_1, \ldots, a_n) \in \mathbb{A}^n : f_i(a_1,\ldots,a_n) = 0 \text{ for all } i\}$$

## Ideal–Variety Correspondence

For a variety $V \subseteq \mathbb{A}^n$, its **ideal** is:

$$I(V) = \{f \in k[x_1,\ldots,x_n] : f(P) = 0 \text{ for all } P \in V\}$$

For an ideal $I \subseteq k[x_1,\ldots,x_n]$, its **variety** is $V(I)$.

## Hilbert's Nullstellensatz

Over an algebraically closed field $k = \bar{k}$:

$$I(V(J)) = \sqrt{J} \quad \text{(the radical of }J\text{)}$$

This gives a bijection:

$$\left\{\text{radical ideals in }k[x_1,\ldots,x_n]\right\} \longleftrightarrow \left\{\text{affine varieties in }\mathbb{A}^n\right\}$$

## Coordinate Ring

The **coordinate ring** of $V$ is $k[V] = k[x_1,\ldots,x_n]/I(V)$. Its elements are polynomial functions on $V$.

## Zariski Topology

Affine varieties are the **closed sets** of the **Zariski topology** on $\mathbb{A}^n$: the topology where closed sets are exactly the affine varieties. It is much coarser than the usual metric topology.

## Irreducibility

A variety $V$ is **irreducible** if it cannot be written as $V = V_1 \cup V_2$ with both $V_i$ proper subvarieties. Irreducible varieties correspond to **prime ideals**.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathbb{A}^n_k$ | affine $n$-space over $k$: the set $k^n$ viewed geometrically |
| $V(f_1,\ldots,f_r)$ | affine variety: common zero locus of polynomials $f_i$ |
| $I(V)$ | ideal of $V$: all polynomials vanishing on $V$ |
| $k[x_1,\ldots,x_n]$ | polynomial ring in $n$ variables over $k$ |
| $\sqrt{J}$ | radical of ideal $J$: $\{f : f^m \in J \text{ for some } m\}$ |
| Nullstellensatz | Hilbert's theorem: $I(V(J)) = \sqrt{J}$ over algebraically closed $k$ |
| Coordinate ring $k[V]$ | $k[x_1,\ldots,x_n]/I(V)$: polynomial functions on $V$ |
| Zariski topology | topology on $\mathbb{A}^n$ whose closed sets are the affine varieties |
| Irreducible variety | cannot be expressed as a union of two proper subvarieties |
| Algebraically closed | every non-constant polynomial has a root ($\mathbb{C}$ is, $\mathbb{R}$ is not) |
