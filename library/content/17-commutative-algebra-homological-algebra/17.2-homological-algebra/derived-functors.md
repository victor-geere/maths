---
title: Derived Functors
tag: homological-algebra
summary: Derived functors extend a left- or right-exact functor to a sequence of functors that measure its failure of exactness by applying it to resolutions; Ext and Tor are the canonical examples.
links:
  - modules
  - exact-sequences
  - projective-injective
  - free-resolutions
  - ext-tor
  - chain-complexes
---

# Derived Functors

A **derived functor** extends a functor $F$ that is only partially exact to a whole sequence $\{R^nF\}$ (right-derived) or $\{L_nF\}$ (left-derived) that together measure the obstruction to exactness. The idea is: replace the argument by a projective (or injective) resolution, apply $F$, and take homology. This produces a long exact sequence that connects values of $F$ at different modules, turning short exact sequences into long exact sequences in the derived functors. The most important examples are $\mathrm{Ext}^n = R^n\mathrm{Hom}(M,-)$ and $\mathrm{Tor}_n = L_n(M\otimes-)$; in topology and geometry, sheaf cohomology is $R^n\Gamma$ (the derived functor of global sections).

## Right-Derived Functors

Let $F: \mathcal{A} \to \mathcal{B}$ be a **left-exact** functor between abelian categories with enough injectives. Given $M \in \mathcal{A}$, choose an injective resolution $0 \to M \to I^0 \to I^1 \to \cdots$. Define:
$$R^nF(M) = H^n(F(I^\bullet))$$

This is independent of the choice of resolution.

## Left-Derived Functors

Let $F$ be **right-exact** and the category have enough projectives. For $M$, choose a projective resolution $\cdots \to P_1 \to P_0 \to M \to 0$. Define:
$$L_nF(M) = H_n(F(P_\bullet))$$

## Long Exact Sequence

Given $0 \to A \to B \to C \to 0$ short exact, derived functors produce:
$$0 \to FA \to FB \to FC \to R^1FA \to R^1FB \to R^1FC \to R^2FA \to \cdots$$

(for right-derived $F$) and analogously for left-derived.

## Key Examples

| Functor $F$ | $R^nF$ or $L_nF$ |
|---|---|
| $\mathrm{Hom}_R(M,-)$ | $\mathrm{Ext}^n_R(M,-)$ |
| $M \otimes_R -$ | $\mathrm{Tor}_n^R(M,-)$ |
| $\Gamma(X,-)$ (global sections) | $H^n(X,-)$ (sheaf cohomology) |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Left-exact functor | preserves $0 \to A \to B \to C$ |
| Right-exact functor | preserves $A \to B \to C \to 0$ |
| Injective resolution $I^\bullet$ | $0 \to M \to I^0 \to I^1 \to \cdots$, all $I^n$ injective |
| Projective resolution $P_\bullet$ | $\cdots \to P_1 \to P_0 \to M \to 0$, all $P_n$ projective |
| $R^nF(M)$ | right-derived: $H^n(F(I^\bullet))$ |
| $L_nF(M)$ | left-derived: $H_n(F(P_\bullet))$ |
| $R^0F \cong F$ | zeroth derived functor recovers $F$ |
| Long exact sequence | sequence of derived functor values from short exact sequence |
| Enough injectives/projectives | every object embeds in injective / is surjected from projective |
| $\delta$-functor | sequence of functors connected by long exact sequences |
