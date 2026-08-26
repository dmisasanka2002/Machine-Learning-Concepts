"""ROC and Precision-Recall curves — used in 05_Model_Evaluation/02_classification_metrics.ipynb."""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc, precision_recall_curve
from viz_utils import set_style, savefig

def main():
    set_style()
    from sklearn.datasets import make_classification
    from sklearn.linear_model import LogisticRegression
    X, y = make_classification(n_samples=400, weights=[0.85, 0.15], random_state=1)
    model = LogisticRegression().fit(X, y)
    scores = model.predict_proba(X)[:, 1]

    fpr, tpr, _ = roc_curve(y, scores)
    roc_auc = auc(fpr, tpr)
    prec, rec, _ = precision_recall_curve(y, scores)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    axes[0].plot(fpr, tpr, color="#3B82F6", label=f"AUC = {roc_auc:.3f}")
    axes[0].plot([0,1],[0,1],"--", color="#9CA3AF")
    axes[0].set_xlabel("False Positive Rate"); axes[0].set_ylabel("True Positive Rate")
    axes[0].set_title("ROC Curve"); axes[0].legend()

    axes[1].plot(rec, prec, color="#F97316")
    axes[1].set_xlabel("Recall"); axes[1].set_ylabel("Precision")
    axes[1].set_title("Precision-Recall Curve (imbalanced data)")
    savefig(fig, "roc_pr_curves.png")
    plt.close(fig)
    print("saved, AUC=", round(roc_auc,3))

if __name__ == "__main__":
    main()
