---
title: Normed Spaces & Banach Spaces
tag: functional-analysis
summary: Vector spaces equipped with a norm, and the complete such spaces — where every Cauchy sequence converges.
links:
  - lp-spaces
  - hilbert-spaces
  - metric-spaces
  - vector-spaces
---

# Normed Spaces & Banach Spaces

A **normed space** is a vector space equipped with a **norm** — a function that measures the "length" or "size" of each element, generalising the length of a vector in $\mathbb{R}^n$. A **Banach space** is a normed space that is also **complete**: every Cauchy sequence of elements converges to a limit inside the space. Completeness is the property that makes analysis possible — without it, limits of reasonable sequences might fall outside the space, invalidating arguments. Banach spaces provide the natural setting for functional analysis: linear operators, dual spaces, fixed-point theorems, and the study of differential equations all live here.

## Norm

A **norm** on a vector space $V$ over $\mathbb{R}$ (or $\mathbb{C}$) is a function $\|\cdot\| : V \to \mathbb{R}$ satisfying:

1. **Positive definiteness:** $\|v\| \geq 0$, with $\|v\| = 0 \iff v = \mathbf{0}$
2. **Homogeneity:** $\|\alpha v\| = |\alpha|\,\|v\|$
3. **Triangle inequality:** $\|u + v\| \leq \|u\| + \|v\|$

Every norm induces a metric: $d(u, v) = \|u - v\|$.

## Banach Space

A normed space $(V, \|\cdot\|)$ is a **Banach space** if it is **complete** — every Cauchy sequence converges to an element of $V$:

$$\|v_m - v_n\| \to 0 \implies \exists\, v \in V : \|v_n - v\| \to 0$$

## Standard Examples

| Space | Norm | Banach? |
|---|---|---|
| $\mathbb{R}^n$ | $\|x\|_2 = \sqrt{\sum x_i^2}$ | yes |
| $\ell^p$ ($p \geq 1$) | $\|x\|_p = \left(\sum_{n=1}^\infty |x_n|^p\right)^{1/p}$ | yes |
| $C([a,b])$ | $\|f\|_\infty = \sup|f|$ | yes |
| $L^p(\Omega)$ | $\|f\|_p$ | yes |
| $\mathbb{Q}$ | $|x|$ | **no** (incomplete) |

## Equivalent Norms

Two norms $\|\cdot\|_1$ and $\|\cdot\|_2$ on $V$ are **equivalent** if there exist $c, C > 0$ with:

$$c\|v\|_1 \leq \|v\|_2 \leq C\|v\|_1 \quad \text{for all } v \in V$$

Equivalent norms define the same topology. In **finite dimensions**, all norms are equivalent.

## Key Theorems

- **Hahn–Banach:** linear functionals extend from subspaces to the whole space.
- **Open Mapping:** a bounded surjective operator between Banach spaces is open.
- **Closed Graph:** an operator with a closed graph is bounded.
- **Uniform Boundedness (Banach–Steinhaus):** pointwise-bounded families of operators are uniformly bounded.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\|v\|$ | norm of $v$ — its "length" |
| Normed space | vector space with a norm |
| Banach space | complete normed space |
| Cauchy sequence | $(v_n)$ where $\|v_m - v_n\| \to 0$ as $m,n \to \infty$ |
| Complete | every Cauchy sequence converges within the space |
| $\ell^p$ | sequence space: $\{(x_n) : \sum|x_n|^p < \infty\}$ |
| $C([a,b])$ | continuous functions on $[a,b]$ with sup-norm |
| Equivalent norms | norms with $c\|\cdot\|_1 \leq \|\cdot\|_2 \leq C\|\cdot\|_1$ |
| Bounded operator | $T$ with $\|Tv\| \leq M\|v\|$ for some constant $M$ |
| Hahn–Banach theorem | extension theorem for linear functionals |
| Open Mapping theorem | bounded surjective map between Banach spaces is open |
