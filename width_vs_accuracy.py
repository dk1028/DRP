# Remake the bar graph in reverse order (from 60% to 100%)

import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
n = 100  # number of labeled data points
N = 10000  # number of unlabeled data points
true_mean = 5  # true mean of the distribution

# Simulate true outcomes
Y_labeled = np.random.normal(true_mean, 1, n)
X_unlabeled = np.random.normal(true_mean, 1, N)

# Function to simulate predictions with a given accuracy
def generate_predictions(true_values, accuracy):
    noise_std = (1 - accuracy) * 2  # More noise for lower accuracy
    return true_values + np.random.normal(0, noise_std, len(true_values))

# Function to calculate prediction-powered CI and its width
def prediction_powered_ci_width(Y_labeled, f_X_labeled, f_X_unlabeled, n, N):
    delta = np.mean(f_X_labeled - Y_labeled)
    theta_f = np.mean(f_X_unlabeled)
    theta_pp = theta_f - delta
    
    var_f_Y = np.var(f_X_labeled - Y_labeled, ddof=1) / n
    var_f = np.var(f_X_unlabeled, ddof=1) / N
    se = np.sqrt(var_f_Y + var_f)
    
    ci_lower = theta_pp - 1.96 * se
    ci_upper = theta_pp + 1.96 * se
    return ci_upper - ci_lower

# Accuracy levels to test
accuracies = [1.0, 0.9, 0.8, 0.7, 0.6]
labels = ['100%', '90%', '80%', '70%', '60%']

# Compute CI widths
ci_widths = [
    prediction_powered_ci_width(
        Y_labeled,
        generate_predictions(Y_labeled, acc),
        generate_predictions(X_unlabeled, acc),
        n, N
    )
    for acc in accuracies
]


# Reverse the order of accuracies and corresponding CI widths
accuracies_reversed = accuracies[::-1]
labels_reversed = labels[::-1]
ci_widths_reversed = ci_widths[::-1]

# Create bar plot
x = np.arange(len(accuracies_reversed))
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x, ci_widths_reversed, align='center')
ax.set_xticks(x)
ax.set_xticklabels(labels_reversed)
ax.set_ylabel('CI Width')
ax.set_xlabel('Prediction Accuracy')
ax.set_title('Prediction-Powered CI Width vs. Prediction Accuracy')
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
