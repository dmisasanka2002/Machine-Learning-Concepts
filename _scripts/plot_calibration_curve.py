import numpy as np
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from viz_utils import set_style, savefig

def main():
    set_style()
    X, y = make_classification(n_samples=2000, n_features=15, n_informative=5, random_state=1)
    fig, ax = plt.subplots(figsize=(5.5,5.5))
    ax.plot([0,1],[0,1],"--", color="#9CA3AF", label="Perfectly calibrated")
    for name, model in [("Logistic Regression", LogisticRegression()), ("Naive Bayes", GaussianNB())]:
        model.fit(X[:1000], y[:1000])
        probs = model.predict_proba(X[1000:])[:,1]
        frac_pos, mean_pred = calibration_curve(y[1000:], probs, n_bins=10)
        ax.plot(mean_pred, frac_pos, "o-", label=name)
    ax.set_xlabel("Mean predicted probability"); ax.set_ylabel("Fraction of positives")
    ax.set_title("Calibration Curves (Reliability Diagram)")
    ax.legend()
    savefig(fig, "calibration_curve.png")
    plt.close(fig)
    print("saved")

if __name__ == "__main__":
    main()
