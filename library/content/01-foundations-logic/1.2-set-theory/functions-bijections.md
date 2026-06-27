---
title: Functions & Bijections
tag: set-theory
summary: Functions, injections, surjections, bijections, inverses, and composition; cardinality via bijections.
links:
  - cartesian-product
  - relations
  - countability
---

# Functions & Bijections

A **function** from set A to set B, written f: A → B, is a relation that assigns to each element of A exactly one element of B.

## Definition

f ⊆ A × B is a function if:
- **Defined on all of A**: ∀a ∈ A, ∃b ∈ B, (a, b) ∈ f
- **Single-valued**: ∀a ∈ A, if (a, b) ∈ f and (a, b') ∈ f, then b = b'

## Notation

For function f: A → B:
- f(a) = b means (a, b) ∈ f
- A is the **domain** of f
- B is the **codomain** of f
- f(A) = {f(a) | a ∈ A} is the **range** (or **image**)

## Examples

### Example 1: Simple Function
- f: {1, 2, 3} → {a, b, c} defined by f(1) = a, f(2) = b, f(3) = c
- Domain: {1, 2, 3}
- Codomain: {a, b, c}
- Range: {a, b, c}

### Example 2: Real Functions
- f: ℝ → ℝ defined by f(x) = x²
- Domain: ℝ
- Codomain: ℝ
- Range: [0, ∞) ⊊ ℝ

### Example 3: Partial Function (Not a Total Function)
- g: ℝ → ℝ defined by g(x) = 1/x is NOT a function on all of ℝ (undefined at 0)
- Restricting domain: g: ℝ \ {0} → ℝ is a function

## Types of Functions

### Injection (One-to-One)

A function f: A → B is **injective** if different inputs give different outputs:

**∀a, a' ∈ A, if f(a) = f(a') then a = a'**

Equivalently: **∀a, a' ∈ A, if a ≠ a' then f(a) ≠ f(a')**

**Example**: f(x) = x + 1 is injective
- If x₁ + 1 = x₂ + 1, then x₁ = x₂ ✓

**Non-example**: f(x) = x² is not injective
- f(2) = f(-2) = 4 but 2 ≠ -2

### Surjection (Onto)

A function f: A → B is **surjective** if every element of B is mapped to:

**∀b ∈ B, ∃a ∈ A, f(a) = b**

Equivalently: **f(A) = B** (range equals codomain)

**Example**: f: ℝ → ℝ defined by f(x) = x + 1 is surjective
- For any y ∈ ℝ, let a = y - 1, then f(a) = y ✓

**Non-example**: f(x) = x² from ℝ to ℝ is not surjective
- No x has x² = -1

### Bijection (One-to-One and Onto)

A function is a **bijection** if it is both injective and surjective.

**Bijections establish a perfect correspondence** between domain and codomain.

**Example**: f: ℝ → ℝ defined by f(x) = 2x + 1 is a bijection
- Injective: if 2x₁ + 1 = 2x₂ + 1, then x₁ = x₂
- Surjective: for any y, let x = (y - 1)/2, then f(x) = y

## Inverse Functions

If f: A → B is a bijection, the **inverse function** f⁻¹: B → A is defined by:

**f⁻¹(b) = a iff f(a) = b**

### Properties

- f⁻¹ is also a bijection
- f⁻¹(f(a)) = a for all a ∈ A
- f(f⁻¹(b)) = b for all b ∈ B
- (f⁻¹)⁻¹ = f

### Example

f: ℝ → ℝ defined by f(x) = 2x + 1

f⁻¹(y) = (y - 1)/2

Verify: f⁻¹(f(x)) = f⁻¹(2x + 1) = (2x + 1 - 1)/2 = x ✓

## Composition of Functions

If f: A → B and g: B → C, the **composition** g ∘ f: A → C is:

**(g ∘ f)(a) = g(f(a))**

### Properties

- Associative: (h ∘ g) ∘ f = h ∘ (g ∘ f)
- Not commutative: f ∘ g ≠ g ∘ f (generally)
- Injection preserved: if f, g are injective, so is g ∘ f
- Surjection preserved: if f, g are surjective, so is g ∘ f
- Bijection preserved: if f, g are bijections, so is g ∘ f

## Cardinality and Bijections

Two sets have the **same cardinality** if there exists a bijection between them.

Notation: |A| = |B| if there's a bijection f: A → B.

### Examples

- ℕ and ℤ have the same cardinality (though ℤ seems "larger")
- ℝ and ℝ² have the same cardinality
- But ℕ and ℝ have different cardinalities

See [[countability]] and [[cantors-theorem]].

## Identity and Inclusion

### Identity Function
id_A: A → A defined by id_A(a) = a

- id is injective and surjective (hence bijective)
- f ∘ id_A = f and id_B ∘ f = f

### Inclusion Function
If S ⊆ A, the **inclusion** i: S → A is defined by i(s) = s.

- Injective (different elements stay different)
- Surjective only if S = A

## Key Facts

- Functions must be defined on entire domain, single-valued
- Injections preserve distinctness
- Surjections are "onto" the codomain
- Bijections are invertible and establish perfect correspondence
- Composition of bijections is a bijection
- Cardinality measured via bijections (for infinite sets)
