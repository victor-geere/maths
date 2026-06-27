---
title: Categorical Database Theory
tag: category-theory
summary: Modelling databases as functors from a schema category to Set — giving a principled categorical foundation for relational algebra, data migration, and query optimisation.
links:
  - functors
  - natural-transformations
  - limits-colimits
  - adjoint-functors
---

# Categorical Database Theory

**Categorical Database Theory**, developed primarily by David Spivak, models databases and data migration using the language of category theory. A **database schema** is modelled as a small category $\mathcal{C}$ (where objects are entity types and morphisms are foreign-key relationships), and an **instance** of the schema — the actual data — is a functor $I : \mathcal{C} \to \textbf{Set}$ assigning a set of rows to each table and a function between sets to each foreign key. This functorial view unifies relational algebra, query languages, and data migration into a single categorical framework: queries become natural transformations, data migration between schemas becomes adjoint functors, and joins, projections, and unions correspond to limits and colimits. The approach has led to practical tools (the **CQL** language) and provides mathematically principled foundations for database theory.

## Database Schema as a Category

A **schema** is a small category $\mathcal{C}$:

- **Objects:** table names ($A$, $B$, $C$, …)
- **Morphisms** $f : A \to B$: foreign-key columns (each row of $A$ points to a row of $B$)
- **Composition:** chained foreign keys
- **Identity:** the primary key pointing to itself

## Database Instance as a Functor

An **instance** $I : \mathcal{C} \to \textbf{Set}$:

- $I(A)$: the set of rows in table $A$
- $I(f) : I(A) \to I(B)$: the foreign-key function

**Morphisms between instances** are natural transformations $\eta : I \Rightarrow J$ — consistent row mappings across all tables.

## Relational Operations as Categorical Constructions

| Database operation | Category-theoretic construction |
|---|---|
| Join | Limit (pullback) in **Set** |
| Union | Colimit (pushout) in **Set** |
| Projection | Composition with forgetful functor |
| Selection (filter) | Equaliser |
| Data migration | Adjoint functors between functor categories |

## Data Migration

Given a schema morphism $F : \mathcal{C} \to \mathcal{D}$ (a functor between schemas), data can be migrated in three ways:

- **$\Sigma_F$** (left pushforward): colimit-based, "union-like"
- **$\Delta_F$** (restriction): $I \mapsto I \circ F$, the pullback along $F$
- **$\Pi_F$** (right pushforward): limit-based, "join-like"

These form adjunctions: $\Sigma_F \dashv \Delta_F \dashv \Pi_F$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Schema $\mathcal{C}$ | a small category encoding tables and foreign keys |
| Instance $I : \mathcal{C} \to \textbf{Set}$ | functor assigning data to each table |
| $I(A)$ | the set of rows in table $A$ |
| $I(f)$ | the foreign-key function for morphism $f$ |
| Natural transformation $\eta : I \Rightarrow J$ | a consistent mapping between two database instances |
| Pullback | categorical join: limit over a cospan |
| Pushout | categorical union: colimit over a span |
| Data migration | moving data from one schema to another via adjoint functors |
| $\Delta_F$ | pullback functor: restriction of instances along $F$ |
| $\Sigma_F$ | left pushforward: $\Sigma_F \dashv \Delta_F$ |
| $\Pi_F$ | right pushforward: $\Delta_F \dashv \Pi_F$ |
| CQL | Categorical Query Language — a practical implementation |
