"""PCA eigenvectors overlaid on the actual hand-worked 5-point example."""
import numpy as np
import matplotlib.pyplot as plt
from viz_utils import set_style, savefig

def main():
    set_style()
    X = np.array([[2,1],[-1,-2],[0,0],[1,2],[-2,-1]], dtype=float)
    cov = np.cov(X.T, bias=True)
    eigvals, eigvecs = np.linalg.eigh(cov)
    order = np.argsort(eigvals)[::-1]
    eigvals, eigvecs = eigvals[order], eigvecs[:, order]

    fig, ax = plt.subplots(figsize=(6,6))
    ax.scatter(X[:,0], X[:,1], s=70, color="#3B82F6", edgecolor="k", zorder=3)
    colors = ["#EF4444", "#F97316"]
    for i in range(2):
        v = eigvecs[:, i] * np.sqrt(eigvals[i]) * 1.8
        ax.annotate("", xy=v, xytext=(0,0),
                    arrowprops=dict(arrowstyle="->", color=colors[i], lw=2.5))
        ax.text(v[0]*1.1, v[1]*1.1, f"PC{i+1} (var={eigvals[i]:.1f})", color=colors[i], fontsize=10)
    ax.axhline(0, color="#E5E7EB", zorder=0); ax.axvline(0, color="#E5E7EB", zorder=0)
    ax.set_xlim(-4,4); ax.set_ylim(-4,4)
    ax.set_aspect("equal")
    ax.set_title("PCA — Principal Components (hand-worked example)")
    savefig(fig, "pca_eigenvectors.png")
    plt.close(fig)
    print("saved")

if __name__ == "__main__":
    main()
