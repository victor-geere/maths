---
title: Truth Tables
tag: logic
summary: Systematic enumeration of truth values for all input combinations of a proposition.
links:
  - propositions-connectives
  - tautologies-contradictions
---

# Truth Tables

A **truth table** is a systematic way to display all possible truth values of a logical expression given all possible assignments of truth values to its variables.

## Construction

For n variables, a truth table has 2ⁿ rows (one for each possible combination of truth values).

### Example: Two Variables

| P | Q | P ∧ Q | P ∨ Q | P → Q | ¬P | ¬Q | P ↔ Q |
|---|---|-------|-------|-------|----|----|-------|
| T | T | T | T | T | F | F | T |
| T | F | F | T | F | F | T | F |
| F | T | F | T | T | T | F | F |
| F | F | F | F | T | T | T | T |

### Example: Three Variables

For P, Q, R:

| P | Q | R | P ∧ Q | Q ∨ R | (P ∧ Q) → (Q ∨ R) |
|---|---|---|-------|-------|------------------|
| T | T | T | T | T | T |
| T | T | F | T | T | T |
| T | F | T | F | T | T |
| T | F | F | F | F | T |
| F | T | T | F | T | T |
| F | T | F | F | T | T |
| F | F | T | F | T | T |
| F | F | F | F | F | T |

## Applications

Truth tables are used to:
- **Verify logical equivalence**: Two formulas are equivalent if they have identical truth columns
- **Determine satisfiability**: Check if there exists any assignment making the formula true
- **Analyze argument validity**: Verify that the conclusion is true whenever all premises are true

## Limitations

For formulas with many variables, truth tables become impractical:
- 10 variables → 1024 rows
- 20 variables → over 1 million rows

This motivates the use of algebraic methods and automated reasoning systems.
