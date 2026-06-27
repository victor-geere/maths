---
title: Ultraproducts
tag: logic
summary: An ultraproduct is a quotient of a product of structures by an ultrafilter; Łoś's theorem says a sentence holds in the ultraproduct iff it holds in ultrafilter-many factors, giving a powerful model-construction tool.
links:
  - structures-models
  - compactness-logic
  - lowenheim-skolem
---

# Ultraproducts

An **ultraproduct** is a way of combining infinitely many structures into a single structure by choosing which "majority" of them to listen to, where the notion of majority is encoded by an **ultrafilter** $\mathcal{U}$ on the index set $I$. Given structures $\{\mathcal{M}_i\}_{i \in I}$, the ultraproduct $\prod_\mathcal{U} \mathcal{M}_i$ is the direct product $\prod_i M_i$ modulo the equivalence $(a_i) \sim (b_i)$ iff $\{i : a_i = b_i\} \in \mathcal{U}$. **Łoś's theorem** is the key fact: a first-order sentence $\varphi$ holds in $\prod_\mathcal{U} \mathcal{M}_i$ iff $\{i : \mathcal{M}_i \models \varphi\} \in \mathcal{U}$. Ultraproducts give an elegant proof of the compactness theorem and are the foundation of non-standard analysis.

## Ultrafilters

A **filter** on $I$ is a collection $\mathcal{F}$ of subsets closed under supersets and finite intersections, with $I \in \mathcal{F}$, $\emptyset \notin \mathcal{F}$. An **ultrafilter** additionally satisfies: for every $A \subseteq I$, either $A \in \mathcal{U}$ or $I \setminus A \in \mathcal{U}$ (maximality / decidability).

- **Principal ultrafilter**: $\mathcal{U} = \{A : i_0 \in A\}$ for some fixed $i_0$; gives ultraproduct $\cong \mathcal{M}_{i_0}$.
- **Non-principal**: contains all cofinite sets; exists by Zorn's lemma.

## Łoś's Theorem

$$\prod_\mathcal{U} \mathcal{M}_i \models \varphi([a_i]) \iff \{i \in I : \mathcal{M}_i \models \varphi(a_i)\} \in \mathcal{U}$$

## Non-Standard Analysis via Ultraproducts

Take $\mathcal{M}_i = \mathbb{R}$ for all $i \in \mathbb{N}$ and a non-principal ultrafilter $\mathcal{U}$. The ultrapower ${}^*\mathbb{R} = \prod_\mathcal{U} \mathbb{R}$ is a **non-standard real field** containing infinitesimals (e.g., the class of $(1, 1/2, 1/3, \ldots)$) and infinite elements.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Filter $\mathcal{F}$ on $I$ | collection of subsets closed under supersets and finite intersections |
| Ultrafilter $\mathcal{U}$ | maximal filter; decides every subset |
| $\prod_\mathcal{U} \mathcal{M}_i$ | ultraproduct: $\prod M_i$ modulo $\mathcal{U}$-equivalence |
| Łoś's theorem | $\varphi$ holds in ultraproduct iff holds on $\mathcal{U}$-large set of factors |
| $\mathcal{U}$-large set | set $A \in \mathcal{U}$ |
| Principal ultrafilter | $\{A : i_0 \in A\}$; concentrates on one index |
| Non-principal ultrafilter | contains all cofinite sets; requires Zorn/AC |
| ${}^*\mathbb{R}$ | non-standard reals: ultrapower of $\mathbb{R}$ |
| Infinitesimal | $\epsilon \in {}^*\mathbb{R}$ with $0 < \epsilon < r$ for all real $r > 0$ |
| Ultrapower | ultraproduct with all $\mathcal{M}_i$ equal |
