---
title: Expected Value & Variance
tag: statistics
summary: The mean (centre of mass) and spread of a random variable's distribution — the two most fundamental summaries of any probability distribution.
links:
  - random-variables
  - probability-axioms
  - moment-generating
---

# Expected Value & Variance

The **expected value** (or mean) $\mathbb{E}[X]$ of a random variable is its long-run average: if the experiment is repeated many times, the average of the observed values converges to $\mathbb{E}[X]$ by the Law of Large Numbers. The **variance** $\text{Var}(X)$ measures how spread out the values are around this mean — a small variance means values cluster near the mean, a large variance means they are widely scattered. Together, mean and variance are the two most important summaries of a distribution. They combine elegantly: the variance of a sum of independent variables is the sum of their variances, and the mean is linear in general. These properties underpin the theory of estimation, regression, and hypothesis testing.

## Expected Value

**Discrete:**
$$\mathbb{E}[X] = \sum_k x_k\, p(x_k)$$

**Continuous:**
$$\mathbb{E}[X] = \int_{-\infty}^\infty x\, f(x)\,dx$$

Exists when $\sum_k |x_k| p(x_k) < \infty$ (or the integral converges absolutely).

## Properties of Expectation

| Property | Formula |
|---|---|
| Linearity | $\mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y]$ |
| Constant | $\mathbb{E}[c] = c$ |
| Non-negativity | $X \geq 0 \Rightarrow \mathbb{E}[X] \geq 0$ |
| LOTUS | $\mathbb{E}[g(X)] = \sum_k g(x_k)p(x_k)$ (or integral form) |
| Independence | $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$ if $X \perp Y$ |

## Variance

$$\text{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$$

The **standard deviation** $\sigma_X = \sqrt{\text{Var}(X)}$ has the same units as $X$.

## Properties of Variance

| Property | Formula |
|---|---|
| Scaling | $\text{Var}(aX) = a^2\text{Var}(X)$ |
| Shift | $\text{Var}(X + c) = \text{Var}(X)$ |
| Independent sum | $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)$ if $X \perp Y$ |
| General sum | $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y)$ |

## Covariance and Correlation

$$\text{Cov}(X, Y) = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)] = \mathbb{E}[XY] - \mu_X\mu_Y$$

$$\rho(X,Y) = \frac{\text{Cov}(X,Y)}{\sigma_X\sigma_Y} \in [-1, 1]$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathbb{E}[X]$ | expected value (mean) of $X$ |
| $\mu_X$ | another notation for $\mathbb{E}[X]$ |
| $\text{Var}(X)$ | variance of $X$: $\mathbb{E}[(X-\mu)^2]$ |
| $\sigma_X$ | standard deviation: $\sqrt{\text{Var}(X)}$ |
| $\sigma_X^2$ | variance (same as $\text{Var}(X)$) |
| LOTUS | Law of the Unconscious Statistician: $\mathbb{E}[g(X)]$ via $g(x)$ weighted by PMF/PDF |
| Linearity of expectation | $\mathbb{E}[aX+bY] = a\mathbb{E}[X]+b\mathbb{E}[Y]$ — holds without independence |
| $X \perp Y$ | $X$ and $Y$ are independent |
| $\text{Cov}(X,Y)$ | covariance — measures linear association between $X$ and $Y$ |
| $\rho(X,Y)$ | Pearson correlation coefficient: $\text{Cov}/(\sigma_X\sigma_Y) \in [-1,1]$ |
| $\mathbb{E}[X^2] - (\mathbb{E}[X])^2$ | computational formula for variance |
