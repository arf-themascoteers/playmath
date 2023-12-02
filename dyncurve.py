import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
matplotlib.use("TkAgg")

fig, ax = plt.subplots()
x = np.linspace(0, 1, 100)
line, = ax.plot(x, np.exp(0 * x))

def update(i):
    y = np.exp(i * x)
    line.set_ydata(y)
    ax.set_title(f'Iteration {i}')
    ax.set_ylim(0, np.max(y))  # Update y-axis limits
    return line,

num_iterations = 10
animation = FuncAnimation(fig, update, frames=range(num_iterations), interval=500)

plt.show()