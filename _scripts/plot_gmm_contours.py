"""GMM soft-clustering contours vs K-Means hard boundary — for GMM notebook."""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs
from viz_utils import set_style, savefig

def main():
    set_style()
    X, y = make_blobs(n_samples=200, centers=3, cluster_std=[1.0,1.8,0.9], random_state=3)
    gmm = GaussianMixture(n_components=3, random_state=0).fit(X)

    x_min,x_max = X[:,0].min()-2, X[:,0].max()+2
    y_min,y_max = X[:,1].min()-2, X[:,1].max()+2
    xx, yy = np.meshgrid(np.linspace(x_min,x_max,200), np.linspace(y_min,y_max,200))
    Z = -gmm.score_samples(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    fig, ax = plt.subplots(figsize=(6.5,5.5))
    ax.contour(xx, yy, Z, levels=12, cmap="Blues", alpha=0.6)
    labels = gmm.predict(X)
    ax.scatter(X[:,0], X[:,1], c=labels, cmap="viridis", s=25, edgecolor="k", linewidth=0.3)
    ax.scatter(gmm.means_[:,0], gmm.means_[:,1], c="red", marker="X", s=200, edgecolor="k")
    ax.set_title("Gaussian Mixture Model — Soft Clustering (density contours)")
    savefig(fig, "gmm_contours.png")
    plt.close(fig)
    print("saved")

if __name__ == "__main__":
    main()
