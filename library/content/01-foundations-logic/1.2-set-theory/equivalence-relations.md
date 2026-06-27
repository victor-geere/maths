---
title: Equivalence Relations
tag: set-theory
summary: Reflexive, symmetric, transitive relations partitioning sets into equivalence classes.
links:
  - relations
  - partial-orders
---

# Equivalence Relations

An **equivalence relation** on a set A is a relation that is reflexive, symmetric, and transitive.

## Definition

R ⊆ A × A is an equivalence relation if:
1. **Reflexive**: ∀a ∈ A, (a, a) ∈ R
2. **Symmetric**: ∀a, b ∈ A, (a, b) ∈ R ⟹ (b, a) ∈ R
3. **Transitive**: ∀a, b, c ∈ A, (a, b) ∈ R ∧ (b, c) ∈ R ⟹ (a, c) ∈ R

## Notation

If R is an equivalence relation, we often write **a ~ b** or **a ≡ b** instead of (a, b) ∈ R.

## Examples

### Example 1: Equality
- Relation: a = b
- Reflexive: a = a ✓
- Symmetric: if a = b then b = a ✓
- Transitive: if a = b and b = c then a = c ✓

### Example 2: Congruence Modulo n
For n ∈ ℕ, define a ≡ b (mod n) if n | (a - b).

- Reflexive: n | 0, so a ≡ a (mod n) ✓
- Symmetric: if n | (a - b) then n | (b - a) ✓
- Transitive: if n | (a - b) and n | (b - c) then n | ((a - b) + (b - c)) = (a - c) ✓

### Example 3: Similar Triangles
Define triangles T₁ ~ T₂ if they have the same angles.

- Reflexive: a triangle has the same angles as itself ✓
- Symmetric: if T₁ has the same angles as T₂, then T₂ has the same as T₁ ✓
- Transitive: if T₁, T₂ have the same angles and T₂, T₃ have the same angles, then T₁, T₃ have the same ✓

### Example 4: Have the Same Cardinality
For sets A ~ B if |A| = |B|.

- Reflexive: |A| = |A| ✓
- Symmetric: |A| = |B| ⟹ |B| = |A| ✓
- Transitive: |A| = |B| ∧ |B| = |C| ⟹ |A| = |C| ✓

## Equivalence Classes

Given an equivalence relation ~ on A and element a ∈ A, the **equivalence class** of a is:

**[a] = {x ∈ A | x ~ a}**

The equivalence class contains all elements equivalent to a.

### Example 1: Modular Arithmetic
For ≡ (mod 3) on ℤ:
- [0] = {..., -6, -3, 0, 3, 6, ...} (multiples of 3)
- [1] = {..., -5, -2, 1, 4, 7, ...} (numbers leaving remainder 1)
- [2] = {..., -4, -1, 2, 5, 8, ...} (numbers leaving remainder 2)

### Properties of Equivalence Classes

1. **a ∈ [a]** — each element is in its own class
2. **a ~ b ⟺ [a] = [b]** — equivalent elements have the same class
3. **a ≁ b ⟹ [a] ∩ [b] = ∅** — non-equivalent elements have disjoint classes
4. **⋃_{a∈A} [a] = A** — all classes cover A

## Partitions

A **partition** of A is a collection of non-empty, pairwise disjoint subsets whose union is A.

### Fundamental Theorem

An equivalence relation on A determines a unique partition of A into equivalence classes, and conversely, every partition of A determines a unique equivalence relation.

### Example

The equivalence relation ≡ (mod 3) on ℤ partitions ℤ into 3 equivalence classes: [0], [1], [2].

## Quotient Sets

The **quotient set** or **quotient space** A/~ is the set of all equivalence classes:

**A/~ = {[a] | a ∈ A}**

### Example

ℤ/3 (read "Z modulo 3") = {[0], [1], [2]}

This is formally equivalent to ℤ_3 = {0, 1, 2} with arithmetic operations.

### Cardinality

For finite A and equivalence relation ~:
- If all equivalence classes have the same size k
- And there are m equivalence classes
- Then |A| = m · k

Example: ℤ/n has exactly n equivalence classes, each infinite.

## Function Well-Definedness

Equivalence relations are crucial for defining functions on quotient sets. A function f: A/~ → B is **well-defined** if:

Whenever [a] = [b], we have f([a]) = f([b]).

This ensures the function doesn't depend on the representative chosen.

## Common Equivalence Relations

| Relation | Set | Equivalence Classes |
|----------|-----|-------------------|
| = | Any set A | Singletons {a} |
| ≡ (mod n) | ℤ | n residue classes [0], [1], ..., [n-1] |
| ~ (similarity) | Triangles | Classes of similar triangles |
| ≈ (isomorphism) | Graphs | Classes of isomorphic graphs |
| ~ (homotopy) | Spaces | Homotopy classes of paths |

## Key Facts

- Equivalence relations partition their domain
- Each partition corresponds to an equivalence relation
- Equivalence classes are non-overlapping and exhaustive
- Functions on equivalence classes must be well-defined
