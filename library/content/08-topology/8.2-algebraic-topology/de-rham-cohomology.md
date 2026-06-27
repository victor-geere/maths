---
title: de Rham Cohomology
tag: algebraic-topology
summary: Cohomology groups built from differential forms on smooth manifolds, related to singular cohomology by de Rham's theorem.
links:
  - differential-forms
  - singular-homology
  - euler-characteristic
  - smooth-manifolds
---

# de Rham Cohomology

**de Rham cohomology** uses the calculus of differential forms to define topological invariants of smooth manifolds. A **closed form** (with $d\omega = 0$) that is not **exact** (not of the form $d\eta$) witnesses a topological hole. The $k$-th de Rham cohomology group $H^k_{\text{dR}}(M)$ is the quotient of closed $k$-forms by exact $k$-forms, and it captures the $k$-dimensional holes of the manifold. The profound **de Rham's theorem** states that this purely analytic object is isomorphic to singular cohomology with real coefficients — connecting the smooth world of calculus to the combinatorial world of algebraic topology, and making computation via integration possible.

## Differential Forms and the Exterior Derivative

A **$k$-form** on a smooth manifold $M$ is a smooth alternating $k$-linear map on tangent vectors.

The **exterior derivative** $d : \Omega^k(M) \to \Omega^{k+1}(M)$ satisfies:

1. $d(f) = df$ (gradient) for $f \in \Omega^0$
2. $d \circ d = 0$ (key identity: $d^2 = 0$)
3. $d(\alpha \wedge \beta) = d\alpha \wedge \beta + (-1)^k \alpha \wedge d\beta$

## Closed and Exact Forms

- **Closed:** $\omega$ with $d\omega = 0$ — locally looks like $d\eta$
- **Exact:** $\omega = d\eta$ for some $(k-1)$-form $\eta$

Since $d^2 = 0$: every exact form is closed. The failure of the converse measures topology.

## de Rham Cohomology Groups

$$H^k_{\text{dR}}(M) = \frac{\ker(d : \Omega^k \to \Omega^{k+1})}{\text{im}(d : \Omega^{k-1} \to \Omega^k)} = \frac{Z^k}{B^k}$$

## de Rham's Theorem

$$H^k_{\text{dR}}(M) \cong H^k(M; \mathbb{R})$$

The de Rham cohomology is isomorphic to singular cohomology with $\mathbb{R}$ coefficients. The isomorphism is given by **integration**:

$$[\omega] \mapsto \left[\sigma \mapsto \int_\sigma \omega\right]$$

## Standard Examples

| Manifold $M$ | $H^0$ | $H^1$ | $H^2$ |
|---|---|---|---|
| $\mathbb{R}^n$ | $\mathbb{R}$ | $0$ | $0$ |
| $S^1$ | $\mathbb{R}$ | $\mathbb{R}$ | $0$ |
| $S^2$ | $\mathbb{R}$ | $0$ | $\mathbb{R}$ |
| $T^2$ | $\mathbb{R}$ | $\mathbb{R}^2$ | $\mathbb{R}$ |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\Omega^k(M)$ | space of smooth $k$-forms on $M$ |
| $d$ | exterior derivative: $\Omega^k \to \Omega^{k+1}$ |
| $d^2 = 0$ | key identity: $d(d\omega) = 0$ for all $\omega$ |
| Closed form | $\omega$ with $d\omega = 0$ |
| Exact form | $\omega = d\eta$ for some form $\eta$ |
| $Z^k$ | closed $k$-forms: $\ker(d : \Omega^k \to \Omega^{k+1})$ |
| $B^k$ | exact $k$-forms: $\text{im}(d : \Omega^{k-1} \to \Omega^k)$ |
| $H^k_{\text{dR}}(M)$ | $k$-th de Rham cohomology group: $Z^k/B^k$ |
| de Rham's theorem | $H^k_{\text{dR}}(M) \cong H^k(M;\mathbb{R})$ |
| $\wedge$ | exterior (wedge) product of differential forms |
| Integration pairing | $\int_\sigma \omega$ pairs a $k$-chain $\sigma$ with a $k$-form $\omega$ |
| Poincaré lemma | on $\mathbb{R}^n$: every closed form is exact (no holes) |
