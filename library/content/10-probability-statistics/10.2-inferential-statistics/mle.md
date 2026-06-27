---
title: Point Estimation & MLE
tag: statistics
summary: Estimating unknown parameters from data — point estimators summarise a sample as a single best guess, and Maximum Likelihood Estimation finds the parameter that makes the observed data most probable.
links:
  - random-variables
  - expectation-variance
  - confidence-intervals
  - likelihood-ratio
---

# Point Estimation & MLE

A **point estimator** is a statistic $\hat{\theta}$ computed from a sample $X_1, \ldots, X_n$ that serves as a single best guess for an unknown population parameter $\theta$. Good estimators are **unbiased** (average value equals $\theta$), **consistent** (converge to $\theta$ as $n\to\infty$), and **efficient** (have small variance). **Maximum Likelihood Estimation (MLE)** is the most widely used method: it picks the parameter value that maximises the probability (likelihood) of having observed the data we actually saw. Under regularity conditions, MLEs are consistent, asymptotically normal, and achieve the Cramér–Rao lower bound on variance — making them asymptotically efficient.

## Estimator Properties

- **Unbiasedness:** $\mathbb{E}[\hat{\theta}] = \theta$
- **Consistency:** $\hat{\theta} \xrightarrow{P} \theta$ as $n \to \infty$
- **MSE (Mean Squared Error):** $\text{MSE}(\hat{\theta}) = \text{Var}(\hat{\theta}) + \text{Bias}(\hat{\theta})^2$

## Maximum Likelihood Estimation

The **likelihood function** for observed data $x_1, \ldots, x_n$ and parameter $\theta$:

$$L(\theta) = \prod_{i=1}^n f(x_i;\, \theta)$$

The **MLE** is $\hat{\theta}_{\text{MLE}} = \arg\max_\theta L(\theta)$.

In practice: maximise the **log-likelihood** $\ell(\theta) = \log L(\theta) = \sum_i \log f(x_i;\theta)$.

**Score equation:** $\ell'(\hat{\theta}) = 0$.

## Standard MLEs

| Model | MLE |
|---|---|
| $N(\mu, \sigma^2)$: estimate $\mu$ | $\hat{\mu} = \bar{X}$ |
| $N(\mu, \sigma^2)$: estimate $\sigma^2$ | $\hat{\sigma}^2 = \frac{1}{n}\sum(X_i-\bar{X})^2$ (biased) |
| $\text{Bernoulli}(p)$: estimate $p$ | $\hat{p} = \bar{X}$ |
| $\text{Poisson}(\lambda)$: estimate $\lambda$ | $\hat{\lambda} = \bar{X}$ |

## Cramér–Rao Lower Bound

For any unbiased estimator $\hat{\theta}$:

$$\text{Var}(\hat{\theta}) \geq \frac{1}{\mathcal{I}(\theta)}$$

where $\mathcal{I}(\theta) = -\mathbb{E}[\ell''(\theta)]$ is the **Fisher information**. MLEs achieve this bound asymptotically.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\hat{\theta}$ | point estimator of parameter $\theta$ |
| $L(\theta)$ | likelihood function |
| $\ell(\theta) = \log L(\theta)$ | log-likelihood — usually easier to maximise |
| MLE | Maximum Likelihood Estimator |
| Unbiased | $\mathbb{E}[\hat{\theta}] = \theta$ |
| Consistent | $\hat{\theta} \to \theta$ in probability as $n \to \infty$ |
| MSE | Mean Squared Error: $\text{Var}+\text{Bias}^2$ |
| $\mathcal{I}(\theta)$ | Fisher information: $-\mathbb{E}[\ell''(\theta)]$ |
| Cramér–Rao bound | $\text{Var}(\hat{\theta}) \geq 1/\mathcal{I}(\theta)$ for unbiased estimators |
| Score equation | $\ell'(\theta) = 0$ — finds the MLE |
| Asymptotically normal | $\sqrt{n}(\hat{\theta}-\theta) \to N(0, 1/\mathcal{I}(\theta))$ for MLEs |
