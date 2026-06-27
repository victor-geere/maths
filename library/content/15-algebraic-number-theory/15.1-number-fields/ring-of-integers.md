---
title: Ring of Integers
tag: algebraic-number-theory
summary: The ring 𝒪_K of algebraic integers in a number field K — the analogue of ℤ inside ℚ, in which unique factorisation of ideals (not elements) holds.
links:
  - number-fields
  - dedekind-domains
  - ideal-class-group
  - norm-trace-discriminant
---

# Ring of Integers

The **ring of integers** $\mathcal{O}_K$ of a number field $K$ is the subring of elements of $K$ that satisfy a monic polynomial equation with integer coefficients — the algebraic integers in $K$. It plays the role of $\mathbb{Z}$ inside $\mathbb{Q}$: just as $\mathbb{Z}$ is the "integer part" of $\mathbb{Q}$, $\mathcal{O}_K$ is the integer part of $K$. While elements of $\mathcal{O}_K$ generally do not factor uniquely into irreducibles (unlike $\mathbb{Z}$), **ideals** in $\mathcal{O}_K$ do factor uniquely into prime ideals — this is Dedekind's great discovery. The ring $\mathcal{O}_K$ is always a **Dedekind domain**, a Noetherian integrally closed domain of Krull dimension 1, and its structure determines most of the arithmetic of $K$.

## Definition

An element $\alpha \in K$ is an **algebraic integer** if it satisfies a monic polynomial with $\mathbb{Z}$ coefficients:

$$\alpha^n + a_{n-1}\alpha^{n-1} + \cdots + a_1\alpha + a_0 = 0, \quad a_i \in \mathbb{Z}$$

The **ring of integers** is:

$$\mathcal{O}_K = \{\alpha \in K : \alpha \text{ is an algebraic integer}\}$$

## Properties

- $\mathcal{O}_K$ is a **free $\mathbb{Z}$-module** of rank $[K:\mathbb{Q}] = n$: there exist $\omega_1, \ldots, \omega_n \in \mathcal{O}_K$ with $\mathcal{O}_K = \mathbb{Z}\omega_1 \oplus \cdots \oplus \mathbb{Z}\omega_n$
- $\mathcal{O}_K \otimes_\mathbb{Z} \mathbb{Q} = K$
- $\mathcal{O}_K \cap \mathbb{Q} = \mathbb{Z}$

## Standard Examples

| Field $K$ | $\mathcal{O}_K$ |
|---|---|
| $\mathbb{Q}$ | $\mathbb{Z}$ |
| $\mathbb{Q}(\sqrt{d})$, $d \equiv 2,3 \pmod 4$ | $\mathbb{Z}[\sqrt{d}]$ |
| $\mathbb{Q}(\sqrt{d})$, $d \equiv 1 \pmod 4$ | $\mathbb{Z}\!\left[\frac{1+\sqrt{d}}{2}\right]$ |
| $\mathbb{Q}(\zeta_n)$ | $\mathbb{Z}[\zeta_n]$ |
| $\mathbb{Q}(\sqrt[3]{2})$ | $\mathbb{Z}[\sqrt[3]{2}]$ |

## Integral Basis

An **integral basis** for $\mathcal{O}_K$ is a $\mathbb{Z}$-basis $\{\omega_1,\ldots,\omega_n\}$. The **discriminant** is $\text{disc}(K) = \det(\sigma_i(\omega_j))^2$ and measures ramification.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathcal{O}_K$ | ring of integers of number field $K$ |
| Algebraic integer | satisfies a monic polynomial with $\mathbb{Z}$ coefficients |
| $\mathbb{Z}$-module of rank $n$ | free abelian group of rank $n$ |
| Integral basis | a $\mathbb{Z}$-basis $\{\omega_1,\ldots,\omega_n\}$ of $\mathcal{O}_K$ |
| $\text{disc}(K)$ | discriminant: $\det(\sigma_i(\omega_j))^2$; measures ramification |
| Dedekind domain | the algebraic structure of $\mathcal{O}_K$: Noetherian, integrally closed, Krull dim 1 |
| $\mathbb{Z}[\sqrt{d}]$ | $\{a + b\sqrt{d} : a,b \in \mathbb{Z}\}$ |
| $\zeta_n = e^{2\pi i/n}$ | a primitive $n$-th root of unity |
| Squarefree $d$ | $d$ has no square factor $> 1$ |
| $d \equiv 1 \pmod{4}$ | congruence condition determining the form of $\mathcal{O}_K$ |
