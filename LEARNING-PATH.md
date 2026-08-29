# Learning Path - Beginner → Intermediate → Advanced
The 12-stage folder structure (`00_Mathematics/` → `12_Projects/`) defines
*dependency* order. This document defines *difficulty* order - the same
files, read up to **three separate times**, each pass going deeper. This
works because every algorithm notebook in this repo bundles intuition,
full derivation, and practical code in one file
(`44-NOTEBOOK-TEMPLATE-V2.md`'s 12-section template) - so "beginner" means
*which sections* of a file to read, not a different, easier file.

**Rule of thumb**: Beginner = §1 (Theory) + §4 (Visual) + §6 (sklearn) of
each file - get it working and build intuition. Intermediate = add §2
(Derivation), §3 (Numerical Example), §5 (From-Scratch) - understand *why*
it works. Advanced = add §7-§12 (Experiment, Failure Cases, Assumptions,
Complexity, Exercises, Research Notes) - know its limits and its place in
the literature. Files that are wholly new at one level (e.g. everything
in `07_ML_Theory/`) are marked accordingly rather than split by section.

An interactive version of this checklist: `learning-path-interface.html`
(open directly in a browser, no install needed).

---

## LEVEL 1 - BEGINNER
**Goal**: get oriented, run every core algorithm once, build correct
intuition. Skip derivations entirely on this pass - re-deriving before
you've seen an algorithm *work* is demotivating and unnecessary.

### Stage 0 - Math (just enough to read later formulas)
- [ ] `00_Mathematics/01_linear_algebra.ipynb` - §1-4 only (vectors, dot
  product, matrices, inverse) - skip eigenvalues/SVD for now
- [ ] `00_Mathematics/03_probability.ipynb` - §1-3 only (Bayes' theorem,
  distributions)

### Stage 1 - Foundations (all of it - none of this is hard, all of it matters)
- [ ] `01_Foundations/01_what_is_ml.ipynb`
- [ ] `01_Foundations/02_ml_terminology.ipynb`
- [ ] `01_Foundations/03_learning_paradigms.ipynb`
- [ ] `01_Foundations/04_ml_workflow.ipynb`
- [ ] `01_Foundations/05_problem_formulation.ipynb`

### Stage 2 - Data (all of it - practical, not mathematical)
- [ ] `02_Data/01_data_types.ipynb`
- [ ] `02_Data/02_sampling.ipynb`
- [ ] `02_Data/03_cleaning_and_missing_values.ipynb`
- [ ] `02_Data/04_outliers.ipynb`
- [ ] `02_Data/05_encoding.ipynb`
- [ ] `02_Data/06_scaling.ipynb`
- [ ] `02_Data/07_data_leakage.ipynb` - read in full, this one's important
      even at Beginner level
- [ ] `02_Data/08_feature_engineering.ipynb`
- [ ] `02_Data/09_feature_selection.ipynb`

### Stage 3 - Your first 7 algorithms (§1 Theory + §6 sklearn ONLY)
- [ ] `03_Supervised_Learning/Regression/01_linear_regression.ipynb`
- [ ] `03_Supervised_Learning/Classification/01_logistic_regression.ipynb`
- [ ] `03_Supervised_Learning/Classification/05_knn.ipynb`
- [ ] `03_Supervised_Learning/Classification/11_decision_trees.ipynb`
- [ ] `03_Supervised_Learning/Classification/07_naive_bayes.ipynb`
- [ ] `04_Unsupervised_Learning/01_kmeans.ipynb`
- [ ] `04_Unsupervised_Learning/10_pca.ipynb`

### Stage 4 - Basic evaluation (know if your model is any good)
- [ ] `05_Model_Evaluation/01_regression_metrics.ipynb`
- [ ] `05_Model_Evaluation/02_classification_metrics.ipynb`

### Stage 5 - Orientation
- [ ] `11_Algorithm_Selection_and_Comparison/01_how_to_choose_an_algorithm.ipynb`
      - the flowchart, as a map of everything you'll deepen next

### Beginner capstone
- [ ] `12_Projects/02_classification_project_social_ads.ipynb` - sklearn
      only, no derivations needed, just the full pipeline once end-to-end

**You're done with Beginner when**: you can fit and evaluate any of the 7
algorithms above on a new dataset from `datasets/` without looking
anything up, and can state in one sentence what each one is doing.

---

## LEVEL 2 - INTERMEDIATE
**Goal**: understand *why* every algorithm works - full derivations, hand-
verified numeric examples, from-scratch implementations. This is the bulk
of the repo and the bulk of the work. Re-read every Stage-3 file from
Beginner in full this time, then continue into everything else.

### Stage 0 - Math, completed
- [ ] `00_Mathematics/01_linear_algebra.ipynb` - full (eigenvalues, SVD,
      pseudoinverse)
- [ ] `00_Mathematics/02_calculus_and_matrix_calculus.ipynb`
- [ ] `00_Mathematics/03_probability.ipynb` - full
- [ ] `00_Mathematics/04_statistics.ipynb`

### Stage 2 - Data, completed
- [ ] `02_Data/10_imbalanced_data_handling.ipynb`

### Stage 3 - Supervised Learning, full depth
**Regression**: `01_linear_regression` (full - Normal Equation, Gauss-
Markov, SVD, gradient descent) → `02_linear_regression_from_scratch` →
`03_polynomial_regression` → `04_ridge_regression` → `05_lasso_regression`
→ `06_elastic_net` → `07_generalized_linear_models`
**Classification**: `01_logistic_regression` (full) →
`02_logistic_regression_from_scratch` → `03_multinomial_logistic_regression`
→ `04_perceptron` → `05_knn` (full) → `06_knn_from_scratch` →
`07_naive_bayes` (full) → `08_naive_bayes_from_scratch` → `09_lda` →
`10_qda` → `11_decision_trees` (full) → `12_decision_trees_from_scratch`
→ `13_svm` (primal + margin only - save the dual/KKT derivation for
Advanced) → `14_svm_from_scratch`
**Ensemble Learning**: `01_bagging` → `02_random_forest` (full) →
`03_random_forest_from_scratch` → `04_extra_trees` → `05_adaboost` →
`06_gradient_boosting` → `07_xgboost_lightgbm_catboost` →
`08_voting_and_stacking` → `09_blending`

### Stage 4 - Unsupervised Learning, full depth
`01_kmeans` (full) → `02_kmeans_from_scratch` → `03_kmedoids` →
`04_hierarchical` → `05_hierarchical_from_scratch` → `06_dbscan` →
`07_optics` → `08_gmm_and_em` (E-step/M-step derivation) → `09_kde` →
`10_pca` (full - Lagrange derivation, eigen-decomposition) →
`11_pca_from_scratch` → `12_kernel_pca` → `13_ica` → `14_nmf` →
`15_tsne_umap` → `16_anomaly_detection` → `17_generative_vs_discriminative`

### Stage 5 - Model Evaluation, completed
- [ ] `05_Model_Evaluation/03_ranking_metrics.ipynb`
- [ ] `04_calibration.ipynb`
- [ ] `05_cross_validation.ipynb`
- [ ] `06_learning_curves.ipynb`
- [ ] `07_validation_strategies.ipynb`

### Stage 6 - Optimization
- [ ] `06_Optimization/01_objective_functions.ipynb`
- [ ] `02_convexity.ipynb`
- [ ] `03_gradient_descent.ipynb`
- [ ] `04_sgd_and_minibatch.ipynb`
- [ ] `05_momentum_and_adaptive_methods.ipynb`
- [ ] `06_optimization_diagnostics.ipynb`
- [ ] `07_hyperparameter_optimization.ipynb`

### Stage 9 - Interpretability
- [ ] `09_Interpretability/01_coefficients.ipynb` through `05_shap.ipynb`
      (all 5)

### Stage 10 - Responsible ML
- [ ] `10_Responsible_ML/01_bias_in_ml.ipynb` through
      `04_reproducibility.ipynb` (all 4)

### Stage 11 - Comparison, completed
- [ ] `11_Algorithm_Selection_and_Comparison/02_compare_regression_algorithms.ipynb`
      through `06_complexity_cheatsheet.ipynb` (5 remaining files)

### Intermediate capstones
- [ ] `12_Projects/01_regression_project_insurance_cost.ipynb`
- [ ] `12_Projects/03_clustering_project_customer_segmentation.ipynb`
- [ ] `12_Projects/05_dimensionality_reduction_project_iris.ipynb`

**You're done with Intermediate when**: you can derive any algorithm's
training rule from its objective function on a blank sheet of paper, and
your hand-worked numeric example matches your code's output - the
standard every file in this repo was itself held to.

---

## LEVEL 3 - ADVANCED
**Goal**: the mathematical machinery and theory that make published ML
research legible - not more algorithms, but the tools underneath them.

### Stage 3 - the derivation you deferred
- [ ] `03_Supervised_Learning/Classification/13_svm.ipynb` - now the full
      Lagrangian dual + KKT derivation
- [ ] `15_kernel_methods.ipynb` - full, including the RKHS note

### Stage 6 - generalized optimization theory
- [ ] `06_Optimization/07_lagrange_duality_and_kkt.ipynb` - the general
      recipe SVM was a special case of

### Stage 7 - ML Theory (all of it - this entire folder is Advanced tier)
- [ ] `07_ML_Theory/01_hypothesis_spaces_and_erm.ipynb`
- [ ] `02_loss_and_risk.ipynb`
- [ ] `03_bias_variance_tradeoff.ipynb`
- [ ] `04_generalization_and_capacity.ipynb`
- [ ] `05_curse_of_dimensionality.ipynb`
- [ ] `06_vc_dimension_and_pac.ipynb`
- [ ] `07_no_free_lunch.ipynb`
- [ ] `08_bayes_optimal_and_bayes_error.ipynb`
- [ ] `09_concentration_and_uniform_convergence.ipynb`

### Stage 0 - the math that supports Stage 7 and beyond
- [ ] `00_Mathematics/05_information_theory.ipynb`
- [ ] `00_Mathematics/06_bayesian_inference.ipynb`

### Stage 5 - rigorous comparison
- [ ] `05_Model_Evaluation/08_statistical_model_comparison.ipynb`
      (McNemar's test, multiple-comparisons correction)
- [ ] Conformal Prediction append to `04_calibration.ipynb`

### Stage 8 - Classical Reinforcement Learning (all of it)
- [ ] `08_Classical_Reinforcement_Learning/01_mdp_and_bellman_equations.ipynb`
- [ ] `02_dynamic_programming.ipynb`
- [ ] `03_monte_carlo_methods.ipynb`
- [ ] `04_temporal_difference_learning.ipynb`
- [ ] `05_q_learning.ipynb`

### Beyond this repo - awareness, not mastery
- [ ] `99_Advanced_Topics_Pointers/01_gaussian_processes.ipynb` through
      `06_distribution_shift.ipynb` (all 6, short reads)

### Advanced capstone
- [ ] `12_Projects/04_anomaly_detection_project_cardio.ipynb` - the one
      project requiring imbalanced-data handling AND anomaly detection
      together, plus a written justification citing `07_ML_Theory/`
      concepts (bias-variance, Bayes error) for every modeling choice made

**You're done with Advanced when**: you can read an ML theory paper's
introduction and abstract and follow the argument - recognize "empirical
risk," "generalization bound," "VC dimension," "KL divergence," and
"Lagrangian dual" as tools you've derived yourself, not jargon.
