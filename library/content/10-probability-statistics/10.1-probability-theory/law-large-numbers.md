---
title: Law of Large Numbers
tag: statistics
summary: As the number of independent trials grows, the sample mean converges to the population mean — in probability (weak LLN) or almost surely (strong LLN).
links:
  - expectation-variance
  - central-limit-theorem
  - moment-generating
---

# Law of Large Numbers

The **Law of Large Numbers (LLN)** is the mathematical justification for statistical inference: it guarantees that the sample mean of a large number of independent, identically distributed random variables converges to the true population mean $\mu$. This is why casino operators are confident in their long-run profits, pollsters trust large samples, and scientists replicate experiments. There are two versions: the **Weak LLN** says the sample mean converges to $\mu$ **in probability** (the deviation becomes unlikely), while the **Strong LLN** gives the stronger statement that convergence holds **almost surely** (with probability 1). Both rest on the variance shrinking as $1/n$ when averaging $n$ independent variables.

## Setup

Let $X_1, X_2, \ldots$ be iid random variables with $\mathbb{E}[X_i] = \mu$ and $\text{Var}(X_i) = \sigma^2 < \infty$.

Define the **sample mean**: $\bar{X}_n = \dfrac{1}{n}\sum_{i=1}^n X_i$.

## Key Properties of $\bar{X}_n$

$$\mathbb{E}[\bar{X}_n] = \mu, \qquad \text{Var}(\bar{X}_n) = \frac{\sigma^2}{n}$$

The variance shrinks to 0, pulling the distribution tightly around $\mu$.

## Weak Law of Large Numbers

$$\bar{X}_n \xrightarrow{P} \mu: \quad \forall\, \varepsilon > 0,\; P(|\bar{X}_n - \mu| > \varepsilon) \to 0 \text{ as } n \to \infty$$

**Proof via Chebyshev:** $P(|\bar{X}_n - \mu| > \varepsilon) \leq \dfrac{\text{Var}(\bar{X}_n)}{\varepsilon^2} = \dfrac{\sigma^2}{n\varepsilon^2} \to 0$.

## Strong Law of Large Numbers

$$\bar{X}_n \xrightarrow{\text{a.s.}} \mu: \quad P\!\left(\lim_{n\to\infty}\bar{X}_n = \mu\right) = 1$$

Requires only $\mathbb{E}[|X|] < \infty$ (finite mean). Proved by Kolmogorov.

## Relationship to Central Limit Theorem

The LLN says **where** $\bar{X}_n$ converges ($\to \mu$). The CLT says **how fast** and in what **shape**: $\sqrt{n}(\bar{X}_n - \mu)/\sigma \to N(0,1)$.

## Examples

- Flipping a fair coin: the fraction of heads $\to 1/2$ as flips $\to \infty$.
- Casino: the house edge ensures average profit $\to$ positive for large number of bets.
- Polling: sample proportion converges to true population proportion.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\bar{X}_n$ | sample mean of $n$ observations |
| $\mu = \mathbb{E}[X]$ | population mean (true expected value) |
| $\sigma^2 = \text{Var}(X)$ | population variance |
| iid | independent and identically distributed |
| $\xrightarrow{P}$ | convergence in probability |
| $\xrightarrow{\text{a.s.}}$ | almost sure convergence (with probability 1) |
| Weak LLN | $P(|\bar{X}_n - \mu| > \varepsilon) \to 0$ for all $\varepsilon > 0$ |
| Strong LLN | $P(\lim_n \bar{X}_n = \mu) = 1$ |
| Chebyshev's inequality | $P(|X - \mu| > \varepsilon) \leq \sigma^2/\varepsilon^2$ |
| CLT | Central Limit Theorem — describes the distribution of $\bar{X}_n$ around $\mu$ |
