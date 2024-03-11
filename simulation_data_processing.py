import numpy as np
import matplotlib.pyplot as plt
from utils import simu_int_2, read_files_from_folder, simu_data_processing
norm_factor = 3

simu_int = simu_int_2

data = read_files_from_folder('data/simulation3')
means, std_devs, counts = simu_data_processing(data)

counts_normalized = {key: counts[key] / simu_int[key] for key in counts if key in simu_int}
keys = list(counts_normalized.keys())

nd2_simu = np.array([counts_normalized[key] * key**2 for key in keys]) * norm_factor
nd2_simu_err = np.array([np.sqrt(counts[key]) / simu_int[key] * key**2  for key in keys]) * norm_factor
keys_ = np.array(keys) / 1000
