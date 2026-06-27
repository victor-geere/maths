---
title: Integers
tag: number-theory
summary: ℤ extends ℕ with negatives; integral domain with factorization; modular arithmetic foundation.
links:
  - peano-axioms
  - rationals
  - modular-arithmetic
---

# Integers

The **integers** are the set ℤ = {..., -3, -2, -1, 0, 1, 2, 3, ...}

They extend the natural numbers by adding negatives to ensure that subtraction is always possible.

## Construction from Natural Numbers

### Via Ordered Pairs

One rigorous construction represents integers as equivalence classes of ordered pairs of natural numbers.

Define pairs (m, n) and (m', n') as equivalent if m + n' = m' + n.

The integer represented by [(m, n)] is interpreted as m - n:
- [(3, 1)] ≈ 3 - 1 = 2
- [(2, 5)] ≈ 2 - 5 = -3
- [(0, 0)] ≈ 0

**ℤ** = {[(m, n)] | m, n ∈ ℕ}

### Positive and Negative Parts

Each integer z can be written uniquely as:
- If z > 0: z as a positive integer (successor of natural numbers)
- If z = 0: the additive identity
- If z < 0: negation of a positive integer

## Operations

### Addition

For integers a, b ∈ ℤ:

(m, n) + (p, q) = (m + p, n + q)

Equivalently (in difference notation): (m - n) + (p - q) = (m + p) - (n + q)

**Properties**:
- Closed: a + b ∈ ℤ
- Associative: (a + b) + c = a + (b + c)
- Identity: a + 0 = a
- Inverse: a + (-a) = 0
- Commutative: a + b = b + a

### Multiplication

For integers a, b ∈ ℤ:

(m, n) · (p, q) = (m·p + n·q, m·q + n·p)

Equivalently: (m - n) · (p - q) = (m·p + n·q) - (m·q + n·p)

**Properties**:
- Closed: a · b ∈ ℤ
- Associative: (a · b) · c = a · (b · c)
- Identity: a · 1 = a
- Commutative: a · b = b · a
- Distributive: a · (b + c) = a·b + a·c

**Note**: No multiplicative inverses (except ±1), so ℤ is not a field.

### Negation

For a ∈ ℤ:
- If a = m - n, then -a = n - m
- (-1) · a = -a

### Subtraction

a - b = a + (-b)

This is now always defined (unlike in ℕ).

## Ordering

For integers a, b ∈ ℤ:

**a < b** if b - a is a positive integer.

**Properties**:
- Transitive: if a < b and b < c, then a < c
- Antisymmetric: not both a < b and b < a
- Total: for any a, b, exactly one of a < b, a = b, or b < a holds
- Compatible with addition: if a < b, then a + c < b + c
- Compatible with multiplication: if a < b and c > 0, then a·c < b·c

## Divisibility

For integers a, b ∈ ℤ:

**a divides b** (written a | b) if there exists k ∈ ℤ such that b = a·k.

**Examples**:
- 3 | 12 because 12 = 3 · 4
- 5 | -10 because -10 = 5 · (-2)
- 0 | 0 (every integer divides 0)
- ±1 divide every integer

### Prime Numbers

An integer p > 1 is **prime** if its only positive divisors are 1 and p itself.

**Examples**: 2, 3, 5, 7, 11, 13, ...

**Fundamental Theorem of Arithmetic**: Every integer > 1 can be uniquely factored into primes (up to order and signs).

## Absolute Value

For a ∈ ℤ:

|a| = max(a, -a)

**Examples**:
- |5| = 5
- |-5| = 5
- |0| = 0

**Properties**:
- |a| ≥ 0 with equality iff a = 0
- |a · b| = |a| · |b|
- |a + b| ≤ |a| + |b| (triangle inequality)

## Modular Arithmetic

For a, b, n ∈ ℤ with n > 0:

**a ≡ b (mod n)** if n | (a - b)

This means a and b have the same remainder when divided by n.

**Example**: 17 ≡ 5 (mod 3) because 3 | (17 - 5) = 12

This is an equivalence relation, partitioning ℤ into n residue classes.

## Cardinality

ℤ is **countably infinite**: |ℤ| = ℵ₀

Enumeration: 0, 1, -1, 2, -2, 3, -3, ...

## Algebraic Structure

ℤ forms a **ring** under addition and multiplication:
- Abelian group under addition (with identity 0 and inverses)
- Monoid under multiplication (with identity 1, but no inverses except ±1)
- Distributive law connects the operations

ℤ is an **integral domain**: a · b = 0 implies a = 0 or b = 0.

## Relationship to Other Sets

- **ℕ ⊂ ℤ** (natural numbers are integers)
- **ℤ ⊂ ℚ** (integers are rational numbers via n/1)
- **ℚ ⊂ ℝ** (rationals are real numbers)

## Key Facts

- ℤ adds negatives to ℕ (closure under subtraction)
- ℤ is closed under addition, subtraction, multiplication
- ℤ is NOT closed under division (hence not a field)
- Every integer has a unique prime factorization
- Modular arithmetic on ℤ is fundamental to number theory
- Countably infinite cardinality
