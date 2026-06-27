---
title: Étale Cohomology
tag: algebraic-geometry
summary: A cohomology theory for algebraic varieties over fields of arbitrary characteristic, constructed from étale covers to avoid the pathologies of Zariski cohomology.
links:
  - sheaf-cohomology
  - arithmetic-geometry
  - schemes
---

# Étale Cohomology

**Étale cohomology** is a cohomology theory for algebraic varieties that works over fields of any characteristic, including positive characteristic $p$. It was developed by Grothendieck and his school in the 1960s to prove the Weil conjectures, which required a cohomological Lefschetz trace formula analogous to the one from topology. The key idea: replace the open sets of the Zariski topology (which are too coarse) with **étale maps** — the algebraic analogue of local isomorphisms. For a prime $\ell \neq \text{char}(k)$, the $\ell$-adic étale cohomology $H^i_{\text{ét}}(X_{\bar{k}}, \mathbb{Z}_\ell)$ carries a natural Galois action and recovers (over $\mathbb{C}$) the singular cohomology of the associated complex manifold. Deligne's proof of the Riemann hypothesis for varieties over finite fields (Weil conjectures, 1974) rests entirely on étale cohomology.

## Étale Maps

A morphism $f : X \to Y$ of schemes is **étale** if it is smooth of relative dimension 0: locally it looks like $\text{Spec}(A[x]/(g)) \to \text{Spec}(A)$ where $g$ is a polynomial with invertible derivative.

Étale maps are the algebraic analogue of local diffeomorphisms: they are local isomorphisms in a suitable sense.

## Étale Site

The **étale site** of $X$ is the category of étale maps $U \to X$, with covers being collections of étale maps $\{U_i \to U\}$ that are jointly surjective. Sheaves on this site give étale sheaves.

## $\ell$-adic Cohomology

For a prime $\ell \neq \text{char}(k)$:

$$H^i_{\text{ét}}(X_{\bar{k}}, \mathbb{Z}_\ell) = \varprojlim_n H^i_{\text{ét}}(X_{\bar{k}}, \mathbb{Z}/\ell^n\mathbb{Z})$$

## Key Properties

- **Base change:** behaves well under field extensions and base change
- **Galois action:** the absolute Galois group $\text{Gal}(\bar{k}/k)$ acts on $H^i_\text{ét}$
- **Comparison theorem:** over $\mathbb{C}$: $H^i_\text{ét}(X_\mathbb{C}, \mathbb{Z}_\ell) \cong H^i(X(\mathbb{C}), \mathbb{Z}) \otimes \mathbb{Z}_\ell$
- **Lefschetz trace formula:** $\#X(\mathbb{F}_q) = \sum_i (-1)^i \text{Tr}(\text{Frob}_q | H^i_\text{ét}(X_{\bar{\mathbb{F}}_q}, \mathbb{Q}_\ell))$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Étale map | smooth morphism of relative dimension 0; algebraic local isomorphism |
| Étale site | the category of étale covers used to define sheaves |
| $\ell$ | a prime different from $\text{char}(k)$; the coefficient ring characteristic |
| $H^i_\text{ét}(X, \mathbb{Z}_\ell)$ | $\ell$-adic étale cohomology |
| $\mathbb{Z}_\ell$ | $\ell$-adic integers: $\varprojlim \mathbb{Z}/\ell^n\mathbb{Z}$ |
| $\mathbb{Q}_\ell = \mathbb{Z}_\ell[1/\ell]$ | $\ell$-adic numbers |
| $\text{Gal}(\bar{k}/k)$ | absolute Galois group; acts on étale cohomology |
| Frobenius $\text{Frob}_q$ | the $q$-power map; a generator of $\text{Gal}(\bar{\mathbb{F}}_q/\mathbb{F}_q)$ |
| Lefschetz trace formula | $\#X(\mathbb{F}_q) = \sum(-1)^i\text{Tr}(\text{Frob}|H^i_\text{ét})$ |
| Weil conjectures | rationality, functional equation, Riemann hypothesis for zeta functions |
| $\varprojlim$ | inverse limit (projective limit) |
