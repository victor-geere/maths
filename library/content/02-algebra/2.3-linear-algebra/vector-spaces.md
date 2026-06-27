---
title: Vector Spaces
tag: linear-algebra
summary: Abstract spaces closed under vector addition and scalar multiplication.
links:
  - linear-independence
  - basis-dimension
  - dot-product-norms
---

## Definition

A **vector space** over a field $F$ is a set $V$ with:
- **Addition:** $\mathbf{u} + \mathbf{v} \in V$
- **Scalar multiplication:** $c\mathbf{v} \in V$ for $c \in F$

satisfying the eight axioms: commutativity and associativity of addition, identity ($\mathbf{0}$) and inverses ($-\mathbf{v}$), and the scalar multiplication rules.

## Standard Examples

| Space | Field | Dimension |
|---|---|---|
| $\mathbb{R}^n$ | $\mathbb{R}$ | $n$ |
| $M_{m \times n}(\mathbb{R})$ | $\mathbb{R}$ | $mn$ |
| $P_n$ (polynomials degree $\leq n$) | $\mathbb{R}$ | $n+1$ |
| $C([a,b])$ (continuous functions) | $\mathbb{R}$ | $\infty$ |

## Subspaces

$W \subseteq V$ is a **subspace** if it is closed under addition and scalar multiplication (and contains $\mathbf{0}$).

**Subspace criterion:** $W \neq \emptyset$, and $\mathbf{u}, \mathbf{v} \in W$, $c \in F \Rightarrow \mathbf{u} + c\mathbf{v} \in W$.

## Key Subspaces of a Matrix

For $A \in M_{m\times n}$:
- **Column space** $\text{col}(A) \subseteq \mathbb{R}^m$
- **Null space** $\text{null}(A) = \{\mathbf{x} : A\mathbf{x} = \mathbf{0}\} \subseteq \mathbb{R}^n$
- **Row space** $\subseteq \mathbb{R}^n$

**Rank-Nullity:** $\dim(\text{col}(A)) + \dim(\text{null}(A)) = n$.

## Notes

- Vector spaces provide the abstract setting for linear algebra.
- The axioms ensure linearity: any linear combination of elements stays in the space.
