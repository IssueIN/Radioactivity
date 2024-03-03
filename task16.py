import os
import matplotlib.pyplot as plt
import numpy as np
from utils import fetch_values_from_folder

def intensity(n, d, t=1):
    n = np.array(n)
    d = np.array(d)
    return n / t * d**2

def su_calc(x,n):
    stdu = np.sqrt((((x**4)/400)*0.000001)+((4*(x**2)*(n**2)/400)*n))
    return stdu

def error(d, n):
    n = np.array(n)
    d = np.array(d)
    error = np.sqrt(d ** 4 * n  + (2 * n * d)**2 * (0.003) ** 2)
    return error

x, y, y_raw = fetch_values_from_folder('data/task16')
x = np.array(x) / 100
intensity_ = intensity(y, x)
y_err = error(x, y)

plt.errorbar(x, intensity_, yerr=y_err, fmt='o')
plt.xlabel('distance(m)')
plt.ylabel('intensity')
plt.title('task16') 
plt.show()