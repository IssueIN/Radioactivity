import matplotlib.pyplot as plt
from utils import fetch_values_from_folder, linear_fit
import numpy as np

x, y, y_ = fetch_values_from_folder('data/task18/3.8')
y_exp = np.log(y)
x_err = np.ones(len(x)) * 0.01
y_err = np.sqrt(y) / y
plt.errorbar(x, y_exp, xerr=x_err, yerr=y_err, fmt='o', capsize=2, capthick=1.5, markersize=3, label='data points')

bds = [6, 6, 13, 13] #end of 1, start of 2, end of 2, start of 3
params, cov, x_fit, y_fit = linear_fit(x, y_exp, y_err, bds)
[plt.plot(x_fit[i], y_fit[i], label=f'Line {i+1} Fit') for i in range(3)]

[print(f'Line {i+1}: y = {params[i][0]}x + {params[i][1]}') for i in range(3)]

  
plt.xlabel('Distance (mm)')
plt.ylabel('Log Counts')
plt.title('Absorption Curve of Aluminium')
plt.legend()
plt.grid(True)
plt.show()
