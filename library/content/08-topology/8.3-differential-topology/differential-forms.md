---
title: Differential Forms
tag: differential-topology
summary: Antisymmetric multilinear objects on a manifold that generalise functions, gradients, curl, and volume — and can be integrated over curves, surfaces, and higher-dimensional submanifolds.
links:
  - tangent-spaces
  - smooth-manifolds
  - de-rham-cohomology
  - stokes-manifolds
---

# Differential Forms

**Differential forms** are the natural objects to integrate over manifolds. A **$k$-form** is an antisymmetric multilinear map on $k$ tangent vectors at each point, smoothly varying over the manifold. In $\mathbb{R}^3$, the familiar objects of vector calculus are secretly differential forms: functions are $0$-forms, the integrands $f\,dx$ of line integrals are $1$-forms, flux integrands $\mathbf{F} \cdot d\mathbf{S}$ are $2$-forms, and volume elements $f\,dx\,dy\,dz$ are $3$-forms. The **exterior derivative** $d$ unifies gradient, curl, and divergence into a single operation, and **Stokes' theorem** on manifolds — the grand unification of the fundamental theorem of calculus, Green's theorem, the classical Stokes theorem, and the divergence theorem — becomes a single elegant statement: $\int_M d\omega = \int_{\partial M} \omega$.

## $k$-Forms

A **$k$-form** $\omega$ on a manifold $M$ assigns to each point $p$ an antisymmetric $k$-linear map on $T_pM$.

**Basis in coordinates $(x^1, \ldots, x^n)$:** $k$-forms are spanned by:

$$dx^{i_1} \wedge dx^{i_2} \wedge \cdots \wedge dx^{i_k}, \quad i_1 < i_2 < \cdots < i_k$$

The space of $k$-forms is $\Omega^k(M)$, with $\dim\Omega^k(\mathbb{R}^n) = \binom{n}{k}$.

## Wedge Product

$$\alpha \wedge \beta = (-1)^{kl}\,\beta \wedge \alpha \quad (\alpha \in \Omega^k, \beta \in \Omega^l)$$

Antisymmetric (switching two factors negates the form).

## Exterior Derivative

$d : \Omega^k \to \Omega^{k+1}$, defined in coordinates:

$$d\omega = \sum_{i_1 < \cdots < i_k} \sum_j \frac{\partial \omega_{i_1\cdots i_k}}{\partial x^j}\,dx^j \wedge dx^{i_1} \wedge \cdots \wedge dx^{i_k}$$

Key properties: $d^2 = 0$; $d(f) = \nabla f$ for $f \in \Omega^0$.

## Dictionary: Vector Calculus in $\mathbb{R}^3$

| Differential form | Vector calculus object |
|---|---|
| $f$ (0-form) | scalar function |
| $f\,dx + g\,dy + h\,dz$ (1-form) | vector field $\mathbf{F} = (f,g,h)$ |
| $d$(1-form) | curl $\nabla \times \mathbf{F}$ |
| $d$(2-form) | divergence $\nabla \cdot \mathbf{F}$ |
| $dx\wedge dy\wedge dz$ (3-form) | volume element $dV$ |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\Omega^k(M)$ | space of smooth $k$-forms on $M$ |
| $k$-form | antisymmetric $k$-linear map on tangent vectors |
| $dx^i$ | basis 1-form: differential of the $i$-th coordinate |
| $\wedge$ | wedge (exterior) product; antisymmetric |
| $d$ | exterior derivative: $\Omega^k \to \Omega^{k+1}$ |
| $d^2 = 0$ | key identity: exterior derivative applied twice gives zero |
| Closed form | $d\omega = 0$ |
| Exact form | $\omega = d\eta$ |
| $\binom{n}{k}$ | binomial coefficient: number of $k$-forms on $\mathbb{R}^n$ |
| Antisymmetric | swapping two arguments changes the sign |
| Pullback $f^*\omega$ | pulling back a form on $N$ to $M$ via $f : M \to N$ |
| Integration of $k$-forms | $\int_{\Sigma} \omega$ over a $k$-dimensional submanifold $\Sigma$ |
