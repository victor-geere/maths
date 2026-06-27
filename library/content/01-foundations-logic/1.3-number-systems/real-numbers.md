---
title: Real Numbers & Completeness
tag: analysis
summary: Complete ordered field ℝ — Cauchy sequences, Dedekind cuts, foundation of analysis and calculus.
links:
  - rationals
  - countability
  - cantors-theorem
---

# Real Numbers & Completeness

The **real numbers** ℝ are an ordered field that is **complete**, meaning every non-empty bounded subset has a least upper bound.

## Construction from Rationals

### Dedekind Cuts

A **Dedekind cut** partitions ℚ into two sets (A, B) such that:
1. A ∪ B = ℚ
2. A ≠ ∅ and B ≠ ∅
3. Every element of A is less than every element of B
4. A has no maximum (is "open at the top")

Each cut represents a real number (rational or irrational).

**Example cuts**:
- Cut for √2: A = {q ∈ ℚ | q < 0 or q² < 2}, B = {q ∈ ℚ | q > 0 and q² ≥ 2}
- Cut for 3: A = {q ∈ ℚ | q ≤ 3}, B = {q ∈ ℚ | q > 3}

### Cauchy Sequences

Alternatively, real numbers are equivalence classes of Cauchy sequences of rationals.

**Cauchy sequence**: (aₙ) where ∀ε > 0, ∃N such that |aₙ - aₘ| < ε for all n, m > N.

Two sequences are equivalent if their difference converges to 0.

**Example**: 3.1, 3.14, 3.141, 3.1415, ... represents π.

## Properties

### Algebraic Structure

ℝ is a **field** under addition and multiplication:
- Closed under +, −, ·, ÷ (÷ nonzero)
- Associative, commutative, distributive
- Additive identity: 0; additive inverses: −x
- Multiplicative identity: 1; multiplicative inverses: 1/x (x ≠ 0)

### Ordering

ℝ is an **ordered field**:
- Compatible ordering: if a < b and c ∈ ℝ, then a + c < b + c
- If a < b and c > 0, then ac < bc
- Transitive, antisymmetric, total

### Completeness (The Key Property)

**Completeness Axiom**: Every non-empty subset of ℝ that is bounded above has a least upper bound (supremum).

This is the crucial property that distinguishes ℝ from ℚ.

**Consequence**: The limit of any Cauchy sequence of real numbers exists in ℝ.

## Infinite Decimal Expansions

Every real number has a unique infinite decimal expansion:

x = ±(d₀.d₁d₂d₃...)

where dᵢ ∈ {0, 1, 2, ..., 9}

(Excluding trailing 9s: 0.999... = 1.000...)

### Rational vs. Irrational

- **Rational**: terminating or eventually repeating decimal
  - 1/3 = 0.333...
  - 1/4 = 0.25000...
  
- **Irrational**: non-repeating, non-terminating
  - √2 ≈ 1.41421356...
  - π ≈ 3.14159265...
  - e ≈ 2.71828182...

## Subsets of ℝ

### Intervals

**Bounded intervals**:
- [a, b] = {x | a ≤ x ≤ b} (closed)
- (a, b) = {x | a < x < b} (open)
- [a, b) = {x | a ≤ x < b} (half-open)

**Unbounded intervals**:
- [a, ∞) = {x | x ≥ a}
- (-∞, b] = {x | x ≤ b}
- ℝ = (-∞, ∞)

### Important Subsets

- **Algebraic numbers**: roots of polynomials with rational coefficients (countable, includes ℚ)
- **Transcendental numbers**: not algebraic (uncountable; examples: π, e)
- **Irrational numbers**: not rational (uncountable)

## Cardinality

ℝ is **uncountably infinite**: |ℝ| = c = 2^ℵ₀

**Proof** (Cantor's diagonal argument): 
- Assume ℝ is countable, listed as r₁, r₂, r₃, ...
- Each rᵢ has a decimal expansion: rᵢ = 0.dᵢ₁dᵢ₂dᵢ₃...
- Define x = 0.x₁x₂x₃... where xᵢ ≠ dᵢᵢ
- Then x differs from each rᵢ in the i-th decimal place
- But x should be in the enumeration — **contradiction!**
- Therefore ℝ is uncountable.

## Topology

### Open and Closed Sets

- **Open set**: Every point has a neighborhood entirely in the set
  - Open intervals (a, b) are open
  - ℝ is open
  
- **Closed set**: Complement is open
  - Closed intervals [a, b] are closed
  - ∅ and ℝ are both open and closed

### Compactness

A set is **compact** if every open cover has a finite subcover.

In ℝ: A set is compact iff it is closed and bounded.

**Examples**: [0, 1] is compact; (0, 1), ℝ are not compact.

## Limits and Continuity

### Limit of a Sequence

(aₙ) converges to L if ∀ε > 0, ∃N such that |aₙ − L| < ε for all n > N.

**Uses completeness**: Cauchy sequence → limit exists

### Continuity

f: ℝ → ℝ is continuous at x if small changes in input cause small changes in output.

**Completeness ensures**: continuous images of compact sets are compact

## Comparison to ℚ

| Property | ℚ | ℝ |
|----------|---|---|
| Field | Yes | Yes |
| Ordered | Yes | Yes |
| Complete | No | Yes |
| Cardinality | ℵ₀ (countable) | c (uncountable) |
| Cauchy sequences | May not converge | Always converge |
| √2 exists | No | Yes |
| Completeness axiom | N/A | Core property |

## Key Theorems

### Bolzano-Weierstrass
Every bounded sequence in ℝ has a convergent subsequence.

(Uses completeness via supremum)

### Extreme Value Theorem
A continuous function on a compact set achieves its maximum and minimum.

### Intermediate Value Theorem
If f is continuous on [a, b] and f(a) < y < f(b), then ∃c ∈ (a, b) with f(c) = y.

All rely on ℝ's completeness.

## Relationship to Other Sets

- **ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ**
- **ℚ is dense in ℝ** (every real is a limit of rationals)
- **ℝ is the "natural home" for calculus** (limits, continuity, integrals)

## Key Facts

- Complete ordered field with unique up to isomorphism
- Every Cauchy sequence converges (unlike ℚ)
- Uncountably infinite (unlike ℚ, ℤ, ℕ)
- Contains √2, π, e (unlike ℚ)
- Least upper bound property essential for calculus
- Enables rigorous definitions of limits, derivatives, integrals
