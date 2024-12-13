import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, uniform


# A)
x = [82, 106, 120, 68, 83, 89, 130, 92, 99, 89]
sigma = 10
mu = 90
samples = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(samples, norm.pdf(samples, mu, sigma))
plt.grid(True)
plt.show()

# B)
x1 = 82
ver_x = np.exp(-((x1 - mu)**2) / (2 * sigma**2)) * (2* np.pi * sigma**2)**-0.5

print(f'b) Scipy results: {norm.pdf(x1, mu, sigma)} My results: {ver_x}')

# C)

total_ver = np.prod(norm.pdf(x, mu, sigma))
print(f'c) {total_ver}')

# D)
mu = 90
sigma = 10
mu_apriori = norm.pdf(mu, 100, 50)
sigma_apriori = uniform.pdf(sigma, 1, 70)

probab_apriori = mu_apriori * sigma_apriori

print(f'd) {probab_apriori}')

# E)
print(f'e) {probab_apriori * total_ver}')

# F)
mus = [70, 75, 80, 85, 90, 95, 100]
sigmas = [5, 10, 15, 20]

observations = []
for mu in mus:
    for sigma in sigmas:
        observations.append((probab_apriori * total_ver * np.prod(norm.pdf(x, mu, sigma)), mu, sigma))

best_results = max(observations, key=lambda x: x[0])

print(f'f) sigma: {best_results[1]}, mu: {best_results[2]}')