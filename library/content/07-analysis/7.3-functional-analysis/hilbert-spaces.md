---
title: Inner Product Spaces & Hilbert Spaces
tag: functional-analysis
summary: Vector spaces with an inner product generalising the dot product, and the complete such spaces — the infinite-dimensional analogues of Euclidean space.
links:
  - banach-spaces
  - lp-spaces
  - spectral-theorem
  - bounded-operators
---

# Inner Product Spaces & Hilbert Spaces

A **Hilbert space** is the infinite-dimensional analogue of Euclidean space: a vector space equipped with an **inner product** that defines lengths and angles, and which is **complete** (every Cauchy sequence converges). Hilbert spaces are the natural setting for quantum mechanics (state spaces are Hilbert spaces), signal processing (the $L^2$ space of square-integrable functions), and the theory of Fourier series (orthonormal bases in $L^2$). Their geometry — orthogonality, projections, orthonormal bases — works exactly as in $\mathbb{R}^n$, but now in infinite dimensions, making Hilbert spaces simultaneously abstract and computationally tractable.

## Inner Product

An **inner product** on a real vector space $V$ is a map $\langle \cdot, \cdot \rangle : V \times V \to \mathbb{R}$ satisfying:

1. **Linearity in first argument:** $\langle \alpha u + \beta v, w\rangle = \alpha\langle u,w\rangle + \beta\langle v,w\rangle$
2. **Symmetry:** $\langle u, v\rangle = \langle v, u\rangle$
3. **Positive definiteness:** $\langle v, v\rangle \geq 0$, with equality iff $v = \mathbf{0}$

The induced norm: $\|v\| = \sqrt{\langle v, v\rangle}$.

For complex spaces, symmetry becomes conjugate symmetry: $\langle u, v\rangle = \overline{\langle v, u\rangle}$.

## Hilbert Space

An inner product space that is **complete** under the induced norm is a **Hilbert space**.

## Standard Examples

| Space | Inner product |
|---|---|
| $\mathbb{R}^n$ | $\langle x, y\rangle = \sum_i x_i y_i$ |
| $\mathbb{C}^n$ | $\langle x, y\rangle = \sum_i x_i\overline{y_i}$ |
| $L^2(\Omega)$ | $\langle f, g\rangle = \int_\Omega f(x)\overline{g(x)}\,dx$ |
| $\ell^2$ | $\langle x, y\rangle = \sum_n x_n\overline{y_n}$ |

## Key Identities

**Cauchy–Schwarz:** $|\langle u, v\rangle| \leq \|u\|\,\|v\|$

**Parallelogram law:** $\|u+v\|^2 + \|u-v\|^2 = 2(\|u\|^2 + \|v\|^2)$

## Orthogonality and Projection

$u \perp v$ if $\langle u, v\rangle = 0$.

**Projection onto a closed subspace $M$:** every $v \in H$ decomposes uniquely as $v = m + m^\perp$ where $m \in M$ and $m^\perp \in M^\perp$.

## Orthonormal Bases

A sequence $\{e_n\}$ is **orthonormal** if $\langle e_m, e_n\rangle = \delta_{mn}$. If it is also complete (total), every $v \in H$ has a **Fourier expansion**:

$$v = \sum_n \langle v, e_n\rangle\, e_n \qquad \text{(Parseval: } \|v\|^2 = \sum_n |\langle v, e_n\rangle|^2\text{)}$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\langle u, v\rangle$ | inner product of $u$ and $v$ |
| $\|v\| = \sqrt{\langle v,v\rangle}$ | norm induced by the inner product |
| Hilbert space | complete inner product space |
| $L^2(\Omega)$ | square-integrable functions; $\langle f,g\rangle = \int f\bar{g}$ |
| $\ell^2$ | square-summable sequences |
| $u \perp v$ | $u$ and $v$ are orthogonal: $\langle u,v\rangle = 0$ |
| $M^\perp$ | orthogonal complement of subspace $M$ |
| Orthonormal | vectors with $\langle e_m, e_n\rangle = \delta_{mn}$ |
| $\delta_{mn}$ | Kronecker delta: 1 if $m=n$, else 0 |
| Cauchy–Schwarz | $|\langle u,v\rangle| \leq \|u\|\,\|v\|$ |
| Parseval's identity | $\|v\|^2 = \sum_n |\langle v,e_n\rangle|^2$ |
| Fourier expansion | expressing $v$ in terms of an orthonormal basis |
