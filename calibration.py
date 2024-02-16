import pandas as pd
import matplotlib.pyplot as plt

def read_csv_data(csv_file, col_name=['t', 'voltage']):
  df = pd.read_csv(csv_file, header=None, names=col_name, skiprows=1)
  return df

def truncate_data(df, n):
  df_sub = df.head(n)
  return df_sub

def plot_data(df, title='plot', xlabel='Time (s)', ylabel='Voltage (V)'):
  plt.figure()
  plt.plot(df['t'], df['voltage'], marker='o', linestyle='-')  # Adjust marker and line styles as needed
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.show()


csv_file_path = 'data/waveform_sr/PULSEF03.CSV'
df = read_csv_data(csv_file_path) 
plot_data(df, title='test', xlabel='Time (s)', ylabel='Voltage (V)')

