---
title: Moment Generating Functions
tag: statistics
summary: The function M(t) = E[e^{tX}] encodes all moments of a distribution and uniquely identifies it — a powerful analytical tool for sums of independent variables.
links:
  - expectation-variance
  - random-variables
  - central-limit-theorem
  - law-large-numbers
---

# Moment Generating Functions

The **moment generating function (MGF)** $M_X(t) = \mathbb{E}[e^{tX}]$ is a function of a real variable $t$ that encodes the entire distribution of $X$ in a single formula. Expanding $e^{tX}$ as a power series and taking expectations reveals that the derivatives of $M_X$ at $t=0$ give all the **moments** of $X$: the first derivative gives the mean, the second gives $\mathbb{E}[X^2]$, and so on. Moreover, if two random variables have the same MGF (when it exists in a neighbourhood of 0), they have the same distribution. This uniqueness property makes MGFs invaluable for proving the Central Limit Theorem, identifying distributions of sums of independent variables, and deriving tail bounds.

## Definition

$$M_X(t) = \mathbb{E}[e^{tX}] = \begin{cases}\sum_k e^{tx_k}\,p(x_k) & \text{(discrete)} \\ \int_{-\infty}^\infty e^{tx}\,f(x)\,dx & \text{(continuous)}\end{cases}$$

Defined for $t$ in an open interval $(-h, h)$ around $0$.

## Recovering Moments

$$\mathbb{E}[X^n] = M_X^{(n)}(0) = \left.\frac{d^n M_X}{dt^n}\right|_{t=0}$$

- $M_X'(0) = \mathbb{E}[X]$
- $M_X''(0) = \mathbb{E}[X^2]$
- $\text{Var}(X) = M_X''(0) - (M_X'(0))^2$

## Key Property: Sums of Independent Variables

If $X$ and $Y$ are independent:

$$M_{X+Y}(t) = M_X(t)\cdot M_Y(t)$$

This multiplicative property makes MGFs ideal for studying sums.

## Standard MGFs

| Distribution | $M_X(t)$ |
|---|---|
| $\text{Bernoulli}(p)$ | $1-p+pe^t$ |
| $\text{Bin}(n,p)$ | $(1-p+pe^t)^n$ |
| $\text{Poisson}(\lambda)$ | $e^{\lambda(e^t-1)}$ |
| $N(\mu,\sigma^2)$ | $e^{\mu t + \sigma^2 t^2/2}$ |
| $\text{Exp}(\lambda)$ | $\dfrac{\lambda}{\lambda-t}$, $t<\lambda$ |

## Uniqueness Theorem

If $M_X(t) = M_Y(t)$ for $t \in (-h, h)$ (some $h > 0$), then $X$ and $Y$ have the same distribution.

## Characteristic Function

The **characteristic function** $\varphi_X(t) = \mathbb{E}[e^{itX}]$ (with $i = \sqrt{-1}$) always exists and uniquely determines the distribution — even when the MGF does not.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $M_X(t)$ | moment generating function of $X$: $\mathbb{E}[e^{tX}]$ |
| $M_X^{(n)}(0)$ | $n$-th derivative at $t=0$: gives $\mathbb{E}[X^n]$ |
| $\mathbb{E}[X^n]$ | $n$-th moment of $X$ |
| Uniqueness theorem | same MGF $\Rightarrow$ same distribution |
| $M_{X+Y} = M_X \cdot M_Y$ | multiplicative property for independent $X, Y$ |
| Characteristic function $\varphi_X(t)$ | $\mathbb{E}[e^{itX}]$ — always exists; useful when MGF doesn't |
| $i = \sqrt{-1}$ | imaginary unit |
| Tail bound | MGF used in Chernoff bounds to bound $P(X > a)$ |
| Power series expansion | $e^{tX} = 1 + tX + t^2X^2/2! + \cdots$ — used to derive moment formulas |
