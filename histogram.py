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
    plt.hist(data, bins=10)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

file_path = 'data/task11/200cy1s'
data = read_first_column(file_path)
plot_histogram(data)
plt.show()

