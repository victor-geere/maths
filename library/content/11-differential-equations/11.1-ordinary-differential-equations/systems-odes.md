---
title: Systems of ODEs & Phase Portraits
tag: ode
summary: Coupled first-order ODEs expressed in matrix form x' = Ax, solved via eigenvalues and eigenvectors, with behaviour visualised in the phase plane.
links:
  - constant-coeff-odes
  - eigenvalues
  - laplace-transform
---

# Systems of ODEs & Phase Portraits

A **system of ODEs** is a collection of coupled differential equations in which each unknown function's derivative depends on all the unknowns. Any higher-order ODE can be rewritten as a first-order system, making this the universal framework for differential equations. For **linear systems** $\mathbf{x}' = A\mathbf{x}$ with constant matrix $A$, the solutions are exponentials built from the eigenvalues and eigenvectors of $A$. The **phase portrait** — a picture of solution curves in the $(x_1, x_2)$-plane — reveals the qualitative behaviour: stable spirals, unstable nodes, saddle points, and centres, determined entirely by the eigenvalues of $A$.

## Matrix Form

A system of $n$ first-order ODEs:

$$\mathbf{x}' = A\mathbf{x} + \mathbf{b}(t), \quad \mathbf{x}(t) = \begin{pmatrix}x_1(t)\\\vdots\\x_n(t)\end{pmatrix}$$

For the homogeneous case $\mathbf{b} = \mathbf{0}$: $\mathbf{x}' = A\mathbf{x}$.

## Solution via Eigenvalues

If $A$ has eigenpairs $(\lambda_k, \mathbf{v}_k)$, then $e^{\lambda_k t}\mathbf{v}_k$ is a solution. General solution:

$$\mathbf{x}(t) = \sum_k C_k e^{\lambda_k t}\mathbf{v}_k$$

## Phase Portrait Classification (2D: eigenvalues $\lambda_{1,2}$)

| Eigenvalue type | Phase portrait |
|---|---|
| $\lambda_1 < \lambda_2 < 0$ | Stable node (all trajectories $\to \mathbf{0}$) |
| $0 < \lambda_1 < \lambda_2$ | Unstable node (all trajectories $\to \infty$) |
| $\lambda_1 < 0 < \lambda_2$ | Saddle point (unstable) |
| $\lambda = \alpha \pm \beta i$, $\alpha < 0$ | Stable spiral (inward) |
| $\lambda = \alpha \pm \beta i$, $\alpha > 0$ | Unstable spiral (outward) |
| $\lambda = \pm \beta i$ (pure imaginary) | Centre (closed ellipses) |

## Converting Higher-Order ODE to System

$y'' + by' + cy = 0$ becomes $\mathbf{x}' = A\mathbf{x}$ with $x_1 = y$, $x_2 = y'$:

$$A = \begin{pmatrix}0 & 1 \\ -c & -b\end{pmatrix}$$

## Fundamental Matrix

$\Phi(t)$ with columns = linearly independent solutions satisfies $\Phi' = A\Phi$, $\Phi(0) = I$.

General solution: $\mathbf{x}(t) = \Phi(t)\mathbf{c}$ for arbitrary constant vector $\mathbf{c}$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathbf{x}' = A\mathbf{x}$ | linear ODE system in matrix form |
| $A$ | coefficient matrix |
| $\lambda_k$ | eigenvalue of $A$ |
| $\mathbf{v}_k$ | eigenvector of $A$ corresponding to $\lambda_k$ |
| $e^{\lambda t}\mathbf{v}$ | a fundamental solution |
| Phase portrait | diagram of solution trajectories in the $(x_1, x_2)$-plane |
| Equilibrium | fixed point where $\mathbf{x}' = \mathbf{0}$: usually the origin |
| Stable node | eigenvalues real, negative; all trajectories approach origin |
| Saddle point | eigenvalues of opposite sign; most trajectories escape |
| Spiral | complex eigenvalues; trajectories spiral in or out |
| Centre | purely imaginary eigenvalues; closed orbit trajectories |
| $\Phi(t)$ | fundamental matrix: columns are independent solutions |
