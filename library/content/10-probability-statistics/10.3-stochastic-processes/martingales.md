---
title: Martingales
tag: stochastic-processes
summary: Stochastic processes where the conditional expectation of future values equals the current value — a formal model of a "fair game."
links:
  - brownian-motion
  - expectation-variance
  - markov-chains
---

# Martingales

A **martingale** is a stochastic process that models a "fair game": given all information up to the present, the expected future value equals the current value — no trend up or down. Named after a betting strategy (doubling bets to recover losses), martingales are one of the most important structures in modern probability theory. The **optional stopping theorem** (Doob) says that in a fair game, you cannot expect to profit by choosing when to stop — you cannot beat a martingale. Martingales are central to financial mathematics (risk-neutral pricing), hypothesis testing (sequential testing), and the rigorous analysis of algorithms (probabilistic arguments).

## Definition

A sequence $(M_n, \mathcal{F}_n)_{n \geq 0}$ is a **martingale** if:

1. $M_n$ is $\mathcal{F}_n$-measurable (adapted)
2. $\mathbb{E}[|M_n|] < \infty$
3. **Martingale property:** $\mathbb{E}[M_{n+1} \mid \mathcal{F}_n] = M_n$ for all $n$

**Submartingale:** $\mathbb{E}[M_{n+1} \mid \mathcal{F}_n] \geq M_n$ (tends upward)

**Supermartingale:** $\mathbb{E}[M_{n+1} \mid \mathcal{F}_n] \leq M_n$ (tends downward)

## Standard Examples

| Process | Martingale? |
|---|---|
| $W(t)$ (standard BM) | yes |
| $W(t)^2 - t$ | yes |
| $S_n = X_1 + \cdots + X_n$ where $\mathbb{E}[X_i]=0$ | yes |
| $\prod_i X_i$ where $\mathbb{E}[X_i]=1$ | yes |
| Biased random walk | no (sub or super) |

## Optional Stopping Theorem (Doob)

If $(M_n)$ is a martingale and $\tau$ is a stopping time with $\mathbb{E}[\tau] < \infty$ (and mild integrability), then:

$$\mathbb{E}[M_\tau] = \mathbb{E}[M_0]$$

**Application:** In a fair coin-flipping game, no stopping strategy can make you expect to profit.

## Martingale Convergence Theorem

An $L^2$-bounded martingale ($\sup_n \mathbb{E}[M_n^2] < \infty$) converges almost surely and in $L^2$.

## Doob's Maximal Inequality

$$P\!\left(\max_{0 \leq k \leq n} M_k \geq \lambda\right) \leq \frac{\mathbb{E}[M_n^+]}{\lambda}$$

## Risk-Neutral Pricing

In finance, under the **risk-neutral measure** $Q$, the discounted price process $e^{-rt}S_t$ is a martingale — guaranteeing no arbitrage.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $M_n$ | the value of the martingale at time $n$ |
| $\mathcal{F}_n$ | filtration (information available up to time $n$) |
| Adapted process | $M_n$ depends only on $\mathcal{F}_n$, not the future |
| $\mathbb{E}[M_{n+1}\mid\mathcal{F}_n] = M_n$ | martingale property — "fair game" condition |
| Stopping time $\tau$ | a random time determined by the process (not by looking into the future) |
| Optional Stopping Theorem | $\mathbb{E}[M_\tau] = \mathbb{E}[M_0]$ under regularity conditions |
| Submartingale | $\mathbb{E}[M_{n+1}\mid\mathcal{F}_n] \geq M_n$ — tends to increase |
| Supermartingale | $\mathbb{E}[M_{n+1}\mid\mathcal{F}_n] \leq M_n$ — tends to decrease |
| Martingale convergence | $L^2$-bounded martingale converges a.s. |
| Risk-neutral measure $Q$ | probability measure under which discounted prices are martingales |
| $L^2$-bounded | $\sup_n \mathbb{E}[M_n^2] < \infty$ |
