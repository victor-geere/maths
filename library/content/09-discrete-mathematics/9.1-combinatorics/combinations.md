---
title: Combinations & Binomial Coefficients
tag: discrete
summary: Unordered selections of r items from n — when only which items are chosen matters, not their order.
links:
  - permutations
  - binomial-theorem
  - inclusion-exclusion
---

# Combinations & Binomial Coefficients

A **combination** is an unordered selection of items — a subset, rather than a sequence. Whenever we ask "how many ways to choose $r$ from $n$?" without caring about order (a committee, a hand of cards, a set of toppings), we are counting combinations. The answer is the **binomial coefficient** $\binom{n}{r}$, read "$n$ choose $r$", which also appears as the coefficient of $x^r$ in the expansion of $(1+x)^n$. Binomial coefficients form Pascal's triangle, satisfy elegant symmetry and recurrence relations, and arise throughout probability (computing odds), algebra (polynomial expansions), and combinatorics.

## Formula

$$\binom{n}{r} = C(n,r) = \frac{n!}{r!\,(n-r)!}$$

The number of ways to choose $r$ objects from $n$ distinct objects when order does not matter.

## Relationship to Permutations

$$\binom{n}{r} = \frac{P(n,r)}{r!}$$

Dividing by $r!$ removes the overcounting due to ordering the $r$ chosen items.

## Key Identities

| Identity | Formula |
|---|---|
| Symmetry | $\binom{n}{r} = \binom{n}{n-r}$ |
| Pascal's rule | $\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$ |
| Boundary | $\binom{n}{0} = \binom{n}{n} = 1$ |
| Row sum | $\sum_{r=0}^n \binom{n}{r} = 2^n$ |
| Alternating sum | $\sum_{r=0}^n (-1)^r\binom{n}{r} = 0$ |
| Vandermonde | $\binom{m+n}{r} = \sum_{k=0}^r \binom{m}{k}\binom{n}{r-k}$ |

## Pascal's Triangle

Row $n$ lists $\binom{n}{0}, \binom{n}{1}, \ldots, \binom{n}{n}$. Each entry is the sum of the two entries directly above it (Pascal's rule).

## With Repetition (Stars and Bars)

Choosing $r$ items from $n$ types with repetition allowed (order irrelevant):

$$\binom{n+r-1}{r}$$

The "stars and bars" formula counts ways to distribute $r$ identical items into $n$ distinct bins.

## Examples

- A poker hand (5 from 52): $\binom{52}{5} = 2{,}598{,}960$
- Ways to choose a committee of 4 from 10 people: $\binom{10}{4} = 210$
- Number of ways to put 7 identical balls into 3 distinct boxes: $\binom{9}{7} = 36$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\binom{n}{r}$ | binomial coefficient "$n$ choose $r$": $n!/(r!(n-r)!)$ |
| $C(n,r)$ | alternative notation for $\binom{n}{r}$ |
| Combination | an unordered selection of $r$ from $n$ |
| Pascal's rule | $\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$ |
| Symmetry | $\binom{n}{r} = \binom{n}{n-r}$: choosing $r$ is the same as leaving $n-r$ |
| Stars and bars | combinatorial technique for counting multisets |
| Vandermonde identity | $\binom{m+n}{r} = \sum_k\binom{m}{k}\binom{n}{r-k}$ |
| $2^n$ | total number of subsets of an $n$-element set |
| $r!$ | $r$ factorial — accounts for the orderings of the chosen items |
| Unordered selection | a subset; position does not matter |
