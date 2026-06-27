---
title: QR Decomposition
tag: linear-algebra
summary: Factoring a matrix into an orthogonal and upper triangular factor via Gram–Schmidt.
links:
  - gram-schmidt
  - orthogonality
  - lu-decomposition
---

## Statement

Every $A \in M_{m \times n}$ with $m \geq n$ can be written as:

$$A = QR$$

where:
- $Q \in M_{m \times n}$: columns are orthonormal
- $R \in M_{n \times n}$: upper triangular with positive diagonal entries

The decomposition is **unique** when $A$ has full column rank.

## Algorithm: Gram–Schmidt

Apply Gram–Schmidt orthogonalisation to the columns of $A$:

$$\mathbf{q}_1 = \frac{\mathbf{a}_1}{\|\mathbf{a}_1\|}, \quad \mathbf{q}_k = \frac{\mathbf{a}_k - \sum_{j<k} (\mathbf{a}_k \cdot \mathbf{q}_j)\mathbf{q}_j}{\|\cdots\|}$$

The entries $r_{jk} = \mathbf{q}_j \cdot \mathbf{a}_k$ fill the matrix $R$.

## Applications

| Application | Role of QR |
|---|---|
| Least squares | $A\mathbf{x} \approx \mathbf{b}$ → solve $R\mathbf{x} = Q^T\mathbf{b}$ |
| Eigenvalue algorithms | QR algorithm iterates $A \leftarrow RQ$ |
| Orthonormal bases | Columns of $Q$ form one |

## Householder vs Gram–Schmidt

- **Classical Gram–Schmidt** is intuitive but numerically unstable.
- **Householder reflections** give a more stable QR (standard in practice).

## Notes

- For square $Q$ (full QR), $Q$ is orthogonal: $Q^TQ = QQ^T = I$.
- QR is central to numerical linear algebra; the QR algorithm computes eigenvalues.
