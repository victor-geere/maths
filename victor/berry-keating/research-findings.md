# Research findings — the verified foundation

**Purpose.** This document collects everything from the Berry–Keating series review that is
*actually proven*, stated accurately and self-containedly, so that a new research project can
start from solid ground. Provenance and the audit trail (errata, refutations, logs) live in
[worksheet.md](worksheet.md) and
[barry-keating-addendum-errata.html](barry-keating-addendum-errata.html); none of the discarded
claims are repeated here.

**Rigour policy** (repo convention): every statement below is tagged
**proven** (complete proof here, or classical with citation),
**conditional** (named hypothesis stated), or
**RH-equivalent** (unconditionally proven *equivalent* to RH — these mark the frontier, they are
not stepping stones). The Riemann Hypothesis itself is **open**; nothing here proves it.

Standing notation: $p, q$ primes; $\Lambda$ the von Mangoldt function; $\pi(x)$ the prime count;
$\xi(s) = \tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$;
$\Xi(\lambda) = \xi(\tfrac12 + i\lambda)$ (real, even, entire of order 1, $\Xi(0)\ne0$);
nontrivial zeros $\rho = \tfrac12 + i\gamma_\rho$ with $|\mathrm{Im}\,\gamma_\rho| < \tfrac12$;
$\mathbb C^+ = \{\mathrm{Im}\,z > 0\}$; $E^*(z) = \overline{E(\bar z)}$;
$N(T)$ the zero-counting function.

---

## 1. Elementary arithmetic results

### 1.1 The composite-generator sieve — **proven**

**Lemma 1.** Let $I_n = [2^n, 2^{n+1}-1]$, let $\mathcal P_n$ be the primes $<2^n$, and let
$G_n$ be the set of $x \in I_n$ expressible as $x = p_1p_2\cdots p_k$ with $p_i \in \mathcal P_n$
(*repetitions allowed*) and $k \ge 2$. Then $G_n$ is exactly the set of composites in $I_n$;
the complement of $G_n$ in $I_n$ is the set of primes in $I_n$, and after stage $n$ all primes
$\le M_n = 2^{n+1}-1$ are known.

*Proof.* A product of $k\ge2$ primes is composite. Conversely, if $x \in I_n$ is composite with
prime factorisation $x = q_1\cdots q_k$ ($k\ge2$, multiplicities counted), then each
$q_i = x/m$ for an integer $m \ge 2$, so $q_i \le x/2 < 2^n$, i.e. $q_i \in \mathcal P_n$.
Induction over $n$ makes the recursion well-founded. $\blacksquare$

*Remark.* Repetitions are necessary ($4 = 2\cdot2$); read $p_1\cdots p_k$ as a multiset.

### 1.2 Equidistribution of the normalised primes — **proven**

**Lemma 2.** Let $\mu_n = \frac1{k_n}\sum_{p\le M_n}\delta_{\{p/M_n\}}$ with $k_n = \pi(M_n)$.
For each fixed $k \in \mathbb Z\setminus\{0\}$,

$$\widehat\mu_n(k) = \frac1{k_n}\sum_{p\le M_n} e^{2\pi i k p/M_n} = O_k\!\left(\frac1{\log M_n}\right)\longrightarrow 0,$$

and $\widehat\mu_n(0) = 1$. Hence $\mu_n \to$ Lebesgue measure on $\mathbb T$ weak-\*.

*Proof.* Write $S = \int_{2^-}^{M} e(kt/M)\,d\pi(t)$, $\pi(t) = \mathrm{Li}(t) + E(t)$ with
$E(t) \ll t\,e^{-c\sqrt{\log t}}$ (prime number theorem, de la Vallée Poussin). Integration by
parts bounds the $E$-part by $(1+|k|)M e^{-c\sqrt{\log M}}$. In the main part substitute
$t = Ms$: the range $s \le M^{-1/2}$ gives $O(\sqrt M)$; on $s \ge M^{-1/2}$ expand
$\frac1{\log(Ms)} = \frac1{\log M}\big(1 - \frac{\log s}{\log M} + O(\frac{\log^2 s}{\log^2 M})\big)$
and use $\int_0^1 e(ks)\,ds = 0$, $\int_0^1|\log s|\,ds = 1$. Altogether
$S \ll_k M/\log^2 M$; divide by $k_n \sim M/\log M$. Weyl's criterion finishes. $\blacksquare$

**Fact 2a** (calibration for exponential sums over primes at *rational* frequencies) — **proven**.
For fixed $a/q$ with $(a,q)=1$, the prime number theorem in arithmetic progressions gives
$\sum_{p\le x} e(ap/q) \sim \frac{\mu(q)}{\varphi(q)}\,\frac{x}{\log x}$
(Ramanujan-sum main term); e.g. $\sum_{p\le x}e(p/3) \sim -\tfrac12\,x/\log x$. Minor-arc
(Vinogradov) savings **do not** apply at such frequencies. Any future argument using prime
exponential sums must route major-arc frequencies through PNT-type main terms, as in Lemma 2.

---

## 2. The Berry–Keating generator, exactly — **proven**

**Proposition 3.** On $L^2(\mathbb R_+, dx)$ the operator
$H = -i\big(x\frac{d}{dx} + \tfrac12\big)$, defined on $C_c^\infty(0,\infty)$, is essentially
self-adjoint. The map $(U_1 f)(u) = e^{u/2}f(e^u)$ is unitary onto $L^2(\mathbb R)$ and
$U_1 H U_1^{-1} = -i\,d/du$. Consequently $H$ has purely absolutely continuous, simple spectrum
equal to $\mathbb R$, and the normalised Mellin transform

$$(\mathcal M f)(\lambda) = \frac1{\sqrt{2\pi}}\int_0^\infty f(x)\,x^{-\frac12-i\lambda}\,dx$$

is unitary onto $L^2(\mathbb R, d\lambda)$ with $\mathcal M H \mathcal M^{-1} = $ multiplication
by $\lambda$.

*Proof.* Unitarity of $U_1$ is the substitution $x = e^u$. With $f(x) = x^{-1/2}g(\log x)$ one
computes $xf' + \tfrac12 f = x^{-1/2}g'(\log x)$, so $U_1(Hf) = -ig'$. The operator $-i\,d/du$
on $C_c^\infty(\mathbb R)$ has deficiency indices $(0,0)$ (solutions of $-i\psi' = \pm i\psi$
are $e^{\mp u} \notin L^2(\mathbb R)$), hence is essentially self-adjoint; Fourier transform
diagonalises it. Unitary conjugation transports everything; $\mathcal M = \mathcal F U_1$.
$\blacksquare$

**Bookkeeping.** On $L^2(\mathbb R_+, dx/x)$ the same flow has generator $-ix\partial_x$ (no
$\tfrac12$) and Mellin kernel $x^{-i\lambda}\,dx/x$. The "$+i/2$" that appears in
critical-line formulas is exactly the Jacobian of $L^2(dx) \leftrightarrow L^2(dx/x)$ — it is
*not* an arithmetic phenomenon.

**Consequence (read before designing anything).** The spectrum is a continuum; discrete
spectrum — at the zeros or anywhere — can only come from *changing the space or the boundary
conditions* (Planck-cell regularisations are semiclassical counting heuristics; Sierra-type
models $x(p + \ell_p^2/p)$ achieve discreteness matching only the smooth zero count; Connes'
construction changes the underlying space). This localises the entire Hilbert–Pólya difficulty.

---

## 3. No-go theorems (proven design constraints)

These are proved facts about whole *classes* of constructions. A new project should treat them
as boundary fences: any proposal violating one is dead on arrival.

**N1 (spectral confinement of contractive compressions) — proven.**
Let $A$ be a bounded normal operator and $V$ a linear contraction. Every eigenvalue of
$VAV^{*}$ lies in $\{tw : t\in[0,1],\ w \in \mathrm{conv}\,\sigma(A)\}$.
*Proof:* for a unit eigenvector $v$, $\lambda = \langle V^{*}v, A\,V^{*}v\rangle$, and the
numerical range of a normal operator is the closed convex hull of its spectrum. $\blacksquare$
*Consequence:* no sequence of contractive compressions of a model with spectrum in a bounded
region (e.g. $[0,1] + i/2$) can produce eigenvalues near $\gamma_1 = 14.13\ldots$ — under any
hypothesis. Finite models must let the numerical range grow with the truncation.

**N2 ($1/\pi(M)$-normalised prime kernels degenerate) — proven.**
With $u = \lambda - \bar\mu$, $\;K_n = \frac1{k_n}\sum_{p \le M_n} p^{-1+iu}$ satisfies:
$K_n \to 0$ locally uniformly on $\{\mathrm{Im}\,u > -1\}$, and $|K_n| \to \infty$ for
$\mathrm{Im}\,u < -1$. *Proof:* $|p^{iu}| = p^{-\mathrm{Im}\,u}$ plus Chebyshev bounds:
$\sum_{p\le M}p^{-1+\delta} \asymp M^{\delta}/(\delta\log M)$ for $\delta>0$ and
$\sum_{p \le M} p^{-1} \sim \log\log M$, against $k_n \sim M/\log M$. $\blacksquare$
*Consequence:* averaged prime Gram kernels have no nonzero limit; positivity cannot be
"passed to the limit" through them. Unnormalised kernels are the correct objects (§6.1).

**N3 (real entire functions are never Hermite–Biehler) — proven.**
If $E$ is entire with $\overline{E(\bar z)} = E(z)$, then $|E(x-iy)| = |E(x+iy)|$ for all
$x,y$, so the strict HB inequality fails everywhere; moreover the antisymmetric expression
$\big[E(\lambda)\overline{E(\bar\mu)} - \overline{E(\bar\lambda)}E(\mu)\big]/\big(2\pi i(\bar\mu-\lambda)\big)$
vanishes identically. In particular $\Xi$ itself cannot serve as a de Branges structure
function; the correct target involving $\Xi$ is stated in §6.2 and §7.1.

**N4 (holomorphic moments cannot certify real support) — proven.**
$\delta_0$ and the uniform measure on the unit circle are conjugation-symmetric probability
measures on $\mathbb C$ with identical moment sequences $\int z^k\,d\nu = \delta_{k,0}$
$(k \ge 0)$. Hence no argument of the form "the trace moments
$\frac1N\,\mathrm{Tr}\,(H_N)^k$ are real and determinate, therefore the limiting spectral
support is real" is valid. Reality of spectra comes from symmetry
($\langle Hu,v\rangle = \langle u,Hv\rangle$), i.e. self-adjointness — the original
Hilbert–Pólya requirement. (Carleman-type determinacy is still a fine tool *on* $\mathbb R$;
it just cannot move a measure onto $\mathbb R$.)

---

## 4. The explicit formula — the correct prime↔zero bridge — **proven (classical), normalisation verified**

**Theorem 4** (Guinand 1948; Weil 1952; Barner 1981; Iwaniec–Kowalski, Thm 5.12).
Let $h$ be even, holomorphic on $|\mathrm{Im}\,z| \le \tfrac12 + \delta$, with
$h(z) \ll (1+|z|)^{-2-\delta}$ there, and $g(u) = \frac1{2\pi}\int_{\mathbb R}h(r)e^{-iur}dr$.
Then, unconditionally, with zeros counted with multiplicity,

$$\sum_\rho h(\gamma_\rho) = h\!\left(\tfrac i2\right) + h\!\left(-\tfrac i2\right) - g(0)\log\pi + \frac1{2\pi}\int_{\mathbb R} h(r)\,\mathrm{Re}\,\psi\!\left(\tfrac14 + \tfrac{ir}2\right) dr - 2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,g(\log n),$$

where $\psi = \Gamma'/\Gamma$.

**Verified instance** (30-digit arithmetic; usable as a regression test for any future code):
$h(r) = e^{-(r/6)^2}$, $g(u) = \frac{3}{\sqrt\pi}e^{-9u^2}$:

| term | value |
|---|---|
| zero side $\sum_\rho h(\gamma_\rho)$ | $0.0077863602482884239503\ldots$ |
| $h(i/2) + h(-i/2)$ | $2.013937226\ldots$ |
| $-g(0)\log\pi$ | $-1.937534033\ldots$ |
| archimedean integral | $-0.046598878\ldots$ |
| prime side | $-0.022017955\ldots$ |
| difference of sides | $9.4\times10^{-32}$ |

**Reading.** This is a *distributional trace identity*, not an operator equality. It is the
entire rigorous content of "primes ↔ zeros duality" available unconditionally, and every
spectral program is an attempt to realise it as the trace formula of a self-adjoint operator.
Its positivity form is §7.2.

---

## 5. Unconditional facts about the zeros — **proven**

**5.1 Counting (Riemann–von Mangoldt).**
$N(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e} + \frac78 + O(\log T)$. In particular $N(T)$ is
polynomially bounded, and $\sum_j \gamma_j^{-p} < \infty$ **iff** $p > 1$ (ordinates
$\gamma_j > 0$ sorted). Smooth unfolding for numerics:
$x_j = \bar N(\gamma_j)$, $\bar N(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e} + \frac78$.

**5.2 Scaled ordinate distribution.** The empirical measures of
$\{\gamma_j/\gamma_N\}_{j\le N}$ converge weak-\* to the uniform distribution on $[0,1]$
(symmetrised: uniform on $[-1,1]$, even moments $\frac1{2k+1}$, odd moments $0$; the moment
problem is determinate).
*Proof:* $\dfrac{N(t\gamma_N)}{N(\gamma_N)} = t\Big(1 + \dfrac{\log t}{\log(\gamma_N/2\pi e)}\Big) + O\Big(\dfrac{\log\gamma_N}{N}\Big) \to t$
for each $t \in (0,1]$; convergence of CDFs gives weak-\* convergence; moments by bounded
convergence; determinacy from compact support. $\blacksquare$
*Numerical caution:* the $1/\log\gamma_N$ distortion is large at accessible heights
(measured $\frac1N\sum(\gamma_j/\gamma_N)^2 = 0.443$ at $N=40$ vs limit $1/3$); do not
"validate" this lemma by small-$N$ numerics.

**5.3 The zero spectrum's zeta function.** $Z(s) = \sum_{\gamma_j>0}\gamma_j^{-s}$
(Voros' *secondary* zeta function) converges for $\mathrm{Re}\,s > 1$ and continues
meromorphically, with its leading singularity (a double-pole structure at $s = 1$) inherited
from $N(T) \sim \frac{T}{2\pi}\log T$. A spectral zeta function encodes its spectrum in
*poles*; $\xi(s)$ carries the zeros as *zeros*. Keep the two categories separate.

**5.4 Verification data.** RH is verified for all zeros of height $\le 3\times10^{12}$
(Platt–Trudgian 2021); at least $5/12$ of all zeros lie on the critical line
(Pratt–Robles–Zaharescu–Zeindler 2020). These are computational/partial results, not evidence
usable as hypotheses.

---

## 6. Correct constructions to build on

### 6.1 The unnormalised prime kernel and its Hilbert space — **proven**

For $\lambda \in \mathbb C^+$ set $v_\lambda = \big(p^{-1/2+i\lambda}\big)_{p\ \mathrm{prime}}$;
then $\|v_\lambda\|_{\ell^2}^2 = \sum_p p^{-1-2\,\mathrm{Im}\lambda} < \infty$, and

$$K(\lambda,\mu) := \langle v_\lambda, v_\mu\rangle = \sum_p p^{-1+i(\lambda-\bar\mu)} = P\big(1 - i(\lambda-\bar\mu)\big)$$

is a positive-definite kernel on $\mathbb C^+\times\mathbb C^+$, where $P$ is the prime zeta
function. Classical facts about $P$: $P(s) = \sum_{k\ge1}\frac{\mu(k)}{k}\log\zeta(ks)$,
giving continuation to $\mathrm{Re}\,s > 0$ with logarithmic singularities at $s = 1/k$ and at
the points where $\zeta(ks) = 0$; near $s=1$, $P(s) = \log\frac1{s-1} + O(1)$. So $K$ is exact
and positive on $\mathbb C^+$, with a boundary logarithmic singularity on the diagonal — this
(not any $1/k_n$-average, see N2) is the honest "prime kernel".

The associated reproducing-kernel space is a Hilbert space of prime Dirichlet series
$F_w(\lambda) = \sum_p \overline{w_p}\,p^{-1/2+i\lambda}$ ($w \in \ell^2$), analytic on
$\mathbb C^+$. The translation flow $\lambda \mapsto \lambda + t$ acts unitarily
(diagonally, as $p^{it}$) with self-adjoint generator $= $ multiplication by $\log p$:
**the natural operator carried by the primes has pure point spectrum $\{\log p\}$, each simple.**
This is the *geometric side* of Theorem 4. The Hilbert–Pólya problem is precisely to construct
the dual object whose spectrum is the *zero side*; the obstruction to naive duality is
quantified exactly by §7.2.

### 6.2 De Branges spaces: the correct formulas and the correct target — **proven (classical)**

For entire $E$ with $E^*(z) = \overline{E(\bar z)}$, the de Branges kernel is the
*sesquilinear*

$$K_E(w,z) = \frac{i\,\big[E(z)\overline{E(w)} - E^{*}(z)\overline{E^{*}(w)}\big]}{2\pi\,(z-\bar w)},\qquad K_E(z,z) = \frac{|E(z)|^2 - |E^{*}(z)|^2}{4\pi\,\mathrm{Im}\,z}.$$

$E$ is **Hermite–Biehler (HB)** if $|E^{*}(z)| < |E(z)|$ on $\mathbb C^+$; then
$\mathcal H(E)$ exists with reproducing kernel $K_E \succeq 0$.
**Hermite–Biehler theorem** (Levin, ch. VII): if $E = A - iB$ is HB ($A,B$ real entire), then
$A$ and $B$ have only real, interlacing zeros.
**Correct target formulation:** exhibiting *any* HB function $E$ whose $A$-part
$\tfrac12(E + E^{*})$ equals $\Xi$ would prove RH (by the HB theorem, $A$'s zeros are then
real). By N3 this cannot be $E = \Xi$ itself. Conversely, RH furnishes such an $E$: with all
zeros real, $-\Xi'/\Xi$ is a Herglotz function on $\mathbb C^+$ (a convergent sum of Poisson
kernels over the paired zeros $\pm\gamma$), which makes $E = \Xi + i\,\Xi'$ Hermite–Biehler.
So this formulation is *equivalent* to RH, not easier — it locates the difficulty without
reducing it. Rigorous existing theory in this direction: Burnol's Sonine spaces; Lagarias'
survey of dB-space formulations.

### 6.3 The Tate/Mellin dictionary — **proven (classical)**

Mellin–Plancherel (Proposition 3) extends to the idele class group: on the $K$-invariant
subspace the scaling flow is unitarily equivalent to translation on $L^2(\mathbb R)$ — purely
absolutely continuous spectrum $\mathbb R$, *no discrete zeros*. The basic $K$-invariant vector
with Gaussian archimedean component has zeta integral

$$\int e^{-\pi x^2}\,|x|^s\,d^\times x \cdot \prod_p (1-p^{-s})^{-1} = \pi^{-s/2}\Gamma(s/2)\,\zeta(s) = \Lambda(s),$$

so the transform of that vector on the critical line is
$\Lambda(\tfrac12 + i\lambda)$ — an $L^2$-function identity (it decays like
$e^{-\pi|\lambda|/4}$), valuable as a *function-space* fact, not a spectral realisation.

---

## 7. The frontier: statements unconditionally equivalent to RH — **RH-equivalent**

These are theorems (the equivalences are proven); their positive resolution is RH itself.
They are the precise walls where every route of the reviewed series terminates, and where a new
project must aim if it aims at RH.

### 7.1 Hermite–Biehler positivity for shifted $\Xi$ — equivalence **proven** (full proof)

**Theorem 7.1.** For $h>0$ let $E_h(z) = \Xi(z+ih)$, so $E_h^{*}(z) = \Xi(z-ih)$, and let
$K_h$ be its de Branges kernel (§6.2). The following are equivalent:
1. RH (all zeros of $\Xi$ real);
2. $E_h$ is HB for every $h>0$;
3. $K_h \succeq 0$ on $\mathbb C^+\times\mathbb C^+$ for every $h>0$.

*Proof.* Unconditionally $\Xi(z) = \Xi(0)\prod_j\big(1 - z^2/\gamma_j^2\big)$ over the zero
multiset $\{\pm\gamma_j\}$, $\sum|\gamma_j|^{-2}<\infty$ (even Hadamard product; Titchmarsh
§2.12).

$(1)\Rightarrow(2)$: with all $\gamma_j$ real, for $z = x+iy$, $y>0$:
$$\left|\frac{E_h^{*}(z)}{E_h(z)}\right| = \prod_j\frac{|\gamma_j - z + ih|\,|\gamma_j + z - ih|}{|\gamma_j - z - ih|\,|\gamma_j + z + ih|} < 1,$$
since $(\gamma\mp x)^2 + (h-y)^2 < (\gamma\mp x)^2 + (h+y)^2$ factorwise, and the product
converges (factors $= 1 + O(\gamma_j^{-2})$).

$(2)\Rightarrow(3)$: $\varphi = E_h^{*}/E_h$ is a Schur function on $\mathbb C^+$. The Szegő
kernel $S(w,z) = \frac{i}{2\pi(z-\bar w)}$ is positive definite
($\frac{i}{z-\bar w} = \int_0^\infty e^{izt}\overline{e^{iwt}}\,dt$), and for Schur $\varphi$
the kernel $(1-\varphi(z)\overline{\varphi(w)})S(w,z) = \langle(I - M_\varphi M_\varphi^{*})S_w, S_z\rangle$
is positive semi-definite because $\|M_\varphi\|_{H^2} \le 1$. Multiplying by
$E_h(z)\overline{E_h(w)}$ (a congruence) gives exactly $K_h \succeq 0$.

$(3)\Rightarrow(1)$: the diagonal of $K_h$ gives $|\Xi(z-ih)| \le |\Xi(z+ih)|$ on
$\mathbb C^+$; taking $z = w - ih$ at a zero $w$ with $\mathrm{Im}\,w > h$ shows $w - 2ih$ is
again a zero. If RH failed, pick a zero $\gamma_0$ with $c = \mathrm{Im}\,\gamma_0 > 0$
(conjugation symmetry). For each $K \in \mathbb N$ take $h = c/(2K)$: iterating the step
$K$ times yields zeros with imaginary parts $c(1 - j/K)$, $j = 0,\dots,K$, all on the vertical
segment through $\mathrm{Re}\,\gamma_0$. Over all $K$ this forces infinitely many distinct
zeros in a compact set — impossible for a nonzero entire function. $\blacksquare$

### 7.2 Weil positivity — equivalence **proven (classical)**

For $g \in C_c^\infty(\mathbb R)$ let $\hat g(r) = \int g(u)e^{iru}du$ and let $Q(g)$ be the
right-hand side of Theorem 4 at $h = |\hat g|^2$ (admissible). Then

$$\mathrm{RH} \iff Q(g) \ge 0 \ \text{ for all } g \in C_c^\infty(\mathbb R).$$

The direction RH $\Rightarrow$ positivity is immediate from Theorem 4
($\sum_\rho|\hat g(\gamma_\rho)|^2 \ge 0$ when all $\gamma_\rho$ are real); the converse is
Weil's theorem (Weil 1952; Bombieri 2000). *Support bookkeeping:* the prime side of $Q(g)$
involves the autocorrelation $g\star\tilde g$, whose support is twice that of $g$; prime terms
vanish identically iff $\mathrm{supp}\,g \subseteq (-\tfrac12\log2, \tfrac12\log2)$, in which
case $Q(g)$ reduces to pole + archimedean terms — the regime of the known archimedean
positivity results (Yoshida; Connes–Consani).

### 7.3 Other proven equivalences and the adelic status

- **Li's criterion:** RH $\iff \lambda_n = \sum_\rho\big[1-(1-1/\rho)^n\big] \ge 0$ for all
  $n\ge1$ (Li 1997; Bombieri–Lagarias 1999).
- **Connes' program:** the *semi-local* trace formula is proven (Connes 1999); the *global*
  Hilbert-space trace formula is equivalent to Weil positivity, hence to RH.
- **Meyer (2005), proven:** the flow on suitable *nuclear* (non-Hilbert) function spaces over
  the adele class space realises **all** zeros, with multiplicity, unconditionally. This
  calibrates the problem exactly: spectral realisations exist; what is missing — provably — is
  a realisation with a positive inner product. Positivity is the entire remaining content.
- **Connes–Consani (2021–), proven partials:** Weil positivity at the archimedean place;
  ζ-cycle/prolate-operator realisations of low zeros.

---

## 8. Conditional results, stated correctly — **conditional**

**Montgomery (1973).** Assume RH. With
$F(\alpha,T) = N(T)^{-1}\sum_{0<\gamma,\gamma'\le T}T^{i\alpha(\gamma-\gamma')}w(\gamma-\gamma')$,
$w(x) = 4/(4+x^2)$: $F(\alpha,T) = T^{-2|\alpha|}\log T\,(1+o(1)) + |\alpha| + o(1)$ uniformly
for $|\alpha| \le 1$. For test functions with $\mathrm{supp}\,\hat f \subset (-1,1)$ this gives
the GUE pair-correlation density $1 - \big(\frac{\sin\pi u}{\pi u}\big)^2$. Beyond
$|\alpha| = 1$, and for full $n$-level statistics, GUE behaviour is **conjectural**
(Rudnick–Sarnak: restricted support, under the corresponding hypotheses; Odlyzko: numerical).
GUE statistics, even if fully established, are statements about the on-line statistics and do
not by themselves imply RH.

**Verified low-height statistics** (usable as a benchmark): first 120 zeros, unfolded by
$\bar N$ (§5.1): mean gap $1.0003$, gap variance $0.124$ (asymptotic GUE $\approx 0.18$,
Poisson $= 1$), minimum gap $0.387$ — clear level repulsion.

---

## 9. Starting points for a new project (suggestions, constrained by §3)

Directions consistent with every proven constraint above — listed as *options*, not results:

1. **Work on the boundary of the prime kernel (§6.1).** The space of prime Dirichlet series
   with its $\{\log p\}$-generator is exact; the explicit formula (Theorem 4) describes its
   interaction with the zero side. Studying the boundary quadratic form as
   $\mathrm{Im}\,\lambda \downarrow 0$ *is* the Weil form; restricted-support positivity
   (§7.2 bookkeeping) is the tractable entry point, with the archimedean case already proven
   in the literature.
2. **Sonine/Burnol spaces.** The rigorous de Branges-space home of $\zeta$; extending the
   known structure results is genuine mathematics with no false step required.
3. **Li coefficients.** Unconditional computation and asymptotic analysis of $\lambda_n$;
   positivity for finite ranges is provable and cumulative.
4. **Inverse spectral question for finite models (respecting N1).** Characterise which
   sequences are eigenvalues of structured non-contractive truncations whose numerical range
   grows; the Sierra-school models realise the smooth count rigorously — the fluctuation term
   is the open, well-posed target.
5. **Semi-local Weil positivity.** Extend Connes–Consani's archimedean positivity to places
   $\{ \infty, 2\}$, $\{\infty,2,3\},\dots$ — each instance is a self-contained provable/refutable
   problem, and the full limit is RH.

What a viable construction **must** provide, per §3: unbounded (or norm-growing) finite
stages (N1); unnormalised or correctly weighted kernels (N2); a non-real structure function if
de Branges-shaped (N3); self-adjointness rather than moment reality (N4); and its trace
identity must reduce to Theorem 4 — at which point its positivity statement will be found
equivalent to RH (§7), which is as it must be.

---

## 10. References

Guinand, *Proc. LMS* (2) 50 (1948) 107–119 · Weil, *Comm. Sém. Math. Lund* (1952) 252–265 ·
Barner, *J. reine angew. Math.* 323 (1981) 139–152 · Iwaniec–Kowalski, *Analytic Number
Theory*, Thm 5.12 · Titchmarsh, *Theory of the Riemann Zeta-function* (2nd ed.), §§2.1, 2.12,
9.3–9.4 · Levin, *Distribution of Zeros of Entire Functions*, ch. VII · de Branges, *Hilbert
Spaces of Entire Functions* (1968) · Lagarias, in *Frontiers in Number Theory, Physics and
Geometry I* (2006) · Burnol, *C.R.A.S.* (2002/03), *Forum Math.* 16 (2004) 789–840 · Berry–
Keating, *SIAM Rev.* 41 (1999) 236–266 · Sierra–Rodríguez-Laguna, *PRL* 106 (2011) 200201 ·
Connes, *Selecta Math.* 5 (1999) 29–106 · Connes–Consani, *Selecta Math.* 27 (2021) and
ζ-cycles papers · Meyer, *Duke Math. J.* 127 (2005) 519–595 · Voros, *Zeta Functions over
Zeros of Zeta Functions* (2010) · Montgomery, *PSPM* 24 (1973) 181–193 · Rudnick–Sarnak,
*Duke Math. J.* 81 (1996) 269–322 · Odlyzko, *Math. Comp.* 48 (1987) 273–308 · Li, *JNT* 65
(1997) 325–333 · Bombieri–Lagarias, *JNT* 77 (1999) 274–287 · Bombieri, *Rend. Lincei* (9) 11
(2000) 183–233 · Platt–Trudgian, *Bull. LMS* 53 (2021) 792–797 ·
Pratt–Robles–Zaharescu–Zeindler, *Res. Math. Sci.* 7 (2020).

---

*Everything above tagged proven is safe to cite and build on; everything tagged RH-equivalent
is a wall, not a bridge. The discarded material (and why it was discarded) is documented in
[worksheet.md](worksheet.md) and
[barry-keating-addendum-errata.html](barry-keating-addendum-errata.html).*
