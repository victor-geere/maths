---
title: Completion & Formal Power Series
tag: commutative-algebra
summary: The completion of a ring at an ideal is a formal inverse limit that makes the ideal infinitesimally small, yielding power series rings and p-adic integers as key examples.
links:
  - localisation
  - prime-maximal-ideals
  - graded-rings
  - p-adic-numbers
---

# Completion & Formal Power Series

The **$I$-adic completion** $\hat{R}$ of a ring $R$ at an ideal $I$ is the inverse limit $\varprojlim R/I^n$, the ring of compatible sequences $(r_n)$ with $r_n \in R/I^n$ and $r_{n+1} \equiv r_n \pmod{I^n}$. Completion makes the ideal $I$ "infinitesimally small", replacing $R$ with a ring where elements can be expanded in power series in generators of $I$. The key examples are: the formal power series ring $k[[x]] = \hat{k[x]}_{(x)}$, and the $p$-adic integers $\mathbb{Z}_p = \hat{\mathbb{Z}}_{(p)}$. Completion converts local algebraic geometry into the study of formal power series and is the basis for $p$-adic analysis and Hensel's lemma.

## Construction

For $R$ Noetherian and $I = (a_1,\ldots,r)$:
$$\hat{R} = \varprojlim_{n} R/I^n = \{(r_1, r_2, \ldots) \in \prod R/I^n : r_{n+1} \equiv r_n \pmod{I^n}\}$$

There is a canonical ring map $\iota: R \to \hat{R}$, $r \mapsto (r \bmod I^n)_n$.

## Key Examples

| Ring $R$ | Ideal $I$ | Completion $\hat{R}$ |
|---|---|---|
| $\mathbb{Z}$ | $(p)$ | $\mathbb{Z}_p$ ($p$-adic integers) |
| $k[x]$ | $(x)$ | $k[[x]]$ (formal power series) |
| $k[x_1,\ldots,x_n]$ | $(x_1,\ldots,x_n)$ | $k[[x_1,\ldots,x_n]]$ |
| $\mathcal{O}_{X,p}$ (local ring of variety) | $\mathfrak{m}_p$ | formal neighbourhood of $p$ |

## Artin–Rees Lemma & Exactness

For Noetherian $R$ and finitely generated $M$, the $I$-adic topology on $M$ is separated and the completion is exact on finitely generated modules:
$$\widehat{M \otimes_R N} \cong \hat{M} \otimes_{\hat{R}} \hat{N}$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\hat{R}$ | $I$-adic completion of $R$ |
| $\varprojlim R/I^n$ | inverse limit: compatible sequences in quotients |
| $I^n$ | $n$-th power of ideal $I$ |
| $k[[x]]$ | formal power series: $\sum_{n\geq 0} a_n x^n$, $a_n \in k$ |
| $\mathbb{Z}_p$ | $p$-adic integers: completion of $\mathbb{Z}$ at $(p)$ |
| Canonical map $\iota: R \to \hat{R}$ | $r \mapsto (r\bmod I^n)_n$ |
| Artin–Rees lemma | controls how $I$-adic filtrations interact with submodules |
| Separated topology | $\bigcap_n I^n M = 0$ (Krull's theorem for Noetherian local rings) |
| Formal power series | element of $k[[x]]$: possibly non-convergent infinite sum |
