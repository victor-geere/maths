---
title: Multiple Regression
tag: statistics
summary: Modelling the response variable as a linear combination of multiple predictors, estimated by OLS in matrix form.
links:
  - linear-regression
  - mle
  - anova
  - expectation-variance
---

# Multiple Regression

**Multiple linear regression** extends simple linear regression to $p$ predictors $X_1, \ldots, X_p$, modelling the response as:

$$Y = \beta_0 + \beta_1 X_1 + \cdots + \beta_p X_p + \varepsilon$$

The model is naturally expressed in matrix form $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$, and the OLS solution $\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$ simultaneously minimises the sum of squared residuals across all coefficients. Multiple regression allows for **controlling** confounders, detecting **interaction effects**, and building predictive models. The Gauss–Markov theorem guarantees OLS is optimal under standard assumptions; the F-test tests whether all predictors together are useful; and partial $t$-tests assess individual predictors holding others fixed.

## Matrix Form

$$\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}, \quad \boldsymbol{\varepsilon} \sim N(\mathbf{0}, \sigma^2 \mathbf{I})$$

where $\mathbf{Y} \in \mathbb{R}^n$, design matrix $\mathbf{X} \in \mathbb{R}^{n \times (p+1)}$ (first column all 1s), $\boldsymbol{\beta} \in \mathbb{R}^{p+1}$.

## OLS Estimator

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$$

Exists when $\mathbf{X}$ has full column rank (no perfect multicollinearity).

## Properties

- $\mathbb{E}[\hat{\boldsymbol{\beta}}] = \boldsymbol{\beta}$ (unbiased)
- $\text{Var}(\hat{\boldsymbol{\beta}}) = \sigma^2(\mathbf{X}^T\mathbf{X})^{-1}$
- BLUE by Gauss–Markov

## Global $F$-Test

$H_0: \beta_1 = \cdots = \beta_p = 0$ (no predictors useful):

$$F = \frac{\text{ESS}/p}{\text{RSS}/(n-p-1)} \sim F_{p,n-p-1} \text{ under } H_0$$

## Coefficient of Determination

$$R^2 = 1 - \frac{\text{RSS}}{\text{TSS}}, \qquad \bar{R}^2 = 1 - \frac{\text{RSS}/(n-p-1)}{\text{TSS}/(n-1)}$$

$\bar{R}^2$ (adjusted) penalises adding uninformative predictors.

## Assumptions (LINE)

**L**inearity, **I**ndependence of errors, **N**ormality of errors, **E**qual variance (homoscedasticity).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathbf{X}$ | design matrix: $n \times (p+1)$, first column of 1s |
| $\boldsymbol{\beta}$ | coefficient vector $(\beta_0, \beta_1, \ldots, \beta_p)^T$ |
| $\hat{\boldsymbol{\beta}}$ | OLS estimate: $(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$ |
| $\mathbf{X}^T$ | transpose of design matrix |
| $p$ | number of predictors (excluding intercept) |
| $n$ | sample size |
| $F_{p,n-p-1}$ | $F$-distribution used for the global test |
| $R^2$ | coefficient of determination |
| $\bar{R}^2$ | adjusted $R^2$: penalises model complexity |
| Multicollinearity | near-perfect linear dependence among predictors |
| Confounder | a variable affecting both $X$ and $Y$; regression controls for it |
| Homoscedasticity | equal variance of errors $\varepsilon_i$ |
