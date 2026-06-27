---
title: Method of Separation of Variables
tag: pde
summary: Reducing a PDE to a system of ODEs by assuming the solution is a product of functions each depending on only one variable, then superimposing eigensolutions.
links:
  - heat-equation
  - wave-equation
  - laplace-poisson
  - fourier-series
---

# Method of Separation of Variables

**Separation of variables** is the most widely used technique for solving linear PDEs on bounded domains with simple geometry. The key assumption is that the solution can be written as a product $u(x,t) = X(x)T(t)$ (or a product over all variables), so that substituting into the PDE separates it into two (or more) independent ODEs connected only by a shared **separation constant** $\lambda$. The boundary conditions determine the allowed values of $\lambda$ — the **eigenvalues** — and the corresponding solutions $X_n(x)$ form an **orthogonal basis**. The general solution is then the **superposition** (Fourier series) of all these eigensolutions, with coefficients determined by the initial condition.

## General Approach

For a linear homogeneous PDE $\mathcal{L}[u] = 0$ on a rectangular domain with homogeneous boundary conditions:

1. **Assume** $u = X(x)T(t)$ (or appropriate product form)
2. **Substitute** into the PDE and divide to separate variables:
   $$\frac{T'(t)}{T(t)} = \frac{X''(x)}{X(x)} = -\lambda$$
3. **Solve the spatial ODE** $X'' + \lambda X = 0$ with boundary conditions → eigenvalues $\lambda_n$ and eigenfunctions $X_n(x)$
4. **Solve the temporal ODE** for each $\lambda_n$ → $T_n(t)$
5. **Superimpose** (Fourier expansion): $u(x,t) = \sum_n c_n X_n(x) T_n(t)$
6. **Apply initial condition** to find coefficients $c_n$

## Common Eigenvalue Problems

**Dirichlet (zero endpoints):** $X''+\lambda X = 0$, $X(0)=X(L)=0$:

$$\lambda_n = (n\pi/L)^2, \quad X_n = \sin(n\pi x/L), \quad n=1,2,3,\ldots$$

**Neumann (zero derivatives):** $X''+\lambda X = 0$, $X'(0)=X'(L)=0$:

$$\lambda_n = (n\pi/L)^2, \quad X_n = \cos(n\pi x/L), \quad n=0,1,2,\ldots$$

**Periodic:** eigenfunctions $\sin(n\pi x/L)$ and $\cos(n\pi x/L)$ together.

## Fourier Coefficients

For Dirichlet boundary conditions, $c_n$ are the Fourier sine coefficients:

$$c_n = \frac{2}{L}\int_0^L f(x)\sin\!\left(\frac{n\pi x}{L}\right)dx$$

## Limitations

- Requires **linear**, **homogeneous** equation and boundary conditions
- Applies most directly to rectangular, cylindrical, or spherical domains
- Non-homogeneous boundary conditions: first reduce to homogeneous by subtracting a steady-state solution

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $u = X(x)T(t)$ | separation of variables ansatz |
| $-\lambda$ | separation constant |
| $\lambda_n$ | eigenvalue: $(n\pi/L)^2$ for Dirichlet BC |
| $X_n(x)$ | eigenfunction corresponding to $\lambda_n$ |
| $T_n(t)$ | time factor for eigenvalue $\lambda_n$ |
| Superposition | $u = \sum_n c_n X_n T_n$: general solution as sum of eigensolutions |
| Fourier coefficients $c_n$ | weights determined by initial/boundary data |
| Dirichlet BC | $u = 0$ at both endpoints |
| Neumann BC | $\partial u/\partial n = 0$ at boundary (zero-flux) |
| Sturm–Liouville problem | eigenvalue problem generating orthogonal eigenfunctions |
| Orthogonal eigenfunctions | $\int_0^L X_m X_n\,dx = 0$ for $m \neq n$ |
