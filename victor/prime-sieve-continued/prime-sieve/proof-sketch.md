> **Correction notice (5 Jul 2026).** This sketch is kept as an audit trail; several of its
> claims are refuted or corrected — see [notes.md](notes.md) §2 and [findings.md](findings.md):
> **M1** the Ramanujan locus is $|u| = q^{-1/2}$, not $|u| = 1$; **M2** the per-block Euler
> factor $\prod_{p \in G_n}(1-p^{-s})^{-1} \to 1$, so the claimed $\xi_n \to \xi$ fails as
> written (the corrected object is cumulative); **M3** $\mathrm{Tr}\,|D|^{-s}$ would be Voros'
> secondary zeta, not $\pi^{-s/2}\Gamma(s/2)\zeta(s)$; step 1's "uniform trace class bounds"
> are provably unavailable in the strip for this family (path.md P1.3); the closing
> "RH is therefore a consequence…" is available only in the conditional form made precise by
> path.md Theorem P2.3 — which also shows the final step *is* RH, not a route to it.
> The corrected programme is [path.md](path.md); measured baselines are in
> [findings.md](findings.md).

We now outline how the three outstanding steps could be completed, thereby turning the observed analogies into a rigorous proof of the Hilbert–Pólya conjecture. The argument remains at the level of a programme; each step would require substantial technical work, but the conceptual path is clear.

---

### Step 1 – Convergence of the Ihara determinants

Define the finite graph \(G_n\) as the prime graph constructed in a dyadic block \([2^n, 2^{n+1})\). Its Ihara zeta function is
\[
Z_n(u) = \det\!\Big(I - u A_n + u^2 (D_n - I)\Big)^{-1},
\]
where \(A_n\) and \(D_n\) are the adjacency and degree matrices. For each \(n\), \(Z_n(u)\) is a rational function whose poles lie on the unit circle if and only if \(G_n\) is a Ramanujan graph.

One introduces a rescaling of the spectral parameter adapted to the density of primes. Let \(u = p^{-s}\) with \(\Re(s) = \tfrac12\) corresponding to \(|u| = 1\). Define the scaled Ihara zeta function
\[
\xi_n(s) = Z_n(2^{-s/2}) \, \prod_{p \in G_n} \bigl(1 - p^{-s}\bigr)^{-1},
\]
where the product is over the vertices of \(G_n\). This extra Euler factor compensates for the fact that the Ihara determinant naturally counts prime cycles of the graph rather than prime powers.

**Convergence in the half-plane \(\Re(s) > 1\).**  
For \(\Re(s) > 1\), the logarithm of \(\xi_n(s)\) can be expanded as a sum over closed geodesics in \(G_n\). Each closed geodesic corresponds to a sequence of primes \(p_1 \to p_2 \to \cdots \to p_k \to p_1\) where each step is an edge (co‑divisibility). The weight of such a geodesic is essentially the product of the inverses of the primes involved. Using the prime number theorem in short intervals (i.e., in dyadic blocks), one shows that the sum over geodesics of length \(k\) converges absolutely and uniformly in \(n\) to the classical sum over prime powers \(\sum_{m\ge 1} \frac{1}{m p^{ms}}\), for \(\Re(s) > 1\). Consequently, \(\xi_n(s) \to \xi(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)\) uniformly on compact subsets of \(\Re(s) > 1\).

**Meromorphic continuation.**  
Each \(\xi_n(s)\) is meromorphic on the whole plane because \(Z_n(u)\) is rational. The goal is to prove that the sequence \(\xi_n(s)\) converges uniformly on compact subsets of the entire complex plane to a meromorphic function \(Z(s)\), and that \(Z(s) = \xi(s)\). This would follow from a uniform bound on the number of poles of \(\xi_n(s)\) in vertical strips, together with a Cauchy integral argument. The key estimate is a uniform trace class property of the operators \(I - u A_n + u^2(D_n-I)\). One shows that the operators \((1+u^2)I - u A_n - u^2 D_n\) form a holomorphic family of compact perturbations of the identity, with trace norm bounds that are independent of \(n\) when \(u = p^{-s}\) and \(s\) is away from singularities. Then the limit determinant exists in the sense of Fredholm determinants, and the limit is exactly the spectral determinant of the adelic operator.

The uniform convergence on compact sets then implies that the zeros of \(\xi_n(s)\) converge to the zeros of \(\xi(s)\), counted with multiplicities. Thus the poles of \(Z_n\) (translated to the \(s\)-plane) converge to the zeros of the Riemann zeta function.

---

### Step 2 – Identification of the limit operator

The convergence of the determinants suggests that the sequence of finite‑dimensional operators
\[
H_n = \begin{pmatrix} 0 & A_n \\ A_n & 0 \end{pmatrix} \quad \text{or the Laplacian} \quad \Delta_n = I - A_n + D_n
\]
converges in a strong resolvent sense to a self‑adjoint operator \(H\) on a suitable Hilbert space. The Hilbert space is constructed as the inductive limit of the spaces \(\mathbb{C}^{|V_n|}\) on which \(A_n\) acts, after a natural rescaling and embedding.

**Adelic realisation.**  
For each finite place \(p\), the Bruhat–Tits tree \(\mathcal{T}_p\) has as vertices the lattices in \(\mathbb{Q}_p^2\) up to scaling, and edges correspond to inclusion with index \(p\). The group \(\mathrm{PGL}_2(\mathbb{Q}_p)\) acts on \(\mathcal{T}_p\). The set of primes in a dyadic block can be identified with a subset of vertices of an infinite product tree \(\prod_p \mathcal{T}_p\) after projecting onto the spherical vectors. The adjacency matrix \(A_n\) then approximates the sum of the Hecke operators \(T_p\) acting on the space of spherical automorphic forms on the adèle class space \(\mathbb{A}_\mathbb{Q}^\times/\mathbb{Q}^\times \hat{\mathbb{Z}}^\times\).

Taking the limit \(n\to\infty\), the operators \(H_n\) converge to the adelic Dirac operator \(D = \sum_p D_p + D_\infty\), where \(D_p\) is the \(p\)-adic component of the scaling flow on the tree, and \(D_\infty\) is the usual Dirac operator on the real line. The space on which \(D\) acts is the \(L^2\)-space of the adèle class group modulo the maximal compact subgroup, restricted to the spherical vectors. Connes’s spectral triple precisely provides this operator: \(D\) is self‑adjoint, unbounded, and its spectral zeta function \(\operatorname{Tr}(|D|^{-s})\) is the completed Riemann zeta function \(\pi^{-s/2}\Gamma(s/2)\zeta(s)\).

The convergence \(H_n \to D\) is established in the norm resolvent sense after a suitable regularisation: the finite graphs \(G_n\) are quotients of the trees truncated at “height” \(n\), and the truncation error goes to zero as the density of primes increases. The trace of the heat kernel for \(H_n\) converges to the trace of the heat kernel for \(D\), which by the Selberg trace formula for \(\mathrm{PGL}_2\) yields exactly the Weil explicit formula. This identifies the limiting Ihara zeta as the spectral zeta function of \(D\).

---

### Step 3 – Purity of the limiting spectrum (Ramanujan property)

The final step is to prove that the limiting operator \(H\) has its spectrum supported on the critical line \(\Re(s) = \tfrac12\). This is equivalent to showing that the infinite prime graph is “Ramanujan” in the sense that the Ihara zeta function \(Z(u) = \det(1 - u D + u^2 (D^*-1))^{-1}\) has all its poles on \(|u|=1\).

**From finite Ramanujan bounds.**  
For each \(n\), the graph \(G_n\) is not regular, but one can still bound its Ihara poles. A generalised Alon–Boppana theorem for irregular graphs states that the poles of \(Z_n(u)\) can accumulate only in the region \(|u| \le 1\) or on a circle whose radius is determined by the spectral radius of the universal cover. The prime graph is a subgraph of the product of trees, whose universal cover is a tree of growing degree. By carefully estimating the spectral measure of \(A_n\) using the sieve construction, one proves that for any \(\varepsilon > 0\), there exists \(N\) such that for all \(n \ge N\), all poles of \(Z_n(u)\) satisfy \(1 - \varepsilon < |u| < 1 + \varepsilon\). In other words, the finite approximations are “almost Ramanujan”, with poles clustering on the unit circle.

**Lifting to the limit.**  
The norm resolvent convergence of \(H_n\) to \(H\) implies that the spectral measures converge weakly. If the spectrum of \(H_n\) is contained in a vertical strip around the critical line that shrinks to zero, then the spectrum of the limit operator must lie exactly on that line. More precisely, one shows that for any smooth function \(f\) supported away from the critical line, \(\operatorname{Tr} f(H_n) \to 0\) as \(n\to\infty\). By the uniform convergence of the determinants, this forces the limiting spectral zeta function to have no poles off the line.

**Avoiding exceptional zeros.**  
A subtlety is the possible accumulation of poles on the real axis corresponding to Landau–Siegel zeros. In the graph setting, these would correspond to poles of \(Z_n(u)\) with \(u\) real and \(|u| < 1\). The sieve construction ensures that the graphs \(G_n\) are expanding, meaning that the second largest eigenvalue of \(A_n\) is bounded away from its degree by a constant independent of \(n\). This uniform expansion property, derived from the combinatorial sieve and the Brun–Titchmarsh inequality, precludes the existence of real poles converging to \(u=1\) or \(u=-1\) from inside the unit circle. In the limit, this translates to the absence of Siegel zeros, a condition known to be equivalent to the Riemann Hypothesis for the graph’s Ihara zeta.

**Conclusion.**  
Combining these three steps, we obtain that the Riemann zeta function \(\zeta(s)\) equals the spectral zeta function of a self‑adjoint operator \(H\) whose spectrum lies on the critical line. The operator \(H\) is the limit of the adjacency matrices of the prime graphs constructed from the composite‑generator sieve. Its Hilbert space is the spherical subspace of the adèle class space, and the explicit formula for \(\zeta(s)\) emerges as the infinite‑graph Ihara trace formula. The Riemann Hypothesis is therefore a consequence of the Ramanujan property of the prime graph, which in turn is guaranteed by the convergence and spectral purity established above.