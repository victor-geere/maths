---
title: Schemes & Spec
tag: algebraic-geometry
summary: Schemes are the fundamental objects of modern algebraic geometry — locally ringed spaces built from prime spectra of commutative rings, unifying classical varieties over any field with arithmetic geometry over ℤ.
links:
  - sheaves
  - affine-varieties
  - morphisms-schemes
  - ring-axioms
---

# Schemes & Spec

A **scheme** is Grothendieck's central innovation: a geometric space built from commutative rings. The **spectrum** $\text{Spec}(R)$ of a ring $R$ consists of all prime ideals of $R$, equipped with the Zariski topology and a sheaf of rings $\mathcal{O}$ that encodes algebraic information locally. A general scheme is obtained by gluing affine schemes (spectra) along open subsets, just as a manifold is obtained by gluing open subsets of $\mathbb{R}^n$. This framework simultaneously handles classical varieties over algebraically closed fields, varieties over $\mathbb{Q}$, and arithmetic objects like $\text{Spec}(\mathbb{Z})$ — which is a "curve" whose "points" are the prime numbers. The scheme-theoretic language resolved decades of foundational difficulties and enabled the proof of the Weil conjectures and Fermat's Last Theorem.

## Spectrum of a Ring

For a commutative ring $R$:

$$\text{Spec}(R) = \{\mathfrak{p} \subseteq R : \mathfrak{p} \text{ is a prime ideal}\}$$

**Zariski topology:** the closed sets are $V(\mathfrak{a}) = \{\mathfrak{p} : \mathfrak{a} \subseteq \mathfrak{p}\}$ for ideals $\mathfrak{a} \subseteq R$.

**Structure sheaf** $\mathcal{O}$: on the basic open set $D(f) = \{\mathfrak{p} : f \notin \mathfrak{p}\}$:

$$\mathcal{O}(D(f)) = R_f = R\!\left[\frac{1}{f}\right]$$

## Affine Scheme

An **affine scheme** is a locally ringed space $(\text{Spec}(R), \mathcal{O})$ for some commutative ring $R$.

Key examples:
- $\text{Spec}(k) = \{(0)\}$: a single point (for a field $k$)
- $\text{Spec}(k[x]) = \mathbb{A}^1_k$: the affine line (one point per prime ideal)
- $\text{Spec}(\mathbb{Z})$: "the arithmetic line"; points $(p)$ for primes $p$ and generic point $(0)$

## General Scheme

A **scheme** $(X, \mathcal{O}_X)$ is a locally ringed space that can be covered by open sets $U_i$ with $(U_i, \mathcal{O}_X|_{U_i}) \cong (\text{Spec}(R_i), \mathcal{O}_{R_i})$ for commutative rings $R_i$.

## Geometric Points

The **geometric points** of $X$ over an algebraically closed field $\bar{k}$ are morphisms $\text{Spec}(\bar{k}) \to X$. These recover the classical points of a variety.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\text{Spec}(R)$ | prime spectrum of ring $R$: the set of prime ideals |
| $\mathfrak{p}$ | a prime ideal (a point of $\text{Spec}(R)$) |
| Zariski topology | open sets $D(f) = \{\mathfrak{p} : f \notin \mathfrak{p}\}$ |
| $D(f)$ | basic open set in $\text{Spec}(R)$: primes not containing $f$ |
| $\mathcal{O}$ | structure sheaf of the scheme |
| $R_f = R[1/f]$ | localisation of $R$ inverting $f$ |
| Locally ringed space | topological space with a sheaf of local rings |
| Affine scheme | $(\text{Spec}(R), \mathcal{O}_R)$ for some commutative ring $R$ |
| Generic point | the point $(0) \in \text{Spec}(R)$ for an integral domain $R$ |
| $\text{Spec}(\mathbb{Z})$ | the arithmetic line; points are prime numbers and $(0)$ |
| Geometric point | morphism $\text{Spec}(\bar{k}) \to X$ |
