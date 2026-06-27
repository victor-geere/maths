---
title: Cartesian Product
tag: set-theory
summary: A × B = {(a,b) | a ∈ A, b ∈ B} — ordered pairs and n-tuples.
links:
  - sets-notation
  - relations
  - functions-bijections
---

# Cartesian Product

## Definition

The **Cartesian product** of sets A and B, written A × B, is the set of all ordered pairs (a, b) where a ∈ A and b ∈ B.

**Definition**: A × B = {(a, b) | a ∈ A ∧ b ∈ B}

### Ordered Pairs

An **ordered pair** (a, b) is distinct from (b, a) unless a = b.

- (a, b) = (c, d) if and only if a = c and b = d

This contrasts with unordered pairs {a, b} = {b, a}.

## Examples

### Finite Sets

- A = {1, 2}, B = {a, b}
- A × B = {(1, a), (1, b), (2, a), (2, b)}
- B × A = {(a, 1), (a, 2), (b, 1), (b, 2)}
- Note: A × B ≠ B × A (unless A = B or one is empty)

### Real Numbers

- ℝ × ℝ = ℝ² = the Euclidean plane
- Points are ordered pairs (x, y) where x, y ∈ ℝ
- Visualized as the coordinate plane

### Mixed Sets

- ℕ × {a, b} = {(0, a), (0, b), (1, a), (1, b), (2, a), (2, b), ...}

## Cardinality

For finite sets A and B:

**|A × B| = |A| × |B|**

### Examples

- |{1, 2} × {a, b, c}| = 2 × 3 = 6
- |A × B| = 5 × 7 = 35 where |A| = 5, |B| = 7

## General Cartesian Products

### Multiple Sets

For sets A₁, A₂, ..., Aₙ:

A₁ × A₂ × ... × Aₙ = {(a₁, a₂, ..., aₙ) | aᵢ ∈ Aᵢ for all i}

Elements are **n-tuples** or **ordered n-tuples**.

**Example**: ℝ × ℝ × ℝ = ℝ³ (three-dimensional space)

### Exponentiation Notation

A^n = A × A × ... × A (n times)

**Examples**:
- ℝ² = ℝ × ℝ (plane)
- ℝ³ = ℝ × ℝ × ℝ (3D space)
- {0, 1}³ = {(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)}

## Properties

### Commutativity

A × B = B × A if and only if A = B or one is empty

Generally: **A × B ≠ B × A** (order matters)

### Associativity

(A × B) × C ≠ A × (B × C) in general, but they have the same "essentially"

- (A × B) × C contains ((a, b), c)
- A × (B × C) contains (a, (b, c))
- These are technically different, but both represent the same data

### Distributivity over Union and Intersection

- **A × (B ∪ C) = (A × B) ∪ (A × C)**
- **A × (B ∩ C) = (A × B) ∩ (A × C)**
- **(A ∪ B) × C = (A × C) ∪ (B × C)**
- **(A ∩ B) × C = (A × C) ∩ (B × C)**

### With Set Operations

- **A × ∅ = ∅**
- **∅ × B = ∅**
- **A × B ⊆ A' × B'** if A ⊆ A' and B ⊆ B'

## Relations and Functions

Relations and functions are subsets of Cartesian products:

- A **relation** from A to B is a subset of A × B
- A **function** f: A → B is a special relation where each a ∈ A pairs with exactly one b ∈ B

**Example**: The function f(x) = x² can be represented as the relation:
{(x, x²) | x ∈ ℝ} ⊆ ℝ × ℝ

See [[relations]] and [[functions-bijections]] for more details.

## Applications

- **Coordinates**: Points in spaces (ℝⁿ)
- **Graphs**: Edge sets in directed graphs (V × V)
- **Database theory**: Records as tuples in product spaces
- **Logic**: Truth tables as subsets of boolean products
- **Probability**: Sample spaces as product sets

## Key Facts

- Cartesian product is non-commutative (A × B ≠ B × A usually)
- Empty set absorbs: A × ∅ = ∅
- Cardinality multiplies: |A × B| = |A| × |B|
- Gives "tuples" or "coordinates" for structured data
