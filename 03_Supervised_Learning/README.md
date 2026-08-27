# `03_Supervised_Learning/` - README
**Stage 3 of 12 · Core tier · Prerequisites: `00_Mathematics/`, `02_Data/`**

Three subfolders, each a coherent arc: Regression (continuous targets),
Classification (categorical targets), Ensemble Learning (combining many
weak models into one strong one - depends on having at least one base
learner, usually Decision Trees, already covered).

## `Regression/` - reading order
`01_linear_regression.ipynb` → `02_linear_regression_from_scratch.ipynb`
→ `03_polynomial_regression.ipynb` → `04_ridge_regression.ipynb` →
`05_lasso_regression.ipynb` → `06_elastic_net.ipynb` →
`07_generalized_linear_models.ipynb` → `08_support_vector_regression.ipynb`
(the last depends on `Classification/13_svm.ipynb`'s margin derivation,
so it's listed last despite living in this folder).

## `Classification/` - reading order
`01_logistic_regression.ipynb` → `02_logistic_regression_from_scratch.ipynb`
→ `03_multinomial_logistic_regression.ipynb` → `04_perceptron.ipynb` →
`05_knn.ipynb` → `06_knn_from_scratch.ipynb` → `07_naive_bayes.ipynb` →
`08_naive_bayes_from_scratch.ipynb` → `09_lda.ipynb` → `10_qda.ipynb` →
`11_decision_trees.ipynb` → `12_decision_trees_from_scratch.ipynb` →
`13_svm.ipynb` → `14_svm_from_scratch.ipynb` → `15_kernel_methods.ipynb`
(placed last since it generalizes SVM's dual - better understood in
hindsight, once you've seen the specific case it generalizes).

## `Ensemble_Learning/` - reading order
`01_bagging.ipynb` → `02_random_forest.ipynb` →
`03_random_forest_from_scratch.ipynb` → `04_extra_trees.ipynb` →
`05_adaboost.ipynb` → `06_gradient_boosting.ipynb` →
`07_xgboost_lightgbm_catboost.ipynb` → `08_voting_and_stacking.ipynb` →
`09_blending.ipynb`. Requires Decision Trees from `Classification/`
first (every ensemble method here uses trees as the base learner).

## What you should be able to do after this folder
Derive the closed-form or iterative training rule for any of these
algorithms from its objective function, by hand, on a small dataset -
and know which one to reach for first given a new problem (cross-check
against `11_Algorithm_Selection_and_Comparison/`).

## Where this feeds forward
`05_Model_Evaluation/` evaluates everything trained here;
`09_Interpretability/` explains what a trained model from here is
actually doing; `11_Algorithm_Selection_and_Comparison/02` and `03`
benchmark these algorithms head-to-head on real data.
