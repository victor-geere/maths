---
title: Bernoulli & Binomial
tag: statistics
summary: The Bernoulli distribution models a single yes/no trial; the Binomial counts successes in n independent Bernoulli trials.
links:
  - random-variables
  - expectation-variance
  - poisson-distribution
  - normal-distribution
---

# Bernoulli & Binomial

The **Bernoulli distribution** is the simplest non-trivial distribution: a single trial that succeeds with probability $p$ and fails with probability $1-p$. Repeat this trial $n$ times independently and count the successes — that count follows the **Binomial distribution** $\text{Bin}(n, p)$. The Binomial is one of the most important distributions in probability: it models coin flips, quality control defects, survey responses, and any process where outcomes are binary and independent. Its probabilities are given by the binomial coefficients, connecting combinatorics directly to probability. For large $n$, the Binomial is approximated by the Normal (CLT) or Poisson (when $p$ is small) distributions.

## Bernoulli Distribution

A random variable $X \sim \text{Bernoulli}(p)$:

$$P(X = 1) = p, \qquad P(X = 0) = 1 - p = q$$

- $\mathbb{E}[X] = p$
- $\text{Var}(X) = pq = p(1-p)$

## Binomial Distribution

$X \sim \text{Bin}(n, p)$: the number of successes in $n$ independent Bernoulli$(p)$ trials.

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n$$

- $\mathbb{E}[X] = np$
- $\text{Var}(X) = np(1-p)$

## Sum of Bernoullis

If $X_1, \ldots, X_n \overset{\text{iid}}{\sim} \text{Bernoulli}(p)$, then $X = X_1 + \cdots + X_n \sim \text{Bin}(n, p)$.

## Reproductive Property

If $X \sim \text{Bin}(m, p)$ and $Y \sim \text{Bin}(n, p)$ independently, then $X + Y \sim \text{Bin}(m+n, p)$.

## Approximations

**Normal:** for large $n$ and moderate $p$:
$$X \approx N(np,\, np(1-p))$$

**Poisson:** when $n$ is large and $p$ is small with $\lambda = np$ fixed:
$$P(X = k) \approx \frac{e^{-\lambda}\lambda^k}{k!}$$

## Mode

The most likely value is $\lfloor (n+1)p \rfloor$ or $\lfloor (n+1)p \rfloor - 1$ if $(n+1)p$ is an integer.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\text{Bernoulli}(p)$ | single trial: 1 with prob $p$, 0 with prob $1-p$ |
| $\text{Bin}(n,p)$ | number of successes in $n$ independent Bernoulli$(p)$ trials |
| $p$ | success probability |
| $q = 1-p$ | failure probability |
| $\binom{n}{k}$ | binomial coefficient: ways to choose $k$ successes from $n$ trials |
| $\mathbb{E}[X] = np$ | expected number of successes |
| $\text{Var}(X) = np(1-p)$ | variance of Binomial |
| iid | independent and identically distributed |
| Reproductive property | sum of independent Binomials with same $p$ is Binomial |
| $\lambda = np$ | Poisson approximation parameter |
| Mode | the most probable value |
