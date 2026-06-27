---
title: Iterated Maps & Orbits
tag: dynamical-systems
summary: A discrete dynamical system iterates a map f on a set X; the orbit of a point x is the sequence x, f(x), f²(x), … and studying orbits reveals fixed points, periodicity, and chaotic behaviour.
links:
  - fixed-points-stability
  - logistic-map
  - chaos
  - fractals
---

# Iterated Maps & Orbits

A **discrete dynamical system** is defined by a set $X$ (the **state space**) and a function $f: X \to X$. The **orbit** of a point $x_0 \in X$ is the sequence $x_0, x_1 = f(x_0), x_2 = f^2(x_0) = f(f(x_0)), \ldots$, where $f^n = f \circ f \circ \cdots \circ f$ ($n$ times) denotes the $n$-th iterate. Iterating even simple maps can produce extraordinarily complex behaviour: the logistic map $f(x) = rx(1-x)$ on $[0,1]$ transitions from stable fixed points through periodic orbits to full chaos as the parameter $r$ increases. The study of orbits — their limiting behaviour, periodicity, sensitivity to initial conditions, and statistical properties — is the heart of discrete dynamical systems.

## Definitions

- **Orbit of $x_0$**: $\mathcal{O}(x_0) = \{f^n(x_0) : n \geq 0\}$
- **Fixed point**: $f(x^*) = x^*$
- **Period-$n$ point**: $f^n(x) = x$ but $f^k(x) \neq x$ for $0 < k < n$
- **Eventually periodic**: $f^m(x)$ is periodic for some $m \geq 0$
- **$\omega$-limit set**: $\omega(x) = \{y : f^{n_k}(x) \to y\text{ for some }n_k \to \infty\}$ — where orbits accumulate

## Types of Behaviour

| Behaviour | Description |
|---|---|
| Fixed point | orbit $\{x^*\}$ |
| Periodic orbit | finite cycle $\{x_0, x_1, \ldots, x_{n-1}\}$ |
| Quasi-periodic | dense orbit on a torus |
| Chaotic | sensitive, dense orbit with positive Lyapunov exponent |

## Conjugacy

Two maps $f: X \to X$ and $g: Y \to Y$ are **topologically conjugate** if there is a homeomorphism $h: X \to Y$ with $h \circ f = g \circ h$. Conjugate maps have the same orbit structure.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $f^n$ | $n$-th iterate of $f$: $f$ composed with itself $n$ times |
| Orbit $\mathcal{O}(x_0)$ | sequence $x_0, f(x_0), f^2(x_0), \ldots$ |
| Fixed point $x^*$ | $f(x^*) = x^*$ |
| Period-$n$ point | $f^n(x) = x$, smallest such $n$ |
| $\omega$-limit set $\omega(x)$ | accumulation points of the orbit |
| Topological conjugacy | $h \circ f = g \circ h$ for homeomorphism $h$ |
| State space $X$ | domain on which $f$ acts |
| Attractor | invariant set attracting nearby orbits |
| Repeller | invariant set from which orbits diverge |
