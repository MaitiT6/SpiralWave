import numpy as np
import matplotlib.pyplot as plt

# Read parameters from external text file
with open('input.txt', 'r') as file:
    exec(file.read())

#Defining parameters
Nx = int(L/dx) # Number of grid points
Nt = int(T/dt)  # Number of time steps
pi = 4.0 * np.arctan(1.0)   # Define pi

# Initial steady state value of the dependent variables
uss = (1+s)
vss = (1+s)**2

# Function to initialize variables with small fluctuations around steady state
def random_init(var, var_ss, var_c, start_x, end_x, start_y, end_y):
    np.random.seed(idum)
    var1 = np.random.rand(end_x - start_x, end_y - start_y)
    var1[var1 <= 0.0] = 0.001
    var2 = np.random.rand(end_x - start_x, end_y - start_y)
    var3 = -4.0 * da * np.log(var1)
    var4 = np.cos(2.0 * np.pi * var2)
    var_rand = np.sqrt(var3) * var4
    var_rand = var_ss + var_rand / var_c

    var[start_x:end_x, start_y:end_y] = var_rand
    return var

# Initialize variables with steady-state values
u = np.full((Nx, Nx), uss)
v = np.full((Nx, Nx), vss)

# Define the sub-region for random initialization
start_x, end_x = 95, 105  # Example values for x-direction
start_y, end_y = 95, 105  # Example values for y-direction

# Apply random initialization to the specified sub-region
u = random_init(u, uss, c1, start_x, end_x, start_y, end_y)
v = random_init(v, vss, c2, start_x, end_x, start_y, end_y)

# Boundary conditions (zero flux)
u[:, 0] = u[:, 1]
u[:, -1] = u[:, -2]
u[0, :] = u[1, :]
u[-1, :] = u[-2, :]

v[:, 0] = v[:, 1]
v[:, -1] = v[:, -2]
v[0, :] = v[1, :]
v[-1, :] = v[-2, :]

# Boundary conditions (periodic)
# u[:, 0] = u[:, -2]
# u[:, -1] = u[:, 1]
# u[0, :] = u[-2, :]
# u[-1, :] = u[1, :]

# v[:, 0] = v[:, -2]
# v[:, -1] = v[:, 1]
# v[0, :] = v[-2, :]
# v[-1, :] = v[1, :]

# Laplacian function using central difference method
def laplacian(u,dx):
    lap = np.zeros_like(u)
    lap[1:-1, 1:-1] = (u[:-2, 1:-1] + u[2:, 1:-1] + u[1:-1, :-2] + u[1:-1, 2:] - 4 * u[1:-1, 1:-1]) / (dx**2)
    return lap
       
    
# Time evolution using Euler's method
for t in range(Nt):
    lap_u = laplacian(u,dx)
    lap_v = laplacian(v,dx)
    
    u += dt * ((D*lap_u) + (((u*u)/v) - u + s))
    v += dt * ((lap_v) + (m*(u**2-v)))
    
# Boundary conditions (zero flux)
    u[:, 0] = u[:, 1]
    u[:, -1] = u[:, -2]
    u[0, :] = u[1, :]
    u[-1, :] = u[-2, :]

    v[:, 0] = v[:, 1]
    v[:, -1] = v[:, -2]
    v[0, :] = v[1, :]
    v[-1, :] = v[-2, :]
    
    # Boundary conditions (periodic)
    # u[:, 0] = u[:, -2]
    # u[:, -1] = u[:, 1]
    # u[0, :] = u[-2, :]
    # u[-1, :] = u[1, :]
    
    # v[:, 0] = v[:, -2]
    # v[:, -1] = v[:, 1]
    # v[0, :] = v[-2, :]
    # v[-1, :] = v[1, :]
       
#saving final value of u and v      
final_u=u.copy()
final_v=v.copy()
np.savez('final_values.npz', final_u=final_u, final_v=final_v)




