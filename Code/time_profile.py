import matplotlib.pyplot as plt
import numpy as np
import os

directory = '/data/'
data_file = os.path.join(directory, '100_100.txt')
data = np.loadtxt(data_file, skiprows=1)
x = data[:, 0]
u = data[:, 1]
v = data[:, 2]

plt.plot(x,u,lw=3,c='darkgreen')
plt.xlabel('Time(a.u.)', fontdict={'color': 'black', 'size': 20}, labelpad=10)
plt.ylabel('Concentration of $U$', fontdict={'color': 'black', 'size': 20}, labelpad=5)
plt.xticks(np.linspace(600, 760, num=5), fontsize=20)
plt.yticks(np.linspace(0,5, num=6), fontsize=20)
plt.tick_params(axis='both', width=2, length=8)
plt.gca().spines['top'].set_linewidth(3)
plt.gca().spines['right'].set_linewidth(3)
plt.gca().spines['bottom'].set_linewidth(3)
plt.gca().spines['left'].set_linewidth(3)
plt.xlim(600,760)
plt.savefig("oscillation.pdf", bbox_inches='tight')
plt.show()
