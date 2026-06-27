---
title: Monads
tag: category-theory
summary: An endofunctor with unit and multiplication satisfying monoid laws — the categorical abstraction of computational effects, algebraic structures, and closure operators.
links:
  - functors
  - natural-transformations
  - adjoint-functors
---

# Monads

A **monad** is an endofunctor $T : \mathcal{C} \to \mathcal{C}$ equipped with two natural transformations — a **unit** $\eta : \text{id} \Rightarrow T$ and a **multiplication** $\mu : T^2 \Rightarrow T$ — satisfying associativity and unit axioms that make $(T, \eta, \mu)$ a **monoid in the category of endofunctors**. Every adjunction $F \dashv G$ gives rise to a monad $T = G \circ F$, and conversely every monad arises from an adjunction. In computer science, monads model **computational effects**: the list monad captures non-determinism, the Maybe monad models failure, the IO monad encapsulates input/output, and the state monad carries state — all unified by the same categorical definition. This connection, popularised by Eugenio Moggi and Philip Wadler, made Haskell's monad framework one of the most influential ideas in programming language theory.

## Definition

A **monad** on $\mathcal{C}$ is a triple $(T, \eta, \mu)$ where:

- $T : \mathcal{C} \to \mathcal{C}$ is an endofunctor
- $\eta : \text{id}_\mathcal{C} \Rightarrow T$ is the **unit** (return)
- $\mu : T^2 \Rightarrow T$ is the **multiplication** (join/flatten)

satisfying the **monad laws:**

1. $\mu \circ T\mu = \mu \circ \mu T$ (associativity)
2. $\mu \circ T\eta = \text{id}_T = \mu \circ \eta T$ (unit laws)

## From Adjunctions

Every adjunction $F \dashv G$ gives a monad: $T = GF$, $\eta$ = unit of adjunction, $\mu = G\varepsilon F$ where $\varepsilon$ is the counit.

## Kleisli Category

The **Kleisli category** $\mathcal{C}_T$ of a monad has the same objects as $\mathcal{C}$ but morphisms $A \to B$ in $\mathcal{C}_T$ are morphisms $A \to T(B)$ in $\mathcal{C}$. Composition uses $\mu$.

## Examples

| Monad $T$ | Category | Models |
|---|---|---|
| $T(A) = A \times S$ (state) | **Set** | Stateful computations |
| $T(A) = A + \{*\}$ (Maybe) | **Set** | Partial functions / failure |
| $T(A) = $ list$(A)$ | **Set** | Non-determinism |
| $T(A) = P(A)$ (powerset) | **Set** | Non-determinism |
| Free algebra functor | **Set** | Algebraic theories |

## Algebras over a Monad

A **$T$-algebra** (Eilenberg–Moore algebra) is an object $A$ with a morphism $\alpha : T(A) \to A$ satisfying $\alpha \circ \eta_A = \text{id}_A$ and $\alpha \circ \mu_A = \alpha \circ T\alpha$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $(T, \eta, \mu)$ | monad: endofunctor with unit and multiplication |
| $T : \mathcal{C} \to \mathcal{C}$ | endofunctor |
| $\eta : \text{id} \Rightarrow T$ | unit (return): embeds $A$ into $T(A)$ |
| $\mu : T^2 \Rightarrow T$ | multiplication (join/flatten): collapses $T(T(A))$ to $T(A)$ |
| $T^2 = T \circ T$ | composition of $T$ with itself |
| Monad laws | associativity and unit laws (mirror monoid axioms) |
| Kleisli category | morphisms $A \to B$ are $A \to T(B)$; composition uses $\mu$ |
| $T$-algebra | object $A$ with $\alpha : T(A) \to A$ satisfying compatibility |
| Maybe monad | $T(A) = A \sqcup \{*\}$; models computations that may fail |
| State monad | $T(A) = (A \times S)^S$; threads a state $S$ through computations |
