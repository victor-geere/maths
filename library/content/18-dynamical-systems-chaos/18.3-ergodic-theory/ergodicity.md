---
title: Ergodicity
tag: dynamical-systems
summary: An ergodic transformation is one for which the only invariant measurable sets have measure 0 or 1; by Birkhoff's theorem, time averages equal space averages for ergodic systems.
links:
  - measure-preserving
  - birkhoff-ergodic
  - mixing-entropy
  - haar-measure
---

# Ergodicity

An ergodic transformation is one for which the **time average** of any observable equals its **space average** — the fundamental law of statistical mechanics. Formally, a measure-preserving transformation $T: (X,\mu) \to (X,\mu)$ is **ergodic** if every $T$-invariant measurable set $A$ (with $T^{-1}A = A$) satisfies $\mu(A) \in \{0,1\}$. This means the system cannot be decomposed into two invariant parts of positive measure: dynamics on the whole space is "indecomposable". By Birkhoff's ergodic theorem, ergodicity is equivalent to: for $\mu$-a.e. $x$ and every $f \in L^1(\mu)$, $\frac{1}{n}\sum_{k=0}^{n-1} f(T^k x) \to \int f\,d\mu$.

## Definition

$(X, \mathcal{B}, \mu, T)$ is **ergodic** if:
$$T^{-1}A = A \implies \mu(A) = 0 \text{ or } 1$$

Equivalently, the only $T$-invariant $L^2$ functions are constants (a.e.).

## Ergodic Hierarchy

Ergodicity sits at the base of a hierarchy of stronger mixing properties:
$$\text{Bernoulli} \implies \text{Mixing} \implies \text{Weak mixing} \implies \text{Ergodic}$$

## Examples

| System | Ergodic? |
|---|---|
| Irrational rotation $T_\alpha$, $\alpha \notin \mathbb{Q}$ | Yes |
| Rational rotation $T_{p/q}$ | No (period-$q$ orbits form invariant sets) |
| Doubling map $x \mapsto 2x \pmod 1$ | Yes (and mixing) |
| Bernoulli shift | Yes (and Bernoulli) |

## Mean Ergodic Theorem (von Neumann)

For $f \in L^2(\mu)$:
$$\frac{1}{n}\sum_{k=0}^{n-1} f \circ T^k \xrightarrow{L^2} \mathbb{E}[f | \mathcal{I}]$$

where $\mathcal{I}$ is the $\sigma$-algebra of $T$-invariant sets. If $T$ is ergodic, $\mathcal{I}$ is trivial and the limit is $\int f\,d\mu$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Ergodic transformation | only invariant sets have measure $0$ or $1$ |
| Invariant set $A$ | $T^{-1}A = A$ |
| Time average | $\frac{1}{n}\sum_{k=0}^{n-1} f(T^k x)$ |
| Space average | $\int f\,d\mu$ |
| Birkhoff's theorem | time avg $=$ space avg a.e. when $T$ ergodic |
| $L^2(\mu)$ | square-integrable functions; $\int |f|^2\,d\mu < \infty$ |
| Mean ergodic theorem | $L^2$-convergence of time averages |
| Ergodic decomposition | any MPS is an integral of ergodic components |
| Irrational rotation | ergodic but not mixing |
| Mixing | $\mu(T^{-n}A \cap B) \to \mu(A)\mu(B)$; stronger than ergodic |
