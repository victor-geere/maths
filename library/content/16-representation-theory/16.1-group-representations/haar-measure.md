---
title: Haar Measure
tag: representation-theory
summary: Haar measure is a translation-invariant Borel measure on a locally compact group, unique up to scaling, that enables integration over groups and is the foundation of harmonic analysis.
links:
  - fourier-on-groups
  - peter-weyl
  - lebesgue-measure
  - topological-spaces
---

# Haar Measure

**Haar measure** is a canonical way to integrate functions on a locally compact topological group, generalising the Lebesgue measure on $\mathbb{R}^n$ and the counting measure on finite groups. It is the unique (up to positive scalar multiple) left-translation-invariant regular Borel measure on any locally compact Hausdorff group $G$. The existence and uniqueness of Haar measure is a foundational theorem of abstract harmonic analysis: it allows one to average functions over the group, define $L^2(G)$, and carry out Fourier analysis in full generality. For compact groups, Haar measure can be normalised to be a probability measure, enabling an elegant theory of representations.

## Definition

A **left Haar measure** on a locally compact group $G$ is a nonzero regular Borel measure $\mu$ satisfying **left invariance**:
$$\mu(gE) = \mu(E) \quad \text{for all } g \in G,\ E \subseteq G \text{ Borel}$$

where $gE = \{gh : h \in E\}$.

**Theorem (Haar, 1933)**: Every locally compact Hausdorff group $G$ admits a left Haar measure, unique up to a positive scalar.

## Examples

| Group $G$ | Haar measure $d\mu$ |
|---|---|
| $(\mathbb{R}^n, +)$ | Lebesgue measure $dx_1 \cdots dx_n$ |
| Finite group | counting measure: $\mu(E) = |E|$ |
| $S^1 = U(1)$ | arc-length $d\theta / 2\pi$ |
| $GL_n(\mathbb{R})$ | $|\det A|^{-n} dA$ (product of matrix entries) |

## Modular Function

In general, $\mu(Eg) \neq \mu(E)$: the right-translate of Haar measure may differ by a factor. The **modular function** $\Delta: G \to \mathbb{R}_{>0}$ measures this: $\mu(Eg) = \Delta(g)^{-1}\mu(E)$. A group is **unimodular** if $\Delta \equiv 1$ (left = right Haar measure). Compact and abelian groups are unimodular.

## Role in Representation Theory

For a compact group $G$ with normalised Haar measure ($\mu(G) = 1$), the Peter–Weyl theorem uses $L^2(G, \mu)$ as the arena for harmonic analysis, and the averaging operator $\frac{1}{\mu(G)}\int_G \rho(g)\,d\mu(g)$ projects onto $G$-fixed vectors, replacing the finite-group average $\frac{1}{|G|}\sum_g$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Locally compact group | topological group with compact neighbourhoods of every point |
| Borel measure | measure defined on the Borel $\sigma$-algebra |
| Left invariance | $\mu(gE) = \mu(E)$ for all $g \in G$ |
| $d\mu$ | integration with respect to Haar measure |
| Modular function $\Delta(g)$ | ratio $\mu(Eg)/\mu(E)$; measures failure of right invariance |
| Unimodular group | $\Delta \equiv 1$; left and right Haar measures coincide |
| $L^2(G, \mu)$ | square-integrable functions on $G$ w.r.t. Haar measure |
| Normalised Haar measure | choice with $\mu(G) = 1$, valid when $G$ is compact |
| Averaging operator | $f \mapsto \int_G \rho(g)f\,d\mu(g)$; projection onto invariants |
