---
title: Field Extensions
tag: abstract-algebra
summary: Larger fields containing a given field as a subfield, classified by degree.
links:
  - field-axioms
  - galois-theory
  - polynomial-rings
---

## Definition

$E$ is a **field extension** of $F$ (written $E/F$) if $F \subseteq E$ and $E$ is a field.

$E$ is naturally a vector space over $F$; its dimension is the **degree**:

$$[E : F] = \dim_F E$$

The extension is **finite** if $[E:F] < \infty$.

## Algebraic Extensions

An element $\alpha \in E$ is **algebraic over $F$** if it satisfies a polynomial $f \in F[x]$. The unique monic irreducible polynomial it satisfies is its **minimal polynomial**.

$$[F(\alpha) : F] = \deg(\text{min poly of } \alpha)$$

## Tower Law

For $F \subseteq K \subseteq E$:

$$[E : F] = [E : K] \cdot [K : F]$$

## Examples

- $[\mathbb{C} : \mathbb{R}] = 2$ (basis: $\{1, i\}$; minimal poly of $i$: $x^2+1$).
- $[\mathbb{Q}(\sqrt{2}) : \mathbb{Q}] = 2$.
- $[\mathbb{Q}(\sqrt[3]{2}) : \mathbb{Q}] = 3$.

## Splitting Fields

The **splitting field** of $f \in F[x]$ is the smallest extension of $F$ over which $f$ factors completely into linear factors.

## Notes

- Algebraic closures (e.g. $\overline{\mathbb{Q}}$) are the "maximal" algebraic extensions.
- Field extensions are the setting for Galois theory and solving polynomial equations.
