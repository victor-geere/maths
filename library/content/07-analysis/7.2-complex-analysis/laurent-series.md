---
title: Laurent Series & Residues
tag: complex-analysis
summary: The generalisation of Taylor series to functions with poles, including negative-power terms and the residue at each singularity.
links:
  - holomorphic-functions
  - cauchys-integral-theorem
  - residue-theorem
  - power-series
---

# Laurent Series & Residues

A **Laurent series** is the natural generalisation of a Taylor series to complex functions that may have **poles** — isolated singularities where the function blows up. While a Taylor series contains only non-negative powers of $(z - z_0)$, a Laurent series also includes negative powers, forming a "doubly infinite" sum. The coefficient of the $(-1)$-power term — the **residue** — is the most important quantity attached to a singularity: it controls the value of contour integrals around the singularity via the Residue Theorem. Laurent series and residues are the practical tools that make complex analysis applicable to the evaluation of real definite integrals, the study of differential equations, and the computation of inverse Laplace transforms.

## Laurent Series

For a function $f$ holomorphic on an annulus $r < |z - z_0| < R$:

$$f(z) = \sum_{n=-\infty}^{\infty} a_n (z - z_0)^n$$

where:

$$a_n = \frac{1}{2\pi i}\oint_\gamma \frac{f(z)}{(z-z_0)^{n+1}}\,dz$$

The sum splits into the **principal part** (negative powers) and the **analytic part** (non-negative powers).

## Classification of Isolated Singularities

| Type | Principal part | Example |
|---|---|---|
| Removable | no negative powers | $\frac{\sin z}{z}$ at $z=0$ |
| Pole of order $m$ | finitely many terms (down to $a_{-m}$) | $\frac{1}{z^m}$ at $z=0$ |
| Essential singularity | infinitely many negative powers | $e^{1/z}$ at $z=0$ |

## Residue

The **residue** of $f$ at $z_0$ is the Laurent coefficient $a_{-1}$:

$$\text{Res}(f, z_0) = a_{-1} = \frac{1}{2\pi i}\oint_\gamma f(z)\,dz$$

**For a simple pole:** $\text{Res}(f, z_0) = \lim_{z \to z_0}(z-z_0)f(z)$

**For a pole of order $m$:** $\text{Res}(f, z_0) = \dfrac{1}{(m-1)!}\lim_{z\to z_0}\dfrac{d^{m-1}}{dz^{m-1}}\!\left[(z-z_0)^m f(z)\right]$

## Example

$f(z) = \dfrac{e^z}{z^2}$ has a pole of order 2 at $z = 0$.

Laurent series: $\dfrac{1}{z^2}\left(1 + z + \dfrac{z^2}{2!} + \cdots\right) = \dfrac{1}{z^2} + \dfrac{1}{z} + \dfrac{1}{2} + \cdots$

Residue at $0$: $a_{-1} = 1$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Laurent series | $\sum_{n=-\infty}^\infty a_n(z-z_0)^n$ — power series including negative powers |
| $a_n$ | Laurent coefficients |
| Principal part | the terms with negative powers of $(z-z_0)$ |
| Analytic part | the terms with non-negative powers (a Taylor series) |
| $\text{Res}(f, z_0)$ | residue of $f$ at $z_0$: the coefficient $a_{-1}$ |
| Isolated singularity | a point where $f$ is not holomorphic but is holomorphic nearby |
| Removable singularity | singularity that can be "filled in" to make $f$ holomorphic |
| Pole of order $m$ | singularity with principal part down to $(z-z_0)^{-m}$ |
| Essential singularity | singularity with infinitely many negative-power terms |
| Annulus | the region $r < |z - z_0| < R$ between two concentric circles |
| Simple pole | a pole of order 1 |
