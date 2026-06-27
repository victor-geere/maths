---
title: Randomised Complexity (BPP, RP)
tag: logic
summary: Randomised complexity classes allow TMs to flip coins; BPP contains problems solvable with bounded error probability, RP with one-sided error. BPP is widely believed equal to P, but this is unproven.
links:
  - p-vs-np
  - np-completeness
  - space-complexity
  - turing-machines
---

# Randomised Complexity (BPP, RP)

**Randomised complexity** studies what can be computed efficiently when a Turing machine is allowed to flip fair coins. A **probabilistic TM** (PTM) has a transition function that at each step may choose uniformly between two next steps. The key class is **BPP** (Bounded-error Probabilistic Polynomial time): problems decidable in polynomial time with error probability $\leq 1/3$. By amplification (repeating and taking a majority vote), the error can be reduced to $2^{-k}$ with $O(k)$ repetitions. Most complexity theorists believe $\mathbf{BPP} = \mathbf{P}$ (randomness adds no long-term power), supported by pseudorandomness theory and the hardness-vs-randomness paradigm, but the equality is unproven.

## Definitions

A **probabilistic TM** $M$ accepts with probability $\Pr[M(x) = 1]$ (over coin flips).

$$\mathbf{RP} = \{L : \exists\text{ poly-time PTM with } x\in L \Rightarrow \Pr[\mathrm{accept}] \geq 1/2,\ x\notin L \Rightarrow \Pr[\mathrm{accept}] = 0\}$$

$$\mathbf{BPP} = \{L : \exists\text{ poly-time PTM with } \Pr[\text{correct}] \geq 2/3\}$$

$$\mathbf{ZPP} = \mathbf{RP} \cap \mathbf{co{-}RP} \text{ (zero-error, expected poly time)}$$

## Inclusions

$$\mathbf{P} \subseteq \mathbf{ZPP} \subseteq \mathbf{RP} \subseteq \mathbf{BPP} \subseteq \mathbf{P/poly}, \quad \mathbf{BPP} \subseteq \mathbf{PSPACE}$$
$$\mathbf{RP} \subseteq \mathbf{NP}$$

## Amplification

If $M$ decides $L$ with error $\leq 1/3$, run $M$ $k$ times and take majority: error $\leq e^{-\Omega(k)}$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Probabilistic TM (PTM) | TM with coin flips; each path has a probability |
| $\mathbf{RP}$ | one-sided error: no false positives |
| $\mathbf{BPP}$ | two-sided bounded error $\leq 1/3$ |
| $\mathbf{ZPP}$ | zero-error expected polynomial time |
| co-RP | complements of RP problems; no false negatives |
| Error probability | $\Pr[M(x) \neq \chi_L(x)]$ |
| Amplification | repeat and vote to reduce error exponentially |
| $\mathbf{P/poly}$ | polynomial-size circuit families |
| Hardness-vs-randomness | pseudorandom generators from hard functions $\Rightarrow$ BPP = P |
