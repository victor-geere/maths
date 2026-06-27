---
title: Peano Arithmetic
tag: logic
summary: Peano arithmetic (PA) is the standard first-order axiomatisation of the natural numbers; it is strong enough for most number-theoretic reasoning yet incomplete and unable to prove its own consistency.
links:
  - godels-incompleteness
  - consistency-independence
  - peano-axioms
  - mathematical-induction
---

# Peano Arithmetic

**Peano arithmetic (PA)** is the standard first-order formal system for the natural numbers, named after Giuseppe Peano. Its language contains $0$, the successor function $S$, addition $+$, and multiplication $\times$. The axioms assert that $0$ is not a successor, $S$ is injective, addition and multiplication are defined recursively, and — crucially — an **induction schema**: for every formula $\varphi(x)$, if $\varphi(0)$ and $\forall x(\varphi(x) \to \varphi(Sx))$, then $\forall x\,\varphi(x)$. PA is powerful enough to prove all of elementary number theory, yet by Gödel's theorems it is incomplete and cannot prove Con(PA). The study of what PA can and cannot prove — proof theory and ordinal analysis — reveals deep connections between logic, combinatorics, and computability.

## Axioms of PA

1. $\forall x\,(S(x) \neq 0)$ — $0$ is not a successor
2. $\forall x\,\forall y\,(S(x) = S(y) \to x = y)$ — $S$ is injective
3. $\forall x\,(x + 0 = x)$
4. $\forall x\,\forall y\,(x + S(y) = S(x+y))$
5. $\forall x\,(x \times 0 = 0)$
6. $\forall x\,\forall y\,(x \times S(y) = x \times y + x)$
7. **Induction schema**: for every $\mathcal{L}_{PA}$-formula $\varphi(x)$:
$$\varphi(0) \land \forall x(\varphi(x) \to \varphi(S(x))) \to \forall x\,\varphi(x)$$

## What PA Can and Cannot Prove

PA proves: all true $\Sigma_1$ sentences (those of the form $\exists x_1 \cdots \exists x_n\,\varphi$ with $\varphi$ bounded), prime factorisation, Euclid's theorem, Chinese remainder theorem.

PA cannot prove: Con(PA), the Paris–Harrington theorem (a combinatorial strengthening of Ramsey's theorem), Goodstein's theorem.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| PA | Peano arithmetic: standard first-order theory of $\mathbb{N}$ |
| $S(x)$ | successor of $x$: $x+1$ |
| Induction schema | axiom scheme: one axiom per formula $\varphi$ |
| $\Sigma_1$ sentence | $\exists x_1\cdots\exists x_n\,\varphi$ with $\varphi$ bounded (decidable) |
| Con(PA) | "PA is consistent"; not provable in PA |
| Paris–Harrington theorem | true combinatorial statement unprovable in PA |
| Goodstein's theorem | every Goodstein sequence terminates; unprovable in PA |
| Non-standard model of PA | model containing elements $> S^n(0)$ for all $n$ |
| Robinson arithmetic $Q$ | PA without induction schema; finitely axiomatisable |
