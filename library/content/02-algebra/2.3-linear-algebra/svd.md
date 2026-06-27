---
title: Singular Value Decomposition (SVD)
tag: linear-algebra
summary: Factoring any matrix into orthogonal and diagonal components, generalising diagonalisation.
links:
  - diagonalisation
  - eigenvalues
  - orthogonality
---

## Statement

Every real matrix $A \in M_{m \times n}$ can be written as:

$$A = U \Sigma V^T$$

where:
- $U \in M_{m \times m}$: orthogonal (columns are **left singular vectors**)
- $\Sigma \in M_{m \times n}$: diagonal with $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0$ (**singular values**), $r = \text{rank}(A)$
- $V \in M_{n \times n}$: orthogonal (columns are **right singular vectors**)

## Computing SVD

- Singular values: $\sigma_i = \sqrt{\lambda_i(A^T A)}$
- Columns of $V$: eigenvectors of $A^T A$
- Columns of $U$: eigenvectors of $AA^T$

## Applications

| Application | How SVD is used |
|---|---|
| Low-rank approximation | Keep top $k$ singular values/vectors |
| Pseudoinverse | $A^+ = V\Sigma^+ U^T$ |
| PCA | SVD of the data matrix |
| Least squares | Stable numerical solution |
| Image compression | Truncated SVD |

## Eckart–Young Theorem

The best rank-$k$ approximation to $A$ in Frobenius norm is:

$$A_k = \sum_{i=1}^k \sigma_i \mathbf{u}_i \mathbf{v}_i^T$$

## Notes

- SVD exists for every matrix (no square or invertibility requirements).
- Numerically, SVD is the most robust matrix decomposition.
- The condition number $\sigma_1/\sigma_r$ measures sensitivity of $A\mathbf{x}=\mathbf{b}$ to perturbations.
