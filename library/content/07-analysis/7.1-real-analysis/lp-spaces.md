---
title: Lᵖ Spaces
tag: analysis
summary: Spaces of functions whose p-th power is Lebesgue integrable, with a norm making them complete Banach spaces.
links:
  - lebesgue-integral
  - lebesgue-measure
  - banach-spaces
---

# Lᵖ Spaces

The **$L^p$ spaces** (read "ell-pee") are families of function spaces that make it possible to do linear algebra and geometry with functions. For $1 \leq p < \infty$, the space $L^p(\Omega)$ consists of all measurable functions $f$ on a domain $\Omega$ for which $|f|^p$ is Lebesgue integrable, equipped with the norm $\|f\|_p = \left(\int |f|^p\right)^{1/p}$. These spaces are **Banach spaces** — complete normed spaces — and $L^2$ is additionally a **Hilbert space**, with an inner product that makes it the natural infinite-dimensional analogue of Euclidean space. $L^p$ spaces are fundamental in harmonic analysis, PDEs, probability theory, and functional analysis.

## Definition

For $1 \leq p < \infty$ and a measure space $(\Omega, \mathcal{F}, \mu)$:

$$L^p(\Omega) = \left\{f : \Omega \to \mathbb{R} \;\text{measurable} : \int_\Omega |f|^p\,d\mu < \infty\right\}$$

with norm:

$$\|f\|_p = \left(\int_\Omega |f(x)|^p\,d\mu(x)\right)^{1/p}$$

Elements are equivalence classes: $f \sim g$ if $f = g$ almost everywhere.

For $p = \infty$:

$$\|f\|_\infty = \text{ess\,sup}|f| = \inf\{M : |f| \leq M \text{ a.e.}\}$$

## Key Inequalities

**Hölder's Inequality** (conjugate exponents $\frac{1}{p} + \frac{1}{q} = 1$):

$$\int |fg|\,d\mu \leq \|f\|_p \|g\|_q$$

**Minkowski's Inequality** (triangle inequality in $L^p$):

$$\|f + g\|_p \leq \|f\|_p + \|g\|_p$$

## Important Cases

| $p$ | Space | Key property |
|---|---|---|
| $1$ | $L^1$ | integrable functions; dual is $L^\infty$ |
| $2$ | $L^2$ | Hilbert space; inner product $\langle f,g\rangle = \int fg$ |
| $\infty$ | $L^\infty$ | essentially bounded functions |

## Completeness (Riesz–Fischer Theorem)

Every $L^p$ space ($1 \leq p \leq \infty$) is a **Banach space** — complete under the $\|\cdot\|_p$ norm. In particular, Cauchy sequences in $L^p$ converge to an element of $L^p$.

## Inclusion Relations

On a finite measure space $\Omega$: if $1 \leq p \leq q \leq \infty$ then $L^q(\Omega) \subseteq L^p(\Omega)$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $L^p(\Omega)$ | space of measurable functions with finite $p$-norm on $\Omega$ |
| $\|f\|_p$ | $L^p$ norm: $\left(\int |f|^p\right)^{1/p}$ |
| $\|f\|_\infty$ | essential supremum of $|f|$ |
| $\text{ess\,sup}$ | essential supremum — smallest $M$ with $|f| \leq M$ a.e. |
| Hölder's inequality | $\int|fg| \leq \|f\|_p\|g\|_q$ for conjugate $p, q$ |
| Minkowski's inequality | triangle inequality: $\|f+g\|_p \leq \|f\|_p + \|g\|_p$ |
| Conjugate exponents | $p$ and $q$ with $1/p + 1/q = 1$ |
| Banach space | a complete normed vector space |
| Hilbert space | a Banach space with an inner product |
| $\langle f, g\rangle$ | inner product in $L^2$: $\int fg\,d\mu$ |
| Riesz–Fischer Theorem | $L^p$ is complete for all $1 \leq p \leq \infty$ |
| Almost everywhere (a.e.) | holds except on a set of measure zero |
