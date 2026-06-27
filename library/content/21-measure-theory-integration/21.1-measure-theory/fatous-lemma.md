---
title: Fatou's Lemma
tag: measure-theory
summary: Fatou's lemma states that for non-negative measurable functions, the integral of the pointwise liminf is at most the liminf of the integrals; it is the key step in proving the MCT and DCT.
links:
  - lebesgue-integral
  - monotone-convergence
  - dominated-convergence
  - measure-spaces
---

# Fatou's Lemma

**Fatou's lemma** (Pierre Fatou, 1906) is a fundamental inequality in measure theory relating the integral of a limit inferior to the limit inferior of the integrals. For non-negative measurable functions $f_n \geq 0$:
$$\int_X \liminf_{n\to\infty} f_n\,d\mu \leq \liminf_{n\to\infty}\int_X f_n\,d\mu$$
This is a one-sided result: the integral of the $\liminf$ cannot exceed the $\liminf$ of the integrals, but it may be strictly smaller (mass can "escape to infinity"). Fatou's lemma is the key tool in proving the Monotone Convergence Theorem and the Dominated Convergence Theorem, and it provides the fundamental obstruction to interchanging integrals and limits for general sequences.

## Statement

**Fatou's Lemma**: Let $f_n: X \to [0,\infty]$ be measurable. Then:
$$\int_X \liminf_{n\to\infty} f_n\,d\mu \leq \liminf_{n\to\infty}\int_X f_n\,d\mu$$

## Proof

Set $g_k = \inf_{n \geq k} f_n$. Then $g_k \leq f_n$ for $n \geq k$, so $\int g_k \leq \int f_n$ for $n \geq k$, thus $\int g_k \leq \inf_{n \geq k}\int f_n$. Taking $k \to \infty$: $g_k \nearrow \liminf f_n$, so by MCT: $\int\liminf f_n = \lim_k\int g_k \leq \liminf_n\int f_n$. $\square$

## Where Equality Fails

Take $f_n = \mathbf{1}_{[n,n+1]}$ on $\mathbb{R}$ with Lebesgue measure. Then $\liminf f_n = 0$ everywhere, so $\int \liminf f_n = 0$, but $\int f_n = 1$ for all $n$, so $\liminf \int f_n = 1 > 0$. Mass escaped to $+\infty$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\liminf_{n}f_n(x)$ | $\lim_{k\to\infty}\inf_{n\geq k}f_n(x)$; smallest cluster value |
| $\liminf_{n}\int f_n$ | $\lim_{k\to\infty}\inf_{n\geq k}\int f_n$ |
| $g_k = \inf_{n\geq k}f_n$ | monotone increasing approximation |
| Fatou's inequality | $\int\liminf f_n \leq \liminf\int f_n$ |
| Mass escape | loss of mass as $f_n$ concentrates near $\pm\infty$ |
| Non-negativity | essential; Fatou fails for general real-valued $f_n$ |
| Reverse Fatou | $\limsup\int f_n \leq \int\limsup f_n$ if $f_n \leq g \in L^1$ |
