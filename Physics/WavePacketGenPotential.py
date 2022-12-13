import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Set up the potential
def V(x):
    return 0.5 * (1-(x)**2)**2

# Set up the initial wave function
def psi_0(x):
    return np.exp(-x**2 / 2)

# Set up the time-evolution operator
def U(t, x):
    return np.exp(-1j * V(x) * t / hbar)

# Set up the grid
x_min = -5
x_max = 5
N = 1000
dx = (x_max - x_min) / (N - 1)
x = np.linspace(x_min, x_max, N)

# Set up the animation
fig = plt.figure()

# Set up the axes
ax = plt.axes(xlim=(x_min, x_max), ylim=(-1, 1))
line, = ax.plot([], [], lw=2)

# Set up the time variable
hbar = 1
t_min = 0
t_max = 10
dt = 0.01

# Set up the initial wave function
psi = psi_0(x)

# This function updates the plot
def update(t):
    global psi
    psi = U(t, x) * psi
    line.set_data(x, psi)
    return line

# This function is called to create the animation
anim = animation.FuncAnimation(fig, update, frames=np.arange(t_min, t_max, dt), interval=10)

# Show the animation
plt.show()
