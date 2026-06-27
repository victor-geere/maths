---
title: Signed Measures & Hahn Decomposition
tag: measure-theory
summary: A signed measure assigns real values (possibly negative) to measurable sets with countable additivity; the Hahn decomposition splits the space into a positive and negative part, and Jordan decomposition writes ν = ν⁺ − ν⁻.
links:
  - measure-spaces
  - radon-nikodym
  - lebesgue-integral
---

# Signed Measures & Hahn Decomposition

A **signed measure** $\nu: \mathcal{F} \to [-\infty, +\infty]$ is like a measure but allowed to take negative values, with the condition that it cannot take both $+\infty$ and $-\infty$ as values and is countably additive for disjoint unions. Signed measures arise naturally as differences of two measures ($\nu = \mu_1 - \mu_2$), as the distributional derivative of a function of bounded variation, and in the Radon–Nikodym theorem when the density $f$ is not required to be non-negative. The **Hahn decomposition theorem** says the space can be partitioned into a "positive part" $P$ (where $\nu$ behaves like a positive measure) and a "negative part" $N$. The **Jordan decomposition** then writes $\nu = \nu^+ - \nu^-$ as the difference of two mutually singular positive measures.

## Signed Measure

$\nu: \mathcal{F} \to [-\infty,+\infty]$ (at most one of $\pm\infty$ in the range) with:
- $\nu(\emptyset) = 0$
- Countable additivity: $\nu(\bigsqcup_n A_n) = \sum_n \nu(A_n)$ for pairwise disjoint $A_n$

## Hahn Decomposition

**Theorem**: For a signed measure $\nu$ on $(X,\mathcal{F})$, there exist measurable sets $P, N$ with $P \sqcup N = X$ such that:
- $\nu(A) \geq 0$ for all $A \subseteq P$ (**positive set**)
- $\nu(A) \leq 0$ for all $A \subseteq N$ (**negative set**)

The decomposition $X = P \sqcup N$ is unique up to $|\nu|$-null sets.

## Jordan Decomposition

$$\nu^+(A) = \nu(A \cap P), \quad \nu^-(A) = -\nu(A \cap N)$$
$$\nu = \nu^+ - \nu^-, \quad |\nu| = \nu^+ + \nu^-$$

$\nu^+, \nu^-$ are mutually singular positive measures ($\nu^+ \perp \nu^-$) and $|\nu|$ is the **total variation measure**.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Signed measure $\nu$ | countably additive real-valued set function |
| Positive set $P$ | $\nu(A) \geq 0$ for all $A \subseteq P$ |
| Negative set $N$ | $\nu(A) \leq 0$ for all $A \subseteq N$ |
| Hahn decomposition | $X = P \sqcup N$; unique up to null sets |
| $\nu^+$ | positive part: $\nu^+(A) = \nu(A \cap P)$ |
| $\nu^-$ | negative part: $\nu^-(A) = -\nu(A \cap N)$ |
| Jordan decomposition | $\nu = \nu^+ - \nu^-$, $\nu^+ \perp \nu^-$ |
| Total variation $|\nu|$ | $\nu^+ + \nu^-$; a positive measure |
| $\nu^+ \perp \nu^-$ | mutually singular: supported on disjoint sets |
