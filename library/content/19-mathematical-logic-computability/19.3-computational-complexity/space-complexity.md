---
title: Space Complexity (PSPACE, L)
tag: logic
summary: Space complexity measures memory usage; PSPACE contains problems solvable in polynomial space, L in logarithmic space. PSPACE contains NP, and quantified Boolean formula (QBF) is PSPACE-complete.
links:
  - p-vs-np
  - np-completeness
  - randomised-complexity
  - turing-machines
---

# Space Complexity (PSPACE, L)

**Space complexity** measures the amount of memory (tape cells) a Turing machine uses, as a function of input length. While time complexity focuses on speed, space complexity captures memory requirements and often behaves differently — in particular, space can be **reused**, allowing more power per unit. The main classes are: **L** (logarithmic space), **NL** (nondeterministic log space), **P** and **NP** (time-based but also space-bounded), and **PSPACE** (polynomial space). The key inclusion is $\mathbf{L} \subseteq \mathbf{NL} \subseteq \mathbf{P} \subseteq \mathbf{NP} \subseteq \mathbf{PSPACE}$; whether any of these is strict (besides $\mathbf{L} \subsetneq \mathbf{PSPACE}$) is open.

## Definitions

$$\mathbf{DSPACE}(s(n)) = \{L : L\text{ decided by TM using }O(s(n))\text{ space}\}$$

$$\mathbf{L} = \mathbf{DSPACE}(\log n), \quad \mathbf{PSPACE} = \bigcup_k \mathbf{DSPACE}(n^k)$$

## PSPACE-Completeness

**QBF** (Quantified Boolean Formula) = $\{\langle\varphi\rangle : \varphi$ is a true closed QBF$\}$, where $\varphi = Q_1 x_1 \cdots Q_n x_n\, \psi$ with $Q_i \in \{\forall, \exists\}$.

**Theorem**: QBF is PSPACE-complete. The extra universal quantifiers capture the power beyond NP.

## Savitch's Theorem

$$\mathbf{NSPACE}(s(n)) \subseteq \mathbf{DSPACE}(s(n)^2)$$

In particular, $\mathbf{PSPACE} = \mathbf{NPSPACE}$ (nondeterminism doesn't help for polynomial space).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Space complexity | max tape cells used by TM on length-$n$ input |
| $\mathbf{L}$ | $O(\log n)$ deterministic space |
| $\mathbf{NL}$ | $O(\log n)$ nondeterministic space |
| $\mathbf{PSPACE}$ | polynomial space |
| $\mathbf{NPSPACE}$ | nondeterministic polynomial space |
| QBF | Quantified Boolean Formula; PSPACE-complete |
| Savitch's theorem | NSPACE$(s) \subseteq$ DSPACE$(s^2)$ |
| $\mathbf{L} \subseteq \mathbf{P}$ | log space $\Rightarrow$ poly time (space $\leq$ time on each cell) |
| $\mathbf{P} \subseteq \mathbf{PSPACE}$ | poly time uses at most poly space |
| Inclusion chain | $\mathbf{L} \subseteq \mathbf{NL} \subseteq \mathbf{P} \subseteq \mathbf{NP} \subseteq \mathbf{PSPACE}$ |
