import matplotlib.pyplot as plt
import numpy as np

data = np.load('final_values.npz')
u = data['final_u']
v = data['final_v']

plt.imshow(u, extent=[0, 200, 0, 200],origin='lower')
plt.xticks(np.linspace(0,200, num=3), fontsize=15)
plt.yticks(np.linspace(0,200, num=3), fontsize=15)
cbar = plt.colorbar()
#cbar.set_ticks([5,7,9,11])
cbar.ax.tick_params(labelsize=15)
plt.savefig("Spiral.pdf", bbox_inches='tight')
plt.show()
