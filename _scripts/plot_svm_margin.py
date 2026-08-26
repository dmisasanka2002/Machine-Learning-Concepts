"""SVM margin + support vectors, highlighted explicitly — for SVM notebook."""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from viz_utils import set_style, savefig

def main():
    set_style()
    X = np.array([[2,2],[3,3],[3,1],[0,0],[1,0],[0,1]], dtype=float)
    y = np.array([1,1,1,-1,-1,-1])
    clf = SVC(kernel="linear", C=1e5).fit(X, y)

    fig, ax = plt.subplots(figsize=(6,5.5))
    ax.scatter(X[:,0], X[:,1], c=y, cmap="coolwarm", s=80, edgecolor="k", zorder=3)
    ax.scatter(clf.support_vectors_[:,0], clf.support_vectors_[:,1], s=250,
               facecolors="none", edgecolors="black", linewidths=1.8, zorder=2, label="Support vectors")

    w, b = clf.coef_[0], clf.intercept_[0]
    xx = np.linspace(-1, 4, 50)
    yy = -(w[0]*xx+b)/w[1]
    margin = 1/np.linalg.norm(w)
    yy_up = yy + margin*np.sqrt(1+(w[0]/w[1])**2)
    yy_down = yy - margin*np.sqrt(1+(w[0]/w[1])**2)
    ax.plot(xx, yy, "k-", label="Decision boundary")
    ax.plot(xx, yy_up, "k--", linewidth=1)
    ax.plot(xx, yy_down, "k--", linewidth=1)
    ax.set_xlim(-1,4); ax.set_ylim(-1,4)
    ax.set_title("SVM: Maximum Margin & Support Vectors")
    ax.legend()
    savefig(fig, "svm_margin_diagram.png")
    plt.close(fig)
    print("saved")

if __name__ == "__main__":
    main()
