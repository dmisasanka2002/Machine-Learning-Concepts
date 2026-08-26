"""
Visualizes gradient descent converging on a convex cost surface (used in
06_Optimization and Linear/Logistic Regression notebooks).
"""
import numpy as np
import matplotlib.pyplot as plt
from viz_utils import set_style, savefig, PALETTE

def cost(w0, w1, X, y):
    m = len(y)
    preds = w0 + w1 * X
    return (1/(2*m)) * np.sum((preds - y) ** 2)

def gradient_descent_path(X, y, lr=0.05, n_iter=40):
    w0, w1 = 0.0, 0.0
    m = len(y)
    path = [(w0, w1, cost(w0, w1, X, y))]
    for _ in range(n_iter):
        preds = w0 + w1 * X
        g0 = (1/m) * np.sum(preds - y)
        g1 = (1/m) * np.sum((preds - y) * X)
        w0 -= lr * g0
        w1 -= lr * g1
        path.append((w0, w1, cost(w0, w1, X, y)))
    return np.array(path)

def main():
    set_style()
    rng = np.random.default_rng(0)
    X = np.linspace(0, 5, 20)
    y = 2.5 * X + 1.0 + rng.normal(0, 1.0, size=20)

    path = gradient_descent_path(X, y, lr=0.05, n_iter=60)

    w0_range = np.linspace(-2, 4, 80)
    w1_range = np.linspace(-1, 5, 80)
    W0, W1 = np.meshgrid(w0_range, w1_range)
    Z = np.zeros_like(W0)
    for i in range(W0.shape[0]):
        for j in range(W0.shape[1]):
            Z[i, j] = cost(W0[i, j], W1[i, j], X, y)

    fig, ax = plt.subplots(figsize=(6, 5))
    cs = ax.contour(W0, W1, Z, levels=25, cmap="Blues")
    ax.plot(path[:, 0], path[:, 1], "o-", color=PALETTE["line"], markersize=3,
            linewidth=1.2, label="Gradient descent path")
    ax.scatter([path[-1,0]], [path[-1,1]], color="black", zorder=5, label="Converged")
    ax.set_xlabel("w0 (intercept)")
    ax.set_ylabel("w1 (slope)")
    ax.set_title("Gradient Descent on a Convex Cost Surface")
    ax.legend()
    savefig(fig, "gradient_descent_convergence.png")
    plt.close(fig)
    print("Saved. Final (w0, w1, cost):", path[-1])

if __name__ == "__main__":
    main()
