---
title: Euler Characteristic
tag: algebraic-topology
summary: A topological invariant χ = V − E + F (and its higher-dimensional generalisation) that classifies surfaces and detects holes.
links:
  - eulers-polyhedra
  - singular-homology
  - simplicial-complexes
  - de-rham-cohomology
---

# Euler Characteristic

The **Euler characteristic** $\chi$ is a single integer that encodes global topological information about a space. For a polyhedron it equals $V - E + F$ (vertices minus edges plus faces), but this is just the tip of the iceberg: the Euler characteristic equals the alternating sum of the **Betti numbers** — the ranks of the homology groups — which count holes of each dimension. It is a **topological invariant**: homeomorphic spaces have the same Euler characteristic, making it a powerful tool for classifying surfaces. The Gauss–Bonnet theorem connects it to geometry (total curvature), and the Lefschetz fixed-point theorem uses it to count fixed points of continuous maps.

## Definition (Polyhedra)

For a convex polyhedron (or any space homeomorphic to one):

$$\chi = V - E + F$$

where $V$ = vertices, $E$ = edges, $F$ = faces.

## Definition (Homology)

For a topological space with finitely generated homology:

$$\chi(X) = \sum_{n=0}^\infty (-1)^n \beta_n$$

where $\beta_n = \text{rank}(H_n(X))$ is the $n$-th **Betti number**.

## Standard Values

| Space | $\chi$ |
|---|---|
| Sphere $S^2$ | $2$ |
| Torus $T^2$ | $0$ |
| Klein bottle | $0$ |
| $\mathbb{R}P^2$ (projective plane) | $1$ |
| Genus-$g$ surface $\Sigma_g$ | $2 - 2g$ |
| Point | $1$ |
| $S^1$ (circle) | $0$ |

## Gauss–Bonnet Theorem

For a closed Riemannian surface $S$:

$$\iint_S K\,dA = 2\pi\chi(S)$$

where $K$ is the Gaussian curvature. This connects topology ($\chi$) to geometry ($K$).

## Lefschetz Fixed-Point Theorem

For a continuous $f : X \to X$ on a compact polyhedron, the **Lefschetz number**:

$$L(f) = \sum_n (-1)^n \text{tr}(f_* : H_n(X) \to H_n(X))$$

If $L(f) \neq 0$, then $f$ has a fixed point. When $f = \text{id}$, $L(\text{id}) = \chi(X)$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\chi$ (chi) | Euler characteristic: $V-E+F$ or $\sum(-1)^n\beta_n$ |
| $\beta_n$ | $n$-th Betti number: $\text{rank}(H_n(X))$ |
| $H_n(X)$ | $n$-th homology group |
| $V, E, F$ | number of vertices, edges, faces |
| Genus $g$ | number of handles on a surface; $\chi = 2-2g$ |
| $\Sigma_g$ | closed orientable surface of genus $g$ |
| Gauss–Bonnet theorem | $\iint_S K\,dA = 2\pi\chi(S)$ |
| $K$ | Gaussian curvature |
| Lefschetz number $L(f)$ | alternating sum of traces of $f_*$ on homology |
| $f_*$ | induced map on homology groups |
| Topological invariant | a quantity preserved under homeomorphism |
| Riemannian surface | a surface with a metric (notion of distance and curvature) |
