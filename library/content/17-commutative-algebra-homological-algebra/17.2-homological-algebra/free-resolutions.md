---
title: Free Resolutions
tag: homological-algebra
summary: A free resolution of a module M is an exact complex of free modules terminating at M; the length and structure of minimal free resolutions capture deep properties of M encoded in its Betti numbers.
links:
  - modules
  - exact-sequences
  - projective-injective
  - ext-tor
  - chain-complexes
---

# Free Resolutions

A **free resolution** of an $R$-module $M$ is an exact sequence:
$$\cdots \to F_2 \xrightarrow{d_2} F_1 \xrightarrow{d_1} F_0 \xrightarrow{\epsilon} M \to 0$$
where each $F_i$ is a **free $R$-module**. Every module admits a free resolution (just take $F_0$ to be a free module mapping onto $M$, then resolve the kernel, etc.). Free resolutions are the primary tool for computing derived functors $\mathrm{Ext}$ and $\mathrm{Tor}$, and their structure — especially in the case of graded modules over polynomial rings — encodes deep geometric and algebraic information via the **Betti numbers** $\beta_{i,j}(M) = \dim_k \mathrm{Tor}_i^R(M,k)_j$.

## Construction

Given $M$, choose a surjection $F_0 = R^{\beta_0} \twoheadrightarrow M$ (let $K_0 = \ker(F_0 \to M)$). Then choose $F_1 \twoheadrightarrow K_0$, giving $K_1 = \ker(F_1 \to K_0)$. Continue to get:
$$\cdots \to F_2 \to F_1 \to F_0 \to M \to 0$$

## Minimal Free Resolutions

Over a local ring $(R, \mathfrak{m})$ or a graded ring, a free resolution is **minimal** if all maps have entries in $\mathfrak{m}$ (no unit entries). Minimal resolutions are unique up to isomorphism.

**Betti numbers**: $\beta_i(M) = \mathrm{rank}(F_i)$ in the minimal free resolution.

## Hilbert's Syzygy Theorem

Over $R = k[x_1,\ldots,x_n]$, every finitely generated graded module has a **finite** free resolution of length $\leq n$. The **projective dimension** $\mathrm{pd}(M) \leq n$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Free resolution | exact sequence $\cdots \to F_1 \to F_0 \to M \to 0$ with $F_i$ free |
| Free module $F_i$ | isomorphic to $R^{\beta_i}$ |
| Syzygy | element of $\ker(F_i \to F_{i-1})$; a relation among relations |
| Minimal free resolution | maps have entries in $\mathfrak{m}$; unique up to isomorphism |
| Betti number $\beta_i(M)$ | rank of $F_i$ in minimal resolution; $= \dim_k \mathrm{Tor}_i(M,k)$ |
| $\mathrm{pd}(M)$ | projective dimension: length of shortest free resolution |
| Hilbert's syzygy theorem | $\mathrm{pd}(M) \leq n$ for modules over $k[x_1,\ldots,x_n]$ |
| Augmentation $\epsilon: F_0 \to M$ | the surjection starting the resolution |
| $d_i: F_i \to F_{i-1}$ | differential maps in the resolution |
