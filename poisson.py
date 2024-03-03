import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

m = 150
ns = np.arange(1, 221)
prob_sci = poisson.pmf(ns, m)

plt.scatter(ns, prob_sci)
plt.show()