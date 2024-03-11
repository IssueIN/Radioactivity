import matplotlib.pyplot as plt
import numpy as np
from utils import read_files_from_folder

def data_process(data):
    data_processed = {}
    for data_ in data:
        for value_str, key_ in data_:
            try:
                value = float(value_str)
                key = -float(key_)
            except ValueError:
                continue
            if key in data_processed:
                data_processed[key].append(value)
            else:
                data_processed[key] = [value]
    return data_processed

def plot_histogram(data, distance, xlabel='Energy deposited', ylabel='Frequency'):
    plt.figure()
    plt.ylim(0, 350)
    plt.hist(data, bins=20)
    plt.title(f'Historgram for {distance} mm')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

folder_path = 'data/'
folder_name = 'simulation2/'
data = read_files_from_folder(folder_path+folder_name)
data_processed = data_process(data)

for key in data_processed:
    plot_histogram(data_processed[key], key)
    plt.savefig(f'output/{folder_name}{key}.png')