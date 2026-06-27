---
title: Hensel's Lemma
tag: algebraic-number-theory
summary: If a polynomial has a simple root modulo p, it lifts uniquely to a root in ℤ_p — allowing local solutions to be "bootstrapped" from mod-p solutions.
links:
  - p-adic-numbers
  - local-fields
  - newton-raphson
---

# Hensel's Lemma

**Hensel's Lemma** is the $p$-adic analogue of Newton's method: if a polynomial $f(x)$ has a simple root modulo $p$ (i.e. $f(a) \equiv 0 \pmod{p}$ and $f'(a) \not\equiv 0 \pmod{p}$), then this root lifts uniquely to a root in $\mathbb{Z}_p$. This "lifting" process is iterative — knowing a root mod $p^n$ gives a root mod $p^{n+1}$ — and converges in the $p$-adic metric because the corrections get $p$-adically smaller at each step. Hensel's Lemma is extraordinarily useful: it shows that $\mathbb{Q}_p$ contains all $(p-1)$-th roots of unity (when $p$ is odd), gives criteria for a polynomial to have roots in $\mathbb{Q}_p$, and allows local arithmetic to be computed modulo high powers of $p$.

## Statement (Simple Root Version)

Let $f \in \mathbb{Z}_p[x]$ and suppose $a_0 \in \mathbb{Z}$ satisfies:

$$f(a_0) \equiv 0 \pmod{p} \quad \text{and} \quad f'(a_0) \not\equiv 0 \pmod{p}$$

Then there exists a **unique** $a \in \mathbb{Z}_p$ with $f(a) = 0$ and $a \equiv a_0 \pmod{p}$.

## Proof by Iteration (Newton's Method $p$-adically)

Given $a_n$ with $f(a_n) \equiv 0 \pmod{p^n}$, set:

$$a_{n+1} = a_n - \frac{f(a_n)}{f'(a_n)}$$

Since $f'(a_0) \not\equiv 0 \pmod{p}$, the denominator is invertible in $\mathbb{Z}_p$, and $f(a_{n+1}) \equiv 0 \pmod{p^{n+1}}$.

## General Version

More generally: if $f(a_0) \equiv 0 \pmod{p^{2k+1}}$ and $v_p(f'(a_0)) = k$, then there exists $a \in \mathbb{Z}_p$ with $f(a) = 0$ and $a \equiv a_0 \pmod{p^{k+1}}$.

## Applications

- **Roots of unity:** $x^{p-1} - 1 \equiv 0 \pmod{p}$ has $p-1$ simple roots, so $\mathbb{Q}_p$ contains all $(p-1)$-th roots of unity (Teichmüller lifts)
- **Square roots:** $a \in \mathbb{Z}_p^\times$ is a square in $\mathbb{Z}_p$ iff $a \pmod{p}$ is a square in $\mathbb{F}_p^*$ (for $p$ odd)
- **Factoring polynomials:** if $f \equiv g h \pmod{p}$ with $\gcd(g,h) = 1$ in $\mathbb{F}_p[x]$, then $f$ factors in $\mathbb{Z}_p[x]$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $f \in \mathbb{Z}_p[x]$ | polynomial with $p$-adic integer coefficients |
| $a_0 \in \mathbb{Z}$ | initial approximate root mod $p$ |
| Simple root mod $p$ | $f(a_0) \equiv 0$ and $f'(a_0) \not\equiv 0 \pmod{p}$ |
| $v_p(x)$ | $p$-adic valuation of $x$ |
| $a_{n+1} = a_n - f(a_n)/f'(a_n)$ | Newton's method lifting step |
| Teichmüller lift | canonical lift of $a \in \mathbb{F}_p^*$ to $(p-1)$-th root of unity in $\mathbb{Z}_p$ |
| $\mathbb{Z}_p^\times$ | units in $\mathbb{Z}_p$: elements with $v_p(x) = 0$ |
| Factoring over $\mathbb{Z}_p$ | Hensel lifting factors a poly mod $p$ to factors over $\mathbb{Z}_p$ |
| Convergence in $\mathbb{Q}_p$ | $\sum a_n$ converges iff $|a_n|_p \to 0$ |
