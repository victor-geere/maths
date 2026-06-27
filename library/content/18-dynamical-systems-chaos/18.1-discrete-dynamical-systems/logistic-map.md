---
title: The Logistic Map
tag: dynamical-systems
summary: The logistic map f(x) = rx(1−x) is the paradigmatic example of a one-dimensional discrete dynamical system exhibiting fixed points, periodic orbits, period-doubling, and chaos as the parameter r varies.
links:
  - iterated-maps
  - bifurcations
  - chaos
  - lyapunov-exponents
  - fractals
---

# The Logistic Map

The **logistic map** $f_r: [0,1] \to [0,1]$, $f_r(x) = rx(1-x)$, is perhaps the simplest example of a deterministic system that exhibits complex, seemingly random behaviour. Introduced in ecology by Robert May (1976) as a model of population dynamics, it became the canonical example demonstrating that chaos can arise from entirely deterministic rules with just one parameter $r \in [0,4]$. The map's complete dynamics are now understood: for $r < 1$ all orbits die out, for $1 < r < 3$ there is a single stable fixed point, then a cascade of period-doubling bifurcations leads to chaos at $r \approx 3.5699$, beyond which periods of every length coexist with chaotic behaviour (Sharkovskii's theorem: period 3 implies all periods).

## Definition & Fixed Points

$$f_r(x) = rx(1-x), \quad x \in [0,1], \quad r \in [0,4]$$

Fixed points: $f_r(x) = x \Rightarrow x = 0$ and $x^* = 1 - 1/r$ (for $r > 1$).

Stability of $x^*$: $f_r'(x^*) = r(1 - 2x^*) = 2 - r$.
- Stable ($|f_r'| < 1$) for $1 < r < 3$.
- Period-doubling at $r = 3$ ($f_r'(x^*) = -1$).

## Bifurcation Sequence

$$r_1 = 3,\ r_2 \approx 3.449,\ r_3 \approx 3.544,\ \ldots,\ r_\infty \approx 3.5699$$

At $r = 4$, the map is **fully chaotic**: it is topologically conjugate to the doubling map $\theta \mapsto 2\theta \pmod{1}$ on the circle via $x = \sin^2(\pi\theta)$.

## Lyapunov Exponent

$$\lambda = \lim_{n\to\infty} \frac{1}{n}\sum_{k=0}^{n-1} \ln|f_r'(x_k)|$$

Chaos occurs when $\lambda > 0$; periodicity when $\lambda < 0$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $f_r(x) = rx(1-x)$ | logistic map with parameter $r$ |
| $r \in [0,4]$ | parameter range ensuring $f_r: [0,1] \to [0,1]$ |
| Fixed point $x^* = 1 - 1/r$ | non-zero fixed point for $r > 1$ |
| Stability condition $|f'(x^*)| < 1$ | linearised criterion for stability |
| Period-doubling at $r_1 = 3$ | first bifurcation: $f'(x^*) = -1$ |
| $r_\infty \approx 3.5699$ | accumulation of period-doublings; onset of chaos |
| $r = 4$ | fully chaotic regime; conjugate to angle-doubling map |
| Lyapunov exponent $\lambda$ | $\lambda > 0$ signals chaos |
| Sharkovskii's theorem | period 3 $\Rightarrow$ period $n$ for all $n$ |
| Conjugacy to doubling map | $x = \sin^2(\pi\theta)$ intertwines $f_4$ with $\theta\mapsto 2\theta$ |
