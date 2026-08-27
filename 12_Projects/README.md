# `12_Projects/` - README
**Stage 12 of 12 (final) · Core tier · Prerequisites: everything (this is the capstone)**

End-to-end applications on real repo datasets - each project should cite
`11_Algorithm_Selection_and_Comparison/` when justifying its algorithm
choice, use proper validation strategy from `05_Model_Evaluation/`, and
include a brief interpretability/fairness pass from `09_Interpretability/`
and `10_Responsible_ML/` wherever the data plausibly involves people.

## Files
1. `01_regression_project_insurance_cost.ipynb` - `datasets/insurance.csv`
2. `02_classification_project_social_ads.ipynb` - `datasets/logistic regression dataset-Social_Network_Ads.csv`
3. `03_clustering_project_customer_segmentation.ipynb` - `datasets/Customers.csv`
4. `04_anomaly_detection_project_cardio.ipynb` - `datasets/cardio_modify.csv`
   (depends on `04_Unsupervised_Learning/16_anomaly_detection.ipynb` and
   `02_Data/10_imbalanced_data_handling.ipynb`)
5. `05_dimensionality_reduction_project_iris.ipynb` - `datasets/Iris.csv`


## What "done" looks like for a project
Not just a trained model with a metric - a short written justification
connecting back to earlier stages: which algorithm(s) were compared and
why the winner was chosen (`11_`), how generalization error was honestly
estimated (`05_`), what the model is actually keying on
(`09_`), and any fairness/robustness caveats worth flagging (`10_`). This
is the difference between a tutorial exercise and a genuine applied-ML
deliverable, and it's the intended payoff of working through all 12
stages in order rather than jumping straight here.
