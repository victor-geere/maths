---
title: Normal Distribution
tag: statistics
summary: The bell curve N(μ, σ²) — arises naturally from the Central Limit Theorem.
links:
  - central-limit-theorem
  - bayes-theorem
---

## Key Formula

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

## Notes

The normal (Gaussian) distribution $\mathcal{N}(\mu, \sigma^2)$ is parameterised by mean $\mu$ and variance $\sigma^2$.

### Standard normal

$Z \sim \mathcal{N}(0,1)$. Any normal can be standardised: $Z = \dfrac{X - \mu}{\sigma}$.

CDF: $\Phi(z) = P(Z \leq z)$ — tabulated or computed via the error function:

$$\Phi(z) = \frac{1}{2}\left[1 + \text{erf}\!\left(\frac{z}{\sqrt{2}}\right)\right]$$

### Empirical rule (68–95–99.7)

$$P(\mu - \sigma \leq X \leq \mu + \sigma) \approx 68.3\%$$
$$P(\mu - 2\sigma \leq X \leq \mu + 2\sigma) \approx 95.4\%$$
$$P(\mu - 3\sigma \leq X \leq \mu + 3\sigma) \approx 99.7\%$$

### Properties

- Symmetric about $\mu$; mean = median = mode
- Defined on $(-\infty, \infty)$
- $\text{Var}(X) = \sigma^2$, $\text{skewness} = 0$, $\text{kurtosis} = 3$
- Sum of independent normals is normal: $X+Y \sim \mathcal{N}(\mu_X+\mu_Y,\,\sigma_X^2+\sigma_Y^2)$

### Why it is everywhere

The [[central-limit-theorem|Central Limit Theorem]] guarantees that sample means of i.i.d. random variables with finite variance are approximately normal for large $n$ — regardless of the underlying distribution.
