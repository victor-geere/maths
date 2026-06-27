---
title: Infinity-Categories (∞-categories)
tag: category-theory
summary: Generalisations of categories where morphisms exist at every level — objects, morphisms, 2-morphisms, … — with all compositions coherently associative up to homotopy.
links:
  - 2-categories
  - simplicial-complexes
  - homotopy-theory
  - topos-theory
---

# Infinity-Categories (∞-categories)

An **$\infty$-category** (or $(\infty, 1)$-category) is a mathematical structure that has morphisms at every level — objects are 0-morphisms, arrows are 1-morphisms, homotopies between arrows are 2-morphisms, homotopies between homotopies are 3-morphisms, and so on — with all compositions being associative and unital only **up to coherent homotopy**. The key insight, due to Boardman–Vogt, May, Segal, and Lurie, is that homotopy theory is intrinsically categorical at this level. $\infty$-categories encompass classical categories (where all $n$-morphisms for $n \geq 2$ are identities), topological spaces (viewed as $\infty$-groupoids), and the derived categories of homological algebra. Jacob Lurie's work in Higher Topos Theory and Higher Algebra placed $\infty$-categories at the foundation of modern algebraic geometry and derived algebraic geometry.

## Motivation

Classical categories have a defect: two objects can be "the same" in more than one way (isomorphism), but the category remembers only that an isomorphism exists, not the isomorphism itself. $\infty$-categories fix this by keeping track of all the choices coherently.

## Models

Several equivalent models exist:

| Model | Description |
|---|---|
| Quasi-categories (Joyal/Lurie) | Simplicial sets satisfying the inner horn filling condition |
| Segal spaces (Rezk) | Simplicial spaces with Segal and completeness conditions |
| Simplicially-enriched categories | Categories where hom-sets are simplicial sets |
| Kan complexes | $\infty$-groupoids (all morphisms invertible) |

## Quasi-Categories (Joyal Model)

A **quasi-category** is a simplicial set $X$ such that every **inner horn** $\Lambda^n_k \hookrightarrow \Delta^n$ ($0 < k < n$) has a filler — a morphism $\Delta^n \to X$ extending the horn.

The vertices $X_0$ are **objects**, the 1-simplices $X_1$ are **morphisms**, and the 2-simplices encode composition up to homotopy.

## $\infty$-Groupoids

An $\infty$-groupoid is a quasi-category where all morphisms are invertible. By the **homotopy hypothesis** (Grothendieck), $\infty$-groupoids are equivalent to homotopy types (topological spaces up to weak homotopy equivalence).

## Applications

- **Derived algebraic geometry:** sheaves on schemes are $\infty$-categorical
- **Topological field theory:** extended TFTs take values in $(\infty,n)$-categories
- **Homological algebra:** stable $\infty$-categories generalise triangulated categories

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\infty$-category | a category with coherent morphisms at all levels |
| $(\infty,1)$-category | $\infty$-category where all $k$-morphisms for $k \geq 2$ are invertible |
| $(\infty,n)$-category | $\infty$-category where $k$-morphisms for $k > n$ are invertible |
| Quasi-category | simplicial set with inner horn filling — Joyal's model |
| $\Delta^n$ | the standard $n$-simplex (as a simplicial set) |
| $\Lambda^n_k$ | the $k$-th inner horn of $\Delta^n$ (removing the $k$-th face) |
| Inner horn filling | the key lifting condition defining quasi-categories |
| $\infty$-groupoid | $\infty$-category where all morphisms are invertible |
| Homotopy hypothesis | $\infty$-groupoids $\simeq$ homotopy types |
| Weak homotopy equivalence | map inducing isomorphisms on all homotopy groups |
| Stable $\infty$-category | an $\infty$-category with a zero object and suspensions; generalises derived categories |
