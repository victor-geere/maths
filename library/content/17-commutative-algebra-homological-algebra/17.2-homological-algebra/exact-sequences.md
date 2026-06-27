---
title: Exact Sequences
tag: homological-algebra
summary: An exact sequence is a chain of module homomorphisms where the image of each map equals the kernel of the next; exact sequences encode fundamental relationships between modules and are the backbone of homological algebra.
links:
  - modules
  - chain-complexes
  - ext-tor
  - free-resolutions
  - derived-functors
---

# Exact Sequences

An **exact sequence** is a sequence of module homomorphisms $\cdots \to A \xrightarrow{f} B \xrightarrow{g} C \to \cdots$ in which $\mathrm{im}(f) = \ker(g)$ at every module. Exact sequences are the primary language of homological algebra: they encode how modules fit together, generalise the first isomorphism theorem, and measure the failure of functors (like $\mathrm{Hom}$ and $\otimes$) to preserve algebraic structure. The **short exact sequence** $0 \to A \to B \to C \to 0$ captures extensions of $C$ by $A$, while **long exact sequences** in homology and cohomology are the main computational tool in algebraic topology and algebraic geometry.

## Definition

A sequence $\cdots \xrightarrow{f_{n-1}} M_n \xrightarrow{f_n} M_{n+1} \xrightarrow{f_{n+1}} \cdots$ is **exact at $M_n$** if $\mathrm{im}(f_{n-1}) = \ker(f_n)$.

It is **exact** if it is exact at every module.

## Short Exact Sequences

$$0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$$

This means: $f$ is injective, $g$ is surjective, and $\mathrm{im}(f) = \ker(g)$, i.e., $B$ is an **extension** of $C$ by $A$.

- **Split short exact sequence**: $B \cong A \oplus C$ (there exists a section $s: C \to B$ with $g \circ s = \mathrm{id}_C$).

## Long Exact Sequences

Applying a left-exact functor $F$ (like $\mathrm{Hom}_R(P,-)$) to a short exact sequence need not preserve exactness at the right. The failure is measured by **derived functors** giving a long exact sequence:
$$0 \to FA \to FB \to FC \to R^1FA \to R^1FB \to \cdots$$

## Snake Lemma

Given a commutative diagram with exact rows:
$$\begin{array}{ccccccc} 0 \to & A & \to & B & \to & C & \to 0 \\ & \downarrow f & & \downarrow g & & \downarrow h & \\ 0 \to & A' & \to & B' & \to & C' & \to 0 \end{array}$$
there is an exact **connecting homomorphism** $\delta: \ker(h) \to \mathrm{coker}(f)$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Exact sequence | $\mathrm{im}(f_n) = \ker(f_{n+1})$ at every module |
| Short exact sequence | $0 \to A \to B \to C \to 0$ |
| $\ker(f)$ | kernel: $\{m : f(m) = 0\}$ |
| $\mathrm{im}(f)$ | image: $\{f(m) : m \in M\}$ |
| $\mathrm{coker}(f)$ | cokernel: $N/\mathrm{im}(f)$ |
| Split exact sequence | $B \cong A \oplus C$ with a section |
| Extension of $C$ by $A$ | short exact sequence $0 \to A \to B \to C \to 0$ |
| Left-exact functor | preserves exactness at the first two terms |
| Long exact sequence | sequence arising from derived functors |
| Snake lemma | produces connecting homomorphism $\delta: \ker h \to \mathrm{coker} f$ |
