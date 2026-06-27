---
title: Hilbert's Basis Theorem
tag: commutative-algebra
summary: Hilbert's basis theorem states that if R is Noetherian then R[x] is Noetherian, implying polynomial rings over fields or ℤ in finitely many variables are Noetherian and every ideal is finitely generated.
links:
  - noetherian-rings
  - ring-axioms
  - ideals
  - polynomial-rings
---

# Hilbert's Basis Theorem

**Hilbert's Basis Theorem** (1888) states that if $R$ is a Noetherian commutative ring, then the polynomial ring $R[x]$ is also Noetherian. By induction, $R[x_1, \ldots, x_n]$ is Noetherian for any $n$. In particular, $k[x_1, \ldots, x_n]$ is Noetherian for any field $k$, meaning every ideal in a polynomial ring over a field is finitely generated. This was revolutionary: before Hilbert's proof, generating sets of invariants were constructed by explicit, often painful computation; Hilbert proved existence non-constructively. The theorem is the foundational result ensuring that algebraic varieties are defined by finitely many equations.

## Statement

**Theorem (Hilbert, 1888)**: If $R$ is a Noetherian ring, then $R[x]$ is Noetherian.

**Corollary**: $k[x_1, \ldots, x_n]$ is Noetherian for any field $k$ and any $n \geq 0$. Every ideal in $k[x_1,\ldots,x_n]$ is finitely generated.

## Proof Sketch

Suppose $I \subseteq R[x]$ is an ideal. Let $I_d = \{\text{leading coefficients of degree-}d\text{ elements of }I\} \cup \{0\}$. Then $I_0 \subseteq I_1 \subseteq \cdots$ is an ascending chain of ideals in $R$, which stabilises at some $N$ since $R$ is Noetherian. Choose finitely many generators for each $I_d$, $d \leq N$, and lift these to elements of $I$. One shows these finitely many polynomials generate all of $I$.

## Applications

- Every affine variety over $k$ is the zero locus of finitely many polynomials.
- The ring of polynomial invariants $k[V]^G$ of a finite group $G$ is finitely generated (by Noether's theorem, a consequence).
- In algebraic geometry: coherent sheaves on Noetherian schemes have finitely generated stalks.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Noetherian ring | every ideal is finitely generated (ACC holds) |
| $R[x]$ | polynomial ring: polynomials in $x$ with coefficients in $R$ |
| $k[x_1,\ldots,x_n]$ | polynomial ring in $n$ variables over field $k$ |
| Finitely generated ideal | $I = (f_1,\ldots,f_r)$ for finitely many generators |
| Leading coefficient | coefficient of the highest-degree term |
| Ascending chain condition | every chain $I_1 \subseteq I_2 \subseteq \cdots$ stabilises |
| Ring of invariants $k[V]^G$ | polynomials invariant under group $G$ action |
| Noether's theorem (algebra) | $k[V]^G$ is finitely generated when $G$ is finite |
