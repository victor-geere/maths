---
title: Chinese Remainder Theorem
tag: number-theory
summary: Solving simultaneous congruences with pairwise coprime moduli.
links:
  - modular-arithmetic
  - eulers-totient
  - bezouts-identity
---

## Statement

Let $m_1, \ldots, m_k$ be pairwise coprime positive integers ($\gcd(m_i, m_j)=1$ for $i \neq j$). For any integers $a_1, \ldots, a_k$, the system:

$$x \equiv a_1 \pmod{m_1}, \quad x \equiv a_2 \pmod{m_2}, \quad \ldots, \quad x \equiv a_k \pmod{m_k}$$

has a **unique** solution modulo $M = m_1 m_2 \cdots m_k$.

## Construction

Let $M_i = M/m_i$ and $y_i = M_i^{-1} \pmod{m_i}$ (exists since $\gcd(M_i, m_i)=1$). Then:

$$x \equiv \sum_{i=1}^k a_i M_i y_i \pmod{M}$$

## Example

Solve: $x \equiv 2 \pmod{3}$, $x \equiv 3 \pmod{5}$, $x \equiv 2 \pmod{7}$.

$M = 105$, $M_1 = 35, M_2 = 21, M_3 = 15$.

- $35 \cdot y_1 \equiv 1 \pmod{3}$: $y_1 = 2$ (since $35 \equiv 2$ and $2 \cdot 2 = 4 \equiv 1$)
- $21 \cdot y_2 \equiv 1 \pmod{5}$: $y_2 = 1$ (since $21 \equiv 1$)
- $15 \cdot y_3 \equiv 1 \pmod{7}$: $y_3 = 1$ (since $15 \equiv 1$)

$$x \equiv 2 \cdot 70 + 3 \cdot 21 + 2 \cdot 15 = 140 + 63 + 30 = 233 \equiv 23 \pmod{105}$$

## Ring-Theoretic Form

CRT says there is a ring isomorphism:

$$\mathbb{Z}/M\mathbb{Z} \cong \mathbb{Z}/m_1\mathbb{Z} \times \cdots \times \mathbb{Z}/m_k\mathbb{Z}$$

## Notes

- CRT is the foundation of several fast algorithms (e.g. integer arithmetic, polynomial interpolation).
- Without coprimality, solutions may not exist or may not be unique.
