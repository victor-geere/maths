---
title: Fourier Analysis on Groups
tag: representation-theory
summary: Fourier analysis generalises from the circle to any locally compact abelian group via the Pontryagin dual, and to compact non-abelian groups via the Peter–Weyl expansion in matrix coefficients.
links:
  - peter-weyl
  - haar-measure
  - fourier-series
  - characters
  - pontryagin-duality
---

# Fourier Analysis on Groups

Classical Fourier analysis decomposes functions on $\mathbb{R}$ or $S^1$ into sinusoidal components. **Abstract harmonic analysis** extends this programme to arbitrary locally compact groups by using their representation theory. For a locally compact **abelian** group $G$, the role of frequencies is played by the **Pontryagin dual** $\hat{G}$ of continuous homomorphisms $G \to S^1$, and the Fourier transform is an isomorphism $L^2(G) \to L^2(\hat{G})$. For **compact non-abelian** groups, the Peter–Weyl theorem provides the analogue: $L^2(G)$ decomposes into matrix coefficient spaces of irreducible representations indexed by $\hat{G}$.

## Abelian Case: Pontryagin Duality

For a locally compact abelian group $G$, the **Pontryagin dual** is:
$$\hat{G} = \{\xi: G \to S^1 \mid \xi \text{ continuous homomorphism}\}$$

The **Fourier transform** is:
$$\hat{f}(\xi) = \int_G f(g)\,\overline{\xi(g)}\,d\mu(g)$$

**Plancherel theorem**: $\|f\|_{L^2(G)} = \|\hat{f}\|_{L^2(\hat{G})}$ — the Fourier transform is a unitary isomorphism.

**Examples**: $\widehat{\mathbb{R}} \cong \mathbb{R}$ (classical Fourier), $\widehat{S^1} \cong \mathbb{Z}$ (Fourier series), $\widehat{\mathbb{Z}/n\mathbb{Z}} \cong \mathbb{Z}/n\mathbb{Z}$ (DFT).

## Non-Abelian Case: Matrix Coefficient Expansion

For a compact group $G$ with irreducible unitary representations $\{\rho_\lambda\}$, the **non-abelian Fourier transform** of $f \in L^1(G)$ is the operator:
$$\hat{f}(\lambda) = \int_G f(g)\,\rho_\lambda(g)\,d\mu(g) \in \mathrm{End}(V_\lambda)$$

**Inversion formula**: $f(g) = \sum_{\lambda \in \hat{G}} \dim(V_\lambda)\,\mathrm{tr}(\hat{f}(\lambda)\rho_\lambda(g)^*)$

## Convolution Theorem

The Fourier transform converts convolution to multiplication (or operator composition):
$$\widehat{f * h}(\lambda) = \hat{f}(\lambda)\,\hat{h}(\lambda)$$

where $(f * h)(g) = \int_G f(x)h(x^{-1}g)\,d\mu(x)$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\hat{G}$ | Pontryagin dual (abelian case) or unitary dual (non-abelian) |
| $\xi: G \to S^1$ | character of abelian group: continuous group homomorphism |
| $\hat{f}(\xi)$ | Fourier transform of $f$ at frequency $\xi$ |
| Plancherel theorem | Fourier transform is a unitary isomorphism $L^2(G) \to L^2(\hat{G})$ |
| $\hat{f}(\lambda)$ | non-abelian Fourier transform: an operator in $\mathrm{End}(V_\lambda)$ |
| Inversion formula | recovers $f(g)$ from $\{\hat{f}(\lambda)\}$ |
| Convolution $f*h$ | $\int_G f(x)h(x^{-1}g)\,d\mu(x)$ |
| Convolution theorem | $\widehat{f*h}(\lambda) = \hat{f}(\lambda)\hat{h}(\lambda)$ |
| $S^1$ | unit circle group: $\{e^{i\theta}\} \subset \mathbb{C}^\times$ |
