---
title: Exponential Distribution
tag: statistics
summary: The continuous distribution of waiting times between events in a Poisson process — uniquely characterised by its memoryless property.
links:
  - random-variables
  - poisson-distribution
  - expectation-variance
---

# Exponential Distribution

The **Exponential distribution** with rate $\lambda > 0$ describes the waiting time until the first event in a Poisson process occurring at rate $\lambda$. It is the continuous analogue of the Geometric distribution and is the only continuous distribution with the **memoryless property**: the remaining waiting time is independent of how long you have already waited. This makes it the natural model for lifetimes of components without wear (lightbulbs in idealised models), inter-arrival times in queuing theory, and survival times in reliability engineering. Its connection to the Poisson process ties it to much of applied probability.

## PDF and CDF

$$f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$$

$$F(x) = 1 - e^{-\lambda x}, \quad x \geq 0$$

## Parameters

- **Mean:** $\mathbb{E}[X] = \dfrac{1}{\lambda}$
- **Variance:** $\text{Var}(X) = \dfrac{1}{\lambda^2}$
- **Median:** $\dfrac{\ln 2}{\lambda}$
- **Mode:** $0$

## Memoryless Property

$$P(X > s + t \mid X > s) = P(X > t) \quad \text{for all } s, t \geq 0$$

The exponential distribution is the **unique** continuous distribution with this property. Given that you have already waited $s$ seconds, the probability of waiting at least $t$ more seconds is the same as if you started fresh.

## Relationship to Poisson Process

If events in a Poisson process occur at rate $\lambda$:
- Time until first event $\sim \text{Exp}(\lambda)$
- Number of events in $[0,t] \sim \text{Poisson}(\lambda t)$

## Minimum of Independent Exponentials

If $X_i \sim \text{Exp}(\lambda_i)$ independently, then $\min(X_1, \ldots, X_n) \sim \text{Exp}(\lambda_1 + \cdots + \lambda_n)$.

## Alternative Parametrisation

Some texts use $\text{Exp}(\beta)$ with mean $\beta = 1/\lambda$ (the **scale** parametrisation) rather than the rate $\lambda$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\text{Exp}(\lambda)$ | exponential distribution with rate $\lambda$ |
| $\lambda$ | rate parameter (events per unit time) |
| $1/\lambda$ | mean waiting time |
| $f(x) = \lambda e^{-\lambda x}$ | probability density function |
| $F(x) = 1 - e^{-\lambda x}$ | cumulative distribution function |
| Memoryless property | $P(X>s+t\mid X>s) = P(X>t)$ |
| Scale parameter $\beta$ | $\beta = 1/\lambda$: alternative way to parametrise |
| Poisson process | process in which inter-arrival times $\sim \text{Exp}(\lambda)$ |
| Survival function | $P(X > x) = e^{-\lambda x} = 1 - F(x)$ |
| Hazard rate | for Exp: constant $= \lambda$ (no wear or ageing) |
