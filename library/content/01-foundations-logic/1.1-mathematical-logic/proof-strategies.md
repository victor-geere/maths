---
title: Proof Strategies
tag: logic
summary: Techniques for proving different statement forms — direct, contrapositive, contradiction, induction, cases.
links:
  - direct-proof
  - proof-by-contradiction
  - mathematical-induction
  - strong-induction
---

# Proof Strategies

Proof strategies are techniques for constructing valid mathematical arguments. The choice of strategy depends on the form of the statement being proved.

## Universal Statements (∀x P(x))

### Direct Proof
Assume x is an arbitrary element of the domain and derive P(x).

**Example**: Prove ∀x ∈ ℤ, if x is even then x² is even.
- Let x be an arbitrary even integer
- Then x = 2k for some integer k
- So x² = (2k)² = 4k² = 2(2k²), which is even ✓

### Proof by Contrapositive
To prove P → Q, prove ¬Q → ¬P.

**Example**: Prove ∀n ∈ ℤ, if n² is even then n is even.
- Contrapositive: if n is odd, then n² is odd
- If n is odd, n = 2k + 1
- Then n² = (2k + 1)² = 4k² + 4k + 1 = 2(2k² + 2k) + 1, which is odd ✓

### Proof by Contradiction
Assume ¬P and derive a contradiction.

**Example**: Prove √2 is irrational.
- Assume √2 = p/q where p, q are integers in lowest terms
- Then 2q² = p², so p² is even, hence p is even
- Write p = 2m, then 2q² = 4m², so q² = 2m², making q² even, hence q even
- But then both p and q are even, contradicting lowest terms ✓

## Existential Statements (∃x P(x))

### Constructive Proof
Explicitly construct or provide a witness.

**Example**: Prove ∃x ∈ ℝ (x² - 3x + 2 = 0).
- Let x = 1
- Then 1 - 3 + 2 = 0 ✓

### Existential Proof by Cases
Show that one of several possibilities holds.

**Example**: Prove ∃x ∈ ℝ (x² = x).
- Case 1: x = 0 gives 0 = 0 ✓

## Conditional Statements (P → Q)

### Direct Proof
Assume P and derive Q.

### Proof by Cases
Partition the hypothesis and prove Q in each case.

**Example**: Prove ∀x ∈ ℤ, x² ≥ 0.
- Case 1: x ≥ 0, then x² ≥ 0
- Case 2: x < 0, then x² = (-x)² where -x > 0, so x² > 0 ≥ 0 ✓

## Special Techniques

### Mathematical Induction
For statements of the form ∀n ∈ ℕ P(n):
1. **Base case**: Prove P(0) or P(1)
2. **Inductive step**: Assume P(k) and prove P(k+1)

**Example**: Prove ∀n ∈ ℕ, 1 + 2 + ... + n = n(n+1)/2.
- Base: 1 = 1(2)/2 ✓
- Step: Assume sum up to k equals k(k+1)/2
- Then sum up to k+1 = k(k+1)/2 + (k+1) = (k+1)(k+2)/2 ✓

### Proof by Equivalence
Chain of bidirectional implications: A ↔ B ↔ C shows A, B, C are equivalent.

### Vacuous Truth
If P → Q and P is false, then P → Q is trivially true.

**Example**: "All unicorns have exactly one horn" — vacuously true since unicorns don't exist.

## Common Mistakes

- **Assuming what you need to prove** (circular reasoning)
- **Confusing implication direction** (proving Q → P instead of P → Q)
- **Mishandling quantifiers** (proving one example for a universal statement)
- **Overlooking cases** in proof by cases
- **Using incorrect logic in induction**

## Proof Organization

1. State what you're proving clearly
2. Identify the proof strategy
3. Present steps logically
4. Justify each major step
5. Explicitly state the conclusion
