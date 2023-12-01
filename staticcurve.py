import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,100)
for i in range(10):
    y = np.exp(i*x)
    plt.plot(x,y)
    plt.show()