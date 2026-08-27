# `00_Mathematics/` - README
**Stage 0 of 12 · Foundation tier · No prerequisites**

The mathematical toolkit every later section draws on. Nothing in this
folder is ML-specific - it's the shared language (vectors, derivatives,
probability, statistics) that lets later derivations move fast without
re-explaining notation every time.

## Files, in reading order
1. `01_linear_algebra.ipynb` - vectors, matrices, norms, eigenvalues/
   eigenvectors, projections
2. `02_calculus_and_matrix_calculus.ipynb` - gradients, Jacobians,
   Hessians, chain rule
3. `03_probability.ipynb` - Bayes' theorem, distributions, expectation
4. `04_statistics.ipynb` - MLE/MAP, CLT
5. `05_information_theory.ipynb`

## What you should be able to do after this folder
Read $\nabla f$, $\nabla^2 f$, $P(A\mid B)$, $E[X]$, $\text{Var}(X)$
without translating in your head; recognize an eigenvalue equation when
one appears (it will, repeatedly - PCA, spectral properties of Ridge's
$X^TX+\lambda I$).

## Where this feeds forward
Every derivation in `03_Supervised_Learning/` and `04_Unsupervised_Learning/`
cites back here rather than re-deriving matrix calculus or Bayes' rule from
scratch. If a later notebook's math looks unfamiliar, the gap is probably
here, not there.
