---
title: Numerical Eigenvalue Methods (QR Algorithm)
tag: numerical-methods
summary: The QR algorithm iteratively applies QR decompositions to converge a matrix to (quasi-)triangular form, revealing its eigenvalues on the diagonal.
links:
  - eigenvalues
  - qr-decomposition
  - condition-number
  - svd
---

# Numerical Eigenvalue Methods (QR Algorithm)

Computing the eigenvalues of a general matrix is a fundamentally iterative problem — no finite algorithm can extract them exactly from characteristic polynomials once $n \geq 5$ (by Abel–Ruffini). The **QR algorithm**, developed by Francis and Kublanovskaya in 1961, is the practical answer: it iteratively factorises the matrix as $A = QR$ and multiplies in reverse order $A \leftarrow RQ$, gradually driving the matrix toward upper-triangular (Schur) form. The diagonal entries of the resulting triangular matrix are the eigenvalues. Shifts and deflation make the modern QR algorithm converge cubically in practice. It is ranked among the top ten algorithms of the 20th century and underlies the `eig` function in every numerical computing library.

## Basic QR Iteration

**Initialise:** $A_0 = A$

**Iterate** ($k = 0, 1, 2, \ldots$):

1. Compute $A_k = Q_k R_k$ (QR factorisation)
2. Set $A_{k+1} = R_k Q_k$

**Key property:** $A_{k+1} = Q_k^T A_k Q_k$ (orthogonal similarity), so all $A_k$ share the same eigenvalues.

**Convergence:** $A_k$ converges to upper-triangular (Schur) form when eigenvalues have distinct moduli:

$$A_k \to \begin{pmatrix}\lambda_1 & * & \cdots \\ 0 & \lambda_2 & \cdots \\ \vdots & & \ddots\end{pmatrix}$$

## Shifts (Accelerating Convergence)

Replace $A_k - \sigma_k I = Q_k R_k$ (where $\sigma_k$ is a shift chosen to accelerate convergence), then $A_{k+1} = R_k Q_k + \sigma_k I$.

**Wilkinson shift:** $\sigma_k = $ eigenvalue of the bottom-right $2\times 2$ block closest to $a_{nn}$. Gives **cubic convergence**.

## Practical Workflow

For large matrices:
1. **Reduce to Hessenberg form** ($O(n^3)$): apply Householder reflections; much cheaper for the QR iteration
2. **Apply QR iteration** to the Hessenberg matrix ($O(n^2)$ per step)

## Other Eigenvalue Methods

| Method | Best for |
|---|---|
| Power iteration | Largest eigenvalue |
| Inverse iteration | Eigenvalue nearest a target $\sigma$ |
| Lanczos / Arnoldi | Large sparse matrices |
| Divide-and-conquer | Symmetric tridiagonal; used in SVD |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $A_k = Q_k R_k$ | QR factorisation at step $k$ |
| $A_{k+1} = R_k Q_k$ | reversed product; same eigenvalues |
| $Q_k$ | orthogonal matrix from QR factorisation |
| $R_k$ | upper-triangular matrix from QR factorisation |
| Schur form | upper-triangular matrix similar to $A$; diagonal = eigenvalues |
| Shift $\sigma_k$ | scalar subtracted to accelerate convergence |
| Wilkinson shift | shift based on bottom-right $2\times2$ submatrix |
| Hessenberg form | almost-upper-triangular (non-zero only one subdiagonal); reduces QR cost |
| Deflation | splitting off a smaller subproblem once an eigenvalue converges |
| Cubic convergence | with Wilkinson shifts; each step cubes the error |
| Power iteration | $\mathbf{v}_{k+1} = A\mathbf{v}_k/\|A\mathbf{v}_k\|$; finds dominant eigenvector |
