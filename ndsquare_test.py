import os
import matplotlib.pyplot as plt
import numpy as np
from utils import fetch_values_from_folder, nd2, nd2_err, dead_time_correction
from data_processing.sihun_data_processing import x_s, n_s, nd2_s
from data_processing.sam_data_processing import x_sam, nd2_sam, nd2_sam_err_
from data_processing.task16_data_processing import x_t16, nd2_t16, nd2_t16_err
from simulation_data_processing import keys_, nd2_simu, nd2_simu_err

x, n, n_raw = fetch_values_from_folder('data/ndsquare_data/')
x_2, n_2, n_2_raw = fetch_values_from_folder('data/ndsquare/')

x_2 = (np.array(x_2)) / 100
nd2_2 = nd2(n_2, x_2)

x = (np.array(x)) / 100 
n_corrected = dead_time_correction(n, 1.32813e-6)
nd2_corrected = nd2(n_corrected, x)
nd2_ = nd2(n, x)
n_err = nd2_err(x, n_corrected)
print(x_s[1], nd2_s[1])
# plt.errorbar(x, nd2_corrected, yerr=n_err, fmt='o', label='dead time corrected data points')
plt.scatter(x_2, nd2_2, label='second dataset')
plt.scatter(x_s, nd2_s + 0.3, label='sihun data', c='green')
plt.scatter(x_sam, nd2_sam, label='sam data', c='yellow')
plt.scatter(x_t16, nd2_t16 + 1.1, label='task16')
# plt.errorbar(keys_, nd2_simu, yerr = nd2_simu_err, fmt='o', label='simulation') 
plt.scatter(x, nd2_, c='red', label ='raw data points')
plt.legend()
plt.xlabel('distance(m)')
plt.ylabel('nd2')
plt.title('ndsquare') 
plt.show()