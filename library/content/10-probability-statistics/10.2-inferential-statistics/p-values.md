---
title: p-Values
tag: statistics
summary: The probability, under the null hypothesis, of observing a test statistic at least as extreme as the one computed — a measure of how surprising the data is if H₀ were true.
links:
  - hypothesis-testing
  - confidence-intervals
  - likelihood-ratio
---

# p-Values

The **$p$-value** is the probability, computed assuming $H_0$ is true, of observing a test statistic at least as extreme as the one actually obtained from the data. A small $p$-value means the observed data would be very surprising if $H_0$ were true — providing evidence against it. We reject $H_0$ when $p < \alpha$ (the pre-chosen significance level). The $p$-value is widely used but widely misinterpreted: it is **not** the probability that $H_0$ is true, nor the probability that the result occurred by chance, nor a measure of practical significance. It is a continuous measure of evidence, and its correct interpretation is essential for drawing valid scientific conclusions.

## Definition

For a test statistic $T$ with observed value $t_{\text{obs}}$:

$$p\text{-value} = P(T \geq t_{\text{obs}} \mid H_0) \quad \text{(one-sided, upper)}$$

$$p\text{-value} = 2P(T \geq |t_{\text{obs}}| \mid H_0) \quad \text{(two-sided)}$$

## Decision Rule

$$p < \alpha \implies \text{reject } H_0 \quad \text{at significance level } \alpha$$

## Examples

**Two-sided $z$-test:** observed $z = 2.1$:

$$p = 2P(Z \geq 2.1) = 2(1 - \Phi(2.1)) \approx 2(0.018) = 0.036$$

At $\alpha = 0.05$: reject $H_0$ (since $0.036 < 0.05$).

## Common Misinterpretations

| Wrong | Right |
|---|---|
| "$p = 0.03$, so there is a 3% chance $H_0$ is true" | The $p$-value is not $P(H_0)$ |
| "We proved the effect is real" | We only rejected $H_0$; the effect could be trivially small |
| "$p > 0.05$ means $H_0$ is true" | Failure to reject $\neq$ accepting $H_0$ |

## Relationship to Confidence Intervals

At level $\alpha$: reject $H_0: \theta = \theta_0$ $\iff$ $\theta_0 \notin$ the $100(1-\alpha)$\% CI for $\theta$.

## $p$-Value Distribution

Under $H_0$ (and continuous test statistic): $p$-value $\sim \text{Uniform}(0,1)$.

Under $H_1$: $p$-values are stochastically smaller — concentrated near 0.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $p$-value | $P(\text{test statistic} \geq t_{\text{obs}} \mid H_0)$ |
| $\alpha$ | significance level; threshold for rejection |
| $t_{\text{obs}}$ | the observed value of the test statistic |
| $\Phi(z)$ | CDF of the standard normal |
| Two-sided $p$-value | $2P(T \geq |t_{\text{obs}}|)$ |
| Reject $H_0$ | conclude the data is incompatible with $H_0$ at level $\alpha$ |
| Statistical significance | $p < \alpha$; does not imply practical significance |
| Practical significance | the effect size — how large is the actual difference? |
| Effect size | a standardised measure of magnitude (e.g. Cohen's $d$) |
| $\text{Uniform}(0,1)$ | distribution of $p$-values under $H_0$ |
