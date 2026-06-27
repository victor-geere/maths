---
title: Generating Functions
tag: discrete
summary: Formal power series that encode sequences as coefficients, turning combinatorial identities into algebraic manipulations.
links:
  - combinations
  - recurrence-relations
  - power-series
  - catalan-numbers
---

# Generating Functions

A **generating function** encodes an entire sequence $a_0, a_1, a_2, \ldots$ as the coefficients of a formal power series $A(x) = \sum_{n=0}^\infty a_n x^n$. The power series is treated as an algebraic object — we can add, multiply, differentiate, and compose generating functions — and each operation corresponds to a combinatorial operation on the sequences. This converts combinatorial problems (counting structured objects, solving recurrences, proving identities) into algebraic problems about power series. Generating functions are one of the most powerful unifying tools in combinatorics: a single formula like $\frac{1}{1-x}$ encodes $1, 1, 1, \ldots$; $(1+x)^n$ encodes the binomial coefficients $\binom{n}{0}, \binom{n}{1}, \ldots, \binom{n}{n}$.

## Ordinary Generating Function (OGF)

$$A(x) = \sum_{n=0}^\infty a_n x^n = a_0 + a_1 x + a_2 x^2 + \cdots$$

The sequence $(a_n)$ is extracted by reading off coefficients: $a_n = [x^n] A(x)$.

## Exponential Generating Function (EGF)

$$\hat{A}(x) = \sum_{n=0}^\infty a_n \frac{x^n}{n!}$$

Used when the sequence counts labelled structures (permutations, trees with labelled nodes).

## Standard Generating Functions

| Sequence $a_n$ | OGF $A(x)$ |
|---|---|
| $1, 1, 1, \ldots$ | $\dfrac{1}{1-x}$ |
| $\binom{n}{k}$ (fixed $k$) | $\dfrac{x^k}{(1-x)^{k+1}}$ |
| $\binom{n+k}{k}$ | $\dfrac{1}{(1-x)^{k+1}}$ |
| Fibonacci: $0,1,1,2,3,5,\ldots$ | $\dfrac{x}{1-x-x^2}$ |
| Catalan: $1,1,2,5,14,\ldots$ | $\dfrac{1-\sqrt{1-4x}}{2x}$ |

## Key Operations

| Combinatorial operation | OGF operation |
|---|---|
| $a_n + b_n$ | $A(x) + B(x)$ |
| $a_n \cdot c$ | $c \cdot A(x)$ |
| $\sum_{k=0}^n a_k b_{n-k}$ (convolution) | $A(x) \cdot B(x)$ |
| $a_{n+1}$ (shift) | $(A(x) - a_0)/x$ |
| $n \cdot a_n$ | $x A'(x)$ |

## Solving Recurrences

To solve $a_n = 2a_{n-1} + 1$ with $a_0 = 0$: multiply by $x^n$, sum over $n$, substitute $A(x)$, solve:

$$A(x) = \frac{x}{(1-x)(1-2x)} = \frac{1}{1-2x} - \frac{1}{1-x}$$

Extract coefficients: $a_n = 2^n - 1$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $A(x)$ | ordinary generating function of sequence $(a_n)$ |
| $[x^n] A(x)$ | the coefficient of $x^n$ in $A(x)$ — extracts $a_n$ |
| OGF | ordinary generating function: $\sum a_n x^n$ |
| EGF | exponential generating function: $\sum a_n x^n/n!$ |
| Formal power series | a power series used algebraically, ignoring convergence |
| Convolution | $(a * b)_n = \sum_{k=0}^n a_k b_{n-k}$; corresponds to product of OGFs |
| $A'(x)$ | derivative of $A(x)$; coefficient of $x^n$ in $A'$ is $(n+1)a_{n+1}$ |
| Fibonacci sequence | $F_n = F_{n-1} + F_{n-2}$; $F_0=0$, $F_1=1$ |
| Catalan numbers | $C_n = \binom{2n}{n}/(n+1)$; OGF $= (1-\sqrt{1-4x})/(2x)$ |
| Partial fractions | decomposing a rational generating function to extract coefficients |
