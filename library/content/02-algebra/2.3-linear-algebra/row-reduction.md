---
title: Row Reduction & Echelon Form
tag: linear-algebra
summary: The fundamental algorithm for solving linear systems and computing rank.
links:
  - linear-systems
  - basis-dimension
  - lu-decomposition
---

## Elementary Row Operations

1. **Swap** two rows: $R_i \leftrightarrow R_j$
2. **Scale** a row: $R_i \leftarrow cR_i$ ($c \neq 0$)
3. **Replace:** $R_i \leftarrow R_i + cR_j$

These operations preserve the solution set of a linear system.

## Row Echelon Form (REF)

A matrix is in **row echelon form** if:
- All zero rows are at the bottom.
- Each leading entry (pivot) is to the right of the pivot in the row above.

## Reduced Row Echelon Form (RREF)

Additionally:
- Each pivot is 1.
- Each pivot is the only non-zero entry in its column.

Every matrix has a unique RREF.

## Gaussian Elimination

Forward pass to REF, then back-substitution. **Gauss-Jordan** continues to RREF.

## Rank

The **rank** of a matrix = number of pivots in its REF = dimension of column space = dimension of row space.

**Rank-Nullity theorem:** for $A \in M_{m\times n}$:

$$\text{rank}(A) + \text{nullity}(A) = n$$

## Example

$$\begin{pmatrix}1&2&3\\2&4&7\\3&6&10\end{pmatrix} \xrightarrow{R_2-2R_1, R_3-3R_1} \begin{pmatrix}1&2&3\\0&0&1\\0&0&1\end{pmatrix} \xrightarrow{R_3-R_2} \begin{pmatrix}1&2&3\\0&0&1\\0&0&0\end{pmatrix}$$

Rank = 2, nullity = 1.
