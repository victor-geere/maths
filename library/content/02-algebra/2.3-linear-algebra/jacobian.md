---
title: Jacobian Matrix
tag: linear-algebra
summary: Matrix of all first-order partial derivatives; best linear approximation of a vector function.
links:
  - partial-derivatives
  - matrix-multiplication
  - chain-rule
---

## Key Formula

$$J_{ij} = \frac{\partial f_i}{\partial x_j}, \qquad J = \begin{pmatrix} \nabla f_1^\top \\ \vdots \\ \nabla f_m^\top \end{pmatrix}$$

## Notes

For $f: \mathbb{R}^n \to \mathbb{R}^m$, the Jacobian $J(\mathbf{x})$ is the $m \times n$ matrix of [[partial-derivatives|partial derivatives]].

### Best linear approximation

Near $\mathbf{x}_0$:

$$f(\mathbf{x}_0 + \mathbf{h}) \approx f(\mathbf{x}_0) + J(\mathbf{x}_0)\,\mathbf{h}$$

This is the multivariable analogue of the tangent line.

### Jacobian determinant

When $m = n$, $\det(J)$ measures the **local volume scaling factor** of the map $f$.

- $\det(J) > 0$: orientation preserved
- $\det(J) < 0$: orientation reversed
- $\det(J) = 0$: map is locally degenerate (not invertible near that point)

**Change of variables** in multiple integrals uses $|\det(J)|$:

$$\int_{\phi(U)} f(\mathbf{y})\,d\mathbf{y} = \int_U f(\phi(\mathbf{x}))\,|\det J_\phi(\mathbf{x})|\,d\mathbf{x}$$

Example: for polar coordinates $x = r\cos\theta$, $y = r\sin\theta$, the Jacobian determinant is $r$, giving the familiar $r\,dr\,d\theta$.

### Chain rule in matrix form

For $h = f \circ g$ where $g: \mathbb{R}^k \to \mathbb{R}^n$, $f: \mathbb{R}^n \to \mathbb{R}^m$:

$$J_h(\mathbf{x}) = J_f(g(\mathbf{x})) \cdot J_g(\mathbf{x})$$

a [[matrix-multiplication|matrix multiplication]].
