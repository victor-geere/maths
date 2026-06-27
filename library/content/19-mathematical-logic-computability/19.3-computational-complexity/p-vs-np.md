---
title: P vs NP
tag: logic
summary: P is the class of problems solvable in polynomial time; NP is the class verifiable in polynomial time. Whether P = NP — i.e., whether every efficiently verifiable problem is efficiently solvable — is the most famous open question in mathematics.
links:
  - np-completeness
  - space-complexity
  - turing-machines
  - big-o-notation
---

# P vs NP

The **P vs NP problem** asks whether every problem whose solution can be **verified** in polynomial time can also be **solved** in polynomial time. The class **P** contains problems solvable in $O(n^k)$ time for some fixed $k$; **NP** contains problems where a proposed solution (certificate) can be verified in polynomial time. Clearly P $\subseteq$ NP; the question is whether NP $\subseteq$ P. Most complexity theorists believe P $\neq$ NP — that there are problems easy to check but hard to solve — but no proof exists. A proof either way would be one of the most significant results in the history of mathematics, with immediate consequences for cryptography, optimisation, and artificial intelligence.

## Definitions

**Deterministic TM running in polynomial time**: accepts or rejects in $O(n^k)$ steps on inputs of length $n$.

$$\mathbf{P} = \bigcup_{k \geq 0} \mathrm{DTIME}(n^k)$$

**NP** (nondeterministic polynomial time): $L \in \mathbf{NP}$ iff there is a polynomial-time verifier $V$ and polynomial $p$ such that:
$$x \in L \iff \exists c \text{ with } |c| \leq p(|x|) \text{ and } V(x,c) = 1$$

where $c$ is a **certificate** (witness).

## Examples

| Class | Problem |
|---|---|
| P | Sorting, shortest paths, primality testing |
| NP | SAT, Hamiltonian cycle, graph colouring, integer factoring |
| NP-complete | SAT, 3-SAT, Clique, Vertex Cover |

## Significance

- If P = NP: RSA and most cryptographic protocols break (factoring becomes easy).
- If P $\neq$ NP: confirms that hard problems are genuinely hard.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathbf{P}$ | polynomial-time decidable problems |
| $\mathbf{NP}$ | polynomial-time verifiable (with certificate) |
| Certificate / witness $c$ | short proof that $x \in L$ |
| Polynomial time | $O(n^k)$ for some fixed $k$ |
| $\mathbf{P} \subseteq \mathbf{NP}$ | verified by running the solver and checking |
| P vs NP | open: is $\mathbf{NP} \subseteq \mathbf{P}$? |
| Nondeterministic TM | TM that may branch; accepts if some branch accepts |
| co-NP | complements of NP problems; $\mathbf{NP} \cap \mathbf{co{-}NP}$ contains factoring |
