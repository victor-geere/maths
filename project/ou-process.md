# The Ornstein–Uhlenbeck Process — A Phase‑1 Worked Case (the engine behind damping)

*Phase‑1 deliverable (see [README](../README.md)). Where the Fibonacci note builds
a kernel **on the circle** by hand, this note identifies the continuous‑time
process that **performs the damping step itself**. The Ornstein–Uhlenbeck (OU)
generator is a self‑adjoint operator on a Gaussian $L^2$ space whose spectrum is
the integers, its semigroup is exactly geometric damping $r^n$ realised by the
Mehler kernel, and its spectral zeta function is the Riemann zeta function. Every
statement below is classical and unconditional (Hermite polynomials, Mehler's
formula, the Mellin transform of the heat trace). Nothing here bears on RH — the
appearance of $\zeta$ is as a **spectral zeta of an explicitly diagonalised
operator**, not a statement about its zeros.*

---

## 0. Summary

The (stationary, standardised) OU process is the diffusion
$$dX_t=-X_t\,dt+\sqrt2\,dW_t,$$
with stationary law the standard Gaussian
$\gamma(dx)=e^{-x^2/2}\,dx/\sqrt{2\pi}$. Its generator on $H=L^2(\mathbb R,\gamma)$
is
$$L=\partial_x^2-x\,\partial_x.$$

| | statement | mechanism |
|---|---|---|
| **O1** Spectrum | $L$ is essentially self‑adjoint and $\le0$ on polynomials; eigenpairs $(\,-n,\ He_n)$, $n\ge0$, with $He_n$ the probabilists' Hermite polynomials — spectrum $=-\mathbb N$ | Hermite ODE $He_n''-xHe_n'=-nHe_n$ + completeness in $L^2(\gamma)$ |
| **O2** Number operator | $-L=a^{\dagger}a$ with $a=\partial_x$, $a^{\dagger}=x-\partial_x$, $[a,a^{\dagger}]=1$; so $-L$ **is** the number operator, spectrum $\mathbb N$ | ladder relations $aHe_n=nHe_{n-1}$, $a^{\dagger}He_n=He_{n+1}$ |
| **O3** Damping $=$ semigroup | $P_t=e^{tL}$ has $P_tHe_n=e^{-nt}He_n$; setting $r=e^{-t}\in(0,1)$ the eigenvalues are the **geometric damping** $r^n$, with closed‑form **Mehler kernel** | functional calculus + Mehler's formula |
| **O4** Trace / heat | $\operatorname{Tr}P_t=\sum_{n\ge0}e^{-nt}=\frac{1}{1-e^{-t}}=\int_{\mathbb R}M_t(x,x)\,\gamma(dx)$; primed trace $\Theta(t)=\frac{1}{e^{t}-1}=\frac1t-\frac12+\frac{t}{12}-\cdots$ | geometric series $=$ Mehler diagonal integral; Bernoulli expansion |
| **O5** Spectral zeta | the nonzero eigenvalues of $-L$ are $\{1,2,3,\dots\}$, so $\zeta_{-L}(s)=\sum_{n\ge1}n^{-s}=\zeta(s)$ and $\Gamma(s)\zeta(s)=\int_0^\infty t^{s-1}\Theta(t)\,dt$ | Mellin transform of the heat trace; the $\Gamma$ factor is automatic |

The OU process is therefore the **canonical self‑adjoint realisation of the
recipe's damping step**: "damp the $n$‑th mode by $r^n$" is exactly "run the OU
semigroup for time $t=-\log r$."

---

## 1. Setup and the recipe's missing piece

The general recipe ([spectral-triple.html](../victor/spectral-triple.html) §3) starts
by damping a sequence with weights $w_n$ — geometric $w_n=r^n$ is the leading
example. The recipe takes those weights as given. This note supplies the
**dynamics** that produce them: a Markov process whose semigroup applies precisely
the multiplier $n\mapsto r^n$ to the spectral index, with the integers as its
generator's spectrum.

Work on $H=L^2(\mathbb R,\gamma)$, $\gamma(dx)=e^{-x^2/2}\,dx/\sqrt{2\pi}$, with
$\langle f,g\rangle_\gamma=\int_{\mathbb R}f\overline g\,d\gamma$. The OU SDE
$dX_t=-X_t\,dt+\sqrt2\,dW_t$ has $\gamma$ as its unique invariant measure, and its
Markov generator (the drift–diffusion operator) is $L=\partial_x^2-x\,\partial_x$.
The probabilists' Hermite polynomials are
$$He_0=1,\quad He_1=x,\quad He_2=x^2-1,\quad He_3=x^3-3x,\ \dots,\qquad
\langle He_m,He_n\rangle_\gamma=n!\,\delta_{mn}.$$

---

## 2. Self‑adjointness and the integer spectrum

> **Theorem O1 (spectrum).** On the dense domain of polynomials, $L$ is symmetric
> and $\le0$; it is essentially self‑adjoint, and its closure has pure point
> spectrum with eigenpairs $(\,-n,\ He_n)$, $n=0,1,2,\dots$. Thus
> $\operatorname{spec}(L)=\{0,-1,-2,\dots\}=-\mathbb N$.

*Proof.* The Hermite polynomials satisfy the Hermite differential equation
$He_n''-xHe_n'=-nHe_n$, i.e. $LHe_n=-nHe_n$. They are orthogonal and **complete**
in $L^2(\gamma)$ (the Gaussian has exponential moments, so polynomials are dense),
hence an orthogonal basis of eigenvectors. Symmetry of $L$ on polynomials is
integration by parts against $d\gamma$:
$\langle Lf,g\rangle_\gamma=-\int f'g'\,d\gamma=\langle f,Lg\rangle_\gamma$, which
also shows $\langle Lf,f\rangle_\gamma=-\|f'\|_\gamma^2\le0$. A symmetric operator
with a complete orthonormal system of eigenvectors is essentially self‑adjoint and
its closure has exactly that point spectrum. $\;\blacksquare$

This is the cleanest possible instance of the project's organising slogan —
**"the arithmetic sequence *is* the spectrum"** — with the sequence being the
non‑negative integers themselves.

---

## 3. The number operator: $-L=a^{\dagger}a$

> **Theorem O2 (creation/annihilation).** Let $a=\partial_x$ and
> $a^{\dagger}=x-\partial_x$ on $L^2(\gamma)$. Then $a^{\dagger}=a^{*}$,
> $[a,a^{\dagger}]=1$, and
> $$-L=a^{\dagger}a=N,\qquad N\,He_n=n\,He_n.$$
> So $-L$ is the harmonic‑oscillator **number operator**, with spectrum
> $\mathbb N$ and ground state $He_0=1$ ($N\,He_0=0$).

*Proof.* For polynomials, $\langle\partial_xf,g\rangle_\gamma=\int f'g\,e^{-x^2/2}\frac{dx}{\sqrt{2\pi}}
=-\int f\,(g'-xg)\,e^{-x^2/2}\frac{dx}{\sqrt{2\pi}}=\langle f,(x-\partial_x)g\rangle_\gamma$
(integration by parts; the Gaussian kills the boundary term), so
$\partial_x^{*}=x-\partial_x=a^{\dagger}$. The lowering relation
$\partial_xHe_n=nHe_{n-1}$ and the raising relation
$(x-\partial_x)He_n=He_{n+1}$ are the standard Hermite identities; together
$a^{\dagger}aHe_n=(x-\partial_x)(nHe_{n-1})=nHe_n$, i.e. $a^{\dagger}a=-L$. Finally
$[a,a^{\dagger}]=[\partial_x,\,x-\partial_x]=[\partial_x,x]=1$. $\;\blacksquare$

The OU process is thus a probabilist's route to the quantum number operator: the
same operator whose spectrum is $\mathbb N$ appears in the spectral‑triple
manuscript as the bare counting index $n$ of the Fourier modes $e^{in\theta}$.

---

## 4. The semigroup is the damping; the Mehler kernel is its closed form

> **Theorem O3 (semigroup $=$ geometric damping, with Mehler closed form).** For
> $t>0$ and $r=e^{-t}\in(0,1)$, the OU semigroup $P_t=e^{tL}$ acts by
> $P_tHe_n=e^{-nt}He_n=r^nHe_n$, and is the integral operator
> $$(P_tf)(x)=\int_{\mathbb R}M_t(x,y)\,f(y)\,\gamma(dy),\qquad
> M_t(x,y)=\sum_{n\ge0}\frac{r^n}{n!}He_n(x)He_n(y)
> =\frac{1}{\sqrt{1-r^2}}\,\exp\!\left(\frac{2r\,xy-r^2(x^2+y^2)}{2(1-r^2)}\right).$$
> $M_t$ is a positive definite kernel (a probability transition density);
> equivalently $P_t$ is a positive, self‑adjoint, contractive Markov operator with
> spectrum $\{r^n:n\ge0\}$.

*Proof.* $P_t=e^{tL}$ acts on the eigenbasis by $e^{-nt}$ (functional calculus),
giving the diagonal action and spectrum $\{r^n\}$, with $r^n\ge0$ — hence positive
semidefinite and (being a Markov semigroup) contractive. The kernel reproducing
this action against $\gamma$ is the bilinear generating series
$\sum_n\frac{r^n}{n!}He_n(x)He_n(y)$ because $\{He_n/\sqrt{n!}\}$ is orthonormal;
**Mehler's formula** sums it to the displayed Gaussian, valid for $|r|<1$.
Positive definiteness is immediate from $\langle f,P_tf\rangle_\gamma=\sum_n r^n|\hat f_n|^2\ge0$.
$\;\blacksquare$

**The bridge to the circle recipe.** Under the project's identification of the
spectral index $n$ with the Fourier mode $e^{in\theta}$, the operator
$\operatorname{diag}(r^{|n|})$ that the recipe applies on $\mathbb T$ is exactly
$P_t$ restricted to that index (folded to $|n|$ by the even symmetrisation). The
Mehler kernel is the real‑line analogue of the Fibonacci/zeta circle kernels:
where Fibonacci sums $\sum F_nr^n\cos n\theta$ to a **rational** closed form via
its generating function, OU sums $\sum\frac{r^n}{n!}He_n(x)He_n(y)$ to a
**Gaussian** closed form via Mehler's. Geometric damping is not an ad‑hoc choice —
it is the unique multiplier coming from a Markov semigroup, which is *why* it
preserves positivity (Bochner on the circle ↔ Markov positivity here).

---

## 5. Trace, heat expansion, and the spectral zeta function

> **Theorem O4 (trace / heat kernel).** For $t>0$,
> $$\operatorname{Tr}P_t=\sum_{n\ge0}e^{-nt}=\frac{1}{1-e^{-t}}
> =\int_{\mathbb R}M_t(x,x)\,\gamma(dx),$$
> and the **primed** heat trace (dropping the zero mode) is
> $$\Theta(t):=\operatorname{Tr}'e^{tL}=\sum_{n\ge1}e^{-nt}=\frac{1}{e^{t}-1}
> =\frac1t-\frac12+\frac{t}{12}-\frac{t^{3}}{720}+\cdots
> =\sum_{k\ge0}\frac{B_k}{k!}\,t^{\,k-1},$$
> the generating function of the Bernoulli numbers $B_k$.

*Proof.* The eigenvalue sum is a geometric series. For the integral form, set
$r=e^{-t}$; the Mehler diagonal is
$M_t(x,x)=\frac{1}{\sqrt{1-r^2}}\exp\!\big(\frac{r}{1+r}x^2\big)$, and
$$\int_{\mathbb R}M_t(x,x)\,\frac{e^{-x^2/2}}{\sqrt{2\pi}}\,dx
=\frac{1}{\sqrt{1-r^2}}\sqrt{\frac{1+r}{1-r}}=\frac{1}{1-r}=\frac{1}{1-e^{-t}},$$
the Gaussian integral converging because $\frac{r}{1+r}-\frac12=-\frac{1-r}{2(1+r)}<0$.
The Bernoulli expansion is the definition $\frac{t}{e^{t}-1}=\sum_k\frac{B_k}{k!}t^k$.
$\;\blacksquare$

> **Theorem O5 (the spectral zeta of $-L$ is $\zeta$).** The spectral zeta function
> of the OU generator, formed from its nonzero eigenvalues $\{1,2,3,\dots\}$, is the
> Riemann zeta function:
> $$\zeta_{-L}(s)=\sum_{n\ge1}n^{-s}=\zeta(s),\qquad\Re s>1,$$
> and it is the Mellin transform of the heat trace,
> $$\Gamma(s)\,\zeta(s)=\int_0^\infty t^{s-1}\,\Theta(t)\,dt .$$
> Its analytic continuation has the special values
> $\zeta(0)=-\tfrac12$, $\zeta(-1)=-\tfrac1{12}$, $\zeta(-2k)=0$, read off the
> Bernoulli coefficients of $\Theta$ via $\zeta(-k)=-\dfrac{B_{k+1}}{k+1}$.

*Proof.* The nonzero spectrum of $-L$ is exactly the positive integers, each
simple (Theorem O1), so $\zeta_{-L}(s)=\sum_{n\ge1}n^{-s}=\zeta(s)$. For
$\Re s>1$, $\int_0^\infty t^{s-1}e^{-nt}\,dt=\Gamma(s)n^{-s}$; summing over $n\ge1$
and exchanging (absolute convergence) gives
$\int_0^\infty t^{s-1}\Theta(t)\,dt=\Gamma(s)\zeta(s)$. The continuation and the
negative‑integer values are the standard heat‑kernel/Mellin argument: the
small‑$t$ asymptotics of $\Theta$ have coefficients $B_k/k!$, and the
meromorphic structure of $\int_0^1 t^{s-1}\Theta\,dt$ produces the residues/values
$\zeta(-k)=-B_{k+1}/(k+1)$. $\;\blacksquare$

This is the OU instance of **Methodology pillar 4** (explicit formulas with an
archimedean Gamma correction): the identity $\Gamma(s)\zeta(s)=\int_0^\infty
t^{s-1}\operatorname{Tr}'e^{tL}\,dt$ has a spectral side (sum over the integer
spectrum) and an analytic side, with the **Gamma factor appearing automatically**
as the Mellin kernel — the same archimedean factor that decorates the completed
$\zeta$. It is a genuine, fully rigorous trace identity, modest but exact.

---

## 6. The semigroup as a transfer operator (where OU sits in the plan)

The OU semigroup $\{P_t\}_{t\ge0}$ is a bona‑fide **transfer operator** in the
sense of **Methodology pillar 3**: it is the self‑adjoint Markov (Koopman/transfer)
operator of the OU dynamics, with the composition law $P_sP_t=P_{s+t}$ realising
transfer‑operator composition and the generator $L$ as its infinitesimal form.
Unlike the η↔ζ rotation ([eta-zeta-transfer.md](eta-zeta-transfer.md)), which need
not preserve positivity, the OU transfer is **positivity‑preserving by
construction** — it is the benign baseline against which the indefinite cases are
measured.

Two forward links:

- **To Phase 5 (helix / time).** The damping parameter here is genuine *time*
  $t=-\log r$ flowing along a one‑parameter self‑adjoint semigroup. That is exactly
  the "added time axis" the helix proposal
  ([helix-quaternion-proposal.md](helix-quaternion-proposal.md)) wants to make
  geometric: sweeping $t$ stacks the spectra into a sheet, and $-L$ is the
  candidate self‑adjoint generator of that time before any quaternionic lift.
- **To Phase 4 (generalisation).** OU is the continuous‑time, Gaussian‑measure
  prototype of "sequence → self‑adjoint operator → spectrum → transfer operator →
  explicit formula" with **every arrow unconditional**, including a spectral zeta
  that is literally $\zeta$. It fixes the template the harder Dirichlet‑series
  objects are asked to imitate.

---

## 7. Numerical verification (to fill in)

Target checks for a small script (extends [prime-zeros.py](../victor/prime-zeros.py)):

| quantity | formula | check |
|---|---|---|
| eigenvalues of $P_t$ | $e^{-nt}$ | vs. eigenvalues of a discretised $L=\partial_x^2-x\partial_x$ on a Hermite grid |
| Mehler closed form | $M_t(x,y)=\frac{1}{\sqrt{1-r^2}}e^{(2rxy-r^2(x^2+y^2))/2(1-r^2)}$ | vs. truncated $\sum_{n\le N}\frac{r^n}{n!}He_n(x)He_n(y)$ |
| trace | $\frac{1}{1-e^{-t}}$ | vs. $\sum_n e^{-nt}$ and vs. $\int M_t(x,x)\,d\gamma$ (quadrature) |
| heat expansion | $\frac1t-\frac12+\frac{t}{12}-\cdots$ | small‑$t$ fit of $\Theta(t)=1/(e^t-1)$, recover $B_k$ |
| spectral zeta | $\Gamma(s)\zeta(s)=\int_0^\infty t^{s-1}\Theta\,dt$ | numerical Mellin vs. `mpmath.zeta`; check $\zeta(0)=-\tfrac12$, $\zeta(-1)=-\tfrac1{12}$ |

---

## 8. Scope and honest limits

- **Proven / unconditional.** O1–O5 are classical: the Hermite spectral
  decomposition, Mehler's formula, the geometric trace, and the Mellin transform
  $\Gamma(s)\zeta(s)=\int t^{s-1}/(e^t-1)\,dt$. The OU generator is an explicitly
  diagonalised self‑adjoint operator with spectrum $\mathbb N$.
- **No RH content.** $\zeta$ appears here as a **spectral zeta function** of a
  fully understood operator — a statement about the eigenvalues $1,2,3,\dots$, not
  about the nontrivial zeros. The integers $\mathbb N$ are not the zeta zeros, and
  nothing in this note moves toward a Hilbert–Pólya operator. (See the
  prime‑sine‑wave §7 warning: a clean appearance of $\zeta$ is not a criterion.)
- **What it contributes.** It grounds the recipe's damping step in genuine
  dynamics, gives the cleanest "sequence = spectrum" example (the integers), a
  positivity‑preserving transfer operator, and the model trace identity with an
  automatic Gamma factor — the rigorous baseline for Phases 4–5.
- **Open / not claimed here.** A precise functor from the OU semigroup on
  $L^2(\gamma)$ to the circle operators on $L^2(\mathbb T)$ (beyond the index‑level
  matching of §4), and the quaternionic time lift of §6, are deferred to Phases 4
  and 5.
- **Standard results used.** Hermite ODE, orthogonality and completeness in
  $L^2(\gamma)$; Mehler's bilinear generating formula; the OU semigroup / generator
  correspondence; the Mellin representation $\Gamma(s)\zeta(s)=\int_0^\infty
  t^{s-1}(e^t-1)^{-1}\,dt$ and $\zeta(-k)=-B_{k+1}/(k+1)$.
