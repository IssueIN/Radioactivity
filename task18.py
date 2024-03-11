import matplotlib.pyplot as plt
from utils import fetch_values_from_folder
import numpy as np

x, y, y_ = fetch_values_from_folder('data/task18/3.8')
x_err = np.ones(len(x)) * 0.01
y_err = np.sqrt(y)
plt.errorbar(x, y, xerr=x_err, yerr=y_err, fmt='o', capsize=2, capthick=1.5, markersize=3)
plt.yscale('log')
plt.xlabel('distance(mm)')
plt.ylabel('Log Counts')
plt.title('task18 - absorption curve of Copper')
plt.show()

