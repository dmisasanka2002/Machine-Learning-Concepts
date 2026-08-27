# `02_Data/` - README
**Stage 2 of 12 · Foundation/Core tier · Prerequisites: `01_Foundations/`, `00_Mathematics/04_statistics.ipynb`**

Getting raw data into a shape a model can learn from correctly - and not
accidentally cheating in the process (`07_data_leakage.ipynb` is the
single most consequential file in this folder despite being one of the
lighter ones mathematically).

## Files, in reading order
1. `01_data_types.ipynb`
2. `02_sampling.ipynb`
3. `03_cleaning_and_missing_values.ipynb`
4. `04_outliers.ipynb`
5. `05_encoding.ipynb`
6. `06_scaling.ipynb`
7. `07_data_leakage.ipynb`
8. `08_feature_engineering.ipynb`
9. `09_feature_selection.ipynb`
10. `10_advanced_data_transformation.ipynb`
11. `11_imbalanced_data_handling.ipynb`

## What you should be able to do after this folder
Look at any dataset in `datasets/` and correctly classify every column's
type, identify likely sampling/leakage risks, and produce a clean,
correctly-encoded, correctly-scaled feature matrix ready for
`03_Supervised_Learning/` or `04_Unsupervised_Learning/`.

## Where this feeds forward
Every algorithm notebook from here on assumes its input $X$ has already
passed through this pipeline - none of them re-derive encoding/scaling.
`07_data_leakage.ipynb` specifically should be re-read before
`05_Model_Evaluation/05_cross_validation.ipynb`, since leakage is a
cross-cutting risk that resurfaces there.
