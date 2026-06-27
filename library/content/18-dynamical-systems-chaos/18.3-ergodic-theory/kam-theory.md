---
title: Hamiltonian Systems & KAM Theory
tag: dynamical-systems
summary: Hamiltonian systems preserve energy and phase-space volume; KAM theory (Kolmogorov–Arnold–Moser) shows that most invariant tori of an integrable Hamiltonian system survive small perturbations.
links:
  - measure-preserving
  - mixing-entropy
  - ergodicity
  - stable-unstable-manifolds
  - phase-portraits
---

# Hamiltonian Systems & KAM Theory

A **Hamiltonian system** is a dynamical system on phase space $\mathbb{R}^{2n}$ (or a symplectic manifold) governed by Hamilton's equations $\dot{q}_i = \partial H/\partial p_i$, $\dot{p}_i = -\partial H/\partial q_i$, where $H(p,q)$ is the Hamiltonian (energy). Hamiltonian flows preserve the Hamiltonian $H$ (energy conservation) and the **Liouville measure** $dp\,dq$ (Liouville's theorem, the mathematical form of conservation of phase-space volume). **KAM theory** (Kolmogorov 1954, Arnold 1963, Moser 1962) answers the question: do the invariant tori of an integrable system persist under small perturbations? The answer is mostly yes — a positive-measure set of tori with sufficiently irrational frequency ratios survive — but the remaining orbits can be chaotic (Arnold diffusion).

## Hamilton's Equations

$$\dot{q}_i = \frac{\partial H}{\partial p_i}, \quad \dot{p}_i = -\frac{\partial H}{\partial q_i}, \quad i = 1,\ldots,n$$

The flow preserves $H$ (so trajectories lie on level sets $\{H = E\}$) and the symplectic form $\omega = \sum dp_i \wedge dq_i$.

## Integrable Systems & Action-Angle Variables

A Hamiltonian with $n$ degrees of freedom is **completely integrable** (Liouville–Arnold) if it has $n$ independent conserved quantities $F_1 = H, F_2, \ldots, F_n$ in involution ($\{F_i, F_j\} = 0$). In **action-angle coordinates** $(I, \theta) \in \mathbb{R}^n \times \mathbb{T}^n$: $H = H(I)$, $\dot{I} = 0$, $\dot{\theta} = \nabla_I H(I) = \omega(I)$ (frequencies).

## KAM Theorem

**KAM Theorem**: For $H = H_0(I) + \epsilon H_1(I,\theta)$ (small perturbation of integrable system $H_0$), most invariant tori with **Diophantine** frequency vectors $\omega = (\omega_1,\ldots,\omega_n)$ (satisfying $|k \cdot \omega| \geq \gamma |k|^{-\tau}$ for all $k \in \mathbb{Z}^n \setminus \{0\}$) survive for small $\epsilon$.

The surviving tori form a set of positive measure (close to full measure for small $\epsilon$).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Hamiltonian $H(p,q)$ | energy function; generates the flow via Hamilton's equations |
| Phase space | $\mathbb{R}^{2n}$ with coordinates $(q_1,\ldots,q_n,p_1,\ldots,p_n)$ |
| Symplectic form $\omega = \sum dp_i\wedge dq_i$ | closed non-degenerate 2-form; preserved by Hamiltonian flow |
| Liouville's theorem | Hamiltonian flow preserves volume $dp\,dq$ |
| Completely integrable | $n$ independent integrals in involution |
| Action-angle coordinates $(I,\theta)$ | $H=H(I)$; $\theta$ evolves linearly in $t$ |
| Invariant torus | $\{I = \mathrm{const}\}$; parametrised by $\theta \in \mathbb{T}^n$ |
| Frequency vector $\omega(I)$ | $\dot{\theta} = \omega(I)$; rational $\Rightarrow$ periodic, irrational $\Rightarrow$ quasi-periodic |
| Diophantine condition | $|k\cdot\omega| \geq \gamma|k|^{-\tau}$; measures irrationality |
| KAM theorem | most tori (with Diophantine $\omega$) survive small perturbations |
| Arnold diffusion | slow drift along resonances in perturbed Hamiltonian systems ($n \geq 3$) |
