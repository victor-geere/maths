---
title: Normal Forms (CNF, DNF)
tag: logic
summary: Standardized forms for propositional formulas — Conjunctive and Disjunctive Normal Forms.
links:
  - propositions-connectives
  - tautologies-contradictions
---

# Normal Forms (CNF, DNF)

## Disjunctive Normal Form (DNF)

A formula is in **Disjunctive Normal Form** if it is a disjunction of conjunctions of literals (where a literal is a variable or its negation).

**General Structure**: (A ∧ B ∧ ...) ∨ (C ∧ D ∧ ...) ∨ ...

### Examples

- P ∨ Q
- (P ∧ Q) ∨ R
- (P ∧ ¬Q) ∨ (¬P ∧ Q) ∨ (¬P ∧ ¬Q)
- P ∧ Q (a single conjunctive clause)

### Conversion to DNF

1. Eliminate implications and biconditionals:
   - P → Q ≡ ¬P ∨ Q
   - P ↔ Q ≡ (P ∧ Q) ∨ (¬P ∧ ¬Q)

2. Apply De Morgan's Laws to move negations inward:
   - ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
   - ¬(P ∨ Q) ≡ ¬P ∧ ¬Q

3. Distribute disjunction over conjunction:
   - P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R)

## Conjunctive Normal Form (CNF)

A formula is in **Conjunctive Normal Form** if it is a conjunction of disjunctions of literals.

**General Structure**: (A ∨ B ∨ ...) ∧ (C ∨ D ∨ ...) ∧ ...

### Examples

- P ∧ Q
- (P ∨ Q) ∧ R
- (P ∨ ¬Q) ∧ (¬P ∨ Q) ∧ (Q ∨ R)
- P ∨ Q (a single disjunctive clause)

### Conversion to CNF

1. Eliminate implications and biconditionals (as above)

2. Apply De Morgan's Laws (as above)

3. Distribute conjunction over disjunction:
   - P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R)

## Conversion Example

Convert (P → Q) ∧ (Q → R) to CNF:

1. Eliminate implications:
   - (¬P ∨ Q) ∧ (¬Q ∨ R)

2. Already in CNF!

Convert P → (Q ∧ R) to DNF:

1. Eliminate implications:
   - ¬P ∨ (Q ∧ R)

2. Already in DNF!

## Applications

- **SAT solvers**: Work with CNF formulas
- **Automated reasoning**: Both forms useful for different algorithms
- **Circuit design**: DNF and CNF correspond to different gate arrangements
- **Knowledge representation**: Normal forms enable systematic inference

## Complexity

- Converting to DNF can exponentially increase formula length (worst case)
- Converting to CNF typically adds polynomial overhead
- This is why SAT problems are NP-complete but conversion itself is tractable
