import os
import matplotlib.pyplot as plt
import numpy as np
from utils import fetch_values_from_folder, nd2, nd2_err, dead_time_correction
from sihun_data_processing import x_s, n_s, nd2_s
from simulation_data_processing import keys_, nd2_simu, nd2_simu_err

x, n, n_raw = fetch_values_from_folder('data/ndsquared3/')
x = (np.array(x)) / 100 
n_corrected = dead_time_correction(n, 1.5e-6)
nd2_corrected = nd2(n_corrected, x)
nd2_ = nd2(n, x)
n_err = nd2_err(x, n_corrected)

plt.errorbar(x, nd2_corrected, yerr=n_err, fmt='o', label='dead time corrected data points')
plt.scatter(x_s, nd2_s, label='sihun data', c='green')
plt.scatter(x, nd2_, c='red', label ='raw data points')
plt.errorbar(keys_, nd2_simu, yerr = nd2_simu_err, fmt='o', label='simulation') 
plt.yscale('log')
plt.legend()
plt.xlabel('distance(m)')
plt.ylabel('nd2')
plt.title('ndsquare') 
plt.show()