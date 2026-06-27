---
title: Euler's Theorem & Totient
tag: number-theory
summary: Generalisation of Fermat's Little Theorem to composite moduli via the totient function.
links:
  - fermats-little-theorem
  - modular-arithmetic
  - chinese-remainder-theorem
---

## Euler's Totient Function

$\phi(n)$ counts the integers in $\{1, \ldots, n\}$ that are coprime to $n$:

$$\phi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)$$

where the product runs over distinct prime divisors of $n$.

### Values

| $n$ | $\phi(n)$ |
|---|---|
| 1 | 1 |
| $p$ (prime) | $p-1$ |
| $p^k$ | $p^k - p^{k-1}$ |
| $mn$ ($\gcd(m,n)=1$) | $\phi(m)\phi(n)$ |

## Euler's Theorem

For $\gcd(a, n) = 1$:

$$a^{\phi(n)} \equiv 1 \pmod{n}$$

Fermat's Little Theorem is the special case $n = p$ prime (since $\phi(p) = p-1$).

## Proof Sketch

The units $(\mathbb{Z}/n\mathbb{Z})^*$ form a group of order $\phi(n)$. Lagrange's theorem gives $a^{\phi(n)} \equiv 1$.

## Applications

- **Modular inverse:** $a^{-1} \equiv a^{\phi(n)-1} \pmod{n}$ when $\gcd(a,n)=1$.
- **RSA cryptosystem:** key generation uses $\phi(n) = (p-1)(q-1)$ for $n = pq$.

## Example

$\phi(12) = 12(1-\tfrac{1}{2})(1-\tfrac{1}{3}) = 4$.

So $5^4 \equiv 1 \pmod{12}$. Check: $5^2 = 25 \equiv 1 \pmod{12}$, so $5^4 \equiv 1$ ✓.

## Sum Formula

$$\sum_{d \mid n} \phi(d) = n$$
