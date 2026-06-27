---
title: Sets & Notation
tag: set-theory
summary: Fundamental concepts—elements, membership, set-builder notation, and cardinality.
links:
  - subsets-power-sets
  - set-operations
  - cartesian-product
---

# Sets & Notation

A **set** is a collection of distinct objects called **elements** or **members**.

## Basic Notation

### Listing Elements
- S = {1, 2, 3} — set containing 1, 2, and 3
- S = {a, b, c} — set containing elements a, b, c
- {} or ∅ — the empty set (no elements)

### Set-Builder Notation
S = {x | condition on x} — set of all x satisfying the condition

Examples:
- {x | x ∈ ℕ and x < 5} = {0, 1, 2, 3, 4} (or {1, 2, 3, 4} if ℕ excludes 0)
- {x | x ∈ ℝ and x² < 4} = {x ∈ ℝ | -2 < x < 2}
- {2n | n ∈ ℤ} = {..., -4, -2, 0, 2, 4, ...} (even integers)

## Membership and Equality

### Element Membership
- x ∈ S — "x is in S" or "x belongs to S"
- x ∉ S — "x is not in S"

### Set Equality
S = T if and only if S and T have exactly the same elements.

**Example**: {1, 2, 3} = {3, 2, 1} (order doesn't matter)

## Common Sets

| Notation | Meaning |
|----------|---------|
| ∅ | Empty set |
| ℕ | Natural numbers {0, 1, 2, 3, ...} or {1, 2, 3, ...} |
| ℤ | Integers {..., -2, -1, 0, 1, 2, ...} |
| ℚ | Rational numbers {p/q \| p, q ∈ ℤ, q ≠ 0} |
| ℝ | Real numbers |
| ℂ | Complex numbers |
| [a, b] | Closed interval {x ∈ ℝ \| a ≤ x ≤ b} |
| (a, b) | Open interval {x ∈ ℝ \| a < x < b} |

## Cardinality

The **cardinality** of a set S, denoted |S| or #S, is the number of elements it contains.

Examples:
- |{1, 2, 3}| = 3
- |∅| = 0
- |ℕ| = ∞ (but see **Infinite Sets** for subtlety)

## Finite vs. Infinite Sets

- **Finite set**: Has finitely many elements
- **Infinite set**: Has infinitely many elements

## Singleton and Pairs

- **Singleton**: Set with exactly one element, e.g., {5}
- **Ordered pair**: (a, b) where order matters; (a, b) ≠ (b, a) unless a = b
- **Unordered pair**: {a, b}; same as {b, a}

## Set Operations (Preview)

Sets can be combined:
- **Union**: S ∪ T = all elements in S or T (or both)
- **Intersection**: S ∩ T = elements in both S and T
- **Complement**: S^c = elements not in S
- **Difference**: S \ T = elements in S but not in T

More details: see [[set-operations]]

## Important Principles

### Distinctness
Sets are unordered collections of distinct elements. {1, 1, 2} is the same as {1, 2}.

### Extensionality
Two sets are equal if they have the same elements, regardless of how they're described.

**Example**: {x ∈ ℤ | x² < 4} = {x ∈ ℤ | -2 ≤ x ≤ 1} both equal {-1, 0, 1}

### No Duplicates in Formal Sets
In formal set theory, each element appears once. Multisets allow repeated elements.

## Naïve Set Theory vs. Axiomatic

- **Naïve approach**: Think of sets as arbitrary collections (intuitive but has paradoxes)
- **Formal approach**: Use axioms (like ZFC) to avoid paradoxes like Russell's

Russell's Paradox: Let R = {x | x ∉ x}. Is R ∈ R?
- If R ∈ R, then by definition of R, R ∉ R (contradiction)
- If R ∉ R, then by definition of R, R ∈ R (contradiction)

Formal axioms ensure such self-referential sets don't exist.

## Notation Summary

| Notation | Meaning |
|----------|---------|
| x ∈ S | x is an element of S |
| x ∉ S | x is not an element of S |
| {x \| P(x)} | Set of all x satisfying property P |
| \|S\| | Cardinality of S |
| ∅ | Empty set |
| S = T | S and T have the same elements |
