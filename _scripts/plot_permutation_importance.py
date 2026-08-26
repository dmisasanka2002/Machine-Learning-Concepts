import numpy as np
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from viz_utils import set_style, savefig

def main():
    set_style()
    data = load_iris()
    model = RandomForestClassifier(random_state=0).fit(data.data, data.target)
    result = permutation_importance(model, data.data, data.target, n_repeats=20, random_state=0)
    order = np.argsort(result.importances_mean)
    fig, ax = plt.subplots(figsize=(6,4))
    ax.barh(np.array(data.feature_names)[order], result.importances_mean[order],
            xerr=result.importances_std[order], color="#3B82F6")
    ax.set_xlabel("Permutation Importance (accuracy drop)")
    ax.set_title("Permutation Importance — Iris Random Forest")
    savefig(fig, "permutation_importance.png")
    plt.close(fig)
    print("saved")

if __name__ == "__main__":
    main()
