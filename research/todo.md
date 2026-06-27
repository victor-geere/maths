# Todo — Spectral Number Theory Research

Derived from [plan/project.md](../plan/project.md) and [research/index.md](index.md).
Status as of 2026-06-27.

---

## Phase 0 — Foundations & tooling

- [ ] Add `fibonacci_kernel(r, N, theta)` to `victor/prime-zeros.py`
- [ ] Add `ou_mehler(t, x, y, N)` to `victor/prime-zeros.py`
- [ ] Add `eta_kernel(r, sigma, theta)` to `victor/prime-zeros.py`
- [ ] Create `research/deliverables/spectral-data-sheet.md` with template row; fill in as objects are verified

---

## Phase 1 — Rigorous cases

### 1a. Prime sine wave — **COMPLETE**

No open items.

### 1b. Fibonacci kernel

- [ ] Run §6 numerics: verify $K_r(0)$ vs. truncated sum, PD on $\theta$-grid, eigenvalues vs. FFT, $\|K_r\|_2^2$ via Parseval; fill in §6 table in `project/fibonacci-kernel.md`
- [ ] Prove Lucas transfer multiplier: $L_n = F_{n-1} + F_{n+1}$ as bounded multiplier between Fibonacci and Lucas kernels, with explicit-formula trace identity

### 1c. Ornstein–Uhlenbeck process

- [ ] Run §7 numerics: Mehler closed form vs. truncated Hermite sum, trace $= 1/(1-e^{-t})$, Bernoulli coefficients, $\Gamma(s)\zeta(s)$ Mellin match (use `mpmath`); fill in §7 table in `project/ou-process.md`
- [ ] Formalise the functor $L^2(\gamma) \to L^2(\mathbb{T})$: show $\mathrm{diag}(r^{|n|})$ on $\mathbb{T}$ intertwines with $P_t|_{|n|}$ on $L^2(\gamma)$ as a bounded map *(Phase 4 gate)*

---

## Phase 2 — Dirichlet family

### 2a. η ↔ ζ transfer

- [ ] Run §5 numerics: verify E3 rotation identity ($K^\eta_r + K^\zeta_r(\cdot+\pi) \approx 0$), extra zeros, transfer correction Dirichlet coefficients; fill in §5 table in `project/eta-zeta-transfer.md`
- [ ] Prove measure-level equality: extra mass in eta explicit formula at $\{k \log 2\}$ with coefficients $1/k$

### 2b. Spectral triple / RH framework

- [ ] Upgrade Theorem 6.1 proof sketch to a full proof or a precise citation to Weil/Barner with a clear statement of what remains to verify
- [ ] Survey effective-bound literature (Bombieri–Lagarias zero-free regions via explicit formulas); add findings to open-questions list in `project/spectral-triple.md`

### 2c. General Dirichlet series *(not started)*

- [ ] Write `project/dirichlet-series.md`: kernel ↔ functional-equation dictionary for $L(s,\chi)$; state which steps go through unconditionally

---

## Phase 3 — Dynamical / hard cases *(independent of Phases 4 & 5)*

### 3a. Zeros ↔ primes explicit formula

- [ ] State Weil explicit formula with full hypotheses (Barner 1981 version); identify which step in Theorem 6.1 sketch is conditional on RH and which is unconditional

### 3b. Collatz orbit statistics *(not started)*

- [ ] Write feasibility memo: define the sequence (stopping-time distribution or orbit-length counts), check whether geometric damping gives convergence, decide if a spectral note is tractable

---

## Phase 4 — Generalisation

**Blocked.** Gate conditions:
- [ ] Phase 1b numerics done
- [ ] Phase 1c numerics done
- [ ] $L^2(\gamma) \to L^2(\mathbb{T})$ functor formalised

When unblocked:
- [ ] Write `project/generalised-algorithm.md`: abstract inputs/outputs, operator construction, hypotheses table, spectral-triple recipe as special case

---

## Phase 5 — Helix lift & quaternionic time

- [ ] Define quaternionic Hilbert module precisely (coefficient ring $\mathbb{H}$, right vs. left structure, S-spectrum setup); consult Colombo–Sabadini–Struppa
- [ ] Attempt H4(2): prove $D_t = -j\partial_t$ is self-adjoint on the module in the S-spectrum sense
- [ ] Test H4(3) numerically: apply helix lift to η kernel and verify that the cone indicator $Z^2 - (P^2 + G^2)$ becomes non-negative

---

## Numerical verification checklist

| Note | Check | Status |
|---|---|---|
| prime-sine-wave §6 | $\|Ψ_2\|^2 = P(4)$ to 10 digits | Done |
| fibonacci-kernel §6 | $K_r(0)$, PD grid, eigenvalues, $\|K_r\|_2^2$ | Not done |
| ou-process §7 | Mehler, trace, heat kernel, Mellin $\Gamma\zeta$ | Not done |
| eta-zeta-transfer §5 | rotation identity, extra zeros, transfer correction | Not done |
| spectral-triple §8 | extend to 100+ zeros, vary $\varepsilon$, port to Python | Partial (HTML only) |
| helix §6 | cone indicator on η kernel after helix lift | Not done |
