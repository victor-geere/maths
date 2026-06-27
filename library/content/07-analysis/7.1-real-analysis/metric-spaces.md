---
title: Metric Spaces
tag: analysis
summary: Sets equipped with a distance function satisfying positivity, symmetry, and the triangle inequality.
links:
  - limits
  - continuity
  - compactness
  - uniform-convergence
---

# Metric Spaces

A **metric space** is a set $X$ together with a **distance function** (metric) $d : X \times X \to \mathbb{R}$ that formalises the intuitive notion of "how far apart" two points are. The three axioms — non-negativity, symmetry, and the triangle inequality — capture the essential properties of Euclidean distance and allow the concepts of limits, continuity, convergence, and compactness to be developed in a unified abstract setting. Metric spaces provide the minimal structure needed for analysis: from $\mathbb{R}^n$ with Euclidean distance, to function spaces with the supremum norm, to graphs with shortest-path distances, all are metric spaces and all obey the same theorems.

## Definition

A **metric** on a set $X$ is a function $d : X \times X \to \mathbb{R}$ satisfying for all $x, y, z \in X$:

1. **Non-negativity:** $d(x, y) \geq 0$, with $d(x,y) = 0 \iff x = y$
2. **Symmetry:** $d(x, y) = d(y, x)$
3. **Triangle inequality:** $d(x, z) \leq d(x, y) + d(y, z)$

## Standard Examples

| Space | Metric |
|---|---|
| $\mathbb{R}^n$ | Euclidean: $d(\mathbf{x},\mathbf{y}) = \|\mathbf{x}-\mathbf{y}\|_2$ |
| $\mathbb{R}^n$ | $\ell^\infty$: $d(\mathbf{x},\mathbf{y}) = \max_i|x_i - y_i|$ |
| $C([a,b])$ | Sup-norm: $d(f,g) = \sup_{x\in[a,b]}|f(x)-g(x)|$ |
| Discrete set | $d(x,y) = 0$ if $x=y$, else $1$ |

## Key Concepts

### Open Ball
$$B(x, r) = \{y \in X : d(x, y) < r\}$$

### Open and Closed Sets
A set $U$ is **open** if every point has an open ball contained in $U$. A set $F$ is **closed** if its complement is open (equivalently, $F$ contains all its limit points).

### Convergence
$x_n \to x$ in $(X, d)$ if $d(x_n, x) \to 0$.

### Continuity
$f : X \to Y$ is continuous at $x$ if $d_X(x_n, x) \to 0 \implies d_Y(f(x_n), f(x)) \to 0$.

### Completeness
$(X, d)$ is **complete** if every Cauchy sequence converges in $X$.

$\mathbb{R}$ is complete; $\mathbb{Q}$ is not.

## Cauchy Sequence
$(x_n)$ is **Cauchy** if $d(x_m, x_n) \to 0$ as $m, n \to \infty$:

$$\forall\,\varepsilon > 0,\;\exists\, N : m,n \geq N \implies d(x_m, x_n) < \varepsilon$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $(X, d)$ | a set $X$ with metric $d$ |
| $d(x, y)$ | the distance between points $x$ and $y$ |
| $B(x, r)$ | open ball of radius $r$ centred at $x$ |
| Triangle inequality | $d(x,z) \leq d(x,y) + d(y,z)$ |
| Open set | a set where every point has a neighbourhood contained in the set |
| Closed set | complement of an open set; contains all its limit points |
| Convergence | $x_n \to x$ means $d(x_n, x) \to 0$ |
| Cauchy sequence | a sequence where terms eventually become arbitrarily close to each other |
| Complete metric space | one where every Cauchy sequence converges |
| $C([a,b])$ | the space of continuous functions on $[a,b]$ |
| Sup-norm | $\|f\|_\infty = \sup_x |f(x)|$ |
| Discrete metric | $d(x,y) = 1$ if $x \neq y$, else $0$ |
