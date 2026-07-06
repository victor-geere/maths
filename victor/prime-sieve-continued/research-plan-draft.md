# research-plan.md — prime-sieve-continued: mapping the sieve's eigenvalues to $\mathrm{Im}\,\rho = \pm\gamma$

*Charter of the continued program (5 Jul 2026). Inputs: (i) the five-framework triage of
[../prime-sieve/closed-form.md](prime-sieve/closed-form.md) performed in a parallel session,
recorded as a decision in §1; (ii) the proven/refuted record of [../adele/](adele/) Phases 1–7
and [../prime-sieve/findings.md](prime-sieve/findings.md) / [path.md](prime-sieve/path.md).
Tags per the repository [rigour convention](CLAUDE.md). **RH is open.** The terminal
identification "spectrum $=$ all zeros, on a Hilbert space" is RH-equivalent territory (Weil
positivity) and is priced as a **wall** throughout (gate E5) — never as a step. Every near-term
gate below is designed to have standalone value if the wall never falls.*

---

## 0. Objective, in its honest form

Build **sieve-computable finite self-adjoint matrices** $H_n$ whose eigenvalues converge —
*individually and certifiably*, not merely in distribution — to the imaginary parts
$\pm\gamma$ of the nontrivial zeros $\rho = \tfrac12 + i\gamma$.

Two classical normalisation facts fix what "map eigenvalues to $\mathrm{Im}(s)$" can mean, and
they are the reason the target is $\mathrm{Im}$ only:

**Lemma 0 (the critical line is the unitarity line — proven, classical).** On
$L^2(\mathbb{R}_+,dx)$ the dilation group $(U_t f)(x) = e^{t/2} f(e^t x)$ is unitary; its
generator is $D_\infty = -i\big(x\frac{d}{dx} + \tfrac12\big)$, essentially self-adjoint, and the
Mellin transform diagonalises it with spectrum $\mathbb{R}$. The $\tfrac12$ is exactly the
$L^2$-Plancherel line $\mathrm{Re}\,s = \tfrac12$. *Consequence:* any self-adjoint realization
sees only $\mathrm{Im}\,s$; $\mathrm{Re}\,\rho = \tfrac12$ is carried by the normalisation of the
construction, never produced as output. An eigenvalue program targets $\gamma$ and can target
nothing else.

**Pairing.** The functional equation induces a symmetry $J$ with $JDJ^{-1} = -D$ on the target
(§3.1), so the spectrum is symmetric about $0$: eigenvalues come in $\pm\gamma$ pairs. The finite
stages must carry the same symmetry **by construction** (gate E1), so that the pairing is a
stage-exact theorem, not an asymptotic hope.

**Charter sentence (adopted from the triage, §1):** use framework #5's finite matrices as the
working expression, framework #2's adelic operator $D$ as the target, and treat the convergence
claim as **the open problem it is** — with the convergence *mode* (K2 below) as the technical
crux.

---

## 1. The imported triage (decision record)

A parallel session triaged the five closed forms of
[closed-form.md](prime-sieve/closed-form.md). Verdict, adopted here:

| # | Framework | Zeros appear as | Eigenvalue-native, $\pm\gamma$-paired? | Role in this folder |
|---|---|---|---|---|
| 1 | Dirichlet series $F_n(s)$ | singularities of a generating function | no | stays in `prime-sieve/` (C1/determinant level) |
| 2 | Adèle class space: $D = -i(x\frac{d}{dx}+\tfrac12)$ at $\infty$, difference operators on Bruhat–Tits trees at finite places, on the spherical subspace of $L^2(\mathbb{A}_\mathbb{Q}/\mathbb{Q}^\times)$ | spectrum of a self-adjoint operator, symmetric about $0$ | **yes** | **target** |
| 3 | Ihara determinant $\det(1-uA)^{-1}$ | vanishing locus of a determinant | no — adjacency eigenvalues are *not* the $\gamma$'s | toolkit only (§3.2b) |
| 4 | Mellin/partial von Mangoldt $\Phi_n(s)$ | poles of a meromorphic continuation | no | evaluation-side only |
| 5 | Hilbert-space limit $H_n = D_n + \varepsilon_n A_n$ | matrix eigenvalues | **yes** — the only expression where *the sieve itself* has eigenvalues | **working expression — redesigned in §3.2** |

Two caveats from the same triage, adopted as **binding constraints** (both were independently
already in-repo as corrections M4/M5 — corroboration, not new input):

- **K1 (the wall).** In framework #2, "$\mathrm{spec}(D) = $ all zeros" is essentially
  **equivalent to RH** (via Weil positivity): identifying the eigenvalues with the *full* set
  $\{\pm\gamma\}$ is precisely the unproven step, not a settled fact. In-repo form: correction
  M4 ([closed-form.md](prime-sieve/closed-form.md) banner) — proven results are the
  semi-local trace formula (Connes 1999) and Meyer's (2005) unconditional realization on
  *nuclear non-Hilbert* spaces; positivity is the entire remaining content.
- **K2 (the mode).** **Strong resolvent convergence is too weak** for the intended conclusion:
  it guarantees every point of $\mathrm{spec}(D)$ is approached by eigenvalues of $H_n$
  (spectral *inclusion* — no zeros missed), but permits **spectral pollution** (spurious limit
  points). Norm-resolvent convergence, or extra compactness/positivity input, is required
  before "eigenvalues of $H_n \to$ exactly $\{\pm\gamma\}$" follows. In-repo form: correction
  M5; [path.md](prime-sieve/path.md) P4 (Reed–Simon VIII.7).

---

## 2. The in-repo record this plan is bound by

| Statement | Status | Where |
|---|---|---|
| The composite-generator sieve enumerates every prime (= finite place) stage by stage | **proven** | [../adele/phase1.md](adele/phase1.md) Lemma 1 |
| Def 4.1's $H_n$ is vacuous ($A \equiv 0$); corrected to $H_n' = D_n' + \varepsilon_n A'$, $\varepsilon_n = c/\lVert A'\rVert$ | **proven / corrected** | [../adele/phase3.md](adele/phase3.md) Prop 3.1, Def 3.2 |
| Eigenvalue$\to$zero at the $\{\log p\}$ scaling is impossible: counting $N_A(T) \sim e^T/T$ vs $N(T) \sim \frac{T}{2\pi}\log\frac{T}{2\pi}$; no affine rescaling repairs it | **refuted** (Thm 3.3) | [../adele/phase3.md](adele/phase3.md) §3.4; empirically [../adele/phase4.md](adele/phase4.md) §4.3 |
| Weak/statistical spectral convergence $\ne$ Hilbert–Pólya (density match is necessary, nowhere near sufficient) | **binding logical note** | [../adele/phase4.md](adele/phase4.md) §4.2 |
| Sieve-truncated **trace** converges to the arithmetic side at proven rate $M_n^{-\varepsilon}$; adelic place-by-place balance verified to $10^{-36}$ | **proven + verified** | [../adele/phase4.md](adele/phase4.md) Thm 4.1/4.2; [../adele/phase6.md](adele/phase6.md); [../adele/adele_trace.py](adele/adele_trace.py) |
| Meyer 2005: unconditional realization of *all* zeros on nuclear non-Hilbert spaces — positivity is the whole content; any positivity-free "success" has silently changed category | **proven neighbour / detector** | [path.md](prime-sieve/path.md) P4 |
| Connes–Moscovici 2022 prolate operator: proven semiclassical **counting** match to $N(T)$; exact spectral identification open | **proven neighbour** | [path.md](prime-sieve/path.md) P4 |
| Graph/divisor-operator spectra are block-structural, not arithmetic (exactly 4 detached at every stage); no graph-Siegel exceptionals at $\beta = \tfrac12$ | **measured** | [../prime-sieve/findings.md](prime-sieve/findings.md) F4 |
| No closed quantum graph with $s$-independent unitary scattering matches the von Mangoldt support termwise | **proven no-go** | [../prime-sieve/findings.md](prime-sieve/findings.md) F8 |
| Rank-unfolding against the target's counting function fabricates agreement (defect D2); evidence rules I0 | **binding** | [../prime-sieve/implementation.md](prime-sieve/implementation.md) I0; notes §2.2 |

The two refutations in rows 3–4 are not history; they are **gates E0 and E4's design** (§5): the
continued program institutionalises them as regression tests that every new candidate must face.

---

## 3. Corrected working objects

### 3.1 The target $D$ (framework #2), stated with its honest spectral status

$D$ acts on the spherical subspace of $L^2(\mathbb{A}_\mathbb{Q}/\mathbb{Q}^\times)$: at the
archimedean place as $-i(x\frac{d}{dx}+\tfrac12)$ (Lemma 0), at each finite place as the scaling
difference operator on the Bruhat–Tits tree. What is *proven* about its spectrum on which space
is exactly the M4 correction: the semi-local trace formula is proven; on the Hilbert-space
ambient the statement "spectrum $=$ zeros" is the RH-equivalent endpoint (K1); on Meyer's
nuclear ambient all zeros are realized unconditionally but the Hilbert/positivity structure —
the part that would make self-adjointness bite — is given up. **Task E2a below therefore begins
by fixing the ambient space and recording, with tags, what is known about
$\mathrm{spec}(D)$ there.** No step of this plan may quietly assume the answer.

The $\pm\gamma$ pairing lives here: $D$ is self-adjoint and the functional-equation symmetry
$J$ (composition of the adelic Fourier transform with inversion, the unitary implementing
$s \leftrightarrow 1-s$) satisfies $JDJ^{-1} = -D$, so $\mathrm{spec}(D) = -\mathrm{spec}(D)$.

### 3.2 The working family $H_n$ — three candidates, one primary

**(a) Legacy comparator: $H_n' = D_n' + \varepsilon_n A'$** ([phase3](adele/phase3.md)
Def 3.2, $\varepsilon_n = c/\lVert A'\rVert$). Non-vacuous, self-adjoint, and **dead as an
eigenvalue map at its own scaling** (Thm 3.3). Role: negative control — it must *fail* gate E0,
reproducing the refutation as a regression test.

**(b) Graph/divisor operators** (the [../prime-sieve/](prime-sieve/) lab). The bipartite
divisor graph gives *exact* $\pm\lambda$-paired spectra at every stage (chiral symmetry — the
finite avatar of the $\pm\gamma$ pairing), a stable normalised gap $\approx 0.56$ (F3), and the
weighted Ihara–Bass machinery (F2). Per triage row #3 and finding F4, its eigenvalues are
divisor-structural, **not** approximants of $\gamma$. Role: toolkit — the pairing mechanism for
E1, gap/locus technology, pollution diagnostics. Not the map.

**(c) Primary: the sieve-Galerkin compression $H^G_n = P_n\,D\,P_n$.** Compress the *target
itself* along the sieve's own filtration:

- **Finite places.** Stage $n$ admits exactly the places $p \le M_n$ (proven, Phase 1), each
  with local levels $k \le K_n(p) = \lfloor \log M_n / \log p \rfloor$ — i.e. the basis of local
  scaling levels is **the sieve's prime-power inventory $\{p^k \le M_n\}$**, the *same*
  truncation whose trace error is already proven $O(M_n^{-\varepsilon})$
  ([phase4](adele/phase4.md) Thm 4.2).
- **Archimedean place.** A dilation-adapted window (log-variable cutoff $|\log x| \le L_n$ with
  a band-limit dual cutoff — prolate/time-band-limiting structure, the Connes–Moscovici fiber),
  with Mellin–Hermite basis functions whose matrix elements are exact integrals.
- **Symmetry.** $V_n = \mathrm{ran}\,P_n$ is chosen $J$-invariant, so $J H^G_n J^{-1} = -H^G_n$
  **exactly at every stage** (gate E1 is a construction, not a limit).

Matrix elements of $D$ (and of $D^2$, needed by E3b) are explicit: geometric sums at finite
places, Gaussian/Mellin integrals at $\infty$ — all `mpmath`-computable at the same
`dps=35` used by [adele_trace.py](adele/adele_trace.py).

*Why compression is the right redesign:* eigenvalues of compressions of a self-adjoint operator
are governed by min–max; the entire difficulty becomes the behaviour of $P_n \uparrow I$ —
which is precisely where the honest obstruction (K2: pollution) lives. The naive $H_n$ hid that
obstruction inside an ad-hoc coupling; $H^G_n$ exposes it to the correct theory.

### 3.3 The density design law (repairing obstruction O1 *by design*)

Thm 3.3 kills any candidate whose intrinsic eigenvalue count has the wrong shape. Write the
zero-counting function as smooth part plus fluctuation, $N(T) = \frac{T}{2\pi}\log\frac{T}{2\pi}
- \frac{T}{2\pi} + \tfrac78 + S(T) + \cdots$. The design law:

- **E0a (smooth part — archimedean, attainable).** The $T\log T$ shape is a *two-cutoff
  dilation* phenomenon (Berry–Keating regularisation; proven for the prolate operator's
  counting, CM 2022). The archimedean window of §3.2(c) is chosen exactly so the stage Weyl law,
  **derived from the operator with zero fitted parameters**, has the
  $\frac{T}{2\pi}\log\frac{T}{2\pi}$ shape on the stage window $T \le T_n$.
- **E0b (fluctuation part — arithmetic, the open content).** The finite places must supply the
  $S(T)$-type fluctuations *without* disturbing the smooth law — measurable against fixed
  smooth test functions (unfolding-free); its full pointwise version is wall-adjacent and is
  **not** assumed.
- **Bookkeeping.** $\dim V_n = \#\{p^k \le M_n\} + O(L_n^2)$-archimedean; the spectral
  resolution of a log-window of length $2L_n$ is $\Delta\gamma \sim \pi/L_n$, so the derived
  stage window $T_n = T(M_n)$ must satisfy
  $\frac{T_n}{2\pi}\log\frac{T_n}{2\pi} \lesssim \dim V_n$ — a computation, part of E0's
  deliverable, **never** a fit to $N(T)$.

---

## 4. Obstruction ledger

| # | Obstruction | Source | Answered by |
|---|---|---|---|
| O1 | density mismatch (already killed one candidate) | Thm 3.3, phase4 §4.3 | gate E0 (+ §3.3 design law) |
| O2 | $\pm\gamma$ pairing must be structural, not asymptotic | Lemma 0 / §3.1 | gate E1 |
| O3 | convergence mode: strong-resolvent $\Rightarrow$ inclusion only; pollution possible | K2 / M5 / path P4 | gates E2, E3 |
| O4 | completeness ("no extra spectrum, none missing") $\Leftrightarrow$ RH via positivity; Krein risk: stagewise self-adjointness does not give a positive limit pairing | K1 / path P4 | gate E5 — **priced, not attacked** |
| O5 | evidence hygiene: target-consuming normalisation fabricates agreement | D2 / I0 | harness rules in E4 |
| O6 | the **shape decoy**: matching the smooth $T\log T$ law is *not* evidence of matching zeros (any two-cutoff dilation model does it) | CM/BK calibration; the `flawed/` series | E4c controls |

---

## 5. Gates

### E0 — the density gate (first kill, cheapest)

*Task.* Derive the intrinsic Weyl law of $H^G_n$ (E0a) and verify it numerically with **zero
fitted parameters**; run the same gate on the negative controls.
*Pass:* intrinsic $N_n(T) / \big(\frac{T}{2\pi}\log\frac{T}{2\pi}\big) \to 1$ on derived windows
$T \le T_n$, coefficients derived, not fitted. *Fail:* candidate dies, recorded, per the
phase-4 precedent.
*Pre-registered expectations:* legacy $H_n'$ **must fail** (Thm 3.3 regression); graph one-mode
**must fail** (F4: structural spectra); $H^G_n$ is the live question.
*Tag target:* proven (it is a computation about a finite explicit operator family).

### E1 — the pairing lemma (days, by construction)

*Task.* Prove: $V_n$ $J$-invariant $\Rightarrow$ $\mathrm{spec}(H^G_n) = -\mathrm{spec}(H^G_n)$
with paired eigenvectors — the stage-exact $\pm\gamma$ avatar. One page; the bipartite/chiral
mechanism of §3.2(b) is the model.
*Tag target:* proven.

### E2 — spectral inclusion (the unconditional convergence theorem)

- **E2a.** Fix the ambient space rigorously (Hilbert $L^2(X)$-with-regularisation vs Meyer
  nuclear) and record with tags what is proven about $\mathrm{spec}(D)$ there — the M4
  correction done properly, once, so no later step can equivocate.
- **E2b.** Prove $P_n \to I$ strongly on an explicit core of $D$ (Schwartz-type spherical
  vectors), hence $H^G_n \to D$ in the **strong resolvent** sense, hence **spectral inclusion**:
  every point of $\mathrm{spec}(D)$ is a limit of stage eigenvalues — *no zero is missed*.
  (Named-theorem route: Reed–Simon VIII; Weidmann's compression conditions.)

*Honest payoff statement:* E2 alone can never certify an eigenvalue *is* near a zero (K2); it
certifies none are missing. *Tag target:* proven.

### E3 — pollution control (the crux; three sub-routes)

- **E3a (norm-resolvent on windows — deep, open).** Compact/trace-class resolvent differences +
  Krein spectral-shift control $\Rightarrow$ local Hausdorff convergence of spectra
  (pollution-free) on energy windows. This is hurdle (ii) of the old program made precise. Per
  path.md P4: **if achieved with a positive limit pairing it closes onto the wall** (real
  spectrum $\Rightarrow$ C2 $\Rightarrow$ RH by P2.3) — so full-strength E3a is expected
  RH-equivalent-or-harder. Work it only for partial windows; price it openly.
- **E3b (certified enclosures — the tractable core of this folder).** **Second-order relative
  spectra** (Shargorodsky; Levitin–Shargorodsky 2004; Boulton–Levitin; Davies–Plum): from the
  pencil built of $P_nDP_n$ and $P_nD^2P_n$, every pencil root $z$ **certifies**
  $\mathrm{spec}(D) \cap [\mathrm{Re}\,z - |\mathrm{Im}\,z|,\ \mathrm{Re}\,z + |\mathrm{Im}\,z|]
  \ne \emptyset$ — pollution-free *by theorem*, no norm-resolvent needed. Deliverable: certified
  intervals around stage eigenvalues, with radii $|\mathrm{Im}\,z|$ decreasing in $n$ at a
  measured rate. *Cross-science note:* this technology was built to kill spectral pollution in
  relativistic quantum chemistry — spurious states of compressed **Dirac operators**; we reuse
  it on the adelic Dirac. *Tag target:* proven (the enclosure theorem is classical; our part is
  computing $D^2$ elements).
- **E3c (positivity input).** Naming it is gate E5. Not a work item.

### E4 — the evaluation harness (pre-registered, D2-safe)

- **E4a — trace-consistency gate (the strongest test; target already verified in-repo).**
  $\sum_{\lambda \in \mathrm{spec}(H^G_n)} g_t(\lambda)$ must converge, within the proven
  $O(M_n^{-\varepsilon})$ envelope, to the place-by-place values already verified to $10^{-36}$
  ([phase6](adele/phase6.md); Gaussian pair $h,g$ of `adele_trace.py`). Persistent excess
  $=$ **quantified pollution mass**; deficit $=$ quantified spectral loss. Uses only in-repo
  verified numbers; consumes no new target data.
- **E4b — matched displacement (evaluation only).** On the fixed window $[0, 50]$ (first ten
  $\gamma_k$), median $|\lambda_k - \gamma_k|$ under optimal matching; success $=$ decreasing in
  $n$ at a measured rate. The $\gamma$ list is used **only here, only as final evaluation** —
  never in construction, scaling, or normalisation (rule I0/D2).
- **E4c — controls.** *Positive:* compression of a model with known point spectrum (harmonic
  oscillator) — validates the pipeline. *Decoy:* the bare archimedean prolate/xp compression —
  **must pass E0's shape and must fail E4b**; this is the anti-O6 test that the harness cannot
  be fooled by the smooth Weyl law (the exact false positive that seduced the `flawed/`
  series). *Negatives:* legacy $H_n'$, graph one-mode (must fail E0).

### E5 — the wall, priced (not a work item)

Completeness — "$\mathrm{spec} = \{\pm\gamma\}$, nothing extra, nothing missing, on a genuine
Hilbert space" — is equivalent to RH (Weil positivity; Connes' global trace formula; path.md
P2.3/P4). Meyer 2005 is the standing category-change detector: a realization without positivity
is *unconditional and already exists*, so any claimed success must state where its positivity
comes from. **Unconditional ceiling of this folder, stated in advance:** (i) a certified sublist
of true $\mathrm{spec}(D)$ points (E3b), (ii) no-missing-spectrum inclusion (E2), (iii)
trace-consistency at the proven rate (E4a). All three together still do **not** decide RH, and
per [CLAUDE.md](CLAUDE.md) may never be presented as approaching it.

---

## 6. Numerical program (staged, all pre-registered)

| Step | Content | Depends on |
|---|---|---|
| N0 | Stage builder: $J$-invariant basis; matrix elements of $D$ and $D^2$ (`mpmath`, `dps=35`); sizes $\dim V_n \sim \#\{p^k \le M_n\} + O(L_n^2)$, a few $\times 10^3$ at $n \le 14$ | §3.2(c) |
| N1 | E0 density runs on $H^G_n$ + all controls; publish pass/fail against the pre-registered criteria verbatim | N0 |
| N2 | E4a trace-consistency against the phase-6 numbers; first E3b enclosures at small $n$ | N0 |
| N3 | E4b displacement metric; `findings-2.md` in the style of [../prime-sieve/findings.md](prime-sieve/findings.md), every claim tagged | N1, N2 |

Pre-registered success/failure criteria (fixed now, before any run): E0 pass/fail as in §5;
E4a residual within $C\,M_n^{-1/2}$ envelope with $C$ derived from prime-side.md Prop 6.1;
E4b median displacement monotone decreasing over at least three consecutive stages; any
outcome — including total failure of $H^G_n$ at E0 — is a reportable finding.

---

## 7. Ordering, dependencies, effort

```
E1 (pairing lemma, days)
   └─→ E0 (density gate; first kill) ──→ E2a/E2b (inclusion theorem)
                                            ├─→ E3b (certified enclosures)  ── tractable core
                                            │        └─→ E4 (harness: E4a → E4b, with E4c controls)
                                            └─→ E3a (norm-resolvent windows) ── deep/open
E5: wall — priced only, consulted at every writeup.
```

Priority: **E1 → E0 → E2 → E3b/E4 → (E3a only after the cheap gates have spoken).** The
near-term deliverables with standalone value regardless of the wall: the E1 lemma, the E0
density law, the E2 inclusion theorem, and E3b's certified intervals.

---

## 8. Do-not list (binding)

- **No unfolding, fitting, or calibration against $N(T)$ or the $\gamma$ list** (D2/I0). E0
  runs with zero fitted parameters; $\gamma$'s appear only inside E4b as final evaluation.
- **No statistical claims as Hilbert–Pólya progress** — density/ensemble agreement is necessary,
  nowhere near sufficient ([phase4](adele/phase4.md) §4.2).
- **No spectral conclusions from strong-resolvent convergence alone** (K2/M5): inclusion may be
  claimed, exactness may not.
- **No eigenvalue programs at the $\{\log p\}$ density** — closed by Thm 3.3.
- **No silent category change**: if a construction's positivity evaporates (Krein/indefinite
  limit pairing), say so and re-tag — Meyer is the calibration, path.md P4 the detector.
- **No presenting gate progress as "approaching RH"** (E5; [CLAUDE.md](CLAUDE.md):
  RH-equivalent restatements are walls; the declaration bar is the full proven chain plus
  adversarial, symbolic, and numerical verification).
- Inherited closed routes: naive stage lifts (F7), closed $s$-independent-unitary quantum-graph
  matching (F8), rank-unfolding (D2).

---

## 9. Contract with the source folders

**Imports** (this folder builds on, and must not re-derive): phase-1 sieve completeness; the
phase-3/4 corrections and refutations; the phase-6 trace anchor ($10^{-36}$) as E4a's target;
`prime-sieve/` evidence rules I0, findings F2–F9, and path.md's P2.3/P4 pricing.
**Exports:** any gate that lands **proven** is reflected upstream in
[../adele/index.md](adele/index.md)'s status tables per repo convention.
**Division of labour:** trace level lives in `adele/` (done), determinant level in
`prime-sieve/` (gates G1–G6), **eigenvalue level here** — triage row #5 aimed at row #2.

| Gate | Current tag |
|---|---|
| E0 density law | **open** (design law stated; computation pending) |
| E1 pairing lemma | **open** (proof expected routine) |
| E2 inclusion theorem | **open** (unconditional target) |
| E3a norm-resolvent windows | **open**; full strength expected RH-equivalent-or-harder |
| E3b certified enclosures | **open** (enclosure theorem classical — proven; our instantiation pending) |
| E4 harness | **open** (targets: in-repo verified values) |
| E5 completeness | **RH-equivalent** — wall (Weil positivity); not a task |
| RH | **open** |
