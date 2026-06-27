---
title: Modules over Rings
tag: commutative-algebra
summary: A module over a ring is a generalisation of a vector space where the scalars form a ring rather than a field; modules are the central objects of homological algebra and commutative algebra.
links:
  - ring-axioms
  - ideals
  - tensor-products
  - exact-sequences
  - projective-injective
---

# Modules over Rings

A **module** over a ring $R$ is a generalisation of a vector space in which the scalars come from a ring rather than a field. Just as vector spaces are the fundamental objects of linear algebra, modules are the fundamental objects of homological and commutative algebra. Virtually every algebraic structure — ideals, group representations, sheaves of $\mathcal{O}_X$-modules, chain complexes — can be expressed as a module. The theory of modules over a ring encodes a great deal of the ring's structure: for a field, all modules are free (vector spaces); for $\mathbb{Z}$, modules are abelian groups; for $k[x]$, finitely generated modules correspond to linear operators and their Jordan form.

## Definition

A **left $R$-module** is an abelian group $(M, +)$ together with a scalar multiplication $R \times M \to M$, $(r, m) \mapsto r \cdot m$, satisfying:
- $r(m + n) = rm + rn$
- $(r+s)m = rm + sm$
- $(rs)m = r(sm)$
- $1_R m = m$

## Examples

| Ring $R$ | Modules over $R$ |
|---|---|
| Field $k$ | $k$-vector spaces |
| $\mathbb{Z}$ | abelian groups |
| $k[x]$ | $k$-vector spaces with a chosen linear operator |
| $R$ itself | ideals (as submodules), $R/I$ (quotient modules) |

## Free, Projective, Injective Modules

- **Free module**: $M \cong R^n$; has a basis.
- **Projective**: direct summand of a free module; $\mathrm{Hom}(P,-)$ is exact.
- **Injective**: $\mathrm{Hom}(-,I)$ is exact.

## Module Homomorphisms

An $R$-module homomorphism $f: M \to N$ is a map of abelian groups with $f(rm) = rf(m)$ for all $r \in R$, $m \in M$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $R$-module $M$ | abelian group with $R$-action satisfying ring-action axioms |
| $R^n$ | free module of rank $n$: $R$-linear combinations of $n$ generators |
| Submodule | $R$-stable subgroup $N \subseteq M$ |
| Quotient module $M/N$ | cosets of $N$ in $M$, with induced $R$-action |
| $\mathrm{Hom}_R(M,N)$ | set of $R$-module homomorphisms $M \to N$ |
| $R$-module homomorphism | group homomorphism commuting with $R$-action |
| Free module | has a free basis; $\cong R^n$ |
| Projective module | direct summand of a free module |
| Injective module | $\mathrm{Hom}(-,I)$ is exact |
| Torsion element | $m \in M$ with $rm = 0$ for some non-zero $r$ |
