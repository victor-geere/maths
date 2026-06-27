---
title: Simplicial Complexes
tag: algebraic-topology
summary: Combinatorial building-blocks for topological spaces — built from vertices, edges, triangles, and their higher-dimensional analogues glued together coherently.
links:
  - singular-homology
  - euler-characteristic
  - fundamental-group
---

# Simplicial Complexes

A **simplicial complex** is a combinatorial and geometric object built by gluing together simple pieces called **simplices** — points (0-simplices), line segments (1-simplices), filled triangles (2-simplices), solid tetrahedra (3-simplices), and so on. They provide a way to discretise and approximate topological spaces, making abstract topological invariants computable. A triangulation of a surface replaces it by a simplicial complex with the same topology. Simplicial complexes are the foundation of the original (simplicial) homology theory, and their combinatorial nature makes them amenable to computer computation — they are the primary tool in **topological data analysis (TDA)**.

## Simplices

A **$k$-simplex** is the convex hull of $k+1$ affinely independent points in $\mathbb{R}^n$:

$$\sigma = [v_0, v_1, \ldots, v_k] = \left\{\sum_{i=0}^k \lambda_i v_i : \lambda_i \geq 0,\; \sum_i \lambda_i = 1\right\}$$

A **face** of $\sigma$ is any simplex formed by a subset of $\{v_0, \ldots, v_k\}$.

| $k$ | Name | Example |
|---|---|---|
| 0 | Vertex | a point |
| 1 | Edge | a line segment |
| 2 | Triangle | a filled triangle |
| 3 | Tetrahedron | a solid tetrahedron |

## Simplicial Complex

A **simplicial complex** $K$ is a collection of simplices closed under taking faces:

$$\sigma \in K,\; \tau \text{ face of } \sigma \implies \tau \in K$$

Any two simplices in $K$ intersect in a common face (or not at all).

## Euler Characteristic

$$\chi(K) = \sum_{k=0}^n (-1)^k f_k$$

where $f_k$ is the number of $k$-simplices. This is a topological invariant.

## Simplicial Homology

The **chain groups** $C_k(K)$ are free abelian groups on the $k$-simplices. The **boundary map** $\partial_k : C_k \to C_{k-1}$ sends each simplex to the alternating sum of its faces:

$$\partial_k [v_0, \ldots, v_k] = \sum_{i=0}^k (-1)^i [v_0, \ldots, \hat{v}_i, \ldots, v_k]$$

where $\hat{v}_i$ means $v_i$ is omitted. The homology groups $H_k = \ker\partial_k / \text{im}\,\partial_{k+1}$ are topological invariants.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $k$-simplex $\sigma$ | convex hull of $k+1$ affinely independent points |
| $[v_0, \ldots, v_k]$ | simplex with vertices $v_0, \ldots, v_k$ |
| Face | a sub-simplex formed by a subset of vertices |
| Simplicial complex $K$ | a collection of simplices closed under taking faces |
| $f_k$ | number of $k$-simplices in $K$ |
| $\chi(K)$ | Euler characteristic of $K$ |
| $C_k(K)$ | $k$-th chain group: free abelian group on $k$-simplices |
| $\partial_k$ | boundary map: $C_k \to C_{k-1}$ |
| $\hat{v}_i$ | vertex $v_i$ omitted from the list |
| $H_k$ | $k$-th homology group: $\ker\partial_k / \text{im}\,\partial_{k+1}$ |
| Triangulation | decomposition of a space into simplices |
| TDA | Topological Data Analysis — uses simplicial complexes to study data |
