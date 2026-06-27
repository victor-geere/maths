---
title: Dot Product & Norms
tag: linear-algebra
summary: Measuring lengths and angles in vector spaces via inner products and norms.
links:
  - orthogonality
  - gram-schmidt
  - vector-spaces
---

## Dot Product (Euclidean)

For $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$:

$$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = \mathbf{u}^T \mathbf{v}$$

**Geometric interpretation:**

$$\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$$

where $\theta$ is the angle between $\mathbf{u}$ and $\mathbf{v}$.

## Euclidean Norm

$$\|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}} = \sqrt{\sum_i v_i^2}$$

## Norm Axioms

A **norm** on $V$ satisfies:
1. $\|\mathbf{v}\| \geq 0$, with equality iff $\mathbf{v} = \mathbf{0}$
2. $\|c\mathbf{v}\| = |c|\|\mathbf{v}\|$
3. $\|\mathbf{u}+\mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$ (triangle inequality)

## Common Norms on $\mathbb{R}^n$

| Norm | Formula |
|---|---|
| $\ell^1$ | $\sum_i |v_i|$ |
| $\ell^2$ (Euclidean) | $\sqrt{\sum_i v_i^2}$ |
| $\ell^\infty$ | $\max_i |v_i|$ |
| $\ell^p$ | $\left(\sum_i |v_i|^p\right)^{1/p}$ |

## Cauchy–Schwarz Inequality

$$|\mathbf{u} \cdot \mathbf{v}| \leq \|\mathbf{u}\|\|\mathbf{v}\|$$

Equality holds iff $\mathbf{u}$ and $\mathbf{v}$ are linearly dependent.

## Notes

- The dot product is a special case of an **inner product** (bilinear, symmetric, positive-definite).
- Norms and inner products generalise to abstract vector spaces and function spaces.
