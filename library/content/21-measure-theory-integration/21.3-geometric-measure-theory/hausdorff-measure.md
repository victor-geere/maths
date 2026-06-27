---
title: Hausdorff Measure
tag: measure-theory
summary: The d-dimensional Hausdorff measure generalises length and area to non-integer dimensions; it assigns finite positive measure to d-dimensional subsets of ℝⁿ and is the basis for Hausdorff dimension in fractal geometry.
links:
  - measure-spaces
  - lebesgue-measure
  - hausdorff-dimension
  - outer-measure
  - rectifiable-sets
---

# Hausdorff Measure

The **$d$-dimensional Hausdorff measure** $\mathcal{H}^d$ is a Borel measure on $\mathbb{R}^n$ that generalises $d$-dimensional volume to arbitrary (including fractional) values of $d$. For $d \in \{0,1,2,\ldots,n\}$, $\mathcal{H}^d$ agrees with the standard measure: $\mathcal{H}^0$ is counting measure, $\mathcal{H}^1$ is arc length, $\mathcal{H}^2$ is area, and $\mathcal{H}^n = c_n \lambda^n$ (proportional to Lebesgue measure). For non-integer $d$, $\mathcal{H}^d$ assigns finite positive measure to $d$-dimensional fractal sets (like the Cantor set with $d = \log 2/\log 3$). The **Hausdorff dimension** of a set $F$ is the unique value $d = d_H(F)$ where $\mathcal{H}^d(F)$ transitions from $\infty$ to $0$, making Hausdorff measure the natural tool for measuring fractals and the foundation of geometric measure theory.

## Definition

For $d \geq 0$ and $\delta > 0$, define:
$$\mathcal{H}^d_\delta(F) = \inf\left\{\sum_i \omega_d\left(\frac{|U_i|}{2}\right)^d : F \subseteq \bigcup_i U_i,\ |U_i| \leq \delta\right\}$$

where $|U_i| = \mathrm{diam}(U_i)$ and $\omega_d = \pi^{d/2}/\Gamma(d/2+1)$ (volume of unit $d$-ball).

$$\mathcal{H}^d(F) = \lim_{\delta \to 0}\mathcal{H}^d_\delta(F)$$

## Relationship to Lebesgue Measure

$\mathcal{H}^n = \lambda^n$ on $\mathbb{R}^n$ (with the normalisation $\omega_n$).

## Hausdorff Dimension

$d_H(F) = \inf\{d : \mathcal{H}^d(F) = 0\} = \sup\{d : \mathcal{H}^d(F) = \infty\}$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathcal{H}^d$ | $d$-dimensional Hausdorff measure |
| $\mathcal{H}^d_\delta$ | Hausdorff premeasure at scale $\delta$ |
| $|U_i| = \mathrm{diam}(U_i)$ | diameter of covering set |
| $\omega_d$ | volume of unit $d$-ball: $\pi^{d/2}/\Gamma(d/2+1)$ |
| $\delta$-cover | collection $\{U_i\}$ with $\mathrm{diam}(U_i)\leq\delta$ covering $F$ |
| $d_H(F)$ | Hausdorff dimension |
| $\mathcal{H}^0$ | counting measure |
| $\mathcal{H}^1$ | 1-dimensional Hausdorff measure = arc length |
| $\mathcal{H}^n = \lambda^n$ | in $\mathbb{R}^n$, Hausdorff = Lebesgue (up to normalisation) |
