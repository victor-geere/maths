---
title: Chi-Squared & t-Distributions
tag: statistics
summary: Two distributions derived from the Normal — chi-squared arises as a sum of squared standard normals, and the t-distribution as the ratio of a normal to the square root of a scaled chi-squared.
links:
  - normal-distribution
  - random-variables
  - hypothesis-testing
  - mle
---

# Chi-Squared & t-Distributions

The **chi-squared** and **Student's $t$** distributions are workhorses of inferential statistics, arising directly from samples drawn from Normal populations. The **chi-squared distribution** $\chi^2_k$ is the distribution of a sum of squares of $k$ independent standard normal variables — it quantifies the variability of a sample variance. The **$t$-distribution** $t_k$ with $k$ degrees of freedom arises when estimating a population mean from a small sample whose variance is also unknown — it accounts for the extra uncertainty from estimating the variance, producing heavier tails than the Normal. Both distributions underpin the most widely used hypothesis tests and confidence intervals in classical statistics.

## Chi-Squared Distribution

If $Z_1, \ldots, Z_k \overset{\text{iid}}{\sim} N(0,1)$, then:

$$Q = Z_1^2 + Z_2^2 + \cdots + Z_k^2 \sim \chi^2_k$$

- $\mathbb{E}[Q] = k$
- $\text{Var}(Q) = 2k$
- PDF: $f(x) = \dfrac{x^{k/2-1}e^{-x/2}}{2^{k/2}\Gamma(k/2)}$, $\;x > 0$

**Key use:** If $X_1,\ldots,X_n \overset{\text{iid}}{\sim} N(\mu,\sigma^2)$, then $\dfrac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$.

## Student's $t$-Distribution

If $Z \sim N(0,1)$ and $Q \sim \chi^2_k$ independently:

$$T = \frac{Z}{\sqrt{Q/k}} \sim t_k$$

- $\mathbb{E}[T] = 0$ (for $k > 1$)
- $\text{Var}(T) = \dfrac{k}{k-2}$ (for $k > 2$)
- As $k \to \infty$: $t_k \to N(0,1)$

**Key use:** one-sample $t$-test:

$$T = \frac{\bar{X} - \mu_0}{S/\sqrt{n}} \sim t_{n-1} \quad \text{under } H_0 : \mu = \mu_0$$

## $F$-Distribution

The ratio of two independent chi-squared variables (scaled by their degrees of freedom):

$$F = \frac{Q_1/d_1}{Q_2/d_2} \sim F_{d_1, d_2}$$

Used in ANOVA and comparing variances.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\chi^2_k$ | chi-squared distribution with $k$ degrees of freedom |
| $k$ | degrees of freedom — number of independent squared normals |
| $Z_i \sim N(0,1)$ | independent standard normal variables |
| $t_k$ | Student's $t$-distribution with $k$ degrees of freedom |
| $S^2$ | sample variance $= \frac{1}{n-1}\sum(X_i - \bar{X})^2$ |
| $\bar{X}$ | sample mean |
| $\Gamma(k/2)$ | gamma function: $\Gamma(n) = (n-1)!$ for positive integers |
| $F_{d_1,d_2}$ | $F$-distribution with degrees of freedom $d_1$ and $d_2$ |
| Degrees of freedom | number of independent pieces of information; $n-1$ for sample variance |
| Heavy tails | $t$-distribution has more probability far from the mean than Normal |
| $t$-test | hypothesis test using the $t$-distribution for unknown $\sigma$ |
