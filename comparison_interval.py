# Re-importing libraries and re-running the corrected visualization with the additional high-accuracy scenario

import numpy as np
import matplotlib.pyplot as plt

# Simulating confidence interval widths for different methods
n_values = np.linspace(50, 1000, 10)  # Different labeled dataset sizes
classical_width = 1 / np.sqrt(n_values)  # Classical method (high variance, wide CI)
imputation_width = 0.8 * classical_width  # Imputation (biased, smaller but inaccurate)
prediction_powered_width = 0.5 * classical_width  # Prediction-powered (valid but tighter)
high_accuracy_width = 0.2 * classical_width  # Highly accurate model, 99% accurate predictions

# Plotting the confidence interval widths
plt.figure(figsize=(8, 5))
plt.plot(n_values, classical_width, label="Classical Inference", linestyle="--", marker="o")
plt.plot(n_values, imputation_width, label="Imputation (Biased)", linestyle="--", marker="s")
plt.plot(n_values, prediction_powered_width, label="Prediction-Powered Inference", linestyle="-", marker="d")
plt.plot(n_values, high_accuracy_width, label="99% Accurate Predictions", linestyle="-.", marker="^", color='purple')

# Labels and title
plt.xlabel("Number of Labeled Data Points (n)")
plt.ylabel("Confidence Interval Width")
plt.title("Comparison of Confidence Interval Widths")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()