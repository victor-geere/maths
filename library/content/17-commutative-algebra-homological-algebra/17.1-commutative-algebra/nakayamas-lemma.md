---
title: Nakayama's Lemma
tag: commutative-algebra
summary: Nakayama's lemma says that if M is a finitely generated module over a local ring and M = JM for the Jacobson radical J, then M = 0; it is used ubiquitously to lift generators from residue fields to the full ring.
links:
  - modules
  - prime-maximal-ideals
  - noetherian-rings
  - localisation
---

# Nakayama's Lemma

**Nakayama's lemma** is one of the most used results in commutative algebra and algebraic geometry. In its basic form it says: if $M$ is a finitely generated module over a commutative ring $R$ and $J$ is the Jacobson radical of $R$ (the intersection of all maximal ideals), then $JM = M$ implies $M = 0$. Over a local ring $(R, \mathfrak{m})$, this becomes: if $\mathfrak{m}M = M$ then $M = 0$. The practical power of Nakayama's lemma is in lifting: if $m_1, \ldots, m_r$ generate $M/\mathfrak{m}M$ as a $k = R/\mathfrak{m}$-vector space, then $m_1, \ldots, m_r$ generate $M$ as an $R$-module. This turns statements about the "fibre" (residue field) into statements about the full module.

## Statement

**Nakayama's Lemma**: Let $R$ be a commutative ring, $J = J(R)$ its Jacobson radical, and $M$ a **finitely generated** $R$-module. If $JM = M$, then $M = 0$.

**Local version**: If $(R, \mathfrak{m})$ is a local ring and $M$ is finitely generated, then:
$$\mathfrak{m} M = M \implies M = 0$$

**Lifting generators**: If $(R,\mathfrak{m})$ is local and $M$ finitely generated, then:
$$M = \mathfrak{m}M + Rm_1 + \cdots + Rm_r \implies M = Rm_1 + \cdots + Rm_r$$

## Proof Idea

Apply the **Cayley–Hamilton trick**: if $M = JM$ with $M = Rm_1 + \cdots + Rm_n$, write $m_i = \sum_j a_{ij}m_j$ with $a_{ij} \in J$. Then $(I - A)\mathbf{m} = 0$ where $A = (a_{ij})$. By Cayley–Hamilton, $\det(I-A)M = 0$, and $\det(I-A) \equiv 1 \pmod{J}$, hence is a unit, so $M = 0$.

## Application: Free Modules over Local Rings

If $M$ is a finitely generated projective module over a local ring $R$, then $M$ is free.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Jacobson radical $J(R)$ | $\bigcap_{\mathfrak{m}\text{ maximal}} \mathfrak{m}$ |
| $JM$ | $\{\sum j_im_i : j_i \in J, m_i \in M\}$ |
| Local ring $(R,\mathfrak{m})$ | ring with unique maximal ideal $\mathfrak{m}$ |
| $M/\mathfrak{m}M$ | residue module: $M$ tensored with $k = R/\mathfrak{m}$ |
| $k = R/\mathfrak{m}$ | residue field of local ring $R$ |
| Lift of generators | generators of $M/\mathfrak{m}M$ over $k$ lift to generators of $M$ over $R$ |
| Cayley–Hamilton | $p(A)v = 0$ for characteristic polynomial $p$; used in proof |
| Finitely generated | $M = Rm_1 + \cdots + Rm_n$ for some finite set $\{m_i\}$ |
