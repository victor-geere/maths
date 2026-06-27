---
title: First-Order Logic
tag: logic
summary: Predicate logic with quantifiers, variables, and functions — more expressive than propositional logic.
links:
  - propositions-connectives
  - quantifiers
  - proof-strategies
---

# First-Order Logic

**First-order logic** (FOL), also called predicate logic or the predicate calculus, extends propositional logic by introducing predicates, quantifiers, and variables.

## Components

### Syntax

1. **Variables**: x, y, z, ... (range over domain elements)
2. **Constants**: a, b, c, ... (specific elements)
3. **Predicates**: P(x), Q(x, y), ... (describe properties or relations)
4. **Functions**: f(x), g(x, y), ... (map elements to elements)
5. **Quantifiers**: ∀ (universal), ∃ (existential)
6. **Connectives**: ¬, ∧, ∨, →, ↔

### Examples of Formulas

- ∀x (Human(x) → Mortal(x)): All humans are mortal
- ∃x (Prime(x) ∧ Even(x)): There exists an even prime
- ∀x ∃y (y = x + 1): For every x, there is a successor y

## Semantics

### Interpretation

An **interpretation** assigns:
- A domain D (non-empty set)
- Meanings to predicates (subsets of D or Dⁿ)
- Meanings to functions (functions on D)
- Meanings to constants (elements of D)

### Truth Under Interpretation

A formula is **true** under an interpretation if it holds in that interpretation's domain with the assigned meanings.

### Models

An **model** is an interpretation that makes all formulas in a theory true.

## Key Concepts

### Validity and Satisfiability

- A formula is **valid** if it's true under all interpretations (e.g., P → P)
- A formula is **satisfiable** if it's true under at least one interpretation
- A formula is **unsatisfiable** if it's false under all interpretations (a contradiction)

### Logical Consequence

Formula C is a **logical consequence** of formulas A and B (written A, B ⊨ C) if C is true in every interpretation where both A and B are true.

### Completeness and Decidability

- **Gödel's Completeness Theorem**: A formula is valid iff it's provable from the axioms of FOL
- **Church–Turing Undecidability**: There is no algorithm to determine if an arbitrary FOL formula is valid

## Examples in Mathematics

### Set Theory
∀x ∀y (x = y ↔ ∀z (z ∈ x ↔ z ∈ y))
— Extensionality: sets are equal if they have the same elements

### Group Theory
∀x ∀y ∃z (x · y = z) ∧ (∃e ∀x (x · e = x)) ∧ (∀x ∃x⁻¹ (x · x⁻¹ = e))
— Closure, identity, and inverse properties

### Arithmetic
∀x ∀y (x + (y + 1) = (x + y) + 1)
— Successor property

## Limitations

FOL cannot express:
- Second-order properties (e.g., "every subset has an upper bound")
- Cardinality constraints beyond the domain size (e.g., "there are uncountably many...")
- Non-standard quantification (e.g., "most x satisfy P(x)")

These require **second-order logic** or extensions.
