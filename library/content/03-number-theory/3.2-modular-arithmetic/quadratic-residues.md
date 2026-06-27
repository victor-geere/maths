---
title: Quadratic Residues
tag: number-theory
summary: Integers that are perfect squares modulo a prime, and the Legendre symbol.
links:
  - modular-arithmetic
  - fermats-little-theorem
  - eulers-totient
---

## Definition

For a prime $p$ and $a$ with $p \nmid a$, the integer $a$ is a **quadratic residue** mod $p$ (written QR) if:

$$x^2 \equiv a \pmod{p}$$

has a solution. Otherwise $a$ is a **quadratic non-residue** (QNR).

## Legendre Symbol

$$\left(\frac{a}{p}\right) = \begin{cases} 0 & p \mid a \\ 1 & a \text{ is QR mod } p \\ -1 & a \text{ is QNR mod } p \end{cases}$$

**Euler's criterion:**

$$\left(\frac{a}{p}\right) \equiv a^{(p-1)/2} \pmod{p}$$

## Counting

Among $\{1, \ldots, p-1\}$, exactly $\frac{p-1}{2}$ are QRs and $\frac{p-1}{2}$ are QNRs.

## Quadratic Reciprocity (Gauss)

For distinct odd primes $p, q$:

$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}}$$

Simplified: $\left(\frac{p}{q}\right) = \left(\frac{q}{p}\right)$ unless both $p \equiv q \equiv 3 \pmod 4$, in which case they differ.

## Example

Is 3 a QR mod 11?

$3^{(11-1)/2} = 3^5 = 243 \equiv 243 - 22 \cdot 11 = 1 \pmod{11}$.

So $\left(\frac{3}{11}\right) = 1$ — yes, 3 is a QR mod 11. Indeed $5^2 = 25 \equiv 3 \pmod{11}$.

## Notes

- Quadratic residues generalise to the Jacobi symbol for composite moduli.
- They play a central role in primality tests and cryptographic protocols.
