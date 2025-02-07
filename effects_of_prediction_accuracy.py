import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
n = 100  # number of labeled data points
N = 10000  # number of unlabeled data points
true_mean = 5  # true mean of the distribution
alpha = 0.05  # significance level

# Simulate true outcomes
Y_labeled = np.random.normal(true_mean, 1, n)
X_unlabeled = np.random.normal(true_mean, 1, N)


# Function to simulate predictions with a given accuracy
def generate_predictions(true_values, accuracy):
    noise_std = (1 - accuracy) * 2  # More noise for lower accuracy
    predictions = true_values + np.random.normal(0, noise_std, len(true_values))
    return predictions


# Function to calculate prediction-powered confidence interval
def prediction_powered_ci(Y_labeled, f_X_labeled, f_X_unlabeled, n, N, alpha):
    delta = np.mean(f_X_labeled - Y_labeled)
    theta_f = np.mean(f_X_unlabeled)
    theta_pp = theta_f - delta

    var_f_Y = np.var(f_X_labeled - Y_labeled, ddof=1) / n
    var_f = np.var(f_X_unlabeled, ddof=1) / N
    se = np.sqrt(var_f_Y + var_f)

    ci_lower = theta_pp - 1.96 * se
    ci_upper = theta_pp + 1.96 * se

    return theta_pp, (ci_lower, ci_upper)


# Accuracy levels to test
accuracies = [1.0, 0.9, 0.8, 0.7, 0.6]
ci_results = []

for acc in accuracies:
    f_X_labeled = generate_predictions(Y_labeled, acc)
    f_X_unlabeled = generate_predictions(X_unlabeled, acc)

    theta_pp, ci = prediction_powered_ci(Y_labeled, f_X_labeled, f_X_unlabeled, n, N, alpha)
    ci_results.append((acc, ci, theta_pp))

# Plotting the results
plt.figure(figsize=(10, 6))
for acc, ci, theta_pp in ci_results:
    plt.errorbar(acc, theta_pp, yerr=[[theta_pp - ci[0]], [ci[1] - theta_pp]], fmt='o',
                 label=f'Accuracy {acc * 100:.0f}%')

plt.axhline(true_mean, color='r', linestyle='--', label='True Mean')
plt.xlabel('Prediction Accuracy')
plt.ylabel('Estimated Mean with 95% CI')
plt.title('Effect of Prediction Accuracy on Prediction-Powered Inference')
plt.legend()
plt.grid(True)
plt.show()
