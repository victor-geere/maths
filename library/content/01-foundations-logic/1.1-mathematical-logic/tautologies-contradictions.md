---
title: Tautologies & Contradictions
tag: logic
summary: Formulas always true (tautologies) or always false (contradictions) regardless of variable assignments.
links:
  - propositions-connectives
  - truth-tables
  - normal-forms
---

# Tautologies & Contradictions

## Tautologies

A **tautology** is a proposition that is always true, regardless of the truth values of its component propositions.

### Examples

- **Law of Excluded Middle**: P ∨ ¬P
  - For any P, either P is true or ¬P is true

- **Law of Non-Contradiction**: ¬(P ∧ ¬P)
  - P cannot be both true and false simultaneously

- **Identity Laws**:
  - P → P (always true)
  - P ↔ P (always true)

- **Implication Tautology**: (P → Q) ∨ ¬P
  - Either the implication holds or the antecedent is false

### Truth Table Example

| P | Q | P ∨ ¬P | (P → Q) ∨ ¬P |
|---|---|--------|-------------|
| T | T | T | T |
| T | F | T | T |
| F | T | T | T |
| F | F | T | T |

## Contradictions

A **contradiction** is a proposition that is always false, regardless of the truth values of its components.

### Examples

- **Contradiction**: P ∧ ¬P
  - P cannot be both true and false

- **Negated Law of Excluded Middle**: ¬(P ∨ ¬P)
  - The negation of a tautology

- **False Premise Implication**: (P ∧ ¬P) → Q
  - While the full formula is a tautology (always true), the antecedent is a contradiction

### Truth Table Example

| P | Q | P ∧ ¬P | (P ∧ ¬P) ∧ Q |
|---|---|--------|------------|
| T | T | F | F |
| T | F | F | F |
| F | T | F | F |
| F | F | F | F |

## Contingencies

A **contingency** is a proposition that is sometimes true and sometimes false.

Example: P → Q (depends on the specific values of P and Q)

## Logical Equivalence

Two propositions are **logically equivalent** if they have the same truth value under all assignments. This can be verified:
- By truth tables (if feasible)
- By algebraic manipulation using known tautologies
- By showing each implies the other

**Notation**: P ≡ Q or P ⇔ Q
