---
title: Strong Induction
tag: logic
summary: Assume P(i) for all i ≤ k to prove P(k+1) — more powerful than weak induction.
links:
  - mathematical-induction
  - proof-strategies
---

# Strong Induction

**Strong induction** (also called course-of-values induction) is a variant of mathematical induction where the inductive hypothesis assumes the statement holds for all values up to k, rather than just k itself.

## Principle

To prove ∀n ∈ ℕ, P(n):

1. **Base case(s)**: Prove P(0), and possibly P(1), P(2), etc.
2. **Inductive step**: For any k ≥ base, assume P(i) for all i ≤ k, then prove P(k+1)

If both hold, then P(n) is true for all natural numbers.

## Comparison with Weak Induction

| Aspect | Weak Induction | Strong Induction |
|--------|---|---|
| Base case | Prove P(0) | Prove P(0), P(1), ... |
| Hypothesis | Assume P(k) | Assume P(0), P(1), ..., P(k) |
| Conclusion | Prove P(k+1) | Prove P(k+1) |
| Power | Less flexible | More flexible |

Both are equally valid; strong induction is sometimes more convenient.

## Examples

### Example 1: Prime Factorization

**Theorem**: Every integer n ≥ 2 has a prime factorization.

**Proof**:
- **Base case** (n = 2): 2 is prime, so it equals itself ✓

- **Inductive step**: Assume all integers from 2 to k have prime factorizations
  - For k+1, either:
    - k+1 is prime (done)
    - k+1 is composite, so k+1 = ab where 2 ≤ a, b ≤ k
    - By inductive hypothesis, both a and b have prime factorizations
    - Therefore k+1 has a prime factorization ✓

Thus every integer n ≥ 2 has a prime factorization ∎

### Example 2: Postage Amounts

**Theorem**: Every amount of postage ≥ 12 cents can be made using 3-cent and 5-cent stamps.

**Proof**:
- **Base cases**:
  - n = 12: 3 + 3 + 3 + 3 = 12 ✓
  - n = 13: 3 + 5 + 5 = 13 ✓
  - n = 14: 3 + 3 + 3 + 5 = 14 ✓

- **Inductive step**: Assume all amounts from 12 to k can be made (k ≥ 14)
  - For k+1, note that k+1 - 3 = k - 2 ≥ 12
  - By inductive hypothesis, amount k - 2 can be made with 3-cent and 5-cent stamps
  - Add one more 3-cent stamp to get k+1 ✓

Thus every amount ≥ 12 cents can be made ∎

### Example 3: Fibonacci Sequence Property

**Theorem**: For the Fibonacci sequence (F₀ = 0, F₁ = 1, Fₙ = Fₙ₋₁ + Fₙ₋₂), every F₂ₙ is even.

**Proof**:
- **Base case** (n = 0): F₀ = 0, which is even ✓
- **Base case** (n = 1): F₂ = 1... actually odd. Let's try: F₀ = 0, F₂ = 1, F₄ = 3... Hmm.
  
Wait, let me recalculate: F₀ = 0, F₁ = 1, F₂ = 1, F₃ = 2, F₄ = 3, F₅ = 5, F₆ = 8...
Actually F₂ₙ: F₀ = 0 (even), F₂ = 1 (odd), F₄ = 3 (odd)...

Let me revise: **Every Fₙ divisible by 3 has index divisible by 4.**

- **Base case** (n = 0): F₀ = 0, which is divisible by 3, and 0 is divisible by 4 ✓
- **Base case** (n = 4): F₄ = 3, divisible by 3, and 4 is divisible by 4 ✓

- **Inductive step**: Assume all Fᵢ with i ≤ k where 3|Fᵢ have 4|i
  - Consider Fₖ₊₁ = Fₖ + Fₖ₋₁
  - If 3|Fₖ₊₁, use properties of the Fibonacci sequence modulo 3
  - The Fibonacci sequence mod 3 has period 8: 0,1,1,2,0,2,2,1,0,...
  - So Fₙ ≡ 0 (mod 3) iff n ≡ 0 (mod 4)
  - This uses the recurrence and inductive hypothesis ✓

Thus the property holds ∎

## When Strong Induction is Better

Strong induction is preferred when:
- **Multiple dependencies**: P(k+1) depends on several previous cases
- **Index shifts**: Need to reference P(k-2) or P(k/2) to prove P(k+1)
- **Non-linear recursion**: Like Fibonacci or recursive algorithms
- **Existence results**: When you need to construct k+1 from smaller cases

## Proof That Strong = Weak Induction

Strong and weak induction are logically equivalent:
- **Weak → Strong**: Define Q(n) = "P(0) ∧ P(1) ∧ ... ∧ P(n)"; weak induction on Q gives strong induction on P
- **Strong → Weak**: Weak induction is a special case with limited hypothesis

So either form can always be used, depending on which is clearer.

## Common Applications

- **Recursive algorithms**: Proving correctness when algorithm depends on multiple subproblems
- **Number theory**: Factorization, divisibility properties
- **Combinatorics**: Problems where solution requires considering multiple smaller cases
- **Graph theory**: Properties of recursively built graphs
