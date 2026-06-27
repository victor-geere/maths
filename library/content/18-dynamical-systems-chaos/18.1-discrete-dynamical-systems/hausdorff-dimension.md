---
title: Hausdorff Dimension
tag: dynamical-systems
summary: The Hausdorff dimension is a real-valued generalisation of topological dimension defined via covering measurements at fine scales; it equals the topological dimension for smooth sets but can be non-integer for fractals.
links:
  - fractals
  - julia-mandelbrot
  - iterated-function-systems
  - lebesgue-measure
---

# Hausdorff Dimension

The **Hausdorff dimension** $d_H(F)$ of a set $F \subset \mathbb{R}^n$ is a real number in $[0,n]$ that generalises the intuitive notion of dimension. For a smooth manifold it agrees with the topological dimension, but for fractals it takes non-integer values — the Cantor set has $d_H \approx 0.631$ and the boundary of the Mandelbrot set has $d_H = 2$. The definition is based on measuring how the number of $\epsilon$-balls needed to cover $F$ scales as $\epsilon \to 0$: if $N(\epsilon) \sim \epsilon^{-d}$ then $d$ is the **box-counting dimension**, and the Hausdorff dimension is a rigorous version of this. Hausdorff dimension is the standard measure of fractal complexity and appears in the study of dynamical systems, number theory (badly approximable numbers), and geometric measure theory.

## Hausdorff Measure

For $d \geq 0$ and $F \subseteq \mathbb{R}^n$:
$$\mathcal{H}^d(F) = \lim_{\delta \to 0} \inf \left\{ \sum_i |U_i|^d : F \subseteq \bigcup_i U_i,\ |U_i| \leq \delta \right\}$$

where $|U|$ is the diameter of set $U$.

## Hausdorff Dimension

$$d_H(F) = \inf\{d \geq 0 : \mathcal{H}^d(F) = 0\} = \sup\{d : \mathcal{H}^d(F) = \infty\}$$

At $d = d_H(F)$, the Hausdorff measure $\mathcal{H}^{d_H}(F)$ can be $0$, $\infty$, or positive and finite.

## Box-Counting Dimension

$$d_B(F) = \lim_{\epsilon \to 0} \frac{\log N(\epsilon)}{\log(1/\epsilon)}$$

where $N(\epsilon)$ = minimum number of $\epsilon$-boxes covering $F$. In practice, $d_B$ is easier to compute than $d_H$, and $d_H \leq d_B$ (with equality for self-similar sets satisfying the open set condition).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathcal{H}^d(F)$ | $d$-dimensional Hausdorff measure of $F$ |
| $d_H(F)$ | Hausdorff dimension: critical value where $\mathcal{H}^d$ transitions |
| Diameter $|U|$ | $\sup\{d(x,y) : x,y \in U\}$ |
| $\delta$-cover | collection of sets $U_i$ with $|U_i| \leq \delta$ covering $F$ |
| Box-counting dimension $d_B$ | $\lim \frac{\log N(\epsilon)}{\log(1/\epsilon)}$ |
| $N(\epsilon)$ | minimum number of $\epsilon$-balls to cover $F$ |
| Open set condition | separation condition ensuring $d_H = $ similarity dimension for IFS |
| Self-similar set | $F = \bigcup f_i(F)$; $d_H$ solves $\sum r_i^{d_H} = 1$ |
| $d_H \leq d_B$ | Hausdorff $\leq$ box-counting; equal under open set condition |
