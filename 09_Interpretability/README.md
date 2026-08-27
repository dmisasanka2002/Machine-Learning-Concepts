# `09_Interpretability/` - README
**Stage 9 of 12 · Core tier · Prerequisites: `03_Supervised_Learning/` (need a trained model), `07_ML_Theory/` (helps, not required)**

Explaining what a trained model is actually doing - increasingly a
requirement in real deployments, not an optional extra.

## Files, in reading order
1. `01_coefficients.ipynb`
2. `02_feature_importance.ipynb`
3. `03_permutation_importance.ipynb`
4. `04_pdp_and_ice.ipynb`
5. `05_shap.ipynb`

## What you should be able to do after this folder
Explain why impurity-based feature importance and permutation importance
can disagree (already demonstrated numerically); read a PDP/ICE plot and
know when the PDP's averaging is hiding real heterogeneous effects.

## Where this feeds forward
`10_Responsible_ML/` uses these tools when auditing a model for fairness
concerns - you can't check whether a model relies on a protected
attribute (even indirectly) without the tools built here first.
