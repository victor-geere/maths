---
title: Divisibility Rules
tag: number-theory
summary: Quick tests to determine whether an integer is divisible by small numbers.
links:
  - prime-factorisation
  - euclids-algorithm
  - modular-arithmetic
---

## Definition

An integer $a$ **divides** $b$ (written $a \mid b$) if $b = ka$ for some integer $k$.

Equivalently, $a \mid b \iff b \bmod a = 0$.

## Common Rules

| Divisor | Rule |
|---|---|
| 2 | last digit is even (0, 2, 4, 6, 8) |
| 3 | sum of digits divisible by 3 |
| 4 | last two digits form a number divisible by 4 |
| 5 | last digit is 0 or 5 |
| 6 | divisible by both 2 and 3 |
| 7 | double the last digit and subtract from the rest; repeat |
| 8 | last three digits divisible by 8 |
| 9 | sum of digits divisible by 9 |
| 10 | last digit is 0 |
| 11 | alternating sum of digits divisible by 11 |

## Why They Work

Most rules follow from $10 \equiv 1 \pmod{9}$, $10 \equiv -1 \pmod{11}$, etc.

**Digit-sum rule for 9:** if $n = \sum_k d_k \cdot 10^k$, then since $10^k \equiv 1^k = 1 \pmod{9}$:

$$n \equiv \sum_k d_k \pmod{9}$$

## Basic Divisibility Properties

- $a \mid b$ and $a \mid c \Rightarrow a \mid (mb + nc)$ for any integers $m, n$
- $a \mid b$ and $b \mid c \Rightarrow a \mid c$
- $a \mid b$ and $b \mid a \Rightarrow |a| = |b|$

## Example

Is $123{,}456$ divisible by 3? Digit sum: $1+2+3+4+5+6 = 21$, and $3 \mid 21$. Yes.

Is it divisible by 9? $21 \div 9$ has remainder 3. No.
