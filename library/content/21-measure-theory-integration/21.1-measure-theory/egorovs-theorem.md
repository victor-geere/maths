---
title: Egorov's Theorem
tag: measure-theory
summary: "Egorov's theorem states that on a finite measure space, almost everywhere convergence implies nearly uniform convergence: for any ε > 0 there is a set of measure less than ε outside which convergence is uniform."
links:
  - measure-spaces
  - lebesgue-integral
  - uniform-convergence
  - dominated-convergence
---

# Egorov's Theorem

**Egorov's theorem** (Dmitri Egorov, 1911) bridges pointwise almost-everywhere convergence and uniform convergence in measure theory. On a **finite** measure space, if $f_n \to f$ almost everywhere, then for every $\varepsilon > 0$ there exists a measurable set $E$ with $\mu(X \setminus E) < \varepsilon$ such that $f_n \to f$ **uniformly** on $E$. In other words, almost-everywhere convergence is "nearly uniform" on finite measure spaces — we can confine the bad behaviour to an arbitrarily small set. Egorov's theorem is used to prove Lusin's theorem (measurable functions are "nearly continuous") and is essential in demonstrating that $L^p$ convergence and other modes of convergence are related to almost-everywhere convergence on finite spaces.

## Statement

**Egorov's Theorem**: Let $(X,\mathcal{F},\mu)$ be a **finite** measure space ($\mu(X) < \infty$) and $f_n, f: X \to \mathbb{R}$ measurable with $f_n \to f$ $\mu$-a.e. Then for every $\varepsilon > 0$ there exists $E \in \mathcal{F}$ with $\mu(X \setminus E) < \varepsilon$ and:
$$f_n \to f \text{ uniformly on } E$$

## Proof Sketch

Set $A_n^k = \bigcup_{m \geq n}\{|f_m - f| \geq 1/k\}$. For each $k$, $\mu(A_n^k) \to 0$ (by a.e. convergence). Choose $n_k$ with $\mu(A_{n_k}^k) < \varepsilon/2^k$. Set $E = X \setminus \bigcup_k A_{n_k}^k$. Then $\mu(X \setminus E) < \varepsilon$ and on $E$: $|f_m - f| < 1/k$ for all $m \geq n_k$.

## Finiteness is Essential

On $(\mathbb{R}, \mathcal{L}, \lambda)$ (infinite measure): $f_n = \mathbf{1}_{[n,\infty)}$ converges a.e. to 0 but not nearly uniformly (any set of finite complement $X \setminus E$ with $\lambda(E^c) < \varepsilon$ still contains $[N,\infty)$ for some $N$, on which $f_n = 1$ for $n > N$).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Finite measure space | $\mu(X) < \infty$ |
| A.e. convergence | $f_n(x) \to f(x)$ except on a null set |
| Uniform convergence on $E$ | $\sup_{x\in E}|f_n(x)-f(x)| \to 0$ |
| Egorov's theorem | a.e. convergence is nearly uniform on finite spaces |
| $\mu(X\setminus E) < \varepsilon$ | the set $X\setminus E$ where uniformity fails has small measure |
| Lusin's theorem | measurable $f$ is continuous on a nearly full-measure set |
| Nearly uniform | uniform on $E$ with $\mu(E^c) < \varepsilon$ |
| Tightness | related concept: mass doesn't escape to infinity |
