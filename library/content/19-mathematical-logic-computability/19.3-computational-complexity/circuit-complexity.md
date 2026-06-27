---
title: Circuit Complexity
tag: logic
summary: Boolean circuits are DAGs computing functions by AND, OR, NOT gates; circuit complexity measures the size and depth needed to compute a function, giving non-uniform models that are potentially easier to prove lower bounds for.
links:
  - p-vs-np
  - np-completeness
  - randomised-complexity
  - turing-machines
---

# Circuit Complexity

A **Boolean circuit** is a directed acyclic graph (DAG) where leaves are labelled by input variables or constants, and internal nodes are labelled by Boolean operations (AND $\land$, OR $\lor$, NOT $\neg$). The **size** of a circuit is the number of gates; the **depth** is the length of the longest path from input to output. Circuit complexity studies how small and shallow circuits can compute Boolean functions. Circuits are a **non-uniform** model: each input length $n$ may use a different circuit $C_n$. The class $\mathbf{P/poly}$ consists of problems decidable by polynomial-size circuit families. Proving super-polynomial circuit lower bounds for NP functions would imply P $\neq$ NP, making circuit complexity a central approach to the P vs NP problem.

## Definitions

A **circuit** $C$ of size $s$ and depth $d$ over inputs $x_1,\ldots,x_n$ computes a Boolean function $f: \{0,1\}^n \to \{0,1\}$.

**$\mathbf{P/poly}$**: $L \in \mathbf{P/poly}$ iff there is a polynomial $p$ and circuits $\{C_n\}$ with $|C_n| \leq p(n)$ and $C_n(x) = 1 \iff x \in L$ for all $x$ of length $n$.

**NC**: $\bigcup_k \mathbf{NC}^k$ where $\mathbf{NC}^k$ = poly-size, $O(\log^k n)$-depth circuits. $\mathbf{NC}^1 \subseteq \mathbf{L} \subseteq \mathbf{NC}^2 \subseteq \mathbf{P}$.

## Key Results

- **Karp–Lipton**: If NP $\subseteq$ P/poly then PH collapses to $\Sigma_2^P$.
- **Shannon (1949)**: Almost all Boolean functions require exponential circuit size.
- **Razborov–Smolensky**: Parity $\notin$ AC$^0[p]$ for prime $p \neq 2$ (restricted circuits).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Boolean circuit | DAG with AND, OR, NOT gates |
| Size $s$ | number of gates in circuit |
| Depth $d$ | longest input-to-output path |
| $\mathbf{P/poly}$ | polynomial-size circuit families; contains P |
| Non-uniform | different circuits for each input length |
| $\mathbf{NC}$ | Nick's class: polylog-depth, poly-size circuits |
| AC$^0$ | constant-depth, poly-size circuits; cannot compute parity |
| Karp–Lipton theorem | NP $\subseteq$ P/poly $\Rightarrow$ PH collapses |
| Circuit lower bound | proving no small circuit computes a function |
| Fan-in | number of inputs to a gate |
