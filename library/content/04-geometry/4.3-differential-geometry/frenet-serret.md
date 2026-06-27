---
title: Frenet–Serret Formulas
tag: differential-geometry
summary: The equations governing how the natural frame (T, N, B) rotates as it moves along a space curve.
links:
  - curvature
  - arc-length
  - gaussian-curvature
---

# Frenet–Serret Formulas

As a particle moves along a smooth curve in 3D space, it carries with it a natural **moving frame** of three mutually perpendicular unit vectors: the tangent $\mathbf{T}$, the principal normal $\mathbf{N}$, and the binormal $\mathbf{B}$. The **Frenet–Serret formulas** describe exactly how this frame rotates with arc length — and the rate of rotation is captured by just two numbers at each point: the **curvature** $\kappa$ (how fast the curve bends) and the **torsion** $\tau$ (how fast the curve twists out of its instantaneous plane). Together, $\kappa(s)$ and $\tau(s)$ completely characterise a curve in 3D up to rigid motion.

## The Frenet–Serret Frame

Given a unit-speed curve $\mathbf{r}(s)$:

- **Unit tangent:** $\mathbf{T} = \mathbf{r}'(s)$
- **Principal normal:** $\mathbf{N} = \dfrac{\mathbf{T}'(s)}{|\mathbf{T}'(s)|}$
- **Binormal:** $\mathbf{B} = \mathbf{T} \times \mathbf{N}$

## The Formulas

$$\frac{d\mathbf{T}}{ds} = \kappa\, \mathbf{N}$$

$$\frac{d\mathbf{N}}{ds} = -\kappa\, \mathbf{T} + \tau\, \mathbf{B}$$

$$\frac{d\mathbf{B}}{ds} = -\tau\, \mathbf{N}$$

In matrix form:

$$\frac{d}{ds}\begin{pmatrix}\mathbf{T}\\\mathbf{N}\\\mathbf{B}\end{pmatrix} = \begin{pmatrix}0 & \kappa & 0 \\ -\kappa & 0 & \tau \\ 0 & -\tau & 0\end{pmatrix}\begin{pmatrix}\mathbf{T}\\\mathbf{N}\\\mathbf{B}\end{pmatrix}$$

## Curvature and Torsion

- **Curvature** $\kappa \geq 0$: measures bending; $\kappa = 0$ for a straight line.
- **Torsion** $\tau \in \mathbb{R}$: measures twisting; $\tau = 0$ for a plane curve.

For a general parametric space curve $\mathbf{r}(t)$:

$$\kappa = \frac{\|\mathbf{r}' \times \mathbf{r}''\|}{\|\mathbf{r}'\|^3}, \qquad \tau = \frac{(\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}'''}{\|\mathbf{r}' \times \mathbf{r}''\|^2}$$

## Fundamental Theorem of Space Curves

Given smooth functions $\kappa(s) > 0$ and $\tau(s)$, there exists a unique (up to rigid motion) unit-speed curve in $\mathbb{R}^3$ with those curvature and torsion functions. This is the **fundamental theorem of space curves**.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $s$ | arc length parameter |
| $\mathbf{T}$ | unit tangent vector ($\mathbf{r}'(s)$) |
| $\mathbf{N}$ | principal normal unit vector (direction of bending) |
| $\mathbf{B}$ | binormal unit vector ($\mathbf{T} \times \mathbf{N}$) |
| $\kappa$ (kappa) | curvature — rate of change of $\mathbf{T}$ |
| $\tau$ (tau) | torsion — rate of twisting out of the osculating plane |
| Moving frame | the orthonormal frame $(\mathbf{T}, \mathbf{N}, \mathbf{B})$ attached to the curve |
| Osculating plane | the plane spanned by $\mathbf{T}$ and $\mathbf{N}$ at a point |
| Osculating circle | circle in the osculating plane with radius $1/\kappa$ |
| Unit-speed curve | curve parametrised so $\|\mathbf{r}'(s)\|=1$ |
| $\times$ | cross product of two vectors |
| $\cdot$ | dot product of two vectors |
| Rigid motion | a distance-preserving transformation (rotation + translation) |
