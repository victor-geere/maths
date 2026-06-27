---
title: Simple Linear Regression
tag: statistics
summary: Modelling a linear relationship between a response variable Y and a single predictor X, estimating the slope and intercept by minimising squared residuals.
links:
  - expectation-variance
  - mle
  - hypothesis-testing
  - multiple-regression
---

# Simple Linear Regression

**Simple linear regression** models the relationship between a numerical response $Y$ and a single numerical predictor $X$ by fitting a straight line $Y = \beta_0 + \beta_1 X + \varepsilon$. The coefficients $\beta_0$ (intercept) and $\beta_1$ (slope) are estimated by **Ordinary Least Squares (OLS)**: minimising the sum of squared differences between observed $y_i$ and fitted $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$. Linear regression is the foundational model of statistical learning — it quantifies how much $Y$ changes per unit increase in $X$, provides formal hypothesis tests on the relationship, and gives a starting framework that extends to multiple predictors, generalised linear models, and machine learning.

## The Model

$$Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \quad \varepsilon_i \overset{\text{iid}}{\sim} N(0, \sigma^2)$$

- $\beta_0$: population intercept
- $\beta_1$: population slope (effect of 1-unit increase in $X$ on $Y$)
- $\varepsilon_i$: random error (noise)

## OLS Estimators

Minimise $\text{RSS} = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2$:

$$\hat{\beta}_1 = \frac{\sum_i(x_i - \bar{x})(y_i - \bar{y})}{\sum_i(x_i - \bar{x})^2} = \frac{S_{xy}}{S_{xx}}$$

$$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}$$

## Properties (under Gauss–Markov)

- $\hat{\beta}_0$ and $\hat{\beta}_1$ are **unbiased**: $\mathbb{E}[\hat{\beta}_j] = \beta_j$
- **BLUE**: Best Linear Unbiased Estimators (by Gauss–Markov theorem)

## Coefficient of Determination $R^2$

$$R^2 = 1 - \frac{\text{RSS}}{\text{TSS}} = \frac{\text{ESS}}{\text{TSS}} \in [0,1]$$

- $\text{TSS} = \sum(y_i-\bar{y})^2$ (total variation)
- $\text{ESS} = \sum(\hat{y}_i-\bar{y})^2$ (explained variation)
- $R^2 = r^2$ where $r$ is the Pearson correlation

## Testing $H_0: \beta_1 = 0$

$$T = \frac{\hat{\beta}_1}{\text{SE}(\hat{\beta}_1)} \sim t_{n-2} \text{ under } H_0$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $Y$ | response (dependent) variable |
| $X$ | predictor (independent) variable |
| $\beta_0$ | intercept: predicted $Y$ when $X=0$ |
| $\beta_1$ | slope: change in $Y$ per unit change in $X$ |
| $\varepsilon_i$ | error term; assumed $\sim N(0,\sigma^2)$ |
| $\hat{\beta}_0, \hat{\beta}_1$ | OLS estimates of intercept and slope |
| RSS | Residual Sum of Squares: $\sum(y_i - \hat{y}_i)^2$ |
| TSS | Total Sum of Squares: $\sum(y_i - \bar{y})^2$ |
| ESS | Explained Sum of Squares: $\text{TSS} - \text{RSS}$ |
| $R^2$ | coefficient of determination: fraction of variance explained |
| Gauss–Markov theorem | OLS is BLUE under homoscedastic errors |
| BLUE | Best Linear Unbiased Estimator |
