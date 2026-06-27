---
title: p-adic Absolute Value
tag: algebraic-number-theory
summary: A non-Archimedean absolute value on ℚ that measures divisibility by p — larger powers of p are "smaller" — giving a topology opposite to the usual one.
links:
  - p-adic-numbers
  - local-fields
  - metric-spaces
---

# p-adic Absolute Value

For a prime $p$, the **$p$-adic absolute value** $|\cdot|_p$ on $\mathbb{Q}$ assigns to each rational number a size that reflects how divisible it is by $p$: a large power of $p$ is $p$-adically small. This reverses the usual intuition — $p^{100}$ is tiny in $\mathbb{Q}_p$ while it is enormous in $\mathbb{R}$. The $p$-adic absolute value satisfies the **ultra-metric (strong triangle) inequality** $|x+y|_p \leq \max(|x|_p, |y|_p)$, which is much stronger than the usual triangle inequality and gives $p$-adic analysis its distinctive character. By **Ostrowski's theorem**, every non-trivial absolute value on $\mathbb{Q}$ is either the standard absolute value $|\cdot|_\infty$ or one of the $p$-adic absolute values $|\cdot|_p$.

## Definition

For a rational number $x = p^v \frac{a}{b}$ with $p \nmid a$ and $p \nmid b$ (and $v \in \mathbb{Z}$), the **$p$-adic valuation** is:

$$v_p(x) = v$$

The **$p$-adic absolute value** is:

$$|x|_p = p^{-v_p(x)}, \qquad |0|_p = 0$$

## Properties

1. **Non-negativity:** $|x|_p \geq 0$, with equality iff $x = 0$
2. **Multiplicativity:** $|xy|_p = |x|_p|y|_p$
3. **Ultra-metric:** $|x+y|_p \leq \max(|x|_p, |y|_p)$ (stronger than triangle inequality)

## Ultra-Metric Consequences

- All triangles in $\mathbb{Q}_p$ are **isosceles** (at least two sides equal)
- Every open ball is **both open and closed** (clopen)
- Convergence: $\sum a_n$ converges iff $a_n \to 0$

## Ostrowski's Theorem

Every non-trivial absolute value on $\mathbb{Q}$ is either:
- $|\cdot|_\infty$ (standard absolute value), or
- $|\cdot|_p$ for some prime $p$

## Product Formula

$$|x|_\infty \prod_{p \text{ prime}} |x|_p = 1 \quad \text{for all } x \in \mathbb{Q}^*$$

This links all absolute values together and is a prototype for adèlic formulas.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $v_p(x)$ | $p$-adic valuation: the exponent of $p$ in the factorisation of $x$ |
| $|x|_p = p^{-v_p(x)}$ | $p$-adic absolute value |
| $|x|_\infty$ | standard (real) absolute value |
| Ultra-metric | $|x+y| \leq \max(|x|,|y|)$; stronger than the triangle inequality |
| Isosceles | in ultra-metric spaces all triangles have at least two equal sides |
| Clopen | simultaneously open and closed |
| Ostrowski's theorem | $|\cdot|_\infty$ and $|\cdot|_p$ are the only absolute values on $\mathbb{Q}$ |
| Product formula | $|x|_\infty \prod_p |x|_p = 1$ for $x \in \mathbb{Q}^*$ |
| $\mathbb{Q}^*$ | non-zero rationals |
| Completion | $\mathbb{R} = $ completion of $\mathbb{Q}$ by $|\cdot|_\infty$; $\mathbb{Q}_p = $ completion by $|\cdot|_p$ |
