# PSC2-S04 — the model pair: harmonic sine ↔ Riemann Xi, and the HS-gate foundations

*Source document S04. Extracted from `prime-sieve-continued/sine-harmonic.html` (the greedy
Egyptian-fraction reconstruction, with proofs) and
`prime-sieve-continued/harmonic_sine_to_xi_sweep.html` (the product analogy), audited against
the folder's evidence rules. The model pair is **harness apparatus**: it calibrates the
evaluation gates and grounds the HS-conjectures of the charter §4. It is not, and may not be
presented as, evidence about zero locations (see §5).*

---

## 1. The core analogy — both sides proven as stated

$$\frac{\sin(\pi t)}{\pi t} = \prod_{n=1}^\infty\Big(1 - \frac{t^2}{n^2}\Big)
\qquad\longleftrightarrow\qquad
\Xi(t) = \Xi(0)\prod_{k=1}^\infty\Big(1 - \frac{t^2}{t_k^2}\Big),$$

$\Xi(t) = \xi(\tfrac12 + it)$, zeros exactly $\pm t_k$, $t_k = \mathrm{Im}\,\rho_k$. Both
entire of order 1 and **even**. The general genus-1 Hadamard factors $\exp(s/\rho)$ cancel in
the paired quadratic form — **pairing kills the convergence factors** (classical; even
Hadamard product, Titchmarsh §2.12). This identity of *shape* is exact; the identity of
*content* (where the $t_k$ are) is the open problem, untouched by the analogy.

## 2. The greedy Egyptian-fraction stage structure — proven

**Lemma 2.1 (greedy unit-fraction invariant).** For $t \in (0,1)$, $r_0 = t$,
$q_{k+1} = \lceil 1/r_k \rceil$, $r_{k+1} = r_k - 1/q_{k+1}$:

1. $q_1 \ge 2$ and $q_{k+1} \ge q_k(q_k - 1) + 1$ (Sylvester growth $2, 3, 7, 43, 1807,\dots$);
2. $0 \le r_k < 1/(q_k(q_k-1))$;
3. rational $t = a/b$ terminates in $K \le a$ steps (Fibonacci–Sylvester);
4. $r_k < 2^{-2^{k-1}}$ for $k \ge 2$ — **doubly exponential** convergence.

*Proof:* ceiling property gives (2); integrality gives (1); numerator descent gives (3);
$a_k = q_k - 1$ squares each step, giving (4). (Full proof in the source document §4.) $\blacksquare$

**Theorem 2.2 (harmonic reconstruction; closed form).** With the rotation recursion carrying
$(\sin\theta_k, \cos\theta_k)$ exactly (angle addition; step sines from dyadic bisection —
Pythagoras only),
$$\sin(\pi x) = \mathrm{sgn}(x)\,(-1)^m\,\mathrm{Im}\prod_{k=1}^{K}\exp\Big(\frac{i\pi}{q_k}\Big),$$
finite and exact for rational $x$; $|s_k - \sin(\pi t)| \le \pi r_k < \pi\,2^{-2^{k-1}}$.
**proven.**

**Role in PSC2.** The greedy stages are the model-side counterpart of the sieve stages: a
finite, exact, stage-by-stage construction of a canonical-product object, with a proven
(here doubly-exponential; there $O(M_n^{-1/2})$) stage error. The comparison calibrates what
"exact finite stages" look like when everything works.

## 3. The log-expansion / moment identities — proven; basis of gate HS2

Model side:
$$\log\frac{\sin(\pi z)}{\pi z} = -\sum_{m\ge1}\frac{\zeta(2m)}{m}\,z^{2m}\qquad (|z| < 1).$$

Arithmetic side, identically derived from the even Hadamard product:
$$\log\frac{\Xi(t)}{\Xi(0)} = -\sum_{m\ge1}\frac{\sigma(2m)}{m}\,t^{2m},\qquad
\sigma(2m) := \sum_k t_k^{-2m}\quad(|t| < t_1),$$

$\sigma$ = Voros' *secondary* zeta at even integers — the correct category (moments of the
zero set), kept strictly separate from the spectral-zeta category error M3
([S06](PSC2-S06-constraints-and-walls.md) §3). The targets $\sigma(2m)$ are computable from
Taylor coefficients of $\xi$ at $s = \tfrac12$ via `mpmath` — **no zero list is consumed**.
This underwrites gate **HS2** (charter §4): stage moments
$\sigma_n(2m) = \sum_k \lambda_k^{-2m}$ vs $\sigma(2m)$, a low-window, $\gamma$-free
pollution/loss detector, Li-coefficient-adjacent but strictly below the Li-positivity wall.

## 4. The pairing law — basis of gate HS5

Four facts held separately in the sources are one constraint:

1. paired Hadamard factors cancel exponentials (§1, classical);
2. one-sided $m^{-s}$ couplings monotonically destroy FE symmetry (F6, verified negative;
   design law C-2: AFE symmetry by construction);
3. $J$-invariant stages have exactly $\pm$-paired spectra (gate E1);
4. bipartite chiral symmetry pairs the divisor-graph spectra exactly (F3).

**Claim HS5 (to prove, expected routine after E1).** For $\pm$-paired stage spectra, the stage
canonical product $\Xi_n(t) = \Xi(0)\prod(1 - t^2/\lambda_k^2)$ is even and exponential-factor
free, and evenness in $t$ **is** the functional equation $s \leftrightarrow 1-s$ of the stage
determinant. E1 and C-2 are one design law at two levels; H\*-d should be implemented as
"paired spectra, even products."

## 5. What the model pair may NOT be used for — binding

- **X8 (sweep-as-evidence).** The source document's "sweep" deforms zeros from integers to the
  actual $\rho_j$ along chosen paths $\gamma_j(\lambda)$. The paths are chosen **using the
  known zero list**: the construction consumes its target. Valid Weierstrass theory; zero
  information about zero locations; same defect class as rank-unfolding (D2/I0). Salvage is
  exactly HS1/HS5/HS6/HS7 — nothing else.
- **X9 (nearest-integer numerology).** $N_\zeta(T) \sim \frac{T}{2\pi}\log\frac{T}{2\pi}$ vs
  $N_{\mathbb Z}(T) \sim T$: two growth classes apart; the $k$-th-zero-to-$k$-th-integer
  pairing drifts unboundedly. Any "ordinates track integers" conjecture is dead on arrival
  (density law O1).
- **HS6 (the only load-bearing role).** The sine model is the mandatory decoy control: run the
  full pipeline on the exact model with spectrum $\mathbb Z_{>0}$; it must pass every
  internal-consistency step and must **fail** every arithmetic test by the density-class gap.
  Any harness configuration on which the sine model scores as "arithmetic" is fabricating
  evidence and is invalid. **The analogy is the control, not the evidence.**

## 6. Gate HS1 — the stage paired-product gate (statement)

For stage eigenvalues $0 < \lambda_1 \le \cdots \le \lambda_{d_n}$ of $H^G_n$ (pairing by E1),
define $\Xi_n(t) = \Xi(0)\prod_k(1 - t^2/\lambda_k^2)$.

**Conjecture HS1. — open.** If E0 and E3b pass, $\Xi_n \to \Xi$ uniformly on derived windows
$|t| \le T'_n$, $T'_n \to \infty$. The eigenvalue-level avatar of C1 — the L4→L3 bridge.
*Hygiene:* $\Xi$ computed independently from $\xi(\tfrac12 + it)$ (`mpmath`); no zero list;
$\lambda_k$ from the stage construction with zero fitted parameters. *Pricing:* full-strength
uniform convergence with completeness is wall-adjacent; the windowed, rate-measured version is
an evaluation metric below the wall. *Falsifier:* pointwise divergence on $[0,30]$ while E4a
passes — reportable either way (quantified determinant-level pollution).

## 7. Gate HS7 — zero genealogy (statement)

Do the certified E3b enclosure intervals form persistent chains across stages, with chain
displacements decreasing at a measured rate? An intrinsic, parameter-free "sweep"; chain
breaks localize pollution events. Distinct from the closed F7 lift question (compressions obey
min–max; graph stages do not). **exploratory**, falsifier built in.
