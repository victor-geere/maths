# Notes — the prime-sieve / Ihara–Connes program: findings, significance, working log

*Companion to [path.md](path.md) (the corrected proof path) and [implementation.md](implementation.md)
(the corrected constructions and numerical protocol). Started 5 July 2026.*

*Rigour policy (repo convention, [CLAUDE.md](../CLAUDE.md)): every claim below is tagged
**proven** / **conditional** / **RH-equivalent** / **heuristic**. Refutations of our own material
are recorded as positive findings, per the precedent of [../flawed/](../flawed/) and the
Phase 3–4 corrections in [../adele/](../adele/).*

---

## 0. TL;DR

The folder proposes: build finite graphs from the composite-generator sieve, show their Ihara
determinants converge to the completed zeta $\xi(s)$, identify the limit operator with the adelic
Dirac operator of the Connes–Consani(–Moscovici) picture, and derive RH as a limiting Ramanujan
property. **The idea survives; the current artifacts do not.** As of this review:

- the graph the three scripts actually build is **empty** (no edges, proven and confirmed by
  execution, §2.1) — the same $pq \ge 2^{2n}$ trap that made Phase 3's Def 4.1 vacuous;
- the "unfolding" step that produced the reported pole↔zero matches is **tautological** (proven
  and confirmed by execution, §2.2): it discards its input, so it "matches" the zeros for *any*
  graph, including the empty one;
- several supporting claims in [proof-sketch.md](proof-sketch.md) /
  [closed-form.md](closed-form.md) / [ihara-connes.html](ihara-connes.html) misstate the
  classical theory (§2.3) and are corrected in [path.md](path.md).

What survives is genuinely valuable and is developed in [path.md](path.md): a precise two-lemma
**Hurwitz dictionary** showing exactly what determinant convergence buys (given it, uniform
spectral-gap bounds are *equivalent* to RH, and partial gap bounds are *equivalent* to zero-free
regions — a graded, falsifiable ladder whose first rung is de la Vallée Poussin's classical
region); a **corrected, non-vacuous graph** (the bipartite divisor graph, mirroring Phase 3's
repair); and a structural reason (Kotani–Sunada pole confinement) why graph determinants are
better approximants than Turán's partial sums, which provably fail the analogous program.

Nothing in this folder proves, or is claimed to prove, RH. The wall (positivity / uniform
Ramanujan) is *relocated into graph-spectral coordinates*, not lowered — see
[path.md](path.md) §P6 and [../adele/phase7.md](../adele/phase7.md).

---

## 1. What the program attempts (fair statement)

From [ihara-connes.html](ihara-connes.html) §§3–4 (the two paragraphs this review completes):

1. **Step 3 (CCM connection).** Supply finite, computable approximations to the adele class
   space $X = \mathbb{A}_\mathbb{Q}/\mathbb{Q}^\times$: finite graphs whose Ihara zeta plays the
   role of a spectral determinant, so that "RH = Ramanujan property of the limit" becomes a
   statement attackable with combinatorics and analytic number theory.
2. **Step 4 (three hurdles).** (i) uniform Fredholm-determinant convergence; (ii) norm-resolvent
   convergence of graph operators to an adelic Dirac operator; (iii) uniform spectral-gap
   ("almost-Ramanujan") bounds from sieve inequalities.

The strategy is sound *as a scheme*; the precise content of each hurdle, and what solving each
would actually deliver, is the subject of [path.md](path.md). The version in
[proof-sketch.md](proof-sketch.md) ends with "The Riemann Hypothesis is therefore a
consequence…" — that conclusion is **not** available at the claimed strength; the corrected
endgame (what is genuinely equivalent to what) is Theorem P2.3 in [path.md](path.md).

---

## 2. Verified defects in the current artifacts — all **proven**

### 2.1 D1: the scripts' prime graph is empty ($A \equiv 0$) — **proven, confirmed by execution**

All three scripts ([ihara-riemann-spectrums.py](ihara-riemann-spectrums.py),
[ihara-zeta-convergence.py](ihara-zeta-convergence.py),
[numeric-verification.py](numeric-verification.py)) share `build_prime_graph`: vertices are the
primes $p \in I_n = [2^n, 2^{n+1})$, and an edge $\{p,q\}$ is added when some composite
$m \in I_n$ is divisible by both.

**Claim.** For $n \ge 2$ no edge is ever added.

*Proof.* If $p \ne q$ both divide $m$ then $m \ge pq \ge 2^n \cdot 2^n = 2^{2n} > 2^{n+1}-1$,
so no $m \in I_n$ qualifies. (Independently: every prime factor of a composite $m \in I_n$ is
$< 2^n$ — Lemma 1 of [../adele/phase1.md](../adele/phase1.md) — while the vertex set consists of
primes $\ge 2^n$; the script's `fac_in` intersection is empty for *two* separate reasons.)
$\blacksquare$

*Execution check (5 Jul 2026):* edges added $= 0$ for $n = 6, 8, 10$ ($|V| = 13, 43, 137$).

**Consequence.** With $A = 0$, $D = 0$, the generalized eigenvalue pencil used for the poles
degenerates to $\det(M - uK) = (u^2-1)^N$: every "pole" is $u = \pm 1$, artifact of the empty
graph. This is exactly why the apps report *all* poles "on the unit circle" — it is not a
Ramanujan phenomenon, and it also explains why the poles sat on $|u| = 1$ rather than on the
correct Ramanujan circle $|u| = q^{-1/2}$ (§2.3, M1).

**Significance.** This is the *same* vacuity as Phase 3's Def 4.1
([../adele/phase3.md](../adele/phase3.md)), reproduced in graph clothing, and it strengthens
that finding into a design principle: **within one dyadic block, large primes cannot be coupled
through composites of that block; any non-vacuous coupling must be cross-scale** — small primes
$< 2^n$ to composites in $I_n$. The corrected (bipartite) graph is Definition I1.1 in
[implementation.md](implementation.md), mirroring the Phase 3 repair $H_n' = D_n' +
\varepsilon_n A'$.

### 2.2 D2: the unfolding is tautological — **proven, confirmed by execution**

`unfold_eigenvalues` / `unfold_args` compute, for sorted input of length $N$,
`unfolded[i] = invert_zero_count((i+0.5)/N)`. The input *values* never enter — only the count
$N$ does. Two consequences, both confirmed by execution:

1. `unfold(random) == unfold(linspace)` exactly: the "unfolded poles" are identical for any
   data whatsoever, hence identical for the empty graph. Any agreement with the Riemann zeros
   certifies nothing about the graph.
2. Since the quantile $(i+0.5)/N < 1$, every output lies below
   $\bar N^{-1}(1) \approx 14.92$: the pipeline is *incapable* of producing a value near even
   the second zero $\gamma_2 = 21.02\ldots$. The reported comparisons were never a match at all.

**Significance.** A protocol lesson now baked into
[implementation.md](implementation.md) §I3: *rank-based unfolding against the target's own
counting function is forbidden as evidence* — it manufactures the answer. Honest observables:
raw pole angles, counting-function fluctuations, pointwise determinant values against
$\xi(s)$ computed independently (mpmath), and gap statistics on raw data. Same failure class as
N2's normalized-kernel degeneracy in
[../berry-keating/research-findings.md](../berry-keating/research-findings.md) §3: an operation
that erases the arithmetic content while keeping the cosmetic shape of a comparison.

### 2.3 D3: misstatements of classical theory in the prose artifacts — **proven corrections**

- **M1 (Ramanujan circle).** [proof-sketch.md](proof-sketch.md) and the html assert poles on
  $|u| = 1$ iff Ramanujan. For a $(q{+}1)$-regular graph the nontrivial Ihara poles satisfy
  $qu^2 - \lambda u + 1 = 0$; for $|\lambda| \le 2\sqrt q$ the pair lies on $|u| = q^{-1/2}$
  (both roots have product $1/q$), and the Ramanujan condition is "all nontrivial poles on
  $|u| = q^{-1/2}$" — the circle $|u|=1$ carries only trivial factors. Under $u = q^{-s}$ this
  is $\mathrm{Re}\,s = \tfrac12$, as it must be. (Ihara 1966; Terras 2011, ch. 2; Kotani–Sunada
  2000 for the irregular annulus $q_{\max}^{-1/2} \le |u| \le q_{\min}^{-1/2}$ for non-real
  poles.)
- **M2 (per-block Euler factor).** proof-sketch's $\xi_n(s) = Z_n(2^{-s/2})\prod_{p \in G_n}
  (1-p^{-s})^{-1}$ takes the product over the *block* $I_n$ only. Since $\sum_{p \in I_n}
  p^{-\sigma} \to 0$ for $\sigma > 1$, that factor tends to $1$, not to $\zeta(s)$: the
  claimed convergence $\xi_n \to \xi$ on $\mathrm{Re}\,s > 1$ fails as written. The corrected
  object is *cumulative* (all primes $\le M_n$, which the sieve has by stage $n$) — see
  [path.md](path.md) P0.
- **M3 (spectral zeta vs $\xi$).** proof-sketch step 2 and closed-form §2 assert
  $\mathrm{Tr}\,|D|^{-s} = \pi^{-s/2}\Gamma(s/2)\zeta(s)$. Category error: a spectral zeta
  function carries its spectrum in *poles*; $\xi(s)$ carries the zeros as *zeros*. If
  $\sigma(|D|) = \{\gamma_\rho\}$ then $\mathrm{Tr}\,|D|^{-s}$ is Voros' *secondary* zeta
  $Z(s) = \sum \gamma_j^{-s}$, a different function with different singularities. Already
  catalogued as a standing distinction in
  [../berry-keating/research-findings.md](../berry-keating/research-findings.md) §5.3. The
  correct determinant-level target is $\det\nolimits_\zeta(D - s)$-style (zeros as zeros), i.e.
  C1 of [path.md](path.md).
- **M4 (Connes 1999 overclaim).** closed-form §2 says the adelic operator's spectrum "*is* the
  set of Riemann zeros (Connes, 1999)". What is proven: the *semi-local* trace formula
  (Connes 1999); the *global* Hilbert-space trace formula is proven **equivalent** to Weil
  positivity, hence RH-equivalent; the unconditional spectral realization of *all* zeros is
  Meyer 2005 on **nuclear, non-Hilbert** spaces, where positivity — the entire remaining
  content — is given up. (research-findings §7.3.) Writing the realization as if it were an
  unconditional Hilbert-space fact hides the wall inside a citation.
- **M5 (strong- vs norm-resolvent).** closed-form §5 asks for *strong* resolvent convergence
  $H_n \to D$ and concludes eigenvalue convergence. Strong resolvent convergence does **not**
  control spectra (spectral pollution; spectra can inflate in the limit inferior sense only);
  norm-resolvent convergence is the mode that gives $\sigma(H_n) \to \sigma(D)$ in local
  Hausdorff distance for self-adjoint families (Reed–Simon VIII.7). Hurdle (ii) is stated with
  the correct mode in [path.md](path.md) P4 — and P2 shows RH-from-determinants does not
  actually need it.

---

## 3. What survives, in one screen (details in [path.md](path.md))

| Surviving asset | Status | Where |
|---|---|---|
| Hurwitz dictionary: given determinant convergence C1, gap bounds $\iff$ zero-free regions; uniform gap $\iff$ RH | **proven** (elementary complex analysis, proofs in path.md P2) | path.md P2 |
| Corrected bipartite divisor graph $B_n$ (non-vacuous, cross-scale) | **proven** non-vacuous; spectral role open | impl.md I1 |
| Cumulative place-cycle (quantum-graph) model: stage-$N$ secular determinant $=$ truncated Euler product exactly | **proven** (elementary) | path.md P0, impl.md I2 |
| Kotani–Sunada pole confinement: finite stages *cannot* have generic complex off-line zeros — only circle $\cup$ real (exceptional) ones | **proven** (classical) | path.md P3 |
| "Graph Siegel zero" dictionary: exceptional real poles $\leftrightarrow$ Landau–Siegel phenomena | heuristic, precisely stated | path.md P3 |
| Gap ladder milestone M1: recover de la Vallée Poussin zero-free region from a $c/\log$ gap | open, falsifiable, plausibly provable | path.md P3, impl.md I5 |
| Turán–Montgomery caution: a natural approximant family provably *fails* C2 (partial sums have zeros in $\mathrm{Re}\,s>1$) | **proven** (Montgomery 1983) — calibrates family choice | path.md P3 |
| Trace-level CCM connection already verified in-repo to $10^{-36}$ | **proven** + verified | ../adele/phase6.md |

---

## 4. The complete program, file by file — significance of each finding

### Pre-existing artifacts

**[ihara-connes.html](ihara-connes.html)** — the program manifesto (dialogue form). *Findings:*
the three-hurdle decomposition (§4) and the CCM framing (§3). *Significance:* the decomposition
is the right one — it survives, corrected, as path.md P1/P3/P4 — and the CCM framing is made
operational in path.md P5 (trace level: done in-repo; determinant level: the actual open
target). *Corrections required:* its closing sentence ("solving these would complete a new
proof of RH") is true only in the conditional sense made precise by Theorem P2.3 — and P2.3
simultaneously shows hurdle (iii)-at-full-strength *is* RH given (i), so the sentence, read
carefully, says "proving something equivalent to RH would prove RH." The honest content is the
graded ladder (P2.4), which the html misses entirely. Misstatements M1/M5 originate here.

**[proof-sketch.md](proof-sketch.md)** — three-step programme sketch. *Findings that survive:*
the shape "determinant convergence + limit identification + spectral purity"; the correct
instinct that the archimedean factor and the trace formula must appear; the Siegel-zero
subtlety flagged in step 3 (kept, sharpened into the graph-Siegel dictionary P3.2).
*Findings refuted:* the per-block Euler factor (M2 — its $\xi_n$ does not converge to $\xi$);
the spectral-zeta identification (M3 — Voros category error); "poles on $|u| = 1$" (M1);
"uniform trace-class bounds… independent of $n$" is asserted for a family that provably leaves
trace class in the strip (P1.3) — the sketch's step 1 hides the entire analytic continuation
problem in one sentence. *Significance:* the sketch is the folder's clearest statement of
intent, and its failure modes taught us exactly where the real content lives (H\*).

**[closed-form.md](closed-form.md)** — survey of five embeddings of the sieve. *Findings that
survive:* the five-space table is a genuinely useful map (dyadic Dirichlet series; adelic trace;
Bruhat–Tits/Ihara; Mellin; Hilbert-space limit), and §4's warning that continuation "might
require additional input, e.g. the functional equation" is exactly right — it anticipates
obligation H\*-d. *Findings refuted:* M4 (Connes-1999 overclaim — the Hilbert-space spectral
realization is not an unconditional theorem; Meyer 2005 is, on nuclear spaces, at the price of
positivity — the price *is* the problem); M5 (strong- vs norm-resolvent). *Significance:* the
document shows the sieve is representation-agnostic — the same arithmetic feeds every
framework; what varies is which wall-coordinate you face.

**[ihara-riemann-spectrums.py](ihara-riemann-spectrums.py),
[ihara-zeta-convergence.py](ihara-zeta-convergence.py),
[numeric-verification.py](numeric-verification.py)** — the numerical pipeline. *Findings
(after this review):* D1 — the graph they build is empty, $A \equiv 0$, all reported poles are
the $(u^2-1)^N$ pencil artifact; D2 — the unfolding step is input-independent and range-capped
below $\gamma_2$, so every reported pole↔zero "match" was manufactured; the one healthy panel
(explicit-formula balance $W_\infty - A_n$ vs zero sum in `numeric-verification.py`) duplicates
what [../adele/adele_trace.py](../adele/adele_trace.py) already verifies to $10^{-36}$.
*Significance:* D1 is a *theorem* about the sieve (block-local coupling of block primes is
impossible — it upgrades Phase 3's vacuity from an incident to a structural principle), and D2
is now codified as evidence-hygiene rule I0.1. The scripts' patch plan is
[implementation.md](implementation.md) I7.2; their replacement lab code ran its first honest
baselines on 5 Jul 2026 (I8).

### New documents (this review)

**[path.md](path.md)** — the corrected proof path. *Core findings:* P1.2/P1.3 (exactly where
the bare Euler truncation lives and dies — proven both ways); the Hurwitz dictionary P2.1–P2.4
(given C1: full gap $\iff$ RH, partial gaps $\iff$ zero-free regions — the program's endgame
stated as a theorem instead of a hope); Kotani–Sunada confinement P3.1 + Turán–Montgomery
caution P3.4 (why *spectral* approximants are the right family and partial sums are the wrong
one — arguably the deepest single justification for the whole graph approach); hypothesis H\*
with four separable proof obligations; the three-route gap program with the wall marked.
*Significance:* converts the folder from "suggestive analogy + broken numerics" to "one open
conjecture (H\*), one gating lemma (W), one tractable proposition (P3.5), two machine-checkable
structure questions (Q-γ1/2), and a proven dictionary that prices every outcome."

**[implementation.md](implementation.md)** — measurement protocol + code. *Core findings:* the
evidence-hygiene rules I0 (each defect becomes a mechanical guard); the control-column design
(decoupled model must reproduce the truncated Euler product to full precision — the pipeline's
own explicit formula); the first baseline run I8, in which *every* declared "suspicious"
criterion fired exactly where it should: the raw $\beta = \tfrac12$ gap census landed in the
audit branch (Perron-scaling artefact, not arithmetic), and the weighted pole locus visibly
escapes the classical annulus — demonstrating that obligation W is the gating lemma, not a
formality. *Significance:* the folder now has falsification machinery that runs, with declared
success/failure criteria written down *before* the data.

**[notes.md](notes.md)** (this file) — the audit trail and significance map, per the
[worksheet.md](../berry-keating/worksheet.md) precedent.

---

## 5. Cross-science web (borrowings, each with its precise role and tag)

| Borrowed from | Object | Role here | Tag |
|---|---|---|---|
| **Quantum chaos** (Berry–Keating; Bohigas–Giannoni–Schmit; Gnutzmann–Smilansky) | RMT universality for chaotic spectra; quantum graphs | CUE gap-statistics diagnostic (I3); the flower-graph model whose orbit lengths are $\log m$ (I6) | heuristic diagnostic; never evidence of zero location (research-findings §8) |
| **Quantum graphs** (Kottos–Smilansky) | secular determinant $\det(I - e^{isL}\Sigma)$, exact periodic-orbit expansion | re-expresses HP as: *match orbit amplitudes to $\Lambda(m)/\sqrt m$ under unitary $\Sigma$* — the wall becomes a measurable "distance to unitarity" (I6) | exploratory, precisely stated |
| **Statistical mechanics** (Lee–Yang 1952; Asano 1970; Borcea–Brändén) | partition-function zeros confined to circles, preserved under gluing | route γ2: is the sieve recursion an Asano contraction on stage polynomials? machine-checkable per stage | open (Q-γ2) |
| **Random matrix / spectral graph theory** (Alon–Boppana; Friedman; Bordenave; MSS; Bilu–Linial) | Ramanujan bounds; tangle-free trace method; interlacing families | routes β and γ1; MSS is type-correct for our *bipartite* stages | open; full strength sits at the wall (P2.3) |
| **Number theory over function fields** (Ihara; Deligne via LPS) | graph-RH from RH over $\mathbb F_q$ | calibration: the only *completed* Ramanujan constructions import a proven RH-analogue — a measure of the rung's true height | proven (elsewhere); imported as calibration |
| **Sieve theory as operator theory** (Montgomery's large sieve; Brun–Titchmarsh) | norm bounds on incidence bilinear forms | route α: the proven prototype of "sieve inequality $=$ spectral gap"; target P3.5 → dlVP rung | open, tractable |
| **Topology / dynamics** (solenoids, Bohr compactification; Ruelle transfer operators) | each place-cycle circle has circumference $\log p$; the tower's inverse limit is the adelic solenoid — the zeros' almost-periodic home; determinants are Ruelle zeta functions | explains *why* finite stages see zero-phases mod $2\pi/\log p$ and evade no-go N1 (multiplicative, bounded encoding) | heuristic frame, with the N1-evasion argument precise |
| **Noncommutative geometry** (Connes; Connes–Consani scaling site; Connes–Moscovici prolate operator) | adele class space; archimedean fiber; a concrete self-adjoint operator whose negative spectrum tracks low zeros | P4's limit-object candidates; P5's trace→determinant ladder; prolate = archimedean model of hurdle (ii) | trace level proven (in-repo); operator level open |
| **p-adic holography** (Gubser et al. 2017) | Bruhat–Tits tree as $p$-adic AdS | decorative intuition for "stages as bulk cutoffs"; no load-bearing use | heuristic only |

No-go audit against research-findings §3 (the design passes): **N1** evaded — zeros encoded
multiplicatively as pole phases on compact circles, unboundedness carried by $\log p$ metric
data, not operator norms; **N2** evaded — Bass/secular determinants are unnormalised; **N3**
respected — stage polynomials are real, reality confined to the $u$-locus by self-adjointness
(the loophole N3 allows); **N4** respected — no moment-to-reality arguments anywhere; reality
comes from self-adjointness at every stage.

---

## 6. Master status table (the whole folder, one screen)

| Item | Tag |
|---|---|
| D1 empty graph; D2 tautological unfolding; M1–M5 corrections | **proven** (refutations, confirmed by execution) |
| Corrected objects $X_N$, $B_n$; non-vacuity | **proven** |
| C1 on $\mathrm{Re}\,s > 1$; death of bare model at $\sigma = 1$ (P1.2/P1.3) | **proven** |
| Hurwitz dictionary (P2.1–P2.4): gap $\iff$ RH; partial gaps $\iff$ zero-free regions, given C1 | **proven** |
| Kotani–Sunada confinement (P3.1); Turán–Montgomery caution (P3.4) | **proven** (classical) |
| H\* (coupled determinants converge in the strip) | **open** — the conjecture |
| Obligation W (weighted confinement locus) | **open** — gating lemma; baseline I8 shows it is genuinely needed |
| P3.5 ($c/\log$ gap from sieve inequalities) → M1 dlVP rung | **open, tractable** |
| Q-γ1 covering tower; Q-γ2 Asano gluing | **open**, machine-checkable |
| Full uniform Ramanujan for the stages (with C1) | **= RH** by P2.3; treat as RH-equivalent wall |
| Hurdle (ii) with positive limit space | **open**; positivity is the wall (Meyer calibration) |
| Graph-Siegel dictionary; solenoid frame; quantum-graph unitarity coordinate | **heuristic**, precisely stated |
| RH | **open** — unchanged, as it must be |

---

## 7. Working log

### Dump 1 — 5 Jul 2026, after reading the folder and running the defect checks

- Confirmed D1/D2 by execution before writing anything (edges $=0$ at $n{=}6,8,10$; unfold
  ignores input; unfold range capped at $\bar N^{-1}(1) \approx 14.9$). The folder's numerical
  "evidence" is void — but the *scheme* is better than its execution, and the repair is close to
  the Phase 3 repair.
- Central realization while checking Hurwitz directions: **given C1 (locally uniform
  determinant convergence on the open strip), C2 (eventual nonvanishing off the line on
  compacts) is not merely sufficient for RH — it is equivalent to it.** Forward: Hurwitz/Rouché.
  Backward: if RH holds, $\xi$ is zero-free on any compact $K$ off the line, so
  $\min_K|\xi| > 0$ and uniform convergence forces $D_n \ne 0$ on $K$ eventually. So the whole
  program, if C1 succeeds, lands **exactly on the repo's frontier wall in new coordinates** —
  consistent with [../adele/phase7.md](../adele/phase7.md): reproduction cannot be upgraded to
  decision without new positivity. The graded corollary is the actionable part: *partial* gaps
  $\iff$ *zero-free regions*, an honest ladder with provable rungs.
- Why graph determinants beat Turán partial sums as approximants: self-adjointness of finite
  adjacency confines Ihara poles (Kotani–Sunada) to circle $\cup$ reals — the failure mode is
  only the *exceptional real pole*, the graph avatar of a Siegel zero. Partial sums
  $\sum_{n\le N} n^{-s}$ have no such confinement and provably violate the analogue of C2 even
  where $\zeta$ itself is zero-free (Montgomery 1983). **Family choice is load-bearing; spectral
  origin of the approximants is the advantage.**
- The three known technologies for full Ramanujan bounds are all reality/positivity
  technologies: Deligne (RH over $\mathbb F_q$!) behind LPS; real-rootedness of expected
  characteristic polynomials behind MSS interlacing families; Lee–Yang/Asano circle methods in
  the statistical-mechanics reading. This is the N3/Hermite–Biehler shape again — reality of
  zeros from a positivity structure. Expect the wall there; say so plainly.
- Quantum-graph reformulation (Kottos–Smilansky): a metric graph with one bond of length
  $\log p$ per prime has periodic-orbit lengths exactly $\{\log n\}$ — the support of the
  explicit formula's prime side. Self-adjointness makes the secular zeros real *automatically*;
  the entire difficulty transmutes into matching orbit *amplitudes* to $\Lambda(n)/\sqrt n$
  under a **unitarity** constraint on the vertex scattering matrix. The wall in quantum-graph
  coordinates = unitarity/positivity of the S-matrix. Falsifiable toy: best unitary fit to the
  first 100 amplitudes (impl.md I6).
- Large sieve inequality is literally an operator-norm bound (a spectral-gap statement) for the
  primes-vs-progressions incidence structure — the proven prototype of "sieve inequality
  $\Rightarrow$ gap". Brun–Titchmarsh + large sieve should give a $c/\log M_n$ gap for $B_n$;
  through the dictionary that is exactly de la Vallée Poussin strength. If the machinery cannot
  reproduce dlVP, it is broken; if it can, each gap improvement maps to a zero-free-region
  improvement (Vinogradov–Korobov as the second rung).
- No-go audit for the corrected design: N1 (bounded numerical range) evaded because zeros are
  encoded *multiplicatively* (pole phases on a compact circle per place; unboundedness lives in
  the $\log p$ scale factors, not operator norms); N2 evaded because Bass determinants are
  unnormalized; N3 respected because graph char polys are real — reality is confined to the
  *u*-circle by self-adjointness, exactly the loophole N3 permits; N4 respected — we never argue
  from moments to real support, only from self-adjointness.
- Topology note for later: the family $\{$circle of circumference $\log p\}_p$ glues into the
  adelic solenoid — the zeros' natural home is the Bohr-type compactification; each finite stage
  sees a finite sub-product. Benjamini–Schramm convergence of the finite stages to the
  tree/solenoid limit gives spectral-measure (Plancherel/Kesten–McKay) convergence — the proven
  model case of hurdle (ii)'s weak form.

### Dump 2 — 5 Jul 2026, after writing path.md

- The sharpest sentence in path.md and the one to remember: **P1.3 + P2.3 together say the
  program's two halves are "cross the line" (C1, open) and "the wall itself" (C2 $\iff$ RH,
  given C1)** — so the Ihara program is a *coordinate change* on the Hilbert–Pólya problem, not
  a detour around it. This matches phase7's verdict for the trace level and now extends it to
  the determinant level. No surprise, but now it is a theorem-grade statement rather than a
  suspicion, and the graded corollary P2.4 is the actionable residue: partial gaps are exactly
  zero-free regions — provable rungs exist below the wall.
- Division of labour crystallised while writing P0: the place-cycle model owns the *arithmetic
  exactness* (determinant $=$ truncated Euler product, provable convergence for $\sigma > 1$,
  provable death at $\sigma = 1$); the bipartite divisor graph owns the *coupling freedom*
  (composites correlate small primes — the only non-vacuous coupling the dyadic sieve admits,
  per D1). Hypothesis H\* is the precise bet that coupling freedom buys strip convergence. All
  previous drafts conflated these two objects; separating them is what makes H\* falsifiable.
- H\*'s proof obligations (a)–(d) were chosen so each is independently checkable: (b) is a
  consistency check numerics can kill early; (d) — build the stages with an exact $s \mapsto
  1-s$ functional-equation symmetry — is a *design constraint*, and quite possibly the most
  fertile idea in the whole file: functional-equation symmetry at every finite stage would give
  Vitali the identification set for free and is a discrete analogue of the adelic Poisson
  summation. Worth a dedicated experiment (implementation I2.3).
- Noted while writing P4: the correct statement is "(ii)-with-positivity $\Rightarrow$ C2
  $\Rightarrow$ (with C1) RH", and the *converse-flavoured* claim "(ii) is RH-equivalent" must
  NOT be asserted — Meyer's nuclear realization shows the equivalence-shape without positivity;
  the equivalence with positivity is expected but unproven. Tag discipline held.
- The Siegel-zero/exceptional-eigenvalue dictionary (P3.2) plus Kotani–Sunada (P3.1) yields the
  clean falsifiable prediction for numerics: **all non-Perron real $u$-poles of the corrected
  weighted stages retreat toward the Ramanujan circle as $n$ grows; the Perron pole persists
  (it is the $s=1$ pole of $\zeta$).** If a second real pole persists, that is a "graph Siegel
  zero" and would be genuinely important to document either way. This is the kind of experiment
  the folder should have run instead of the unfolding.

### Dump 3 — 5 Jul 2026, after the first baseline run (implementation.md I8)

- The declared-criteria discipline paid off immediately: the very first gap census produced a
  *stronger-than-expected* signal ($g_n \log M_n$ growing), and the pre-registered rule routed
  it to "audit" instead of excitement. Diagnosis on inspection: Perron dominance of the
  rank-one $2^n(pq)^{-1-\beta}$ structure — scaling, not arithmetic. Had the old pipeline's
  habits persisted, this would have become a claim; under the new rules it became a
  calibration task. This is the cultural point of the whole review.
- The weighted pole census ($|u| \in [0.19, 4.18]$, 208 real poles at $n{=}7$) proves by
  demonstration that obligation W is the gate: without the weighted confinement theorem there
  is no locus against which "Ramanujan-ness" or "graph-Siegel" even means anything. W is
  elementary-looking (weighted Bass + quadratic formula reasoning) and is the correct next
  mathematical action, before any more numerics.
- Control column behaving exactly at the proven Euler-tail rate (ratio stable across $n$)
  means future anomalies are signal, not plumbing. Cheap to maintain, priceless to have.
- Honest summary of the day: the folder went from "a beautiful idea supported by broken
  evidence" to "a priced ladder: W → P3.5 → (with H\*) dlVP rung; H\*-d symmetry experiment;
  Q-γ1/2 structure probes; everything above priced at the wall by P2.3." Nothing moved on RH
  itself — nothing could have; P2.3 is the proof of *why* — but the program now knows exactly
  what it is doing and what each success would mean.
- Next session should start with: (1) obligation W symbolically at $n \le 6$; (2) the
  functional-equation sweep I2.3 (most fertile unknown); (3) graph-Siegel tracking only after
  W lands.

### Dump 4 — 5 Jul 2026, after implementing the lab and running everything ([findings.md](findings.md))

- The lab is real now ([prime_graph_lab.py](prime_graph_lab.py)), the three streamlit scripts
  are fixed (D1 corrected with regression asserts, D2 functions raise loudly, honest panels),
  and the prose artifacts carry correction notices with originals preserved — the folder is
  audit-clean per the [../flawed/](../flawed/) convention.
- Biggest single win: the **weighted Ihara–Bass identity discovered-by-testing** (F2) — the
  resolvent form validated to $10^{-15}$ on the actual stage graph, naive form refuted at
  $10^{-1}$. Obligation W went from "elementary-looking open lemma" to "numeric half banked,
  symbolic half routine." Everything spectral now routes through $\det M(u)$.
- Most instructive negative: the FE-asymmetry sweep (F6). One-sided $m^{-s}$ couplings
  *monotonically destroy* functional-equation symmetry — so H\*'s family must carry AFE
  symmetry by construction (Riemann–Siegel kernels). That single design law reshaped the new
  plan's G2 and feels like the folder's compass from here.
- Most satisfying confirmation: graph-Siegel tracking (F4) — detached spectrum is exactly
  4 eigenvalues at every stage, all accounted for by block structure (Perron ± mirror + one
  complex pair), zero arithmetic exceptions. The community-detection reading (detached NB
  eigenvalues count blocks) turns an RH-adjacent worry into a provable-looking combinatorial
  statement (plan G4).
- New micro-theorem (F8): the quantum-graph no-go — unitary mixing vs $\Lambda$-support is a
  genuine dichotomy (unique factorisation does the work). Proved in three lines, witnessed
  numerically, and it fences off an entire tempting model class while naming the three doors
  that remain (energy dependence / openness / interference). Candidate N5 for the repo's
  no-go catalogue.
- Everything still lands where P2.3 says it must: below the wall, rungs only. The plan's
  near-term theorems (G1 locus, G3 normalised gap ≈ 0.56, G4 anti-Siegel) are all
  independently meaningful even if H\* dies — that is the shape a healthy program should have.

### Dump 5 — 5 Jul 2026, pivot: the eigenvalue-level program gets its own folder

- New charter written: [../research-plan.md](../research-plan.md)
  — the eigenvalue$\to\pm\gamma$ program, split off so this folder keeps the determinant level
  (G1–G6) and `../adele/` keeps the trace level. Trigger: a parallel-session triage of
  [closed-form.md](closed-form.md)'s five frameworks — only #2 (Connes' $D$) and #5 ($H_n$)
  are eigenvalue-native with $\pm\gamma$ pairing; #3 (our Ihara determinant) is explicitly
  *not* (adjacency eigenvalues are not $\gamma$'s — consistent with F4's structural verdict).
- Design decisions recorded there: primary object is the **sieve-Galerkin compression**
  $H^G_n = P_n D P_n$ ($J$-invariant stages ⇒ exact $\pm$ pairing; basis = the sieve's
  prime-power inventory + a prolate-type archimedean window); the phase-3/4 refutations become
  gates (E0 density with zero fitted parameters; E4c shape-decoy control); pollution is
  handled by **second-order relative spectra** (certified, pollution-free enclosures — no
  norm-resolvent needed) plus the E4a trace-consistency test against the $10^{-36}$ anchor.
- Alternative routes noted, not taken now: full norm-resolvent windows (E3a — expected
  wall-adjacent); Krein-space reformulations (category change, Meyer detector applies).
- Still queued from the morning instruction: gate G1 (weighted locus theorem → `gate-1.md`),
  folder self-containment (`imports/` for `../adele/`, `../berry-keating/` references), and
  closed-form.md Part II. Recon done; the G1 proof skeleton (incidence/Schur argument for the
  resolvent-form identity; Herglotz per-edge partial fractions ⇒ annulus
  $\big|\,|z| - \sqrt{\langle d^{(2)}\rangle_\psi}\,\big| \le w_{\max}$ for non-real spectrum)
  is worked out and waiting to be written and verified.

### Dump 6 — 5 Jul 2026, evaluation: "greedy harmonic decomposition" proposal (rejected route)

- Proposal evaluated for [../research-plan.md](../research-plan.md):
  $\delta_n(\theta) = \Theta(\theta - \theta_n - \alpha_n)$, $\alpha_n = \pi/(n+2)$,
  $\theta_{n+1} = \theta_n + \delta_n\alpha_n$, claimed to give a monotone nested family
  $\mathcal S(\theta)$ with counting $(\theta/\pi)\ln N + O(1)$.
- **Refuted by execution** (`scratchpad/greedy_harmonic_check.py`): nesting fails at
  $\theta = \pi/2$ — $\mathcal S(\pi/2-\varepsilon) = \{1,5,41,1805,\dots\}$ vs
  $\mathcal S(\pi/2+\varepsilon) = \{0,\dots\}$, disjoint heads; and greedy residuals collapse
  quadratically ($r' < \pi/((n+1)(n+2))$ after selecting $n$), so selected indices square each
  step ⇒ counting is $O(\log\log N)$, not $x\ln N$ (measured: 1–3 elements up to $10^7$ vs
  claimed 5–15). The stated properties belong to a different object (a prescribed threshold
  family $\delta_n = \mathbf 1_{\theta\ge\theta_n^*}$), not to the greedy rule.
- Even repaired to the nested threshold version with count $x\ln N$: log-density sets are
  "single fake places" ($x\ln N \leftrightarrow \ln N/\ln p$, $p_{\mathrm{eff}} = e^{\pi/\theta}$)
  with Dirichlet-series abscissa $0$ — no pole at $s=1$, no critical-strip structure, no
  multiplicativity; fails gate E0's shape by two growth classes ($\log N$ vs $T\log T$) and a
  tunable continuous $\theta$ invites target-fitting (rule I0/D2). Principled home for
  "prescribed counting systems" is **Beurling generalized primes** (Diamond–Zhang), a different
  program. Marginal salvage: single-place log-lattice null model for E4c controls — already
  covered. **Not added to the plan.**
