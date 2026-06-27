---
title: Ramification & Splitting of Primes
tag: algebraic-number-theory
summary: How a rational prime p behaves in 𝒪_K — whether it splits into distinct primes, remains inert, or ramifies — encoded by the factorisation p𝒪_K = 𝔭₁^e₁⋯𝔭_g^eg.
links:
  - unique-factorisation-ideals
  - ring-of-integers
  - norm-trace-discriminant
  - galois-number-fields
---

# Ramification & Splitting of Primes

When a rational prime $p \in \mathbb{Z}$ is viewed inside the ring of integers $\mathcal{O}_K$ of a number field, the ideal $(p) = p\mathcal{O}_K$ factors into prime ideals:

$$p\mathcal{O}_K = \mathfrak{p}_1^{e_1} \cdots \mathfrak{p}_g^{e_g}$$

The numbers $e_i$ (ramification indices) and $f_i = [\mathcal{O}_K/\mathfrak{p}_i : \mathbb{F}_p]$ (residue degrees) together satisfy $\sum_{i=1}^g e_i f_i = n = [K:\mathbb{Q}]$. The prime $p$ **ramifies** if any $e_i > 1$, **splits completely** if $g = n$ (all $e_i = f_i = 1$), and is **inert** if $g = 1$, $e_1 = 1$, $f_1 = n$. These three behaviours control the local arithmetic of $K$ at $p$ and are fundamental to the Langlands program and class field theory.

## The Factorisation

$$p\mathcal{O}_K = \mathfrak{p}_1^{e_1} \cdots \mathfrak{p}_g^{e_g}$$

with $\sum_{i=1}^g e_i f_i = n$ where $f_i = [\mathcal{O}_K/\mathfrak{p}_i : \mathbb{F}_p]$.

## Behaviour Types

| Condition | Behaviour | Example ($K=\mathbb{Q}(\sqrt{d})$) |
|---|---|---|
| $g = n$, all $e_i = f_i = 1$ | **Splits completely** | $p \nmid 2d$, $\left(\frac{d}{p}\right) = 1$ |
| $g = 1$, $e_1 = 1$, $f_1 = n$ | **Inert** | $p \nmid 2d$, $\left(\frac{d}{p}\right) = -1$ |
| Some $e_i > 1$ | **Ramifies** | $p \mid \text{disc}(K)$ |

## Ramification and Discriminant

A prime $p$ **ramifies** in $K$ if and only if $p \mid \text{disc}(K/\mathbb{Q})$.

Only finitely many primes ramify in any number field.

## Quadratic Fields

For $K = \mathbb{Q}(\sqrt{d})$ and odd prime $p \nmid d$, the Legendre symbol determines the splitting:

$$\left(\frac{d}{p}\right) = \begin{cases}+1 & p \text{ splits} \\ -1 & p \text{ inert} \\ 0 & p \text{ ramifies}\end{cases}$$

## Galois Extensions

When $K/\mathbb{Q}$ is Galois, all $\mathfrak{p}_i$ are conjugate and $e_i = e$, $f_i = f$ for all $i$:

$$efg = n$$

The **decomposition group** $D(\mathfrak{p}|p)$ and **inertia group** $I(\mathfrak{p}|p)$ capture the local Galois action.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $p\mathcal{O}_K = \mathfrak{p}_1^{e_1}\cdots\mathfrak{p}_g^{e_g}$ | factorisation of $(p)$ in $\mathcal{O}_K$ |
| $e_i$ | ramification index of $\mathfrak{p}_i$ over $p$ |
| $f_i = [\mathcal{O}_K/\mathfrak{p}_i : \mathbb{F}_p]$ | residue degree |
| $g$ | number of prime ideals above $p$ |
| $\sum e_i f_i = n$ | fundamental identity |
| Splits completely | $g=n$, all $e_i=f_i=1$ |
| Inert | $g=1$, $e=1$, $f=n$; $p$ stays prime |
| Ramifies | some $e_i > 1$ |
| $\left(\frac{d}{p}\right)$ | Legendre symbol: $+1$, $-1$, or $0$ |
| $\text{disc}(K)$ | discriminant; $p$ ramifies iff $p \mid \text{disc}$ |
| Decomposition group $D(\mathfrak{p}|p)$ | stabiliser of $\mathfrak{p}$ in $\text{Gal}(K/\mathbb{Q})$ |
| Inertia group $I(\mathfrak{p}|p)$ | subgroup acting trivially on $\mathcal{O}_K/\mathfrak{p}$ |
