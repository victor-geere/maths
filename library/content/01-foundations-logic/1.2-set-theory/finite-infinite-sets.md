---
title: Finite & Infinite Sets
tag: set-theory
summary: Finite sets with cardinality n; countably and uncountably infinite sets; hierarchy of infinities.
links:
  - countability
  - cantors-theorem
  - cardinal-arithmetic
---

# Finite & Infinite Sets

## Finite Sets

A set A is **finite** if it has finitely many elements, i.e., |A| = n for some n ∈ ℕ.

### Cardinality of Finite Sets

The cardinality |A| is simply the count of elements.

Examples:
- |∅| = 0
- |{a, b, c}| = 3
- |{1, 2, 3, ..., n}| = n

### Properties

1. **Finite sets are well-ordered**: Any finite set can be arranged in a sequence
2. **Subsets of finite sets are finite**: If A is finite and B ⊆ A, then B is finite and |B| ≤ |A|
3. **Union of finite sets is finite**: If A and B are finite, so is A ∪ B
4. **Cartesian product is finite**: If A and B are finite, then |A × B| = |A| × |B|

## Infinite Sets

A set A is **infinite** if it is not finite, i.e., for all n ∈ ℕ, there exists a bijection to {1, 2, ..., n} that is not surjective.

Intuitively, an infinite set has "unboundedly many" elements.

### Examples

- ℕ = {0, 1, 2, 3, ...} — countably infinite
- ℤ = {..., -1, 0, 1, 2, ...} — countably infinite
- ℝ = all real numbers — uncountably infinite
- ℚ = all rational numbers — countably infinite
- The set of all functions f: ℕ → {0, 1} — uncountably infinite

## Infinite Cardinals

Since infinite sets can't be counted in the usual way, mathematicians use the language of bijections:

### Countably Infinite

A set A is **countably infinite** if there is a bijection between A and ℕ.

Notation: |A| = ℵ₀ (aleph-null)

**Examples**:
- ℤ is countably infinite: ..., -2, -1, 0, 1, 2, ... can be listed
  - Bijection: pairs (0, ±1, 1, ±2, 2, ±3, ...)
- ℚ is countably infinite (Cantor's diagonal argument)
- Even-valued functions ℕ → ℕ is countably infinite

### Uncountably Infinite

A set A is **uncountably infinite** if it is infinite but no bijection with ℕ exists.

Notation: |A| = c (the cardinality of the continuum) or 2^ℵ₀

**Examples**:
- ℝ is uncountably infinite (Cantor's diagonal argument)
- ℝ² = ℝ × ℝ is also uncountably infinite (but same cardinality as ℝ)
- P(ℕ) — the power set of ℕ — is uncountably infinite

## Countability

A set is **countable** if it is finite or countably infinite.

A set is **uncountable** if it is infinite but not countable.

| Category | Type | Example |
|----------|------|---------|
| Finite | n elements | {1, 2, 3} |
| Countably infinite | ℵ₀ elements | ℕ, ℤ, ℚ |
| Uncountable | Larger than ℵ₀ | ℝ, ℝ², P(ℕ) |

## Hierarchy of Infinities

Cantor proved that there are infinitely many different infinite cardinalities:

ℵ₀ < c < 2^c < ...

where:
- ℵ₀ = cardinality of ℕ
- c = cardinality of ℝ (also 2^ℵ₀)
- 2^c = cardinality of P(ℝ)

### Key Result: Cantor's Theorem

For any set A, |A| < |P(A)|.

This means:
- ℵ₀ < |P(ℕ)| = c
- c < |P(ℝ)|
- And this continues indefinitely

## Key Theorems

### Theorem (Infinite Divisibility)
If A is infinite and B is non-empty and finite, then |A| = |A × B|.

Explanation: Adding finitely many copies doesn't increase cardinality.

### Theorem (Countable Union)
The union of countably many countable sets is countable.

**Consequence**: ℚ = countable union of countable sets, so ℚ is countable.

### Theorem (Pigeonhole for Infinite)
If f: A → B where A is infinite and B is countable, then f⁻¹(b) is infinite for some b ∈ B.

## Fundamental Questions

### The Continuum Hypothesis

**CH**: Is there a set whose cardinality is strictly between ℵ₀ and c?

**Status**: 
- Cannot be proved or disproved from standard axioms (Gödel, Cohen)
- If we assume CH, there is no such set
- If we deny CH, such sets exist

## Practical Implications

- **Finite algorithms**: Guaranteed to terminate
- **Countable algorithms**: Can enumerate all cases (e.g., BFS on countable graphs)
- **Uncountable problems**: Cannot enumerate; require abstract methods

## Visual Comparison

```
|∅| = 0 < 1 = |{a}| < 2 = |{a,b}| < ... < ℵ₀ = |ℕ| < c = |ℝ| < 2^c < ...

0   1       2              Countable Infinity   Uncountable Infinities
```
