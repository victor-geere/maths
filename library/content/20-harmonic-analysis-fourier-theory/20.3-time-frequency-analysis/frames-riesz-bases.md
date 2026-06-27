---
title: Frames & Riesz Bases
tag: harmonic-analysis
summary: A frame in a Hilbert space is a generalisation of an orthonormal basis allowing redundancy; Riesz bases are stable non-orthogonal bases, and frames provide stable signal representations with overcompleteness.
links:
  - wavelets
  - hilbert-spaces
  - fourier-series
  - uncertainty-principle
---

# Frames & Riesz Bases

A **frame** is a generalisation of an orthonormal basis in a Hilbert space that allows **redundancy** (overcomplete systems) while still providing stable signal representations. A collection $\{e_k\}_{k \in K}$ in a Hilbert space $H$ is a **frame** if there exist constants $0 < A \leq B < \infty$ (frame bounds) such that:
$$A\|f\|^2 \leq \sum_{k} |\langle f, e_k\rangle|^2 \leq B\|f\|^2 \quad \forall f \in H$$
Frames allow **stable reconstruction** of $f$ from its measurements $\{\langle f, e_k\rangle\}$, even when the $e_k$ are not orthogonal and may be linearly dependent. **Riesz bases** are frames that are also Schauder bases (no redundancy), characterised as bounded invertible images of orthonormal bases. Frames are essential in signal processing (oversampled filter banks), compressed sensing, and quantum information.

## Definitions

**Frame**: $\{e_k\}$ satisfies $A\|f\|^2 \leq \sum_k|\langle f,e_k\rangle|^2 \leq B\|f\|^2$ for all $f \in H$.

**Tight frame**: $A = B$; then $f = \frac{1}{A}\sum_k \langle f, e_k\rangle e_k$.

**Parseval frame** (unit tight frame): $A = B = 1$.

**Riesz basis**: $\{e_k\}$ is a frame and a Schauder basis; equivalently, $\{Te_k\}$ is an ONB for some invertible $T$.

## Frame Operator

The **frame operator** $S: H \to H$, $Sf = \sum_k \langle f, e_k\rangle e_k$, is bounded, positive, and invertible (for a frame). **Reconstruction**: $f = \sum_k \langle f, S^{-1}e_k\rangle e_k = \sum_k \langle f, e_k\rangle S^{-1}e_k$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Frame $\{e_k\}$ | $A\|f\|^2 \leq \sum|\langle f,e_k\rangle|^2 \leq B\|f\|^2$ |
| Frame bounds $A, B$ | $0 < A \leq B < \infty$ |
| Tight frame | $A = B$ |
| Parseval frame | $A = B = 1$ |
| Redundancy | more vectors than needed for a basis |
| Riesz basis | frame that is a Schauder basis; image of ONB under invertible $T$ |
| Frame operator $S$ | $Sf = \sum_k\langle f,e_k\rangle e_k$; positive invertible |
| Dual frame $\{S^{-1}e_k\}$ | allows reconstruction $f = \sum\langle f,e_k\rangle S^{-1}e_k$ |
| Gabor frame | frame from STFT atoms $\{M_{m\beta}T_{n\alpha}g\}$ |
| Wavelet frame | frame from dilated/translated wavelets |
