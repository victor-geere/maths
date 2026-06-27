---
title: Systems of Linear Equations
tag: algebra
summary: Solving multiple simultaneous linear equations in several unknowns.
links:
  - row-reduction
  - matrix-multiplication
  - determinant
---

## General Form

A system of $m$ equations in $n$ unknowns:

$$a_{11}x_1 + \cdots + a_{1n}x_n = b_1$$
$$\vdots$$
$$a_{m1}x_1 + \cdots + a_{mn}x_n = b_m$$

Written in matrix form: $A\mathbf{x} = \mathbf{b}$.

## Solution Types

- **Unique solution:** exactly one $\mathbf{x}$ satisfies the system ($A$ has full column rank, $\mathbf{b}$ is consistent).
- **Infinitely many solutions:** system is underdetermined or has free variables.
- **No solution:** system is inconsistent ($\mathbf{b}$ not in the column space of $A$).

## Methods

### Substitution
Express one variable from one equation and substitute into the others. Practical for small systems.

### Elimination (Gaussian)
Add multiples of one equation to others to zero out variables. Equivalent to row-reducing the augmented matrix $[A|\mathbf{b}]$.

### Cramer's Rule
For $n \times n$ invertible $A$:

$$x_i = \frac{\det(A_i)}{\det(A)}$$

where $A_i$ is $A$ with the $i$-th column replaced by $\mathbf{b}$.

## Consistency via Rank

- System is **consistent** iff $\text{rank}(A) = \text{rank}([A|\mathbf{b}])$.
- Unique solution iff additionally $\text{rank}(A) = n$.

## Example

$$x + y = 3, \quad 2x - y = 0$$

Add equations: $3x = 3 \Rightarrow x = 1$, then $y = 2$.
