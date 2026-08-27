# `06_Optimization/` - README
**Stage 6 of 12 · Core tier · Prerequisites: `00_Mathematics/02_calculus_and_matrix_calculus.ipynb`**

The engine behind every algorithm in `03_Supervised_Learning/` that
doesn't have a closed form (Logistic Regression, SVM's dual, and - via
the shared derivation - everything in the DL repo). Deliberately placed
*after* Supervised/Unsupervised Learning rather than before: you've
already seen gradient descent used informally (Linear Regression's GD
path in `08-Linear-Regression-Additions.md`, Logistic Regression's
2-iteration trace) - this folder now derives the machinery properly and
generalizes it.

## Files, in reading order
1. `01_objective_functions.ipynb`
2. `02_convexity.ipynb`
3. `03_gradient_descent.ipynb`
4. `04_sgd_and_minibatch.ipynb`
5. `05_momentum_and_adaptive_methods.ipynb`
6. `06_optimization_diagnostics.ipynb`
7. `07_hyperparameter_optimization.ipynb`
8. `08_lagrange_duality_and_kkt.ipynb`

## What you should be able to do after this folder
Derive the gradient-descent update rule for a new loss function you
haven't seen before, explain why Adam's bias-correction terms exist,
and diagnose a bad training run from its loss curve shape alone.

## Where this feeds forward
`03_Supervised_Learning/Classification/01_logistic_regression.ipynb` and
`13_svm.ipynb`, revisited: their gradient derivations are special cases
of what's derived generally here. `07_ML_Theory/02_convexity.ipynb`'s
convexity proofs for specific algorithms lean on this folder's general
convexity definition.
