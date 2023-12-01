import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = np.linspace(0, 1, 100)
line, = ax.plot(x, np.exp(0 * x))

def update(i):
    y = np.exp(i * x)
    line.set_ydata(y)
    ax.set_title(f'Iteration {i}')
    return line,

num_iterations = 10
animation = FuncAnimation(fig, update, frames=range(num_iterations), interval=500)

plt.show()