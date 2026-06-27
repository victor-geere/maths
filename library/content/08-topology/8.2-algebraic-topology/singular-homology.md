---
title: Singular Homology
tag: algebraic-topology
summary: Topological invariants built from continuous maps of simplices into a space, detecting holes of each dimension.
links:
  - simplicial-complexes
  - euler-characteristic
  - fundamental-group
  - de-rham-cohomology
---

# Singular Homology

**Singular homology** assigns to every topological space $X$ a sequence of abelian groups $H_n(X)$ that count "holes" of each dimension: $H_0$ counts connected components, $H_1$ detects loops that cannot be filled in, $H_2$ detects enclosed voids, and so on. Unlike simplicial homology, which requires the space to be triangulated, singular homology works for **any** topological space by considering all possible continuous maps from standard simplices into $X$ — even very wild ones. The groups are topological invariants: homeomorphic spaces have isomorphic homology groups, making them powerful tools for distinguishing spaces that are otherwise hard to tell apart.

## Singular Chains

A **singular $n$-simplex** in $X$ is a continuous map $\sigma : \Delta^n \to X$, where $\Delta^n$ is the standard $n$-simplex.

The **singular chain group** $C_n(X; \mathbb{Z})$ is the free abelian group on all singular $n$-simplices.

## Boundary Maps

The boundary of a singular $n$-simplex $\sigma : \Delta^n \to X$ is:

$$\partial_n \sigma = \sum_{i=0}^n (-1)^i \sigma|_{[v_0,\ldots,\hat{v}_i,\ldots,v_n]}$$

These maps satisfy the crucial identity $\partial_{n-1} \circ \partial_n = 0$.

## Homology Groups

$$H_n(X) = \frac{\ker \partial_n}{\text{im}\, \partial_{n+1}} = \frac{Z_n}{B_n}$$

- **Cycles** $Z_n = \ker\partial_n$: chains with no boundary
- **Boundaries** $B_n = \text{im}\,\partial_{n+1}$: chains that are boundaries of something
- A cycle represents a hole if it is not the boundary of any higher-dimensional chain.

## Standard Examples

| Space $X$ | $H_0$ | $H_1$ | $H_2$ |
|---|---|---|---|
| Point | $\mathbb{Z}$ | $0$ | $0$ |
| $S^1$ (circle) | $\mathbb{Z}$ | $\mathbb{Z}$ | $0$ |
| $S^2$ (sphere) | $\mathbb{Z}$ | $0$ | $\mathbb{Z}$ |
| $T^2$ (torus) | $\mathbb{Z}$ | $\mathbb{Z}^2$ | $\mathbb{Z}$ |
| $\mathbb{R}P^2$ | $\mathbb{Z}$ | $\mathbb{Z}/2\mathbb{Z}$ | $0$ |

## Euler Characteristic

$$\chi(X) = \sum_n (-1)^n \text{rank}(H_n(X))$$

## Hurewicz Theorem

For a simply connected space: $H_1(X) = \pi_1(X)^{\text{ab}}$ (abelianisation of the fundamental group), and the first non-trivial $\pi_n(X) \cong H_n(X)$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $H_n(X)$ | $n$-th singular homology group of $X$ |
| $\Delta^n$ | standard $n$-simplex |
| Singular $n$-simplex | a continuous map $\sigma : \Delta^n \to X$ |
| $C_n(X;\mathbb{Z})$ | singular chain group — free abelian group on singular simplices |
| $\partial_n$ | boundary map $C_n \to C_{n-1}$ |
| $\partial^2 = 0$ | fundamental identity: boundary of boundary is zero |
| $Z_n$ | cycles: $\ker\partial_n$ |
| $B_n$ | boundaries: $\text{im}\,\partial_{n+1}$ |
| $\text{rank}(H_n)$ | the Betti number $\beta_n$ — number of independent $n$-dimensional holes |
| Hurewicz theorem | relates $\pi_n$ (homotopy) to $H_n$ (homology) |
| $\mathbb{R}P^2$ | real projective plane |
| Abelianisation | $G^{\text{ab}} = G/[G,G]$ — making a group commutative |
