import numpy as np
import matplotlib.pyplot as plt

# Define functions for M1 and M2 calculations
def m1(d, s):
    """
    Calculate M1 given a fixed value of d and s.
    M1 is defined as (1/d) * ((sqrt(2 / (1 + s)) - 1)^2).
    """
    return (1 / d) * ((np.sqrt(2 / (1 + s)) - 1) ** 2)

def m2(s):
    """
    Calculate M2 given s.
    M2 is defined as (1 - s) / (1 + s).
    """
    return (1 - s) / (1 + s)

# Set fixed value for D and range for s
d_fixed = 0.25
s_values = np.linspace(0, 1, 500)

# Calculate M1 and M2 for each s at fixed D
M1_s = m1(d_fixed, s_values)
M2_s = m2(s_values)

# Create a figure for plotting
plt.figure(figsize=(8, 5))

# Fill regions between the curves with different colors
# Region 1: Fill where M1_s > M2_s (Turing curve above Hopf curve)
plt.fill_between(s_values, M2_s, y2=np.max(M2_s), color='lightyellow', alpha=0.3)

# Region 2: Fill where M2_s > M1_s (Hopf curve above Turing curve)
plt.fill_between(s_values, M1_s, M2_s, where=(M2_s > M1_s), color='lightgreen', alpha=0.3)

# Region 3: Fill below Turing curve (M1_s), where M1_s > 0
plt.fill_between(s_values, 0, M1_s, where=(M1_s > 0), color='lightblue', alpha=0.3)

# Plot the curves for Turing and Hopf
plt.plot(s_values, M2_s, c='green', label='Hopf Curve', linewidth=3)
plt.plot(s_values, M1_s, c='blue', label='Turing Curve', linewidth=3)

# Add text annotations to the plot
plt.text(0.6, 0.6, 'Homogeneous Steady State', color='black', fontsize=18, ha='center', va='center')
plt.text(0.3, 0.4, 'Oscillatory', color='black', fontsize=18, ha='center', va='center')
plt.text(0.3, 0.33, 'State', color='black', fontsize=18, ha='center', va='center')
plt.text(0.2, 0.1, 'Turing-Hopf State', color='black', fontsize=18, ha='center', va='center')

# Labels and legend
plt.legend(loc='upper right', fontsize=24, facecolor='white')
plt.xlabel('$\sigma$', fontdict={'color': 'black', 'size': 20}, labelpad=10)
plt.ylabel('$\mu$', fontdict={'color': 'black', 'size': 20}, rotation='horizontal', labelpad=20)

# Tick marks and line widths customization
plt.xticks(np.linspace(0, 1, num=6), fontsize=15)
plt.yticks(np.linspace(0, 1, num=6), fontsize=15)
plt.tick_params(axis='both', width=2, length=8)
plt.gca().spines['top'].set_linewidth(3)
plt.gca().spines['right'].set_linewidth(3)
plt.gca().spines['bottom'].set_linewidth(3)
plt.gca().spines['left'].set_linewidth(3)

# Set the x and y axis limits
plt.xlim(0, 1)
plt.ylim(0, 1)

# Set figure size
plt.gcf().set_size_inches(8, 6)

# Save the plot as a PNG image
plt.savefig("Bifurcation_Curve.png", bbox_inches='tight')

# Display the plot
plt.show()

