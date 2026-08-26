"""
Shared plotting style + reusable helpers for every notebook in the repo.
Import at the top of any notebook:  from _scripts.viz_utils import *
Keeps all 30+ notebooks visually consistent (one of the house standards).
"""
import matplotlib.pyplot as plt
import numpy as np

PALETTE = {
    "class0": "#3B82F6",   # blue
    "class1": "#F97316",   # orange
    "class2": "#10B981",   # green
    "line":   "#EF4444",   # red
    "grid":   "#E5E7EB",
}

def set_style():
    plt.rcParams.update({
        "figure.figsize": (6, 4.5),
        "figure.dpi": 110,
        "axes.grid": True,
        "grid.color": PALETTE["grid"],
        "grid.linewidth": 0.6,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "font.size": 11,
    })

def savefig(fig, name, assets_dir="../_assets"):
    """Save a figure into the shared _assets/ folder used by every notebook."""
    import os
    os.makedirs(assets_dir, exist_ok=True)
    path = os.path.join(assets_dir, name)
    fig.savefig(path, bbox_inches="tight")
    return path

def draw_prereq_graph(edges, save_path="../_assets/prereq_graph.png"):
    """edges: list of (from_notebook, to_notebook) prerequisite pairs."""
    import networkx as nx
    G = nx.DiGraph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G, seed=42)
    fig, ax = plt.subplots(figsize=(9, 6))
    nx.draw(G, pos, ax=ax, with_labels=True, node_color=PALETTE["class0"],
            node_size=1800, font_size=7, font_color="white", arrows=True,
            edge_color="#9CA3AF")
    savefig(fig, "prereq_graph.png", assets_dir=save_path.rsplit("/", 1)[0])
    plt.close(fig)
