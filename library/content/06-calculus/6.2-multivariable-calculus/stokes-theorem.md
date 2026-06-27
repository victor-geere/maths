---
title: Stokes' Theorem
tag: multivariable-calculus
summary: Relates the surface integral of the curl of a vector field to the line integral of the field around the surface's boundary.
links:
  - greens-theorem
  - divergence-theorem
  - grad-div-curl
---

# Stokes' Theorem

**Stokes' Theorem** is the three-dimensional generalisation of Green's Theorem. It relates the **surface integral** of the curl of a vector field over an oriented surface $S$ to the **line integral** of the field around the boundary curve $\partial S$. This powerful identity is the mathematical statement that the total rotation (curl) inside a surface equals the net circulation around its edge — a principle that is ubiquitous in electromagnetism (Faraday's law, Ampère's law) and fluid mechanics. Together with the Divergence Theorem and Green's Theorem, it is one of the three pillars of vector calculus and all three are unified by the **generalised Stokes' theorem** of differential geometry.

## Statement

Let $S$ be an oriented surface with boundary curve $\partial S$ (oriented by the right-hand rule). For a vector field $\mathbf{F}$ with continuous first partial derivatives on $S$:

$$\iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \oint_{\partial S} \mathbf{F} \cdot d\mathbf{r}$$

## Orientation Convention (Right-Hand Rule)

If the fingers of the right hand curl in the direction of traversal of $\partial S$, the thumb points in the direction of the surface normal $\mathbf{n}$.

## Special Case: Green's Theorem

When $S$ is a flat region $D$ in the $xy$-plane with $\mathbf{n} = \mathbf{k}$:

$$\iint_D (\nabla \times \mathbf{F}) \cdot \mathbf{k}\,dA = \oint_{\partial D} \mathbf{F} \cdot d\mathbf{r}$$

which is exactly Green's Theorem.

## Example

Evaluate $\oint_C \mathbf{F}\cdot d\mathbf{r}$ for $\mathbf{F} = (-y, x, z^2)$ and $C$ the circle $x^2+y^2=1$ in the plane $z=1$.

Take $S$ to be the disk $x^2+y^2\leq 1$, $z=1$, $\mathbf{n} = \mathbf{k}$:

$$\nabla\times\mathbf{F} = (0, 0, 2), \qquad \iint_S (0,0,2)\cdot(0,0,1)\,dA = 2\pi(1)^2 = 2\pi$$

## Application: Faraday's Law

$$\mathcal{E} = \oint_C \mathbf{E}\cdot d\mathbf{r} = -\frac{d}{dt}\iint_S \mathbf{B}\cdot d\mathbf{S}$$

Stokes' Theorem connects the EMF around a circuit to the rate of change of magnetic flux through it.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\iint_S (\nabla \times \mathbf{F})\cdot d\mathbf{S}$ | surface integral of the curl |
| $\oint_{\partial S} \mathbf{F}\cdot d\mathbf{r}$ | line integral of $\mathbf{F}$ around boundary $\partial S$ |
| $\nabla \times \mathbf{F}$ | curl of $\mathbf{F}$: measures rotation |
| $d\mathbf{S}$ | vector area element $\mathbf{n}\,dA$ |
| $d\mathbf{r}$ | vector line element along $\partial S$ |
| $\partial S$ | the boundary curve of surface $S$ |
| Right-hand rule | convention relating orientation of surface and boundary |
| Oriented surface | a surface with a consistently chosen normal direction |
| EMF | electromotive force — the circulation of the electric field |
| Magnetic flux | $\iint_S \mathbf{B}\cdot d\mathbf{S}$ — amount of magnetic field through $S$ |
| Faraday's law | $\mathcal{E} = -d\Phi_B/dt$; a physical application of Stokes' Theorem |
