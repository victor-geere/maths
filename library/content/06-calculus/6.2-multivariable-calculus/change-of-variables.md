---
title: Change of Variables (Jacobian)
tag: multivariable-calculus
summary: Transforming a multiple integral to a new coordinate system using the Jacobian determinant as a scaling factor.
links:
  - double-integrals
  - triple-integrals
  - jacobian
---

# Change of Variables (Jacobian)

When computing a double or triple integral, the region of integration or the integrand may be awkwardly shaped in Cartesian coordinates but simple in another coordinate system. The **change of variables** formula handles this exactly as $u$-substitution does in one dimension, but now the role of $|du/dx|$ is played by the **Jacobian determinant** $|J|$ — a generalisation that measures how area (or volume) is scaled by the coordinate transformation. The formula is fundamental to polar, cylindrical, spherical coordinate integrals and to any custom transformation that straightens a complicated region.

## Two-Variable Formula

Let $(x, y) = \mathbf{T}(u, v)$ be a differentiable transformation. The **Jacobian** of the transformation is:

$$J = \frac{\partial(x, y)}{\partial(u, v)} = \begin{vmatrix}\dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v}\\[6pt]\dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v}\end{vmatrix} = \frac{\partial x}{\partial u}\frac{\partial y}{\partial v} - \frac{\partial x}{\partial v}\frac{\partial y}{\partial u}$$

Then:

$$\iint_R f(x,y)\,dA = \iint_S f(x(u,v),y(u,v))\,|J|\,du\,dv$$

where $S$ is the pre-image of $R$ under $\mathbf{T}$.

## Three-Variable Formula

For $(x,y,z) = \mathbf{T}(u,v,w)$:

$$\iiint_E f\,dV = \iiint_{E'} f(\mathbf{T}(u,v,w))\,|J|\,du\,dv\,dw, \quad J = \frac{\partial(x,y,z)}{\partial(u,v,w)}$$

## Standard Jacobians

| Transformation | Jacobian $|J|$ |
|---|---|
| Polar: $x=r\cos\theta$, $y=r\sin\theta$ | $r$ |
| Cylindrical: add $z=z$ | $r$ |
| Spherical: $x=\rho\sin\phi\cos\theta$, … | $\rho^2\sin\phi$ |

## Example

Evaluate $\iint_R e^{(x+y)/(x-y)}\,dA$ over the square $R$ with vertices $(0,0),(1,0),(1/2,1/2),(0,1)$ by the substitution $u = x+y$, $v = x-y$:

$$J = \begin{vmatrix}\tfrac{1}{2}&\tfrac{1}{2}\\\tfrac{1}{2}&-\tfrac{1}{2}\end{vmatrix} = -\tfrac{1}{2}, \quad |J| = \tfrac{1}{2}$$

Region in $uv$: $0 \leq u \leq 1$, $0 \leq v \leq 1$ (after working out bounds):

$$\iint e^{u/v}\cdot\tfrac{1}{2}\,du\,dv \quad \text{(now separable)}$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $J$ | Jacobian determinant of the transformation |
| $\dfrac{\partial(x,y)}{\partial(u,v)}$ | the Jacobian matrix of partial derivatives |
| $|J|$ | absolute value of the Jacobian (always non-negative) |
| Transformation $\mathbf{T}$ | the map $(u,v) \mapsto (x,y)$ |
| Pre-image $S$ | the region in $(u,v)$ space that maps to $R$ in $(x,y)$ space |
| $dA$ | area element, replaced by $|J|\,du\,dv$ |
| $dV$ | volume element, replaced by $|J|\,du\,dv\,dw$ |
| Determinant | a scalar computed from a square matrix; here measures area/volume scaling |
| Polar coordinates | $x = r\cos\theta$, $y = r\sin\theta$; Jacobian $= r$ |
| Spherical coordinates | Jacobian $= \rho^2\sin\phi$ |
| Invertible transformation | one-to-one near every point, so the change of variables is valid |
