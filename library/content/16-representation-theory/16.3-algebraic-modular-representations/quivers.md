---
title: Quivers & Path Algebras
tag: representation-theory
summary: A quiver is a directed graph whose representations (assignments of vector spaces to vertices and linear maps to arrows) give a unified framework for modules over finite-dimensional algebras, classified by Gabriel's theorem.
links:
  - linear-representations
  - algebraic-groups
  - modular-representations
---

# Quivers & Path Algebras

A **quiver** is simply a directed graph (with vertices and arrows between them), but its representation theory is remarkably rich and unified. A **representation** of a quiver $Q$ assigns a vector space $V_i$ to each vertex $i$ and a linear map $V_s \to V_t$ to each arrow $s \to t$. Quiver representations encompass a vast range of linear-algebraic classification problems — Jordan normal forms, flags, indecomposable modules over polynomial rings — and provide a unified language for the representation theory of finite-dimensional algebras via the **path algebra** $kQ$. Gabriel's theorem (1972) is a landmark: a quiver has finitely many indecomposable representations if and only if its underlying graph is a Dynkin diagram of type $A, D,$ or $E$.

## Definitions

**Quiver** $Q = (Q_0, Q_1, s, t)$: a set of vertices $Q_0$, arrows $Q_1$, with source $s(\alpha)$ and target $t(\alpha)$ for each $\alpha \in Q_1$.

**Representation** $M$ of $Q$ over $k$: for each $i \in Q_0$ a vector space $M_i$, and for each $\alpha: i\to j$ a linear map $M_\alpha: M_i \to M_j$.

**Morphism**: a tuple $(f_i: M_i \to N_i)$ of linear maps commuting with all $M_\alpha, N_\alpha$.

## Path Algebra

The **path algebra** $kQ$ has basis all paths (including trivial paths $e_i$ at each vertex); multiplication is concatenation (when composable, else 0). Then:
$$\mathrm{Rep}(Q, k) \cong kQ\text{-mod}$$
representations of $Q$ are exactly left $kQ$-modules.

## Gabriel's Theorem

A connected quiver $Q$ (ignoring arrow orientations) has **finitely many** isomorphism classes of indecomposable representations over an algebraically closed field if and only if its underlying undirected graph is a **Dynkin diagram** $A_n$, $D_n$, or $E_{6,7,8}$.

In this case, indecomposables are indexed by **positive roots** of the corresponding root system.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Quiver $Q$ | directed graph: vertices $Q_0$, arrows $Q_1$ |
| $s(\alpha), t(\alpha)$ | source and target of arrow $\alpha$ |
| Representation of $Q$ | vector spaces at vertices + linear maps along arrows |
| Path algebra $kQ$ | algebra with basis = paths in $Q$, multiplication = concatenation |
| $e_i$ | trivial path at vertex $i$; idempotent in $kQ$ |
| $kQ$-mod | category of left $kQ$-modules |
| Indecomposable representation | not isomorphic to a direct sum of non-zero representations |
| Gabriel's theorem | finite rep type $\Leftrightarrow$ Dynkin type $A_n, D_n, E_{6,7,8}$ |
| Finite representation type | finitely many indecomposables up to isomorphism |
| Positive roots | indecomposables in finite type are indexed by these |
