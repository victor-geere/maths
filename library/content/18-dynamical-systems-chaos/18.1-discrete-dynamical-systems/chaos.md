---
title: Chaos & Sensitive Dependence
tag: dynamical-systems
summary: A chaotic system is a deterministic dynamical system with sensitive dependence on initial conditions — nearby trajectories diverge exponentially — combined with topological transitivity and dense periodic orbits.
links:
  - logistic-map
  - lyapunov-exponents
  - iterated-maps
  - fractals
  - bifurcations
---

# Chaos & Sensitive Dependence

**Chaos** in a deterministic dynamical system refers to behaviour that appears random despite following exact deterministic rules. A system is **chaotic** if it is (1) **sensitive to initial conditions** — nearby trajectories diverge exponentially over time — (2) **topologically transitive** — there is a dense orbit — and (3) has **dense periodic orbits**. Sensitivity is measured by the **Lyapunov exponent**: a positive Lyapunov exponent means that two trajectories starting $\epsilon$ apart will diverge to distance $\sim \epsilon e^{\lambda t}$, making long-term prediction impossible regardless of computational precision. The famous "butterfly effect" captures this sensitivity: Lorenz (1963) discovered that a simple system of 3 ODEs modelling atmospheric convection was chaotic, implying inherent limits on weather forecasting.

## Devaney's Definition of Chaos

A continuous map $f: X \to X$ on a metric space is **chaotic** (in the sense of Devaney) if:
1. **Sensitive dependence**: $\exists \delta > 0$ such that for all $x \in X$ and $\epsilon > 0$, there is $y$ with $d(x,y) < \epsilon$ and $n$ with $d(f^n(x), f^n(y)) > \delta$.
2. **Topological transitivity**: $\exists x$ with dense orbit.
3. **Dense periodic orbits**: the periodic points are dense in $X$.

## Lyapunov Exponent

For a map $f$ on $\mathbb{R}$:
$$\lambda(x_0) = \lim_{n\to\infty} \frac{1}{n}\sum_{k=0}^{n-1}\ln|f'(x_k)|$$

- $\lambda > 0$: chaos (exponential divergence)
- $\lambda < 0$: periodic/stable
- $\lambda = 0$: boundary (e.g., period-doubling onset)

## Lorenz System

$$\dot{x} = \sigma(y-x), \quad \dot{y} = x(\rho - z) - y, \quad \dot{z} = xy - \beta z$$

For $\sigma = 10, \rho = 28, \beta = 8/3$, the system is chaotic with a **strange attractor** — the Lorenz butterfly.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Sensitive dependence | nearby orbits diverge exponentially |
| Lyapunov exponent $\lambda$ | rate of divergence: $\lambda > 0$ signals chaos |
| Topological transitivity | some orbit is dense in $X$ |
| Dense periodic orbits | periodic points are everywhere |
| Strange attractor | fractal attractor in phase space of a chaotic system |
| Lorenz system | classic 3-ODE chaotic system modelling convection |
| Butterfly effect | colloquial term for sensitive dependence on initial conditions |
| Mixing | statistical strengthening of transitivity |
| Devaney chaos | sensitive + transitive + dense periodic orbits |
| Topological entropy $h(f)$ | measure of exponential orbit complexity; $h > 0$ implies chaos |
