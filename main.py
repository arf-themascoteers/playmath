import numpy as np
import matplotlib.pyplot as plt

x  = np.random.rand(3, 5)
for i in x:
    plt.plot(i)

plt.show()


common_variance = 1.0
mean = np.zeros(5)
covariance_matrix = common_variance * np.eye(5)
random_array_isotropic = np.random.multivariate_normal(mean, covariance_matrix, size=3)
print(random_array_isotropic)

for i in random_array_isotropic:
    plt.plot(i)

plt.show()
#
