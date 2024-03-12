import numpy as np
from utils import fetch_values_from_folder, nd2, nd2_err

x_t16, n_t16, _raw = fetch_values_from_folder('data/task16')
x_t16 = np.array(x_t16) / 100
nd2_t16 = nd2(n_t16, x_t16)
nd2_t16_err = nd2_err(x_t16, n_t16)

# x_t16, n_t16, _raw = fetch_values_from_folder('data/task16_test')
# x_t16 = np.array(x_t16) / 100
# nd2_t16 = nd2(n_t16, x_t16)
# nd2_t16_err = nd2_err(x_t16, n_t16)

