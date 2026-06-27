---
title: Ideal Class Group
tag: algebraic-number-theory
summary: The group measuring the failure of unique factorisation in the ring of integers 𝒪_K — its order is the class number h_K.
links:
  - ring-of-integers
  - dedekind-domains
  - unique-factorisation-ideals
  - minkowskis-theorem
---

# Ideal Class Group

In $\mathbb{Z}$, every element factors uniquely into primes. In a general ring of integers $\mathcal{O}_K$, this fails: in $\mathbb{Z}[\sqrt{-5}]$ for example, $6 = 2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$, two genuinely different factorisations into irreducibles. Dedekind's revolutionary insight was that while **elements** may not factor uniquely, **ideals** always do: every ideal in $\mathcal{O}_K$ is a unique product of prime ideals. The **ideal class group** $\text{Cl}(K)$ measures precisely the failure of elements to factor uniquely — it is the group of fractional ideals modulo principal ideals. The **class number** $h_K = |\text{Cl}(K)|$ is finite (by Minkowski's theorem), and $h_K = 1$ exactly when $\mathcal{O}_K$ is a UFD.

## Fractional Ideals

A **fractional ideal** of $\mathcal{O}_K$ is a non-zero $\mathcal{O}_K$-submodule $\mathfrak{a} \subseteq K$ such that $d\mathfrak{a} \subseteq \mathcal{O}_K$ for some $d \in \mathbb{Z} \setminus \{0\}$.

The set of fractional ideals forms an abelian group $\text{Frac}(\mathcal{O}_K)$ under multiplication.

## Principal Ideals

A fractional ideal is **principal** if $\mathfrak{a} = (\alpha) = \alpha\mathcal{O}_K$ for some $\alpha \in K^*$.

The principal fractional ideals form a subgroup $\text{Prin}(\mathcal{O}_K) \subseteq \text{Frac}(\mathcal{O}_K)$.

## Ideal Class Group

$$\text{Cl}(K) = \text{Frac}(\mathcal{O}_K) / \text{Prin}(\mathcal{O}_K)$$

The **class number** is $h_K = |\text{Cl}(K)|$.

**Key fact:** $h_K = 1 \iff \mathcal{O}_K$ is a principal ideal domain $\iff$ $\mathcal{O}_K$ is a UFD.

## Examples

| Field $K$ | $h_K$ | $\text{Cl}(K)$ |
|---|---|---|
| $\mathbb{Q}(\sqrt{-1})$ | 1 | trivial |
| $\mathbb{Q}(\sqrt{-5})$ | 2 | $\mathbb{Z}/2\mathbb{Z}$ |
| $\mathbb{Q}(\sqrt{-23})$ | 3 | $\mathbb{Z}/3\mathbb{Z}$ |
| $\mathbb{Q}(\sqrt{10})$ | 2 | $\mathbb{Z}/2\mathbb{Z}$ |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\text{Cl}(K)$ | ideal class group of $K$ |
| $h_K = |\text{Cl}(K)|$ | class number |
| Fractional ideal | $\mathcal{O}_K$-submodule of $K$ of the form $\frac{1}{d}\mathfrak{a}$ |
| Principal ideal | $(\alpha) = \alpha\mathcal{O}_K$ for some $\alpha \in K^*$ |
| $\text{Frac}(\mathcal{O}_K)$ | group of fractional ideals |
| $\text{Prin}(\mathcal{O}_K)$ | subgroup of principal fractional ideals |
| $h_K = 1$ | class number 1 iff $\mathcal{O}_K$ is a UFD |
| UFD | unique factorisation domain |
| $\mathbb{Z}[\sqrt{-5}]$ | ring of integers of $\mathbb{Q}(\sqrt{-5})$; $h=2$, fails UFD |
| $K^*$ | multiplicative group of nonzero elements of $K$ |
