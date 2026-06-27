---
title: Diagonalisation
tag: linear-algebra
summary: Writing a matrix as PDP⁻¹ where D is diagonal, when eigenvectors form a basis.
links:
  - eigenvalues
  - linear-independence
  - spectral-theorem
---

## Definition

A square matrix $A$ is **diagonalisable** if there exists an invertible $P$ and diagonal $D$ such that:

$$A = PDP^{-1} \iff AP = PD$$

The columns of $P$ are eigenvectors of $A$; the diagonal entries of $D$ are the corresponding eigenvalues.

## Diagonalisability Criterion

$A \in M_n$ is diagonalisable iff it has $n$ **linearly independent eigenvectors** (i.e. eigenvectors form a basis of $\mathbb{R}^n$).

**Sufficient condition:** $n$ distinct eigenvalues.

## Powers via Diagonalisation

$$A^k = PD^kP^{-1}, \qquad D^k = \text{diag}(\lambda_1^k, \ldots, \lambda_n^k)$$

This makes computing matrix powers and exponentials efficient.

## Example

$$A = \begin{pmatrix}3&1\\0&2\end{pmatrix}, \quad \lambda_1=3, \lambda_2=2$$

Eigenvectors: $\mathbf{v}_1 = \begin{pmatrix}1\\0\end{pmatrix}$, $\mathbf{v}_2 = \begin{pmatrix}-1\\1\end{pmatrix}$.

$$P = \begin{pmatrix}1&-1\\0&1\end{pmatrix}, \quad D = \begin{pmatrix}3&0\\0&2\end{pmatrix}$$

## Not Every Matrix is Diagonalisable

The matrix $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ (only eigenvalue $0$, geometric multiplicity 1 < algebraic multiplicity 2) is not diagonalisable — only **Jordan normal form** applies.

## Notes

- Real symmetric matrices are always diagonalisable (Spectral Theorem) with orthogonal $P$.
