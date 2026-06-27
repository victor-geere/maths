---
title: Orthogonality
tag: linear-algebra
summary: Perpendicularity in vector spaces, orthogonal complements, and orthogonal projections.
links:
  - dot-product-norms
  - gram-schmidt
  - spectral-theorem
---

## Definition

Vectors $\mathbf{u}$ and $\mathbf{v}$ are **orthogonal** (written $\mathbf{u} \perp \mathbf{v}$) if:

$$\mathbf{u} \cdot \mathbf{v} = 0$$

A set of vectors is **orthogonal** if all pairs are orthogonal; **orthonormal** if additionally each has unit norm.

## Orthogonal Complement

For a subspace $W \subseteq V$:

$$W^\perp = \{\mathbf{v} \in V : \mathbf{v} \perp \mathbf{w} \;\forall\, \mathbf{w} \in W\}$$

$W^\perp$ is a subspace, and $V = W \oplus W^\perp$ (direct sum).

## Orthogonal Projection

The projection of $\mathbf{v}$ onto a subspace $W$ with orthonormal basis $\{\mathbf{q}_1,\ldots,\mathbf{q}_k\}$:

$$\text{proj}_W \mathbf{v} = \sum_{i=1}^k (\mathbf{v} \cdot \mathbf{q}_i)\mathbf{q}_i = QQ^T\mathbf{v}$$

This is the **closest point** in $W$ to $\mathbf{v}$ (minimises $\|\mathbf{v} - \mathbf{w}\|$).

## Orthogonal Matrices

$Q$ is orthogonal if $Q^TQ = I$ (equivalently, columns are orthonormal).

- $\det(Q) = \pm 1$
- $Q^{-1} = Q^T$
- $\|Q\mathbf{v}\| = \|\mathbf{v}\|$ (isometry: preserves lengths and angles)

## Pythagorean Theorem

If $\mathbf{u} \perp \mathbf{v}$:

$$\|\mathbf{u} + \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2$$

## Notes

- Least-squares problems reduce to orthogonal projection onto the column space of $A$.
- Orthonormal bases make coordinate changes numerically stable.
