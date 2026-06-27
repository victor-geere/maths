---
title: Structures & Models
tag: logic
summary: A structure is a set equipped with interpretations of the symbols in a formal language; a model is a structure in which a given set of sentences is true, forming the basis of model theory.
links:
  - completeness-theorem
  - compactness-logic
  - first-order-logic
  - lowenheim-skolem
---

# Structures & Models

A **structure** (or **interpretation**) for a first-order language $\mathcal{L}$ consists of a non-empty set $M$ (the **domain** or **universe**) together with interpretations of each symbol: constants $c$ become elements $c^M \in M$, function symbols $f$ become functions $f^M: M^n \to M$, and relation symbols $R$ become subsets $R^M \subseteq M^n$. A **model** of a theory $T$ is a structure $\mathcal{M}$ in which every sentence of $T$ is true. Model theory studies the relationship between syntactic theories and their semantic models, asking: which theories have models? how many? of what sizes? The compactness theorem and Löwenheim–Skolem theorems give the basic answers.

## Formal Definitions

A **first-order language** $\mathcal{L}$ consists of constant symbols, function symbols (each with an arity), relation symbols (each with an arity), logical connectives, quantifiers $\forall, \exists$, and variables.

An **$\mathcal{L}$-structure** $\mathcal{M} = (M, \ldots)$ assigns:
- to each constant $c$: an element $c^\mathcal{M} \in M$
- to each $n$-ary function $f$: a function $f^\mathcal{M}: M^n \to M$
- to each $n$-ary relation $R$: a set $R^\mathcal{M} \subseteq M^n$

## Satisfaction

For a sentence $\varphi$ and structure $\mathcal{M}$, write $\mathcal{M} \models \varphi$ ("$\mathcal{M}$ satisfies $\varphi$") defined recursively:
- $\mathcal{M} \models R(a_1,\ldots,a_n)$ iff $(a_1,\ldots,a_n) \in R^\mathcal{M}$
- $\mathcal{M} \models \varphi \land \psi$ iff $\mathcal{M} \models \varphi$ and $\mathcal{M} \models \psi$
- $\mathcal{M} \models \forall x\,\varphi(x)$ iff $\mathcal{M} \models \varphi(a)$ for all $a \in M$

## Elementary Equivalence

$\mathcal{M} \equiv \mathcal{N}$ (elementarily equivalent) if they satisfy exactly the same first-order sentences. Isomorphic structures are elementarily equivalent, but not conversely.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathcal{L}$-structure $\mathcal{M}$ | domain $M$ with interpretations of all $\mathcal{L}$-symbols |
| Domain / Universe $M$ | underlying set of a structure |
| $c^\mathcal{M}$ | interpretation of constant $c$ |
| $R^\mathcal{M}$ | interpretation of relation $R$ as a subset of $M^n$ |
| $\mathcal{M} \models \varphi$ | $\mathcal{M}$ satisfies sentence $\varphi$ |
| Model of $T$ | structure satisfying every sentence in theory $T$ |
| Elementary equivalence $\equiv$ | same first-order theory |
| $\mathcal{M} \cong \mathcal{N}$ | isomorphic structures |
| Theory $T$ | set of sentences closed under logical consequence |
