# `05_Model_Evaluation/` - README
**Stage 5 of 12 · Core tier · Prerequisites: `03_Supervised_Learning/` or `04_Unsupervised_Learning/` (need a trained model to evaluate), `00_Mathematics/04_statistics.ipynb`**

How to know whether a trained model is actually good - and whether one
model is meaningfully better than another, not just luckier on one split.

## Files, in reading order
1. `01_regression_metrics.ipynb`
2. `02_classification_metrics.ipynb`
3. `03_ranking_metrics.ipynb`
4. `04_calibration.ipynb`
5. `05_cross_validation.ipynb`
6. `06_learning_curves.ipynb`
7. `07_validation_strategies.ipynb`
8. `08_statistical_model_comparison.ipynb`

## What you should be able to do after this folder
Choose the right metric for a task (never just "accuracy" by default -
`02_classification_metrics.ipynb` and `41-Imbalanced-Data.md`'s
accuracy-paradox example are the concrete warning), estimate
generalization error with an honest confidence interval, and state
whether two models' CV scores differ by more than noise (the paired
t-test worked example already built).

## Where this feeds forward
`11_Algorithm_Selection_and_Comparison/` is essentially this folder's
metrics applied comparatively across every algorithm in `03_`/`04_`.
