---
title: Period-Doubling & Bifurcations
tag: dynamical-systems
summary: A bifurcation is a qualitative change in the dynamics of a system as a parameter varies; period-doubling bifurcations cascade to chaos and are governed by the universal Feigenbaum constants.
links:
  - fixed-points-stability
  - logistic-map
  - chaos
  - lyapunov-exponents
---

# Period-Doubling & Bifurcations

A **bifurcation** occurs when a small change in a parameter causes a qualitative change in the behaviour of a dynamical system — such as a fixed point becoming unstable and giving birth to a periodic orbit. The **period-doubling bifurcation** is the most important route to chaos: as a parameter increases, a stable fixed point becomes a stable 2-cycle, then a 4-cycle, then an 8-cycle, and so on in an infinite cascade that accumulates at the onset of chaos. Feigenbaum discovered that the ratio of successive bifurcation parameter values converges to the **Feigenbaum constant** $\delta \approx 4.669$, which is universal across all one-dimensional maps with a quadratic maximum.

## Types of Bifurcations

- **Saddle-node (fold)**: two fixed points collide and annihilate as a parameter changes.
- **Transcritical**: two fixed points exchange stability.
- **Pitchfork**: one fixed point becomes three (symmetric systems).
- **Hopf**: an equilibrium loses stability and a limit cycle is born.
- **Period-doubling (flip)**: a periodic orbit doubles its period; eigenvalue $\lambda = -1$.

## Period-Doubling Cascade

For the logistic map $f_r(x) = rx(1-x)$ with parameter $r$:

| $r$ range | Behaviour |
|---|---|
| $0 < r < 1$ | $x = 0$ stable |
| $1 < r < 3$ | stable fixed point $x^* = 1 - 1/r$ |
| $3 < r < 3.449\ldots$ | stable 2-cycle |
| $3.449 < r < 3.544\ldots$ | stable 4-cycle |
| $r_\infty \approx 3.5699\ldots$ | onset of chaos |

## Feigenbaum Constants

- $\delta = \lim_{n\to\infty} \frac{r_n - r_{n-1}}{r_{n+1} - r_n} \approx 4.6692\ldots$ (rate of bifurcation accumulation)
- $\alpha \approx 2.5029\ldots$ (scaling of orbit width)

These constants are universal for all maps with a single quadratic maximum.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Bifurcation | qualitative change in dynamics as parameter varies |
| Bifurcation parameter | control parameter $r$ (or $\mu$) |
| Saddle-node bifurcation | two fixed points merge and disappear |
| Hopf bifurcation | equilibrium spawns a limit cycle |
| Period-doubling (flip) | orbit period doubles; eigenvalue through $-1$ |
| Cascade | sequence of period-doublings accumulating at $r_\infty$ |
| Feigenbaum constant $\delta \approx 4.669$ | universal ratio of bifurcation parameter spacings |
| $r_\infty \approx 3.5699$ | onset of chaos in logistic map |
| Bifurcation diagram | plot of orbit vs parameter showing all bifurcations |
