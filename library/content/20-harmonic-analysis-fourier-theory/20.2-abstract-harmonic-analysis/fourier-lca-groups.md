---
title: Fourier Analysis on Locally Compact Groups
tag: harmonic-analysis
summary: Abstract harmonic analysis extends Fourier analysis from ℝ to all locally compact groups using Haar measure; for abelian groups this gives Pontryagin duality, and for compact groups the Peter–Weyl theorem.
links:
  - pontryagin-duality
  - haar-measure
  - peter-weyl
  - fourier-on-groups
---

# Fourier Analysis on Locally Compact Groups

**Abstract harmonic analysis** extends the classical Fourier transform from $\mathbb{R}$ to arbitrary locally compact groups using the invariant integration provided by Haar measure. For a locally compact abelian (LCA) group $G$, the Fourier transform $\hat{f}(\xi) = \int_G f(g)\overline{\xi(g)}\,d\mu(g)$ defines an $L^2$-isometry from $L^2(G)$ to $L^2(\hat{G})$ (Plancherel), and inversion recovers $f$. Pontryagin duality ($\hat{\hat{G}} \cong G$) is the algebraic backbone. For compact non-abelian groups, the Peter–Weyl theorem replaces the character group $\hat{G}$ with the unitary dual — the collection of irreducible unitary representations — and the Fourier transform becomes an operator-valued integral. This general framework encompasses signal processing on homogeneous spaces, quantum mechanics on Lie groups, and the representation theory of reductive groups.

## LCA Groups: Fourier Analysis

For $G$ LCA with Haar measure $\mu$ and Pontryagin dual $\hat{G}$:

$$\hat{f}(\xi) = \int_G f(g)\overline{\xi(g)}\,d\mu(g), \quad \xi \in \hat{G}$$

**Plancherel**: $\|f\|_{L^2(G)} = \|\hat{f}\|_{L^2(\hat{G})}$ (with dual Haar measure on $\hat{G}$).

**Inversion**: $f(g) = \int_{\hat{G}} \hat{f}(\xi)\xi(g)\,d\hat{\mu}(\xi)$.

## Compact Non-Abelian Groups

For compact group $G$ with unitary dual $\hat{G} = \{[\rho]\}$:
$$\hat{f}(\rho) = \int_G f(g)\rho(g)^*\,d\mu(g) \in \mathrm{End}(V_\rho)$$

Peter–Weyl: $L^2(G) \cong \widehat{\bigoplus}_{\rho \in \hat{G}} V_\rho \otimes V_\rho^*$.

## Convolution Algebra

$L^1(G)$ with convolution $(f*h)(g) = \int_G f(x)h(x^{-1}g)\,d\mu(x)$ is a Banach algebra (group algebra). Fourier transform is an algebra homomorphism $L^1(G) \to C_0(\hat{G})$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| LCA group | locally compact abelian group |
| Haar measure $\mu$ | left-invariant regular Borel measure on $G$ |
| $\hat{G}$ | Pontryagin dual (abelian) or unitary dual (general) |
| $\hat{f}(\xi)$ | Fourier transform; operator-valued for non-abelian $G$ |
| Plancherel formula | $\|f\|_{L^2(G)} = \|\hat{f}\|_{L^2(\hat{G})}$ |
| Inversion formula | recovers $f$ from $\hat{f}$ |
| Group algebra $L^1(G)$ | Banach algebra under convolution |
| Unitary dual $\hat{G}$ | irreducible unitary representations of $G$ |
| Peter–Weyl theorem | $L^2(G) \cong \bigoplus_{\rho} V_\rho \otimes V_\rho^*$ for compact $G$ |
