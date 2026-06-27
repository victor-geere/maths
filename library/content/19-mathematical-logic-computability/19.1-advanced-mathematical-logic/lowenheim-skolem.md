---
title: Löwenheim–Skolem Theorems
tag: logic
summary: The Löwenheim–Skolem theorems show that any first-order theory with an infinite model has models of every infinite cardinality, implying that first-order logic cannot pin down the size of its models.
links:
  - structures-models
  - compactness-logic
  - completeness-theorem
  - countability
---

# Löwenheim–Skolem Theorems

The **Löwenheim–Skolem theorems** reveal a fundamental limitation of first-order logic: it cannot control the cardinality of its models. If a first-order theory has an infinite model, it has models of **every** infinite cardinality. The **downward** theorem (Löwenheim 1915, Skolem 1920) says any satisfiable theory in a countable language has a countable model; the **upward** theorem (Tarski, Skolem) says any theory with an infinite model has models of every larger cardinality. This leads to **Skolem's paradox**: set theory (which proves the existence of uncountable sets) has a countable model — yet within that model, sets appear uncountable because no bijection to $\mathbb{N}$ exists *inside* the model.

## Downward Löwenheim–Skolem Theorem

If $\mathcal{M}$ is an $\mathcal{L}$-structure with $|\mathcal{L}| \leq \kappa$ and $A \subseteq M$ with $|A| \leq \kappa$, there is an **elementary substructure** $\mathcal{N} \preceq \mathcal{M}$ with $A \subseteq N$ and $|N| \leq \kappa$.

**Corollary**: Any satisfiable countable theory has a countable model.

## Upward Löwenheim–Skolem Theorem

If $\mathcal{M}$ is an infinite $\mathcal{L}$-structure and $\kappa \geq |\mathcal{L}| + |M| + \aleph_0$, there is an elementary extension $\mathcal{N} \succeq \mathcal{M}$ with $|N| = \kappa$.

## Elementary Substructure

$\mathcal{N} \preceq \mathcal{M}$ (elementary substructure) means $N \subseteq M$ and for every formula $\varphi(x_1,\ldots,x_n)$ and $a_i \in N$: $\mathcal{N} \models \varphi(a_1,\ldots,a_n) \iff \mathcal{M} \models \varphi(a_1,\ldots,a_n)$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathcal{N} \preceq \mathcal{M}$ | $\mathcal{N}$ is an elementary substructure of $\mathcal{M}$ |
| Elementary extension | $\mathcal{N} \succeq \mathcal{M}$: $\mathcal{M} \preceq \mathcal{N}$ |
| $\kappa$ | an infinite cardinal |
| $\aleph_0$ | cardinality of $\mathbb{N}$ |
| Downward L–S | satisfiable countable theory has countable model |
| Upward L–S | infinite models exist in all larger cardinalities |
| Skolem's paradox | ZFC has countable model yet proves uncountable sets exist |
| Categoricity | theory has exactly one model of some cardinality up to isomorphism |
