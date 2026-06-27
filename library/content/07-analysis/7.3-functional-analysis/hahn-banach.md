---
title: Hahn–Banach Theorem
tag: functional-analysis
summary: A linear functional defined on a subspace of a normed space can always be extended to the whole space without increasing its norm.
links:
  - banach-spaces
  - bounded-operators
  - hilbert-spaces
---

# Hahn–Banach Theorem

The **Hahn–Banach Theorem** is the fundamental extension theorem of functional analysis. It guarantees that a bounded linear functional defined on a subspace of a normed space can always be extended to the entire space, with the norm preserved. This seemingly technical result has far-reaching consequences: it guarantees that the dual space of any normed space is non-trivial (there are plenty of bounded linear functionals), it implies separation theorems for convex sets, and it is the foundation for duality theory in optimisation and economics. The theorem was proved by Hans Hahn in 1927 and independently by Stefan Banach in 1929.

## Statement (Normed Space Version)

Let $X$ be a real normed space, $Y \subseteq X$ a subspace, and $f : Y \to \mathbb{R}$ a bounded linear functional with $|f(y)| \leq M\|y\|$ for all $y \in Y$. Then there exists a bounded linear functional $F : X \to \mathbb{R}$ such that:

$$F|_Y = f \qquad \text{and} \qquad \|F\| = \|f\| = M$$

## Geometric Form (Separation Theorem)

If $A$ and $B$ are disjoint convex sets in a normed space, with $A$ open, then there exists a continuous linear functional $f$ and a scalar $c$ such that:

$$f(a) < c \leq f(b) \quad \text{for all } a \in A,\; b \in B$$

This is the **Hahn–Banach separation theorem** — a hyperplane separates the two sets.

## Key Consequences

1. **Non-triviality of the dual:** for any $x_0 \neq 0$ in $X$, there exists $F \in X^*$ with $F(x_0) = \|x_0\|$ and $\|F\| = 1$.
2. **Reflexivity test:** a normed space is reflexive ($X \cong X^{**}$) if the natural embedding $X \hookrightarrow X^{**}$ is surjective; Hahn–Banach controls this.
3. **Optimality:** in convex optimisation, dual variables (Lagrange multipliers) exist as linear functionals by Hahn–Banach.

## General Version (Sublinear Functional)

Let $p : X \to \mathbb{R}$ be a **sublinear** functional ($p(x+y) \leq p(x)+p(y)$, $p(\lambda x) = \lambda p(x)$ for $\lambda \geq 0$). If $f \leq p$ on $Y$, then $f$ extends to $F : X \to \mathbb{R}$ with $F \leq p$ on all of $X$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Linear functional | a linear map $f : X \to \mathbb{R}$ (or $\mathbb{C}$) |
| Bounded linear functional | $|f(x)| \leq M\|x\|$ for some constant $M$ |
| $\|f\|$ | norm of $f$: $\sup_{\|x\|=1}|f(x)|$ |
| Extension | $F$ extends $f$ if $F(y) = f(y)$ for all $y \in Y$ |
| $F|_Y$ | restriction of $F$ to the subspace $Y$ |
| Dual space $X^*$ | space of all bounded linear functionals on $X$ |
| $X^{**}$ | bidual space: $(X^*)^*$ |
| Reflexive space | $X \cong X^{**}$ via the natural embedding |
| Sublinear functional | satisfies $p(x+y) \leq p(x)+p(y)$ and positive homogeneity |
| Convex set | set where the segment between any two points stays inside |
| Separation theorem | a hyperplane strictly separates two disjoint convex sets |
| Hyperplane | a subspace of codimension 1; $\{x : f(x) = c\}$ for a nonzero functional $f$ |
