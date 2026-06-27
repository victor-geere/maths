---
title: Gram–Schmidt Process
tag: linear-algebra
summary: Converting a linearly independent set into an orthonormal basis.
links:
  - orthogonality
  - dot-product-norms
  - qr-decomposition
---

## Algorithm

Given linearly independent vectors $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$, produce orthonormal $\{\mathbf{q}_1, \ldots, \mathbf{q}_k\}$ spanning the same subspace:

**Step 1:** $\mathbf{u}_1 = \mathbf{v}_1$, $\mathbf{q}_1 = \mathbf{u}_1 / \|\mathbf{u}_1\|$

**Step $j$** (for $j = 2, \ldots, k$):

$$\mathbf{u}_j = \mathbf{v}_j - \sum_{i=1}^{j-1} (\mathbf{v}_j \cdot \mathbf{q}_i)\,\mathbf{q}_i, \qquad \mathbf{q}_j = \frac{\mathbf{u}_j}{\|\mathbf{u}_j\|}$$

Each $\mathbf{u}_j$ subtracts the component of $\mathbf{v}_j$ in the already-constructed directions.

## Example

$\mathbf{v}_1 = \begin{pmatrix}1\\1\\0\end{pmatrix}$, $\mathbf{v}_2 = \begin{pmatrix}1\\0\\1\end{pmatrix}$:

$$\mathbf{q}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\\0\end{pmatrix}$$

$$\mathbf{u}_2 = \begin{pmatrix}1\\0\\1\end{pmatrix} - \frac{1}{2}\begin{pmatrix}1\\1\\0\end{pmatrix} = \begin{pmatrix}1/2\\-1/2\\1\end{pmatrix}$$

$$\mathbf{q}_2 = \frac{\mathbf{u}_2}{\|\mathbf{u}_2\|} = \frac{1}{\sqrt{6}}\begin{pmatrix}1\\-1\\2\end{pmatrix}$$

## Connection to QR

Gram–Schmidt on the columns of $A$ computes the QR decomposition $A = QR$:
- $Q$ has columns $\mathbf{q}_1, \ldots, \mathbf{q}_k$
- $R_{ij} = \mathbf{v}_j \cdot \mathbf{q}_i$ (for $i \leq j$)

## Notes

- Classical Gram–Schmidt can lose orthogonality numerically; **modified** Gram–Schmidt is more stable.
- Works in any inner product space, not just $\mathbb{R}^n$.
