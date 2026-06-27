---
title: Relations
tag: set-theory
summary: Subsets of A × B with properties (reflexive, symmetric, transitive) defining orders and equivalences.
links:
  - cartesian-product
  - equivalence-relations
  - partial-orders
---

# Relations

A **relation** from set A to set B is any subset of the Cartesian product A × B.

**Definition**: R ⊆ A × B

If (a, b) ∈ R, we write **a R b** and say "a is related to b by R".

## Notation

For a relation R ⊆ A × B:
- **(a, b) ∈ R** or equivalently **a R b** — a is related to b
- **(a, b) ∉ R** or equivalently **a ⊭ R b** — a is not related to b

## Examples

### Relation on ℝ
- R = {(x, y) ∈ ℝ × ℝ | x < y} — the "less than" relation
- 2 < 5, so (2, 5) ∈ R
- 7 ≮ 3, so (7, 3) ∉ R

### Divisibility
- D = {(a, b) ∈ ℤ × ℤ | a | b} — "a divides b"
- (2, 6) ∈ D because 2 divides 6
- (3, 7) ∉ D because 3 doesn't divide 7

### Membership in Family
- P = {(x, S) ∈ ℝ × P(ℝ) | x ∈ S}
- (2, {1, 2, 3}) ∈ P because 2 ∈ {1, 2, 3}

## Properties of Relations

A relation R on a set A (where R ⊆ A × A) may have properties:

### Reflexive
**R is reflexive** if (a, a) ∈ R for all a ∈ A.

- Equality (=) is reflexive: a = a
- ≤ is reflexive: a ≤ a
- < is not reflexive: a ≮ a

### Symmetric
**R is symmetric** if (a, b) ∈ R implies (b, a) ∈ R.

- Equality (=) is symmetric: if a = b then b = a
- Friendship is (usually) symmetric
- ≤ is not symmetric: 2 ≤ 3 but 3 ≤ 2 is false

### Antisymmetric
**R is antisymmetric** if (a, b) ∈ R and (b, a) ∈ R imply a = b.

- ≤ is antisymmetric: if a ≤ b and b ≤ a, then a = b
- ⊆ is antisymmetric: if A ⊆ B and B ⊆ A, then A = B
- Equality is antisymmetric (vacuously)

### Transitive
**R is transitive** if (a, b) ∈ R and (b, c) ∈ R imply (a, c) ∈ R.

- Equality: if a = b and b = c, then a = c
- < and ≤ are transitive
- "Parent of" is transitive (ancestor relation)

## Composition of Relations

If R ⊆ A × B and S ⊆ B × C, the **composition** R ∘ S is:

**R ∘ S = {(a, c) ∈ A × C | ∃b ∈ B such that (a, b) ∈ R and (b, c) ∈ S}**

### Example

- R = {(1, 2), (2, 3), (3, 4)} where a R b means (a, b) ∈ R
- S = {(2, x), (3, y), (4, z)}
- R ∘ S = {(1, x), (2, y), (3, z)} (chain the relations)

## Inverse Relation

The **inverse** (or **converse**) of R ⊆ A × B is:

**R⁻¹ = {(b, a) | (a, b) ∈ R} ⊆ B × A**

### Example

- R = {(1, a), (2, b), (3, a)}
- R⁻¹ = {(a, 1), (b, 2), (a, 3)}

### Properties

- (R⁻¹)⁻¹ = R
- (R ∘ S)⁻¹ = S⁻¹ ∘ R⁻¹
- R is symmetric iff R = R⁻¹

## Domain and Range

For R ⊆ A × B:

- **Domain**: dom(R) = {a ∈ A | ∃b ∈ B, (a, b) ∈ R}
- **Range**: ran(R) = {b ∈ B | ∃a ∈ A, (a, b) ∈ R}

## Representing Relations

### Matrix Representation
For finite sets, represent as a 0-1 matrix:

R = {(1, a), (2, b), (2, c)}

|   | a | b | c |
|---|---|---|---|
| 1 | 1 | 0 | 0 |
| 2 | 0 | 1 | 1 |

1 in position (i, j) means (i, j) ∈ R

### Graph Representation
Draw nodes for set elements, directed edges for relation pairs.

```
1 → a
2 → b
2 → c
```

## Classification of Relations

Relations can be classified by their properties:

| Type | Properties | Example |
|------|-----------|---------|
| Equivalence | Reflexive, symmetric, transitive | Equality, congruence |
| Partial order | Reflexive, antisymmetric, transitive | ≤, ⊆ |
| Strict order | Irreflexive, antisymmetric, transitive | <, ⊂ |
| Total order | Partial order + all pairs comparable | Usual ordering on ℝ |

See [[equivalence-relations]] and [[partial-orders]] for details.
