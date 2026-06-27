---
title: Tropical Geometry
tag: algebraic-geometry
summary: A combinatorial shadow of algebraic geometry obtained by replacing the field operations with (min, +) — turning algebraic varieties into piecewise-linear polyhedral complexes.
links:
  - affine-varieties
  - projective-varieties
  - dimension-degree
---

# Tropical Geometry

**Tropical geometry** is a piecewise-linear "shadow" of algebraic geometry that replaces the usual arithmetic $(+, \times)$ with the **tropical semiring** $(\min, +)$. In tropical mathematics, addition is replaced by minimum and multiplication by addition: $a \oplus b = \min(a,b)$ and $a \odot b = a + b$. Every polynomial becomes a piecewise-linear function, and every algebraic variety becomes a **tropical variety** — a polyhedral complex (union of polyhedra). This "degenerating" of geometry to combinatorics preserves deep information: tropical varieties retain intersection-theoretic data (tropical Bézout theorem), count curves and cycles (Mikhalkin's theorem), and connect algebraic geometry to convex geometry, combinatorics, and optimisation. The field, named by Imre Simon and developed into a discipline by Mikhalkin, Speyer, Sturmfels, and others, has had striking applications to enumerative geometry.

## The Tropical Semiring

$$\mathbb{T} = \mathbb{R} \cup \{\infty\}$$

- **Tropical addition:** $a \oplus b = \min(a,b)$ (identity element: $\infty$)
- **Tropical multiplication:** $a \odot b = a + b$ (identity element: $0$)

Note: there are no tropical subtraction or division — $\mathbb{T}$ is a **semiring**, not a ring.

## Tropicalisation

For a polynomial $f = \sum c_\alpha x^\alpha \in K[x_1^{\pm1},\ldots,x_n^{\pm1}]$ (with $K = \mathbb{C}((t))$ or similar), the **tropicalisation** is:

$$\text{trop}(f) = \min_\alpha (\nu(c_\alpha) + \alpha \cdot w)$$

a piecewise-linear function (the **tropical polynomial**).

The **tropical variety** of $f$ is:

$$T(f) = \{w \in \mathbb{R}^n : \text{the minimum in trop}(f) \text{ is achieved at least twice}\}$$

It is the **corner locus** of the tropical polynomial.

## Fundamental Theorem of Tropical Geometry

For a variety $V = V(f_1,\ldots,f_r) \subseteq (K^*)^n$:

$$\text{Trop}(V) = \overline{\{(\nu(x_1),\ldots,\nu(x_n)) : (x_1,\ldots,x_n) \in V(K^*)\}}$$

The tropicalisation is the closure of the image of $V$ under the valuation map.

## Tropical Lines and Curves

A **tropical line** in $\mathbb{R}^2$ is a "Y"-shape with three rays. Two tropical lines meet in exactly 1 point (tropical Bézout). A genus-$g$ tropical curve is a graph with first Betti number $g$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathbb{T}$ | tropical semiring $\mathbb{R} \cup \{\infty\}$ |
| $a \oplus b = \min(a,b)$ | tropical addition |
| $a \odot b = a + b$ | tropical multiplication |
| Tropical polynomial | piecewise-linear function from a classical polynomial via tropicalisation |
| Tropical variety | corner locus of a tropical polynomial; a polyhedral complex |
| $\text{Trop}(V)$ | the tropical variety associated to algebraic variety $V$ |
| Valuation $\nu$ | a map $K^* \to \mathbb{R}$ measuring "order of vanishing" |
| $K = \mathbb{C}((t))$ | Puiseux/Laurent series field; the main field for tropicalisation |
| Corner locus | the subset where the minimum of the tropical polynomial is achieved $\geq 2$ times |
| Polyhedral complex | a union of convex polytopes glued along faces |
| First Betti number | $b_1 = \#\text{edges} - \#\text{vertices} + 1$ for a graph; equals the genus |
