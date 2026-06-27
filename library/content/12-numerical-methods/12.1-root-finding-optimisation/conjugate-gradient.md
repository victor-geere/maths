---
title: Conjugate Gradient Method
tag: numerical-methods
summary: An iterative method for solving large symmetric positive-definite linear systems, converging in at most n steps and dramatically outperforming gradient descent for ill-conditioned problems.
links:
  - gradient-descent
  - lu-decomposition
  - eigenvalues
  - big-o-notation
---

# Conjugate Gradient Method

The **Conjugate Gradient (CG) method** is the gold standard for solving large, sparse symmetric positive-definite (SPD) linear systems $A\mathbf{x} = \mathbf{b}$ when direct methods like LU factorisation are too expensive. It generates a sequence of search directions that are mutually **$A$-conjugate** (orthogonal with respect to the inner product defined by $A$), guaranteeing that each iteration makes progress in a new, unexplored direction. In exact arithmetic, CG converges in at most $n$ steps (the dimension of the space). In practice, for well-clustered eigenvalues or after preconditioning, it converges in far fewer iterations, making it indispensable in scientific computing, finite-element analysis, and machine learning.

## Problem Setup

Solve $A\mathbf{x} = \mathbf{b}$ where $A \in \mathbb{R}^{n\times n}$ is **symmetric positive definite (SPD)**.

Equivalent to minimising the quadratic:

$$f(\mathbf{x}) = \frac{1}{2}\mathbf{x}^T A\mathbf{x} - \mathbf{b}^T\mathbf{x}$$

($f$ has a unique minimum at $\mathbf{x}^* = A^{-1}\mathbf{b}$.)

## Algorithm

**Initialise:** $\mathbf{x}_0$, $\mathbf{r}_0 = \mathbf{b} - A\mathbf{x}_0$, $\mathbf{p}_0 = \mathbf{r}_0$

**Iterate** ($k = 0, 1, 2, \ldots$):

$$\alpha_k = \frac{\mathbf{r}_k^T \mathbf{r}_k}{\mathbf{p}_k^T A \mathbf{p}_k}$$

$$\mathbf{x}_{k+1} = \mathbf{x}_k + \alpha_k \mathbf{p}_k$$

$$\mathbf{r}_{k+1} = \mathbf{r}_k - \alpha_k A\mathbf{p}_k$$

$$\beta_k = \frac{\mathbf{r}_{k+1}^T \mathbf{r}_{k+1}}{\mathbf{r}_k^T \mathbf{r}_k}$$

$$\mathbf{p}_{k+1} = \mathbf{r}_{k+1} + \beta_k \mathbf{p}_k$$

Stop when $\|\mathbf{r}_k\|$ is small enough.

## Convergence

$$\frac{\|\mathbf{e}_k\|_A}{\|\mathbf{e}_0\|_A} \leq 2\left(\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}\right)^k$$

where $\kappa = \lambda_{\max}/\lambda_{\min}$ is the condition number of $A$.

**CG vs. Gradient Descent:** CG converges as fast as $\sqrt{\kappa}$-times faster because its conjugate directions do not repeat.

## Preconditioning

Solve $M^{-1}A\mathbf{x} = M^{-1}\mathbf{b}$ where $M \approx A$ is easy to invert. Reduces effective $\kappa$ dramatically.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $A$ | symmetric positive-definite matrix |
| $\mathbf{x}^* = A^{-1}\mathbf{b}$ | the exact solution |
| $\mathbf{r}_k = \mathbf{b} - A\mathbf{x}_k$ | residual at step $k$ |
| $\mathbf{p}_k$ | search direction at step $k$ |
| $\alpha_k$ | step size (exact line search along $\mathbf{p}_k$) |
| $\beta_k$ | parameter that makes new direction conjugate to all previous ones |
| $A$-conjugate | $\mathbf{p}_i^T A \mathbf{p}_j = 0$ for $i \neq j$ |
| $\|\mathbf{e}\|_A = \sqrt{\mathbf{e}^T A\mathbf{e}}$ | energy norm |
| $\kappa = \lambda_{\max}/\lambda_{\min}$ | condition number of $A$ |
| SPD | symmetric positive definite: $\mathbf{x}^T A\mathbf{x} > 0$ for $\mathbf{x} \neq \mathbf{0}$ |
| Preconditioner $M$ | a matrix approximating $A$ that is easy to invert |
