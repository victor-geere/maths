---
title: Random Variables
tag: statistics
summary: Functions mapping outcomes to real numbers, enabling the application of calculus and algebra to probabilistic quantities.
links:
  - sample-spaces
  - probability-axioms
  - expectation-variance
---

# Random Variables

A **random variable** is a function that assigns a real number to each outcome in a sample space, translating the language of events into the language of numbers — and thereby opening probability to the full power of analysis. Rather than thinking about events like "the die shows an even number," we think about the random variable $X$ whose value is the die's result. This shift allows us to compute expected values, variances, and moment generating functions; to study distributions via density functions or mass functions; and to state limit theorems like the central limit theorem. Random variables are the central objects of modern probability and statistics.

## Definition

A **random variable** $X$ on probability space $(\Omega, \mathcal{F}, P)$ is a measurable function:

$$X : \Omega \to \mathbb{R}$$

The **distribution** of $X$ is the probability measure $P_X(B) = P(X \in B)$ on $\mathbb{R}$.

## Discrete vs. Continuous

**Discrete random variable:** takes countably many values $x_1, x_2, \ldots$ Characterised by a **probability mass function (PMF)**:

$$p(x_k) = P(X = x_k) \geq 0, \qquad \sum_k p(x_k) = 1$$

**Continuous random variable:** takes values in an interval. Characterised by a **probability density function (PDF)** $f(x) \geq 0$:

$$P(a \leq X \leq b) = \int_a^b f(x)\,dx, \qquad \int_{-\infty}^\infty f(x)\,dx = 1$$

## Cumulative Distribution Function (CDF)

$$F(x) = P(X \leq x)$$

Valid for any random variable. Properties:
- Non-decreasing: $x_1 < x_2 \Rightarrow F(x_1) \leq F(x_2)$
- Right-continuous: $\lim_{y \to x^+} F(y) = F(x)$
- $\lim_{x\to-\infty}F(x) = 0$, $\lim_{x\to+\infty}F(x) = 1$

For continuous $X$: $f(x) = F'(x)$.

## Independence

Random variables $X$ and $Y$ are **independent** if:

$$P(X \in A,\, Y \in B) = P(X \in A)\,P(Y \in B) \quad \text{for all Borel sets } A, B$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $X : \Omega \to \mathbb{R}$ | random variable — maps outcomes to real numbers |
| PMF $p(x)$ | probability mass function for discrete $X$: $P(X = x)$ |
| PDF $f(x)$ | probability density function for continuous $X$ |
| CDF $F(x)$ | cumulative distribution function: $P(X \leq x)$ |
| $P(X \in B)$ | probability that $X$ takes a value in set $B$ |
| Discrete | takes countably many values |
| Continuous | takes values in an interval; described by a PDF |
| Independence | $P(X \in A, Y \in B) = P(X \in A)P(Y \in B)$ |
| Distribution $P_X$ | the probability measure induced by $X$ on $\mathbb{R}$ |
| Support | the set of values $x$ where $p(x) > 0$ or $f(x) > 0$ |
| Measurable function | $\{X \leq x\} \in \mathcal{F}$ for all $x$ — so $P(X \leq x)$ is well-defined |
