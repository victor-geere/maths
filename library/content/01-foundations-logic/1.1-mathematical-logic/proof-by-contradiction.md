---
title: Proof by Contradiction
tag: logic
summary: Assume ¬P and derive a contradiction to prove P — reductio ad absurdum.
links:
  - proof-strategies
  - direct-proof
---

# Proof by Contradiction

**Proof by contradiction** (also called reductio ad absurdum) proves a statement by assuming its negation and deriving a contradiction.

## Principle

To prove statement P:
1. Assume ¬P (the negation of P)
2. Derive a contradiction from ¬P
3. Conclude that P must be true

This relies on the law of non-contradiction: a statement and its negation cannot both be true.

## Basic Examples

### Example 1: √2 is Irrational

**Theorem**: √2 is not a rational number.

**Proof**:
- Assume √2 is rational (negation of the claim)
- Then √2 = p/q where p, q are integers with no common factors
- Squaring: 2 = p²/q², so 2q² = p²
- This means p² is even, so p must be even (since the square of an odd number is odd)
- Let p = 2m, then 2q² = 4m², so q² = 2m²
- This means q² is even, so q must be even
- But now both p and q are even, contradicting that they have no common factors
- **Contradiction!** Therefore √2 is irrational ∎

### Example 2: There are Infinitely Many Primes

**Theorem**: There is no largest prime number.

**Proof**:
- Assume there is a largest prime p
- Consider N = 2 × 3 × 5 × 7 × ... × p + 1 (product of all primes up to p, plus 1)
- N is not divisible by any prime ≤ p (remainders are always 1)
- So either N is prime (contradicting p being largest) or N has a prime factor > p (also contradicting p being largest)
- **Contradiction!** Therefore there are infinitely many primes ∎

### Example 3: Irrational Number Subtraction

**Theorem**: If x is rational and y is irrational, then x - y is irrational.

**Proof**:
- Assume x - y is rational (where x is rational and y is irrational)
- Since x is rational and x - y is rational, their difference is:
  y = x - (x - y) = rational - rational = rational
- But this contradicts y being irrational
- **Contradiction!** Therefore x - y is irrational ∎

## Formal Structure

For statement P:

```
Assume ¬P
...
Derive Q and ¬Q (or equivalent contradiction)
...
Therefore P
```

## Proof by Contradiction vs. Contrapositive

These are related but different:

- **Contrapositive of P → Q**: Prove ¬Q → ¬P directly
- **Contradiction for P → Q**: Assume P ∧ ¬Q and derive a contradiction

They prove the same result but take different logical paths.

## Advantages

- **Powerful for negative statements**: "There does not exist..." or "X is not..."
- **Indirect reasoning**: Don't need to construct Q explicitly
- **Works when forward direction is obscure**: Sometimes easier to find contradiction than direct path
- **Elegant**: Many famous theorems use this approach

## Disadvantages

- **Non-constructive**: Doesn't tell you what the true statement is, only that negation is false
- **Can be lengthy**: Assuming the negation might lead to complex scenarios
- **Less intuitive**: Harder to understand than direct proofs for some readers
- **Proof verification**: More steps to check for errors

## Important Variations

### Proof by Contradiction + Cases

Assume negation, then show it leads to a contradiction in all cases.

**Example**: For any two real numbers, either x ≤ y or x > y.
- Assume neither holds
- Then x > y and x ≤ y simultaneously
- **Contradiction!**

### Vacuous Proof (Special Case)

When the hypothesis of P → Q is false, the implication is vacuously true:

**Example**: "All unicorns are blue" — true because no unicorns exist (the negation leads to contradiction with definition).

## When to Use Contradiction

- Proving negations: "X is not equal to Y"
- Proving existence with constraints: "There exists unique X such that..."
- Results that seem "extreme": "There is no smallest positive real number"
- When direct proof is unclear but contradiction is obvious
