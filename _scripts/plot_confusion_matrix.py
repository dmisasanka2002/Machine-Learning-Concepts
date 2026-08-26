"""Confusion matrix heatmap — for Model Evaluation notebook."""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from viz_utils import set_style, savefig

def main():
    set_style()
    cm = np.array([[130,10],[20,40]])  # TN,FP / FN,TP -- matches the worked example in 16-Model-Evaluation-Additions.md
    fig, ax = plt.subplots(figsize=(5,4.5))
    im = ax.imshow(cm, cmap="Blues")
    for i in range(2):
        for j in range(2):
            ax.text(j, i, cm[i,j], ha="center", va="center",
                    color="white" if cm[i,j]>cm.max()/2 else "black", fontsize=14)
    ax.set_xticks([0,1]); ax.set_xticklabels(["Pred Neg","Pred Pos"])
    ax.set_yticks([0,1]); ax.set_yticklabels(["Actual Neg","Actual Pos"])
    ax.set_title("Confusion Matrix (worked example: TP=40, FP=10, FN=20, TN=130)")
    savefig(fig, "confusion_matrix.png")
    plt.close(fig)
    print("saved")

if __name__ == "__main__":
    main()
