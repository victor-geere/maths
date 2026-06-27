---
title: Hilbert Space Formalism
tag: quantum-mechanics
summary: The mathematical framework of quantum mechanics — states as unit vectors, observables as self-adjoint operators, measurement outcomes as spectra, and dynamics as unitary evolution.
links:
  - hilbert-spaces
  - spectral-theory
  - bounded-operators
  - observables-operators
  - dirac-notation
---

# Hilbert Space Formalism

Quantum mechanics is formulated entirely in the language of Hilbert spaces. A **quantum state** is a unit vector in a complex Hilbert space $\mathcal{H}$; a physical **observable** is a self-adjoint operator on $\mathcal{H}$ whose spectrum gives the possible measurement outcomes; and **time evolution** is a one-parameter group of unitary operators. This is the same structure that governs the spectral theory of convolution operators on $L^2(\mathbb{T})$: the eigenvalues of a self-adjoint operator are real, the eigenvectors are orthonormal, and the spectral theorem diagonalises the operator — in both QM and in spectral number theory, the arithmetic sequence becomes the spectrum.

## The State Space

The **state** of a quantum system is a vector $|\psi\rangle \in \mathcal{H}$ with $\langle\psi|\psi\rangle = 1$ (a unit vector). Two vectors differing only by a phase $e^{i\theta}$ represent the same physical state.

**Pure vs. mixed states.** A **pure state** is a single unit vector (or equivalently the rank-1 projection $|\psi\rangle\langle\psi|$). A **mixed state** is a convex combination of pure states, represented by a **density matrix** $\rho \geq 0$ with $\mathrm{tr}(\rho) = 1$.

**Composite systems.** If system $A$ lives in $\mathcal{H}_A$ and system $B$ in $\mathcal{H}_B$, the joint system lives in the **tensor product** $\mathcal{H}_A \otimes \mathcal{H}_B$. States that do not factorise as $|\psi_A\rangle \otimes |\psi_B\rangle$ are **entangled**.

## Observables and Self-Adjoint Operators

An **observable** is a self-adjoint (Hermitian) operator $A = A^*$ on $\mathcal{H}$.

**Why self-adjoint?** Self-adjointness forces the spectrum to be real — a necessary condition for measurement outcomes to be real numbers — and guarantees the spectral theorem.

**Domain subtlety.** On infinite-dimensional spaces, $A$ may be **unbounded** (e.g. position $\hat{x}$, momentum $\hat{p} = -i\hbar\partial_x$). Then $A$ is only defined on a dense domain $\mathcal{D}(A) \subset \mathcal{H}$, and self-adjointness requires $A = A^*$ with equal domains — stronger than mere symmetry ($\langle Au, v\rangle = \langle u, Av\rangle$ for all $u,v \in \mathcal{D}(A)$).

## The Spectral Theorem

For every self-adjoint operator $A$ there exists a **projection-valued measure** (PVM) $E: \mathcal{B}(\mathbb{R}) \to \mathcal{B}(\mathcal{H})$ such that:

$$A = \int_{\mathbb{R}} \lambda\, dE(\lambda)$$

**Discrete spectrum.** If $A$ has a purely discrete spectrum with eigenvalues $\lambda_n$ and orthonormal eigenvectors $|n\rangle$:

$$A = \sum_n \lambda_n |n\rangle\langle n|, \qquad \mathbf{1} = \sum_n |n\rangle\langle n|$$

The second identity is **completeness** (resolution of the identity). Every state expands as $|\psi\rangle = \sum_n c_n |n\rangle$ with $c_n = \langle n|\psi\rangle$ and $\sum_n |c_n|^2 = 1$.

**Continuous spectrum.** For $\hat{x}$ on $L^2(\mathbb{R})$, the "eigenvectors" $|x\rangle$ are distributions (not true $L^2$ vectors), and completeness reads $\int |x\rangle\langle x|\,dx = \mathbf{1}$.

## Measurement Postulate and the Born Rule

When observable $A$ is measured on state $|\psi\rangle$:

- The outcome is one of the **eigenvalues** $\lambda \in \sigma(A)$.
- The probability of outcome $\lambda_n$ (discrete case) is $P(\lambda_n) = |\langle n|\psi\rangle|^2 = \langle\psi|E_n|\psi\rangle$.
- After the measurement the state **collapses** to the normalised projection $E_n|\psi\rangle / \|E_n|\psi\rangle\|$.
- The **expectation value** is $\langle A\rangle_\psi = \langle\psi|A|\psi\rangle = \sum_n \lambda_n |\langle n|\psi\rangle|^2$.

## Canonical Commutation Relations

Position $\hat{x}$ and momentum $\hat{p} = -i\hbar\partial_x$ on $L^2(\mathbb{R})$ satisfy:

$$[\hat{x},\hat{p}] = \hat{x}\hat{p} - \hat{p}\hat{x} = i\hbar\mathbf{1}$$

This algebraic relation (not their specific matrix/differential realisation) is the core of the Heisenberg uncertainty principle $\Delta x\,\Delta p \geq \hbar/2$.

**Number operator.** The **harmonic oscillator** creation/annihilation operators $a^\dagger, a$ satisfy $[a, a^\dagger] = 1$. The **number operator** $N = a^\dagger a$ has eigenvalues $0, 1, 2, \ldots$ with eigenstates the Hermite functions — exactly the spectrum of the Ornstein–Uhlenbeck generator $L = \partial_x^2 - x\partial_x$ (up to sign), which is the damping mechanism at the core of the kernel construction in this project.

## Time Evolution

**Schrödinger picture.** The state evolves; operators are fixed. The **Schrödinger equation** is:

$$i\hbar\frac{d}{dt}|\psi(t)\rangle = H|\psi(t)\rangle$$

where $H = H^*$ is the **Hamiltonian**. The formal solution is $|\psi(t)\rangle = e^{-iHt/\hbar}|\psi(0)\rangle$. The propagator $U(t) = e^{-iHt/\hbar}$ is **unitary** ($U(t)^* = U(t)^{-1}$), preserving norms and inner products.

**Heisenberg picture.** Alternatively, states are fixed and operators evolve: $A(t) = U(t)^* A U(t)$.

**Heat kernel / imaginary time.** Replacing $t \mapsto -i\tau$ (Wick rotation) sends $e^{-iHt/\hbar}$ to $e^{-H\tau/\hbar}$, a **semigroup** of self-adjoint operators. Its integral kernel is the **heat kernel** $p_\tau(x,y)$; for the harmonic oscillator, this is the **Mehler kernel** whose Fourier coefficients are exactly the geometric weights $r^n$ used in damping arithmetic sequences.

## Standard Hilbert Spaces in QM

| System | Hilbert space $\mathcal{H}$ | Key operators |
|---|---|---|
| Particle on $\mathbb{R}$ | $L^2(\mathbb{R})$ | $\hat{x}$, $\hat{p} = -i\hbar\partial_x$ |
| Harmonic oscillator | $L^2(\mathbb{R})$ | $H = \hbar\omega(N + \tfrac{1}{2})$, $N = a^\dagger a$ |
| Spin-$\tfrac{1}{2}$ | $\mathbb{C}^2$ | Pauli matrices $\sigma_x, \sigma_y, \sigma_z$ |
| Many-body (bosons) | Fock space $\bigoplus_n \mathcal{H}^{\otimes_s n}$ | $a, a^\dagger$ (field operators) |
| Functions on the circle | $L^2(\mathbb{T})$ | Convolution operators $T_K$, shift $S$ |

The last row is the arena of this research project: the Hilbert space $L^2(\mathbb{T})$ with convolution operators whose spectra are the damped arithmetic sequences $(a_n w_n)$.

## Connection to Spectral Number Theory

The formal analogy between QM and the spectral kernel framework is exact:

| Quantum mechanics | Spectral kernel framework |
|---|---|
| Hilbert space $\mathcal{H}$ | $L^2(\mathbb{T})$ |
| Observable $A = A^*$ | Convolution operator $T_K$ |
| Eigenvalues $\lambda_n \in \sigma(A)$ | Damped sequence $\lambda_n = a_n w_n$ |
| Orthonormal eigenbasis $\{|n\rangle\}$ | Exponentials $\{e^{in\theta}\}$ |
| Completeness $\sum_n |n\rangle\langle n| = \mathbf{1}$ | Parseval's identity |
| Positive semidefiniteness | Bochner positivity ($\lambda_n \geq 0$) |
| Hamiltonian semigroup $e^{-Ht}$ | Mehler kernel / geometric damping $r^n$ |

The transfer operator between two kernels is the QM analogue of a relative Hamiltonian, and the explicit formula is the analogue of the trace identity $\mathrm{tr}(e^{-Ht}) = \sum_n e^{-\lambda_n t}$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathcal{H}$ | complex Hilbert space (state space of the system) |
| $\|\psi\rangle$ | ket: a state vector (Dirac notation) |
| $\langle\psi\|$ | bra: the dual functional to $\|\psi\rangle$ |
| $\langle\phi\|\psi\rangle$ | inner product (bracket) |
| $\|\psi\rangle\langle\psi\|$ | rank-1 projection onto $\|\psi\rangle$ |
| $A = A^*$ | self-adjoint (Hermitian) operator — real spectrum |
| $\sigma(A)$ | spectrum of $A$: possible measurement outcomes |
| $\sigma_p(A)$ | point spectrum: genuine eigenvalues |
| PVM $E(\cdot)$ | projection-valued measure; integrates to give $A$ |
| Born rule | $P(\lambda_n) = \|\langle n\|\psi\rangle\|^2$ |
| $\langle A\rangle_\psi$ | expectation value $\langle\psi\|A\|\psi\rangle$ |
| $[A,B] = AB - BA$ | commutator |
| $[\hat{x},\hat{p}] = i\hbar$ | canonical commutation relation |
| $H$ | Hamiltonian: the energy observable generating time evolution |
| $U(t) = e^{-iHt/\hbar}$ | time-evolution operator (unitary) |
| $N = a^\dagger a$ | number operator; spectrum $\{0,1,2,\ldots\}$ |
| Mehler kernel | heat kernel of the harmonic oscillator / OU generator |
| $\rho$ | density matrix: $\rho \geq 0$, $\mathrm{tr}(\rho)=1$ |
| $T_K$ | convolution operator on $L^2(\mathbb{T})$ with kernel $K$ |
