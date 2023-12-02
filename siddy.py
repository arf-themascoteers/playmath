import pandas as pd
import matplotlib.pyplot as plt
from pysptools.distance import SID


data = pd.read_csv("dataset_min.csv").to_numpy()
plt.plot(data[0])
plt.plot(data[1])
plt.show()

x = SID(data[0:10], data[10:20])
print(x)


