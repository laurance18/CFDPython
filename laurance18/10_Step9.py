import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# SECTION: 2D Laplace Equation

## Functions

def plot2D(x, y, p):
    fig = plt.figure(figsize=(11, 7), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, p[:], rstride=1, cstride=1, cmap=cm.viridis,
                    linewidth=0, antialiased=False)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.view_init(30, 225)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')


def laplace2d(p, y, dx, dy, l1norm_target):
    l1norm = 1
    pn = np.empty_like(p)

    while l1norm > l1norm_target:  # no time stepping: iterate to equilibrium
        pn = p.copy()

        # five-point stencil: each point is the weighted average of its neighbours
        p[1:-1, 1:-1] = ((dy**2 * (pn[1:-1, 2:] + pn[1:-1, 0:-2]) +
                          dx**2 * (pn[2:, 1:-1] + pn[0:-2, 1:-1])) /
                         (2 * (dx**2 + dy**2)))

        p[:, 0] = 0        # p = 0 @ x = 0
        p[:, -1] = y       # p = y @ x = 2
        p[0, :] = p[1, :]  # dp/dy = 0 @ y = 0
        p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 1

        l1norm = np.sum(np.abs(p - pn)) / np.sum(np.abs(pn))

    return p


## Variable declarations
nx = 31
ny = 31
dx = 2 / (nx - 1)
dy = 1 / (ny - 1)  # y spans 0..1, so dy is not 2 / (ny - 1)

x = np.linspace(0, 2, nx)
y = np.linspace(0, 1, ny)

## ICs
p = np.zeros((ny, nx))  # p = 0 everywhere to start

## BCs
p[:, 0] = 0        # p = 0 @ x = 0
p[:, -1] = y       # p = y @ x = 2
p[0, :] = p[1, :]  # dp/dy = 0 @ y = 0
p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 1

plot2D(x, y, p)

# Iterate
p = laplace2d(p, y, dx, dy, 1e-4)

# Plot
plot2D(x, y, p)
plt.show()
