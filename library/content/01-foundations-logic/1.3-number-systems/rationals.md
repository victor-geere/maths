---
title: Rational Numbers
tag: number-theory
summary: ℚ = {p/q | p,q ∈ ℤ, q≠0} — field with terminating/repeating decimals; dense in ℝ but countable.
links:
  - integers
  - real-numbers
  - countability
---

# Rational Numbers

The **rational numbers** are the set ℚ = {p/q | p, q ∈ ℤ, q ≠ 0}.

They extend the integers by adding division (except by zero), allowing all multiplicative equations to be solved.

## Construction from Integers

### Via Fractions

Represent rationals as fractions p/q where p ∈ ℤ (numerator) and q ∈ ℤ⁺ (denominator).

Two fractions are equivalent if they represent the same ratio:

**p/q ≈ r/s if p · s = q · r**

**ℚ** = {p/q | p ∈ ℤ, q ∈ ℕ⁺} / ≈

Each rational is an equivalence class of fractions.

### Reduced Form

Every rational has a **canonical form** p/q where gcd(|p|, q) = 1 and q > 0.

**Examples**:
- 6/9 = 2/3 (canonical)
- -8/12 = -2/3 (canonical)
- 0/1 = 0 (canonical)

## Operations

### Addition

p/q + r/s = (p·s + q·r) / (q·s)

**Example**: 1/2 + 1/3 = (1·3 + 2·1) / (2·3) = 5/6

### Multiplication

(p/q) · (r/s) = (p·r) / (q·s)

**Example**: (2/3) · (3/5) = 6/15 = 2/5

### Division

(p/q) ÷ (r/s) = (p/q) · (s/r) = (p·s) / (q·r)

**Example**: (2/3) ÷ (4/5) = (2/3) · (5/4) = 10/12 = 5/6

### Negation

-p/q = (-p)/q = p/(-q) (usually written in canonical form: (-p)/q)

### Reciprocal

For p/q ≠ 0, the reciprocal is q/p.

## Properties

### Algebraic Structure

ℚ is a **field** under addition and multiplication:
- Abelian group under addition (identity 0, inverses -p/q)
- Abelian group under multiplication (identity 1, inverses q/p for p ≠ 0)
- Distributive law: a · (b + c) = a·b + a·c

This means:
- All linear equations have solutions in ℚ
- All polynomial equations with rational coefficients have rational solutions or can be extended

### Ordering

For p/q, r/s ∈ ℚ (with q, s > 0):

**p/q < r/s if p·s < q·r**

Properties:
- Transitive, antisymmetric, total
- Compatible with operations: if a < b and c > 0, then a·c < b·c

### Density

**Between any two distinct rationals, there exists another rational.**

For p/q < r/s, the midpoint (p·s + q·r) / (2·q·s) is rational and satisfies:

p/q < (p·s + q·r) / (2·q·s) < r/s

**Consequence**: ℚ is **dense** in ℝ (every real number can be approximated arbitrarily closely by rationals).

## Decimal Representations

### Terminating Decimals

A rational p/q (in lowest terms) has a terminating decimal iff q = 2^a · 5^b for some a, b ≥ 0.

**Examples**:
- 1/2 = 0.5
- 1/4 = 0.25
- 3/8 = 0.375

### Repeating Decimals

A rational p/q (in lowest terms) with q ≠ 2^a · 5^b has a repeating (periodic) decimal.

**Examples**:
- 1/3 = 0.333... = 0.3̄
- 1/7 = 0.142857142857... = 0.1̄4̄2̄8̄5̄7̄
- 22/7 ≈ 3.142857̄... (approximates π)

### Every Rational Has a Decimal Expansion

Every rational has either terminating or eventually repeating decimal representation.

Conversely, every terminating or repeating decimal represents a rational.

## Countability

ℚ is **countably infinite**: |ℚ| = ℵ₀

**Proof**: Enumerate rationals by the sum |p| + q:

```
0/1
1/1, -1/1
2/1, 1/2, -1/2, -2/1
3/1, 2/2, 1/3, -1/3, -2/2, -3/1
...
```

Skip duplicates. This gives a complete enumeration of ℚ.

## Gaps in ℚ

Despite density, ℚ has "gaps"—there are irrational numbers.

**Examples of irrationals**:
- √2 ≈ 1.414... (no rational p/q satisfies p²/q² = 2)
- π ≈ 3.14159... (transcendental)
- e ≈ 2.71828... (transcendental)

Proof that √2 is irrational: Assume √2 = p/q in lowest terms.
- Then 2 = p²/q², so p² = 2q²
- p² is even, so p is even: p = 2m
- Then 4m² = 2q², so q² = 2m², making q even
- But then gcd(p, q) ≥ 2, contradicting lowest terms

This shows **ℚ ≠ ℝ**.

## Algebraic vs. Transcendental

- **Algebraic number**: root of a polynomial with rational (or integer) coefficients
  - All rationals are algebraic: p/q is a root of qx - p = 0
  - √2 is algebraic: root of x² - 2 = 0
  
- **Transcendental number**: not algebraic (e.g., π, e)

The algebraic numbers (countable) form a proper subset of ℝ.

## Relationship to Other Sets

- **ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ**
- **ℚ is a field**, unlike ℤ
- **ℚ is countable**, while ℝ is uncountable
- **ℚ is dense in ℝ**, yet ℝ has "more" numbers

## Key Facts

- ℚ is closed under +, −, ·, ÷ (except division by 0)
- ℚ is a field (all nice algebraic properties)
- Dense: between any two rationals is another
- Countably infinite (same cardinality as ℤ or ℕ)
- Every rational has terminating or repeating decimal
- √2 and π are not rational (proof by contradiction)
- Enables both exact arithmetic and density properties
