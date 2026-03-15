import numpy as np
from matplotlib import pyplot

# SECTION: Wave Propogation Equation

length = 2 # length to discretize
nx = 51 # number of nodes
nt = 30 # number of time steps
dx = length / (nx-1) # spatial spacing
dt = 0.015  # time spacing

# Wave definition
u = np.ones(nx)
u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s

# Plot setup for timestep animation
x = np.linspace(0, length, nx)
pyplot.ion()
fig, ax = pyplot.subplots()
line, = ax.plot(x, u, lw=2)
ax.set_xlim(0, length)
ax.set_ylim(0.9, 2.1)

# Loops
for n in range (nt):
  un = np.copy(u) # since loop below will iterate for the same timestep
  for i in range (1, nx): # make a copy of the array so it doesnt change
    # u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
    u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1]) # This time, it is nonlinear

  line.set_ydata(u)
  pyplot.pause(0.08) # Animation

pyplot.ioff()
pyplot.show()