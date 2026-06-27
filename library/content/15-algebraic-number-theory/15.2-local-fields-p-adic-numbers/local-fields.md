---
title: Local Fields
tag: algebraic-number-theory
summary: Complete discrete valuation fields with finite residue field — the building blocks of local class field theory and the local counterparts of number fields.
links:
  - p-adic-numbers
  - p-adic-absolute-value
  - hensels-lemma
  - adeles-ideles
---

# Local Fields

A **local field** is a complete discretely valued field with a finite residue field. The two main examples are: the $p$-adic numbers $\mathbb{Q}_p$ (characteristic 0) and the Laurent series $\mathbb{F}_q((t))$ over a finite field (positive characteristic). Every finite extension of $\mathbb{Q}_p$ is again a local field. Local fields are "local" in the sense of algebraic geometry — they see the arithmetic of a number field at a single prime — and the **local-global principle** says that to solve an equation over $\mathbb{Q}$, necessary conditions come from each local field $\mathbb{Q}_p$ and from $\mathbb{R}$. Local class field theory gives a complete description of all abelian extensions of a local field in terms of its multiplicative group.

## Definition

A **local field** is a non-discrete locally compact topological field. Equivalently, it is:

- A complete discrete valuation field $F$ with finite residue field $\kappa$, or
- A finite extension of $\mathbb{Q}_p$ or $\mathbb{F}_p((t))$

## Discrete Valuation

A **discrete valuation** on a field $F$ is a surjective group homomorphism $v : F^* \to \mathbb{Z}$ satisfying:

$$v(x+y) \geq \min(v(x), v(y))$$

with $v(0) = +\infty$.

The **valuation ring** is $\mathcal{O} = \{x : v(x) \geq 0\}$ with **maximal ideal** $\mathfrak{m} = \{x : v(x) > 0\}$ and **residue field** $\kappa = \mathcal{O}/\mathfrak{m}$.

## Structure of Local Fields

| Local field | Char | Residue field $\kappa$ | Uniformiser $\pi$ |
|---|---|---|---|
| $\mathbb{Q}_p$ | 0 | $\mathbb{F}_p$ | $p$ |
| $\mathbb{Q}_p(\sqrt{p})$ | 0 | $\mathbb{F}_p$ | $\sqrt{p}$ |
| $\mathbb{F}_q((t))$ | $p$ | $\mathbb{F}_q$ | $t$ |

## Local Class Field Theory

For a local field $F$, there is a canonical isomorphism (the **local Artin map**):

$$\text{Art}_F : F^\times \xrightarrow{\sim} \text{Gal}(F^{\text{ab}}/F)$$

from the multiplicative group to the Galois group of the maximal abelian extension. This is local class field theory.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Local field | complete discrete valuation field with finite residue field |
| Discrete valuation $v$ | $v : F^* \to \mathbb{Z}$; surjective group homomorphism |
| Valuation ring $\mathcal{O}$ | $\{x \in F : v(x) \geq 0\}$ |
| Maximal ideal $\mathfrak{m}$ | $\{x \in \mathcal{O} : v(x) > 0\} = (\pi)$ |
| Uniformiser $\pi$ | element with $v(\pi) = 1$; generates $\mathfrak{m}$ |
| Residue field $\kappa = \mathcal{O}/\mathfrak{m}$ | finite field at the local field |
| $F^{\text{ab}}$ | maximal abelian extension of $F$ |
| Local Artin map $\text{Art}_F$ | isomorphism $F^\times \xrightarrow{\sim} \text{Gal}(F^{\text{ab}}/F)$ |
| Locally compact | every point has a compact neighbourhood |
| $\mathbb{F}_q((t))$ | formal Laurent series over $\mathbb{F}_q$; char $p$ local field |
