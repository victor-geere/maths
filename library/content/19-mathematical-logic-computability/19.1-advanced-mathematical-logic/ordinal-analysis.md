---
title: Ordinal Analysis
tag: logic
summary: Ordinal analysis assigns to each formal theory a proof-theoretic ordinal measuring its consistency strength; PA has ordinal ε₀ and stronger theories have larger ordinals encoding their combinatorial reach.
links:
  - peano-arithmetic
  - godels-incompleteness
  - consistency-independence
---

# Ordinal Analysis

**Ordinal analysis** is the branch of proof theory that measures the "consistency strength" of formal systems by assigning each a **proof-theoretic ordinal** — the smallest ordinal the system cannot prove is well-ordered. For Peano arithmetic (PA), this ordinal is $\varepsilon_0$ (the smallest ordinal satisfying $\omega^{\varepsilon_0} = \varepsilon_0$), proved by Gentzen (1936). Stronger systems have larger proof-theoretic ordinals: PA + transfinite induction up to $\varepsilon_0$ proves Con(PA), making the ordinal a precise measure of logical strength. Ordinal analysis converts metamathematical questions (consistency, provability) into concrete combinatorial questions about ordinal notations and well-foundedness.

## Ordinals as Measuring Sticks

The **proof-theoretic ordinal** $|T|$ of a theory $T$ is defined as:
$$|T| = \sup\{\alpha : T \vdash \text{"$\alpha$ is well-ordered"}\}$$

Equivalently, it is the order type of $T$'s provably recursive functions, or the smallest ordinal not achievable by $T$'s induction principles.

## Key Results

| Theory $T$ | Proof-theoretic ordinal $|T|$ |
|---|---|
| Robinson arithmetic $Q$ | $\omega$ |
| Peano arithmetic PA | $\varepsilon_0 = \omega^{\omega^{\omega^{\cdots}}}$ |
| ATR$_0$ | $\Gamma_0$ (Feferman–Schütte ordinal) |
| $\Pi_1^1$-CA$_0$ | $\psi(\Omega_\omega)$ |
| ZFC | unknown (very large) |

## $\varepsilon_0$ and Gentzen's Theorem

$\varepsilon_0 = \sup\{\omega, \omega^\omega, \omega^{\omega^\omega}, \ldots\}$ is the least fixed point of $\alpha \mapsto \omega^\alpha$.

**Gentzen's Theorem**: PA is consistent, provable using transfinite induction up to $\varepsilon_0$ but not below. Thus $|\mathrm{PA}| = \varepsilon_0$.

## Goodstein's Theorem

The Goodstein sequence $G(m)$ always terminates. Its proof uses ordinals up to $\varepsilon_0$; the statement is true but unprovable in PA.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Proof-theoretic ordinal $|T|$ | smallest ordinal not provably well-ordered by $T$ |
| $\varepsilon_0$ | least fixed point of $\alpha \mapsto \omega^\alpha$; proof-theoretic ordinal of PA |
| $\omega^\alpha$ | ordinal exponentiation |
| Well-ordering | every non-empty subset has a least element |
| Transfinite induction | induction along a well-ordered set beyond $\omega$ |
| Gentzen's theorem | Con(PA) provable using induction up to $\varepsilon_0$ |
| ATR$_0$ | arithmetical transfinite recursion; $|\mathrm{ATR}_0| = \Gamma_0$ |
| $\Gamma_0$ | Feferman–Schütte ordinal; limit of predicativity |
| Goodstein sequence | sequence proved terminating using ordinals but not in PA |
