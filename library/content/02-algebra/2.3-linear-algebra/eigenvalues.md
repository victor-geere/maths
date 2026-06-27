---
title: Eigenvalues & Eigenvectors
tag: linear-algebra
summary: Av = λv — directions preserved (only scaled) by a linear map.
links:
  - determinant
  - matrix-multiplication
  - linear-independence
---

## Key Formula

$$A\mathbf{v} = \lambda\mathbf{v} \iff \det(A - \lambda I) = 0$$

## Notes

An **eigenvector** $\mathbf{v} \neq \mathbf{0}$ is a direction that $A$ only stretches or shrinks — by the **eigenvalue** $\lambda$ (which can be negative, zero, or complex).

### Finding eigenvalues

1. Form the **characteristic polynomial** $p(\lambda) = \det(A - \lambda I)$
2. Solve $p(\lambda) = 0$ — roots are the eigenvalues
3. For each $\lambda$, solve $(A - \lambda I)\mathbf{v} = \mathbf{0}$ for eigenvectors

For a $2\times 2$ matrix: $p(\lambda) = \lambda^2 - \text{tr}(A)\,\lambda + \det(A)$.

### Key facts

$$\prod_i \lambda_i = \det(A), \qquad \sum_i \lambda_i = \text{tr}(A)$$

### Diagonalisation

If $A$ has $n$ [[linear-independence|linearly independent]] eigenvectors $\mathbf{v}_1,\ldots,\mathbf{v}_n$ with eigenvalues $\lambda_1,\ldots,\lambda_n$:

$$A = PDP^{-1}, \qquad D = \text{diag}(\lambda_1,\ldots,\lambda_n), \qquad P = [\mathbf{v}_1 \cdots \mathbf{v}_n]$$

Powers become easy: $A^k = PD^kP^{-1}$.

### Spectral theorem

A real **symmetric** matrix ($A = A^\top$) has:
- All real eigenvalues
- Orthonormal eigenvectors → $A = QDQ^\top$ (orthogonal diagonalisation)

### Applications

- PCA: eigenvectors of the covariance matrix are principal components
- PageRank: dominant eigenvector of the link matrix
- Stability: eigenvalues of Jacobian determine stability of equilibria
- Vibrations: eigenvalues give natural frequencies
