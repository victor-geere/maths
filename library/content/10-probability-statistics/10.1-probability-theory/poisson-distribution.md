---
title: Poisson Distribution
tag: statistics
summary: The distribution of the number of rare events in a fixed interval when events occur independently at a constant average rate λ.
links:
  - random-variables
  - expectation-variance
  - binomial-distribution
  - exponential-distribution
---

# Poisson Distribution

The **Poisson distribution** with parameter $\lambda > 0$ models the count of rare, independent events occurring at a constant average rate $\lambda$ over a fixed period of time or space. Phone calls arriving at a switchboard, radioactive decays in one second, typos per page, or customers entering a shop per hour — whenever events are rare, independent, and arrive at a roughly constant rate, the Poisson distribution is the natural model. It is the limiting case of the Binomial when $n \to \infty$ and $p \to 0$ with $np \to \lambda$, and it has the remarkable property that its mean and variance are both equal to $\lambda$.

## PMF

$$P(X = k) = \frac{e^{-\lambda}\lambda^k}{k!}, \quad k = 0, 1, 2, \ldots$$

## Parameters

- **Mean:** $\mathbb{E}[X] = \lambda$
- **Variance:** $\text{Var}(X) = \lambda$
- **Mode:** $\lfloor \lambda \rfloor$ (and $\lfloor\lambda\rfloor - 1$ if $\lambda \in \mathbb{Z}$)

## Reproductive Property

If $X \sim \text{Poisson}(\lambda)$ and $Y \sim \text{Poisson}(\mu)$ independently:

$$X + Y \sim \text{Poisson}(\lambda + \mu)$$

## Poisson as Limit of Binomial

If $X_n \sim \text{Bin}(n, \lambda/n)$, then for fixed $k$:

$$P(X_n = k) \to \frac{e^{-\lambda}\lambda^k}{k!} \text{ as } n \to \infty$$

## Poisson Process

Arrivals in a Poisson process at rate $\lambda$ over time $[0,t]$ are $\text{Poisson}(\lambda t)$. The inter-arrival times follow the **Exponential$(\lambda)$** distribution.

## Examples

- A website receives 200 visits/hour on average. Probability of exactly 0 in a given minute:

$$P(X=0) = e^{-200/60} \approx e^{-3.33} \approx 0.036$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\text{Poisson}(\lambda)$ | Poisson distribution with rate $\lambda$ |
| $\lambda$ | average rate (mean and variance) |
| $e$ | Euler's number $\approx 2.71828$ |
| $k!$ | $k$ factorial |
| $\mathbb{E}[X] = \lambda$ | mean equals the rate parameter |
| $\text{Var}(X) = \lambda$ | variance also equals $\lambda$ — unique property |
| Reproductive property | sum of independent Poissons is Poisson with summed rates |
| Poisson process | a counting process with independent, rate-$\lambda$ arrivals |
| Inter-arrival time | time between consecutive events; $\sim \text{Exp}(\lambda)$ |
| Rare events | events with small individual probability but many trials |
