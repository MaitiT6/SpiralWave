import numpy as np
import matplotlib.pyplot as plt

# Data for sigma, mueps, and frequency
sigma = [
    0.1, 0.15, 0.2, 0.25, 0.3, 
    0.35, 0.4, 0.45, 0.5, 0.55, 
    0.6, 0.65, 0.7, 0.75, 0.8
]

mueps = [
    -0.373, -0.332, -0.296, -0.265, -0.238, 
    -0.216, -0.198, -0.179, -0.164, -0.148, 
    -0.131, -0.112, -0.089, -0.075, -0.060
]

freq = [
    0.0775, 0.078, 0.0765, 0.0745, 0.0715, 
    0.0675, 0.063, 0.0590, 0.054, 0.0490, 
    0.0445, 0.041, 0.0375, 0.031, 0.0285
]

# Create figure and axis
fig, ax1 = plt.subplots()

# Plot mueps (var2) on the left y-axis
ax1.set_xlabel('Frequency $(\\nu_s)$', fontdict={'color': 'black', 'size': 20})
ax1.set_ylabel('$\epsilon\mu_1$', fontdict={'color': 'green', 'size': 20})
ax1.scatter(freq, mueps, color='green', marker='^', label='Var2', s=150, alpha=0.8, zorder=1)
ax1.tick_params(axis='y', labelcolor='green', width=2, length=8, labelsize=15)
ax1.tick_params(axis='x', labelcolor='black', width=2, length=8, labelsize=15)

# Create a second y-axis for sigma (var3)
ax2 = ax1.twinx()
ax2.set_ylabel('$\sigma$', fontdict={'color': 'blue', 'size': 20})
ax2.scatter(freq, sigma, color='blue', marker='o', label='Var3', s=150, alpha=0.6, zorder=1)
ax2.tick_params(axis='y', labelcolor='blue', width=2, length=8, labelsize=15)

# Customize x-ticks and figure size
plt.xticks(np.linspace(0.025, 0.08, num=6), fontsize=15)

# Customize the appearance of the plot's axes
plt.gca().spines['top'].set_linewidth(2.5)
plt.gca().spines['right'].set_linewidth(2.5)
plt.gca().spines['bottom'].set_linewidth(2.5)
plt.gca().spines['left'].set_linewidth(2.5)

# Set figure size
plt.gcf().set_size_inches(8, 6)

# Save the figure with tight layout
plt.savefig("frequency.pdf", bbox_inches='tight')

# Display the plot
plt.show()

