---
title: Turing Machines
tag: logic
summary: A Turing machine is an abstract model of computation with a finite state controller and an infinite tape; it defines what is computable and undecidable, and is equivalent in power to all other known models of computation.
links:
  - church-turing
  - halting-problem
  - recursive-functions
  - p-vs-np
---

# Turing Machines

A **Turing machine** (Alan Turing, 1936) is a mathematical model of computation consisting of a finite-state controller and an infinite tape of cells. At each step, the machine reads the current tape symbol, transitions to a new state, writes a symbol, and moves left or right. Despite this extreme simplicity, Turing machines can compute any function that any digital computer can compute — they are the universal model of computation. Their power comes from the infinite tape (unbounded memory) and the ability to simulate any algorithmic process. Crucially, not all problems are computable: the **halting problem** (does a given machine halt on a given input?) is undecidable — no Turing machine can solve it.

## Formal Definition

A Turing machine is a tuple $M = (Q, \Gamma, b, \Sigma, \delta, q_0, F)$ where:
- $Q$: finite set of states
- $\Gamma$: tape alphabet ($b \in \Gamma$ is the blank symbol)
- $\Sigma \subseteq \Gamma \setminus \{b\}$: input alphabet
- $\delta: Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$: transition function
- $q_0 \in Q$: start state
- $F \subseteq Q$: accepting states

## Computation

A **configuration** is $(q, \text{tape content}, \text{head position})$. The machine accepts input $w$ if it reaches a state in $F$; it may also reject or loop forever.

## Universal Turing Machine

There exists a **universal Turing machine** $U$ that, given the description $\langle M \rangle$ of any machine $M$ and input $w$, simulates $M$ on $w$. This is the theoretical basis for stored-program computers.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $Q$ | finite set of states |
| $\Gamma$ | tape alphabet |
| $\Sigma$ | input alphabet |
| $\delta$ | transition function |
| $b$ | blank symbol |
| $L, R$ | head moves left, right |
| Configuration | snapshot: state + tape + head position |
| Accept / Reject / Loop | possible outcomes of a computation |
| Universal TM $U$ | simulates any other Turing machine |
| Decidable language | recognised by a TM that always halts |
| Recognisable language | recognised by some TM (may loop) |
