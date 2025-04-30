import numpy as np
import matplotlib.pyplot as plt

# Define parameters
n_values = np.arange(50, 2050, 50)
N_small = 500  # Small unlabeled dataset (underpowered scenario)

# True parameters for simulation
p_true = 0.5
eta_bad_model = 0.3  # High model error scenario

# Variance computations
var_Y = p_true * (1 - p_true)
var_f_minus_Y = lambda eta: eta - eta**2 * (1 - 2*p_true)**2
var_f = var_Y  # Assume variance of predictions similar to true variance

# Widths for intervals
width_classical = lambda n: 1.96 * np.sqrt(var_Y / n)
width_ppi = lambda n, N, eta: 1.96 * np.sqrt(var_f / N + var_f_minus_Y(eta) / n)

# Calculate interval widths
widths_classical = [width_classical(n) for n in n_values]
widths_ppi_bad_model = [width_ppi(n, 10000, eta_bad_model) for n in n_values]
widths_ppi_small_N = [width_ppi(n, N_small, 0.1) for n in n_values]  # Good model, small N

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(n_values, widths_classical, label='Classical Interval', color='gray', linewidth=2)
plt.plot(n_values, widths_ppi_bad_model, label='PPI (Inaccurate Model)', linestyle='--', color='red', linewidth=2)
plt.plot(n_values, widths_ppi_small_N, label='PPI (Small N)', linestyle=':', color='blue', linewidth=2)

plt.title('Underpowered Prediction-Powered Inference Cases')
plt.xlabel('Number of Labeled Samples (n)')
plt.ylabel('Interval Width')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
