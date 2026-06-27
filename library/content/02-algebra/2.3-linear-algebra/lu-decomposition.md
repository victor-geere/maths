---
title: LU Decomposition
tag: linear-algebra
summary: Factoring a matrix into lower and upper triangular factors for efficient solving.
links:
  - row-reduction
  - matrix-multiplication
  - determinant
---

## Definition

For a square matrix $A$, the **LU decomposition** writes:

$$A = LU$$

where $L$ is **lower triangular** with 1s on the diagonal, and $U$ is **upper triangular**.

With partial pivoting:

$$PA = LU$$

where $P$ is a permutation matrix.

## Why Useful

To solve $A\mathbf{x} = \mathbf{b}$:
1. Compute $A = LU$ once ($O(n^3)$).
2. Solve $L\mathbf{y} = \mathbf{b}$ by forward substitution.
3. Solve $U\mathbf{x} = \mathbf{y}$ by back substitution.

Steps 2–3 are $O(n^2)$, so multiple right-hand sides are cheap.

## Algorithm

LU is essentially Gaussian elimination: the multipliers used to zero entries below the diagonal become the entries of $L$; the resulting echelon form is $U$.

## Example

$$A = \begin{pmatrix}2&1\\6&4\end{pmatrix} = \begin{pmatrix}1&0\\3&1\end{pmatrix}\begin{pmatrix}2&1\\0&1\end{pmatrix} = LU$$

## Determinant via LU

$$\det(A) = \det(L)\det(U) = \prod_i u_{ii}$$

since $\det(L) = 1$ (lower triangular with unit diagonal).

## Notes

- LU exists without pivoting iff all leading principal minors are non-zero.
- With partial pivoting, $PA = LU$ always exists for non-singular $A$.
- The Cholesky factorisation $A = LL^T$ is the LU variant for symmetric positive-definite matrices.
