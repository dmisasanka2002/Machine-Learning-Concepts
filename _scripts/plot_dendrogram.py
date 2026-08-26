"""Dendrogram — used in Hierarchical Clustering notebook."""
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from viz_utils import set_style, savefig

def main():
    set_style()
    import numpy as np
    X = np.array([[1,2],[1.5,1.8],[5,8],[8,8],[1,0.6],[9,11]])
    Z = linkage(X, method="ward")
    fig, ax = plt.subplots(figsize=(6,4.5))
    dendrogram(Z, labels=[f"P{i}" for i in range(len(X))], ax=ax, color_threshold=5)
    ax.set_title("Agglomerative Clustering — Ward Linkage Dendrogram")
    ax.set_ylabel("Distance (Ward criterion)")
    savefig(fig, "dendrogram_ward.png")
    plt.close(fig)
    print("saved")

if __name__ == "__main__":
    main()
