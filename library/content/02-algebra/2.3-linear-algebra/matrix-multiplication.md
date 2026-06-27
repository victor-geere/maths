---
title: Matrix Multiplication
tag: linear-algebra
summary: Composition of linear maps; (AB)ᵢⱼ = Σₖ Aᵢₖ Bₖⱼ.
links:
  - determinant
  - eigenvalues
  - jacobian
  - linear-independence
---

## Key Formula

$$(AB)_{ij} = \sum_{k=1}^{n} A_{ik}\, B_{kj}$$

## Notes

If $A$ is $m \times n$ and $B$ is $n \times p$, then $AB$ is $m \times p$. The **inner dimensions must match**.

### Interpretation

If $A$ represents linear map $f$ and $B$ represents linear map $g$, then $AB$ represents $f \circ g$ — **apply $g$ first, then $f$**.

### Algebraic properties

| Property | Formula |
|---|---|
| Associativity | $(AB)C = A(BC)$ |
| Distributivity | $A(B+C) = AB + AC$ |
| Non-commutativity | $AB \neq BA$ in general |
| Identity | $AI = IA = A$ |
| Transpose | $(AB)^\top = B^\top A^\top$ |

### Block multiplication

For conformably partitioned matrices, blocks multiply as if they were scalars:

$$\begin{pmatrix} A & B \\ C & D \end{pmatrix}\begin{pmatrix} E \\ F \end{pmatrix} = \begin{pmatrix} AE + BF \\ CE + DF \end{pmatrix}$$

### Computational cost

Naïve multiplication of two $n \times n$ matrices costs $O(n^3)$ operations. The Strassen algorithm achieves $O(n^{2.807})$; the current asymptotic best is $\approx O(n^{2.371})$.

The [[determinant|determinant]] and [[eigenvalues|eigenvalues]] of a matrix are defined in terms of its action as a linear map.
