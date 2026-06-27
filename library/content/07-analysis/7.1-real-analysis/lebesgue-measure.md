---
title: Lebesgue Measure
tag: analysis
summary: A rigorous generalisation of length, area, and volume that assigns a size to a vastly larger collection of subsets of ℝⁿ than Riemann's approach allows.
links:
  - lebesgue-integral
  - riemann-integral
  - compactness
---

# Lebesgue Measure

The **Lebesgue measure** is the standard way to assign a precise notion of "size" — length in $\mathbb{R}$, area in $\mathbb{R}^2$, volume in $\mathbb{R}^3$ — to subsets of Euclidean space. Invented by Henri Lebesgue around 1902, it extends the elementary formulas for lengths of intervals and areas of rectangles to a vast collection of sets (the **measurable sets**) using a process of countable additivity: the measure of a countable disjoint union is the sum of the measures. This framework resolves the fundamental limitations of Riemann integration — allowing integration of a much wider class of functions and enabling the powerful convergence theorems that make modern analysis work.

## Construction on $\mathbb{R}$

Start with intervals: for an interval $I = [a, b]$, define $|I| = b - a$.

The **outer measure** of any set $A \subseteq \mathbb{R}$:

$$\lambda^*(A) = \inf\left\{\sum_{n=1}^\infty |I_n| : A \subseteq \bigcup_{n=1}^\infty I_n,\; I_n \text{ open intervals}\right\}$$

A set $A$ is **Lebesgue measurable** if it satisfies Carathéodory's criterion:

$$\lambda^*(E) = \lambda^*(E \cap A) + \lambda^*(E \cap A^c) \quad \text{for all } E \subseteq \mathbb{R}$$

For measurable $A$, define $\lambda(A) = \lambda^*(A)$.

## Properties

1. **Countable additivity:** if $A_1, A_2, \ldots$ are disjoint measurable sets,
   $$\lambda\!\left(\bigsqcup_{n=1}^\infty A_n\right) = \sum_{n=1}^\infty \lambda(A_n)$$
2. **Translation invariance:** $\lambda(A + t) = \lambda(A)$.
3. **Null sets:** $\lambda(\{x\}) = 0$; $\lambda(\mathbb{Q}) = 0$ (countable sets have measure zero).
4. **Open/closed intervals:** $\lambda([a,b]) = \lambda((a,b)) = b - a$.

## Null Sets

A set $N$ is a **null set** (measure zero) if $\lambda(N) = 0$. Properties that hold everywhere except on a null set hold **almost everywhere (a.e.)**.

## Vitali Set — Non-Measurability

Not all subsets of $\mathbb{R}$ are measurable. The **Vitali set** (constructed using the axiom of choice) is an example of a non-measurable set — a demonstration that measure theory requires careful axioms.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\lambda(A)$ | Lebesgue measure of set $A$ |
| $\lambda^*(A)$ | Lebesgue outer measure — defined for all subsets |
| Measurable set | a set satisfying Carathéodory's criterion |
| Null set | a set of measure zero |
| Almost everywhere (a.e.) | holds for all points except possibly a null set |
| Countable additivity | $\lambda(\bigsqcup A_n) = \sum \lambda(A_n)$ for disjoint measurable $A_n$ |
| Outer measure | infimum over all countable interval covers |
| Carathéodory criterion | condition for measurability: $\lambda^*(E) = \lambda^*(E\cap A)+\lambda^*(E\cap A^c)$ |
| Translation invariance | $\lambda(A+t) = \lambda(A)$; measure does not depend on position |
| Vitali set | a non-measurable subset of $\mathbb{R}$, constructed via the axiom of choice |
| $\mathbb{Q}$ | the rational numbers |
