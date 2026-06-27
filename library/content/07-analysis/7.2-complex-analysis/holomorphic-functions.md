---
title: Holomorphic Functions
tag: complex-analysis
summary: Complex functions that are complex-differentiable at every point — analytic functions with remarkable rigidity and geometric properties.
links:
  - complex-numbers
  - cauchy-riemann
  - cauchys-integral-theorem
  - eulers-formula
---

# Holomorphic Functions

A **holomorphic function** is a complex-valued function of a complex variable that is **complex-differentiable** — not just at a point, but in an open neighbourhood of every point in its domain. This apparently modest requirement turns out to impose extraordinary rigidity: a holomorphic function is automatically infinitely differentiable, expressible as a convergent power series (analytic), and completely determined on its entire domain by its values on any small open set. This stands in stark contrast to real analysis, where a smooth function can be modified locally without affecting distant values. Holomorphic functions are the central objects of **complex analysis**, one of the most elegant branches of mathematics.

## Definition

A function $f : U \to \mathbb{C}$ (where $U \subseteq \mathbb{C}$ is open) is **holomorphic** at $z_0$ if the complex derivative:

$$f'(z_0) = \lim_{h \to 0} \frac{f(z_0 + h) - f(z_0)}{h}$$

exists, where $h \to 0$ through complex values. $f$ is holomorphic on $U$ if it is holomorphic at every point of $U$.

## The Key Constraint: Direction Independence

In $\mathbb{R}$, $h \to 0$ along the real line. In $\mathbb{C}$, $h$ can approach zero from any direction in the complex plane. Requiring the limit to be the same regardless of direction imposes the **Cauchy–Riemann equations**.

## Examples

| Function | Holomorphic? | Notes |
|---|---|---|
| $f(z) = z^n$ | yes | polynomial |
| $f(z) = e^z$ | yes | entire |
| $f(z) = \sin z$, $\cos z$ | yes | entire |
| $f(z) = \ln z$ | yes on $\mathbb{C}\setminus(-\infty,0]$ | branch cut needed |
| $f(z) = \bar{z}$ | no | fails C–R equations |
| $f(z) = |z|^2$ | no (except at $z=0$) | not C–R |

## Remarkable Consequences of Holomorphicity

1. **Infinite differentiability:** holomorphic $\Rightarrow$ infinitely differentiable.
2. **Analyticity:** holomorphic $\Rightarrow$ locally equal to its Taylor series.
3. **Cauchy's theorem:** integrals over closed curves vanish.
4. **Maximum modulus principle:** $|f|$ has no interior maximum unless $f$ is constant.
5. **Liouville's theorem:** a bounded entire function is constant.
6. **Identity theorem:** if two holomorphic functions agree on a set with a limit point, they agree everywhere on their domain.

## Entire Functions

A function holomorphic on all of $\mathbb{C}$ is called **entire**. Examples: polynomials, $e^z$, $\sin z$, $\cos z$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Holomorphic | complex-differentiable in an open neighbourhood of every point |
| $f'(z_0)$ | complex derivative at $z_0$ |
| $h \to 0$ in $\mathbb{C}$ | $h$ approaches zero from any direction in the complex plane |
| Entire function | holomorphic on all of $\mathbb{C}$ |
| Cauchy–Riemann equations | necessary and sufficient conditions for holomorphicity in terms of real/imaginary parts |
| $\bar{z}$ | complex conjugate of $z$: if $z = x+iy$ then $\bar{z} = x-iy$ |
| Maximum modulus principle | $|f|$ cannot have a local maximum inside the domain |
| Liouville's theorem | bounded entire function must be constant |
| Identity theorem | two holomorphic functions agreeing on a dense set are identical |
| Branch cut | a curve removed from $\mathbb{C}$ to make a multi-valued function single-valued |
| $U \subseteq \mathbb{C}$ | an open subset of the complex plane |
