---
title: Pontryagin Duality
tag: harmonic-analysis
summary: Pontryagin duality states that every locally compact abelian group G is canonically isomorphic to the dual of its dual group Ĝ; it is the abstract version of Fourier inversion and unifies all classical Fourier transforms.
links:
  - fourier-on-groups
  - fourier-transform
  - haar-measure
  - fourier-series
---

# Pontryagin Duality

**Pontryagin duality** (1934) is the fundamental duality theorem for locally compact abelian (LCA) groups. Given an LCA group $G$, its **Pontryagin dual** $\hat{G} = \mathrm{Hom}(G, S^1)$ is the group of continuous homomorphisms $G \to S^1$ (characters), with the compact-open topology. Pontryagin duality asserts that $\hat{\hat{G}} \cong G$ canonically (the double dual is $G$ itself). This theorem unifies all classical Fourier dualities: $\hat{\mathbb{R}} \cong \mathbb{R}$ (classical Fourier transform), $\hat{\mathbb{T}} \cong \mathbb{Z}$ (Fourier series), $\hat{\mathbb{Z}} \cong \mathbb{T}$ (discrete Fourier), $\hat{\mathbb{Z}/N\mathbb{Z}} \cong \mathbb{Z}/N\mathbb{Z}$ (DFT). The Plancherel theorem for LCA groups — $\|\hat{f}\|_{L^2(\hat{G})} = \|f\|_{L^2(G)}$ — is a corollary.

## Pontryagin Dual

For an LCA group $G$, its dual:
$$\hat{G} = \{\xi: G \to S^1 \mid \xi \text{ continuous homomorphism}\}$$
with pointwise multiplication and compact-open topology, is itself a LCA group.

## Duality Theorem

**Theorem**: The canonical evaluation map $\iota: G \to \hat{\hat{G}}$, $\iota(g)(\xi) = \xi(g)$, is a topological group isomorphism $G \cong \hat{\hat{G}}$.

## Examples

| $G$ | $\hat{G}$ | Fourier theory |
|---|---|---|
| $\mathbb{R}$ | $\mathbb{R}$ | Fourier transform |
| $\mathbb{T} = \mathbb{R}/\mathbb{Z}$ | $\mathbb{Z}$ | Fourier series |
| $\mathbb{Z}$ | $\mathbb{T}$ | discrete Fourier series |
| $\mathbb{Z}/N\mathbb{Z}$ | $\mathbb{Z}/N\mathbb{Z}$ | DFT |
| $\mathbb{Q}_p$ | $\mathbb{Q}_p$ | $p$-adic Fourier |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| LCA group | locally compact abelian topological group |
| Character $\xi: G \to S^1$ | continuous group homomorphism |
| $\hat{G}$ | Pontryagin dual: group of characters of $G$ |
| $\hat{\hat{G}} \cong G$ | Pontryagin duality theorem |
| Compact-open topology | topology on $\hat{G}$ from compact subsets of $G$ |
| Fourier transform on $G$ | $\hat{f}(\xi) = \int_G f(g)\overline{\xi(g)}\,d\mu(g)$ |
| Plancherel for LCA | $\|f\|_{L^2(G)} = \|\hat{f}\|_{L^2(\hat{G})}$ |
| $S^1$ | unit circle: $\{z \in \mathbb{C} : |z| = 1\}$ |
