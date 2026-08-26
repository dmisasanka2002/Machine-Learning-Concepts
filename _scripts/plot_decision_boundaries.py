"""Decision boundary plot — used in KNN, Decision Tree, SVM, Logistic Regression notebooks."""
import numpy as np
import matplotlib.pyplot as plt
from viz_utils import set_style, savefig, PALETTE

def plot_boundary(model, X, y, title, filename, h=0.05):
    set_style()
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    fig, ax = plt.subplots()
    ax.contourf(xx, yy, Z, alpha=0.25, cmap="coolwarm")
    scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", edgecolor="k", s=35)
    ax.set_title(title)
    ax.set_xlabel("Feature 1"); ax.set_ylabel("Feature 2")
    savefig(fig, filename)
    plt.close(fig)

if __name__ == "__main__":
    from sklearn.datasets import make_moons
    from sklearn.svm import SVC
    X, y = make_moons(n_samples=150, noise=0.2, random_state=1)
    model = SVC(kernel="rbf", C=1.0).fit(X, y)
    plot_boundary(model, X, y, "SVM (RBF kernel) Decision Boundary", "svm_decision_boundary.png")
    print("saved")
