---
title: Uniform Distribution
tag: statistics
summary: The distribution that assigns equal probability to all outcomes in an interval (continuous) or a finite set (discrete).
links:
  - random-variables
  - expectation-variance
  - probability-axioms
---

# Uniform Distribution

The **Uniform distribution** is the mathematical embodiment of "equally likely." For a continuous Uniform$(a, b)$, every subinterval of the same length has the same probability — the density is flat. For a discrete Uniform on $\{1, \ldots, n\}$, each value occurs with probability $1/n$. These are the default distributions when we have no preference among outcomes: rolling a fair die, choosing a random number from a table, or drawing uniformly from a set. The continuous uniform distribution also plays a foundational role through the **probability integral transform**: if $F$ is any continuous CDF, then $F(X) \sim \text{Uniform}(0,1)$ — a fact used in simulation and goodness-of-fit testing.

## Continuous Uniform Distribution

$X \sim \text{Uniform}(a, b)$:

$$f(x) = \frac{1}{b-a}, \quad a \leq x \leq b$$

$$F(x) = \frac{x-a}{b-a}, \quad a \leq x \leq b$$

- $\mathbb{E}[X] = \dfrac{a+b}{2}$ (midpoint)
- $\text{Var}(X) = \dfrac{(b-a)^2}{12}$

## Discrete Uniform Distribution

$X$ takes values $\{a, a+1, \ldots, b\}$ each with probability $\dfrac{1}{b-a+1}$:

- $\mathbb{E}[X] = \dfrac{a+b}{2}$
- $\text{Var}(X) = \dfrac{(b-a)(b-a+2)}{12}$

## Probability Integral Transform

If $X$ has continuous CDF $F$, then $U = F(X) \sim \text{Uniform}(0,1)$.

**Simulation:** if $U \sim \text{Uniform}(0,1)$, then $X = F^{-1}(U)$ has CDF $F$.

## Order Statistics

If $U_{(1)} \leq U_{(2)} \leq \cdots \leq U_{(n)}$ are order statistics of $n$ iid Uniform$(0,1)$ samples, then:

$$\mathbb{E}[U_{(k)}] = \frac{k}{n+1}$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\text{Uniform}(a,b)$ | continuous uniform distribution on $[a,b]$ |
| $f(x) = 1/(b-a)$ | constant density — all intervals of equal length equally likely |
| $F(x) = (x-a)/(b-a)$ | CDF of Uniform$(a,b)$ |
| $\mathbb{E}[X] = (a+b)/2$ | mean is the midpoint of the interval |
| $\text{Var}(X) = (b-a)^2/12$ | variance of continuous Uniform |
| Probability integral transform | $F(X) \sim \text{Uniform}(0,1)$ for any continuous CDF $F$ |
| $F^{-1}$ | quantile function (inverse CDF) |
| Order statistics | $X_{(1)} \leq X_{(2)} \leq \cdots \leq X_{(n)}$ — sorted sample values |
| iid | independent and identically distributed |
| Simulation | generating samples from $F$ via $F^{-1}(U)$ where $U \sim \text{Uniform}(0,1)$ |
