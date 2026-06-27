---
title: Basis & Dimension
tag: linear-algebra
summary: Minimal spanning sets of a vector space and the invariant count of vectors they contain.
links:
  - vector-spaces
  - linear-independence
  - row-reduction
---

## Basis

A **basis** of a vector space $V$ is a set $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ that is:
1. **Linearly independent**
2. **Spanning:** every $\mathbf{v} \in V$ is a linear combination of $\mathcal{B}$

Equivalently, every $\mathbf{v} \in V$ has a **unique** representation $\mathbf{v} = c_1\mathbf{b}_1 + \cdots + c_n\mathbf{b}_n$.

## Dimension

All bases of a finite-dimensional vector space $V$ have the same number of vectors. This common count is the **dimension** $\dim V$.

## Standard Bases

- $\mathbb{R}^n$: standard basis $\{\mathbf{e}_1, \ldots, \mathbf{e}_n\}$, dimension $n$.
- $M_{m\times n}$: matrix units $E_{ij}$, dimension $mn$.
- $P_n$: $\{1, x, x^2, \ldots, x^n\}$, dimension $n+1$.

## Finding a Basis

Row-reduce the matrix whose rows are the spanning vectors. Non-zero rows of the echelon form give a basis for the row space.

## Dimension Inequalities

- $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$
- If $U \subseteq W \subseteq V$ then $\dim U \leq \dim W \leq \dim V$.
- If $\dim U = \dim W$ and $U \subseteq W$, then $U = W$.

## Notes

- Infinite-dimensional spaces (e.g. function spaces) require more care; bases exist by Zorn's lemma.
- Dimension is the fundamental numeric invariant of a vector space over a field.
