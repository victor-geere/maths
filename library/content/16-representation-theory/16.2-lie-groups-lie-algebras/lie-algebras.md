---
title: Lie Algebras
tag: representation-theory
summary: A Lie algebra is a vector space with an antisymmetric bilinear bracket satisfying the Jacobi identity; it captures the infinitesimal structure of a Lie group and classifies its representations.
links:
  - lie-groups
  - exponential-map
  - root-systems
  - representations-sl2
  - simple-lie-algebras
---

# Lie Algebras

A **Lie algebra** $\mathfrak{g}$ is a vector space over a field $k$ equipped with a bilinear bracket $[\cdot, \cdot]: \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$ that is antisymmetric and satisfies the Jacobi identity. Lie algebras arise naturally as the tangent space at the identity of a Lie group, linearising the group structure into something purely algebraic. The classification of simple Lie algebras over $\mathbb{C}$ — completed by Killing and Cartan — is one of the great achievements of 19th-century mathematics, and the resulting list (four infinite families $A_n, B_n, C_n, D_n$ plus five exceptionals) governs the representation theory of all compact simple Lie groups.

## Definition

A **Lie algebra** over $k$ is a $k$-vector space $\mathfrak{g}$ with a bracket $[\cdot,\cdot]: \mathfrak{g}\times\mathfrak{g} \to \mathfrak{g}$ satisfying:

1. **Antisymmetry**: $[X,Y] = -[Y,X]$
2. **Jacobi identity**: $[X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0$

for all $X, Y, Z \in \mathfrak{g}$.

## Examples

- $\mathfrak{gl}_n(k)$: $n\times n$ matrices with $[A,B] = AB - BA$
- $\mathfrak{sl}_n$: traceless matrices, $\dim = n^2-1$
- $\mathfrak{so}(n)$: skew-symmetric matrices, $[A,B] = AB-BA$
- $\mathfrak{su}(n)$: skew-Hermitian traceless matrices

## Key Structures

- **Subalgebra**: a subspace closed under the bracket.
- **Ideal**: a subspace $\mathfrak{h}$ with $[\mathfrak{g}, \mathfrak{h}] \subseteq \mathfrak{h}$.
- **Adjoint representation**: $\mathrm{ad}_X(Y) = [X,Y]$; gives $\mathrm{ad}: \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$.
- **Killing form**: $B(X,Y) = \mathrm{tr}(\mathrm{ad}_X \circ \mathrm{ad}_Y)$; non-degenerate iff $\mathfrak{g}$ is semisimple (**Cartan's criterion**).

## Representations

A **representation** of $\mathfrak{g}$ is a Lie algebra homomorphism $\phi: \mathfrak{g} \to \mathfrak{gl}(V)$, i.e., $\phi([X,Y]) = [\phi(X), \phi(Y)]$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $[X,Y]$ | Lie bracket |
| Antisymmetry | $[X,Y] = -[Y,X]$ |
| Jacobi identity | $[X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0$ |
| $\mathfrak{gl}_n, \mathfrak{sl}_n, \mathfrak{so}_n, \mathfrak{su}_n$ | classical matrix Lie algebras |
| Ideal $\mathfrak{h}$ | subspace with $[\mathfrak{g},\mathfrak{h}] \subseteq \mathfrak{h}$ |
| Adjoint rep $\mathrm{ad}_X$ | $Y \mapsto [X,Y]$; Lie algebra acting on itself |
| Killing form $B(X,Y)$ | $\mathrm{tr}(\mathrm{ad}_X \mathrm{ad}_Y)$; encodes semisimplicity |
| Semisimple Lie algebra | direct sum of simple algebras; Killing form non-degenerate |
| Simple Lie algebra | no non-trivial ideals |
| Lie algebra homomorphism | linear map preserving the bracket |
