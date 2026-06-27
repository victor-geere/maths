---
title: Partial Orders
tag: set-theory
summary: Reflexive, antisymmetric, transitive relations; posets with comparability and Hasse diagrams.
links:
  - relations
  - equivalence-relations
---

# Partial Orders

A **partial order** on a set A is a relation that is reflexive, antisymmetric, and transitive.

## Definition

R ⊆ A × A is a partial order if:
1. **Reflexive**: ∀a ∈ A, (a, a) ∈ R
2. **Antisymmetric**: ∀a, b ∈ A, (a, b) ∈ R ∧ (b, a) ∈ R ⟹ a = b
3. **Transitive**: ∀a, b, c ∈ A, (a, b) ∈ R ∧ (b, c) ∈ R ⟹ (a, c) ∈ R

The pair (A, R) is called a **partially ordered set** or **poset**.

## Notation

For partial orders, we use **≤** or **⪯** instead of R.

**a ≤ b** means (a, b) is in the partial order.

## Examples

### Example 1: Standard Ordering
- Set: ℝ with relation ≤
- Reflexive: a ≤ a ✓
- Antisymmetric: if a ≤ b and b ≤ a then a = b ✓
- Transitive: if a ≤ b and b ≤ c then a ≤ c ✓

### Example 2: Subset Ordering
- Set: P(S) (power set) with relation ⊆
- Reflexive: A ⊆ A ✓
- Antisymmetric: if A ⊆ B and B ⊆ A then A = B ✓
- Transitive: if A ⊆ B and B ⊆ C then A ⊆ C ✓

### Example 3: Divisibility
- Set: ℕ with relation |
- Define a | b if b is divisible by a (i.e., ∃k, b = ka)
- Reflexive: a | a ✓
- Antisymmetric: if a | b and b | a then a = b ✓
- Transitive: if a | b and b | c then a | c ✓

## Comparable and Incomparable Elements

In poset (A, ≤):
- **a and b are comparable** if a ≤ b or b ≤ a
- **a and b are incomparable** if neither a ≤ b nor b ≤ a (denoted a ∥ b)

### Example

In (ℕ, |):
- 2 and 3 are incomparable: 2 ∤ 3 and 3 ∤ 2
- 2 and 4 are comparable: 2 | 4
- 3 and 6 are comparable: 3 | 6

In (P({1, 2, 3}), ⊆):
- {1} and {2} are incomparable
- {1} and {1, 2} are comparable

## Total (Linear) Order

A partial order ≤ on A is a **total order** (or **linear order**) if every two elements are comparable:

**∀a, b ∈ A, a ≤ b ∨ b ≤ a**

### Examples of Total Orders

- (ℝ, ≤) — real numbers with standard order
- (ℕ, ≤) — natural numbers
- (Strings, lexicographic order)

### Non-Total Partial Order

- (P({1, 2}), ⊆): {1} and {2} are incomparable, so not total
- (ℕ, |): 2 and 3 are incomparable, so not total

## Special Elements

For subset S ⊆ A in poset (A, ≤):

### Maximum and Minimum

- **Maximum of S**: m ∈ S such that ∀s ∈ S, s ≤ m
- **Minimum of S**: m ∈ S such that ∀s ∈ S, m ≤ s

Maximum/minimum may not exist.

### Maximal and Minimal

- **Maximal element of S**: m ∈ S such that ∀s ∈ S, if m ≤ s then m = s (no larger element in S)
- **Minimal element of S**: m ∈ S such that ∀s ∈ S, if s ≤ m then s = m (no smaller element in S)

Every maximum is maximal, but not conversely.

### Example

S = {2, 3, 6} under divisibility (|):
- 6 is maximum: 2 | 6 and 3 | 6
- 2 is minimal: 2 | 2 (and nothing smaller divides 2 except 1, not in S)
- No element is maximal above 6 (since 6 doesn't divide anything else in S)

## Hasse Diagrams

A **Hasse diagram** visualizes a finite poset by:
1. Drawing elements as nodes
2. Drawing edges upward from a to b if a < b and no c has a < c < b

### Example: Divisibility on {1, 2, 3, 4, 6, 12}

```
        12
       /  \
      4    6
      |    |
      2    3
       \  /
        1
```

Edges go upward for the divisibility order.

## Bounds

For subset S ⊆ A in poset (A, ≤):

- **Upper bound**: u ∈ A such that ∀s ∈ S, s ≤ u
- **Lower bound**: l ∈ A such that ∀l ∈ L, l ≤ s
- **Supremum (lub)**: least upper bound
- **Infimum (glb)**: greatest lower bound

These may not exist in arbitrary posets.

## Complete Partial Orders

A poset is **complete** if every non-empty subset has both supremum and infimum.

- (ℝ, ≤) with added ±∞ is complete
- (ℕ, |) is not complete (e.g., {2, 3} has no supremum)

## Key Facts

- Partial order generalizes standard ordering
- Not all pairs of elements need be comparable
- Divisibility is an important partial order in number theory
- Subset containment is a fundamental partial order
- Posets are visualized with Hasse diagrams
