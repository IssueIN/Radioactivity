import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils import nd2, nd2_err
file_path = 'data/borrowed_data/pureData.xlsx'

def read_data(file_path):
    df = pd.read_excel(file_path)
    selected_data = df.iloc[:, [1, 2]]  
    selected_data_clean = selected_data.dropna()
    x = selected_data_clean.iloc[:,0].values.tolist()
    n = selected_data_clean.iloc[:,1].values.tolist()
    return x, n


x_s, n_s = read_data(file_path)
n_s = np.array(n_s) / 20
nd2_s = nd2(n_s, x_s)
nd2_s_err = nd2_err(x_s, n_s)
