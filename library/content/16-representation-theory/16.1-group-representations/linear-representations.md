---
title: Linear Representations
tag: representation-theory
summary: A linear representation of a group is a homomorphism into the invertible linear transformations of a vector space, making abstract symmetry concrete and computable.
links:
  - group-axioms
  - group-homomorphisms
  - vector-spaces
  - characters
  - matrix-multiplication
---

# Linear Representations

A **linear representation** of a group $G$ is a way of realising the abstract symmetry encoded by $G$ as explicit linear transformations of a vector space. Concretely, it is a group homomorphism $\rho: G \to GL(V)$, where $V$ is a vector space over a field $k$ and $GL(V)$ is the group of invertible linear maps $V \to V$. Representation theory allows us to study abstract groups by examining how they act linearly on vector spaces, and it has profound applications in physics, number theory, and combinatorics. The key insight is that even when a group is defined abstractly, its representations can be classified using the powerful tools of linear algebra.

## Definition

A **representation** of $G$ on a finite-dimensional $k$-vector space $V$ is a group homomorphism:

$$\rho: G \to GL(V)$$

satisfying $\rho(gh) = \rho(g)\rho(h)$ and $\rho(e) = \mathrm{id}_V$ for all $g, h \in G$. The **degree** of $\rho$ is $\dim_k V$.

## Irreducibility & Maschke's Theorem

A $G$-invariant subspace $W \subseteq V$ satisfies $\rho(g)W \subseteq W$ for all $g$. A representation is **irreducible** if its only $G$-invariant subspaces are $\{0\}$ and $V$.

**Maschke's Theorem**: If $G$ is finite and $\mathrm{char}(k) \nmid |G|$, every representation decomposes uniquely as a direct sum of irreducibles:
$$V \cong V_1^{\oplus m_1} \oplus \cdots \oplus V_r^{\oplus m_r}$$

## Equivalence

Representations $\rho$ on $V$ and $\sigma$ on $W$ are **equivalent** if there exists an invertible intertwiner $T: V \to W$ with $T\rho(g) = \sigma(g)T$ for all $g \in G$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $GL(V)$ | group of invertible linear maps $V \to V$ |
| $\rho: G \to GL(V)$ | linear representation |
| $\dim_k V$ | dimension of $V$ over field $k$ |
| Irreducible representation | no proper non-zero $G$-invariant subspace |
| $G$-invariant subspace | subspace $W$ with $\rho(g)W \subseteq W$ for all $g$ |
| Maschke's Theorem | finite-group reps decompose into irreducibles when char $\nmid |G|$ |
| $\oplus$ | direct sum of representations |
| Multiplicity $m_i$ | number of times irreducible $V_i$ appears |
| Intertwiner | linear map $T$ with $T\rho(g) = \sigma(g)T$ |
| $k[G]$ | group algebra: formal $k$-linear combinations of group elements |
