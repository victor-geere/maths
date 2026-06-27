---
title: Condition Number & Stability
tag: numerical-methods
summary: The condition number measures how much a problem's solution amplifies input errors — a large condition number signals that small perturbations cause large changes in the output.
links:
  - gaussian-elimination
  - svd
  - eigenvalues
  - lu-decomposition
---

# Condition Number & Stability

The **condition number** $\kappa(A)$ of a matrix or problem quantifies its **sensitivity to perturbations**: by how much does a small relative change in the input get amplified in the output? For a well-conditioned problem ($\kappa$ close to 1), the computed answer is reliable even in floating-point arithmetic. For an ill-conditioned problem ($\kappa \gg 1$), tiny rounding errors in the data or arithmetic can produce wildly inaccurate results — the algorithm is not to blame; the problem itself is sensitive. Understanding condition numbers is essential for trusting (or distrusting) numerical results, and it is the bridge between the mathematics of linear algebra and the realities of finite-precision computation.

## Condition Number of a Matrix

For an invertible matrix $A \in \mathbb{R}^{n\times n}$:

$$\kappa(A) = \|A\|\,\|A^{-1}\|$$

**With the $\ell^2$ (spectral) norm:**

$$\kappa_2(A) = \frac{\sigma_{\max}(A)}{\sigma_{\min}(A)} = \frac{\lambda_{\max}(A^TA)^{1/2}}{\lambda_{\min}(A^TA)^{1/2}}$$

where $\sigma_{\max}, \sigma_{\min}$ are the largest and smallest singular values.

## Error Amplification for $A\mathbf{x} = \mathbf{b}$

If $\mathbf{b}$ is perturbed by $\delta\mathbf{b}$, the solution changes by $\delta\mathbf{x}$:

$$\frac{\|\delta\mathbf{x}\|}{\|\mathbf{x}\|} \leq \kappa(A)\,\frac{\|\delta\mathbf{b}\|}{\|\mathbf{b}\|}$$

Similarly for perturbations $\delta A$ in the matrix itself.

## Interpretation

If $\kappa(A) \approx 10^k$, then about $k$ significant digits are lost in the solution relative to the data precision. In IEEE double precision ($\approx 16$ decimal digits), a system with $\kappa \approx 10^{12}$ will have only about 4 reliable digits.

## Condition Number and Eigenvalues (Symmetric Case)

For symmetric $A$:

$$\kappa_2(A) = \frac{|\lambda_{\max}|}{|\lambda_{\min}|}$$

## Numerical Stability

An algorithm is **numerically stable** if it produces an output that is the exact solution to a nearby problem — small rounding errors are not amplified. Gaussian elimination with partial pivoting is numerically stable for most matrices encountered in practice.

## Singular Matrices

If $A$ is singular (non-invertible), $\kappa(A) = \infty$: the system may have no solution or infinitely many.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\kappa(A)$ | condition number of $A$: $\|A\|\|A^{-1}\|$ |
| $\kappa_2(A)$ | spectral condition number: $\sigma_{\max}/\sigma_{\min}$ |
| $\sigma_{\max}, \sigma_{\min}$ | largest and smallest singular values of $A$ |
| $\|A\|$ | matrix norm (operator norm) |
| Well-conditioned | $\kappa \approx 1$; small input errors remain small in output |
| Ill-conditioned | $\kappa \gg 1$; small input errors may cause large output errors |
| $\delta\mathbf{b}$ | perturbation (error) in the right-hand side $\mathbf{b}$ |
| $\delta\mathbf{x}$ | resulting perturbation in the solution $\mathbf{x}$ |
| Numerical stability | algorithm does not amplify rounding errors |
| Floating-point precision | IEEE double: $\approx 2^{-52} \approx 2.2 \times 10^{-16}$ relative error |
| Singular matrix | $A^{-1}$ does not exist; $\kappa = \infty$ |
