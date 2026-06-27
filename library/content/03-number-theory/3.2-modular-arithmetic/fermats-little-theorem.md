---
title: Fermat's Little Theorem
tag: number-theory
summary: For prime p and integer a not divisible by p, a^(p−1) ≡ 1 (mod p).
links:
  - modular-arithmetic
  - eulers-totient
  - lagranges-theorem
---

## Statement

Let $p$ be prime and $a \in \mathbb{Z}$ with $p \nmid a$. Then:

$$a^{p-1} \equiv 1 \pmod{p}$$

Equivalently (for all integers $a$):

$$a^p \equiv a \pmod{p}$$

## Proof via Group Theory

The multiplicative group $(\mathbb{Z}/p\mathbb{Z})^*$ has order $p-1$. By [[lagranges-theorem|Lagrange's theorem]], the order of any element divides the group order, so $a^{p-1} \equiv 1 \pmod{p}$. $\square$

## Proof via Necklaces (combinatorial)

Count necklaces of $p$ beads with $a$ colours: there are $a^p$ colourings total; necklaces with all beads the same colour: $a$; the remaining $a^p - a$ are grouped in orbits of size $p$, so $p \mid a^p - a$.

## Applications

### Modular Inverse

When $p$ is prime and $p \nmid a$:

$$a^{-1} \equiv a^{p-2} \pmod{p}$$

### Fast Exponentiation

Reduce $a^k \pmod{p}$ by computing $k \bmod (p-1)$ first.

### Primality Testing

If $a^{n-1} \not\equiv 1 \pmod{n}$ for some $a$, then $n$ is composite (Fermat witness). The converse fails for Carmichael numbers.

## Example

$2^{12} \pmod{13}$: by FLT, $2^{12} \equiv 1 \pmod{13}$. ✓

$7^{100} \pmod{11}$: $100 = 9 \cdot 10 + 10$, so $7^{100} \equiv 7^{10} \equiv (7^5)^2 \pmod{11}$. Since $7^{10} \equiv 1$ by FLT, $7^{100} \equiv 1 \pmod{11}$.
