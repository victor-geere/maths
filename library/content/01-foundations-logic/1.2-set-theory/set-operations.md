---
title: Set Operations (∪, ∩, \)
tag: set-theory
summary: Union, intersection, difference, complement, and De Morgan's laws for sets.
links:
  - sets-notation
  - subsets-power-sets
---

# Set Operations (∪, ∩, \)

## Union (∪)

The **union** of sets A and B, written A ∪ B, is the set of all elements that are in A or B (or both).

**Definition**: A ∪ B = {x | x ∈ A ∨ x ∈ B}

### Examples

- {1, 2} ∪ {2, 3} = {1, 2, 3}
- {a, b} ∪ ∅ = {a, b}
- ℕ ∪ {-1} = {-1, 0, 1, 2, ...}

### Properties

- **Commutative**: A ∪ B = B ∪ A
- **Associative**: (A ∪ B) ∪ C = A ∪ (B ∪ C)
- **Idempotent**: A ∪ A = A
- **Identity**: A ∪ ∅ = A
- **Absorption**: A ∪ (A ∩ B) = A

## Intersection (∩)

The **intersection** of sets A and B, written A ∩ B, is the set of all elements in both A and B.

**Definition**: A ∩ B = {x | x ∈ A ∧ x ∈ B}

### Examples

- {1, 2, 3} ∩ {2, 3, 4} = {2, 3}
- {a, b} ∩ {c, d} = ∅
- ℤ ∩ ℚ = ℚ (integers are rational numbers)

### Properties

- **Commutative**: A ∩ B = B ∩ A
- **Associative**: (A ∩ B) ∩ C = A ∩ (B ∩ C)
- **Idempotent**: A ∩ A = A
- **Identity**: A ∩ A = A
- **Absorption**: A ∩ (A ∪ B) = A

### Disjoint Sets

If A ∩ B = ∅, the sets are **disjoint** (have no common elements).

## Difference (\)

The **difference** (or **complement relative to**) of B from A, written A \ B or A − B, is the set of all elements in A but not in B.

**Definition**: A \ B = {x | x ∈ A ∧ x ∉ B}

### Examples

- {1, 2, 3} \ {2, 4} = {1, 3}
- {a, b, c} \ {a, b, c} = ∅
- ℝ \ ℚ = irrational numbers

### Properties

- **A \ A = ∅**
- **A \ ∅ = A**
- **∅ \ A = ∅**
- **Not commutative**: A \ B ≠ B \ A (generally)
- **Not associative**: (A \ B) \ C ≠ A \ (B \ C) (generally)

## Complement (^c)

The **complement** of A (relative to universal set U), written A^c or A', is the set of all elements in U but not in A.

**Definition**: A^c = {x ∈ U | x ∉ A} = U \ A

### Examples (U = {1, 2, 3, 4, 5})

- {1, 2}^c = {3, 4, 5}
- {1, 2, 3, 4, 5}^c = ∅
- ∅^c = {1, 2, 3, 4, 5}

### Properties

- **(A^c)^c = A** (double complement)
- **A ∪ A^c = U** (complement law)
- **A ∩ A^c = ∅**
- **U^c = ∅** and **∅^c = U**

## De Morgan's Laws

For any sets A and B:

- **(A ∪ B)^c = A^c ∩ B^c** — complement of union is intersection of complements
- **(A ∩ B)^c = A^c ∪ B^c** — complement of intersection is union of complements

### Example

Let U = {1, 2, 3, 4, 5}, A = {1, 2}, B = {2, 3}

- (A ∪ B)^c = {1, 2, 3}^c = {4, 5}
- A^c ∩ B^c = {3, 4, 5} ∩ {1, 4, 5} = {4, 5} ✓

## Distributive Laws

- **Union distributes over intersection**: A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
- **Intersection distributes over union**: A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)

## Symmetric Difference (Δ)

The **symmetric difference** of A and B, written A Δ B, is the set of elements in exactly one of A or B.

**Definition**: A Δ B = (A \ B) ∪ (B \ A) = (A ∪ B) \ (A ∩ B)

### Example

- {1, 2, 3} Δ {2, 3, 4} = {1, 4}

## Generalized Operations

For collections {A₁, A₂, ..., Aₙ}:

- **Union**: ⋃ᵢ₌₁ⁿ Aᵢ = A₁ ∪ A₂ ∪ ... ∪ Aₙ
- **Intersection**: ⋂ᵢ₌₁ⁿ Aᵢ = A₁ ∩ A₂ ∩ ... ∩ Aₙ

These extend naturally to infinite collections as well.

## Summary Table

| Operation | Definition | Notation |
|-----------|-----------|----------|
| Union | Elements in A or B | A ∪ B |
| Intersection | Elements in both A and B | A ∩ B |
| Difference | Elements in A but not B | A \ B |
| Complement | Elements not in A | A^c |
| Symmetric Diff. | Elements in exactly one | A Δ B |
