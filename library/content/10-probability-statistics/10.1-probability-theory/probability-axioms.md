---
title: Probability Axioms (Kolmogorov)
tag: statistics
summary: The three axioms — non-negativity, normalisation, and countable additivity — that uniquely determine a consistent probability measure.
links:
  - sample-spaces
  - conditional-probability
  - random-variables
---

# Probability Axioms (Kolmogorov)

In 1933, Andrey Kolmogorov placed probability theory on a rigorous axiomatic foundation. A **probability measure** $P$ on a sample space $(\Omega, \mathcal{F})$ is a function assigning a real number to each event, subject to just three axioms. These axioms are minimal: they rule out contradictions (negative probabilities, total probability $\neq 1$, incoherent assignments to disjoint events) while leaving room for all the rich structure of probability theory. Every theorem in probability — the law of total probability, Bayes' theorem, the central limit theorem — follows from these three axioms and the definitions built on them.

## Kolmogorov's Three Axioms

Let $(\Omega, \mathcal{F})$ be a measurable space. A **probability measure** is a function $P : \mathcal{F} \to \mathbb{R}$ satisfying:

**Axiom 1 (Non-negativity):**
$$P(A) \geq 0 \quad \text{for all } A \in \mathcal{F}$$

**Axiom 2 (Normalisation):**
$$P(\Omega) = 1$$

**Axiom 3 (Countable Additivity / $\sigma$-additivity):**
If $A_1, A_2, \ldots \in \mathcal{F}$ are pairwise disjoint ($A_i \cap A_j = \emptyset$ for $i \neq j$):

$$P\!\left(\bigsqcup_{n=1}^\infty A_n\right) = \sum_{n=1}^\infty P(A_n)$$

## Consequences of the Axioms

| Property | Formula |
|---|---|
| Complement rule | $P(A^c) = 1 - P(A)$ |
| Impossible event | $P(\emptyset) = 0$ |
| Monotonicity | $A \subseteq B \Rightarrow P(A) \leq P(B)$ |
| Inclusion–exclusion | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Finite additivity | $A \cap B = \emptyset \Rightarrow P(A \cup B) = P(A) + P(B)$ |
| Boole's inequality | $P\!\left(\bigcup_{i} A_i\right) \leq \sum_i P(A_i)$ |

## Conditional Probability

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

## Law of Total Probability

If $\{B_n\}$ is a partition of $\Omega$:

$$P(A) = \sum_n P(A \mid B_n)\,P(B_n)$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $P(A)$ | probability of event $A$ |
| $P : \mathcal{F} \to [0,1]$ | probability measure |
| $\mathcal{F}$ | sigma-algebra of measurable events |
| $\sigma$-additivity | countable additivity: sum over a countable disjoint union |
| $P(\Omega) = 1$ | normalisation: total probability is 1 |
| $P(A^c) = 1-P(A)$ | complement rule |
| $P(\emptyset) = 0$ | the impossible event has probability 0 |
| Boole's inequality | union bound: $P(\bigcup A_i) \leq \sum P(A_i)$ |
| $P(A|B)$ | conditional probability of $A$ given $B$ |
| Partition | pairwise disjoint events covering $\Omega$ |
| Law of total probability | $P(A) = \sum_n P(A|B_n)P(B_n)$ for partition $\{B_n\}$ |
