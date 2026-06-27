---
title: Propositions & Connectives
tag: logic
summary: Atomic propositions and logical operators (¬, ∧, ∨, →, ↔) with truth conditions.
links:
  - truth-tables
  - normal-forms
  - tautologies-contradictions
---

# Propositions & Connectives

## Propositions

A **proposition** is a declarative statement that is either true or false, but not both.

Examples:
- "2 + 2 = 4" (true)
- "Paris is in France" (true)
- "5 > 10" (false)

Non-propositions:
- "Is it raining?" (question)
- "Close the door" (command)
- "x > 3" (open statement, depends on x)

## Logical Connectives

Propositions are combined using logical operators:

### Negation (¬)
The negation of proposition P is true when P is false, and false when P is true.

| P | ¬P |
|---|---|
| T | F |
| F | T |

### Conjunction (∧)
"P and Q" is true only when both P and Q are true.

| P | Q | P ∧ Q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

### Disjunction (∨)
"P or Q" is true when at least one of P or Q is true.

| P | Q | P ∨ Q |
|---|---|-------|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

### Implication (→)
"If P then Q" is false only when P is true and Q is false.

| P | Q | P → Q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

### Biconditional (↔)
"P if and only if Q" is true when P and Q have the same truth value.

| P | Q | P ↔ Q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

## De Morgan's Laws

- ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
- ¬(P ∨ Q) ≡ ¬P ∧ ¬Q

## Operator Precedence

1. Negation (¬)
2. Conjunction (∧)
3. Disjunction (∨)
4. Implication (→)
5. Biconditional (↔)
