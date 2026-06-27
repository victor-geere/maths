---
title: Outer Measure & Carathéodory's Theorem
tag: measure-theory
summary: An outer measure is a monotone countably subadditive function on all subsets; Carathéodory's theorem shows that the measurable sets form a σ-algebra on which the outer measure is a genuine measure.
links:
  - measure-spaces
  - sigma-algebras
  - lebesgue-measure
  - null-sets
---

# Outer Measure & Carathéodory's Theorem

An **outer measure** $\mu^*: 2^X \to [0,\infty]$ is a function defined on *all* subsets of $X$ (not just a σ-algebra) satisfying $\mu^*(\emptyset) = 0$, monotonicity ($A \subseteq B \Rightarrow \mu^*(A) \leq \mu^*(B)$), and countable subadditivity ($\mu^*(\bigcup_n A_n) \leq \sum_n \mu^*(A_n)$). Outer measures are constructed from simpler data (e.g., lengths of intervals) via covering arguments. **Carathéodory's theorem** then identifies which sets are "genuinely measurable": a set $E$ is **$\mu^*$-measurable** (Carathéodory measurable) if $\mu^*(A) = \mu^*(A \cap E) + \mu^*(A \cap E^c)$ for all $A$. The collection of measurable sets forms a σ-algebra, and $\mu^*$ restricted to it is a complete measure. This is the standard construction of Lebesgue measure.

## Outer Measure

$\mu^*: 2^X \to [0,\infty]$ satisfies:
1. $\mu^*(\emptyset) = 0$
2. $A \subseteq B \Rightarrow \mu^*(A) \leq \mu^*(B)$
3. $\mu^*\!\left(\bigcup_n A_n\right) \leq \sum_n \mu^*(A_n)$

## Carathéodory Measurability

$E \subseteq X$ is **$\mu^*$-measurable** if for all $A \subseteq X$:
$$\mu^*(A) = \mu^*(A \cap E) + \mu^*(A \setminus E)$$

**Carathéodory's Theorem**: The class $\mathcal{M}$ of $\mu^*$-measurable sets is a σ-algebra, and $\mu^*|_{\mathcal{M}}$ is a complete measure.

## Lebesgue Outer Measure

On $\mathbb{R}$: $\lambda^*(A) = \inf\left\{\sum_n |I_n| : A \subseteq \bigcup_n I_n, I_n \text{ open intervals}\right\}$.

The Lebesgue measurable sets are exactly the Carathéodory measurable sets for $\lambda^*$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Outer measure $\mu^*$ | monotone, countably subadditive, $\mu^*(\emptyset)=0$; defined on $2^X$ |
| Countable subadditivity | $\mu^*(\bigcup A_n) \leq \sum \mu^*(A_n)$ |
| Carathéodory measurable | $\mu^*(A) = \mu^*(A\cap E) + \mu^*(A\setminus E)$ for all $A$ |
| Carathéodory's theorem | measurable sets form σ-algebra; $\mu^*$ is complete there |
| $\lambda^*$ | Lebesgue outer measure on $\mathbb{R}$ |
| Covering | $A \subseteq \bigcup I_n$; used to define $\lambda^*$ |
| Complete measure | null-set subsets are measurable with measure 0 |
| Regularity | outer measure approximated by open/compact sets |
