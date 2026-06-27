---
title: Sample Spaces & Events
tag: statistics
summary: The foundational framework of probability — a sample space lists all possible outcomes of an experiment, and events are subsets we assign probabilities to.
links:
  - probability-axioms
  - conditional-probability
  - random-variables
---

# Sample Spaces & Events

Before assigning probabilities, we must be precise about what we are measuring. A **sample space** $\Omega$ is the set of all possible outcomes of a random experiment — rolling a die, drawing a card, measuring a patient's temperature. An **event** is any subset of $\Omega$ to which we wish to assign a probability. This set-theoretic framework, introduced by Kolmogorov in 1933, gives probability theory its rigorous foundation: events can be combined using union (A or B), intersection (A and B), and complement (not A), and a **probability measure** assigns each event a number between 0 and 1 consistent with three axioms. Getting the sample space right is the first and most important step in any probabilistic analysis.

## Sample Space

The **sample space** $\Omega$ is the set of all possible outcomes of a random experiment.

| Experiment | Sample space $\Omega$ |
|---|---|
| Flip a coin | $\{H, T\}$ |
| Roll a die | $\{1, 2, 3, 4, 5, 6\}$ |
| Pick a real number in $[0,1]$ | $[0, 1]$ |
| Sequence of coin flips | $\{H,T\}^{\mathbb{N}}$ |

## Events

An **event** $A$ is a subset $A \subseteq \Omega$.

- **Elementary event:** a single outcome $\{\omega\}$
- **Certain event:** $\Omega$ (always occurs)
- **Impossible event:** $\emptyset$ (never occurs)

## Set Operations on Events

| Operation | Notation | Meaning |
|---|---|---|
| Union | $A \cup B$ | $A$ or $B$ (or both) occur |
| Intersection | $A \cap B$ | both $A$ and $B$ occur |
| Complement | $A^c = \Omega \setminus A$ | $A$ does not occur |
| Difference | $A \setminus B$ | $A$ occurs but not $B$ |

## Sigma-Algebra

For continuous sample spaces, not every subset can be assigned a probability consistently. A **$\sigma$-algebra** $\mathcal{F}$ is a collection of subsets of $\Omega$ closed under countable unions and complements — these are the **measurable events**.

The triple $(\Omega, \mathcal{F}, P)$ is a **probability space**.

## Mutually Exclusive and Exhaustive

- **Mutually exclusive:** $A \cap B = \emptyset$ (cannot both occur)
- **Exhaustive:** $A \cup B = \Omega$ (at least one must occur)
- **Partition:** a collection of mutually exclusive, exhaustive events

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\Omega$ | sample space — the set of all possible outcomes |
| $\omega \in \Omega$ | a single outcome (sample point) |
| Event $A$ | a subset $A \subseteq \Omega$ |
| $P(A)$ | probability of event $A$ |
| $A \cup B$ | union: "$A$ or $B$" |
| $A \cap B$ | intersection: "$A$ and $B$" |
| $A^c$ | complement of $A$: "not $A$" |
| $\emptyset$ | empty set — the impossible event |
| $\sigma$-algebra $\mathcal{F}$ | collection of measurable events, closed under countable unions and complements |
| Probability space | $(\Omega, \mathcal{F}, P)$ — the full probabilistic model |
| Mutually exclusive | $A \cap B = \emptyset$: events cannot both occur |
| Partition | mutually exclusive events that collectively cover $\Omega$ |
