---
title: Hypothesis Testing
tag: statistics
summary: A formal procedure for deciding between a null hypothesis H₀ and an alternative H₁ based on data, controlling the probability of Type I error (false rejection).
links:
  - confidence-intervals
  - p-values
  - chi-squared-t
  - likelihood-ratio
---

# Hypothesis Testing

**Hypothesis testing** provides a formal framework for deciding whether data provides sufficient evidence to reject a stated assumption. We begin with a **null hypothesis** $H_0$ (a specific claim about a parameter, e.g. "the mean is 0") and an **alternative** $H_1$. A **test statistic** is computed from the data, and we reject $H_0$ if the statistic falls in a **rejection region** chosen to control the probability of falsely rejecting a true $H_0$ — the **Type I error rate** $\alpha$. The framework balances two types of errors: rejecting truth (Type I) and failing to detect a real effect (Type II). It is the backbone of scientific experimentation, clinical trials, and quality control.

## Key Concepts

| Concept | Definition |
|---|---|
| $H_0$ (null) | the default hypothesis; assumed true until evidence against |
| $H_1$ (alternative) | what we seek evidence for |
| Test statistic $T$ | a function of the data; measures evidence against $H_0$ |
| Rejection region | values of $T$ that lead to rejecting $H_0$ |
| Significance level $\alpha$ | $P(\text{reject } H_0 \mid H_0 \text{ true}) = \alpha$ |
| Power $1-\beta$ | $P(\text{reject } H_0 \mid H_1 \text{ true})$ |

## Type I and Type II Errors

| | $H_0$ true | $H_0$ false |
|---|---|---|
| Reject $H_0$ | **Type I error** (false positive, rate $\alpha$) | Correct (power) |
| Fail to reject | Correct | **Type II error** (false negative, rate $\beta$) |

## One-Sample $t$-Test

Test $H_0 : \mu = \mu_0$ vs $H_1 : \mu \neq \mu_0$ (two-sided):

$$T = \frac{\bar{X} - \mu_0}{S/\sqrt{n}} \sim t_{n-1} \text{ under } H_0$$

Reject $H_0$ if $|T| > t_{n-1,\,\alpha/2}$.

## $z$-Test (known $\sigma$)

$$Z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}} \sim N(0,1) \text{ under } H_0$$

Reject if $|Z| > z_{\alpha/2}$.

## One-Sided Tests

$H_1 : \mu > \mu_0$: reject if $T > t_{n-1,\alpha}$.

$H_1 : \mu < \mu_0$: reject if $T < -t_{n-1,\alpha}$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $H_0$ | null hypothesis |
| $H_1$ (or $H_a$) | alternative hypothesis |
| $\alpha$ | significance level; Type I error rate |
| $\beta$ | Type II error rate |
| Power $= 1-\beta$ | probability of correctly rejecting a false $H_0$ |
| $T$ | test statistic |
| $p$-value | probability under $H_0$ of observing a result at least as extreme as $T$ |
| Rejection region | critical region where $H_0$ is rejected |
| Two-sided test | $H_1 : \theta \neq \theta_0$ |
| One-sided test | $H_1 : \theta > \theta_0$ or $H_1 : \theta < \theta_0$ |
| $t_{n-1,\alpha/2}$ | critical value for two-sided $t$-test at level $\alpha$ |
