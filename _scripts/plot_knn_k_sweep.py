"""K sweep showing bias-variance effect of k in KNN — for KNN notebook."""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.neighbors import KNeighborsClassifier
from viz_utils import set_style, savefig

def main():
    set_style()
    X, y = make_moons(n_samples=150, noise=0.25, random_state=3)
    ks = [1, 5, 15, 40]
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    h = 0.05
    x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
    y_min, y_max = X[:,1].min()-1, X[:,1].max()+1
    xx, yy = np.meshgrid(np.arange(x_min,x_max,h), np.arange(y_min,y_max,h))
    for ax, k in zip(axes, ks):
        model = KNeighborsClassifier(n_neighbors=k).fit(X, y)
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
        ax.contourf(xx, yy, Z, alpha=0.25, cmap="coolwarm")
        ax.scatter(X[:,0], X[:,1], c=y, cmap="coolwarm", edgecolor="k", s=18)
        ax.set_title(f"k={k}")
    fig.suptitle("KNN Decision Boundary vs k (variance -> bias as k grows)")
    savefig(fig, "knn_k_sweep.png")
    plt.close(fig)
    print("saved")

if __name__ == "__main__":
    main()
