---
title: Monoidal Categories
tag: category-theory
summary: Categories equipped with a tensor product bifunctor and a unit object satisfying associativity and unit axioms up to natural isomorphism.
links:
  - categories-morphisms
  - adjoint-functors
  - string-diagrams
  - monads
---

# Monoidal Categories

A **monoidal category** is a category $\mathcal{C}$ equipped with a **tensor product** $\otimes : \mathcal{C} \times \mathcal{C} \to \mathcal{C}$ and a **unit object** $I$, together with natural isomorphisms expressing associativity $(A \otimes B) \otimes C \cong A \otimes (B \otimes C)$ and unit conditions $I \otimes A \cong A \cong A \otimes I$. Monoidal categories abstract the idea of "things that can be composed in parallel" — tensor products of vector spaces, composition of cobordisms, simultaneous processes in physics, and sequential programs are all captured by the monoidal structure. They are the natural setting for braiding, symmetry, duality, and the graphical calculus of **string diagrams**, and appear at the heart of quantum groups, topological field theories, and categorical logic.

## Definition

A **monoidal category** $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ consists of:

- A category $\mathcal{C}$
- A **tensor product** bifunctor $\otimes : \mathcal{C} \times \mathcal{C} \to \mathcal{C}$
- A **unit object** $I \in \mathcal{C}$
- Natural isomorphisms:
  - **Associator** $\alpha_{A,B,C} : (A \otimes B) \otimes C \xrightarrow{\sim} A \otimes (B \otimes C)$
  - **Left unitor** $\lambda_A : I \otimes A \xrightarrow{\sim} A$
  - **Right unitor** $\rho_A : A \otimes I \xrightarrow{\sim} A$

satisfying the **pentagon** and **triangle** coherence axioms.

## Examples

| Category | $\otimes$ | Unit $I$ |
|---|---|---|
| **Vect$_k$** | tensor product $V \otimes W$ | base field $k$ |
| **Set** | Cartesian product $A \times B$ | singleton $\{*\}$ |
| **Set** | disjoint union $A \sqcup B$ | $\emptyset$ |
| **Top** | product topology | point |
| **Rel** (relations) | $A \times B$ | $\{*\}$ |
| Endofunctors of $\mathcal{C}$ | composition $F \circ G$ | identity functor |

## Symmetric Monoidal Category

A **symmetric monoidal category** has a natural isomorphism $\sigma_{A,B} : A \otimes B \xrightarrow{\sim} B \otimes A$ (the swap) satisfying $\sigma_{B,A} \circ \sigma_{A,B} = \text{id}$.

## Braided Monoidal Category

A **braiding** is like symmetry but without requiring $\sigma_{B,A} \circ \sigma_{A,B} = \text{id}$ — allowing non-trivial braiding. Arises in knot theory and quantum groups.

## Closed Monoidal Category

Has **internal hom** objects $[A, B]$ (or $A \multimap B$) with natural bijections $\text{Hom}(C \otimes A, B) \cong \text{Hom}(C, [A,B])$ — the tensor-hom adjunction.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $(\mathcal{C}, \otimes, I)$ | monoidal category |
| $\otimes$ | tensor product (monoidal product) |
| $I$ | unit object |
| $\alpha_{A,B,C}$ | associator: $(A\otimes B)\otimes C \cong A\otimes(B\otimes C)$ |
| $\lambda_A$ | left unitor: $I \otimes A \cong A$ |
| $\rho_A$ | right unitor: $A \otimes I \cong A$ |
| Pentagon axiom | coherence condition on associators |
| Triangle axiom | coherence condition on unitors and associator |
| Symmetric | has $\sigma: A\otimes B \cong B\otimes A$ with $\sigma^2=\text{id}$ |
| Braided | has $\sigma: A\otimes B \cong B\otimes A$ without $\sigma^2=\text{id}$ |
| Closed monoidal | has internal hom $[A,B]$ with $\text{Hom}(C\otimes A,B)\cong\text{Hom}(C,[A,B])$ |
