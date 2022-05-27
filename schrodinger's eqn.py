# Work in progress

# Aim: To make a program that solves schrodinger's eqn for a given potential and initial conditions and plots it in matplotlib

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import special
from tkinter import *

pi = np.pi
e = np.exp

a = 2*pi*1.0

# tkinter gui to ask potential functions

top = Tk()
top.geometry("150x100")

L1 = Label(top, text="V(x) = ")
L1.pack(side=LEFT)
E1 = Entry(top, bd=5)
E1.pack(side=RIGHT)

top.mainloop()

# putting that potential function in the ode and solving it

# displaying the function as a graph in matplotlib

# evaluating the wave function at these values

# xvals = np.linspace(-1000, a, 1000)

# A = (2/a)**(1/2)  # Normalization constant


# def psi(n, x):  # sourcery skip: inline-immediately-returned-variable
#     wf = (1/(pi))**(1/4)*(1/(np.sqrt(2 ^ n*math.factorial(n)))) * \
#         (special.hermite(n, monic=False))*np.exp(-x**2/2)
#     return wf


# yvals1 = psi(1, xvals)
# yvals2 = psi(2, xvals)
# yvals3 = psi(3, xvals)

# plt.plot(xvals, yvals1, linewidth=2.0, label="n = 1")
# plt.plot(xvals, yvals2, linewidth=1.0, label="n = 2")
# plt.plot(xvals, yvals3, linewidth=0.5, label="n = 3")
# plt.title("Wave function for infinite square well")
# plt.xlabel("x values")
# plt.ylabel("Wave function $\psi(x)$")
# plt.grid()
# plt.legend()

# plt.show()
