"""Bias-variance tradeoff curve — used in 07_ML_Theory/04_bias_variance_tradeoff.ipynb."""
import numpy as np
import matplotlib.pyplot as plt
from viz_utils import set_style, savefig

def main():
    set_style()
    complexity = np.linspace(1, 20, 100)
    bias2 = 25 / complexity**1.1
    variance = 0.06 * complexity**1.6
    noise = np.full_like(complexity, 2.0)
    total = bias2 + variance + noise

    fig, ax = plt.subplots()
    ax.plot(complexity, bias2, label="Bias$^2$", color="#3B82F6")
    ax.plot(complexity, variance, label="Variance", color="#F97316")
    ax.plot(complexity, noise, "--", label="Irreducible error", color="#9CA3AF")
    ax.plot(complexity, total, label="Total Expected Error", color="#EF4444", linewidth=2.2)
    opt = complexity[np.argmin(total)]
    ax.axvline(opt, color="black", linestyle=":", linewidth=1)
    ax.text(opt+0.3, ax.get_ylim()[1]*0.9, "Sweet spot", fontsize=9)
    ax.set_xlabel("Model Complexity"); ax.set_ylabel("Error")
    ax.set_title("Bias-Variance Tradeoff")
    ax.legend()
    savefig(fig, "bias_variance_tradeoff.png")
    plt.close(fig)
    print("saved, optimal complexity ~", round(opt,2))

if __name__ == "__main__":
    main()
