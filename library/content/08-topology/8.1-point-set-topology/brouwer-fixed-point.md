---
title: Brouwer Fixed-Point Theorem
tag: topology
summary: Every continuous map from a closed ball to itself has at least one fixed point.
links:
  - topological-spaces
  - compactness
  - connectedness
  - fundamental-group
---

# Brouwer Fixed-Point Theorem

The **Brouwer Fixed-Point Theorem** is one of the most celebrated and surprising results in topology. It states that any continuous function mapping a closed ball to itself must leave at least one point unchanged — a **fixed point**. In one dimension this is elementary (intermediate value theorem: a continuous $f : [0,1] \to [0,1]$ must cross the diagonal). In higher dimensions it seems almost paradoxical: no matter how you stir a cup of coffee, some point always returns to exactly where it started. Proved by L.E.J. Brouwer in 1910 using newly developed tools of algebraic topology, it has profound applications in economics (Nash equilibria exist), differential equations, and numerical analysis.

## Statement

Let $D^n = \{x \in \mathbb{R}^n : \|x\| \leq 1\}$ be the closed unit $n$-ball. Every continuous function $f : D^n \to D^n$ has a **fixed point**: a point $x^* \in D^n$ with $f(x^*) = x^*$.

## Low-Dimensional Cases

**$n=1$:** $f : [0,1] \to [0,1]$ continuous. Let $g(x) = f(x) - x$. Then $g(0) \geq 0$ and $g(1) \leq 0$, so by IVT there exists $x^*$ with $g(x^*) = 0$.

**$n=2$:** Imagine a disk. Any continuous self-map has a fixed point. Proof uses the fact that $\pi_1(S^1) = \mathbb{Z}$ while $\pi_1(D^2) = 0$ — no retraction of $D^2$ onto $S^1$ exists.

## Proof via No-Retraction Lemma

The Brouwer theorem is equivalent to the **No-Retraction Lemma**: there is no continuous map $r : D^n \to S^{n-1}$ that fixes every point of $S^{n-1}$ (no retraction of the ball onto its boundary).

**Proof that no-retraction $\Rightarrow$ fixed point:** if $f$ had no fixed point, define $r(x)$ as the point where the ray from $f(x)$ through $x$ hits $S^{n-1}$. Then $r$ is a retraction — contradiction.

## Applications

- **Nash Equilibrium:** every finite game has a Nash equilibrium (via fixed points of the best-response correspondence on a simplex).
- **Existence of ODE solutions:** Peano's theorem on existence of solutions.
- **Sperner's Lemma:** a combinatorial fixed-point result equivalent to Brouwer in dimension $n$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $D^n$ | closed unit $n$-ball: $\{x \in \mathbb{R}^n : \|x\| \leq 1\}$ |
| $S^{n-1}$ | unit $(n-1)$-sphere: boundary of $D^n$ |
| Fixed point | a point $x^*$ with $f(x^*) = x^*$ |
| Retraction | a continuous $r : X \to A$ with $r(a) = a$ for all $a \in A$ |
| No-Retraction Lemma | no retraction of $D^n$ onto its boundary $S^{n-1}$ exists |
| $\pi_1(X)$ | fundamental group of $X$ — measures loops |
| IVT | Intermediate Value Theorem |
| Nash equilibrium | a strategy profile where no player benefits from unilateral deviation |
| Sperner's Lemma | a combinatorial lemma equivalent to Brouwer |
| $\|x\|$ | Euclidean norm of $x$ |
| Continuous self-map | a continuous $f : X \to X$ |
