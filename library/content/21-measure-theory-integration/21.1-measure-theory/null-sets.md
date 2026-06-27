---
title: Null Sets & Completeness
tag: measure-theory
summary: A null set has measure zero; a measure is complete if all subsets of null sets are measurable. Completeness ensures that sets indistinguishable from null sets are treated as null, which is essential for almost-everywhere statements.
links:
  - measure-spaces
  - lebesgue-measure
  - sigma-algebras
  - borel-sets
  - outer-measure
---

# Null Sets & Completeness

A **null set** (or **measure-zero set**) for a measure space $(X, \mathcal{F}, \mu)$ is a measurable set $N \in \mathcal{F}$ with $\mu(N) = 0$. Null sets are "negligible" — they have zero size and can often be ignored in analysis. A measure $\mu$ is **complete** if every subset of a null set is measurable (and hence also a null set). The Lebesgue measure on $\mathbb{R}$ is complete (after Lebesgue completion of the Borel σ-algebra), but the Borel measure is not. Completeness is essential for the phrase **"almost everywhere" (a.e.)**: a property holds a.e. if the set where it fails is a null set. Almost-everywhere convergence, almost-everywhere equality of functions, and almost-sure events in probability all rely on null sets.

## Null Sets

$N \in \mathcal{F}$ is a **$\mu$-null set** if $\mu(N) = 0$.

Key properties:
- Countable union of null sets is null: $\mu(N_1 \cup N_2 \cup \cdots) \leq \sum \mu(N_n) = 0$.
- A subset of a null set need not be measurable (unless $\mu$ is complete).

## Complete Measure

$(X,\mathcal{F},\mu)$ is **complete** if: $N \in \mathcal{F}$, $\mu(N) = 0$, $A \subseteq N$ $\Rightarrow$ $A \in \mathcal{F}$ (and $\mu(A) = 0$).

**Completion**: Any measure space $(X,\mathcal{F},\mu)$ has a completion $(X,\bar{\mathcal{F}},\bar{\mu})$ where $\bar{\mathcal{F}} = \{A \triangle N : A \in \mathcal{F}, N \subseteq \text{null set}\}$.

## Almost Everywhere

A property $P(x)$ holds **$\mu$-almost everywhere** (a.e. or $\mu$-a.e.) if $\mu(\{x : P(x)\text{ fails}\}) = 0$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Null set | $N \in \mathcal{F}$ with $\mu(N) = 0$ |
| $\mu$-a.e. | almost everywhere: property fails only on a null set |
| Complete measure | subsets of null sets are measurable |
| Completion $\bar{\mathcal{F}}$ | smallest complete σ-algebra extending $\mathcal{F}$ |
| $A \triangle B$ | symmetric difference $(A\setminus B)\cup(B\setminus A)$ |
| Lebesgue null set | set of Lebesgue measure 0 (e.g., countable sets, Cantor set) |
| Cantor set | uncountable null set |
| Negligible set | informal synonym for null set |
| Almost sure (a.s.) | probability theory term for almost everywhere |
