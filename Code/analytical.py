import numpy as np
import matplotlib.pyplot as plt

# Function to calculate epsilon * m1
def epsilon_m1(sigma):
    """
    Calculate epsilon * m1 for a given sigma value using the defined formula.
    """
    # Intermediate calculations
    fu = (1 - sigma) / (1 + sigma)
    fv = -1 / ((1 + sigma) ** 2)
    gu = 2 * (1 + sigma)
    gv = -1
    mu = 0.37
    mu0 = -(fu / gv)
    omegaH2 = (1 - sigma) / (1 + sigma)
    
    # Numerator and denominator for epsilon * m1 calculation
    num = omegaH2 + (mu0 * gu) ** 2 + (mu0 * gv) ** 2
    numerator = -0.310 * num
    denominator = mu0 * gu ** 2
    epsilon_m1_value = numerator / denominator
    
    return epsilon_m1_value

# Generate values of sigma in the range 0 < sigma < 0.9
s_values = np.linspace(0, 0.9, 100)
epsilon_m1_values = [epsilon_m1(s) for s in s_values]

# List of specific (sigma, epsilon * m1) points to plot
specific_points = [
    (0.1, -0.373), (0.15, -0.332), (0.2, -0.296), (0.25, -0.265), (0.3, -0.238),
    (0.35, -0.216), (0.4, -0.198), (0.45, -0.179), (0.5, -0.164), (0.55, -0.148),
    (0.6, -0.131), (0.65, -0.112), (0.7, -0.089), (0.75, -0.075), (0.8, -0.060)
]

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the epsilon * m1 curve
plt.plot(s_values, epsilon_m1_values, label=r'$\epsilon \cdot \mu_1$', color='green', linewidth=3)

# Plot specific points (sigma, epsilon * m1) as blue triangles
for sigma, epsilon_m1_value in specific_points:
    plt.scatter(sigma, epsilon_m1_value, color='blue', s=200, zorder=5, marker='^',alpha=0.6)

# Set labels and axis limits
plt.xlabel(r'$\sigma$', fontdict={'color': 'black', 'size': 20}, labelpad=1)
plt.ylabel(r'$\epsilon \cdot \mu_1$', fontdict={'color': 'black', 'size': 20}, labelpad=5)
plt.xlim(0.05, 0.85)
plt.ylim(-0.5, 0.0)

# Customize ticks and axis appearance
plt.xticks(np.linspace(0.2, 0.8, num=4), fontsize=15)
plt.yticks(np.linspace(-0.5, 0.0, num=6), fontsize=15)
plt.tick_params(axis='both', width=2, length=8)
plt.gca().spines['top'].set_linewidth(3)
plt.gca().spines['right'].set_linewidth(3)
plt.gca().spines['bottom'].set_linewidth(3)
plt.gca().spines['left'].set_linewidth(3)

# Save and show the plot
plt.savefig("analytical.pdf", bbox_inches='tight')  # Save with tight layout
plt.show()

