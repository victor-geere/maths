---
title: Recurrence Relations
tag: algorithms
summary: Equations that define a sequence in terms of its earlier values — solved by characteristic roots, generating functions, or the Master Theorem.
links:
  - generating-functions
  - master-theorem
  - mathematical-induction
---

# Recurrence Relations

A **recurrence relation** defines each term of a sequence in terms of previous terms. They arise naturally wherever a problem of size $n$ reduces to smaller instances: the Fibonacci sequence, factorial, the running time of merge sort, and the number of moves in the Tower of Hanoi are all governed by recurrences. Solving a recurrence means finding a **closed-form expression** $a_n = f(n)$ in terms of $n$ alone, without reference to earlier terms. The three main techniques are the **characteristic root method** (for linear homogeneous recurrences), **generating functions** (for more complex cases), and the **Master Theorem** (for divide-and-conquer algorithms).

## Linear Homogeneous Recurrences with Constant Coefficients

$$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \cdots + c_k a_{n-k}$$

**Characteristic equation:** $r^k = c_1 r^{k-1} + \cdots + c_k$.

**Distinct roots $r_1, \ldots, r_k$:** general solution $a_n = A_1 r_1^n + A_2 r_2^n + \cdots + A_k r_k^n$.

**Repeated root $r$ of multiplicity $m$:** contributes $(A_0 + A_1 n + \cdots + A_{m-1}n^{m-1})r^n$.

## Examples

### Fibonacci
$F_n = F_{n-1} + F_{n-2}$, $F_0=0$, $F_1=1$.

Characteristic roots: $r = \frac{1 \pm \sqrt{5}}{2}$ (the golden ratio $\phi$ and $\hat{\phi}$).

$$F_n = \frac{\phi^n - \hat{\phi}^n}{\sqrt{5}}, \quad \phi = \frac{1+\sqrt{5}}{2}$$

### Tower of Hanoi
$T_n = 2T_{n-1} + 1$, $T_1 = 1$.

$$T_n = 2^n - 1$$

## Linear Non-Homogeneous

$a_n = c_1 a_{n-1} + \cdots + c_k a_{n-k} + f(n)$.

Solve the homogeneous part, then find a particular solution for $f(n)$.

## Divide-and-Conquer Recurrences

Of the form $T(n) = a\,T(n/b) + f(n)$ — solved by the Master Theorem.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $a_n$ | the $n$-th term of the sequence |
| Recurrence relation | an equation defining $a_n$ in terms of $a_{n-1}, a_{n-2}, \ldots$ |
| Closed form | an explicit formula for $a_n$ as a function of $n$ only |
| Characteristic equation | $r^k = c_1 r^{k-1}+\cdots+c_k$; roots determine the general solution |
| Characteristic root | a solution to the characteristic equation |
| $\phi$ (phi) | the golden ratio $(1+\sqrt{5})/2 \approx 1.618$ |
| Homogeneous | right-hand side depends only on earlier $a_i$, not an extra function of $n$ |
| Non-homogeneous | includes an additional "forcing" term $f(n)$ |
| Particular solution | a specific solution to the non-homogeneous recurrence |
| General solution | particular solution + general solution to the homogeneous part |
| Tower of Hanoi | classic puzzle with $T_n = 2^n-1$ moves |
| Fibonacci numbers | $F_0=0, F_1=1, F_n = F_{n-1}+F_{n-2}$ |
