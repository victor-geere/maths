---
title: Localisation
tag: commutative-algebra
summary: Localisation inverts a multiplicative subset of a ring to create a new ring in which those elements become units, enabling local study of rings and the construction of the sheaf of regular functions.
links:
  - ring-axioms
  - prime-maximal-ideals
  - modules
  - schemes
---

# Localisation

**Localisation** is the process of formally inverting a multiplicative subset $S$ of a commutative ring $R$ to obtain a new ring $S^{-1}R$ (also written $R[S^{-1}]$) in which every element of $S$ becomes invertible. This generalises the construction of $\mathbb{Q}$ from $\mathbb{Z}$ (inverting all non-zero integers) and of rational functions from polynomials. Localisation is one of the most powerful tools in commutative algebra and algebraic geometry: localising at a prime ideal $\mathfrak{p}$ gives a **local ring** $R_\mathfrak{p}$ that focusses attention on the behaviour of $R$ near the point $\mathfrak{p}$, and the assignment $\mathfrak{p} \mapsto R_\mathfrak{p}$ assembles into the structure sheaf of $\mathrm{Spec}(R)$.

## Construction

Let $S \subseteq R$ be a **multiplicative set**: $1 \in S$ and $s,t \in S \Rightarrow st \in S$.

Define $S^{-1}R$ as the set of fractions $\{r/s : r \in R, s \in S\}$ modulo the equivalence:
$$(r, s) \sim (r', s') \iff \exists t \in S,\ t(rs' - r's) = 0$$

Addition and multiplication of fractions are defined in the usual way. There is a canonical ring map $\iota: R \to S^{-1}R$, $r \mapsto r/1$.

## Key Special Cases

| Multiplicative set $S$ | Localisation $S^{-1}R$ |
|---|---|
| $R \setminus \mathfrak{p}$ (prime complement) | Local ring $R_\mathfrak{p}$ |
| $\{f^n : n \geq 0\}$ | $R_f = R[f^{-1}]$; principal open set |
| $R \setminus \{0\}$ (for a domain) | Field of fractions $\mathrm{Frac}(R)$ |

## Localisation of Modules

For an $R$-module $M$ and multiplicative set $S$: $S^{-1}M = S^{-1}R \otimes_R M$, with $(r/s)\cdot(m/t) = rm/st$.

## Universal Property

$S^{-1}R$ is characterised: for any ring map $f: R \to T$ sending every $s \in S$ to a unit, there is a unique $\tilde{f}: S^{-1}R \to T$ with $\tilde{f} \circ \iota = f$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Multiplicative set $S$ | subset of $R$ closed under multiplication, containing 1 |
| $S^{-1}R$ | localisation of $R$ at $S$: fractions $r/s$ with $s \in S$ |
| $R_\mathfrak{p}$ | localisation at prime complement $R \setminus \mathfrak{p}$; a local ring |
| Local ring | ring with a unique maximal ideal |
| $R_f$ | $R[f^{-1}]$: invert powers of $f$ |
| $\mathrm{Frac}(R)$ | field of fractions of an integral domain |
| $S^{-1}M$ | localised module: $S^{-1}R \otimes_R M$ |
| $\iota: R \to S^{-1}R$ | canonical map $r \mapsto r/1$ |
| Universal property | $S^{-1}R$ is initial among rings receiving $R \to T$ inverting $S$ |
