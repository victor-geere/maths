---
title: Ext & Tor Functors
tag: homological-algebra
summary: Ext and Tor are the derived functors of Hom and ⊗, measuring the failure of these functors to be exact and encoding the homological complexity of modules over a ring.
links:
  - modules
  - exact-sequences
  - projective-injective
  - free-resolutions
  - derived-functors
  - chain-complexes
---

# Ext & Tor Functors

**$\mathrm{Ext}^n_R(M, N)$** and **$\mathrm{Tor}_n^R(M, N)$** are the derived functors of $\mathrm{Hom}_R(M, -)$ and $M \otimes_R -$ respectively. While $\mathrm{Hom}$ is left-exact and $\otimes$ is right-exact, neither is fully exact in general; $\mathrm{Ext}$ and $\mathrm{Tor}$ measure the failure of exactness in a systematic way. They are computed by taking projective (or free) resolutions of $M$ and applying the functor, then taking homology. $\mathrm{Ext}^1(M, N)$ classifies extensions of $M$ by $N$; $\mathrm{Tor}_1(M,N)$ measures the failure of $M \ (or $N$) to be flat. These invariants appear throughout algebra, topology (cohomology of groups, sheaf cohomology), and geometry.

## Computing Ext

Take a projective resolution $P_\bullet \to M \to 0$. Apply $\mathrm{Hom}_R(-,N)$ to get a cochain complex $P^\bullet$:
$$0 \to \mathrm{Hom}(P_0, N) \to \mathrm{Hom}(P_1, N) \to \cdots$$

Then $\mathrm{Ext}^n_R(M, N) = H^n(P^\bullet)$.

## Computing Tor

Take a projective resolution $P_\bullet \to M \to 0$. Apply $- \otimes_R N$:
$$\cdots \to P_1 \otimes N \to P_0 \otimes N \to 0$$

Then $\mathrm{Tor}_n^R(M, N) = H_n(P_\bullet \otimes N)$.

## Key Properties

- $\mathrm{Ext}^0(M,N) \cong \mathrm{Hom}_R(M,N)$; $\mathrm{Tor}_0(M,N) \cong M \otimes_R N$.
- $M$ is projective $\iff$ $\mathrm{Ext}^{\geq 1}(M,-) = 0$.
- $M$ is flat $\iff$ $\mathrm{Tor}_{\geq 1}(M,-) = 0$.
- $\mathrm{Ext}^1(M,N)$ classifies short exact sequences $0 \to N \to E \to M \to 0$.
- Long exact sequences: $\cdots \to \mathrm{Ext}^n(M,A) \to \mathrm{Ext}^n(M,B) \to \mathrm{Ext}^n(M,C) \to \mathrm{Ext}^{n+1}(M,A) \to \cdots$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathrm{Ext}^n_R(M,N)$ | $n$-th derived functor of $\mathrm{Hom}_R(M,-)$ |
| $\mathrm{Tor}_n^R(M,N)$ | $n$-th derived functor of $M \otimes_R -$ |
| Projective resolution $P_\bullet$ | $\cdots \to P_1 \to P_0 \to M \to 0$, $P_i$ projective |
| Cochain complex $P^\bullet$ | $\mathrm{Hom}(P_\bullet,N)$ with differentials reversed |
| $H^n(P^\bullet)$ | $n$-th cohomology: $\ker(d^n)/\mathrm{im}(d^{n-1})$ |
| $H_n(P_\bullet \otimes N)$ | $n$-th homology of tensored complex |
| Flat module | $\mathrm{Tor}_{\geq 1}(M,-) = 0$ |
| $\mathrm{Ext}^1$ classifies extensions | short exact sequences $0 \to N \to E \to M \to 0$ |
| Long exact sequence | sequence of $\mathrm{Ext}^n$ or $\mathrm{Tor}_n$ from short exact sequence |
| Global dimension | $\sup_M \mathrm{pd}(M)$; measures homological complexity of ring |
