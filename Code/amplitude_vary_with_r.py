import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, FancyArrowPatch

# Load the simulation data
data = np.load('final_values.npz')
u = data['final_u']
v = data['final_v']

# Create the plot with the simulation data
plt.imshow(u, cmap='Paired', extent=[0, 200, 0, 200], origin='lower')

# Add colorbar with custom tick size
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=15)

# Set x and y ticks with custom font size
plt.xticks(np.linspace(0, 200, num=3), fontsize=15)
plt.yticks(np.linspace(0, 200, num=3), fontsize=15)

# Define ellipses to be drawn on the plot
ellipses = [
    {'center': (178, 97), 'width': 90, 'height': 30, 'angle': 85, 
     'color': 'white', 'linewidth': 2, 'linestyle': '--'}  # First ellipse
]

# Add ellipses to the plot
for ellipse_params in ellipses:
    ellipse = Ellipse(
        ellipse_params['center'], 
        ellipse_params['width'], 
        ellipse_params['height'], 
        angle=ellipse_params['angle'],
        color=ellipse_params['color'], 
        fill=False,  # Non-filled ellipses
        linewidth=ellipse_params['linewidth'],
        linestyle=ellipse_params['linestyle']  # Set the linestyle here
    )
    plt.gca().add_patch(ellipse)

# Define circles to be drawn on the plot
circles = [
    {'center': (90, 113), 'radius': 40, 'color': 'white', 
     'linewidth': 2, 'linestyle': '--'}  # First circle
]

# Add circles to the plot
for circle_params in circles:
    circle = Circle(
        circle_params['center'], 
        circle_params['radius'], 
        color=circle_params['color'], 
        fill=False,  # Non-filled circles
        linewidth=circle_params['linewidth'],
        linestyle=circle_params['linestyle']  # Set the linestyle here
    )
    plt.gca().add_patch(circle)

# Define arrows to be drawn on the plot
arrows = [
    {'posA': (60, 150), 'posB': (80, 175), 'color': 'black', 'linewidth': 3, 'radius': -0.1}, 
    {'posA': (90, 178), 'posB': (125, 185), 'color': 'black', 'linewidth': 3, 'radius': -0.15}, 
    {'posA': (135, 182), 'posB': (170, 160), 'color': 'black', 'linewidth': 3, 'radius': -0.2}, 
    {'posA': (95, 88), 'posB': (95, 112), 'color': 'blue', 'linewidth': 3, 'radius': 0}, 
    {'posA': (191, 101), 'posB': (164, 101), 'color': 'blue', 'linewidth': 3, 'radius': 0}
]

# Add arrows to the plot
for arrow_params in arrows:
    arrow = FancyArrowPatch(
        posA=arrow_params['posA'], 
        posB=arrow_params['posB'], 
        connectionstyle=f"arc3,rad={arrow_params['radius']}",  # Curved arrow with specified curvature
        color=arrow_params['color'], 
        linewidth=arrow_params['linewidth'], 
        arrowstyle="->",  # Style of the arrowhead
        mutation_scale=15  # Size of the arrowhead
    )
    plt.gca().add_patch(arrow)

# Add text annotations
plt.text(110, 194, 'r increases', color='black', fontsize=15, ha='center', va='center')
plt.text(95, 114, 'A', color='blue', fontsize=20, ha='center', va='center', fontweight='bold')
plt.text(155, 101, 'B', color='blue', fontsize=20, ha='center', va='center', fontweight='bold')

# Save the plot as a PDF
plt.savefig('contour.pdf', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()

