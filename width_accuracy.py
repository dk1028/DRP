# Remake the bar graph in reverse order (from 60% to 100%)

# Reverse the lists
labels_reversed = labels[::-1]
ci_widths_reversed = ci_widths[::-1]

# Create reversed bar plot
x = np.arange(len(labels_reversed))
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x, ci_widths_reversed, align='center')
ax.set_xticks(x)
ax.set_xticklabels(labels_reversed)
ax.set_ylabel('CI Width')
ax.set_xlabel('Prediction Accuracy')
ax.set_title('Prediction-Powered CI Width vs. Prediction Accuracy (Reversed Order)')
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
