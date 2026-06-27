# Research Project Plan — Spectral Number Theory

*Derived from [README.md](../README.md) and all current project notes.
Status as of 2026-06-27.*

---

## 1. Goal and pipeline

Build a **generalised algorithm** that takes any arithmetic sequence and
mechanically produces:

```
sequence  →  damped kernel  →  self-adjoint operator  →  spectrum
                                                             ↓
                              explicit formula  ←  transfer operator
```

The pipeline is prototype-complete for the zeros↔primes / RH case
([spectral-triple.md](../project/spectral-triple.md)); the plan below fills in the
remaining objects and tightens the rigour.

---

## 2. Current status by phase

### Phase 0 — Foundations and tooling

| Item | Status | Gap |
|---|---|---|
| General recipe (damp → symmetrise → kernel) | **Done** (spectral-triple.html §3) | — |
| Python toolkit `prime-zeros.py` | **Partial** — computes $Z,P,G$, helix, cone indicator | Fibonacci, OU, eta checks not yet added |
| Spectral data sheet (catalogue rows) | **Not started** | Need one row per object (see §3) |

**Next actions (Phase 0)**
- [ ] Extend `prime-zeros.py` with functions `fibonacci_kernel(r, N, theta)`,
  `ou_mehler(t, x, y, N)`, and `eta_kernel(r, sigma, theta)` so the §6 numerical
  verification blocks in each note can be filled in programmatically.
- [ ] Create `project/spectral-data-sheet.md` with an empty template row and
  fill in completed objects as they are verified.

---

### Phase 1 — Easy, fully rigorous cases

#### 1a. Prime sine wave ([prime-sine-wave.md](../project/prime-sine-wave.md))

| Theorem | Status |
|---|---|
| T1 Domain $\sigma>\tfrac12$ | **Proved** |
| T2 Energy $= P(2\sigma)$ | **Proved** |
| T3 Kernel $= P(s+\overline{s'})$ | **Proved** |
| T4 Boundary blow-up (Mertens rate) | **Proved** |
| Numerics §6 (10-digit match at $s=2$) | **Done** |

Status: **complete**. No open items.

#### 1b. Fibonacci kernel ([fibonacci-kernel.md](../project/fibonacci-kernel.md))

| Theorem | Status |
|---|---|
| F1 Domain $r<1/\varphi$, positive definite | **Proved** |
| F2 Rational closed form | **Proved** |
| F3 Spectrum $\lambda_n=F_{|n|}r^{|n|}$ | **Proved** |
| F4 Total mass | **Proved** |
| Numerics §6 | **Not done** |
| Fibonacci↔Lucas transfer multiplier | **Open** |

**Next actions (Phase 1b)**
- [ ] Add `fibonacci_kernel` to `prime-zeros.py`; verify $K_r(0)$ vs. truncated
  sum, PD (min ≥ 0 on $\theta$-grid), eigenvalues vs. FFT, and $\|K_r\|_2^2$
  via Parseval. Fill in the table in §6.
- [ ] State and prove (or cite) the Lucas transfer multiplier: $L_n=F_{n-1}+F_{n+1}$
  as a bounded multiplier between the Fibonacci and Lucas kernels, with the
  explicit-formula trace identity it implies.

#### 1c. Ornstein–Uhlenbeck process ([ou-process.md](../project/ou-process.md))

| Theorem | Status |
|---|---|
| O1 Spectrum $-\mathbb{N}$, Hermite eigenbasis | **Proved** |
| O2 Number operator $-L=a^\dagger a$ | **Proved** |
| O3 Semigroup $=$ geometric damping, Mehler kernel | **Proved** |
| O4 Trace / heat kernel, Bernoulli expansion | **Proved** |
| O5 Spectral zeta $= \zeta$, $\Gamma(s)\zeta(s)=\int t^{s-1}\Theta\,dt$ | **Proved** |
| Numerics §7 | **Not done** |
| Functor $L^2(\gamma)\to L^2(\mathbb{T})$ beyond index-level | **Open** |

**Next actions (Phase 1c)**
- [ ] Add `ou_mehler` to `prime-zeros.py`; verify Mehler closed form vs. truncated
  Hermite sum, trace $= 1/(1-e^{-t})$, Bernoulli coefficients, and
  $\Gamma(s)\zeta(s)$ Mellin numerical match (use `mpmath`). Fill in §7 table.
- [ ] (Phase 4 prerequisite) Formalise the index-level correspondence
  $\operatorname{diag}(r^{|n|})$ on $\mathbb{T}$ ↔ $P_t|_{|n|}$ on $L^2(\gamma)$
  as a bounded intertwining map.

---

### Phase 2 — Dirichlet-series family

#### 2a. η ↔ ζ transfer ([eta-zeta-transfer.md](../project/eta-zeta-transfer.md))

| Theorem | Status |
|---|---|
| E1 Domain: η converges for $\Re s>0$ | **Proved** |
| E2 Multiplier $\eta=(1-2^{1-s})\zeta$ | **Proved** |
| E3 Transfer = rotation by $\pi$ | **Proved** |
| E4 Zero sets: shared critical-strip zeros | **Proved** |
| Measure-level explicit-formula equality for transfer correction | **Open** |
| Numerics §5 | **Not done** |

**Next actions (Phase 2a)**
- [ ] Add `eta_kernel` to `prime-zeros.py`; verify E3 ($K^\eta_r+K^\zeta_r(\cdot+\pi)\approx0$),
  extra zeros, and transfer correction Dirichlet coefficients. Fill in §5 table.
- [ ] Prove (or give a precise reference for) the measure-level equality: the
  eta correction to the explicit formula carries extra mass at $\{k\log 2\}$
  with coefficients $1/k$.

#### 2b. Spectral triple / RH framework ([spectral-triple.md](../project/spectral-triple.md))

| Result | Status |
|---|---|
| Zero kernel positive definite (unconditional) | **Proved** |
| Transfer kernel $K^\varepsilon_{\mathrm{RH}}$ defined and trace-class | **Proved** |
| Theorem 6.1: RH ↔ positivity of $T_\varepsilon$ | **Heuristic** (proof sketch only) |
| Quaternionic positivity Theorem 7.1 | **Heuristic** |
| Numerical test (30 zeros, primes ≤ 100) | **Done** (in HTML) |
| Effective bound: verification up to $\omega=T$ → no zeros below $T$ | **Open** |
| Mollifier → closed-form kernel | **Open** |
| $T_\varepsilon$ spectrum as $\varepsilon\to0$ | **Open** |

**Next actions (Phase 2b)**
- [ ] Upgrade proof sketch of Theorem 6.1 to a full proof (or a precise citation
  to Weil/Barner + a statement of what remains to verify).
- [ ] Add the effective-bound question to the open-questions list and survey the
  literature (Bombieri–Lagarias zero-free regions via explicit formulas).

#### 2c. General Dirichlet series and $L$-functions

Status: **not started**.

**Next actions (Phase 2c)**
- [ ] Write `project/dirichlet-series.md`: kernel ↔ functional-equation
  dictionary for $L(s,\chi)$; state which parts of the spectral-triple recipe
  go through unconditionally for Dirichlet $L$-functions.

---

### Phase 3 — Dynamical / hard cases

#### 3a. Zeros ↔ primes explicit formula (at achievable rigour)

Current state: treated heuristically in spectral-triple.md. The precise
conditions on the test function $f$ and the truncation error are not analysed.

**Next actions**
- [ ] State Weil's explicit formula with full hypotheses (Barner 1981 version);
  identify exactly which step in the Theorem 6.1 proof sketch is conditional on
  RH and which is unconditional.

#### 3b. Collatz orbit statistics

Status: **not started**. Listed in the README catalogue; no note exists.

**Next actions**
- [ ] Assess feasibility: define the sequence (stopping-time distribution or
  orbit-length counts), check whether geometric damping suffices for convergence,
  and decide whether a spectral note is tractable. Write a brief feasibility
  memo before committing a full note.

---

### Phase 4 — Generalisation

Status: **not started** (awaits completion of Phases 1–2).

Target deliverable: `project/generalised-algorithm.md` containing:

- Abstract inputs: sequence class, growth rate, symmetry.
- Abstract outputs: operator, spectrum, transfer operator, explicit formula,
  positivity criterion.
- Honest hypotheses table: which outputs are unconditional vs. conditional.
- The spectral-triple recipe as the special case.

**Prerequisites before starting Phase 4**
- Fibonacci OU numerics done (§§1b,1c above).
- η↔ζ measure-level equality settled (§2a).
- Functor $L^2(\gamma)\to L^2(\mathbb{T})$ formalised (§1c).

---

### Phase 5 — Helix lift and quaternionic time

#### ([helix-quaternion-proposal.md](../project/helix-quaternion-proposal.md))

| Result | Status |
|---|---|
| H1 Helix = universal cover of $\mathbb{T}$ | **Proved** |
| H2 Sign = half-turn; negativity = winding | **Proved** |
| H3 η phase winds past $2\pi$ | **Proved** |
| H4 $j$-time: $D_t=-j\partial_t$ self-adjoint; cone restoration | **Conjecture** |
| Sign-aware helix lift in `prime-zeros.py` | **Done** |
| Quaternionic Hilbert module definition | **Open** |
| S-spectrum / slice-regular self-adjointness of $D_t$ | **Open** |
| Cone-restoration claim (H4 part 3) | **Open** |

**Next actions (Phase 5)**
- [ ] Define the quaternionic Hilbert module precisely (coefficient ring $\mathbb{H}$,
  right vs. left structure, S-spectrum setup); consult Colombo–Sabadini–Struppa.
- [ ] Attempt to prove H4 part (2): $D_t=-j\partial_t$ is self-adjoint on the
  module in the S-spectrum sense.
- [ ] Test H4 part (3) numerically on the η kernel (which is indefinite on the
  circle by E3): verify that the helix lift makes the cone indicator non-negative.

---

## 3. Spectral data sheet (work in progress)

One row per catalogue object. Columns: object | kernel closed form | damping | spectrum | self-adjoint domain | dual object.

| Object | Kernel closed form | Damping range | Spectrum | Dual |
|---|---|---|---|---|
| Fibonacci $F_n$ | $2\,\Re\frac{re^{i\theta}}{1-re^{i\theta}-r^2e^{2i\theta}}$ | $r<1/\varphi$ | $\{F_n r^n\}$ | Lucas (open) |
| Prime sine wave $p^{-s}$ | none (no closed form) | $\Re s>\tfrac12$ | $\{p^{-2\sigma}\}$ | — |
| OU / integers $\mathbb{N}$ | Mehler: $\frac{1}{\sqrt{1-r^2}}e^{(2rxy-r^2(x^2+y^2))/2(1-r^2)}$ | $r=e^{-t}<1$ | $\{r^n\}=\{e^{-nt}\}$ | spectral zeta $=\zeta$ |
| Zeta magnitude $n^{-1/2}$ | $2\,\Re\operatorname{Li}_{1/2}(re^{i\theta})$ | $r<1$ | $\{n^{-1/2}r^n\}$ | zeros via Weil |
| Dirichlet eta (alternating) | $-K^\zeta_r(\theta+\pi)$ | $r<1$ | alternating signs | $\zeta$ via rotation by $\pi$ |
| Riemann zeros $\gamma_n$ | $2\sum\gamma_n r^n\cos n\theta$ | $r<1$ | $\{\gamma_n r^n\}$ | prime powers via Weil |
| Prime powers $\Lambda(n)/\sqrt{n}$ | (no closed form) | Gaussian | von Mangoldt weights | zeros via Weil |
| Collatz | (not assessed) | — | — | — |
| General Dirichlet $L(s,\chi)$ | (not assessed) | — | — | — |

---

## 4. Numerical verification checklist

| Note | Check | Status |
|---|---|---|
| prime-sine-wave §6 | $\|Ψ_2\|^2=P(4)$ to 10 digits | **Done** |
| fibonacci-kernel §6 | $K_r(0)$, PD grid, eigenvalues, $\|K_r\|_2^2$ | **Not done** |
| ou-process §7 | Mehler, trace, heat, Mellin $\Gamma\zeta$ | **Not done** |
| eta-zeta-transfer §5 | rotation identity, extra zeros, transfer correction | **Not done** |
| spectral-triple §8 | extend to 100+ zeros, vary $\varepsilon$, port to Python | **Partial** (HTML only) |
| helix §6 | cone indicator on η kernel | **Not done** |

---

## 5. Guardrails

- Every result must be tagged: **proven**, **conditional** (state the hypothesis),
  or **heuristic/exploratory**.
- A clean appearance of $\zeta$ or $\mathbb{N}$ in a spectrum is *not* a criterion
  for RH (prime-sine-wave §7).
- Numerical experiments are evidence, not proof; report minimum values and
  truncation errors explicitly.
- Do not start Phase 4 until Phase 1 numerics are done; do not start Phase 5
  proofs until the quaternionic module is properly defined.

---

## 6. Dependency graph

```
prime-sine-wave  ──┐
fibonacci-kernel  ─┤
ou-process        ─┼──►  Phase 4 (generalised algorithm)
eta-zeta-transfer ─┤                  │
spectral-triple   ─┘                  ▼
                              Phase 5 (helix / quaternion)
```

Phase 3 (Collatz, full explicit formula) can proceed independently of Phase 4/5.
