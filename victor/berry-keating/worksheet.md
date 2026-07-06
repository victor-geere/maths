# Worksheet — review of the arithmetic Berry–Keating series

**Scope.** Full mathematical review of the nine documents in `victor/barry-keating/`, feeding the
companion document [barry-keating-addendum-errata.html](barry-keating-addendum-errata.html).
No existing document is altered; everything here is reasoning, verification, and preliminary
results. Rigour tags follow the repo convention: **proven** / **conditional** / **heuristic**.

**Verdict up front.** The series culminates (hp-3, hp-7) in the claim that RH is proved. That claim
is wrong. The chain breaks at several independent points, three of which are fatal and provable in
a few lines each (§2 below). A handful of genuinely correct results can be salvaged and completed
(§5); every remaining route to RH inside this framework lands, provably, on a statement *equivalent*
to RH (Weil positivity / Hermite–Biehler positivity / Connes' global trace formula), so no gap is
"bridgeable" by more of the same — the addendum states these walls precisely instead of pretending
to cross them. **RH remains open; nothing in the series or in the addendum proves it.**

---

## 1. Document inventory and dependency graph

| Doc | Title claim | Depends on | Verdict |
|---|---|---|---|
| [barry-keating-hamiltonian-sieve.html](barry-keating-hamiltonian-sieve.html) | base framework: sieve → operator → de Branges space | — | §2–§3: core false (E1–E7); sieve lemma + equidistribution salvageable |
| [barry-keating-completing.html](barry-keating-completing.html) | "all tractable gaps closed" | sieve | kernel/identification false (E5–E7); numerics fabricated (E19) |
| [barry-keating-hp-1.html](barry-keating-hp-1.html) | Task 1: sharp convergence $\Xi_n\to\Xi$ | sieve | false (E8–E11) |
| [barry-keating-hp-2.html](barry-keating-hp-2.html) | Task 2: moment determinacy | hp-1 | limits false; strategy a non sequitur (E12) |
| [barry-keating-hp-3.html](barry-keating-hp-3.html) | Task 3: **"RH proved"** via de Branges | sieve §10, hp-1, hp-2 | **false on its face** (E13, Lemma L2) |
| [barry-keating-hp-4.html](barry-keating-hp-4.html) | Task 4: adelic spectral triple | hp-3 | asserts the open part of Connes' program as done (E14) |
| [barry-keating-hp-5.html](barry-keating-hp-5.html) | Task 5: intertwiner with Connes operator | hp-3, hp-4 | one correct computation, wrong conclusion (E15) |
| [barry-keating-hp-6.html](barry-keating-hp-6.html) | Task 6: GUE statistics | hp-1 | numerics impossible as coded; theorem overclaims (E16) |
| [barry-keating-hp-7.html](barry-keating-hp-7.html) | Task 7: Langlands / "program complete" | all above | inherits everything; own errors besides (E17) |

Notation used throughout (theirs): $M_n = 2^{n+1}-1$, $k_n = \pi(M_n)$,
$\mathcal H_n = \mathrm{span}\{e_p(\xi) = e^{2\pi i p\xi/M_n}\}$,
$\widehat H_n e_p = (p/M_n + i/2)e_p$, $N_n \approx \alpha\log M_n$ ($\alpha\approx 1.6$),
$H_n^{\mathrm{osc}} = V_n\widehat H_n V_n^{\!*}$ with $(V_n)_{m,p} = \langle\psi_m, U e_p\rangle$,
$\Xi_n(\lambda) = \det(\lambda I - H_n^{\mathrm{osc}})$, $\Xi(\lambda) = \xi(\tfrac12+i\lambda)$.

---

## 2. Master obstructions (each fatal on its own)

### L1 — Numerical-range (triangle) lemma. **proven**

**Lemma.** Let $\widehat H_n$ be normal on $\mathcal H_n$ with spectrum
$\{p/M_n + i/2 : p \le M_n\} \subset [0,1]+i/2$, and let $V:\mathcal H_n\to\mathbb C^{N}$ be any
contraction ($\|V\|\le 1$; the oscillator embedding is one, being
projection ∘ unitary ∘ inclusion of orthonormal systems). Then **every eigenvalue of
$H^{\mathrm{osc}} = V\widehat H_n V^{\!*}$ lies in the triangle
$T=\mathrm{conv}\{0,\; i/2,\; 1+i/2\}$**; in particular $|\lambda|\le\sqrt5/2 < 1.12$.

*Proof.* If $H^{\mathrm{osc}}v=\lambda v$, $\|v\|=1$, put $u=V^{\!*}v$, $\|u\|\le1$. Then
$\lambda = \langle v, V\widehat H_n V^{\!*}v\rangle = \langle u,\widehat H_n u\rangle$.
If $u=0$ then $\lambda = 0\in T$; otherwise
$\lambda = \|u\|^2\,\langle\hat u,\widehat H_n\hat u\rangle$ with $\hat u = u/\|u\|$, and for a
normal operator the numerical range is the closed convex hull of the spectrum, so
$\langle\hat u,\widehat H_n\hat u\rangle \in [0,1]+i/2$. Hence
$\lambda \in \{t\,w : t\in[0,1],\, w\in[0,1]+i/2\} = T$. $\blacksquare$

**Consequences.**
- Sieve Thm 6.1 ("eigenvalues of $H_n^{\mathrm{osc}}\to\gamma_j$, assuming RH") is false *even
  under RH*: no eigenvalue can ever leave $|\lambda|<1.12$, while $\gamma_1 = 14.1347\ldots$
- Sieve Thm 7.1 / completing Thm 3.1 ($\Xi_n\to\Xi$ locally uniformly) is false: all $N_n$ roots
  of $\Xi_n$ lie in $T$, so for $|\lambda|\ge 2$,
  $|\Xi_n(\lambda)|\ge(|\lambda|-\sqrt5/2)^{N_n}\to\infty$, while $\Xi(\lambda)$ is finite.
- hp-1 Lemma 2.1 fails at the single point $\lambda=-1$ (distance $\ge 1$ from $T$ and from the
  line $\mathrm{Im}\,\lambda = 1/2$): the left side has
  $\mathrm{Re}\sum_j(-1-\lambda_j)^{-1}\le -\tfrac{4}{17}N_n\to-\infty$
  (each $w_j=-1-\lambda_j$ has $\mathrm{Re}\,w_j\in[-2,-1]$, $|w_j|^2\le 17/4$), while the right
  side is bounded by $1+o(1)$ in modulus. Contradiction for all large $n$.

### L2 — The claimed de Branges kernel of $\Xi$ is identically zero. **proven**

$\Xi(\lambda)=\xi(\tfrac12+i\lambda)$ is a *real entire* function:
$\overline{\Xi(\bar\lambda)} = \Xi(\lambda)$ (real Maclaurin coefficients; classical). The kernel
used in sieve §10.2, completing Lemma 2.2, hp-3 §1/§3, hp-5 §1,

$$K_\Xi(\lambda,\mu) = \frac{\Xi(\lambda)\overline{\Xi(\bar\mu)} - \overline{\Xi(\bar\lambda)}\,\Xi(\mu)}{2\pi i(\bar\mu-\lambda)},$$

has numerator $\Xi(\lambda)\Xi(\mu)-\Xi(\lambda)\Xi(\mu)\equiv 0$. So $K_\Xi\equiv 0$ and the
"de Branges space $\mathcal H(\Xi)$" built on it is $\{0\}$. Numerically confirmed (T6 below):
numerator $<10^{-31}$ at generic complex points where $|\Xi|\approx 0.48$.

Worse, **no real entire function can be a de Branges structure function**: reality gives
$|E(x-iy)| = |\overline{E(x-iy)}| = |E(x+iy)|$ for all $x,y$, so the required strict inequality
$|E(x-iy)|<|E(x+iy)|$ ($y>0$) fails identically. hp-3 Theorem 3.1 ("$\Xi$ is a de Branges
function, hence RH") is therefore false as stated — independently of the location of the zeros.
Two further slips in the same section: their kernel formula is a misquote of de Branges' (the
correct reproducing kernel is sesquilinear,
$K(w,z) = \big[E(z)\overline{E(w)} - E^{*}(z)\overline{E^{*}(w)}\big]\,i/\big(2\pi(z-\bar w)\big)$
with $E^*(z) = \overline{E(\bar z)}$, which also degenerates for real $E$); and for real $E$ the
phase $\varphi(t)=\arg E(t)$ is piecewise constant in $\{0,\pi\}$, so "$\varphi' >0$"
(their Lemma 2.1 applied to $\Xi$) is absurd. The honest de Branges-side statement is the
Hermite–Biehler equivalence A.6 below — which is *equivalent* to RH, not a route around it.

### L3 — The prime kernels converge to zero (inside a strip) and diverge off it. **proven**

For $u=\lambda-\bar\mu$, $K_n = \frac1{k_n}\sum_{p\le M_n}p^{-1+iu}$, and $|p^{iu}| = p^{-\mathrm{Im}\,u}$:

- $\mathrm{Im}\,u \ge 0$: $\sum_p p^{-1-\mathrm{Im}\,u} \le \sum_{p\le M_n} p^{-1} \sim \log\log M_n$, so $|K_n| \ll \log\log M_n / k_n \to 0$.
- $-1<\mathrm{Im}\,u<0$, $\delta = -\mathrm{Im}\,u$: $\sum_p p^{-1+\delta} \asymp M_n^{\delta}/(\delta\log M_n)$, so $|K_n| \asymp M_n^{\delta-1}/\delta \to 0$.
- $\mathrm{Im}\,u<-1$: $|K_n| \asymp M_n^{\delta-1}\to\infty$.

So on $\{|\mathrm{Im}(\lambda-\bar\mu)|<1\}$ the limit is the **zero kernel** (consistent with L2:
$K_\infty = 0 = K_\Xi$ — the "identification" is vacuously true and proves nothing), and on
$\mathrm{Im}(\lambda-\bar\mu)<-1$ there is no limit at all. This kills sieve Thm 10.1 and
completing Thm 2.1. The specific error in their HS proof: the bound
"$\iint_\Omega p^{i\lambda}q^{-i\bar\mu}\,d\lambda\,d\mu = O(1/\log(p/q))$" is false for a
complex domain $\Omega$, where $|p^{i\lambda}|$ grows like $p^{|\mathrm{Im}\,\lambda|}$; there is
also an algebra slip ($|\sum_p|^2$ expanded without cross terms). Note the internal contradiction:
sieve §10.2 Step 1 *admits* the pointwise limit does not exist, then proceeds via unspecified
weights $\langle p\rangle_n$ that are set to $1$ again in the same section.

---

## 3. Errata catalogue

Severity: ★★★ fatal to the chain · ★★ major (claim false/unproven as stated) · ★ minor/fixable.

| # | Location | Claim | Finding |
|---|---|---|---|
| E1 ★★ | sieve §5.1; hp-1 §1 | "$\widehat H_n f(\xi) = (\xi+i/2)f(\xi)$… eigenvalues $p/M_n+i/2$" | Multiplication by $\xi$ has no eigenvectors and does not preserve $\mathcal H_n$; the $e_p$ are eigenvectors of $\frac{M_n}{2\pi i}\partial_\xi + \frac i2$. Also $\{e_p\}$ is orthonormal on $\mathbb R/M_n\mathbb Z$, not on $[0,1)$ as written. Even fixed, the operator is *normal with complex spectrum in a unit box*, not a Hilbert–Pólya candidate. |
| E2 ★★ | sieve Thm 5.1 | strong resolvent convergence $\widehat H_n \to \widehat H_{BK}$ | No identification map between the spaces is defined; spectra are incompatible ($[0,1]+i/2$ vs $\mathbb R$); srs limits cannot move spectra that way. No proof given. Correct spectral theory of $\widehat H_{BK}$: A.3. |
| E3 ★★★ | sieve Thm 6.1 | eigenvalues of $H_n^{\mathrm{osc}} \to \gamma_j$ under RH | False even under RH by **L1** (all eigenvalues in $T$, $\gamma_1 = 14.13$). One-line "proof" in the doc. |
| E4 ★★★ | sieve Thm 7.1; completing Thm 3.1 | $\Xi_n \to \Xi$ locally uniformly | False by **L1** (roots trapped in $T$, degree $\to\infty$). The completing proof also asserts $\int_0^1\log(1-(\xi+i/2)/\lambda)\,d\xi$ "is exactly the Weierstrass product of $\Xi$" — a zero-free function of $|\lambda|>1.12$ equated with a function whose zeros are $\pm\gamma_j$. |
| E5 ★★★ | sieve §10.1–10.2; completing Thm 2.1 | $K_n \to K_\infty \ne 0$ in HS norm on compacts | False by **L3**; oscillatory-integral bound false on complex domains; $\vert\sum\vert^2$ algebra slip; self-contradiction with their own Step 1. |
| E6 ★★★ | sieve §10.2 Step 2–3; completing Lemma 2.2; hp-3 §1 | $K_\infty = K_\Xi$, the de Branges kernel of $\Xi$ | $K_\Xi \equiv 0$ (**L2**); identification is $0=0$; the invoked "uniqueness of the dB kernel given the zero set" is also false (different spaces share $A$-zero sets: $E = A-iB$ vs $A-i(B+tA)$). |
| E7 ★★ | sieve §10.3; completing §2.3 | $\hat H_\infty$ symmetric, def. indices $(1,1)$, "spectrum of any s.a. extension = zeros of $\Xi$"; "RH ⟺ some s.a. extension has real spectrum" | Space is $\{0\}$, so all of it is vacuous. Even in a genuine $\mathcal H(E)$: the self-adjoint extensions form a family with *different, interlacing* spectra (zero sets of $\cos\theta\,A + \sin\theta\,B$); and *every* self-adjoint extension has real spectrum by definition — the stated "equivalence" with RH is empty. |
| E8 ★★★ | hp-1 Lemma 2.1 | $\Xi_n'/\Xi_n = \frac1{k_n}\sum_p(\lambda-p/M_n-i/2)^{-1} + O((\log M_n)^3/\sqrt{M_n})$ | Trace of an $N_n\times N_n$ resolvent has $N_n$ poles of total residue $N_n$; RHS has $k_n$ poles of total residue $1$. Refuted at $\lambda=-1$ via **L1**. The claimed decay $\epsilon_{p,q}\ll e^{-c\vert\log p-\log q\vert^2}$ is useless: for the $\asymp (M_n/\log M_n)^2$ pairs $p,q\in(M_n/2,M_n]$, $\vert\log p-\log q\vert\le\log 2$ and nothing is small. |
| E9 ★★ | hp-1 Lemma 3.1 | explicit formula with remainder | Malformed: for fixed compactly supported $\Phi$ the prime sum is eventually independent of $n$; the displayed mix of truncation, tail and VK-error does not typecheck. Correct, verified statement: **A.4**. |
| E10 ★★★ | hp-1 Lemma 3.2 | $\frac1{k_n}\sum_p\frac1{\lambda - p/M_n - i/2} \approx \sum_\rho\frac1{\lambda-\gamma}$, exp. small error | Poles live in $[0,1]+i/2$ vs at the real $\gamma_j$. Numerically (T4): LHS$\,\to -0.805 - 1.107i$ at $\lambda=i$; RHS $= -0.0462i$ **exactly imaginary** (zeros come in $\pm\gamma,\pm\bar\gamma$ quadruples). "Proof" is a citation wave (Goldston–Gonek, Chandee) with no derivation. |
| E11 ★★ | hp-1 §5, Thm 4.1 | numerics "$\max\vert\Xi_n-\Xi\vert\approx 10^{-6}$ at $N=400$"; $\vert\Xi_n-\Xi\vert \le Ce^{-c\sqrt{\log M_n}}$ | No code/data; impossible by **L1**; theorem rests on E8+E10. |
| E12 ★★★ | hp-2 §3–5 | moments converge to $(2\pi)^{2k}/(2k+1)$; odd moments vanish; determinacy ⟹ zeros real | $\mu_2^{(n)}$ **diverges** (T5: $3.3 \to 23 \to 207$ across $M=2^{16},2^{20},2^{24}$); odd "moments" are sums of positive terms; and determinacy of a *real* moment problem cannot constrain planar support: $\delta_0$ and the uniform measure on the unit circle have identical holomorphic moments $\int z^k\,d\nu = \delta_{k,0}$. The Carleman computation itself (their Thm 4.1) is correct but applied to an unestablished bound — and trivial anyway under their own compact-support claim. |
| E13 ★★★ | hp-3 (whole document) | "$\Xi$ is a de Branges function ⟹ RH proved" | Impossible: real entire functions are never HB (**L2**); kernel misquoted; phase-monotonicity lemma inapplicable (arg of a real function is piecewise constant); premise kernels converge to $0$. The honest statement is A.6 (RH-equivalent, not a proof). |
| E14 ★★ | hp-4 §4.1, L5.2, Thm 6.1 | $D_K$ pure point with spectrum = zeros; $N(T)$ "faster than any polynomial"; $\vert D\vert^{-p}$ trace class for $p>2$; $\zeta_D = \xi$ | The pure-point claim *is* the open content of Connes' program (his zeros are an absorption spectrum; the global trace formula is equivalent to RH — see A.7). $N(T)\sim\frac{T}{2\pi}\log T$ is polynomially bounded. On the point part $\sum\gamma_j^{-p}<\infty \iff p>1$; on the a.c. part $\vert D\vert^{-p}$ is never compact. $\mathrm{Tr}\,\vert D\vert^{-s}$ is Voros' *secondary* zeta (poles, not zeros, carry the information) — equating it with $\xi(s)$ is a category error; the trace of a restricted tensor product does not factor as claimed. |
| E15 ★★ | hp-5 | intertwiner $\mathcal W$; image "= $\mathscr H_\infty$"; $\mathcal W\mathbf 1_K \propto \xi(\tfrac12+i\lambda)$ | The Mellin computation in Thm 4.1 is correct *formal* intertwining — but with **multiplication by $\lambda$ on $L^2(\mathbb R)$** (Mellin–Plancherel): purely a.c. spectrum $\mathbb R$, no discrete zeros; "$\mathscr H_\infty$" is $\{0\}$. $\mathbf 1_K$ is not integrable against $\vert g\vert^{1/2+i\lambda}$ (divergent at the archimedean place); with a Gaussian one gets Tate's genuine identity $\mathcal W(\mathrm{gauss}\otimes\mathbf 1_{\widehat{\mathbb Z}})(\lambda) = \Lambda(\tfrac12+i\lambda) = \pi^{-s/2}\Gamma(s/2)\zeta(s)\vert_{s=\frac12+i\lambda}$ — an $L^2$ function, not a reproducing-kernel identity. §2.1's transform is unitary from $L^2(dx)$, not $L^2(dx/x)$, as normalised (fix in A.3). |
| E16 ★★★ | hp-6 | GUE numerics + "rigorous derivation" | Premise false (T1). The unfolding code returns `ranks/(N+1)` — constant spacings (std $1.6\times10^{-14}$, T2): the claimed "excellent fit to GUE" is unreproducible from the listed code. Montgomery's theorem misstated (their $\widehat F$ is the FT of the sine-kernel square, with the $\delta$ term and the $\vert\alpha\vert>1$ behaviour wrong; the theorem is conditional on RH and support-restricted; full GUE is conjectural — Rudnick–Sarnak is restricted-support and under RH). "$\mathbb E[\cdot]$" appears with no probability space. Honest replacement numerics: T9. |
| E17 ★★ | hp-7 | trivial character rep; "infinitesimal generator of the Hecke algebra"; zeros as its spectrum | $\varphi_0\equiv 1\notin L^2(C_{\mathbb Q})$ (infinite volume); discrete Hecke translations have no infinitesimal generator — $D$ generates the $\mathbb R_{>0}$ flow; the spectrum on $L^2(C_{\mathbb Q})^K$ is a.c. $=\mathbb R$ (same non sequitur as E15). The Tate/class-field exposition is standard; every RH-relevant claim is unsupported. |
| E18 ★ | completing §3.2, §5 | Mellin formula; PT bullet | "$ (Uf)(x) = \frac1{\sqrt{2\pi}}\int_0^1 f(\xi)\,x^{-i\log x}\,d\xi$" has integrand independent of $\xi$ — a rank-one map; garbled beyond repair as printed. "Unbroken PT ⟹ real spectrum selecting $\Xi$ zeros" — PT symmetry only forces conjugation-symmetric spectra; unbrokenness is exactly what would need proof. |
| E19 ★★★ | completing §4 | output table: max error $0.436\to0.0436$, first eig $\to 14.180$ | **Fabricated.** Running the listed code verbatim (T1): max error $37.8\to30.2$ for $N=40\to120$; first positive-imag eigenvalue $0.8433$ (stable); eigenvalues up to modulus $2.4\times10^3$; 116/120 have $\vert\mathrm{Re}\vert>1$. Same matrix appears in sieve §8 and hp-6 §2. |

**Cross-cutting contradictions.**
C1: hp-1 §1 (eigenvalues $= p/M_n+i/2$, a unit box) vs hp-2 §1–2 and completing §4 (eigenvalues $\approx\gamma_j\in[14,50]$).
C2: sieve abstract ("spectrum = zeros *conditionally on RH*") vs hp-3/hp-7 ("RH proved").
C3: sieve §10.2 Step 1 (no pointwise kernel limit) vs completing Thm 2.1 (HS convergence of the same kernel).
C4: $K_\Xi$ claimed "positive definite with the same zeros as $\Xi$" while being $\equiv 0$.
C5: hp-6 comments "ours is not Hermitian" while the program's goal is a self-adjoint operator.

---

## 4. Numerical evidence (all scripts in scratchpad; scratch venv numpy/scipy/mpmath)

**T1 — their matrix, their code, verbatim** (completing §4 = sieve §8 = hp-6 §2):

| N | claimed max err | actual max err | claimed 1st eig | actual 1st eig |
|---|---|---|---|---|
| 40 | 0.428391 | **37.815581** | 14.563116 | **0.843324** |
| 60 | 0.202159 | **35.563188** | 14.336884 | **0.843255** |
| 80 | 0.112456 | **33.605444** | 14.247181 | **0.843251** |
| 100 | 0.068312 | **31.847540** | 14.203037 | **0.843250** |
| 120 | 0.043567 | **30.235085** | 14.180292 | **0.843250** |

At $N=120$: $\max|\lambda| = 2.39\times10^3$; 116 of 120 eigenvalues have $|\mathrm{Re}\,\lambda|>1$.

**T2 — hp-6 unfolding:** spacings all equal to $N/(N+1)$ (std $1.6\times10^{-14}$) for *any* input
spectrum; a delta spike, not a Wigner fit.

**T3 — kernel limit** ($u=\lambda-\bar\mu$): $|K_n(u{=}1)| = 4.95\times10^{-4},\,6.4\times10^{-5},\,1.0\times10^{-5},\,2\times10^{-6}$
at $M=2^{14},2^{17},2^{20},2^{23}$ (→ 0, like $1/\log M$); at $u=-1.5i$: $81.6,\,232.8,\,662.6,\,1882.8$ (diverges). Matches L3 exactly.

**T4 — hp-1 Lemma 3.2 at $\lambda=i$:** LHS $= -0.7871 - 1.1430i$ at $M=2^{22}$, tracking the
predicted limit $\int_0^1 dt/(i/2-t) = -0.8047-1.1071i$; zero side
$\sum_\rho (i-\gamma)^{-1} = -0.0462i$ (40 zero pairs + smooth tail; purely imaginary
unconditionally). Both components disagree; no error term can rescue it.

**T5 — hp-2 second moment:** $\mu_2^{(n)} = 3.30,\ 23.2,\ 207.2$ at $M = 2^{16}, 2^{20}, 2^{24}$
versus claimed limit $(2\pi)^2/3 = 13.16$. Diverges $\sim M/\mathrm{polylog}(M)$, as the
Chebyshev-type estimate $\sum_{p\le M}(p/M)^{2k} \sim \frac{1}{2k+1}\frac{M}{\log M}$ predicts.

**T6 — $K_\Xi\equiv 0$:** $|\Xi(\lambda)-\overline{\Xi(\bar\lambda)}| < 10^{-30}$ at
$\lambda = 3.7,\ 14,\ 2.3+0.9i$; kernel numerator $8.6\times10^{-32}$ at
$(\lambda,\mu)=(1.3+0.4i,\,-0.7+1.1i)$ where $|\Xi(\lambda)| = 0.48$.

**T7 — Guinand–Weil explicit formula verified to $9.4\times10^{-32}$** (30-digit arithmetic),
$h(r) = e^{-(r/6)^2}$, $g(u) = \frac{\sigma}{2\sqrt\pi}e^{-\sigma^2u^2/4}$, $\sigma=6$:

| term | value |
|---|---|
| zero side $\sum_\rho h(\gamma_\rho)$ | $0.00778636024828842395\ldots$ |
| poles $h(i/2)+h(-i/2)$ | $2.013937226\ldots$ |
| $-g(0)\log\pi$ | $-1.937534033\ldots$ |
| archimedean $\frac1\pi\int_0^\infty h(r)\,\mathrm{Re}\,\psi(\tfrac14+\tfrac{ir}2)\,dr$ | $-0.046598878\ldots$ |
| primes $-2\sum_n \Lambda(n)n^{-1/2}g(\log n)$ | $-0.022017955\ldots$ |
| **RHS total** | $0.00778636024828842395\ldots$ |

This pins the exact normalisation used in Addendum A.4 and is the *correct* prime↔zero bridge the
series needed. (Feeds `research/phase-3-dynamical/explicit-formula.md`.)

**T8 — honest Task-2 content is log-slow:** $\frac1N\sum_{j\le N}(\gamma_j/\gamma_N)^2 = 0.4433$
at $N=40$ vs limit $1/3$; consistent with the $1+O(1/\log\gamma_N)$ CDF distortion proved in A.5.

**T9 — honest Task-6 numerics** (first 120 zeros, Riemann–von Mangoldt unfolding
$x_j = \bar N(\gamma_j)$, $\bar N(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e}+\frac78$):
mean spacing $1.0003$; variance $0.124$ (GUE $\approx 0.18$ asymptotically, Poisson $=1$);
min gap $0.387$ — clear level repulsion, GUE-consistent at low height (cf. Odlyzko).

---

## 5. What survives, completed in the addendum

- **A.1 (proven) Sieve correctness.** $G_n$ is exactly the set of composites in $I_n$: every prime
  factor of a composite $x<2^{n+1}$ satisfies $p\le x/2 < 2^n$ (factors may repeat — the note's
  $p_1\cdots p_k$ must be read as a multiset). Complete proof supplied.
- **A.2 (proven) Equidistribution of $\{p/M_n\}$** with rate: $\widehat\mu_n(k) = O_k(1/\log M_n)$,
  by partial summation against $\pi(t)$ + PNT; hence vague convergence to Lebesgue. The cited
  "Vinogradov bound for all $0<\alpha\le1/2$" is *misquoted* (at $\alpha=1/3$,
  $\sum_{p\le x}e(p/3) \sim -\tfrac12\,x/\log x$, not $\ll x/\log^A x$); rational $\alpha = k/M_n$
  is major-arc and needs the PNT route, which fortunately is all the lemma requires.
- **A.3 (proven) Spectral theory of the actual Berry–Keating generator.**
  $H = -i(x\partial_x+\tfrac12)$ is essentially self-adjoint on $C_c^\infty(0,\infty)\subset L^2(\mathbb R_+,dx)$,
  unitarily equivalent to $-i\,d/du$ via $u=\log x$, diagonalised by the Mellin transform
  $(\mathcal Mf)(\lambda) = \frac1{\sqrt{2\pi}}\int_0^\infty f(x)\,x^{-1/2-i\lambda}\,dx$;
  spectrum $\mathbb R$, purely a.c., simple. The $+i/2$ of the documents is the
  $L^2(dx)\leftrightarrow L^2(dx/x)$ Jacobian, nothing more. Corollary: *any* claim of discrete
  spectrum requires changing the space/boundary conditions — that is where the entire difficulty
  lives (Berry–Keating regularisations; Connes' quotient; Sierra's $x(p+\ell_p^2/p)$).
- **A.4 (proven, verified) Guinand–Weil explicit formula** for $\zeta$, with the T7-verified
  normalisation, for even $h$ holomorphic in $|\mathrm{Im}\,z|\le\frac12+\delta$ with
  $h(z)\ll(1+|z|)^{-2-\delta}$:
  $$\sum_\rho h(\gamma_\rho) = h(\tfrac i2)+h(-\tfrac i2) - g(0)\log\pi
  + \frac1{2\pi}\int_{\mathbb R} h(r)\,\mathrm{Re}\,\psi(\tfrac14+\tfrac{ir}2)\,dr
  - 2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,g(\log n),$$
  $g(u) = \frac1{2\pi}\int h(r)e^{-iur}dr$. Unconditional (Guinand 1948; Weil 1952; Barner 1981;
  Iwaniec–Kowalski Thm 5.12).
- **A.5 (proven) Honest Task 2.** Unconditionally, the ordinate counting function gives
  $N(tT)/N(T)\to t$, so the empirical measure of $\{\gamma_j/\gamma_N\}_{j\le N}$
  (symmetrised) → uniform on $[-1,1]$; even moments $\to 1/(2k+1)$; Carleman is immediate;
  the moment problem is determinate. **And it cannot help:** holomorphic moments do not see
  planar support ($\delta_0$ vs unit-circle uniform), so "determinacy + real moments ⟹ real
  zeros" is unfixable as a strategy. Reality of spectrum comes from self-adjointness or nothing.
- **A.6 (proven; RH-equivalent reformulation) Honest Task 3.** For $h>0$ let
  $E_h(z) = \Xi(z+ih)$. Then: RH $\iff$ $E_h$ is Hermite–Biehler for every $h>0$ $\iff$ the
  (correctly written) de Branges kernel of $E_h$ is positive definite on $\mathbb C^+$ for every
  $h>0$. Proof via the unconditional even Hadamard product
  $\Xi(z) = \Xi(0)\prod_\gamma(1-z^2/\gamma^2)$ and factor-wise Blaschke estimates; converse by
  exhibiting an upper-half-plane zero of $E_{c/2}$ from any putative zero with
  $\mathrm{Im}\,\gamma_0 = c>0$. This is what hp-3 *should* have said: the kernel positivity is
  not a lemma on the way to RH, it **is** RH.
- **A.7 (status map) Honest Tasks 4/5/7.** What is actually proven in the adelic picture
  (Tate's thesis; Connes' S-local trace formula; Meyer's unconditional spectral realisation
  *without* positivity; Burnol's Sonine/de Branges spaces; Connes–Consani archimedean Weil
  positivity and ζ-cycles) versus what is open and RH-equivalent (the global trace
  formula / Weil positivity). Corrected statements for E14's zeta-function claims (Voros
  secondary zeta; $\sum\gamma^{-p}<\infty\iff p>1$).
- **A.8 (proven equivalence) The wall, stated exactly.** Weil's criterion: RH $\iff$
  $Q(g)\ge 0$ for all $g\in C_c^\infty(\mathbb R)$, where $Q(g)$ is the explicit-formula
  functional applied to $h = |\hat g|^2$. Every surviving route of the series terminates here.
- **A.9 (conditional/numerical) Honest Task 6.** Montgomery (1973, under RH, Fourier support in
  $[-1,1]$): pair correlation consistent with GUE; full GUE statistics conjectural
  (Rudnick–Sarnak restricted; Odlyzko's computations); T9 illustrates at low height.

## 6. The irreducible gap

Within this framework the following are *equivalent to RH* (each unconditionally proven
equivalent): (i) Weil positivity (A.8); (ii) HB/kernel positivity of $E_h$ for all $h>0$ (A.6);
(iii) validity of Connes' global trace formula in the required function spaces (A.7). The series'
strategy — finite prime kernels → limit kernel → positive de Branges structure → real zeros —
fails not for want of technique but because its limit object is $0$ (L2/L3) and its finite spectra
are trapped (L1); any *repaired* version must inject positivity exactly of type (i)/(ii), i.e.,
must prove RH itself. This is the precise sense in which "all tractable gaps" were *not* closed
and cannot be closed by these means. Per repo convention (`CLAUDE.md`): no assertion that this
framework implies RH is warranted; the only honest tags are the ones above.

## 7. Key references

Berry–Keating (SIAM Rev. 41, 1999); Connes (Selecta Math. 5, 1999); Connes–Consani (Selecta Math.
27, 2021; ζ-cycles); R. Meyer (Duke Math. J. 127, 2005); Burnol (Sonine spaces, C.R.A.S.
2002–03; Forum Math. 16, 2004); de Branges (*Hilbert Spaces of Entire Functions*, 1968); Levin
(*Distribution of Zeros of Entire Functions*, ch. VII); Lagarias (dB spaces & L-functions, 2006);
Guinand (PLMS 1948); Weil (1952); Barner (Crelle 323, 1981); Iwaniec–Kowalski (Thm 5.12);
Montgomery (PSPM 24, 1973); Rudnick–Sarnak (Duke 81, 1996); Odlyzko (Math. Comp. 48, 1987);
Voros (*Zeta Functions over Zeros of Zeta Functions*, 2010); Li (JNT 65, 1997);
Bombieri–Lagarias (JNT 77, 1999); Bender–Brody–Müller (PRL 118, 2017) with the ensuing
self-adjointness critiques; Sierra–Rodríguez-Laguna (PRL 106, 2011); Titchmarsh (2nd ed.);
Platt–Trudgian (Bull. LMS 53, 2021); Pratt–Robles–Zaharescu–Zeindler (Res. Math. Sci. 7, 2020).
