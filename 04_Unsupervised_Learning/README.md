# `04_Unsupervised_Learning/` - README
**Stage 4 of 12 · Core tier · Prerequisites: `00_Mathematics/`, `02_Data/` (does NOT require `03_Supervised_Learning/`, though `12_kernel_pca.ipynb` and `15_tsne_umap.ipynb` benefit from having seen Kernel Methods and PCA respectively first)**

Three loosely-coupled arcs: clustering (grouping), density/latent-variable
modeling (GMM/KDE), and dimensionality reduction (PCA family + t-SNE/UMAP)
- plus anomaly detection, which borrows tools from both clustering and
density estimation.

## Reading order
**Clustering**: `01_kmeans.ipynb` → `02_kmeans_from_scratch.ipynb` →
`03_kmedoids.ipynb` → `04_hierarchical.ipynb` →
`05_hierarchical_from_scratch.ipynb` → `06_dbscan.ipynb` → `07_optics.ipynb`
**Density/latent-variable**: `08_gmm_and_em.ipynb` → `09_kde.ipynb`
**Dimensionality reduction**: `10_pca.ipynb` → `11_pca_from_scratch.ipynb`
→ `12_kernel_pca.ipynb` → `13_ica.ipynb` → `14_nmf.ipynb` →
`15_tsne_umap.ipynb`
**Cross-cutting**: `16_anomaly_detection.ipynb`,
`17_generative_vs_discriminative.ipynb` (can be read any time - it's a
conceptual bridge back to `03_Supervised_Learning/Classification/`'s
LDA/QDA/Naive Bayes vs. Logistic Regression distinction)

## What you should be able to do after this folder
Given unlabeled data, choose and justify a clustering method (k-known vs.
unknown, spherical vs. arbitrary-shape - cross-check against
`11_Algorithm_Selection_and_Comparison/04`), reduce dimensionality with a
justified method choice, and explain the difference between K-Means and
GMM as hard vs. soft versions of the same underlying idea
(`15-GMM-EM-Additions.md` §4 makes this explicit).

## Where this feeds forward
`11_Algorithm_Selection_and_Comparison/04` and `05` compare everything
here head-to-head; `12_Projects/03_clustering_project_customer_segmentation.ipynb`
and `05_dimensionality_reduction_project_iris.ipynb` are the applied
capstones.
