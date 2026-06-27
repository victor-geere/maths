---
title: Confidence Intervals
tag: statistics
summary: A random interval constructed from data that contains the true parameter value with a specified probability — the most important tool for communicating estimation uncertainty.
links:
  - mle
  - hypothesis-testing
  - chi-squared-t
  - normal-distribution
---

# Confidence Intervals

A **confidence interval (CI)** is an interval $[L, U]$ computed from sample data that is designed to contain the unknown parameter $\theta$ with a specified probability $1 - \alpha$ (the **confidence level**, typically 95%). The key subtlety: the interval is random (different samples give different intervals), and the parameter is fixed — so we say "the procedure captures $\theta$ in 95% of repeated experiments," not "there is a 95% probability that $\theta$ lies in this particular interval." Confidence intervals quantify estimation uncertainty far more usefully than point estimates alone, and they are the standard reporting format in scientific publications.

## Definition

A **$100(1-\alpha)$\% confidence interval** for $\theta$ is a pair $(L(\mathbf{X}), U(\mathbf{X}))$ of statistics satisfying:

$$P(L(\mathbf{X}) \leq \theta \leq U(\mathbf{X})) = 1 - \alpha$$

## Normal Mean — Known $\sigma$

$$\bar{X} \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}$$

where $z_{\alpha/2}$ is the upper $\alpha/2$ quantile of $N(0,1)$.

For 95%: $z_{0.025} = 1.96$.

## Normal Mean — Unknown $\sigma$

$$\bar{X} \pm t_{n-1,\,\alpha/2}\frac{S}{\sqrt{n}}$$

where $t_{n-1,\,\alpha/2}$ is the upper $\alpha/2$ quantile of the $t_{n-1}$ distribution, and $S$ is the sample standard deviation.

## Width and Sample Size

Half-width of the CI for the mean: $w = z_{\alpha/2}\sigma/\sqrt{n}$.

To achieve width $\leq 2w$:

$$n \geq \left(\frac{z_{\alpha/2}\,\sigma}{w}\right)^2$$

## Interpretation

Out of 100 independent 95% CIs computed from 100 different samples, approximately 95 will contain the true $\theta$. Any single interval either does or does not contain $\theta$ — it is the **procedure** that has the 95% coverage probability.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $1-\alpha$ | confidence level (e.g. 0.95 for 95% CI) |
| $\alpha$ | significance level (e.g. 0.05) |
| $z_{\alpha/2}$ | upper $\alpha/2$ quantile of $N(0,1)$; $z_{0.025} = 1.96$ |
| $t_{n-1,\alpha/2}$ | upper $\alpha/2$ quantile of $t_{n-1}$ |
| $\bar{X}$ | sample mean |
| $S$ | sample standard deviation: $\sqrt{\frac{1}{n-1}\sum(X_i-\bar{X})^2}$ |
| $\sigma$ | population standard deviation (assumed known) |
| $n$ | sample size |
| Coverage probability | $P(L \leq \theta \leq U)$ — should equal $1-\alpha$ |
| Half-width | $z_{\alpha/2}\sigma/\sqrt{n}$ — determines precision |
| Margin of error | another name for half-width of a CI |
