"""
Animates Lloyd's algorithm (K-Means) iterating to convergence, saved as GIF.
Used in 04_Unsupervised_Learning/01_kmeans.ipynb per the 'animations, not
just static plots' visual standard.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from viz_utils import set_style, PALETTE

def lloyds_algorithm_history(X, k, n_iter=8, seed=0):
    rng = np.random.default_rng(seed)
    centroids = X[rng.choice(len(X), k, replace=False)]
    history = []
    for _ in range(n_iter):
        dists = np.linalg.norm(X[:, None, :] - centroids[None, :, :], axis=2)
        labels = dists.argmin(axis=1)
        history.append((centroids.copy(), labels.copy()))
        new_centroids = np.array([X[labels == j].mean(axis=0) if np.any(labels==j)
                                   else centroids[j] for j in range(k)])
        centroids = new_centroids
    history.append((centroids.copy(), labels.copy()))
    return history

def main():
    set_style()
    rng = np.random.default_rng(1)
    X = np.vstack([
        rng.normal([2, 2], 0.6, size=(30, 2)),
        rng.normal([8, 3], 0.6, size=(30, 2)),
        rng.normal([5, 8], 0.6, size=(30, 2)),
    ])
    history = lloyds_algorithm_history(X, k=3, n_iter=6)

    fig, ax = plt.subplots(figsize=(5.5, 5))
    def update(i):
        ax.clear()
        centroids, labels = history[i]
        ax.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", s=30, edgecolor="k")
        ax.scatter(centroids[:, 0], centroids[:, 1], c="red", marker="X", s=200, edgecolor="k")
        ax.set_title(f"Lloyd's Algorithm — Iteration {i}")
        ax.set_xlim(X[:,0].min()-1, X[:,0].max()+1)
        ax.set_ylim(X[:,1].min()-1, X[:,1].max()+1)

    anim = FuncAnimation(fig, update, frames=len(history), interval=800)
    anim.save("../_assets/kmeans_lloyd_animation.gif", writer=PillowWriter(fps=1))
    plt.close(fig)
    print("saved gif with", len(history), "frames")

if __name__ == "__main__":
    main()
