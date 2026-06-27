---
title: Opposite Categories & Duality
tag: category-theory
summary: The opposite category reverses all arrows, turning every categorical statement into its dual — a principle of "free theorems" that doubles every result.
links:
  - categories-morphisms
  - functors
  - products-coproducts
  - initial-terminal-objects
---

# Opposite Categories & Duality

One of the most powerful features of category theory is the **duality principle**: every categorical definition and theorem has a **dual** obtained by formally reversing all arrows. The **opposite category** $\mathcal{C}^{\text{op}}$ of a category $\mathcal{C}$ is the category with the same objects but all morphisms reversed. A concept defined purely in categorical terms — limits, colimits, initial objects, products, and so on — automatically gives rise to a dual concept when applied to $\mathcal{C}^{\text{op}}$. This means that every theorem proved in category theory yields a second theorem for free, without any extra work. Duality is a pervasive feature of mathematics, and category theory makes it precise and systematic.

## Definition

Given a category $\mathcal{C}$, the **opposite category** $\mathcal{C}^{\text{op}}$ has:

- The same objects as $\mathcal{C}$
- For each morphism $f : A \to B$ in $\mathcal{C}$, a morphism $f^{\text{op}} : B \to A$ in $\mathcal{C}^{\text{op}}$
- Composition: $g^{\text{op}} \circ^{\text{op}} f^{\text{op}} = (f \circ g)^{\text{op}}$ (note the reversal)

## The Duality Principle

If a statement $P$ holds in **every** category $\mathcal{C}$, then the dual statement $P^{\text{op}}$ (obtained by replacing every $\mathcal{C}$ with $\mathcal{C}^{\text{op}}$ and reversing all arrows) also holds in every category.

## Examples of Dual Concepts

| Concept | Dual concept |
|---|---|
| Initial object | Terminal object |
| Product | Coproduct |
| Limit | Colimit |
| Monomorphism (injective) | Epimorphism (surjective) |
| Left adjoint | Right adjoint |
| Pullback | Pushout |
| Kernel | Cokernel |

## Contravariant Functors

A **contravariant functor** $F : \mathcal{C} \to \mathcal{D}$ is the same as a covariant functor $F : \mathcal{C}^{\text{op}} \to \mathcal{D}$.

Example: the hom functor $\text{Hom}(-, B) : \mathcal{C}^{\text{op}} \to \textbf{Set}$ sends $A \mapsto \text{Hom}(A,B)$ and reverses morphisms.

## Presheaves

A **presheaf** on $\mathcal{C}$ is a functor $F : \mathcal{C}^{\text{op}} \to \textbf{Set}$. The category of presheaves $[\mathcal{C}^{\text{op}}, \textbf{Set}]$ is central to the Yoneda lemma and topos theory.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathcal{C}^{\text{op}}$ | opposite category: same objects, all arrows reversed |
| $f^{\text{op}}$ | the morphism $f : A \to B$ viewed as $B \to A$ in $\mathcal{C}^{\text{op}}$ |
| Duality principle | every categorical statement has a dual obtained by reversing arrows |
| Dual concept | the concept obtained by applying a definition to $\mathcal{C}^{\text{op}}$ |
| Monomorphism | $f : A \to B$ such that $f \circ g = f \circ h \Rightarrow g = h$ (left-cancellable) |
| Epimorphism | $f : A \to B$ such that $g \circ f = h \circ f \Rightarrow g = h$ (right-cancellable) |
| Contravariant functor | functor $\mathcal{C}^{\text{op}} \to \mathcal{D}$; reverses arrow direction |
| Presheaf | a functor $\mathcal{C}^{\text{op}} \to \textbf{Set}$ |
| $\text{Hom}(-,B)$ | contravariant hom functor: $A \mapsto \text{Hom}(A,B)$ |
| Pushout | colimit of a span; dual to pullback |
| Cokernel | dual to kernel; quotient by image |
