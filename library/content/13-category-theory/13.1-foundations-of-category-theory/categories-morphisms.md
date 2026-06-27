---
title: Categories, Objects & Morphisms
tag: category-theory
summary: The foundational definition of a category — a collection of objects and arrows between them satisfying identity and associativity — the language underlying all of modern mathematics.
links:
  - functors
  - natural-transformations
  - opposite-categories
  - group-homomorphisms
---

# Categories, Objects & Morphisms

**Category theory** is the mathematical study of abstract structure and the mappings between structures. A **category** consists of a collection of **objects** and **morphisms** (arrows) between them, satisfying two axioms: every object has an identity morphism, and morphisms can be **composed** associatively. This minimal definition captures the essence of almost every mathematical structure: sets with functions, groups with homomorphisms, topological spaces with continuous maps, and vector spaces with linear maps are all categories. Category theory provides a unified language for mathematics — a single theorem proved in a category immediately applies to every example of that category — and has become indispensable in algebra, topology, logic, and computer science.

## Definition

A **category** $\mathcal{C}$ consists of:

- A collection $\text{ob}(\mathcal{C})$ of **objects** (denoted $A, B, C, \ldots$)
- For each pair of objects $A, B$, a set $\text{Hom}(A, B)$ of **morphisms** from $A$ to $B$ (written $f : A \to B$)
- A **composition law:** for $f : A \to B$ and $g : B \to C$, a morphism $g \circ f : A \to C$
- For each object $A$, an **identity morphism** $\text{id}_A : A \to A$

**Axioms:**
1. **Associativity:** $(h \circ g) \circ f = h \circ (g \circ f)$
2. **Unit laws:** $\text{id}_B \circ f = f = f \circ \text{id}_A$

## Standard Examples

| Category | Objects | Morphisms |
|---|---|---|
| **Set** | sets | functions |
| **Grp** | groups | group homomorphisms |
| **Top** | topological spaces | continuous maps |
| **Vect$_k$** | $k$-vector spaces | linear maps |
| **Ring** | rings | ring homomorphisms |
| **Cat** | small categories | functors |
| A poset $(P, \leq)$ | elements of $P$ | arrows $a \to b$ iff $a \leq b$ |
| A monoid $M$ | one object $\bullet$ | elements of $M$ (composition = monoid operation) |

## Isomorphisms

A morphism $f : A \to B$ is an **isomorphism** if there exists $g : B \to A$ with $g \circ f = \text{id}_A$ and $f \circ g = \text{id}_B$.

Objects $A$ and $B$ are **isomorphic** ($A \cong B$) if an isomorphism exists between them.

## Endomorphisms and Automorphisms

An **endomorphism** is $f : A \to A$. An **automorphism** is an endomorphism that is also an isomorphism. The automorphisms of $A$ form a group $\text{Aut}(A)$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathcal{C}$ | a category |
| $\text{ob}(\mathcal{C})$ | the collection of objects of $\mathcal{C}$ |
| $\text{Hom}(A,B)$ | hom-set: morphisms from $A$ to $B$ |
| $f : A \to B$ | a morphism from object $A$ to object $B$ |
| $g \circ f$ | composition: apply $f$ first, then $g$ |
| $\text{id}_A$ | identity morphism on $A$: $f \circ \text{id}_A = f$, $\text{id}_B \circ f = f$ |
| Isomorphism | morphism with a two-sided inverse |
| $A \cong B$ | objects $A$ and $B$ are isomorphic |
| Endomorphism | morphism $f : A \to A$ |
| Automorphism | invertible endomorphism |
| **Set** | the category of sets and functions |
| **Grp** | the category of groups and homomorphisms |
| Small category | objects and morphisms form sets (not proper classes) |
