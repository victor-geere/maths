---
title: Church–Turing Thesis
tag: logic
summary: The Church–Turing thesis is the assertion that every effectively computable function is computable by a Turing machine; it is a philosophical thesis, not a theorem, but is supported by the equivalence of all known models of computation.
links:
  - turing-machines
  - recursive-functions
  - halting-problem
---

# Church–Turing Thesis

The **Church–Turing thesis** is the foundational claim of computability theory: every function that can be computed by an effective (algorithmic) procedure can be computed by a **Turing machine**. Independently, Alonzo Church proposed that the effectively computable functions are exactly the **$\lambda$-definable** functions; Kleene identified them with the **general recursive functions**. All three definitions turn out to be equivalent, providing powerful evidence for the thesis. The thesis is not a mathematical theorem (since "effectively computable" is an informal, intuitive notion) but it has the status of a well-confirmed scientific hypothesis: no natural computation model has been found that exceeds Turing machine power. It sets the boundary between the solvable and the unsolvable.

## Equivalent Models

All the following define the same class of computable functions:
- Turing machines
- $\lambda$-calculus (Church)
- General recursive functions (Kleene)
- Register machines / RAM machines
- Cellular automata (Conway's Game of Life)
- Any modern programming language

## Physical Church–Turing Thesis

The stronger claim: every physical process can be simulated by a Turing machine. This is debated — quantum computation and hypercomputation are potential challenges, though no physical hypercomputer has been demonstrated.

## Implications

- There exist well-defined mathematical problems with no algorithmic solution (e.g., halting problem, Hilbert's 10th problem).
- Any two universal computational systems can simulate each other.
- The limits of computation are fundamental, not technological.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Effective procedure | algorithm: finite, deterministic, step-by-step computation |
| Turing-computable | computable by some Turing machine |
| $\lambda$-calculus | Church's model: computation as function application |
| General recursive function | Kleene's model: built from basic functions by composition and recursion |
| Church–Turing thesis | effective computability $=$ Turing computability |
| Universal computation | ability to simulate any other computation |
| Hypercomputation | hypothetical computation beyond Turing machines |
| Hilbert's 10th problem | no algorithm for solvability of Diophantine equations (Matiyasevich) |
