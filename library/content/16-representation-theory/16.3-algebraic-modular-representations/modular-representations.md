---
title: Modular Representations
tag: representation-theory
summary: Modular representation theory studies representations of groups over fields of characteristic p dividing the group order, where Maschke's theorem fails and the theory is far richer and more subtle.
links:
  - linear-representations
  - algebraic-groups
  - highest-weight
  - characters
---

# Modular Representations

**Modular representation theory** studies representations of a finite group $G$ over a field $k$ whose characteristic $p$ divides $|G|$. In this setting, Maschke's theorem fails: not every representation is completely reducible, and there exist **indecomposable** representations that are not direct sums of simpler ones. The theory is far richer and more complicated than the characteristic-0 case, and has deep connections to algebraic geometry (via algebraic groups in characteristic $p$), algebraic topology (via stable module categories), and number theory (via the $p$-adic Langlands programme). Key invariants include the **decomposition matrix** relating ordinary and modular characters, the **Brauer characters**, and the block theory.

## Failure of Complete Reducibility

In characteristic $p \mid |G|$, the averaging operator $\frac{1}{|G|}\sum_{g\in G} \rho(g)$ is undefined. A classic example: for $G = \mathbb{Z}/p\mathbb{Z}$ acting on $k^2$ via $1 \mapsto \begin{pmatrix}1&1\\0&1\end{pmatrix}$, this 2-dimensional representation has a 1-dimensional subrepresentation but no complement.

## Indecomposable vs Irreducible

A representation is:
- **Irreducible**: no proper non-zero subrepresentation.
- **Indecomposable**: cannot be written as $V_1 \oplus V_2$ with $V_i \neq 0$.

In characteristic 0, irreducible $\Leftrightarrow$ indecomposable (for finite groups). In characteristic $p$, indecomposables can be much more complex.

## Brauer Characters & Decomposition Matrix

The **Brauer character** $\phi_S$ of an irreducible mod-$p$ representation $S$ is defined by lifting eigenvalues to characteristic 0. The **decomposition matrix** $D = (d_{\chi S})$ records how ordinary irreducibles $\chi$ decompose modulo $p$ into modular irreducibles $S$: $[\chi \downarrow p : S] = d_{\chi S}$.

## Block Theory

Representations split into **blocks** — indecomposable two-sided ideals of the group algebra $kG$. Each block has a **defect group** $D \leq G$ (a $p$-subgroup) that controls its complexity.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Characteristic $p$ | the field satisfies $1+1+\cdots+1 = 0$ ($p$ times) |
| $p \mid |G|$ | $p$ divides the group order; Maschke's theorem fails |
| Indecomposable representation | not a direct sum of proper subrepresentations |
| Brauer character $\phi_S$ | characteristic-0 lift of the trace of a mod-$p$ representation |
| Decomposition matrix $D$ | encodes how ordinary characters reduce mod $p$ |
| Block | indecomposable two-sided ideal of $kG$ |
| Defect group | $p$-subgroup $D$ measuring complexity of a block |
| $kG$ | group algebra of $G$ over field $k$ |
| Complete reducibility | every subrepresentation has a complement (fails when $p\mid|G|$) |
