# The Generalised Algorithm — Phase 4

*Status: **design note / sketch** (gate partly discharged). The $L^2(\gamma)\to L^2(\mathbb{T})$ functor is now proved (Lemma O6, [ou-process.md](../../project/ou-process.md) §4.1) and the OU numerics (1c) are done; the one remaining gate is the **Fibonacci §6 numerics (1b)**. Until then this stays a sketch, not a proof note.*

*When ready, this becomes `project/generalised-algorithm.md` following the proof-note template.*

---

## 0. Purpose

Every catalogue object in the [spectral data sheet](../deliverables/spectral-data-sheet.md) is the **same construction** applied to a different non-negative arithmetic sequence. This note abstracts that construction into one algorithm: a map

$$\mathcal{S}\colon\ (a_n)_{n\ge0}\ \longmapsto\ \bigl(T_K,\ \{\lambda_n\},\ M,\ \mathrm{ExplFn},\ D(z)\bigr)$$

from a damped non-negative sequence to a self-adjoint operator together with its four derived invariants — **spectrum**, **transfer operator** $M$, **explicit function** (trace identity), and **Fredholm determinant** $D(z)$. The §3 tables read those last two columns of the data sheet *across* objects and expose the pattern; §4 sketches the general theorem; §5 grades each step by tractability.

---

## 1. The construction as a functor (the "one construction")

```
sequence (a_n ≥ 0)
   │  damp        w_n  (geometric r^n  |  Gaussian e^{-σ²n²})
   ▼
λ_n = a_n w_n        symmetrise  λ_{-n}=λ_n
   │  Fourier
   ▼
K(θ) = Σ_n λ_{|n|} e^{inθ}        (real, even, PD by Bochner)
   │  convolution
   ▼
T_K  on  L²(𝕋)        self-adjoint, eigenpairs (λ_{|n|}, e^{inθ})
   ├───────────────┬────────────────────┬────────────────────┐
   ▼               ▼                    ▼                    ▼
spectrum {λ_n}  transfer M        explicit function     Fredholm det
                = multiplier m_n  (trace identity)      D(z)=∏(1−zλ_n)
```

The objects on $L^2(\gamma)$ (Ornstein–Uhlenbeck) join this picture through the
**intertwiner $J\colon L^2(\gamma)\to L^2(\mathbb{T})$** of Lemma O6, which carries
the OU semigroup $P_t$ to Poisson convolution $D_r$ ($r=e^{-t}$) on the even
subspace. So $\mathcal{S}$ is defined on a single category containing both the
circle objects and the Hermite/OU object.

---

## 2. Algorithm statement

**Input:**
- A sequence $(a_n)_{n \ge 0}$ with $a_n \ge 0$.
- A growth class: $a_n = O(n^\alpha)$, $O(\varphi^n)$, etc.
- A symmetry: even extension $a_{-n} = a_n$, or a twist (character, sign).
- A damping rule: geometric $w_n = r^n$, or Gaussian $w_n = e^{-\sigma^2 n^2}$.

**Output:**

| Output | Unconditional? | Depends on |
|---|---|---|
| Self-adjoint operator $T_K$ on $L^2(\mathbb{T})$ | Yes, when damped sequence is $\ell^1$ | — |
| Spectrum $\{\lambda_n\} = \{a_n w_n\}$ | Yes | — |
| Positive definiteness | Yes if $a_n \ge 0$ (Bochner) | $a_n \ge 0$ |
| Trace-class / Fredholm determinant $D(z)=\prod_n(1-z\lambda_n)$ | Yes, when $\sum\lambda_n<\infty$ | $\ell^1$ damping |
| Transfer operator $M: T^{(1)}_r \to T^{(2)}_r$ (multiplier $m_n=\lambda^{(2)}_n/\lambda^{(1)}_n$) | Case by case | $m\in\ell^\infty$ |
| Explicit function (trace identity) | Conditional | Analytic continuation of the associated $L$-function |
| Positivity criterion | Often conditional | RH or GRH for zeta / $L$-functions |

---

## 3. The three derived invariants (read across the data sheet)

The two columns added to the data sheet — **explicit function** and **Fredholm
determinant** — are not ad hoc: each is a functor of the spectrum, and its closed
form is dictated by the *arithmetic type* of $\{\lambda_n\}$.

### 3.1 Transfer operator / multiplier

For two objects with spectra $\lambda^{(1)}_n,\lambda^{(2)}_n$, the transfer
operator is the Fourier multiplier $m_n=\lambda^{(2)}_n/\lambda^{(1)}_n$. It is
bounded iff $m\in\ell^\infty$ and trace-class iff $(\lambda^{(2)}-\lambda^{(1)})\in\ell^1$.
Worked multipliers: $\eta\leftrightarrow\zeta$ is the sign twist $m_n=(-1)^{n-1}$
(rotation by $\pi$); Lucas $\leftrightarrow$ Fibonacci is $m_n=L_n/F_n\to\sqrt5$;
$L(s,\chi)\leftrightarrow\zeta$ is the Gauss-sum rotation sum.

### 3.2 Explicit function (trace identity)

The bridge between the spectral side $\sum_n F(\lambda_n)$ and an arithmetic dual.
It always specialises one of four templates:

| Trace functional | General form | Specialisations (data sheet) |
|---|---|---|
| Spectral zeta | $\zeta_T(s)=\sum_n\lambda_n^{-s}$ | $\zeta(2\sigma)$, prime zeta $P(2\sigma)$, $L(2\sigma,\chi)$ |
| Heat trace + Mellin | $\Theta(t)=\sum_n e^{-t\lambda_n}$, $\int_0^\infty t^{s-1}\Theta\,dt$ | OU: $\Gamma(s)\zeta(s)=\int_0^\infty u^{s-1}(e^u-1)^{-1}du$ |
| Reproducing kernel | $\langle\Psi_s,\Psi_{s'}\rangle=\sum_n a_n^2\,n^{-(s+\overline{s'})}$ | $\zeta(s+\overline{s'})$, $L(s+\overline{s'},\chi_1\bar\chi_2)$ |
| Weil pairing | $\sum_\gamma\hat f(\gamma)=2\hat f(\tfrac i2)-2\sum_n\tfrac{\Lambda(n)}{\sqrt n}f(\log n)+\text{arch}$ | zeros $\leftrightarrow$ primes (verified, [spectral-triple-verify.py](../../victor/spectral-triple-verify.py)) |

### 3.3 Fredholm determinant — closed form by spectrum type

$D(z)=\det(I-zT_K)=\prod_n(1-z\lambda_n)$ is entire in $z$ (order $=$ the
convergence exponent of $\{\lambda_n\}$), with zeros exactly $\{1/\lambda_n\}$. Its
closed form is a clean function of the spectrum's arithmetic type:

| Spectrum type $\lambda_n$ | Object(s) | $D(z)=\prod_n(1-z\lambda_n)$ |
|---|---|---|
| geometric $q^n$ | OU ($q=e^{-t}$) | $q$-Pochhammer $(z;q)_\infty$ |
| difference of geometrics | Fibonacci, ζ-magnitude | $q$-Pochhammer type ($q=\varphi r$ resp.\ $r$); no elementary form |
| power $n^{-2\sigma}$ | natural sine wave | order-$\tfrac1{2\sigma}$ entire fn; $\dfrac{\sin(\pi\sqrt z)}{\pi\sqrt z}$ at $\sigma=1$ |
| prime-indexed $p^{-2\sigma}$ | prime sine wave, $L(s,\chi)$ | Euler product; $1/\zeta(2\sigma)$ resp.\ $1/L(2\sigma,\chi)$ at $z=1$ |
| zero-indexed $\gamma_n r^n$ | Riemann zeros | damped $\prod_n(1-z\gamma_n r^n)$; true spectral det $=\xi(s)/\xi(0)=\prod_\rho(1-s/\rho)$ |

**Observation.** The determinant is the common invariant; the special functions
that appear elsewhere in the project ($q$-Pochhammer, $\sin$ product, Euler
product, Hadamard $\xi$) are exactly the four arithmetic regimes of $D(z)$.

---

## 4. Sketch

> **General Theorem (sketch).** Let $a=(a_n)_{n\ge0}$, $a_n\ge0$, and let $w$ be a
> damping with $\lambda_n:=a_nw_n\in\ell^1$. Then:
>
> 1. $K(\theta)=\sum_{n\in\mathbb Z}\lambda_{|n|}e^{in\theta}$ is a real, even,
>    continuous, positive-definite kernel, and $T_Kf=K*f$ is **self-adjoint and
>    trace-class** on $L^2(\mathbb T)$ with eigenpairs $(\lambda_{|n|},e^{in\theta})$.
> 2. $D(z)=\det(I-zT_K)=\prod_n(1-z\lambda_{|n|})$ is **entire** of order $\le$ the
>    convergence exponent of $\lambda$, with zero set $\{\lambda_{|n|}^{-1}\}$.
> 3. If $\lambda^{(2)}_n=m_n\lambda^{(1)}_n$ with $m\in\ell^\infty$, the **transfer
>    operator** $M$ is the Fourier multiplier $(m_n)$, bounded with $\lVert M\rVert=\lVert m\rVert_\infty$.
> 4. If the Dirichlet series $L_a(s)=\sum_n a_n n^{-s}$ continues to a meromorphic
>    function with a functional equation, the Mellin transform of the heat trace
>    $\Theta(t)=\sum_n e^{-t\lambda_n}$ yields an **explicit formula** relating
>    $\sum_n F(\lambda_n)$ to the zeros and the generalised von Mangoldt data of $L_a$.

*Proof sketch.*

- **(1)** $\ell^1$ gives absolute, uniform convergence of the Fourier series, so
  $K\in C(\mathbb T)$; evenness is the symmetrisation $\lambda_{-n}=\lambda_n$;
  positive-definiteness is Bochner ($\lambda_n\ge0$). Convolution is diagonalised
  by the Fourier basis, so $T_K$ has eigenvalues $\lambda_{|n|}$ and is
  self-adjoint; $\sum_n\lambda_n<\infty$ makes it trace-class.
- **(2)** Trace-class $\Rightarrow$ the Fredholm determinant exists
  (Grothendieck) and equals the eigenvalue product (Lidskii); the growth order is
  the exponent of convergence of $\{1/\lambda_n\}$ via the Hadamard factorisation.
- **(3)** Both $T^{(1)},T^{(2)}$ are diagonal in the Fourier basis, so their
  "ratio" is the diagonal multiplier $m_n$; boundedness $\Leftrightarrow m\in\ell^\infty$.
- **(4)** Write $\Theta(t)=\sum_n e^{-t\lambda_n}$, take its Mellin transform, and
  shift the contour past the poles coming from the continuation of $L_a$. The pole
  at $s=1$ and the trivial/archimedean factors give the smooth terms; the
  nontrivial zeros give the oscillatory sum. **This is the one step that is not
  automatic** — it needs the analytic continuation and the location of the zeros.

Each catalogue object is **(1)–(3) instantiated** with the explicit-function and
Fredholm-determinant columns of §3 as the output, and **(4) instantiated** only
where the dual $L$-function is understood (ζ, $L(s,\chi)$, prime zeta).

The spectral-triple recipe (Phase 2b) is the special case $a_n=\gamma_n$ (zero
ordinates) dual to $a_n=\Lambda(n)/\sqrt n$ (prime powers), where step (4) is the
**verified** Weil identity and the positivity of step (4)'s functional is Weil's
criterion ($\Leftrightarrow$ RH).

---

## 5. Tractability

Grading each output by how much is mechanical vs. how much is open. This is the
honest map of where the generalisation can go *now* and where it is gated.

| Tier | Meaning | Outputs in this tier |
|---|---|---|
| **A — mechanical / unconditional** | follows from $\ell^1$ damping + Bochner + the spectral theorem; no number theory needed | construction of $T_K$; spectrum; positive-definiteness; trace-class; $D(z)$ as a **convergent product**; spectral zeta $\zeta_T(s)$ in its half-plane of convergence; heat trace $\Theta(t)$ |
| **B — case-by-case but tractable** | needs the *arithmetic type* of the spectrum but no deep conjecture | **closed form** of $D(z)$ (geometric → $q$-Pochhammer, power → $\sin$ product, prime-indexed → Euler product); transfer multiplier existence/boundedness; reproducing-kernel identity $\zeta(s+\overline{s'})$ etc. |
| **C — conditional / hard** | requires continuation past convergence, zero locations, or RH/GRH | the **explicit formula** (step (4)) as an identity past $\Re s=1$; the Hadamard/$\xi$ form of $D(z)$ for the zero-indexed object; any **positivity ⟺ RH** criterion; effective zero-free regions |

**What is computable today.** Tiers A and B are fully within reach for every row
of the data sheet (the Fredholm-determinant column was filled and three of its
closed forms numerically confirmed to $\le10^{-6}$ truncation / $10^{-31}$ for the
$q$-Pochhammer). Tier C is exactly the RH-adjacent content and stays tagged
*conditional* / *heuristic*.

**Gate status (CLAUDE.md guardrail).** Phase 4 may begin once Phase 1 numerics and
the $L^2(\gamma)\to L^2(\mathbb T)$ functor are done:

| Gate dependency | Status |
|---|---|
| $L^2(\gamma)\to L^2(\mathbb T)$ functor (Lemma O6) | **Done** ([ou-process.md](../../project/ou-process.md) §4.1) |
| Phase 1c — OU §7 numerics | **Done** ([ou-verify.py](../../victor/ou-verify.py)) |
| Phase 1b — Fibonacci §6 numerics | **Open** (only remaining gate) |

So the write-up is unblocked except for the Fibonacci §6 verification; the Tier-A/B
content above can be drafted now, Tier-C deferred.

---

## 6. Deliverable outline

```
§0  Abstract inputs and outputs
§1  The recipe (damp → symmetrise → kernel) — condensed from spectral-triple.html §3
§2  Existence and self-adjointness: general theorem (Sketch §4 (1))
§3  Positive definiteness: Bochner on 𝕋
§4  Transfer operators: definition, boundedness, trace class (Sketch §4 (3))
§5  Explicit formulas: general trace identity (Sketch §4 (4))
§6  Fredholm determinant: the four arithmetic regimes (data sheet §3.3)
§7  Positivity criteria: when unconditional vs. conditional (Tractability §5)
§8  Catalogue: one paragraph per object, pointing to its full note
§9  Special case: the spectral-triple recipe recovered
§10 Open problems
```

---

## 7. Worked cases to cite

| Object | Full note | Status at time of writing |
|---|---|---|
| Prime sine wave | `project/prime-sine-wave.md` | Complete (T1–T4 + §6) |
| Natural sine wave | `project/sine-wave.md` | Complete (T1–T5 + §7) |
| Fibonacci kernel | `project/fibonacci-kernel.md` | Proofs done; §6 numerics **open** (the gate) |
| OU process | `project/ou-process.md` | Complete (O1–O6 + numerics) |
| η↔ζ transfer | `project/eta-zeta-transfer.md` | E1–E4 proved; §5 open |
| Dirichlet $L(s,\chi)$ | `project/dirichlet-series.md` | Core complete (D1–D5 + §6) |
| Spectral triple | `project/spectral-triple.md` | Transfer identity verified; positivity ⟺ RH conditional |

---

## 8. Open problems

1. **Universality of the determinant regimes.** Is every $D(z)$ arising from
   $\mathcal S$ one of the four §3.3 types, or are there intermediate (e.g.
   automorphic) spectra giving genuinely new closed forms?
2. **Step (4) without RH.** For which sequences does the explicit formula hold
   *unconditionally* (continuation only), and where is RH/GRH genuinely needed?
3. **Functoriality of $M$.** Does $\mathcal S$ send arithmetic operations on
   sequences (Dirichlet convolution, character twist) to natural operations on the
   transfer operators / determinants?
4. **The Gaussian-damping branch.** §3.3 is worked for geometric damping; redo the
   determinant taxonomy for Gaussian $w_n=e^{-\sigma^2n^2}$ (theta-type products).
