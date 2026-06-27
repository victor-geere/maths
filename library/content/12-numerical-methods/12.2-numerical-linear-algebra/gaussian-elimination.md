---
title: Gaussian Elimination
tag: numerical-methods
summary: The fundamental algorithm for solving linear systems by row-reducing the augmented matrix to upper-triangular form, then back-substituting.
links:
  - row-reduction
  - lu-decomposition
  - condition-number
  - linear-systems
---

# Gaussian Elimination

**Gaussian elimination** is the algorithmic embodiment of the row-reduction technique for solving linear systems $A\mathbf{x} = \mathbf{b}$. By applying a sequence of elementary row operations to the augmented matrix $[A|\mathbf{b}]$, it transforms $A$ to upper-triangular form (**row echelon form**), after which the unknowns are found by **back substitution** from the bottom row upward. This is the most widely taught algorithm in linear algebra and the computational basis of many other numerical methods. In practice, **partial pivoting** — always swapping rows to place the largest available entry in the pivot position — is essential for numerical stability, preventing catastrophic cancellation errors that arise with small pivots.

## Algorithm

**Forward elimination** — reduce to upper triangular form:

For column $k = 1, \ldots, n-1$:
1. (**Partial pivoting**) swap row $k$ with the row below having the largest $|a_{ik}|$
2. For each row $i = k+1, \ldots, n$: compute multiplier $m_{ik} = a_{ik}/a_{kk}$, then

$$R_i \leftarrow R_i - m_{ik} R_k$$

**Back substitution** — solve $U\mathbf{x} = \mathbf{b}'$ (where $U$ is upper triangular):

$$x_n = b_n'/u_{nn}, \qquad x_i = \frac{b_i' - \sum_{j=i+1}^n u_{ij}x_j}{u_{ii}}$$

## Complexity

- Forward elimination: $O(n^3/3)$ operations
- Back substitution: $O(n^2/2)$ operations
- Total: $O(n^3)$ — dominated by forward elimination

## Partial Pivoting

Partial pivoting (reordering rows) is essential in floating-point arithmetic. Without it, small pivots cause large multipliers $m_{ik}$, amplifying rounding errors. The result is $PA = LU$ where $P$ is a permutation matrix.

## Relation to LU Factorisation

The multipliers $m_{ik}$ stored during elimination become the entries of the lower-triangular matrix $L$; the resulting upper-triangular form is $U$. So Gaussian elimination computes the LU factorisation.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $A\mathbf{x} = \mathbf{b}$ | the linear system being solved |
| $[A|\mathbf{b}]$ | augmented matrix (the system in matrix form) |
| $m_{ik} = a_{ik}/a_{kk}$ | elimination multiplier used to zero the $(i,k)$ entry |
| Pivot | the diagonal entry $a_{kk}$ used as the divisor |
| Partial pivoting | swapping rows so the largest available entry becomes the pivot |
| Back substitution | solving a triangular system from bottom to top |
| Row echelon form | upper-triangular form after forward elimination |
| $O(n^3)$ | cubic time complexity |
| $P$ | permutation matrix (row-swapping) |
| $PA = LU$ | factorisation incorporating pivoting |
| Rounding error | numerical error from finite-precision arithmetic |
