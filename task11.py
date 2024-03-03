import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from utils import read_file, filepath

def filepath_(filename):
  return filepath('data/task11/', filename)

data = read_file(filepath_('150cy1s'))

min_data, max_data = int(min(data)), int(max(data))
bins = np.arange(min_data, max_data + 2) - 0.5 
counts, bins = np.histogram(data, bins=bins)
yerr = np.sqrt(counts)

plt.stairs(counts, bins, label='Histogram')

m = 114 / 30
ns = np.arange(min_data, max_data + 1)
pois = 150 * poisson.pmf(ns, m)

plt.scatter(ns, pois, color='green', label='Poisson PMF')

plt.errorbar(ns, counts, yerr=yerr, fmt='o', ecolor='red', capsize=3)

plt.xlabel('Counts')
plt.ylabel('Frequency')
plt.title('Comparison between Histogram and Poisson Distribution')
plt.legend()

plt.show()
