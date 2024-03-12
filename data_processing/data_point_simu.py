import random

def generate_data_file(central_value, len_data, filename, value_range=1.0):
    """
    Generate a file with 'len_data' values around 'central_value'.

    Parameters:
    - central_value: The central value around which the data is generated.
    - len_data: The number of data points to generate.
    - filename: Name of the file to save the data.
    - value_range: The range (+/-) within which to generate data around the central value.
    """
    with open(filename, 'w') as file:
        for _ in range(len_data):
            # Generate a random value around the central value within the specified range
            value = central_value + random.uniform(-value_range, value_range)
            # Write the value to the file, followed by a newline character
            file.write(f"{value}\n")

    print(f"Data file '{filename}' with {len_data} values around {central_value} has been created.")


generate_data_file(central_value=23.5, len_data=250, filename="data/ndsquare_data/75", value_range=0.2)
