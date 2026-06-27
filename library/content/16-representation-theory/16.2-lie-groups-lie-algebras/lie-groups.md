---
title: Lie Groups
tag: representation-theory
summary: A Lie group is a group that is also a smooth manifold, so that the group operations are smooth; they capture continuous symmetry and include examples like rotation groups and matrix groups.
links:
  - lie-algebras
  - exponential-map
  - smooth-manifolds
  - root-systems
  - haar-measure
---

# Lie Groups

A **Lie group** is simultaneously a group and a smooth manifold, with the requirement that multiplication and inversion are smooth maps. Lie groups are the mathematical objects encoding **continuous symmetry**: the group $SO(3)$ of rotations in 3D space, the unitary group $U(n)$ governing quantum mechanics, and the symmetry groups of differential equations are all Lie groups. The infinitesimal structure of a Lie group — the tangent space at the identity — forms a **Lie algebra**, and much of the representation theory of Lie groups can be understood at this linearised level. Lie groups are the foundation of modern physics, differential geometry, and the geometric Langlands programme.

## Definition

A **Lie group** is a group $G$ equipped with a smooth manifold structure such that:
- multiplication $G \times G \to G$, $(g,h) \mapsto gh$ is smooth;
- inversion $G \to G$, $g \mapsto g^{-1}$ is smooth.

## Matrix Lie Groups

The most common Lie groups are **matrix groups** — closed subgroups of $GL_n(\mathbb{R})$ or $GL_n(\mathbb{C})$:

| Group | Definition | Dimension |
|---|---|---|
| $GL_n(\mathbb{R})$ | invertible real $n\times n$ matrices | $n^2$ |
| $SL_n(\mathbb{R})$ | $\det = 1$ matrices | $n^2-1$ |
| $O(n)$ | $A^TA = I$ | $n(n-1)/2$ |
| $SO(n)$ | $A^TA=I$, $\det A=1$ | $n(n-1)/2$ |
| $U(n)$ | $A^*A = I$ (unitary) | $n^2$ |
| $SU(n)$ | unitary, $\det = 1$ | $n^2-1$ |
| $Sp_{2n}$ | symplectic | $n(2n+1)$ |

## Lie Algebra

The **Lie algebra** $\mathfrak{g} = T_eG$ is the tangent space at the identity, equipped with the **Lie bracket** $[X,Y]$ (the derivative of conjugation). The exponential map $\exp: \mathfrak{g} \to G$ connects the two.

## Representations

A **representation** of a Lie group $G$ is a smooth group homomorphism $\rho: G \to GL(V)$. For connected $G$, representations of $G$ are in bijection with representations of $\mathfrak{g}$ satisfying integrability conditions.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Lie group | group with compatible smooth manifold structure |
| $GL_n(k)$ | general linear group: invertible $n\times n$ matrices over $k$ |
| $SL_n$ | special linear group: $\det = 1$ |
| $O(n), SO(n)$ | orthogonal, special orthogonal groups |
| $U(n), SU(n)$ | unitary, special unitary groups |
| $Sp_{2n}$ | symplectic group |
| $\mathfrak{g} = T_eG$ | Lie algebra: tangent space at identity |
| Lie bracket $[X,Y]$ | antisymmetric bilinear map on $\mathfrak{g}$ encoding curvature |
| $\exp: \mathfrak{g} \to G$ | exponential map from algebra to group |
| Smooth homomorphism | group homomorphism that is also a smooth map |
