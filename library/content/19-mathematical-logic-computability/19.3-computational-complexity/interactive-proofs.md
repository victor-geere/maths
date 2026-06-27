---
title: Interactive Proofs & IP = PSPACE
tag: logic
summary: An interactive proof system involves a computationally powerful prover convincing a polynomial-time verifier of a statement through interaction; the class IP equals PSPACE, a surprising collapse proved by Shamir (1992).
links:
  - p-vs-np
  - np-completeness
  - randomised-complexity
  - space-complexity
---

# Interactive Proofs & IP = PSPACE

An **interactive proof system** is a protocol between a computationally unbounded **prover** $P$ and a probabilistic polynomial-time **verifier** $V$, exchanging messages. The prover tries to convince the verifier that $x \in L$; the verifier accepts with high probability if $x \in L$ (completeness) and rejects with high probability if $x \notin L$ regardless of the prover's strategy (soundness). The class **IP** of languages with interactive proof systems is captured by this model. The astonishing **IP = PSPACE** theorem (Shamir 1992) shows that interactive proofs are extraordinarily powerful — equivalent to polynomial space — enabling a verifier to check statements like graph non-isomorphism and QBF satisfiability.

## Definitions

An **interactive proof** for $L$ is a pair $(P, V)$ with:
- **Completeness**: $x \in L \Rightarrow \Pr[V\text{ accepts}] \geq 2/3$ (in interaction with honest $P$)
- **Soundness**: $x \notin L \Rightarrow \Pr[V\text{ accepts}] \leq 1/3$ (for any prover $P^*$)

$$\mathbf{IP} = \{L : L\text{ has an interactive proof system}\}$$

## IP = PSPACE (Shamir, 1992)

**Theorem**: $\mathbf{IP} = \mathbf{PSPACE}$.

Upper bound (IP $\subseteq$ PSPACE): The verifier's optimal strategy can be computed in PSPACE.

Lower bound (PSPACE $\subseteq$ IP): The QBF protocol — the prover arithmetises the formula and uses **sum-check protocol** over a field — gives an interactive proof for QBF (PSPACE-complete).

## Sum-Check Protocol

For a multilinear polynomial $f: \mathbb{F}^n \to \mathbb{F}$, the verifier wishes to check $\sum_{x \in \{0,1\}^n} f(x) = C$. The prover peels off one variable at a time; each round reduces to checking a lower-dimensional sum.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Prover $P$ | computationally unbounded; sends messages |
| Verifier $V$ | probabilistic polynomial-time; decides to accept/reject |
| Completeness | $x \in L \Rightarrow V$ accepts with high probability |
| Soundness | $x \notin L \Rightarrow V$ rejects regardless of prover |
| $\mathbf{IP}$ | class of languages with interactive proof systems |
| $\mathbf{IP} = \mathbf{PSPACE}$ | Shamir 1992 |
| Sum-check protocol | interactive reduction to checking a single field element |
| Arithmetisation | encoding Boolean formula as a polynomial over a field |
| $\mathbf{MIP}$ | multi-prover interactive proofs; equals NEXP |
| Zero-knowledge proof | interactive proof revealing nothing beyond membership |
