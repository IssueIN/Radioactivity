from utils import fetch_values_from_folder, nd2, nd2_err
import numpy as np

folder_path = 'data/borrowed_data/sam/'

x_sam, n_sam, n_sam_raw = fetch_values_from_folder(folder_path)
x_sam = (np.array(x_sam)) / 100
nd2_sam = nd2(n_sam, x_sam)
nd2_sam_err_ = nd2_err(x_sam, n_sam)