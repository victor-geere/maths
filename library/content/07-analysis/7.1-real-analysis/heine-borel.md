---
title: Heine–Borel Theorem
tag: analysis
summary: In ℝⁿ, a subset is compact if and only if it is both closed and bounded.
links:
  - compactness
  - metric-spaces
  - continuity
---

# Heine–Borel Theorem

The **Heine–Borel Theorem** gives a completely concrete characterisation of compact subsets of $\mathbb{R}^n$: a set is compact if and only if it is **closed** and **bounded**. This equivalence — between an abstract covering property and two elementary geometric conditions — is one of the most useful theorems in real analysis. It means that in $\mathbb{R}^n$ one never needs to verify the open-cover condition directly; checking closedness and boundedness is sufficient. The theorem makes the extreme value theorem, uniform continuity on closed intervals, and the convergence of subsequences all straightforward to apply.

## Statement

A subset $K \subseteq \mathbb{R}^n$ is **compact** if and only if $K$ is **closed** and **bounded**.

Equivalently (in $\mathbb{R}^n$): $K$ is compact $\iff$ every sequence in $K$ has a subsequence converging to a point in $K$.

## Proof Sketch (for $\mathbb{R}$)

**Bounded + Closed $\Rightarrow$ Compact:**

1. $K$ bounded means $K \subseteq [-M, M]$ for some $M$.
2. Any sequence in $K$ lies in the bounded set $[-M,M]$.
3. By **Bolzano–Weierstrass**, it has a convergent subsequence with limit $\ell$.
4. Since $K$ is closed, $\ell \in K$. Hence $K$ is sequentially compact, hence compact.

**Compact $\Rightarrow$ Bounded:** if $K$ were unbounded, the open cover $\{(-n, n) : n \in \mathbb{N}\}$ would have no finite subcover.

**Compact $\Rightarrow$ Closed:** if $K$ were not closed, some limit point $p \notin K$ could be used to build an open cover with no finite subcover.

## Failure Outside $\mathbb{R}^n$

Heine–Borel fails in general metric spaces. In $C([0,1])$ with sup-norm, the closed unit ball $\{f : \|f\|_\infty \leq 1\}$ is closed and bounded but **not** compact (the sequence $f_n(x) = \sin(n\pi x)$ has no convergent subsequence in $C([0,1])$).

## Consequences

- **Extreme Value Theorem:** continuous $f : K \to \mathbb{R}$ on compact $K$ attains its max and min.
- **Uniform Continuity:** continuous $f$ on compact $K$ is uniformly continuous.
- **Finite covers:** any open cover of $[a,b]$ reduces to a finite one.

## Examples

| Set | Closed? | Bounded? | Compact? |
|---|---|---|---|
| $[a, b]$ | yes | yes | **yes** |
| $(a, b)$ | no | yes | no |
| $\mathbb{R}$ | yes | no | no |
| $\{x : \|x\| \leq 1\}$ in $\mathbb{R}^n$ | yes | yes | **yes** |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Compact | every open cover has a finite subcover; in $\mathbb{R}^n$: closed and bounded |
| Closed | contains all its limit points; complement is open |
| Bounded | contained in some ball $B(0, M)$ for finite $M$ |
| Bolzano–Weierstrass | every bounded sequence in $\mathbb{R}^n$ has a convergent subsequence |
| Sequential compactness | every sequence has a subsequence converging within the set |
| Extreme Value Theorem | continuous function on compact set attains its max and min |
| Uniform continuity | $\forall\,\varepsilon>0,\;\exists\,\delta>0$ independent of $x$: $|x-y|<\delta\Rightarrow|f(x)-f(y)|<\varepsilon$ |
| $C([0,1])$ | space of continuous functions on $[0,1]$ |
| Sup-norm $\|\cdot\|_\infty$ | $\|f\|_\infty = \sup_{x}|f(x)|$ |
| $\mathbb{R}^n$ | $n$-dimensional Euclidean space |
