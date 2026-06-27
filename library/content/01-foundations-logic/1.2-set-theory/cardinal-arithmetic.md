---
title: Cardinal Arithmetic
tag: set-theory
summary: Arithmetic operations on cardinalities — addition, multiplication, exponentiation of infinite cardinals.
links:
  - countability
  - cantors-theorem
  - finite-infinite-sets
---

# Cardinal Arithmetic

**Cardinal arithmetic** extends addition, multiplication, and exponentiation to infinite sets by defining operations on their cardinalities.

## Basic Definitions

For sets A and B with cardinalities κ = |A| and λ = |B|:

### Addition (κ + λ)

κ + λ = |A ∪ B| where A and B are disjoint.

Alternatively: κ + λ = |A ⊔ B| (disjoint union)

**Property**: The operation is well-defined (independent of choice of A and B)

### Multiplication (κ · λ)

κ · λ = |A × B|

### Exponentiation (κ^λ)

κ^λ = |A^B| where A^B is the set of all functions from B to A.

**Note**: |A^B| denotes the set of functions, not powers in the usual sense.

## Finite Cardinal Arithmetic

For finite cardinals (ordinary numbers):

- 3 + 2 = 5
- 3 · 2 = 6
- 2³ = 8

These follow standard arithmetic.

## Infinite Cardinal Arithmetic

### Addition with Infinity

For infinite cardinal ℵ and finite κ:

- ℵ₀ + n = ℵ₀ (add finite to countable → countable)
- ℵ₀ + ℵ₀ = ℵ₀ (union of two countable sets is countable)
- c + ℵ₀ = c (uncountable + countable = uncountable)

**Key insight**: Once infinite, adding finite numbers doesn't increase cardinality.

### Multiplication with Infinity

For infinite cardinal ℵ and finite κ ≥ 1:

- ℵ₀ · n = ℵ₀ (countable × finite = countable)
- ℵ₀ · ℵ₀ = ℵ₀ (countable × countable = countable)
- c · ℵ₀ = c (uncountable × countable = uncountable)
- c · c = c (uncountable × uncountable = uncountable)

**Key insight**: Countable × countable is still countable (e.g., ℚ and ℕ × ℕ)

### Exponentiation with Infinity

These operations often increase cardinality:

- 2^ℵ₀ = c (set of all subsets of ℕ has cardinality of continuum)
- ℵ₀^ℵ₀ = c (all sequences of natural numbers)
- c^ℵ₀ = c (functions from ℕ to ℝ... actually equal to c)
- c^c > c (functions from ℝ to ℝ is "larger" than c)

## Key Rules for Infinite Cardinals

If κ is an infinite cardinal and λ ≤ κ:

1. **κ + λ = κ** (adding ≤ cardinals doesn't grow)
2. **κ · λ = κ** if λ ≥ 1 (multiplying by ≤ cardinals doesn't grow)
3. **κ^n = κ** for finite n (finite exponents don't grow)
4. **2^κ > κ** (Cantor's theorem—exponentiation does grow)

## Examples

### Example 1: |ℤ| + |ℚ|

|ℤ| = ℵ₀, |ℚ| = ℵ₀

|ℤ| + |ℚ| = ℵ₀ + ℵ₀ = ℵ₀

Intuition: Union of two countable sets is countable.

### Example 2: |ℝ| · |ℕ|

|ℝ| = c, |ℕ| = ℵ₀

|ℝ| · |ℕ| = c · ℵ₀ = c

Intuition: ℝ × ℕ has same cardinality as ℝ (can be "folded" back into ℝ).

### Example 3: 2^|ℝ|

By Cantor's theorem:
|P(ℝ)| = 2^|ℝ| = 2^c > c

This set is strictly larger than the continuum.

## The Generalized Continuum Hypothesis (GCH)

**GCH**: For any infinite cardinal κ, there is no cardinal strictly between κ and 2^κ.

In other words: 2^κ is the "next" cardinal after κ.

**Status**: Independent of ZFC (Gödel, Cohen) — cannot be proved or disproved from standard axioms.

## Ordinal vs. Cardinal Arithmetic

- **Ordinal arithmetic**: concerns order structure (depends on ordering)
- **Cardinal arithmetic**: concerns only cardinality (symmetric and commutative)

Example:
- Ordinal: 1 + ω = ω, but ω + 1 = ω + 1 (not equal)
- Cardinal: |1| + |ω| = |ω| = |ω| + |1| (same result)

## Operations on the Aleph Hierarchy

For aleph numbers ℵₙ:

- ℵₙ + 1 = ℵₙ
- ℵₙ + ℵₙ = ℵₙ
- ℵₙ · ℵₙ = ℵₙ
- 2^ℵₙ > ℵₙ (but doesn't necessarily equal ℵ_{n+1} without GCH)

## Practical Implications

### Combinatorics and Counting

Infinite sets require cardinal arithmetic:
- "How many functions from ℕ to ℝ?" → c^ℵ₀
- "How many subsets of ℝ?" → 2^c
- "How many reals?" → c

### Computer Science

- Computable functions: ℵ₀ (finite descriptions)
- All functions ℕ → ℕ: 2^ℵ₀ > ℵ₀
- Most functions are uncomputable

## Key Facts

- Infinity + finite = infinity (same cardinality)
- Infinity × countable = infinity (depends on both cardinalities)
- 2^infinity is strictly larger
- GCH is unprovable; add it as an axiom if desired
- Cardinal arithmetic is commutative and associative (unlike ordinal arithmetic)
