import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def filepath(folderpath, filename):
  return folderpath + filename

def read_file(filename):
    data = [] 
    with open(filename, 'r') as file:
        next(file) 
        for line in file:
            energy = float(line.split(',')[0])
            data.append(energy)
    return data

def fetch_values_from_folder(directory):
  x = [] 
  y = [] 
  raw_y = []

  for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
      try:
        with open(file_path, 'r') as file:
          values = [float(line.strip()) for line in file.readlines()]
                    
          if values:
            mean_value = np.mean(values)
            y.append(mean_value)
            x.append(float(filename))
            raw_y.append(values)
      except ValueError as ve:
        print(f"Could not convert the content of {filename} to a float: {ve}")
      except Exception as e:
        print(f"An error occurred while processing {filename}: {e}")
  return x, y, raw_y

def scatter_plot(x, y, xlabel='distance(cm)', ylabel='Counts', title='preliminary measurement'):
  plt.scatter(x, y)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)
  plt.show()

def linear_func(x, a, b):
    return a * x + b

def linear_fit(x, y, y_err, bds):
  x_groups = [x[:bds[0]], x[bds[1]:bds[2]], x[bds[3]:]]
  y_groups = [y[:bds[0]], y[bds[1]:bds[2]], y[bds[3]:]]
  y_err_groups = [y_err[:bds[0]], y_err[bds[1]:bds[2]], y_err[bds[3]:]]

  fit_params = []
  fit_cov = []
  x_fit = []
  y_fit = []
  for i in range(3):
    params, cov = curve_fit(linear_func, x_groups[i], y_groups[i], sigma=y_err_groups[i])
    fit_params.append(params)
    fit_cov.append(cov)
    x_fit.append(np.linspace(min(x_groups[i])-0.2, max(x_groups[i])+0.2, 100))
    y_fit.append(linear_func(x_fit[i], *params))
  return fit_params, fit_cov, x_fit, y_fit

