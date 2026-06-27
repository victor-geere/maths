---
title: Permutations
tag: discrete
summary: Ordered arrangements of objects — counting the number of ways to arrange r items chosen from n distinct items.
links:
  - combinations
  - inclusion-exclusion
  - symmetric-groups
---

# Permutations

A **permutation** is an ordered arrangement of objects. Whenever the order in which items are arranged or selected matters — passwords, race finishings, seating arrangements — we are counting permutations. The fundamental insight is that selecting and ordering $r$ items from $n$ distinct items can be done by a chain of independent choices: $n$ choices for the first position, $n-1$ for the second (since one is used), and so on, giving a product of falling factorial form. Permutations underpin combinatorics, probability theory, symmetric group theory, and the analysis of algorithms that depend on the order of their inputs.

## Counting Ordered Arrangements

### All $n$ Objects
The number of ways to arrange all $n$ distinct objects in a row:

$$n! = n \times (n-1) \times \cdots \times 2 \times 1$$

Convention: $0! = 1$.

### $r$ Objects from $n$ (without repetition)

$$P(n, r) = {}_nP_r = \frac{n!}{(n-r)!} = n(n-1)\cdots(n-r+1)$$

### With Repetition Allowed
$$n^r$$

(each of $r$ positions can be any of the $n$ objects).

### Permutations of a Multiset
If there are $n$ objects with $n_1$ identical of type 1, $n_2$ of type 2, … , $n_k$ of type $k$ (where $n_1 + \cdots + n_k = n$):

$$\frac{n!}{n_1!\, n_2!\, \cdots\, n_k!}$$

## Circular Permutations

Arrangements around a circle (rotations are considered identical):

$$(n-1)!$$

For a necklace (reflections also identical): $\dfrac{(n-1)!}{2}$.

## Examples

- Arranging 5 books on a shelf: $5! = 120$
- Picking and ordering 3 students from a class of 30 for 1st/2nd/3rd place: $P(30,3) = 30 \times 29 \times 28 = 24{,}360$
- Number of distinct arrangements of "MISSISSIPPI" (11 letters, M×1, I×4, S×4, P×2):

$$\frac{11!}{1!\,4!\,4!\,2!} = 34{,}650$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $n!$ | $n$ factorial: $n \times (n-1) \times \cdots \times 1$ |
| $P(n,r)$ or ${}_nP_r$ | number of $r$-permutations of $n$ objects without repetition |
| $n^r$ | permutations of $r$ from $n$ with repetition |
| Ordered arrangement | a sequence where position matters |
| Multiset | a collection where items may be repeated |
| Falling factorial | $n(n-1)\cdots(n-r+1)$ — product of $r$ descending terms |
| Circular permutation | arrangement around a circle; $(n-1)!$ |
| $0! = 1$ | convention: empty product equals 1 |
| Repetition allowed | each selected item can be chosen again |
| Distinct objects | objects that can be told apart |
