import numpy as np
from scipy.optimize import curve_fit

def exp_decay(x, N0, miu):
    return N0 * np.exp(-miu * x)

def fit_exp_decay(x_data, y_data, initial_guess):
    popt, pcov = curve_fit(exp_decay, x_data, y_data, p0=initial_guess)
    return popt, pcov

# x_data = np.array([1, 2, 3, 4, 5])
# y_data = np.array([8, 4, 2, 1, 0.5])

# initial_guess = (10, 0.3)  

# # Now you can call the fit function
# popt, pcov = fit_exp_decay(x_data, y_data, initial_guess)

# # popt contains the best fit values for N0 and miu
# N0_opt, miu_opt = popt
# print(f"Optimal values are N0 = {N0_opt} and miu = {miu_opt}")
