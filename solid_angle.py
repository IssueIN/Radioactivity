from scipy.integrate import quad
from scipy.special import j1
from math import exp
import numpy as np
import matplotlib.pyplot as plt

def integrand(k, Rs, Rd, z):
    u = k * Rs
    Z = z / Rs
    F = Rd / Rs
    return 4* np.pi * u **(-1) * exp(- u * Z) * j1(u) * j1(u * F)

Rs = 0.5e-3
Rd = 9.53e-3
z_values = np.linspace(1e-3, 1.0, int(1e4))

# results = [quad(lambda k: integrand(k, Rs, Rd, z), 0, np.inf)[0] for z in z_values]
# errors = [quad(lambda k: integrand(k, Rs, Rd, z), 0, np.inf)[1] for z in z_values]
results = [quad(lambda k: integrand(k, Rs, Rd, z), np.inf, 0)[0] for z in z_values]
errors = [quad(lambda k: integrand(k, Rs, Rd, z), np.inf, 0)[1] for z in z_values]

plt.scatter(z_values,np.array(results))
plt.show()
# for z, result in zip(z_values, results):
#     print(f"The integral for z={z} evaluates to: {result}")

# for z, error in zip(z_values, errors):
#     print(f"Estimated error for z={z}: {error}")