# The PSC2 program: a four-level operator-theoretic study of the Riemann explicit formula

*Manuscript. Date: 7 Jul 2026. Status of the Riemann Hypothesis throughout this document:
**open**. This manuscript reports on project PSC2 (`victor/research/`): its charter
([PSC2-000](PSC2-000-charter.md)), conventions ([PSC2-001](PSC2-001-conventions.md)), source
compendium (S00–S06), sixteen work packages, and fourteen finding notes (F01–F14). Every claim
below carries the project's rigour tag — **proven**, **verified**, **conditional**,
**RH-equivalent**, **heuristic/exploratory**, **dead end**, **wall**, **open** — and nothing
tagged below **proven** is used to support anything tagged **proven**.*

---

## Abstract

PSC2 is a structured research program that studies the Guinand–Weil explicit formula of the
Riemann zeta function as a single object seen at four levels of resolution: a **trace** level
(L1), where the prime side of the explicit formula is realised as the trace of a constructed
self-adjoint package and verified adelically to $10^{-36}$; a **character** level (L2), where
the same data is the flow character $\chi_W(z) = -\frac{\zeta'}{\zeta}(\frac12 - iz)$ and a
circularity theorem closes the level; a **determinant** level (L3), where finite sieve stages
carry secular polynomials, a proven weighted Ihara–Bass identity, and a Hurwitz dictionary
that prices the remaining distance to RH exactly; and an **eigenvalue** level (L4), where a
sieve-Galerkin compression $H^G_n = P_n D P_n$ of the dilation generator is pushed through a
pre-registered gauntlet of falsifiable gates. The program's method is as much the subject of
this manuscript as its mathematics: every experiment is pre-registered with two-sided
criteria, every harness carries positive controls, must-fail negative controls, and a decoy
model, and every negative result is filed as a finding with the same care as a positive one.
The headline results to date: four new theorems (the pairing lemma; the weighted Ihara–Bass
identity in multigraph form; a uniform normalised-gap theorem with explicit constant; an
edge-purity "anti-Siegel" theorem for all stages and all weights) and one exact structural
law (the sieve-step gluing law); three informative kills executed by their own pre-registered
falsifiers (the primary candidate's first instantiation at the density gate, with a proven
no-go lemma covering its whole design class; the "exactly 4 detached eigenvalues" census; the
Asano/Lee–Yang gluing route, closed entirely); one salvage (the rewindow of the
density gate, which repairs the killed component by redesigning the phase-space window along
the Berry–Keating wedge and reopens the E-track); and the arbitration of that salvage: under
the full evaluation harness — trace, displacement, product, moment, and genealogy gates with
a two-sided control battery — the rewindowed family passed every shape gate and **closed as
counting law only** at the pre-registered decision point (its sieve inventory carries no
measurable arithmetic beyond its derived counting law on the evaluation window), moving the
E-track to its chartered successor candidate, the Connes–Moscovici prolate pencil (WP15).
None of this decides RH, and the program's
own ledger proves *why* it cannot yet: every route terminates at one of six proven
RH-equivalent walls, all of which are the same wall — positivity — in different coordinates.
The value of the program is the graded ladder of unconditional results below that wall, the
complete map of dead ends, and a harness discipline that makes false progress mechanically
difficult to report.

---

## 1. The problem, and the program's stance on it

The Riemann Hypothesis asserts that every nontrivial zero $\rho = \beta + i\gamma$ of
$\zeta(s)$ has $\beta = \tfrac12$. The Hilbert–Pólya heuristic proposes to prove it by
exhibiting a self-adjoint operator whose spectrum is $\{\gamma_\rho\}$: self-adjointness
forces reality of the spectrum, and reality of the $\gamma$-coordinates *is* RH once the
normalisation carries $\mathrm{Re}\,s = \tfrac12$.

PSC2's stance, fixed in its charter and proven rather than assumed where possible, is:

1. **The program is a coordinate change on Hilbert–Pólya, not a detour around it.** The four
   levels (trace, character, determinant, eigenvalue) are bridged by proven identities, and
   the obstruction appears at the same height in every coordinate system: Weil positivity
   $\equiv$ reality of the $\chi_W$-poles $\equiv$ stage-determinant zero confinement
   (C2 given C1) $\equiv$ spectral completeness with positivity — all proven equivalent to
   RH ([S06 §4](sources/PSC2-S06-constraints-and-walls.md)).
2. **RH-equivalent restatements are walls, not steps.** They are priced, consulted as
   calibrators, and never scheduled as work items. The actionable residue is the graded
   ladder of unconditional statements strictly below the wall.
3. **Negative knowledge is curated as carefully as positive knowledge.** Twelve closed routes
   (the X-ledger), four no-go theorems (N1–N4), and five classical-theory corrections
   (M1–M5) are binding on every proposal; a proposal violating one is dead on arrival.
4. **An unconditional proof of RH is a permitted outcome, at a bar that does not move**
   ([PSC2-001 §4](PSC2-001-conventions.md)): every link proven, the chain terminating in the
   zeros themselves, surviving adversarial and independent verification. Nothing in this
   manuscript is presented as approaching that bar.

The program inherits, from its parent repository, a concrete cautionary artifact: a discarded
proof series (`flawed/barry-keating-hp-*`) that claimed RH and was refuted at three
independent, provable points, one of which — rank-unfolding against the target's own counting
function — is now the first rule of the evidence hygiene protocol (I0). The methodology of
§2 exists because that failure mode is known to be reachable.

## 2. Methodology: pre-registration, controls, and the rigour economy

Every experiment in PSC2 runs under rule I0 ([S06 §5](sources/PSC2-S06-constraints-and-walls.md)):

- **Pre-registered, two-sided criteria.** Each work package states, before any run, what
  outcome falsifies its hypothesis and what happens next in either branch. The finding note
  copies the criteria verbatim and applies them mechanically. Five of the fourteen findings
  to date landed in a falsifier or pre-registered closure branch — the branches are real,
  not decorative.
- **No target consumption.** No unfolding, fitting, calibration, or normalisation against
  $N(T)$ or the zero list anywhere in construction or metrics; the $\gamma$-list may appear
  only in final-evaluation metrics (gate E4b) and in one regression line per run.
- **Harness validity is itself tested.** Every gate runs a positive control that must pass
  (proving the metric passable), negative controls that must fail (legacy operator, graph
  one-mode), and the sine decoy — the exact model $\sin(\pi t)/\pi t$ with spectrum
  $\mathbb Z_{>0}$, which must pass every internal-consistency step and fail every
  arithmetic test. A harness on which the decoy scores as "arithmetic" is invalid.
- **Regression anchors.** Every run first reproduces the in-repo verified numbers
  ([N00](numerics/PSC2-N00-verification-targets.md)); a mismatch is a finding, not a nit.
- **The model pair is the control, not the evidence.** The analogy
  $\sin(\pi t)/\pi t = \prod(1 - t^2/n^2) \leftrightarrow \Xi(t) = \Xi(0)\prod(1 - t^2/t_k^2)$
  ([S04](sources/PSC2-S04-model-pair.md)) supplies exact finite stages (greedy
  Egyptian-fraction reconstruction, proven, doubly-exponential rate) used to calibrate what
  "exact finite stages" look like when everything works — and to build decoys.

This is unusual discipline for pure mathematics, and it is load-bearing: the objects under
study (spectra that should match zero statistics) are precisely the kind where confirmation
bias has historically manufactured results.

## 3. Level L1 — the verified foundation (motivation, findings, significance)

**Motivation.** Before anything spectral can be attempted, the prime side of the explicit
formula must exist as a constructed, unconditional object with quantitative error control —
otherwise every later comparison is against a moving target.

**The construction** ([S00](sources/PSC2-S00-verified-foundation.md)). A dyadic
composite-generator sieve enumerates the primes exactly, block by block
($I_n = [2^n, 2^{n+1})$, $M_n = 2^{n+1}-1$), using no primality test — primes are the gaps
the composite generator misses (Lemma 1.2, **proven**). The normalised prime positions
equidistribute at rate $O_k(1/\log M_n)$ (Theorem 1.3, **proven**), which has a design
consequence used everywhere downstream: *positions are flat; all arithmetic information
lives in the logarithms $\{\log q\}$ and the von Mangoldt weights.* On the weighted space
$\ell^2_\Lambda$ the translation flow has generator $A$ with spectrum $\{k \log p\}$, the
weight operator $W = w(A)$ is a function of it, and

$$\mathrm{Tr}\big(\mathbb W^{1/2} g(\mathbb A)\, \mathbb W^{1/2}\big)
= \sum_{n \ge 2} \frac{\Lambda(n)}{\sqrt n}\big(g(\log n) + g(-\log n)\big)$$

realises the arithmetic Weil functional as a genuine operator trace (Theorem 3.4 /
Definition 3.5, **proven**), with the stage-$n$ truncation error proven $O(M_n^{-1/2})$
(Proposition 6.1, **proven**). Realised adelically place by place (Connes' semi-local trace
formula), the geometric and spectral sides of the explicit formula balance numerically to
$\sim 10^{-36}$ at 35-digit precision, and the measured truncation constant converges to
$2.0$ (`adele_trace.py`, **verified**).

**Significance and the honest boundary.** This is the program's one fully solid pillar: the
prime side is a trace of constructed data. But the identity it feeds — the explicit formula
— is Guinand–Weil, which holds *whether or not the zeros lie on the line*. L1 anchors every
later gate (E4a trace-consistency) and decides nothing about RH; the program proves this
about itself at the next level.

## 4. Level L2 — the character level, and why it is closed

**Finding** ([S01](sources/PSC2-S01-character-level.md), all **proven**). The sieve's own
data assembles into the flow character
$\chi_W(z) = \mathrm{Tr}(W e^{izA}) = -\frac{\zeta'}{\zeta}(\frac12 - iz)$, holomorphic on
$\{\mathrm{Im}\,z > \frac12\}$; its meromorphic continuation has simple poles exactly at the
zeros. The explicit formula *is* the residue calculus of $h(z)\chi_W(z)$ across the line
$\mathrm{Im}\,z = \frac12$.

**The circularity theorem** (**proven**, binding): any proposal of the shape "(a) let the
sieve connect primes to zeros, then (b) use Weil to prove the sides equal" is circular —
the sieve delivers $\chi_W$ only where the zeros are absent, and the only operation
producing the zeros is the continuation, which *is* step (b). The loop has unit length and
returns the explicit formula, which carries zero information about $\{\beta_\rho\}$.

**Significance.** L2 is the sharpest statement of *where the zeros live* in the sieve's
data: behind an analytic continuation whose crossing is exactly the explicit formula. The
level is closed — everything provable there is proven, and everything beyond is a wall
(RH $\iff$ $\chi_W$ continues holomorphically to $\{\mathrm{Im}\,z > 0\}\setminus\{\frac i2\}$,
Corollary 4.1, **RH-equivalent**). All open work therefore lives at L3 and L4.

## 5. Level L3 — the determinant level: theorems won, routes closed

**Motivation.** If eigenvalues are too rigid (see L4's obstructions), determinants are the
next coordinate: finite sieve stages carry secular polynomials
$p_n(u) = \det(I - uB_w)$ of a weighted non-backtracking operator on the bipartite divisor
graph (primes $p < 2^n$ vs composites $m \in I_n$, edge $p \sim m$ iff $p \mid m$, weights
$v_p(m)p^{-\beta}$). The Hurwitz dictionary (**proven**) prices the level: *if* stage
determinants converge to $e(s)\xi(s)$ on the strip (conjecture C1 / hypothesis H\*, open),
then eventual stage-zero confinement off the critical line (C2) is **equivalent** to RH —
the wall in determinant coordinates — while every partial confinement theorem is a genuine
zero-free-region theorem (the "graded ladder", P2.4).

**Findings.**

- **F03 (WP06) — the weighted Ihara–Bass identity is proven** in multigraph form, by an
  explicit block-triangular factorisation, certified in exact rational arithmetic at all
  stages $n \le 6$ and cross-checked symbolically. The honest weighted pole locus that
  follows is a fat annulus — **proven**, fitted-constant-free, and *weak* by its own
  pre-registered standard: it cannot separate structural from arithmetic detachment. The
  weakness was recorded and the downstream theorem target re-scoped, exactly as the WP's
  falsifier prescribed.
- **F04 (WP07) — the uniform normalised-gap theorem (G3) is proven**: the random-walk
  spectral gap of the stage graphs satisfies $g_{\mathrm{sym}}(n) \ge c > 0$ for all $n$,
  with explicit $c = 1.2\times10^{-7}$ for $n \ge 10$ (hub-minorization; Perron–Frobenius
  below), against a census flat at $\approx 0.566$ out to $n = 15$. The sharp constant and
  the gap-rung extensions (routes α/β, which would feed P2.4 zero-free regions) remain open.
- **F05 (WP08) — the edge-purity ("anti-Siegel") theorem is proven for every stage and every
  weight $\beta$**: the peripheral spectrum of $B_w$ is exactly the simple Perron pair
  $\{\pm\rho\}$ — no eigenvalue, real or complex, shares the peripheral circle. The same
  run's pre-registered β-sweep *fired the falsifier* on the older census claim: "exactly 4
  detached at every stage" is a finite-window artifact (a persistent fifth detaches at
  $\beta = 0.30$ from $n = 8$). What survives, verified at all 66 sweep points: no real
  detached eigenvalue besides the Perron pair — the graph avatar of "no Siegel zero" stays
  clean, with margin improving in $n$.
- **F06 (WP13) — the sieve step obeys an exact gluing law (proven), and precisely that law
  closes route γ.** Adjoining one composite multiplies the stage polynomial by an explicit
  Green-quadratic multiplier: $p_{G+x} = p_G \Psi_x$. The hoped-for Asano/Lee–Yang
  contraction structure — a zero locus preserved by the sieve step, which (at full
  Ramanujan strength, with C1) would have been RH-adjacent — does **not** exist: strict
  Perron injection at every same-component core step, proven and measured 45/45 at
  $n \le 6$. Route γ is closed entirely (X13).

**Significance.** L3 now owns four of the program's five theorems. Its open beam is H\*
(WP12): a coupled, functional-equation-symmetric stage family converging on the strip. The
Gonek–Hughes–Keating hybrid formula is the evidence *for*; Turán–Montgomery (partial sums
of $\zeta$ have zeros right of $\sigma = 1$) is the standing caution that family choice is
load-bearing.

## 6. Level L4 — the eigenvalue level: the gates, the kill, and the salvage

**Motivation and design.** By Lemma 1.1 (**proven**, classical) the critical line is the
unitarity line of the dilation group: a self-adjoint realisation can only ever see
$\mathrm{Im}\,\rho$; $\mathrm{Re}\,\rho = \frac12$ is carried by the normalisation. An
eigenvalue program targets $\gamma$ and can target nothing else. The working object is the
**sieve-Galerkin compression** $H^G_n = P_n D P_n$ of the dilation generator, compressed
along the sieve's own filtration, with the functional-equation symmetry $J$
($JDJ^{-1} = -D$) carried **by construction** at every stage. The known obstructions are
answered by gates, not hope: E0 (density), E1 (pairing), E2 (inclusion), E3 (pollution),
E4 (pre-registered evaluation harness), E5 (completeness — the wall, priced, never
scheduled).

**F01 (WP01) — the pairing lemma (E1) is proven.** If $JV_n = V_n$, the compression
anticommutes with $J|_{V_n}$: the stage spectrum is exactly $\pm$-paired with unitarily
paired eigenvectors. Corollary: in the parity grading the compression is exactly
off-diagonal, so stage spectra are $\{\pm s_i\}$ with $s_i$ singular values of the graded
block — pairing holds *exactly*, not asymptotically. The residual obligation (actually
constructing a $J$-invariant basis compatible with the sieve inventory) was discharged by
the next finding's builder.

**F02 (WP02) — the density gate kills the first instantiation, by proof.** The N0 builder
(Gaussian bumps at $u = \pm\log q$ + a Hermite disk at the archimedean place; matrix
elements exact at 35 digits) was run against the pre-registered gate: counting function
$N^+(T)$ must track $R(T) = \frac{T}{2\pi}\log\frac{T}{2\pi}$ on derived windows with zero
fitted parameters. It failed decisively — deviation *growing* $3.5 \to 6.3$ across stages
against a required decrease to $\le 0.05$ — and the finding upgraded the failure to a
theorem: **no fixed basis whose phase-space cells are frequency intervals centred on
$\tau = 0$ can pass E0** (the counting law of any such family is concave; a three-line
lemma shows concave laws are bounded away from the convex target by
$\varepsilon \ge \frac{\rho-1}{\rho+1} \to \frac13$ on the derived windows). The kill is
informative: the N0 design inherited the *position* reading of the inventory — the residue
of the refuted eigenvalue-at-$\{\log p\}$ picture — whereas in the explicit formula the
primes enter as **translation lengths** (frequency data). Per the falsifier, the E-track
was stopped pending a redesigned window.

**F07 (WP02b) — the rewindow: salvaging $H^G_n$ on the Berry–Keating wedge.** The redesign
note of F02 prescribed the escape, and WP02b pre-registered it: keep the ambient, the gate,
the metric, the windows, and the bar *identical*, and change only the phase-space window
that defines $V_n$. The W1 builder places modulated coherent states on the sieve sites
($u_0 = 0$ and $u_q = \log q$), with derived tiling widths, and gives each site a frequency
ladder that switches on at the wedge boundary $\tau_{\min}(u) = 2\pi e^{u-1}$ — i.e.
phase-space support $|u| \le 1 + \log\frac{|\tau|}{2\pi}$, the two-cutoff Berry–Keating
wedge, realised on the sieve's own inventory with zero fitted parameters (the $+1$ in the
wedge extent is what makes the tiled cell count equal $R(T)$ *including* the $-T/2\pi$
term; the derivation is one integral, performed before the run). The predicted density
$\sim \frac{1}{2\pi}\log\frac{T}{2\pi}$ is increasing: the law is convex, structurally
outside the killed class. Outcome of the pre-registered run (7 Jul 2026, finding
[F07](findings/PSC2-F07-density-rewindow.md)): **E0b PASS** — deviation strictly decreasing
$0.118 \to 0.104 \to 0.064 \to 0.022 \to 0.020$ over stages $n = 4, 6, 8, 10, 12$, final
deviation $\le 0.05$ met, spectrum tracking the derived ladder law throughout, all
must-fail controls failing, positive control passing. Two consequences, both pre-registered
in advance of the run: the E-track (WP03–WP05) **reopens** with $H^{G,\mathrm{w}}_n$ as the
working primary; and per obstruction O6 the pass is **not evidence about zeros** — a
wedge-shaped basis passes E0 regardless of arithmetic content; E0 is a filter that can only
kill. The arithmetic content of the E-track lives entirely downstream, in E4b and the decoy
battery.

**Significance.** L4 now has a live primary again, constructed — not merely postulated —
with exact pairing, a parameter-free Weyl law, and $D^2$ matrix elements already delivered
for the certified-enclosure pencil of WP04. The level's ceiling is stated in advance and
has not moved: even certified enclosures + no-missing-spectrum + trace-consistency together
do not decide RH (gate E5 is the wall).

## 7. Exhaustive reading of the findings: what is actually established

The program's ledger, read as one statement:

1. **The prime side of the explicit formula is fully constructive.** Sieve, trace, rate,
   adelic realisation: proven, verified to $10^{-36}$, with $O(M_n^{-1/2})$ stage error.
   (L1.)
2. **The zeros are provably *not* in the constructive data.** They appear only across an
   analytic continuation that is itself the explicit formula; any sieve-plus-Weil shortcut
   is circular by theorem. (L2.)
3. **Finite stages can carry exact structure without carrying arithmetic.** The stage
   graphs have proven pairing, proven uniform gap, proven edge purity, a proven per-step
   gluing law — and proven/verified *absence* of the structures that would have encoded
   zeros cheaply: no eigenvalues at $\{\log p\}$ density (density mismatch, proven), no
   preserved Asano locus (F06), no naive stage lifts (X5), detached graph spectra
   block-structural rather than arithmetic (F4/F05) — and now the sharpest instance:
   a family that *passes* the counting-law gate with a derived, convex, parameter-free
   Weyl law still carries no measurable arithmetic beyond that law (F10–F14: the wedge
   family and its arithmetic-blind decoy are indistinguishable at certified resolution).
   Structure is abundant; arithmetic transfer is the hard part, exactly as the walls
   predict.
4. **Design classes can be killed by proof, not just by measurement.** F02's no-go lemma
   and F06's strict-injection theorem each close an entire family of constructions. This is
   the program's distinctive product: negative results with the generality of theorems.
5. **The gate discipline works in both directions.** Three falsifiers fired (F02, F05
   count-census, F06), plus one falsifier branch quantified on a fixed window (F09),
   plus one pre-registered family closure (F11: counting law only); two
   gates passed after derived redesigns (F07 density; F08 enclosures, its saturation
   caveat measured and carried forward); every verdict was mechanical against criteria
   fixed in advance — including one INDETERMINATE (F09's branch rule: an
   operationalisation artifact, disclosed two-sidedly and resolved by a labelled
   post-hoc supplement rather than by moving the bar), one run invalidated by its own
   control line and repeated after a disclosed control redesign (F10: the decoy's
   site grid had to be nested, like the inventory it imitates), and one letter-criterion
   pass correctly *rejected* by a resolution budget fixed in advance (F11: E4b's median
   decreased at every stage, by a total of $0.128$ against a certified floor of $0.73$ —
   sub-resolution drift, not localisation). No verdict depended on a choice made after
   seeing data.
6. **Everything terminates at one wall.** Completeness on a genuine Hilbert space, Weil/Li
   positivity, C2-given-C1, real $\chi_W$-poles, Hermite–Biehler structure for $\Xi$,
   norm-resolvent limits with positive pairing: all proven equivalent to RH (W1–W6). Meyer
   2005 calibrates the category: on nuclear non-Hilbert spaces all zeros are realised
   *unconditionally*, so **positivity — not spectral realisation — is the entire remaining
   content** of Hilbert–Pólya. Any claimed spectral success must say where its positivity
   comes from, or it has silently reproduced Meyer.

## 8. Relation to the Riemann Hypothesis

Directly: **nothing in PSC2 bears on the truth of RH**, and the program proves *why* its
current instruments cannot: each of its levels has a proven RH-equivalent ceiling, and its
rigour convention forbids presenting motion below the ceiling as motion toward it.

Structurally, the program contributes to the RH literature in three honest ways:

- **Unconditional infrastructure.** The trace identity with rate, the Ihara–Bass identity,
  the gap and edge-purity theorems, and the gluing law are theorems independent of RH, in
  the intersection of analytic number theory and spectral graph theory.
- **Equivalence cartography.** The four-level picture with proven bridges makes precise
  that Weil positivity, determinant confinement, and spectral completeness are one
  obstruction, and prices every proposed route against it in advance. The graded ladder
  (P2.4) converts any future partial confinement theorem into a zero-free region — the
  correct unconditional currency.
- **Failure taxonomy.** The X-ledger and no-go theorems (density mismatch; concave counting
  laws; unfolding fabrication; closed unitary quantum graphs vs $\Lambda$-support;
  normalised kernels degenerating; holomorphic moments not certifying real support) are
  reusable filters for anyone's Hilbert–Pólya proposal, not just this one.

## 9. Adjacent concepts

- **Connes' noncommutative geometry.** L1/L2 live on Connes' adèle class space; the
  semi-local trace formula is the proven part, the global Hilbert-space statement is the
  wall (W6). PSC2's E-track is a finite-stage Galerkin shadow of that picture.
- **Berry–Keating $xp$ and quantum chaos.** The wedge window of F07 is the BK two-cutoff
  regularisation made rigorous at the level of counting; the Connes–Moscovici prolate wave
  operator (2022) is the proven neighbour showing a genuinely self-adjoint archimedean
  operator can carry the smooth counting law — and simultaneously the proof that carrying
  it is not evidence about zeros (obstruction O6).
- **de Branges spaces / Hermite–Biehler.** The structure-function route is priced as wall
  W5; the proven N3 no-go (real entire functions are never HB) fences off the naive
  version.
- **Li coefficients and Weil positivity.** WP10/WP11 pursue the unconditional fragments
  (restricted-support positivity; finite-range Li asymptotics) strictly below the
  positivity wall (W6).
- **Ihara zeta functions, Ramanujan graphs, non-backtracking spectra.** The G-track is a
  transplant of this technology onto the divisor structure of the sieve blocks; F03–F05 are
  contributions to weighted non-backtracking spectral theory in their own right
  (Kotani–Sunada, Krzakala et al., Bordenave–Lelarge–Massoulié are the imported
  calibrators).
- **Lee–Yang/Asano contractions and stable polynomials (Borcea–Brändén).** WP13 asked
  whether the sieve step belongs to the stability-preserving class; the proven answer is
  no (F06) — a data point for the limits of Lee–Yang methods on arithmetic gluings.
- **Beurling generalised primes.** The principled home for "which prime-like systems admit
  which spectral realisations" (X7's salvage); a natural laboratory for separating
  arithmetic content from density content.
- **Crystalline measures (Meyer).** The unconditional realisation of all zeros on nuclear
  spaces is the standing category detector for the whole field.

## 10. Further research (scheduled; each with WP, falsifier, and standalone value)

Reopened by F07, in the pre-registered order:

1. **WP04 — certified enclosures (E3b), first in line.** Second-order relative spectra from
   the pencil $(P_n D P_n, P_n D^2 P_n)$ — pollution-free by classical theorem
   (Shargorodsky; Levitin–Shargorodsky; Davies–Plum). The W1 builder already delivers the
   $D^2$ matrix elements. Deliverable: certified boxes around stage spectra, unconditional.
   *(Done — 7 Jul 2026, [F08](findings/PSC2-F08-certified-enclosures.md): gate passed,
   machinery certified end-to-end; measured rate $\alpha \approx 0.01$ — the radii saturate
   at a floor $\approx 1.72$ on $[0,50]$, the wedge's fixed-aperture band-limit; the caveat
   travels to WP03/WP05, and the escalation route if E4b needs finer resolution is the
   prolate pencil.)*
2. **WP03 — the inclusion theorem (E2).** Fix the ambient once (E2a), prove $P_n \to I$
   strongly on a core $\Rightarrow$ strong-resolvent convergence $\Rightarrow$ no zero
   missed (E2b). Unconditional; the honest half of K2.
   *(Done — 7 Jul 2026, [F09](findings/PSC2-F09-inclusion-theorem.md): E2a delivered as a
   tagged four-ambient record (M4 done once, charter H9 stays deferred). E2b: the chain
   as written above is incomplete — strong convergence of projections does **not** give
   strong-resolvent convergence of compressions; the missing hypothesis is graph-norm
   control, precisely the K2 pollution mechanism. The proven replacement: graph-norm
   stage density $\Rightarrow$ spectral inclusion, quantitatively, via the stage
   resolution function $r_n(\lambda)$ — the real-$\lambda$ restriction of the F08
   pencil; plus the finite-place prototype realising the chain verbatim, and coarse
   inclusion on W1 with explicit constants. The W1 instantiation fired the WP's
   falsifier, quantified: certified floors $r_n \ge 0.73$ on $[0,50]$ at every fine-grid
   stage, a deep sub-wedge unit vector with $\mathrm{dist}(\varphi, V_n) = 1.0000$, and a
   permanent spectral hole below $9.34$ — the wedge's fixed aperture again (F08's
   fingerprint as an exact lower envelope). Constrains the window design; the
   prolate-pencil escalation stands; E4b's resolution budget is now binding on WP05.)*
3. **WP05 — the evaluation harness (E4 + HS gates).** Trace-consistency against the
   $10^{-36}$ anchor within the proven $O(M_n^{-1/2})$ envelope (excess = pollution mass,
   deficit = spectral loss); matched displacement on $[0, 50]$ with the $\gamma$-list as
   final evaluation only; the full decoy battery (bare prolate compression must pass E0's
   shape and fail E4b). **This is where the W1 family's arithmetic content is actually
   tested for the first time** — now under the binding F08+F09 resolution budget
   (enclosure radii floor $\approx 1.72$; quasi-mode floor $\ge 0.73$; no spectrum below
   $9.34$), which the E4b design must price in advance.
   *(Done — 7 Jul 2026, [F10](findings/PSC2-F10-e4a-trace-consistency.md)–[F14](findings/PSC2-F14-hs7-genealogy.md):
   the harness is delivered, candidate-independent, and valid two-sidedly — the positive
   h.o. control converges to $6\times10^{-11}$, the sine decoy passes both internal
   identities and fails every arithmetic test, and one run was invalidated by its own
   decoy-control line and repeated after a disclosed nested-grid redesign. Verdicts,
   all mechanical: E4a fails by persistent excess ($+2.73\times10^{-2}$, stage-stable,
   attributable to 0.2% to the two eigenvalues below $\gamma_1$ — the wedge counting
   law's $T/2\pi$ surplus made flesh); E4b's letter rule fires on a $0.128$ drift that
   the pre-registered budget correctly rejects as sub-resolution ($< 0.73$), and W1
   ($0.680$) does not beat the density-matched decoy ($0.695$); HS1 diverges — its
   conjectured implication is refuted for W1; HS2 fires $\gamma$-free; HS7 shows the
   pollution is structural (15/17 chains persist, drift $0.026$). The pre-registered
   closure branch fires: **the W1 family closes as counting law only**, and the E-track
   moves to the chartered escalation
   [WP15](workpackages/PSC2-WP15-prolate-pencil.md), the prolate pencil, which reuses
   this harness verbatim. Per O6: none of this is evidence about zeros.)*

Independent of the E-track:

4. **WP12 — H\* via the AFE-symmetric V2 family** (L3's load-bearing beam; the single most
   valuable open target).
5. **WP07 §ext — gap rungs (routes α/β)** toward a Bordenave-type real-sector bulk bound;
   shared engine with the surviving anti-Siegel conjecture; any success is a genuine
   zero-free-region statement via P2.4.
6. **WP09–WP11** — truncation-rate proposition with constants; restricted-support Weil
   positivity (first new instance: places $\{\infty, 2\}$); unconditional finite-range Li
   asymptotics.
7. **WP14 — escape routes from the F8 no-go** (energy-dependent scattering, open systems,
   pseudo-orbit interference) — opportunistic.

## 11. Alternative routes (unscheduled; priced against the ledger)

- **The genuine prolate pencil.** Replace the fixed-basis compression outright by the
  Connes–Moscovici prolate operator's finite stages (quadratic in $(D, x)$). This was the
  pre-registered fallback had F07 failed; it remains the natural next family if W1 fails
  at E4b. Cost: exact matrix elements are heavier; benefit: the proven counting theorem
  comes with the operator. *(W1 did fail at E4b — 7 Jul 2026, F11 — and this route is no
  longer "unscheduled": it is chartered as
  [WP15](workpackages/PSC2-WP15-prolate-pencil.md), charter row T12.)*
- **Positivity transfer from nuclear spaces.** Meyer realises all zeros unconditionally
  without positivity; the open question with actual content is whether any functorial
  passage nuclear $\to$ Hilbert preserves enough structure to make a positive pairing —
  this is W4 territory and must be priced as such, but "understand exactly *what* fails"
  is an unconditional research object.
- **Beurling systems as a control family.** Run the entire gate battery on generalised
  primes with tunable counting laws: which gates detect arithmetic (Möbius/unique
  factorisation) versus mere density? This would sharpen O6 from a caution into a
  classification.
- **Function-field calibration.** Over $\mathbb F_q(t)$ the RH analogue is a theorem
  (Weil), and Ihara zeta *is* the honest analogue of the stage determinants; mapping the
  G-track constructions onto a case where the wall is down could identify exactly which
  ingredient the number-field case lacks.
- **The de Branges chain, restricted.** Not the full W5 wall, but the unconditional
  fragments: which canonical systems have the stage products $\Xi_n$ of gate HS1 as
  transfer matrices?

All five respect the X-ledger; none may be presented as a step toward RH until it produces
an unconditional theorem below a wall.

## 12. Research program sketch — the next step (PSC3 outline)

A concrete, falsifiable continuation, in the charter's own format:

**Phase A (weeks).** WP04 first (E3b certified enclosures on the W1 family; the $D^2$
blocks exist today). Falsifier: enclosure widths not shrinking with stage — then the W1
family is numerically hollow regardless of E0b, and the prolate-pencil alternative route
is promoted. In parallel: WP09 (rate proposition — a paper-sized standalone).

**Phase B (weeks–months).** WP03 (E2 inclusion, unconditional) and WP05 (E4a/E4b + full
decoy battery). Pre-registered decision point: if the W1 family shows no displacement
improvement over the bare-wedge decoy at E4b, the E-track closes *as a family* and the
finding states plainly that wedge + sieve inventory carries no arithmetic beyond its
counting law — itself a publishable sharpening of O6. Success criterion (fixed now):
median displacement decreasing over three consecutive stages with the decoy flat.
*(This decision point occurred — 7 Jul 2026,
[F11](findings/PSC2-F11-e4b-matched-displacement.md): W1 and the decoy indistinguishable
at certified resolution ($0.680$ vs $0.695$ against a $0.73$ floor); the family closed
as counting law only and [WP15](workpackages/PSC2-WP15-prolate-pencil.md) was chartered.)*

**Phase C (months, parallel).** WP12 (H\*): build the AFE-symmetric V2 coupled family with
pairing-by-construction (HS5, proven), test C1 on $\{\sigma > 1\}$ with couplings on, then
the normal-family bound on strip compacts. Falsifier: FE-asymmetry growth (the X4
signature) at any coupling strength. WP07 route β: the real-sector bulk bound, sharing
F06's banked positives (graded chain, off-centre avoided disk).

**Phase D (continuous).** The ledger: every landing updates the charter; every falsifier
fired closes a route in writing; the declaration bar of PSC2-001 §4 stands unmoved.

**Pricing statement (binding).** Phases A–C are all strictly below the walls. If every one
of them succeeds completely, RH remains open, and the program will say so; what will have
changed is the size of the unconditional platform — certified spectra, a strip-convergent
determinant family, a zero-free-region engine — on which any future assault on the
positivity wall would stand.

## 13. Status declaration

Per [PSC2-001 §4](PSC2-001-conventions.md): no chain of results in this program terminates
in a statement about the zeros themselves; several chains terminate, by proof, in
RH-equivalent walls. **RH is open.** The program's door to a proof is open at a bar that
does not move; nothing here is within sight of that bar, and this manuscript should be
read, and cited, accordingly.

---

*Provenance: charter and ledger [PSC2-000](PSC2-000-charter.md); conventions
[PSC2-001](PSC2-001-conventions.md); sources S00–S06 in [sources/](sources/); findings
F01–F14 in [findings/](findings/); all numerics reproducible from
[numerics/](numerics/) (see [README](README.md) for the run list and regression targets).*
