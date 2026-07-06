# references.md — the completed results `research-plan.md` builds on

*Every citation in [research-plan.md](research-plan.md) §1–§2 (the imported triage and the
in-repo record) points at a task that was finished in an earlier phase of this program. This
note collects those tasks in one place, each reconstructed from first principles — preliminaries,
construction, statement, and proof — so the charter can be read without chasing links. Nothing
here is new content: it is a faithful reassembly of
[adele/phase1.md](adele/phase1.md), [adele/phase3.md](adele/phase3.md),
[adele/phase4.md](adele/phase4.md), [adele/phase6.md](adele/phase6.md),
[berry-keating/prime-side.md](berry-keating/prime-side.md),
[prime-sieve/path.md](prime-sieve/path.md), [prime-sieve/findings.md](prime-sieve/findings.md),
and [prime-sieve/implementation.md](prime-sieve/implementation.md). Tags follow the repository
[rigour convention](CLAUDE.md) and are reproduced unchanged from the source note.*

Order follows the dependency chain research-plan.md actually uses: sieve completeness first
(everything downstream needs an enumeration of the primes), then the finite-matrix track
(attempted, diagnosed, corrected, and finally refuted as an eigenvalue map), then the trace
track (restated, proved, and realised adelically — this is what survives), then the calibration
results imported from the parallel Ihara/graph lab (positive and negative controls for
research-plan.md's gate E0/E4).

---

## 1. Sieve completeness and the equidistribution rate

*Source: [adele/phase1.md](adele/phase1.md). Cited in research-plan.md §2 row 1 and §5 (E0/E2
depend on "stage $n$ admits exactly the primes $p \le M_n$").*

### 1.1 Preliminaries

For $n \ge 1$ let $I_n = [2^n,\, 2^{n+1}-1]$, $M_n = 2^{n+1}-1$, and $\mathcal P_n$ the set of
primes $< 2^n$.

### 1.2 Construction — the composite-generator sieve

**Definition (dyadic composite generator).**
$$
G_n = \{\, x \in I_n : x = p_1 p_2 \cdots p_k,\ p_i \in \mathcal P_n,\ k \ge 2 \,\}.
$$
$G_n$ is built from *already-known* primes ($\mathcal P_n$, the output of previous blocks) —
no primality test is used.

### 1.3 Lemma 1.2 (sieve correctness) — proven

$G_n$ is exactly the set of composites in $I_n$; equivalently, the primes in $I_n$ are precisely
the gaps $I_n \setminus G_n$.

*Proof.* If $x \in I_n$ is composite it has a factor $d$ with $1 < d \le \sqrt x < 2^{(n+1)/2}
\le 2^n$, so $d$ has a prime factor $p < 2^n$, i.e. $p \in \mathcal P_n$; dividing out primes
$< 2^n$ repeatedly expresses $x$ as a product of members of $\mathcal P_n$ with $k \ge 2$
factors. Conversely, any such product is composite. $\blacksquare$

This is the sieve's defining property: primes are detected as the numbers the composite
generator *misses*. Every downstream phase's "stage $n$ has produced every prime $\le M_n$"
claim is exactly this lemma, block by block.

### 1.4 Theorem 1.3 (equidistribution rate) — proven

Let $k_n = \pi(M_n)$ and form the normalised empirical prime measure on $\mathbb T = [0,1)$,
$$
\mu_n = \frac1{k_n}\sum_{p \le M_n} \delta_{\{p/M_n\}}.
$$
For each fixed $k \ne 0$,
$$
\widehat\mu_n(k) = \frac1{k_n}\sum_{p\le M_n} e^{2\pi i k p / M_n} = O_k\!\Big(\frac1{\log M_n}\Big).
$$

*Proof sketch.* Summation by parts against $\pi(t)$ with the PNT error term
$\pi(t) = \mathrm{li}(t) + O(t\,e^{-c\sqrt{\log t}})$; the smooth $\mathrm{li}$ part integrates
to $O(1/\log M_n)$ after division by $k_n \sim M_n/\log M_n$, and the PNT error term is smaller.
(Full proof: [berry-keating/prime-sieve.html](berry-keating/prime-sieve.html) Theorem 3.1.)

**Why it matters (the design consequence used everywhere downstream).** Equidistribution says
the normalised *positions* of primes on the circle carry only Lebesgue density in the limit —
all arithmetic information migrates into the *multiplicative* data $\{\log p\}$ and the von
Mangoldt weights. This is why every operator built later (§5 below) is built from $\log p$ and
$\Lambda$, never from prime positions, and why a normalised prime sum collapses to nothing (this
is constraint C2 of §5.1 below).

### 1.5 Numerical record (reproduced from `sieve_operator.py::phase1_report`)

```
  n       M_n  k_n=pi(M_n)    |mu(1)|    |mu(2)|    |mu(3)| |mu(1)|*logM_n
  8       511           97    0.09758    0.05782    0.04455         0.6085
 10      2047          309    0.07185    0.04895    0.04906         0.5478
 12      8191         1028    0.06106    0.04097    0.03659         0.5502
 14     32767         3512    0.05262    0.03604    0.02975         0.5471
 16    131071        12251    0.04603    0.03056    0.02394         0.5424
 18    524287        43390    0.04054    0.02652    0.01982         0.5339
 20   2097151       155611    0.03591    0.02316    0.01736         0.5227
```

The last column stays in $[0.52, 0.61]$ across $2^8$–$2^{21}$ while $|\widehat\mu_n(1)|$ itself
falls $2.7\times$ — a clean confirmation of the $\Theta(1/\log M_n)$ rate.

Task status: Lemma 1.2 and Theorem 1.3 are both **proven**; Phase 1 has no open mathematical
problem and is the one fully solid pillar everything downstream is measured against.

---

## 2. The naive Sieving Laplacian: its vacuity, and its correction

*Source: [adele/phase3.md](adele/phase3.md). Cited in research-plan.md §2 row 2 and §3.2(a) as
the "legacy comparator" $H_n'$ — the negative control gate E0 must reject.*

### 2.1 Preliminaries — the plan's original construction

On $V_n = \{\text{primes } p \in I_n\}$ and $W_n = \{\text{composites } m \in I_n\}$, the
original plan (Definition 4.1) sets
$$
A_{p,q} = \sum_{m \in W_n} \frac{a_p(m)\,a_q(m)}{\mathrm{rad}(m)}\,\delta_{p\ne q},\qquad
D_n = \mathrm{diag}\Big(\log p - \tfrac1{N_n}\textstyle\sum_q \log q\Big),\qquad
H_n = D_n + \varepsilon_n A,\ \ \varepsilon_n = \frac{c}{\log M_n},
$$
with $a_p(m)$ the exponent of $p$ in $m$. The intended mechanism: off-diagonal $A$ supplies
"level repulsion" shifting the raw eigenvalues $\log p$ toward the Riemann zeros.

### 2.2 Proposition 3.1 (vacuity) — proven

With $V_n = \{\text{primes in } I_n\}$ as in Definition 4.1, $A = 0$ identically, hence
$H_n = D_n$ for every $n$.

*Proof.* A term $a_p(m)a_q(m)$ with $p \ne q$ is nonzero only if $m$ is divisible by two
distinct primes $p, q \in V_n$, i.e. $p, q \ge 2^n$. Then $m \ge pq \ge 2^n\cdot 2^n = 2^{2n}$.
But $m \in I_n$ means $m < 2^{n+1}$, and $2^{2n} \ge 2^{n+1}$ for all $n \ge 1$ — contradiction.
So no $m \in W_n$ contributes any off-diagonal entry. $\blacksquare$

Numerical confirmation (`sieve_operator.py::phase3_report`): $\lVert A\rVert_{\mathrm{op}} =
0.0000$ at every tested $n$, and $\mathrm{Spec}(H_n) = \mathrm{Spec}(D_n)$ is completely
insensitive to the coupling strength.

### 2.3 Definition 3.2 (corrected Sieving Laplacian) — construction

Take the basis $V_n' = \{\text{primes } p < 2^n\} = \mathcal P_n$ (Phase 1's sieve primes,
§1.2). For composites $m \in I_n$,
$$
A'_{p,q} = \sum_{m \in W_n} \frac{a_p(m)\,a_q(m)}{\mathrm{rad}(m)}\,\delta_{p\ne q},\qquad
p, q \in \mathcal P_n,
$$
and $H_n' = D_n' + \varepsilon_n A'$ with $D_n' = \mathrm{diag}(\log p)_{p < 2^n}$
(recentred). Now $m = pq\cdots$ with $p,q < 2^n$ and $pq \in [2^n, 2^{n+1})$ is perfectly
possible, so $A' \ne 0$ — the basis change from "primes in the current block" to "all
generator primes below the block" is what repairs the vacuity of §2.2.

**Numerical check** (`repair_report`): $\lVert A'\rVert_{\mathrm{op}}$ grows from $9.27$ ($n=8$)
to $64.71$ ($n=14$), empirically $\lVert A'\rVert \sim 2^{n/2}$, because $A'$ sums over
$\sim 2^n$ composites on a basis of only $\sim 2^n/n$ primes.

**The normalisation correction.** The plan's own $\varepsilon_n = c/\log M_n$ was calibrated for
a *small* perturbation of $D_n$, but here $\varepsilon_n\lVert A'\rVert$ climbs unboundedly
($1.5 \to 6.2$ across the tested range). The fix is to normalise by the operator norm itself,
$$
\varepsilon_n = \frac{c}{\lVert A'\rVert} = O(2^{-n/2}),
$$
so $\varepsilon_n \lVert A'\rVert \equiv c$ stays bounded and $H_n' = D_n' + \varepsilon_n A'$ is
a well-defined, bounded self-adjoint perturbation of $D_n'$ for every $n$. With this
normalisation, Definition 3.2 is the non-vacuous, correctly-scaled Sieving Laplacian.

### 2.4 Theorem 3.3 (density mismatch) — proven, imported

Even a well-normalised $H_n'$ cannot have the zeros as eigenvalues, for a reason independent of
the choice of $A$: the spectrum $\{\log p\}$ (and any bounded perturbation of it on a comparable
basis) has counting function $N_A(T) \sim e^T/T$, growing exponentially; the zeros have
$N(T) \sim \frac{T}{2\pi}\log\frac{T}{2\pi}$, growing like $T\log T$. No unitary conjugation and
no affine rescaling $aA+b$ maps one counting asymptotic to the other.

*Proof (full statement imported from [berry-keating/prime-side.md](berry-keating/prime-side.md)
Proposition 3.7 — reproduced in full in §5.7 below).* The $k=1$ layer of $\sigma(A)$ contributes
$\pi(e^T) = \frac{e^T}T(1+O(1/T))$ eigenvalues below $T$ (PNT), and higher powers add at most
$O(e^{T/2}T)$; both are exponential in $T$. The zero-counting function is $\frac{T}{2\pi}
\log\frac T{2\pi e} + O(\log T)$ (Riemann–von Mangoldt). An exponential and a $T\log T$ counting
function disagree for all large $T$ under any affine rescaling, so the two spectra differ as
sets, however the basis or coupling is chosen. $\blacksquare$

**Numerical confirmation** (`phase4_report`, $n=14$, $N=1612$): the best affine fit of
$\mathrm{Spec}(H_{14})$ onto the first $1612$ zeros has RMS residual $14.7$ — the same order as
the first zero itself; the first six "fitted" values sit near $50$–$56$ while the first six
zeros are $14$–$38$. There is no convergence to unfold.

**Consequence used by research-plan.md.** This theorem is why the working object of the
continued program is *not* "an $H_n$ whose eigenvalues are the zeros" but the sieve-Galerkin
compression $H^G_n = P_n D P_n$ of the adelic operator $D$ (research-plan.md §3.2(c)), and why
$H_n'$ is kept only as the negative control gate E0 must reject.

---

## 3. The logical gap: weak spectral convergence is not Hilbert–Pólya

*Source: [adele/phase4.md](adele/phase4.md) §4.2. Cited in research-plan.md §2 row 4 as a
"binding logical note," and underlies obstruction O3/K2 of the continued plan.*

The plan's original Conjecture 5.1 asserted that the rescaled eigenvalue-counting measure of
$H_n$ converges weakly to the distribution $d\Xi$ of the zero ordinates:
$$
\lim_{n\to\infty}\frac1{N_n}\sum_{\lambda\in\mathrm{Spec}(H_n)}
f\!\Big(\frac{\lambda-\mu_n}{\sigma_n}\Big) = \int_{\mathbb R} f(t)\,d\Xi(t),\qquad
f \in C_c^\infty.
$$

**The objection.** Even if this held, it is a statement about the *statistics* of the spectrum
(a normalised counting measure converging to a density), not about individual eigenvalues — in
the spirit of GUE universality. It would say "$H_n$ has roughly the right density of levels";
it would **not** exhibit a self-adjoint operator whose spectrum *equals* $\{\gamma_\rho\}$.
Density matching is necessary for a Hilbert–Pólya realization but nowhere near sufficient, and
the repository's rigour convention forbids treating it as progress toward RH for exactly this
reason.

**Consequence used by research-plan.md.** This is the reason gate E0 (density) is explicitly
*not* accepted as a success criterion on its own — it is a first, cheap, necessary filter, with
the real content sitting in gates E2/E3 (pollution-free spectral convergence) and E5 (the
positivity wall), per obstruction O3 of research-plan.md §4.

---

## 4. The prime-side trace identity: RKHS, flow, generator, weight

*Source: [berry-keating/prime-side.md](berry-keating/prime-side.md) §2–3, imported wholesale by
[adele/phase4.md](adele/phase4.md) as Theorem 4.1. This is the unconditional package that gives
Theorem 4.1/4.2 of §5 below their content.*

### 4.1 Preliminaries

The Guinand–Weil explicit formula pairs a **zero side** $\sum_\rho h(\gamma_\rho)$ (spectral
data of an operator nobody has constructed) with a **prime side**
$\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}(g(\log n)+g(-\log n))$ plus archimedean terms
(arithmetic data, unconditionally available). The goal of this section is to realise the prime
side as a genuine operator trace.

Three design constraints, all proven in the companion notes, fix the shape of the
construction:

- **(C1) No normalisation.** $1/\pi(M_n)$-normalised prime sums tend to zero uniformly
  (elementary Chebyshev estimate) — every object below is an unnormalised, absolutely
  convergent sum.
- **(C2) Positions are flat; structure lives in the logarithms.** This is Theorem 1.3 of §1.4
  above: $\widehat\mu_n(k) = O_k(1/\log M_n) \to 0$. All arithmetic content must be drawn from
  the unnormalised multiplicative data $\{\log q\}$ and their weights.
- **(C3) Constructivity.** The sieve enumerates the primes exactly, block by block (Lemma 1.2 of
  §1.3), at the quantitative rate of Theorem 1.3 — the package must be recoverable as a limit of
  finite stages with controlled error (this is §5 below).

### 4.2 Construction — the von Mangoldt kernel and its RKHS

**Definition 2.1.** Let $\mathcal Q = \{p^k : p \text{ prime}, k \ge 1\}$ be the prime powers,
$\Lambda(p^k) = \log p$, and
$$
\ell^2_\Lambda = \Big\{ x = (x_q)_{q\in\mathcal Q} : \lVert x\rVert_\Lambda^2 :=
\sum_{q\in\mathcal Q}\Lambda(q)\lvert x_q\rvert^2 < \infty\Big\},\qquad
\langle x,y\rangle_\Lambda = \sum_q \Lambda(q)\,x_q\overline{y_q}.
$$

**Lemma 2.2 (well-definedness) — proven.** For $\lambda \in \mathbb C^+$ let
$v_\lambda = (q^{-1/2+i\lambda})_{q\in\mathcal Q}$. Then $v_\lambda \in \ell^2_\Lambda$,
$\lambda \mapsto v_\lambda$ is holomorphic $\mathbb C^+ \to \ell^2_\Lambda$, and
$$
\lVert v_\lambda\rVert_\Lambda^2 = \sum_q \Lambda(q)\,q^{-1-2\,\mathrm{Im}\,\lambda}
= -\frac{\zeta'}{\zeta}(1+2\,\mathrm{Im}\,\lambda).
$$

*Proof.* $|q^{-1/2+i\lambda}|^2 = q^{-1-2\,\mathrm{Im}\,\lambda}$, and $\sum_q \Lambda(q)q^{-s} =
-\zeta'/\zeta(s)$ is the classical Dirichlet series, absolutely convergent for
$\mathrm{Re}\,s > 1$ (here $s = 1+2\,\mathrm{Im}\,\lambda > 1$). Holomorphy is termwise
differentiation of a locally uniformly dominated series. $\blacksquare$

**Definition–Proposition 2.3 (the von Mangoldt kernel) — proven.** For $\lambda,\mu\in\mathbb
C^+$,
$$
K_\Lambda(\lambda,\mu) := \langle v_\lambda, v_\mu\rangle_\Lambda =
\sum_{q\in\mathcal Q}\Lambda(q)\,q^{-1+i(\lambda-\bar\mu)} =
-\frac{\zeta'}{\zeta}\big(1-i(\lambda-\bar\mu)\big),
$$
and $K_\Lambda$ is positive semi-definite on $\mathbb C^+\times\mathbb C^+$.

*Proof.* With $u=\lambda-\bar\mu$, $\mathrm{Re}(1-iu) = 1+\mathrm{Im}\,\lambda+\mathrm{Im}\,\mu>1$,
so the Dirichlet series identity applies term by term. Positivity is automatic for a Gram
kernel: $\sum_{i,j}c_i\bar c_j K_\Lambda(\lambda_i,\lambda_j) = \lVert\sum_i c_i
v_{\lambda_i}\rVert_\Lambda^2 \ge 0$. $\blacksquare$

(Totality of $\{v_\lambda\}$ in $\ell^2_\Lambda$ — Lemma 2.4 — and the resulting RKHS
$\mathcal H_\Lambda$ — Definition 2.5 — complete the construction of ingredient (i); omitted here
as research-plan.md does not directly cite them, but they underwrite Theorem 3.4 below.)

### 4.3 Construction — the translation flow, its generator, and the trace identity

**Proposition 3.1 (translation flow and generator) — proven.** The shift $(U_tF)(\lambda) =
F(\lambda+t)$ on $\mathcal H_\Lambda$ corresponds to the diagonal unitary group
$(\Lambda_t x)_q = q^{it}x_q$ on $\ell^2_\Lambda$. This group is strongly continuous; its
self-adjoint generator is
$$
(Ax)_q = (\log q)\,x_q,\qquad \mathcal D(A) = \Big\{x : \sum_q\Lambda(q)(\log q)^2|x_q|^2<\infty\Big\},
$$
with pure point spectrum $\sigma(A) = \{\log q : q\in\mathcal Q\} = \{k\log p\}$, every
eigenvalue simple, no further spectrum in any bounded interval.

*Proof.* Simplicity: $\log q$ are pairwise distinct across $\mathcal Q$ because $p^k=p'^{k'}$
forces $p=p'$, $k=k'$ by unique factorisation. Discreteness: every bounded interval contains
finitely many prime powers, so $\sigma(A)$ is closed and discrete, each point an isolated simple
eigenvalue with eigenvector $\delta_q$; Stone's theorem identifies the generator. $\blacksquare$

**Remark 3.2 (the weights are spectral data).** Since $\sigma(A)$ is simple pure point, every
diagonal operator is a Borel function of $A$; in particular the weight operator below is
$W=w(A)$ with $w(k\log p) = \Lambda(p^k)/\sqrt{p^k} = (\log p)e^{-k\log p/2}$.

**Lemma 3.3 (diagonal trace-class criterion) — proven.** A diagonal operator $D$ on
$\ell^2_\Lambda$ with entries $(d_q)$ is trace class iff $\sum_q|d_q|<\infty$, and then
$\mathrm{Tr}\,D = \sum_q d_q$.

*Proof.* The vectors $e_q = \delta_q/\sqrt{\Lambda(q)}$ form an orthonormal basis and
$De_q = d_q e_q$, so the singular values of $D$ are $\{|d_q|\}$ and, when the sum converges
absolutely, $\mathrm{Tr}\,D = \sum_q\langle De_q,e_q\rangle_\Lambda = \sum_q d_q$. $\blacksquare$

**Theorem 3.4 (prime-side trace identity) — proven.** Let $W=w(A)\ge0$ as above and let
$g:\mathbb R\to\mathbb C$ be Borel with $|g(x)|\le Ce^{-(1/2+\varepsilon)x}$ on $x\ge\log2$ for
some $\varepsilon>0$. Then $W^{1/2}g(A)W^{1/2}$ is trace class and
$$
\mathrm{Tr}\big(W^{1/2}g(A)W^{1/2}\big) = \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,g(\log n),
\qquad
\big\lVert W^{1/2}g(A)W^{1/2}\big\rVert_{\mathrm{tr}} \le C\cdot\Big(-\frac{\zeta'}{\zeta}(1+\varepsilon)\Big).
$$

*Proof.* $W^{1/2}g(A)W^{1/2}$ is diagonal with entries $\frac{\Lambda(q)}{\sqrt q}g(\log q)$, and
$$
\sum_q\frac{\Lambda(q)}{\sqrt q}|g(\log q)| \le C\sum_q\Lambda(q)q^{-1-\varepsilon} =
C\Big(-\frac{\zeta'}{\zeta}(1+\varepsilon)\Big) < \infty.
$$
Apply Lemma 3.3; the trace is the stated sum, running over all $n\ge2$ with $\Lambda(n)\ne0$.
$\blacksquare$

**Definition 3.5 (the symmetric double).** $\mathbb A = A\oplus(-A)$, $\mathbb W = W\oplus W$ on
$\ell^2_\Lambda\oplus\ell^2_\Lambda$, self-adjoint with simple pure point spectrum
$\{\pm k\log p\}$. For $g$ Borel with $|g(x)|\le Ce^{-(1/2+\varepsilon)|x|}$, applying Theorem
3.4 to each summand gives the arithmetic Weil functional as a trace:
$$
\mathrm{Tr}\big(\mathbb W^{1/2}g(\mathbb A)\mathbb W^{1/2}\big) =
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\big(g(\log n)+g(-\log n)\big) =: \mathcal W_{\mathrm{ar}}(g).
$$

This is exactly the object [adele/phase4.md](adele/phase4.md) cites as **Theorem 4.1** — the
proven trace identity that replaces the refuted eigenvalue-to-zero conjecture (§2.4 above).

### 4.4 The classical explicit formula, as a trace

**Fact 4.1 (Guinand–Weil explicit formula) — classical, cited.** Let $h$ be even, holomorphic
on $|\mathrm{Im}\,r|\le\tfrac12+\delta$, with $h(r)\ll(1+|r|)^{-2-\delta}$ there, and
$g(x)=\frac1{2\pi}\int h(r)e^{-irx}dr$. Then, with $\rho=\tfrac12+i\gamma_\rho$ running over the
nontrivial zeros with multiplicity,
$$
\sum_\rho h(\gamma_\rho) = h\big(\tfrac i2\big)+h\big(-\tfrac i2\big) - g(0)\log\pi +
\frac1{2\pi}\int h(r)\,\mathrm{Re}\,\frac{\Gamma'}{\Gamma}\Big(\tfrac14+\tfrac{ir}2\Big)dr -
2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(\log n).
$$
(Guinand 1948; Weil 1952; Montgomery–Vaughan Thm 12.13; Iwaniec–Kowalski Thm 5.12. Verified
numerically to $2\times10^{-31}$ — reproduced in §5.6 below.)

**Corollary 4.2 (the explicit formula's prime side as an operator trace) — proven, given Fact
4.1.** For $h,g$ as in Fact 4.1,
$$
\sum_\rho h(\gamma_\rho) = h\big(\tfrac i2\big)+h\big(-\tfrac i2\big) - g(0)\log\pi +
\frac1{2\pi}\int h(r)\,\mathrm{Re}\,\frac{\Gamma'}{\Gamma}\Big(\tfrac14+\tfrac{ir}2\Big)dr -
\mathrm{Tr}\big(\mathbb W^{1/2}g(\mathbb A)\mathbb W^{1/2}\big).
$$

*Proof.* It suffices that $g$ lie in the trace class of Definition 3.5 with $\varepsilon=\delta$.
Shift the contour in $g(x)=\frac1{2\pi}\int h(r)e^{-irx}dr$ to $\mathrm{Im}\,r =
\mp(\tfrac12+\delta)$ (legitimate by strip holomorphy and decay of $h$):
$|g(x)|\le e^{-(1/2+\delta)|x|}\cdot\frac1{2\pi}\int|h(\xi\mp i(\tfrac12+\delta))|d\xi$. Since $g$
is even, $2\sum_n\frac{\Lambda(n)}{\sqrt n}g(\log n) = \mathcal W_{\mathrm{ar}}(g) =
\mathrm{Tr}(\mathbb W^{1/2}g(\mathbb A)\mathbb W^{1/2})$ by Theorem 3.4/Definition 3.5.
$\blacksquare$

**Reading, used throughout research-plan.md.** The prime side is now the trace of a
*constructed* self-adjoint package $(\mathbb A,\mathbb W)$; the zero side is still only a sum —
the spectral data of an operator that does not yet exist. Weil's criterion says RH is equivalent
to the positivity $\sum_\rho h(\gamma_\rho)\ge0$ for admissible $h$; by Corollary 4.2 that
positivity is a statement about this prime-side trace plus explicit archimedean terms — proven
equivalent to RH, not a route around it. This is the origin of research-plan.md's obstruction O4
/ gate E5 (the wall, priced not attacked).

---

## 5. Truncation-rate convergence: the sieve produces the trace, with a proven error bound

*Source: [berry-keating/prime-side.md](berry-keating/prime-side.md) §6 Proposition 6.1, cited as
**Theorem 4.2** in [adele/phase4.md](adele/phase4.md). This is what research-plan.md §3.2(c) and
§5 gate E4a mean by "trace-consistency at the proven $M_n^{-\varepsilon}$ rate."*

**Proposition 6.1 (stage-$n$ approximation) — proven.** Let $M_n = 2^{n+1}-1$. After stage $n$
of the composite-generator sieve, the set $\mathcal Q\cap[2,M_n]$ is known exactly (primes by
Lemma 1.2 of §1.3; prime powers as powers of the listed primes). Let $P_n$ be the orthogonal
projection of $\ell^2_\Lambda$ onto $\mathrm{span}\{\delta_q : q\le M_n\}$ and $A_n=P_nAP_n$,
$W_n=P_nWP_n$ (finite rank $\#(\mathcal Q\cap[2,M_n])$). Then:

1. $A_n \to A$ in the strong resolvent sense, and $\sigma(A_n) = \{\log q : q\le M_n\}\cup\{0\}$
   exhausts $\sigma(A)$ from below.
2. For $g$ as in Theorem 3.4 (§4.3), the stage-$n$ trace has quantitatively controlled error:
$$
\Big|\mathrm{Tr}\big(W^{1/2}g(A)W^{1/2}\big) - \mathrm{Tr}\big(W_n^{1/2}g(A_n)W_n^{1/2}\big)\Big|
\le C\sum_{q>M_n}\Lambda(q)q^{-1-\varepsilon} \le C\,c\,\frac{1+\varepsilon}\varepsilon\,M_n^{-\varepsilon},
$$
with $c$ the Chebyshev constant in $\psi(x)\le cx$.

*Proof.* (1) For $\mathrm{Im}\,z\ne0$ and $x\in\ell^2_\Lambda$, $(A_n-z)^{-1}x - (A-z)^{-1}x$ is
supported on coordinates $q>M_n$ with entries $\big(\frac{-1}z - \frac1{\log q - z}\big)x_q$,
bounded by $(|z|^{-1}+|\mathrm{Im}\,z|^{-1})|x_q|$; the tail of $x$ vanishes, giving strong
resolvent convergence.
(2) The difference of traces is, in absolute value, at most $C\sum_{q>M_n}\Lambda(q)q^{-1-\varepsilon}$.
Writing the sum as a Stieltjes integral against $\psi(t)=\sum_{q\le t}\Lambda(q)$ and integrating
by parts,
$$
\int_{M_n}^\infty t^{-1-\varepsilon}d\psi(t) = -M_n^{-1-\varepsilon}\psi(M_n) +
(1+\varepsilon)\int_{M_n}^\infty\psi(t)t^{-2-\varepsilon}dt \le c\,\frac{1+\varepsilon}\varepsilon\,M_n^{-\varepsilon},
$$
using $\psi(t)\le ct$ (Chebyshev) and dropping the negative boundary term. $\blacksquare$

**Proposition 3.7 (rigidity: the counting-function proof behind Theorem 3.3 of §2.4) — proven.**
(i) If a self-adjoint $B$ on $\ell^2_\Lambda$ satisfies $e^{itB}=e^{itA}$ for all $t$, then
$B=A$. (ii) With $N_A(T)=\#(\sigma(A)\cap[0,T])$ and $N(T)$ the zero-counting function,
$$
N_A(T) = \sum_{k\ge1}\pi(e^{T/k}) = \frac{e^T}T(1+O(1/T)),\qquad
N(T) = \frac T{2\pi}\log\frac T{2\pi e} + O(\log T)
$$
(prime number theorem; Riemann–von Mangoldt). No unitary conjugation or affine rescaling
identifies the two counting asymptotics.

*Proof.* (i) Differentiate strongly at $t=0$ on the common core of finitely supported vectors.
(ii) The $k=1$ term of $N_A$ is $\pi(e^T)=\frac{e^T}T(1+O(1/T))$ by PNT; $k\ge2$ terms total at
most $O(e^{T/2}T)$. An exponential and a $T\log T$ counting function disagree for large $T$
under any affine map, so the spectra differ as sets. $\blacksquare$

This is the precise content research-plan.md §2 row 3 cites as "Thm 3.3" and is why the
eigenvalue-to-zero program was abandoned in favour of the trace program (§4 above) and its
adelic realisation (§6 below).

Numerical record (`sieve_operator.py::repaired_trace_report`, Gaussian test $g$ at $t=0.2$):
$\mathrm{Tr}\,g(H_n')$ diverges with matrix dimension ($16.7\to632.6$ across $n=8\ldots14$) and
has nothing to do with the arithmetic side of the explicit formula (the constant
$0.603035\ldots$) — confirming that no finite matrix on prime *positions* computes the
explicit-formula trace, which is the motivation for moving to the adelic construction of §6.

---

## 6. The adelic place-by-place Weil trace (Connes 1999), verified to $10^{-36}$

*Source: [adele/phase6.md](adele/phase6.md). Cited in research-plan.md §2 row 5 and used as
gate E4a's target throughout §5 of the charter.*

### 6.1 Preliminaries — why the finite-matrix approach was the wrong vehicle

§2–5 above show: the vacuous operator is repaired (§2.3), the repair still cannot map
eigenvalues to zeros (§2.4/§5), and even its *trace* diverges with dimension and is
disconnected from the arithmetic side (end of §5). The reason is structural: the explicit-formula
trace is not $\sum_i g(\lambda_i)$ over a finite spectrum — it is a sum of *local distributions*,
one per place of $\mathbb Q$. The fix is to move to the space where those distributions live.

### 6.2 Construction — the trace on $X = \mathbb A_{\mathbb Q}/\mathbb Q^\times$

Connes (1999) realises the Weil explicit formula as the trace of the scaling action of the idèle
class group $C_{\mathbb Q} = \mathbb I_{\mathbb Q}/\mathbb Q^\times$ on functions over the adèle
class space $X$. The trace factors over the places $v$ of $\mathbb Q$ into local principal-value
integrals:
$$
\underbrace{\sum_\rho h(\gamma_\rho)}_{\text{spectral side}} =
\underbrace{W_\infty(g)}_{\text{archimedean place}} - \underbrace{\sum_p W_p(g)}_{\text{finite places = the sieve}},
$$
with local terms
$$
W_p(g) = \int_{\mathbb Q_p^\times}{}'\frac{g(|u|)}{|1-u|_p}\,d^*u =
2\sum_{k\ge1}\frac{\log p}{p^{k/2}}g(k\log p),
$$
$$
W_\infty(g) = h\big(\tfrac i2\big)+h\big(-\tfrac i2\big) - g(0)\log\pi +
\frac1{2\pi}\int h(r)\,\mathrm{Re}\,\frac{\Gamma'}{\Gamma}\Big(\tfrac14+\tfrac{ir}2\Big)dr.
$$

The finite-place term $W_p$ is a single prime's full prime-power contribution, evaluating exactly
to the von Mangoldt block $\Lambda(p^k)/p^{k/2}$; $\sum_p W_p(g) = 2\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}g(\log n)$ is a genuine sum *over places*, not over a basis of vectors
— there is no finite Hilbert space and no matrix $H_n$ at all. (This is the same object proven,
from the Hilbert-space side, to be a trace in §4.3's Theorem 3.4/Definition 3.5; here it is
organised geometrically.)

**Where the sieve enters.** The finite places of $\mathbb Q$ are the primes. The
composite-generator sieve of §1 enumerates them exactly, block by block $I_n = [2^n,2^{n+1})$,
so "compute the geometric side to stage $n$" means "sum $W_p$ over the primes the sieve has
output by stage $n$."

### 6.3 Numerical verification

**(a) The geometric side, place by place** (`adele_trace.py::place_breakdown`, $t=0.2$):

```
     place                  local term W_v(g)
  infinity     0.60303464961426464498    (pole + Gamma integral)
         2             0.38013321408074931683
         3             0.17810905607029957823
         5            0.035638958359344853761
         7           0.0081635277715376329746
        11          0.00068961339521426152495
       ...          (decaying like p^{-1/2} g(log p))
     sum p             0.60303464960929003883    (arithmetic side, p<=97)
```

**(b) Explicit-formula balance** (`balance_report`), reproducing prime-side.md §7E adelically:

```
  t = 0.05
    right side  W_inf - arithmetic  : 0.00009175670097147148537
    zero side   sum_rho h(gamma)    : 0.00009175670097147148537
    discrepancy                     : 7.9e-37

  t = 0.2
    right side  W_inf - arithmetic  : 8.860364360447289769e-18
    zero side   sum_rho h(gamma)    : 8.8603643604472897685e-18
    discrepancy                     : 4.5e-37
```

Geometric and spectral sides agree to $\sim10^{-36}$ at 35-digit precision.

**(c) Sieve truncation rate** (`truncation_rate`), realising Proposition 6.1 (§5) adelically:

```
    n       M_n       |error|  |error|*M_n^eps
    8       511    0.088009003        1.9894707
   12      8191    0.022115086        2.0015069
   16    131071   0.0055239611        1.9998799
   20   2097151   0.0013810483        1.9999711
```

$|\text{error}|\cdot M_n^{1/2}\to2.0$: the sieve produces the geometric side stage by stage with
a controlled $M_n^{-1/2}$ error.

### 6.4 What this fixes, and what it does not

**Fixes.** The vacuous/ill-scaled finite operator (§2) is replaced by a well-defined, convergent
object living on $X$: the geometric side of the Connes trace formula, computed one place at a
time, with the sieve supplying the places and a proven truncation rate.

**Does not.** This is still the *prime/geometric* side of a duality. It equals the zero side by
the explicit formula (verified above), but that identity is Guinand–Weil, not a construction of a
self-adjoint operator whose spectrum *is* $\{\gamma_\rho\}$. RH remains encoded, equivalently, in
the boundary regularity of the flow character $\chi_W(z) = -\zeta'/\zeta(\tfrac12-iz)$
(§4.4 reading) — undecided. This is exactly what research-plan.md's §3.1 means by "no step of
this plan may quietly assume the answer": the target $D$'s spectrum on the Hilbert-space ambient
being "all zeros" is still the open, RH-equivalent statement (K1 in research-plan.md §1).

---

## 7. Meyer's unconditional realization on nuclear non-Hilbert spaces

*Source: cited in [prime-sieve/path.md](prime-sieve/path.md) P4 and
[berry-keating/research-findings.md](berry-keating/research-findings.md) §7.3. Used in
research-plan.md as the calibration ("Meyer is the standing category-change detector") behind
obstruction O4 and gate E5, and behind the do-not-list item "no silent category change."*

This is an imported classical result (Meyer, *Duke Math. J.* 127 (2005) 519–595); the repository
does not reprove it, only cites and uses its statement as a calibration point. Stated as
recorded in research-findings.md §7.3:

**Meyer's theorem (2005) — proven (classical, cited).** The flow on suitable *nuclear*
(non-Hilbert) function spaces over the adèle class space realises **all** nontrivial zeros of
$\zeta$, with multiplicity, unconditionally — no hypothesis is needed.

**Why this calibrates every claim in this program.** Connes' *semi-local* trace formula (§6
above) is proven; the *global* Hilbert-space version of the same statement — "spectrum of a
self-adjoint operator on a genuine Hilbert space equals $\{\gamma_\rho\}$ exactly" — is
equivalent to Weil positivity, hence to RH (§4.4's reading of Corollary 4.2). Meyer's theorem
shows that dropping the Hilbert-space requirement (moving to a nuclear space) removes the
obstruction entirely: an unconditional spectral realization of *all* zeros already exists. This
proves that **positivity, not spectral realization per se, is the entire remaining content** of
the Hilbert–Pólya problem. Consequently: any construction in this program that claims a
spectral "success" without a Hilbert-space structure carrying a positive inner product has
silently changed category to Meyer's (already unconditional, already known) result, not made
progress toward RH. This is exactly the discipline research-plan.md §5 (gate E5) and §8
(do-not-list) enforce.

---

## 8. Connes–Moscovici's prolate wave operator

*Source: cited in [prime-sieve/path.md](prime-sieve/path.md) P4, referenced in research-plan.md
§3.3 (E0a design law) as the model for the archimedean window's Weyl-law shape.*

Imported classical result (Connes–Moscovici, *PNAS* 119 (2022) e2123174119); cited, not
reproved. As recorded in path.md P4(b):

**Connes–Moscovici (2022) — proven neighbour, cited.** A concrete self-adjoint operator (the
prolate wave operator, the archimedean/time-band-limiting fiber of the adelic construction)
whose negative spectrum matches the squares of the low Riemann zeros numerically, with a
**proven semiclassical counting match** to $N(T)$. Exact spectral identification with the zeros
remains open/conjectural.

**Why research-plan.md relies on it.** Gate E0a of the continued program requires the
archimedean window of the sieve-Galerkin compression $H^G_n$ (research-plan.md §3.2(c)) to
reproduce the $\frac T{2\pi}\log\frac T{2\pi}$ Weyl-law shape "with zero fitted parameters." The
Connes–Moscovici result is the proven precedent that a genuinely self-adjoint archimedean
operator (built from dilation/band-limiting structure, not fitted to $N(T)$) can carry the
correct semiclassical counting law unconditionally — it is the reason E0a is stated as
attainable rather than aspirational, and it fixes the model (prolate/time-band-limited
structure) research-plan.md's archimedean window is designed to instantiate. It is *not* itself
evidence about exact zero locations (E0's density gate is deliberately weaker than, and
insufficient for, a Hilbert–Pólya claim — §3 above).

---

## 9. Graph/divisor operator spectra are block-structural, not arithmetic

*Source: [prime-sieve/findings.md](prime-sieve/findings.md) F4 (measurement), calibrated by
path.md P3.2 (the graph-Siegel dictionary, heuristic). Cited in research-plan.md §2 row 8 and
§3.2(b), fixing the role of the bipartite divisor graph as toolkit, not the eigenvalue map.*

### 9.1 Preliminaries — the bipartite divisor graph

Vertex classes $\mathcal P_n = \{\text{primes } p<2^n\}$ and $\mathcal C_n = \{\text{composites }
m\in I_n\}$; edge $p\sim m$ iff $p\mid m$, weighted $w_\beta(p,m)=a_p(m)p^{-\beta}$ ($\beta=
\tfrac12$ default). Its weighted non-backtracking (Hashimoto) operator $B_n^{\mathrm{nb}}$ has
stage polynomial $\det(I-uB_n^{\mathrm{nb}})$.

### 9.2 Measurement (`prime_graph_lab.py`, run 5 Jul 2026)

```
    n    #eigs   mu1       #detached  #detached-real   detached real list
     6     218     3.542         4           2       [±3.542]   (bipartite mirror: yes)
     7     476     5.281         4           2       [±5.281]
     8    1010     7.687         4           2       [±7.687]
     9    2146    10.966         4           2       [±10.966]
```

At every stage exactly **4** eigenvalues of the weighted non-backtracking operator detach from
the $\sqrt{\mu_1}$ bulk disk: the Perron eigenvalue, its bipartite mirror $-\mu_1$ (both real),
and one complex-conjugate pair. No other real eigenvalue ever detaches. Tag: measurement
**verified**; the reading below is **heuristic**.

**Reading.** Community-detection theory (Krzakala et al.) identifies detached non-backtracking
eigenvalues with *structural blocks* of the graph — here, exactly the prime/composite
bipartition. The detached set is therefore exhausted by structure, leaving no arithmetic
exceptions: this confirms the pre-registered prediction of path.md's graph-Siegel dictionary
(P3.2) that finite regular graph stages cannot carry generic complex off-line "zeros," only
real ones (the graph avatar of Landau–Siegel zeros), and here even those are absent beyond the
Perron pair.

**Why research-plan.md relies on this.** research-plan.md §3.2(b) files the graph/divisor
operators as *toolkit only* — "its eigenvalues are divisor-structural, not approximants of
$\gamma$" — citing exactly this finding. Gate E0 of the continued program pre-registers that
this graph one-mode candidate **must fail** the density test, as a regression test reproducing
F4's structural verdict.

---

## 10. The quantum-graph no-go theorem

*Source: [prime-sieve/findings.md](prime-sieve/findings.md) F8. Cited in research-plan.md §2 row
9 as a "proven no-go," and standing behind the caution in gate E4c against "shape decoy" false
positives (obstruction O6).*

### 10.1 Preliminaries — the flower graph model

Kottos–Smilansky flower graph: one vertex, one loop of length $\log p$ per prime $p\le P$; bond
scattering matrix $\Sigma$ unitary; secular determinant $F(s)=\det(I-e^{isL}\Sigma)$,
$L=\mathrm{diag}(\ell_e)$. Self-adjointness makes the zeros of $F$ real automatically;
periodic-orbit lengths are $\sum_p k_p\log p = \log m$ — the explicit formula's support. The
question: can orbit amplitudes equal $\Lambda(m)/\sqrt m$ under a unitary $\Sigma$?

### 10.2 Proposition (no-go) — proven

No finite metric "flower" graph with loop lengths $\{\log p\}$ and an $s$-independent unitary
vertex scattering matrix $\Sigma$ can have its periodic-orbit expansion match
$\sum_m\Lambda(m)m^{-s}$ term by term.

*Proof.* Orbit lengths are $\log m$ by construction, and by unique factorisation distinct $m$
give distinct lengths, so matching is forced termwise as generalised Dirichlet series. A mixed
orbit through distinct loops $p\ne q$ has length $\log(pq\cdots)$ with $\Lambda=0$, so its
amplitude (a product of $\Sigma$-entries) must vanish. If *every* mixed closed word has zero
amplitude, $\Sigma$ is reducible on the loop blocks, i.e. the evolution decouples into single
loops — which is exactly the bare Euler product, provably non-convergent in the critical strip
(path.md Proposition P1.3). If $\Sigma$ is irreducible, some mixed closed word has all steps
nonzero — contradiction. $\blacksquare$

Numerical witness (Neumann flower, loops $2,3,5,7,11$): mixed amplitude $|\sigma_{pq}\sigma_{qp}|
= 0.04 \ne 0 = \Lambda(pq)$ for $(2,3),(2,5),(3,5)$.

**Significance.** Within closed, $s$-independent-unitary quantum graphs, "chaotic mixing" and
"arithmetic support on prime powers" are mutually exclusive. Whatever realises the explicit
formula spectrally must either make amplitudes energy-dependent (where the $\Gamma$-factor
lives — the archimedean window of research-plan.md §3.2(c)), work with open systems/resonances,
or achieve the $\Lambda$-support by interference across pseudo-orbits rather than termwise. This
is one of the standing no-go results research-plan.md's gate E4c ("controls") is built to
respect: no candidate construction in this folder may be a closed, unitary, $s$-independent
quantum graph and simultaneously claim to reproduce the von Mangoldt support.

---

## 11. Evidence hygiene: the rank-unfolding fabrication defect

*Source: [prime-sieve/implementation.md](prime-sieve/implementation.md) I0, correcting defect D2
of the graveyard scripts. Cited in research-plan.md §2 row 10 and adopted verbatim as binding
rule §8's "no unfolding, fitting, or calibration against $N(T)$ or the $\gamma$ list."*

### 11.1 The defect (D2, from the discarded `barry-keating-hp-*` series)

Earlier scripts compared computed spectra against the Riemann zeros by **rank-unfolding**:
mapping the $k$-th computed eigenvalue to the $k$-th zero via the target's own smooth counting
function $\bar N$, then reporting the resulting "match." Because $\bar N$ is built from the very
quantity being tested (the zero locations), any sufficiently regular input spectrum will produce
an apparently good match after unfolding — the transformation *consumes the target's counting
function* and manufactures agreement regardless of whether the underlying construction has any
arithmetic content. This is the specific mechanism that let the `flawed/barry-keating-hp-*`
series claim false progress.

### 11.2 The corrected rule (I0, binding on every experiment in the folder)

1. **No rank-based unfolding against the target's own counting function.** Any comparison with
   Riemann zeros must use raw computed quantities (determinant values, pole coordinates, raw
   angle gaps) against independently computed truth (`mpmath.zetazero`, `mpmath.zeta`).
2. **Non-vacuity guards.** Every graph build asserts `edges > 0`; every pencil/eigen computation
   asserts the operator is not identically zero (this is the mechanical regression test for
   defect D1, the empty-graph artifact — see §2.2/§9.1 above).
3. **Correct circles.** The Ramanujan locus is $|u|=q^{-1/2}$ (regular) or the weighted
   Kotani–Sunada annulus — never $|u|=1$.
4. **Two-sided reporting.** Every experiment states, before running, what outcome would falsify
   the hypothesis it probes; results are recorded either way.
5. **Cross-checks against in-repo verified numbers.** The explicit-formula balance is checked
   against `adele_trace.py` values (§6.3 above), not recomputed ad hoc.

**Why research-plan.md relies on this.** Every one of the continued program's gates is designed
to consume only raw, independently verifiable quantities: E4b's displacement metric uses the
$\gamma$ list *only as final evaluation*, never in construction, scaling, or normalisation
(research-plan.md §5, E4b; §8 do-not-list). E4c's "decoy" control is precisely designed to
verify the harness cannot be fooled by a construction that reproduces the smooth $T\log T$ shape
(gate E0) without any genuine displacement improvement (gate E4b) — the anti-O6 test that
targets the exact failure mode D2/I0 were written to catch.

---

## Cross-reference: where each section is used in research-plan.md

| §here | Result | Cited in research-plan.md as |
|---|---|---|
| 1 | Sieve completeness (Lemma 1.2); equidistribution (Thm 1.3) | §2 row 1; the "proven, Phase 1" input to E0/E2 |
| 2 | Vacuity (Prop 3.1); correction (Def 3.2) | §2 row 2; §3.2(a) legacy comparator $H_n'$ |
| 2.4 | Density mismatch (Thm 3.3) | §2 row 3; obstruction O1 |
| 3 | Weak convergence $\ne$ HP | §2 row 4; obstruction O3/K2 |
| 4 | Trace identity (Thm 3.4, Cor 4.2) | §2 row 5, "Thm 4.1" |
| 5 | Truncation rate (Prop 6.1); rigidity (Prop 3.7) | §2 row 5, "Thm 4.2"; source of Thm 3.3 |
| 6 | Adelic Weil trace, $10^{-36}$ | §2 row 5; gate E4a's target |
| 7 | Meyer 2005 | §2 row 6; obstruction O4, gate E5 |
| 8 | Connes–Moscovici 2022 | §2 row 7; gate E0a's model |
| 9 | Graph spectra block-structural (F4) | §2 row 8; §3.2(b) toolkit-only role |
| 10 | Quantum-graph no-go (F8) | §2 row 9; gate E4c anti-decoy design |
| 11 | Evidence hygiene (I0/D2) | §2 row 10; §8 do-not-list |
