---
title: Reducibility & Degrees
tag: logic
summary: Many-one and Turing reducibility compare the relative difficulty of computational problems; Turing degrees partition all problems by computational equivalence, with the halting problem at degree 0' and a rich infinite structure above.
links:
  - halting-problem
  - turing-machines
  - recursive-functions
  - p-vs-np
---

# Reducibility & Degrees

**Reducibility** is the relation "$A$ is no harder to compute than $B$": if we could solve $B$, we could solve $A$. The two main notions are **many-one reducibility** ($A \leq_m B$: instances of $A$ map to instances of $B$ by a computable function) and **Turing reducibility** ($A \leq_T B$: $A$ is computable by a TM with oracle access to $B$). The equivalence classes under $\leq_T$ are called **Turing degrees** (or **degrees of unsolvability**). The degree of decidable problems is $\mathbf{0}$; the halting problem has degree $\mathbf{0'}$ (one jump above $\mathbf{0}$). The structure of Turing degrees is enormously complex — it contains incomparable elements, a dense linear order, and many other features studied in degree theory.

## Many-One Reducibility

$A \leq_m B$ if there is a computable total function $f: \Sigma^* \to \Sigma^*$ such that $w \in A \iff f(w) \in B$ for all $w$.

If $A \leq_m B$ and $B$ is decidable, then $A$ is decidable.
If $A \leq_m B$ and $A$ is undecidable, then $B$ is undecidable.

## Turing Reducibility

$A \leq_T B$ if $A$ is computable by a TM with an **oracle** for $B$ (can query membership in $B$ in one step).

$A \equiv_T B$ (Turing equivalent) if $A \leq_T B$ and $B \leq_T A$.

## The Jump Operator

The **Turing jump** $A' = \{\langle M \rangle : M^A\text{ halts on }\langle M \rangle\}$ (the halting problem relativised to oracle $A$) satisfies:
- $A <_T A'$ (strictly harder than $A$)
- $\mathbf{0'} = $ degree of $HALT$
- $\mathbf{0''} = $ degree of $HALT^{HALT}$, etc.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $A \leq_m B$ | many-one reducibility: $w \in A \iff f(w) \in B$ for computable $f$ |
| $A \leq_T B$ | Turing reducibility: $A$ computable with oracle $B$ |
| Oracle | black-box able to answer membership queries for $B$ |
| Turing degree | equivalence class under $\equiv_T$ |
| $\mathbf{0}$ | degree of decidable (computable) sets |
| $\mathbf{0'}$ | degree of halting problem |
| Turing jump $A'$ | halting problem relativised to $A$ |
| Incomparable degrees | $A \not\leq_T B$ and $B \not\leq_T A$ |
| Degree theory | study of the structure of Turing degrees |
