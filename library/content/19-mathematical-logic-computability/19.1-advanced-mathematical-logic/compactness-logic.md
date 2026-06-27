---
title: Compactness Theorem
tag: logic
summary: The compactness theorem states that a set of first-order sentences has a model if and only if every finite subset has a model; it is the principal tool for building non-standard models.
links:
  - completeness-theorem
  - structures-models
  - lowenheim-skolem
  - ultraproducts
---

# Compactness Theorem

The **compactness theorem** of first-order logic states: a set $\Sigma$ of first-order sentences has a model if and only if every **finite** subset of $\Sigma$ has a model. This is the most widely applied result in model theory. It says that satisfiability is a "finitary" property: you cannot rule out the existence of a model by any infinite, essentially infinitary argument. The name comes from the analogous topological fact that a product of compact spaces is compact (Stone space compactness). The compactness theorem is used to build non-standard models of arithmetic (containing "infinite" natural numbers), non-standard analysis (infinitesimals), and to show that many properties (e.g., being a finite group) are not first-order axiomatisable.

## Statement

**Compactness Theorem**: A set $\Sigma$ of first-order $\mathcal{L}$-sentences is satisfiable (has a model) if and only if every finite $\Sigma_0 \subseteq \Sigma$ is satisfiable.

## Applications

**Non-standard models of arithmetic**: Add constants $c > 0, c > 1, c > 2, \ldots$ to the language. Every finite subset of $\mathbb{N}$'s theory plus these sentences is satisfiable (use $c = n+1$ for each finite set). By compactness, there is a model containing an element larger than every standard natural number.

**Non-standard analysis**: Similarly add $0 < \epsilon < 1/n$ for all $n$; compactness gives a field with an infinitesimal $\epsilon$.

**Finiteness is not first-order**: No first-order theory axiomatises exactly the finite structures (by compactness, any such theory has an infinite model).

## Proof Sketch

Follows from the completeness theorem: $\Sigma$ is unsatisfiable $\Rightarrow$ $\Sigma$ is inconsistent $\Rightarrow$ some finite $\Sigma_0 \vdash \bot$ $\Rightarrow$ $\Sigma_0$ is unsatisfiable.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Satisfiable | has at least one model |
| Finitely satisfiable | every finite subset has a model |
| Compactness theorem | satisfiable $\Leftrightarrow$ finitely satisfiable |
| Non-standard model | model containing elements not in the "intended" model |
| Non-standard natural number | element $> n$ for every standard $n \in \mathbb{N}$ |
| Infinitesimal | element $\epsilon > 0$ with $\epsilon < 1/n$ for all standard $n$ |
| Stone space | topological space of ultrafilters; compactness of logic mirrors topology |
| $\Sigma_0 \vdash \bot$ | finite $\Sigma_0$ derives a contradiction |
