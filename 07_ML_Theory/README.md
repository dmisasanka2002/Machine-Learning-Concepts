# `07_ML_Theory/` - README
**Stage 7 of 12 · Core/Advanced tier · Prerequisites: `05_Model_Evaluation/`, `06_Optimization/`, `00_Mathematics/`**

The "why" behind everything: why models generalize (or don't), why more
data helps, why no algorithm dominates universally, and how much error
is irreducible no matter how good your model gets. This is the folder
that turns "I can fit these algorithms" into "I understand the field
well enough to read a theory paper."

## Files, in reading order
1. `01_hypothesis_spaces_and_erm.ipynb`
2. `02_loss_and_risk.ipynb`
3. `03_bias_variance_tradeoff.ipynb`
4. `04_generalization_and_capacity.ipynb`
5. `05_curse_of_dimensionality.ipynb`
6. `06_vc_dimension_and_pac.ipynb`
7. `07_no_free_lunch.ipynb`
8. `08_bayes_optimal_and_bayes_error.ipynb`
9. `09_concentration_and_uniform_convergence.ipynb`

## What you should be able to do after this folder
Explain, with the actual inequality, why a more flexible model needs more
data to generalize reliably; prove a simple hypothesis class's VC
dimension from scratch (as done for 2D linear classifiers); recognize
"Bayes error," "generalization gap," and "no free lunch" when they appear
in a paper's introduction, with real understanding of what's being
claimed.

## Where this feeds forward
This is the conceptual capstone of the "core" sequence (stages 0-7);
`09_Interpretability/` and `10_Responsible_ML/` build on this folder's
formalization of risk to precisely state what interpretability and
fairness metrics are actually measuring.
