---
title: Peano Axioms (Natural Numbers)
tag: number-theory
summary: Axiomatic foundation of ℕ — successor, injectivity, non-circularity, and mathematical induction.
links:
  - mathematical-induction
  - integers
  - rationals
---

# Peano Axioms (Natural Numbers)

The **Peano axioms** are a set of foundational axioms that characterize the natural numbers. They provide a rigorous definition of ℕ without relying on intuition or prior understanding.

## The Five Axioms

**Axiom 1** (Constant): There exists a natural number 0.

**Axiom 2** (Successor): Every natural number n has a successor, denoted S(n) or n+1.

**Axiom 3** (Injectivity): If S(n) = S(m), then n = m.
- Different numbers have different successors.

**Axiom 4** (Non-circularity): There is no natural number n such that S(n) = 0.
- 0 is not a successor of any number.

**Axiom 5** (Mathematical Induction): If a set K contains 0 and is closed under the successor operation (n ∈ K ⟹ S(n) ∈ K), then K contains all natural numbers.

## Building ℕ

From these axioms, we construct the natural numbers:

- 0 (by Axiom 1)
- S(0) = 1
- S(1) = S(S(0)) = 2
- S(2) = S(S(S(0))) = 3
- ...

This generates ℕ = {0, 1, 2, 3, ...}

## Operations on Natural Numbers

### Addition

Defined recursively:
- **Base case**: n + 0 = n
- **Recursive case**: n + S(m) = S(n + m)

**Example**: 2 + 3 = 2 + S(2) = S(2 + 2) = S(S(2 + 1)) = S(S(S(2 + 0))) = S(S(S(2))) = 5 ✓

### Multiplication

Defined recursively:
- **Base case**: n · 0 = 0
- **Recursive case**: n · S(m) = (n · m) + n

**Example**: 2 · 3 = 2 · S(2) = (2 · 2) + 2 = 4 + 2 = 6 ✓

### Exponentiation

Defined recursively:
- **Base case**: n^0 = 1
- **Recursive case**: n^S(m) = (n^m) · n

**Example**: 2^3 = 2^S(2) = (2^2) · 2 = 4 · 2 = 8 ✓

## Properties Derived from Axioms

### Associativity of Addition

(m + n) + k = m + (n + k)

Proof: By induction on k, using the definition of addition.

### Commutativity of Addition

m + n = n + m

Proof: By induction, establishing base cases and inductive steps.

### Distributivity

m · (n + k) = (m · n) + (m · k)

Proof: By induction using definitions and associativity/commutativity.

### Ordering

Define m < n (m precedes n) if there exists k ≠ 0 such that m + k = n.

Properties:
- Irreflexive: not (n < n)
- Transitive: if m < n and n < k, then m < k
- Total: for any m, n, exactly one of m < n, m = n, or n < m holds

## Consistency and Completeness

### Consistency

The Peano axioms are **consistent** if we can construct a model.

**Standard model**: ℕ = {0, 1, 2, 3, ...} with standard S, + satisfies all axioms.

### Categoricity

The Peano axioms are **categorical** for first-order logic with induction:
- All finite models (with induction interpreted classically) are isomorphic to {0, 1, ..., n}
- But second-order Peano axioms uniquely determine ℕ up to isomorphism

This means the axioms essentially pin down the natural numbers uniquely.

## Alternative Formulations

Some sources start with 1 instead of 0:

- **Axiom 1'**: There exists a natural number 1.
- **Axiom 4'**: No natural number has 1 as its successor.

This gives ℕ = {1, 2, 3, ...}

## Why Axioms?

Before Peano's axioms (19th century), mathematicians used natural numbers intuitively. The axioms provide:

1. **Rigor**: No ambiguity about what ℕ is
2. **Justification for induction**: Axiom 5 validates the inductive proof technique
3. **Foundation**: Enables construction of integers, rationals, reals as extensions
4. **Completeness**: All standard properties of ℕ follow from these axioms

## Beyond Natural Numbers

The Peano axioms form the foundation for building:

1. **Integers (ℤ)**: Add inverses of addition
2. **Rationals (ℚ)**: Add inverses of multiplication
3. **Reals (ℝ)**: Require additional axioms (completeness)
4. **Higher mathematics**: Built on this foundation

## Key Insight

The Peano axioms show that:
- Natural numbers need not be primitive concepts
- They can be precisely defined through logical axioms
- This recursive characterization justifies mathematical induction
- Foundation for all of arithmetic and mathematics

## See Also

- [[mathematical-induction]] — uses Axiom 5
- [[integers]] — extension of ℕ
- [[rationals]] — further extension
