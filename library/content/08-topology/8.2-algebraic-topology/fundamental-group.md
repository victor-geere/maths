---
title: Homotopy & Fundamental Group
tag: algebraic-topology
summary: Homotopy formalises continuous deformation of paths; the fundamental group classifies the loop structure of a space.
links:
  - topological-spaces
  - brouwer-fixed-point
  - covering-spaces
  - euler-characteristic
---

# Homotopy & Fundamental Group

**Homotopy** is the precise notion of "continuous deformation": two paths are homotopic if one can be continuously deformed into the other while keeping endpoints fixed. The **fundamental group** $\pi_1(X, x_0)$ collects all loops based at a point $x_0$ up to homotopy, with the group operation being concatenation of loops. This group is the first and most computable algebraic invariant of a topological space — it detects holes of dimension 1. A space with a trivial fundamental group ($\pi_1 = 0$) is **simply connected**: every loop can be contracted to a point. The fundamental group distinguishes the circle ($\pi_1 = \mathbb{Z}$) from the disk ($\pi_1 = 0$), and it is the starting point of all of algebraic topology.

## Homotopy of Paths

Two paths $\gamma_0, \gamma_1 : [0,1] \to X$ with the same endpoints are **homotopic** (written $\gamma_0 \simeq \gamma_1$) if there is a continuous map $H : [0,1] \times [0,1] \to X$ with:

$$H(t, 0) = \gamma_0(t), \quad H(t, 1) = \gamma_1(t), \quad H(0, s) = x_0, \quad H(1, s) = x_1$$

## Fundamental Group

The **fundamental group** $\pi_1(X, x_0)$ consists of homotopy classes of loops based at $x_0$ (paths with $\gamma(0) = \gamma(1) = x_0$), with:

- **Group operation:** concatenation $[\gamma] \cdot [\delta] = [\gamma * \delta]$
- **Identity:** the constant loop at $x_0$
- **Inverse:** the reversed loop $[\bar{\gamma}]$, $\bar{\gamma}(t) = \gamma(1-t)$

## Standard Examples

| Space $X$ | $\pi_1(X)$ |
|---|---|
| $\mathbb{R}^n$, $D^n$, convex set | $\{e\}$ (trivial) |
| $S^1$ (circle) | $\mathbb{Z}$ |
| $T^2$ (torus) | $\mathbb{Z} \times \mathbb{Z}$ |
| Figure-eight | $\mathbb{Z} * \mathbb{Z}$ (free group on 2 generators) |
| $\mathbb{R}P^2$ | $\mathbb{Z}/2\mathbb{Z}$ |

## Simply Connected

$X$ is **simply connected** if it is path-connected and $\pi_1(X) = \{e\}$. Equivalently, every loop can be contracted to a point.

## Van Kampen's Theorem

If $X = U \cup V$ with $U, V, U \cap V$ path-connected:

$$\pi_1(X) \cong \pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V)$$

(amalgamated free product) — the group-theoretic gluing of the pieces.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\pi_1(X, x_0)$ | fundamental group of $X$ based at $x_0$ |
| Homotopy $H$ | continuous deformation; $H : [0,1] \times [0,1] \to X$ |
| $\gamma_0 \simeq \gamma_1$ | paths $\gamma_0$ and $\gamma_1$ are homotopic |
| $[\gamma]$ | homotopy class of the loop $\gamma$ |
| $\gamma * \delta$ | concatenation: traverse $\gamma$ then $\delta$ |
| $\bar{\gamma}$ | reverse of $\gamma$: $\bar{\gamma}(t) = \gamma(1-t)$ |
| Simply connected | path-connected with trivial fundamental group |
| $\mathbb{Z} * \mathbb{Z}$ | free group on two generators |
| Amalgamated free product | group-theoretic gluing used in Van Kampen's theorem |
| Van Kampen's theorem | computes $\pi_1$ of a union from $\pi_1$ of the pieces |
| $S^1$ | the unit circle; $\pi_1(S^1) \cong \mathbb{Z}$ |
| $T^2$ | the torus $S^1 \times S^1$; $\pi_1(T^2) \cong \mathbb{Z}^2$ |
