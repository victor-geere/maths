# The Prime Side of Hilbert–Pólya

**An unconditional spectral package assembled from the prime kernel**

*Research note — 3 July 2026*

**Sources.** This note is built from exactly two companion documents — the unnormalised prime
kernel ([prime-kernel.html](prime-kernel.html)) and the rigorous core of the composite-generator
sieve ([prime-sieve.html](../berry-keating/prime-sieve.html)) — plus classical literature cited in §9. Every
result below is tagged **proven** / **conditional** per the repository convention; the single
imported classical identity (Fact 4.1) is cited, not reproved, and its normalisation is verified
numerically to $10^{-30}$ in §7.

---

## 0. Scope: what "the prime side" means

The Hilbert–Pólya idea asks for a self-adjoint operator whose spectrum is the multiset
$\{\gamma_\rho\}$ of ordinates of the nontrivial zeros $\rho = \tfrac12 + i\gamma_\rho$ of
$\zeta$. The Guinand–Weil explicit formula (Fact 4.1) is an identity between two sides:

- a **zero side** $\sum_\rho h(\gamma_\rho)$ — spectral data of an operator *nobody has
  constructed*;
- a **prime side** $\sum_{n\ge2} \frac{\Lambda(n)}{\sqrt n}\big(g(\log n) + g(-\log n)\big)$
  plus archimedean terms — arithmetic data that is unconditionally available.

[prime-kernel.html](prime-kernel.html) §1 identifies the three ingredients a construction on the
prime side needs:

> "the reproducing-kernel-Hilbert-space package built on top of it, its exact translation-flow
> spectral theory, and its precise boundary behaviour — the three ingredients a future
> construction on the 'prime side' of Hilbert–Pólya needs."

This note performs that construction. Concretely:

1. **Ingredient (i) upgraded (§2).** The RKHS package is rebuilt with the von Mangoldt weights
   the explicit formula actually uses. The kernel acquires the closed form
   $K_\Lambda(\lambda,\mu) = -\frac{\zeta'}{\zeta}\big(1 - i(\lambda-\bar\mu)\big)$.
2. **Ingredient (ii) upgraded (§3–4).** The translation flow has self-adjoint generator $A$ with
   simple pure point spectrum $\{k\log p\}$, and the arithmetic side of the explicit formula is
   realised as a genuine operator trace: $\mathcal W_{\mathrm{ar}}(g) = \mathrm{Tr}\big(\mathbb W\, g(\mathbb A)\big)$.
3. **Ingredient (iii) upgraded (§5).** At the boundary the kernel is $2\pi\times$ the Szegő
   kernel of the half-plane plus a regular part whose diagonal value is $-\gamma_E$
   (Euler–Mascheroni). The depth to which the kernel continues holomorphically below its
   boundary is $1 - \sup_\rho \beta \le \tfrac12$, with equality **iff** RH; the flow's weighted
   character $\chi_W(z) = -\frac{\zeta'}{\zeta}(\tfrac12 - iz)$ has poles exactly at the shifted
   zeros, and RH is equivalent to those poles being real.
4. **Constructive skeleton (§6).** The sieve of [prime-sieve.html](../berry-keating/prime-sieve.html) produces the
   spectrum stage by stage, with a proven truncation bound for the trace identity.

**What this note does *not* do.** It does not construct the zero side, and it does not prove RH.
All equivalences with RH below are proven *as equivalences*; no claim is made about which side of
them holds. Per the repository convention, nothing here is asserted to imply RH except statements
provably tied to the zeros themselves (via the meromorphic continuation of $\zeta'/\zeta$ and the
classical explicit formula), and those are stated as equivalences only.

---

## 1. The three ingredients, and the design constraints

| Ingredient (from [prime-kernel.html](prime-kernel.html)) | As recorded there | Upgraded here |
|---|---|---|
| (i) RKHS package | $K(\lambda,\mu) = P(1-i(\lambda-\bar\mu))$, $\mathcal H_P \cong \ell^2(\mathrm{primes})$ | $K_\Lambda(\lambda,\mu) = -\frac{\zeta'}{\zeta}(1-i(\lambda-\bar\mu))$, $\mathcal H_\Lambda \cong \ell^2_\Lambda(\mathcal Q)$ (§2) |
| (ii) translation flow | generator $\mathrm{diag}(\log p)$, simple pure point | generator $\mathrm{diag}(\log q)$ on prime powers; trace identity = arithmetic side of the explicit formula (§3–4) |
| (iii) boundary behaviour | $K(\lambda,\lambda) = -\log(2\,\mathrm{Im}\,\lambda) + c_0 + o(1)$ | Szegő pole $\frac{1}{2\,\mathrm{Im}\,\lambda} - \gamma_E + O(\mathrm{Im}\,\lambda)$; continuation depth $= \tfrac12$ iff RH; $\chi_W$ pole catalogue (§5) |

Three design constraints, all **proven** in the companions, dictate the shape of the
construction:

- **(C1) No normalisation.** The $1/\pi(M_n)$-normalised prime sums tend to zero uniformly
  ([prime-sieve.html](../berry-keating/prime-sieve.html) §4, one-line Chebyshev estimate; also
  [prime-kernel.html](prime-kernel.html) §1). Every object below is an *unnormalised, absolutely
  convergent* sum.
- **(C2) Positions are flat; structure lives in the logarithms.** The normalised prime measure
  equidistributes: $\widehat\mu_n(k) = O_k(1/\log M_n) \to 0$
  ([prime-sieve.html](../berry-keating/prime-sieve.html) Theorem 3.1). Rescaled prime *positions* carry only
  density in the limit; all arithmetic content must be drawn from the unnormalised multiplicative
  data — the frequencies $\{\log q\}$ and their weights. That is exactly what the kernel package
  uses.
- **(C3) Constructivity.** The sieve enumerates the primes exactly, block by block
  ([prime-sieve.html](../berry-keating/prime-sieve.html) Lemma 1.2), at the quantitative rate of its
  Proposition 1.3. The package must therefore be recoverable as a limit of finite stages with
  controlled error — done in §6.

---

## 2. Ingredient (i) upgraded: the von Mangoldt kernel and its RKHS

The arithmetic side of the explicit formula is supported on prime **powers** $n = p^k$ with
weights $\Lambda(n)/\sqrt n = (\log p)\,p^{-k/2}$ — not on primes with weight $1$. The prime
kernel of the companion note is the correct prototype but carries the wrong weights for
Hilbert–Pólya; the upgrade is forced (uniquely — Proposition 3.6).

**Definition 2.1.** Let $\mathcal Q = \{p^k : p \text{ prime},\ k \ge 1\}$ be the set of prime
powers, $\Lambda(p^k) = \log p$ the von Mangoldt weight, and

$$
\ell^2_\Lambda \;=\; \Big\{ x = (x_q)_{q \in \mathcal Q} \;:\; \Vert x\Vert_\Lambda^2 := \sum_{q \in \mathcal Q} \Lambda(q)\,\lvert x_q\rvert^2 < \infty \Big\},
\qquad
\langle x, y\rangle_\Lambda = \sum_{q} \Lambda(q)\, x_q \overline{y_q}.
$$

**Lemma 2.2 (well-definedness). — proven**
For $\lambda \in \mathbb C^+$ let $v_\lambda = \big(q^{-1/2+i\lambda}\big)_{q\in\mathcal Q}$. Then
$v_\lambda \in \ell^2_\Lambda$, the map $\lambda \mapsto v_\lambda$ is holomorphic
$\mathbb C^+ \to \ell^2_\Lambda$, and

$$
\Vert v_\lambda \Vert_\Lambda^2 \;=\; \sum_{q} \Lambda(q)\, q^{-1-2\,\mathrm{Im}\,\lambda} \;=\; -\frac{\zeta'}{\zeta}\big(1 + 2\,\mathrm{Im}\,\lambda\big).
$$

*Proof.* $\lvert q^{-1/2+i\lambda}\rvert^2 = q^{-1-2\,\mathrm{Im}\,\lambda}$, and
$\sum_q \Lambda(q)\, q^{-s} = -\frac{\zeta'}{\zeta}(s)$ is the classical Dirichlet series of
$-\zeta'/\zeta$, absolutely convergent for $\mathrm{Re}\,s > 1$ — here
$s = 1 + 2\,\mathrm{Im}\,\lambda > 1$. Holomorphy is termwise differentiation of a locally
uniformly dominated series, exactly as in Lemma 2.1 of
[prime-kernel.html](prime-kernel.html). $\blacksquare$

**Definition–Proposition 2.3 (the von Mangoldt kernel). — proven**
For $\lambda, \mu \in \mathbb C^+$,

$$
K_\Lambda(\lambda,\mu) \;:=\; \langle v_\lambda, v_\mu \rangle_\Lambda \;=\; \sum_{q\in\mathcal Q} \Lambda(q)\, q^{-1+i(\lambda-\bar\mu)} \;=\; -\frac{\zeta'}{\zeta}\big(1 - i(\lambda - \bar\mu)\big),
$$

and $K_\Lambda$ is positive semi-definite on $\mathbb C^+\times\mathbb C^+$.

*Proof.* With $u = \lambda - \bar\mu$, $\mathrm{Re}(1-iu) = 1 + \mathrm{Im}\,\lambda +
\mathrm{Im}\,\mu > 1$, so the Dirichlet series identity applies term by term. Positivity is
automatic for a Gram kernel:
$\sum_{i,j} c_i \bar c_j K_\Lambda(\lambda_i,\lambda_j) = \Vert \sum_i c_i v_{\lambda_i}\Vert_\Lambda^2 \ge 0$.
$\blacksquare$

*Domain remark (as in the companion).* The series converges on the larger region
$\mathrm{Im}\,\lambda + \mathrm{Im}\,\mu > 0$, where $K_\Lambda$ continues holomorphically in two
variables; we keep to $\mathbb C^+\times\mathbb C^+$ where it is manifestly a Gram kernel.

**Lemma 2.4 (totality / uniqueness of coefficients). — proven**
If $x \in \ell^2_\Lambda$ and $\langle v_\lambda, x\rangle_\Lambda = 0$ for all
$\lambda \in \mathbb C^+$, then $x = 0$. Hence $\{v_\lambda\}_{\lambda\in\mathbb C^+}$ is total
in $\ell^2_\Lambda$.

*Proof.* Set $c_q = \Lambda(q)\,\overline{x_q}\,q^{-1/2}$, so that
$\langle v_\lambda, x\rangle_\Lambda = \sum_q c_q\, e^{i\lambda \log q}$. By Cauchy–Schwarz, for
every $\sigma > 0$,

$$
\sum_q \lvert c_q\rvert\, q^{-\sigma} \;\le\; \Vert x\Vert_\Lambda \Big( \sum_q \Lambda(q)\, q^{-1-2\sigma} \Big)^{1/2} \;=\; \Vert x\Vert_\Lambda \Big( -\tfrac{\zeta'}{\zeta}(1+2\sigma) \Big)^{1/2} < \infty,
$$

so the general Dirichlet series $G(\sigma) := \sum_q c_q q^{-\sigma}$ (this is
$\langle v_{i\sigma}, x\rangle_\Lambda$) converges absolutely for $\sigma>0$ and vanishes
identically. Enumerate $\mathcal Q = \{q_1 < q_2 < \cdots\}$. Then

$$
q_1^{\sigma} G(\sigma) = c_{q_1} + \sum_{j\ge2} c_{q_j} (q_1/q_j)^{\sigma} \longrightarrow c_{q_1}
\qquad (\sigma \to \infty),
$$

by dominated convergence ($\lvert c_{q_j}\rvert (q_1/q_j)^{\sigma} \le \lvert c_{q_j}\rvert\, q_1/q_j$
for $\sigma \ge 1$, summable by the bound above with $\sigma = 1$, and each term $\to 0$). Since
$G \equiv 0$, $c_{q_1} = 0$; induction along the enumeration gives $c_q = 0$ for all $q$, i.e.
$x = 0$. $\blacksquare$

**Definition 2.5 (the RKHS of von Mangoldt Dirichlet series).**
For $x \in \ell^2_\Lambda$ set
$F_x(\lambda) = \langle v_\lambda, x\rangle_\Lambda = \sum_q \Lambda(q)\,\overline{x_q}\, q^{-1/2+i\lambda}$,
holomorphic on $\mathbb C^+$, and let
$\mathcal H_\Lambda = \{F_x : x \in \ell^2_\Lambda\}$ with
$\Vert F_x\Vert_{\mathcal H_\Lambda} := \Vert x\Vert_\Lambda$ — well defined by Lemma 2.4. Then
$x \mapsto F_x$ is an isometric isomorphism $\ell^2_\Lambda \to \mathcal H_\Lambda$, and
$\mathcal H_\Lambda$ is a reproducing kernel Hilbert space with kernel $K_\Lambda$:
$K_\Lambda(\cdot,\mu) = F_{v_\mu}$, and
$\langle F_x, K_\Lambda(\cdot,\mu)\rangle_{\mathcal H_\Lambda} = \langle x, v_\mu\rangle_\Lambda = \overline{F_x(\mu)}$
— the same conjugate-linearity bookkeeping as §4 of [prime-kernel.html](prime-kernel.html).

**Remark 2.6 (relation to the prime kernel). — proven**
Splitting $\mathcal Q$ by the exponent $k$,

$$
K_\Lambda \;=\; \sum_{k\ge1} L_k, \qquad L_k(u) \;=\; \sum_p \log p\; p^{-k(1-iu)}, \qquad u = \lambda-\bar\mu .
$$

The $k=1$ layer is the derivative of the prime kernel of the companion note along its own
translation flow: $L_1(u) = -i\,\frac{d}{du} P(1-iu) = -i\,\partial K/\partial u$. Each layer
$k \ge 2$ converges for $\mathrm{Im}\,u > \frac1k - 1$, hence is holomorphic on the full strip
$\mathrm{Im}\,u > -\tfrac12$ relevant below. So the von Mangoldt kernel is *forced* by
ingredients (i)+(ii) together: differentiate the prime kernel along the flow (this installs the
$\log p$ weights) and complete with the regular higher layers (this installs the prime powers).
What results carries exactly the explicit formula's weights.

---

## 3. Ingredient (ii) upgraded: the flow, its generator, and the trace identity

**Proposition 3.1 (translation flow and generator). — proven**
The shift $(U_t F)(\lambda) = F(\lambda+t)$ on $\mathcal H_\Lambda$ corresponds under §2.5 to the
diagonal unitary group $(\Lambda_t x)_q = q^{it} x_q$ on $\ell^2_\Lambda$. The group
$\{\Lambda_t\}$ is strongly continuous; its self-adjoint generator is

$$
(A x)_q = (\log q)\, x_q, \qquad \mathcal D(A) = \Big\{x : \sum_q \Lambda(q) (\log q)^2 \lvert x_q\rvert^2 < \infty\Big\},
$$

with **pure point spectrum** $\sigma(A) = \{\log q : q \in \mathcal Q\} = \{k \log p\}$, **every
eigenvalue simple**, and no further spectrum in any bounded interval.

*Proof.* Identical to Proposition 5.1 of [prime-kernel.html](prime-kernel.html), with two
substitutions. Simplicity: $\log q$ are pairwise distinct across $\mathcal Q$ because
$p^k = p'^{k'}$ forces $p = p'$, $k = k'$ by unique factorisation. Discreteness: every bounded
interval contains finitely many prime powers, so $\sigma(A)$ is closed and discrete, each point
an isolated simple eigenvalue with eigenvector $\delta_q$; Stone's theorem identifies the
generator. $\blacksquare$

**Remark 3.2 (the weights are spectral data).** Since $\sigma(A)$ is simple and pure point,
every diagonal operator is a Borel function of $A$. In particular the weight operator of
Theorem 3.4 below is $W = w(A)$ with

$$
w(k\log p) \;=\; \frac{\Lambda(p^k)}{\sqrt{p^k}} \;=\; (\log p)\, e^{-\frac{k \log p}{2}}, \qquad w = 0 \ \text{off } \sigma(A),
$$

well defined on the spectrum by unique factorisation. The pair $(A, W)$ therefore contains no
data beyond $A$ itself plus one Borel function — "the primes carry a self-adjoint operator" in
the exact sense of the companion, now with the explicit-formula weights attached spectrally.

**Lemma 3.3 (diagonal trace-class criterion). — proven**
A diagonal operator $D$ on $\ell^2_\Lambda$ with entries $(d_q)$ is trace class iff
$\sum_q \lvert d_q\rvert < \infty$, and then $\mathrm{Tr}\,D = \sum_q d_q$ (independently of the
weight in the inner product).

*Proof.* The vectors $e_q = \delta_q / \sqrt{\Lambda(q)}$ form an orthonormal basis of
$\ell^2_\Lambda$ and $D e_q = d_q e_q$; thus $\lvert D\rvert e_q = \lvert d_q\rvert e_q$, the
singular values of $D$ are $\{\lvert d_q\rvert\}$, and
$\mathrm{Tr}\,\lvert D\rvert = \sum_q \lvert d_q\rvert$. When finite,
$\mathrm{Tr}\, D = \sum_q \langle D e_q, e_q\rangle_\Lambda = \sum_q d_q$ converges absolutely.
$\blacksquare$

**Theorem 3.4 (prime-side trace identity). — proven**
Let $W = w(A) \ge 0$ as in Remark 3.2 and let $g:\mathbb R \to \mathbb C$ be Borel with
$\lvert g(x)\rvert \le C e^{-(1/2+\varepsilon)x}$ on $x \ge \log 2$ for some
$\varepsilon > 0$. Then $W^{1/2}\, g(A)\, W^{1/2}$ is trace class on $\ell^2_\Lambda$ and

$$
\mathrm{Tr}\big(W^{1/2} g(A) W^{1/2}\big) \;=\; \sum_{n \ge 2} \frac{\Lambda(n)}{\sqrt n}\, g(\log n),
\qquad
\big\Vert W^{1/2} g(A) W^{1/2} \big\Vert_{\mathrm{tr}} \;\le\; C \cdot \Big(-\frac{\zeta'}{\zeta}(1+\varepsilon)\Big).
$$

*Proof.* $W^{1/2} g(A) W^{1/2}$ is diagonal with entries
$\frac{\Lambda(q)}{\sqrt q}\, g(\log q)$, and

$$
\sum_q \frac{\Lambda(q)}{\sqrt q}\,\lvert g(\log q)\rvert \;\le\; C \sum_q \Lambda(q)\, q^{-1-\varepsilon} \;=\; C\,\Big(-\frac{\zeta'}{\zeta}(1+\varepsilon)\Big) < \infty .
$$

Apply Lemma 3.3; the trace is the stated sum, which runs over prime powers — i.e. over all
$n \ge 2$ with $\Lambda(n) \ne 0$. $\blacksquare$

**Definition 3.5 (the symmetric double).** The zero side of the explicit formula is even in
$\gamma \leftrightarrow -\gamma$; the matching prime-side operator is the double

$$
\mathbb A = A \oplus (-A), \qquad \mathbb W = W \oplus W \quad \text{on} \quad \ell^2_\Lambda \oplus \ell^2_\Lambda,
$$

self-adjoint with simple pure point spectrum $\{\pm k\log p\}$. For $g$ Borel with
$\lvert g(x)\rvert \le Ce^{-(1/2+\varepsilon)\lvert x\rvert}$, Theorem 3.4 applied to each summand
gives the **arithmetic Weil functional as a trace**:

$$
\mathrm{Tr}\big(\mathbb W^{1/2} g(\mathbb A)\, \mathbb W^{1/2}\big) \;=\; \sum_{n\ge2} \frac{\Lambda(n)}{\sqrt n}\big(g(\log n) + g(-\log n)\big) \;=:\; \mathcal W_{\mathrm{ar}}(g).
$$

**Proposition 3.6 (uniqueness of the weight). — proven**
If $W'$ is a positive diagonal operator on $\ell^2_\Lambda$ with
$\mathrm{Tr}\big(W'^{1/2} g(A) W'^{1/2}\big) = \sum_{n\ge2} \frac{\Lambda(n)}{\sqrt n} g(\log n)$
for all continuous compactly supported $g \ge 0$, then $W' = W$.

*Proof.* Fix $q_0 \in \mathcal Q$. Since $\sigma(A)$ is discrete, choose $g$ a continuous bump
with $g(\log q_0) = 1$, supported so small that no other $\log q$ meets its support. Both sides
reduce to single terms: $w'_{q_0} = \Lambda(q_0)/\sqrt{q_0}$. $\blacksquare$

**Proposition 3.7 (rigidity: the zero side is not a re-coordinatisation). — proven**
(i) If a self-adjoint $B$ on $\ell^2_\Lambda$ satisfies $e^{itB} = e^{itA}$ for all $t$, then
$B = A$ (uniqueness of the Stone generator).
(ii) Let $N_A(T) = \#\{\sigma(A) \cap [0,T]\}$ and let $N(T)$ be the zero-counting function.
Then

$$
N_A(T) = \sum_{k\ge1} \pi\big(e^{T/k}\big) = \frac{e^T}{T}\big(1 + O(1/T)\big),
\qquad
N(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e} + O(\log T)
$$

(prime number theorem; Riemann–von Mangoldt, both unconditional). Consequently no unitary
conjugation $VAV^{*}$, nor any affine rescaling $aA + b$, has spectrum with the zeros' counting
asymptotics: the spectrum $\{k\log p\}$ grows exponentially in density, the zeros logarithmically.
The dual object Hilbert–Pólya asks for must live on a **new** space, paired with $(A,W)$ through
the explicit formula — it cannot be obtained by deforming coordinates inside the prime side.
(This sharpens the "pinned to $\{\log p\}$" reading of
[prime-kernel.html](prime-kernel.html) §5.)

*Proof.* (i) Differentiate strongly at $t=0$ on the common core of finitely supported vectors.
(ii) The $k=1$ term is $\pi(e^T) = \frac{e^T}{T}(1+O(1/T))$ by PNT; the terms $k \ge 2$ total at
most $(T/\log 2)\, e^{T/2} = O(e^{T/2}\, T)$. Unitaries preserve spectra; affine maps send
$N_A(T)$ to $N_A((T-b)/a)$, still exponential. An exponential and a $T\log T$ counting function
disagree for large $T$, so the spectra differ as sets. $\blacksquare$

---

## 4. The explicit formula as a trace identity

**Fact 4.1 (Guinand–Weil explicit formula — classical, cited).**
Let $h$ be even, holomorphic on $\lvert \mathrm{Im}\, r\rvert \le \tfrac12 + \delta$, with
$h(r) \ll (1+\lvert r\rvert)^{-2-\delta}$ there, and let
$g(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} h(r)\, e^{-irx}\, dr$. Then, with $\rho = \tfrac12 + i\gamma_\rho$
running over the nontrivial zeros with multiplicity,

$$
\sum_\rho h(\gamma_\rho)
\;=\; h\Big(\frac{i}{2}\Big) + h\Big(-\frac{i}{2}\Big)
\;-\; g(0)\log\pi
\;+\; \frac{1}{2\pi}\int_{-\infty}^{\infty} h(r)\, \mathrm{Re}\,\frac{\Gamma'}{\Gamma}\Big(\frac14 + \frac{ir}{2}\Big)\, dr
\;-\; 2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\, g(\log n).
$$

*References:* Guinand (1948), Weil (1952), Montgomery–Vaughan Thm 12.13, Iwaniec–Kowalski
Thm 5.12. This exact normalisation (every constant and factor) is confirmed numerically to
$2\times10^{-31}$ in §7E.

**Corollary 4.2 (the explicit formula with its prime side as an operator trace). — proven,
given Fact 4.1**
For $h, g$ as in Fact 4.1,

$$
\sum_\rho h(\gamma_\rho)
\;=\; h\Big(\frac{i}{2}\Big) + h\Big(-\frac{i}{2}\Big)
\;-\; g(0)\log\pi
\;+\; \frac{1}{2\pi}\int_{-\infty}^{\infty} h(r)\, \mathrm{Re}\,\frac{\Gamma'}{\Gamma}\Big(\frac14 + \frac{ir}{2}\Big) dr
\;-\; \mathrm{Tr}\big(\mathbb W^{1/2}\, g(\mathbb A)\, \mathbb W^{1/2}\big).
$$

*Proof.* It suffices to check $g$ lies in the trace class of Definition 3.5 with
$\varepsilon = \delta$. Shift the contour in $g(x) = \frac{1}{2\pi}\int h(r) e^{-irx} dr$ to
$\mathrm{Im}\, r = \mp(\tfrac12+\delta)$ (legitimate by the strip holomorphy and decay of $h$):
$\lvert g(x)\rvert \le e^{-(1/2+\delta)\lvert x\rvert}\cdot \frac{1}{2\pi}\int \lvert h(\xi \mp i(\tfrac12+\delta))\rvert\, d\xi$.
Since $g$ is even, $2\sum_n \frac{\Lambda(n)}{\sqrt n} g(\log n) = \mathcal W_{\mathrm{ar}}(g) = \mathrm{Tr}(\mathbb W^{1/2} g(\mathbb A) \mathbb W^{1/2})$
by Theorem 3.4 / Definition 3.5. $\blacksquare$

**Reading 4.3 (the honest asymmetry).** In Corollary 4.2 the prime side is now the trace of a
*constructed* self-adjoint package $(\mathbb A, \mathbb W)$; the zero side
$\sum_\rho h(\gamma_\rho)$ is still only a sum — the spectral data of an operator that does not
yet exist. Hilbert–Pólya is precisely the demand that the left side become
$\mathrm{Tr}\, h(H)$ for a self-adjoint $H$ on a genuine Hilbert space. Weil's criterion
(Weil 1952) says RH is equivalent to the positivity
$\sum_\rho h(\gamma_\rho) \ge 0$ whenever $h = \lvert\widehat{\phi}\rvert^2$-type
(i.e. $g = \phi * \tilde\phi$, $\phi \in C_c^\infty$); by Corollary 4.2 that positivity is a
statement *about* our prime-side trace plus explicit archimedean terms — proven equivalent to
RH, not a route around it. By Proposition 3.7 the missing operator cannot be conjured by
re-coordinatising $(\mathbb A, \mathbb W)$; it must be a second object dual to it through this
identity.

---

## 5. Ingredient (iii) upgraded: boundary behaviour, and where RH sits

Throughout, $u = \lambda - \bar\mu$; the kernel's natural boundary is $\mathrm{Im}\,u = 0$.

**Proposition 5.1 (Szegő comparison; the boundary constant is $-\gamma_E$). — proven**
Let $S(\lambda,\mu) = \frac{i}{2\pi(\lambda-\bar\mu)}$ be the Szegő (reproducing) kernel of the
Hardy space $H^2(\mathbb C^+)$. Then

$$
R(u) \;:=\; K_\Lambda(\lambda,\mu) - 2\pi\, S(\lambda,\mu) \;=\; -\frac{\zeta'}{\zeta}(1-iu) - \frac{i}{u}
$$

extends holomorphically across $u = 0$ with $R(0) = -\gamma_E$, and along the diagonal

$$
K_\Lambda(\lambda,\lambda) \;=\; \frac{1}{2\,\mathrm{Im}\,\lambda} \;-\; \gamma_E \;+\; O(\mathrm{Im}\,\lambda), \qquad \mathrm{Im}\,\lambda \downarrow 0 .
$$

*Proof.* From $\zeta(s) = \frac{1}{s-1} + \gamma_E + O(s-1)$,
$\log\zeta(s) = -\log(s-1) + \gamma_E (s-1) + O((s-1)^2)$, hence
$-\frac{\zeta'}{\zeta}(s) = \frac{1}{s-1} - \gamma_E + O(s-1)$. Substitute $s = 1 - iu$, so
$\frac{1}{s-1} = \frac{i}{u}$: the pole cancels in $R$ and $R(0) = -\gamma_E$. The diagonal is
$u = 2i\,\mathrm{Im}\,\lambda$, giving the stated expansion. $\blacksquare$

*Comparison with ingredient (iii) as imported:* the prime kernel had a **logarithmic**
singularity with constant $c_0 = \sum_{k\ge2}\frac{\mu(k)}{k}\log\zeta(k) = -0.3157\ldots$
([prime-kernel.html](prime-kernel.html) §3, §6.3); the von Mangoldt kernel has a **simple pole**
— exactly $2\pi\times$ Szegő — with constant $-\gamma_E = -0.5772\ldots$ (verified §7C). To
leading order at its boundary the prime side is the *free* object $H^2(\mathbb C^+)$; the entire
arithmetic content sits in the regular part $R$.

**Theorem 5.2 (continuation depth of the boundary correction). — proven**
$R$ continues to a meromorphic function on $\mathbb C$, holomorphic at $u=0$, with simple poles
exactly at

$$
u_\rho = -\gamma - i(1-\beta) \quad (\rho = \beta + i\gamma \ \text{nontrivial zero, residue } -i\,m_\rho),
\qquad
u = -i(1+2k) \quad (k \ge 1, \ \text{trivial zeros}).
$$

Consequently:

1. *(Unconditional regularity.)* $R$ is holomorphic in a neighbourhood of every real $u$
   — because $\zeta(1+it) \ne 0$ (de la Vallée Poussin) — and, quantitatively, in the region
   $\{\mathrm{Im}\,u > -c/\log(\lvert\mathrm{Re}\,u\rvert + 2)\}$ for the classical zero-free
   constant $c$.
2. *(Depth.)* The supremum of $d \ge 0$ such that $R$ is holomorphic on
   $\{\mathrm{Im}\,u > -d\}$ equals $1 - \sup_\rho \beta \le \tfrac12$; the inequality is an
   equality **iff RH**. (That the depth never exceeds $\tfrac12$ is unconditional: zeros with
   $\beta = \tfrac12$ exist — Hardy 1914.)

*Proof.* $-\zeta'/\zeta$ is meromorphic on $\mathbb C$ with simple poles at $s=1$ (residue $1$),
at each nontrivial zero $\rho$ (residue $-m_\rho$) and each trivial zero $-2k$ (residue $-1$);
$s = 1 - iu$ maps these to $u = i(s-1)$, i.e. $u = 0$, $u_\rho = -\gamma - i(1-\beta)$,
$u = -i(1+2k)$, with residues multiplied by $i$ (if $f(s) \sim \frac{c}{s - s_0}$ then, in $u$,
$f \sim \frac{ic}{u - u_0}$). The $u = 0$ pole is removed by the Szegő subtraction
(Proposition 5.1). Since $0 < \beta < 1$ strictly, every $u_\rho$ has
$\mathrm{Im}\,u_\rho = -(1-\beta) < 0$; statement 1 follows from the classical zero-free region
$\beta \le 1 - c/\log(\lvert\gamma\rvert+2)$. For statement 2: no pole lies above
$\mathrm{Im}\,u = -(1-\sup_\rho\beta)$, and poles come arbitrarily close to that line by
definition of the supremum; by the functional equation the zeros are symmetric under
$\beta \leftrightarrow 1-\beta$, so $\sup_\rho \beta \ge \tfrac12$, with equality precisely when
no zero has $\beta > \tfrac12$, i.e. precisely under RH. $\blacksquare$

**Theorem 5.3 (the flow character: ingredients (ii) and (iii) fused). — proven**
For $\mathrm{Im}\,z > \tfrac12$ the operator $W e^{izA}$ is trace class on $\ell^2_\Lambda$, and
the **weighted flow character**

$$
\chi_W(z) \;:=\; \mathrm{Tr}\big(W e^{izA}\big) \;=\; \sum_{q\in\mathcal Q} \Lambda(q)\, q^{-\frac12 + iz} \;=\; -\frac{\zeta'}{\zeta}\Big(\frac12 - iz\Big)
$$

is holomorphic there. It continues meromorphically to all of $\mathbb C$, with simple poles
exactly at:

| pole | location | residue |
|---|---|---|
| pole of $\zeta$ | $z = \tfrac{i}{2}$ | $+i$ |
| nontrivial zero $\rho = \beta+i\gamma$ | $z_\rho = -\gamma + i\big(\beta - \tfrac12\big)$ | $-i\, m_\rho$ |
| trivial zero $-2k$ | $z = -i\big(2k + \tfrac12\big)$ | $-i$ |

Moreover $\chi_W(z) = K_\Lambda$ evaluated at $u = z - \tfrac{i}{2}$: **the flow character is
the kernel continued to depth $\tfrac12$ below its boundary** — real time for the flow probes
exactly the depth that Theorem 5.2 shows RH governs.

*Proof.* Trace class: the diagonal entries are $\Lambda(q) q^{-1/2+iz}$ with absolute sum
$\sum_q \Lambda(q)\, q^{-1/2-\mathrm{Im}\,z} = -\frac{\zeta'}{\zeta}(\tfrac12 + \mathrm{Im}\,z)$,
finite iff $\mathrm{Im}\,z > \tfrac12$ (Lemma 3.3), and the trace is the Dirichlet series at
$s = \tfrac12 - iz$. The pole catalogue is the $s$-plane list transported by
$z = i(s - \tfrac12)$, residues multiplied by $i$ as in Theorem 5.2. The last statement is
$1 - i(z - \tfrac{i}{2}) = \tfrac12 - iz$. $\blacksquare$

**Corollary 5.4 (RH as a regularity statement about the prime side). — proven equivalences**
The following are equivalent:

1. The Riemann Hypothesis.
2. $\chi_W$ continues holomorphically to $\{\mathrm{Im}\,z > 0\}\setminus\{\tfrac{i}{2}\}$.
3. Every zero-pole $z_\rho$ of $\chi_W$ is real.
4. The boundary correction $R$ of Theorem 5.2 is holomorphic on
   $\{\mathrm{Im}\,u > -\tfrac12\}$.

*Proof.* $z_\rho \in \mathbb R \Leftrightarrow \beta = \tfrac12$. If RH fails, the functional
equation supplies a zero with $\beta > \tfrac12$, i.e. a pole with
$\mathrm{Im}\,z_\rho = \beta - \tfrac12 \in (0, \tfrac12)$, destroying 2; conversely under RH all
$z_\rho$ are real and the only singularity with $\mathrm{Im}\,z > 0$ is $z = \tfrac{i}{2}$. The
map $\rho \mapsto z_\rho$ is injective, and residues $-i m_\rho \ne 0$, so no pole can cancel.
Equivalence with 4 is Theorem 5.2(2). $\blacksquare$

**Remark 5.5 (under RH: the flow hears the zeros). — conditional (assumes RH)**
Under RH, $\chi_W$ extends meromorphically across the real axis with simple real poles exactly at
$z = -\gamma_\rho$ (both signs, since zeros come in conjugate pairs), residues $-i m_\rho$: the
singular support of the boundary character of the prime-side flow is precisely the set of zero
ordinates. This is the prime-side half of the trace-formula duality (Gutzwiller/Selberg reading:
for the conjectural $H$ with spectrum $\{\gamma_\rho\}$, the singularities of
$\mathrm{Tr}\,e^{itH}$ should sit at the "orbit lengths" $\{\pm k\log p\} = \sigma(\mathbb A)$;
here, dually, the singularities of the weighted character of $e^{itA}$ sit at the zeros). §7D
verifies the pole numerically at $-\gamma_1$: approaching to distance $10^{-3}$ multiplies
$\lvert\chi_W\rvert$ to $999.6 \approx 10^3$, the signature of a simple pole with residue of
modulus $1$.

---

## 6. Finite stages: the sieve as the constructive skeleton

The package is not just an existence statement — the sieve of
[prime-sieve.html](../berry-keating/prime-sieve.html) produces it stage by stage.

**Proposition 6.1 (stage-$n$ approximation). — proven**
Let $M_n = 2^{n+1}-1$. After stage $n$ of the composite-generator sieve, the set
$\mathcal Q \cap [2, M_n]$ is known exactly (primes by
[prime-sieve.html](../berry-keating/prime-sieve.html) Lemma 1.2; prime powers as powers of the listed primes). Let
$P_n$ be the orthogonal projection of $\ell^2_\Lambda$ onto
$\mathrm{span}\{\delta_q : q \le M_n\}$ and $A_n = P_n A P_n$, $W_n = P_n W P_n$ (finite rank
$\#(\mathcal Q\cap[2,M_n])$). Then:

1. $A_n \to A$ in the strong resolvent sense, and
   $\sigma(A_n) = \{\log q : q \le M_n\} \cup \{0\}$ exhausts $\sigma(A)$ from below.
2. For $g$ as in Theorem 3.4, the stage-$n$ trace has quantitatively controlled error:

$$
\Big| \mathrm{Tr}\big(W^{1/2} g(A) W^{1/2}\big) - \mathrm{Tr}\big(W_n^{1/2}\, g(A_n)\, W_n^{1/2}\big) \Big|
\;\le\; C \sum_{q > M_n} \Lambda(q)\, q^{-1-\varepsilon}
\;\le\; C\, c\,\frac{1+\varepsilon}{\varepsilon}\, M_n^{-\varepsilon},
$$

with $c$ the Chebyshev constant in $\psi(x) \le c\,x$.

*Proof.* 1. For $\mathrm{Im}\,z \ne 0$ and $x \in \ell^2_\Lambda$,
$(A_n - z)^{-1}x - (A - z)^{-1}x$ is supported on coordinates $q > M_n$ with entries
$\big(\frac{-1}{z} - \frac{1}{\log q - z}\big) x_q$, bounded by
$(\lvert z\rvert^{-1} + \lvert\mathrm{Im}\,z\rvert^{-1})\lvert x_q\rvert$; the tail of $x$
vanishes, giving strong resolvent convergence.
2. The difference of traces is $\sum_{q > M_n} \frac{\Lambda(q)}{\sqrt q}\, g(\log q)$ in
absolute value at most $C\sum_{q>M_n}\Lambda(q) q^{-1-\varepsilon}$. Writing the sum as a
Stieltjes integral against $\psi(t) = \sum_{q \le t}\Lambda(q)$ and integrating by parts:

$$
\int_{M_n}^{\infty} t^{-1-\varepsilon}\, d\psi(t)
= -M_n^{-1-\varepsilon}\psi(M_n) + (1+\varepsilon)\int_{M_n}^{\infty} \psi(t)\, t^{-2-\varepsilon} dt
\;\le\; c\,\frac{1+\varepsilon}{\varepsilon}\, M_n^{-\varepsilon},
$$

using $\psi(t) \le c\,t$ (Chebyshev) and dropping the negative boundary term. $\blacksquare$

**Remark 6.2 (spectral production rate).** By Proposition 1.3 of
[prime-sieve.html](../berry-keating/prime-sieve.html), the dyadic block $I_n$ contributes
$\frac{2^n}{n\log 2}(1 + O(1/n))$ new simple eigenvalues of $A$ in
$[\,n\log 2, (n+1)\log 2\,)$ from $k=1$, plus $O(2^{n/2} n)$ from higher powers. The counting
functions of the two sides of Corollary 4.2 are starkly different — $N_A(T) \sim e^T/T$
(Proposition 3.7) against $N(T) \sim \frac{T}{2\pi}\log\frac{T}{2\pi e}$ — as they must be: in
the explicit formula the two spectra pair through a Fourier transform, not through a bijection.

**Remark 6.3 (what survives normalisation, revisited).** Theorem 3.1 of
[prime-sieve.html](../berry-keating/prime-sieve.html) says the *normalised positions* of the primes flatten to
Lebesgue measure at rate $O_k(1/\log M_n)$ — consistent with constraint (C2): the spectrum's
arithmetic rigidity is invisible to position statistics. What the unnormalised package retains is
multiplicative: the $\mathbb Q$-linear independence of $\{\log p\}$ (unique factorisation:
$\sum_i a_i \log p_i = 0$ with $a_i \in \mathbb Z$ forces $\prod p_i^{a_i} = 1$, so all
$a_i = 0$), which makes the additive group generated by $\sigma(A)$ free abelian on the primes.
That rigidity, together with the $\Lambda$-weights, is exactly what feeds the explicit formula.

---

## 7. Numerical verification

Reference values in 30-digit arithmetic (mpmath 1.4.1); truncated sums over prime powers
$q \le 10^7$ ($664{,}579$ primes, double precision, numpy sieve). All checks verify statements
**proved** above; none is evidence for anything unproven.

### 7A — Kernel identity $K_\Lambda(\lambda,\mu) = -\frac{\zeta'}{\zeta}(1-i(\lambda-\bar\mu))$ (Prop. 2.3)

| $\lambda$ | $\mu$ | $s = 1-i(\lambda-\bar\mu)$ | truncated sum | $-\zeta'/\zeta(s)$ | diff |
|---|---|---|---|---|---|
| $0.3+0.5i$ | $-0.2+0.7i$ | $2.2-0.5i$ | $0.307624995+0.243332091i$ | $0.307624993+0.243332094i$ | $3.1\times10^{-9}$ |
| $1.1+0.3i$ | $1.1+0.3i$ | $1.6$ | $1.185959779$ | $1.186064947$ | $1.1\times10^{-4}$ |

(The larger truncation error at the second point, nearer the abscissa of convergence, is the
slowly convergent Dirichlet tail — same phenomenon and same caveat as
[prime-kernel.html](prime-kernel.html) §6.1; the identity is exact by Proposition 2.3.)

### 7B — Positive semi-definiteness (Prop. 2.3)

At $\lambda \in \{0.2+0.4i,\ -0.5+0.6i,\ 1.3+0.25i,\ 0.8i\}$ (the companion's test points), the
$4\times4$ Gram matrix $G_{ij} = K_\Lambda(\lambda_i, \lambda_j)$ is exactly Hermitian
($\max\lvert G - G^{*}\rvert = 0$) with eigenvalues

$$
\{0.002570,\ 0.092477,\ 0.766271,\ 2.121465\} \quad — \ \text{all positive.}
$$

### 7C — Boundary constant $-\gamma_E$ (Prop. 5.1)

| $\eta$ | $-\zeta'/\zeta(1+\eta) - 1/\eta$ |
|---|---|
| 0.5 | $-0.494765$ |
| 0.1 | $-0.558964$ |
| 0.02 | $-0.573485$ |
| 0.005 | $-0.576279$ |
| 0.001 | $-0.577028$ |
| 0.0001 | $-0.577197$ |

converging to $-\gamma_E = -0.5772156649\ldots$ — the von Mangoldt analogue of the companion's
$c_0$ table (§6.3 there). Continuity across a real boundary point away from the pole (Thm 5.2.1),
at $u = 2$: $R(2 + 0.01i) = -0.420977 - 0.288379i$,
$R(2 + 10^{-4} i) = -0.421790 - 0.289552i$, $R(2) = -0.421798 - 0.289563i$.

### 7D — Flow character and pole catalogue (Thm 5.3)

Identity $\chi_W(z) = -\frac{\zeta'}{\zeta}(\tfrac12 - iz)$:

| $z$ | truncated $\sum_q \Lambda(q) q^{-1/2+iz}$ | closed form | diff |
|---|---|---|---|
| $0.7+1.5i$ | $0.253048486+0.390679918i$ | $0.253048550+0.390679867i$ | $8.2\times10^{-8}$ |
| $-1.2+2i$ | $0.054000841-0.218043774i$ | $0.054000841-0.218043774i$ | $1.6\times10^{-11}$ |

Residues (evaluated as $(z-z_0)\,\chi_W(z)$ at distance $10^{-8}$ from each pole):
at $z = \tfrac{i}{2}$: $1.0000000\,i$ (Thm 5.3 predicts $+i$); at
$z = -\gamma_1 = -14.134725\ldots$: $-1.0000000\,i$ (predicts $-i\,m_{\rho_1} = -i$). Near the
real axis at height $10^{-3}$: $\lvert\chi_W\rvert = 0.229$ at the smooth point
$\mathrm{Re}\,z = 5$, versus $\lvert\chi_W\rvert = 999.6 \approx 10^3$ at
$\mathrm{Re}\,z = -\gamma_1$ — the simple-pole signature of Remark 5.5.

### 7E — Explicit-formula balance (Fact 4.1 / Cor. 4.2), Gaussian test $h(r) = e^{-t r^2}$

With $g(x) = \frac{1}{2\sqrt{\pi t}} e^{-x^2/4t}$, at $t = 0.05$ (zero side needs only
$\gamma_k \le \gamma_7$ at 30-digit precision):

| term | value |
|---|---|
| $h(i/2) + h(-i/2)$ | $+2.025156903$ |
| $-g(0)\log\pi$ | $-1.444152602$ |
| archimedean integral | $-0.465084550$ |
| $-\,\mathrm{Tr}(\mathbb W^{1/2} g(\mathbb A)\mathbb W^{1/2})$ (trace $= +0.115827994$) | $-0.115827994$ |
| **right side total** | $9.17567009714715\times10^{-5}$ |
| **zero side** $\sum_\rho h(\gamma_\rho)$ | $9.17567009714715\times10^{-5}$ |

Discrepancy $2.0\times10^{-31}$; at $t = 0.2$ the two sides are $8.860364360\times10^{-18}$ with
discrepancy $7.3\times10^{-31}$ — four terms of order $1$ cancelling to thirty digits. This pins
every constant in the stated normalisation of Fact 4.1 (the same computation with the
archimedean term doubled misses by $0.465$, ruling out the neighbouring convention).

---

## 8. Summary: the package, and what remains

The prime side of Hilbert–Pólya, assembled unconditionally from the three ingredients of
[prime-kernel.html](prime-kernel.html) under the design constraints of
[prime-sieve.html](../berry-keating/prime-sieve.html):

| component | object | closed form / value | status |
|---|---|---|---|
| space | $\ell^2_\Lambda(\mathcal Q) \cong \mathcal H_\Lambda$ | von Mangoldt Dirichlet series on $\mathbb C^+$ | proven |
| kernel | $K_\Lambda$ | $-\frac{\zeta'}{\zeta}(1-i(\lambda-\bar\mu))$, positive definite | proven |
| flow / generator | $U_t$, $A$ | $\sigma(A) = \{k\log p\}$, simple, pure point | proven |
| weights | $W = w(A)$ | $w(k\log p) = (\log p)p^{-k/2}$, unique (Prop 3.6) | proven |
| trace identity | $\mathrm{Tr}(\mathbb W^{1/2} g(\mathbb A)\mathbb W^{1/2})$ | $= \mathcal W_{\mathrm{ar}}(g)$, arithmetic side of Guinand–Weil | proven |
| boundary | $K_\Lambda - 2\pi S_{H^2}$ | regular at $u=0$, value $-\gamma_E$ | proven |
| character | $\chi_W(z) = \mathrm{Tr}(W e^{izA})$ | $-\frac{\zeta'}{\zeta}(\tfrac12 - iz)$, poles $= i/2$ and shifted zeros | proven |
| RH criterion | poles of $\chi_W$ real $\Leftrightarrow$ depth $\tfrac12$ $\Leftrightarrow$ RH | Cor 5.4 | proven equivalence |
| finite stages | sieve $\Rightarrow$ $A_n \to A$, trace error $\ll_\varepsilon M_n^{-\varepsilon}$ | Prop 6.1 | proven |

**What remains is the zero side, and only the zero side.** The explicit formula now reads

$$
\underbrace{\sum_\rho h(\gamma_\rho)}_{\text{spectrum of a missing operator}}
\;=\; \big[\text{explicit archimedean terms}\big] \;-\; \underbrace{\mathrm{Tr}\big(\mathbb W^{1/2}\, g(\mathbb A)\, \mathbb W^{1/2}\big)}_{\text{constructed, unconditional}} .
$$

The missing object must be a new Hilbert space with a self-adjoint operator whose spectral
measure makes the left side a genuine positive trace; by Proposition 3.7 it is not obtainable by
any re-coordinatisation of the prime side, and by Corollary 5.4 its existence question is
concentrated entirely in a boundary-regularity statement about objects this note has already
constructed: whether the flow character $\chi_W$ — equivalently the kernel $K_\Lambda$ pushed to
depth $\tfrac12$ — meets its unitary boundary with all singularities on the real line. That
statement is equivalent to RH (Weil; Corollary 5.4); nothing in this note decides it.

---

## 9. References

- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math.
  Lund (1952) 252–265.
- A. P. Guinand, *A summation formula in the theory of prime numbers*, Proc. LMS (2) 50 (1948).
- H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, Thm 12.13 (explicit
  formula), Chebyshev bounds.
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, Thm 5.12.
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed. (zero-free region,
  Riemann–von Mangoldt, Hardy's theorem).
- G. H. Hardy, *Sur les zéros de la fonction $\zeta(s)$ de Riemann*, C. R. Acad. Sci. Paris 158
  (1914).
- M. Reed, B. Simon, *Methods of Modern Mathematical Physics I* (Stone's theorem, trace class,
  strong resolvent convergence).
- Companions: [prime-kernel.html](prime-kernel.html) (the three ingredients),
  [prime-sieve.html](../berry-keating/prime-sieve.html) (sieve, equidistribution, no-normalisation estimate).

---

*End — the prime side is constructed, exact, and unconditional: space, kernel, flow, generator,
weights, trace identity, boundary law. The zero side remains what Hilbert–Pólya always was: the
missing half of a duality whose prime half is now on the page.*
