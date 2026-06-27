---
title: p-adic Numbers
tag: algebraic-number-theory
summary: The completion of ℚ with respect to the p-adic absolute value — a number system where numbers are "close" if their difference is highly divisible by p.
links:
  - p-adic-absolute-value
  - local-fields
  - hensels-lemma
---

# p-adic Numbers

The **$p$-adic numbers** $\mathbb{Q}_p$ are the completion of $\mathbb{Q}$ with respect to the **$p$-adic absolute value** — a metric in which two numbers are close if their difference is divisible by a high power of $p$. This is the opposite of the usual absolute value: the integer $p^{100}$ is $p$-adically tiny, while $1/p$ is $p$-adically huge. Introduced by Hensel in 1897, $p$-adic numbers provide a "local" perspective on number theory: by working in $\mathbb{Q}_p$, we see the arithmetic of $\mathbb{Q}$ at the prime $p$ in isolation. The **Hasse–Minkowski theorem** shows that a quadratic form has rational solutions iff it has real and $p$-adic solutions for every prime $p$ — a paradigm called the **local-global principle** or **Hasse principle**.

## The $p$-adic Integers $\mathbb{Z}_p$

The **$p$-adic integers** $\mathbb{Z}_p$ can be defined as the inverse limit:

$$\mathbb{Z}_p = \varprojlim_n \mathbb{Z}/p^n\mathbb{Z}$$

An element of $\mathbb{Z}_p$ is a compatible sequence $(a_1, a_2, a_3, \ldots)$ with $a_n \in \mathbb{Z}/p^n\mathbb{Z}$ and $a_n \equiv a_{n-1} \pmod{p^{n-1}}$.

## $p$-adic Expansion

Every $a \in \mathbb{Z}_p$ has a unique **$p$-adic expansion**:

$$a = a_0 + a_1 p + a_2 p^2 + \cdots, \quad a_i \in \{0, 1, \ldots, p-1\}$$

(an "infinite integer" to the left in base $p$).

## The $p$-adic Numbers $\mathbb{Q}_p$

$$\mathbb{Q}_p = \text{Frac}(\mathbb{Z}_p) = \{p^{-n}a : n \geq 0, a \in \mathbb{Z}_p\}$$

Every $x \in \mathbb{Q}_p$ has an expansion $x = \sum_{k \geq -N} a_k p^k$ for some $N \geq 0$.

## Algebraic Properties

- $\mathbb{Z}_p$ is a local ring with maximal ideal $(p) = p\mathbb{Z}_p$
- $\mathbb{Z}_p/(p) \cong \mathbb{F}_p$
- $\mathbb{Q}_p$ is a **local field** (complete, discrete valuation field, finite residue field)
- $\mathbb{Q}_p^\times \cong \mathbb{Z} \times \mathbb{Z}_p^\times$ (via $p$-adic valuation)

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathbb{Z}_p$ | $p$-adic integers: $\varprojlim \mathbb{Z}/p^n\mathbb{Z}$ |
| $\mathbb{Q}_p$ | $p$-adic numbers: fraction field of $\mathbb{Z}_p$ |
| $p$-adic expansion | $a = \sum_{k\geq-N} a_k p^k$ with $a_k \in \{0,\ldots,p-1\}$ |
| $\varprojlim$ | inverse limit (projective limit) |
| Local ring | ring with a unique maximal ideal |
| Residue field | $\mathbb{Z}_p/(p) \cong \mathbb{F}_p$ |
| $\mathbb{Q}_p^\times$ | multiplicative group of nonzero $p$-adic numbers |
| Local-global principle | rational solution exists iff solutions exist over $\mathbb{R}$ and all $\mathbb{Q}_p$ |
| Hasse–Minkowski theorem | quadratic forms: local-global principle holds |
| Completion | the process of adding limits of Cauchy sequences |
