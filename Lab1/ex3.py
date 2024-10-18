import matplotlib.pyplot as plt
import numpy as np

regression_file = "regresie.csv"

data = np.genfromtxt(regression_file, delimiter=",")

A = data[:, 0]
b = data[:, 1]

x, residuals, rank, s = np.linalg.lstsq(np.column_stack((A, np.ones((len(A))))), b)

print(x)

samples = np.linspace(-3, 3, 2000)
plt.plot(samples, x[0] * samples + x[1], c='black')
plt.scatter(A, b, marker='.', c='r')
plt.grid(True)
plt.show()