---
title: Brownian Motion
tag: stochastic-processes
summary: A continuous-time stochastic process with independent Gaussian increments — the scaling limit of random walks and the foundation of stochastic calculus.
links:
  - markov-chains
  - normal-distribution
  - martingales
---

# Brownian Motion

**Brownian motion** (or the **Wiener process**) is the canonical continuous-time stochastic process: a random path that wanders continuously yet is nowhere differentiable, with independent Gaussian increments at every scale. Physically, it models the erratic motion of a pollen grain suspended in water — observed by Robert Brown in 1827 and explained by Einstein in 1905. Mathematically, it is the **scaling limit of the simple random walk**, the **driving noise** for stochastic differential equations (SDEs), and the underlying process in the Black–Scholes model for option pricing. Brownian motion is to stochastic calculus what the real line is to classical calculus: the fundamental object from which everything else is built.

## Definition

A stochastic process $\{W(t) : t \geq 0\}$ is a **standard Brownian motion** if:

1. $W(0) = 0$
2. **Continuous paths:** $t \mapsto W(t)$ is continuous almost surely
3. **Independent increments:** $W(t) - W(s)$ is independent of $\mathcal{F}_s$ for $t > s$
4. **Gaussian increments:** $W(t) - W(s) \sim N(0, t-s)$

## Key Properties

- $\mathbb{E}[W(t)] = 0$, $\text{Var}(W(t)) = t$
- $\text{Cov}(W(s), W(t)) = \min(s,t)$
- Paths are continuous but **nowhere differentiable** (with probability 1)
- **Quadratic variation:** $[W]_t = t$ (not 0, unlike smooth functions)

## Scaling and Symmetry

- **Scaling:** $c^{-1/2}W(ct)$ is also standard BM (self-similar with exponent $1/2$)
- **Time reversal:** $W(T-t) - W(T)$ is BM for fixed $T$
- **Reflection:** $-W(t)$ is BM

## Connection to Random Walk

If $X_1, X_2, \ldots \overset{\text{iid}}{\sim} \pm 1$ (fair), the scaled partial sum:

$$W^{(n)}(t) = \frac{1}{\sqrt{n}}\sum_{k=1}^{\lfloor nt \rfloor} X_k \xrightarrow{d} W(t)$$

(Donsker's invariance principle / functional CLT).

## Stochastic Calculus (Itô)

The stochastic differential $dW$ satisfies $(dW)^2 = dt$, giving Itô's formula:

$$df(W_t) = f'(W_t)\,dW_t + \tfrac{1}{2}f''(W_t)\,dt$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $W(t)$ or $B(t)$ | standard Brownian motion at time $t$ |
| Wiener process | another name for standard Brownian motion |
| $N(0,t)$ | normal distribution with mean 0 and variance $t$ |
| Independent increments | $W(t)-W(s)$ independent of the past up to time $s$ |
| Gaussian increments | increments $W(t)-W(s) \sim N(0,t-s)$ |
| Quadratic variation $[W]_t$ | equals $t$; reflects the roughness of BM paths |
| $(dW)^2 = dt$ | Itô's rule for products of differentials |
| Itô's formula | stochastic chain rule for functions of BM |
| SDE | Stochastic Differential Equation |
| Nowhere differentiable | BM paths have infinite variation on any interval |
| Donsker's theorem | scaled random walk converges in distribution to BM |
