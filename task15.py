import os
import matplotlib.pyplot as plt
import numpy as np

def plot_values_from_files(directory):
    x = []  # Filenames will be stored here
    y = []  # File contents (numerical values) will be stored here

    # Walk through the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r') as file:
                    value = float(file.read().strip()) 
                    filename = float(filename)
                    y.append(value)  
                    x.append(filename)  
            except ValueError:
                print(f"Could not convert the content of {filename} to a float.")
            except Exception as e:
                print(f"An error occurred while processing {filename}: {e}")

    y_err = [np.sqrt(y_) for y_ in y]
    print(y_err)

    print(x)
    print(y)
    
    plt.errorbar(x, y, yerr=y_err, fmt='o')
    plt.xlabel('distance(cm)')
    plt.ylabel('Counts')
    plt.title('preliminary measurement')
    plt.tight_layout()  
    plt.show()

# Example usage:
# plot_values_from_files('/path/to/your/directory')
plot_values_from_files('data/task15')