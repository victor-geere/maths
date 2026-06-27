---
title: Natural Transformations
tag: category-theory
summary: A morphism between functors — a coherent family of morphisms, one for each object, satisfying a naturality square that encodes true "naturality" in mathematics.
links:
  - functors
  - categories-morphisms
  - yoneda-lemma
  - adjoint-functors
---

# Natural Transformations

A **natural transformation** is a morphism between two functors. If $F, G : \mathcal{C} \to \mathcal{D}$ are functors, a natural transformation $\eta : F \Rightarrow G$ provides, for each object $A \in \mathcal{C}$, a morphism $\eta_A : F(A) \to G(A)$ in $\mathcal{D}$, such that these morphisms are "compatible" with all morphisms in $\mathcal{C}$ in a precise sense called the **naturality condition**. Natural transformations formalise the intuition of doing something "in a way that doesn't depend on choices" — the term "natural" in mathematics (natural isomorphism, natural map) refers precisely to being a natural transformation. They are the 2-morphisms of the 2-category **Cat**, and the Yoneda lemma — perhaps the most important result in category theory — is entirely about natural transformations.

## Definition

Given functors $F, G : \mathcal{C} \to \mathcal{D}$, a **natural transformation** $\eta : F \Rightarrow G$ is a family of morphisms $\{\eta_A : F(A) \to G(A)\}_{A \in \mathcal{C}}$ such that for every morphism $f : A \to B$ in $\mathcal{C}$, the following **naturality square** commutes:

$$\begin{array}{ccc} F(A) & \xrightarrow{F(f)} & F(B) \\ {\scriptscriptstyle\eta_A}\downarrow & & \downarrow{\scriptscriptstyle\eta_B} \\ G(A) & \xrightarrow{G(f)} & G(B) \end{array}$$

i.e. $\eta_B \circ F(f) = G(f) \circ \eta_A$.

## Natural Isomorphism

A natural transformation $\eta : F \Rightarrow G$ is a **natural isomorphism** if every component $\eta_A$ is an isomorphism in $\mathcal{D}$. Then $F \cong G$ as functors.

## Examples

- The **double-dual embedding** $V \hookrightarrow V^{**}$: a natural isomorphism for finite-dimensional vector spaces (but not for infinite-dimensional ones).
- **Determinant:** $\det : GL_n(R) \to R^*$ is natural in $R$ (a natural transformation of functors from **Ring** to **Grp**).
- Singular cohomology and de Rham cohomology are naturally isomorphic (on smooth manifolds) — this is de Rham's theorem.

## Functor Categories

Given categories $\mathcal{C}$ and $\mathcal{D}$, the **functor category** $[\mathcal{C}, \mathcal{D}]$ (or $\mathcal{D}^\mathcal{C}$) has:
- **Objects:** functors $F : \mathcal{C} \to \mathcal{D}$
- **Morphisms:** natural transformations $\eta : F \Rightarrow G$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\eta : F \Rightarrow G$ | natural transformation from functor $F$ to functor $G$ |
| $\eta_A : F(A) \to G(A)$ | the component of $\eta$ at object $A$ |
| Naturality square | the commutative diagram encoding $\eta_B \circ F(f) = G(f) \circ \eta_A$ |
| Commutes | a diagram commutes if all paths between two objects give the same composite |
| Natural isomorphism | $\eta$ where every $\eta_A$ is an isomorphism |
| $F \cong G$ | functors $F$ and $G$ are naturally isomorphic |
| Functor category $[\mathcal{C},\mathcal{D}]$ | category whose objects are functors and morphisms are natural transformations |
| $V^{**}$ | double dual of a vector space |
| $GL_n(R)$ | group of invertible $n\times n$ matrices over ring $R$ |
| $R^*$ | units (invertible elements) of ring $R$ |
| 2-morphism | a morphism between morphisms; natural transformations are 2-morphisms in **Cat** |
