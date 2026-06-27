---
title: Central Limit Theorem
tag: statistics
summary: Sums of independent random variables converge in distribution to a normal.
links:
  - normal-distribution
---

## Key Formula

$$\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{\;d\;} \mathcal{N}(0,1) \quad \text{as } n\to\infty$$

## Notes

Let $X_1, X_2, \ldots$ be i.i.d. with mean $\mu$ and finite variance $\sigma^2$. The standardised sample mean converges **in distribution** to a standard [[normal-distribution|normal]].

### What "in distribution" means

The CDF of $\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}}$ converges pointwise to $\Phi(z)$ — it does **not** mean the random variables themselves converge.

### Practical upshot

For $n \geq 30$ (rule of thumb), the sample mean $\bar{X}_n$ is approximately $\mathcal{N}\!\left(\mu,\, \frac{\sigma^2}{n}\right)$, regardless of the underlying distribution.

This justifies:
- **$z$-tests** and **$t$-tests** for hypothesis testing
- **Confidence intervals** of the form $\bar{X} \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}$
- **Control charts** in quality control

### Berry–Esseen bound

The CLT approximation error is bounded:

$$\sup_x \left|P\!\left(\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \leq x\right) - \Phi(x)\right| \leq \frac{C\,\rho}{\sigma^3\sqrt{n}}$$

where $\rho = E[|X_1 - \mu|^3]$ and $C \approx 0.4748$.

### Multivariate CLT

For i.i.d. random vectors with mean $\boldsymbol{\mu}$ and covariance matrix $\Sigma$:

$$\sqrt{n}(\bar{\mathbf{X}}_n - \boldsymbol{\mu}) \xrightarrow{d} \mathcal{N}(\mathbf{0},\, \Sigma)$$
