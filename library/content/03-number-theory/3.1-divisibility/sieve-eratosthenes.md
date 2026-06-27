---
title: Sieve of Eratosthenes
tag: number-theory
summary: Ancient algorithm for finding all primes up to a given bound by successive elimination.
links:
  - prime-factorisation
  - prime-counting
  - divisibility-rules
---

## Algorithm

To find all primes up to $N$:

1. List all integers from 2 to $N$.
2. Start with $p = 2$ (the smallest prime).
3. Mark all **multiples** of $p$ greater than $p$ as composite.
4. Find the next unmarked number $> p$; set $p$ to that number.
5. Repeat until $p > \sqrt{N}$.
6. All remaining unmarked numbers are prime.

## Why $\sqrt{N}$ Suffices

If $n \leq N$ is composite, it has a prime factor $\leq \sqrt{N}$. So all composites are marked when we process primes up to $\sqrt{N}$.

## Example: Primes up to 30

Start: $2, 3, 4, 5, 6, 7, 8, 9, 10, 11, \ldots, 30$

- Sieve by 2: remove $4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30$
- Sieve by 3: remove $9, 15, 21, 27$
- Sieve by 5: remove $25$ ($\sqrt{30} < 6$, so stop)

Primes: $2, 3, 5, 7, 11, 13, 17, 19, 23, 29$.

## Complexity

- **Time:** $O(N \log \log N)$
- **Space:** $O(N)$

A **segmented sieve** reduces space to $O(\sqrt{N})$ by processing in blocks.

## Variants

- **Linear sieve:** $O(N)$ time by marking each composite exactly once.
- **Sieve of Sundaram / Atkin:** alternative constructions with similar complexity.

## Notes

- Despite being over 2000 years old, the sieve remains competitive for generating all primes below $\sim 10^9$.
