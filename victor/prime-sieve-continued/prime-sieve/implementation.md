# implementation.md — corrected constructions, measurement protocol, and code

*Implements [path.md](path.md). Everything here is either a definition, a computation, or a
falsification test; claims inherit their tags from path.md. The defects D1/D2 and misstatements
M1–M5 of the old artifacts ([notes.md](notes.md) §2) are treated as regression tests: the code
below is built so that each of them would now be caught mechanically.*

Run style follows the repo convention (plain scripts printing tables, no notebooks;
`cd victor && source .venv/bin/activate`). Dependencies: `numpy`, `mpmath` (already pinned).
`scipy` is used only if present (dense eigensolvers suffice at the sizes below).

---

## I0. Evidence hygiene (binding rules for every experiment in this folder)

1. **No rank-based unfolding against the target's own counting function** (D2). Any comparison
   with Riemann zeros must use raw computed quantities (determinant values, pole coordinates,
   raw angle gaps) against independently computed truth (`mpmath.zetazero`, `mpmath.zeta`).
2. **Non-vacuity guards** (D1): every graph build asserts `edges > 0` and prints the edge
   count; every pencil/eigen computation asserts the operator is not identically zero.
3. **Correct circles** (M1): Ramanujan locus is $|u| = q^{-1/2}$ (regular) or the weighted
   Kotani–Sunada annulus — never $|u| = 1$, which carries only trivial factors.
4. **Two-sided reporting**: every experiment states, before running, what outcome would
   *falsify* the hypothesis it probes; results are recorded either way (repo worksheet culture).
5. **Cross-checks against in-repo verified numbers**: the explicit-formula balance is checked
   against [../adele/adele_trace.py](../adele/adele_trace.py) values (e.g. arithmetic side
   $0.603035\ldots$ at $t = 0.2$), not recomputed ad hoc.

---

## I1. Corrected constructions

### I1.1 Bipartite divisor graph $B_n$ (Definition P0.2)

Vertices: $\mathcal P_n = \{p < 2^n\}$ (row class) and $\mathcal C_n = \{m \in I_n
\text{ composite}\}$ (column class). Weighted incidence
$$W_{p,m} \;=\; a_p(m)\, p^{-\beta}, \qquad a_p(m) = v_p(m)\ (\text{multiplicity}),\quad
\beta = \tfrac12 \text{ (default)}.$$

- One-mode prime-side operator: $S_n = W W^{\mathsf T}$,
  $(S_n)_{pq} = \sum_{m \in I_n} a_p(m) a_q(m) (pq)^{-\beta}$ — the graph form of Phase 3's
  corrected coupling $A'$.
- Directed edge set $E = \{(p \to m), (m \to p) : W_{p,m} \ne 0\}$; weighted
  **non-backtracking operator**
  $$\big(B^{\mathrm{nb}}_w\big)_{(x \to y),(y' \to z)} \;=\;
  \mathbb{1}[y' = y]\;\mathbb{1}[z \ne x]\;\sqrt{W_{y,z}\,W_{x,y}}\big/\text{(calibration)},$$
  with the square-root split making $B^{\mathrm{nb}}_w$ similarity-equivalent to the standard
  weighted Hashimoto form. Stage polynomial: $\phi_n(u) = \det(I - u\,B^{\mathrm{nb}}_w)$.
- **Proof obligation W** (path.md P3.1): the weighted Ihara/Bass three-term identity for
  $\phi_n$ (Mizuno–Sato 2004) and the resulting confinement locus. *Machine check first*: at
  $n \le 6$ expand both sides symbolically (sympy-verifier MCP: `verify_equation` on the
  coefficient lists) before attempting the general proof.

Non-vacuity (D1 regression): for $n = 8$: $|\mathcal P_n| = 54$, $|\mathcal C_n| = 213$, and
every even composite contributes edges through $p = 2$; the build asserts this.

### I1.2 Place-cycle control object (Definition P0.1)

$D^{\mathrm{cyc}}_n(s) = \prod_{p \le M_n}(1 - p^{-s})$ — computed directly in `mpmath` at
working precision 30. Role: *control column* in every table. Any coupled-model pipeline run
with couplings dialed to zero **must reproduce this column to full precision** (consistency
test for the machinery itself).

### I1.3 Coupled determinant family (the H\* candidates)

$$D_n(s; \theta) \;=\; G_\infty(s)\; \det\!\big(I - u(s)\, B^{\mathrm{nb}}_{w(\theta)}\big),
\qquad G_\infty(s) = \tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2),$$
where $\theta$ dials the composite-coupling strength ($\theta = 0$: decoupled, must equal
$D^{\mathrm{cyc}}_n \cdot G_\infty$; the $u(s)$-dictionary per place is $u_p = p^{-s}$ realised
through the weighted holonomies). Free design choices to be *fitted by experiment I2.3, then
frozen*: $\beta$, the archimedean split, and the symmetrisation.

---

## I2. Determinant pipeline (probes C1 / H\*)

### I2.1 Pointwise comparison protocol

Grids: $\sigma \in \{1.2, 1.5, 2, 3\} \times t \in [0, 40]$ (proven region — rate check), and
$\sigma \in \{0.6, 0.75\} \times t \in [0, 40]$ (strip — exploratory; record, never over-read).
Report $|D_n(s) - e(s)\xi(s)|$ (or $|D^{\mathrm{cyc}}_n(s)\,\zeta(s) - 1|$ for the control)
against $n$, with the **predicted** rate column
$\varepsilon_n(\sigma) \asymp M_n^{1-\sigma}\big/((\sigma-1)\log M_n)$ from path.md P1.2.
*Falsifier:* control column disagreeing with the predicted Euler-tail rate means the pipeline
itself is broken (not the mathematics).

### I2.2 Table format (regression-friendly, mirrors adele/phase6.md style)

```
  sigma    n      |D_n * zeta - 1|     predicted tail     ratio
  1.50     8      ...                  ...                ~1
  1.50    12      ...                  ...                ~1
```

### I2.3 Functional-equation design experiment (H\*-d; the fertile one)

For candidate weightings, measure the stage asymmetry
$$\mathcal A_n \;=\; \sup_{s \in \text{grid}} \Big| \frac{D_n(s;\theta)}{D_n(1-s;\theta)} - 1 \Big|
\quad\text{on } \mathrm{Re}\,s = \tfrac12 + \{0.1, 0.2\},\ t \in [0,30].$$
Design target: weight/prefactor choices driving $\mathcal A_n \to 0$ with $n$ — a discrete
functional equation. *Why it matters:* an exact stage symmetry would hand H\* its
identification set (path.md P1, obligation d) and is the graph analogue of adelic Poisson
summation. *Falsifier:* if no member of the family can reduce $\mathcal A_n$ below $O(1)$ while
keeping I2.1's control consistency, H\* as formulated is in trouble — report either way.

---

## I3. Honest spectral statistics (replaces the retired unfolding)

Allowed observables on the stage spectra (raw data only):

1. **Raw angle gaps vs CUE.** For non-real poles $u = re^{i\vartheta}$ of $\phi_n$, take the
   ordered $\vartheta_k \in (0,\pi)$, normalise mean gap to 1 **by dividing by the empirical
   mean gap** (data-internal, no target information), and compare the gap density with the
   $\beta = 2$ Wigner surmise $p(s) = \frac{32}{\pi^2}s^2 e^{-4s^2/\pi}$ (KS distance).
   Motivation: quantum-graph and quantum-chaos universality (Bohigas–Giannoni–Schmit;
   Gnutzmann–Smilansky) predicts RMT statistics for chaotic stages; Montgomery's theorem makes
   GUE the conditional benchmark on the zeta side. *This is a consistency diagnostic, not
   evidence about zero locations* (research-findings §8: statistics do not imply RH).
2. **Counting-function fluctuations.** $N_n(\vartheta)$ = number of pole angles $\le \vartheta$
   minus its own smooth fit (fit internally, e.g. by polynomial in $\vartheta$ — never by the
   Riemann $\bar N$); the fluctuation field is the honest signal to compare across $n$.
3. **Pointwise determinant values** (I2) — the unfakeable observable.

Banned: mapping ranks through $\bar N^{-1}$ (D2); any "match" produced by a transformation
that consumes the target's counting function.

---

## I4. Pole-locus and gap measurements (probes P3)

### I4.1 Gap census (target Proposition P3.5, milestone M1 input)

For $n = 6..14$: compute the spectrum of the symmetrised one-mode operator
$\widetilde S_n = \Pi^{\perp} S_n \Pi^{\perp}$ ($\Pi$ = Perron projection) and of
$B^{\mathrm{nb}}_w$; report
$$\lambda_1(n)\ (\text{Perron}),\quad \lambda_2(n),\quad
g_n = 1 - \lambda_2/\lambda_1,\quad g_n \cdot \log M_n .$$
**M1 criteria** (declared in advance): $g_n \log M_n \to c \in (0,\infty)$ ⇒ consistent with
de la Vallée Poussin strength (route α calibration good); $\to 0$ ⇒ route α falsified at this
weighting (revisit $\beta$); $\to \infty$ ⇒ *suspicious* — audit before celebrating (per repo
convention, surprising strength is a bug until proven otherwise).

### I4.2 Graph-Siegel tracking (P3.2 prediction)

Track all real poles of $\phi_n$ across $n$: prediction — exactly one persistent real pole
(Perron, the $s = 1$ avatar); all others drift toward the confinement locus. *Falsifier /
discovery:* a second persistent real pole is a "graph Siegel zero"; if observed, document it
prominently (that outcome would be more interesting than the prediction holding).

### I4.3 Structure probes for route γ (Q-γ1, Q-γ2)

- **Q-γ1 (covering):** test whether $B_{n+1}$ contains a 2-lift-like structure over $B_n$:
  compare $\mathrm{spec}(S_n)$ with $\mathrm{spec}(S_{n+1})$ for interlacing/containment
  patterns (Bilu–Linial signature: old spectrum $\cup$ new spectrum with new part bounded).
  Numeric first; if a pattern appears, formulate the exact covering map combinatorially.
- **Q-γ2 (Asano):** at $n \le 6$, express $\phi_{n+1}$ in terms of $\phi_n$-data and test
  whether the recursion step is an Asano contraction (zeros of the glued polynomial confined
  given confinement of the parts) — finite polynomial identities, run through the
  sympy-verifier MCP (`verify_equation`, `check_zero`).

---

## I5. Milestone M1 — the de la Vallée Poussin rung (first real deliverable)

Chain (all pieces named in path.md): measured $c/\log$ gap (I4.1) $\to$ Proposition P3.5
(proof: Brun–Titchmarsh + large sieve on the divisor-count fluctuation matrix) $\to$ *given H\**,
P2.4 converts it to a zero-free region of width $\asymp 1/\log|t|$ — dlVP strength. Success =
an independent graph-spectral re-derivation of the classical region (a real, publishable-grade
consistency theorem *below* the wall); the second rung (Vinogradov–Korobov strength) requires a
gap of $\asymp \log^{-2/3}$ quality — listed, not promised.

Status accounting: today this milestone has **zero proven links** on the graph side (P3.5
unproven, H\* open); its value is that every link is separately attackable and separately
falsifiable — no all-or-nothing leap.

---

## I6. Quantum-graph amplitude probe (the unitarity wall, made measurable — exploratory)

Kottos–Smilansky flower graph: one vertex, one loop of length $\log p$ per $p \le P$; bond
scattering matrix $\Sigma$ unitary (Neumann default:
$\sigma_{ee'} = \frac{2}{2B} - \delta_{e', \bar e}$); secular determinant
$F(s) = \det(I - e^{i s L}\,\Sigma)$, $L = \mathrm{diag}(\ell_e)$. Self-adjointness makes the
zeros of $F$ real *automatically*; periodic-orbit lengths are $\sum_p k_p \log p = \log m$ —
the explicit formula's support. The entire arithmetic difficulty becomes: **can orbit
amplitudes equal $\Lambda(m)/\sqrt m$ under a unitary $\Sigma$?** Experiment: tabulate, for
$m \le 100$, the Neumann amplitudes vs $\Lambda(m)/\sqrt m$; then minimise the weighted
mismatch over a small unitary family (diagonal phases $\times$ DFT). Output: a "distance to
unitarity" curve — a *quantitative coordinate for the wall* (research-findings §7: positivity
is the entire remaining content; here positivity $=$ unitarity). No RH-ward claim attaches to
any outcome; the number itself is the deliverable.

---

## I7. Code

### I7.1 Consolidated lab script — **now implemented as [prime_graph_lab.py](prime_graph_lab.py)**

*(5 Jul 2026: the lab exists as a real script with sections `control bass gaps siegel coupled
fe qgamma1 cue flower`, extending the sketch below with the Bass-identity test, the coupled/FE
H\* probes, Q-γ1, and the flower no-go witness. Run results: [findings.md](findings.md).
The sketch below is kept as the original specification.)*

```python
"""prime_graph_lab.py -- corrected numerics for victor/prime-sieve (path.md / implementation.md).

Sections: build (I1), determinants (I2), stats (I3), gaps & poles (I4).
Every routine prints its non-vacuity guards. No rank-unfolding anywhere (rule I0.1).
"""
import numpy as np
from math import log, pi
import mpmath as mp

mp.mp.dps = 30

# ---------- sieve (shared with adele/ scripts) ----------
def sieve_primes(limit):
    if limit < 2: return np.array([], dtype=int)
    s = np.ones(limit + 1, dtype=bool); s[:2] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if s[p]: s[p*p::p] = False
    return np.flatnonzero(s)

def stage(n):
    """primes < 2^n (generators), composites in I_n, all primes <= M_n."""
    M = (1 << (n + 1)) - 1
    P = sieve_primes(M)
    gens = P[P < (1 << n)]
    inblock = set(P[(P >= (1 << n))].tolist())
    comps = [m for m in range(1 << n, M + 1) if m not in inblock]
    return gens, comps, P, M

# ---------- I1.1 bipartite divisor graph ----------
def build_bipartite(n, beta=0.5):
    gens, comps, P, M = stage(n)
    gi = {int(p): i for i, p in enumerate(gens)}
    W = np.zeros((len(gens), len(comps)))
    for j, m in enumerate(comps):
        x = m
        for p in gens:
            if x == 1: break
            if p * p > x:                          # leftover x is a prime < 2^n (Lemma 1)
                W[gi[x], j] += float(x) ** (-beta); x = 1; break
            k = 0
            while x % p == 0: x //= p; k += 1
            if k: W[gi[int(p)], j] += k * float(p) ** (-beta)
        assert x == 1, f"factorisation left x={x} for m={m}"
    edges = int((W > 0).sum())
    assert edges > 0, "D1 regression: bipartite graph must be non-empty"
    print(f"[build] n={n}: |P|={len(gens)} |C|={len(comps)} edges={edges}")
    return W, gens, comps, M

def one_mode(W):
    S = W @ W.T
    assert np.abs(S).sum() > 0, "D1 regression: coupling matrix is zero"
    return S

def nonbacktracking(W):
    """Weighted Hashimoto operator on directed edges of the bipartite graph."""
    P, C = W.shape
    edges = [(i, j) for i in range(P) for j in range(C) if W[i, j] != 0]
    fwd = {e: k for k, e in enumerate(edges)}            # p->m
    nE = len(edges)
    B = np.zeros((2 * nE, 2 * nE))                       # [0:nE]=p->m, [nE:]=m->p
    w = lambda i, j: np.sqrt(W[i, j])
    for k, (i, j) in enumerate(edges):
        for k2, (i2, j2) in enumerate(edges):
            if j2 == j and i2 != i:      # m->p2 after p->m, no backtrack
                B[k, nE + k2] = w(i, j) * w(i2, j)
            if i2 == i and j2 != j:      # p->m2 after m->p, no backtrack
                B[nE + k, k2] = w(i, j) * w(i, j2)
    assert np.abs(B).sum() > 0
    return B

# ---------- I1.2 / I2 determinants ----------
def euler_control(s, M):
    return mp.fprod([1 - mp.power(p, -s) for p in sieve_primes(M)])

def det_table(n_list, sigmas=(1.5, 2.0), t=7.0):
    print("\n[I2.1] control-column check: |Euler_n(s) * zeta(s) - 1| vs predicted tail")
    print("  sigma    n        |err|            predicted        ratio")
    for sig in sigmas:
        s = mp.mpf(sig) + 1j * mp.mpf(t)
        for n in n_list:
            M = (1 << (n + 1)) - 1
            err = abs(euler_control(s, M) * mp.zeta(s) - 1)
            pred = mp.power(M, 1 - sig) / ((sig - 1) * mp.log(M))
            print(f"  {sig:4.2f}  {n:4d}   {mp.nstr(err, 6):>14}   {mp.nstr(pred, 6):>14}"
                  f"   {mp.nstr(err / pred, 4):>8}")

# ---------- I3 honest statistics ----------
def raw_angle_gaps_vs_cue(u_poles):
    th = np.sort(np.angle(u_poles[np.abs(u_poles.imag) > 1e-9]))
    th = th[th > 0]
    if len(th) < 10:
        print("[I3] too few non-real poles for statistics"); return None
    gaps = np.diff(th); gaps = gaps / gaps.mean()        # data-internal normalisation only
    xs = np.sort(gaps); F_emp = np.arange(1, len(xs) + 1) / len(xs)
    # Wigner beta=2 surmise p(s) = (32/pi^2) s^2 exp(-4 s^2/pi); its CDF in closed form:
    from math import erf
    F_cue = np.array([erf(2*x/np.sqrt(pi)) - (4*x/pi)*np.exp(-4*x*x/pi) for x in xs])
    ks = np.max(np.abs(F_emp - F_cue))
    print(f"[I3] raw-gap KS distance to CUE surmise: {ks:.4f}  (N={len(xs)})")
    return ks

# ---------- I4 gaps and pole loci ----------
def gap_census(n_list, beta=0.5):
    print("\n[I4.1] weighted one-mode gap census")
    print("    n     lam1(Perron)   lam2        gap g_n     g_n*log(M_n)")
    for n in n_list:
        W, gens, comps, M = build_bipartite(n, beta)
        lam = np.linalg.eigvalsh(one_mode(W))[::-1]
        g = 1 - lam[1] / lam[0]
        print(f"  {n:4d}   {lam[0]:10.4f}  {lam[1]:10.4f}   {g:8.5f}   {g*log(M):10.5f}")

def pole_census(n, beta=0.5):
    W, gens, comps, M = build_bipartite(n, beta)
    B = nonbacktracking(W)
    mu = np.linalg.eigvals(B)                 # poles u = 1/mu (mu != 0)
    mu = mu[np.abs(mu) > 1e-10]; u = 1.0 / mu
    nreal = np.sum(np.abs(u.imag) < 1e-9)
    print(f"[I4.2] n={n}: {len(u)} poles, {nreal} real; "
          f"|u| range [{np.abs(u).min():.4f}, {np.abs(u).max():.4f}]")
    real_u = np.sort(u.real[np.abs(u.imag) < 1e-9])
    print(f"        real poles (graph-Siegel tracking): {np.round(real_u[:6], 5)} ...")
    return u

if __name__ == "__main__":
    det_table([6, 8, 10, 12])
    gap_census([6, 7, 8, 9])
    u = pole_census(8)
    raw_angle_gaps_vs_cue(u)
```

### I7.2 Patches to the three existing scripts (do not delete; annotate)

| File | Action |
|---|---|
| `ihara-riemann-spectrums.py` | Header comment pointing to D1/D2 ([notes.md](notes.md) §2); replace `build_prime_graph` with `build_bipartite`; delete the `|u|=1` filter (M1) in favour of the weighted locus; retire `unfold_eigenvalues` from any evidentiary path. |
| `ihara-zeta-convergence.py` | Same graph fix; replace Q–Q-after-unfolding with I3 raw-gap and I2 pointwise panels. |
| `numeric-verification.py` | Keep the $W_\infty - A_n$ vs zero-sum panel (genuine explicit formula; cross-check against `../adele/adele_trace.py` §6.3 values); drop the `S_Ihara` column (it was unfolding output, D2). |

### I7.3 Symbolic verification tasks (sympy-verifier MCP)

1. Weighted Bass identity at $n \le 6$ (obligation W): coefficients of
   $\det(I - uB^{\mathrm{nb}}_w)$ vs the three-term form.
2. Q-γ2 Asano-step identities at $n \le 6$.
3. Regression: $\theta = 0$ coupled determinant $\equiv$ Euler control (I1.3), symbolically at
   $n \le 4$, numerically at all $n$.

---

## I8. First baseline run (5 Jul 2026, code of I7.1 executed verbatim) — recorded honestly

```
[I2.1]  sigma=1.5: |err|/predicted = 0.0678, 0.0722, 0.0704, 0.0709   (n = 6, 8, 10, 12)
        sigma=2.0: |err|/predicted = 0.1336, 0.1417, 0.1397, 0.1409
[I4.1]  n=6,7,8:  g_n = 0.806, 0.787, 0.810 ;  g_n*log(M_n) = 3.91, 4.36, 5.05
[I4.2]  n=7 (beta=1/2): 438 poles, 208 real, |u| in [0.189, 4.182]
[I3]    raw-gap KS distance to CUE surmise: 0.837 (N=114)
```

Readings (each per its pre-declared criterion):

1. **Control column ✓.** The error/predicted ratio is stable in $n$ at each $\sigma$ — the
   pipeline reproduces the proven Euler-tail rate (P1.2). Machinery trustworthy.
2. **Gap census → the "suspicious" branch.** $g_n \log M_n$ *grows* (relative gap roughly
   constant $\approx 0.8$). Per I4.1's declared rule this is **audit, not celebration**: the
   raw one-mode gap at $\beta = \tfrac12$ is almost certainly Perron-scaling artefact (the
   rank-one $2^n (pq)^{-1-\beta}$ dominance), not arithmetic content. The dictionary that
   converts this gap into a P3.5-grade statement is exactly what obligation W + P3.5 must
   supply; no strength claim is made from this table.
3. **Weighted pole locus is genuinely open.** Poles spill far outside any unit-type annulus
   ($|u|$ up to $4.18$; 208 real poles): the classical Kotani–Sunada bounds do **not** apply
   verbatim to this weighting — obligation W is not a formality, it is *the* gating lemma, and
   graph-Siegel tracking (I4.2) is undefined until W fixes the reference locus.
4. **No RMT signature at this stage/calibration** (KS $= 0.84$). Expected for a tiny,
   Perron-dominated, highly irregular stage; recorded so that any future "GUE emerges"
   claim has a baseline to beat.

Net: the corrected machinery works, and every open item is exactly where path.md said it
would be — in the weighting/dictionary (W, H\*, P3.5), not in the plumbing.

## Deliverable order (dependency-sorted)

1. Run I7.1 as-is (control tables + first gap census + pole census). *Everything downstream
   depends on these baselines.*
2. I2.3 functional-equation design sweep → freeze $(\beta, G_\infty^{(n)}, \text{symmetrisation})$.
3. I4.2 graph-Siegel tracking across $n$ (the experiment the folder should have run first).
4. Obligation W symbolic → general proof attempt.
5. P3.5 proof attempt (route α) with the frozen weighting; M1 verdict.
6. Q-γ1/Q-γ2 structure probes; I6 unitarity-distance curve.
