"""PCA projection + variance-explained plot — used in PCA notebook."""
import numpy as np
import matplotlib.pyplot as plt
from viz_utils import set_style, savefig

def plot_pca(X_2d_proj, y, explained_var_ratio, filename="pca_projection.png"):
    set_style()
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    sc = axes[0].scatter(X_2d_proj[:, 0], X_2d_proj[:, 1], c=y, cmap="viridis", edgecolor="k", s=30)
    axes[0].set_xlabel("PC1"); axes[0].set_ylabel("PC2")
    axes[0].set_title("Data Projected onto Top 2 Principal Components")

    axes[1].bar(range(1, len(explained_var_ratio)+1), explained_var_ratio, color="#3B82F6")
    axes[1].plot(range(1, len(explained_var_ratio)+1), np.cumsum(explained_var_ratio), "o-", color="#EF4444", label="Cumulative")
    axes[1].set_xlabel("Principal Component"); axes[1].set_ylabel("Variance Explained Ratio")
    axes[1].set_title("Scree Plot"); axes[1].legend()
    savefig(fig, filename)
    plt.close(fig)

if __name__ == "__main__":
    from sklearn.datasets import load_iris
    from sklearn.decomposition import PCA
    data = load_iris()
    X, y = data.data, data.target
    pca = PCA(n_components=4).fit(X)
    X_proj = pca.transform(X)[:, :2]
    plot_pca(X_proj, y, pca.explained_variance_ratio_)
    print("saved")
