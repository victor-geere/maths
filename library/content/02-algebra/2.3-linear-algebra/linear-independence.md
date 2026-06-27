---
title: Linear Independence & Span
tag: linear-algebra
summary: Vectors are independent when no one is a linear combination of the others.
links:
  - determinant
  - eigenvalues
---

## Key Formula

$$\sum_{i=1}^{n} c_i\,\mathbf{v}_i = \mathbf{0} \;\implies\; c_i = 0 \;\forall\, i$$

## Notes

A set $\{\mathbf{v}_1, \ldots, \mathbf{v}_n\}$ is **linearly independent** if the only solution to $\sum c_i \mathbf{v}_i = \mathbf{0}$ is the trivial one (all $c_i = 0$).

If a non-trivial solution exists, the set is **linearly dependent** — at least one vector is redundant.

### Span

$$\text{span}\{\mathbf{v}_1,\ldots,\mathbf{v}_n\} = \left\{\sum_{i=1}^n c_i\mathbf{v}_i \;\middle|\; c_i \in \mathbb{R}\right\}$$

The span is the smallest subspace containing all the vectors.

### Basis and dimension

A **basis** of a vector space $V$ is a linearly independent set that spans $V$.

All bases of $V$ have the same number of vectors — this is the **dimension** $\dim(V)$.

### Checking independence

- Stack vectors as columns of matrix $A$
- Row-reduce to echelon form
- Independent iff every column has a pivot (equivalently, $\det(A) \neq 0$ when $A$ is square)

### Rank-nullity theorem

For a linear map represented by $m \times n$ matrix $A$:

$$\text{rank}(A) + \text{nullity}(A) = n$$

where $\text{rank}(A) = \dim(\text{col}(A))$ and $\text{nullity}(A) = \dim(\ker(A))$.

Geometric read: the dimensions of the image and kernel sum to the dimension of the domain.
