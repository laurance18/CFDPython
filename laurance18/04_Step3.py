import numpy as np
from matplotlib import pyplot

# SECTION: 1D Diffusion Equation

length = 2 # length to discretize
nx = 51 # number of nodes
nt = 30 # number of time steps
dx = length / (nx-1) # spatial spacing
nu = 1 # viscosity
sigma = 0.2 # Courant number, keep ideally between 0 and 1

def CFL(sigma, nu, dx):
  return float(sigma * dx**2 / nu) # Different formula!

u = np.ones(nx)
u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s

dt = CFL(sigma, nu, dx)
print(f"dt: {dt}")

# Plot setup for timestep animation
x = np.linspace(0, length, nx)
pyplot.ion()
fig, ax = pyplot.subplots()
line, = ax.plot(x, u, lw=2)
ax.set_xlim(0, length)
ax.set_ylim(0.9, 2.1)

for n in range(nt):  #iterate through time
  un = u.copy() ##copy the existing values of u into un
  for i in range(1, nx - 1):
    u[i] = un[i] + nu * dt / dx**2 * (un[i+1] - 2 * un[i] + un[i-1])

  line.set_ydata(u)
  pyplot.pause(0.08) # Animation

pyplot.ioff()
pyplot.show()