import matplotlib.pyplot as plt
import numpy as np

def read_first_column(filename):
    data = [] 
    with open(filename, 'r') as file:
        next(file) 
        for line in file:
            energy = float(line.split(',')[0])
            data.append(energy)
    return data

def plot_histogram(data, title='Histogram', xlabel='Energy deposited', ylabel='Frequency'):
    counts, bins = np.histogram(data, bins=50)
    plt.stairs(counts, bins)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()

file_path = 'data/data_task_8_2.txt'
data = read_first_column(file_path)
plot_histogram(data)

