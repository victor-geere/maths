---
title: Spectral Theorem
tag: linear-algebra
summary: Real symmetric matrices are orthogonally diagonalisable with real eigenvalues.
links:
  - diagonalisation
  - eigenvalues
  - orthogonality
---

## Statement (Real Symmetric Case)

If $A \in M_n(\mathbb{R})$ is **symmetric** ($A = A^T$), then:

1. All eigenvalues of $A$ are **real**.
2. Eigenvectors for **distinct eigenvalues are orthogonal**.
3. $A$ is **orthogonally diagonalisable**: there exists orthogonal $Q$ and diagonal $D$ such that:

$$A = QDQ^T, \qquad Q^TQ = I$$

## Proof Sketch

The key step is showing $\mathbb{R}^n$ has an orthonormal basis of eigenvectors. Induct: find one eigenvector $\mathbf{q}_1$, then $A$ restricts to the orthogonal complement $\mathbf{q}_1^\perp$ (which is $A$-invariant by symmetry), and repeat.

## Complex Case (Spectral Theorem for Normal Matrices)

A complex matrix $A$ is **unitarily diagonalisable** iff it is **normal**: $AA^* = A^*A$.

Special cases: Hermitian ($A^*=A$), skew-Hermitian, unitary.

## Consequences

- **Positive-definite matrices:** $A = QDQ^T$ with all $\lambda_i > 0$.
- **Quadratic forms:** $\mathbf{x}^T A \mathbf{x} = \sum_i \lambda_i y_i^2$ in the eigenbasis.
- **Principal axes:** the eigenvectors of a quadratic form give its natural axes.

## Example

$$A = \begin{pmatrix}2&1\\1&2\end{pmatrix}, \quad \lambda_1 = 3,\; \lambda_2 = 1$$

Eigenvectors: $\mathbf{q}_1 = \tfrac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}$, $\mathbf{q}_2 = \tfrac{1}{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}$.

$$A = \begin{pmatrix}1/\sqrt{2}&1/\sqrt{2}\\1/\sqrt{2}&-1/\sqrt{2}\end{pmatrix}\begin{pmatrix}3&0\\0&1\end{pmatrix}\begin{pmatrix}1/\sqrt{2}&1/\sqrt{2}\\1/\sqrt{2}&-1/\sqrt{2}\end{pmatrix}$$

## Notes

- The spectral theorem is the foundation of principal component analysis (PCA).
- It generalises to compact self-adjoint operators on Hilbert spaces.
