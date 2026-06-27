---
title: Markov Chains
tag: stochastic-processes
summary: Random processes where the future depends only on the present state, not the history — characterised by a transition matrix and classified by their long-run behaviour.
links:
  - random-variables
  - expectation-variance
  - poisson-process
---

# Markov Chains

A **Markov chain** is a random process that jumps between states, where the probability of transitioning to the next state depends only on the **current state** — not on how the process got there. This "memoryless" property, called the **Markov property**, makes the process analytically tractable while remaining rich enough to model queues, stock prices, search engine rankings (PageRank), genetics, and text generation. The long-run behaviour is governed by the **stationary distribution**: a probability vector $\pi$ such that, once reached, the system stays at that distribution. Under mild conditions (irreducibility and aperiodicity), every Markov chain converges to its unique stationary distribution regardless of where it starts.

## Definition

A sequence $(X_0, X_1, X_2, \ldots)$ of random variables taking values in a state space $S$ is a **Markov chain** if:

$$P(X_{n+1} = j \mid X_0, X_1, \ldots, X_n) = P(X_{n+1} = j \mid X_n)$$

## Transition Matrix

For a finite state space $S = \{1, \ldots, k\}$, the **transition matrix** $P$ has entries:

$$P_{ij} = P(X_{n+1} = j \mid X_n = i)$$

Every row sums to 1 ($\sum_j P_{ij} = 1$). The $n$-step transition probabilities are $P^n$.

## Stationary Distribution

A probability vector $\pi$ (with $\sum_j \pi_j = 1$) is a **stationary distribution** if:

$$\pi P = \pi, \quad \text{i.e.}\quad \pi_j = \sum_i \pi_i P_{ij}$$

## Ergodic Theorem

For an **irreducible** and **aperiodic** Markov chain, there is a unique stationary distribution $\pi$, and:

$$P^n_{ij} \to \pi_j \text{ as } n \to \infty$$

The long-run fraction of time in state $j$ is $\pi_j$.

## Classification of States

- **Recurrent:** the chain returns to this state with probability 1
- **Transient:** eventually leaves and never returns with positive probability
- **Absorbing:** $P_{ii} = 1$
- **Irreducible:** all states communicate (every state reachable from every other)
- **Period of state $i$:** $d = \gcd\{n \geq 1 : P^n_{ii} > 0\}$; aperiodic if $d = 1$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $X_n$ | state at time $n$ |
| $P_{ij}$ | transition probability from state $i$ to state $j$ |
| $P$ (matrix) | transition matrix; rows sum to 1 |
| $P^n$ | $n$-step transition matrix |
| $\pi$ | stationary distribution: $\pi P = \pi$ |
| Markov property | future depends only on present, not past |
| Irreducible | all states communicate — any state reachable from any other |
| Aperiodic | period $d=1$ for all states; no forced cycles |
| Ergodic | irreducible + aperiodic; guarantees unique stationary distribution |
| Recurrent | chain returns to state with probability 1 |
| Transient | chain leaves state permanently with positive probability |
| Absorbing state | $P_{ii}=1$; once entered, never leaves |
