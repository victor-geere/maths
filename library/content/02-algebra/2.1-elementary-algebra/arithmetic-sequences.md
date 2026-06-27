---
title: Arithmetic Sequences
tag: algebra
summary: Sequences with a constant difference between consecutive terms.
links:
  - geometric-sequences
  - binomial-theorem
  - mathematical-induction
---

## Definition

A sequence $(a_n)$ is **arithmetic** if there exists a constant $d$ (the **common difference**) such that:

$$a_n = a_{n-1} + d \quad \text{for all } n \geq 2$$

## General Term

$$a_n = a_1 + (n-1)d$$

## Sum of First $n$ Terms

$$S_n = \sum_{k=1}^n a_k = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}\bigl(2a_1 + (n-1)d\bigr)$$

The second form — "average of first and last, times count" — is attributed to Gauss.

## Example

Sequence: $3, 7, 11, 15, \ldots$ ($a_1 = 3$, $d = 4$).

- $a_{10} = 3 + 9 \cdot 4 = 39$
- $S_{10} = \frac{10}{2}(3 + 39) = 210$

## Recognising Arithmetic Sequences

The sequence is arithmetic iff the **first differences** $a_{n+1} - a_n$ are all equal.

## Arithmetic Mean

For three terms in AP: $a, b, c$ arithmetic $\iff b = \frac{a+c}{2}$ (the middle term is the arithmetic mean).

## Notes

- Arithmetic sequences model uniform growth/change (e.g. linear motion with constant velocity).
- The sum $S_n$ is always a quadratic in $n$.
