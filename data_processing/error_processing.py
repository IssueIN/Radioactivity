import os
import matplotlib.pyplot as plt
import numpy as np
import random

def fetch_values_error(directory):
  x = [] 
  y = []
  y_sum = []
  dt=[]
  data = {}

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
            y_sum.append(np.sum(values))
            dt.append(len(values))
            data[float(filename)] = values

      except ValueError as ve:
        print(f"Could not convert the content of {filename} to a float: {ve}")
      except Exception as e:
        print(f"An error occurred while processing {filename}: {e}")
  return x, y, y_sum, dt, data

def nd2(n, d, t=1):
    n = np.array(n)
    d = np.array(d)
    return n / t * d**2

def nd2_err(d, n, dt=1):
    n = np.array(n)
    d = np.array(d)
    dt = np.array(dt)
    # error = (1/dt) * np.sqrt(d ** 4 * n  + (2 * n * d * 0.003) ** 2)
    error = (n/dt*d**2) * np.sqrt(1 / n + (2 * 0.003 / d)**2)
    #error = np.sqrt(d ** 4 * n  + (2 * n * d)**2 * (0.003) ** 2)
    return error

def len_modification(base, data):
  result_dict = {}
  for key in base:
      if key in data:
          list_length = base[key]
          # list_length = min(list_length, len(base[key]))
          # result_dict[key] = random.sample(data[key], list_length)
          result_dict[key] = random.choices(data[key], k=list_length)
      else:
          print(f"Key {key} not found in data_dict")
  return result_dict

err_norm = {
  0.6: 150,
  1.5: 150,
  2.0: 150,
  3.0: 150,
  4.0: 150,
  5.0: 120,
  6.0: 120,
  7.0: 120,
  8.0: 120,
  9.0: 120,
  10.0: 100,
  11.0: 100,
  12.0: 100,
  13.0: 100,
  14.0: 100,
  15.0: 80,
  16.0: 80,
  17.0: 80,
  18.0: 80,
  19.0: 80,
  20.0: 60,
  23.0: 60,
  26.0: 60,
  29.0: 60,
  35.0: 60,
  39.0: 60,
  45.0: 40,
  49.0: 40,
  55.0: 40,
  59.0: 40,
  65.0: 40,
  69.0: 40,
  75.0: 40,
  79.0: 30,
  85.0: 30,
  90.0: 30,
  95.0: 30
}

x_, n_, n_tot_, dt_, data = fetch_values_error('data/ndsquare_data/')

data_modified = len_modification(err_norm, data)

x = list(err_norm.keys())
dt = list(err_norm.values())
n_tot = [np.sum(data_modified[key]) for key in x]

x = (np.array(x)) / 100 
nd2_ = nd2(n_tot, x, dt)
nd2_err_ = nd2_err(x, n_tot, dt)

plt.errorbar(x, nd2_, yerr=nd2_err_, fmt='o', label ='raw data points', markersize=3, capsize=1.5)
plt.legend()
plt.xlabel('distance(m)')
plt.ylabel('nd2')
plt.title('ndsquare') 
plt.show()