---
title: L-Functions & Dirichlet Series
tag: algebraic-number-theory
summary: Complex analytic functions encoding arithmetic information as Euler products — generalising the Riemann zeta function to characters, number fields, and algebraic varieties.
links:
  - artin-reciprocity
  - dirichlets-theorem
  - riemann-hypothesis
  - adeles-ideles
---

# L-Functions & Dirichlet Series

An **$L$-function** is a complex analytic function, typically given by a **Dirichlet series** $\sum a_n n^{-s}$ and an **Euler product** $\prod_p f_p(p^{-s})^{-1}$, encoding arithmetic information about a mathematical object — a Dirichlet character, a number field, an elliptic curve, a modular form, or a Galois representation. The prototype is the **Riemann zeta function** $\zeta(s) = \sum_{n=1}^\infty n^{-s} = \prod_p (1-p^{-s})^{-1}$. L-functions satisfy a **functional equation** relating $s$ to $1-s$, have analytic continuations to $\mathbb{C}$ (typically minus a pole at $s=1$), and their zeros on the critical strip $0 < \text{Re}(s) < 1$ govern the distribution of primes. The **generalised Riemann hypothesis** conjectures all non-trivial zeros lie on $\text{Re}(s) = 1/2$.

## Riemann Zeta Function

$$\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s} = \prod_{p \text{ prime}} \frac{1}{1-p^{-s}}, \quad \text{Re}(s) > 1$$

## Dirichlet $L$-Functions

For a Dirichlet character $\chi : (\mathbb{Z}/m\mathbb{Z})^\times \to \mathbb{C}^\times$:

$$L(s,\chi) = \sum_{n=1}^\infty \frac{\chi(n)}{n^s} = \prod_p \frac{1}{1-\chi(p)p^{-s}}, \quad \text{Re}(s) > 1$$

**Application:** $L(1, \chi) \neq 0$ for $\chi \neq \chi_0$ implies **Dirichlet's theorem** on primes in arithmetic progressions.

## Dedekind Zeta Function

For a number field $K$:

$$\zeta_K(s) = \sum_{\mathfrak{a} \subseteq \mathcal{O}_K} \frac{1}{N(\mathfrak{a})^s} = \prod_{\mathfrak{p}} \frac{1}{1-N(\mathfrak{p})^{-s}}, \quad \text{Re}(s) > 1$$

**Class number formula:**

$$\lim_{s\to 1}(s-1)\zeta_K(s) = \frac{2^{r_1}(2\pi)^{r_2}h_K R_K}{w_K\sqrt{|\text{disc}(K)|}}$$

## Artin $L$-Functions

For a Galois representation $\rho : \text{Gal}(\bar{K}/K) \to GL_n(\mathbb{C})$:

$$L(s, \rho) = \prod_\mathfrak{p} \det\!\left(I - N(\mathfrak{p})^{-s} \rho(\text{Frob}_\mathfrak{p})\right)^{-1}$$

These generalise both Dirichlet $L$-functions and Dedekind zeta functions.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $L(s, \chi)$ | Dirichlet $L$-function for character $\chi$ |
| $\zeta_K(s)$ | Dedekind zeta function of number field $K$ |
| $\zeta(s)$ | Riemann zeta function ($K = \mathbb{Q}$) |
| Euler product | $\prod_p f(p^{-s})$; one factor per prime |
| Dirichlet series | $\sum a_n n^{-s}$; converges for $\text{Re}(s)$ large enough |
| Functional equation | relation between $L(s,\chi)$ and $L(1-s,\bar\chi)$ |
| Analytic continuation | the $L$-function extends to all $s \in \mathbb{C}$ |
| $N(\mathfrak{a}) = |\mathcal{O}_K/\mathfrak{a}|$ | norm of ideal $\mathfrak{a}$ |
| $h_K$ | class number |
| $R_K$ | regulator |
| $w_K$ | number of roots of unity in $K$ |
| GRH | generalised Riemann hypothesis: zeros have $\text{Re}(s)=1/2$ |
