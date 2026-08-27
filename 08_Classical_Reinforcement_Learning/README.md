# `08_Classical_Reinforcement_Learning/` - README
**Stage 8 of 12 (parallel branch) · Core tier · Prerequisites: `00_Mathematics/03_probability.ipynb`**

Classical, tabular RL only - MDPs through Q-learning. Deep RL (function-
approximated policies/value functions, DQN, policy gradients,
actor-critic) is explicitly out of scope here and lives in the separate
DL repository, consistent with the scope decision made early in this
project: classical RL is genuinely classical ML theory (dynamic
programming, Bellman equations), not deep learning.

## Files, in reading order
1. `01_mdp_and_bellman_equations.ipynb` (source: `26-Classical-Reinforcement-Learning.md` §1)
2. `02_dynamic_programming.ipynb` (§2)
3. `03_monte_carlo_methods.ipynb` (§3)
4. `04_temporal_difference_learning.ipynb` (§4)
5. `05_q_learning.ipynb` (§5)

## What you should be able to do after this folder
Set up a small MDP, write its Bellman equation, and hand-trace one
iteration each of value iteration, TD(0), and Q-learning - all three were
verified numerically in the source content and should reproduce exactly.

## Where this feeds forward
Nowhere else in this repo directly (RL is a self-contained branch,
parallel to the main supervised/unsupervised sequence) - it's here for
completeness of "classical ML," not because later notebooks depend on it.
