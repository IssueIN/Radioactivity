import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from utils import read_file, filepath

def filepath_(filename):
    return filepath('data/task12/task12-', filename)

def gaussian(m, ns):
    sigma = np.sqrt(m)
    gaussian = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(ns - m)**2/(2 * sigma**2)) 
    return gaussian

data = read_file(filepath_('250cy1s'))

bins = 20
counts, bin_edges = np.histogram(data, bins=bins)
bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
yerr = np.sqrt(counts)  # Poisson error for each bin

plt.stairs(counts, bin_edges, label='Histogram')

m = 8820 / 60
ns = bin_centers #np.linspace(min(bin_edges), max(bin_edges), len(counts))
# pois = 200 * poisson.pmf(ns, m)

plt.scatter(ns, 900 * gaussian(m, ns), color='green', label='Gaussian')

plt.errorbar(bin_centers, counts, yerr=yerr, fmt='o', ecolor='red', capsize=3, label='Error')

plt.xlabel('Counts')
plt.ylabel('Frequency')
plt.title('Comparison between Histogram and Gaussian Distribution')
plt.legend()

plt.show()

plt.show()
