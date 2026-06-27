---
title: NP-Completeness & Cook–Levin
tag: logic
summary: A problem is NP-complete if it is in NP and every NP problem reduces to it in polynomial time; the Cook–Levin theorem shows SAT is NP-complete, making it the hardest problem in NP.
links:
  - p-vs-np
  - space-complexity
  - reducibility-degrees
  - turing-machines
---

# NP-Completeness & Cook–Levin

An **NP-complete** problem is simultaneously in NP and as hard as every other problem in NP — if it can be solved in polynomial time, then all of NP can be. The **Cook–Levin theorem** (Cook 1971, Levin 1973) proves that **SAT** (satisfiability of propositional formulas) is NP-complete: every NP problem reduces to SAT in polynomial time. Subsequently, Karp (1972) showed 21 other combinatorial problems are NP-complete by polynomial reductions. NP-complete problems are believed (but not proved) to be intractable: no polynomial-time algorithm is known, and finding or ruling one out would resolve P vs NP.

## Definitions

$A \leq_p B$ (**polynomial-time many-one reduction**): $x \in A \iff f(x) \in B$ for a polynomial-time computable $f$.

$L$ is **NP-hard** if every $A \in \mathbf{NP}$ satisfies $A \leq_p L$.

$L$ is **NP-complete** if $L \in \mathbf{NP}$ and $L$ is NP-hard.

## Cook–Levin Theorem

**SAT** = $\{\langle \varphi \rangle : \varphi$ is a satisfiable propositional formula$\}$ is NP-complete.

**Proof sketch**: Given a nondeterministic TM $M$ accepting in time $p(n)$, encode a tableau (computation table) as a propositional formula $\varphi_M$ of size $O(p(n)^2)$ such that $\varphi_M$ is satisfiable iff $M$ accepts its input. So $L(M) \leq_p SAT$.

## Classic NP-Complete Problems

3-SAT, Clique, Independent Set, Vertex Cover, Hamiltonian Cycle, Hamiltonian Path, Travelling Salesman (decision), Graph Colouring ($k \geq 3$), Subset Sum, Integer Programming.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| SAT | propositional satisfiability |
| 3-SAT | SAT where each clause has exactly 3 literals |
| NP-complete | hardest problems in NP; all of NP reduces to them |
| NP-hard | every NP problem reduces to this (may not be in NP) |
| $A \leq_p B$ | polynomial-time many-one reduction |
| Cook–Levin theorem | SAT is NP-complete |
| Karp reductions | chain of polynomial reductions showing 21 problems NP-complete |
| Tableau | computation history matrix used in Cook–Levin proof |
| P = NP iff | some NP-complete problem is in P |
