---
title: Galois Theory of Number Fields
tag: algebraic-number-theory
summary: Applying Galois theory to extensions of number fields — the Galois group controls ramification, splitting of primes, and the structure of the extension.
links:
  - galois-theory
  - ramification
  - number-fields
  - artin-reciprocity
---

# Galois Theory of Number Fields

When a number field extension $K/\mathbb{Q}$ is **Galois** — that is, normal and separable — the **Galois group** $G = \text{Gal}(K/\mathbb{Q})$ acts on $K$ by field automorphisms fixing $\mathbb{Q}$. This group action encodes deep arithmetic: the splitting behaviour of a prime $p$ in $\mathcal{O}_K$ is controlled by the **Frobenius element** $\text{Frob}_\mathfrak{p} \in G$, the **decomposition group** $D(\mathfrak{p}|p)$ captures the local Galois action, and the **inertia group** $I(\mathfrak{p}|p)$ encodes the ramification. The Galois group thus becomes a dictionary between algebraic (field theory) and arithmetic (prime splitting) information — a dictionary made precise by class field theory for abelian extensions and the Langlands program for non-abelian extensions.

## Galois Extensions

$K/\mathbb{Q}$ is **Galois** with group $G = \text{Gal}(K/\mathbb{Q})$ iff:
- $|G| = [K:\mathbb{Q}]$
- $K^G = \mathbb{Q}$ (fixed field is $\mathbb{Q}$)
- Equivalently: $K$ is the splitting field of a separable polynomial over $\mathbb{Q}$

## Frobenius Element

For $\mathfrak{p}$ a prime of $\mathcal{O}_K$ above $p$ (unramified), the **Frobenius element** $\text{Frob}_\mathfrak{p} \in G$ is the unique $\sigma \in D(\mathfrak{p}|p)$ with:

$$\sigma(\alpha) \equiv \alpha^p \pmod{\mathfrak{p}} \quad \text{for all } \alpha \in \mathcal{O}_K$$

## Decomposition and Inertia Groups

For $\mathfrak{p}$ a prime of $\mathcal{O}_K$ above $p$:

- **Decomposition group:** $D(\mathfrak{p}|p) = \{\sigma \in G : \sigma(\mathfrak{p}) = \mathfrak{p}\}$
- **Inertia group:** $I(\mathfrak{p}|p) = \{\sigma \in G : \sigma(\alpha) \equiv \alpha \pmod{\mathfrak{p}} \text{ for all }\alpha \in \mathcal{O}_K\}$

With $|D| = ef$, $|I| = e$ (ramification index), $|D/I| = f$ (residue degree).

## Splitting and the Frobenius

For Galois $K/\mathbb{Q}$:
- $p$ **splits completely** iff $\text{Frob}_\mathfrak{p} = \text{id}$ for all $\mathfrak{p}|p$
- $p$ is **inert** iff $D(\mathfrak{p}|p) = G$ and $e=1$
- $p$ **ramifies** iff $I(\mathfrak{p}|p) \neq \{1\}$

## Chebotarev Density Theorem

For Galois $K/\mathbb{Q}$ and conjugacy class $C \subseteq G$, the set of primes $p$ with $\text{Frob}_\mathfrak{p} \in C$ has **density** $|C|/|G|$ in the primes.

This is the grand generalisation of Dirichlet's theorem on primes in arithmetic progressions.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $G = \text{Gal}(K/\mathbb{Q})$ | Galois group of $K/\mathbb{Q}$ |
| $K^G$ | fixed field under $G$; equals $\mathbb{Q}$ for Galois extensions |
| $\text{Frob}_\mathfrak{p}$ | Frobenius element at $\mathfrak{p}$: the arithmetic Frobenius $\sigma(\alpha)\equiv\alpha^p$ |
| $D(\mathfrak{p}|p)$ | decomposition group: stabiliser of $\mathfrak{p}$ in $G$ |
| $I(\mathfrak{p}|p)$ | inertia group: kernel of $D \to \text{Gal}(\kappa_\mathfrak{p}/\mathbb{F}_p)$ |
| $e$ | ramification index; $|I| = e$ |
| $f$ | residue degree; $|D/I| = f$ |
| Splits completely | Frobenius is trivial; $g = [K:\mathbb{Q}]$ primes above $p$ |
| Chebotarev density | primes with Frobenius in class $C$ have density $|C|/|G|$ |
| Conjugacy class $C$ | primes with $\text{Frob}_\mathfrak{p} \in C$ form a set of density $|C|/|G|$ |
