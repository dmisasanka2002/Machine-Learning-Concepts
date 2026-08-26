"""
Generates the 'How to Choose an ML Algorithm' flowchart as a static image
using matplotlib boxes/arrows (no graphviz dependency needed at runtime).
Used in 11_Algorithm_Selection_and_Comparison/01_how_to_choose_an_algorithm.ipynb
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

def box(ax, xy, text, w=2.6, h=0.7, color="#3B82F6", fontsize=8.3, fontcolor="white"):
    x, y = xy
    b = FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.08",
                        linewidth=1, edgecolor="#1F2937", facecolor=color)
    ax.add_patch(b)
    ax.text(x, y, text, ha="center", va="center", fontsize=fontsize, color=fontcolor, wrap=True)
    return (x, y)

def arrow(ax, p1, p2, label=""):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=12,
                         linewidth=1.1, color="#4B5563")
    ax.add_patch(a)
    if label:
        mx, my = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
        ax.text(mx+0.15, my, label, fontsize=7.5, color="#111827", style="italic")

fig, ax = plt.subplots(figsize=(21, 8))
ax.set_xlim(-0.5, 20.5); ax.set_ylim(4.8, 12); ax.axis("off")

root = box(ax, (10, 11.2), "What is your goal?", color="#111827", w=3.4, h=0.8)

labeled = box(ax, (4.5, 9.6), "Labeled data?\n(Supervised)", color="#1D4ED8", w=3.2, h=0.9)
unlabeled = box(ax, (15.5, 9.6), "No labels\n(Unsupervised)", color="#1D4ED8", w=3.2, h=0.9)
arrow(ax, (8.6,10.9), (5.3,10.0), "Yes")
arrow(ax, (11.4,10.9), (14.7,10.0), "No")

reg = box(ax, (2.0, 8.0), "Target is\ncontinuous?\n(Regression)", color="#2563EB", w=2.9, h=1.0)
clf = box(ax, (7.0, 8.0), "Target is\ncategorical?\n(Classification)", color="#2563EB", w=2.9, h=1.0)
arrow(ax, (3.6,9.15), (2.3,8.5))
arrow(ax, (5.4,9.15), (6.6,8.5))

lin = box(ax, (0.7, 6.0), "Linear relationship,\nneed interpretability\n-> Linear / Ridge /\nLasso Regression", color="#60A5FA", w=3.0, h=1.15)
nonlin = box(ax, (3.3, 6.0), "Non-linear pattern,\nmany features\n-> Random Forest /\nGradient Boosting Reg.", color="#60A5FA", w=3.0, h=1.15)
arrow(ax, (1.3,7.5), (0.8,6.6))
arrow(ax, (2.6,7.5), (3.1,6.6))

small_interp = box(ax, (5.8, 6.0), "Need interpretability,\nfew features\n-> Logistic Regression /\nDecision Tree / Naive Bayes", color="#60A5FA", w=3.2, h=1.15)
many_feat = box(ax, (9.2, 6.0), "Complex boundary,\nmany features\n-> SVM (RBF) /\nRandom Forest / Boosting", color="#60A5FA", w=3.2, h=1.15)
arrow(ax, (6.4,7.5), (5.9,6.6))
arrow(ax, (7.7,7.5), (9.0,6.6))

cluster = box(ax, (13.2, 8.0), "Group similar\npoints together?\n(Clustering)", color="#2563EB", w=3.0, h=1.0)
reduce = box(ax, (18.0, 8.0), "Reduce dimensions /\nvisualize structure?\n(Dim. Reduction)", color="#2563EB", w=3.0, h=1.0)
arrow(ax, (14.8,9.15), (13.5,8.5))
arrow(ax, (16.2,9.15), (17.6,8.5))

k_known = box(ax, (11.9, 6.0), "Know # clusters,\nroughly spherical?\n-> K-Means", color="#60A5FA", w=2.9, h=1.15)
k_unknown = box(ax, (15.0, 6.0), "Unknown shape,\nnoise/outliers?\n-> DBSCAN /\nHierarchical", color="#60A5FA", w=2.9, h=1.15)
arrow(ax, (12.8,7.5), (12.0,6.6))
arrow(ax, (13.9,7.5), (14.8,6.6))

linear_dr = box(ax, (17.0, 6.0), "Linear structure,\ninterpretable axes\n-> PCA", color="#60A5FA", w=2.8, h=1.15)
nonlinear_dr = box(ax, (19.5, 6.0), "Only for 2D/3D\nvisualization\n-> t-SNE / UMAP", color="#60A5FA", w=2.8, h=1.15)
arrow(ax, (17.5,7.5), (17.1,6.6))
arrow(ax, (18.6,7.5), (19.3,6.6))

ax.set_title("How to Choose an ML Algorithm", fontsize=17, weight="bold", pad=16)
plt.tight_layout()
fig.savefig("../_assets/algorithm_choice_flowchart.png", dpi=130, bbox_inches="tight")
print("saved")
