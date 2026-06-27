---
title: Arithmetic Geometry
tag: algebraic-geometry
summary: The study of algebraic varieties over non-algebraically-closed fields, especially number fields and finite fields, combining algebraic geometry with number theory.
links:
  - schemes
  - elliptic-curves
  - etale-cohomology
  - number-fields
---

# Arithmetic Geometry

**Arithmetic geometry** is the branch of mathematics where algebraic geometry meets number theory: it studies algebraic varieties defined over fields like $\mathbb{Q}$ (the rationals), $\mathbb{Z}$ (the integers), number fields, finite fields $\mathbb{F}_p$, or $p$-adic fields $\mathbb{Q}_p$. The central questions are fundamentally arithmetic — how many rational or integer points does a variety have? What is the structure of those points? — but the tools are geometric. The Weil conjectures (proved by Deligne), Fermat's Last Theorem (Wiles), and the Birch and Swinnerton-Dyer conjecture all belong to arithmetic geometry. The framework of schemes over $\text{Spec}(\mathbb{Z})$ unifies the geometry of varieties over different fields through a single "arithmetic surface."

## The Arithmetic-Geometric Dictionary

| Arithmetic | Geometry |
|---|---|
| Integer/rational point on $V$ | Morphism $\text{Spec}(\mathbb{Z}) \to V$ or $\text{Spec}(\mathbb{Q}) \to V$ |
| Reduction mod $p$ | Fibre of $V/\mathbb{Z}$ over $\text{Spec}(\mathbb{F}_p)$ |
| $p$-adic point | Morphism $\text{Spec}(\mathbb{Q}_p) \to V$ |
| Galois action on points | Monodromy action on geometric fibres |
| Conductor of elliptic curve | Measures ramification at primes |

## Rational Points and Faltings' Theorem

**Faltings' theorem (Mordell conjecture, 1983):** A smooth projective curve $C$ of genus $g \geq 2$ over $\mathbb{Q}$ has **only finitely many rational points**.

This single theorem shows that most Diophantine equations have only finitely many solutions.

## Weil Conjectures

For a smooth projective variety $V$ over $\mathbb{F}_q$, the zeta function:

$$Z(V,t) = \exp\!\left(\sum_{n=1}^\infty \frac{\#V(\mathbb{F}_{q^n})}{n} t^n\right)$$

satisfies (Weil, conjectured; Deligne, proved 1974):

1. **Rationality:** $Z(V,t) \in \mathbb{Q}(t)$
2. **Functional equation:** relates $Z(V,t)$ and $Z(V, q^{-\dim V}t^{-1})$
3. **Riemann hypothesis:** poles and zeros lie on circles $|t| = q^{-i/2}$

## Arithmetic Surfaces

A **model** of a curve $C/\mathbb{Q}$ is a scheme $\mathcal{C} \to \text{Spec}(\mathbb{Z})$ with generic fibre $C$. Studying $\mathcal{C}$ encodes information about $C$ at all primes simultaneously.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Arithmetic geometry | algebraic geometry over number fields, finite fields, or mixed characteristic |
| Rational point | a point in $V(k)$ for some field $k$ (often $k=\mathbb{Q}$) |
| $\mathbb{F}_q$ | the finite field with $q = p^r$ elements |
| $\mathbb{Q}_p$ | the $p$-adic numbers |
| $\text{Spec}(\mathbb{Z})$ | the arithmetic line; the universal base for schemes |
| Faltings' theorem | genus $\geq 2$ curve over $\mathbb{Q}$ has finitely many rational points |
| Weil conjectures | rationality, functional equation, and Riemann hypothesis for $Z(V,t)$ |
| $Z(V,t)$ | the zeta function of $V$ over $\mathbb{F}_q$ |
| $\#V(\mathbb{F}_{q^n})$ | number of $\mathbb{F}_{q^n}$-rational points on $V$ |
| Model | a scheme over $\text{Spec}(\mathbb{Z})$ with a given generic fibre |
| Good/bad reduction | whether the fibre over $\text{Spec}(\mathbb{F}_p)$ is smooth |
