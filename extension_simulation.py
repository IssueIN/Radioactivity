import numpy as np
import matplotlib.pyplot as plt
from utils import simu_int_2, read_files_from_folder, simu_data_processing

simu_int = simu_int_2

data = read_files_from_folder('data/simulation3')
means, std_devs, counts = simu_data_processing(data)

counts_normalized = {key: counts[key] / simu_int[key] for key in counts if key in simu_int}
keys = list(counts_normalized.keys())

nd2 = [counts_normalized[key] * key**2 for key in keys]
nd2_err = [np.sqrt(counts[key]) / simu_int[key] * key**2  for key in keys]

plt.figure(figsize=(10, 6))  
plt.errorbar(keys, nd2, yerr = nd2_err, fmt='o')  

plt.xlabel('distance(mm)')  
plt.ylabel('nd2')  
#plt.xscale('log')
plt.title('simulation') 
# plt.ylim(-1, max(counts_normalized.values()) + 1)
plt.show()
