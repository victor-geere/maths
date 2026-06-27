---
title: Cantor's Theorem
tag: set-theory
summary: "|A| < |P(A)| — there is no largest infinity; infinite hierarchy of cardinals ℵ₀ < c < 2^c..."
links:
  - countability
  - finite-infinite-sets
  - cardinal-arithmetic
---

# Cantor's Theorem

**Cantor's Theorem** states that for any set A, the cardinality of A is strictly less than the cardinality of its power set P(A).

**Statement**: |A| < |P(A)|

This fundamental result implies there is no "largest" infinity—infinities form an infinite hierarchy.

## Proof

We prove by contradiction that there cannot be a surjection from A to P(A).

**Assume** f: A → P(A) is a function.

**Construct** the set: B = {a ∈ A | a ∉ f(a)}

This is the set of all elements that are not in their own image under f.

**Key observation**: B ⊆ A (B is a subset of A, so B ∈ P(A))

**Claim**: B is not in the range of f.

**Proof of claim**: Suppose f(b) = B for some b ∈ A. Then:
- **Case 1**: b ∈ B
  - By definition of B: b ∉ f(b)
  - But f(b) = B, so b ∉ B
  - **Contradiction!**
- **Case 2**: b ∉ B
  - Then b ∉ f(b) is false, so b ∈ f(b)
  - But f(b) = B, so b ∈ B
  - **Contradiction!**

Both cases lead to contradiction, so no b has f(b) = B.

**Conclusion**: f is not surjective onto P(A).

Since this holds for any function f: A → P(A), there is no surjection, and hence no bijection. Therefore, |A| < |P(A)|. ∎

## The Diagonal Set

The set B = {a ∈ A | a ∉ f(a)} is called the **diagonal set** or **Cantor's set**. It's constructed similarly to Cantor's diagonal argument for uncountability of ℝ.

## Implications

### Infinite Hierarchy of Cardinalities

For any set A:
- |A| < |P(A)| < |P(P(A))| < ...

Starting from ℕ:
- |ℕ| = ℵ₀
- |P(ℕ)| = 2^ℵ₀ = c (continuum)
- |P(P(ℕ))| = 2^c
- And this continues forever

### No Universal Set

There cannot be a "set of all sets" because:
- Any such set S would satisfy: |S| ≥ |A| for all A
- But then |S| = |S| < |P(S)| (by Cantor's theorem)
- This is a contradiction

This resolves **Russell's Paradox** in a fundamental way.

### Aleph Numbers

The infinite cardinals are denoted:
- ℵ₀ = |ℕ| (smallest infinite cardinal)
- ℵ₁ = |P(ℕ)| = c (if Continuum Hypothesis is true)
- ℵ₂, ℵ₃, ... (progressively larger infinities)

Cantor's theorem guarantees these form an infinite ascending chain.

## Applications

### Computability

In computability theory, Cantor's theorem explains why:
- Computable functions: countable (each algorithm is a finite string)
- All functions from ℕ → ℕ: uncountable
- Therefore: "most" functions are uncomputable

**Count**: ℵ₀ computable functions vs. 2^ℵ₀ total functions

### Measure Theory

Cantor's theorem suggests why uncountable sets have "more structure":
- Countable sets have Lebesgue measure 0
- Uncountable sets (like ℝ) can have positive measure
- The "typical" subset of ℝ is uncountable and has measure 0

### Logic and Set Theory

**Gödel's Incompleteness**: Related to infinities beyond what finite axioms can characterize

## Related Theorems

### Cantor-Schröder-Bernstein Theorem

If there are injections f: A → B and g: B → A, then there exists a bijection between A and B.

This allows us to compare cardinalities even without explicit bijections.

### Continuum Hypothesis (CH)

**Question**: Is there a set whose cardinality is strictly between ℵ₀ and c?

- If CH is true: ℵ₁ = c (no such set exists)
- If CH is false: such sets exist

Gödel (1938) and Cohen (1963) proved that CH is **independent** of ZFC set theory—it can neither be proved nor disproved from standard axioms.

## Historical Context

Cantor's work on infinite sets was revolutionary but also controversial:

- Unveiled in the late 1800s
- Some mathematicians found it philosophically troubling
- Poincaré called it "a beautiful but dangerous principle"
- Now considered fundamental to modern mathematics

## Key Insight

**There is no largest infinity.**

For any infinite set A, we can always construct P(A), which is "strictly larger." This creates an infinite hierarchy of infinities, providing a rich mathematical structure far beyond simple "countable vs. uncountable."
