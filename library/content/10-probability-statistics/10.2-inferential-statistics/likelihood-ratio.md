---
title: Likelihood Ratio Tests
tag: statistics
summary: A general method for testing composite hypotheses by comparing the maximum likelihood under H₁ to that under H₀ via the ratio Λ = L(H₀)/L(H₁).
links:
  - mle
  - hypothesis-testing
  - p-values
  - chi-squared-t
---

# Likelihood Ratio Tests

The **Likelihood Ratio Test (LRT)** is the most general and theoretically optimal method for testing hypotheses. It compares how well the data is explained under the null hypothesis $H_0$ to how well it is explained under the unrestricted model $H_1$ by forming the ratio $\Lambda = L(\hat{\theta}_{H_0}) / L(\hat{\theta})$. A small ratio (close to 0) means the data is much better explained by $H_1$ than $H_0$ — evidence against $H_0$. The power of the LRT is guaranteed by the **Neyman–Pearson lemma** for simple hypotheses: no other test at the same significance level has greater power. For large samples, **Wilks' theorem** provides a simple chi-squared approximation for the distribution of $-2\log\Lambda$.

## Setup

- $H_0$: $\theta \in \Theta_0$ (restricted parameter space)
- $H_1$: $\theta \in \Theta$ (full parameter space, $\Theta_0 \subset \Theta$)

The **likelihood ratio statistic**:

$$\Lambda = \frac{\sup_{\theta \in \Theta_0} L(\theta)}{\sup_{\theta \in \Theta} L(\theta)} = \frac{L(\hat{\theta}_{H_0})}{L(\hat{\theta}_{\text{MLE}})} \in [0, 1]$$

Reject $H_0$ when $\Lambda < c$ (or equivalently $-2\log\Lambda > \chi^2$ critical value).

## Wilks' Theorem

Under $H_0$ and regularity conditions, as $n \to \infty$:

$$-2\log\Lambda \xrightarrow{d} \chi^2_r$$

where $r = \dim\Theta - \dim\Theta_0$ is the number of restrictions (degrees of freedom).

**Practical use:** reject $H_0$ at level $\alpha$ if $-2\log\Lambda > \chi^2_{r,\alpha}$.

## Neyman–Pearson Lemma (Simple vs. Simple)

For testing $H_0: \theta = \theta_0$ vs $H_1: \theta = \theta_1$, the most powerful level-$\alpha$ test rejects when:

$$\frac{L(\theta_0; \mathbf{x})}{L(\theta_1; \mathbf{x})} < k_\alpha$$

## Example

Test $H_0: \mu = 0$ vs $H_1: \mu \neq 0$ for $X_1, \ldots, X_n \sim N(\mu, \sigma^2)$ (known $\sigma$).

$$-2\log\Lambda = \frac{n\bar{X}^2}{\sigma^2} = Z^2 \sim \chi^2_1 \text{ under } H_0$$

This recovers the standard $z$-test.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\Lambda$ | likelihood ratio statistic: $L(H_0)/L(H_1)$ |
| $-2\log\Lambda$ | log-likelihood ratio statistic; $\to \chi^2_r$ under $H_0$ |
| $\Theta_0 \subset \Theta$ | null parameter space is a subset of full space |
| $\hat{\theta}_{\text{MLE}}$ | unrestricted MLE |
| $\hat{\theta}_{H_0}$ | restricted MLE (MLE subject to $H_0$) |
| $r = \dim\Theta - \dim\Theta_0$ | degrees of freedom (number of restrictions) |
| Wilks' theorem | $-2\log\Lambda \to \chi^2_r$ as $n\to\infty$ under $H_0$ |
| Neyman–Pearson lemma | the LRT is the most powerful test for simple hypotheses |
| $\chi^2_{r,\alpha}$ | upper $\alpha$ quantile of chi-squared with $r$ df |
| Composite hypothesis | $H_0$ specifying a range of values, not a single point |
| Power | $P(\text{reject } H_0 \mid H_1)$ |
