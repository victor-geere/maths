---
title: Covering Spaces
tag: algebraic-topology
summary: A covering space wraps surjectively over a base space, with each small neighbourhood evenly covered by disjoint sheets.
links:
  - fundamental-group
  - topological-spaces
  - continuity-topology
---

# Covering Spaces

A **covering space** is a topological space $\tilde{X}$ that maps onto a base space $X$ in a particularly controlled way: every point of $X$ has a neighbourhood that is evenly divided into disjoint "sheets", each mapped homeomorphically by the covering map $p$. Covering spaces provide a geometric way to study the fundamental group — the sheets correspond to cosets of a subgroup of $\pi_1(X)$, and the **universal cover** corresponds to the trivial subgroup. The theory creates a beautiful correspondence between subgroups of $\pi_1(X)$ and connected covering spaces, mirroring Galois theory's correspondence between field extensions and subgroups.

## Definition

A **covering map** $p : \tilde{X} \to X$ is a continuous surjection such that for every $x \in X$, there is an open neighbourhood $U \ni x$ with:

$$p^{-1}(U) = \bigsqcup_{\alpha} V_\alpha$$

a disjoint union of open sets $V_\alpha \subseteq \tilde{X}$, each mapped homeomorphically by $p$ onto $U$. The sets $V_\alpha$ are the **sheets** over $U$.

## Degree

The number of sheets $|p^{-1}(x)|$ is the **degree** of the covering (constant if $X$ is connected).

## Examples

| Covering map $p$ | Base $X$ | Cover $\tilde{X}$ | Degree |
|---|---|---|---|
| $p(\theta) = e^{2\pi i\theta}$ | $S^1$ | $\mathbb{R}$ | $\infty$ |
| $z \mapsto z^n$ on $S^1$ | $S^1$ | $S^1$ | $n$ |
| $\mathbb{R}^2 \to T^2$ | $T^2$ | $\mathbb{R}^2$ | $\infty$ |

## Lifting

**Path lifting:** any path $\gamma$ in $X$ starting at $x_0$ lifts uniquely to a path $\tilde{\gamma}$ in $\tilde{X}$ starting at any chosen $\tilde{x}_0 \in p^{-1}(x_0)$.

**Homotopy lifting:** homotopies also lift — the fundamental tool for computing monodromy.

## Galois Correspondence

For a path-connected, locally path-connected, semi-locally simply connected base $X$:

$$\left\{\begin{array}{c}\text{connected covering spaces}\\\text{of }X\end{array}\right\} \longleftrightarrow \left\{\begin{array}{c}\text{subgroups of }\pi_1(X, x_0)\end{array}\right\}$$

The **universal cover** $\tilde{X}$ corresponds to the trivial subgroup $\{e\}$ and has $\pi_1(\tilde{X}) = \{e\}$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $p : \tilde{X} \to X$ | covering map |
| $\tilde{X}$ | covering space (the "upstairs" space) |
| $X$ | base space (the "downstairs" space) |
| Sheet | a connected component of $p^{-1}(U)$, mapped homeomorphically to $U$ |
| Degree | number of sheets $= |p^{-1}(x)|$ |
| Path lifting | unique lift of a path in $X$ to $\tilde{X}$ |
| Universal cover | the simply connected covering space; unique up to isomorphism |
| Monodromy | how sheets permute as a loop is traversed |
| $\pi_1(X, x_0)$ | fundamental group of $X$ |
| $S^1$ | unit circle |
| $T^2 = S^1 \times S^1$ | the torus |
| Galois correspondence | bijection between covering spaces and subgroups of $\pi_1$ |
