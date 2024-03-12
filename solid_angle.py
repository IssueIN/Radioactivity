from scipy.integrate import quad
from scipy.special import j1
from math import exp
import numpy as np
import matplotlib.pyplot as plt

def integrand(k, Rs, Rd, z):
    u = k * Rs
    Z = z / Rs
    F = Rd / Rs
    return  4 * np.pi *F * u **(-1) * np.exp(- u * Z) * j1(u) * j1(u * F)

def solid_angle(z_values, Rs = 9.53e-3, Rd = 5e-3):
    solid_angle = [quad(lambda k: integrand(k, Rs, Rd, z), 0, np.inf)[0] for z in z_values]
    solid_angle_err = [quad(lambda k: integrand(k, Rs, Rd, z), 0, np.inf)[1] for z in z_values]
    return solid_angle, solid_angle_err


def solid_angle_numerical(d, a=9.53e-3, s=5e-3):
    d = np.array(d)
    alpha = (a/d)**2
    beta = (s/d)**2
    F1 = (5/16)*(beta/(1+beta)**(7/2)) - (35/16)*(beta**2/(1+beta)**(9/2))
    F2 = (35/128)*(beta/(1+beta)**(9/2)) - (315/256)*(beta**2/(1+beta)**(11/2)) + (1155/1024)*(beta**3/(1+beta)**(13/2))
    omega = 2 * np.pi * (1 - (1/(1+beta)**(1/2) - (3/8) * (alpha*beta)/(1+beta)**(5/2) + alpha**2*F1 - alpha**3*F2))
    return omega

z_values = np.linspace(1e-3, 1.0, 100)  # Range of z values as an example

def monte_carlo_integration(z_values, Rs=9.53e-3, Rd=5e-3, num_samples=1000000):
    mc_estimates = []
    for z in z_values:
        # Generate samples: since the integral is from 0 to infinity,
        # we use an exponential distribution for importance sampling.
        samples = np.random.exponential(scale=1/Rs, size=num_samples)
        # Evaluate the integrand at each sample point.
        integrand_values = integrand(samples, Rs, Rd, z)
        # Compute the Monte Carlo estimate for this z-value.
        mc_estimate = integrand_values.mean()
        mc_estimates.append(mc_estimate)
    return mc_estimates


# Rs = 0.5e-3
# Rd = 9.53e-3
# z_values = np.linspace(1e-3, 1.0, int(1e4))

# results = [quad(lambda k: integrand(k, Rs, Rd, z), 0, np.inf)[0] for z in z_values]
# errors = [quad(lambda k: integrand(k, Rs, Rd, z), 0, np.inf)[1] for z in z_values]


# for z, result in zip(z_values, results):
#     print(f"The integral for z={z} evaluates to: {result}")

# for z, error in zip(z_values, errors):
#     print(f"Estimated error for z={z}: {error}")