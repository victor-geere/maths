---
title: Direct Proof
tag: logic
summary: Assume hypothesis P and logically derive conclusion Q to prove P → Q.
links:
  - proof-strategies
  - proof-by-contradiction
---

# Direct Proof

**Direct proof** is the most straightforward proof technique: to prove P → Q, assume P is true and derive Q.

## Structure

1. State the hypothesis P
2. Apply definitions, axioms, and known theorems
3. Perform logical deductions
4. Conclude that Q follows from P

## Basic Examples

### Example 1: Proving a Statement About Even Numbers

**Theorem**: If n is even, then n + 1 is odd.

**Proof**:
- Assume n is even
- By definition, n = 2k for some integer k
- Then n + 1 = 2k + 1
- By definition, 2k + 1 is odd (in the form 2m + 1 where m = k)
- Therefore n + 1 is odd ∎

### Example 2: Proving a Conditional Statement

**Theorem**: If x > 0, then x² + 1 > x.

**Proof**:
- Assume x > 0
- We want to show x² + 1 > x, equivalently x² - x + 1 > 0
- Complete the square: x² - x + 1 = (x - 1/2)² + 3/4
- Since (x - 1/2)² ≥ 0, we have x² - x + 1 ≥ 3/4 > 0
- Therefore x² + 1 > x ∎

## Multi-Step Direct Proofs

For more complex theorems, direct proofs often involve chaining implications.

### Example 3: Transitivity of Equality

**Theorem**: If a = b and b = c, then a = c.

**Proof**:
- Assume a = b and b = c
- Since a = b, we can substitute: a = c (by transitivity of equality)
- Therefore a = c ∎

### Example 4: Properties of Modular Arithmetic

**Theorem**: If a ≡ b (mod n) and c ≡ d (mod n), then a + c ≡ b + d (mod n).

**Proof**:
- Assume a ≡ b (mod n) and c ≡ d (mod n)
- By definition: n | (a - b) and n | (c - d)
- Then there exist integers k, m such that a - b = nk and c - d = nm
- Adding: (a - b) + (c - d) = nk + nm = n(k + m)
- This means (a + c) - (b + d) = n(k + m)
- Therefore n | ((a + c) - (b + d)), so a + c ≡ b + d (mod n) ∎

## Advantages and Disadvantages

### Advantages
- **Natural**: Follows the logical structure directly
- **Verifiable**: Each step can be checked independently
- **Clear**: Readers can follow the reasoning easily

### Disadvantages
- **May be difficult**: Sometimes the forward path to Q is not obvious
- **Dead ends**: You might explore promising avenues that don't lead to Q
- **Inefficient**: Might require many intermediate steps

## When Direct Proof Works Best

- **Simple statements**: P and Q have clear logical relationships
- **Constructive proofs**: When you can explicitly build or derive Q
- **Computational proofs**: When Q follows from calculations
- **Chain reasoning**: When you can use lemmas to bridge P and Q

## Tips for Direct Proofs

1. **Start with the hypothesis**: Explicitly state what you're assuming
2. **Use relevant definitions**: Unpack definitions to make properties explicit
3. **Work forward from P**: Apply logical rules to advance toward Q
4. **Keep Q in mind**: Periodically check if you can derive Q now
5. **Label key steps**: Make the logical progression clear

## Combination with Other Techniques

Direct proofs often combine with:
- **Proof by cases**: Direct proof within each case
- **Induction**: Direct proof in the inductive step
- **Lemmas**: Use direct proofs to establish helper results
