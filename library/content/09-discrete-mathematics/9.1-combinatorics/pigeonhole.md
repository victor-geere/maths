---
title: Pigeonhole Principle
tag: discrete
summary: If n+1 objects are distributed into n containers, at least one container holds two or more objects.
links:
  - combinations
  - inclusion-exclusion
  - ramsey-theory
---

# Pigeonhole Principle

The **Pigeonhole Principle** is perhaps the simplest non-trivial principle in mathematics, yet it yields surprisingly deep results. If you place $n+1$ pigeons into $n$ holes, at least one hole must contain more than one pigeon. This obvious-sounding observation — which follows from counting alone — can be used to prove results in number theory, geometry, combinatorics, and even analysis. In its **generalised form**, it guarantees that some container holds at least $\lceil m/n \rceil$ items when $m$ objects are distributed into $n$ containers. The principle is the combinatorial version of the infinite contains something finite: whenever you have more objects than categories, repetition is inevitable.

## Basic Statement

If $m$ objects are placed into $n$ containers and $m > n$, then at least one container holds **two or more** objects.

## Generalised Pigeonhole Principle

If $m$ objects are placed into $n$ containers, then at least one container holds at least:

$$\left\lceil \frac{m}{n} \right\rceil \text{ objects}$$

where $\lceil \cdot \rceil$ denotes the ceiling function.

## Examples

**Number theory:** Among any 13 integers, two must share the same remainder when divided by 12 (since there are only 12 possible remainders $0, 1, \ldots, 11$).

**Geometry:** In any group of 5 points placed inside a unit square, two points are within distance $\frac{\sqrt{2}}{2}$ of each other (divide the square into 4 triangles by the diagonals).

**Graph theory:** In any group of 6 people, either 3 know each other or 3 are all strangers (Ramsey number $R(3,3) = 6$).

**Sequence:** Any sequence of more than $n^2$ distinct real numbers contains either an increasing or a decreasing subsequence of length $n+1$ (Erdős–Szekeres theorem).

## Infinite Pigeonhole Principle

If infinitely many objects are placed in finitely many containers, then at least one container holds infinitely many objects.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $m$ | number of objects (pigeons) |
| $n$ | number of containers (holes) |
| $\lceil x \rceil$ | ceiling of $x$: smallest integer $\geq x$ |
| $\lfloor x \rfloor$ | floor of $x$: largest integer $\leq x$ |
| Generalised pigeonhole | at least one container holds $\geq \lceil m/n \rceil$ objects |
| Remainder (mod $n$) | $m \bmod n$: the remainder when $m$ is divided by $n$ |
| Erdős–Szekeres theorem | sequence of $n^2+1$ distinct reals has monotone subsequence of length $n+1$ |
| Ramsey number $R(3,3)$ | smallest $n$ such that any 2-colouring of $K_n$ contains a monochromatic triangle |
| Monotone subsequence | one that is entirely non-decreasing or non-increasing |
| Infinite pigeonhole | infinitely many objects in finitely many bins $\Rightarrow$ some bin is infinite |
