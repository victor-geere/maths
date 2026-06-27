---
title: Rectifiable Sets
tag: measure-theory
summary: A set is k-rectifiable if it is contained in a countable union of Lipschitz images of ℝᵏ; rectifiable sets have a well-defined tangent plane almost everywhere and support a k-dimensional area formula.
links:
  - hausdorff-measure
  - area-coarea
  - currents
  - smooth-manifolds
---

# Rectifiable Sets

A set $E \subseteq \mathbb{R}^n$ is **$k$-rectifiable** if, up to a set of $\mathcal{H}^k$-measure zero, it is contained in a countable union of Lipschitz images of bounded subsets of $\mathbb{R}^k$. Rectifiable sets are the natural generalisation of smooth $k$-dimensional submanifolds to the non-smooth setting: they have a well-defined approximate tangent $k$-plane $\mathcal{H}^k$-almost everywhere (by Rademacher's theorem on Lipschitz differentiability), and the $k$-dimensional Hausdorff measure $\mathcal{H}^k(E)$ gives their area. Rectifiable sets are the primary objects of **geometric measure theory**, where they serve as the supports of **rectifiable currents** and appear in the solution to Plateau's problem (the least-area surface spanning a given curve).

## Definitions

$E \subseteq \mathbb{R}^n$ is **$k$-rectifiable** if:
$$E \subseteq E_0 \cup \bigcup_{i=1}^\infty f_i(A_i)$$
where $\mathcal{H}^k(E_0) = 0$ and each $f_i: A_i \subseteq \mathbb{R}^k \to \mathbb{R}^n$ is Lipschitz.

$E$ is **purely $k$-unrectifiable** if $\mathcal{H}^k(E \cap f(A)) = 0$ for every Lipschitz $f: A \subseteq \mathbb{R}^k \to \mathbb{R}^n$.

## Approximate Tangent Planes

For $\mathcal{H}^k$-a.e. $x \in E$, there is an approximate tangent $k$-plane $T_xE$: the blow-up $\frac{1}{r}(E - x)$ converges as measures to the $k$-flat $T_xE$ as $r \to 0$.

## Area Formula (for Lipschitz maps)

For Lipschitz $f: \mathbb{R}^k \to \mathbb{R}^n$ and measurable $A \subseteq \mathbb{R}^k$:
$$\int_A J_k f(x)\,d\mathcal{L}^k(x) = \int_{\mathbb{R}^n} \#(f^{-1}(y) \cap A)\,d\mathcal{H}^k(y)$$
where $J_k f = \sqrt{\det(Df^T Df)}$ is the $k$-dimensional Jacobian.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $k$-rectifiable | contained in Lipschitz images of $\mathbb{R}^k$ up to null set |
| Lipschitz map | $|f(x)-f(y)| \leq L|x-y|$; $L$ = Lipschitz constant |
| $\mathcal{H}^k(E)$ | $k$-dimensional Hausdorff measure of $E$ |
| Approximate tangent plane $T_xE$ | $k$-dimensional limit of blow-up at $x$ |
| Purely unrectifiable | no positive-measure intersection with any Lipschitz image |
| Rademacher's theorem | Lipschitz functions are differentiable a.e. |
| $k$-dimensional Jacobian $J_kf$ | $\sqrt{\det(Df^TDf)}$; measures local area distortion |
| Area formula | $\int J_kf = \int \#(f^{-1}(y))\,d\mathcal{H}^k$ |
