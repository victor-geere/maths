---
title: Prime & Maximal Ideals
tag: commutative-algebra
summary: Prime ideals are the algebraic analogue of prime numbers and correspond to irreducible varieties; maximal ideals correspond to points, and the spectrum Spec(R) assembles all prime ideals into a geometric space.
links:
  - ideals
  - localisation
  - modules
  - krull-dimension
  - schemes
---

# Prime & Maximal Ideals

**Prime ideals** are the central objects of commutative algebra, serving as the algebraic counterparts of prime numbers and irreducible subvarieties. A prime ideal $\mathfrak{p}$ of a commutative ring $R$ is an ideal such that $ab \in \mathfrak{p} \Rightarrow a \in \mathfrak{p}$ or $b \in \mathfrak{p}$, equivalently $R/\mathfrak{p}$ is an integral domain. A **maximal ideal** $\mathfrak{m}$ is one where $R/\mathfrak{m}$ is a field, corresponding geometrically to a "point" in the spectrum. The **prime spectrum** $\mathrm{Spec}(R)$, the set of all prime ideals with the Zariski topology, is the fundamental geometric object attached to any commutative ring and the foundation of scheme theory.

## Definitions

An ideal $I \subsetneq R$ is:
- **Prime**: $ab \in I \Rightarrow a \in I$ or $b \in I$ (equivalently $R/I$ is an integral domain)
- **Maximal**: no ideal $J$ with $I \subsetneq J \subsetneq R$ exists (equivalently $R/I$ is a field)

Every maximal ideal is prime (since fields are integral domains). The converse fails: $(0) \subset \mathbb{Z}$ is prime but not maximal.

## Spectrum

$$\mathrm{Spec}(R) = \{\mathfrak{p} \subset R : \mathfrak{p} \text{ is prime}\}$$

The **Zariski topology** on $\mathrm{Spec}(R)$ has closed sets $V(I) = \{\mathfrak{p} : I \subseteq \mathfrak{p}\}$.

The **maximal spectrum** $\mathrm{MaxSpec}(R) \subseteq \mathrm{Spec}(R)$ records the closed points.

## Correspondence

If $R = k[x_1,\ldots,x_n]/I$ (coordinate ring of an affine variety $X$ over algebraically closed $k$), then:
- Points of $X$ $\longleftrightarrow$ maximal ideals of $R$ (Nullstellensatz)
- Irreducible subvarieties $\longleftrightarrow$ prime ideals of $R$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Prime ideal $\mathfrak{p}$ | $ab\in\mathfrak{p} \Rightarrow a\in\mathfrak{p}$ or $b\in\mathfrak{p}$; $R/\mathfrak{p}$ is a domain |
| Maximal ideal $\mathfrak{m}$ | $R/\mathfrak{m}$ is a field; no larger proper ideal |
| Integral domain | commutative ring with $ab=0 \Rightarrow a=0$ or $b=0$ |
| $\mathrm{Spec}(R)$ | set of prime ideals with Zariski topology |
| $V(I)$ | closed set $\{\mathfrak{p} : I \subseteq \mathfrak{p}\}$ in $\mathrm{Spec}(R)$ |
| Zariski topology | topology where closed sets are $V(I)$ |
| Nilradical | $\sqrt{(0)} = \bigcap_{\mathfrak{p}\in\mathrm{Spec}} \mathfrak{p}$; all nilpotents |
| Jacobson radical | $\bigcap_{\mathfrak{m}\text{ maximal}} \mathfrak{m}$ |
| $\mathrm{MaxSpec}(R)$ | maximal ideal spectrum; the "classical" points |
