---
title: Artin Reciprocity
tag: algebraic-number-theory
summary: The central theorem of class field theory — a single map from the idèle class group to the Galois group of any abelian extension that simultaneously generalises all classical reciprocity laws.
links:
  - class-field-theory
  - galois-number-fields
  - adeles-ideles
  - quadratic-residues
---

# Artin Reciprocity

**Artin reciprocity** is the central theorem of class field theory, proved by Emil Artin in 1927. It states that for any abelian Galois extension $L/K$ of number fields, there is a canonical surjective group homomorphism — the **Artin map** — from the idèle class group $C_K = \mathbb{A}_K^\times / K^\times$ to the Galois group $\text{Gal}(L/K)$. This single theorem simultaneously generalises **quadratic reciprocity** (about the Legendre symbol), the **law of quadratic reciprocity** for general symbols, **cubic and quartic reciprocity**, and all higher power reciprocity laws. The reciprocity law was the culmination of 150 years of work from Gauss through Hilbert to Artin, and it forms the foundation of class field theory — the complete classification of abelian extensions of number fields.

## The Artin Map

For an abelian Galois extension $L/K$ and an unramified prime $\mathfrak{p}$ of $K$, the **Artin symbol** is:

$$\left(\frac{L/K}{\mathfrak{p}}\right) = \text{Frob}_\mathfrak{p} \in \text{Gal}(L/K)$$

the Frobenius element at $\mathfrak{p}$.

**Artin map (global):** extending linearly to all ideals coprime to the discriminant:

$$\text{Art}_{L/K} : I_K^S \to \text{Gal}(L/K), \quad \mathfrak{a} = \prod \mathfrak{p}^{n_\mathfrak{p}} \mapsto \prod \left(\frac{L/K}{\mathfrak{p}}\right)^{n_\mathfrak{p}}$$

**Artin Reciprocity:** this map is surjective with kernel containing all principal ideals $(\alpha)$ with $\alpha \equiv 1 \pmod{\mathfrak{f}}$ (for a suitable conductor $\mathfrak{f}$).

## Quadratic Reciprocity as a Special Case

For $K = \mathbb{Q}$, $L = \mathbb{Q}(\sqrt{p^*})$ (where $p^* = (-1)^{(p-1)/2}p$):

The Artin symbol $\left(\frac{L/\mathbb{Q}}{(q)}\right) = \left(\frac{p^*}{q}\right)$ (Legendre symbol). Artin reciprocity then implies:

$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\frac{q-1}{2}}$$

— the classical **quadratic reciprocity law**.

## Conductor and Ray Class Groups

The **conductor** $\mathfrak{f}$ of the extension $L/K$ is the smallest modulus such that $L$ is contained in the ray class field of conductor $\mathfrak{f}$. The Artin map factors through the ray class group:

$$C_K \to C_K(\mathfrak{f}) \twoheadrightarrow \text{Gal}(L/K)$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\text{Art}_{L/K}$ | Artin map: ideals $\to$ Galois group |
| $\left(\frac{L/K}{\mathfrak{p}}\right)$ | Artin symbol at $\mathfrak{p}$: the Frobenius element |
| $\text{Frob}_\mathfrak{p}$ | Frobenius: $\sigma(\alpha) \equiv \alpha^{N\mathfrak{p}} \pmod{\mathfrak{p}}$ |
| $I_K^S$ | group of fractional ideals coprime to set $S$ |
| Conductor $\mathfrak{f}$ | the modulus controlling the Artin map's kernel |
| Ray class group $C_K(\mathfrak{f})$ | generalised ideal class group modulo $\mathfrak{f}$ |
| Quadratic reciprocity | $\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{(p-1)(q-1)/4}$ |
| Legendre symbol $\left(\frac{a}{p}\right)$ | $+1$, $-1$, or $0$ according to whether $a$ is a QR mod $p$ |
| Abelian extension | a Galois extension with abelian Galois group |
