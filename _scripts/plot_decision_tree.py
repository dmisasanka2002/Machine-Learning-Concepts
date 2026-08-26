"""Decision tree diagram + entropy bar comparison — for Decision Tree notebook."""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from viz_utils import set_style, savefig

def main():
    set_style()
    X = np.array([[1,1],[1,0],[0,1],[0,0],[1,1],[0,0],[1,0],[0,1]])  # Weather(1=Sunny), Weekend(1=Yes)
    y = np.array([1,0,1,0,1,0,1,0])  # matches the worked example pattern roughly
    clf = DecisionTreeClassifier(max_depth=2, random_state=0).fit(X, y)
    fig, ax = plt.subplots(figsize=(8,5))
    plot_tree(clf, feature_names=["Weather(Sunny=1)","Weekend(Yes=1)"], class_names=["No","Yes"],
              filled=True, ax=ax, fontsize=9)
    ax.set_title("Decision Tree — split on Information Gain")
    savefig(fig, "decision_tree_diagram.png")
    plt.close(fig)
    print("saved")

if __name__ == "__main__":
    main()
