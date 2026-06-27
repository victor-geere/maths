---
title: Lyapunov Exponents
tag: dynamical-systems
summary: Lyapunov exponents measure the average exponential rate of divergence or convergence of nearby trajectories; a positive largest Lyapunov exponent is the hallmark of chaos.
links:
  - chaos
  - iterated-maps
  - logistic-map
  - mixing-entropy
---

# Lyapunov Exponents

**Lyapunov exponents** quantify how quickly nearby trajectories in a dynamical system separate or converge. For a trajectory starting at $x_0$, the **largest Lyapunov exponent** $\lambda_1$ measures the average exponential growth rate of perturbations: a perturbation of size $\epsilon$ grows like $\epsilon e^{\lambda_1 t}$ for large $t$. A **positive** $\lambda_1$ is the defining quantitative signature of chaos — it implies that arbitrarily small uncertainties in initial conditions grow to macroscopic size, fundamentally limiting predictability. For systems in $\mathbb{R}^n$, there is a whole **Lyapunov spectrum** $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n$; the sum $\sum \lambda_i$ equals the average divergence of the vector field (Liouville's theorem: $\sum \lambda_i = 0$ for Hamiltonian systems).

## Definition: One-Dimensional Map

For $f: \mathbb{R} \to \mathbb{R}$ and orbit $x_0, x_1, \ldots$:
$$\lambda = \lim_{n \to \infty} \frac{1}{n} \ln|Df^n(x_0)| = \lim_{n\to\infty} \frac{1}{n}\sum_{k=0}^{n-1} \ln|f'(x_k)|$$

(when the limit exists, by Oseledets' multiplicative ergodic theorem).

## Definition: Flows in $\mathbb{R}^n$

For $\dot{x} = g(x)$ and solution $\phi_t(x_0)$, the **variational equation** is $\dot{\xi} = Dg(\phi_t(x_0))\xi$. The Lyapunov exponents are:
$$\lambda_i = \lim_{t\to\infty} \frac{1}{t} \ln \|\Phi_t e_i\|$$

where $\Phi_t$ is the fundamental matrix and $\{e_i\}$ is a well-chosen basis (Oseledets subspaces).

## Kaplan–Yorke Dimension

The **Lyapunov dimension** (Kaplan–Yorke conjecture):
$$d_{KY} = j + \frac{\lambda_1 + \cdots + \lambda_j}{|\lambda_{j+1}|}$$
where $j$ is the largest index with $\lambda_1 + \cdots + \lambda_j \geq 0$. For chaotic attractors, $d_{KY}$ often approximates the Hausdorff dimension.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Lyapunov exponent $\lambda$ | average exponential rate of divergence of nearby orbits |
| $\lambda > 0$ | chaos: exponential divergence |
| $\lambda < 0$ | convergence: stable behaviour |
| $\lambda = 0$ | neutral; e.g., quasi-periodic or at onset of chaos |
| Lyapunov spectrum | ordered tuple $\lambda_1 \geq \cdots \geq \lambda_n$ for $n$-dim system |
| Oseledets theorem | almost every orbit has well-defined Lyapunov exponents |
| Variational equation | ODE $\dot{\xi} = Dg(\phi_t) \xi$ governing linearised perturbations |
| $\sum_i \lambda_i$ | equals average $\nabla \cdot g$ (Liouville); 0 for Hamiltonian systems |
| Kaplan–Yorke dimension | $d_{KY}$: Lyapunov-based estimate of attractor dimension |
