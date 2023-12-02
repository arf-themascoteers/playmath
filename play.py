import numpy as np
import matplotlib.pyplot as plt

def quadratic_function(x):
    return x ** 2

x_values = np.linspace(0, 10, 100)
y_values = quadratic_function(x_values)

highlight_x = 3
highlight_y = quadratic_function(highlight_x)

plt.plot(x_values, y_values, label='y = x^2')
plt.scatter(highlight_x, highlight_y, color='red', label='Point (3, 9)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = x^2 with Highlighted Point')

plt.legend()

plt.text(highlight_x, highlight_y, f'({highlight_x}, {highlight_y})', fontsize=10, verticalalignment='bottom')

plt.show()
