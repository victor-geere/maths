---
title: Measures & Measure Spaces
tag: measure-theory
summary: A measure on a σ-algebra assigns non-negative sizes to measurable sets in a countably additive way; together with a measurable space it forms a measure space, the foundation of integration theory.
links:
  - sigma-algebras
  - lebesgue-measure
  - outer-measure
  - probability-axioms
  - null-sets
---

# Measures & Measure Spaces

A **measure** $\mu$ on a measurable space $(X, \mathcal{F})$ is a function $\mu: \mathcal{F} \to [0, \infty]$ that assigns a non-negative extended real number to each measurable set, satisfying $\mu(\emptyset) = 0$ and **countable additivity**: for pairwise disjoint sets $A_1, A_2, \ldots \in \mathcal{F}$, $\mu(\bigcup_n A_n) = \sum_n \mu(A_n)$. The triple $(X, \mathcal{F}, \mu)$ is a **measure space**. Measures generalise length, area, volume, counting, and probability in a unified framework. The Lebesgue measure on $\mathbb{R}^n$ assigns to each nice set its $n$-dimensional volume; the counting measure assigns $|A|$ to finite sets; probability measures satisfy $\mu(X) = 1$. Measure spaces are the foundation of modern integration (Lebesgue integral), probability theory, and ergodic theory.

## Definition

A **measure** on $(X, \mathcal{F})$ is $\mu: \mathcal{F} \to [0,\infty]$ with:
1. $\mu(\emptyset) = 0$
2. **Countable additivity**: $A_n \in \mathcal{F}$ pairwise disjoint $\Rightarrow \mu\!\left(\bigsqcup_n A_n\right) = \sum_n \mu(A_n)$

## Examples

| Measure space | $\mu$ |
|---|---|
| $(\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n), \lambda^n)$ | Lebesgue measure |
| $(\mathbb{N}, 2^\mathbb{N}, \#)$ | Counting measure: $\mu(A) = |A|$ |
| $(X, \mathcal{F}, \delta_{x_0})$ | Dirac measure: $\mu(A) = \mathbf{1}_{x_0 \in A}$ |
| $(\Omega, \mathcal{F}, \mathbb{P})$ | Probability space: $\mathbb{P}(\Omega) = 1$ |

## Properties

- **Monotonicity**: $A \subseteq B \Rightarrow \mu(A) \leq \mu(B)$
- **Subadditivity**: $\mu(\bigcup_n A_n) \leq \sum_n \mu(A_n)$
- **Continuity from below**: $A_n \nearrow A \Rightarrow \mu(A_n) \nearrow \mu(A)$
- **Continuity from above**: $A_n \searrow A$, $\mu(A_1) < \infty \Rightarrow \mu(A_n) \searrow \mu(A)$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $(X,\mathcal{F},\mu)$ | measure space |
| Countable additivity | $\mu(\bigsqcup A_n) = \sum\mu(A_n)$ |
| $\sigma$-finite measure | $X = \bigcup_n X_n$ with $\mu(X_n) < \infty$ |
| Finite measure | $\mu(X) < \infty$ |
| Probability measure | $\mu(X) = 1$ |
| Counting measure $\#$ | $\#(A) = |A|$ |
| Dirac measure $\delta_x$ | $\delta_x(A) = \mathbf{1}_{x \in A}$ |
| $A_n \nearrow A$ | increasing sequence of sets converging to $A$ |
| Null set | $A$ with $\mu(A) = 0$ |
| Complete measure | if $\mu(A) = 0$ and $B \subseteq A$ then $B \in \mathcal{F}$ and $\mu(B) = 0$ |
