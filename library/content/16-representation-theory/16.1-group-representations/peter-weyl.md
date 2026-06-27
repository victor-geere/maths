---
title: Peter–Weyl Theorem
tag: representation-theory
summary: The Peter–Weyl theorem decomposes L²(G) for a compact group G into an orthogonal direct sum of finite-dimensional irreducible representation spaces, generalising the Fourier series decomposition.
links:
  - haar-measure
  - fourier-on-groups
  - hilbert-spaces
  - linear-representations
  - characters
---

# Peter–Weyl Theorem

The **Peter–Weyl theorem** is the fundamental structure theorem for the representation theory of compact groups. It states that the Hilbert space $L^2(G)$ of square-integrable functions on a compact group $G$ (with respect to Haar measure) decomposes as a completed orthogonal direct sum of finite-dimensional subspaces, one for each irreducible unitary representation. This generalises Fourier series (which decomposes $L^2(S^1)$ into exponentials $e^{in\theta}$) and finite-group representation theory (where every function on $G$ expands in terms of matrix coefficients of irreducible representations). The theorem underlies virtually all of harmonic analysis on compact groups.

## Statement

Let $G$ be a compact Hausdorff group with normalised Haar measure. Let $\{(\rho_\lambda, V_\lambda)\}_{\lambda \in \hat{G}}$ be a complete set of (pairwise inequivalent) irreducible unitary representations.

**Peter–Weyl Theorem**: There is an orthogonal decomposition of Hilbert spaces:
$$L^2(G) \cong \widehat{\bigoplus_{\lambda \in \hat{G}}} V_\lambda \otimes V_\lambda^*$$

Concretely, the **matrix coefficient functions** $u^\lambda_{ij}(g) = \langle e_i, \rho_\lambda(g)e_j \rangle$ (for an orthonormal basis $\{e_i\}$ of $V_\lambda$) form an orthogonal basis of $L^2(G)$, with:
$$\langle u^\lambda_{ij}, u^\mu_{kl} \rangle_{L^2(G)} = \frac{\delta_{\lambda\mu}\delta_{ik}\delta_{jl}}{\dim V_\lambda}$$

## Consequences

- Every continuous function on $G$ can be uniformly approximated by linear combinations of matrix coefficients (**density**).
- Every irreducible unitary representation of $G$ is **finite-dimensional**.
- The **characters** $\chi_\lambda(g) = \mathrm{tr}(\rho_\lambda(g))$ form an orthonormal basis of the space of square-integrable class functions.

## Example: $G = S^1$

The irreducible representations of $S^1 = \{e^{i\theta}\}$ are $\rho_n(e^{i\theta}) = e^{in\theta}$, $n \in \mathbb{Z}$. Peter–Weyl recovers the classical Fourier series decomposition $L^2(S^1) \cong \widehat{\bigoplus}_{n \in \mathbb{Z}} \mathbb{C} e_n$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $L^2(G)$ | square-integrable functions on $G$ w.r.t. Haar measure |
| $\hat{G}$ | unitary dual: set of equivalence classes of irreducible unitary reps |
| $V_\lambda \otimes V_\lambda^*$ | tensor product of rep space and its dual |
| Matrix coefficient $u^\lambda_{ij}(g)$ | $\langle e_i, \rho_\lambda(g)e_j\rangle$; entry of rep matrix |
| Orthogonal decomposition | $\widehat{\bigoplus}$: completed (Hilbert-space) direct sum |
| Unitary representation | $\rho(g)$ is unitary for all $g$: $\rho(g)^* = \rho(g)^{-1}$ |
| $\chi_\lambda$ | character: $\chi_\lambda(g) = \mathrm{tr}(\rho_\lambda(g))$ |
| Class function | function constant on conjugacy classes |
| Density | matrix coefficients are dense in $C(G)$ and $L^2(G)$ |
