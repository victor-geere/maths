---
title: Compactness
tag: analysis
summary: A topological property generalising "closed and bounded" in ℝⁿ, ensuring every open cover has a finite subcover.
links:
  - metric-spaces
  - heine-borel
  - continuity
---

# Compactness

**Compactness** is one of the most important and subtlest concepts in analysis and topology. In $\mathbb{R}^n$, compact sets are exactly the **closed and bounded** sets — but the true definition is purely topological and works in any metric or topological space: a set is compact if every open cover has a **finite subcover**. This finiteness condition is extraordinarily powerful: it converts infinite processes into finite ones, guarantees that continuous functions attain their maximum and minimum values, and ensures that sequences have convergent subsequences. Compactness underlies the Heine–Borel theorem, the extreme value theorem, and the study of complete metric spaces.

## Definition

A set $K$ in a metric space $(X, d)$ is **compact** if every open cover of $K$ has a finite subcover:

If $K \subseteq \bigcup_{\alpha \in A} U_\alpha$ (each $U_\alpha$ open), then there exist finitely many $\alpha_1, \ldots, \alpha_n$ such that $K \subseteq U_{\alpha_1} \cup \cdots \cup U_{\alpha_n}$.

## Sequential Compactness

In metric spaces, compactness is equivalent to **sequential compactness**: every sequence in $K$ has a subsequence converging to a point in $K$.

## Heine–Borel Theorem

In $\mathbb{R}^n$, a set is compact $\iff$ it is **closed and bounded**.

## Key Properties of Compact Sets

1. Every compact set is **closed** and **bounded**.
2. A **closed** subset of a compact set is compact.
3. **Continuous image:** if $f : K \to Y$ is continuous and $K$ is compact, then $f(K)$ is compact.
4. **Extreme Value Theorem:** a continuous $f : K \to \mathbb{R}$ on compact $K$ attains its maximum and minimum.
5. A continuous bijection from a compact space to a Hausdorff space is a homeomorphism.

## Compactness vs. Completeness

| Property | Meaning |
|---|---|
| Complete | every Cauchy sequence converges |
| Compact | every sequence has a convergent subsequence (in the space) |

Compact metric spaces are complete, but complete spaces need not be compact (e.g. $\mathbb{R}$).

## Example

$K = [0, 1] \subset \mathbb{R}$ is compact: closed (contains $0$ and $1$) and bounded. Any sequence in $[0,1]$ has a convergent subsequence by Bolzano–Weierstrass.

$K = (0, 1)$ is **not** compact: the sequence $x_n = 1/n$ converges to $0 \notin (0,1)$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Compact set | a set in which every open cover has a finite subcover |
| Open cover | a collection of open sets whose union contains $K$ |
| Finite subcover | a finite sub-collection that still covers $K$ |
| Sequential compactness | every sequence has a convergent subsequence in the set |
| Closed set | contains all its limit points |
| Bounded set | contained within some ball of finite radius |
| Heine–Borel Theorem | in $\mathbb{R}^n$: compact $\iff$ closed and bounded |
| Extreme Value Theorem | continuous $f$ on compact $K$ attains its max and min |
| Bolzano–Weierstrass | every bounded sequence in $\mathbb{R}^n$ has a convergent subsequence |
| Hausdorff space | a topological space where distinct points have disjoint neighbourhoods |
| Homeomorphism | a continuous bijection with continuous inverse |
