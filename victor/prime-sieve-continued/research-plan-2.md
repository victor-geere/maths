# research-plan-2.md — consolidated open problems, unification, and new conjectures

*Second-generation plan for `prime-sieve-continued/` (6 Jul 2026). Built **only** from the files
in this folder. Supersedes nothing: [research-plan-draft.md](research-plan-draft.md) (the E-gate
charter) and [prime-sieve/new-research-plan.md](prime-sieve/new-research-plan.md) (the G-gate
plan) remain the operative task lists at their levels; this document (i) inventories **every**
open problem and conjecture across the folder in one place, (ii) triages them into *tractable* /
*hard-but-valid* / *wall* / *dead end*, (iii) states the unifying picture that relates the
folder's concepts, and (iv) extracts and prices **new conjectures** from the prime sieve together
with [harmonic_sine_to_xi_sweep.html](harmonic_sine_to_xi_sweep.html) /
[sine-harmonic.html](sine-harmonic.html). Tags per the folder
[rigour convention](CLAUDE.md). **RH is open.** Nothing below is, or may be presented as,
progress toward RH beyond its tag.*

---

## 1. The unified picture: one object, four levels, and a model pair

Everything in this folder is an attack on a single identity at increasing strength. Write the
zero ordinates as $\pm t_k$ ($t_k = \mathrm{Im}\,\rho_k$) and the sieve's prime-power inventory
as $\{p^k \le M_n\}$.

| Level | Object | Statement | Status in folder |
|---|---|---|---|
| **L1 trace** (linear in a test function $g$) | place-by-place Weil trace $W_\infty(g) - \sum_p W_p(g)$ | explicit formula as a distributional identity | **proven + verified to $10^{-36}$** ([adele/phase6.md](adele/phase6.md), [adele/adele_trace.py](adele/adele_trace.py)); rate $O(M_n^{-1/2})$ proven |
| **L2 character** (fixed $s$) | flow character $\chi_W(z) = -\frac{\zeta'}{\zeta}(\tfrac12 - iz)$ as a trace of sieve data | log-derivative of the determinant; poles at the zeros, reached only by continuation | **proven** ([berry-keating/prime-side.md](berry-keating/prime-side.md) Thm 5.3; circularity of "bridge + Weil" proven, [adele/phase7.md](adele/phase7.md) Obs 7.1) |
| **L3 determinant** (uniform in $s$) | stage determinants $D_n(s) \to e(s)\,\xi(s)$ locally uniformly on the strip (statement C1) | Hadamard-product-level identity | **open** — conjecture H\* ([prime-sieve/path.md](prime-sieve/path.md) P1); given C1, C2 $\iff$ RH (P2.3, **proven**, the wall) |
| **L4 eigenvalue** (the zero set itself) | $\mathrm{spec}(H^G_n) \to \{\pm t_k\}$, individually certified | Hilbert–Pólya | **open** — the E-gates ([research-plan-draft.md](research-plan-draft.md)); completeness (E5) is **RH-equivalent** |

Each level is strictly stronger than the one above it, and the ladder is bridged by proven
identities: $\log\det(I - T_n(s)) = -\sum_k \frac1k \mathrm{Tr}\,T_n(s)^k$ connects L1→L3
(path.md P5), and Hurwitz/Rouché connects L3→L4 zero-locations (P2.1–P2.2). The wall appears at
the *same* height in every coordinate system — Weil positivity (L1), real poles of $\chi_W$
(L2), C2 (L3), completeness-with-positivity (L4) — all **proven equivalent to RH** and none of
them a step toward it. That invariance is itself a theorem-grade finding of this folder
(path.md P2.3, phase7 §7.5, research-findings §7): **the program is a coordinate change on
Hilbert–Pólya, not a detour around it.** The actionable residue is the graded ladder *below*
the wall (P2.4: partial gap bounds $\iff$ zero-free regions; E2/E3b: inclusion + certified
enclosures).

### 1.1 The model pair (what the harmonic-sine documents add)

[sine-harmonic.html](sine-harmonic.html) and
[harmonic_sine_to_xi_sweep.html](harmonic_sine_to_xi_sweep.html) install a **calibration pair**
alongside the arithmetic object:

$$\frac{\sin(\pi t)}{\pi t} = \prod_{n\ge1}\Big(1 - \frac{t^2}{n^2}\Big)
\qquad\longleftrightarrow\qquad
\Xi(t) = \Xi(0)\prod_{k\ge1}\Big(1 - \frac{t^2}{t_k^2}\Big),$$

both entire of order 1, both **even** (paired zeros $\pm$), both with genus-1 exponential
convergence factors cancelling *exactly because* the zeros are paired (sweep doc §7). The sine
side is the model where everything the arithmetic side wants is **already true and elementary**:

- the zero set is known ($\mathbb{Z}$), real, simple, with **linear** counting $N(T) \sim T$;
- the log-expansion encodes a zeta family:
  $\log\frac{\sin \pi z}{\pi z} = -\sum_{m\ge1}\frac{\zeta(2m)}{m}z^{2m}$ (sweep doc §4);
- there is a finite, exact, stage-by-stage *sieve-like construction*: the greedy
  Egyptian-fraction (Fibonacci–Sylvester) expansion, terminating on rationals, converging
  doubly exponentially ($r_k < 2^{-2^{k-1}}$, proven in sine-harmonic.html §4), built from
  nothing but ceiling divisions and Pythagoras.

The structural dictionary — each row's left column **proven** on the sine side, right column
the arithmetic analogue with its honest tag:

| sine side (proven, elementary) | arithmetic side (tag) |
|---|---|
| zeros at $\mathbb{Z}$; $N(T) \sim T$ | zeros at $\pm t_k$; $N(T) \sim \frac{T}{2\pi}\log\frac{T}{2\pi}$ (**proven**, RvM) |
| evenness of $\sin(\pi t)/\pi t$ = pairing $\pm n$ | $J$-symmetry $JDJ^{-1} = -D$; gate E1; bipartite chiral pairing F3 (**proven mechanisms**) |
| genus-1 factors cancel in paired product (§7) | design law C-2 / F6: functional-equation symmetry must be built in, not approximated (**verified negative** for one-sided kernels) |
| $\log$-expansion coefficients $= \zeta(2m)$ | $\log$-expansion coefficients $= \sigma(2m) = \sum_k t_k^{-2m}$, Voros' secondary zeta at even integers (**proven** identity; see conjecture HS2) |
| greedy Egyptian stages: finite, exact, doubly-exponential | sieve stages: finite, exact enumeration of places (**proven**, phase1 Lemma 1), trace rate $O(M_n^{-1/2})$ (**proven**) |
| Weierstrass sweep §9: zeros movable one pair at a time | **target-consuming** as evidence — see dead end X8 below |

**What the model pair is for.** Not a proof device — a *harness* device. It supplies (i) the
canonical positive control and the canonical **decoy** for every evaluation gate (the sine
product passes every "shape" test and must fail every "arithmetic" test — exactly the anti-O6
role of E4c), and (ii) two genuinely new, D2-safe observables (HS1, HS2 below) that connect the
eigenvalue level L4 to the determinant level L3 *without consuming the $\gamma$-list*.

---

## 2. Complete inventory of open problems

Every open item in the folder, deduplicated, with source and triage. Tags: **T** = tractable
now (proof or computation with a clear method), **H** = hard but valid (open research, below
the wall), **W** = wall (RH-equivalent; priced, never worked as a step), **D** = dead end
(closed by proof or refutation; binding).

### 2.1 Tractable open problems (T)

| # | Problem | Source | Method / first action |
|---|---|---|---|
| T1 | **E1 pairing lemma**: $V_n$ $J$-invariant $\Rightarrow$ $\mathrm{spec}(H^G_n) = -\mathrm{spec}(H^G_n)$ with paired eigenvectors | [research-plan-draft.md](research-plan-draft.md) §5 | one page; chiral/bipartite mechanism of F3 is the model. Days. |
| T2 | **E0 density gate**: derive the intrinsic Weyl law of $H^G_n$, zero fitted parameters; run negative controls (legacy $H_n'$ must fail; graph one-mode must fail) | draft §5, §3.3 | computation on an explicit finite family; pre-registered pass/fail criteria already written |
| T3 | **E2a/E2b inclusion**: fix the ambient space with tags (M4 done properly, once); prove $P_n \to I$ strongly on a core $\Rightarrow$ strong-resolvent convergence $\Rightarrow$ spectral inclusion (no zero missed) | draft §5 | Reed–Simon VIII, Weidmann compression conditions; unconditional |
| T4 | **E3b certified enclosures**: second-order relative spectra from the pencil $(P_nDP_n, P_nD^2P_n)$ — pollution-free intervals by classical theorem | draft §5 | compute $D^2$ matrix elements (`mpmath`, dps 35); enclosure theorem is classical (Shargorodsky, Levitin–Shargorodsky, Davies–Plum) |
| T5 | **E4 harness**: E4a trace-consistency against the $10^{-36}$ anchor; E4b displacement on $[0,50]$ (evaluation only); E4c controls incl. the prolate decoy | draft §5–6 | targets are in-repo verified numbers; extend with HS1/HS2/HS6 below |
| T6 | **G1 weighted locus theorem** — the identity $\det(I-uB_w) = \prod_e(1-u^2w_e^2)\det M(u)$ plus an honest confinement locus for non-real zeros | [prime-sieve/new-research-plan.md](prime-sieve/new-research-plan.md); numeric half banked at $10^{-15}$ (F2) | **the previous written attempt is quarantined in [flawed/gate-1.md](flawed/gate-1.md)** — see D-item X10. The Schur-complement identity proof there is likely salvageable; the locus theorem's upper bound and the "Asano compatibility" theorem are not. Re-derive from scratch; verify with sympy at $n \le 6$. |
| T7 | **G3 normalised-gap census + theorem**: $g_{\mathrm{sym}}(n) \ge c > 0$ uniformly (measured stable $\approx 0.56$, F3) | new-research-plan G3 | run the census to $n \le 14$ *first* (cheap falsifier), then Brun–Titchmarsh + large-sieve proof attempt; independently publishable regardless of the zeta connection — **update 7 Jul 2026: base theorem proven** in the extracted project (census flat $\approx 0.566$ to $n=15$; uniform gap via elementary hub minorization, explicit $c$; sharp constant + α/β rungs still open; `victor/research/findings/PSC2-F04-normalised-gap.md`) |
| T8 | **G4 anti-Siegel block-purity**: detached spectrum of $B_w$ = structural part exactly (measured: exactly 4 at every stage, F4); sweep $\beta \in [0.3,0.7]$ | new-research-plan G4 | community-detection technology (Krzakala et al.); shares divisor-count concentration input with T7. Needs G1's locus first. — **update 7 Jul 2026: executed in the extracted project, falsifier branch** — the β-sweep refuted the count ("exactly 4" is a window artifact of $n \le 10$, $\beta \ge 0.4$; the detached set is a growing hierarchy of imaginary pairs); the real-detached census is exactly the Perron pair at every sweep point, and an **edge-purity theorem is proven** for all $n \ge 4$, all β (`victor/research/findings/PSC2-F05-anti-siegel.md`) |
| T9 | **Truncation-rate bound**: state and test the $O(M_n^{-1/2})$ bound as a standalone proposition with constants | [adele/index.md](adele/index.md) open items | already implicit in phase6 §6.3c; make it a tagged proposition with a regression test |
| T10 | **Restricted-support Weil positivity**: $\mathrm{supp}\,g \subseteq (-\tfrac12\log2, \tfrac12\log2)$ — prime terms vanish; archimedean case proven in literature (Yoshida; Connes–Consani) | [berry-keating/research-findings.md](berry-keating/research-findings.md) §7.2, §9.1 | each support-widening instance is self-contained provable/refutable; first new instance: place set $\{\infty, 2\}$ (§9.5) |
| T11 | **Li coefficients, finite ranges**: unconditional computation/asymptotics of $\lambda_n$; positivity for finite ranges is provable and cumulative | research-findings §9.3 | connects to conjecture HS2 below (both are zero-power-sum families) |
| T12 | **HS1 / HS2 / HS6 gates** (new, this plan) | §4 below | pre-registered; all targets computable without the $\gamma$-list |

### 2.2 Hard but valid open problems (H)

| # | Problem | Source | Honest pricing |
|---|---|---|---|
| H1 | **H\*** — sieve-computable coupled stage determinants satisfying C1 on the open strip | path.md P1; the folder's real L3 conjecture | falsifiable via obligations (a)–(d); the V2 (AFE-symmetric) family of G2 is the live candidate after V1's elimination (F5/F6). If no V2 member beats baseline, demote and refocus on trace-ladder payoffs. |
| H2 | **G2 / H\*-d functional-equation design**: stages with exact $s \leftrightarrow 1-s$ symmetry | new-research-plan G2; notes.md Dump 2 calls it "possibly the most fertile idea in the file" | strengthened by HS5 below (pairing = evenness in $t$); gate criterion pre-registered (FE asymmetry decreasing in $n$) |
| H3 | **P3.5 / route α**: weighted non-backtracking gap $\ge c/\log M_n$ from sieve inequalities → dlVP-strength zero-free region via P2.4 (needs C1) | path.md P3.3 | proof inputs identified (Brun–Titchmarsh, Montgomery large sieve, phase1 Lemma 2); the $1/\log$ calibration match is a good sign *and* a ceiling warning (cannot exceed dlVP without new input) |
| H4 | **Route β**: Bordenave's tangle-free trace method with the sieve's equidistribution replacing randomness | path.md P3.3 | independent engine for the same dlVP rung; a useful cross-check, not extra strength |
| H5 | **G6 / Q-γ2 Asano gluing**: does the sieve step act on stage polynomials $\prod_e(1-u^2w_e^2)\det M(u)$ as a locus-preserving Asano/Schur–Szegő composition? | path.md route γ; new-research-plan G6 | machine-checkable at $n \le 6$; falsifier: no identifiable structure ⇒ close route γ entirely. The gate-1.md "proof" of this is void (X10). |
| H6 | **G5 escape routes from the F8 no-go**: energy-dependent $\Sigma(s)$ / open-resonance systems / pseudo-orbit interference budget | new-research-plan G5 | exploratory tier; each has a small first experiment; the inner-function question in G5.1 is Hermite–Biehler-shaped and will terminate at the wall if it succeeds — price it so |
| H7 | **E3a norm-resolvent on windows**: compact/trace-class resolvent differences + Krein shift control on energy windows | draft §5 | full strength expected RH-equivalent-or-harder (closes onto the wall via P2.3); work only partial windows, only after cheap gates |
| H8 | **BS-convergence of unbounded-degree stages**: weighted/rescaled Benjamini–Schramm setup for $B_n$ (vertex 2 has degree $\sim 2^{n-1}$) | path.md P4(c) | prerequisite for any measure-level spectral statement about the graph stages |
| H9 | **Rigorous adelic/quaternionic operator definition** (the E2a ambient, done to publication standard) | adele/index.md open items; draft E2a | overlaps T3; the hard part is the finite-place domain bookkeeping |
| H10 | **Sonine/Burnol de Branges spaces**: extend known structure results | research-findings §9.2 | genuine mathematics with no false step required; long horizon |

### 2.3 Walls (W) — RH-equivalent; consulted, never worked as steps

| # | Wall | Where proven equivalent |
|---|---|---|
| W1 | E5 completeness: $\mathrm{spec} = \{\pm t_k\}$, nothing extra/missing, on a genuine Hilbert space | Weil positivity; draft §5 E5; phase7 §7.5 |
| W2 | C2 at full uniform strength, given C1 | path.md P2.3 (**proven** equivalence) |
| W3 | Route γ at full Ramanujan strength, with C1 | P2.3 corollary; MSS reality-of-roots = Hermite–Biehler in polynomial coordinates |
| W4 | Hurdle (ii) with a positive limit pairing (norm-resolvent + positivity) | path.md P4; Meyer 2005 is the category-change detector |
| W5 | HB structure function with $A$-part $= \Xi$; $K_h \succeq 0$ for all $h > 0$ | research-findings §6.2, Thm 7.1 (**proven** equivalence, full proof in-folder) |
| W6 | Weil positivity itself; Li positivity for all $n$; Connes global trace formula | research-findings §7.2–7.3 |

Calibration constants for every wall: **Meyer 2005** (unconditional realization of all zeros
exists on nuclear non-Hilbert spaces — positivity is the *entire* remaining content; any
"success" without positivity has silently changed category) and **Connes–Moscovici 2022**
(proven semiclassical counting match; exact identification open).

---

## 3. Conjectures that need proving (explicit statements, current evidence)

The folder's live conjectures, in decreasing order of evidential support:

1. **Uniform normalised gap (G3).** $\exists\, c > 0: g_{\mathrm{sym}}(n) \ge c$ for all $n$.
   *Evidence:* stable at $0.54$–$0.57$ for $n = 6\ldots9$ (F3). *Tag:* heuristic → target
   proven. *Kill switch:* census drift at $n \le 14$.
2. **Block-purity of detached spectrum (G4).** Exactly the structural eigenvalues (Perron,
   mirror, one conjugate pair) detach at every stage and weighting in a $\beta$-window.
   *Evidence:* exact count 4 at $n = 6\ldots9$, $\beta = \tfrac12$ (F4). *Tag:* measured →
   target proven ("no graph-Siegel avatar"). — **Update 7 Jul 2026 (falsifier fired):** the
   count form is **refuted** in the extracted project (persistent fifth at $\beta = 0.30$
   from $n = 8$; the anchor $\beta = \tfrac12$ census becomes 6 at $n = 11, 12$). The
   surviving, strengthened form — real-detached $=$ the Perron pair only at every sweep
   point, plus a proven edge-purity theorem (all $n \ge 4$, all β) — is recorded in
   `victor/research/findings/PSC2-F05-anti-siegel.md`.
3. **H\* (C1 in the strip, coupled family).** *Evidence for:* Gonek–Hughes–Keating hybrid
   shape; *against:* Turán–Montgomery caution (P3.4), V1's elimination. *Tag:* open,
   falsifiable; the folder's single most valuable target at L3.
4. **E0 Weyl law for $H^G_n$.** The sieve-Galerkin compression's intrinsic counting has the
   $\frac{T}{2\pi}\log\frac{T}{2\pi}$ shape on derived windows with zero fitted parameters.
   *Evidence:* design argument only (§3.3 of the draft; CM 2022 for the archimedean part).
   *Tag:* open — **this is the first kill and should run before anything else at L4.**
5. **Q-γ2 Asano structure (G6/H5).** *Evidence:* the per-edge product form is Asano-native
   (F2). *Tag:* open, machine-checkable.
6. **HS1, HS2, HS3, HS7** — new, stated and priced in §4.

---

## 4. New conjectures from the prime sieve + the harmonic-sine documents

Extracted from [harmonic_sine_to_xi_sweep.html](harmonic_sine_to_xi_sweep.html) read against
the folder's proven record. Each has a pre-registered falsifier and consumes **no**
target-side data beyond what E4's rules already allow (I0/D2 hygiene). HS4 and X8 are the
*negative* extractions — decoys the same document suggests and the density law kills.

### HS1 — the stage paired-product gate (connects L4 to L3, D2-safe)

For a stage operator $H^G_n$ with positive eigenvalues $0 < \lambda_1 \le \cdots \le
\lambda_{d_n}$ (pairing by E1), define the **stage canonical product**

$$\Xi_n(t) \;=\; \Xi(0)\prod_{k=1}^{d_n}\Big(1 - \frac{t^2}{\lambda_k^2}\Big).$$

**Conjecture HS1.** If gates E0 (density) and E3b (certified enclosures with shrinking radii)
pass, then $\Xi_n(t) \to \Xi(t)$ uniformly on windows $|t| \le T'_n$ with $T'_n \to \infty$
slowly (a derived, not fitted, fraction of the E0 window $T_n$).

*Why this is new:* it is the eigenvalue-level (L4) *avatar of C1* — a determinant-level
statement built from stage spectra rather than from graph determinants, i.e. a bridge between
the E-gates and H\* that neither plan currently has. The sweep document's core analogy
(sine product ↔ $\Xi$ product) is exactly this object with $\lambda_k$ in place of $t_k$.
*Hygiene:* $\Xi(t)$ on the comparison window is computed independently via `mpmath` from
$\xi(\tfrac12 + it)$ — **no zero list is consumed**; the $\lambda_k$ come from the stage
construction with zero fitted parameters. *Falsifier:* pointwise divergence on $[0, 30]$ while
E4a passes would quantify pollution mass at determinant level — a reportable finding either
way. *Pricing:* uniform convergence on **all** of $\mathbb{R}$ with completeness would imply the
zero set — wall-adjacent at full strength (it would imply C1+C2 territory); the windowed,
rate-measured version is an evaluation metric strictly below the wall. *Tag:* open
(exploratory until E0/E3b exist).

### HS2 — the secondary-zeta moment gate (a Li-adjacent, γ-list-free harness)

From the paired product, exactly as $\log\frac{\sin\pi z}{\pi z} = -\sum_m \frac{\zeta(2m)}{m}z^{2m}$:

$$\log\frac{\Xi(t)}{\Xi(0)} \;=\; -\sum_{m\ge1}\frac{\sigma(2m)}{m}\,t^{2m},
\qquad \sigma(2m) := \sum_k t_k^{-2m}$$

— Voros' secondary zeta at even integers (the category M3 warns about, used here in its
**correct** category: moments, not spectral determinants). The targets $\sigma(2m)$ are
computable from Taylor coefficients of $\xi$ at $s = \tfrac12$ — again **no zero list**.

**Conjecture HS2 (moment gate E4d).** The stage moments
$\sigma_n(2m) = \sum_k \lambda_k^{-2m}$ converge to $\sigma(2m)$ for each fixed $m \ge 1$, at
a rate consistent with the E3b enclosure radii; persistent excess = pollution mass weighted
toward the low spectrum, deficit = spectral loss (the L3 analogue of E4a's budget).

*Why this is worth having:* (i) it is dominated by the **lowest** eigenvalues ($t_1^{-2m}$
dominates), so it complements E4a (which tests the whole trace) with a low-window,
zero-list-free displacement proxy for E4b; (ii) it ties the folder to the **Li-coefficient**
direction already endorsed as viable (research-findings §9.3): $\sigma(2m)$ and $\lambda_n^{\mathrm{Li}}$
are both zero-power-sum families — but note the pricing difference: *positivity of Li's for
all $n$ is a wall (W6); convergence of stage moments is an evaluation metric, not a positivity
claim.* *Falsifier:* $\sigma_n(2)$ failing to stabilise across three stages while E0 passes.
*Tag:* open; the identity itself is **proven** (classical, from the even Hadamard product,
Titchmarsh §2.12 — already imported for Thm 7.1's proof).

### HS3 — Sylvester filtration for the archimedean window (exploratory)

The greedy Egyptian expansion produces, for any target angle, a nested sequence of unit
fractions $1/q_k$ with $q_{k+1} \ge q_k(q_k - 1) + 1$ (Sylvester growth, doubly exponential
accuracy — **proven** in sine-harmonic.html §4).

**Proposal HS3.** Use the Sylvester denominators as the adaptive resolution schedule for the
archimedean window of $H^G_n$ (draft §3.2c): log-variable cutoffs $L_n$ and band-limit duals
chosen on the $\{1/q_k\}$ grid rather than uniformly, matching the doubly-exponential
convergence of the model side to the prolate/time-band-limiting structure.

*Honest assessment:* this is a **basis-engineering heuristic**, not a conjecture about zeros.
Value if true: better-conditioned N0 matrices at equal dimension. *Falsifier:* no measurable
conditioning/e-value-stability gain over the uniform Mellin–Hermite basis at $n \le 10$.
*Tag:* exploratory. *Guard:* the schedule must be fixed before any comparison with target
quantities (I0).

### HS5 — pairing as the single design law (unification, provable at stage level)

Four facts the folder currently holds separately are one fact:

1. genus-1 exponential factors cancel in the **paired** Hadamard product (sweep doc §7,
   classical);
2. one-sided $m^{-s}$ couplings monotonically destroy FE symmetry (F6, verified negative) —
   design law C-2: AFE symmetry by construction;
3. gate E1: $J$-invariant stages have exactly $\pm$-paired spectra (draft §3.1);
4. the bipartite divisor graph's chiral symmetry gives exact $\pm\lambda$ pairing at every
   stage (F3).

**Claim HS5 (to prove; expected routine).** For any stage family whose spectrum is exactly
$\pm$-paired (E1 mechanism), the stage canonical product $\Xi_n$ of HS1 is an **even entire
function of $t$ with no exponential factors** — i.e. the stage-exact form of the sweep
document's §7 cancellation — and, under the dictionary $t \leftrightarrow s = \tfrac12 + it$,
evenness in $t$ **is** the functional-equation symmetry $s \leftrightarrow 1 - s$ of the stage
determinant. Consequently the G2/V2 design law (C-2) and gate E1 are the *same constraint at
two levels*, and H\*-d ("build the FE into the stages") should be implemented as: **work only
with paired spectra and even stage products.**

*Tag:* open, expected provable in a page (it is bookkeeping once E1 is proved); its value is
architectural — it collapses two independent design constraints into one, and gives G2's V2
family a spectral (rather than kernel-schematic) definition.

### HS6 — the sine model as mandatory decoy control (harness addition)

Add to E4c: run the **entire** pipeline (E0 shape check, HS1 product, HS2 moments, E4b
displacement) on the exact model with spectrum $\mathbb{Z}_{>0}$ (dilation/harmonic-oscillator
realization; equivalently the sine product itself).

Pre-registered expectations: it must **pass** every internal-consistency step (its own Weyl
law, its own product convergence — all elementary and exact) and must **fail** E0's
$T\log T$ shape and E4b against the arithmetic targets by the density-class gap
($T$ vs $T\log T$ — the same two-growth-class kill as O1/Thm 3.3). Any harness configuration
on which the sine model scores as "arithmetic" is fabricating evidence and is invalid. This
institutionalises the sweep document's analogy in its only load-bearing role: **the analogy is
the control, not the evidence.** *Tag:* harness rule; costs one afternoon.

### HS7 — zero genealogy across stages (exploratory measurement)

The sweep document's §9 deformation moves zeros continuously in an external parameter
$\lambda$. The folder's honest analogue of that motion is **stage index $n$**: as
$P_n \uparrow$, the certified E3b enclosures move.

**Question HS7.** Do the certified enclosure intervals form persistent chains across stages
(each stage-$(n{+}1)$ interval containing or overlapping a stage-$n$ predecessor), with chain
displacements decreasing at a measured rate? A positive answer gives an *intrinsic*,
parameter-free version of "sweeping one zero at a time"; chain breaks localize pollution
events. *Relation to closed routes:* this is **not** the F7 lift question (which asked for
spectrum containment of graph stages and is closed); enclosure chains are about the compression
family $H^G_n$, where min–max monotonicity gives them at least a fighting chance.
*Tag:* exploratory measurement; falsifier built in (chains break early and often).

### HS4 — the nearest-integer decoy (negative extraction; recorded to prevent reuse)

The sweep document's §5 table carries a "nearest integer" column ($t_1 \approx 14$,
$t_2 \approx 21$, …) and §9 pairs the $k$-th zero with the $k$-th integer. **Any conjecture of
the form "zero ordinates track (scaled) integers" is dead on arrival** by the density design
law: $N_\zeta(T) \sim \frac{T}{2\pi}\log\frac{T}{2\pi}$ vs $N_{\mathbb{Z}}(T) \sim T$ — two
growth classes apart, the *same* obstruction (O1/Thm 3.3) that killed the $\{\log p\}$
eigenvalue program, in the opposite direction. The k-th-zero-to-k-th-integer pairing drifts
without bound; low-height proximity is numerology. Recorded as a **dead end** (X9 below) so
the table's suggestion is never picked up as a research path.

---

## 5. Dead ends and refuted routes (binding; do not reopen)

| # | Route | Killed by | Where |
|---|---|---|---|
| X1 | Eigenvalue→zero at the $\{\log p\}$ scaling (any affine rescaling) | density mismatch $e^T/T$ vs $\frac{T}{2\pi}\log\frac{T}{2\pi}$, **proven** (Thm 3.3); RMS residual 14.7 measured | [adele/phase3.md](adele/phase3.md) §3.4, [adele/phase4.md](adele/phase4.md) §4.3 |
| X2 | Block-local coupling (primes of $I_n$ through composites of $I_n$) | $pq \ge 2^{2n}$: coupling identically zero, **proven** twice over (Def 4.1 vacuity; empty graph D1) | phase3 Prop 3.1; [prime-sieve/notes.md](prime-sieve/notes.md) §2.1 |
| X3 | Rank-unfolding / any target-consuming normalisation as evidence | input-independent output; range-capped below $\gamma_2$; **proven + confirmed by execution** (D2) | notes.md §2.2; rule I0 |
| X4 | One-sided $m^{-s}$ coupling kernels (family V1) | FE asymmetry monotonically worsens; **verified negative** (F5/F6) | [prime-sieve/findings.md](prime-sieve/findings.md) |
| X5 | Naive stage-to-stage lifts/coverings (Q-γ1 as posed) | containment fraction $\approx 0.17$, nowhere near lift signature; **verified negative** (F7) | findings.md |
| X6 | Closed quantum graphs, $s$-independent unitary scattering, termwise $\Lambda$-matching | **proven no-go** (F8, unique-factorisation dichotomy); only the three G5 doors remain | findings.md |
| X7 | Greedy harmonic decomposition proposal ($\delta_n$ threshold family) | nesting fails at $\theta = \pi/2$; counting $O(\log\log N)$ not $x\ln N$; **refuted by execution**; Beurling generalized primes is the principled home | notes.md Dump 6 |
| X8 | The §9 Weierstrass **sweep as evidence** about zero locations | the paths $\gamma_j(\lambda)$ are *chosen using the known zero list* — the construction consumes its target (route-(W) shape, phase7 §7.2; D2/I0 class). Valid as classical function theory; carries **zero** information about where zeros are. Salvage: HS1/HS5/HS6/HS7. | this plan §4 |
| X9 | "Zero ordinates near integers" (sweep doc §5 table) | two growth classes apart (O1); numerology at low height | this plan HS4 |
| X10 | The gate-1.md locus + Asano proofs **as written** | quarantined in [flawed/](flawed/): the locus theorem's upper-bound derivation is incoherent mid-proof (mislabeled degree quantities, patched estimates); the "Asano compatibility" argument is circular (it invokes the conclusion for $G'$ and concludes stability from an annulus that *grows*, a non sequitur), and the leaf condition fails for the actual sieve graph (prime-power composites have degree 1). The **identity** (Theorem 2.1, Schur complement) is plausibly correct and worth salvaging under T6 with independent verification. | flawed/gate-1.md |
| X11 | Statistical/ensemble agreement as Hilbert–Pólya progress; RMT at this calibration | phase4 §4.2 (binding logical note); F9 null (neither CUE nor Poisson) | phase4; findings.md |
| X12 | The discarded `barry-keating-hp-*` proof series and `hamiltonian-sieve` | refuted at three independent provable points; kept as audit trail | [flawed/](flawed/), [berry-keating/worksheet.md](berry-keating/worksheet.md) |

**Intractable-as-posed** (distinct from dead: not refuted, but no known method and priced at or
above the wall): full-strength E3a; full-strength route γ; hurdle (ii) with positivity; any
direct attack on W1–W6. These are consulted for pricing, never scheduled.

---

## 6. The relationship map

```
                         MODEL PAIR (proven, elementary)
   sin(πt)/πt = ∏(1 − t²/n²)  ←──dictionary §1.1──→  Ξ(t) = Ξ(0)∏(1 − t²/t_k²)
   greedy Egyptian stages (exact, 2^-2^k)             sieve stages (exact, M_n^-1/2)
        │  controls (HS6)                                   │
        ▼                                                   ▼
  ┌──────────────────────── EVALUATION HARNESS (I0/D2-safe) ────────────────────────┐
  │  E4a trace vs 10^-36 anchor · E4b displacement · HS1 paired product ·           │
  │  HS2 moments σ(2m) · HS7 enclosure genealogy · decoys: prolate, sine (HS6)      │
  └───────────────────────────────────────────────────────────────────────────────┘
        ▲                          ▲                          ▲
   L1 TRACE (proven)          L3 DETERMINANT (open)      L4 EIGENVALUE (open)
   phase6 Weil balance   ←P5→  C1 / H* (G-gates)    ←HS1→  H^G_n (E-gates)
   rate O(M_n^-1/2)            P2 Hurwitz dictionary        E0→E1→E2→E3b
        │                          │                          │
        └────────── L2 CHARACTER χ_W: one contour integral; ──┘
                    "bridge + Weil" is circular (phase7, proven)
                                   │
                            THE WALL (W1–W6, all one wall):
              Weil positivity ⇔ C2|C1 ⇔ completeness ⇔ HB ⇔ RH  — priced, not attacked
                    calibrators: Meyer 2005 · Connes–Moscovici 2022
```

One sentence per edge: the sieve **is** the stage structure at every level (it enumerates the
places — proven); the model pair calibrates what "exact finite stages of a canonical product"
looks like when everything works; HS5 says the pairing/evenness/functional-equation constraint
is a single design law across all levels; the harness converts every ambition into a
pre-registered, target-free measurement; and every path terminates at the same proven wall,
which this folder prices and does not attack.

---

## 7. Priority ordering

Near-term (all T-class, standalone value regardless of the wall):

```
T1 E1 pairing lemma ─┬→ HS5 unification claim (routine after E1)
                     └→ T2 E0 density gate (first kill) ─→ T3 E2 inclusion ─→ T4 E3b enclosures
T6 G1 locus re-derivation (salvage identity; honest locus)  ─→ T8 G4 anti-Siegel
T7 G3 gap census to n≤14 (falsifier first), then proof attempt
T5+T12 harness build-out: E4a/b/c + HS6 sine decoy + HS2 moment gate + HS1 product gate
T9 truncation-rate proposition · T10 restricted-support positivity · T11 Li ranges
```

Then the H-class in order H2 (V2 family, now spectrally defined via HS5) → H3/H4 (gap rungs)
→ H5 (Asano, small-$n$ verdict) → H1 (H\* verdict from the accumulated evidence) → the rest.
HS3 and HS7 run opportunistically alongside N0–N3 of the draft's numerical program.

**Success criteria are the pre-registered ones already written** (draft §6, new-research-plan
gates, plus the falsifiers stated per-item in §4 above). Every outcome, including total
failure of $H^G_n$ at E0, is a reportable finding.

---

## 8. Status ledger

| Item | Tag |
|---|---|
| L1 trace identity + $10^{-36}$ verification + rate | **proven** |
| L2 character identity; circularity of "sieve bridge + Weil" | **proven** |
| Hurwitz dictionary; Kotani–Sunada; Turán–Montgomery caution; F8 no-go; N1–N4; Thm 7.1 | **proven** (classical/in-folder) |
| Weighted Ihara–Bass identity | verified $10^{-15}$; symbolic proof **open** (T6; prior attempt quarantined, X10) — **update 7 Jul 2026: proven** in the extracted project (explicit factorisation + exact $\mathbb{Q}$-certification at $n \le 6$; see `victor/research/findings/PSC2-F03-weighted-locus.md`, which also delivered T6's honest locus: weak annulus, anti-Siegel target re-scoped to the measured census) |
| E-gates E0–E4; G-gates G1–G6; H\*; P3.5; Q-γ2 | **open** (triaged T/H above) |
| HS1 product gate; HS2 moment gate; HS7 genealogy | **open** (new; pre-registered) |
| HS5 pairing unification | **open**, expected routine after E1 |
| HS3 Sylvester basis | **exploratory** |
| HS4 / X8 / X9 (sweep-as-evidence, integer proximity) | **dead ends**, recorded |
| E5 / C2 / route-γ-full / (ii)-with-positivity / HB / Weil & Li positivity | **RH-equivalent** — walls |
| RH | **open** |
