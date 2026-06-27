# Spectral Number Theory — Kernels, Transfer Operators & Explicit Formulas

A research workspace exploring a single recurring idea: **turn an arithmetic
sequence into a self‑adjoint operator, study its spectrum, and connect different
sequences through transfer operators governed by explicit formulas.**

The recurring objects are infinite series drawn from number theory and
combinatorics — Fibonacci, Collatz, integer and prime sums, the primes
themselves, the Riemann zeta function, the Dirichlet eta function, general
Dirichlet series, and $L$‑functions — together with the **Ornstein–Uhlenbeck
process**, the continuous‑time diffusion whose Markov semigroup *is* the damping
step and whose generator's spectrum is the integers themselves (its spectral
zeta function is $\zeta$). The long‑term goal is a **generalised
algorithm** that takes any such sequence and mechanically produces a positive
definite kernel, a spectral measure, and (where one exists) an explicit formula
linking it to a "dual" sequence. The general recipe in
[victor/spectral-triple.html](victor/spectral-triple.html) is the prototype
special case.

---

## Layout

```
maths/
├── victor/                         # Python experiments + interactive manuscripts
│   ├── prime-zeros.py              # Z/P/G channels, helix lift, quaternion cone
│   ├── spectral-triple.html        # interactive manuscript (KaTeX + Plotly, self-contained)
│   ├── series-spectrum-circle.html # additional interactive visualisation
│   └── requirements.txt            # numpy, matplotlib
│
├── project/                        # one Markdown note per catalogue object
│   ├── prime-sine-wave.md          # Phase 1a — proven (T1–T4)
│   ├── fibonacci-kernel.md         # Phase 1b — proven (F1–F4)
│   ├── ou-process.md               # Phase 1c — proven (O1–O5)
│   ├── eta-zeta-transfer.md        # Phase 2a — proven (E1–E4)
│   ├── spectral-triple.md          # Phase 2b — heuristic
│   └── helix-quaternion-proposal.md # Phase 5 — exploratory/conjectural
│
├── research/                       # structured research notes, one folder per phase
│   ├── index.md                    # phase index with gate conditions and status
│   ├── todo.md                     # actionable task list
│   ├── deliverables/
│   │   └── spectral-data-sheet.md  # one row per catalogue object
│   ├── phase-0-foundations/        # toolkit and recipe consolidation
│   ├── phase-1-rigorous-cases/     # Fibonacci, OU, prime sine wave
│   ├── phase-2-dirichlet-family/   # η, ζ, Dirichlet L-functions
│   ├── phase-3-dynamical/          # Weil explicit formula, Collatz
│   ├── phase-4-generalisation/     # generalised algorithm (blocked on Phase 1)
│   └── phase-5-helix-quaternion/   # helix lift, quaternionic module
│
├── plan/
│   └── project.md                  # master task list with per-phase status tables
│
├── library/                        # reference library, 21 subject folders
│   ├── index.md
│   └── content/
│       ├── 01-foundations-logic/
│       ├── 02-algebra/
│       ├── 03-number-theory/
│       ├── ...                     # through 21-measure-theory-integration/
│       └── 20-harmonic-analysis-fourier-theory/
│
├── sympy/                          # SymPy MCP verification server
│   ├── mcp_server.py               # exposes simplify / verify / check_zero tools
│   ├── requirements.txt
│   ├── environment.yml
│   └── CLAUDE.md
│
├── .mcp.json                       # MCP server configuration (codebase-memory + sympy)
├── CLAUDE.md                       # Claude Code guidance for this repo
└── README.md
```

### MCP servers

| Server | Source | Purpose |
|---|---|---|
| `codebase-memory-mcp` | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Knowledge-graph index for code navigation |
| `sympy-verifier` | `./sympy/mcp_server.py` | Symbolic verification of mathematical claims |

---

## Repository contents

### Project notes (`project/`)

| File | What it is | Status |
|---|---|---|
| [project/prime-sine-wave.md](project/prime-sine-wave.md) | Phase 1a. Four **unconditional** theorems (T1–T4) on the prime sine wave $\Psi_s=\sum_p p^{-s}\sin(p\pi x)$ in $L^2[0,2]$: domain, energy $=P(2\sigma)$, reproducing kernel $=P(s+\overline{s'})$, boundary blow‑up at the critical line. Template for all subsequent notes. | Proven |
| [project/fibonacci-kernel.md](project/fibonacci-kernel.md) | Phase 1b. The Fibonacci kernel via the recipe: rational closed form, spectrum, mass — all unconditional. Template proof pattern for linear recurrences. | Proven |
| [project/ou-process.md](project/ou-process.md) | Phase 1c. The Ornstein–Uhlenbeck process as the **engine behind damping**: generator $L=\partial_x^2-x\partial_x$ self‑adjoint on $L^2(\gamma)$, semigroup $=$ Mehler kernel $=$ geometric damping $r^n$, heat trace whose Mellin transform is $\Gamma(s)\zeta(s)$. | Proven |
| [project/eta-zeta-transfer.md](project/eta-zeta-transfer.md) | Phase 2a. The η↔ζ transfer operator: the multiplier $1-2^{1-s}$ as an alternating‑sign twist / rotation by $\pi$; shared critical‑strip zeros. | Proven (RH‑level claims flagged) |
| [project/spectral-triple.md](project/spectral-triple.md) | Phase 2b. Markdown companion to `spectral-triple.html`. Constructs the spectral transfer operator $T_\varepsilon$ from zeta zeros, primes, and Dirichlet terms; positivity of $T_\varepsilon$ is equivalent to RH. Quaternionic reformulation included. | Heuristic |
| [project/helix-quaternion-proposal.md](project/helix-quaternion-proposal.md) | Phase 5. When positivity fails, lift the circle to a helix (sign = half‑turn, negativity = winding past $2\pi$) and make $j$ the self‑adjoint generator of time. Eta micro‑example. | Exploratory / conjectural |

### Numerical code and interactive visualisations (`victor/`)

| File | What it is | Status |
|---|---|---|
| [victor/prime-zeros.py](victor/prime-zeros.py) | NumPy experiment: separates the explicit‑formula channels $Z,P,G$, builds the signal $R=Z-P+G$, the **sign‑aware helix** lift, the spectral quaternion $Z-iP+jG$ and its cone indicator $Z^2-(P^2+G^2)$. | Working code |
| [victor/spectral-triple.html](victor/spectral-triple.html) | Interactive manuscript: *A Spectral Framework for the Riemann Hypothesis*. General recipe (damping → symmetrisation → kernel), worked kernels (Fibonacci, zeta "trilogy", zeros), Weil‑criterion positivity, quaternionic reformulation, live numerical tests. KaTeX + Plotly, self‑contained. | Exploratory / heuristic |
| [victor/series-spectrum-circle.html](victor/series-spectrum-circle.html) | Interactive visualisation: zeta Dirichlet series terms mapped onto the circle as a spectrum. KaTeX + Plotly, self‑contained. | Exploratory |
| [victor/requirements.txt](victor/requirements.txt) | Python dependencies (`numpy`, `matplotlib`). | — |

### Research notes (`research/`)

Structured working notes, one subfolder per phase. Each phase folder contains an `index.md` plus per-topic notes.

| Folder | Contents |
|---|---|
| [research/phase-0-foundations/](research/phase-0-foundations/) | Toolkit design; Python functions to add to `prime-zeros.py` |
| [research/phase-1-rigorous-cases/](research/phase-1-rigorous-cases/) | Working notes for prime sine wave, Fibonacci kernel, OU process |
| [research/phase-2-dirichlet-family/](research/phase-2-dirichlet-family/) | η↔ζ transfer, spectral triple, Dirichlet L‑functions |
| [research/phase-3-dynamical/](research/phase-3-dynamical/) | Weil/Barner explicit formula, Collatz feasibility |
| [research/phase-4-generalisation/](research/phase-4-generalisation/) | Generalised algorithm (blocked until Phase 1 numerics done) |
| [research/phase-5-helix-quaternion/](research/phase-5-helix-quaternion/) | Helix lift (H1–H3 proved, H4 conjectural), quaternionic Hilbert module |
| [research/deliverables/spectral-data-sheet.md](research/deliverables/spectral-data-sheet.md) | Spectral data sheet: one row per catalogue object |
| [research/todo.md](research/todo.md) | Actionable task list derived from `plan/project.md` |

### Plan and tooling

| File | What it is |
|---|---|
| [plan/project.md](plan/project.md) | Master task list with per-phase status tables; maps to the 16-item GitHub project board |
| [sympy/mcp_server.py](sympy/mcp_server.py) | SymPy MCP verification server — exposes `simplify`, `verify_equation`, `check_zero`, `evaluate_at` tools for symbolic checking of mathematical claims |

> **Tone of the project.** These notes deliberately separate what is *proven*
> from what is *exploratory*. The prime‑sine‑wave note proves theorems and
> explicitly disclaims any bearing on RH; the spectral‑triple manuscript is a
> heuristic framework whose central positivity claim is *equivalent to* RH and
> therefore as hard as RH. New work should keep that distinction sharp.

---

## The setting: a self‑adjoint operator on the unit circle

Everything in the project lives in one place — a Hilbert space of functions on the
unit circle — and turns on one construction: convolution by a kernel is a
self‑adjoint operator whose spectrum *is* the arithmetic sequence.

**The unit circle in the complex plane.** Let
$$\mathbb T=\{z\in\mathbb C:|z|=1\}=\{e^{i\theta}:\theta\in[-\pi,\pi)\}.$$
Points of $\mathbb T$ are complex numbers of modulus one, parametrised by the
angle $\theta$. Damping is what pulls a divergent sequence onto this circle: the
generating variable $z=re^{i\theta}$ with $0<r<1$ sits on a circle of radius $r$
*inside* the unit disc, where power series converge, and the kernel is the radial
limit/section of that generating function (this is exactly why the Fibonacci
kernel inherits the rational closed form $z/(1-z-z^2)$). The circle's rotational
symmetry $\theta\mapsto\theta+\alpha$ is what makes the resulting operators
shift‑invariant — and the rotation by $\pi$ is itself the η↔ζ transfer operator.

**The role of the Hilbert space.** The arena is
$$H=L^2(\mathbb T),\qquad \langle f,g\rangle=\frac1{2\pi}\int_{-\pi}^{\pi}f(\theta)\overline{g(\theta)}\,d\theta.$$
The exponentials $e_n(\theta)=e^{in\theta}$ ($n\in\mathbb Z$) form a **complete
orthonormal basis** of $H$. By Riesz–Fischer, square‑summable coefficient
sequences $(\lambda_n)\in\ell^2$ correspond exactly to functions in $H$ — so an
arithmetic sequence (after damping) *is* a vector in $H$, and its Fourier
coefficients *are* its coordinates. The Hilbert space is what gives the
construction its rigour: orthonormality turns sums over a sequence into geometry
(energies are $\ell^2$ norms, cross‑terms are inner products), as the proven
prime‑sine‑wave theorems show in the companion space $L^2[0,2]$.

**The self‑adjoint operator.** A real, even, summable kernel
$K(\theta)=\sum_{n\in\mathbb Z}\lambda_n e^{in\theta}$ defines the convolution
operator
$$(T_Kf)(\theta)=(K*f)(\theta)=\frac1{2\pi}\int_{-\pi}^{\pi}K(\theta-\phi)f(\phi)\,d\phi.$$
The basis functions diagonalise it: $T_Ke_n=\lambda_n e_n$, so the **eigenvalues
are the Fourier coefficients** $\lambda_n$. Because $K$ is real and even,
$\lambda_n=\lambda_{-n}\in\mathbb R$ and $T_K=T_K^{*}$ is **self‑adjoint**; it is
bounded, compact, or trace class according to the decay of $(\lambda_n)$, and by
**Bochner's theorem** it is positive semidefinite iff every $\lambda_n\ge0$.
Hence:

$$\textbf{the (damped, symmetrised) arithmetic sequence } \{\lambda_n\} \textbf{ is precisely the spectrum of } T_K.$$

This is the exact sense of "turn a sequence into a self‑adjoint operator": the
recipe below is the constructive route from a sequence to its $K$ and $T_K$.

---

## The core idea: the general recipe

Given a nonnegative sequence $(a_n)_{n\ge0}$, the recipe in
[project/spectral-triple.md](project/spectral-triple.md) §3 builds a
shift‑invariant positive definite kernel on the circle $\mathbb T=[-\pi,\pi)$:

1. **Damping** — pick weights $w_n$ with $\sum_n a_n w_n<\infty$ (e.g. geometric
   $w_n=r^n$, or Gaussian $w_n=e^{-\sigma^2 n^2}$).
2. **Symmetrisation** — set $\lambda_0=a_0w_0$ and $\lambda_n=\lambda_{-n}=a_nw_n$.
3. **Kernel** — $K(\theta)=\sum_{n\in\mathbb Z}\lambda_n e^{in\theta}=\lambda_0+2\sum_{n\ge1}\lambda_n\cos(n\theta)$.

By Bochner's theorem on the circle, $K$ is positive definite iff its Fourier
coefficients $\lambda_n$ are nonnegative — which the recipe guarantees by
construction. The sequence is now the **spectrum** of a self‑adjoint convolution
operator. Different sequences (Fibonacci ordinates, zeta zeros $\gamma_n$, prime
powers via von Mangoldt $\Lambda(n)/\sqrt n$) plug into the same machine; the
**transfer operator** is convolution with the *difference* of two such kernels,
and Weil's explicit formula is the identity that makes the zero‑kernel and
prime‑kernel comparable.

The research project below is about turning this prototype into a general,
defensible algorithm.

---

## Research project plan

### Objective

Develop and validate a **generalised algorithm**

```
sequence  ──►  self-adjoint operator  ──►  spectrum  ──►  transfer operator  ──►  explicit formula
```

that applies uniformly across the families below, with the spectral‑triple
recipe recovered as the special case for the zeta zeros / primes pair.

### Object catalogue (the sequences under study)

Studied "including but not limited to":

- **Combinatorial / dynamical:** Fibonacci $F_n$ (and Lucas / linear
  recurrences), Collatz orbit statistics and stopping times.
- **Elementary arithmetic sums:** integer sums $\sum n^{-s}$ ($=\zeta$), partial
  sums, divisor and power sums.
- **Prime objects:** prime sums $\sum_p p^{-s}$ (prime zeta $P$), the primes as a
  point process, von Mangoldt $\Lambda(n)$ prime‑power weights.
- **$L$‑theory:** Riemann zeta $\zeta$, Dirichlet eta $\eta(s)=(1-2^{1-s})\zeta(s)$,
  general Dirichlet series $\sum a_n n^{-s}$, Dirichlet $L$‑functions $L(s,\chi)$,
  and (stretch) higher $L$‑functions.
- **Stochastic / continuous‑time:** the Ornstein–Uhlenbeck process — generator
  with spectrum $-\mathbb N$ and Hermite eigenfunctions, Mehler‑kernel semigroup
  (geometric damping $r^n$), and the number operator $a^{\dagger}a$ it equals;
  its spectral zeta function is $\zeta$ itself.

For each object the deliverable is a filled‑in row of a common **spectral data
sheet**: convergence/damping regime, kernel closed form, spectral measure,
self‑adjointness domain, and dual object under the transfer operator.

### Methodology — four pillars

1. **Self‑adjoint realisation.** For each sequence, construct an explicit
   Hilbert space and operator (multiplication, convolution, or composition /
   transfer operator) that is symmetric, identify its domain, and decide
   essential self‑adjointness (deficiency indices). The
   [prime‑sine‑wave note](project/prime-sine-wave.md) is the template: a concrete
   $L^2$ space, an orthonormal system, and unconditional convergence/energy
   theorems.

2. **Spectral analysis.** Compute the spectral measure / spectrum of each
   operator. Distinguish discrete vs. continuous spectrum, locate natural
   boundaries (cf. the critical line emerging from the singularity of $P$ at
   $z=1$), and relate spectral data to the analytic continuation and functional
   equation of the associated Dirichlet series.

3. **Transfer operators between objects.** Formalise maps that send one
   sequence's kernel to another's — e.g. zeros ↔ primes via the explicit
   formula, $\zeta\leftrightarrow\eta$ via $1-2^{1-s}$, Fibonacci via its
   generating function $z/(1-z-z^2)$. Where the dynamics warrant it, use genuine
   Ruelle–Mayer transfer operators (e.g. Gauss map / continued fractions) and
   their traces.

4. **Explicit formulas.** Derive the analogue of the Weil/Guinand explicit
   formula for each transfer operator — the trace identity that equates a sum
   over the "spectral" side to a sum over the "arithmetic" side, with the
   archimedean (Gamma) correction term. The generalised algorithm's output is
   precisely such a formula plus its positivity/self‑adjointness conditions.

### Phased plan

**Phase 0 — Foundations & tooling.** Consolidate the recipe and the proven
prime‑sine‑wave results; build a small Python/`numpy` (later `mpmath`/`sympy`)
toolkit that, given a sequence and a damping rule, emits the spectrum, the
kernel, and the cumulative spectral measure. Extends
[victor/prime-zeros.py](victor/prime-zeros.py).

**Phase 1 — Easy, fully rigorous cases.** Fibonacci/linear‑recurrence kernels
(closed forms via generating functions) and the prime sine wave. Goal: a
template with complete proofs and numerics that 10‑digit‑match (as in
prime‑sine‑wave §6). The **Ornstein–Uhlenbeck process** supplies the
continuous‑time Markov semigroup behind the damping step, with spectrum
$\mathbb N$ (Hermite/Mehler) and spectral zeta $=\zeta$. *Started:*
[project/fibonacci-kernel.md](project/fibonacci-kernel.md),
[project/ou-process.md](project/ou-process.md).

**Phase 2 — Dirichlet‑series family.** $\zeta$, $\eta$, general Dirichlet
series, Dirichlet $L$‑functions. Establish the kernel ↔ functional‑equation
dictionary and the $\zeta\leftrightarrow\eta$ transfer operator as a clean,
provable instance of "transfer between objects". *Started:*
[project/eta-zeta-transfer.md](project/eta-zeta-transfer.md).

**Phase 3 — Dynamical / hard cases.** Collatz (statistics of orbits as a
transfer‑operator spectrum) and the zeros↔primes explicit formula at the level
of rigor it admits. Clearly flag what is conditional on RH.

**Phase 4 — Generalisation.** Abstract the common structure into the
generalised algorithm: inputs (sequence, growth class, symmetry), outputs
(operator, spectrum, transfer operator, explicit formula, positivity
criterion). State precisely the hypotheses under which each output is
unconditional. Recover the spectral‑triple recipe as the special case.

**Phase 5 — Beyond positivity (exploratory).** When a kernel is *indefinite*
(the η kernel, the zeros↔primes transfer kernel), the circle picture breaks. Lift
the unit circle to a **helix** so that negativity becomes rotation past $2\pi$
along an added time axis, and identify that axis with the quaternionic $j$
direction. See the **Research proposal** section below and the dedicated note
[project/helix-quaternion-proposal.md](project/helix-quaternion-proposal.md);
first step implemented in [victor/prime-zeros.py](victor/prime-zeros.py).

### Deliverables

- A **closed‑form kernel definition** for each object that admits one: the
  explicit expression for $K(\theta)=\sum_n\lambda_n e^{in\theta}$ obtained by
  summing the damped, symmetrised series in closed form — a rational function for
  linear recurrences (e.g. Fibonacci, $K_r(\theta)=2\,\Re\frac{re^{i\theta}}{1-re^{i\theta}-r^2e^{2i\theta}}$),
  a polylogarithm for the zeta magnitude/angle kernels, etc. — stated together
  with its **domain of validity** (the damping range where the sum converges and
  $T_K$ is self‑adjoint). Where no closed form exists, record the convergent
  series definition and its decay rate instead.
- A **spectral data sheet** (one row per object in the catalogue), whose columns
  include the closed‑form kernel above, the damping regime, the spectrum
  $\{\lambda_n\}$, the self‑adjointness domain, and the dual object under the
  transfer operator.
- Per‑object notes in the proven style of
  [project/prime-sine-wave.md](project/prime-sine-wave.md), each with an explicit
  *Scope and honest limits* section.
- A reusable computational toolkit (sequence → kernel → spectrum → cumulative
  measure → numerical positivity test).
- A write‑up of the **generalised algorithm** with theorems stated at their
  honest level of rigor.

### Guardrails (scope discipline)

- Mark every result as **proven**, **conditional** (state the hypothesis), or
  **heuristic/exploratory**.
- Never let a coincidence of abscissae masquerade as a criterion (see
  prime‑sine‑wave §7): a framework is only "RH‑equivalent" if it is provably
  tied to the zeros, not merely to the prime zeta singularity.
- Numerical experiments are evidence, not proof; report them as such.

---

## Research proposal: the helix lift and quaternionic time

> **Status: exploratory / conjectural.** This section is a research *program*, not
> a set of theorems. Quaternionic non‑commutativity makes "self‑adjoint" and
> "spectrum" genuinely subtle, and the η reading below is illustrative. Nothing
> here bears on RH; it only proposes *where to store* the obstruction that
> positivity runs into.

### The problem positivity leaves open

Bochner forces the spectrum $\{\lambda_n\}$ of a circle kernel to be
**nonnegative** for $T_K$ to be positive definite. Several catalogue objects
violate this by construction — the η kernel's alternating signs
([eta-zeta-transfer.md](project/eta-zeta-transfer.md) §3), and the zeros↔primes
transfer kernel whose positivity *is* RH. The usual response is to accept a signed
spectrum and lose the geometry. This proposal instead **re‑encodes the sign as
geometry on a larger space.**

### The helix as the universal cover of the circle

The circle is $\mathbb T=\mathbb R/2\pi\mathbb Z$; its universal cover is the line
$\mathbb R$ via $p:t\mapsto e^{it}$, realised geometrically as the **helix**
$$\mathcal H=\{(\cos t,\ \sin t,\ t):t\in\mathbb R\}\subset\mathbb C\times\mathbb R_t,$$
where the third coordinate $t$ is the *unwrapped* phase (the winding) and is
identified with **time**. The circle discards the integer winding number; the
helix keeps it.

A negative weight is, on the circle, indistinguishable from a positive weight
rotated by half a turn: $-a=a\,e^{i\pi}$. On the helix that half‑turn is genuine
displacement in $t$, and as winding accumulates it crosses $2\pi,4\pi,\dots$ — so
"**negative numbers = rotation beyond $2\pi$**" is literally true on the cover.
Sign becomes the parity of the winding number $\lfloor \Theta/\pi\rfloor$; the
indefinite circle kernel becomes a single‑valued curve climbing the helix.
Sweeping a one‑parameter family (mollifier width $\varepsilon$, or the cumulative
spectral measure $\int_0^\omega$) stacks helices into a sheet — the
**multi‑dimensional framework over time.**

### Quaternionic time: $j$ as the self‑adjoint generator

[spectral-triple.html](victor/spectral-triple.html) §9 already embeds the three
real channels as a quaternion (there written $Z+iP+jG$); here we take
$\mathbf K=Z-iP+jG$ (zeros, primes, Gamma) so the $i$‑channel carries $-P$ and
$\mathbf K$ mirrors the signal $R=Z-P+G$ exactly — the positivity cone
$z^2-(p^2+g^2)\ge0$ is unchanged, depending only on $P^2$. The proposal promotes
the helix axis to the quaternionic $j$‑axis:

- the lift is the quaternionic exponential $t\mapsto e^{jt}=\cos t+j\sin t$ in the
  $(1,j)$‑plane of $\mathbb H$, so winding past $2\pi$ is real motion on the
  $j$‑circle, *distinguishable* from the original spectral phase on the
  $i$‑circle;
- the generator of time‑translation along the helix is
  $D_t=-\,j\,\partial_t$, the quaternionic analogue of the self‑adjoint momentum
  $-i\partial_x$. The claim "**$j$ is the self‑adjoint operator kernel of time**"
  is the statement that the convolution kernel implementing winding‑shift is built
  from $j$ and is self‑adjoint on the appropriate quaternionic Hilbert module —
  so the lifted operator gains a positive *time/$j$* component (the $G$ channel)
  that can restore the cone $z^2-(p^2+g^2)\ge0$ even when $T_K$ was indefinite on
  the circle.

The rigorous toolkit to engage here is quaternionic spectral theory (the
**S‑spectrum** and slice‑regular functions), where a genuine spectral theorem for
self‑adjoint quaternionic operators exists.

### Worked micro‑example: the Dirichlet eta function

On the critical line $s=\tfrac12+ib$, the eta term is
$(-1)^{n-1}n^{-1/2}e^{-ib\log n}$ with cumulative phase
$$\Theta_n=\pi(n-1)-b\log n.$$
The half‑turn $\pi$ per step makes $\Theta_n$ wind without bound, crossing
$2\pi,4\pi,\dots$ — the terms have **rotated beyond $2\pi$**. The *negative* terms
are the even $n$ (sign $(-1)^{n-1}=-1$): their accumulated half‑turns land on
**odd** multiples of $\pi$. Reading this on the helix:

- where $\Theta_n\in 2\pi\mathbb Z$ the term is **real and positive** (a full
  number of turns);
- where $\Theta_n\in\pi+2\pi\mathbb Z$ it is **real and negative** — the "real
  valued (imaginary‑part) terms" that have wound an odd half‑turn past a multiple
  of $2\pi$;
- the $-b\log n$ drift offsets generic terms off the real axis, giving
  **complex‑valued offsets around the $2\pi$ multiples.**

So the η kernel — *indefinite* on the circle — becomes single‑valued once the
winding is restored on the helix, with the $j$‑axis carrying exactly the parity
the circle folded away.

### First steps (concrete)

1. **Extend [victor/prime-zeros.py](victor/prime-zeros.py)**, which already plots a
   helix ($x=R\cos\omega,\ y=R\sin\omega,\ z=\omega$): make the lift *sign‑aware*
   so negative $R$ becomes a half‑turn in $t$ rather than a sign; add the
   quaternion‑valued curve $q(\omega)=Z-iP+jG$ with time along $j$; plot the
   indefinite η kernel and check single‑valuedness.
2. **Define the quaternionic Hilbert module** precisely and prove (or refute)
   that $D_t=-j\partial_t$ is self‑adjoint there in the S‑spectrum sense.
3. **State and test the conjecture:** an indefinite circle kernel $T_K$ lifts to a
   helix kernel that is positive in the quaternionic cone iff [explicit winding
   condition]; recover Bochner (zero winding) as the special case.

### Honest limits

- Conjectural throughout; the eta reading is heuristic illustration, not a proof.
- Quaternion non‑commutativity means "eigenvalue" and "self‑adjoint" must be taken
  in the S‑spectrum / slice‑regular sense — getting this right is part of the work.
- **No RH claim.** Lifting to the helix relocates the positivity obstruction into
  the winding/time channel; it does not remove it. The zeros↔primes case stays
  exactly as hard as RH.

---

## Getting started

```bash
# Python experiments
cd victor
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python prime-zeros.py          # prints R-range / peak; shows 3-D helix if matplotlib is present
```

```bash
# Interactive manuscript — just open it in a browser (uses KaTeX + Plotly via CDN)
open victor/spectral-triple.html
```

The Markdown notes ([project/prime-sine-wave.md](project/prime-sine-wave.md))
render with standard LaTeX math support (e.g. on GitHub or any KaTeX/MathJax
previewer).

---

## References

- A. Weil, *Sur les formules explicites de la théorie des nombres*, 1952.
- K. Barner, *On A. Weil's explicit formula*, 1981.
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, 1999.
- A. M. Odlyzko, *The first $10^{13}$ zeros of the Riemann zeta function*, 1987.
- Nyman–Beurling–Báez‑Duarte criterion (an $L^2$ RH‑equivalent framework), as noted in [project/prime-sine-wave.md](project/prime-sine-wave.md) §7.
- Riesz–Fischer theorem; Mertens' theorems; the prime zeta function $P(z)=\sum_{k\ge1}\tfrac{\mu(k)}{k}\log\zeta(kz)$.
- F. Colombo, I. Sabadini, D. C. Struppa, *Noncommutative Functional Calculus* / the S‑spectrum and slice‑regular functions — the quaternionic spectral theory underpinning the Phase‑5 helix proposal.
