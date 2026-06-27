---
title: Elliptic Curves & Modularity
tag: algebraic-number-theory
summary: Every elliptic curve over ℚ is modular — its L-function equals that of a modular form — a theorem whose proof by Wiles implies Fermat's Last Theorem.
links:
  - elliptic-curves
  - l-functions
  - galois-number-fields
  - artin-reciprocity
---

# Elliptic Curves & Modularity

The **modularity theorem** (formerly the Taniyama–Shimura–Weil conjecture, proved by Wiles, Taylor–Wiles, and Breuil–Conrad–Diamond–Taylor) states that every elliptic curve $E$ over $\mathbb{Q}$ is **modular**: there exists a modular form $f$ of weight 2 such that the $L$-functions agree, $L(E, s) = L(f, s)$. This is a profound bridge between two different worlds: the geometric world of elliptic curves and the analytic world of modular forms. The proof was the centrepiece of Wiles's 1995 proof of **Fermat's Last Theorem**, which deduced from Ribet's theorem that a counterexample to FLT would produce a non-modular elliptic curve — a contradiction. The modularity theorem is also a special case of the **Langlands program**.

## Elliptic Curve $L$-Function

For an elliptic curve $E : y^2 = x^3 + ax + b$ over $\mathbb{Q}$, define $a_p = p + 1 - \#E(\mathbb{F}_p)$ for good primes $p$. Then:

$$L(E, s) = \prod_{p \text{ good}} \frac{1}{1 - a_p p^{-s} + p^{1-2s}} \cdot \prod_{p \text{ bad}} (\text{local factor})$$

## Modular Forms

A **modular form** of weight $k$ and level $N$ is a holomorphic function $f : \mathcal{H} \to \mathbb{C}$ satisfying:

$$f\!\left(\frac{a\tau+b}{c\tau+d}\right) = (c\tau+d)^k f(\tau) \quad \text{for } \begin{pmatrix}a&b\\c&d\end{pmatrix} \in \Gamma_0(N) \subseteq SL_2(\mathbb{Z})$$

with suitable growth conditions. Hecke operators $T_p$ act on modular forms and their eigenvalues give the $a_p$.

## Modularity Theorem

**Theorem (Wiles 1995; Taylor–Wiles; BCDT 2001):** Every elliptic curve $E/\mathbb{Q}$ is modular:

$$\exists \text{ cuspidal newform } f \text{ of weight 2 and level } N_E \text{ such that } L(E,s) = L(f,s)$$

The level $N_E$ is the **conductor** of $E$.

## Implications

**Ribet's Theorem (1990):** if $a^p + b^p = c^p$ ($p \geq 5$ prime) then the **Frey curve** $y^2 = x(x-a^p)(x+b^p)$ would be a semistable non-modular elliptic curve.

**Fermat's Last Theorem:** by the modularity theorem, no such curve exists, so no such solution to $a^p + b^p = c^p$ can exist.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Modularity theorem | every elliptic curve over $\mathbb{Q}$ is modular |
| Modular form $f$ | holomorphic function on upper half-plane $\mathcal{H}$, invariant under $\Gamma_0(N)$ |
| $L(E,s)$ | $L$-function of elliptic curve $E$ |
| $a_p = p+1-\#E(\mathbb{F}_p)$ | trace of Frobenius; Fourier coefficients of the associated modular form |
| $\#E(\mathbb{F}_p)$ | number of points on $E$ over $\mathbb{F}_p$ |
| Level $N$ | the conductor of the modular form (and of the elliptic curve) |
| $\Gamma_0(N)$ | congruence subgroup $\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix} \in SL_2(\mathbb{Z}) : N|c\right\}$ |
| Cuspidal newform | the specific type of modular form corresponding to an elliptic curve |
| Frey curve | elliptic curve built from a hypothetical FLT counterexample |
| Ribet's theorem | Frey curve would be non-modular; combined with Wiles $\Rightarrow$ FLT |
| Fermat's Last Theorem | $a^n + b^n = c^n$ has no integer solutions for $n \geq 3$, $abc \neq 0$ |
