---
title: ANOVA
tag: statistics
summary: Analysis of Variance — a method for testing whether the means of three or more groups are equal by decomposing total variance into between-group and within-group components.
links:
  - hypothesis-testing
  - chi-squared-t
  - multiple-regression
  - expectation-variance
---

# ANOVA

**Analysis of Variance (ANOVA)** tests whether the population means of three or more groups are equal, by decomposing the total variability in the data into variability **between groups** (due to group differences) and variability **within groups** (due to random error). If the between-group variability is large relative to the within-group variability, we have evidence that at least one group mean differs. Despite the name, ANOVA is about testing means, not variances — the variance decomposition is the computational tool. ANOVA is a generalisation of the two-sample $t$-test to multiple groups and is the foundation of experimental design and much of applied statistics.

## Setup: One-Way ANOVA

$k$ groups, $n_j$ observations in group $j$, total $n = \sum n_j$.

**Model:** $Y_{ij} = \mu_j + \varepsilon_{ij}$, $\varepsilon_{ij} \overset{\text{iid}}{\sim} N(0, \sigma^2)$.

**Hypotheses:**

$$H_0: \mu_1 = \mu_2 = \cdots = \mu_k \qquad H_1: \text{at least one } \mu_j \text{ differs}$$

## Sum of Squares Decomposition

$$\underbrace{\sum_{j=1}^k \sum_{i=1}^{n_j}(Y_{ij} - \bar{Y})^2}_{\text{SST (Total)}} = \underbrace{\sum_j n_j(\bar{Y}_j - \bar{Y})^2}_{\text{SSB (Between)}} + \underbrace{\sum_j\sum_i(Y_{ij}-\bar{Y}_j)^2}_{\text{SSW (Within)}}$$

## ANOVA Table

| Source | SS | df | MS | $F$ |
|---|---|---|---|---|
| Between | SSB | $k-1$ | $\text{MSB} = \text{SSB}/(k-1)$ | $F = \text{MSB}/\text{MSW}$ |
| Within | SSW | $n-k$ | $\text{MSW} = \text{SSW}/(n-k)$ | |
| Total | SST | $n-1$ | | |

Under $H_0$: $F \sim F_{k-1,\, n-k}$.

## Assumptions

1. **Independence:** observations are independent
2. **Normality:** responses within each group are normally distributed
3. **Homoscedasticity:** equal variance $\sigma^2$ across all groups

## Post-Hoc Tests

If $H_0$ is rejected, **post-hoc tests** identify which pairs of means differ, controlling the **family-wise error rate** (e.g. Tukey's HSD, Bonferroni).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mu_j$ | population mean of group $j$ |
| $\bar{Y}_j$ | sample mean of group $j$ |
| $\bar{Y}$ | grand mean (average of all observations) |
| SST | total sum of squares |
| SSB | between-group sum of squares (model sum of squares) |
| SSW | within-group sum of squares (error sum of squares) |
| df | degrees of freedom |
| MSB | mean square between = SSB / $(k-1)$ |
| MSW | mean square within = SSW / $(n-k)$ |
| $F$-statistic | $\text{MSB}/\text{MSW}$; large values suggest group differences |
| $F_{k-1,n-k}$ | $F$-distribution with $k-1$ and $n-k$ degrees of freedom |
| Homoscedasticity | equal variance of errors across groups |
| Post-hoc test | follow-up pairwise comparison after rejecting $H_0$ |
| Family-wise error rate | probability of at least one false rejection across multiple tests |
