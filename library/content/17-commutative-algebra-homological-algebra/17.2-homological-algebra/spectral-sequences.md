---
title: Spectral Sequences
tag: homological-algebra
summary: A spectral sequence is an algebraic device — a book of pages of bigraded modules with differentials — that systematically computes the homology of a filtered complex or the composition of two derived functors.
links:
  - chain-complexes
  - derived-functors
  - ext-tor
  - derived-categories
---

# Spectral Sequences

A **spectral sequence** is a powerful computational tool in homological algebra that organises the computation of homology groups through successive approximations. It consists of a sequence of **pages** $E_r = \{E_r^{p,q}\}$ (bigraded modules) with differentials $d_r: E_r^{p,q} \to E_r^{p+r,q-r+1}$ (or $E_r^{p-r,q+r-1}$ for homological ones), where $E_{r+1} = H(E_r, d_r)$ (homology of the previous page). Under mild hypotheses, the pages eventually stabilise to $E_\infty$, which encodes the graded pieces of a filtration on the target homology group. Spectral sequences arise from filtrations on chain complexes, double complexes, and fibre sequences, and are indispensable in algebraic topology, algebraic geometry, and representation theory.

## Structure

A **cohomological spectral sequence** consists of:
- Bigraded abelian groups $\{E_r^{p,q}\}_{p,q \in \mathbb{Z}}$ for each page $r \geq 0$ (or $r \geq 1$ or $r \geq 2$).
- Differentials $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ with $d_r^2 = 0$.
- Isomorphisms $E_{r+1}^{p,q} \cong H^{p,q}(E_r, d_r) = \ker(d_r^{p,q})/\mathrm{im}(d_r^{p-r,q+r-1})$.

## Convergence

The spectral sequence **converges** to $H^n$ (written $E_2^{p,q} \Rightarrow H^{p+q}$) if $E_\infty^{p,q}$ is the associated graded of a filtration on $H^{p+q}$:
$$H^n \text{ filtered with } \mathrm{gr}^p H^n \cong E_\infty^{p, n-p}$$

## Classic Examples

- **Serre spectral sequence**: $E_2^{p,q} = H^p(B; H^q(F)) \Rightarrow H^{p+q}(E)$ for a fibration $F \to E \to B$.
- **Grothendieck spectral sequence**: $R^p F \circ R^q G \Rightarrow R^{p+q}(F \circ G)$ for composable functors.
- **Lyndon–Hochschild–Serre**: $H^p(G/N; H^q(N;M)) \Rightarrow H^{p+q}(G;M)$ for group extensions.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $E_r^{p,q}$ | $(p,q)$ entry on page $r$ of the spectral sequence |
| $d_r: E_r^{p,q} \to E_r^{p+r,q-r+1}$ | differential on page $r$ |
| $E_{r+1} = H(E_r, d_r)$ | next page is homology of current page |
| $E_\infty^{p,q}$ | stable page: limit of pages as $r \to \infty$ |
| Convergence $E_2 \Rightarrow H^*$ | $E_\infty$ is associated graded of target |
| Filtration | descending sequence $H^n = F^0 \supseteq F^1 \supseteq \cdots$ |
| Bigraded module | module indexed by two integers $(p,q)$ |
| Serre spectral sequence | from a fibration $F \to E \to B$ |
| Grothendieck spectral sequence | from composition of right-derived functors |
| Degeneration | spectral sequence collapses at page $E_r$ if $d_r = d_{r+1} = \cdots = 0$ |
