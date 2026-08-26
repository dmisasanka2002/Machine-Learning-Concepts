"""Generates comparison bar charts: accuracy/time tradeoff across classifiers
and regressors on real repo datasets, used in 11_Algorithm_Selection_and_Comparison/."""
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, f1_score
from viz_utils import set_style, savefig

def main():
    set_style()
    df = pd.read_csv("../../repo/datasets/kyphosis.csv") if False else None
    # Use a bundled-style synthetic-but-realistic dataset via sklearn to avoid path coupling
    from sklearn.datasets import load_breast_cancer
    data = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25, random_state=0)
    scaler = StandardScaler().fit(X_train)
    X_train_s, X_test_s = scaler.transform(X_train), scaler.transform(X_test)

    models = {
        "Logistic Regression": LogisticRegression(max_iter=2000),
        "KNN": KNeighborsClassifier(),
        "Decision Tree": DecisionTreeClassifier(random_state=0),
        "Random Forest": RandomForestClassifier(random_state=0),
        "AdaBoost": AdaBoostClassifier(random_state=0),
        "Gradient Boosting": GradientBoostingClassifier(random_state=0),
        "SVM (RBF)": SVC(),
        "Naive Bayes": GaussianNB(),
    }

    rows = []
    for name, model in models.items():
        t0 = time.time()
        model.fit(X_train_s, y_train)
        train_time = time.time() - t0
        preds = model.predict(X_test_s)
        rows.append((name, accuracy_score(y_test, preds), f1_score(y_test, preds), train_time))

    res = pd.DataFrame(rows, columns=["model","accuracy","f1","train_time_s"]).sort_values("accuracy")

    fig, axes = plt.subplots(1, 2, figsize=(13,5))
    axes[0].barh(res.model, res.accuracy, color="#3B82F6")
    axes[0].set_xlim(0.85, 1.0)
    axes[0].set_title("Test Accuracy — Breast Cancer Dataset")
    axes[1].barh(res.model, res.train_time_s, color="#F97316")
    axes[1].set_title("Training Time (s)")
    plt.tight_layout()
    savefig(fig, "classifier_comparison.png")
    plt.close(fig)
    print(res.to_string(index=False))

if __name__ == "__main__":
    main()
