---
title: Duality of Lᵖ
tag: measure-theory
summary: For 1 < p < ∞, the dual Banach space of Lᵖ(μ) is Lᵖ'(μ) where 1/p + 1/p' = 1; every bounded linear functional on Lᵖ is given by integration against a unique Lᵖ' function.
links:
  - lp-spaces
  - minkowskis-inequality
  - radon-nikodym
  - hahn-banach
---

# Duality of Lᵖ

For $1 < p < \infty$, the **dual space** $(L^p(\mu))^*$ — the Banach space of bounded linear functionals on $L^p$ — is isometrically isomorphic to $L^{p'}(\mu)$, where $p' = p/(p-1)$ is the **conjugate exponent** ($1/p + 1/p' = 1$). Every bounded linear functional $\Lambda: L^p \to \mathbb{R}$ has the form $\Lambda(f) = \int fg\,d\mu$ for a unique $g \in L^{p'}$, and $\|\Lambda\| = \|g\|_{p'}$. This is the **Riesz representation theorem** for $L^p$ spaces, proved via the Radon–Nikodym theorem. The endpoints are different: $(L^1)^* = L^\infty$ (for $\sigma$-finite $\mu$), but $(L^\infty)^* \supsetneq L^1$ in general (there are bounded functionals on $L^\infty$ not given by $L^1$ functions).

## Statement

**Theorem (Riesz)**: For $1 \leq p < \infty$ and $\sigma$-finite $(X,\mathcal{F},\mu)$:
$$(L^p(\mu))^* \cong L^{p'}(\mu) \quad \text{isometrically}$$
via the duality pairing $\langle f, g\rangle = \int fg\,d\mu$.

Every $\Lambda \in (L^p)^*$ is $\Lambda(f) = \int f g\,d\mu$ for unique $g \in L^{p'}$ with $\|\Lambda\| = \|g\|_{p'}$.

## Conjugate Exponents

$\frac{1}{p} + \frac{1}{p'} = 1$: so $p' = \frac{p}{p-1}$.

| $p$ | $p'$ |
|---|---|
| 1 | $\infty$ |
| 2 | 2 (self-dual) |
| 4 | 4/3 |
| $\infty$ | 1 |

## Proof Idea

Given $\Lambda \in (L^p)^*$, define $\nu(A) = \Lambda(\mathbf{1}_A)$; show $\nu \ll \mu$; apply Radon–Nikodym to get $g = d\nu/d\mu$; verify $g \in L^{p'}$ and $\|\Lambda\| = \|g\|_{p'}$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $(L^p)^*$ | dual space: bounded linear functionals $L^p \to \mathbb{R}$ |
| Conjugate exponent $p'$ | $1/p + 1/p' = 1$ |
| Duality pairing $\langle f,g\rangle$ | $\int fg\,d\mu$ |
| Isometric isomorphism | bijective linear map preserving norms |
| $\|\Lambda\| = \sup_{\|f\|_p=1}|\Lambda(f)|$ | operator norm |
| Riesz representation | $(L^p)^* \cong L^{p'}$ via integration |
| Self-dual | $L^2$ is self-dual ($p=p'=2$) |
| $(L^1)^* = L^\infty$ | bounded functions represent all $L^1$ functionals |
| $(L^\infty)^* \supsetneq L^1$ | $L^\infty$ has "extra" functionals from finitely additive measures |
