---
title: Poisson Processes
tag: stochastic-processes
summary: A continuous-time stochastic process counting events that occur independently at a constant rate λ — the canonical model for random arrivals.
links:
  - poisson-distribution
  - exponential-distribution
  - markov-chains
---

# Poisson Processes

The **Poisson process** is the fundamental model for counting random events that arrive unpredictably at a constant average rate. Customers arriving at a bank, photons hitting a detector, earthquakes in a region, or calls to a call centre — whenever events are independent and occur at a roughly constant rate, the Poisson process is the natural model. It bridges the Poisson distribution (count of events in a fixed window) and the Exponential distribution (waiting time between events) into a single coherent framework. The Poisson process is the simplest continuous-time Markov chain and the building block for more complex stochastic models.

## Definition

A counting process $\{N(t) : t \geq 0\}$ is a **Poisson process** with rate $\lambda > 0$ if:

1. $N(0) = 0$
2. **Independent increments:** increments over disjoint time intervals are independent
3. **Stationary increments:** $N(t+s) - N(s) \sim \text{Poisson}(\lambda t)$ for all $s, t \geq 0$
4. At most one event can occur at any instant: $P(N(h) \geq 2) = o(h)$

## Key Distributions

- **Count in $[0,t]$:** $N(t) \sim \text{Poisson}(\lambda t)$; $\mathbb{E}[N(t)] = \lambda t$
- **$k$-th arrival time** $S_k = T_1 + \cdots + T_k \sim \text{Gamma}(k, \lambda)$
- **Inter-arrival times** $T_i = S_i - S_{i-1} \overset{\text{iid}}{\sim} \text{Exp}(\lambda)$

## Superposition and Thinning

- **Superposition:** if $N_1 \sim \text{PP}(\lambda_1)$ and $N_2 \sim \text{PP}(\lambda_2)$ independently, then $N_1 + N_2 \sim \text{PP}(\lambda_1 + \lambda_2)$.
- **Thinning:** if each event is independently retained with probability $p$, the retained events form $\text{PP}(\lambda p)$.

## Non-Homogeneous Poisson Process

If the rate varies with time, $\lambda(t)$:

$$N(s,t] \sim \text{Poisson}\!\left(\int_s^t \lambda(u)\,du\right)$$

## Applications

- **Queueing theory:** $M/M/1$ queue uses Poisson arrivals and Exponential service times
- **Reliability:** component failures as a Poisson process
- **Finance:** jump processes in option pricing

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $N(t)$ | number of events in $[0,t]$ |
| $\lambda$ | rate (events per unit time) |
| PP$(\lambda)$ | Poisson process with rate $\lambda$ |
| $T_i$ | inter-arrival time between $(i-1)$-th and $i$-th event |
| $S_k$ | arrival time of the $k$-th event |
| Independent increments | events in non-overlapping intervals are independent |
| Stationary increments | distribution of $N(t+s)-N(s)$ depends only on $t$ |
| $o(h)$ | a term negligible relative to $h$ as $h \to 0$ |
| Superposition | merging independent Poisson processes |
| Thinning | independent random deletion of events |
| $\text{Gamma}(k, \lambda)$ | distribution of sum of $k$ iid $\text{Exp}(\lambda)$ variables |
| $M/M/1$ queue | queue with Poisson arrivals, Exp service, 1 server |
