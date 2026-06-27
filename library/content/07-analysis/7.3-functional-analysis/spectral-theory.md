---
title: Spectral Theory
tag: functional-analysis
summary: The study of the spectrum of a linear operator — the generalisation of eigenvalues to infinite-dimensional spaces.
links:
  - bounded-operators
  - hilbert-spaces
  - spectral-theorem
  - eigenvalues
---

# Spectral Theory

In finite-dimensional linear algebra, every linear operator has **eigenvalues** — scalars $\lambda$ for which $Tv = \lambda v$ has a non-zero solution. **Spectral theory** generalises this to infinite-dimensional spaces, where the situation is richer and more subtle. The **spectrum** of an operator $T$ on a Banach or Hilbert space consists of all complex scalars $\lambda$ for which $T - \lambda I$ fails to be invertible — but this can happen in three genuinely different ways (point spectrum, continuous spectrum, residual spectrum). Spectral theory is the mathematical foundation of quantum mechanics (where observables are self-adjoint operators and their spectra are the possible measurement outcomes) and plays a central role in the analysis of PDEs, signal processing, and operator algebras.

## Resolvent and Spectrum

For $T \in \mathcal{B}(X)$ (bounded operator on a Banach space $X$):

The **resolvent set** $\rho(T) = \{\lambda \in \mathbb{C} : (T - \lambda I)^{-1} \text{ exists and is bounded}\}$.

The **spectrum** $\sigma(T) = \mathbb{C} \setminus \rho(T)$.

The **resolvent** at $\lambda \in \rho(T)$: $R(\lambda, T) = (T - \lambda I)^{-1}$.

## Parts of the Spectrum

| Part | Condition on $T - \lambda I$ |
|---|---|
| **Point spectrum** $\sigma_p(T)$ | not injective: $\exists\, v \neq 0$, $(T-\lambda I)v = 0$ — a genuine eigenvalue |
| **Continuous spectrum** $\sigma_c(T)$ | injective, dense range, but not surjective |
| **Residual spectrum** $\sigma_r(T)$ | injective, range not dense |

## Spectral Radius

$$r(T) = \sup_{\lambda \in \sigma(T)}|\lambda| = \lim_{n\to\infty}\|T^n\|^{1/n}$$

For $T \in \mathcal{B}(X)$, $\sigma(T)$ is always a **non-empty compact subset** of $\mathbb{C}$ contained in the disk $|\lambda| \leq \|T\|$.

## Spectral Theorem for Compact Self-Adjoint Operators

If $T$ is compact and self-adjoint on a Hilbert space $H$, then:

- The spectrum consists of **real** eigenvalues accumulating only at $0$.
- There is an **orthonormal basis** of eigenvectors: $H = \bigoplus_n \ker(T - \lambda_n I)$.
- $T = \sum_n \lambda_n \langle \cdot, e_n\rangle e_n$ (spectral decomposition).

## Quantum Mechanics Connection

In quantum mechanics, each observable is a self-adjoint operator $A$ on a Hilbert space. The spectrum $\sigma(A)$ is the set of **possible measurement outcomes**. The spectral theorem guarantees a complete set of states (eigenvectors) for each observable.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\sigma(T)$ | spectrum of $T$: scalars where $T - \lambda I$ is not invertible |
| $\rho(T)$ | resolvent set: scalars where $(T-\lambda I)^{-1}$ exists and is bounded |
| $R(\lambda, T)$ | resolvent operator $(T-\lambda I)^{-1}$ |
| Point spectrum $\sigma_p$ | eigenvalues — $T - \lambda I$ is not injective |
| Continuous spectrum $\sigma_c$ | injective with dense but non-closed range |
| Residual spectrum $\sigma_r$ | injective with non-dense range |
| Spectral radius $r(T)$ | supremum of $|\lambda|$ over the spectrum |
| Compact operator | maps bounded sets to precompact sets; a "small" infinite-dimensional operator |
| Self-adjoint | $T = T^*$ (Hermitian); has real spectrum |
| $T^*$ | adjoint operator: $\langle Tv, w\rangle = \langle v, T^*w\rangle$ |
| Spectral decomposition | $T = \sum \lambda_n P_n$ where $P_n$ are orthogonal projections |
| Observable (QM) | a self-adjoint operator whose spectrum gives possible measurement values |
