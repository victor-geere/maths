---
title: Consistency & Independence
tag: logic
summary: A statement is independent of a theory if neither it nor its negation is provable; the continuum hypothesis and axiom of choice are famously independent of ZFC, proven by Gödel's constructible universe and Cohen's forcing.
links:
  - godels-incompleteness
  - peano-arithmetic
  - set-operations
  - cantors-theorem
---

# Consistency & Independence

A statement $\varphi$ is **independent** of a theory $T$ if $T \not\vdash \varphi$ and $T \not\vdash \neg\varphi$ — neither $\varphi$ nor its negation is provable from $T$. Independence results reveal the genuine undecidability of mathematical questions within a given axiomatic framework. The most famous examples are in set theory: Gödel (1938) showed the **Axiom of Choice (AC)** and **Continuum Hypothesis (CH)** are consistent with ZF, and Cohen (1963) showed their negations are also consistent. Thus both AC and CH are independent of ZF (and CH is independent of ZFC). Cohen's method of **forcing** — constructing new models by adding "generic" sets — has since produced hundreds of independence results.

## Relative Consistency

To show $T + \varphi$ is consistent (assuming $T$ is consistent), it suffices to exhibit a model of $T$ in which $\varphi$ holds.

- **Gödel's constructible universe $L$**: a canonical minimal inner model of ZF in which AC and GCH hold. So ZF $\not\vdash \neg$AC and ZF $\not\vdash \neg$CH.
- **Cohen forcing**: builds a model $V[G]$ (a generic extension of $V$) in which $\neg$CH holds. So ZFC $\not\vdash$ CH.

## Forcing (Sketch)

Start with a ground model $V \models$ ZFC. Choose a **forcing poset** $\mathbb{P}$ and a $\mathbb{P}$-generic filter $G$ (existing in a larger universe). The **generic extension** $V[G]$ is a new model of ZFC in which $G$ (and the sets it codes) exist.

For the independence of CH: use $\mathbb{P} = \mathrm{Add}(\omega, \aleph_2)$ (adding $\aleph_2$ many Cohen reals). In $V[G]$: $2^{\aleph_0} \geq \aleph_2 > \aleph_1$, so CH fails.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Independent of $T$ | $T \not\vdash \varphi$ and $T \not\vdash \neg\varphi$ |
| Relative consistency | Con$(T) \Rightarrow$ Con$(T + \varphi)$ |
| ZF / ZFC | Zermelo–Fraenkel set theory without / with Axiom of Choice |
| AC | Axiom of Choice |
| CH | Continuum Hypothesis: $2^{\aleph_0} = \aleph_1$ |
| GCH | Generalised CH: $2^{\aleph_\alpha} = \aleph_{\alpha+1}$ |
| Constructible universe $L$ | Gödel's minimal inner model; satisfies AC and GCH |
| Forcing | Cohen's method of building generic model extensions |
| Generic filter $G$ | $\mathbb{P}$-generic: meets every dense subset of $\mathbb{P}$ in $V$ |
| $V[G]$ | generic extension of ground model $V$ |
