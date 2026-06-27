---
title: Mathematical Induction
tag: logic
summary: Prove base case and inductive step to establish ∀n ∈ ℕ, P(n) — justified by Peano axioms.
links:
  - strong-induction
  - peano-axioms
  - proof-strategies
---

# Mathematical Induction

**Mathematical induction** is a proof technique for statements about natural numbers. It works by proving a base case and showing that if the statement holds for one number, it holds for the next.

## Principle

To prove ∀n ∈ ℕ, P(n):

1. **Base case**: Prove P(0) or P(1) (depending on domain)
2. **Inductive step**: For any k, prove that P(k) → P(k+1)

If both hold, then P(n) is true for all natural numbers n.

## Intuition

Imagine dominoes in a row. If:
- The first domino falls (base case)
- Each falling domino knocks over the next one (inductive step)

Then all dominoes will eventually fall.

## Examples

### Example 1: Sum Formula

**Theorem**: ∀n ∈ ℕ, 1 + 2 + 3 + ... + n = n(n+1)/2

**Proof**:
- **Base case** (n = 1): LHS = 1, RHS = 1(2)/2 = 1 ✓

- **Inductive step**: Assume the formula holds for k:
  - 1 + 2 + ... + k = k(k+1)/2
  - Then for k+1:
    - 1 + 2 + ... + k + (k+1) = k(k+1)/2 + (k+1)
    - = (k+1)[k/2 + 1]
    - = (k+1)(k+2)/2 ✓

Therefore the formula holds for all n ∈ ℕ ∎

### Example 2: Divisibility

**Theorem**: ∀n ∈ ℕ, 2ⁿ - 1 is odd

**Proof**:
- **Base case** (n = 1): 2¹ - 1 = 1, which is odd ✓

- **Inductive step**: Assume 2ᵏ - 1 is odd
  - Then 2ᵏ - 1 = 2m + 1 for some integer m
  - So 2ᵏ = 2m + 2
  - Then 2^(k+1) - 1 = 2 · 2ᵏ - 1 = 2(2m + 2) - 1 = 4m + 4 - 1 = 4m + 3 = 2(2m + 1) + 1
  - Which is odd ✓

Therefore 2ⁿ - 1 is odd for all n ∈ ℕ ∎

### Example 3: Inequality

**Theorem**: ∀n ∈ ℕ (n ≥ 3), 2ⁿ > n²

**Proof**:
- **Base case** (n = 3): 2³ = 8 > 9 is false... let's try n = 4
  - 2⁴ = 16 > 16 is false... let's try n = 5
  - 2⁵ = 32 > 25 ✓

- **Inductive step**: Assume 2ᵏ > k² for some k ≥ 5
  - We need to show 2^(k+1) > (k+1)²
  - We have 2^(k+1) = 2 · 2ᵏ > 2k² (by inductive hypothesis)
  - We need 2k² ≥ (k+1)² = k² + 2k + 1
  - This simplifies to k² ≥ 2k + 1, or k² - 2k - 1 ≥ 0
  - For k ≥ 5: 25 - 10 - 1 = 14 ≥ 0 ✓
  - And this inequality is preserved for larger k

Therefore 2ⁿ > n² for all n ≥ 5 ∎

## Variations

### Strong Induction

Assume P holds for all values up to k, not just k itself:

- Assume P(0), P(1), ..., P(k) all true
- Prove P(k+1)

Useful when P(k+1) depends on multiple previous cases.

**Example**: Proving every integer n ≥ 2 has a prime factorization

### Backwards Induction

Prove P(n) by assuming P(n+1) and working backwards. Less common but useful for certain problems.

### Induction on Recursive Structures

Extend induction to trees, lists, and other recursively defined structures.

## Common Mistakes

- **Forgetting the base case**: The base case is essential
- **Wrong base case**: Starting with n = 0 when the statement is about n ≥ 1
- **Incomplete inductive step**: Not carefully deriving P(k+1) from P(k)
- **Circular reasoning**: Using P(n) in the proof of the inductive step
- **Assuming what you need to prove**: In the inductive step, assume only P(k), not P(k+1)

## When to Use Induction

- Formulas with natural number parameters
- Properties of recursively defined sequences
- Statements about divisibility or remainders
- Statements about combinatorial counts
- Proofs involving recursive algorithms

## Non-Inductive Alternatives

For some statements, direct proof or other methods might be cleaner:
- Sum formulas: sometimes provable by telescoping
- Combinatorial identities: sometimes provable by bijection
- Divisibility: sometimes provable by modular arithmetic
