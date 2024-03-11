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

def read_files_from_folder(dir):
  data = []
  for filename in os.listdir(dir):
    temp = []
    file_path = os.path.join(dir, filename)

    if os.path.isfile(file_path):
      try:
        with open(file_path, 'r') as file:
          next(file)
          for line in file:
            columns = line.strip().split(',') 
            temp.append((columns[0], columns[1]))
          data.append(temp)
      except ValueError as ve:
        print(f"Could not convert the content of {filename} to a float: {ve}")
      except Exception as e:
        print(f"An error occurred while processing {filename}: {e}")
  return data

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
    x_fit.append(np.linspace(min(x_groups[i]), max(x_groups[i]), 100))
    y_fit.append(linear_func(x_fit[i], *params))
  return fit_params, fit_cov, x_fit, y_fit

def nd2(n, d, t=1):
    n = np.array(n)
    d = np.array(d)
    return n / t * d**2

def nd2_err(d, n):
    n = np.array(n)
    d = np.array(d)
    error = np.sqrt(d ** 4 * n  + (2 * n * d)**2 * (0.003) ** 2)
    return error

def dead_time_correction(n, dt = 1.8e-6):
  n_ = [n__ / np.exp(-n__*dt) for n__ in n]
  return n_

def simu_data_processing(data):
  aggregated_data = {}
  value_ = {}
  counts = {}

  for data_ in data:
    for value_str, key_ in data_:
      try:
        value = float(value_str) 
        key = - float(key_)
      except ValueError:
        continue  
      if key in aggregated_data:
        aggregated_data[key] += value
        value_[key].append(value)
      else:
        aggregated_data[key] = value
        value_[key] = [value]

  means = {key: aggregated_data[key] / len(value_[key]) for key in aggregated_data}
  std_devs = {key: np.std(value_[key]) for key in aggregated_data}
  counts = {key: len(value_[key]) for key in aggregated_data}
  return means, std_devs, counts

simu_int = {
  400.0: 5000000,
  300.0: 3000000,
  250.0: 2000000,
  200.0: 1000000,
  150.0: 1000000,
  100.0: 500000,
  50.0: 500000,
  40.0: 300000,
  30.0: 200000,
  20.0: 100000
}

simu_int_2 = {
  500.0: 5000000,
  400.0: 5000000,
  300.0: 3000000,
  250.0: 2000000,
  200.0: 1000000,
  150.0: 1000000,
  100.0: 500000,
  80.0: 500000,
  70.0: 500000,
  60.0: 500000,
  50.0: 500000,
  40.0: 300000,
  30.0: 200000,
  20.0: 100000
}




