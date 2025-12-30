# The Five-Rule Framework: A Unified Theory of Cognition and Society

## Project Overview

This repository presents the "Five-Rule Framework," a minimal unified theory aiming to bridge the explanatory gaps across neuroscience, psychology, artificial intelligence, and social science. We propose that complex human intelligence, identity, and societal structures arise from the recursive application of five core principles, grounded in the Free Energy Principle and Active Inference.

The goal is to provide a non-dualistic, computationally grounded explanation for phenomena ranging from neural activity to political polarization.

##  The Fragmentation Problem

Current fields explain parts of the human system:
* **Neuroscience:** Neural mechanisms without a system-level theory of intelligence.
* **Psychology:** Fragmented behavioral models without theoretical unification.
* **Artificial Intelligence:** Imitates cognition without explaining its underlying structure.
* **Philosophy:** Debates mind without empirical constraints.
* **Social Science:** Describes institutions without deriving them from cognition.

The Five-Rule Framework seeks to resolve this fragmentation.

##  The Five Core Principles

Our framework is built upon five interacting principles:

1.  **Prediction (Free Energy Minimization):** The fundamental imperative of any cognitive system is to minimize the discrepancy between its internal model and sensory input.
2.  **Feedback (Active Inference):** Systems actively change their environment (behavior) or their internal models (learning) to reduce prediction error.
3.  **Attention (Precision Weighting):** The system allocates computational resources (attention) by assigning "precision" to specific prediction errors, determining which signals are prioritized.
4.  **Self-Modeling (Hierarchical Control):** The brain constructs a high-level internal model of itself to organize agency, predict its own actions, and interact in social contexts.
5.  **Social Coupling (Synchronization of Priors):** When predictive agents interact, they strive to minimize mutual prediction error, leading to the emergence of shared generative models (culture, language, institutions).

## Repository Contents

* `./paper/`: The full academic paper in LaTeX source (`.tex`) and compiled PDF format (`.pdf`).
* `./figures/`: High-resolution vector graphics (PDF/SVG) for all diagrams presented in the paper.
* `./code/`:
    * `toy_model_prediction.py`: A simple Python simulation demonstrating the core concept of prediction error minimization.
    * (Future additions: More complex simulations of active inference, attention, or social coupling.)
* `README.md`: This file.

##  Toy Model: Prediction Error Minimization

The `toy_model_prediction.py` script provides a basic example of a system attempting to predict a sensory input and updating its internal model based on prediction error. This illustrates Principle I (Prediction) and the fundamental loop of Principle II (Feedback).

```python
# Snippet from toy_model_prediction.py (full code in ./code/)
# The model adjusts its internal 'belief' (prediction) to match the 'actual_stimulus'.
# error = actual_stimulus - model_prediction
# model_prediction += learning_rate * error
