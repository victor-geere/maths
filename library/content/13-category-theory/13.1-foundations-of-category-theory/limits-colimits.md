---
title: Limits & Colimits
tag: category-theory
summary: The general categorical notion of "taking a diagram and finding its best completion" — encompassing products, equalisers, pullbacks, and their duals.
links:
  - products-coproducts
  - adjoint-functors
  - functors
  - initial-terminal-objects
---

# Limits & Colimits

**Limits** and **colimits** are the most fundamental and powerful universal constructions in category theory, unifying a huge variety of mathematical constructions under a single definition. A **limit** of a diagram $D : \mathcal{J} \to \mathcal{C}$ is an object $L$ together with morphisms to each object in the diagram, satisfying a universal property: any other "cone" over the diagram factors uniquely through $L$. **Colimits** are the dual notion — cones under the diagram. Products, equalisers, pullbacks, and inverse limits are all limits; coproducts, coequalisers, pushouts, and direct limits are all colimits. The existence of all small limits (or colimits) in a category is a powerful completeness property that enables most of algebraic topology and sheaf theory.

## Diagrams and Cones

A **diagram** in $\mathcal{C}$ of shape $\mathcal{J}$ is a functor $D : \mathcal{J} \to \mathcal{C}$.

A **cone** over $D$ with apex $L$ is an object $L$ together with morphisms $\lambda_j : L \to D(j)$ for each $j \in \mathcal{J}$, compatible with every morphism in $\mathcal{J}$.

## Limit

The **limit** $\lim D$ is the terminal cone: for any other cone $(C, \{c_j\})$ over $D$, there is a unique morphism $C \to \lim D$ commuting with all cone morphisms.

## Colimit

The **colimit** $\text{colim}\, D$ is the initial cocone: for any other cocone $(C, \{c_j : D(j) \to C\})$, there is a unique morphism $\text{colim}\, D \to C$ commuting with all cocone morphisms.

## Special Cases

| Limit | Shape $\mathcal{J}$ | Name |
|---|---|---|
| $A \times B$ | discrete pair | Product |
| $\{x : f(x)=g(x)\}$ | parallel arrows | Equaliser |
| Pullback | cospan | Pullback |
| $\varprojlim A_n$ | $\mathbb{N}^{\text{op}}$ | Inverse limit |

| Colimit | Shape $\mathcal{J}$ | Name |
|---|---|---|
| $A + B$ | discrete pair | Coproduct |
| Coimage | parallel arrows | Coequaliser |
| Pushout | span | Pushout |
| $\varinjlim A_n$ | $\mathbb{N}$ | Direct limit |

## Completeness

A category is **complete** if it has all small limits, **cocomplete** if it has all small colimits. **Set**, **Grp**, **Top**, **Ab**, and **Vect$_k$** are both complete and cocomplete.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $D : \mathcal{J} \to \mathcal{C}$ | diagram of shape $\mathcal{J}$ in category $\mathcal{C}$ |
| $\mathcal{J}$ | index category (shape of the diagram) |
| Cone | compatible family of morphisms from a single apex to all objects in a diagram |
| Cocone | compatible family of morphisms from diagram objects to a single apex |
| $\lim D$ | limit: terminal cone over $D$ |
| $\text{colim}\, D$ | colimit: initial cocone under $D$ |
| Equaliser | limit over two parallel arrows: $\{x : f(x) = g(x)\}$ |
| Coequaliser | colimit over two parallel arrows |
| Pullback | limit over a cospan $A \to C \leftarrow B$ |
| Pushout | colimit over a span $A \leftarrow C \to B$ |
| Complete category | has all small limits |
| Cocomplete | has all small colimits |
