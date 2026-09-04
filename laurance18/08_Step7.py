import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# SECTION: 2D Diffusion

# Variables
nx = 31
ny = 31
nt = 17
nu = .05
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
sigma = .25
dt = sigma * dx * dy / nu

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)

u = np.ones((ny, nx)) # BCs already applied (everywhere is 1) 
                      # wouldnt be applied if we initiated arrays with something other than np.ones
un = np.copy(u) # Copy of u


# ICs
u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2

# Iterate
for n in range(nt + 1): # Loop across number of time steps
    un = u.copy()

    u[1:-1, 1:-1] = (un[1:-1,1:-1] + 
                    nu * dt / dx**2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +
                    nu * dt / dy**2 * (un[2:,1: -1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1]))
    
    u[0, :] = 1
    u[-1, :] = 1 # BCs being applied (u = v = 1 at x = 0,2 and y=0,2)
    u[:, 0] = 1
    u[:, -1] = 1


# Plot
fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.add_subplot(111, projection='3d')                      
X, Y = np.meshgrid(x, y)                            
surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
plt.show()
