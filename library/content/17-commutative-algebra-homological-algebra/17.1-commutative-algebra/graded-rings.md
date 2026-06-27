---
title: Graded Rings & Modules
tag: commutative-algebra
summary: A graded ring is one decomposed as a direct sum indexed by a monoid, with multiplication respecting the grading; graded rings arise from blow-ups, projective geometry, and the associated graded of a filtered ring.
links:
  - ring-axioms
  - modules
  - hilberts-basis
  - completion
  - projective-varieties
---

# Graded Rings & Modules

A **graded ring** is a ring $R$ equipped with a decomposition $R = \bigoplus_{n \geq 0} R_n$ as abelian groups such that $R_m \cdot R_n \subseteq R_{m+n}$. The canonical example is the polynomial ring $k[x_0,\ldots,x_n]$ graded by total degree: $R_d$ is the space of homogeneous polynomials of degree $d$. Graded rings and modules pervade algebraic geometry (the homogeneous coordinate ring of a projective variety, the Proj construction), commutative algebra (associated graded rings of filtrations, Rees algebras for blow-ups), and algebraic topology (cohomology rings are graded). The grading encodes important geometric and algebraic filtration data.

## Definitions

A **graded ring** is $R = \bigoplus_{n \geq 0} R_n$ with $R_m R_n \subseteq R_{m+n}$. Elements of $R_n$ are **homogeneous of degree $n$**.

A **graded $R$-module** is $M = \bigoplus_{n \in \mathbb{Z}} M_n$ with $R_m M_n \subseteq M_{m+n}$.

## Examples

- $k[x_1,\ldots,x_n]$ graded by degree: $R_d = $ homogeneous polynomials of degree $d$.
- $k[x_1,\ldots,x_n]/(f_1,\ldots,f_r)$ (homogeneous $f_i$): graded quotient ring.
- **Rees algebra** $\mathcal{R}(I) = \bigoplus_{n\geq 0} I^n t^n \subseteq R[t]$ for an ideal $I$: encodes blow-up.
- **Associated graded** $\mathrm{gr}_I R = \bigoplus_{n\geq 0} I^n/I^{n+1}$: local ring at a subvariety.

## Hilbert Function & Series

For a finitely generated graded module $M$ over $k[x_0,\ldots,x_r]$, the **Hilbert function** is $H_M(n) = \dim_k M_n$. For $n \gg 0$, $H_M(n)$ is a polynomial (**Hilbert polynomial**), whose degree encodes the dimension of the projective variety.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $R = \bigoplus_n R_n$ | graded ring decomposition |
| $R_n$ | degree-$n$ part (homogeneous component) |
| Homogeneous element | element lying in a single $R_n$ |
| Graded ideal | ideal $I$ with $I = \bigoplus_n (I \cap R_n)$ |
| Graded module $M = \bigoplus_n M_n$ | $R_m M_n \subseteq M_{m+n}$ |
| Rees algebra $\mathcal{R}(I)$ | $\bigoplus_{n\geq 0} I^n$; used for blow-ups |
| Associated graded $\mathrm{gr}_I R$ | $\bigoplus_{n\geq 0} I^n/I^{n+1}$ |
| Hilbert function $H_M(n)$ | $\dim_k M_n$; measures growth |
| Hilbert polynomial | polynomial agreeing with $H_M(n)$ for $n \gg 0$ |
| $\mathrm{Proj}(R)$ | projective scheme built from graded ring $R$ |
