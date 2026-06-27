---
title: Determinant
tag: linear-algebra
summary: Signed volume scaling factor of a linear map; det(AB) = det(A)det(B).
links:
  - matrix-multiplication
  - eigenvalues
  - linear-independence
---

## Key Formula

$$\det(A) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^{n} A_{i,\sigma(i)}$$

## Notes

The determinant measures **how much a linear map scales $n$-dimensional volume**, with sign indicating whether orientation is preserved.

### Small cases

**$2 \times 2$:**

$$\det\begin{pmatrix}a & b \\ c & d\end{pmatrix} = ad - bc$$

**$3 \times 3$** (cofactor expansion along row 1):

$$\det(A) = a_{11}(a_{22}a_{33}-a_{23}a_{32}) - a_{12}(a_{21}a_{33}-a_{23}a_{31}) + a_{13}(a_{21}a_{32}-a_{22}a_{31})$$

### Key properties

$$\det(AB) = \det(A)\det(B), \quad \det(A^\top) = \det(A), \quad \det(A^{-1}) = \frac{1}{\det(A)}$$

- $\det(I) = 1$
- Swapping two rows negates the determinant
- Multiplying a row by $\lambda$ multiplies $\det$ by $\lambda$
- Adding a multiple of one row to another: no change

### Invertibility criterion

$$A \text{ is invertible} \iff \det(A) \neq 0$$

When $\det(A) = 0$ the columns (rows) are [[linear-independence|linearly dependent]] — the map squashes volume to zero.

### Geometric meaning

In $\mathbb{R}^2$: $|\det(A)|$ is the area of the parallelogram spanned by the columns of $A$.  
In $\mathbb{R}^3$: $|\det(A)|$ is the volume of the parallelepiped.

The [[eigenvalues|eigenvalue]] product $\prod \lambda_i = \det(A)$.
