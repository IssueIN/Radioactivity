import matplotlib.pyplot as plt
import numpy as np
x = 15*np.arange(0, 7)
y = [1129664.000, 11854.000, 2967.000, 1222.000, 687.000, 422.000, 287.000]

plt.scatter(x, y)
plt.xlabel('distance(cm)')
plt.ylabel('Counts')
plt.title('preliminary measurement')
plt.show()