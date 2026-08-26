import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from viz_utils import set_style, savefig

def main():
    set_style()
    X, y = load_digits(return_X_y=True)
    sizes, train_scores, val_scores = learning_curve(
        SVC(kernel="rbf", gamma=0.001), X, y, cv=5,
        train_sizes=np.linspace(0.1, 1.0, 8), scoring="accuracy")
    fig, ax = plt.subplots()
    ax.plot(sizes, train_scores.mean(axis=1), "o-", color="#3B82F6", label="Training score")
    ax.plot(sizes, val_scores.mean(axis=1), "o-", color="#F97316", label="Validation score")
    ax.fill_between(sizes, train_scores.mean(1)-train_scores.std(1), train_scores.mean(1)+train_scores.std(1), alpha=0.15, color="#3B82F6")
    ax.fill_between(sizes, val_scores.mean(1)-val_scores.std(1), val_scores.mean(1)+val_scores.std(1), alpha=0.15, color="#F97316")
    ax.set_xlabel("Training set size"); ax.set_ylabel("Accuracy")
    ax.set_title("Learning Curve — SVM on Digits")
    ax.legend()
    savefig(fig, "learning_curve.png")
    plt.close(fig)
    print("saved, gap at max size:", train_scores.mean(1)[-1]-val_scores.mean(1)[-1])

if __name__ == "__main__":
    main()
