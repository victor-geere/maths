---
title: Subsets & Power Sets
tag: set-theory
summary: Subset relation (⊆), proper subsets (⊂), and power sets P(S) — the set of all subsets.
links:
  - sets-notation
  - set-operations
  - finite-infinite-sets
---

# Subsets & Power Sets

## Subsets

A set A is a **subset** of a set B, written A ⊆ B, if every element of A is also in B.

**Definition**: A ⊆ B ⟺ ∀x (x ∈ A → x ∈ B)

### Examples

- {1, 2} ⊆ {1, 2, 3}
- {1, 2, 3} ⊆ {1, 2, 3} (every set is a subset of itself)
- ∅ ⊆ {1, 2, 3} (the empty set is a subset of every set)
- ℕ ⊆ ℤ (natural numbers are integers)
- {x ∈ ℝ | x² < 1} ⊆ ℝ

### Proper Subsets

A set A is a **proper subset** of B, written A ⊂ B or A ⊊ B, if A ⊆ B and A ≠ B.

**Definition**: A ⊂ B ⟺ A ⊆ B ∧ A ≠ B

Examples:
- {1, 2} ⊂ {1, 2, 3} (proper)
- {1, 2, 3} ⊄ {1, 2, 3} (not proper, they're equal)

### Properties of Subsets

- **Reflexive**: A ⊆ A (every set is a subset of itself)
- **Transitive**: If A ⊆ B and B ⊆ C, then A ⊆ C
- **Antisymmetric**: If A ⊆ B and B ⊆ A, then A = B

These properties make ⊆ a **partial order** on the collection of all sets.

## Power Sets

The **power set** of S, denoted P(S) or 2^S, is the set of all subsets of S.

**Definition**: P(S) = {A | A ⊆ S}

### Examples

**Example 1**: S = {1, 2}
- Subsets of S: ∅, {1}, {2}, {1, 2}
- P({1, 2}) = {∅, {1}, {2}, {1, 2}}

**Example 2**: S = {a}
- Subsets: ∅, {a}
- P({a}) = {∅, {a}}

**Example 3**: S = ∅
- Only subset: ∅
- P(∅) = {∅}

### Cardinality of Power Sets

If |S| = n, then |P(S)| = 2^n

**Proof**: Each element of S can either be included or excluded from a subset. For n elements, there are 2^n binary choices.

Examples:
- |P(∅)| = 2^0 = 1
- |P({1})| = 2^1 = 2
- |P({1, 2})| = 2^2 = 4
- |P({1, 2, 3})| = 2^3 = 8
- |P(ℕ)| = 2^ℵ₀ (uncountably infinite)

## Relationships Between Sets

### Disjoint Sets

Sets A and B are **disjoint** if they have no elements in common.

**Definition**: A ∩ B = ∅

### Chains of Subsets

A **chain** is a sequence of sets where each is a subset of the next:

A₁ ⊆ A₂ ⊆ A₃ ⊆ ... ⊆ Aₙ

**Example**: {1} ⊆ {1, 2} ⊆ {1, 2, 3} ⊆ ℕ

### Partition

A collection of sets {A₁, A₂, ..., Aₙ} **partitions** set S if:
1. Each Aᵢ is non-empty
2. The sets are pairwise disjoint: Aᵢ ∩ Aⱼ = ∅ for i ≠ j
3. Their union is S: A₁ ∪ A₂ ∪ ... ∪ Aₙ = S

**Example**: {{1, 2}, {3}, {4, 5, 6}} partitions {1, 2, 3, 4, 5, 6}

## Key Facts

- **Empty set is unique**: Only one empty set exists
- **Empty set is subset of all sets**: ∅ ⊆ S for any S
- **Subset is reflexive**: A ⊆ A
- **Power set is always larger**: For finite sets, |S| < |P(S)|

## Venn Diagrams

Venn diagrams visualize subset relationships:

```
    ────────────────
    │      U        │
    │  ───────────  │
    │  │     A     ││
    │  │  ─────── ││
    │  │  │   B   │││
    │  │  │       │││
    │  │  └───────┘││
    │  └───────────┘│
    └────────────────┘
```

Here B ⊂ A ⊂ U (U is the universal set)

## Notation Summary

| Notation | Meaning |
|----------|---------|
| A ⊆ B | A is a subset of B |
| A ⊂ B | A is a proper subset of B |
| A ⊄ B | A is not a subset of B |
| P(S) | Power set of S |
| 2^S | Alternative notation for P(S) |
