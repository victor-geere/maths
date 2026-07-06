# PSC2-S03 — the eigenvalue level (L4): the target $D$, the compression $H^G_n$, and the E-gates

*Source document S03. Extracted from `prime-sieve-continued/research-plan-draft.md` (the
E-gate charter, §0–§8). This is the working level of PSC2's numerical program; its refuted
predecessors are recorded in [PSC2-S06](PSC2-S06-constraints-and-walls.md).*

---

## 1. Normalisation facts fixing what the target can be — proven

**Lemma 1.1 (the critical line is the unitarity line). — proven (classical).** On
$L^2(\mathbb R_+, dx)$ the dilation group $(U_t f)(x) = e^{t/2}f(e^t x)$ is unitary with
essentially self-adjoint generator $D_\infty = -i\big(x\frac{d}{dx} + \tfrac12\big)$; the
Mellin transform diagonalises it with purely absolutely continuous simple spectrum
$\mathbb R$. The $\tfrac12$ is the $L^2$-Plancherel line. *Consequence:* a self-adjoint
realisation sees only $\mathrm{Im}\,s$; $\mathrm{Re}\,\rho = \tfrac12$ is carried by the
normalisation, never produced as output. **An eigenvalue program targets $\gamma$ and can
target nothing else.** (Full statement and proof: S00-adjacent, research-findings Prop 3;
`prime-sieve-continued/berry-keating/research-findings.md` §2.)

**Pairing.** The functional-equation symmetry $J$ (adelic Fourier transform composed with
inversion, implementing $s \leftrightarrow 1-s$) satisfies $JDJ^{-1} = -D$, so
$\mathrm{spec}(D) = -\mathrm{spec}(D)$: eigenvalues come in $\pm\gamma$ pairs. Finite stages
must carry this symmetry **by construction** (gate E1).

## 2. The imported triage — decision record

Of the five closed-form frameworks (Dirichlet series; adelic operator $D$; Ihara determinant;
Mellin/von Mangoldt; Hilbert-space matrix limit), only two are eigenvalue-native and
$\pm\gamma$-paired: **#2, the adelic $D$** (target) and **#5, finite self-adjoint matrices**
(working expression). #3's adjacency eigenvalues are *not* the $\gamma$'s (F4, S02 §6).

Two binding constraints:

- **K1 (the wall).** "$\mathrm{spec}(D) = $ all zeros" on the Hilbert-space ambient is
  RH-equivalent (Weil positivity). Proven neighbours: semi-local trace formula (Connes 1999);
  Meyer 2005 on nuclear non-Hilbert spaces. Positivity is the entire remaining content.
- **K2 (the mode).** Strong resolvent convergence gives spectral *inclusion* only and permits
  **pollution**. Norm-resolvent convergence, or extra compactness/positivity input, is
  required before "eigenvalues of $H_n \to$ exactly $\{\pm\gamma\}$" follows (Reed–Simon
  VIII.7).

## 3. The working family — one primary, two controls

**(a) Legacy comparator $H_n' = D_n' + \varepsilon_n A'$** ($\varepsilon_n = c/\lVert A'\rVert$;
S00 §2.3). Non-vacuous, self-adjoint, **dead as an eigenvalue map** (density mismatch, S00
§2.4). Role: negative control — it must fail gate E0.

**(b) Graph/divisor operators** (S02). Exact $\pm\lambda$-paired spectra (chiral symmetry),
stable normalised gap, Ihara–Bass machinery. Eigenvalues divisor-structural, not arithmetic
(F4). Role: toolkit — pairing mechanism, locus technology, pollution diagnostics.

**(c) Primary: the sieve-Galerkin compression $H^G_n = P_n D P_n$.** Compress the target
along the sieve's own filtration:

- *Finite places:* basis = the sieve's prime-power inventory $\{p^k \le M_n\}$ — the same
  truncation whose trace error is proven $O(M_n^{-1/2})$ (S00 §5–6).
- *Archimedean place:* dilation-adapted window (log-cutoff $|\log x| \le L_n$ + band-limit
  dual — prolate/time-band-limiting structure, the Connes–Moscovici fiber), Mellin–Hermite
  basis, exact matrix elements.
- *Symmetry:* $V_n = \mathrm{ran}\,P_n$ chosen $J$-invariant, so $JH^G_nJ^{-1} = -H^G_n$
  exactly at every stage.

Matrix elements of $D$ and $D^2$ are explicit (geometric sums at finite places,
Gaussian/Mellin integrals at $\infty$), `mpmath`-computable at `dps=35`.

*Why compression:* eigenvalues of compressions of a self-adjoint operator obey min–max; the
difficulty becomes the behaviour of $P_n \uparrow I$ — exactly where the honest obstruction
(pollution, K2) lives, exposed to the correct theory rather than hidden in an ad-hoc coupling.

## 4. The density design law (obstruction O1 repaired by design)

$N(T) = \frac{T}{2\pi}\log\frac{T}{2\pi} - \frac{T}{2\pi} + \tfrac78 + S(T) + \cdots$

- **E0a (smooth part, attainable).** The $T\log T$ shape is a two-cutoff dilation phenomenon
  (Berry–Keating regularisation; proven for the prolate operator's counting, CM 2022). Derive
  the stage Weyl law from the operator with **zero fitted parameters**.
- **E0b (fluctuation part — the open content).** Finite places must supply $S(T)$-type
  fluctuations without disturbing the smooth law; measured against fixed smooth test functions,
  unfolding-free.
- **Bookkeeping.** $\dim V_n = \#\{p^k \le M_n\} + O(L_n^2)$; resolution
  $\Delta\gamma \sim \pi/L_n$; derived window $T_n$ must satisfy
  $\frac{T_n}{2\pi}\log\frac{T_n}{2\pi} \lesssim \dim V_n$ — a computation, never a fit.

## 5. Obstruction ledger

| # | Obstruction | Answered by |
|---|---|---|
| O1 | density mismatch (killed one candidate already) | gate E0 + §4 design law |
| O2 | $\pm\gamma$ pairing must be structural | gate E1 |
| O3 | convergence mode: inclusion only; pollution possible | gates E2, E3 |
| O4 | completeness $\iff$ RH via positivity; Krein risk | gate E5 — **priced, not attacked** |
| O5 | target-consuming normalisation fabricates agreement | harness rules (E4, I0) |
| O6 | the shape decoy: matching $T\log T$ is not matching zeros | E4c controls |

## 6. The E-gates (statements; work packages WP01–WP05)

- **E0 — density gate** (first kill): intrinsic Weyl law of $H^G_n$, zero fitted parameters;
  pre-registered: legacy $H_n'$ **must fail**, graph one-mode **must fail**. → WP02
- **E1 — pairing lemma** ($V_n$ $J$-invariant $\Rightarrow$ spectrum symmetric with paired
  eigenvectors; one page). → WP01
- **E2 — spectral inclusion**: fix the ambient with tags (E2a, the K1 correction done once);
  prove $P_n \to I$ strongly on a core $\Rightarrow$ strong-resolvent convergence
  $\Rightarrow$ no zero missed (E2b). Unconditional. → WP03
- **E3 — pollution control**: (a) norm-resolvent on windows — deep, wall-adjacent at full
  strength; (b) **certified enclosures** via second-order relative spectra from the pencil
  $(P_nDP_n, P_nD^2P_n)$ — pollution-free by classical theorem (Shargorodsky;
  Levitin–Shargorodsky 2004; Davies–Plum), the tractable core; (c) positivity input = E5,
  not a work item. → WP04
- **E4 — evaluation harness** (pre-registered, D2-safe): E4a trace-consistency against the
  $10^{-36}$ anchor within the proven $O(M_n^{-1/2})$ envelope (excess = pollution mass,
  deficit = spectral loss); E4b matched displacement on $[0,50]$, $\gamma$-list as final
  evaluation only; E4c controls — positive (harmonic oscillator), decoy (bare prolate/xp
  compression: must pass E0's shape, must fail E4b), negatives (legacy $H_n'$, graph
  one-mode). Extended in PSC2 by the HS-gates ([S04](PSC2-S04-model-pair.md)). → WP05
- **E5 — the wall, priced**: completeness on a genuine Hilbert space $\iff$ RH. Unconditional
  ceiling of the level, stated in advance: certified sublist (E3b) + no-missing-spectrum (E2)
  + trace-consistency (E4a) together still do **not** decide RH.

## 7. Numerical program (staged, pre-registered)

| Step | Content | Depends on |
|---|---|---|
| N0 | stage builder: $J$-invariant basis; matrix elements of $D, D^2$; $\dim V_n \sim$ a few $\times 10^3$ at $n \le 14$ | §3(c) |
| N1 | E0 density runs + all controls; publish against pre-registered criteria verbatim | N0 |
| N2 | E4a trace-consistency vs the S00 §6 numbers; first E3b enclosures | N0 |
| N3 | E4b displacement; HS1/HS2 product and moment gates; findings note | N1, N2 |

Success criteria fixed in advance: E4a residual within $C\,M_n^{-1/2}$ with $C$ derived from
S00 §5 Prop 6.1; E4b median displacement decreasing over three consecutive stages; any
outcome, including total failure of $H^G_n$ at E0, is a reportable finding.
