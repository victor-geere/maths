---
title: Unique Factorisation of Ideals
tag: algebraic-number-theory
summary: In the ring of integers 𝒪_K of a number field, every non-zero ideal factors uniquely as a product of prime ideals — Dedekind's replacement for unique factorisation of elements.
links:
  - ring-of-integers
  - dedekind-domains
  - ideal-class-group
  - ramification
---

# Unique Factorisation of Ideals

While elements of the ring of integers $\mathcal{O}_K$ of a number field may fail to factorise uniquely into irreducibles, Dedekind proved that **ideals** always factorise uniquely into prime ideals. This is the fundamental theorem of algebraic number theory, and it shows that the failure of unique factorisation of elements is entirely captured by the ideal class group. Every non-zero proper ideal $\mathfrak{a} \subseteq \mathcal{O}_K$ can be written in exactly one way as a product:

$$\mathfrak{a} = \mathfrak{p}_1^{e_1} \cdots \mathfrak{p}_r^{e_r}$$

with $\mathfrak{p}_i$ distinct prime ideals and $e_i \geq 1$. This factorisation is the heart of Dedekind's theory, carried out in the setting of **Dedekind domains**, and it provides the correct analogue of the Fundamental Theorem of Arithmetic for rings of integers.

## Statement

**Theorem (Dedekind):** Let $\mathcal{O}_K$ be the ring of integers of a number field $K$. Every non-zero proper ideal $\mathfrak{a} \subseteq \mathcal{O}_K$ factors uniquely as:

$$\mathfrak{a} = \mathfrak{p}_1^{e_1} \mathfrak{p}_2^{e_2} \cdots \mathfrak{p}_r^{e_r}$$

where $\mathfrak{p}_1,\ldots,\mathfrak{p}_r$ are distinct prime ideals and $e_i \geq 1$.

## Ideal Multiplication

For ideals $\mathfrak{a}, \mathfrak{b} \subseteq \mathcal{O}_K$:

$$\mathfrak{a}\mathfrak{b} = \left\{\sum_{\text{finite}} a_ib_i : a_i \in \mathfrak{a}, b_i \in \mathfrak{b}\right\}$$

## Prime Ideals

A non-zero ideal $\mathfrak{p} \subseteq \mathcal{O}_K$ is **prime** if $\mathfrak{p} \neq \mathcal{O}_K$ and $\alpha\beta \in \mathfrak{p} \Rightarrow \alpha \in \mathfrak{p}$ or $\beta \in \mathfrak{p}$.

Equivalently, $\mathcal{O}_K/\mathfrak{p}$ is an integral domain. Since $\mathcal{O}_K$ is a Dedekind domain, prime ideals are also maximal.

## GCD and LCM via Ideal Factorisation

$$\gcd(\mathfrak{a},\mathfrak{b}) = \mathfrak{a} + \mathfrak{b}, \qquad \text{lcm}(\mathfrak{a},\mathfrak{b}) = \mathfrak{a} \cap \mathfrak{b}$$

## Example in $\mathbb{Z}[\sqrt{-5}]$

The element $6$ does not factor uniquely: $6 = 2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$.

But as ideals:
$$6\mathcal{O}_K = (2,1+\sqrt{-5})^2 \cdot (3,1+\sqrt{-5}) \cdot (3,1-\sqrt{-5})$$

— a unique product of four prime ideals.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathfrak{a}\mathfrak{b}$ | product of ideals |
| $\mathfrak{p}$ | a prime ideal of $\mathcal{O}_K$ |
| $e_i$ | exponent (multiplicity) of $\mathfrak{p}_i$ in the factorisation |
| $\mathfrak{a} + \mathfrak{b}$ | sum of ideals: the smallest ideal containing both |
| $\mathfrak{a} \cap \mathfrak{b}$ | intersection of ideals: the largest ideal contained in both |
| $\mathcal{O}_K/\mathfrak{p}$ | quotient ring; a field when $\mathfrak{p}$ is maximal |
| Prime ideal | ideal $\mathfrak{p}$ with $\alpha\beta \in \mathfrak{p} \Rightarrow \alpha \in \mathfrak{p}$ or $\beta \in \mathfrak{p}$ |
| Dedekind domain | the ring structure of $\mathcal{O}_K$ that guarantees unique ideal factorisation |
| $\mathbb{Z}[\sqrt{-5}]$ | a ring of integers where element factorisation fails |
| $\gcd(\mathfrak{a},\mathfrak{b}) = \mathfrak{a}+\mathfrak{b}$ | ideal gcd is the sum |
