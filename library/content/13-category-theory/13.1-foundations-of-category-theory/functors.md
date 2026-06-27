---
title: Functors
tag: category-theory
summary: Structure-preserving maps between categories — they send objects to objects and morphisms to morphisms, respecting composition and identities.
links:
  - categories-morphisms
  - natural-transformations
  - adjoint-functors
---

# Functors

A **functor** is a structure-preserving map between categories: it sends each object of one category to an object in another, and each morphism to a morphism, in a way that preserves composition and identity. Functors are the morphisms of the category **Cat** of all categories — so category theory is itself a category. More importantly, functors encode mathematical relationships: the fundamental group $\pi_1$ is a functor from **Top** to **Grp**; homology groups $H_n$ are functors; the forgetful functor from **Grp** to **Set** strips away group structure. Understanding a mathematical construction as a functor immediately tells you how it behaves under maps, provides naturality conditions, and enables the machinery of adjunctions and the Yoneda lemma.

## Definition

A **functor** $F : \mathcal{C} \to \mathcal{D}$ consists of:

- For each object $A \in \mathcal{C}$: an object $F(A) \in \mathcal{D}$
- For each morphism $f : A \to B$ in $\mathcal{C}$: a morphism $F(f) : F(A) \to F(B)$ in $\mathcal{D}$

satisfying:

1. **Preservation of identity:** $F(\text{id}_A) = \text{id}_{F(A)}$
2. **Preservation of composition:** $F(g \circ f) = F(g) \circ F(f)$

This is a **covariant functor**. A **contravariant functor** reverses arrows: $F(f) : F(B) \to F(A)$.

## Examples

| Functor | $\mathcal{C}$ | $\mathcal{D}$ | Action |
|---|---|---|---|
| Fundamental group $\pi_1$ | **Top$_*$** | **Grp** | $(X, x_0) \mapsto \pi_1(X, x_0)$ |
| Singular homology $H_n$ | **Top** | **Ab** | $X \mapsto H_n(X)$ |
| Forgetful $U$ | **Grp** | **Set** | $(G, \cdot) \mapsto G$ |
| Free group $F$ | **Set** | **Grp** | $S \mapsto F(S)$ |
| Hom functor $\text{Hom}(A, -)$ | $\mathcal{C}$ | **Set** | $B \mapsto \text{Hom}(A,B)$ |
| Dualization $(-)^*$ | **Vect$_k$** | **Vect$_k$** | $V \mapsto V^* = \text{Hom}(V,k)$ |

## Faithful, Full, and Essentially Surjective

- **Faithful:** injective on each hom-set $\text{Hom}(A,B)$
- **Full:** surjective on each hom-set
- **Essentially surjective:** every object in $\mathcal{D}$ is isomorphic to $F(A)$ for some $A$

An **equivalence of categories** is a functor that is full, faithful, and essentially surjective.

## Endofunctors

A functor $F : \mathcal{C} \to \mathcal{C}$ is an **endofunctor**. Monads are endofunctors with additional structure.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $F : \mathcal{C} \to \mathcal{D}$ | functor from category $\mathcal{C}$ to $\mathcal{D}$ |
| $F(A)$ | the image of object $A$ under functor $F$ |
| $F(f)$ | the image of morphism $f$ under functor $F$ |
| Covariant functor | preserves direction of morphisms |
| Contravariant functor | reverses direction of morphisms |
| $F(g \circ f) = F(g)\circ F(f)$ | functoriality: composition preserved |
| Forgetful functor | "forgets" extra structure (e.g. **Grp** → **Set**) |
| Free functor | left adjoint to the forgetful functor |
| Faithful | injective on hom-sets |
| Full | surjective on hom-sets |
| Equivalence of categories | full, faithful, essentially surjective functor |
| Endofunctor | functor from a category to itself |
| **Ab** | category of abelian groups |
