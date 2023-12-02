import matplotlib.pyplot as plt
import numpy as np

signal = np.random.rand(1000)
sampling_rate = 1000
spec_values, _, _, _ = plt.specgram(signal, Fs=sampling_rate)
plt.show()
print(spec_values.shape)
