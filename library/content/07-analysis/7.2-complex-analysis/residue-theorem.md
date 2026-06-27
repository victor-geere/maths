---
title: Residue Theorem
tag: complex-analysis
summary: The contour integral of a meromorphic function equals 2πi times the sum of the residues of its poles inside the contour.
links:
  - laurent-series
  - cauchys-integral-theorem
  - holomorphic-functions
---

# Residue Theorem

The **Residue Theorem** is the most powerful computational tool in complex analysis. It states that the contour integral of a meromorphic function around a closed curve is completely determined by the **residues** at the poles lying inside the curve — a finite sum of local data that encodes the global integral. This is a profound generalisation of Cauchy's Integral Theorem (which says the integral is zero when there are no singularities inside). Beyond complex analysis itself, the Residue Theorem is a practical workhorse: it evaluates real definite integrals that resist all elementary techniques, computes inverse Laplace and Fourier transforms, and appears throughout quantum field theory and number theory.

## Statement

Let $f$ be meromorphic on an open set $U$ containing a simple closed positively oriented contour $\gamma$ and its interior. Let $z_1, \ldots, z_n$ be the poles of $f$ inside $\gamma$. Then:

$$\oint_\gamma f(z)\,dz = 2\pi i \sum_{k=1}^n \text{Res}(f, z_k)$$

## Strategy for Real Integrals

Many real integrals can be evaluated by:
1. Extend the integrand to a complex function $f(z)$.
2. Choose a contour $\gamma$ (often a semicircle or rectangle) whose integral reduces to the real integral.
3. Apply the Residue Theorem to compute the contour integral.
4. Extract the real part.

## Example: $\int_{-\infty}^\infty \frac{1}{1+x^2}\,dx$

Integrate $f(z) = \frac{1}{1+z^2}$ around a large semicircle in the upper half-plane.

Poles: $z = \pm i$. Only $z = i$ is inside the upper semicircle.

$$\text{Res}(f, i) = \lim_{z\to i}(z-i)\frac{1}{(z-i)(z+i)} = \frac{1}{2i}$$

$$\oint_\gamma f\,dz = 2\pi i \cdot \frac{1}{2i} = \pi$$

As the radius $\to \infty$, the arc integral $\to 0$ (Jordan's lemma), so:

$$\int_{-\infty}^\infty \frac{dx}{1+x^2} = \pi$$

## Computing Residues

- **Simple pole** at $z_0$: $\text{Res}(f, z_0) = \lim_{z\to z_0}(z-z_0)f(z)$
- **Ratio form** ($f = p/q$, simple zero of $q$ at $z_0$): $\text{Res} = p(z_0)/q'(z_0)$
- **Order-$m$ pole:** $\text{Res} = \frac{1}{(m-1)!}\lim_{z\to z_0}\frac{d^{m-1}}{dz^{m-1}}[(z-z_0)^m f(z)]$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\oint_\gamma f(z)\,dz$ | contour integral around closed curve $\gamma$ |
| $\text{Res}(f, z_k)$ | residue of $f$ at pole $z_k$ — coefficient $a_{-1}$ of the Laurent series |
| Meromorphic | holomorphic except at isolated poles |
| Positively oriented | counter-clockwise traversal of $\gamma$ |
| Pole | an isolated singularity where $|f(z)| \to \infty$ |
| $2\pi i$ | the key constant in Cauchy's theory |
| Upper half-plane | $\{z \in \mathbb{C} : \text{Im}(z) > 0\}$ |
| Jordan's lemma | the arc integral over a large semicircle vanishes when $|f| \to 0$ fast enough |
| Simple pole | a pole of order 1 |
| $p/q$ residue formula | $\text{Res}(p/q, z_0) = p(z_0)/q'(z_0)$ at a simple zero of $q$ |
