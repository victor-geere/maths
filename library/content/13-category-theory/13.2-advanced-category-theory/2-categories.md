---
title: 2-Categories & Bicategories
tag: category-theory
summary: Categories enriched over Cat — with objects, morphisms, and 2-morphisms between morphisms — capturing the homotopy theory of categories and the structure of adjunctions.
links:
  - categories-morphisms
  - natural-transformations
  - functors
  - infinity-categories
---

# 2-Categories & Bicategories

A **2-category** extends the notion of a category by adding a third level: **2-morphisms** between morphisms. Where a category has objects and morphisms (1-morphisms), a 2-category adds morphisms between morphisms (2-morphisms) — natural transformations are the 2-morphisms of **Cat**. A **bicategory** (or **weak 2-category**) allows the composition of morphisms to be associative and unital only up to specified 2-isomorphisms, rather than strictly. This generality is essential: categories themselves are the objects, functors the 1-morphisms, and natural transformations the 2-morphisms of the 2-category **Cat**. Bicategories arise naturally in algebraic topology (cobordisms), algebra (bimodules), and higher-dimensional physics (topological field theories).

## Definition: Strict 2-Category

A **strict 2-category** $\mathcal{K}$ has:

- A collection of **objects** $A, B, C, \ldots$
- For each pair $(A, B)$, a **category** $\mathcal{K}(A, B)$ whose objects are **1-morphisms** $f : A \to B$ and morphisms are **2-morphisms** $\alpha : f \Rightarrow g$
- **Horizontal composition** of 1-morphisms (composition in $\mathcal{K}$) and **vertical composition** of 2-morphisms (composition within $\mathcal{K}(A,B)$)
- **Horizontal composition** of 2-morphisms (whiskering)

All compositions are strictly associative and unital.

## Bicategory (Weak 2-Category)

A **bicategory** relaxes strictness: associativity and units for horizontal composition hold only up to specified invertible 2-morphisms (associator $\alpha$, left unitor $\lambda$, right unitor $\rho$) satisfying coherence conditions (the pentagon and triangle equations).

## The 2-Category **Cat**

- **Objects:** (small) categories
- **1-morphisms:** functors $F : \mathcal{C} \to \mathcal{D}$
- **2-morphisms:** natural transformations $\eta : F \Rightarrow G$

## Key Examples

| 2-Category | Objects | 1-Morphisms | 2-Morphisms |
|---|---|---|---|
| **Cat** | categories | functors | natural transformations |
| **Bimod** | rings | bimodules | bimodule maps |
| **Span** | sets | spans $A \leftarrow E \rightarrow B$ | maps of spans |
| **2Grp** | 2-groups | 2-group homomorphisms | 2-group 2-morphisms |

## Adjunctions in 2-Categories

An **adjunction** in a 2-category is a 1-morphism $f : A \to B$ with a right adjoint $g : B \to A$ and unit/counit 2-morphisms satisfying the triangle identities. This captures adjoint functors, adjoint linear maps, and more.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| 2-category | a category enriched over **Cat** |
| Objects | the 0-cells of the 2-category |
| 1-morphisms | morphisms between objects (arrows between 0-cells) |
| 2-morphisms | morphisms between 1-morphisms (natural transformations in **Cat**) |
| Vertical composition | composing 2-morphisms with the same source/target 1-morphism |
| Horizontal composition | composing 2-morphisms along 1-morphisms (whiskering) |
| Bicategory | weak 2-category: associativity/units hold up to specified 2-isomorphisms |
| Associator | the 2-isomorphism $(f \circ g) \circ h \cong f \circ (g \circ h)$ in a bicategory |
| Coherence | the conditions (pentagon, triangle) ensuring bicategories behave consistently |
| $\alpha : f \Rightarrow g$ | a 2-morphism between parallel 1-morphisms |
| Whiskering | pre- or post-composing a 2-morphism with a 1-morphism |
