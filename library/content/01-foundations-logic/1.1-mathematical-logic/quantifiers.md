---
title: Quantifiers (∀, ∃)
tag: logic
summary: Universal (∀) and existential (∃) quantifiers for binding variables in logical formulas.
links:
  - first-order-logic
  - proof-strategies
---

# Quantifiers (∀, ∃)

## Universal Quantifier (∀)

The **universal quantifier** ∀ means "for all" or "for every".

**Notation**: ∀x P(x) — "for all x, P(x) is true"

### Interpretation

∀x P(x) is true if and only if P(x) is true for every element in the domain.

### Examples

- ∀x ∈ ℝ, x² ≥ 0 (true: squares are non-negative)
- ∀x ∈ ℕ, x > 0 (false: there exist natural numbers not exceeding 0, depending on convention)
- ∀n ∈ ℤ, n is even or n is odd (true)

### Negation

¬(∀x P(x)) ≡ ∃x ¬P(x)

To show a universal statement false, find one counterexample.

## Existential Quantifier (∃)

The **existential quantifier** ∃ means "there exists" or "there is at least one".

**Notation**: ∃x P(x) — "there exists an x such that P(x) is true"

### Interpretation

∃x P(x) is true if and only if P(x) is true for at least one element in the domain.

### Examples

- ∃x ∈ ℝ, x² = 4 (true: x = 2 or x = -2)
- ∃x ∈ ℝ, x² < 0 (false: no real number squared is negative)
- ∃n ∈ ℕ, n is prime (true: e.g., 2, 3, 5, ...)

### Negation

¬(∃x P(x)) ≡ ∀x ¬P(x)

To show an existential statement false, prove the negation for all elements.

## Quantifier Laws

### De Morgan's Laws for Quantifiers

- ¬(∀x P(x)) ≡ ∃x ¬P(x)
- ¬(∃x P(x)) ≡ ∀x ¬P(x)

### Commutative Laws

- ∀x ∀y P(x, y) ≡ ∀y ∀x P(x, y)
- ∃x ∃y P(x, y) ≡ ∃y ∃x P(x, y)

### Mixed Quantifiers (Order Matters!)

- ∀x ∃y P(x, y): For every x, there exists a y (possibly different for each x)
- ∃y ∀x P(x, y): There exists a y such that for all x, P(x, y) holds

These are **not** equivalent.

**Example**: ∀x ∈ ℝ ∃y ∈ ℝ (y > x) is true, but ∃y ∈ ℝ ∀x ∈ ℝ (y > x) is false.

## Scope and Bound Variables

The **scope** of a quantifier is the portion of the formula it applies to.

In ∀x P(x) ∨ Q(x):
- The ∀ binds x only in P(x)
- Q(x) has a free variable x (not bound by this quantifier)

## Domain of Discourse

The **domain** is the set of values over which variables range. Changing the domain changes truth values:

- ∀x ∈ ℝ, x² ≥ 0 (true)
- ∀x ∈ ℂ, x² ≥ 0 (false: complex numbers don't have standard ordering)
