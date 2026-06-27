---
title: Field Axioms & Examples
tag: abstract-algebra
summary: Algebraic structures where addition and multiplication both form abelian groups.
links:
  - ring-axioms
  - field-extensions
  - ideals
---

## Definition

A **field** $(F, +, \cdot)$ is a commutative ring with unity where every non-zero element has a multiplicative inverse:

$$\forall\, a \in F \setminus \{0\},\; \exists\, a^{-1} \in F : a \cdot a^{-1} = 1$$

Equivalently, $(F \setminus \{0\}, \cdot)$ is an abelian group.

## Axioms (Summary)

| Axiom | Statement |
|---|---|
| Commutativity | $a+b=b+a$, $ab=ba$ |
| Associativity | $(a+b)+c=a+(b+c)$, $(ab)c=a(bc)$ |
| Distributivity | $a(b+c)=ab+ac$ |
| Identities | $0$ for addition, $1$ for multiplication |
| Inverses | $-a$ exists; $a^{-1}$ exists for $a \neq 0$ |

## Standard Examples

| Field | Characteristic |
|---|---|
| $\mathbb{Q}$ | 0 |
| $\mathbb{R}$ | 0 |
| $\mathbb{C}$ | 0 |
| $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$ ($p$ prime) | $p$ |
| $\mathbb{F}_{p^n}$ (finite field) | $p$ |

## Characteristic

The **characteristic** of $F$ is the smallest $n \geq 1$ with $\underbrace{1+\cdots+1}_{n} = 0$, or $0$ if no such $n$ exists.

The characteristic is always $0$ or a prime.

## Notes

- Every field is an integral domain (no zero divisors).
- Finite fields exist of order $p^n$ for prime $p$, $n \geq 1$, and are unique up to isomorphism.
- The study of fields is central to Galois theory and algebraic geometry.
