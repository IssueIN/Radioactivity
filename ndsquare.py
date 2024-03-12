import matplotlib.pyplot as plt
import numpy as np
from utils import fetch_values_nd2, nd2, nd2_err, dead_time_correction

x, n, n_tot, dt = fetch_values_nd2('data/ndsquare_data/')
x = (np.array(x)) / 100 
nd2_ = nd2(n_tot, x, dt)
nd2_err_ = nd2_err(x, n_tot, dt)
plt.errorbar(x, nd2_, yerr=nd2_err_, fmt='o', label ='raw data points')
plt.legend()
plt.xlabel('distance(m)')
plt.ylabel('nd2')
plt.title('ndsquare') 
plt.show()