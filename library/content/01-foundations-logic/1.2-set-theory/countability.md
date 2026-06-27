---
title: Countability
tag: set-theory
summary: Countable vs. uncountable sets; enumeration; Cantor's diagonal argument; ℵ₀ and continuum.
links:
  - finite-infinite-sets
  - cantors-theorem
  - cardinal-arithmetic
---

# Countability

A set is **countable** if it is finite or can be put in one-to-one correspondence with the natural numbers.

## Definition

A set A is countable if there exists an injection f: A → ℕ (or equivalently, a surjection ℕ → A).

For infinite sets specifically:
- **Countably infinite**: bijection with ℕ
- **Countable**: finite or countably infinite

## Enumeration

Countable sets can be **enumerated**: listed as a₀, a₁, a₂, a₃, ... (finite lists end; infinite lists go on forever).

### Examples of Countable Sets

**Finite sets**: {1, 2, 3}, {red, green, blue}, ∅

**Countably infinite sets**:
- ℕ = {0, 1, 2, 3, ...} — enumeration is obvious
- ℤ = {0, 1, -1, 2, -2, 3, -3, ...} — enumerate as: 0, ±1, ±2, ±3, ...
- ℚ = rationals — can be enumerated (Cantor's diagonal argument)
- ℕ × ℕ — pairs (i,j) can be enumerated by diagonals

## Diagonal Enumeration of ℕ × ℕ

List all pairs (m, n) by diagonals:

```
(0,0)
(0,1) (1,0)
(0,2) (1,1) (2,0)
(0,3) (1,2) (2,1) (3,0)
...
```

Flattened: (0,0), (0,1), (1,0), (0,2), (1,1), (2,0), ...

This establishes a bijection with ℕ.

## Cantor's Enumeration of ℚ

Rationals can be enumerated using a modified diagonal argument:

1. Create a grid of all fractions p/q (p ∈ ℤ, q ∈ ℕ⁺)
2. Enumerate by diagonals, skipping duplicates (like 2/2 = 1/1)
3. Each rational appears exactly once

Therefore, |ℚ| = ℵ₀ (countably infinite).

## Properties of Countable Sets

### Closed Under...

1. **Finite unions**: If A, B are countable, so is A ∪ B
2. **Countable unions**: If {Aᵢ | i ∈ ℕ} are countable, so is ⋃ᵢ Aᵢ
3. **Cartesian products (countable)**: If A, B are countable, so is A × B
   - But: A × B might be countable even if A is uncountable!
4. **Subsets**: Any subset of a countable set is countable
5. **Image under function**: If f: A → B and A is countable, then f(A) is countable

### Proof Technique

To show a set A is countable:
1. Find an enumeration a₀, a₁, a₂, ...
2. Or find an injection f: A → ℕ
3. Or prove A is the countable union of countable sets

## Examples

### Example 1: Finite Strings Over Finite Alphabet

Alphabet = {a, b, c}

- All finite strings can be enumerated: ε, a, b, c, aa, ab, ac, ba, bb, bc, ca, cb, cc, aaa, ...
- Order by length, then lexicographically within each length
- Result: countable set

**Application**: Formal language theory, programming languages

### Example 2: Algebraic Numbers

**Algebraic numbers**: solutions to polynomial equations with integer coefficients

- Polynomials with integer coefficients: countable (finite strings of digits)
- Each polynomial has finitely many roots
- Union of countably many finite sets: countable

Therefore, the set of algebraic numbers is countable.

### Example 3: ℚ[x] (Polynomials Over Rationals)

Polynomials with rational coefficients:
- Can encode as finite sequences of rationals
- Countable union of countable sets of degree-n polynomials
- Result: countable

## Uncountable Sets

A set is **uncountable** if it is not countable (infinite but not bijective with ℕ).

### Examples

- **ℝ** (real numbers) — uncountable (Cantor's diagonal argument)
- **[0,1]** (unit interval) — uncountable
- **P(ℕ)** (power set of naturals) — uncountable
- **Irrational numbers** — uncountable

### Theorem (Cantor's Diagonal Argument)

ℝ is uncountable:

1. Assume ℝ is countable, listed as r₀, r₁, r₂, ...
2. Each rᵢ has a decimal expansion: rᵢ = 0.dᵢ₀dᵢ₁dᵢ₂...
3. Construct a new number x = 0.x₀x₁x₂... where xᵢ ≠ dᵢᵢ (diagonals differ)
4. Then x ≠ rᵢ for all i (they differ in the i-th decimal place)
5. But x should be in our enumeration — **contradiction!**
6. Therefore, ℝ is uncountable.

## Implications

### Computability Theory
- Countable: can be listed/enumerated by an algorithm
- Uncountable: cannot be fully enumerated; "most" elements are unreachable computationally

### Measure Theory
- Countable sets have measure zero (in Lebesgue measure)
- "Almost all" reals are irrational (since irrationals are uncountable)

## Comparing Infinities

| Set | Cardinality | Type |
|-----|-------------|------|
| ℕ, ℤ, ℚ | ℵ₀ | Countable |
| ℝ, [0,1], ℤℝ | c = 2^ℵ₀ | Uncountable |
| P(ℝ) | 2^c | More uncountable |
| All sets | ? (continuum hypothesis) | Possibly more hierarchies |

## Key Takeaway

Countability is a fundamental dividing line in mathematics:
- **Countable**: Can be enumerated (even if infinitely)
- **Uncountable**: Cannot be enumerated; requires different techniques (limits, integrals, not infinite sums)
